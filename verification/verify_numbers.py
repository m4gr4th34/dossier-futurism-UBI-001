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

    # (#6) ceiling: at tau=2%, W/P=$100k (global mean) -> $2,000/yr; the prose must quote it.
    d_sus_100k = d_sustained(100_000)
    poison6 = 0
    if "$2,000" not in manuscript: poison6 += 10
    check("C13 ceiling: tau=2%, global-mean $100k/member -> $2,000/yr; quoted in the manuscript",
          d_sus_100k + poison6, 2000, 2000)

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
