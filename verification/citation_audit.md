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

## Status — CLOSED (except one escalation), 2026-07-29

Audit run 2026-07-29 (web verification; paywalled sources verified by identity via
their landing/abstract pages, full text not accessed where noted). Governing rule
applied throughout: **verify or downgrade, never quietly keep.**

**Tally: 20 of 20 items + C19's two sources (items 21–22) resolved · 1 residual (item 16, forum anti-bot wall) · 1 REPORTED-context TO-VERIFY (item 22).**
Ledger moves: **C01, C02, C05, C11, C12 → ESTABLISHED**; **C03 → REPORTED** (its only
source is the interested-party Kleros post-mortem); **C12** rose from pending-REPORTED
to ESTABLISHED on independent peer-reviewed literature. Item 9 was resolved (b): the model's
global-wealth constants moved to cited UBS figures, which flipped the mean scenario
floor → poverty-relevant (see the sensitivity note in the item-9 row). C04, C06–C09, C13–C18
are not citation-gated and are unchanged.

### Disposition table

| Item | Source | Disposition |
|---|---|---|
| 1 | Kenya UBI RCT (Banerjee et al. 2023) | VERIFIED (content); **DOWNGRADED**: no NBER number exists — cited as a 2023 working paper. Backs C05 → ESTABLISHED. |
| 2 | EIP-5320 | VERIFIED (scope); **DOWNGRADED**: draft PR closed unmerged 2022-12-25, never a canonical standard — card/prose say "proposal," not "standard." |
| 3 | Sarafu / Grassroots Economics | **VERIFIED (independent)**: Mattsson et al., Scientific Reports 13:6541 (2023). C12 → ESTABLISHED (was pending-REPORTED). |
| 4 | RWA market figures | VERIFIED within tracker spread (rwa.xyz ~$33.5B; Treasuries ~$13–16B). Stays REPORTED. |
| 5 | Duniter/Ğ1 | VERIFIED (independent, Siddarth 2020 / Gensollen 2020) for RTM/UD/scale; ~10%/yr calibration stays REPORTED. Backs C02 → ESTABLISHED. |
| 6 | Knapp, State Theory of Money | VERIFIED; **corrected**: the "pay-community beyond the state" reading is Rallo's, not Knapp's own. |
| 7 | Weyl & Zhang, Depreciating Licenses | VERIFIED; added published AEJ: Economic Policy 14(3) 2022, DOI 10.1257/pol.20200426. |
| 8 | Blockchain land-admin review | VERIFIED (Owusu Ansah et al., Land Use Policy 125, 2023, DOI 10.1016/j.landusepol.2022.106473); Georgia confirmed by review, Honduras/Sweden per broader record (full text not accessed). |
| 9 | Global mean/median wealth | **RESOLVED-(b)** — model updated to cited UBS figures: mean **$95,384**/adult (2024, GWR 2025), median **$8,654**/adult (end-2022; vintage mismatch stated, no single-vintage 2024 median confirmable). **Sensitivity (armor):** the old $100k round sat *exactly* on the $2,000 floor boundary; the precise $95,384 → ~$1,908/yr moves the mean scenario to just-under-floor (floor → poverty-relevant). The $2,000 floor THRESHOLD is unchanged (author-chosen, C15). |
| 10 | GiveDirectly $270/yr anchor | VERIFIED: $0.75/day = $22.50/mo = ~$270/yr per adult. C15 anchor confirmed. |
| 11 | Alaska PFD magnitude | VERIFIED (state source); **DOWNGRADED**: "~$2,000/person recently" overstated → ~$1,000–$1,700 typical (one-off $3,284 in 2022). Prose + C15 anchor corrected. |
| 12 | Vicente 2023 | VERIFIED (Bernardo M. Vicente, CCI Jan 2023); **tightened**: dividend is conditional/surplus-funded, issuance attaches to the staking coin not the dividend. |
| 13 | Rallo 2020 | VERIFIED (HOPE 52(4):773–793, DOI 10.1215/00182702-8604033). |
| 14 | Bruenig 2018 | VERIFIED (American Solidarity Fund; non-transferable per-person shares). |
| 15 | cleisme.org | CHECKED — **negative**: funds services by minting (3 DUs per DU), no asset levy, no Harberger, no asset-funded personhood dividend. Supports C10. |
| 16 | Ğ1/Duniter forums (French) | **RESIDUAL**: internal search blocked by anti-bot wall; external indexes negative. A logged-in manual pass is still owed. No kill-trigger found. |
| 17 | Olson 1965 | VERIFIED (Harvard UP; group-size / free-rider thesis). |
| 18 | CLT / Champlain Housing Trust | VERIFIED (Davis ed., Lincoln Institute 2010); scale "thousands of homes over decades" accurate in magnitude, unit counts self-reported (REPORTED). |
| 19 | Optimism Collective | VERIFIED (REPORTED; sequencer revenue → public goods via RetroPGF, ~60M+ OP / $100M+ across rounds); funds public goods, not a dividend. |
| 20 | Route-R novelty re-check | **negative** — no protocol-revenue → personhood-gated → no-mint dividend found. C10 stands. |
| + | C01 Worldcoin bans | VERIFIED (Kenya 2023, Spain/Portugal 2024, Brazil 2025); "tens of millions" softened to ~ten-million-plus verified. C01 → ESTABLISHED. |
| + | C03 Proof of Humanity | **DOWNGRADED → REPORTED**: only source is the interested-party Kleros post-mortem. |
| + | C11 French 1958 ordinance | **DOWNGRADED — CLAIM REMOVED**: unverifiable (1958 France = nouveau-franc redenomination, not a currency ban); replaced with the documented Wörgl 1933 central-bank suppression. Wörgl + Freicoin verified → C11 ESTABLISHED. |
| 21 | UBS Global Wealth Report 2026 (US mean/median) | **VERIFIED** (2026-07-29): US mean wealth/adult **$696,277**, median **$68,998** (2025 data, 17th edn.; single-vintage pair). Confirmed via IndexBox + Yahoo/Newsweek coverage. **Edition discrepancy noted:** the GWR 2025 edition (2024 data) reported a much higher US median ~$124,041 — a real drop between editions ("typical Americans' wealth fell 2020–2025"). Backs C19. |
| 22 | US household net worth aggregate (Fed Z.1) | **REPORTED context, TO-VERIFY**: ~$160T US household net worth; a 2% levy ≈ ~$3.2T/yr ≈ ~11% of GDP. Federal Reserve Financial Accounts (Z.1) scale; exact figures to be pinned. Prose-only sanity check — NOT a model output, kept out of the frontier math. |

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
(TRM / Duniter / Ğ1) **searched in French**.

