# THE INPUT-COMPLETENESS LEDGER — mandatory checklist for any SM-facing cell

*Purpose: "make sure we're accounting for every smallest detail that would affect the
math." Every future cell that compares project quantities to measured physics fills this
table in its prereg, before sealing. An unfilled row is a design defect, not a formality.*

| # | Item | The question the cell must answer in writing |
|---|---|---|
| 1 | **Scheme** | For every target: which renormalization scheme / mass definition (pole, MS-bar, on-shell, effective)? Mixed-scheme ratios are ill-defined (precedent: m_t/m_b spans 36–61 across conventions — B615-R correction iii). |
| 2 | **Scale** | At which μ is each running quantity quoted, and why that μ? The object supplies no scale (I6: ABSENT) — so any single-μ comparison is a human convention; either use RG-invariant combinations, or scan μ and price the look-elsewhere. |
| 3 | **Uncertainties** | Full 1σ (asymmetric if given), propagated into both the match windows AND the null (2σ inflation on both sides, or a likelihood treatment). Point-value windows tighter than the measurement's resolution overstate significance by construction (precedent: B615 → B615-R, 0.078 → 0.145+). |
| 4 | **Multi-modal fits** | Octant / mass-ordering / local-minima structure of the global fit (θ₂₃ flipped octant between NuFIT 6.0 and 6.1 — a central value can move by 15% between releases; run each mode as a sensitivity variant). |
| 5 | **Convention constants** | Any target that is a convention, not a measurement (M_GUT, unification scales, scheme-dependent "effective" parameters) is flagged in-output and never drives a verdict. |
| 6 | **Fit-vs-direct** | Where global-fit and direct-measurement values differ (|Vcb|, |Vub| exclusive/inclusive), state which is used and why; note the other. |
| 7 | **Look-elsewhere** | The correction covers ALL grids, tiers, variants, and modes actually examined — including sensitivity variants (Šidák/Bonferroni over the full family, not the headline alone). |
| 8 | **The matched null** | The null model draws targets from the same measure the match criterion uses (unit-uniform / log-uniform / posterior-width-inflated) — never a narrower one (precedent: B615's two in-run null bugs; B539's tautology exclusion). |
| 9 | **MB13 grep** | Keyword-grep + atlas check that the comparison (or its kill) isn't already banked. |
| 10 | **The firewall question** | Is this cell asking the object for VALUES? The banked theorems (K020 Galois firewall; the role-separation law) say values live in the stage. If yes: state explicitly which stage-selection assumption is being tested, or reframe. |
| 11 | **Source freshness** | Targets fetched from the current primary source (NuFIT/PDG release + date recorded), not recalled from memory; the fetch archived in the packet. |
| 12 | **Sealing** | Inputs pasted verbatim BEFORE the seal; design + runner hashed; outputs banked before comparison prose. |

## First application: the recorded B615 audited against this ledger

Pass: 7 (Šidák over grids), 8 (after the two disclosed in-run fixes), 9, 12 (design-hash
verified in-run). Fail: 1 (schemes unstated; G3 mixed), 2 (single implicit μ = M_Z /
mixed), 3 (point values; disclosure flagged it), 4 (single octant), 11 (values recalled
from assistant knowledge, accurate but unarchived). Items 5, 6 partially (M_GUT carried
undflagged in-grid; CKM source unstated). **The verdicts survive the audit** — B615-R
re-ran the failed items and the conclusion strengthened (dissolution). The ledger exists
so the next cell passes all twelve at design time.

---

## Second application: the Maass spectral comparison (B792 / B797, audited 2026-07-29)

*Audited by cc AFTER banking — the row was missing, which is itself a rule-6 defect. The
substance passes; the paper trail did not exist. Recorded rather than quietly added.*

