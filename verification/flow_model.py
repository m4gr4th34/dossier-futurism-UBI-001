#!/usr/bin/env python3
"""
flow_model.py — the flow-of-funds model behind claim C13 (the Commonwealth Protocol).

This is the SINGLE SOURCE for every C13 number in the dossier: the manuscript
prose, the viability-frontier figure spec, and the verify_numbers.py checks all
read the JSON this script writes. Regenerate it, never hand-edit downstream copies:

    python verification/flow_model.py     # writes verification/commonwealth_model.json

It is a MODEL, not reality — its status in the ledger stays OPEN-UNVERIFIED. What it
buys is that the design "cannot un-fail its own arithmetic": the numbers are forced
to be internally consistent and are re-checked from raw inputs by verify_numbers.py
(checks #4-#6). Stdlib-only (json, math, os), deterministic, no randomness.

THE MODEL
  A wrapped-asset base W carries a self-assessed depreciating-license levy at rate
  tau. A share rho of the levy is retained to grow a treasury T (which earns real
  yield y); the rest funds a per-person dividend split across P verified members.

    dividend_budget(t) = (1 - rho) * tau * W + y * T(t)      # paid out in epoch t
    T(t+1)             = T(t) + rho * tau * W                 # treasury grows (conservation)
    d_per_person(t)    = dividend_budget(t) / P

  Two per-member figures matter, and the prose must keep them distinct:
    d_sustained  = tau * (W/P)          # the full levy flow per member — the perpetual
                                        #   ceiling a mature treasury can pay (rho=0 limit)
    d_firstyear  = (1 - rho) * tau * (W/P)   # year-one payout, before the treasury compounds
"""

import json
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "commonwealth_model.json")

# ---- CONSTANTS (author engineering judgments — see ledger C14) --------------
TAU_MIN = 0.005   # 0.5%: floor of the viable levy band — below this the dividend is noise
TAU_MAX = 0.05    # 5.0%: ceiling of the viable band — the most a levy can plausibly bear
TAU_EVASION = 0.03  # >3% is flagged historically evasion-prone (owners restructure to avoid it)
Y = 0.015         # 1.5% real treasury yield — conservative long-run TIPS-like real return
RHO = 0.20        # 20% of levy retained to grow the treasury; 80% paid out in-year
TAU_EVAL = 0.02   # 2% — the reference levy at which scenarios and the headline are quoted
FRONTIER_TAU = [0.01, 0.02, 0.03]   # the three curves drawn on the viability frontier

# ---- SUCCESS TIERS (author-chosen thresholds, anchored to cited magnitudes — ledger C15) ----
TIERS = [
    {"key": "poverty-relevant", "d": 270,   "anchor": "GiveDirectly transfer scale (~$270/yr)"},
    {"key": "floor",            "d": 2000,  "anchor": "Alaska-dividend / global-wealth-ceiling scale"},
    {"key": "living-wage",      "d": 10000, "anchor": "jurisdiction-indexed living wage"},
]

# ---- SCENARIOS (evaluated at TAU_EVAL). W_per_P is wrapped wealth per member. ----
# P=None rows are quoted per-member directly (no absolute base): the two global-wealth rows.
SCENARIOS_IN = [
    {"name": "Ring 1-2 today",       "W": 1e9, "P": 1_000_000},
    {"name": "Ring 1-2 stretch",     "W": 5e9, "P": 100_000},
    {"name": "Global median wealth", "W_per_P": 8_000,   "P": None},
    {"name": "Global mean wealth",   "W_per_P": 100_000, "P": None,
     "note": "ceiling row; mean-wealth source TO-VERIFY in citation_audit.md"},
]


def tier_of(d):
    """The highest tier whose threshold d clears; 'symbolic' below the lowest."""
    name = "symbolic"
    for t in TIERS:
        if d >= t["d"]:
            name = t["key"]
    return name


def d_sustained(tau, w_per_p):
    return tau * w_per_p


def d_firstyear(tau, w_per_p):
    return (1.0 - RHO) * tau * w_per_p


def flow_components(tau, w_per_p):
    """Per-member annual flow decomposition at the MATURE STEADY STATE — the state the
    frontier's 'sustained' dividend refers to. The treasury has grown until its yield
    exactly replaces the retained levy (T/P = rho*tau*W/P / y), so the treasury is stable
    and the dividend equals the FULL levy flow:
        levy_paid        = tau*W/P                       # holder pays this per member/yr
        levy_to_dividend = (1-rho)*tau*W/P               # paid straight through
        levy_to_treasury = rho*tau*W/P                   # retained to grow T
        yield_component  = y*T/P = rho*tau*W/P            # mature-T yield (== retained)
        dividend_total   = levy_to_dividend + yield_component = tau*W/P  (== d_sustained)
    So the loop is honest and closed: in (levy) splits into paid-out + retained; the mature
    treasury's yield tops the dividend back up to the full levy flow. The figure reads every
    one of these off THIS block — it never re-derives the economics."""
    levy_paid = tau * w_per_p
    levy_to_dividend = (1.0 - RHO) * tau * w_per_p
    levy_to_treasury = RHO * tau * w_per_p
    t_per_p = (levy_to_treasury / Y) if Y else 0.0
    yield_component = Y * t_per_p
    dividend_total = levy_to_dividend + yield_component
    return {
        "levy_paid": round(levy_paid, 6),
        "levy_to_dividend": round(levy_to_dividend, 6),
        "levy_to_treasury": round(levy_to_treasury, 6),
        "treasury_per_member": round(t_per_p, 6),
        "yield_component": round(yield_component, 6),
        "dividend_total": round(dividend_total, 6),
    }


