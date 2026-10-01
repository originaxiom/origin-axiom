# B1438 — THE SLOPE LAW: the index and the couplings of the Standard-Model frame are read off one function on the fibre's torsion characters, the cusp shape of the affine representation

cc, 2026-10-01. Found by reading the output of B1435's sealed run while it was still running; tested on four
levels; then proved; then verified on everything the record has. **Verdict: PROVED** (theorems A–E below, with
proofs) **and VERIFIED** (the whole of B1434 reproduced from the slope alone; every coupling of B1435).
It was not predicted. B1435's sealed predictions are read in B1435.

## The function

M is a level of a signed word state, G = F ⋊ ⟨t⟩ its group, μ = t the meridian, λ = [x, y] the longitude. Let χ be
a character of G trivial on μ and non-trivial on the fibre. Then H¹(G; χ) is a line and its classes do not vanish
on λ (B1506's T1: restriction H¹(F; χ) → H¹(∂F) is an isomorphism and the monodromy fixes ∂F). Let u_χ be the class
with u_χ(λ) = 1.

**The slope of χ is s(χ) = u_χ(μ).**

It is the cusp shape of the affine representation g ↦ [[χ(g), u_χ(g)], [0, 1]], whose peripheral holonomy is
parabolic with translations s(χ) on μ and 1 on λ. For the trivial character the class is μ* and the slope is ∞.

## The theorems

Let V(ℓ, α) be the non-split module [[α, cβ], [0, β]], β = α/ℓ, c the class of H¹(G; ℓ); this is every sector
module of the frame (B1374, B1432). Assume ℓ, α, β are non-trivial.

**A (firing).** n(V(ℓ, α)) = [s(α) = s(ℓ)], V(ℓ, α)* ≅ V(ℓ, β⁻¹), and

    I(ℓ, α) = [s(α) = s(ℓ)] − [s(β⁻¹) = s(ℓ)].

*Proof.* 0 → α → V → β → 0 gives H¹(α) → H¹(V) → H¹(β) → H²(α), the last map u_β ↦ c ∪ u_β. H²(G; α) is a line
detected on the boundary torus (its dual is H¹(M, ∂M; α⁻¹), the image of H⁰(∂M)), and
(c ∪ u_β)([μ|λ] − [λ|μ]) = c(λ)u_β(λ)(s(ℓ) − s(β)). A class of H¹(V) with non-zero image in H¹(β) is never
interior: its second component restricts to u_β ≠ 0 on the torus, and coboundaries of the torus have second
component 0 because ρ(p) − 1 = [[0, c(p)], [0, 0]] there. The class from the sub-module, (u_α, 0)ᵀ, restricts to a
coboundary iff (u_α(μ), u_α(λ)) is proportional to (c(μ), c(λ)), that is iff s(α) = s(ℓ). The dual is the same
kind of module with sub-character β⁻¹ and the same extension character. ∎

**B (one count).** |I| ≤ 1 on every sector module. *One count per background, on every level, is a theorem.*

**C (couplings).** Let A, B be firing sectors of a background with extension character ℓ and η the character of the
spin-0 sector they couple to. With every class normalised on the longitude (u(λ) = 1, c(λ) = 1, and the two
matter lines by the invariant pairing ε(N⁻¹·, ·), N = ρ(λ) − 1),

    Y(A, B) = s(ℓ) − s(η)        (and Y = −1 if η is trivial).

*Proof.* Both matter classes lie in the sub-lines, on which ε vanishes, so ε(a ∪ b) ∪ h is zero as a cochain and
only the boundary term of the relative product survives: Y = −⟨ε(e, b)·h, [μ|λ] − [λ|μ]⟩ with e the relative lift,
e₂ = u_A(λ)/c(λ). This is e₂·u_B(λ)h(λ)·(s(α_B) − s(η)), and s(α_B) = s(ℓ) by A. ∎

So a coupling vanishes exactly when the Higgs character has the slope of the extension character. When s(ℓ) = p/q
the matter classes and the extension class all vanish on the peripheral curve γ = μ^q λ^(−p), and
**Y = −h_η(γ)/q: the coupling is the Higgs class evaluated on the curve the matter classes die on.**

**D (letters).** Pulling the normalised cocycle back through the word one letter at a time changes it by a multiple
of the coboundary of 1, and s is minus the sum of those multiples around the closed orbit of χ. In the gauge
σ(x) = 0, σ(y) = 1/(X − 1), with χ = (X, Y):

    L (x ↦ x, y ↦ yx):   χ ↦ (X, XY),      contributes 0
    R (x ↦ xy, y ↦ y):   χ ↦ (XY, Y),      contributes X / ((X − 1)(XY − 1))
    −I:                  χ ↦ (X⁻¹, Y⁻¹),   contributes 1 / (1 − X).

On a + state, with X = e^{2πia} before an R and e^{2πia′} after it,

    s(χ) = ¼ Σ_R [1 + cot(πa) cot(πa′)],

the imaginary parts telescoping around the orbit. Consequences: **s is real** — by that telescoping where the gauge
is defined on + states, and on every character computed otherwise (677 on eleven levels, both signs) — so
s(χ⁻¹) = s(χ) and A reads I = [s(α) = s(ℓ)] − [s(β) = s(ℓ)] (A as stated, and the census, use s(β⁻¹) and do not
depend on this); s is invariant under the deck; a character pulled back to the m-fold cover has
m times the slope, so couplings multiply by m (B1435's double-cover control, now a corollary); and a change of
meridian μ ↦ μλⁿ shifts every slope by n, so **only differences of slopes carry content** — which is all that A
and C use.

**E (no mixing).** Let V_A, V_B be sector modules of two backgrounds whose extension characters differ. Then every
invariant functional V_A ⊗ V_B ⊗ η → k is a multiple of T(a, b) = a_q b_q, the product of the two quotient
components, and it exists only for η⁻¹ = β_A β_B; its triple product on the firing classes is zero. *So the cubic
couplings of a family of backgrounds with distinct extension characters are diagonal in the family; along a deck
orbit they are also equal, because s is deck-invariant. In this frame a deck orbit of three is three copies of one
generation with one set of couplings: no mixing and no splitting.*

*Proof.* A functional to a character is an invariant line of V_A* ⊗ V_B*. With f₂ spanning the sub-line of each
dual, f₂ ⊗ f₂ is one. A line with a component on f₁ ⊗ f₂ alone would need z(ℓ_A − 1) = x·c_A, making the extension
class c_A a coboundary; one with components on both f₁ ⊗ f₂ and f₂ ⊗ f₁ needs the two characters equal, that is
ℓ_A = ℓ_B (and then it is ε); one with a component on f₁ ⊗ f₁ needs c_B a coboundary. The firing classes have
representatives in the sub-lines, on which a_q = 0, so both the cochain and the boundary term vanish. ∎

## Verified

| what | against | result |
|---|---|---|
| **the whole architecture census from the slope alone** (`slope_census.py`, 20 seconds, no index computed; slopes modulo two primes above 2·10⁹) | B1434's record, 68 levels, 942 268 candidate modules: characters, firing, generation-shaped backgrounds, lifted, signs, \|counts\|, ν^c, orbit sizes | **0 levels differ** |
| A, module by module, with exact slopes over ℚ(ζ_N) (`slope_law.py`) | main's index code at three primes, every candidate of the levels run | 0 mismatches; degenerate modules (α or β trivial) never fire |
| C, vanishing | B1435's sealed run, every pair of every background | 0 mismatches |
| C, values (`value_law.py`; Y by B1435's sealed instrument, backgrounds from the slope census) | pair by pair, both signs, all 30 levels | see the run record |
| D (`cot_formula.py`) | exact slopes, 677 characters on 11 levels | max error 1.8·10⁻¹⁴; all slopes real |
| E (`cross_couplings.py`: every invariant functional by linear algebra, its triple product by B1435's instrument) | s961, −LLRLR, the three-fold cover of −LR, M₄ | different ℓ: no functional, or one of quotient·quotient type with Y = 0, in 11 724 of 11 724 cases; same ℓ: ε appears and couples |

## The numbers

- **s961, the root's three-fold cover:** s = 0 on the three characters of order 2 and ±1 on the twelve of order 4
  (six each). Every allowed coupling of its 48 backgrounds is ±1 or ±2.
- **−LLRLR at its own level:** slopes 0, −4/3, −3/2, −3/4. The ten·ten coupling is 3/2 on all eight backgrounds and
  every other coupling is 0.
- **M₂:** ±1/√5. **−LLLRLR at its own level:** 0, −5/3 and two conjugates in ℚ(√5).

## What it means, and the fence

- **The frame cannot split generations.** By B and E a background carries one generation and a deck orbit carries
  it three times with the same couplings. The record's B1362 found the same degeneracy for deck-symmetric textures
  on the closed cover and that the data refute it. Whatever distinguishes three generations is not in this frame.
  **Prior statements of this, which E turns into a computation:** the SM lane's B1506 §5 ("the three blocks of an
  orbit are three distinct vacua … any frame that makes the family index a tensor factor beside SL(2)_β gives every
  family the same λ"), and the web seat's audit, whose oriented-cycle support is the quotient·quotient functional.
- **B is a theorem about rank-two sectors, not about the manifolds.** B1418 measured |I| = 2 on rank-four modules
  of a sibling, and the record already holds the larger parent this points to: E₈ ⊃ SU(5) × SU(5)_⊥ with a flat
  rank-five bundle W, tens from H¹(W) and five-bars from H¹(Λ²W) — built by the audit lane on m010 with
  I(W) = I(Λ²W) = +1 (its R40), carried by the SM lane as an open lead (sL-4), and searched by the web seat on M₆
  in bounded families with largest index 2. Index ±3 is neither found nor excluded anywhere in the record.
- **The frame is one function.** B1374, B1427, B1432, B1434 and B1435 computed ranks of twisted complexes module by
  module. All of it is s on the monodromy-fixed torsion points of the torus, and two rules.
- **The architecture is one object in this frame.** By D the local terms form a 1-cocycle on the action groupoid of
  the mapping class group of the punctured torus (with its boundary) on the torsion points of the character
  torus; states are its conjugacy classes, levels its powers, characters the fixed points, and s the cocycle on
  isotropy. Relations between states are relations in that groupoid. Not developed here.
- **The fence is unchanged.** Main's class index on reducible non-split modules; non-semisimple backgrounds; an
  index is not a generation count. The normalisation of C is canonical for the frame (the longitude and E₆'s own
  pairing); it is not a kinetic normalisation, and Y is not a Yukawa coupling of a four-dimensional field.
  "Allowed" pairs are charge-allowed; E₆'s Clebsch–Gordan constants are not computed. 0 of 19.

## Registered

- The cotangent sum of D is of Dedekind–Rademacher type along the cutting sequence. Whether s is the
  Eisenstein (Sczech) cocycle of the monodromy at the torsion point, and its Fourier transform a partial zeta value
  of the state's real quadratic order at 0, is **not checked** and is a lead.
- The census beyond length six is now seconds of compute; it is a new population and gets its own seal.
- Rational slope p/q means the background's classes extend over the Dehn filling along μ^q λ^(−p). The relation to
  the record's closed fillings (vector-like by B1351) is not worked out.

## Verification

`verification/slope_census.py` (record `slope_census.json`, `slope_census_run.txt`), `slope_law.py`,
`value_law.py` (records `value_law.json`), `cot_formula.py` (`cot_formula_run.txt`), `cross_couplings.py`
(`cross_couplings.json`). Lock:
`tests/test_b1438_slope_law.py`.
