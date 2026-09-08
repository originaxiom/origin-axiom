# B1350 — THE V₁₀ DIRECTION: the one deformation of the cusped object's E₆ holonomy that B1280's pairing law does not cover — the V₁₀ inside the 42 at the subregular point (θ = −1, ι* = +1; L207, main's L204) — computed: the exact part is in (both classes carry the cusp, the class space has no cusp-trivial direction, both are trace-flat at first order); the finite deformations and N(27) are running

**Date:** 2026-09-08 · **Seat:** cc (the SM-derivation branch) · **Status:** OPEN (stages 0–3 PROVED: exact; stage 4 running at the time of this record) · **Price: unchanged** · **Numbering:** B1350, the first of the range this branch now numbers from (the collision note in `docs/SM_SEAT_ALIAS_TABLE.md`).

## Why this arc — the last unpaired direction

B1280 proved that the inversion of m004 acts on the six deformation classes of the E₆ holonomy at the geometric
(principal) point by θ's signs, so every flat-sector deformation there is symmetry-paired and N(27) ≡ 0 on the germ.
Its mod-4 criterion then found that at the other even sl₂ point, the subregular E₆(a₁) — e₆ = V₂⊕V₄⊕V₆⊕V₈⊕V₁₀⊕V₁₀⊕V₁₄⊕V₁₆,
27 = 13 ⊕ 9 ⊕ 5, the outer involution fixing sp(8) = V₂⊕V₆⊕V₁₀⊕V₁₄ and negating the 42 = V₄⊕V₈⊕V₁₀⊕V₁₆ — seven of the
eight tangent directions agree and exactly one does not: **the V₁₀ of the 42**, where θ = −1 but the inversion acts by
(−1)^{10/2+1} = +1. Main's B1299 verified the hole exactly and priced the computation at about a day with a prior of 15 %
for a non-zero net count. This arc does it with B1268's machinery: exact cocycles, Newton to genuine E₆ representations
at 400 bits, twisted cohomology of the 27 and the 27̄ at 60 digits, and B1268's bound −h⁰(∂M; V) ≤ N ≤ h⁰(∂M; V*), which
says a non-zero N needs a cusp-fixed vector at the deformed point.

## 1. The point ((0), (1), exact)

The subregular triple (weighted Dynkin (2,2,2,0,2,2); B1267's instrument) grades e₆ so that the kernel of ad e on each
weight space gives the block multiplicities {2: 1, 4: 1, 6: 1, 8: 1, 10: **2**, 12: 0, 14: 1, 16: 1} — the two V₁₀'s.
ρ₀ = (exp e, exp u f) on the 27 (u the Riley root) is an exact representation of π₁(m004) over ℚ(ω) with

| | h⁰(M) | h¹(M) | h⁰(∂M) | h¹(∂M) | rank(res) | N |
|---|---|---|---|---|---|---|
| 27 at ρ₀ | 0 | 3 | 3 | 6 | 3 | 0 |
| 27̄ at ρ₀ | 0 | 3 | 3 | 6 | 3 | 0 |

(the 3 = one class per block of 27 = V₁₂ ⊕ V₈ ⊕ V₄, exact and at 60 digits alike).

## 2. The two V₁₀ classes and the cusp ((2), exact over ℚ(ω))

For each V₁₀ block (basis ad(f)^k hv, k = 0 … 10) the Fox complex of the block representation gives dim Z¹ = 12,
dim B¹ = 11, **h¹ = 1**: one class per block, two in the isotype. Their restriction to the cusp torus ⟨μ, λ⟩:
**neither class alone is cusp-trivial**, and on the two-dimensional class space the restriction map to H¹(∂M; e₆) has rank
**2** — there is no cusp-trivial combination: every deformation in the V₁₀ isotype moves the cusp holonomy, so by B1268's bound a non-zero N at the deformed point needs the cusp holonomy to keep a fixed vector, which is what stage 4 measures (h⁰(∂M) at ε ≠ 0).

## 3. First-order trace-flatness ((3))

The first-order self-duality defect d/dε [tr ρ_ε(w) − tr ρ_ε(w⁻¹)] along either class vanishes identically on six test
words (to 10⁻¹⁵⁷ in ball arithmetic): both V₁₀ classes are **trace-flat at first order**, so the θ-parity of the class
space cannot be read from first-order character variations (the same was true, implicitly, of B1268's V₈ direction, which
broke self-duality only at finite ε). The parity is read from the finite deformations of §4.

## 4. The deformations and N(27) ((4), 400-bit Newton, 60-digit ranks)

*(pending: the Newton stage is running; its record replaces this line)*



## 5. What this settles

*(pending stage 4)* The exact part already narrows the hole: the unpaired direction is not cusp-trivial, so if N ≠ 0 anywhere along it, it is because the deformed cusp holonomy retains a fixed vector — the fixed-vector locus of B1268 (b), not the generic point.

## Controls (MB12)

- **The point** reproduces B1280's data (h¹ = 3 = 3 at the subregular point, N = 0) exactly and numerically.
- **The classes** are exact (ℚ(ω)), non-coboundary by an exact rank test, and their block h¹ = 1 matches B1280's
  one-dimensional H¹(m004; Sym¹⁰).
- **The cusp restriction** is computed exactly in the block and in the full e₆ (78 coordinates, exact Ad exponentials).
- **B1268's machinery unchanged** (imported, not copied): the Newton search, the cohomology report, the dual.
- **E70-class:** the cocycle values use the left-module Fox convention throughout (B1267's Rep.fox), the adjoint Fox
  operator of B1268 for the first-order derivative.

## Verification

- `verification/v10_direction.py` (stages 0 … 4; `v10_direction_run.txt`; the exact stages alone in
  `v10_direction_stage0123_run.txt`).
- Lock `tests/test_b1350_the_v10_direction.py`: fast — stages 0 … 3 (multiplicities, the point, the two classes and
  their cusp restriction, trace-flatness); slow — stage 4.
- Depends on B1280 (the criterion and the hole), B1268 (the bound and the machinery), B1267 (the instrument), main's
  B1299 (the hole verified and priced).
