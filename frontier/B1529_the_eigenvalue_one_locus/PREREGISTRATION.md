# B1529 — PREREGISTRATION: THE EIGENVALUE-ONE LOCUS — the class index where the cusp acquires the eigenvalue one, near the hyperbolic point of every word state and of m004's levels (sL-10 item 9)

**Sealed before `census.py` and `crossings.py` run on any outcome.** At the seal this arc has computed only:
- `controls.py`, C1–C6, all pass (`controls_run.txt`, `controls.json`). They read banked numbers and theorems only (§6).
- Three instrument tests, disclosed in §6. The locator was run on +LR's first two brackets, with no reading. The reader was run at
  m004's hyperbolic point, for the four only. The census's code was run on +LR, printing the four (banked by sm:B1509) and
  Λ²'s dimensions (banked by sm:B1527).

No multiplicity of Λ² at any base point, no base condition of the four on any state but m004 and its levels (banked), and no
index, h¹ or interior value at any eigenvalue-one crossing has been read.

**Source.**
- **The owner, 2026-10-02:** "do as u recomend with all independently, goal remains", with nothing load-bearing ignored, the
  experiential question included, all allowed states and not only m004, and the hypothesis that the choice might be golden.
- **sL-10 item 9** (OPEN_LEADS; sm:B1527 §7), verbatim: *"The eigenvalue-one locus of the infinite-volume part near the hyperbolic
  point … Off the finite-volume curves the cusp is type two (or type three), and Lemma C gives I = a0 − b0 = 0 except where ρ(ℓ)
  has the eigenvalue 1 … There one twist λ has a non-acyclic cusp, and by Lemma E the index is h¹(V*) − h¹(V) + 2(a0 − b0) +
  s0 − t0, which can jump at isolated points. Do any of them carry I ≠ 0, for ν ⊗ ρ or ν ⊗ Λ²ρ? … Seal before computing."*
- **A correction to the item as registered.** It lists the loci where ρ(ℓ) has the eigenvalue one: ψa + ψb, 3ψa − ψb, 3ψb − ψa.
  For ν ⊗ Λ²ρ, what matters is the eigenvalue one of Λ²ρ(ℓ). Its weights are the pair sums ±(ψa + ψb)/2 and ±(ψa − ψb)/2, each
  of the second pair twice. So the locus for Λ² is ψa + ψb = 0 together with ψa = ψb, and the item omitted ψa = ψb. This arc
  reads all four loci (§2, E1–E4).

## 0. Seen first, and PRIOR ART:

**The repo sweep.** `git fetch --all`, then `scripts/checks/prior_work.py` on "interior polynomial", "four-term sequence",
"simple root", "eigenvalue-one locus", "item 9", "H^1(F, dF", "Menal-Ferrer", "Raghunathan", "special twist". Every hit that
bears was read. The heads were:

| head | commit |
|---|---|
| main | `d2a95da4` (S46, B1463) |
| the audit lane | `24c039c8` |
| this branch | `f1b4587f` |
| seat/determined-hopper | `7cda35aa` |
| seat/magical-wright | `0043be2b` |

What bears, read in full where it bears:
- **sm:B1509 T3, sm:B1511 Theorem B (this branch).** The Wang sequence on the fibre: H¹(M; V) = ker(S − 1) and
  H²(M; V) = coker(S − 1), for V boundary-acyclic. The index of an extension is non-zero exactly where the fibre monodromy has a
  Jordan block. Lemma F below is the same sequence with the cusp not acyclic: the fibre's pair (F, ∂F) enters.
- **sm:B1510 Theorem C (this branch).** The index of a two-sided deformation is zero, by upper semicontinuity, the Euler
  characteristic and the annihilator identity. Lemma K is that argument with the base point at the hyperbolic point and the
  lower bound from duality.
- **Main's B1440 (main).** On a once-punctured-torus bundle, for V with V^F = 0 = (V*)^F, |I(V)| ≤ min(r, n − r), r =
  rank(ρ(ℓ) − 1). Its proof uses the onto map H¹(F; V) → H¹(∂F; V) (cokernel in H²(F, ∂F; V) = V_F = 0). That is the right half
  of Lemma F's four-term sequence.