| # | Item | Status for B792/B797 |
|---|---|---|
| 1 | Scheme | **N/A-by-construction.** The compared quantities are Laplace eigenvalues r_n, λ_n = 1+r_n² of a fixed hyperbolic 3-manifold — scheme-free. The SM targets carry their own schemes via the B743 list (item 11). |
| 2 | Scale | **N/A on the object side** (no μ enters a Laplace eigenvalue); the object supplies no scale (I6: ABSENT), which is precisely why only *dimensionless* PDG ratios were targeted. |
| 3 | Uncertainties | **PASS.** τ_v = max(2·rel_unc_v, 1e-8) uses the full quoted relative uncertainty per target, and the **surrogate null runs the identical window**, so windows and null are matched. Eigenvalue-side uncertainty is mode-count certified: **max \|Δr\| = 5.42e-9**, below the 1e-8 floor (by 1.8× — see the caveat below). |
| 4 | Multi-modal fits | **N/A.** No global-fit targets (no θ₂₃/octant-type quantities in the B743 list). |
| 5 | Convention constants | **PASS by absence** — no M_GUT/unification-scale/scheme-effective targets in the list. |
| 6 | Fit-vs-direct | **N/A** — the B743 list carries per-target sources; no fit/direct ambiguity arises for the mass ratios used. |
| 7 | Look-elsewhere | **PASS.** Per-target surrogate probability (not a headline-only correction), 500 surrogate spectra, applied across Test 1, Test 2's full pairwise-ratio family, and Test 3's six bases. 39 raw Test-2 candidates, **0 gated**. |
| 8 | The matched null | **PASS.** Surrogates are Weyl-distributed (density ~ r² over the observed window, same count) — the same measure the match criterion uses. |
| 9 | MB13 grep | **PARTIAL.** No keyword/atlas check is recorded in the arc. Mitigated: the comparison's *kill* is the standing banked pattern (C17 no-SM-record), so a duplicate-banking risk is low — but the grep was not run and is marked as not-run. |
| 10 | The firewall question | **PASS, and decisive.** Yes, this cell asks the object for VALUES. Per `LISTENING_PROTOCOL` §1 its Tests 1–2 are **rung 4 (single-ratio, number≈number) = "DEAD ON ARRIVAL, however small the σ-distance"**; only **Test 3 (algebraicity) is rung 1**, falsifiable-to-precision, and it was correctly left unclaimed in both directions at 8 digits. **The clean null on Tests 1–2 therefore confirms an inadmissible comparison and is not evidence.** |
| 11 | Source freshness | **PASS by inheritance.** Targets are `frontier/B743_rung1_widened/pdg_targets.json`, sha256 **e93efeaa** — re-verified 2026-07-29 as **byte-identical to B743's sealed record, no drift**. 18 entries, each carrying an explicit source (CODATA 2022 via PDG 2024 muon listings; PDG 2024, Navas et al., Phys. Rev. D 110). Web-verified by two non-authoring agents at B743. **Not recalled from model memory** — the failure mode B615 hit on this item. |
| 12 | Sealing | **PASS, with a disclosed history.** Prereg `c6954bfa`, hash re-verified byte-identical on harvest into B797. The first run was **demoted to a dry run** and the seal placed before the *certified* run, with three declared amendments (A1 mode-certified spectral set, A2 tolerance floor from certification, A3 scope-corrected verdict). |

**Net: 8 PASS, 3 N/A, 1 PARTIAL (item 9, MB13 grep not run).** No item fails.

**Two caveats that belong with the row, not buried in the arc:**
- **Item 3 margin.** The certification clears the *typical* τ_v ≈ 2e-5 by ~4000×, but the **1e-8
  floor by only 1.8×** — eigenvalue uncertainty is 54 % of the tightest usable tolerance. Adequate
  as run; **any future comparison at tighter τ must re-certify first.**
- **Item 10 is the finding.** The protocol had already ruled Tests 1–2 inadmissible before they
  ran. The result worth carrying forward from this cell is not the null but that **rung 1
  (algebraicity) is the only admissible comparison available** — which is independently where the
  B796 campaign falsifier landed.

## THE RECONCILIATION — this ledger's twelve vs the crossing lane's eleven (2026-08-13, closes the Part-0 audit's line 2)

