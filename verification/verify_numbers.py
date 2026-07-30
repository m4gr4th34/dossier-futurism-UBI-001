#!/usr/bin/env python3
"""
verify_numbers.py — Open Dossier survey-consistency verifier (template stub).

This is the Python mirror of the consistency console in index.html. A survey's
verification weight sits mostly in the citation audit (dossier.html); this
script runs the same cross-avenue CONSISTENCY checks the browser console runs,
so CI and the live page always agree.

INSTRUCTIONS FOR AUTHORS:
Keep the AVENUES list below in lockstep with the AVENUES array in index.html
(same name / status / forecast / signpost shape), then add your survey's real
cross-avenue and arithmetic checks alongside the built-in consistency checks.

The contract (unchanged):
  - computed value must fall within [claimed_lo, claimed_hi]
  - if it doesn't, this script exits nonzero — CI goes red — fix the PAPER
  - never widen the tolerance to make a failing check pass
  - label is the exact check as it reads on the page

Run locally:  python verification/verify_numbers.py
CI runs this: on every push (see .github/workflows/verify.yml)
"""

import json
import os
import sys

PASS, FAIL = "PASS", "FAIL"
results = []


def check(label, computed, claimed_lo, claimed_hi, fmt="{:.4g}"):
    ok = claimed_lo <= computed <= claimed_hi
    status = PASS if ok else FAIL
    results.append((status, label, computed, (claimed_lo, claimed_hi)))
    symbol = "✓" if ok else "✗"
    print(f"[{status}] {symbol} {label}")
    print(f"       computed={fmt.format(computed)}  "
          f"claimed=[{fmt.format(claimed_lo)}, {fmt.format(claimed_hi)}]")
    return ok


# ----------------------------------------------------------------
# AVENUES + CHECK RULES — single-sourced from the canonical avenues.json
# at the repo root, the SAME file index.html's console reads. The avenue
# DATA and the check RULES both live there, so neither can drift between
# the page and this verifier.
# ----------------------------------------------------------------
HERE = os.path.dirname(os.path.abspath(__file__))
AVENUES_PATH = os.path.join(HERE, os.pardir, "avenues.json")
# Optional: --avenues <path> overrides the data file (used by the back-catalog baker to
# verify a frozen chapter against its OWN sealed avenues.json). No flag => live-root default.
for i, a in enumerate(sys.argv):
    if a == "--avenues" and i + 1 < len(sys.argv):
        AVENUES_PATH = os.path.abspath(sys.argv[i + 1])
        break
with open(AVENUES_PATH, encoding="utf-8") as f:
    _data = json.load(f)
AVENUES = _data.get("avenues", [])
RULES = _data.get("checks", {})

# Pull the rules once. Defaults are deliberately strict so a malformed
# avenues.json fails loudly rather than silently skipping a check.
MIN_AVENUES        = RULES.get("min_avenues", 1)
SIGNPOST_REQUIRED  = RULES.get("forecast_signpost_required", True)
PCT_MIN            = RULES.get("forecast_pct_min", 0)
PCT_MAX            = RULES.get("forecast_pct_max", 100)

print("=" * 72)
print("SURVEY CONSISTENCY — same checks, same rules as the index.html console")
print("=" * 72)

forecasts     = [a for a in AVENUES if a.get("status") == "FORECAST"]
with_signpost = sum(1 for a in forecasts if a.get("signpost"))
out_of_range  = sum(1 for a in AVENUES
                    if a.get("forecast") is not None
                    and (a.get("forecast") < PCT_MIN or a.get("forecast") > PCT_MAX))

# (1) At least one avenue in the landscape.
check("Consistency: at least one avenue in the landscape", len(AVENUES), MIN_AVENUES, 9999)
# (2) Mandatory-signpost rule: every FORECAST carries a dated signpost
#     (only enforced when the rule is on; expected count flips with the rule).
_expected_signposted = len(forecasts) if SIGNPOST_REQUIRED else with_signpost
check("Consistency: every FORECAST has a dated signpost", with_signpost, _expected_signposted, _expected_signposted)
# (3) All forecast probabilities lie in [PCT_MIN, PCT_MAX].
check(f"Consistency: all forecast probabilities lie in [{PCT_MIN},{PCT_MAX}]", out_of_range, 0, 0)