- **Main's B1297 (main).** The class index, its identity I = (a0 − b0) + s0 − r1 and the annihilator identity.
- **sm:B1527 (this branch).** Lemma C (ν(ℓ) = 1, the cusp decides), Lemma E (I through h¹), Part H (I = 0 at ρ_hyp), the
  type-two ring of X1 at a = 10⁻⁵ with its banked grid, and routes Fox (`cusp_lib`) and W (`wang_lib`), used here as banked
  instruments.
- **sm:B1515 (this branch), §5 (b), (d).** At the hyperbolic point of m004's level M₆, the twisted four has interior classes:
  h¹(ν ⊗ ρ₁) = 1 at 292 characters, 2 at 24 (order 8) and 3 at 4 (order 5), and 1 everywhere on M₁–M₅. It is read by three
  methods, Wang's among them. B1515's lead 2 says why such classes can exist: "Over ℂ, ρ₁ is h ⊗ h̄, outside Menal-Ferrer–Porti's
  theorem". So the four's base condition below is not a theorem, and this banked failure is the census's positive control (C6).
- **The record's citations of Menal-Ferrer–Porti** (B264, B1256, B1396, B1515, and others) use it for the holomorphic symmetric
  powers, as this arc does in Lemma B.
- **sm:B1523 (this branch).** The 536 manifolds of the word states to length 12, and route F's hyperbolic points, reached on all
  536 (two through a rotation of the word).
- **Main's S46 (B1463)**, read at `d2a95da4`: two early corrections (B37, B130) and a GENESIS v1.8 of main's own, from main's
  v1.7 with a log line. It does not bear on this arc. Its number collides with this branch's GENESIS v1.8 (sm:B1528), which was
  made from the same v1.7 with different additions. That is recorded at the bank and left to main's answer to the v1.8 relay.
- Not found on any head in this sense: Lemma F's sequence with a non-acyclic cusp and its interior polynomial, the simple-root
  condition at the base points, Lemma O. The terms' other hits ("simple root" in 138 files, "four-term sequence" in unrelated
  arcs) concern other roots and sequences; the ones that bear are listed above.

**The literature**, searched and read on 2026-10-03:
- **Menal-Ferrer and Porti, "Twisted cohomology for hyperbolic three manifolds"** (arXiv:1001.2242v2, Osaka J. Math. 49 (2012)),
  §0–3 read.
  - Theorem 0.1: for M complete, nonelementary, topologically finite, and ρ_n = (a lift of the holonomy) composed with the
    irreducible holomorphic V_n, n ≥ 2, the map H¹(M; E_ρn) → H¹(∂M; E_ρn) is injective with half the dimension, and
    H²(M) ≅ H²(∂M).
  - The scope is holomorphic V_n only. Lemma 2.14's proof uses the complex structure ("in the last equality we have used the
    complex structure"). §1 lists the irreducibles as the symmetric powers of C².
  - Lemma 3.5 gives V_n^{π₁(M)} = 0. Proposition 3.2 gives V_n^{π₁(T²)} = ℂ for n odd. Corollary 3.7 gives dim H¹ = a (the
    number of cusps for n odd).
  - The four is V₂ ⊗ conj(V₂), which is not holomorphic. Λ² of the four is V₃ ⊕ conj(V₃).
- **Not found in the literature searched:** a statement of the simple-root condition (§2) for twisted characters, or of the four's
  base condition. Both are therefore computed (the census), not cited.
- Raghunathan's original paper was not read. Nothing here rests on it beyond what Menal-Ferrer–Porti state.

## 1. The question

Near the hyperbolic point ρ_hyp of a word state (or a level), in Hom(Γ, SL(4, ℂ)), at the representations where the cusp acquires
the eigenvalue one and one twist has a non-acyclic cusp: is the class index of ν ⊗ ρ or ν ⊗ Λ²ρ ever non-zero?
- sm:B1527 answered it in finite volume (types 0 and 1). This arc asks it everywhere near ρ_hyp: types 2 and 3, and the complex
  representations.
- A non-zero index there would be the first count on a split vacuum near the hyperbolic point.

## 2. Definitions and conventions

- **The group.** Γ = F ⋊ ⟨t⟩, F = ⟨a, b⟩ free, t x t⁻¹ = φ(x) (sm:B1527 `family_lib.word_group`). The cusp is ⟨ℓ, t′⟩ with
  ℓ = abAB, and t′ = t (sign +) or abt (sign −). t′ fixes ℓ exactly, and t′ g t′⁻¹ = φ′(g) is a word in a, b.
