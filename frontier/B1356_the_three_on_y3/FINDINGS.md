# B1356 — THE THREE ON Y₃: the deck's fixed set is the branch knot and only it, so the object's own closing is the Euclidean figure-eight orbifold with holonomy 2T/±1; a deck-symmetric triple of E₇ apexes is charged under no deck-invariant U(1) — in the cover by the sum rule, in the descent because the fixed circle is not singular there — and is told apart by exactly two U(1)s or none, with charges 3 × the weights of the 3̄ of the SU(3) that permutes the apexes; the descent forces two A₂ loci through the knot with the local group 2T × Z₃ = (E₆ fibre) × (centre of SU(3)), crepant Betti numbers (15, 5); and on every S⁴/Γ the E₆ point's antipode carries the A₁ companion (L212 (iii) closed in the global-quotient class)

**Date:** 2026-09-15 · **Seat:** cc (the SM-derivation branch) · **Status:** PROVED (every structural step exact: the flat model over ℚ, the local group over the Hurwitz integers with the octonionic G₂ form, the lattice statements over ℤ; the sum-rule consequences are theorems *conditional on* a compact G₂ closing with E₆ locus Y₃ carrying the deck, which is not constructed) · **Price: unchanged** · **Numbering:** B1356 (L212 (i) and (iii); (ii) untouched).

## 0. Seen from above

