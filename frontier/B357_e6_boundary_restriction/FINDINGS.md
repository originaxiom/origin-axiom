# B357 — the E₆ boundary restriction: rank 6/6, the Lagrangian certified, and the universal-τ identity

**Status: banked (frontier). Campaign W1.3 — the classical-structure deliverable for Gate B. Computer-assisted
(mpmath dps 60, residuals at per-block precision floors). Firewalled; nothing to `CLAIMS.md`; no physics claim.**

## The setup

`M` = the figure-eight complement; the cusp torus has `π₁(T²) = ⟨µ, λ⟩` with `µ = ABB`, `λ = BAbabABa` in the
SnapPy presentation `⟨a,b | abbbaBAAB⟩` (gated in-module: commuting, both parabolic `tr = −2`). At the
principal-composed geometric representation the peripheral holonomy is **regular unipotent**, so per exponent
block: `H⁰(T², Sym^{2m}) = 1`, `H¹(T², Sym^{2m}) = 2`, and the full boundary space `H¹(T², 𝔢₆)` is
**12-dimensional**, block-diagonal over the six exponents, symplectic via cup ⊗ the invariant pairing.

## Results

**1. `rank(r) = 6/6` — no peripherally-invisible deformations.** Each of B347's six `H¹(M, Sym^{2m})` classes
restricts to a **nonzero** class in the 2-dim boundary block (class residuals `1.5e-60 … 1.1e-27`, the floor
per block size). This was the genuinely open question.

**2. The Lagrangian certificate.** With rank 6 the image is 6-dim = half of 12; the Killing form pairs
Sym-blocks diagonally (block-orthogonality), and each block-image is a line in a 2-dim symplectic plane —
isotropic automatically. So the image of `H¹(M,𝔢₆) → H¹(T²,𝔢₆)` is **Lagrangian** — half-lives-half-dies made
concrete at exceptional type; the classical integration cycle a `T[4₁;E₆]` state integral would use.

**3. The universal-τ identity (the sharp new fact).** On **every** cocycle `(u,v) ∈ Z¹(T², Sym^{2m})`, the
leading Neumann–Zagier functionals satisfy
`K(v, h) = τ · K(u, h)` with **one constant** `τ = −2√3·i` — the figure-eight **cusp shape** (SnapPy control
matched to 12 digits; the sign is the orientation convention) — **uniformly in `m`** (cross-block deviation
`≤ 1.3e-52`). Mechanism: at the complete structure `U = exp(N̂)`, `V = exp(τN̂)` share one nilpotent direction,
and `K(·,h)` kills both `im N̂` and `ker N̂`. **Consequence: the leading peripheral (NZ) datum does *not* split
by exponent — there are no "higher cusp shapes" at first order; the E₆ boundary sees the same τ as SL(2).**
(The exponent-dependence of the boundary data begins strictly beyond the leading functional.)

**4. Controls (MB12).** The symplectic form (bar-resolution 2-cycle `[µ|λ]−[λ|µ]`, invariant pairing
`K(e_i,e_j) = δ_{i+j,d}(−1)^i/C(d,i)`, invariance gated ≤ `1e-39`) is **nondegenerate on the honest orthonormal
`H¹` basis in every block** (dets nonzero; antisymmetry at floor `≤ 1e-55`), and `φ_µ = K(z(µ),h) ≠ 0` in every
block — each deformation "opens the cusp" at leading order. *Development note (the controls working): a first
basis choice (the two invariant-line cocycles) was ω-degenerate and mis-spanned `H¹` — caught by exactly these
gates (class residual 0.23, ω ≈ 1e-123) and replaced by the honest `Z¹/B¹` orthonormal complement.*

## Honest tiers and scope

- Numerics at dps 60; every claim carries its residual; the τ-identity is *numerically exact* per block and its
  mechanism (the shared-nilpotent argument) is stated but not formalized as a proof — the natural follow-up.
- Not claimed: the NZ-type Gram against a canonical complementary Lagrangian (the leading functional's
  1-dimensionality — the τ-identity — shows the naive two-functional coordinates have rank 1, so a canonical
  second coordinate needs the depth-2 Jordan functional; scoped as the follow-up), any physics.

**Provenance.** Campaign W1.3 (`docs/OPEN_LEADS.md`); machinery: B347 (`symrep`, per-block Fox cohomology,
`_zeval`), B321 (cusp shape `2√3·i`), B293 (peripheral conventions). Reproducer: `boundary_restriction.py`;
test: `tests/test_b357_e6_boundary_restriction.py`.
