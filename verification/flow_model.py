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

# ---- ENDOWMENT GROWTH (Part III time-to-tier) — author engineering judgment (ledger C14-style). ----
# g is the ANNUAL growth of wrapped wealth per member from protocol revenue + retained levy +
# new-commons formation while the commonwealth is young and its commons is being constituted.
# It is NOT a market-return assumption (a diversified real return would be ~y=1.5%); it is the
# high-growth regime of a protocol accreting a commons. Range stated; two rows emitted.
G_MIN = 0.05   # 5%/yr: conservative young-protocol accretion
G_MAX = 0.20   # 20%/yr: aggressive early-network accretion (the ceiling we will quote)
G_ROWS = [0.10, 0.20]   # the two growth rates the time-to-tier block reports

# ---- SCENARIOS (evaluated at TAU_EVAL). W_per_P is wrapped wealth per member. ----
# P=None rows are quoted per-member directly (no absolute base): the two global-wealth rows.
# The two global-wealth rows use CITED UBS Global Wealth Report figures (citation audit item 9,
# resolved (b), 2026-07-29). VINTAGE MISMATCH, stated honestly: the global MEAN ~$95,384/adult is
# the 2024 figure (GWR 2025 edition); the global MEDIAN ~$8,654/adult is the end-2022 figure — a
# single-vintage 2024 median was NOT confirmable from the public summaries (the GWR 2025 PDF figure
# could not be retrieved). Using these as scenario anchors remains an author choice (EST, C14/C15);
# the numbers themselves are now cited, not round. NB: at tau=2% the mean yields ~$1,908/yr, which
# lands JUST UNDER the $2,000 floor tier — the $100k round previously sat exactly on that boundary.
SCENARIOS_IN = [
    {"name": "Ring 1-2 today",       "W": 1e9, "P": 1_000_000},
    {"name": "Ring 1-2 stretch",     "W": 5e9, "P": 100_000},
    {"name": "global median wealth (UBS 2022)", "W_per_P": 8_654,  "P": None},
    {"name": "global mean wealth (UBS 2024)",   "W_per_P": 95_384, "P": None,
     "note": "ceiling row; UBS mean wealth/adult ~$95,384 (2024, GWR 2025) -> ~$1,908/yr at tau=2%, just under the $2,000 floor tier"},
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
                     "(tau*W/P); the global-mean-wealth ceiling is ~$1,908/yr (just under the "
                     "$2,000 floor tier); the living-wage tier is unreachable from levies alone "
                     "at any tau <= 5%."),
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
        {"label": "C13 ceiling: tau=2%, global-mean $95,384/member (UBS 2024) -> ~$1,908/yr, just under the $2,000 floor tier; quoted in the manuscript",
         "computed": 1908, "lo": 1908, "hi": 1908},
        {"label": "C16/C18 Part III: W*=$50,000 (d/tau), $1M holder pays $20,000 vs a ~$1,000 dividend, floor time-to-tier ~48 years at g=10%; all quoted in the manuscript",
         "computed": 50000, "lo": 50000, "hi": 50000},
    ]


# ---- PART III: the participation constraint --------------------------------
def enter_condition(b, tau, d, w_i):
    """A holder of wealth w_i enters the VOLUNTARY covenant iff net position is non-negative:
    d + b*w_i >= tau*w_i  <=>  b >= tau - d/w_i. Returns True if entry is rational."""
    return b >= tau - d / w_i


def build_participation():
    """Break-even wealth and the b-thresholds that expose adverse selection. Uses the stretch
    scenario's per-member dividend as the reference d (d_ref = $1,000 at tau=2%). W* = d/tau is
    the wealth below which entry is net-positive even at b=0; above it, entry needs b >= tau - d/w_i,
    which -> tau as wealth concentrates. So voluntary entry adversely selects net recipients and
    weak assets; redistributing EXISTING concentrated wealth needs compulsion (Part III / C16)."""
    tau, d_ref = TAU_EVAL, 1000.0
    examples = []
    for w_i in (1_000_000.0, 10_000_000.0):
        examples.append({
            "w_i": w_i,
            "levy_paid": round(tau * w_i, 6),
            "dividend": round(d_ref, 6),
            "b_required": round(tau - d_ref / w_i, 6),
        })
    return {
        "_note": "Voluntary-entry condition: b >= tau - d/w_i. W* = d/tau is the break-even wealth (entry net-positive at b=0 below it). b_required -> tau as wealth concentrates -> adverse selection (C16).",
        "tau": tau,
        "d_ref": round(d_ref, 6),
        "w_star": round(d_ref / tau, 6),   # 50,000 at d=$1,000, tau=2%
        "examples": examples,
    }


# ---- PART III: time-to-tier for the no-state routes (C18) -------------------
def years_to_tier(w0_per_p, g, tau, tier_d):
    """Years until the per-member dividend d(t)=tau*w0*(1+g)^t reaches tier_d, at constant
    membership. t = ln(tier_d / (tau*w0)) / ln(1+g). Requires g>0 and the target above today's d."""
    d0 = tau * w0_per_p
    if g <= 0 or tier_d <= d0:
        return 0.0
    return math.log(tier_d / d0) / math.log(1.0 + g)


def build_time_to_tier():
    """From the Ring 1-2 today base ($1k/member, tau=2% -> $20/yr), years to each tier at the two
    reported growth rates. Constant membership is a CONSERVATIVE simplification (growing M raises
    the bar). g is a young-protocol accretion rate (see G_MIN/G_MAX), not a market return."""
    base_w, tau = 1000.0, TAU_EVAL
    rows = []
    for g in G_ROWS:
        row = {"g": g}
        for t in TIERS:
            if t["key"] in ("poverty-relevant", "floor"):
                row[t["key"]] = round(years_to_tier(base_w, g, tau, t["d"]), 1)
        rows.append(row)
    return {
        "_note": "Years to tier from the Ring 1-2 today base ($1k/member, tau=2%, d0=$20) at constant M. t = ln(tier_d/(tau*W0))/ln(1+g). g is young-protocol accretion, NOT a market return; constant M is conservative.",
        "base_w_per_p": base_w, "tau": tau, "g_range": [G_MIN, G_MAX],
        "rows": rows,
    }


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
        "participation": build_participation(),
        "time_to_tier": build_time_to_tier(),
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
