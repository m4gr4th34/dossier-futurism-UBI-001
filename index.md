An Open Dossier · **Futurism-UBI-001**

# Universal Basic Income

*Irfan Ali-Khan — Independent Researcher*

This dossier asks whether a currency can enforce, by protocol rather than the accident of jurisdiction, both a thriving economy and a floor for a life worth living — and whether it can reach the wealth that escapes into stocks and property. It is a survey first: Part I maps what crypto-UBI projects and the UBI pilots have actually shown, what failed and why, labeled claim by claim; Part II above it proposes a candidate blueprint — the Commonwealth Protocol — labeled throughout as exploratory conjecture. The discipline is a clean split — deployed facts and pilot results cited and labeled, the central stability question and the asset mechanism held open and honest. **Don't trust this paper — run it.**

## THE PREMISE — stated openly as the author's

We are all human, born by lottery onto some coordinates of this rock. Which patch of geography, which institutions, which century — none of it chosen, all of it decisive. Where life is fair, it is mostly because a local leviathan happens, by luck and history, to enforce a measure of fairness; where it isn't, hope does the unpaid work. The rules that govern economic life have always been local, accidental, and enforced from above.

This dossier asks whether that has to remain true. Is there a set of economic rules — enforceable by protocol rather than by the accident of jurisdiction — that a plural consciousness could adopt: rules that encourage a thriving economy *and* guarantee a floor for a life worth living? Is there an overlap between the two, or is the trade-off fundamental? Can an economy with a basic income built into its money survive contact with reality — and can it reach the wealth that today escapes into stocks and property?

This document does not assume the answer is yes. It maps what has been tried, states plainly what failed and why, and then constructs the most rigorous candidate design the evidence permits — with the failure conditions named, so the answer can be *no*.

*(This premise is a normative stance, not a claim; it appears in no ledger row. Every factual statement below carries a label, and every label is true.)*

## PART II — THE CANDIDATE: the Commonwealth Protocol

**DESIGN CONJECTURE — nothing below is asserted to work. One falsifiable core; attack surface enumerated. Working name only.**

This part composes the survivors of Part I into a single design. The organizing rule comes from history: voluntary levy systems survive when the obligation attaches to a benefit at one irrevocable entry point and is enforced by the asset itself thereafter — condominium covenants, Hanseatic dues — and they die when payment is a recurring choice: Freicoin's decaying token lost to non-decaying rivals, and the Articles of Confederation's unenforced requisitions killed the confederation in a decade. Part I's graveyard is this same failure six times over: distribution without demand.

*(figure: The Commonwealth Protocol viability frontier: dividend per member versus wrapped wealth per member, with three success tiers and four scenarios — The whole proposal in one figure: the engine (loop) and its honest ceiling (frontier). Expand to explore.)*

### Four layers, one firewall

*(figure: The Commonwealth Protocol: four layers, with a constitutional firewall isolating the personhood registry from the money layers — Layer 0 — the personhood registry — is firewalled from the money layers and holds exactly one right: the dividend. Layer 1 (the treasury) pays that dividend only from realized yield plus levy, never issuance; Layer 2 wraps assets under a low, banded depreciating-license levy; Layer 3 makes every covenant obligation payable only in the dividend token. Levy flows up into the treasury; the dividend is the one value permitted to cross the firewall to verified persons.)*