- **The modules.** V = ν ⊗ W, with W = ρ (the four) or Λ²ρ, and ν a character.
  - ν|F = ν₀, a torsion character fixed by φ (D of them).
  - κ = ν(t′); this is λ for +, and ν₀(a)ν₀(b)λ for −.
  - ν(ℓ) = 1 always (Lemma C).
- **The base points** are (ρ_hyp, u, λ_c(u)). There ν is trivial on the cusp, κ = 1 for both signs, and ν is of finite order.
- **The fibre's four spaces**, with S₀ the stable letter t′ acting without its character, (S₀z)(g) = W(t′)⁻¹ z(φ′(g)):
  - A = W^ℓ and D = W_ℓ (the invariants and coinvariants of ℓ alone), on which S₀ acts by W(t′)⁻¹;
  - C = H¹(F; ν₀ ⊗ W) and B = H¹(F, ∂F; ν₀ ⊗ W).
  - e = dim A = dim D.
  - g(X; κ) is the dimension of the κ-eigenspace of S₀ on X; am(X; κ) is the algebraic multiplicity.
  - χ_X is the characteristic polynomial, and χ_K = χ_C / χ_D is the **interior polynomial** (K = ker(C → D)).
- **The base condition** at a base point: h¹(V) = h¹(V*) = t0 = s0 (= k), with a0 = b0 = 0.
- **SR, the simple-root condition**, at a base point: am(C; 1) = am(D; 1). Equivalently, χ_K(1) ≠ 0.
- **The crossings on the type-two ring** (sm:B1527 X1: Ballas' slice at a = 10⁻⁵, b free, ℓ's translation of length R0).
  - The eigenvalues of ρ(ℓ) are e^{−ψ/4} (on e1, e4, a Jordan block), e^{(3ψa − ψb)/4} and e^{(3ψb − ψa)/4}, with ψ = ψa + ψb.
  - E1: ψa + ψb = 0, for the four and Λ².
  - E2: 3ψa − ψb = 0, the four.
  - E3: 3ψb − ψa = 0, the four.
  - E4: ψa − ψb = 0, Λ².
  - The special twists κ* are the eigenvalues of S₀ on A. Exactly there t0 ≥ 1.

## 3. The theorems (proved at design time)

**Lemma K (the sandwich; after sm:B1510 Theorem C).** Suppose the base condition holds at a base point with k = h¹ = t0 = s0. Then
near it, in Hom(Γ, SL(4, ℂ)) × {characters}:
- 0 ≤ h¹(V) − s0 ≤ k − s0, and 0 ≤ h¹(V*) − t0 ≤ k − t0;
- t0 ≥ 1 ⇔ s0 ≥ 1, and I = [h¹(V*) − t0] − [h¹(V) − s0].

So I = 0 where t0 = s0 ∈ {0, k}, and ∣I∣ ≤ k − 1 elsewhere. For k = 1, I = 0 near the base point, for every ρ and every character.

*Proof.*
- Upper semicontinuity of the Fox complex gives h¹ ≤ k and t0, s0 ≤ k nearby. Also a0 = b0 = 0 nearby: irreducibility is open.
- χ(M) = 0 and h³ = 0 give h² = h¹ − a0 = h¹. Lefschetz duality gives h²(V) = h¹(M, ∂M; V*). The pair's sequence gives
  h¹(M, ∂M; V*) ≥ s0 − b0. So h¹(V) ≥ s0, and likewise h¹(V*) ≥ t0.
- On the cusp, ℓ and t′ commute. Their joint eigenvalue (1, 1) occurs iff the commuting nilpotents on that generalized eigenspace
  have a common kernel, iff they have a proper sum of images. So t0 ≥ 1 ⇔ s0 ≥ 1.
- Lemma E with a0 = b0 = 0 gives the formula.
- Characters far from λ_c(u) leave the cusp acyclic near ρ_hyp, so there I = a0 − b0 = 0 (Lemma C).
- There are finitely many base points, so one neighbourhood serves. □

