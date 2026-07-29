# Citation audit — Dossier Futurism-UBI-001

This is the verifier of record for every `CITE`-type claim in
[`../claim_ledger.csv`](../claim_ledger.csv). Per the format spec
([`research_pipeline.md`](research_pipeline.md)): *re-fetch and re-check every
CITE against the primary work, or triangulate through three or more independent
citing works; interested-party sources are graded REPORTED, not verified.*

**These items block the citation audit from closing; resolving them changes
ledger statuses from OPEN to their audited state.** Until each is resolved, the
source-backed claims it supports stay at status `OPEN` in the ledger (they become
`ESTABLISHED` only when the audit re-checks them, or are graded `REPORTED` where
the source is an interested party). Nothing here is asserted as verified.

## Status

Audit not yet run. Citations for the 2026-07-29 Part I survey are entered but
unverified: **0 verified · 0 flagged.** The CITE-backed rows awaiting this audit
are C01, C02, C03, C05, C11, C12.

## Open audit items

Each identifier below is currently unresolved in the Part I References. Resolving
it is the work that moves the associated ledger claim(s) from OPEN to their
audited state.

1. **Kenya UBI — NBER working-paper number `TO-VERIFY`.**
   Banerjee, A., Faye, M., Krueger, A., Niehaus, P., Suri, T. (2023),
   *Universal Basic Income: Short-Term Results from a Long-Term Experiment in
   Kenya.* The working-paper number and a resolvable identifier (NBER No. / DOI)
   must be fetched and the ~23,000-adult, three-arm design + "no work
   disincentive" finding checked against the paper.
   *Backs:* C05 (pilot labor-supply evidence).

2. **EIP-5320 — status `TO-VERIFY`.**
   Confirm the Ethereum Improvement Proposal's actual status (Draft / Stagnant /
   Final / Withdrawn) and that it specifies NFTs under continuous self-assessed
   (Harberger/COST) taxation, against the canonical EIPs repository.
   *Backs:* the on-chain-Harberger prior art cited under C09 / C10.

3. **Grassroots Economics / Sarafu — independent-literature cite `TO-VERIFY`.**
   The Sarafu demurrage-adjacent deployment is presently sourced to project
   documentation. Locate independent, peer-reviewed or otherwise evidentiary
   literature (e.g. the Sarafu network-analysis papers) and cite it, or grade the
   claim REPORTED where only project documentation exists.
   *Backs:* C12 (Sarafu as the principal living demurrage-adjacent deployment).

4. **RWA market figures — REPORTED, need triangulation.**
   The "~$32B tokenized RWA / ~$15B Treasuries / ~$0.2B real estate / 97%
   retail-inaccessible" figures come from an industry tracker (BeInCrypto,
   "Real State of Tokenization in 2026") and rwa.xyz. Either triangulate against
   two further independent trackers/primary filings, or grade the figures
   explicitly REPORTED (interested-party / industry-tracker provenance) at audit
   time. They must not be asserted as verified.
   *Backs:* the asset-precedent context under C09 / C10 (Part I §04).

5. **Duniter / Ğ1 — project-documentation claims, REPORTED where uncorroborated.**
   The Universal Dividend calibration (~10% annual growth, generational symmetry)
   and "since 2017 / longest-lived per-person dividend" claims rest on Duniter/Ğ1
   project sources and Laborde (2010), *Relative Theory of Money.* Corroborate the
   deployment-history and issuance-parameter claims independently, or grade the
   uncorroborated portions REPORTED.
   *Backs:* C02 (social-graph proof-of-personhood / longest-lived dividend).

## Closing the audit

When an item resolves, update the associated ledger row's status (OPEN →
ESTABLISHED, or OPEN → the REPORTED grade where the source is an interested
party), re-render, and record the resolution here with the date and the
resolvable identifier. The audit closes only when every item above is resolved.
