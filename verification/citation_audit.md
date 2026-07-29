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
are C01, C02, C03, C05, C11, C12. Part II (the Commonwealth Protocol conjecture,
added 2026-07-29) contributes three further sources — Knapp, Weyl–Zhang, and the
blockchain land-administration review — supporting the C13 design and its
ingredients; they are open items 6–8 below.

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

6. **Knapp, G.F. (1905/1924), The State Theory of Money — verify edition/pagination.**
   Confirm the standard English edition (Macmillan, 1924, tr. Lucas & Bonar) and
   that the chartalist claim used in Part II (a currency holds value because
   obligations are payable in it; a pay-community beyond the state can issue chartal
   money) is faithfully represented, not overstated.
   *Backs:* Part II Layer 3 / the chartalist demand loop (the C13 design premise).

7. **Weyl, E.G. & Zhang, A.L., Depreciating Licenses — confirm SSRN id + the stated limit.**
   DOI 10.2139/ssrn.3698941 (SSRN 3698941). Re-fetch and confirm the allocative-vs-
   investment-efficiency trade-off and, critically, the authors' explicit statement
   that self-assessment cannot incent universally truthful valuations — the caveat
   Part II leans on for Layer 2. Check whether a peer-reviewed version supersedes the
   working paper.
   *Backs:* Part II Layer 2 (the depreciating-license levy) and the valuation-gaming
   attack-surface item.

8. **Blockchain land-administration systematic review — DOI `TO-VERIFY`.**
   ScienceDirect article S0264837722005002 (Land Use Policy, 2022). Resolve the DOI
   and confirm the three cases as used in Part II Ring 3: Honduras stalled on
   political resistance, Sweden concluded its pilot without implementation, Georgia
   succeeded via political buy-in and modern records. Until resolved, cite as
   TO-VERIFY; do not assert the review as verified.
   *Backs:* Part II Ring 3 (the jurisdiction requirement / minimal-leviathan claim).

9. **Global mean / median wealth per adult — source + year + figures `TO-VERIFY`.**
   The flow-of-funds model (C13) uses ~$100,000 as global-mean wealth per adult (the
   ceiling scenario) and ~$8,000 as global-median (a scale scenario). Pin these to the
   UBS Global Wealth Report (formerly Credit Suisse) — exact year and figures — or grade
   the two global-wealth scenario points REPORTED. Until resolved they are model inputs,
   not asserted facts; the "Global mean wealth" scenario row already carries a
   TO-VERIFY note.
   *Backs:* C13 / C15 (the $2,000/yr floor-tier ceiling rests on the mean-wealth figure).

10. **GiveDirectly $270/yr transfer-scale anchor — cross-check.**
    The poverty-relevant tier ($270/yr, C15) is anchored to GiveDirectly's transfer
    magnitude. Cross-check the actual per-recipient annual transfer in the Kenya RCT
    (cf. Part I C05 / the Banerjee et al. NBER paper, open item 1) and confirm the
    anchor is in the right order of magnitude, or restate the anchor.
    *Backs:* C15 (poverty-relevant tier threshold).

11. **Alaska Permanent Fund recent-dividend magnitude — cross-check.**
    The floor tier ($2,000/yr, C15) is anchored partly to the Alaska dividend scale.
    Confirm the recent annual PFD amount (cf. Part I C05 / Jones & Marinescu, which cites
    ~$2,000/person recently) supports the anchor.
    *Backs:* C15 (floor tier threshold).

## Closing the audit

When an item resolves, update the associated ledger row's status (OPEN →
ESTABLISHED, or OPEN → the REPORTED grade where the source is an interested
party), re-render, and record the resolution here with the date and the
resolvable identifier. The audit closes only when every item above is resolved.
