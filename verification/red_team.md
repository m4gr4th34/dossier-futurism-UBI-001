# Red team — adversarial review (intake)

> **Findings are published with the dossier, RESOLVED or OPEN, per doctrine. An empty
> findings list is a red flag about the red team, not a compliment to the dossier.**

## Purpose

This is the intake file for the dossier's adversarial pass — **phase 5** of the
constitution's pipeline (published adversarial review). Referees attack the paper —
Part I (the survey), Part II (the Commonwealth Protocol blueprint), Part III (The
Limit), the flow-of-funds model, and the claim ledger — and every finding is recorded
here whether or not it is fixed. Nothing is hidden: a finding that survives review ships
as an OPEN caveat with the paper; a finding that is fixed ships as RESOLVED with the
commit that fixed it. The point is armor, not applause.

The load-bearing target is **C16** (the participation-constraint derivation, currently
`DERIV / OPEN`, entered precisely to be attacked here) — but nothing is out of scope.

## Intake format

Each finding is recorded with these fields:

- **ID** — `RT-nn` (sequential: RT-01, RT-02, …).
- **Referee** — the reviewer's role/lens (e.g. mechanism-design economist, crypto-security
  auditor, monetary historian, statistician, adversarial generalist).
- **Severity** — one of:
  - **BLOCKER** — falsifies a load-bearing claim or the central finding; must be resolved
    or the claim's label/wording changed before release.
  - **MAJOR** — a real defect in an argument, number, or design element that needs a fix or
    an explicit caveat, but does not sink the dossier.
  - **MINOR** — a weakness, imprecision, or presentation issue worth recording.
- **Target** — what is under attack: a claim id (e.g. `C16`), a section (e.g. Part III
  "The participation constraint"), a figure (e.g. `commonwealth-engine`), or a specific
  model line (e.g. `flow_model.py` `years_to_tier`).
- **Attack** — the objection stated in the referee's own words. Verbatim; not softened.
- **Disposition** — **empty at intake.** Later either:
  - **RESOLVED** — the fix, with the resolving commit hash; or
  - **OPEN** — the caveat as published in the dossier (the standing invitation, with named
    credit to the referee per the open-challenge doctrine).

## Findings

_(none yet — intake open. An empty list here is a statement about the review not having
run, not a claim that the dossier is unassailable.)_

| ID | Referee | Severity | Target | Attack | Disposition |
|---|---|---|---|---|---|
| — | — | — | — | _intake open_ | — |
