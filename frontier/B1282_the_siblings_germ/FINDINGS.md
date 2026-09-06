# B1282 — THE SIBLING'S GERM: on m202 too, the inversion is the E₆ outer automorphism on the deformation space, so the flat E₆ sector of the two-cusped sibling is vector-like near its geometric point — fc's count of three lives only on the singular locus

**Date:** 2026-09-07 · **Seat:** cc (the SM-derivation branch) · **Status:** PROVED (the twelve isometries as automorphisms by exhaustive search, the actions on H¹(m202; Sym^n) at 360 bits with every residual at 10⁻⁵⁵ or below, the theorem by the same linearisation argument as B1280) · **Price: unchanged** · **Numbering:** B1282, this branch's reserved range.

## Why this arc — L208's flat half

B1281 brought the two-cusped sibling m202 onto this branch: main's parity theorem excludes a fixed-locus count of three on
any one-cusped manifold, m202 (commensurable with the object, ℚ(√−3), 2T, Sym = D₆) has an order-3 isometry with three
fixed lines, and fc's R72 writes 3·(16 ⊕ 10 ⊕ 1) on them as a singular-locus Pantev–Wijnholt count. L208 asked B1280's
question on m202: **do its isometries pair the flat E₆ local systems with their duals on cohomology?** If one does, the
count of three cannot come from flat E₆ connections near m202's geometric holonomy, and fc's three is exactly what fc
fenced it as — a singular-locus count.

## 1. m202 and its twelve isometries as automorphisms ((1), exact)

π₁(m202) = ⟨a, b | aabbAbAABBaB⟩ (SnapPy), tr a = tr b = ω̄, both cusps parabolic with hexagonal shape e^{iπ/3},
vol = 4 v_tet = 2 vol(m004), H₁ = ℤ², Sym = D₆ (twelve orientation-preserving isometries). All pairs of reduced words of
length ≤ 5 that send the relator to the identity and preserve the character: **180 automorphisms in twelve classes** by
their action on H₁ = ℤ² and their permutation of the two cusps (the cusp fixed points' orbits under words of length ≤ 6
are disjoint) — fc R72b's 180 and 12, by an independent route. Representatives, with the H₁ matrix (columns = images of
a, b) and the cusp permutation:

| class | a ↦ | b ↦ | H₁ action | cusps | order |
|---|---|---|---|---|---|
| identity | a | b | I | fixed | 1 |
| the inversion | A | B | −I | fixed | 2 |
| swap | b | a | [[0,1],[1,0]] | swapped | 2 |
| (B, A) | B | A | −[[0,1],[1,0]] | swapped | 2 |
| (bA, b), (a, aB) | bA, a | b, aB | reflections | swapped | 2 |
| (A, bA), (aB, B) | A, aB | bA, B | reflections | swapped | 2 |
| (bA, A), (B, aB) | bA, B | A, aB | rotations of order 3 | fixed | 3 |
| (b, bA), (aB, a) | b, aB | bA, a | rotations of order 6 | fixed | 6 |

## 2. The tangent space and the actions ((2)–(4), 360 bits)

The polished holonomy (relator residual 10⁻⁶⁰; Sym^n checked to be a **homomorphism** to 10⁻⁶⁰ — see §4) gives, by Fox
calculus on ⟨a, b | R⟩ in Sym^n ρ:

