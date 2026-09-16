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
| Pantev–Wijnholt: net chiral(R) = χ(M, ∂⁺M), the Euler characteristic of the part of the boundary where the Higgs field's charge points outward | a disc-type ∂⁺ | annular on the object (χ = 0) by its eight cusp symmetries; a disc needs a cusp-fixed weight on a non-self-dual holonomy (L204) — no such point on any computed deformation: the fixed-vector locus along V₁₀ is the Sp(8) family (B1352, §6d) | B1277 addendum, `LITERATURE_SWEEP` §1 |
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
| **O4 — the singular G₂ closing** | the destination's item 1: the conical G₂ geometry over the object's E₆ locus, where chirality is a 7-dimensional index (Acharya–Witten), not an h¹ of m004 — **local model named: the cone over CP³/2T (B1355, §6g)** | the only place C3 can still come from, given W-closed, W-flat-G₂ and the two new walls; I-26 is earned or refuted there |
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

## 6c. The handedness bit at the word level (chat1's handoff of 2026-09-08, received 2026-09-09)

Chat1 asked whether the mirror choice inside the generative rule (a ↦ ab against a ↦ ba) pays the chirality bit, and proved it does not: a ↦ ba, b ↦ a is c_{a⁻¹}∘(a ↦ ab, b ↦ a), an inner automorphism away, so both induce the same map (z, x, xz − y) on the character variety; inversion a ↦ a⁻¹ is not inner and does act. The rule has one handedness PROPERTY, not a choice: its abelianisation [[1,1],[1,0]] has det −1, and on Aut(F₂) the Goldman-bracket multiplier is that determinant (Poisson for +1, anti-Poisson for −1; Goldman's dichotomy, made explicit). This is C1/C4 material — the sign, which the record already places at the closing (B286, B289: forced by the oriented slope, not object-derivable; B1184: unutterable) — and it does not touch C3, the count, which is where B1350 and the walls of §1 live. **One rhyme with this branch's own result:** the det −1 element is the half-deck h of the tower, and the tower's law's positive half rests exactly on its orientation reversal — odd powers of h reverse the fibre's orientation, which is why they fix the carriers and even powers do not (B1304 addendum §2–2′). The four certificates re-run here, all exit 0. Chat1's Q8 candidate (the quaternion character (0,0,0), the node of the Markov surface κ = −2, whose image group Q₈ is the kernel of 2T → ℤ/3) is gated here and parked: (0,0,0) does not satisfy the figure-eight relator — a knot group's two generators are conjugate, conjugates in Q₈ are ±g, so tr(ab) = ±2 ≠ 0 — it is a point of the fibre's F₂ character variety, not of the object's. Its two halves are banked separately (B1042, H114).

## 6d. The fixed-vector locus along V₁₀ (B1352, 2026-09-09)

B1351 stated the count in the seven-dimensional frame: on the cusped object N(27) = −χ(∂⁺M; 27) per weight, and only a
cusp-fixed weight has a boundary condition to choose — so a net count needs a cusp-fixed weight on a non-self-dual
deformation. B1352 computed that locus. From each genuine V₁₀ point of §6b the augmented Newton (relator + μv = v,
λv = v; damping 10⁻⁵⁰) converges quadratically to a point of the fixed-vector locus, and the point is an **Sp(8) point**:
self-dual (defects 10⁻⁵³), cyclic 27, exactly three cusp-fixed weights — the Cartan directions eᵢ ∧ fᵢ of Λ²₀(8) that every
Sp(8)-valued representation carries — h¹(27) = h¹(27̄) = 3, N = 0 (2000 bits). Exactly (ℚ(ω), then two primes): the V₁₀ of
the 42 is the only θ-odd direction that keeps the three cusp-fixed vectors of ρ₀ to first order, and every formal V₁₀
branch constructed loses them at order 4 (order 2 on generic branches) — the order at which the deformation stops being
self-dual (the trace defects scale as t⁴ between two genuine points). **The window is void on every computed deformation:**
at the non-self-dual points there is no boundary condition, and where there is one the count pairs. B1268's never-finished
stage (b) along V₈ (geometric point) stalls under the 10⁻⁵⁰ damping too. Registered: whether a tuned formal branch keeps a
fixed vector beyond order 4 (B1352 §6). O1 closed with its mechanism; O4 (the singular G₂ closing, B1353) and O5 stand.

## 6e. The isolated enhancement point, made finite (B1353, 2026-09-09)

Main's E70 scoped B1259: every element of SO(7) fixes a line, but a *group* can have an isolated fixed point, so the
flat class was not closed by the element lemma. B1353 closes it by the strata. In a flat G₂ orbifold the E₆ locus is the
fixed 3-plane P of 2T ⊂ SU(2)_R, its stabiliser in G₂ is SO(4) on Im ℍ ⊕ ℍ, and a point of P is an isolated fixed
point of its stabiliser Γ_p exactly when Γ_p's image in SO(3) is non-cyclic. All such Γ_p ⊂ SO(4) with kernel 2T are
enumerated by Goursat (R ∈ {2T, 2O}: fourteen groups from D*₂ × 2T of order 96 to 2I × 2T of order 1440; B1084's Ĝ is
(D*₂, C₄; 2O, 2T) and its apex *is* an isolated fixed point of the group). In every one, **every A-type stratum through
the apex contains a line of the E₆ plane** — an A-plane is axis(l) ⊕ {x : l x = x r} and P ⊃ axis(l) — so the
transversal A₁/E₆ collision that Acharya–Witten's E₇ points need never occurs (A₁/A₁ planes do meet only at the apex;
216 of B1084's 435 pairs). The literature's rule closes the rest: chiral fermions arise where an ADE locus passes
through an isolated conical point "not just an orbifold singularity" (Witten 2001), "worse-than-orbifold"
(Acharya–Witten 2001), orbifold points being "modelled on Calabi–Yau singularities" (Acharya–Gukov 2004); the orbifold
link S⁶/Γ_p has b₂ = 0 (no U(1) inflow) and E₆ is anomaly-free (no detector). **O4 stands as the curved conical G₂
closing and only that**: the three E₇ points are not orbifold points. Registered: stabilisers not preserving the E₆
plane (several E₆ branches through the point).

## 6f. The maximal persistence (B1354, 2026-09-09)

B1352's registered residue — whether a tuned formal branch tangent to V₁₀ keeps a cusp-fixed vector beyond order 4 — is
answered: yes, and every such branch is formally self-dual. The obstruction-class tower (the newest class shifts the
obstruction only through the non-keeping classes) is a polynomial system decided by Gröbner bases over two primes: the
order-4 solution family is linear (V₄ = V₈ = V₁₆ = 0, V₆ tied to V₁₄), the higher orders are affine and free, the climb
reaches order 8 with all three vectors kept. Along those branches the traces move at first order but the self-duality
defects vanish through order 8; along the greedy branch they appear at order 4, where the fixed vectors are lost. So on
the object the two conditions a net count needs exclude each other along V₁₀ at every order reached: **cusp-fixed weights
and self-duality are one condition.** O1's residue is void; O4 and O5 stand.

## 6g. The E₇ point made explicit (B1355, 2026-09-09)

O4 has a local model. Acharya–Witten's two families of chiral cones, asked which reaches E-type: the hyperkähler-U(1) family
(the cone on WCP³_{N,N,1,1}) needs a U(1) acting triholomorphically on ℍ/Γ and, in that explicit form, stops at cyclic Γ (the
centraliser of 2T in Sp(1) is ±1); the twistor family does not. *[Correction of record 2026-09-15 (main B1413, the audit lane): AW's
§2.3 Kronheimer unfolding of E₇ reaches E₆ with one chiral 27 of charge 1 and an undescribed topology — a companion-free second local
model; "A-type only" was too broad.]* With M = S⁴/2T the twistor cone is the Bryant–Salamon cone over CP³ divided by 2T acting on
one quaternionic factor: the twistor line over one pole is fixed by all of 2T with normal action 2T ⊂ SU(2) — the E₆ locus — the
line over the other pole is fixed by −1 — an A₁ locus — and they meet only at the apex, a conical singularity whose link CP³/2T has
b₂ = 1 with the E₆ line's class of degree 1. Witten's inflow, the mixed U(1)·E₆² anomaly equal to ∫_U w ≠ 0, forces chiral
E₆-charged matter with U(1) charge at the apex; the literature's count is one 27 per point (E₇ ⊃ E₆ × U(1)). This is the
configuration B1353 proved impossible in the flat class, realised in the curved one, with the object's own group. The three
faces meet in it: 2T (arithmetic), the twistor cone (geometry), the inflow (quantum). What remains is global: a compact closing
whose E₆ locus carries three such apexes (L212).

## 6h. The three on Y₃ (B1356, 2026-09-15)

The "three" of O4, placed on the tower. On the flat Y₃ (B1273) the deck σ fixes exactly one closed geodesic — the lift of the
knot — and the descent ⟨Π, σ⟩ = P2₁3 has one cone circle and no 2-fold axes: Y₃/σ is Thurston's Euclidean figure-eight orbifold
S³(4₁; 2π/3), with holonomy T = 2T/±1 (the deck completes Hantzsche–Wendt's V₄ to the object's McKay group modulo its centre). A
deck-symmetric triple of E₇ apexes is therefore a free orbit off the knot, and the object's own closing has one apex. Witten's
sum rule under the deck says what the C-field U(1)s see: an invariant class gives equal charges and 3q = 0; in the descent the
fixed circle does not compensate, because it is not a singularity of the cover (the harmonic form is smooth across it and the torus
around the knot integrates to zero). So the object's own closing carries one 27 neutral under every C-field U(1), and the cover's
three are told apart by the classes on which the deck acts as its two-dimensional irreducible — exactly two U(1)s or none — with
charge triples in (1, 1, −2) + 3A₂ (the sum rule with the Z₃ global form), the deck orbit of (1, 1, −2) being 3 × the weights of
the 3̄ of the SU(3) whose Weyl group permutes the apexes. Along the knot the G₂ structure forces the deck to act on the E₆ fibre
as the centre of SU(3) (det 1 on the normal ℂ³), so the local group is 2T × Z₃ and ℂ³/(2T × Z₃) has the E₆ plane and two A₂
loci through the knot — a collision E₆ ∩ A₂ ∩ A₂ the cover does not have — with crepant Betti numbers (15, 5): ten non-compact
divisors (the E₆, A₂, A₂ Cartans) and five compact ones. And in the global-quotient class the A₁ companion of B1355 is unavoidable:
on S⁴/Γ the −1 of an E₆ point fixes the antipode; CP²/Γ has no E₆ point; Hitchin's theorem makes these all the global quotients of
manifolds. The three faces: the descent is the one Euclidean member of the figure-eight cone family (geometry); the charge lattice
is the Eisenstein A₂ with the deck as ω (arithmetic); the deck is the SU(3) centre on the fibre and the inflow sees the generations
only through the irreducible pair (quantum). The compact closing is still not constructed (L212, L213).

## 6i. The object's own Joyce orbifold (B1357, 2026-09-15)

The compact flat background the ingredients determine without a choice: the E₆ fibre ℂ²/2T compactified by the Hurwitz torus (2T's
unit-group lattice, unique up to scale), the Hantzsche–Wendt group acting on T³ and on the fibre by the lifts of its holonomy (the
SO(4) ⊂ G₂ of B1356; on the torus the twist is forced into 2T, so there is no E₆ diagram flip), the deck as the tower's. Exact
census: T⁴/2T has 48 singular points in orbits E₆ + D₄ + A₁ + 4A₂ (χ = 5, resolution a K3, χ = 24); the 7-orbifold has one invariant
spinor (N = 1) and four disjoint loci — E₆, SO(8), SU(2) on three copies of Y₃ and SU(3) on T³ — with b₂ = 0, b₃ = 4. The three
Y₃-loci are rigid (the holonomy V₄ fixes no direction of the hyperkähler triple): unbreakable gauge groups, no adjoint matter, pure
N = 1 super-Yang–Mills; the T³-locus is resolvable (b₂ → 2, b₃ → 10). The descent is the object's own closing: E₆, SO(8), SU(2) on
S³(4₁; 2π/3) and SU(3) on T³/Z₃, b₂ = 0, b₃ = 2; along each cone circle the deck enlarges the local group — 2T × Z₃ (E₆, inner, kept),
Z₆(1,2,3) (SU(2)), SL(2,3) (SO(8): triality folds it to G₂), Z₃ × Z₃ (SU(3)) — and its order-6 coset elements fix closed 2-tori: two
compact A₂ loci, one joining E₆–SU(2)–SU(3), one joining E₆–SO(8)–SU(3) along the cone circles. For the chirality bit the decisive
line is the C-field: the deck's two-dimensional irreducible occurs on 3-forms only, never on 2-forms, in the background and in its
resolution — the U(1)² that distinguishes B1356's three generations is not available from the flat closing; it can only be born with
the apexes. Vector-like throughout (B1351). The touching design — the SU(2)-copy of Y₃ brought to the E₆-copy at three deck-related
points with B1355's cone as the local model — is registered, not constructed (L213 (iv)).

## 6j. The E₆ apex family (B1358, 2026-09-15)

O4's local models, as a family: the twistor cones of S⁴/(2T × Γ_R), Γ_R a finite subgroup of the second Sp(1). Computed for Γ_R ∈ {1,
Z₂, Z₃, Z₄, Z₆, Q₈, 2T}: the E₆ locus at the first pole always; the companion at the second pole {±1}·Γ_R — of even order because the
−1 of 2T is there whatever Γ_R is: A₁, A₃, A₅, D₄, E₆, never A₂ (the SU(3) locus of the object's background can never be the companion);
mixed A-loci over the cone circles of S⁴/Γ whenever Γ_R shares an eigenvalue with 2T (they are ADE by the G₂ argument: the cone over a
fixed line is an associative 3-plane whose pointwise stabiliser lies in an SU(2)); no fixed point off the loci. Against B1357's
background only Γ_R = 1 — B1355's cone — fits with nothing else through the apex, and its companion is the SU(2) copy of Y₃ at fibre
distance ½; the apex on the knot (Γ_R = Z₃, forced by the deck's lift) has an A₅ companion and four A₂ branches the background does not
have. At B1355's apex the E₆ line maps to its link with degree 1 and the A₁ line with degree 12, so Witten's mixed-anomaly
coefficients are in the exact ratio E₆ : SU(2) = 12 : 1 — the SU(2) copy receives chiral doublets with charge-weighted count a
twelfth of the E₆'s. The one consistency condition geometry does not settle: the doublet count per apex, since three apexes with an odd
count each would give SU(2) Witten's global anomaly. The destination's item 1 is one picture within the twistor family: the object's own Joyce orbifold with
its SU(2) copy of Y₃ brought to touch its E₆ copy at three deck-related points (L213 (iv)), each B1355's cone, the 27s told apart by
the apexes' own U(1)s (B1356). *[With AW's §2.3 E₇ unfolding as the local model instead (correction of record 2026-09-15), the three
apexes sit on the E₆ copy alone, no companion and no doublet parity — at the price of a topology AW do not describe.]*

## 6k. The K3 alternative, decided (B1359, 2026-09-15)

The fibre compactification of the E₆ singularity is the torus of the Hurwitz order or a K3 with a symplectic 2T; the orbit types of
the 2T action are fixed by the per-order fixed-point numbers through a Burnside count (computed on the Hurwitz units, checked on
every element). For K3 (Nikulin: 8, 6, 4, 2) exactly two configurations survive — E₆ + D₄ + A₅ + 2A₂ and 2E₆ + A₃ + 2A₂, Xiao's #37
and #38 for T₂₄ — and neither has a point of stabiliser ±1; for the torus (16, 9, 4, 1) the count returns B1357's E₆ + D₄ + A₁ + 4A₂
once the origin is required. Since the only companion of B1355's apex that fits (B1358) is an A₁ locus, no K3-fibred background
carries the three-generation design: it lives on the Hurwitz torus. The K3 background itself stays conditional on a K3 with both
the symplectic 2T and the Hantzsche–Wendt twist.

## 6l. The companion-free apex (B1360, 2026-09-15)

The second local model of O4, AW's E₇ → E₆ Kronheimer unfolding (their §2.3; the correction of record on B1355), described enough
for the design. The cone is the total space of Kronheimer's E₇ family over the omitted node's D-term: the node beyond E₆ has index 1
and the roots orthogonal to its coweight are exactly E₆'s 72 (computed), so the generic fibre is the partial resolution with the E₆
configuration collapsed, smooth elsewhere, retracting onto the one surviving curve (H₂ = ℚ, computed); the singular set of the cone is
the E₆ locus and the apex — no companion, no cone lines. The link is the S²-family of fibres (the bundle associated to the Hopf
fibration by the hyperkähler circle) glued at infinity to S³/2O: Mayer–Vietoris gives b₂ = 1, and the E₆ link's pairing with the
generator is the Euler number of the normal of the surviving curve at the E₆ point twisted by the circle, which acts on the tangent
cone ℂ²/2T through the centraliser of 2T in U(2) — the scalars (computed) — hence non-zero. Witten's inflow applies verbatim; the
argument reproduces the known structure of AW's SU(N) cones (b₂ = 1; the circle rotating the core P(1, N) with weight N − 1, trivial
exactly when there is no locus; the orbifold degrees 1/N², 1). For the design: three such apexes on the E₆ copy of Y₃, as a deck
orbit, give B1356's three 27s with the sum-zero U(1)² and the charges 3 × (3̄ weights), with no SU(2) copy touched and no doublet
parity. Open: the integral normalisation of the generator (the charge against the Z₃ global form), the compact closing.

