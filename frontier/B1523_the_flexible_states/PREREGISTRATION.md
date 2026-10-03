# B1523 — PREREGISTRATION: THE FLEXIBLE STATES — which word states carry a projective family at their hyperbolic point, and on which of them no symmetry dualises it (sL-10 item 6, "all allowed, not just m004")

**Sealed before `census.py` runs.** At the seal, dim H¹(M; v) and the isometries' signs have been read only on the controls:
- the literature's m004 = b++LR, Daly's L²R² = b++LLRR and R²L ≅ b++LLR;
- the planted two-cusped m129, the Whitehead link.

On the 536 census manifolds, `controls.py` has read only what is not the outcome:
- the enumeration;
- SnapPy's isometries against the words' prediction;
- the holonomy: relators, the cusp frame and the cusp shape in both routes;
- the theorems dim H¹(M; ℝ) = 1 and dim H¹(M; so(3,1)) = 2 (route R).

**Source.**
- The owner (2026-10-02): *"… all oallowed not just m004, choice might be golden"*. The full message is quoted in sm:B1522's
  PREREGISTRATION.
- sm:B1522 §6 registered this arc: *"which word states are projectively flexible at the hyperbolic point, i.e. where can a
  Ballas-type family exist?"*. It is sL-10 item 6 in OPEN_LEADS.
- Main's B1455 (and sm:B1520) found on m004 that the symmetries act on Ballas' family through one bit, whether they invert the
  longitude, and that this bit dualises. This arc asks where that bit exists at all.

## 0. Seen first, and PRIOR ART:

**The repo sweep.** Run with `scripts/checks/prior_work.py` on 2026-10-02, against these heads:

| head | commit |
|---|---|
| main | `8d1c1329` |
| the audit lane | `7b088f50` |
| this branch | `07faac0a` |
| seat/determined-hopper | `7cda35aa` |
| seat/magical-wright | `0043be2b` |
| seat/outside-bench | `13d2c5b6` |
| seat/paper-review-verification | `5d58b935` |
| seat/physics-seat-evaluation | `659487bb` |
| sep16-branch | `3205984b` |

The terms searched were:
- "projectively rigid", "projective rigidity", "infinitesimally projectively";
- "Heusener", "Daly", "Ballas", "convex projective", "properly convex";
- "H^1(M; v)", "longitude-inverting", "family-dualising", "flexible state";
- "amphichiral", "amphicheiral", "Johnson–Millson".

Every hit that bears on the question was read:
- **Main's B1455** and its handoff `CC_TO_CODEX_AND_SM_2026-10-02_THE_MIRROR_ON_THE_HARMONIC_FAMILY.md`. This is the only file on any
  head that says "longitude-inverting". On m004 the mirrors fall into two classes by the longitude: those keeping it fix every
  ρ_q, and those inverting it send ρ_q to ρ_{1/q}. So the symmetries act on the family through one bit, and that bit dualises.
  - The longitude there is the knot longitude, which is m004's fibre boundary.
  - B1455 states this for m004 only. This arc's "longitude rule" is that statement tested on every word state, with the fibre
    boundary as the longitude.
- **sm:B1520** (this branch): m004's sign table on the v-class, read through the cusp. −I and diag(−1, 1) give −1;
  diag(1, −1) and I give +1. C5 reproduces it.
- **sm:B1522 §6** registers this arc. **sm:B1521** (GENESIS v1.3 §8) records that the family exists off its hyperbolic point
  only for m004.
- **B659's novelty dossier** (`SWEEP_RESULTS.md`, all heads) cites Daly arXiv:2411.04431 and Daly's computer-assisted fillings
  paper. It computes nothing on word states.
- **sm:B1511 / sm:B1515** cite Daly, Ballas and Heusener–Porti for m004's family. They do not compute rigidity elsewhere.
- **The audit lane's** `AFFINE_BACKGROUND*` and `CANONICAL_*` reports concern the affine sphere on m004's Ballas family. On it,
  the knot longitude has characteristic polynomial (X − q)³(X − q⁻³).
- **`papers/sl4_dehn_filling`** (all heads) treats a different SL(4) component of m004, with finite-order meridians, and notes
  that Ballas' family is boundary-unipotent.