**Lemma F (the fibre's four-term sequence; after sm:B1509 T3, sm:B1511 Theorem B and main's B1440).** Let H⁰(F; ν₀ ⊗ W) = 0 =
H⁰(F; (ν₀ ⊗ W)*). Then 0 → A → B → C → D → 0 is exact and S₀-equivariant, and
- h¹(Γ; V) = g(C; κ), h¹(Γ; V*) = g(B; κ), t0 = g(A; κ), s0 = g(D; κ), a0 = b0 = 0;
- I(V) = [g(B; κ) − g(A; κ)] − [g(C; κ) − g(D; κ)];
- I(V) ≠ 0 only if κ is a root of the interior polynomial χ_K.

*Proof.*
- **The sequence** is that of the pair (F, ∂F), ∂F = ⟨ℓ⟩. H⁰(F) = 0 kills the first map's kernel. H²(F, ∂F; ν₀ ⊗ W) ≅
  H⁰(F; (ν₀ ⊗ W)*)* = 0 makes C → D onto. H²(F) = 0 since F is free. t′ preserves the pair, since it fixes ℓ.
- **h¹(V).** The Lyndon–Hochschild–Serre sequence of Γ = F ⋊ ⟨t′⟩ with H⁰(F) = 0 gives H¹(Γ; V) = H¹(F; V)^{t′} =
  ker(κ⁻¹S₀ − 1) on C.
- **h¹(V*).** H¹(F; ν₀⁻¹ ⊗ W*) ≅ H¹(F, ∂F; ν₀ ⊗ W)* by Lefschetz duality on the surface F. The pairing is t′-invariant, since
  the monodromy preserves the orientation. So the κ⁻¹-eigenspace of S₀′ on H¹(F; V*) has the dimension of the κ-eigenspace of S₀
  on B.
- **t0 and s0** are the κ-eigenspaces of W(t′)⁻¹ on W^ℓ and on W_ℓ.
- **The formula** is Lemma E.
- **The criterion.** If κ is not a root of χ_K, exactness of generalized eigenspaces gives E(A; κ) ≅ E(B; κ) and
  E(C; κ) ≅ E(D; κ), as S₀-modules. So both brackets vanish. □

**Lemma O (Λ² has no single eigenvalue-one direction).** For g ∈ SL(4, ℂ), the eigenvalue-one space of Λ²g never has
dimension 1.

*Proof.*
- Λ²g preserves the symmetric non-degenerate form x ∧ y on Λ²ℂ⁴ and has determinant 1, so Λ²g ∈ SO(6, ℂ).
- For g ∈ SO(2m): the spectrum is closed under inversion, the eigenvalue −1 has even multiplicity (det = 1), so the eigenvalue 1
  has even algebraic multiplicity n₁.
- The generalized 1-eigenspace E₁ is non-degenerate, since E_μ ⊥ E_ν unless μν = 1.
- Suppose dim ker(g − 1) = 1 with n₁ ≥ 2. Then X = log(g∣E₁) ∈ so(E₁) is a single nilpotent Jordan block of even size n₁, with a
  cyclic vector x.
- Put c_s = β(x, X^s x). Then β(X^i x, X^j x) = (−1)^i c_{i+j}, and symmetry forces c_s = 0 for s odd.
- The Gram matrix is anti-triangular, so its determinant is ± c_{n₁−1}^{n₁}. That is 0 because n₁ − 1 is odd. This contradicts
  non-degeneracy. □

