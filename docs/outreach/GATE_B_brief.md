# Gate B — realizing `T[4₁; E₆]`, and the 28-survivor embedding question

**For:** a specialist in the 3d-3d correspondence / complex Chern–Simons and character varieties
(Dimofte / Garoufalidis class). **Status:** honest — the objects below are computed and exact; the
realization question is open and specialist-gated.

## Setup (self-contained)

`4₁` is the figure-eight knot complement, the once-punctured-torus bundle with monodromy
`[[2,1],[1,1]]`. Its SL(2,ℂ) geometry is standard; here the gauge group is the exceptional group
**E₆**, `𝔢₆` its Lie algebra (dim 78), `𝔣₄` its fixed subalgebra under the diagram involution θ
(dim 52), so `𝔢₆ = 𝔣₄ ⊕ 26`. The **27** is the minuscule fundamental representation. The
**Kostant exponents** of E₆ are `{1, 4, 5, 7, 8, 11}` (the degrees minus one; six of them = rank).
The **3d-3d correspondence** (Dimofte–Gaiotto–Gukov) assigns to a 3-manifold `M` and a gauge type
`G` a 3d theory `T[M; G]` built from a Neumann–Zagier-type gluing datum on the `G` character
variety; the state-integral construction is explicit for `SU(N)` and classical groups.

## What is computed (exact / high-precision, verified in-repo)

1. **The deformation space is 6-dimensional and uniform.** `dim H¹(π₁(4₁), 𝔢₆) = 6 = rank E₆` —
   exactly one deformation direction per Kostant exponent. The cup-product obstruction vanishes to
   second order in every direction, and (new) the escape sector `{4,8}` is **unobstructed through
   fourth order**: in each `{4,8}` direction the order-4 obstruction class sits ≥ 5 orders of
   magnitude below its own expansion-floor gates, matching an integrable control (the `m=1`
   A-polynomial curve) and far below the coboundary control's exact-tier floor. This is *evidence*
   of local smoothness (there is no formality theorem for knot groups at exceptional type), not
   proof. So `T[4₁; E₆]` would have a genuinely 6-dimensional local moduli to quantize.

2. **The manifold's involution induces θ on the tangent, canonically (a theorem).** The
   orientation-preserving (hyperelliptic) involution of `4₁` induces on `H¹(4₁, 𝔢₆)` exactly the
   diagram involution θ, which multiplies the exponent-`m` line by `(−1)^{m+1}`; the `−1`-eigenspace
   is the pair `{4, 8}`, i.e. the `𝔢₆/𝔣₄ = 26` coset. Two exact lemmas carry this: θ fixes the
   geometric representation pointwise (checked on all 78 chain basis vectors), and the sl₂-commutant
   of `Aut(𝔢₆)` is exactly `{1, θ}` (Smith normal form of the 46 bracket-coupling relations:
   invariant factors `(1,1,1,1,1,2)`, free rank 0) — so the tangent action is canonical, not a
   convention. This closes, at the tangent level, "the involution induces the E₆→F₄ folding."

3. **The character-level embedding search reduces to 28 explicit survivors.** A **chiral** embedding
   is a `2T ↪ E₆` (binary tetrahedral group into E₆) whose restriction to the 27 has *complex*
   character — the case not realized by any canonical embedding. Starting from the full window of
   faithful 27-dim assemblies with a nonzero cubic invariant and complex character (70262 chiral
   assemblies for 2T; every E₆ ingredient — root system, weight systems, and the decompositions
   `Sym²27`, `27⊗27̄`, `Sym³27` — derived in-probe with exact arithmetic), three provably necessary
   conditions were applied as a sieve: a cross-map condition (`V̄ ≼ Sym²V`), torsion realizability
   (each element of order `n` must map to a genuine order-`n` torsion point of simply-connected E₆),
   and adjoint fit (`78`, `650`, `Sym³` restrictions must be genuine characters, consistently at
   shared power classes). Attrition: **70262 → 28** (14 conjugate pairs; the torsion condition is
   the whole bite; the two realized canonical assemblies pass every layer — a direction-of-error
   control). For the A₄ subgroup the same sieve gives **1028 → 2**.

   These 28 are **candidates**: survival of the character-level necessary conditions is not
   realization, and none is excluded beyond the bound. Deciding whether any specific 27-dim assembly
   is an actual homomorphism needs an invariant-theoretic Hom-space computation beyond character
   level (nondegeneracy of the induced cubic + actual conjugacy — a Gröbner-scale computation, or a
   classification of finite subgroups of E₆). What is new is that this must now be asked of only
   **28 explicit objects**, listed in the source.

## The single question

> Does the Dimofte–Gaiotto–Gukov construction admit an exceptional-type state integral
> `T[4₁; E₆]` — even conjecturally — that quantizes the computed 6-dimensional Neumann–Zagier-type
> deformation datum; and, at the arithmetic level, does the invariant-theoretic Hom-space
> computation decide whether **any of the 28 explicit surviving 27-dim assemblies** is realized by
> an actual `2T ↪ E₆` homomorphism (rather than only surviving the character-level necessary
> conditions)?

## Honest scope

State-integral models are standard for `SU(N)`/classical groups; the exceptional case is not.
And — the one caveat the program requires us to state — even a full realization of `T[4₁; E₆]`
would **not** by itself extract numerical physical values from the single object: the program's
value-firewall is a proven property (every discrete invariant of the single seed is a Galois orbit
of its own arithmetic), so this is a mathematical realization question, not a route to physical
constants.

**Provenance.** Rests on B347 (the 6-dim tangent), B351 (the exact Chevalley `𝔢₆` and θ as a
verified automorphism), B352 (second-order integrability), B501 pieces (i)/(ii)/(iii) (the 28-survivor
reduction, order-4 integrability, and the canonical tangent-level θ-identification), with B329/B356
for the embedding/chirality framing; `docs/OPEN_PROBLEMS.md` Gate B. Nothing promotes to
`CLAIMS.md`.
