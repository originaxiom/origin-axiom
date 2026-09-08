# THE CHIRALITY MAP — everything the record knows about chirality, in one place, with what B1280 adds

**Date:** 2026-09-06 · **Seat:** cc · **Purpose:** the owner asked for the repository's chirality knowledge to be retrieved
and the remaining computations run. This document is the retrieval; `frontier/B1280_the_chirality_probe/` is the
computation. It changes no value (0 of 19), no identification and no price. It closes two named computations and
states, for the first time in one place, why every net chirality this record has ever computed on the object is zero.

## 0. Four things the record calls "chirality" — kept apart

| sense | meaning | where it lives | status |
|---|---|---|---|
| **C1 — knot chirality (the CP face)** | is the object isometric to its mirror? | m004 is amphichiral, CS = 0 (B136, B152, B211, B1224); the family R^mL^m is uniformly amphichiral (L32); chiral bundles exist strictly above it (B145, B147: RRL/RLL, field ℚ(√−7), B316) | SETTLED: the object is the amphichiral minimum |
| **C2 — representation chirality** | is the local system V self-dual (V ≅ V\*)? | every SL(2)-factoring holonomy is self-dual (E65); the θ-odd E₆(ℂ) deformations are not (B576, B582: Zariski closure e₆, 27 ≇ 27̄); B71's W1, W2 are the only non-self-dual SL(3) components (B102, B1260) | SETTLED: non-self-dual systems exist and are catalogued |
| **C3 — net chirality (the count)** | N(V) := h¹(M;V) − h¹(M;V\*) ≠ 0 — a chiral spectrum of zero modes | the walls of §1; every value ever computed is in §2 | **ZERO on every representation computed, and now by theorem on the whole θ-odd germ and on all of W1 ∪ W2 (B1280)** |
| **C4 — the chirality bit** | the orientation / sign that a chiral theory must carry | the object cannot sign it (B713, B760: a non-canonical Galois torsor); a closing's orientation (B1273); the observer's registering measurement (B871); registerable = the generation stays chiral (B863) | OPEN as a source: the object registers it, does not supply it |

The Standard Model needs C3 (a chiral spectrum) and C4 (a definite sign). C2 is necessary for C3 and is available;
C1 is the face on which C4 would be read. **This document is about C3 and C4.**

## 1. The walls — where net chirality cannot live, as theorems with their arcs