> **h¹(m202; Sym^n ρ) = 2 for every even n ≤ 22** — one class per cusp (the odd powers also give 2 for this lift, both peripheral traces of which are +2, unlike m004's; they do not enter e₆, which is a sum of even powers); the Zariski tangent space of the
> E₆(ℂ) character variety at the geometric point is H¹(m202; e₆) = ⊕_{n ∈ {2, 8, 10, 14, 16, 22}} H¹(m202; Sym^n), twelve-
> dimensional, with θ = +1 on the f₄ slots {2, 10, 14, 22} and −1 on the 26 slots {8, 16}.

For each isometry σ (intertwiner N with ρ∘σ = Ad(N)∘ρ, residual ≤ 10⁻⁵⁵) the induced 2×2 action f ↦ Sym^n(N)⁻¹ f∘σ on
each slot, checked to preserve Z¹ and B¹, has eigenvalues that are roots of unity of order dividing 6 (as a finite-order
map must):

| slot n | θ | inversion (A,B) | swap, (B,A), (bA,b), (a,aB), (A,bA), (aB,B) | order 3: (bA,A), (B,aB) | order 6: (b,bA), (aB,a) |
|---|---|---|---|---|---|
| 0 | · | (−1, −1) | (±1, ∓1) | (ω, ω̄) | (−ω̄, −ω) |
| 2 | + | **(+1, +1)** | (1, −1) | (ω, ω̄) | (ω, ω̄) |
| 8 | − | **(−1, −1)** | (1, −1) | (ω, ω̄) | (−ω̄, −ω) |
| 10 | + | **(+1, +1)** | (1, −1) | (1, 1) | (1, 1) |
| 14 | + | **(+1, +1)** | (1, −1) | (ω, ω̄) | (ω, ω̄) |
| 16 | − | **(−1, −1)** | (1, −1) | (1, 1) | (−1, −1) |
| 22 | + | **(+1, +1)** | (1, −1) | (1, 1) | (1, 1) |

**The inversion acts on every slot as the scalar (−1)^{n/2+1} — the same universal sign as on m004 — and therefore as θ
on the whole twelve-dimensional tangent space. No other isometry does** (the cusp-swapping ones have eigenvalues (1, −1)
on every slot; the rotations of order 3 and 6 act by (ω, ω̄) on the slots n ≡ 2 mod 6 and trivially or by −1 on the
others). The identity control acts trivially; the n = 0 row is H¹(m202; ℂ) = ℤ² ⊗ ℂ with the H₁ actions of §1.

## 3. THE THEOREM, transferred

θ and ι\* are commuting involutions of the germ of the E₆(ℂ) character variety of m202 at its geometric point, fixing it,
with the same action on the Zariski tangent space; a finite-order automorphism trivial on the tangent space is trivial on
the germ (B1280 §3(a), the same argument). Hence **θρ ≅ ι\*ρ for every ρ on the germ, 27̄_ρ ≅ ι\*(27_ρ), and
N(27_ρ) = h¹(m202; 27_ρ) − h¹(m202; 27̄_ρ) = 0 identically — for every θ-odd deformation of m202's geometric E₆ holonomy,
on m202 and on every cusped cyclic cover to which the inversion lifts.** At the geometric point itself h¹(m202; 27) =
2 + 2 + 2 = 6 (the three even summands of 27 = Sym¹⁶ ⊕ Sym⁸ ⊕ Sym⁰, one class per cusp each), all self-dual, N = 0.

**Consequence for L208.** The flat E₆ sector of the sibling is vector-like near its geometric point, exactly as the
object's is. The count of three that fc's R72 writes on m202's three fixed lines is a singular-locus Pantev–Wijnholt count
(a θ-equivariant abelian Higgs configuration charged on the lines) and nothing else: it is not, and cannot be made into,
an h¹ of a flat E₆ local system near the geometric holonomy. fc fenced it exactly so; this arc proves the fence from the
flat side. The order-3 symmetry that fc's count rests on acts on the deformation classes by (ω, ω̄) on half the slots and
trivially on the rest — it permutes nothing into a triple.

## 4. The error caught on the way (E70), and B1280 re-checked

The first run of §2 returned non-unit eigenvalues for the order-3 and order-6 isometries. The cause: the Sym^n routine
used in B1280's `theta_odd_pairing.py` (and here at first) was an **anti-homomorphism** — the substitution x ↦ g₁₁x + g₁₂y,
y ↦ g₂₁x + g₂₂y composes in reverse order — and two features of m004 had masked it: the relator check cannot see it (the
reversed relator is the inversion's image of the inverse relator, and the inversion is an automorphism, so the anti-
representation still kills the relator), and involutions cannot see it (Ad(g) = Ad(g⁻¹) for their intertwiners). Main's
B1267 hit the same trap and caught it with a homomorphism check; this branch had none. **Fixed at source** (g transposed
before the substitution; a homomorphism assertion now runs before any result in B1280's script and here) and **B1280's
six signs re-computed with the corrected routine over both primes: unchanged**, (+, −, +, +, −, +) — as they had to be,
since the anti-representation is the pullback of the dual by the inversion, an isomorphic local system on which
involutions act with the same eigenvalue. Registered as **E70** in `docs/ERROR_LEDGER.md`.

## 5. Ledger

- L208 (ii) closed: the flat half. What remains of L208 is fc's singular-locus count itself (its independent verification,
  the charge assignment, the lift) and the transport of the E₆ chain to a two-cusped sibling (its price in the
  identification ledger).
- The θ-odd pairing law now holds on the object and on its two-cusped sibling; the inversion is the E₆ outer automorphism
  on the deformation space in both, uniquely among their isometries.
- Values: 0 of 19; no identification moves; price unchanged.

## Controls (MB12)

- The isometry search is exhaustive to word length 5 and reproduces fc's 180 automorphisms and 12 classes by an
  independent route; every named representative sits in a distinct class.
- Every residual is printed and asserted: the relator (10⁻⁶⁰), the parabolic cusps, the intertwiners (≤ 10⁻⁵⁵), the
  Sym^n homomorphism (10⁻⁶⁰), the relator in every Sym^n, the cocycle property of every transported class (10⁻³⁰ relative),
  the singular-value gaps of the Fox kernels (≥ 25 orders at every slot).
- The test can fail and does: eleven of the twelve isometries fail it, each on named slots; the finite-order check
  (eigenvalues roots of unity of order dividing 6) is what caught the anti-homomorphism.
- The odd slots are recorded (h¹ = 2 for this lift; they are not part of e₆), the identity acts trivially, the n = 0 row
  reproduces the H₁ actions of §1; the first selftest expected 0 on the odd slots by analogy with m004 and failed — the
  expectation, not the computation, was wrong (m004's lift has a peripheral trace −2, m202's has none).

## Verification

`verification/sibling_germ.py` (~3 min; `SELFTEST: PASS`; run record `verification/sibling_germ_run.txt`). Lock:
`tests/test_b1282_the_siblings_germ.py` (the isometry search and the slots n ≤ 8 fast; the full set slow-marked). Feeds
on: B1280 (the theorem and the six signs), B1281 (m202 on this branch; main's B1291/B1292; fc's R72/R72b), B1279 (the
automorphism search), B1268 (the lemma; its two-cusped form holds by the same Poincaré–Lefschetz argument). Literature:
Menal-Ferrer–Porti (h¹(M; Sym^{2k}) = the number of cusps); Cartan's linearisation. Registers no identification change.