**Lemma B (Λ²'s base condition is a theorem; Menal-Ferrer–Porti Theorem 0.1).** At every base point, ν ⊗ Λ²ρ_hyp has
h¹ = h¹* = t0 = s0 = 2 and a0 = b0 = 0.

*Proof.*
- Λ²(V₂ ⊗ conj V₂) = V₃ ⊕ conj V₃.
- ν has finite order at λ_c. Let M_ν be the finite cyclic cover of ker ν: complete, nonelementary, topologically finite.
- Shapiro's lemma makes H*(M; ν ⊗ V₃) the ν-isotypic summand of H*(M_ν; V₃), and likewise on the boundary. Restriction commutes
  with the deck group.
- Theorem 0.1 on M_ν makes H¹(M; ν ⊗ V₃) → H¹(∂M; ν ⊗ V₃) injective. The pair's sequence and Lefschetz duality give half the
  dimension, as in its proof. a0 = 0 by Lemma 3.5.
- At λ_c, ν is trivial on the cusp, and V₃^{π₁(T²)} = ℂ (Proposition 3.2), so t0 = s0 = 1 and h¹ = 1 for each summand.
- conj V₃ is the complex conjugate local system of ν⁻¹ ⊗ V₃, which has the same dimensions. □

The four (V₂ ⊗ conj V₂) is outside Theorem 0.1, and its base condition can fail: on M₆ it fails at 28 characters (sm:B1515).

**Lemma P (pairs).** Λ²ρ ≅ (Λ²ρ)* for ρ ∈ SL(4). So I(ν⁻¹ ⊗ Λ²ρ) = −I(ν ⊗ Λ²ρ): Λ²'s special twists come in dual pairs
(u, κ) ↔ (−u, 1/κ) with opposite indices. □

**Theorem N (near the hyperbolic point).** Suppose SR holds for Λ² at every base point of M. Then there is a neighbourhood of
ρ_hyp in Hom(Γ, SL(4, ℂ)) on which I(ν ⊗ Λ²ρ) = 0 for every character ν.

*Proof.*
- At a base point, D has dimension e = 2 and S₀ acts on it unipotently. So am(D; 1) = 2, and SR says χ_C has exactly two roots at 1.
- Near the base point, χ_C (a continuous family on the constant-rank space C) has exactly two roots in a small disc U around 1.
- χ_D has e(ρ) roots there, since W(t′) is near-unipotent.
- By Lemma O and semicontinuity, e(ρ) ∈ {0, 2}.
  - If e(ρ) = 0, the cusp is acyclic for every twist (Lemma C).
  - If e(ρ) = 2, χ_K = χ_C/χ_D has no root in U. Every special twist lies in U, so Lemma F gives I = 0.
- Twists outside U leave the cusp acyclic.
- There are finitely many base points. □

For the four, Lemma K with k = 1 gives the same conclusion wherever the base condition holds; it needs no SR.

**What the theorems leave to computation:**
- whether SR holds for Λ² at every base point (P1);
- whether the four's base condition holds at every base point (P2);
- that, as computed at genuine crossings by routes independent of Lemma F, the index is 0 (P5).

## 4. The instruments

- **`verification/fibre_lib.py` (route T, new code).**
  - T_C as a d × d matrix in the basis of cocycles vanishing on one generator, or on the orthogonal complement of B¹ when both slot
    matrices are near-singular.
  - Fox derivatives grouped by the prefix's exponent sums mod D, so a character costs one small sum (python-flint, 320 bits, radii
    stripped after each product: plain floating point, §6).
  - am from the Taylor coefficients of χ at κ. g by singular values at 60 digits (REL_TOL 10⁻³⁰, margins kept). The cusp ends A
    and D by singular vectors. The interior value χ_K(κ) by polynomial division.
- **`verification/census.py` (instrument (a)).**
  - The 536 states of sm:B1523 (one per manifold) and m004's levels M₂–M₆, at the hyperbolic point (route F, 60 digits).
  - Every torsion character at λ_c, both modules: am(C; 1), am(C′; 1), am(D; 1), e, (h¹, h¹*, t0, s0), I, χ_K(1), route T's
    hypothesis, margins.
  - Four workers.
- **`verification/crossings.py` (instrument (b)), on the ten states of sm:B1527.**
  - Brackets from X1's banked grid (all four functions E1–E4).
  - float64 bisection on X1's pinned solve, then the 60-digit crossing system (the b-free equations, ∣z_ℓ∣ = R0, the crossing
    function = 0) to ∣F∣ < 10⁻⁴⁸.
  - At each crossing, per module concerned: e, the special twists κ*, and route T at every torsion character.
  - Route Fox (`cusp_lib.class_index`) and route W (`wang_lib.index_wang`), the banked instruments, on the trivial character and
    the first two others in sorted order, with their negatives.
- **`verification/read_out.py`** reads P1–P6 and G as below.

## 5. The states

- **Census:** all 536 manifolds of the word states to length 12, and m004's levels M₂–M₆ (the bundles of (LR)ⁿ; M₁ = +LR is a word
  state). That is 46,826 characters on the word states.
- **Crossings:** the ten states of sm:B1527, with the rings X1 banked: ±LR, ±LLRLRR, ±L³RLR², ±L⁴RL³R² (golden, trace 47), and
  ±L⁴RLR³LR² (golden, trace 123).

## 6. Controls and disclosures (before the seal)

