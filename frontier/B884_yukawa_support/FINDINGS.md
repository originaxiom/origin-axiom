# B884 — the invariant cubic on the 27 (45 monomials, all ±1, unique) and the SM-graded Yukawa-support table: 11 coupled cells, 275 exact zeros — the E₆ classic, refined

cc banking seat, 2026-08-04. The first product of the B883 instrument. Mathematics scope;
nothing to `CLAIMS.md`; Gate 5 untouched — **structure only: which couplings the algebra
allows; magnitudes are NOT claimed** (see §4).

## 1. The cubic, exact

The unique e₆-invariant in Sym³(27), solved over ℚ from the invariance equations on the weight
basis: **45 weight-zero triples, support 45/45, every coefficient ±1, nullspace dimension
exactly 1**. This is the J₃(𝕆) determinant in the B854 Chevalley frame — unit structure
constants, inherited not chosen.

## 2. The grading (enhancement point; charges s₁, y, y₂ at 30+ digits)

27 → pieces **[1 | 3,3,2,2 | 6,3,3,2,1,1]** — the singlet, the so(10)-vector 10 as
(3,1)⊕(3̄,1)⊕(1,2)⊕(1,2) (the Higgs-doublet/triplet block), and the 16's SM multiplets.
(A first pass with float64-truncated charges corrupted the readout — the µ-term-shaped cells
vanished; full-precision charges recovered them. The scale-calibration control and gap
classification below are the permanent fix.)

## 3. The support table

- **Calibration control**: the cubic on random dense unit vectors evaluates 0.017–0.18 — the
  natural scale.
- **Gap classification**: the 286 cell-maxima split at a **7.7-order gap** — 11 coupled cells,
  275 zeros (≤ 10⁻¹⁶, numerical zero at eigenvector precision).
- **The 11 cells account exactly for the classic 27³ ⊃ 16·16·10 ⊕ 1·10·10, SM-refined**:
  the two [2,3,6] up/down-Yukawa shapes, three lepton/µ-term-shaped cells ([1,2,2], [2,2,1]×2),
  the [3,3,3] u^c–d^c–triplet cell, the [3,6,6] qq-triplet cell, two [3,3,1] and one [1,3,3]
  singlet–triplet cells. Charge sums ≤ 10⁻²¹ on every coupled cell.

## 4. Honest boundaries

- **Only the zero/nonzero support is basis-invariant.** The magnitude hierarchy inside the
  coupled class depends on intra-piece basis and sampling — reported in `results.json`, not
  claimed. No values, no textures, no Gate-5 contact.
- The support is numeric (30 digits, 7.7-order gap); the cubic itself is exact. An exact
  support proof (per-cell symbolic vanishing) is priced follow-up.
- The grading charge y₂ is the imposed fused-chain Levi (B876's convention), at one root;
  Galois carries the pattern to the other two.

`tests/test_b884_yukawa.py`

## Addendum (2026-08-04, masterplan W2) — the support is PURELY charge-forced: no dynamical zeros

Counting charge-conserving unordered triples among the 286 cells: **exactly 11 — and they are
the 11 coupled cells.** Both directions hold: every charge-conserving cell couples (the cubic
has no accidental zeros on allowed cells), and every zero cell violates charge conservation
(the 275 zeros are conservation-forced, not dynamical). The support table's shape is therefore
exactly as rigid as the charge assignment itself. Residual exactness note: upgrading the 11
nonvanishing verdicts from sampled-at-scale to symbolic requires exact graded bases over the
splitting fields (B886's machinery makes this reachable) — priced, low priority now that the
pattern is decided.
