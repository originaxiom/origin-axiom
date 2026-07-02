# B352 — the cup-product obstruction, computed: all six directions unobstructed at second order (conditional)

**Status: banked (frontier) as a computer-assisted (mpmath dps 100) result — part 2 of the
`{4,8}`-integrability program, answering the B265/B270 open item at second order. Firewalled;
nothing to `CLAIMS.md`; no physics claim.**

## The question and the answer
B265 showed the θ-odd tangent directions `m ∈ {4,8}` of the figure-eight's E₆ character variety
(the `𝔢₆/𝔣₄ = 26` "escape" sector, E₆-Zariski-dense) exist at first order; B270 left open whether
the second-order obstruction `[z ∪ z] ∈ H²(π₁(4₁), 𝔢₆)` kills them. **Answer: no.** The
obstruction class vanishes for the escape directions, for their mix, and in fact for **all six
exponent directions** — while the raw second-order cochains are enormous (`‖q‖` up to `9.4e16`),
so the vanishing is *exactness* (a second-order deformation `z₂` exists), not triviality.

## The numbers (dps 100; classes = |⟨u_m, q⟩| per exponent block; run: 741 s)
| direction | largest class component | q-cochain norm | verdict |
|---|---|---|---|
| control: coboundary | `4.6e-74` | `6.7e-10` | zero ✓ (gauge invariance) |
| control: `m=1` (the real curve) | `2.4e-62` | `1.8e+01` | zero ✓ (the A-poly curve integrates) |
| `m=4` (escape) | `4.2e-62` | `2.1e+09` | **unobstructed** |
| `m=8` (escape) | `4.3e-57` | `9.4e+16` | **unobstructed** |
| `m=4 + m=8` (mix; polarization) | `2.1e-57` | `4.6e+16` | **unobstructed** |
| `m=5, 7, 11` (F₄ directions) | `≤ 1.1e-59` | up to `1.0e+16` | **unobstructed** |

Machinery integrity: relator identity `X(rel) = I` to `9.0e-54`; `X` preserves the **exact**
B351 bracket to `5.3e-71`; first-order (cocycle) residuals `≤ 2.6e-51`; `ad`-solve residuals
`≤ 3.5e-56`. **MB12 positive control:** the H² pairing functionals give `0.10–0.36` on random
vectors — the zeros are information, not a degenerate pairing. **θ-parity signature:** in every
row the `{4,8}`-block components sit 5–10 orders *below* the F₄-block components — the
exact-zero-forced-by-θ (B351's grading: `[z∪z]` is θ-even) versus the numerical floor.

## Architecture (what it took — two honest failures on the way)
1. **Double precision is structurally insufficient**: the `Sym^{2m}` blocks of `Ad ρ` span
   `e^{±2mμ}` ≈ 20 orders of magnitude at `m=11`; a numpy build produced relator residual
   `1e+49`. 2. **Euclidean normalization is not invariant**: transporting the bracket into the
   normalized chain basis gave structure constants spanning `1e-6..1e+73` and a singular Gram.
   The working design: **two bases** — brackets/ad/Gram in the B351 **root basis** (integer
   structure constants; the Gram is exact integers), the group action **block-diagonal in chain
   coordinates** (antidiagonal closed-form intertwiners to B347's symrep basis — no inversions),
   and only *vectors* crossing through `S` at dps 100. The obstruction is extracted by expanding
   `∏ exp(t·ad z(s)) X(s)` over the relator to `t²`: the `t`-coefficient vanishes (cocycle), so
   the `t²`-coefficient lies in the tangent space `ad(𝔢₆)` (a curve in `Aut(𝔢₆)` with vanishing
   first derivative), and `q` is recovered by the exact-Gram normal equations. Rank decisions
   use **structural rank + cliff assertions** (the genuine singular values themselves span ~25
   orders before a >60-order cliff to the true null — a fixed threshold misclassifies; the
   MB13-§4 lesson applied to spectra).

## The honest reading (tiered)
- **Computed:** the quadratic cone of the E₆ character variety at the principal-geometric point
  is the full 6-dim tangent — no second-order obstruction in any direction (and none in the
  `{4,8}` polarization cross-term).
- **Literature anchor (which tier this lands in):** for `SL(n)`, Menal-Ferrer–Porti proved the
  character variety of a cusped hyperbolic 3-manifold is a **smooth** (n−1)-dim manifold at the
  (composed) holonomy. Our computation is the *exceptional-type analogue evaluated concretely*:
  the result is exactly what an "MFP-smoothness at E₆" theorem would predict, and constitutes
  numerical evidence *for* such a theorem — it is **not** a surprise landing, and it is not a
  proof of smoothness.
- **NOT established:** integrability to all orders (third-and-higher obstructions untested; no
  Goldman–Millson formality is available for knot groups); exactness of the numbers (dps-100
  margins of 50+ orders, but numerical); anything at points other than the principal-geometric
  one.
- **Consequence for the CRUX (gate B):** the escape sector is locally *real* — E₆-Zariski-dense
  deformations of the figure-eight's holonomy exist at least to second order. The `T[4₁;E₆]`
  realization question inherits a genuinely 6-dimensional local moduli, strengthening the case
  that the exceptional-type state integral has something to quantize. No value crosses the
  firewall: dimensions and vanishing classes are *form*, per K020.

## The fence
mpmath dps 100 (self-guarded per MB13 §4; no global state leaked); exact integer structure
constants and Gram from B351; exact chain skeleton with closed-form sl₂ action; the geometric
rep from B347 (`‖ρ(rel)−I‖ ~ 1e-60`). `cup_product.py` (reproducer:
`python frontier/B352_cup_product_obstruction/cup_product.py`, ~12 min) ·
`tests/test_b352_cup_product_obstruction.py` (fast structural tier always-on; the full sweep
gated behind `OA_SLOW=1`). Related: **B351** (the exact 𝔢₆ + θ), **B347** (the tangent),
**B265/B270** (the question), **B264** (the E₆ character variety), **OPEN_PROBLEMS** gate B.
Lit: Menal-Ferrer–Porti (*Twisted cohomology of hyperbolic 3-manifolds*; *Local coordinates for
SL(n,C)-character varieties*); Goldman (the symplectic nature / cup-product obstruction);
Nijenhuis–Richardson (deformation obstruction theory).