`controls.py`, all pass (`controls_run.txt`):
- **C1** route T against sm:B1527's Part H: 3,740 of 3,740 rows agree on (h¹, h¹*, t0, s0, I), and route T's hypothesis holds on
  all of them. Kept ≥ 6.4 × 10⁻¹², dropped ≤ 3.8 × 10⁻⁵², slot conditioning ≥ 2.9 × 10⁻⁵.
- **C2** sm:B1509's polynomial on m004: χ_C of the four is s⁴ − 8s³ + 14s² − 8s + 1 = (s − 1)²(s² − 6s + 1) to 7 × 10⁻⁵⁹,
  with am = 2 and g = 1.
- **C3** Lemma O on 53 elements: random elements with eigenvalue pairs of product one (diagonalizable and with Jordan blocks), and
  unipotents of every Jordan type. The eigenvalue-one dimensions seen are 0, 2, 4, 6, never 1.
- **C4** the hypothesis guard: B1509's W₁ on +LR. I = −1 (Fox), H⁰(F; W₁) = 0 and route T's g(C; 1) = h¹ = 1, but
  H⁰(F; W₁*) = 1. So Lemma F does not apply to W₁, and route T reports it.
- **C5** route T at the ten exported type-one points: 276 of 276 X2 rows agree.
- **C6 (the positive control for P2)** sm:B1515's interior classes. On M₁–M₅ the four's h¹ is 1 at every character. On M₆ it is
  1 at 292 characters, 2 at 24 (order 8) and 3 at 4 (order 5): exactly B1515's.

