# B881 — descent stage 2: the SM-graded coset commutation table — 28 mediation channels, every one single-target, the 3-grading verified cell-by-cell

cc banking seat, 2026-08-04. The joint queue's stage 2, honestly scoped **before running**:
this is the mediation skeleton of the broken generators (B867's S1 coset — which X/Y-type
directions connect which matter multiplets), NOT the Yukawa skeleton proper (that lives in the
27 representation — the named follow-up). Mathematics scope; nothing to `CLAIMS.md`; Gate 5
untouched.

## 1. The gradings (all under the commuting charges z₁, y, y₂ at the first enhancement point)

- **W = e₆/K₁ (32)**: pieces [6,6,3,3,3,3,2,2,1,1,1,1] — the SM multiplets of 16 ⊕ 16̄
  (B876's grading, reproduced).
- **K₁ (46)**: pieces [14 | 6,6,6,6,3,3,1,1] — the **unbroken 14** (the SM Levi su(3)⊕su(2)⊕2u(1)
  plus z₁, all charges zero) and **32 broken directions** in eight charged multiplets.

## 2. The table

| channel class | count | target |
|---|---|---|
| each multiplet × its own conjugate | **6** | **the unbroken 14** — the gauge-covariance diagonal |
| cross-pairings (16-piece × 16̄-piece, charge-matched) | **22** | **exactly one broken multiplet each** — [1×3]→3, [1×6]→6, [2×3]→6, [2×6]→3, [3×3]→1, [3×6]→6, [6×3]→6, singlet-cross→broken-1 |
| same-z₁-sign pairs ([16,16] and [16̄,16̄]) | **42** | **0 — the 3-grading, verified on every cell** |
| mixed-sign, charge-mismatched | **8** | **0 — structurally forbidden** |

**Every one of the 28 nonzero cells is single-target** — charge conservation realized exactly,
no leakage at 30 digits in oblique coordinates.

## 3. The trap, for the third time — now a standing rule

The first run reported *every* cell hitting *all nine* targets: the K₁-piece eigenvectors are
complex and **non-orthogonal** (the grading operator restricted to K₁ is non-Hermitian), so
transpose-projections do not discriminate. Same failure class as B875's nearly-parallel sectors
and B876's ill-posed per-sector grading. **Standing rule, earned three times: every
decomposition readout in this program must be oblique (solve in the full eigenbasis), never a
projection, unless the basis is provably orthonormal.**

## 4. What this feeds

- **B867's S1**: the X/Y-mediation channels are now an explicit table — which broken direction
  connects which matter pair is no longer qualitative.
- **G8 (Higgs × generations), partially**: the broken-singlet channels ([3×3]→1 and the
  singlet-cross cells) mark where invariant directions meet matter pairs at the algebra level;
  the Higgs question proper needs the 27.
- **The 27 representation on this Chevalley base** is now the single most valuable missing
  instrument (Yukawa skeleton, the E-clause upgrade, DVT-comparison) — named follow-up.

`tests/test_b881_coset_table.py`
