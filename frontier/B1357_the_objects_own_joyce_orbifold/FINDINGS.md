# B1357 — THE OBJECT'S OWN JOYCE ORBIFOLD: compactifying the E₆ fibre by the Hurwitz torus gives a flat G₂ orbifold (T³ × ℍ/Λ)/(Π ⋉ 2T) with N = 1, whose singular loci are E₆, SO(8) and SU(2) on three copies of Y₃ and SU(3) on T³ — the three Y₃-loci rigid (unbreakable, no adjoints), the T³-locus resolvable — with b₂ = 0 and b₃ = 4 (the four flat moduli); its ℤ/3 descent is the object's own closing, on which the deck folds SO(8) to G₂ by triality, keeps E₆ (inner), and puts two compact A₂ loci through every cone circle (E₆: 2T × Z₃; SU(2): Z₆(1,2,3); SO(8): SL(2,3); SU(3): Z₃ × Z₃), one joining E₆–SU(2)–SU(3) and one joining E₆–SO(8)–SU(3); no C-field U(1) in the background or its resolution carries the deck's irreducible, so the generation-distinguishing U(1)² of B1356 must be born with the curved apexes

**Date:** 2026-09-15 · **Seat:** cc (the SM-derivation branch) · **Status:** PROVED (every number exact: the Hurwitz torus over ℚ, the loci from the permutation action, the invariant forms by exact rank, the local groups over the Hurwitz integers with the octonionic G₂ form; the physical readings — pure SYM on a locus with b₁ = 0, folding by an outer-automorphism monodromy, Joyce's resolution counts, the five-dimensional divisor dictionary — are the standard ones, cited) · **Price: unchanged** · **Numbering:** B1357 (L213; feeds L212).

## 0. Seen from above

B1355 and B1356 are local: the E₇ apex is a cone, the "three" is a deck orbit, and both arcs end with "the compact closing is not
constructed". This arc constructs the one compact object the ingredients determine without any choice: compactify the E₆ fibre
ℂ²/2T by the torus of the Hurwitz order Λ (the lattice 2T preserves), let the Hantzsche–Wendt group act on T³ as it must and on
the fibre by the lifts of its holonomy as the SO(4) ⊂ G₂ of B1356 dictates, and take the quotient. The result is a compact flat
G₂ orbifold — a Joyce orbifold T⁷/Γ with the object's groups in Γ — with exactly one invariant spinor and four singular loci, all
disjoint: E₆ on Y₃ (the object's own closing, B1273), SO(8) on a second copy of Y₃, SU(2) on a third, SU(3) on T³. The first
three are rigid because the Hantzsche–Wendt holonomy rotates the hyperkähler triple with no fixed direction; the fourth is not.
b₂ = 0: the flat background carries no C-field U(1) at all. Its ℤ/3 descent by the deck is the object's own closing (the Euclidean
figure-eight orbifold as E₆ locus, B1356), and there the deck acts on each locus's fibre by an element of the local group that
either is inner (E₆, SU(2), SU(3)) or is the triality of D₄ (SO(8) → G₂), and the deck's coset forces compact A₂ loci — the
compact form of B1356's two A₂ planes — that run through every cone circle and tie the four loci into a web. The question hint 16
left (a b₂ ≥ 2 with the deck acting irreducibly) is decided in the flat class: the irreducible occurs only on 3-forms; the U(1)²
that tells the three generations apart can only come with the apexes themselves.

## 1. The construction

- The fibre: T⁴ = ℍ/Λ, Λ = ℤ⟨1, i, j, (1+i+j+k)/2⟩ the Hurwitz order (a scaled D₄ lattice); 2T = its unit group acts by left
  multiplication and preserves Λ (computed; Λ is closed under multiplication). Its left ideals are principal (class number one),
  so this is the only 2T-invariant lattice up to a right scaling, which is an isometry commuting with 2T.
- The base: T³ = ℝ³/ℤ³ with Π = P2₁2₁2₁ (Y₃ = T³/Π, B1273/B1356). An element of Π with linear part A = conjugation by l ∈ Q₈ acts on
  the fibre by y ↦ r y l̄ for some r ∈ Sp(1) (the SO(4) ⊂ G₂ convention verified in B1356); on the Hurwitz torus r must preserve Λ,
  so r ∈ 2T, and modulo the fibre group the choice is void: the twist is y ↦ y l̄, canonical. (B1084's 2O twist is impossible on the
  torus: (1+i)/√2 does not preserve Λ.)
- The deck: (l₀, 1) with l₀ = (1+i+j+k)/2 and the P2₁3 rotation (B1356).

The moduli match: three radii of the T³ lattice and the fibre scale (four) for the cover, the cubic lattice and the fibre scale (two)
for the descent — exactly b₃ below.

## 2. The singular census (`joyce_orbifold.py`, stages 1–2; exact)

**T⁴/2T.** Fixed points of g on T⁴: 16 (g = −1), 4 (order 4), 9 (order 3), 1 (order 6) — equal to N(g − 1)² in every case
(Lefschetz). 48 singular points in 7 orbits: one E₆ (the origin), one D₄ (three points (1+i)/2, (1+j)/2, (1+k)/2, stabiliser Q₈),
one A₁ (twelve points, stabiliser ±1, representative (1+i+j+k)/4), four A₂ (eight points each, stabiliser Z₃). No A₃ or A₅ points
(the order-4 elements fix only the D₄ points; the order-6 elements only the origin). χ(T⁴/2T) = 5 and the minimal resolution has
χ = 5 + 6 + 4 + 1 + 4·2 = 24: **a K3** — the binary-tetrahedral Kummer surface (the tetrahedral case of Taormina–Wendland).

**The cover (T³ × T⁴)/(Π ⋉ 2T).** Right multiplication by i, j, k fixes the E₆, D₄ and A₁ orbits and permutes the four A₂ orbits as
the regular action of V₄; l₀ fixes one A₂ orbit and cycles the other three (T = A₄ on four points). Hence:

| locus | fibre point(s) | 3-manifold | holonomy | b₁ | fibre monodromy on the root lattice |
|---|---|---|---|---|---|
| E₆ | the origin | Y₃ (Hantzsche–Wendt) | V₄ | 0 | inner (the g are in 2T = Γ) |
| D₄ (SO(8)) | the Q₈ orbit | Y₃ | V₄ | 0 | inner (the g lie in Q₈·{±1}) |
| A₁ (SU(2)) | the twelve points | Y₃ | V₄ | 0 | through order-4 elements: inner on A₁ (SO(3) connected) |
| A₂ (SU(3)) | the four orbits | T³ (the 4-fold holonomy cover of Y₃) | 1 | 3 | trivial |

Four disjoint loci (they sit over distinct fibre points). The 4d theory of the flat background is N = 1 pure super-Yang–Mills for
E₆ × SO(8) × SU(2) (b₁(Y₃) = 0: no adjoint chirals) and SU(3) with three adjoint chirals on T³.

## 3. Betti numbers, the spinor, rigidity (stages 3–4, 7; exact)

Invariant forms of the point group (2T on the fibre, Q₈ on both factors; the deck added for the descent):

| | invariant 1-forms | invariant spinors | b₂ | b₃ |
|---|---|---|---|---|
| cover | 0 | 1 (N = 1) | **0** | **4** |
| descent | 0 | 1 (N = 1) | **0** | **2** |

The deck acts on the cover's four invariant 3-forms with eigenvalues 1, 1, ω, ω̄ — the invariant pair is the descent's b₃. **Rigidity:**
the resolution or deformation parameter of ℂ²/Γ along a locus lies in 𝔥(Γ) ⊗ (ℝ³)^{hol}, ℝ³ the hyperkähler triple rotated by the
locus's holonomy; (ℝ³)^{V₄} = 0, so the E₆, SO(8) and SU(2) loci are rigid — no Joyce resolution and no deformation, the three gauge
groups unbreakable in the flat class; (ℝ³)^{1} = ℝ³ on the T³ locus, resolvable, adding 2 to b₂ (A₂ ⊗ H⁰) and 6 to b₃ (A₂ ⊗ H¹(T³)).
After that resolution: cover b₂ = 2, b₃ = 10; descent (parameter along the Z₃ axis) b₂ = 2, b₃ = 4. The deck acts trivially on the
two added 2-forms (the A₂ fibre's normaliser in 2T is Z₆, inside the connected U(1)_L × Sp(1)_R) and on the six added 3-forms
through H¹(T³) = 1 ⊕ (two-dimensional irreducible). **So the deck's irreducible occurs on four of the cover's ten 3-forms and on no
2-form**: the flat background and its resolution contain no C-field U(1) that tells the three generations apart (hint 16, B1356 §2).

## 4. The descent — the object's own closing (stages 2, 5, 6; exact)

Loci over the singular points: E₆, SO(8) and SU(2) each on S³(4₁; 2π/3) (the deck fixes the three orbits), SU(3) on T³/⟨σ⟩ (the four
A₂ orbits form one P2₁3-orbit with stabiliser Z₃: the orbifold T³/Z₃ with one cone circle, b₁ = 1). Along each locus's cone circle the
local group is ⟨Γ_y, deck⟩ of order 3|Γ_y| (the whole deck coset lies in it), and its strata and McKay ages are:

| cone circle of | local group | strata through it | classes | ages 0/1/2 | crepant b₂, b₄ | non-compact divisors |
|---|---|---|---|---|---|---|
| E₆ | 2T × Z₃ (72) | the E₆ plane, two A₂ orbits of 4 planes | 21 | 1/15/5 | 15, 5 | 10 = 6 + 2 + 2 (B1356) |
| SU(2) | Z₆ with weights (1, 2, 3) (6) | the A₁ plane, one A₂ plane | 6 | 1/4/1 | 4, 1 | 3 = 1 + 2 |
| SO(8) | SL(2,3) = Q₈ ⋊ Z₃ (24) | the D₄ plane, one A₂ orbit of 4 planes | 7 | 1/5/1 | 5, 1 | **4 = 2 + 2: D₄ folded to G₂** |
| SU(3) | Z₃ × Z₃ (9) | three A₂ planes | 9 | 1/7/1 | 7, 1 | 6 = 2 + 2 + 2 |

The SO(8) row is the fold: the deck's lift at a D₄ point normalises Q₈ non-centrally (the local group is SL(2,3), seven classes, not
Q₈ × Z₃ with fifteen), so it acts on the D₄ diagram by triality, the three classes ±i, ±j, ±k fuse, and only two non-compact
divisors survive over the D₄ locus — the rank of G₂ = D₄^{triality}. On the cover the SO(8) is unfolded (its Hantzsche–Wendt
monodromy is inner); on the object's own closing the deck folds it: **the descent's gauge group from the D₄ locus is G₂**. The E₆
is not folded (the deck acts on its fibre as the scalar ω, B1356), the A₁ has nothing to fold, the A₂ over the deck-fixed orbit is
acted on inside its Z₆ normaliser.

**The compact collision loci.** The deck-coset elements y ↦ g y l̄₀ with g of order 6 (eight of them) each fix a closed 2-torus T_g
of T⁴ (the compactification of B1356's A₂ planes); every other deck-coset element fixes finitely many points. The eight tori fall
into the two conjugacy classes of order-6 elements: **two compact A₂ loci Σ₁, Σ₂** (each a torus over the knot circle, modulo the
group). Their incidence with the singular points (computed): Σ₁ contains the E₆ point, all twelve A₁ points and the eight A₂ points
of the deck-fixed orbit; Σ₂ contains the E₆ point, the three D₄ points and the same eight A₂ points. So Σ₁ joins the E₆, SU(2) and
SU(3) loci along their cone circles and Σ₂ joins the E₆, SO(8) → G₂ and SU(3) loci: the object's own closing is a web of six gauge
loci — E₆, G₂, SU(2), SU(3) on the four orbifolds and SU(3) on each of Σ₁, Σ₂ — meeting along the cone circles in the local models
of the table, all compact, all vector-like (codimension-six intersections give five-dimensional theories on circles).

## 5. What it means

1. **The flat class has an object-determined compact member.** Not a choice among Joyce orbifolds: the Hurwitz torus is the unique
   2T-invariant compactification of the fibre up to scale, the twist is forced, the deck is the tower's. The 4d theory is N = 1 with
   E₆ × SO(8) × SU(2) unbreakable on three copies of Y₃ and SU(3) on T³ — no chiral matter (B1351: every closing of the tower is
   vector-like), no C-field U(1) (b₂ = 0). The three faces: geometric — three copies of the object's own closing carrying the three
   gauge groups, and the tetrahedral K3 as the fibre; arithmetic — the Hurwitz order and its unit group, with the D₄ lattice's
   16 two-torsion points splitting as 1 + 3 + 12 under 2T; quantum — exactly one invariant spinor, and the deck's irreducible
   living on 3-forms only.
2. **The descent is where the object's own closing acquires structure**: the deck folds SO(8) to G₂, and its coset creates two compact
   SU(3) loci that thread every cone circle — the web of §4. B1356's remark that the knot's A₂ loci are open (flavour) was the
   linear model's; in the compact flat closing they are closed tori over the knot and carry gauge SU(3)s.
3. **Hint 16, decided in this class.** The generation-distinguishing U(1)² (the sum-zero pair on which the deck acts as rotation) is
   not in the flat background, not in its resolution, and not in the descent: it must be born with the curved apexes — the local
   b₂(link) = 1 class at each cone over CP³/2T (B1355), extended over the closing in the sum-zero combinations. Every other C-field
   U(1) the record could offer is deck-invariant and sees no generation.
4. **The touching design (registered).** The E₆ locus and the SU(2) locus are two copies of Y₃ sitting over fibre points at distance
   ½ (the origin and (1+i+j+k)/4). B1355's apex is a cone whose E₆ line and A₁ line meet only at the apex. A closing that brings the
   SU(2)-copy of Y₃ to touch the E₆-copy at three deck-related points — with the local model the cone over CP³/2T — would be the
   destination's item 1 built from this background. It is a design with a name, not a construction.

## 6. Caveats

1. The physical readings are the standard M-theory dictionary (7d SYM on ADE loci, pure SYM when b₁ = 0, outer-automorphism
   monodromy folding the gauge group, non-compact divisors of the crepant resolution as flavour/gauge Cartans); none is derived here.
2. Joyce's resolution counts (b₂ += rank, b₃ += rank·b₁) are applied to the untwisted T³ locus only; rigidity of the twisted loci is
   the statement that no resolution parameter is monodromy-invariant, which forbids Joyce's construction along them but does not by
   itself say what other geometry could smooth them.
3. The compact collision loci are identified as the fixed tori of the order-6 coset elements and their incidence is computed; their
   topology (a torus bundle over the knot circle modulo the group) and b₁ are not computed.
4. The tetrahedral K3 identification is the χ = 24 count plus the standard fact that the resolution of a symplectic torus quotient is
   K3; the singular configuration E₆ + D₄ + A₁ + 4A₂ (rank 19) is computed here, not taken from the literature.
5. The touching design (§5.4) is not a construction; the flat class cannot contain the apex (B1259, B1353).

## 7. Registered

- **L213 (iv)** — the touching design: the SU(2)-copy of Y₃ brought to the E₆-copy at a deck orbit of three points with the cone
  over CP³/2T as local model; whether a G₂ transition from the flat background does it.
- **L213 (v)** — the five-dimensional theories along the four cone circles (the table of §4) on the knot circle, and the 4d matter
  they leave: the only place matter can enter the object's own closing.
- **L213 (vi)** — the K3 alternative: (T³ × K3)/Γ with Mukai's symplectic 2T on K3 in place of the Hurwitz torus.
- HINT 18 (`docs/HINT_LEDGER.md`): the object's own closing folds SO(8) to G₂ by the deck — a G₂ gauge group on a G₂-holonomy
  background from the same ℤ/3 that makes the closing Euclidean.

## Verification

`verification/joyce_orbifold.py` (about two minutes; record `joyce_orbifold_run.txt`): stage 1 the Hurwitz torus (exact
coordinates in the Hurwitz basis, the fixed points on a 1/12-grid, stabilisers, orbits, Lefschetz check, χ); stage 2 the permutation
action of Q₈ and l₀ on the orbits, the loci of the cover and the descent, the fibre monodromies; stage 3 exact ranks on Λ²ℝ⁷ and
Λ³ℝ⁷ for the point groups, the deck's eigenvalues on the invariant 3-forms; stage 4 rigidity; stage 5 the fixed sets of the
deck-coset elements (tori for the order-6 elements); stage 6 the local groups along the four cone circles with strata, conjugacy
classes and ages (the octonionic complex structure of B1356), the incidence of Σ₁, Σ₂; stage 7 the resolution table. Lock:
`tests/test_b1357_the_objects_own_joyce_orbifold.py`.

**Sources.** Joyce, *Compact manifolds with special holonomy* (2000), ch. 11–12 (T⁷/Γ and the resolution of T³ × ℂ²/Γ). Acharya,
*M theory, Joyce orbifolds and super Yang–Mills*, hep-th/9812205 (SYM on the loci of Joyce orbifolds). Ito–Reid (ages). Taormina–
Wendland, JHEP 08 (2013) 125 (the tetrahedral Kummer surface); Fujiki, Publ. RIMS 24 (1988) (finite automorphism groups of
2-dimensional complex tori). B1273, B1355, B1356 (this branch); B1084 (the linear model).