| wall | statement | arc | mechanism |
|---|---|---|---|
| **W-closed** | on any closed oriented 3-manifold, for irreducible nontrivial V: h¹(V) = h¹(V\*) identically | B1260 (1); B1086's "as PD forces on any closed double" is the special case | Poincaré duality + χ = 0 |
| **W-abelian** | on the cusped object the rank-one sector never carries N ≠ 0, roots or not | B1260 (2) | Alexander reciprocity Δ(t) = Δ(1/t), Δ = t² − 3t + 1, roots φ^{±2}; equivalently (B1280 §4) the inversion ι inverts the meridian, so ι\*ℂ_t = ℂ_{1/t} = ℂ_t\* |
| **W-self-dual** | every V factoring through SL(2) → G (every Sym^n, every 27 along any sl₂, principal or subregular) has N = 0 trivially | E65; B1267 (every cell of the spectrum law); B1268 §2 | V ≅ V\* |
| **W-Hermitian** | any V carrying an invariant Hermitian form of any signature has N = 0 (h¹(V̄) = h¹(V)) | `docs/EXTERNAL_VERIFICATION_2026-09-06.md` §3.2 | conjugation; kills E₆(2), E₆(−14), E₆(−78) holonomies outright — only E₆(6), E₆(−26) and complex images escape |
| **W-boundary** | on the cusped object N(V) = rank(res_V) − h⁰(∂M;V) and **−h⁰(∂M;V) ≤ N(V) ≤ h⁰(∂M;V\*)**; near the geometric E₆ point \|N(27)\| ≤ 1 for every deformation | B1268 (the lemma; the bound; semicontinuity) | Poincaré–Lefschetz on (M, ∂M): net chirality needs cusp-fixed vectors and is at most their number |
| **W-annulus** | the cusp torus's partition by any smooth θ-odd Higgs field's sign has χ(∂⁺M) = χ(∂⁻M) = 0 exactly, so Pantev–Wijnholt's net chiral(R) = −χ(∂⁺M) vanishes on the object | B1277 addendum (the arcs and the corners); the exact form is fc R71's region-swap theorem, re-derived in B1281 | σ swaps the two sign regions and their Euler characteristics sum to χ(T²) − χ(zero set) = 0; the addendum's c₍±2,0₎ caveat is void (a non-transverse zero set has no χ) |
| **W-parity (main B1291, verified B1281)** | on any one-cusped hyperbolic manifold the fixed-point count of a finite-order isometry on the cusp is even (each fixed geodesic line has two ends, all in the one cusp), so \|Fix\| = 3 — the generation count as a fixed-locus count — is excluded on m004; ≥ 2 cusps is the escape | main B1291, B1292; B1281 §2A | \|Fix\| = \|det(A − I)\| ∈ {0,1,2,3,4} with 3 only from the order-3 rotation; m004's cusp is rectangular and admits only ±1; m202's are hexagonal |
| **W-Lefschetz (main B1294, verified B1281)** | on m004 every isometry has L(g) = 1 − s_μ ∈ {0, 2} (the inversions' two arcs); on a closed rational-homology-sphere closing L(g) = 1 − deg g, so the fixed-locus 2 needs an orientation-reversing isometry: a closing may have the 2 or be chiral (CS ∉ {0, ½}), not both | main B1294; B1281 §2B | Lefschetz on H₁ = ℤ⟨μ⟩; the closings on which this branch found the count (Y₃, Y₆, Y₉) are amphicheiral and mirror-paired |
| **W-flat-G₂** | no flat G₂ orbifold supplies Acharya–Witten isolation: every element of SO(7) fixes a line, so every A₁ locus meets the E₆ locus along a line and all localized matter is vector-like | B1084 (the census), B1259 (the theorem) | flatness ⇒ non-isolation ⇒ pairing |
| **W-charge** | the AW U(1) charge operator commutes with neither cusp holonomy, so no charge grading exists on any closed assembly; the U(1) grades the family instead | B1087 | charge / holonomy non-commutativity — the wall's fourth language |
| **W-mirror-quotient** | a quotient of Y₉ by an orientation-reversing lift with C₃ → −C₃ projects every representation onto a self-conjugate one: non-chiral by construction | B1279 §5 | the projected involution inverts the Cartan |
| **W-W1W2 (NEW)** | **on B71's non-self-dual SL(3) components W1, W2, N(M_n; V) = 0 for every point, every central twist and every cusped cyclic cover M_n** | **B1280** (theorem, `chirality_probe_w1w2.py`) | λ = μ^{±3} exactly (B71 P1, c = 1), so the cusp-fixed locus of every cover is one curve K = {μ has an eigenvalue in μ₃}; K is exactly the branch locus of the eight trace coordinates, where the two characters ρ and (Aᵀ, Bᵀ) = τ\*ρ\* coincide (Lawton's ninth trace tr[A,B] = tr[B,A]); τ is the object's period-2 isometry; so V ≅ τ\*V\* on K and N = 0 there, and off K there are no cusp-fixed vectors |
| **W-θ-odd (NEW)** | **on the germ of the E₆(ℂ) character variety at the geometric point — every θ-odd and θ-even deformation — 27̄_ρ ≅ ι\*(27_ρ) and N(27_ρ) = 0 identically, on m004 and on every cusped cyclic cover** | **B1280** (theorem, `theta_odd_pairing.py`, exact over two primes) | the E₆ outer automorphism θ and the pullback ι\* by the object's inversion (a ↦ a⁻¹, b ↦ b⁻¹) are commuting involutions of the germ fixing [ρ₀]; on the tangent space H¹(M; e₆) = ⊕ H¹(M; V_n), n ∈ {2, 8, 10, 14, 16, 22}, θ acts by (+, −, +, +, −, +) (f₄ ⊕ 26) and ι\* by (−1)^{n/2+1} = (+, −, +, +, −, +); a finite-order automorphism trivial on the Zariski tangent space is trivial on the germ; and 27\* = 27∘θ |