**Manual/targeted checks completed 2026-07-29 (items 15, 16, 20):**
- **Item 15 — cleisme.org:** read; a fringe French monnaie-libre movement that funds common
  services by *additional minting* (three extra Universal Dividends per member's UD), not by
  any levy. No extension to non-currency assets, no Harberger/self-assessed levy, no
  asset-funded personhood dividend. **Negative — supports C10.**
- **Item 16 — Ğ1/Duniter governance forums:** internal search **blocked by the forums'
  anti-bot wall**; external `site:` and French-keyword indexing surfaced nothing proposing
  Harberger/self-assessed levies or an extension to non-currency assets. **Negative on
  external indexes, but not exhaustive** — a logged-in in-forum pass is still owed. Recorded
  as a residual, not a closure.
- **Item 20 — route-R novelty re-check** (protocol-revenue endowment → personhood-gated →
  no-mint dividend): adjacent hits each miss a leg — Optimism RetroPGF funds projects not a
  per-person dividend; Worldcoin/PoH/GoodDollar/Circles are minting-funded; Uniswap/Unichain
  route L2 fees to burns. **No genuine hit. C10 stands.**

**KILL-trigger benchmark.** Any single work, even low-quality, that imposes a self-assessed
levy on tokenized real-world assets, routes the proceeds to a personhood-gated no-mint
dividend, payable in that same token → **C10 downgrades to elements (iii)+(iv) only.** None
found across the completed checks; the only residual surface is the anti-bot-blocked Ğ1
forum internal search (item 16).

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

**Closed 2026-07-29.** Item 9 was resolved (b): the model's global-wealth constants now use
cited UBS figures ($95,384 mean 2024 / $8,654 median 2022), flipping the mean scenario to
just-under-floor and correcting the knife-edge the round number had hidden. One residual
remains: **item 16** (the Ğ1 forum internal search was anti-bot blocked) — a logged-in manual
pass is owed, though nothing material surfaced externally.

Each resolved item moved its ledger row per the repo convention (OPEN → ESTABLISHED where a
real evidentiary source was confirmed; OPEN → REPORTED where the only source is an interested
party). Downgrades changed the manuscript wording so language matches status (EIP-5320 =
proposal not standard; Alaska ~$1,000–$1,700 not ~$2,000; the French-1958 claim removed and
replaced with Wörgl 1933; Worldcoin ~ten-million-plus not tens of millions; Vicente's dividend
conditional). Re-open any row by adding a dated item here and reverting its status.
