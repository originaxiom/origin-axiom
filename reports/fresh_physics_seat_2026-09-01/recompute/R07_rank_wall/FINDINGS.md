# R07 — THE RANK WALL (B952/B955): recomputed blind. VERDICT: MATCH (one convention note, one vacuity note)

**Cell:** R07 · **Date:** 2026-09-01 · **Discipline:** blind-first, exact arithmetic.

## Read-before vs read-after (binding record)

**Read BEFORE computing** (claim statements only, permitted):
- `frontier/B952_gut_ledger_rank/FINDINGS.md`
- `frontier/B955_l133_scout/FINDINGS.md`

**Read only AFTER all blind outputs were on disk:**
- `tests/test_b952_rank.py`, `tests/test_b955_l133scout.py` (the locks)
- `frontier/B952_gut_ledger_rank/results.json`, `arc_verdict.json`
- `frontier/B955_l133_scout/arc_verdict.json`, `PRIOR_ART_RANK_REDUCTION.md`,
  `prior_art_rank_reduction.json` (contains the panel's scan record)

Blind code: `e6_scan.py`, `e6_types.py`, `knot_group.py` (written in a prior
session of this cell, committed at e262e63, re-run fresh today with identical
outputs) and `e6_adjoint_scan.py` (written today, still before any arc
verification file was opened). `diff_diagnostic.py` is post-unblinding.

## My blind numbers

**E6 built from the Cartan matrix alone:** 72 roots, dim 78. Root α contributes
to the centralizer of a torus element x iff α(x) ∈ ℤ; centralizer = t ⊕
(contributing root spaces), so **every centralizer of every torus element
contains t and has rank 6** — verified per element, all 66 377 scanned tuples
(n = 4, 5, 6). Semisimple-rank histogram {6: 389, 5: 7074, 4: 37314, 3: 21600}
shows the instrument genuinely discriminates the semisimple part.

**Type tables (deduplicated by contributing-root-set), two torus conventions:**
- **Simply-connected** E6 (x = c/n in the *coroot* basis, α evaluated via the
  Cartan matrix): su(3)⊕su(2)⊕u(1)³ (= A1+A2+u1³) first appears at **order 7**.
  It is NOT in the order ≤ 6 table of the simply-connected group.
- **Adjoint** convention (x = c/n in the *fundamental-coweight* basis, α = m
  evaluates to m·c/n — equivalently "all 6-tuples of root evaluations mod n"):
  A1+A2+u1³ first appears at **n = 6, c = (0,0,0,1,2,1)**, centralizer dim 14.
- Order 1–3 tables reproduce Borel–de Siebenthal: n=2 → {A1+A5, D5+u1, E6},
  n=3 → {A2+A2+A2, A5+u1, D4+u1², E6} (SC convention).

**Knot side (m004):** presentation gens (a,b), relator aaabABBAb; my own
Smith-normal-form of the abelianized relator matrix gives **H₁ = ℤ** (agrees
with snappy). Theorem check: G ↠ Q induces G^ab ↠ Q^ab, and every quotient of ℤ
is cyclic — so no quotient of a knot group has non-cyclic abelianization.
Concretely: homs π₁(m004) → ℤ₃×ℤ₃: 9 total, **0 surjective**. (Heisenberg
3^{1+2} is excluded a fortiori: a surjection onto it would compose to a
surjection onto its abelianization ℤ₃×ℤ₃.)

**Controls (exclusion claims must be shown findable when planted):**
- Hom instrument: surjections FOUND when they exist — A₄: **24**, D₅ (order 10):
  **20**, S₅: **240** surjective homs. So the 0 for ℤ₃×ℤ₃ is a real exclusion.
- Rank instrument: A2+A1 root set alone → rank 3; empty set → 0; all 72 → 6.
- Planted rank drop: the E6 diagram involution (an OUTER operation, i.e. exactly
  what a torus-element centralizer is not) has fixed torus of dim **4** — the
  instrument class can see rank 4 the moment the toral hypothesis is violated.

## Diff against the banked record

| banked | mine | verdict |
|---|---|---|
| B952 rank ledger: rank E6 = 6, SMT = 2+1+3 = 6, SM = 2+1+1 = 4, deficit 2, dim 14 vs 12 | identical (dim of A1+A2+u1³ centralizer = 14 recomputed) | **MATCH** |
| B952 theorem: centralizer of a (set of) semisimple/torus elements contains a maximal torus ⇒ rank-preserving ⇒ rank 4 unreachable by measurement | t ⊆ centralizer verified per element in the full scan; Borel's theorem instantiated concretely | **MATCH** |
| B955 scan: "every torus element of order ≤ 6 … every centralizer has rank 6, no exceptions" | reproduced in both conventions | **MATCH — with a VACUITY NOTE**: as instrumented, this clause could not have failed (the centralizer of a torus element contains the torus by construction, so rank ≥ 6 before any scan runs). The scan's non-vacuous content is the type table, the Borel–de Siebenthal recovery, and the example element — all reproduced. |
| B955: "su(3)⊕su(2)⊕u(1)³ appears in that table (e.g. N=6, x=(0,0,0,1,2,1))" | my blind ADJOINT scan found **the same minimal element (0,0,0,1,2,1) at n=6** before I had seen theirs. Convention note (E23, resolved): that element has order 6 only in the **adjoint** parameterization ("all 6-tuples" of root evaluations, which is what the panel scanned); in **simply-connected** E6 — the group named in B955's prose — its exact order is **18**, and A1+A2+u1³ first occurs at SC order 7. The prose "order ≤ 6 in simply-connected E6" and the example are therefore mutually inconsistent as stated, but the mathematical claim is convention-independent (rank stays 6 for every torus element of every order in either form), so nothing banked is wrong — the scan's "order" is adjoint order / evaluation denominator. | **MATCH with note** |
| B955: H₁(knot complement) = ℤ; every quotient of a knot group has cyclic abelianization; π₁(m004) can never surject onto ℤ₃×ℤ₃ or 3^{1+2} | H₁ = ℤ by my own SNF; theorem verified; 0/9 homs surjective | **MATCH** |
| B955: A₄, D₅, S₅ images of π₁(m004) exist | 24, 20, 240 surjective homs found by brute force | **MATCH** |

Out of scope for this cell (literature claims, not recomputable from committed
files): Keurentjes {6,2,0} for π₁ = ℤ³; the Q4/Acharya citer sweep; the Jordan
rank-1 27-VEV → SU(5) statement. None is load-bearing for the rank wall itself.

**Lock quality note:** `tests/test_b952_rank.py` and `tests/test_b955_l133scout.py`
are prose/JSON-echo locks — they assert that hand-entered numbers equal
themselves and that phrases appear in FINDINGS.md; neither re-runs any E6 or
knot computation. The panel's scan itself has no committed code ("certified
in-sandbox"); this cell now provides an independent committed implementation.

## VERDICT: **MATCH**

Every recomputable clause of B952(a) and B955(b) reproduces, including the
exact banked example element found blind. One clause carries a vacuity note
(rank-6-no-exceptions is tautological as instrumented), one a resolved
convention note (the scan's "order ≤ 6" is adjoint order; the banked example
has SC order 18). The rank wall stands: rank is 6 after every centralizer step
in either convention, and rank 4 is unreachable by measurement alone.