## 6m. The deck's texture (B1361, 2026-09-15)

The flavour face of the design. B1356's apex charges (1, −2), (1, 1), (−2, 1) form an equilateral triangle, so the only E₆ cubic
invariant under both apex U(1)s is 27₁27₂27₃: with the Higgs in the apex 27s the tree-level mass matrices are complex symmetric with
zero diagonal — exactly B1273's texture from the three flat classes of Y₃ (three distinct characters, one product-trivial triple) —
and the bound B1273 proved is an identity: e₂(MM†) = (tr MM†/2)² for every hollow complex symmetric 3 × 3 matrix (symbolic), hence
σ₁ = σ₂ + σ₃, m₃ = m₂ + m₁, refuted by factors 273, 50, 17 at low scale (136, 43, 17 at B1273's). With a neutral Higgs no tree-level
Yukawa survives; the deck alone would allow four cubics — it is the U(1) pair that tells the generations apart which forbids the
diagonal. So the design says of its own flavour: hierarchy is not tree level; it lives in the sector that breaks the apex U(1)s
(Witten's axionic mass, the charged instantons), a Froggatt–Nielsen-like structure with the deck's charges (L213 (vii)). **B1362:** and
not a small one — a deck-symmetric Yukawa is a symmetric circulant with a degenerate pair, and Weyl's inequality on the hollow tree
level gives ‖E‖ ≥ (m₃ − m₂ − m₁)/3 for the U(1)²-violating part: a third of the top, bottom and tau Yukawas, attained numerically.

## 6n. The level mismatch resolved (B1364, 2026-09-15)

The gauge face of the design. On the E₆ root system (SO(10) × U(1) coordinates) the Standard Model's centraliser is SU(2)_β × U(1)²,
β the SO(10)-singlet weight of the 16 (dimension 5, B1269's c(s) recomputed); the centraliser of SU(2)_β is SU(6) (the 30 roots
orthogonal to β); a Q₈ inside SU(2)_β has the same centraliser (no invariants on the 2 or the 3); and an order-4 element of the U(1)²
kills exactly the eight Standard-Model roots among SU(6)'s thirty. Y₃'s fundamental group F(2,6) surjects onto Q₈ in 24 ways (its
holonomy V₄ lifted), each deck-invariant up to conjugation in 2T, and H₁ = (ℤ/4)² has 12 order-4 characters permuted by the deck
without fixed points. The flat connection (Q₈ in SU(2)_β) × (an order-4 character) therefore leaves exactly SU(3) × SU(2) × U(1)_Y × U(1)′
— the 13-dimensional minimum B1269 proved no flat connection can beat — with the deck broken by the character, as B1362 requires.
"No SM lines on Y₃" (B1277, B1300) is true of the alphabet, the sign characters carrying generations by h¹; the apex design carries
its three 27s at points, and they decompose as full 27s: three generations, three 5 + 5̄ pairs, three singlets. The descent cannot
follow (order-3 characters leave at least 17). So the three and the breaking live on the same level, the cover Y₃, and O4's design
has a complete gauge and matter structure: E₆ on Y₃ with the Hurwitz-torus background (B1357), three apexes (B1355/B1360), the
sum-zero U(1)² (B1356), the Q₈-plus-order-4 line (B1364), and a U(1)²-breaking sector owing the hierarchy (B1361–B1362), the
5 + 5̄ masses and the doublet–triplet splitting (B1300). What it is not: a manifold.

## 6o. The bulk of the line, and the neutrino obstruction (B1365, 2026-09-15)

The line's four-dimensional content, computed. The unbroken U(1)′ is the Cartan direction γ orthogonal to the Standard Model, to Y
and to β; on the 27's eleven field types it is B1283's γ exactly (Z′ = −6γ: 4 on Q, u^c, e^c; −2 on d^c, L; 10 on ν^c and N; −8 on
H_u, D; −2 on H_d, D̄), and γ = (2√15/3)·Q_η with Q_η = √(3/8)Q_χ − √(5/8)Q_ψ — the η model, the U(1) that survives when E₆ breaks
directly to a rank-5 group by Wilson lines (Witten 1985; Langacker), family-universal here (B1283's family part came from Y₉'s
flavons); β is the inert U(1)_I. The torus exp(u(1)²) has twelve order-4 elements; four reach exactly the Standard Model and all
four square to one involution whose −1 roots are the colour triplets (3,1)_{∓1/3} of SU(6)'s 5 ⊕ 5̄. By Fox calculus on
⟨a, b | φ³(a) = a, φ³(b) = b⟩ — with b₁ = 0, the three sign characters' h¹ = 1 and the twelve order-4 characters' h¹ = 0 as controls —
the bulk H¹(Y₃; 78_ρ) of every SM-reaching line is three neutral moduli (Ad ρ_{Q₈} = the three sign characters; W = κφ₁φ₂φ₃; three
explicit one-parameter families of flat connections through the Q₈ point along which SM × U(1)_η stays unbroken) and one vector-like
(3,1)_{−1/3} ⊕ (3̄,1)_{+1/3} pair with U(1)_η charge ∓2 and no tree-level mass source; the (2,20) sector is empty for every line and
character (the translations act by −1 on the 2; no character of (ℤ/4)² is −1 on all three translation classes). Then the vacuum: the
only E₆-charged Standard-Model singlets in the design are N and ν^c, both γ = −5/3, and the bulk's singlets are neutral, so the
U(1)_η D-term on singlet VEVs vanishes only at the origin — nothing breaks U(1)_η above the soft scale. U(1)_η charges ν^c (unlike
the E₆SSM's U(1)_N), so the Majorana mass is forbidden, there is no seesaw, and the E₆ cubic's single coupling (B1276) ties
L ν^c H_u to Q u^c H_u: **the neutrinos are Dirac at the up-quark masses; the three-apex design is excluded as it stands.** The remedy
is a 27̄ sector — anti-apexes (nine apexes, since the deck is free on them) or the tower's h¹ pairs on an E₇/E₈ locus — registered as
L215. The deck: no combined line is E₆-conjugate to its deck image (the 27-character differs for all 288), so the three apexes are
made inequivalent by the line alone.

## 6p. The sign is E₆'s (B1366, 2026-09-16)

The last loophole of §6o closed. su(3)_c must be a root A₂ of E₆ (27 → 3·3 + 3·3̄ + 9·1 has embedding index one) and su(2)_L a root A₁
commuting with it; the 120 A₂'s of E₆ form one Weyl orbit, the centraliser of one is A₂ × A₂, every one of its six positive roots gives
27 → 6·2 + 15·1, and the 720 commuting pairs form one orbit. Hypercharge lives in the three-dimensional commutant Cartan and must give
the 27 the Standard Model's multiset; exactly three vectors do — one for each colour-weak singlet chosen as e^c — and the reflections of
the residual su(3)_R permute them: the Standard Model is in E₆ once, and every "flipped" reading is a renaming. For each, the roots
commuting with the SM and Y-neutral are one pair ±β, the two singlets differ by β and carry equal non-zero γ, and the 78's SM singlets
have γ = 0. So the D-term sign theorem, the absent seesaw and the light exotic triplets are properties of E₆ with matter in 27s — the
object's E₆ (B1268) and the object's 27 (B1276) — for any line and any hypercharge; only 27̄s change the sign (L215).

## 6q. The doublet–triplet pincer: the apex route closed (B1367, 2026-09-16)

The E₆ cubic in trinification form, det L + det Q + det Q^c + Tr(Q L Q^c), names its own pairings: N with (H_u, H_d) and with (D, D̄),
ν^c with (L, H_u) and with (D, d^c), each pair one invariant with equal magnitude. With n copies of the 27 and any symmetric coupling
tensor, the doublet block (rows H_u; columns H_d, L) and the triplet block (rows D; columns D̄, d^c) are G ⊗ S_D and G ⊗ S_T with the same
generation matrices, so light up-Higgs doublets = light exotic triplets in every vacuum where the Standard-Model singlets take VEVs —
9 300 configurations (n = 3, 4, 6; fifteen coupling patterns including the deck's hollow one; every VEV support at n = 3), zero
exceptions, and every vacuum with a light Higgs has a light D, which decays the proton through the cubic's diquark and leptoquark
couplings (B1276 §3). Only E₆-breaking couplings acting on the matter split the blocks: a Wilson line on bulk modes does (B1302's
one-triplet vacua on Y₁₂); point-localised 27s never see one (full 27s; holonomy factors are one E₆ element per 27; the U(1)²-breaking
sector is E₆-neutral). So every closing whose E₆-charged matter is at points — the three-apex design and all its anti-apex extensions —
is excluded, with or without 27̄s, whatever the line. Chirality (points, or the cusped object's ends) and splitting (bulk) meet only for
chiral bulk matter: the cusped object's Standard-Model-reaching connections and their cusp-fixed weights, L216.

## 6r. The object's own Standard-Model connections: the last door closed in the seat's frame (B1368, 2026-09-16)

A flat E₆(ℂ) connection of m004 leaving the Standard Model unbroken has its image in c(SM) = SL(2)_β × ℂ*² (B1366): a representation
of the knot group into SL(2)_β — the geometric one or any point of the character variety — times a character on (Y, γ); the family is
two-complex-dimensional once the 22 non-SM roots of SU(6) carry non-trivial characters. Its bulk sectors are SL(2)_β-spins times
characters: 78 = (3,1) ⊕ (1,35) ⊕ (2,20), 27 = (1,15) ⊕ (2,6̄). Exactly over ℚ(ω): the Riley representation satisfies the relator, the
longitude has trace −2 (Calegari) and acts as −(unipotent); the Alexander polynomial is z² − 3z + 1 (roots φ^{±2}) and the geometric
representation's twisted Alexander polynomial z² − 4z + 1 (roots 2 ± √3); h¹(Ad) = 1. Cusp-fixedness: spin-0 sectors only at z = 1
(trivial, no Higgs field, N = 0); spin-½ sectors never for the geometric representation (the longitude's eigenvalue −1 twice); spin 1
once (the neutral deformation). The frame theorem: the 10 of SU(5) is spin 0 in the 27 and spin ½ in the 78, the 5̄ the other way, so
in either frame one half of every generation is never chiral for any flat connection of the family. The λ-parabolic points where the
spin-½ half could be cusp-fixed are eight — the SU(2) dihedral representations (unitary) and the golden reducible points — at most half
a generation. L216 closes in the seat's frame; the disc-convention adjudication (R23) is the physical-bridge lane's. With §1's walls,
B1351 and §6q: the E₆ route from m004 has no chirality mechanism compatible with the Standard Model in any frame the record has.

## 6s. The family in the Standard-Model frame: the free-cusp theorem and the parity census (B1369, 2026-09-16)

The owner's question after the verdict — physics from the family, not the object — in the seat's frame. On a member with several
cusps a spin-0 sector is cusp-fixed on cusp c iff its character is trivial on the peripheral subgroup P_c; if the image of P_c in
H₁(M; ℚ) has full rank b₁ the character factors through the finite group H₁/P_c, has finite order, is unitary, has no Higgs field and
no index. With §6r's spin split, a chiral generation from bulk matter with the Standard Model unbroken needs a *free cusp*, rank
P_c < b₁ — decided by homology, for every flat connection. Census of B1186's 112 members: 77 have no free cusp (all 54 one-cusped
members with b₁ = 1; 23 multi-cusped members with every peripheral rank equal to b₁, m202 and s959 among them — both peripheral
subgroups of m202 have index 7 in ℤ², so a cusp-fixed sector has χ⁷ = 1, and the spin-½ half is cusp-fixed with the Standard Model
unbroken only by finite-order characters: no Higgs field, no index). The 35 members with a free cusp carry 83; there the region-swap
lemma (fc R71, §6c–§6d; B1417) is run in its general form — an isometry fixing the cusp and acting by −1 on the free classes ann(P_c)
maps {F > 0} onto {F < 0} for the leading cusp mode F of every Higgs form, whatever its torus action, so χ(∂⁺) = χ(∂⁻) = 0 — with the
isometries' exact action on H₁ computed from the canonical retriangulation (the combinatorial automorphisms, a new instrument matched
against SnapPy's isometry counts, b₁, peripheral ranks and cusp maps). Parity closes 79 of the 83 free cusps, four of them only by
orientation-reversing isometries. Four cusps on four members remain — o10_150688, o10_150708 (cusp 0), o10_150716, o10_150725
(cusp 1) — where every isometry fixing the cusp acts by +1 on a free class; each cusp lattice has a unique shortest dual vector, so
the partition is annular unless the harmonic form's leading coefficient vanishes, which only the form's cusp expansion (or the
isometries' affine torus action) decides. 108 of 112 members closed; the residual is sL-1's. `frontier/B1369_the_siblings_in_the_sm_frame`.

*Addendum (B1370, the same day).* The four residual cusps developed from the tetrahedra shapes and every fixing isometry's affine
action read off — translation parts included; on all four, for every Higgs class, the unique shortest dual vector is an allowed
mode (half-period translations kill some higher shells, not the first), so the leading cusp mode is cos(2πk·x + φ) and the
partition annular unless the harmonic form's coefficients at the first 4, 2, 4, 2 allowed shells all vanish. The residual is one
Fourier coefficient of a harmonic 1-form per cusp — the cusp expansion of a harmonic form, or the members' Bianchi-type forms.
`frontier/B1370_the_residuals_leading_mode`.

## 6t. Door 2 — the doublet halves: the mixed frame closed at the cusp (B1372, 2026-09-16); the web seat's package verified (B1371)

The exclusions of §6r–§6s pass through the spin-0 half of a generation in each matter frame. The one reading that evades it takes both
halves as SL(2)_β-doublets — the 10 from the 78's (2,20), the 5̄ from the 27's (2,6̄) — so that the non-abelian part of the connection
carries the Higgs data on both. Charge arithmetic at the cusp closes it: a doublet sector is cusp-fixed when a joint eigenvector of the
peripheral holonomy has total holonomy 1, so the character must equal an eigenvalue of ρ(p)^{∓1}; with a non-unitary eigenvalue the 10
(γ = 1, three Y-types) forces Im s = 0 and Im t = ±L while the 5̄ (γ = ⅓) forces Im t = ±3L — never both (0 of 32 sign patterns); with
a unitary eigenvalue e^{2πiθ} the fifteen congruences have solutions only for 4θ ∈ ℤ, and at θ = ±¼ the eigenvector choices are never
uniform (the 10 against the 5̄, or {Q, d^c} against {u^c, e^c, L}), so where the abelian Higgs field vanishes the pieces have opposite
chirality. Parabolic cusp holonomy (the hyperbolic structure on every member) and central holonomy make every doublet sector
vector-like. On m004 the order-4 points of the character variety are the four SU(2) dihedral representations, unitary. Door 2 is
closed on m004 and on the 77 members without a free cusp; it survives only at order-4 points with non-unitary holonomy on the 35
free-cusp members, if such points exist. The web seat's post-closure package (2026-09-15), verified the same day with this bench's own
code, brings no new door: its routes to zero are the record's or orthogonal to the seven-dimensional frame, and its one negative that
fails (the Sol boundary m004(0,1) has irreducible SU(2) representations) concerns no route of this map. `frontier/B1372_the_doublet_halves`, `frontier/B1371_the_web_seats_post_closure_package_verified`.

*Addendum (B1373, the same day).* Door 2's residual followed along the geometric path: on all 83 free cusps, the cone-manifold
continuation to a peripheral eigenvalue ±i reaches the point on 132 of 166 cusp–curve pairs with the other eigenvalue non-unitary every
time (Theorem B), and degenerates before it on the rest (34 ideal points of the real path: 23 near cone angle π, 11 at 2π/3). No order-4 candidate on the
deformations of the hyperbolic structure; what remains lies off the real path or on other components of the character varieties.
`frontier/B1373_the_order_4_points_on_the_geometric_components`.

## 7. Consequence for the destination ledger

The chirality bit (item 1 of `docs/THE_DESTINATION_LEDGER_2026-09-06.md` §5, D3's carrier) is now excluded from:
every closed closing (W-closed), the mirror quotient (W-mirror-quotient), the cusped object's abelian sector
(W-abelian), its elliptic SL(3) components on every cover (W-W1W2), and its E₆ deformation germ together with the fixed-vector locus along V₁₀ (W-θ-odd; B1350, B1352). It can
still come from the singular G₂ closing (O4 — the curved cone, not a flat orbifold point: B1353; three of them only on the cover Y₃, told apart only by the deck's U(1)², while the object's own closing carries one neutral 27: B1356) or be supplied by the observer (O5). **The record's statement is
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