**No head computes infinitesimal projective rigidity, or an isometry's sign on H¹(M; v), on any word state other than m004.**

**The literature.** Each item below was read on 2026-10-02 at the place cited.
- **M. Heusener and J. Porti**, *Infinitesimal projective rigidity under Dehn filling*, Geom. Topol. 15 (2011), arXiv:0908.2863:
  - Cor. 5.4: a one-cusped M is rigid rel cusp iff dim H¹(M; v) = 1, and in general dim ≥ the number of cusps.
  - Lemma 5.5 and Remark 5.6: for a parabolic ℤ², the restriction to two slopes is injective unless they meet at angle π/3.
  - Def. 7.1: a rigid slope.
  - Remark 8.1: the figure-eight knot's longitude is a rigid slope.
  - Prop. 1.9: all but finitely many punctured-torus bundles of tunnel number one are rigid rel cusp.
- **S. Ballas, J. Danciger and G.-S. Lee**, *Convex projective structures on non-hyperbolic three-manifolds*, Geom. Topol. 22
  (2018), arXiv:1508.04794:
  - Def. 3.1 and Thm. 3.2: rigid rel ∂M implies ρ_hyp is a smooth point of Hom and of the character variety.
  - Thm. 1.3: nearby properly convex structures with each cusp opened.
  - **Remark 3.3:** *"In future work, we hope to determine exactly which manifolds of the Hodgson–Weeks cusped census are
    infinitesimally projectively rigid rel boundary."*
- **S. Ballas**, *Constructing convex projective 3-manifolds with generalized cusps*, arXiv:1805.09274:
  - Thm. 0.2: rigid rel ∂M gives a k-dimensional family of convex projective structures with generalized cusps.
  - Introduction and §2, p. 11: *"numerical computations performed by the author, J. Danciger, and G.-S. Lee suggest that a
    majority of manifolds in the SnapPy cusped census are infinitesimally rigid rel ∂M"*. No list is given.
  - A closed totally geodesic surface makes M non-rigid (bending).
- **S. Ballas**, *Finite volume properly convex deformations of the figure-eight knot*, arXiv:1403.3314v3, p. 2: the family keeps
  the meridian unipotent and makes the longitude non-unipotent.
- **S. Ballas**, *Deformations of non-compact projective manifolds*, AGT 14 (2014), arXiv:1210.8419, Thm. 1.2: on rigid
  amphicheiral knot complements with a rigid longitude, the orbifold fillings deform.
- **C. Daly**, *Projective Rigidity of Once-Punctured Torus Bundles via the Twisted Alexander Polynomial*, arXiv:2411.04431v1:
  - Thms. 3.3 and 3.4 give a twisted-Alexander criterion for rigidity rel cusp.
  - §4 has two examples, L²R² and R²L, both rigid.
  - The published version (Geom. Dedicata 2025, "via Twisted Invariants") is behind a login and **was not read**. Its abstract,
    as indexed, names the Wada invariant criterion.
- **C. Daly**, *Computer Assisted Projective Rigidity*, arXiv:2408.08405: covers about two thousand closed fillings of m004 and
  no bundle other than m004.

**What this arc must not present as new.**
- The criterion (Heusener–Porti), the smoothness and the family's existence (BDL, Ballas).
- m004, L²R² and R²L being rigid (Heusener–Porti, Daly).
- m004's sign table and its one-bit structure (B1455, sm:B1520).
- The π/3 structure of a class on a cusp (Heusener–Porti Lemma 5.5).