Disclosed:
- **Route T's first form failed C1 on the two longest words** (492 of 3,740 rows: h¹ read 0 for 1 and 2). It used python-flint's
  ball arithmetic. Through products of about 140 letters the balls' radii grew to 10³¹ on entries of size 10⁶, and the
  characteristic polynomial was garbage. The radii are now stripped after each product (plain floating point at 320 bits). C1
  then passed on all rows, with the zero singular value at 6.5 × 10⁻⁵² on +L⁴RLR³LR² (the input's own precision). Found by the
  controls before the seal.
- **The design notes first said e = 1 for the four at ρ_hyp.** The reader's test at m004's hyperbolic point read e = 2. A
  parabolic element of SO(3, 1) has Jordan type (3, 1), so W^ℓ for ℓ alone is two-dimensional. The cusp group's invariants are
  one-dimensional (t0 = 1). Lemma K's k is t0, so nothing in §3 changes, and SR is stated with am(D; 1), not e. On m004 the
  four's χ_K = s² − 6s + 1 does not vanish at 1, so SR holds for the four there.
- **The locator's test**, on +LR's first two brackets, located E1 at 22.5° (b/a = −2.41421356…, the weight-3 law's
  −tan 67.5°) and E4 at 45° (b/a = 1), with ∣F∣ = 2.5 × 10⁻⁵⁶ and 1.3 × 10⁻⁵⁴ in about 30 s each. No reading was taken.
  - It also found that the slice scale must be X1's float 10⁻⁵, not the decimal: the crossing function read 2 × 10⁻¹⁶ instead of
    10⁻⁵⁶. That was fixed.
- **The reader's test at m004's hyperbolic point**, for the four only (the special twist κ* = 1, at the base). Fox, W and T all
  gave (1, 1, 1, 1, 0), as Part H banked, and χ_K(1) = −4/6 (relative), as C2 implies. Its key error (a misnamed field) was
  fixed.
- **The census's test on +LR** printed the four (banked) and Λ²'s dimensions (2, 2, 2, 2) (banked). The code also computed Λ²'s
  multiplicities inside the test. The harness did not print them, and they were not read.

## 7. Predictions (sealed; `read_out.py` reads them)

| # | prediction | reason | prior |
|---|---|---|---|
| P1 | SR for Λ² at every base point of every word state and every level M₂–M₆: am(C; 1) = am(C′; 1) = 2 at every character, and e = am(D; 1) = 2 | at the trivial character the cup product with the fibration class is non-zero on the restricted classes when the fibre boundary deforms to first order; elsewhere a failure needs χ_K to vanish at a root of unity | 85% |
| P2 | the four's base condition, (h¹, h¹*, t0, s0) = (1, 1, 1, 1), at every base point of every word state | B1527's ten states hold it (416 characters), but M₆ fails it at 28 of 320 (sm:B1515), and the four is outside Menal-Ferrer–Porti | 55% |
| P3 | the theorems' controls everywhere: Λ²'s (2, 2, 2, 2) (Lemma B); I = 0 for both modules (Part H); e = am(D; 1) = 2 for both; route T's hypothesis; no manifold fails to compute; the levels reproduce sm:B1515 | theorems and banked data; the risk is a bug or precision on long words | 93% |
| P4 | on the ten rings: at least 90% of the brackets located; at every located crossing e = 1 for the four (E1, E2, E3) and 2 for Λ² (E1, E4), with 1 or 2 distinct special twists (Λ²'s product 1 to 10⁻³⁰), and (t0, s0) = (1, 1) on every route-T row there | the slice's triangular form; Lemma O | 80% |
| P5 | I = 0 on every row at every located crossing: route T on all characters; Fox and W on the subset, with every identity, and Fox = W = T on (h¹, h¹*, t0, s0, I) | Lemma K for the four on the ten (their base condition is banked); Theorem N for Λ² if P1 holds there | 92% |
| P6 | at every Λ² special twist ∣χ_K(κ*)∣ > 10⁻²⁰ (relative): no coincidence, the mechanism of Theorem N | Theorem N's proof, if P1 holds on the ten | 88% |
| G | the golden form of the owner's hypothesis: P1 and P2 hold on every golden word state (∣trace∣ ∈ {3, 7, 18, 47, 123, 322}), and P5 on the six golden states among the ten | no step above uses the trace field | 80% |

**Recorded, not predicted:** the four's am(C; 1) by character (its SR, which Lemma K does not need), the crossings found by kind,
and the four's interior values at its special twists.

**Outcomes.**
- **A:** P1, P3 and P5 hold. Item 9 is answered NEGATIVE for Λ² near the hyperbolic point of every word state to length 12 and
  every level M₂–M₆, for every deformation in Hom(Γ, SL(4, ℂ)): types 2 and 3, real or complex (Theorem N). For the four the
  same holds wherever P2 holds (Lemma K). Routed to the kill graph with its scope.
- **B:** P1 fails at some base points. There Lemma F leaves a coincidence locus near the base point, where ∣I∣ ≤ 1 is possible
  for Λ². It is registered as the next arc, sealed separately, with the failing points named. Theorem N holds on the rest.
- **C:** P5 fails at a crossing whose base points satisfy SR (Λ²) or the base condition (the four). That contradicts Theorem N or
  Lemma K, and is a bug until shown otherwise: routes, identities, margins and the 100-digit re-read are examined before anything
  is claimed.
- **D:** P2 fails on some word states. There the four has interior classes at its base points, Lemma K does not apply, and Lemma
  F allows a coincidence locus. That is the four's half of the next arc, together with M₆'s 28 characters (banked).

Expected count: 0.85 + 0.55 + 0.93 + 0.80 + 0.92 + 0.88 + 0.80 ≈ 5.7 of 7.

## 8. BANKED IDENTITY: checked before reading

- `controls.py` is re-run first, and must reproduce `controls.json`.
- The census carries its own identities on every manifold and level:
  - Λ²'s (2, 2, 2, 2) and I = 0 (theorems);
  - on +LR, the four's χ_C = (s − 1)²(s² − 6s + 1) (C2);
  - on the levels, B1515's counts (C6).
- A census row failing a theorem's control is a bug, not a result.
- At the crossings, every Fox row carries B1297's identity, the annihilator identity and Lemma E, and every row carries its
  margins.

## 9. What this arc does not decide (the next questions)

- **The coincidence loci.** Where SR or the four's base condition fails (M₆'s 28 characters already, and whatever P1 and P2 find),
  a non-zero index near ρ_hyp needs a special twist to meet a root of χ_K. That is a complex-codimension-one condition on the
  crossing locus, so it is generically missed by the real ring. It needs the complex deformations, and is sealed separately.
- **Non-split extensions** (sm:B1509's W₁, W₂; sm:B1515's members), where the index is ±1. Lemma F's hypothesis fails for them
  (C4).
- **Far from ρ_hyp.** Every statement here is local to the hyperbolic point.
- **The experiential question** (GENESIS FK12, under Gate 5-Q): nothing here bears on it.
- **0 of 19 stays 0.** I-26 stays UNEARNED.