**And where the θ-odd wall ends (B1280 §3(d)).** The signs ε_n(ι) depend only on n, so the same test runs at every
sl₂-embedded E₆ point by root combinatorics: the geometric point is the *unique* even orbit where the criterion holds;
at B1256's subregular point (27 = 13 + 9 + 5, the I-25 typing) the triple is the principal sl₂ of an sp(8) and one
θ-odd direction, the V₁₀ of the 42, is unpaired by every isometry. The wall is a property of the geometric embedding,
and the subregular germ is where the question stays live (O1).

**What the two new walls close.** W-W1W2 finishes the computation B1260 named and `EXTERNAL_VERIFICATION` §3 ran at
six points: not six points but the whole components, all covers, by theorem. W-θ-odd closes **L200** (B1268's
remaining computation, the cusp-fixed θ-odd locus): the locus need not be found — wherever it is, N = 0 on it, because
the object's inversion is the outer automorphism of E₆ on the whole deformation germ. The bound \|N(27)\| ≤ 1 of
W-boundary is sharpened to N(27) = 0 near the geometric point.

## 2. Every net chirality this record has computed

| representation of π₁(m004) | non-self-dual? | cusp-fixed vectors? | h¹(V) | h¹(V\*) | N | source |
|---|---|---|---|---|---|---|
| Sym^n of the geometric rep, n = 0..16 (two primes) | no | n even: yes | 1 (n even), 0 (n odd) | same | 0 | `EXTERNAL_VERIFICATION` §3.3; B1268 |
| the principal 27 (Sym¹⁶ ⊕ Sym⁸ ⊕ Sym⁰) and the subregular 27 (Sym¹² ⊕ Sym⁸ ⊕ Sym⁴), at the geometric point | no | yes (h⁰(∂M) = 3) | 3 | 3 | 0 (rank(res) = 3: all three classes boundary-supported) | B1268 §2 |
| C_{−1}, C_ω, the abelian sector at non-roots; the abelian sector at the Alexander roots φ^{±2} | no (χ\* = χ⁻¹ = ι\*χ) | — | 0 / jump | same | 0 | B1268; B1260 (2) |
| every cell of the spectrum law on the closed double D_t (θ-odd and θ-even dials) | 27 vs 27̄ | closed | 2 or 5 | same | 0 | B1086, B1267 |
| PSL(2,7), the two dual 3-dimensional irreducibles, all 12 homomorphism classes | **yes** | when the meridian has order 4 | 1 / 0 | 1 / 0 | 0 | `EXTERNAL_VERIFICATION` §3.3 |
| the non-semisimple extension 0 → ρ_geom → V → χ_t → 0 at t = 2 ∓ √3 | **yes** | no | 0 | 0 | 0 | `EXTERNAL_VERIFICATION` §3.3 |
| W1, W2 at generic points | **yes** | no | 0 | 0 | 0 | `EXTERNAL_VERIFICATION` §3.3; B1280 (a) |
| W1, W2 on the cusp-fixed curve K (six points; B1280: eighteen more, on W1 and W2, exact structure eig Φ⁻¹ = {1, e, 1/e}) | **yes** | yes, one twist per point (all three for 3 \| n) | 1 (that twist) | 1 | 0, for every cover M_n, n ≤ 9, every twist | `EXTERNAL_VERIFICATION` §3.3; **B1280 (b)** |
| W1, W2 at the repeated-eigenvalue points of K (tr μ = 3/2: a triple eigenvalue 1 of Φ; tr μ = −1/2: a double −1) — the only points where a Jordan asymmetry could have made N ≠ 0 | **yes** | yes | equal Jordan data on V and V\* | | 0 for n ≤ 9, every twist, Wang = Fox | **B1280 (c)** |
| **all of W1 ∪ W2, every twist, every n** | **yes** | on K only | | | **0 by theorem** | **B1280** |
| the θ-odd E₆(ℂ) point reached at 600 bits (relator residual 10⁻⁶³) | **yes** (closure e₆) | **no** (h⁰(∂M; 27_s) = h⁰(∂M; 27̄_s) = 0) | 0 | 0 | 0 | B1268 §3 |
| **the whole E₆ germ at the geometric point, θ-odd deformations included, on m004 and every M_n** | **yes** off F₄ | wherever | h¹(27_ρ) | = h¹(ι\*27_ρ) | **0 by theorem** | **B1280** |