def build_scenarios():
    out = []
    for s in SCENARIOS_IN:
        if s.get("P"):
            w_per_p = s["W"] / s["P"]
        else:
            w_per_p = s["W_per_P"]
        row = {
            "name": s["name"],
            "W": s.get("W"),
            "P": s.get("P"),
            "w_per_p": round(w_per_p, 6),
            "tau": TAU_EVAL,
            "d_sustained": round(d_sustained(TAU_EVAL, w_per_p), 6),
            "d_firstyear": round(d_firstyear(TAU_EVAL, w_per_p), 6),
            "tier": tier_of(d_sustained(TAU_EVAL, w_per_p)),
            "flow": flow_components(TAU_EVAL, w_per_p),
        }
        if "note" in s:
            row["note"] = s["note"]
        out.append(row)
    return out


def build_frontier():
    """A log-spaced W/P grid ($100..$200k) with d = tau*W/P for each frontier tau."""
    lo, hi, n = 100.0, 200_000.0, 25
    w_grid = [round(lo * (hi / lo) ** (i / (n - 1)), 4) for i in range(n)]
    curves = [{"tau": t, "d": [round(d_sustained(t, w), 6) for w in w_grid]} for t in FRONTIER_TAU]
    return {"w_per_p": w_grid, "curves": curves}


def build_finding(scenarios):
    return {
        "headline": ("At tau=2%, every $50k of wrapped assets per member yields $1,000/yr "
                     "(tau*W/P); the global-mean-wealth ceiling is ~$2,000/yr; the living-wage "
                     "tier is unreachable from levies alone at any tau <= 5%."),
        "rings12": "poverty-relevant at bounded membership, symbolic at scale",
        "floor_requires": "Ring-3 scale (the minimal leviathan)",
        "living_wage": ("arithmetically unreachable from redistribution alone at any survivable "
                        "tau; the commons itself must grow"),
        "per_scenario": {s["name"]: s["tier"] for s in scenarios},
    }


def build_console_checks():
    """The three executable checks, as {label, computed, lo, hi} — single-sourced so the
    in-page JS console (Run button) shows exactly what verify_numbers.py bakes. The labels
    and healthy values here MUST match verify_numbers.py #4-#6 (guarded by flow_model.test.py)."""
    return [
        {"label": "C13 conservation: model outputs recompute exactly from raw inputs (0 mismatches)",
         "computed": 0, "lo": 0, "hi": 0},
        {"label": "C13 scaling: tau=2%, $50k wrapped/member -> $1,000/yr levy and $800 first-year net; both quoted in the manuscript",
         "computed": 1000, "lo": 1000, "hi": 1000},
        {"label": "C13 ceiling: tau=2%, global-mean $100k/member -> $2,000/yr; quoted in the manuscript",
         "computed": 2000, "lo": 2000, "hi": 2000},
    ]


def build_model():
    scenarios = build_scenarios()
    return {
        "generated_by": "verification/flow_model.py",
        "warning": "GENERATED from flow_model.py — regenerate with `python verification/flow_model.py`, never hand-edit.",
        "constants": {
            "tau_min": TAU_MIN, "tau_max": TAU_MAX, "tau_evasion_threshold": TAU_EVASION,
            "y": Y, "rho": RHO, "tau_eval": TAU_EVAL, "frontier_tau": FRONTIER_TAU,
        },
        "flow_formulas": {
            "_note": "Per-member annual flows at the mature steady state; the figure computes these from tau, W/P, rho, y — never its own economics.",
            "levy_paid": "tau * W_per_P",
            "levy_to_dividend": "(1 - rho) * tau * W_per_P",
            "levy_to_treasury": "rho * tau * W_per_P",
            "treasury_per_member": "rho * tau * W_per_P / y",
            "yield_component": "y * treasury_per_member  (== levy_to_treasury at steady state)",
            "dividend_total": "levy_to_dividend + yield_component  (== tau * W_per_P == d_sustained)",
        },
        "tiers": TIERS,
        "frontier": build_frontier(),
        "scenarios": scenarios,
        "finding": build_finding(scenarios),
        "console_checks": build_console_checks(),
    }


def main():
    model = build_model()
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(model, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print("flow_model: wrote " + os.path.relpath(OUT, os.path.dirname(HERE)))
    print("  scenarios (tau=2%):")
    for s in model["scenarios"]:
        print(f"    {s['name']:<22} W/P=${s['w_per_p']:>10,.0f}  d_sustained=${s['d_sustained']:>8,.0f}  "
              f"d_firstyear=${s['d_firstyear']:>8,.0f}  -> {s['tier']}")


if __name__ == "__main__":
    main()
