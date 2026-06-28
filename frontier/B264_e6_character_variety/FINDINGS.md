# B264 — the E₆ character variety of the figure-eight: tangent dimension = rank, with directions beyond F₄

**Status: banked observation (frontier). FIREWALLED — geometry / rep theory of flat connections, NOT physics.
Nothing to `CLAIMS.md`.** Addresses chat-1's insight via the decisive existence sub-step. `e6_charvar_tangent.py`
(pyenv, mpmath; self-contained — exact Riley rep, no SnapPy at runtime).

## The question (chat-1, sharpened)
The right object for the type-E₆ 3d-3d theory is the **E₆ character variety** of `π₁(4₁)` (flat E₆ connections),
*not* the geometric `SL(2,ℂ)` holonomy. Decisive sub-step: does `π₁(4₁)` have E₆ deformations **beyond** the named
`SL(2)`-composed ones, or is the variety just the pieces we already understand (B71/B89)?

## Method (rigorous, characteristic 0)
Under the principal `sl(2)→e₆`, the adjoint decomposes by the **exponents of E₆**:
`e₆ = ⊕_{m∈{1,4,5,7,8,11}} Sym^{2m}(V₂)`. So the tangent space to the E₆ character variety at the
principal-composed geometric rep is `H¹(π₁, Ad ρ_prin) = ⊕_m H¹(π₁(4₁), Sym^{2m}(ρ_geo))`. Each summand is computed
**exactly** by Fox calculus on the canonical presentation `⟨a,b | aWb⁻¹W⁻¹⟩`, `W=ba⁻¹b⁻¹a`.

Inputs verified in-script: the relator `abABaBAbaB` has Alexander polynomial `x²−3x+1` (**the figure-eight**); the
exact Riley rep (`a=[[1,1],[0,1]]`, `b=[[1,0],[t,1]]`, `t=e^{iπ/3}`, `t²−t+1=0`) satisfies it; `Sym` is verified a
homomorphism.

> **A debugging note (verify-don't-trust, kept honest):** the first passes were wrong — double precision corrupts
> high `Sym` powers, mod-`p` ≠ char-0 cohomology, and a `Sym` convolution had `x,y` coefficients swapped. Each was
> caught against a known anchor (`dim H¹(Sym²)=1`, Thurston) before trusting the result. Three independent
> validations now agree.

## Result
`dim H¹(π₁(4₁), Sym^{2k}(ρ_geo)) = 1` for **all** `k=1..11` — matching **Menal-Ferrer–Porti** (`= #cusps = 1`,
all `k`) and **Thurston** (`Sym²=1`). Therefore:

> **`dim H¹(π₁, Ad ρ_prin) = 6 = rank(E₆)`.**

The E₆ character variety has a component of dimension **= rank** through the principal rep — **strictly larger** than
the 1-dimensional `SL(2)`-composed family (the figure-eight A-polynomial curve, the exponent-1 direction). The
deformation directions are graded by the exponents `{1,4,5,7,8,11}`; the directions **`{4,8}`** are E₆-exponents
**not** in F₄ (`{1,5,7,11}`) — they deform the rep **out of F₄**, the maximal subgroup containing the principal
`SL(2)`.

## Verdict — and the honest guardrails
**Yes:** `π₁(4₁)` has genuine E₆ deformations beyond the named `SL(2)`-composed / F₄ reps (at the infinitesimal
level). chat-1 is right that the E₆ character variety is rich. Guardrails (verify-don't-trust):
1. This is the **tangent space** (infinitesimal); integrability + Zariski-density of the *generic* deformation is the
   next step (the obstruction `H²` / the quadratic cone).
2. **Richness ≠ SM physics.** The input-E₆ (chosen 6d type) vs output-McKay-E₆ (trace field) selection remains a
   conjecture, and the 4d-lift / chirality / scale walls (B259) are untouched.
3. **Consistent with our SL(n) ladder:** `dim = rank` holds — `SL(2)→1` (A-poly curve), `SL(3)→2` (B71), … ,
   `E₆→6`. The exceptional case `E₆` (no trace-map machinery) is the new frontier; this probe establishes its
   tangent dimension.

Anchors: B71 (SL(3) char variety, dim 2), B89 (SL(4)), B260 (Coulomb branch = char variety), B259 (the wall map),
B247 (the holonomy theorem). Lit: Menal-Ferrer–Porti 2012 (twisted cohomology, hyperbolic 3-manifolds); Thurston
(deformation `H¹(ad)=1`); Kostant (principal `sl(2)`, exponents); Dimofte–Gaiotto–Gukov (3d-3d, type G).