# ----------------------------------------------------------------
# FLOW-OF-FUNDS CHECKS (#4-#6) — the executable verifier for claim C13.
# The model lives in verification/flow_model.py, which writes commonwealth_model.json;
# these checks RE-DERIVE the headline numbers from raw inputs and assert the JSON
# (and the manuscript that quotes it) agree. Fix the model or the paper, never the
# tolerance — the point checks are exact equalities.
#
# --avenues contract: resolve the model JSON and the manuscript RELATIVE to the
# avenues directory, so a frozen chapter verified against its OWN sealed avenues.json
# uses its OWN sealed model/manuscript, never the live root's. Falls back to the
# working-draft locations. If no model JSON is found (a chapter that never sealed one),
# the flow checks are skipped with a note — the 3 consistency checks still run.
# ----------------------------------------------------------------
AVENUES_DIR = os.path.dirname(AVENUES_PATH)
_model_candidates = [
    os.path.join(AVENUES_DIR, "verification", "commonwealth_model.json"),
    os.path.join(AVENUES_DIR, "commonwealth_model.json"),
    os.path.join(HERE, "commonwealth_model.json"),
]
MODEL_PATH = next((p for p in _model_candidates if os.path.exists(p)), None)
_src_candidates = [
    os.path.join(AVENUES_DIR, "editions", "index.source.html"),
    os.path.join(HERE, os.pardir, "editions", "index.source.html"),
]
SRC_PATH = next((p for p in _src_candidates if os.path.exists(p)), None)

if MODEL_PATH is None:
    print("\n[note] no commonwealth_model.json found — skipping flow-of-funds checks #4-#6.")