No row is nonzero. The two theorems say why the rows that *could* have been nonzero — non-self-dual with cusp-fixed
vectors — are not: **the object's own isometries pair every such system with its dual on cohomology.** The
period-2 swap τ does it for the elliptic SL(3) components (on their cusp-fixed curve, which is the branch locus of
the trace coordinates), the inversion ι does it for the E₆ family (on the whole germ) and for the abelian sector
(Alexander reciprocity is ι-invariance of Δ). Off those loci the boundary bound does the rest.

## 3. What is chiral in the record, and what it was for

- **Constructions of C2.** B582 (the θ-odd-twisted mirror double has E₆ holonomies with Zariski closure E₆(ℂ): the
  27 is complex), B576 (the dichotomy: θ-odd ⇒ closure e₆ and non-self-dual; θ-even ⇒ F₄-stable and self-dual),
  B583 (the chiral content), B1268 (a θ-odd point on the cusped object itself). **Complex, yes; counted, no**: B1086
  found the θ-odd dial's spectrum vector-like on the double, B1268 found N = 0 at the θ-odd point reached, and B1280
  finds N = 0 on the whole germ. A non-self-dual 27 whose zero modes are paired by an isometry is the object's
  version of a T-brane: non-commuting Higgs data, no net chirality.
- **Chirality from a closing.** B432/B434 (31 of 31 Dehn fillings are chiral — sense C1; the slope ±5 selection),
  B1273 (the chirality bit of the 3-fold closing is its orientation), B1279 (the mirror pairs the SM vacua of Y₉;
  the quotient by the mirror is non-chiral). **Every closed closing is vector-like (W-closed)**; the bit exists on a
  closing only as an orientation choice the object does not make.
