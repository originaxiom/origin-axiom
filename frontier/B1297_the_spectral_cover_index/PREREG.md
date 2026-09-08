# B1297 — PRE-REGISTRATION (written before any evaluation): the 3-manifold spectral-cover index

*MASTERPLAN v3 Phase 3 (D2). Verification rule 4: "the 3-manifold spectral-cover index is written as
a formula with a stated domain BEFORE it is evaluated (pre-registered; can pass and fail), then evaluated."*
*Drafted 2026-09-07 while B1296's suite runs; sealed by sha256 before the evaluation script is run.*

## 1. What PW §3.1's configurations ARE on a 3-manifold

On Q₃ the twisted 7d SYM's BPS equations are `F_A − φ∧φ = 0, d_A φ = 0, d_A ⋆φ = 0`: a flat
G_ℂ-connection `𝒜 = A + iφ` with the harmonic-metric (moment-map) condition, i.e. a REDUCTIVE
representation `ρ: π₁(Q₃) → G_ℂ` (Corlette–Donaldson). A "spectral cover" is a configuration whose
Higgs eigen-decomposition is single-valued only on a finite cover `C → Q₃`; its 4d chiral matter in a
representation `R` is the twisted cohomology `H¹(Q₃; R_ρ)`. For `E₆ ⊃ SL(3)³ ⋊ ℤ/3` (the trinification
block structure, the ℤ/3 permuting the three blocks of `27 = (3,3̄,1)⊕(1,3,3̄)⊕(3̄,1,3)` — to be
EXHIBITED on the weights, §5(a)) and `C` = the ℤ/3 descent of m004 (B298/B326's 3-fold cyclic cover,
`H₁ = ℤ ⊕ (ℤ/4)²`, one cusp):

    ρ = Ind_{π₁C}^{π₁M} ρ₁ ,   ρ₁ : π₁(C) → SL(3,ℂ),   ρ|_{π₁C} = (ρ₁, ρ₁^τ, ρ₁^{τ²})   (τ = deck)
    27_ρ ≅ Ind_{π₁C}^{π₁M} ( ρ₁ ⊗ (ρ₁^τ)* )                                       (block structure)
    H^k(M; 27_ρ) ≅ H^k(C; ρ₁ ⊗ (ρ₁^τ)*),  and the same on the cusp torus            (Shapiro; C one-cusped)

So the non-abelian E₆ configuration on m004 IS the bifundamental on the cover, and every index below
transfers verbatim: **I(M; 27_ρ) = I(C; ρ₁ ⊗ (ρ₁^τ)*)**.

## 2. The index — derived, with its domain

Let `M` be a compact oriented 3-manifold with boundary a torus `T` (the cusp), `V` a local system,
`V*` its dual. Notation: `a_k = h^k(M;V)`, `c_k = h^k(M,T;V)`, `t_k = h^k(T;V)`, starred for `V*`;
`r₁ = rank(H¹(M;V) → H¹(T;V))`. Inputs used: the long exact sequence of the pair; Lefschetz–Poincaré
duality `a_k = c*_{3−k}`, `t_k = t*_{2−k}`; `χ(M;V) = 0` (open 3-manifold: `a₀ − a₁ + a₂ = 0`, `a₃ = 0`);
`χ(T) = 0`; and the annihilator property `r₁ + r*₁ = t₁` (the images of `H¹(M;V)` and `H¹(M;V*)`
in the dual spaces `H¹(T;V)`, `H¹(T;V*)` are mutual annihilators — the coefficient-dual form of
"half lives, half dies").

**The chiral count.** `n(V) := dim im( H¹(M,T;V) → H¹(M;V) ) = a₁ − r₁` — the interior classes
(= the L² cohomology of the cusped hyperbolic manifold in degree 1, Zucker's theorem for the middle
degree; normalisable 4d zero modes). The **index** is

    I(M;V) := n(V) − n(V*)
            = (a₀ − a*₀) + t*₀ − r₁                                              (exact, always)
            = ½ (a₀ − a*₀)·2 + ½(t*₀ − t₀) + ½(r*₁ − r₁)                          (symmetrised)

Also, for comparison, the full count `F(M;V) := a₁ − a*₁ = (a₀ − a*₀) + r₁ − t₀` and the compactly
supported count `Cc(M;V) := c₁ − c*₁ = I + (t₀ − t*₀) − (a₀ − a*₀)`.

