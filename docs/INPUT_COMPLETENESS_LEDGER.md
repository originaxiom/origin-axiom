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