- **The object cannot sign it.** B713 (triality gauge-only, σ_ω ≡ 0, "which chirality" a non-canonical Galois torsor),
  B760 (no object-native operation — Galois, MCG powers, C, τ, coupling sign — signs the θ-odd chord sector: "the
  object cannot close itself"), B252/B253 (the obstruction and the capability), B301 (the chirality filter), B303
  (the clock is the CP sign), B1246 (θ, not θ̄). B871's registering measurement and B863's "registerable = the
  generation stays chiral" locate C4 with the observer.
- **The census.** B944: 102 arcs, 70 PROVED, on the dynamics of chirality; the four-language wall (PD pairing =
  AW non-isolation = completion kernel = charge/holonomy non-commutativity: B1083, B1084, B1086, B1087, B1105).

## 4. The literature's mechanisms against the object

| mechanism | what it needs | the object | arc |
|---|---|---|---|
| Acharya–Witten: chiral matter at isolated points where an A₁ locus meets an enhanced locus transversally in a G₂ 7-manifold | isolation (0-dimensional fixed sets) | unavailable in the flat class (every SO(7) element fixes a line); needs the non-flat conical G₂ closing over the E₆ locus — the destination's item 1 (B1269 §5) | B1084, B1259, `THE_DESTINATION_LEDGER` §5 |
| Pantev–Wijnholt: net chiral(R) = χ(M, ∂⁺M), the Euler characteristic of the part of the boundary where the Higgs field's charge points outward | a disc-type ∂⁺ | annular on the object (χ = 0) by its eight cusp symmetries; a disc needs a non-unitary holonomy at the golden value (L204) | B1277 addendum, `LITERATURE_SWEEP` §1 |
| T-branes: non-commuting / nilpotent Higgs components carrying localized chiral modes | a non-abelian φ with an unpaired zero-mode spectrum | the θ-odd deformations are exactly such data (B576's closure e₆); their zero modes are h¹ of the complexified connection = what B1268 computed; **B1280: paired by ι on the whole germ, N = 0** | `LITERATURE_SWEEP` §1, §3; B1280 |
| Braun–Cizel–Hübner–Schäfer-Nameki: TCS G₂ manifolds are non-chiral; chirality needs a singular non-TCS transition; no compact chiral G₂ example is constructed | a singular transition | the object's transition (Y₃ flat, Y_n hyperbolic, the two ends) is a candidate carrier, not yet a construction | `LITERATURE_SWEEP` §1, §4 |
| the 3d–3d and index dictionaries: h¹(M; V) of a 3-manifold read as a 4d generation count | an identification never exhibited | I-26 UNEARNED (`docs/IDENTIFICATION_LEDGER.md`); the index theorems live on a CY3 or a G₂ 7-manifold | B1269, `EXTERNAL_VERIFICATION` §3.4 |

## 5. The three faces, read for chirality

- **Geometry (the CP face).** Amphichiral, CS = 0, the eight isometries D₄ with the four orientation-reversing ones
  (B1279 §1). Chirality in sense C1 is absent by construction; in sense C4 it is a bit the mirror could sign only
  as a torsor (B713).
- **Arithmetic.** The two ends φ^{±2}: the Alexander roots, the Novikov zero modes, the two golden eigenlines mod 19
  that the mirror exchanges on Y₉ (B1279). The arithmetic face is *even* under the inversion — which is exactly
  W-abelian.
- **Quantum.** The θ-odd sector is the object's only door to complex representations, and its sign is the torsor
  the object cannot fix (B760). B1280 shows the door's spectrum is even too at the geometric point: ι\* = θ on the deformation germ — and
  *only* there among the sl₂ points. **The three faces agree at the geometric point: the object is even, in every
  sense the record can compute; the one direction it left open, the subregular germ's V₁₀, is closed by B1350 (2026-09-09): genuine non-self-dual E₆ representations along it, N(27) = 0 at each, no cusp-fixed vector.**

## 6. What remains, named

| item | the computation | what it would need to change |
|---|---|---|
| **O1 — the other sl₂ points (COMPUTED, B1280 §3(d))** | the signs ε_n(ι) = (−1)^{n/2+1} are universal, so the test at every even sl₂ orbit of E₆ is root-system combinatorics (`mod4_criterion_other_sl2.py`): **the geometric (principal) point is the unique one where an isometry realises θ on the deformation space.** At B1256's subregular I-25 point the sl₂ is the principal sl₂ of an sp(8) and **exactly one θ-odd direction — the V₁₀ of the 42 — is unpaired** | the subregular germ's V₁₀ direction is the first place on the object where N(27) ≠ 0 is not excluded by symmetry; B1268's cusp-fixed computation, run there, decides it (|N| ≤ h⁰(∂M; 27) still) |
| **O2 — higher rank** | non-self-dual SL(n) components, n ≥ 4, of the object's character variety — none realised in the corpus; the two-sheet mechanism of W-W1W2 is Lawton's SL(3) fact, its SL(n) analogue is the transpose sheet | a rank ≥ 4 non-self-dual system with cusp-fixed vectors and no pairing isometry |
| **O3 — the general theorem** | *conjecture:* N(V) = 0 for every representation of π₁(m004). Mechanism in every case computed: an isometry pairs V with V\* on cohomology (ι for the abelian and E₆ sectors, τ for the SL(3) elliptic components on K), or the cusp keeps no fixed vector | a proof would need, for each V with cusp-fixed vectors, an isometry σ with σ\*V\* ≅ V — false as stated off K on W1/W2, where the bound does the work; the right general statement is not yet formulated |
| **O4 — the singular G₂ closing** | the destination's item 1: the conical G₂ geometry over the object's E₆ locus, where chirality is a 7-dimensional index (Acharya–Witten), not an h¹ of m004 | the only place C3 can still come from, given W-closed, W-flat-G₂ and the two new walls; I-26 is earned or refuted there |
| **O5 — the sign** | C4: the orientation of the singular closing, or the observer's registration (B871) | not a computation on the object: B713/B760 |
| **O6 — the two-cusped sibling (from the seats, B1281)** | m202: tetrahedral, vol = 2 vol(m004), commensurable with the object (cusped arithmetic over ℚ(√−3)), keeps 2T (96 surjections), Sym = D₆, chiral, a ℤ/6 whose order-3 element fixes three geodesic lines running cusp 0 → cusp 1. fc R72's fenced count on them: the inner lift is forced for order 3, every Cartan direction is even, and Pantev–Wijnholt's count with equal charges is 3·(16 ⊕ 10 ⊕ 1) on the SO(10) direction, anomaly-free (or 3·(10 ⊕ 5̄), or one quark family) — "three is in the menu, not selected by it"; PW cited not derived; I-26 unpaid | L208: verify the count independently (lines, charges, lift); **B1280's question on m202 is answered (B1282): the inversion of m202 acts on all six E₆ slots as θ's sign, uniquely, so the flat E₆ sector of the sibling is vector-like near its geometric point and the three is a singular-locus count only**; whether a closing of m202 keeps a count (B1294's theorem says a closed one keeps the 2 only if amphicheiral) |

## 6a. The seats (B1281, 2026-09-07)

Main's B1267, B1290–B1294 and the physics seat's R69–R72 were fetched, re-run on this bench and re-derived with this
branch's code; all agree with the walls above once the quantities are named. N(V) of a flat local system is zero by
theorem on every system this branch supplies (B1280); fc's ±2 and 3 are Pantev–Wijnholt counts for singular θ-even
abelian Higgs configurations charged on fixed geodesic lines — a modelling choice, lift-dependent, and B1280 forces the
outer lift on the geometric germ, so those counts live on abelian backgrounds. The parity theorem excludes 3 on the
object's own cusp; the escape is a two-cusped commensurable sibling (O6). The chirality bit's possible carriers are now
three: the singular G₂ closing (O4), the observer (O5), and m202's fixed lines (O6). On m202 the flat E₆ sector is
paired exactly as on the object (B1282: the inversion is θ on its twelve-dimensional deformation space, uniquely), so the
sibling's three, if it is anything, is a singular-locus count.

## 6b. The V₁₀ direction (B1350, 2026-09-09)

O1's one open direction is computed. Along the V₁₀ of the 42 at the subregular point the E₆ holonomy deforms to genuine representations that are not self-dual (self-duality defects to 5·10⁻⁸ at ε = 0.02/|Y|), and at every one of them h¹(M; 27) = h¹(M; 27̄) = 0, h⁰(∂M; 27) = h⁰(∂M; 27̄) = 0, N(27) = 0 — read at 2000 bits with the torus Euler characteristic and Poincaré duality as consistency checks after B1268's 60-digit report misread the ranks there. The exact calculus (second-order obstruction zero on the whole V₁₀ plane; formal integrability through order 10) says the directions are real; the numerics say they carry no net count. O1 is complete: every sl₂ germ of the object is vector-like. O2–O6 stand.

## 7. Consequence for the destination ledger

The chirality bit (item 1 of `docs/THE_DESTINATION_LEDGER_2026-09-06.md` §5, D3's carrier) is now excluded from:
every closed closing (W-closed), the mirror quotient (W-mirror-quotient), the cusped object's abelian sector
(W-abelian), its elliptic SL(3) components on every cover (W-W1W2), and its E₆ deformation germ (W-θ-odd). It can
still come from the singular G₂ closing (O4) or be supplied by the observer (O5). **The record's statement is
sharpened, not changed: the object is vector-like on every representation it supplies; the Standard Model's
chirality is the closing's or the observer's.** 0 of 19; price unchanged.

## Provenance

Retrieved and cited above: B71, B102, B127, B128, B134, B136, B144, B145, B147, B152, B193, B252, B253, B301,
B303, B316, B318, B432, B434, B576, B582, B583, B612, B713, B760, B863, B871, B944, B1036, B1064, B1083, B1084,
B1086, B1087, B1098, B1105, B1145, B1183, B1222, B1224, B1226, B1227, B1239, B1246, B1255, B1256, B1257, B1259,
B1260, B1264, B1267, B1268, B1269, B1273, B1277 (and its addendum), B1278, B1279; `docs/THE_SM_VERDICT.md` (E65,
the four-language wall, §3), `docs/EXTERNAL_VERIFICATION_2026-09-06.md` §3, `docs/LITERATURE_SWEEP_2026-09-06_higgs_bundles_and_the_destination.md`,
`docs/MAIN_GOAL.md` JOIN 1, `docs/OPEN_LEADS.md` (L4, L8, L12, L32, L200, L204, B139-G, Campaigns 1, 1′, 1″),
`docs/THE_DESTINATION_LEDGER_2026-09-06.md`. 172 arcs carry "chiral" in their claim line; the ones not cited are
the census's dynamics-of-chirality arcs (B944) and the CP-sign arcs, whose statements are unchanged by this map.