**New, as far as swept:**
- the census of rigidity rel cusp over every word state to length 12 (BDL's Remark 3.3 left it open for the census);
- the isometries' signs on the family's line;
- the reduction of the longitude rule to the fibre boundary being a rigid slope (Lemma R);
- the list of states where a family exists and no symmetry dualises it.

## 1. The question, and a correction to how it was registered

**Registered (sL-10 item 6):** *"Which word states are projectively flexible at the hyperbolic point: dim H¹(π; v) beyond the cusp's
share …? Census over the states of length ≤ 8."*

**Corrected here, before the seal (ERROR_LEDGER, E2 instance).** The family exists where dim H¹(π; v) *equals* the cusp's share,
not where it exceeds it. The chain is:
- rigidity rel cusp is dim H¹(v) = 1 (Heusener–Porti Cor. 5.4);
- it makes ρ_hyp a smooth point with three-dimensional tangent H¹(so(3,1)) ⊕ H¹(v) (BDL Thm. 3.2);
- the v-direction then integrates to a one-parameter family of convex projective structures with the cusp opened (Ballas
  Thm. 0.2).

The share beyond the cusp, where dim H¹(v) ≥ 2, is what can obstruct or enlarge the family; there this method decides nothing. The
registered range, length ≤ 8, is widened to 12.

**The question, exact.**
- For each word state w to length 12, is its bundle M_w rigid rel cusp (so a projective family exists at its hyperbolic point)?
- For each isometry β of a rigid M_w, what is its sign ε_β = ±1 on the line H¹(M_w; v)?
- Which rigid states have **no** isometry with ε_β = −1?

On those states, B1455's vanishing criterion V* ≅ σ*V cannot be met near the hyperbolic point (Lemma T). They are the first
places in the record where a projective family exists and no symmetry forces its vacua to count zero.

## 2. Definitions

- **Word states and manifolds** (sm:B1516 C4, sm:B1517, main's B1434/B1439):
  - a word state is a signed primitive cyclic word in L and R with both letters, up to rotation and the L↔R swap: **758** to
    length 12;
  - its bundle is SnapPy's `b++w` (sign +) or `b+-w` (sign −);
  - a state and its reverse are one manifold: **536**.
- **The kinds of self-map.** These are the h ∈ GL₂(ℤ) with h w h⁻¹ = w^{±1} (`words.py`):

  | kind | when | orientation | effect on the cusp |
  |---|---|---|---|
  | id and ι | always | kept | cusp map I |
  | rev | w ~ reverse(w) | kept | −I |
  | swap | w ~ swap(w) | reversed | diag(−1, 1) |
  | swaprev | w ~ swap(reverse(w)) | reversed | diag(1, −1) |

  The cusp maps are written in SnapPy's basis (meridian μ = the fibre boundary, longitude λ = the section). The kinds with the
  identity form a group. C2 checks the prediction |Isom| = 2(1 + rev + swap + swaprev) and the cusp maps on all 536.

  The census's classes are:

  | class | manifolds |
  |---|---|
  | chiral ("none") | 220 |
  | rev only | 250 |
  | swaprev only | 42 |
  | swap only | 2 |
  | all three | 22 |
- **Longitude-inverting:** a rev or swap map, which sends the fibre boundary to its inverse. **262** manifolds have none:
  220 chiral and 42 swaprev-only, 131 per sign.
  - By length 6–12: 2, 2, 8, 14, 36, 62, 138.
  - They carry 482 of the 758 states: a manifold carries two states iff it has neither rev nor swaprev.
- **v**, **rigid rel cusp**, **a rigid slope:** as in §0. sl(4, ℝ) = so(3,1) ⊕ v as Γ-modules (Johnson–Millson), with v 9-dimensional.
- **The sign ε_β.** An isometry β acts on the line H¹(M; v) of a rigid state by ε_β = ±1. It is computed through the cusp: β acts on
  H¹(P; v) through its normaliser, and the restriction is injective (Heusener–Porti).
- **Dualising and mirror-broken.** A rigid state is *dualising* if some β has ε_β = −1; D∘β then fixes the family's direction, D
  being duality, which acts on v by −1. It is *mirror-broken* if no β does.
- **Golden:** the monodromy field is ℚ(√5), i.e. tr(w)² − 4 is 5 times a square. There are **14** golden manifolds:
  - with a longitude-inverting isometry (10): ±LR, ±L⁵R, ±L³RL²R, ±L⁴R⁴, ±L⁸R²;
  - without one (4): **±L⁴RL³R²** (trace 47) and **±L⁴RLR³LR²** (trace 123).

## 3. Lemmas (proved now)

**Setting.** Work in the frame with the cusp at ∞, the meridian μ translating by t_μ = 1. Complexify: v ⊗ ℂ ≅ V₂ ⊗ V̄₂, with
V₂ = Sym²ℂ² spanned by x², xy, y², and x the vector the translations fix. The translation z ↦ z + s acts by exp(s N ⊗ 1 + s̄ 1 ⊗ N̄),
where N y = x and N x = 0.

**The real classes.** By van Est–Nomizu (unipotent coefficients) and Künneth, H¹(P; v ⊗ ℂ) is spanned by ω₁ : s ↦ s·y² ⊗ x̄² and
ω₂ : s ↦ s̄·x² ⊗ ȳ². The real classes are c_a = aω₁ + āω₂, a ∈ ℂ, so dim H¹(P; v) = 2. C5–C8 confirm this numerically.

**Lemma S (slopes).** c_a restricted to a slope with translation t is zero in H¹(⟨t⟩; v) iff Re(a t³) = 0.
- *Proof.* In the coinvariants of exp(N_t), c_a(t) ≡ −4 Re(a t³)/|t|² · xy ⊗ x̄ȳ. Both W₂-terms of c_a reduce to xy ⊗ x̄ȳ modulo
  N_t(W₁), and the higher terms of exp lie in im N_t.
- So a class vanishes on three slope directions 60° apart. This is Heusener–Porti's π/3 (Lemma 5.5, Remark 5.6).
- The fibre boundary μ (t = 1) is a rigid slope iff a ∉ iℝ.
- *Checked live before the seal (C9),* on route R's box of the 16 primitive slopes μ^p λ^q with |p| ≤ 3 and 0 ≤ q ≤ 3:
  - on m004 the zero slopes are exactly μ⁻¹λ², λ and μλ², at 30°, 90° and 150° from the fibre boundary (residuals about 1e-60
    against 1e-3 to 0.3 for the other thirteen);
  - on L²R² only λ vanishes, since its 30° and 150° directions are not lattice directions;
  - on R²L, which has no reflection, none vanishes.

**Lemma ι.** An isometry with cusp map I (the identity and ι) has ε = +1 on a rigid state.
- *Proof.* Its normaliser is a translation T. c ↦ Ad(T)c gives a continuous homomorphism from the translations ℝ² to
  GL(H¹(P; v)).
- It is unipotent, since ad of a parabolic is nilpotent on v.
- It is trivial on ρ(P), whose action is inner: Ad(ρ g)c = c + δ(c(g)).
- A unipotent representation of the compact torus ℝ²/ρ(P) is trivial. Restriction is injective, so ε = +1.

**Lemma rev.** An isometry with cusp map −I has ε = −1 on a rigid state.
- *Proof.* The lattice forbids a shear: α t_μ = −t_μ and α t_λ = k t_μ − t_λ force k = 0. So the normaliser is z ↦ −z,
  diag(i, −i).
- It acts on x^p y^{2−p} ⊗ x̄^q ȳ^{2−q} by (−1)^{p+q}, and on s by −1. Hence c_a ↦ c_{−a}: −1 on all of H¹(P; v).

**Lemma R (orientation-reversing).** For β reversing orientation, β* is a reflection of H¹(P; v) (trace 0, determinant −1), and
**ε_β = −1 iff [β inverts the fibre boundary] XOR [the fibre boundary is not a rigid slope].**
- *Proof.* The normaliser is z ↦ ±z̄, with + for β keeping μ and − for β inverting it: α·t̄_μ = ±t_μ with t_μ = 1. A shear in
  the cusp map is possible here (a rhombic lattice, e.g. λ ↦ λ − μ when Re t_λ = ½), but it does not change the normaliser.
- Complex conjugation exchanges the two tensor factors, so z ↦ z̄ sends c_a ↦ c_ā, and z ↦ −z̄ sends c_a ↦ c_{−ā}.
- The class's line is preserved, so a ∈ ℝ or a ∈ iℝ.
  - For a ∈ ℝ: the μ-keeping map has ε = +1, the μ-inverting map has ε = −1, and μ is rigid (Lemma S).
  - For a ∈ iℝ: the signs are the opposite, and μ is not rigid.
- **So the longitude rule on a reflective state is exactly the statement that its fibre boundary is a rigid slope.** The census
  measures both sides separately:
  - ε by the isometries' normalisers;
  - μ's rigidity by Heusener–Porti's restriction: route R by a residual, route C by a rank test.
- Lemma R makes their agreement a check (P8).

**Lemma T (the tangent argument).** Let M_w be rigid, F = D∘β* a count-odd map (optionally followed by conjugating a twist), and
ρ_s any curve through ρ_hyp whose tangent has a nonzero v-part: the family, with any central twist.
- F has finite order and fixes ρ_hyp. By the linearisation of finite group actions at a fixed point, Fix(F) is a submanifold near
  ρ_hyp, tangent to Fix(dF).
- dF acts on the v-line by −ε_β.
- If ε_β = +1 for every β: every Fix(F) is tangent to {v-part = 0}, so ρ_s ∉ Fix(F) for 0 < |s| small. **The family's vacua off
  the hyperbolic point are fixed by no count-odd map.**
- If some ε_β = −1: Fix(D∘β*) is tangent to a space containing the v-line, so a family of count-odd-fixed vacua exists. On m004 it
  is Ballas' family itself (B1455, sm:B1520).
- At the hyperbolic point itself every unitary vacuum is fixed (sm:B1522 Lemma U).

**What the lemmas decide without the census.**
- Every rigid **chiral** manifold (220) is mirror-broken, by Lemma ι.
- Every rigid rev-bearing manifold (272) is dualising, by Lemma rev.
- The census decides:
  - rigidity itself;
  - the fibre boundary's rigidity on the 66 reflective manifolds (all three, swap only, swaprev only);
  - whether the 2 swap-only manifolds are dualising (iff μ is rigid);
  - whether the 42 swaprev-only manifolds are dualising (iff μ is not rigid).

## 4. BANKED IDENTITY: the controls

`controls.py` passes C1–C9 at the seal (`controls.json`, `controls_run.txt`):

| check | content |
|---|---|
| C1 | the enumeration 758/536, recounted by Burnside over the necklaces; the 262 by length; the golden 14 |
| C2 | SnapPy's isometries on all 536: orders, cusp maps by kind; the meridian is the fibre boundary, by exact rank over ℚ |
| C3 | relators, the cusp frame and the cusp shape in both routes, on all 536. The shapes agree with each other and with the conjugate of SnapPy's cusp shape (a convention) |
| C4 | dim H¹(ℝ) = 1 and dim H¹(so(3,1)) = 2 on all 536 (route R), and in both routes on the controls |
| C5 | the literature (below) |
| C6 | the two routes agree on the controls |
| C7 | the planted m129: (2, 4, 2) in both routes |
| C8 | the cusp lemmas on the controls |
| C9 | Lemma S live on the literature's manifolds: their zero slopes in the box, as in §3 |

C5, the literature:
- m004, L²R² and R²L are rigid in both routes;
- m004's signs are sm:B1520's table;
- m004's fibre boundary is a rigid slope (Heusener–Porti Remark 8.1) and its section is not (Ballas 1403.3314 p. 2: the meridian
  stays unipotent).

**Disclosed: C3's relator bar.**
- The first run used 1e-45, an arbitrary bar, and flagged one manifold. Route R's simplified relators on b+-LLLLLLRLLRLR have
  lengths 11 and 33, with partial products of norm 1e8. They carry 2.9e-41; route C carries 4.0e-57 on the same manifold.
- On that manifold, route R's so-module still had dropped singular values ≤ 2e-49 against kept ≥ 4e-3.
- The bar is now 1e-35, five orders under the rank tolerance 1e-30, and every rank decision's own margin is read per manifold
  (P4).
- No cohomology of v had been computed on any census manifold when this was changed.

**Disclosed: route C's frame bug (ERROR_LEDGER, E31 instance).**
- Route C first took the meridian's fixed point from the first row of A − 1. That row vanishes when the meridian fixes 0. On
  b++LR and b++LLRR the "frame" was lower-triangular and the det −1 signs came out as 1.17 and 0.70.
- The frame now reads the larger row, uses a unitary-up-to-scale S, and asserts that both peripheral curves are upper-triangular.
  A normaliser check was added.
- Found on the controls before any census manifold was read.

**`census.py` re-reads the three literature controls first.** Their records must equal `controls.json`'s in dimensions, signs and
slopes (P1).

## 5. Read-out, predictions and priors

`census.py` runs both routes on all 536 manifolds, and `read_out.py` reads the predictions.
- Route R is the real form on SnapPy's simplified presentation.
- Route C is the complex form on the unsimplified presentation. It shares no code with route R: its frame, normaliser, module
  model and SVD are its own.

The decisions and their margins:

| decision | rule |
|---|---|
| rank | dropped < 1e-35, kept > 1e-20 |
| ε | within 1e-20 of ±1, with eigen-residual < 1e-20 |
| slopes | both routes > 1e-20 for rigid, both < 1e-30 for not rigid |

| | prediction | basis | prior |
|---|---|---|---|
| P1 | the controls pass and the census re-reads them | §4 | 99% |
| P2 | every one of the 536 manifolds is rigid rel cusp | Heusener–Porti Prop. 1.9; Ballas' "majority" | 80% |
| P3 | on every rigid manifold with an orientation-reversing isometry, ε = −1 exactly on the fibre-boundary-inverting isometries (equivalently, by Lemma R, the fibre boundary is a rigid slope there) | m004 and L²R² (2 of 2); by Lemma R a binary per reflective state, so it needs a reason that holds everywhere | 65% |
| P4 | the routes agree on every manifold, and every decision keeps its margin | — | 99% (a failure is a bug, found before any reading) |
| P5 | the mirror-broken rigid manifolds are exactly the rigid ones without a longitude-inverting isometry (with P2: 262 manifolds, 131 per sign, 482 states) | Lemmas ι, rev, R with P3 | 55% |
| P6 | the fibre boundary is a rigid slope on every rigid manifold, chiral ones included | P3, and genericity of a on chiral states | 60% |
| P7 | **the golden reading:** of the 14 golden manifolds, the mirror-broken ones are exactly ±L⁴RL³R² and ±L⁴RLR³LR² (8 states) | P2, P3 on the golden ones | 55% |
| P8 | the lemmas hold on every rigid manifold in both routes. Cusp map I gives +1 and acts as 1; −I gives −1 and acts as −1; det −1 acts as a reflection; a translation acts trivially; Lemma R's equivalence | §3 | 99% (a failure is a bug) |
| P9 | Lemma S on every rigid manifold: the zero slopes in the box lie in one coset of 60°. On a reflective manifold that coset is 30° + 60°ℤ when the fibre boundary is rigid and 60°ℤ when it is not | §3, C9 | 99% (a failure is a bug) |

**Outcomes.**
- **A:** no rigid manifold is mirror-broken. By Lemma ι this needs all 220 chiral manifolds non-rigid. Reading A would point to a
  bug or to a wholesale failure of rigidity, to be found before banking.
- **B:** mirror-broken flexible states exist. They are listed by length, sign and kind, the golden ones flagged. **Expected.**
- **C:** some manifolds are not rigid. They are listed, and the family's existence there is undecided by this method.

B and C can occur together.

**What B would mean, and what it would not.**
- On a mirror-broken flexible state, the projective family exists (BDL, Ballas) and no count-odd map fixes its vacua off the
  hyperbolic point (Lemma T). B1455's symmetry proof that the index vanishes is unavailable there.
- **It does not say the index is nonzero.** That needs the family off its hyperbolic point and the class index on it. That is the
  next arc, to be registered as sL-10 item 8 and sealed before computing.
- **It does not say a chirality is selected.** Main's L241 (both orders over a split vacuum count opposite, sm:B1511/B1512) holds
  whatever the stabiliser.

**The golden reading registered.** The owner's "choice might be golden", in its second sealed form (the first was sm:B1522's
Galois reflections on the levels): does the golden field shield a state from mirror-breaking? P7 says it does not:
- two golden manifold pairs are mirror-broken, chosen by their words (no rev, no swap), not by their field;
- all the other golden words carry rev.

## 6. What it does not do

- It does not compute any family off the hyperbolic point, any class index, or any vacuum's order.
- It does not treat states beyond length 12, nor non-bundle cusped manifolds.
- On a non-rigid state, if any, it decides nothing about a family.
- creates_law is to be decided at banking under B1214's rule. No Standard-Model number is touched: **0 of 19**; I-26 stays
  UNEARNED.
