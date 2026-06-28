# B275 — an explicit E₆-irreducible flat connection on the figure-eight (a concrete witness for B274/B265)

**Status: banked observation (frontier). FIREWALLED — an explicit flat connection, NOT physics. Nothing to
`CLAIMS.md`.** An explicit *numerical* witness illustrating B274's rigorous existence. `b275_witness.py` (sage,
ComplexField 240) + `b275_verdict.py` (pyenv).

## What this adds
B274 **proves** `ρ_prin` is a smooth point ⇒ E₆-irreducible flat connections exist unconditionally. B275 **exhibits
one**: an explicit `(A,B)` in E₆ (built in the 78-dim adjoint) solving the figure-eight relator `R(A,B)=I` with a
**nonzero `{4,8}` (E₆∖F₄) component** — hence E₆-Zariski-dense by B265's subalgebra computation, and genuinely off
`ρ_prin` / off the principal SL(2).

## Construction (and why it's delicate)
- **Balanced principal triple** `e'=Σ√cᵢ eᵢ, f'=Σ√cᵢ fᵢ` (same `h`; a conjugate rep, same character variety) so the
  adjoint `exp` entries are `O(10³)` not `O(10¹⁵)`. **High precision (ComplexField 240) is mandatory:** the relator
  is a product of 10 large-norm unipotents that cancel to `I`; in double precision the product blows up to `~10³⁶`
  and cancellation destroys it (verified: double-precision relator residual `~10⁴`).
- **Seed** `= s·(exp-4 H¹ cocycle)`, `s=0.03` (the genuine `H¹` generator from the `W₄` restriction, not a
  coboundary). **True Newton** (Jacobian rebuilt each step) with a ridge-regularized solve for the rank-deficient
  cocycle Jacobian; the exp-4 coordinate is **pinned** to `s` each step — without the pin, the min-norm step
  collapses the (integrable) exp-4 deformation back to `ρ_prin` (observed: exp-4 → exactly 0).

## Result
An explicit `(A,B)` with relator residual `|R−I| ≈ 7.9×10⁻⁸` and a **nonzero exp-4 component `≈ 5.6×10⁻⁵`** (vs
exactly `0` when the deformation collapses) — a genuine flat E₆ connection off `ρ_prin`, E₆-dense by B265. The
residual floor (`~10⁻⁸`) is set by the double-precision recover preconditioner.

## Honest scope
This is an explicit **numerical** witness (relator satisfied to ~8 digits) **illustrating** the rigorous existence —
**B274 is the proof** (smooth point, all orders), **B265** gives the density (exp-4 ≠ 0 ⇒ E₆-dense). B275 makes
"exist" concrete. Sharpening to a higher-precision or exact witness would require a high-precision recover (the
trace-form inverse at full precision) — not pursued, as existence is already settled by B274.

Anchors: B274 (smoothness/existence), B265 (density), B273 (the cocycle/obstruction machinery), B271 (the exponent
modules). Lit: Goldman (character-variety deformations); the Newton/Burnside pattern from `sln_toolkit` (B153).