**Layer 0 — personhood, firewalled.** A registry of unique humans (method evaluated against Part I's open criteria) whose members hold exactly one right — the dividend — and whose governance shares no token or treasury coupling with any other layer. The central-bank-independence lesson, applied to identity; the direct answer to the Proof of Humanity fork war.

**Layer 1 — the treasury.** Yield-bearing tokenized assets (today that means Treasuries — the one production-grade rail). The dividend is paid from realized yield plus levy inflow, never issuance. This is an invariant, not a policy: the dividend can be small, but it cannot be fake — and sustainability becomes an accounting identity a script can check.

**Layer 2 — the covenant wrapper.** Assets join the commonwealth by being wrapped under a covenant that runs with the asset, condominium-style. Wrapped assets carry a low, asset-class-tuned depreciating-license levy (Weyl–Zhang): self-assessed within bands, forced-sale softened, small holdings exempt — because loss-aversion, not economic theory, is what the mechanism must survive. Self-assessment is used for allocation, never claimed as a truthful price oracle: its authors state plainly that it cannot incent all owners to announce true valuations.

**Layer 3 — the demand loop.** Every covenant obligation — levy, fee, settlement — is payable only in the dividend token. Knapp's tax-driven money without the state: a pay-community whose obligations anchor its currency.

### The loop that creates demand

*(figure: The chartalist demand loop: levy-payers must buy the token that dividend-recipients sell — Dividend recipients sell tokens to asset holders, who must pay their levy in those same tokens to the treasury, which pays the dividend back to recipients. The loop gives the token a computable floor — roughly the levy rate times the wrapped-asset base divided by velocity — the structural demand every failed crypto-UBI lacked.)*

Asset holders must acquire the token each epoch to meet the levy; dividend recipients are the natural sellers. The UBI recipients become the levy-payers' counterparties by construction — structural flow, not speculation or goodwill. The token's floor is then a computable function of wrapped-asset value, levy rate, and velocity: an attackable claim, which is the point.

### The arithmetic of the dream

Strip the mechanism to its core and one variable dominates: **wrapped wealth per member** (W ⁄ P). A levy at rate τ, paid only in the dividend token and split across the membership, delivers a per-member dividend whose sustainable ceiling is simply `τ · W ⁄ P` — the full levy flow — while the first-year payout is `(1 − ρ) · τ · W ⁄ P`, since a share ρ is retained to compound the treasury, whose real yield y lifts the dividend in later years. Everything else is detail; the scale of the dream is set by how much wealth each member brings inside.

Against that we set three success tiers — author-chosen thresholds (claim `C15`), each anchored to a cited magnitude rather than derived: **poverty-relevant** at $270/yr (GiveDirectly transfer scale), **floor** at $2,000/yr (Alaska-dividend / global-wealth-ceiling scale), and **living wage** at roughly $10,000/yr and up (jurisdiction-indexed).

The model that turns this into arithmetic — its parameter ranges are engineering judgments, not empirical findings (claim `C14`: τ in a 0.5–3% viable band, real yield 1.5%, retention ρ 20%) — returns a blunt result, stated strictly as model output under those stated assumptions. At τ=2%, every $50,000 of wrapped assets per member yields **$1,000/yr** in full levy, of which about **$800** is paid out in the first year before the treasury compounds. So Rings 1–2 fund a *poverty-relevant* dividend at bounded membership (the hundred-thousand-member stretch case) or a merely *symbolic* one at population scale. A universal *floor* needs roughly global-mean wealth per member — about $100,000, a **$2,000/yr** ceiling — which is out of reach without Ring 3, the minimal leviathan. And a *living wage* from levies alone is arithmetically unreachable at any survivable τ: even 5% on mean global wealth is only $5,000/yr. The conclusion the arithmetic forces is narrow and honest — redistribution sets a floor; it does not manufacture a wage. For more than a floor, **the commons itself must grow**.

### Entry by rings — earning the way to property

*(figure: Entry by rings: earning the way from protocol-native assets out to real property — Ring 1 (protocol-native assets — namespaces, blockspace, protocol land) enforces perfectly by code and bootstraps the system. Ring 2 (tokenized financial assets) enforces strongly via issuer covenants, drawn in by listing plus aggregated dividend-recipient demand. Ring 3 (real property) splits: route 3a acquires assets under ordinary contract law with no new state role; route 3b reaches scale fast only if a jurisdiction adopts the covenant. On-chain title has historically worked only where the state already worked (Georgia), not where it did not (Honduras). Part III works the split.)*

The record forbids leading with real property: blockchain land registries succeeded where states already functioned (Georgia — political buy-in, modern records) and died where they did not (Honduras — political resistance; Sweden — pilot concluded, never implemented). So the design earns its way inward-out. For Ring 3 the claim is stated exactly: the protocol does not replace the leviathan; it hands the smallest possible leviathan a redistribution instrument that runs itself. The premise's question — how small can the leviathan get — is answered ring by ring: zero, issuer-sized, registry-sized. And Ring 3 itself splits, once the participation constraint is worked in Part III: route 3a acquires real assets under ordinary contract law with no new state role at all, and only route 3b — jurisdictional adoption — needs the leviathan, for speed rather than for possibility.

### The falsifiable core

> **OPEN-UNVERIFIED** — **Open challenge (C13), now executable.** Universality here means universal *within the registry* — every verified member, no means test — not universal across humanity. The sharpened question: **which tier can Rings 1–2 reach, at what membership, sustained for N ≥ 5 years, with zero issuance?** The flow-of-funds model (`verification/flow_model.py`, checked by `verify_numbers.py` #4–#6) makes this a mechanical arithmetic rather than a promise — it already shows a universal floor needs Ring-3 scale, so if a jurisdiction-free Rings-1–2 deployment cannot clear the poverty-relevant tier at its membership, that refutes the strong form and the dossier reports it. Either answer is the result; the design cannot un-fail its own arithmetic. The first person to parameterize a real deployment and run it gets named credit.

### Attack surface, enumerated now

**Wrapping evasion**

Hold the asset in an LLC, trade the LLC off-chain. Unanswerable in Ring 3 without jurisdiction; partly answerable in Ring 2 via issuer covenants. Stated as a scope limit, not solved.

**Valuation gaming**

Inherited from the depreciating-license literature, with its own admission that self-assessment is not a truth serum. Mitigated by low rates and bands; never claimed solved.

**Velocity collapse**

If wrapped-asset value stagnates, levy demand stagnates and the dividend's real value erodes. This is the failure mode the falsifiable core exists to test.

**Bootstrap subsidy vs time-symmetry**

Early-entrant boosts smell like every token ponzi. Constraint borrowed from Ğ1's Relative Theory of Money: any founding-cohort incentive must be bounded, published, decaying — and the model must test whether entry clears with none.

**Regulatory kill-switch**

The French ordinance of 1958 shut down demurrage currencies by decree; a protocol levy on securities can simply be prohibited. Jurisdictional analysis is unfinished work.

**The tiny-dividend truth**

At plausible early scale this pays cents, exactly like GoodDollar. The honest promise is a growth invariant — the dividend grows with the commons and is never faked by issuance — not a living wage.

### What is and is not new

The load-bearing novelty is the **chartalist anchor**. No published protocol design cites both Knapp and Harberger — and that pairing is the whole trick. The pay-community reading of Knapp (Rallo 2020) licenses tax-driven money *without a state*: a currency holds value because obligations are payable in it, and a voluntary pay-community can wield that logic as well as a government can. No one has connected that reading to an asset levy or to a per-person dividend. The Commonwealth Protocol does exactly that — the levy on wrapped assets is payable only in the dividend token, so the levy-payers must buy what the dividend-recipients sell.

Three further elements are, to our knowledge, individually unprecedented in this combination: an **RWA-wrapper levy** — a Harberger/Weyl–Zhang levy on covenant-wrapped real-world assets, not NFTs and not digital land, the only places self-assessed levies have actually run; a **zero-issuance dividend**, paid only from realized yield plus levy inflow, the exact inverse of every deployed personhood dividend, which mints; and a **computed viability frontier** with an explicit ceiling finding, so the design states in advance which tier it can and cannot reach.

The narrowed claim, stated exactly (`C10`): to our knowledge, no published work at any quality tier combines (i) a Harberger/partial-common-ownership levy on covenant-wrapped real-world assets, (ii) a zero-issuance per-person dividend paid only from realized yield plus levy inflow, (iii) covenant obligations payable only in the dividend token — a chartalist demand anchor operated by a non-state pay-community — and (iv) a flow-of-funds viability frontier with an explicit ceiling finding. The search that grounds this claim is dated, documented, and repeatable; two minor leads remain open and are listed in the audit trail.

### Nearest neighbors, and the distinctions that matter

**Vicente (2023), Web3-enabled Harbergeorgism.** The closest work: a Harberger-plus-Georgist levy on tokenized *land* funding a citizens' dividend for a charter city. Four distinctions. It levies land, not covenant-wrapped real-world assets broadly. It is partly *issuance*-funded, where the treasury invariant forbids minting outright. Its beneficiary is a charter-city government; ours is a non-state pay-community. And it runs *two* tokens, where the Commonwealth's single-token payability is load-bearing, not cosmetic: because the levy is payable only in the dividend token, the asset-holders who owe the levy must acquire it from the dividend-recipients who hold it — that one fact makes the recipients the levy-payers' structural counterparties, the demand every two-token design in the graveyard failed to manufacture.

**Bruenig (2018), Social Wealth Fund for America.** A per-person dividend paid from the realized yield of a collectively-owned asset fund — the same yield-dividend right the Commonwealth grants. But it is statist (the fund is a public institution), off-chain, and *levy-free*: the state acquires assets by purchase, taxation, and stock transfers. The Commonwealth replaces those state acquisition routes with the covenant levy, and the state itself with a firewalled registry.

**1Hive / Duncan, Harberger Taxation and Open Source.** The nearest on naming and on per-person distribution: a self-assessed levy on software licenses funding a "digital commonwealth," with per-person governance shares. But the levy is on software, not real-world assets plus yield, and its per-person shares are *governance* rights. In the Commonwealth the registry's members hold the dividend right ONLY and govern nothing — the constitutional firewall the Proof of Humanity fork war exists to justify.

## PART III — THE LIMIT: what needs a state, what doesn't, and what each costs

**THE FINDING — this part states the dossier's central result: the binding constraint is political, not technical. It is derived, labeled, and attackable.**

### The participation constraint

The covenant is voluntary, so ask when a rational holder of wealth W joins it. Wrapping costs the levy τ·W each year and returns the dividend d plus whatever idiosyncratic benefit b the covenant confers per dollar wrapped — liquidity, clear title, market access. Entry is rational only when `b ≥ τ − d/W`. Two facts follow. Below a break-even wealth `W* = d/τ` — at τ=2% and a $1,000 dividend, **$50,000** — entry pays for itself even at b=0: the small holder is a net recipient and joins freely. Above it, the term d/W shrinks toward nothing: a holder of $1M pays **$20,000**/yr against a ~$1,000 dividend and needs b ≥ 1.9% to enter; at $10M, b ≥ 1.99%. For concentrated wealth the condition is simply b ≥ τ.

So voluntary entry *adversely selects*: net recipients and weak assets — those whose owners most value the covenant's liquidity and title — flow in; concentrated wealth and strong assets stay out unless the private benefit happens to exceed the levy. A voluntary levy therefore cannot reach the wealth that redistribution most wants to reach. Redistributing existing concentrated wealth requires compulsion — a levy no one may decline — and a compulsory levy is a tax, which is a state monopoly. This is claim `C16`, derived from the premises stated above, and it is the dossier's hinge.

*Technology cannot solve a participation constraint. It can only raise b — and b is bounded by what liquidity, title, and access are actually worth.*

### Why polities don't adopt it either — without the ideology premise

One might answer: then let a state run it. But the same constraint reappears as politics. Olson's logic of collective action (1965) is enough — a commons levy imposes concentrated costs on organized wealth-holders and spreads diffuse benefits over an unorganized many, so the concentrated side out-organizes the diffuse side and blocks adoption in *any* polity, whatever its professed ideology. The argument needs no claim about any nation's beliefs, which is exactly why it is robust. The confirming asymmetry is in the record: Alaska's dividend has survived four decades of ordinary politics *after* its creation — electorates keep a commons dividend once it exists — yet no polity has retrofitted one onto existing private wealth. Creation against incumbents is the barrier, not maintenance. This is claim `C17`.

An honesty note, because the temptation here is to over-claim: whether a basic income at living-wage scale would raise or lower aggregate wealth is unproven in either direction — the pilots do not reach that regime (Part I's labor-supply limit, `C06`). This dossier asserts no growth promise. The limit it states is about who can adopt the mechanism, not about what the mechanism would do to output.

### The three routes that need no one's permission

If compulsion is off the table, the design does not die — it slows down. Three accumulation routes fund the dividend without ever violating the participation constraint, because none asks a reluctant holder to wrap.

**Route 3a — acquisition under ordinary contract law.** Community land trusts already do this: the Champlain Housing Trust has run covenant-encumbered, resale-restricted (Georgist-flavored) tenure at the scale of thousands of homes for decades, using nothing but private property and contract law. The commonwealth's treasury — its retained levy plus protocol revenue — compounds into trust-held real assets the same way. The state's only role is enforcing contracts, which it does for everyone; no new political permission is required.

**Route R — a protocol-revenue endowment.** The protocol's own infrastructure rents — blockspace, sequencer revenue, namespace fees — can fund the dividend with zero coercion. The revenue half already runs at scale: Optimism's Collective directs sequencer revenue to public goods through iterated retrospective funding. No one has yet pointed such an engine at a personhood-gated, no-mint dividend; doing so is the design's most immediately buildable route.

**Route N — a new-commons constitution.** The cleanest route creates the asset inside the covenant, as Alaska's oil revenue was born inside its dividend. An asset class that never existed outside the commonwealth has no incumbent to out-organize and no exit to adversely select — the participation constraint simply never binds, because there was never an outside holder to decline.

**Route 3b — jurisdictional adoption.** The fast branch survives, but relabeled: a jurisdiction that adopts the covenant reaches scale in one legislative act rather than decades of compounding. Part III's whole first half is the analysis of why that act is unlikely — it must be won against incumbents at a constitutional moment, not maintained afterward.

### The cost is time

The no-state routes buy their way past the participation constraint with time, and the model prices it. From today's Ring 1–2 base ($1,000 wrapped per member, a $20/yr dividend at τ=2%), holding membership constant, the dividend reaches the poverty-relevant tier in about **27 years** and the floor tier in about **48 years** at an endowment growth rate of 10%/yr; at 20%/yr, in about 14 and 25 years. The governing variable is the endowment growth rate g, not the levy rate τ — once the levy is set, time is bought with growth. Two honesty flags: g in the modeled 5–20% range is a young-protocol accretion assumption (protocol revenue plus retained levy plus new-commons formation), an author judgment in the `C14` family, not a market-return promise; and constant membership is a conservative simplification — a growing membership raises the bar and lengthens the wait. This is claim `C18`.

### The conclusion, and the premise answered

The technical objects exist. The registry, the zero-issuance invariant, the covenant levy, the chartalist anchor, the arithmetic and its ceiling — this dossier has built their composition and made it testable, and its own verifier re-derives every number on this page. What does not exist is the collective choice. The fast path opens only at constitutional moments, on new commons, before incumbents form; the slow path is open now, to anyone, and requires no permission — only patience measured in the growth rate of a commons.

The premise asked whether there could be a plural consciousness with economic rules that hold a thriving economy and a life worth living in the same hand. The dossier's earned answer: the rules can be written and the machine can be run — the missing input is the consciousness itself. That is the limit. It is stated here not as a defeat, but as an address.

**PART I · THE RECORD**

## PART I — THE RECORD: what has been tried, what failed, what held

### How to read this part

Every claim here is either a cited finding, a reported claim from an interested party (recorded for provenance, not proof), or an author judgment labeled as such. Where a project's own documentation is the only source, that is said plainly. One honesty caveat governs this first release: the citations are entered but this dossier's own citation audit has not yet run, so every source-backed claim currently sits at status OPEN — it becomes ESTABLISHED only once that audit re-fetches and re-checks it. Nothing here is asserted as verified.

Ledger snapshot, entered 2026-07-29 — twelve claims, none yet verified: six are citation-backed but awaiting the citation audit (status OPEN); four are author judgments held `OPEN-UNVERIFIED`, including `C08`, the central open challenge; one is `EXPLORATORY-CONJECTURE` (the asset-redistribution mechanism, `C09`); and one is a `NOVEL` claim recorded to-our-knowledge (`C10`, pending a deeper novelty search). Zero are asserted as established. Every count is a live status, not a verified one; the full typed ledger is claim_ledger.csv in the repository.

## Avenues

| Avenue | Thesis | Status | Forecast | Sources |
|---|---|---|---|---|
| Proof of personhood | Per-person issuance stands or falls on sybil resistance; biometric (Worldcoin), social-graph (Duniter/Ğ1), and adjudication (Proof of Humanity) have all shipped — none has uniqueness, privacy, and scale at once. | OPEN-UNVERIFIED | — | C01, C02, C03, C04 |
| Monetary levers | Reserve-yield issuance (GoodDollar) and demurrage (Gesell/Freicoin/Wörgl/Sarafu) exist as mechanisms; none has defended a dividend's real purchasing power at scale. | OPEN-UNVERIFIED | — | C08, C11, C12 |
| Work incentives (the pilots) | Finland, Kenya, Stockton, and Alaska show small-to-null labor-supply effects at modest transfers; no pilot reaches the living-wage regime. Cited; awaiting this dossier's own citation audit. | OPEN | — | C05, C06 |
| The Commonwealth Protocol (Part II) | The candidate composition: covenant-wrapped assets whose depreciating-license levy is payable only in the token that pays a per-person dividend, under a zero-issuance treasury beside a firewalled personhood registry. Established ingredients (chartalism, Harberger/Weyl–Zhang, sovereign-wealth dividends); unproven as a whole. Falsifiable core: C13. Novelty (C10) now grounded by a dated 2026-07-29 prior-art search — see the audit trail. | EXPLORATORY-CONJECTURE | — | C09, C10 (search 2026-07-29), C13 |
| The graveyard | Proof of Humanity's UBI token, Circles UBI, and Freicoin each failed on the demand side — value or acceptance — never on distribution. | OPEN-UNVERIFIED | — | C07 |
| The central challenge | Whether protocol levers — issuance, demurrage, fee recycling, reserve backing — can sustain a UBI's real purchasing power while preserving work incentives; criteria to be set in the reserved blueprint. | OPEN-UNVERIFIED | — | C08 |
| The Limit (Part III) | The dossier's central finding: a voluntary levy adversely selects (entry needs b >= tau - d/W, which fails for concentrated wealth), so redistributing existing concentrated wealth needs a state — but three no-state routes (contract-law acquisition, protocol-revenue endowment, new-commons constitution) fund the dividend anyway, at the cost of time. Derived + argued; red-team pending. | OPEN-UNVERIFIED | — | C16, C17, C18 |

## Consistency checks

Results from `verification/verify_numbers.py` — the same checks the in-page console runs; CI reruns them on every commit.

- [PASS] Consistency: at least one avenue in the landscape
- [PASS] Consistency: every FORECAST has a dated signpost
- [PASS] Consistency: all forecast probabilities lie in [0,100]
- [PASS] C13 conservation: model outputs recompute exactly from raw inputs (0 mismatches)
- [PASS] C13 scaling: tau=2%, $50k wrapped/member -> $1,000/yr levy and $800 first-year net; both quoted in the manuscript
- [PASS] C13 ceiling: tau=2%, global-mean $100k/member -> $2,000/yr; quoted in the manuscript
- [PASS] C16/C18 Part III: W*=$50,000 (d/tau), $1M holder pays $20,000 vs a ~$1,000 dividend, floor time-to-tier ~48 years at g=10%; all quoted in the manuscript

**TOTAL: 7 checks · 7 pass · 0 fail** — All checks pass — the survey is internally consistent.

## 01 Proof of personhood — the binding constraint

Any per-person issuance stands or falls on sybil resistance (A system's ability to stop one actor from minting many fake identities to claim more than their share. For a per-person dividend it is the whole game: without it, one person farms thousands of accounts and the payout collapses.). Three approaches have shipped. **Biometric** (Worldcoin/World ID): iris-scan enrollment at the largest scale attempted — tens of millions of verified users — purchased at the cost of documented regulatory rejection (suspensions or bans including Kenya 2023, Spain and Portugal 2024, Brazil 2025, over consent and data-protection law) and a structural risk no patch removes: biometric identifiers cannot be rotated if compromised. **Social-graph** (Duniter/Ğ1; Circles): membership by certification within a web of trust. Ğ1 has issued a daily Universal Dividend under the Relative Theory of Money since 2017 — the longest-lived per-person crypto dividend in existence — with issuance calibrated for symmetry between generations (roughly 10% annual monetary growth shared equally, so late joiners create the same lifetime share as early ones). Its demonstrated ceiling is scale: a community of tens of thousands, mostly francophone, with modest purchasing power. **Adjudication-based** (Proof of Humanity): a challengeable registry with dispute resolution. The registry functioned; what happened to its paired token is in the graveyard. The honest joint statement, entered as open claim `C04`: no approach has yet demonstrated uniqueness, privacy, and scale simultaneously.

## 02 The money side — issuance, reserves, demurrage

**GoodDollar** is the closest deployed relative of an endowment-funded dividend: supporters stake capital in third-party yield protocols, the yield flows into a reserve contract that mints G$, and daily claimers split the remainder. The mechanics function; the economics are candid about their own limits — G$ trades at a fraction of a cent, and the project's "proof of need" framing (only those for whom tiny sums matter will bother claiming daily) is an admission that per-person value cannot yet be defended at scale. **Demurrage** (the Gesell/Freigeld lineage): the one historical success, Wörgl 1932, operated inside captive demand — the municipality accepted the depreciating scrip for taxes. Where demurrage (A holding fee on money itself: a balance slowly shrinks if you sit on it, to push currency into circulation. Silvio Gesell's idea, tried at Woergl in 1932. It stimulates spending mainly where people are compelled to hold the currency.) has competed voluntarily against non-decaying money, it has lost: Freicoin implemented Gesell faithfully on Bitcoin-derived rails and found almost no users, and the French demurrage experiments of the 1950s were terminated by ordinance — a reminder that the legal kill-switch on parallel currencies predates crypto. The living exception proves the rule: Grassroots Economics' Sarafu community currencies in Kenya operate demurrage-adjacent mechanics inside deliberately local demand loops. Entered as `C11`/`C12`.

## 03 What the pilots actually established about work

Four bodies of evidence anchor the work-incentive question. **Finland 2017–18** (Kangas et al., final report 2020): 2,000 unemployed persons, €560/month unconditional; employment effects small (about 6 additional days worked in the reference period), wellbeing effects clearly positive; a sanction-regime reform mid-experiment confounds the second year, and the report says so. **Kenya** (Banerjee, Suri, Niehaus et al.): the largest UBI RCT ever run — roughly 23,000 treated adults across lump-sum, two-year, and twelve-year arms at about $22.50/month — found no work disincentive and shifts from wage labor toward business formation. **Stockton SEED** (West & Castro Baker, 2021): $500/month, n=125; full-time employment rose 28%→40% in year one versus 32%→37% in control — directionally positive, but a small philanthropic pilot, and labeled as such. **Alaska** (Jones & Marinescu, AEJ: Economic Policy 2022): four decades of a universal annual dividend (about $2,000/person recently) produced no aggregate employment decline, with part-time work up 1.8 points and general-equilibrium stimulus plausibly offsetting individual labor-supply effects. The load-bearing limit, entered as `C06`: modest transfers, modest-to-null effects — and no study anywhere reaches the living-wage regime. Extrapolation in either direction is unsupported.

## 04 Asset precedents — the ingredients of the hard question

Three cited ingredients exist for redistribution beyond currency; no published work combines them. **The sovereign-wealth dividend**: Alaska (and Norway's fund, without the dividend) show that a diversified asset endowment can fund a universal payment for decades — state-run, off-chain. **Harberger taxation** (Weyl & Posner, Radical Markets, 2018): owners self-assess value, pay a continuous levy on the declaration, and must sell at the declared price — a mechanism with a genuine academic literature on its allocative-versus-investment-efficiency trade-off, implemented on-chain only for digital assets and micro-experiments (EIP-5320; Wildcards; Geo Web; This Artwork Is Always On Sale) plus one unoperationalized exploration for real land (CityDAO). **RWA tokenization**: roughly $32B on-chain by mid-2026, led by US Treasuries (about $15B) — but real estate at only about $200M, 97% of value inaccessible to US retail, and a substantial share lacking clear regulatory frameworks (industry-tracker figures; REPORTED grade). The rails exist for Treasuries, barely exist for property, and are legally gated everywhere.

## 05 The graveyard — documented failure modes

**Proof of Humanity's UBI token — died of no-sink issuance plus governance capture.** One token per verified human per hour, streamed continuously, with only cosmetic burns: relentless sell pressure met no structural demand, and the Kleros cooperative's post-mortem documents an ~87% loss on its own liquidity position and a governance war in which token-aligned voters passed proposals that effectively forked the registry. The identity layer and the money layer captured each other. *Forecloses: naked streaming issuance; shared governance between registry and token.*

**Circles UBI (Berlin) — died of the acceptance problem.** Personal-currency web of trust, 7% demurrage, real merchant-onboarding effort, shut down late 2023: participants accumulated tokens faster than the merchant network could absorb them, and the academic post-mortems converge on one sentence — an alternative currency cannot survive on subsidies; it must solve a real coordination problem. *Forecloses: issuance-plus-goodwill as an adoption theory.*

**Freicoin — demurrage without captive demand.** Faithful implementation, negligible adoption: a decaying token is strictly dominated as a store of value and never acquired the exchange economy that would justify holding it. *Forecloses: demurrage as a voluntary default.*

**Democracy Earth's HOUR→UBI lineage** — sold-then-unreleased tokens, missed deadlines, diverted funds, per the Kleros account (an interested party in the dispute; REPORTED, provenance stated). *A caution about token-first funding, not a mechanism result.*

The joint lesson, entered as `C07`: every deployed crypto-UBI failed on the demand side — value or acceptance — never on distribution. Distribution is solved. Defensible value is not.

## 06 Open questions — the territory ahead

(1) Sybil resistance with uniqueness, privacy, and scale together (`C04`). (2) Whether any protocol lever set can sustain a dividend's real purchasing power — no deployed system has, and no agreed success metrics even exist; this dossier's central open challenge (`C08`) will state falsifiable criteria. (3) Work incentives at living-wage scale (`C06`). (4) Endogenous demand: why hold the token — the question every corpse above answers in the negative. (5) Whether non-currency assets can be brought into the loop at all (`C09`/`C10`) — the blueprint's burden, carried openly with its attack surface: capital flight, oracle and valuation manipulation, and the legal enforceability of on-chain claims to off-chain property.

## 07 Design constraints extracted from the record

The blueprint that will sit above this part must satisfy, at minimum: **(i) demand before distribution** — sinks and holding reasons specified before issuance schedules (Circles, Freicoin, PoH-UBI); **(ii) no naked streaming issuance** (PoH-UBI); **(iii) identity layer firewalled from money-layer governance** (the PoH fork war); **(iv) demurrage only inside a captive-demand loop** (Wörgl versus Freicoin; Sarafu); **(v) a purchasing-power target requires an endowment** — the gap between GoodDollar's pennies and Alaska's forty years is the funding problem, not the mechanics; **(vi) the asset mechanism is the answer to the tax-base problem** — wealth held as equities and property is invisible to currency-level redistribution, which is why currency-only UBI coins fought over a base too small to matter; any serious design must reach it, and must survive the enumerated attacks or say that it cannot. A blueprint that cannot fail its own analysis is a whitepaper.

## References

*Full cite cards; identifiers marked TO-VERIFY are to be resolved in the citation audit, never asserted. Until that audit runs, these sources back claims held at status OPEN.*

**Kangas, O., Jauhiainen, S., Simanainen, M., Ylikännö, M. (eds.) (2020).** Evaluation of the Finnish basic income experiment. Ministry of Social Affairs and Health, Reports 2020:15, ISBN 978-952-00-9890-2. Final report of the 2017–18 RCT: 2,000 unemployed recipients of €560/month; small employment effects, clear wellbeing gains, year-two confound from the activation-model reform disclosed.

**Banerjee, A., Faye, M., Krueger, A., Niehaus, P., Suri, T. (2023).** Universal Basic Income: Short-Term Results from a Long-Term Experiment in Kenya. NBER Working Paper (number TO-VERIFY). About 23,000 treated adults across lump-sum, 2-year, and 12-year transfer arms; no work disincentive; shift toward enterprise formation.

**West, S., Castro Baker, A. (2021).** SEED first-year findings. Stockton Economic Empowerment Demonstration (stocktondemonstration.org; no DOI). $500/month, n=125; full-time employment 28%→40% versus 32%→37% control.

**Jones, D., Marinescu, I. (2022).** The Labor Market Impacts of Universal and Permanent Cash Transfers: Evidence from the Alaska Permanent Fund. AEJ: Economic Policy 14(2), 315–340. DOI 10.1257/pol.20190299. Synthetic-control study: no aggregate employment effect; part-time work +1.8pp; general-equilibrium offset interpretation.

**Weyl, E.G., Posner, E. (2018).** Radical Markets. Princeton University Press. Source of the COST/Harberger mechanism and its efficiency trade-off analysis.

**Siddarth, D. et al. (2020).** Who Watches the Watchmen? Sybil-resistance in Proof of Personhood Protocols. arXiv:2008.05300. Comparative review including Duniter's web-of-trust design.

**Avanzo, S. et al. (2025).** Impact of a Blockchain-based UBI Pilot: the case of Circles UBI. arXiv:2504.02714. Berlin pilot post-mortem: token accumulation versus merchant-network attrition; abrupt 2023 shutdown.

**Papadimitropoulos, V. et al. (2024).** Universal basic income on blockchain: the case of Circles UBI. Frontiers in Blockchain. DOI 10.3389/fbloc.2024.1362939. Failure analysis; UBI-on-chain insufficient absent a production/acceptance model.

**Lesaege, C. (2022).** Making sense of recent drama in Proof of Humanity. Medium. REPORTED — interested-party post-mortem; documents the cooperative's UBI-token loss and the registry fork conflict.

**EIP-5320 (2022).** Ethereum Improvement Proposal for NFTs under continuous self-assessed (Harberger) taxation (status TO-VERIFY).

**Industry RWA trackers (2026).** Tokenized RWA about $32B mid-2026; Treasuries about $15B; real estate about $0.2B; retail-access and regulatory-framework gaps. REPORTED grade (BeInCrypto "Real State of Tokenization in 2026"; rwa.xyz), pending triangulation.

**Duniter/Ğ1 documentation and Laborde, S. (2010), Relative Theory of Money.** Project sources for web-of-trust parameters and Universal Dividend calibration; REPORTED where uncorroborated.

**Grassroots Economics / Sarafu documentation.** Kenyan community-currency deployments with demurrage-adjacent mechanics; REPORTED grade pending independent literature (cite TO-VERIFY).

**Knapp, G.F. (1905/1924).** The State Theory of Money. Macmillan (English edn. 1924). Origin of chartalism: a currency holds value because obligations are payable in it; a pay-community beyond the state can, on the same logic, issue chartal money — the premise Part II's demand loop rests on.

**Weyl, E.G. & Zhang, A.L. Depreciating Licenses.** SSRN 3698941, DOI 10.2139/ssrn.3698941. Partial-ownership licenses under a self-assessed depreciating levy; a tunable rate trades allocative against investment efficiency, with the explicit stated limit that self-assessment cannot incent universally truthful valuations — the Layer-2 mechanism and its named caveat.

**Systematic review of blockchain land administration (2022).** Land Use Policy / ScienceDirect, article S0264837722005002 (DOI TO-VERIFY). Cross-case review: Honduras stalled on political resistance, Sweden concluded its pilot without implementation, and Georgia succeeded via political buy-in and modern records — the evidence behind Ring 3's jurisdiction requirement.

**Vicente, B.M. (2023).** Web3-enabled Harbergeorgism: A Policy Mechanism for Charter Cities. Charter Cities Institute Research Paper (Jan 2023). The strongest near-miss for C10: a Harberger-plus-Georgist levy on tokenized land funding a citizens' dividend — but partly issuance-funded, two-token, with no personhood firewall, no chartalist anchor, and no stability frontier.

**Rallo, J.R. (2020).** Georg Friedrich Knapp Was Not a "Chartalist." History of Political Economy 52(4), 773–793. DOI 10.1215/00182702-8604033. The pay-community reading of Knapp — a currency holds value because obligations are payable in it, a logic a non-state pay-community can wield — which licenses the Commonwealth's chartalist demand anchor.

**Bruenig, M. (2018).** Social Wealth Fund for America. People's Policy Project. A per-person dividend paid from the realized yield of a collectively-owned asset fund; statist, off-chain, and levy-free — the nearest yield-dividend right, distinguished by the Commonwealth's covenant levy and firewalled registry.

**Olson, M. (1965).** The Logic of Collective Action: Public Goods and the Theory of Groups. Harvard University Press. The concentrated-costs / diffuse-benefits account of why small organized interests defeat large unorganized ones — the ideology-free basis for Part III's non-adoption argument (C17).

**Davis, J.E. (ed.) (2010).** The Community Land Trust Reader. Lincoln Institute of Land Policy (card TO-VERIFY). Documents the community-land-trust model — covenant-encumbered, resale-restricted tenure under ordinary contract law — the precedent (e.g. the Champlain Housing Trust, thousands of homes over decades) for Part III's no-state acquisition route 3a.

**Optimism Collective — Retroactive Public Goods Funding / sequencer-revenue documentation.** optimism.io governance docs (REPORTED grade; TO-VERIFY). A live, at-scale precedent for funding public goods from protocol (sequencer) revenue — the revenue half of Part III's protocol-endowment route R; no deployment yet points such revenue at a personhood-gated no-mint dividend.