**The finding that forced this section (the audit seat's census):** 23 arcs cite
measured sources; this ledger held TWO rows, both retroactive audits; the
crossings scrupulously fill a DIFFERENT list (CROSSING_REQUIREMENTS' R1–R11 —
B1027 answered R7/R8/R9/R11 and did much of this ledger's work in that
vocabulary, including item-11-style source-limitation disclosure). Neither list
cited the other; whether one covers the other was unasked by every seat. The
mapping, each of the twelve marked:

| # | this ledger's item | status vs R1–R11 |
|---|---|---|
| 1 | Scheme | **GAP as a rule** — no R-item requires scheme declaration. Mitigated in practice for phase targets (the PDG parametrization named in B1027); unmitigated for any future mass-ratio crossing. |
| 2 | Scale | **covered-by-R2** (interpolation derived or RG-insensitive target — the μ-question is R2's content). |
| 3 | Uncertainties | **covered-by-R6** (the precision budget; B1027's σ-powered criteria are the instance). |
| 4 | Multi-modal fits | **GAP as a rule** — B1027 stated the ordering (NO) ad hoc; the octant was N/A for δ_CP **and the N/A was never stated**. This ledger's own discipline: **N/A is a row, not a silence.** |
| 5 | Convention constants | **covered-by-R5** (kind-correctness; convention-vs-measurement is a kind distinction the KIND_TABLE licenses). |
| 6 | Fit-vs-direct | **GAP as a rule** — no R-item; mitigated in practice by naming NuFIT as the source. |
| 7 | Look-elsewhere | **covered-by-R7** verbatim. |
| 8 | The matched null | **covered-by-R6 for exclusion-type verdicts** (powered criteria); **GAP for any HIT-type crossing** — a hit claim needs the matched-null measure and no R-item mandates it. |
| 9 | MB13 grep | **covered-by-R1 + standing MB13 practice** (R1 is atlas/tower-specific; the general grep is corpus practice, noted not guaranteed). |
| 10 | The firewall question | **covered-by-R5 + R10** (kind licensing + channel declaration). |
| 11 | Source freshness | **covered-by-the-B1063 fetch-currency rule** (verdict-time fetches state their release and check the arXiv mirror — banked after the 6.0-existed-while-5.2-was-read defect; item 11 and the rule are convergent, written independently). |
| 12 | Sealing | **covered-by-R8 + the seal-before-compute law** (the E39 chain). |

**Verdict of the reconciliation: eight of twelve covered, FOUR GAPS as rules
(items 1, 4, 6, and 8's hit-branch).** Standing consequence, binding: **any
future crossing prereg fills BOTH lists — the R-numbers AND this ledger's
twelve — with N/A written as a row.** The four gap-items cannot ride the
R-list alone. (Species logged: two checklists, no cross-reference — line 1's
fork-collision trap with the opposite sign: coverage looked absent where it
was present. One day, both signs.)

---

## Third application: the value-probe wave (B1128–B1133), audited at Review 48

*Audited by cc at Review 48 — the rows were missing (a rule-6 defect, itself the same
species as the B792/B797 gap: substance covered ad hoc in each cell's PRECOMMIT, the
ledger row never written). Recorded here rather than quietly added. The wave's cells
(B1128 instrument-null, B1129 natural-values 506-pair grid, B1131 Koide, B1132 meridian)
each compare object quantities to measured SM values; each carried its own
`*_PRECOMMIT.md` with pre-registered routes, base rates, and fishing guards.*

| # | Item | Status for the value-probe wave |
|---|---|---|
| 1 | Scheme | **N/A-by-construction.** The object side is scheme-free (Kashaev-tower ratios, listener-map holonomies, det of a Cartan basis change — topological/Laplace invariants, no renormalization). SM targets carry their own schemes via the fetched sources (item 11). |
| 2 | Scale | **N/A on the object side** (no μ enters a knot invariant; the object supplies no scale, I6: ABSENT) — only dimensionless SM ratios/angles were targeted. |
| 3 | Uncertainties | **PASS.** B1128/B1131 quote σ-distances (the \|U_e1\|/\|U_e2\|=φ miss reported ~5σ; Koide 2/3 to measured precision); B1129's 506-pair grid runs a matched null. |
| 4 | Multi-modal fits | **N/A** — no octant/ordering-sensitive global-fit target drives a verdict; the PMNS e-row ratio is release-stable. Stated as a row, not a silence. |
| 5 | Convention constants | **PASS by absence** — no M_GUT/unification/scheme-effective target. |
| 6 | Fit-vs-direct | **N/A** — the targets used (mixing-angle ratios, Koide) are not fit/direct-ambiguous quantities. |
| 7 | Look-elsewhere | **PASS.** B1126's 352-pair and B1129's 506-pair scans price the full grid; B1131's four bridge routes counted (~8% base rate stated). |
| 8 | The matched null | **PASS for the exclusion verdicts** — B1129's null draws from the same measure the criterion uses; the wave's verdicts are all NEGATIVE (disjoint/null), the branch this ledger fully covers. No HIT-type claim was made (the branch with the R-list gap). |
| 9 | MB13 grep | **PARTIAL** — the atlas/keyword check is corpus practice; each cell cites prior art (B1128←B1116/LISTENER_MAP; B1131←B904) but a dedicated grep row was not recorded. |
| 10 | The firewall question | **PASS, and decisive.** Every cell asks the object for VALUES, and the wave's whole finding is that the answer is DISJOINT (periods) — "physics-shaped, not physics-valued." Per the firewall the admissible reframe (values-as-regulators) is named and left firewalled (B1134). |
| 11 | Source freshness | **PASS.** SM targets fetched from PDG/NuFIT with release + date in each PRECOMMIT (the B1063 fetch-currency rule), not recalled from memory. |
| 12 | Sealing | **PASS.** Each cell sealed its prereg (routes/base-rates/guards) before compute; outputs banked before comparison prose (E39). |

**Net: 7 PASS, 4 N/A, 1 PARTIAL (item 9). No item fails.** The wave's verdicts are all
negatives drawn against matched nulls — the branch this ledger and the R-list both fully
cover; the four rule-gaps (items 1/4/6, and 8's hit-branch) are HIT-branch gaps, and the
wave made no hit. Filed to close the rule-6 defect the R48 gate/integrity audit found.