else:
    with open(MODEL_PATH, encoding="utf-8") as f:
        M = json.load(f)
    cst = M["constants"]
    rho, tau_eval = cst["rho"], cst["tau_eval"]
    manuscript = ""
    if SRC_PATH:
        with open(SRC_PATH, encoding="utf-8") as f:
            manuscript = f.read()

    def d_sustained(w):  # full levy flow per member (perpetual ceiling; rho=0 limit)
        return round(tau_eval * w, 6)

    def d_firstyear(w):  # year-one payout, before the treasury compounds
        return round((1.0 - rho) * tau_eval * w, 6)

    EPS = 1e-6  # float-equality hygiene, NOT a claim tolerance (values are exact integers)

    # (#4) conservation: every scenario's stored outputs must recompute from raw inputs,
    #      and the absolute-budget rows must satisfy dividend_budget/P == d_firstyear.
    mismatches = 0
    for s in M["scenarios"]:
        w = s["w_per_p"]
        if abs(d_sustained(w) - s["d_sustained"]) > EPS: mismatches += 1
        if abs(d_firstyear(w) - s["d_firstyear"]) > EPS: mismatches += 1
        if s.get("W") and s.get("P"):
            budget_fy = (1.0 - rho) * tau_eval * s["W"]   # T(0)=0, so budget is the levy payout
            if abs(budget_fy / s["P"] - s["d_firstyear"]) > EPS: mismatches += 1
    check("C13 conservation: model outputs recompute exactly from raw inputs (0 mismatches)",
          mismatches, 0, 0)

    # (#5) scaling spot-check: at tau=2%, W/P=$50k -> $1,000/yr full levy (tau*W/P) and
    #      $800/yr first-year net ((1-rho)*tau*W/P); the prose must quote BOTH.
    d_sus_50k, d_fy_50k = d_sustained(50_000), d_firstyear(50_000)
    poison5 = 0
    if abs(d_fy_50k - 800) > EPS: poison5 += 1
    if abs(d_sus_50k - 1000) > EPS: poison5 += 1
    if "$1,000" not in manuscript: poison5 += 10
    if "$800" not in manuscript: poison5 += 10
    check("C13 scaling: tau=2%, $50k wrapped/member -> $1,000/yr levy and $800 first-year net; both quoted in the manuscript",
          d_sus_50k + poison5, 1000, 1000)

    # (#6) ceiling: the global-mean scenario (UBS 2024, ~$95,384/member) yields ~$1,908/yr at
    #      tau=2% — just UNDER the $2,000 floor tier (the old $100k round sat exactly on it; the
    #      audit's item-9 fix moved it below). Recompute from the model's mean row; the prose must
    #      quote the corrected figure and say it is just under the floor.
    mean_row = next((s for s in M["scenarios"] if "mean" in s["name"].lower()), None)
    mean_w = mean_row["w_per_p"] if mean_row else 95384
    d_mean = round(tau_eval * mean_w)                       # 1908
    poison6 = 0
    if mean_row is None or abs(mean_row["d_sustained"] - tau_eval * mean_w) > EPS: poison6 += 1
    if d_mean >= 2000: poison6 += 1                         # must be UNDER the floor tier
    if "$1,908" not in manuscript: poison6 += 10
    if "just under the floor" not in manuscript: poison6 += 10
    check("C13 ceiling: tau=2%, global-mean $95,384/member (UBS 2024) -> ~$1,908/yr, just under the $2,000 floor tier; quoted in the manuscript",
          d_mean + poison6, 1908, 1908)

    # (#7) Part III (C16/C18): re-derive the participation-constraint numbers and one time-to-tier
    #      value, and assert the prose quotes them. W* = d_ref/tau = $50,000; a $1M holder pays
    #      $20,000/yr against a ~$1,000 dividend (b_required -> tau); floor time-to-tier at g=10% ~48 yrs.
    P = M.get("participation")
    TT = (M.get("time_to_tier") or {}).get("rows", [])
    if P:
        w_star_re = round(P["d_ref"] / P["tau"], 6)             # 50,000
        levy_1m = next((e["levy_paid"] for e in P["examples"] if e["w_i"] == 1_000_000), None)  # 20,000
        floor_g10 = next((r.get("floor") for r in TT if abs(r["g"] - 0.10) < 1e-9), None)        # 48.3
        poison7 = 0
        if abs(w_star_re - P["w_star"]) > EPS: poison7 += 1
        if levy_1m is None or abs(levy_1m - 20_000) > EPS: poison7 += 1
        if floor_g10 is None or floor_g10 <= 0: poison7 += 1
        if "$50,000" not in manuscript: poison7 += 10
        if "$20,000" not in manuscript: poison7 += 10
        if "48 years" not in manuscript: poison7 += 10   # the g=10% floor time-to-tier, quoted in Part III
        check("C16/C18 Part III: W*=$50,000 (d/tau), $1M holder pays $20,000 vs a ~$1,000 dividend, floor time-to-tier ~48 years at g=10%; all quoted in the manuscript",
              P["w_star"] + poison7, 50_000, 50_000)

    # (#8) Part-country decomposition (C19): re-derive the US mean/median dividends from the model's
    #      cited UBS figures, assert the tiers (US mean is the ONLY scenario clearing the living-wage
    #      tier; US median is poverty-relevant), and require the prose to quote the rounded forms.
    by_name = {s["name"]: s for s in M["scenarios"]}
    us_mean = by_name.get("US mean wealth (UBS 2025)")
    us_med = by_name.get("US median wealth (UBS 2025)")
    poison8 = 0
    if us_mean is None or us_med is None:
        poison8 += 100
    else:
        if abs(tau_eval * us_mean["w_per_p"] - us_mean["d_sustained"]) > EPS: poison8 += 1
        if abs(tau_eval * us_med["w_per_p"] - us_med["d_sustained"]) > EPS: poison8 += 1
        if us_mean["tier"] != "living-wage": poison8 += 1
        if us_med["tier"] != "poverty-relevant": poison8 += 1
        if sum(1 for s in M["scenarios"] if s["tier"] == "living-wage") != 1: poison8 += 1
    if "$13,900" not in manuscript: poison8 += 10   # US mean, rounded form used consistently in prose
    if "$1,380" not in manuscript: poison8 += 10    # US median
    d_us_mean = round(tau_eval * us_mean["w_per_p"]) if us_mean else -1   # 13926
    check("C19 US decomposition: tau=2%, US mean $696,277/adult (UBS 2026) -> ~$13,900/yr (clears the living-wage tier, the only scenario that does), US median $68,998 -> ~$1,380/yr (poverty-relevant); quoted in the manuscript",
          d_us_mean + poison8, 13926, 13926)

# ----------------------------------------------------------------
print()
n_fail = sum(1 for r in results if r[0] == FAIL)
n_pass = sum(1 for r in results if r[0] == PASS)
print("=" * 72)
print(f"TOTAL: {len(results)} checks · {n_pass} pass · {n_fail} fail")
if n_fail:
    print("FAILURES FOUND — fix the paper, not the tolerances.")
else:
    print("All checks pass — the survey is internally consistent.")
print("=" * 72)
sys.exit(1 if n_fail else 0)
