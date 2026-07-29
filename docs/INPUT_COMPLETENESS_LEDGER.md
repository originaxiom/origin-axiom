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