**Domain D** (where the three counts collapse to one number up to sign): (i) `ρ` reductive, so
`a₀ = a*₀` (semisimple module: `dim V^ρ = dim (V*)^ρ`); (ii) the cusp holonomy is a rank-2 lattice
in a ONE-parameter unipotent subgroup times finite-order scalars, so `t₀ = t*₀` (`dim ker N = dim coker N`
for a single nilpotent `N`). In D:

    I = t₀ − r₁ = r*₁ − t₀ ,   F = −I ,   Cc = I .

**Consequences (theorems inside D, each a CHECK the code must reproduce):**
 (T1) antisymmetry: `I(V*) = −I(V)`;
 (T2) closed M (no T): `I = 0` — B1260 §1 generalised from irreducible to semisimple;
 (T3) `V ≅ V*` (self-dual): `r₁ = r*₁ = t₁/2 = t₀` ⇒ `I = 0` — the Lagrangian property; covers
      E65 (`Sym^n` of SL(2)) and every θ-symmetric E₆ configuration;
 (T4) rank-1 `V` (abelian sector) on any knot-like M: `F = 0` by Alexander reciprocity (B1260 §2),
      hence `I = 0` in D — and by Shapiro every configuration ABELIAN ON THE COVER is vector-like;
 (T5) `t₀ = 0` ⇒ `t₁ = 0` ⇒ `r₁ = 0` ⇒ `I = 0`: only local systems with cusp-invariant vectors can be
      chiral; (T6) `I(V∘f) = I(V)` for every diffeomorphism `f` of M (the count is orientation-free);
      combined with complex conjugation, orientation-reversing `f` with `V∘f ≅ V̄` flips the sign of
      the index of `V ⊗ λ` as a function of the twist: `J(λ∘σ) = −J(λ)`.

So on a one-cusped manifold **the whole chirality lives in the boundary map**: `I = t₀ − r₁` is the
failure of "half lives, half dies" for a NON-self-dual local system with cusp invariants. This is the
cohomological form of fc R69's "the cusp keeps the endpoints", and it says exactly when the closed
wall (B1260) and the singular-frame ±2 (B1296) are evaded: never by the object's self-dual local
systems, never on a closing, only through a non-self-dual twist that is TRIVIAL ON THE CUSP.

## 3. The configuration on the descent — why the (ℤ/4)² can enter and how

The trinification factors are `SL(3)`, not `GL(3)`: the 27's cubic form forces every scalar twist to
be a cube root of unity, and `H₁(C) = ℤ ⊕ (ℤ/4)²` has NO order-3 torsion characters — the cubic
characters live on the deck-invariant free generator and give `ψ = κ/κ^τ = 1`. So the family
characters cannot enter as determinant twists. They enter through the (2+1)-reducible SL(3)
configurations on the cover:

    ρ₁ = ( ρ_geo|_{π₁C} ⊗ κ ) ⊕ κ⁻² ,   κ ∈ Hom(H₁(C), μ₄) a family character   (det = κ²·κ⁻² = 1 ✓)

Non-extending to π₁(M) whenever `κ^τ ≠ κ` (the deck action on `(ℤ/4)²` is Φ₃, fixed-point-free on
non-zero elements — B326). The bifundamental decomposes (ρ_geo self-dual, ρ_geo⊗ρ_geo = Sym² ⊕ 1):

    ρ₁ ⊗ (ρ₁^τ)* = Sym²(ρ_geo) ⊗ ψ  ⊕  ψ  ⊕  ρ_geo ⊗ κκ^{2τ}  ⊕  ρ_geo ⊗ κ⁻²κ⁻^τ  ⊕  κ^{2τ}κ⁻² ,   ψ := κ/κ^τ

Characters contribute 0 (T4). The two rank-2 summands have `t₀ = 0` because the lifted longitude has
trace −2 in every SL(2)-lift and is null-homologous in C, so (T5) they contribute 0. Hence

    **I(M; 27_ρ) = I(C; Sym²(ρ_geo|_{π₁C}) ⊗ ψ)** ,   ψ ranging over Hom(H₁(C), μ₄) via κ ↦ κ/κ^τ.

