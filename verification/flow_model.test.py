#!/usr/bin/env python3
"""
flow_model.test.py — lockstep guard for the C13 model / figure / manuscript single source.

Asserts that the commonwealth-engine figure's embedded data (constants, tiers, scenarios)
was GENERATED FROM commonwealth_model.json and never hand-drifted, and that the model JSON
is internally consistent (frontier and scenario dividends equal tau * W/P). Stdlib-only,
fail-loud (non-zero exit on any mismatch); discovered + run by run_tests.js.
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
MODEL = os.path.join(HERE, "commonwealth_model.json")
SRC = os.path.join(ROOT, "editions", "index.source.html")

fails = 0


def check(name, cond):
    global fails
    print(("  PASS  " if cond else "  FAIL  ") + name)
    if not cond:
        fails += 1


def approx(a, b, eps=1e-6):
    return abs(a - b) <= eps


def engine_spec(src):
    """Extract the commonwealth-engine figure's data-figure JSON from the source."""
    for m in re.finditer(r"data-figure='([^']*)'", src):
        raw = m.group(1)
        if '"type":"commonwealth-engine"' in raw or '"type": "commonwealth-engine"' in raw:
            return json.loads(raw)
    return None


def main():
    with open(MODEL, encoding="utf-8") as f:
        M = json.load(f)
    with open(SRC, encoding="utf-8") as f:
        src = f.read()
    spec = engine_spec(src)

    print("flow_model.test: lockstep — figure spec vs commonwealth_model.json")
    check("commonwealth-engine figure found in the source", spec is not None)
    if spec is None:
        print("\n1 FAILURE(S).")
        return 1

    # (1) constants lockstep — the figure embeds y, rho, tau_eval; they MUST equal the model's.
    mc = M["constants"]
    sc = spec.get("constants", {})
    for k in ("y", "rho", "tau_eval"):
        check("spec.constants." + k + " == model.constants." + k,
              k in sc and approx(sc[k], mc[k]))

    # (2) tiers lockstep — thresholds match the model, in order.
    m_tiers = [t["d"] for t in M["tiers"]]
    s_tiers = [t["d"] for t in spec.get("tiers", [])]
    check("spec tier thresholds == model tier thresholds", s_tiers == m_tiers)

    # (3) scenarios lockstep — each spec dot's (w, d) matches a model scenario, and d == tau_eval*w.
    tau_eval = mc["tau_eval"]
    m_by_w = {round(s["w_per_p"], 6): round(s["d_sustained"], 6) for s in M["scenarios"]}
    for s in spec.get("scenarios", []):
        w = round(s["w"], 6)
        check("scenario w=%g present in model" % w, w in m_by_w)
        if w in m_by_w:
            check("scenario w=%g: spec d==model d" % w, approx(s["d"], m_by_w[w]))
            check("scenario w=%g: d == tau_eval*w" % w, approx(s["d"], tau_eval * w))

    # (4) model internal consistency — frontier points are exactly tau*w.
    ok_frontier = True
    for cur in M["frontier"]["curves"]:
        tau = cur["tau"]
        for w, d in zip(M["frontier"]["w_per_p"], cur["d"]):
            if not approx(d, round(tau * w, 6)):
                ok_frontier = False
    check("model frontier: every d == tau*w", ok_frontier)

    # (5) flow decomposition (the mini-loop's numbers) closes EXACTLY, and its dividend equals
    #     the frontier value at that point — so the loop labels can never drift from the chart.
    ok_split = ok_div = ok_yield = True
    for s in M["scenarios"]:
        fl = s.get("flow", {})
        if not approx(fl.get("levy_to_dividend", 0) + fl.get("levy_to_treasury", 0), fl.get("levy_paid", -1)):
            ok_split = False
        if not approx(fl.get("yield_component", -1), fl.get("levy_to_treasury", 0)):
            ok_yield = False
        # dividend_total == frontier value at the scenario's point (== d_sustained), exact.
        if not (approx(fl.get("dividend_total", -1), s["d_sustained"])
                and approx(fl.get("dividend_total", -1), round(s["tau"] * s["w_per_p"], 6))):
            ok_div = False
    check("flow: levy_to_dividend + levy_to_treasury == levy_paid (every scenario)", ok_split)
    check("flow: yield_component == levy_to_treasury at steady state (every scenario)", ok_yield)
    check("flow: dividend_total == frontier value (d_sustained) at the point (every scenario)", ok_div)

    # (6) Part III participation constraint (C16): W* == d/tau exact; and b_required -> tau for
    #     concentrated wealth (>= 0.019 and within 0.001 of tau at W_i >= $1M) — the adverse-selection limit.
    P = M.get("participation", {})
    check("participation: W* == d_ref / tau (exact)", approx(P.get("w_star", -1), P.get("d_ref", 0) / P.get("tau", 1)))
    ok_limit = bool(P.get("examples"))
    for e in P.get("examples", []):
        if e["w_i"] >= 1_000_000:
            b = e["b_required"]
            if not (b >= 0.019 and (P["tau"] - b) <= 0.001 + 1e-9):
                ok_limit = False
    check("participation: b_required >= 0.019 and within 0.001 of tau for W_i >= $1M (b -> tau)", ok_limit)

    # (7) Part III time-to-tier (C18) monotonic in g: a higher growth rate reaches each tier sooner.
    TT = M.get("time_to_tier", {}).get("rows", [])
    ok_mono = len(TT) >= 2
    by_g = sorted(TT, key=lambda r: r["g"])
    for a, b in zip(by_g, by_g[1:]):
        for key in ("poverty-relevant", "floor"):
            if key in a and key in b and not (b[key] < a[key]):
                ok_mono = False
    check("time_to_tier: years strictly decrease as g increases (both tiers)", ok_mono)

    # (8) Part-country decomposition (C19): US mean/median scenarios recompute exactly and land in the
    #     asserted tiers — US mean is the ONLY scenario reaching the living-wage tier.
    by_name = {s["name"]: s for s in M["scenarios"]}
    us_mean = by_name.get("US mean wealth (UBS 2025)")
    us_med = by_name.get("US median wealth (UBS 2025)")
    tau = M["constants"]["tau_eval"]
    check("US mean scenario present, d == tau*W exact",
          bool(us_mean) and approx(us_mean["d_sustained"], round(tau * us_mean["w_per_p"], 6)))
    check("US mean tier == living-wage (the only scenario that clears it)",
          bool(us_mean) and us_mean["tier"] == "living-wage"
          and sum(1 for s in M["scenarios"] if s["tier"] == "living-wage") == 1)
    check("US median present, d == tau*W exact, tier == poverty-relevant",
          bool(us_med) and approx(us_med["d_sustained"], round(tau * us_med["w_per_p"], 6))
          and us_med["tier"] == "poverty-relevant")

    print("\n" + ("%d FAILURE(S)." % fails if fails else "all lockstep checks passed."))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