B1355 named the local model of the destination's E₇ point (the G₂ cone over CP³/2T) and left the "three" to the tower: can the
ℤ/3 descent of Y₃ place three such apexes on one E₆ locus, and what does Witten's sum rule ∑_α ∫_{U_α} w = 0 then say (HINT 16)?
The answer comes from three exact facts about the tower's own geometry. *First*, the deck of Y₃ → S³ fixes exactly one closed
geodesic of the flat Hantzsche–Wendt manifold — the lift of the knot — and acts freely elsewhere; so a deck-symmetric triple is a
free orbit, and the object's own closing (the quotient) is the Euclidean orbifold S³(4₁; 2π/3) whose holonomy is T = A₄ = 2T/±1,
the object's McKay group modulo its centre. *Second*, the sum rule on the cover kills every deck-invariant charge (3q = 0), and the
fixed circle cannot compensate in the descent because it is not a singular locus of the cover (the harmonic form is smooth across
it, so the torus around the knot integrates to zero): the three 27s are charged only under the classes on which the deck acts
irreducibly, which is exactly two U(1)s or none, with charge triples in the coset (1, 1, −2) + 3A₂ forced jointly by the sum rule
and the global form (E₆ × U(1))/Z₃. *Third*, the deck's action on the E₆ fibre along the knot is forced by the G₂ structure to be the
scalar ω — the centre of SU(3) = Stab_{G₂}(knot direction) — so the descent's E₆ locus meets two A₂ loci along the knot, the
local model being ℝ × ℂ³/(2T × Z₃), whose crepant resolution has b₂ = 15, b₄ = 5 (ten non-compact divisors = the E₆, A₂, A₂
Cartans, five compact ones). And L212 (iii) closes in the class where anything is known: on S⁴/Γ the involution −1 of an E₆ point
fixes the antipode too, and CP²/Γ has no E₆ points at all (Hitchin's theorem makes these all the global quotients).

**What this says for the destination:** the three generations of item 1, as a deck orbit, are a *cover* phenomenon. From the
object's own closing they are invisible — one apex, one 27, neutral under every C-field U(1), sitting on an E₆ locus whose knot
carries two SU(3) flavour loci. Only on Y₃, with b₂ ≥ 2 and the deck acting as its two-dimensional irreducible on H², are the
three told apart, and then by a U(1)² whose charges are the weights of the 3̄ of the permutation SU(3).

## 1. The deck on Y₃ (`three_on_y3.py`, stage A; exact over ℚ)

Y₃ = ℝ³/Π with Π = P2₁2₁2₁ (the Hantzsche–Wendt Bieberbach group, holonomy V₄; B1273's identification of the 3-fold cyclic
branched cover of 4₁, Zimmermann 1990) and the deck σ: (x, y, z) ↦ (z, x, y), which normalises Π; ⟨Π, σ⟩ = P2₁3 with point group
T = A₄ = 2T/±1. Computed:

| | result |
|---|---|
| torsion of P2₁3 | the three order-2 cosets are 2₁ screws (no fixed points), the eight order-3 cosets are pure rotations |
| Fix(σ) on Y₃ | the four cosets of Π each contribute one circle on T³ (directions (1,1,1), (−1,1,1), (−1,−1,1), (1,−1,1)); V₄ permutes them: **one closed geodesic** on Y₃, length √3 in lattice units (vol Y₃ = 1/4) — the lift of the knot |
| singular set of ℝ³/P2₁3 | the 3-fold axes form 4 lines mod ℤ³ and **one orbit** under P2₁3: one cone circle of angle 2π/3 — Thurston's Euclidean figure-eight orbifold, Y₃/σ = S³(4₁; 3) |
| holonomy | V₄ (Π's, acting freely) is completed by the deck to T = 2T/±1; lifted to Sp(1), Q₈ and the deck's l₀ = (1+i+j+k)/2 generate 2T exactly |

So a deck-symmetric triple of apexes on Y₃ is a free orbit off the knot, and the object's own closing (the descent) has E₆ locus
the Euclidean orbifold S³(4₁; 3) with one apex and the knot as its cone circle. (The alternative — one apex *on* the knot, fixed by
the deck — is a different design, registered in §7.)

## 2. The sum rule under the deck (stage C; exact over ℤ)

Let X be a compact G₂ closing with E₆ locus Y₃, three apexes P₁, P₂, P₃ (cones over CP³/2T, B1355) forming a deck orbit, and the
deck σ extended to X as an isometry (it preserves φ: orientation-preserving on Y₃ and on the fibre). For a harmonic two-form w on
X the charges q_α = ∫_{U_α} w satisfy ∑_α q_α = ∫_{Y₃ ∖ balls} dw = 0 (Witten, hep-th/0108165 §3; B1355 §3).

1. **Invariant classes charge nothing.** σ*w = w gives q₁ = q₂ = q₃ = q and 3q = 0. In the descent X/σ the single apex P carries
   the same q = 0 — and the knot does not rescue it: the boundary of S³(4₁;3) minus a ball at P minus a tube around the knot is
   U_P ∪ T_K, and ∫_{T_K} w̄ = ⅓∫_{T̃} w = 0 because T̃ = ∂N(K̃) bounds the tube in Y₃ where w is smooth (K̃ is a fixed circle of the
   deck, not a singularity of X). So **the object's own closing has one 27, neutral under every C-field U(1).**
2. **Charges come only from the deck's two-dimensional irreducibles.** The map H²(X; ℚ) → ℚ³ is σ-equivariant with σ permuting the
   coordinates; its image lies in the sum-zero plane, which has no invariants (computed) and is the irreducible two-dimensional
   representation; so the image is 0 or the whole plane: **the three 27s are told apart by exactly two U(1)s or by none.** This
   is HINT 16 sharpened: b₂ ≥ 2 with σ acting as its irreducible on a summand is necessary, and when it is there the flavour
   Cartan is exactly U(1)².
3. **The lattice.** With the global form (E₆ × U(1))/Z₃ (charges ≡ 1 mod 3, B1355 §4), an integral class gives a charge triple in
   {sum 0, all ≡ 1 mod 3} = (1, 1, −2) + 3A₂ (computed on a box). The deck orbit of (1, 1, −2) is (1,1,−2), (−2,1,1), (1,−2,1):
   Gram matrix 6 on the diagonal, −3 off — an equilateral triangle — and it equals **3 × the weights of the 3̄** of the SU(3) whose
   Weyl group S₃ permutes the apexes (computed). Under the pair (w, σ*w) the three apexes carry (1, −2), (1, 1), (−2, 1): each
   component ≡ 1 mod 3, sum zero.

The arithmetic face here is B1268's Eisenstein A₂: the charge lattice of the three generations is the A₂ root lattice with the
deck acting as multiplication by ω.

## 3. The descent's local model along the knot (stage B; exact over the Hurwitz integers, octonionic G₂)

At a point of the fixed circle the deck acts on ℝ⁷ = Im ℍ ⊕ ℍ (the E₆ locus's tangent ⊕ the fibre) through the SO(4) ⊂ G₂, whose
elements (l, r) act as (x, y) ↦ (l x l̄, r y l̄) — the convention verified to be an octonion automorphism, the other one is not. The
E₆ fibre group is the 2T acting trivially on Im ℍ (elements (±1, r), y ↦ ±r y). The deck rotates the normal plane e^⊥ of the knot
direction e = i + j + k by 2π/3, so l = l₀ = (1+i+j+k)/2 (order 6, conjugation of order 3), and r must normalise 2T (r ∈ 2O) with
(l₀, r)³ in the fibre group, i.e. r³ ∈ 2T — which holds for exactly the 24 elements r ∈ 2T (computed on the 48 elements of 2O).
Every admissible r generates the same group with the fibre 2T:

| | computed |
|---|---|
| the local group G | order **72**; centre Z₂ × Z₃; G = (fibre 2T) × ⟨central order-3⟩ = **2T × Z₃** |
| its place in G₂ | every element ℂ-linear for J = L_e on e^⊥ = ℂ³ with det 1: G ⊂ SU(3) = Stab_{G₂}(e); the central Z₃ acts on the fibre as the scalar ω^{±1} — **the centre of SU(3)** — inner on the E₆ singularity: no diagram automorphism (the deck does not fold E₆; contrast B1084's HW twist through 2O/2T) |
| strata of ℂ³/G | one plane in Im ℍ fixed pointwise by 2T (the E₆ locus, ℝ × ℂ/Z₃ near the knot since G acts on it through Z₃); eight planes in the fibre with pointwise stabiliser Z₃ in **two G-orbits of four** — two A₂ loci, each ℝ × ℂ/Z₆ (setwise stabiliser 18 acting through Z₆); the origin (stabiliser G); 32 elements fix only the origin, 39 fix a plane |
| McKay ages (Ito–Reid) | 21 conjugacy classes: 1 of age 0, **15 of age 1, 5 of age 2** — the crepant resolution of ℂ³/G has b₂ = 15, b₄ = 5, χ = 21 |
| the check | non-compact divisors b₂ − b₄ = 10 = 6 + 2 + 2, the Cartans of E₆, A₂, A₂; compact divisors 5 |

So the descent to the object's own closing puts, along the knot, the collision E₆ ∩ A₂ ∩ A₂ with the M-theory local model
ℝ × ℂ³/(2T × Z₃): a five-dimensional theory on ℝ⁴ × K with flavour rank 10 ⊇ E₆ × SU(3) × SU(3) and gauge rank 5 (the standard
reading of the divisor count; cited, not derived). In the flat model the A₂ loci are disc bundles over the knot — open — so their
SU(3)s are flavour, not gauge, unless the closing compactifies them. This collision is not optional: it is forced by the G₂
structure once the deck rotates the knot's normal disc, because det = 1 on ℂ³ makes the fibre rotate by ω and ω·g has a fixed
line for every order-3 element g of 2T.

**The two faces of one group.** In the linear part of the descent's flat G₂ orbifold the first Sp(1) factor carries the E₆ locus's
holonomy lifted (Q₈ and l₀ generate 2T) and the second carries the E₆ fibre group (2T): the object's McKay group sits on both
factors of the SO(4) ⊂ G₂ — as the holonomy of the locus and as the singularity of the fibre (HINT 17).

## 4. L212 (iii) in the global-quotient class (stage D)

The E₆ point's stabiliser contains 2T ⊂ Sp(1)_L, hence the element acting as −1 on the tangent space. On S⁴/Γ (Γ ⊂ O(5) finite) that
element is diag(−1,−1,−1,−1,1) in a frame at the point — computed: its fixed subspace of ℝ⁵ is a line, so it fixes exactly the point
and its **antipode**, with derivative −1 there too; the antipode is an orbifold point whose twistor line is fixed pointwise by −1 with
normal weights (−1, −1): **the A₁ locus of B1355 is the general case**, and can only be enlarged (to A_{2m−1}, D, E if the antipode's
stabiliser is larger). On CP²/Γ the point stabiliser is U(2) and the twistor fibre (for the anti-self-dual orientation whose twistor
space is the flag manifold) is P(ℂ²), on which only the scalars act trivially: 2T ∩ U(1) = ±1 (computed) — **no E₆ point on any
CP²/Γ.** By Hitchin's theorem S⁴ and CP² are the only compact self-dual Einstein 4-manifolds of positive scalar curvature, so among
global quotients of manifolds a self-dual Einstein orbifold with one 2T point and no A-type companion does not exist. What remains of
(iii) is the class of orbifolds that are not global quotients of S⁴ (Galicki–Lawson quotients and their kin, with cyclic isotropy
unless further divided).

## 5. What it means

| design | E₆ locus | apexes | C-field charges of the 27s | extra loci |
|---|---|---|---|---|
| the cover: Y₃ with a deck orbit | Hantzsche–Wendt (flat), b₁ = 0, H₁ = (Z/4)² | three, free orbit off the knot | under the deck-irrep pair only: 3 × weights of 3̄; b₂(X) ≥ 2 needed | three A₁ loci (one per apex, B1355), permuted |
| the descent: the object's own closing | S³(4₁; 2π/3), Euclidean, holonomy 2T/±1 | one | none (every descended class is invariant) | one A₁ locus at the apex; **two A₂ loci through the knot**, local group 2T × Z₃ |

The three generations are therefore not something the object's own closing can exhibit: it carries one neutral 27. The "three" needs
the cover, and there the *only* thing distinguishing the generations is a U(1)² carried by the C-field on which the deck acts as
rotation by 2π/3, with the charges forming the equilateral triangle 3 × (3̄ weights). Witten's mechanism makes such anomalous U(1)s
massive by the axionic coupling; what survives at low energies of the deck-irrep pair is the question the flavour structure hangs on
(§7). And the descent is not a smaller copy of the cover: it carries a new collision along the knot — the E₆ locus meeting two A₂
loci with the five-dimensional theory of ℂ³/(2T × Z₃) — which the cover does not have (the fixed circle is smooth there).

**The three faces.** Geometric: the deck's axis is the branch knot, and the descent is the one Euclidean member of the figure-eight
cone family (n = 2 spherical, n = 3 Euclidean, n ≥ 4 hyperbolic) — the object's own closing is flat. Arithmetic: the charge lattice
of the three generations is the Eisenstein A₂ with the deck as ω, the coset (1,1,−2) + 3A₂ cut out by the sum rule and the Z₃ global
form. Quantum: the deck acts on the E₆ fibre as the centre of SU(3), the McKay ages count (15, 5), and the inflow sees the generations
only through the irreducible pair.

## 6. Caveats

1. No compact G₂ closing with E₆ locus Y₃ and three apexes is constructed; §2 and §5 are theorems about any such closing that
   carries the deck, and the flat orbifold of §3 is the background along the knot, not the closing (the apexes are curved
   insertions the flat class cannot supply, B1259/B1353).
2. The sum rule is used as Witten states it (∫_{Q′} dw over the locus minus balls); the charge normalisation and the "≡ 1 mod 3"
   condition follow B1355 §4's transposition of Witten's U(N) remark; the count "one 27 per apex" remains cited (B1355 caveat 2).
3. The five-dimensional reading of the ℂ³/(2T × Z₃) point (gauge rank = compact divisors, flavour rank = non-compact ones) is the
   standard M-theory dictionary, cited; the spectrum of that theory is not computed.
4. That the underlying space of Y₃/σ is S³ with the cone circle the figure-eight is the branched-cover statement itself (the quotient
   of a cyclic branched cover by its deck is the base); the flat computation verifies the consistency of the model (one fixed circle,
   one singular circle, no other torsion), not the knot type.
5. (iii) is closed only for global quotients of S⁴ and CP²; orbifolds that are not global quotients of a manifold are untouched.

## 7. Registered

- **L213 (i)** — the deck-irrep U(1)²: after Witten's axionic mass, what discrete remnant acts on the three generations (the deck as a
  Z₃ flavour symmetry with the regular representation minus the trivial)? **(ii)** the alternative design with the apex *on* the knot
  (deck-fixed): its local model would be the cone over CP³/(2T × Z₃) with the Z₃ in Sp(2) normalising 2T — a census like B1355's.
  **(iii)** the spectrum of the five-dimensional theory of ℂ³/(2T × Z₃) along the knot, and whether a compact closing can close the
  A₂ loci.
- L212 (ii) unchanged (the E₆ × SU(2) spectrum at the apex; the SU(2) is now known to be unavoidable in the global-quotient class).
- L212 (iii) for orbifolds that are not global quotients.
- HINT 17 (`docs/HINT_LEDGER.md`): the object's McKay group on both Sp(1) factors of SO(4) ⊂ G₂ along the knot.

## Verification

`verification/three_on_y3.py` (about a minute; record `three_on_y3_run.txt`): stage A the flat model (P2₁2₁2₁ and P2₁3 from the
International Tables, exact rationals; the fixed set of the deck, the torsion census, the axis orbits, the Sp(1) lift); stage B the
local group (Hurwitz quaternions, the octonionic G₂ form, the two SO(4) conventions tested, the normaliser 2O built numerically, the
group generated exactly, its strata, the complex structure J = L_e, determinants, ages by conjugacy class); stage C the lattice; stage
D the antipode and the CP² scalars. Lock: `tests/test_b1356_the_three_on_y3.py`.

**Sources.** Witten, *Anomaly cancellation on manifolds of G₂ holonomy*, hep-th/0108165 §3 (the inflow, the sum rule, the global
form U(N)). Acharya–Witten, hep-th/0109152 (the twistor family). Thurston, *The geometry and topology of three-manifolds*, ch. 4
(the figure-eight cone manifolds: Euclidean at 2π/3). Zimmermann, Monatsh. Math. 110 (1990) (Hantzsche–Wendt as the 3-fold branched
cover of 4₁; B1273). Hitchin, *Kählerian twistor spaces*, Proc. LMS 43 (1981) (S⁴ and CP² the only compact positive self-dual
Einstein 4-manifolds). Ito–Reid, *The McKay correspondence for finite subgroups of SL(3, ℂ)* (ages and the Betti numbers of crepant
resolutions). International Tables for Crystallography A, space groups 19 and 198.

*(Currency 2026-09-15, B1357: §3's "the A₂ loci are disc bundles over the knot — open — so their SU(3)s are flavour" is the linear
model's statement. In the compact flat closing (the E₆ fibre closed by the Hurwitz torus, `frontier/B1357_the_objects_own_joyce_orbifold`)
the order-6 coset elements fix closed 2-tori, so the two A₂ loci along the knot are compact and carry gauge SU(3)s; they also thread the
cone circles of the SU(2) and SO(8) loci (Σ₁: E₆–SU(2)–SU(3); Σ₂: E₆–SO(8)–SU(3)). And §2's U(1)²: B1357 shows the flat background and
its resolution carry no 2-form with the deck's irreducible — the U(1)² must be born with the apexes.)*

*(Currency 2026-09-15, B1358: L213 (ii) — the apex on the knot — is negative within the twistor family: its model is forced to the cone
over CP³/(2T × Z₃) (the deck's lift of §3), whose E₆ locus is ℝ³/Z₃ as required but whose companion at the antipode is A₅ = {±1}·Z₃ and
which carries four A₂ branches; neither exists in the object's own background (B1357). `frontier/B1358_the_e6_apex_family` §3.)*