Since `κ ↦ κ/κ^τ = κ∘(1 − τ)` and `1 − τ` is invertible on `(ℤ/4)²` (det = Φ₃(1) = 3, a unit mod 4),
ψ ranges over ALL 16 family characters as κ does. **The deliverable table: `I(C; Sym²⊗ψ)` for the 16
family characters ψ** (ψ trivial on the deck-invariant free generator `e`), in exact arithmetic over
ℚ(ζ₁₂) ⊃ ℚ(√−3, i), each rank re-derived numerically (SVD) as the second method.

## 4. PASS / FAIL — fixed now

- **PASS (the descent carries the bit):** some family character has `I(C; Sym²⊗ψ) ≠ 0`. Then the E₆
  configuration `Ind ρ₁` on m004 has net chirality `n₂₇ − n₂₇̄ = I ≠ 0` in the interior (L²) count — the
  programme's first non-zero net chirality, from the object's own ℤ/3 descent, the (ℤ/4)² supplying the
  twist. Its magnitude is convention-free inside D (`F = −I`); its SIGN is the 27-vs-27̄ naming.
- **FAIL (the fail theorem, in its honest scope):** `I = 0` for all 16 ψ. Then every E₆ configuration on
  m004 that is abelian or (2+1)-reducible on the descent is vector-like (T4 + this table + Shapiro).
  Out of scope and to be SAID: IRREDUCIBLE non-extending SL(3) representations of π₁(C) (the
  corpus's W1/W2 extend to M and are rigid, B1267); a positive there would need X_{SL(3)}(C)'s
  non-deck-invariant components, not examined here.
- **Predictions that are theorems given §2 (checks, not results):** `I(ψ⁻¹) = −I(ψ)`; `I(ψ∘τ) = I(ψ)`;
  order-2 ψ (3 of them) and ψ = 1 give 0; the 12 order-4 characters fall into 4 free deck-orbits = 2
  inverse pairs of orbits, so the table is TWO integers `(I₁, I₂)` up to sign; an orientation-reversing
  lift σ of an m004 isometry that maps an orbit to itself forces that integer to 0 (T6). The symmetry
  census is computed BEFORE the cohomology and its prediction recorded.
- **The B1296 fence:** a configuration whose Higgs direction lands in the F₄ chamber is vector-like or
  SU(3)-anomalous. `Ind ρ₁` is non-abelian (block-permuting), not a Cartan direction; the fence applies
  to its abelian limit `κ → 1` (ψ = 1, the self-dual sector, I = 0 by T3), consistently.

## 5. Controls (MB12: the operation is non-trivial and the criterion can pass AND fail)
 (a) the E₆ block structure exhibited on the 27's weights: an order-3 element of W(E₆) normalising the
     A₂³ subsystem and permuting its three components cyclically, carrying the three 9-blocks to each
     other (the map exhibited, then shown to act — THE IDENTIFICATION RULE);
 (b) B326 reproduced: `H₁(C) = ℤ ⊕ (ℤ/4)²` from the Reidemeister–Schreier presentation (Smith form),
     deck action Φ₃ on the torsion, `(1−τ)` invertible, the deck-stable splitting constructed;
 (c) the geometric rep exact in ℤ[ω] (relator = 1, `tr ρ(ab) = −2 = tr ρ(ℓ)`), the untwisted sector
     `h¹(C;ℂ) = 1 = r₁ = t₀` (half lives, half dies) and `h¹(C;Sym²) ≥ 1` detected (machinery sees h¹);
 (d) every identity of §2 checked numerically on every sector: `r₁ + r*₁ = t₁`, `t₁ = t₀ + t*₀`,
     `F = (a₀−a*₀) + r₁ − t₀`, `I(V*) = −I(V)` — the derivation is TESTED, not trusted;
 (e) NON-VACUITY: the same code on a random 2-generator presentation with a random "peripheral" pair
     returns non-zero indices AND violates the 3-manifold identities of (d) — the identities are
     theorems of the manifold, not tautologies of the code, and the criterion `I ≠ 0` is reachable;
 (f) two methods per rank: exact ℚ(ζ₁₂) Gaussian elimination and floating-point SVD.

*(sealed: see PREREG.sha256 — computed before `step3_index.py` is first run)*
