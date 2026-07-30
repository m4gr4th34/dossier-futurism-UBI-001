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

12. **Vicente, B.M. (2023), "Web3-enabled Harbergeorgism: A Policy Mechanism for Charter
    Cities" — Charter Cities Institute Research Paper, Jan 2023 — resolve the citation.**
    The strongest C10 near-miss. Confirm venue/date and the four distinguishing facts used
    in Part II: Harberger+Georgist levy on tokenized LAND funding a citizens' dividend, but
    partly issuance-funded, two-token, no personhood firewall, no chartalist anchor, no
    stability frontier.
    *Backs:* C10 (nearest-neighbor distinction).

13. **Rallo, J.R. (2020), "Georg Friedrich Knapp Was Not a 'Chartalist'" — History of
    Political Economy 52(4):773–793, DOI 10.1215/00182702-8604033 — verify.**
    The pay-community reading of Knapp that licenses Part II's element (iv), the chartalist
    demand anchor. Confirm DOI/pages and that the reading is represented faithfully.
    *Backs:* C10 / Part II "What is and is not new" (the load-bearing novelty).

14. **Bruenig, M. (2018), "Social Wealth Fund for America" — People's Policy Project — verify.**
    A yield-dividend per-person right, but statist, off-chain, and levy-free. Confirm the
    citation and the distinction (ours replaces state acquisition with the covenant levy).
    *Backs:* C10 (nearest-neighbor distinction).

15. **Manual check OPEN: cleisme.org (fringe French monnaie-libre variant).**
    Not yet read in full. A self-assessed levy on tokenized RWAs routed to a personhood-gated
    no-mint dividend there would trip the C10 KILL-trigger (below). Read and record.
    *Backs:* C10 (residual novelty risk).

16. **Manual check OPEN: Ğ1 / Duniter governance forums (French).**
    Proposals in the forums could contain an un-indexed design closer than the published
    corpus. Skim for the KILL-trigger and record.
    *Backs:* C10 (residual novelty risk).

## C10 novelty search trail (2026-07-29)

Deep prior-art search behind C10's TO-OUR-KNOWLEDGE label. VERDICT: **C10 survives as scoped.**

**Coverage.** Databases/venues: SSRN, NBER, arXiv, the RadicalxChange orbit, Ethereum
research forums, the charter-cities literature, and the French *monnaie-libre* corpus
(TRM / Duniter / Ğ1) **searched in French**. Two manual checks remain open (items 15–16).

**KILL-trigger benchmark.** Any single work, even low-quality, that imposes a self-assessed
levy on tokenized real-world assets, routes the proceeds to a personhood-gated no-mint
dividend, payable in that same token → **C10 downgrades to elements (iii)+(iv) only.** None
found; the two open manual checks are the only places one could still surface.

**Near-miss catalogue (full citations).**
- **Vicente, B.M. (2023).** Web3-enabled Harbergeorgism: A Policy Mechanism for Charter Cities.
  Charter Cities Institute Research Paper (Jan 2023). *Strongest near-miss:* Harberger+Georgist
  levy on tokenized LAND funding a citizens' dividend — but partly issuance-funded, two-token,
  no personhood firewall, no chartalist anchor, no stability frontier.
- **Posner, E.A. & Weyl, E.G. (2017).** Property Is Only Another Name for Monopoly. Journal of
  Legal Analysis 9(1):51–123, DOI 10.1093/jla/lax001; and *Radical Markets* (2018). COST social
  dividend — off-chain, national, no chartalist anchor, no RWA wrapper.
- **de la Rouviere (2018); Riady (2018).** One-sentence gestures at Harberger-revenue-as-UBI; no
  mechanism design.
- **Geo Web SALSA.** Deployed self-assessed licensing on DIGITAL land; no dividend.
- **1Hive / Duncan, "Harberger Taxation and Open Source."** Software-license levy funding a
  "digital commonwealth" with per-person governance shares — nearest on naming and per-person
  distribution; not an RWA levy, not a yield dividend.
- **Circles; Ğ1 / Relative Theory of Money; Encointer; GoodDollar.** Personhood dividends, ALL
  minting-funded — they *invert* our zero-issuance invariant.
- **Bruenig, M. (2018).** Social Wealth Fund for America. People's Policy Project. Dividend-from-
  yield per-person right; statist, off-chain, levy-free.
- **Rallo, J.R. (2020).** Georg Friedrich Knapp Was Not a "Chartalist." HOPE 52(4):773–793, DOI
  10.1215/00182702-8604033. The pay-community reading of Knapp — the theoretical seed of our
  element (iii)/(iv), never coupled to a levy or a dividend.
- **French corpus (TRM/Duniter/monnaie-libre, searched in French).** Currency-issuance only; no
  extension to non-currency assets.

17. **Olson, M. (1965), The Logic of Collective Action — Harvard University Press — verify.**
    Confirm the citation and that the concentrated-costs / diffuse-benefits mechanism is
    represented faithfully as the ideology-free basis for Part III's non-adoption argument.
    *Backs:* C17 (Part III political-limit argument).

18. **Community land trust model — Davis, J.E. (ed.) The Community Land Trust Reader — card `TO-VERIFY`.**
    Resolve the exact citation and confirm the Champlain Housing Trust scale/duration claim
    (thousands of homes over decades under ordinary contract law) used for Part III route 3a.
    *Backs:* C18 (no-state acquisition route).

19. **Optimism Collective sequencer-revenue / RetroPGF — REPORTED, `TO-VERIFY`.**
    Confirm that sequencer revenue funds public goods at scale via retrospective funding, and
    grade REPORTED (project/governance docs, not an independent evidentiary source). It is a
    precedent for the REVENUE half of route R only, not for a dividend.
    *Backs:* C18 (protocol-revenue endowment route).

20. **Novelty re-check (extends the C10 trail): does any published work point a protocol-revenue
    endowment at a personhood-gated, no-mint dividend?**
    Part III route R is the most buildable and therefore the most likely to have a near-miss.
    Run a quick targeted search at audit time (Optimism/RetroPGF + UBI/dividend + proof-of-personhood).
    A hit routing protocol revenue to a personhood-gated no-mint dividend would extend the C10
    near-miss catalogue (and, if it also carried an RWA levy, trip the C10 KILL-trigger).
    *Backs:* C10 / C18 (residual novelty risk on route R).

## Closing the audit

When an item resolves, update the associated ledger row's status (OPEN →
ESTABLISHED, or OPEN → the REPORTED grade where the source is an interested
party), re-render, and record the resolution here with the date and the
resolvable identifier. The audit closes only when every item above is resolved.
