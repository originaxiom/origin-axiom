# B1530 — PREREGISTRATION: THE INTERIOR EXTENSIONS — B1515's rank-five extensions at the hyperbolic point of every word state: at m135's interior classes, at the twists where only interior classes live, and at every simple member, is any member generation-shaped? (sL-10 item 10, first half)

**Sealed before `run_a.py` and `census_bc.py` read any outcome.** At the seal this arc has computed only:
- `controls.py` (S, K1–K4), all hold (`controls_run.txt`, `controls.json`). They read banked members and structure (§6).
- Two dry runs on banked data, disclosed in §6. `run_a.py --dry-run` read sm:B1515's member (1/8, ½) and the trivial character
  on M₆. `census_bc.py --dry-run` ran on m004's levels M₂–M₆, where sm:B1515 banked both population B and the mechanism.

On m135 nothing has been computed beyond sm:B1529's banked rows (K3): no index of W₁, W₂ or their exterior squares, no Jordan type,
no μ, no cup product. On the word states no population-B or Part C quantity has been read.

**Source.**
- **The owner, 2026-10-02:** "do as u recomend with all independently, goal remains", with nothing load-bearing ignored, the
  experiential question included, all allowed states and not only m004, and the hypothesis that the choice might be golden.
- **sm:B1529's census** (committed at `8f833a98`, before sm:B1529's verdict). On every word state to length 12 and on m004's levels
  M₂–M₆, at the hyperbolic point, the twisted four ν ⊗ ρ meets its base condition (h¹ = h¹* = t0 = s0 = 1) at every character with
  ν(t′) = 1, with two exceptions:
  - m135 = −LLRR, at u₁ = (0, ½) and u₂ = (½, 0), where (h¹, h¹*, t0, s0) = (2, 2, 1, 1) with one interior class each. This was
    confirmed exactly over ℚ(i) (sm:B1529 `post_run_exact_m135.json`).
  - M₆, at sm:B1515's 28 characters.
- **sm:B1515 §8**, leads 1–3, verbatim in part: *"The sign law. Is I(W₁) ≥ 0 ≥ I(Λ²W₁) at every λ = 1 member of every level at
  q = 1?"*; *"The interior classes. Why does the twisted geometric four acquire interior classes on M₆ … Read them as
  infinitesimal deformations of the holonomy into SO(4, 1) on a finite cover"*; *"One W with both partners."*
- **sL-10 item 10**, registered here in OPEN_LEADS:
  - (a) the extensions at the interior classes, with the generation test on every word state (this arc);
  - (b) the coincidence loci near ρ_hyp (sm:B1529 §9), sealed separately.

## 0. Seen first, and PRIOR ART:

**The repo sweep.** First `git fetch --all`, then `scripts/checks/prior_work.py`, in two batches:
- "sign law", "Johnson-Millson", "bending", "SO(4, 1)", "SO(4,1)", "Scannell", "Kapovich", "cuspidal cohomology", "parabolic
  cohomology", "Bart", "coincidence", "multiple root";
- "m135", "LLRR", "Massey", "second-order", "second order", "relative obstruction", "generation-shaped", "interior class",
  "parabolic-preserving", "cusp-preserving".

Every hit that bears was read. The heads:

| head | commit |
|---|---|
| main | `399b0bc2` |
| the audit lane | `ddd345a8` |
| this branch | `8f833a98` |
| seat/determined-hopper | `7cda35aa` |
| seat/magical-wright | `0043be2b` |

What bears:
- **sm:B1515 (this branch).** The frame (§1), Lemmas 1–8 and Remark 9. The 24 non-simple order-8 members of M₆ read (+1, −1) at
  boundary-type classes, (0, −1) at the interior class, and W₂ (−1, +1). §5 (c): at such a member r1(Λ²W₁) = 4 = 2 + 1 + 1, *"the
  lift of its interior class. This one is new, and it is what makes the count negative."* That member is control K1.
- **sm:B1529 (this branch).** The census above. Lemma F, the fibre's four-term sequence. `fibre_lib` (route T here). The exact
  reading of m135.
- **sm:B1509 (this branch).** The frame's dictionary, E₈ ⊃ (SU(5) × SU(5)′)/ℤ₅: N(10′) = −I(W), N(5̄′) = −I(Λ²W), and the anomaly
  I(Λ²W) − I(W). T3 is Wang's sequence, H¹ = ker(S − 1) and H² = coker(S − 1).
- **sm:B1513 (this branch).** The up-type coupling is the relative triple product 10′·10′·5′_H. Its independent audit reads a cup
  product as the homomorphism condition on a block map. Lemma B's cubic reading below is a product of this kind for another
  module.
- **Main's B1297, B1440 and B1444 (main).**
  - B1297: the index and its identities.
  - B1440: the rank bound on punctured-torus bundles.
  - B1444 `no_bulk_cubic.py`: the Massey product of an orbit's Higgs classes lands in H²(M; k) = 0. That is another module and
    another product, and it does not decide μ.
- **sm:B1224 and sm:B1226 (this branch).** m135 is amphichiral (Chern–Simons 1/4).
- **OPEN_LEADS L1.** m135 is among the silver states of the metallic diagonal.
- **GENESIS GM5c** (v1.8). The swap-extended metallic family LᵐP, whose squares are the word states LᵐRᵐ. So −LLRR is, up to its
  sign, the square of the silver member L²P, as +LR is the square of the golden LP.
- **sm:B1523 (this branch).** Johnson–Millson appears there as background on flexibility; nothing is computed.
- **Not found on any head:**
  - "relative obstruction" (absent everywhere);
  - "parabolic-preserving" (only sm:B1529's uncommitted draft);
  - any reading of B1515's frame on a word state other than m004's levels;
  - the second-order relative obstruction of an interior class of the four.

**The literature**, searched and read on 2026-10-03:
- **Bart and Scannell, "The generalized cuspidal cohomology problem"**, Canad. J. Math. 58 (2006), 673–690.
  - §2.1: so(4, 1) = so(3, 1) ⊕ ℝ⁴₁ as SO(3, 1)-modules. *"the cuspidal cohomology of Γ with coefficients in the standard
    representation parameterizes infinitesimal parabolic-preserving deformations of Γ into SO(4, 1)"*. PH¹(Γ, ℝ⁴₁) is the kernel of
    the restriction (Scannell).
  - §2.2: bending along a closed embedded totally geodesic surface gives non-zero classes. Kapovich: a lattice generated by two
    parabolics has PH¹ = 0.
  - Theorem 3.1: branched totally geodesic surfaces give classes, dimension at least c₂ − 2c₁.
  - §4.1, Corollary 4.2: PH¹(Γ_d, ℝ⁴₁) = 0 for d = −1, −3, −7.
  - m135's cusp field is ℚ(i), and the twisted classes here live on the finite cover ker ν. Corollary 4.2 is about the Bianchi
    group itself, so it does not exclude them.
- **Monroe, "Branched bending in finite-volume hyperbolic manifolds"**, arXiv:2604.22004 (2026-04-23), §1 and §6.1.
  - The cuspidal cohomology is the kernel of the restriction; for so(4, 1) it agrees with the parabolic one (Kapovich).
  - Garland–Raghunathan: PH¹(Γ, so(3, 1)) = 0 for non-uniform lattices.
  - On the Borromean rings, dim H¹(Γ, ℝ^{3,1}) = 3 with PH¹ = 0, from bending along thrice-punctured spheres.
  - *"the composition of infinitesimal bending deformations supported along intersection hypersurfaces is (typically) not
    integrable"* (after Johnson–Millson).
- **Menal-Ferrer and Porti**, arXiv:1001.2242.
  - Theorem 0.1 is Lemma 3 of sm:B1515: the Higgs bulk Λ²V has no interior class.
  - Theorem 0.3, for n = 2: *"all non-trivial elements in H¹(M; E_Ad∘ρn) are nontrivial in H¹(∂M; E_Ad∘ρn) and have no L²
    representative"* (Garland's L²-infinitesimal rigidity). It is cited for Remark 9's background. It is not used as a proof:
    Part C computes Remark 9's quantity instead.
- **Daly, "Projective rigidity of once-punctured torus bundles via the twisted Alexander polynomial"**, arXiv:2411.04431, §1–2.
  It uses the Lyndon–Hochschild–Serre action on a punctured-torus bundle, the mechanism of Lemma F and sm:B1509 T3.
- **Not found in the literature searched:**
  - PH¹ or a second-order obstruction computed for m135 or its covers;
  - Lemmas A–D below;
  - B1515's frame anywhere outside this repository.

## 1. The question

At the hyperbolic point of every word state to length 12, in B1515's frame (§2): is any member **generation-shaped**, that is,
I(W₁) = I(Λ²W₁) ≠ 0? A generation-shaped member carries one SU(5)′ generation, 10′ + 5̄′, with the cubic anomaly cancelled, in
B1509's dictionary.

The question splits by the twist κ = ν(t′):
- **κ = 1.** Every member is simple except m135's two (Proposition P). At simple members sm:B1515's Lemma 8 holds on every word
  state (Lemma T). So the open cases are:
  - **Part A**, m135's two non-simple members, at every class;
  - **Part C**, the rigidity quantity that decides the simple members.
- **κ ∈ {−1, ±i, ω, ω²} (population B).** A member needs an interior class of ν⁵ ⊗ ρ. Only κ = −1 can be generation-shaped
  (Lemma 5). This is **Part B**.

## 2. Definitions and conventions

- **The states.**
  - Γ = F ⋊ ⟨t⟩, F = ⟨a, b⟩, with the cusp P = ⟨ℓ, t′⟩, ℓ = abAB, t′ = t (+) or abt (−) (sm:B1527 `family_lib`).
  - ρ is the four (h ⊗ h̄, the SO(3, 1) vector representation) at the hyperbolic point.
  - ν = (u, κ): ν|F = u, a torsion character fixed by φ, and κ = ν(t′); ν(ℓ) = 1 always.
  - The base points are κ = 1.
- **The frame** (sm:B1515 §1, verbatim in substance).
  - V = ν ⊗ ρ, L = ν⁻⁴, V_η = ν⁵ ⊗ ρ = V ⊗ L⁻¹, V ⊗ L = ν⁻³ ⊗ ρ, and Λ²V = ν² ⊗ Λ²ρ (the Higgs bulk).
  - A **member** is ν with a class c ≠ 0 in H¹(V_η). Then W₁ = [[V, c·L], [0, L]].
  - W₂ is the opposite order, read through W₂* = [[V*, c′·L⁻¹], [0, L⁻¹]] with c′ ∈ H¹(V_η*); then I(W₂) = −I(W₂*) and
    I(Λ²W₂) = −I(Λ²W₂*).
  - **Case (a):** L = 1. **Case (b):** otherwise.
  - **Simple:** κ = 1 and h¹(V) = h¹(V_η) = h¹(V ⊗ L) = 1.
- **The index** is main's: I(E) = n(E) − n(E*), with n the interior dimension and the B1297 identity I = (a0 − b0) + s0 − r1.
- **The dictionary** (sm:B1509): N(10′) = −I(W), N(5̄′) = −I(Λ²W), and the anomaly I(Λ²W) − I(W).
- **The mechanism quantities.**
  - S₀ on C = H¹(F; V) (sm:B1529 Lemma F; here with V(t′) carrying its character, so the eigenvalue of interest is 1).
  - x is the fibration class, the generator of H¹(M; ℂ) (b₁ = 1).
  - e spans ρ^P.
  - Λ_A ⊂ H¹(T; Λ²V) is the restriction image of H¹(Λ²V).
  - π_A, the parabolic part, is the classes of cocycles of P valued in (Λ²ρ)^P.
  - μ is defined in Lemma B.

## 3. The theorems (proved at design time)

**Lemma T (the cusp at the hyperbolic point is shape-blind).** At the hyperbolic point, ρ|_P is h ⊗ h̄ on a parabolic ℤ² with
cusp shape τ ∉ ℝ.
- For unipotent coefficients, H*(ℤ²; −) is the cohomology of the abelian Lie algebra spanned over ℂ by log ρ(p₁) and log ρ(p₂).
  That span is span(N ⊗ 1, 1 ⊗ N) for every τ ∉ ℝ, since (1, 1) and (τ, τ̄) are independent.
- So sm:B1515's torus table, computed on m004's cusp, holds on every word state's cusp:
  - for every c_P ≠ 0 in H¹(T; ρ), [[ρ_P, c_P], [0, 1]] has (t0, s0) = (1, 2) and its exterior square (2, 3);
  - e ∧ c_P is non-zero in H¹(T; Λ²ρ) and lies in π_A;
  - the torus cups with c_P vanish (t1 = 3 and 5).
- Checked on m135's cusp exactly (S, §6). □

**Lemma 5 (sm:B1515, on every word state).** On P, V has the eigenvalue κ, L has κ⁻⁴, Λ²V has κ² and V ⊗ L has κ⁻³, each times
a unipotent.
- So I(W) ≠ 0 needs κ ∈ μ₄, and I(Λ²W) ≠ 0 needs κ ∈ μ₂ ∪ μ₃ (acyclic ends carry nothing).
- **A generation-shaped member has κ = ±1.** □

**Proposition P (the populations).**
- **κ = 1.** Every character is a member: ν⁵ is trivial on P, and V_η* ≅ conj V_η gives r1(V_η) = 1.
- A member is simple unless the four's base condition fails at u, 5u or −3u. By sm:B1529's census that happens on the word
  states only at m135's u₁ and u₂. On m135 every u has 4u = 0, so 5u = −3u = u, and λ = 1/(ν₀(a)ν₀(b)) has λ⁴ = 1.
- **So the non-simple κ = 1 members of the word states are exactly m135's two, and both are case (a), with ν² = 1.** □

**Lemma 8 holds on every word state** (sm:B1515's mechanism at a simple member, with Lemma T for its Lemma 1).
- At every simple κ = 1 member, (I(W₁), I(Λ²W₁)) = (1 − b0 − δ, bit), where:
  - δ = [the boundary lines of H¹(V) and H¹(V_η) differ] (sm:B1515's ρ, renamed here to keep ρ for the four);
  - bit = [e ∧ c|_P ∈ Λ_A].
- Since e ∧ c|_P ∈ π_A and is non-zero, bit = 1 forces Λ_A ∩ π_A ≠ 0 for Λ²V = ν² ⊗ Λ²ρ.
- **So a simple member is generation-shaped only if Λ_A(ν²) ∩ π_A ≠ 0.** Part C reads that quantity at every χ = ν².

The proof is sm:B1515's. Its inputs are general:
- H²(M; V) ≅ H²(T; V) at simple members; H³(M, ∂M; V) = H⁰(M; V*)^∨ = 0;
- h¹(L) = 1 in case (b) (L non-trivial on F, L(t′) = 1, by Lemma F's sequence with A ≅ B and C ≅ D one-dimensional);
- b₁ = 1, giving x;
- the Higgs bulk has no interior class (Menal-Ferrer–Porti on ker ν²);
- Lemma T. □

**Lemma A (the 10 at the interior class, case (a)).** Suppose:
- ν² = 1 and κ = 1, so L = 1 and V_η = V = V ⊗ L, and V carries the Γ-invariant symmetric form β from ρ;
- h¹(V) = h¹(V*) = 2, t0 = s0 = 1, a0 = b0 = 0;
- c_int is an interior class.

Then **I(W₁(c_int)) = −1**.

*Proof.*
- **The index formula.** W₁|_P splits (c_int|_P is a coboundary), so (t0, s0) = (2, 2). a0 = 0, and b0 = 1 (L* = 1 is an
  invariant line of W₁*). So I = 1 − r1.
- **h¹(W₁).** The sequence 0 → V → W₁ → ℂ → 0 gives h¹(W₁) = (2 − 1) + [x ∪ c_int = 0].
- **x ∪ c_int = 0.** By Wang (sm:B1509 T3), x ∪ c = 0 iff c|_F lies in im(S₀ − 1) on C.
  - The Lefschetz pairing B × C → H²(F, ∂F) = ℂ through β is perfect and S₀-invariant (the monodromy keeps the orientation and
    β). Hence (S₀ − 1)C = (ker(S₀ − 1)|B)^⊥.
  - ker(S₀ − 1)|B = H¹(M, ∂M; V) has dimension 2 (= h¹(V*), Lemma F). It is spanned by a_e (spanning A^{S₀}, t0 = 1) and b_int (a
    lift of c_int; its existence is what interior means).
  - ⟨a_e, c_int⟩ = ±⟨a_e, c_int|∂F⟩ = 0, since c_int|∂F = 0.
  - ⟨b_int, c_int⟩ = ⟨b_int, j b_int⟩ = 0, because the product of two relative classes through a symmetric form is alternating.
- **r1 = 2.** The image of the boundary-type class restricts to a non-zero class in H¹(T; V) ⊂ H¹(T; W₁), and the lift of x
  restricts onto x|_T ≠ 0. So I = 1 − 2 = −1. □

**Lemma B (the 5̄ at the interior class, case (a)).** Under Lemma A's hypotheses:
- every class of H¹(V) lifts to H¹(Λ²W₁(c_int)), because H²(M; Λ²V) → H²(T; Λ²V) is an isomorphism (2 = 2; onto since
  H³(M, ∂M; Λ²V) = 0) and c_int|_T = 0;
- h¹(Λ²W₁) = 4 and s0 = 3 (Λ²W₁|_P = Λ²V|_P ⊕ V|_P).

Let μ ∈ H¹(T; Λ²V)/Λ_A be the restriction of the lift of c_int, read after the splitting e₄′ = e₄ − w on P. It is defined modulo
Λ_A + B¹(P): a change of lift adds Λ_A, and a change of w adds a P-coboundary. Then:
- r1 = 2 (Λ_A) + 1 (the boundary-type class) + [μ ∉ Λ_A];
- **I(Λ²W₁(c_int)) = −[μ ∉ Λ_A]**;
- **so at c_int, (I(W₁), I(Λ²W₁)) = (−1, −[μ ∉ Λ_A]), and m135's member is generation-shaped iff μ ∉ Λ_A.** □

**Remark B′ (what μ is; an interpretation, not used by the reading).** H²(M, ∂M; Λ²V) ≅ H¹(T; Λ²V)/Λ_A, since H²(M, ∂M) → H²(M) is
zero.
- Under this isomorphism, μ is the relative cup square [c_rel ∪ c_rel] of c_int's relative lift. That is the second-order
  obstruction to deforming ρ into SO(5, ℂ) ⊃ SO(4, 1) along c_int with the cusp held fixed.
- By Lefschetz duality it is the cubic form z ↦ ∫ ⟨c_rel ∧ c_rel, z⟩ on z ∈ H¹(M; Λ²V), the deformations of the hyperbolic
  structure (B1515's Higgs bulk). It is a triple product of sm:B1513's kind: the interior class with itself and a Higgs-bulk class.
- If c_int were tangent to a curve of representations into SO(4, 1) holding P's image up to conjugacy, then μ ∈ Λ_A. Bending
  along a closed embedded totally geodesic surface of ker ν is such a curve (Bart–Scannell §2.2). In that case the reading is (−1, 0).

**Lemma C (the 10 at boundary-type classes, case (a)).** Under Lemma A's hypotheses, with am(C; 1) = 4 (sm:B1529, banked), take
c = αc_b + βc_int with α ≠ 0. Then **I(W₁(c)) = [x ∪ c_b ≠ 0] = [S₀ on C has Jordan type (3, 1) at 1]**, the same at every
boundary-type class.

*Proof.*
- By Lemma T, (t0, s0) = (1, 2) and b0 = 1, so I = 1 − r1.
- H¹(W₁) is spanned by c_int's image, which restricts to 0, and the lift of x when x ∪ c = 0, whose restriction projects onto
  x|_T ≠ 0. So r1 = [x ∪ c = 0].
- x ∪ c = α(x ∪ c_b), by Lemma A.
- ker(S₀ − 1)|B = span(a_e, b_int) pairs with ker(S₀ − 1)|C = span(c_b, c_int) through the matrix
  [[0, 0], [⟨b_int, c_b⟩, 0]].
  - ⟨a_e, ·⟩ factors through ∂F. S₀ acts on A and D as J₂, so every invariant class of D lies in (S₀ − 1)D, which a_e
    annihilates.
  - ⟨b_int, c_int⟩ = 0 is Lemma A's.
- So c_b ∈ im(S₀ − 1) iff ⟨b_int, c_b⟩ = 0, iff ker = im on C, iff the Jordan type is (2, 2). With g = 2 and am = 4 the type
  is (3, 1) or (2, 2). □

**Lemma D (the 5̄ at boundary-type classes, case (a)).** At such c:
- h¹(Λ²W₁) = 4 and s0 = 3 (Lemma T: the torus cups vanish and H²(M; Λ²V) ≅ H²(T; Λ²V));
- I(Λ²W₁(c)) = bit − [μ′(c) ∉ Λ_A + ℂ(e ∧ c_P)], with bit = [e ∧ c_P ∈ Λ_A], the same at every boundary-type class, and μ′(c)
  the restriction of the lift of c_int.

So I(Λ²W₁) ∈ {−1, 0, 1}. A generation-shaped boundary-type class needs I(W₁) = I(Λ²W₁) = 1, hence bit = 1, hence Λ_A ∩ π_A ≠ 0
for Λ²ρ on m135 (ν² = 1). That is Part C's quantity at m135's trivial character. □

**Lemma M (the mirror, case (a), ν real).** β gives V ≅ V*, so W₂(c′)* = [[V*, c′], [0, 1]] ≅ W₁(β⁻¹c′).
- Hence I(W₂) = −I(W₁) and I(Λ²W₂) = −I(Λ²W₁) at corresponding classes, interior to interior.
- At a generation-shaped W₁ (both −1), W₂ reads (+1, +1): one 10̄′ + 5′, the anti-generation. □

**Lemma N (the signs at κ = −1).** At κ = −1 every class of V, V_η and V ⊗ L is interior (each is acyclic on P), and L|_P = 1,
Λ²V|_P (κ² = 1) has t0 = s0 = 2.
- **Case (b).** b0 = 0 and s0(W₁) = 1, so I(W₁) = [x_L ∪ c ≠ 0] ≥ 0, while I(Λ²W₁) = 2 − r1 ≤ 0 (r1 ≥ dim Λ_A = 2).
- **Case (a).** b0 = 1 and s0 = 1, so I(W₁) = −[x ∪ c = 0] ≤ 0.
  - Every class y of H¹(V) lifts to Λ²W₁: (c ∪ y)|_T = 0, with Lemma B's isomorphism.
  - So I(Λ²W₁) = −dim(span of the lifts' restrictions modulo Λ_A) ≤ 0.
- **So a generation-shaped κ = −1 member is case (a) and reads (−1, −1).** □

## 4. The instruments

- **Route E, `verification/exact_lib.py` and `exact_states.py` (new code; exact over ℚ(ζ₂₄)).**
  - Fox calculus with left cocycles: Z¹, B¹, H¹ representatives and the restriction to P. The index asserts B1297's identity, the
    annihilator identity and Lemma E at every reading.
  - Extensions [[V, c·L], [0, L]] and exterior squares.
  - The mechanism:
    - `fibre_C`: S₀ on C, Jordan type and χ_C;
    - `cup_with_fibration_class_vanishes`: Wang's test for x ∪ c;
    - `mu_test`: the lift of an interior class and its restriction against Λ_A + B¹(P).
  - m135's holonomy is read exactly in PGL(2, ℚ(i)) (sm:B1529's `exact_sl2`). m004's is read over ℚ(ω) with the same frame, and
    a level is t ↦ tⁿ. The four is H ↦ gHg*/|det g|.
- **Route N, `verification/route_n.py` (60 digits; sm:B1527's `cusp_lib`, banked).**
  - The four at the hyperbolic point in Ballas' paraboloid frame (sm:B1527 `family_lib`).
  - Classes from the Fox kernel, the interior subspace by a numerical kernel. The decisions on projections of unit vectors use an
    absolute threshold (§6, the dry run's finding).
  - Readings by `cusp_lib.class_index`, which checks the identities.
  - Route N reads at route E's own classes, carried across frames by the conjugator X (X ρ_E X⁻¹ = ρ_N on a, b, t; X^−T for the
    duals), and at its own interior class.
- **Part A, `verification/run_a.py`.** m135's eight characters at κ = 1, both routes.
  - Every member: W₁ at its classes (the class; or c_int, c_b, c_b ± c_int, c_b + 2c_int) and W₂* at c′_int, c′_b, c′_b + c′_int.
  - The mechanism (route E): the Jordan type, x ∪ c, μ and bit.
  - The routes compared class by class, and on the interior dimension.
- **Route T (sm:B1529's `fibre_lib`, banked)** and **route G (`verification/census_lib.py`, new).**
  - Route G is Fox calculus on Γ's own presentation, the derivatives grouped by the class of the prefix. It shares no linear
    algebra with `fibre_lib`, `cusp_lib`, `wang_lib` or `exact_lib`.
  - Part C's quantity is read two ways in route G: by rank, and by the torus cup-product pairing between the restricted cocycles
    and π_A through α ∧ β on Λ²ℂ⁴ (Λ_A Lagrangian and π_A isotropic, both checked, so the pairing's rank is
    2 − dim(Λ_A ∩ π_A)).
- **Parts B and C, `verification/census_bc.py`.** sm:B1529's 541 rows: the 536 word states, read as its census read them, and
  M₂–M₆. At the hyperbolic point, 60 digits, four workers.
  - **B:** route T's h¹ at κ ∈ {−1, ±i, ω, ω²} for every character. Route G's h¹ at κ = −1 for every character, and at the other κ
    wherever route T reads h¹ ≥ 1 and at the first two characters of each state.
  - **C:** Λ_A ∩ π_A at χ = ν² for every κ = 1 character ν (the base points of 2u).
- **`verification/read_out.py`** reads §7 from `run_a.json` and `census_bc.json`.
  - A population-B member is ν with ν⁵ among route T's hits.
  - Every κ = −1 member is read by routes N and W (sm:B1527 `wang_lib`, Lemma E) at every class of a basis and the sum of the
    basis. That is done after the census by `post_run_b.py`, which is written only if such a member exists, and disclosed.

## 5. The states

- **Part A:** m135 = −LLRR, its eight characters at κ = 1 (two non-simple, six simple).
- **Parts B and C:** sm:B1529's 536 word states and M₂–M₆.

## 6. Controls and disclosures (before the seal)

- **`controls.py` → `controls_run.txt`, `controls.json` (58 s; all hold).**
  - **S:** Lemma T on m135's cusp at eight exact points of H¹(T; ρ): (t0, s0) = (1, 2) and (2, 3), with e ∧ c_P ≠ 0 at each.
  - **K3:** route E reproduces sm:B1529's exact m135 record at all eight characters: (h¹, h¹*, t0, s0) and n, with (2, 2, 1, 1),
    n = 1 at u₁ and u₂.
  - **K2:** R40 on m010 (sm:B1515 K6) reads I(V) = I(Λ²V) = I(W) = I(Λ²W) = +1, n(Λ²W) = 2 and n(Λ²W*) = 1 exactly, at both
    u = e^{±iπ/3}. That is the positive control: route E reads a generation-shaped configuration where one exists.
  - **K1:** sm:B1515's member on M₆ at u = (1/8, ½) reads exactly h¹(V) = h¹(V_η) = h¹(V ⊗ L) = 2, W₁ (+1, −1) at a boundary-type
    class and (0, −1) at c_int, and W₂ (−1, +1).
  - **K4:** the mechanism functions on banked cases:
    - m004's χ_C = (s − 1)²(s² − 6s + 1) with one J₂ at 1 (sm:B1509, sm:B1515 Lemma 10);
    - M₆'s trivial character, simple and case (a): x ∪ c = 0 and W₁ = (0, 0);
    - K1's member: the lift of V ⊗ L's interior class at c_int restricts outside Λ_A, as the banked (0, −1) requires.
- **`run_a.py --dry-run` → `dry_run_a.json`, `dry_run_a_log.txt`.** The same two M₆ characters, both routes, every class.
  - Routes E and N agree class by class, with route E's classes carried across frames.
  - (1/8, ½): c_int (0, −1), every boundary-type class (1, −1), W₂ (0, 1) at c′_int and (−1, 1) at the boundary-type classes.
  - (0, 0): (0, 0).
  - **The dry run's finding (fixed before the seal; ERROR_LEDGER, E52 instance).** On its first pass, route N's class finder
    returned an "interior class" at the simple character (0, 0), where there is none, and W₁ there read (−1, −1).
    - It decided the rank of a projection that should be zero with a threshold relative to its own largest singular value, so it
      read rounding noise (about 10⁻⁵⁵) as a vector.
    - The decision is now absolute: the columns are projections of unit vectors. `run_a.py` also compares route N's interior
      dimension with route E's at every character.
    - This is the known error class (sm:B1529's `fibre_lib.rank_mp`: "a relative threshold alone would read rounding noise as full
      rank"). Caught before any sealed reading.
- **`census_bc.py --dry-run` → `dry_run_bc.json`** (on M₂–M₆ only).
  - **B:** route G reads h¹ = 0 at κ = −1 at all 507 characters, and routes T and G agree at all 561 comparisons.
    - Route T's hits at κ ≠ 1 are sixteen, all at order-5 characters of M₂ and M₄ at κ ∈ {ω, ω²}. None is a fifth power.
    - So population B is empty on M₂–M₆, as sm:B1515 banked.
  - **C:** Λ_A ∩ π_A = 0 at all 255 χ, by rank and by pairing, with dimensions (2, 2) throughout, as sm:B1515 banked at every
    simple member.
- **Not computed before the seal:** any of m135's W₁, W₂ or Λ² readings; the Jordan type, x ∪ c or μ on m135; any word state's
  population B or Part C.

## 7. Predictions (sealed; `read_out.py` reads them)

| | prediction | prior |
|---|---|---|
| P1 | Lemma A: I(W₁) = −1 at c_int at both of m135's non-simple members, both routes | 97% |
| P2 | **the question at m135:** (I(W₁), I(Λ²W₁)) = (−1, −1) at c_int (Lemma A and μ ∉ Λ_A), so m135's interior class is generation-shaped: W₁ carries one 10′ and one 5̄′. Both routes, both members | 55% |
| P3 | Lemmas C and D: at the boundary-type classes read, I(W₁) is one value, equal to [Jordan type (3, 1)], and no boundary-type class is generation-shaped | 90% |
| P4 | Lemma 8: m135's six simple members read (I(W₁), I(Λ²W₁)) = (0, 0) | 95% |
| P5 | Lemma M: W₂ reads −W₁ at the corresponding classes, at all eight characters | 97% |
| P6 | population B at κ = −1 is empty on every word state and level: no character with h¹(ν⁵ ⊗ ρ) ≥ 1 at κ = −1, by routes T and G | 75% |
| P7 | Part C: Λ_A ∩ π_A = 0 at every χ = ν² (κ = 1) on every word state and level, by rank and by pairing | 97% |
| P8 | the mechanism at m135: x ∪ c_int = 0, and c_int lifts to H¹(Λ²W₁), at both members | 97% |
| G | the golden form of the owner's hypothesis: every state carrying a generation-shaped member at its hyperbolic point is golden (∣trace∣ ∈ {3, 7, 18, 47, 123, 322}) | 40% |

Recorded, not predicted:
- the Jordan type at u₁ and u₂;
- bit and the boundary-type Λ² readings;
- population B's hits at ±i, ω and ω², with their golden distribution, the members they make, and Lemma 5's check there;
- Part C's margins and isotropy.

The priors:
- P2's 55% rests on K1. On M₆ the interior class's lift restricts outside Λ_A, the analogue of μ ∉ Λ_A. Against it, m135's class
  could be a bending class with μ = 0 (Remark B′).
- G's 40% follows P2, since m135 is not golden.

## 8. BANKED IDENTITY: checked before reading

- `controls.py` is re-run first and must reproduce `controls.json` (S, K1–K4 all hold). Otherwise nothing is read.
- `run_a.py` repeats K3 at m135's eight characters (route E's h¹ rows), and every reading carries B1297's identity, the
  annihilator identity and Lemma E.
- `census_bc.py`'s rows on M₂–M₆ must reproduce `dry_run_bc.json` (population B empty; Λ_A ∩ π_A = 0).
- Route T's h¹ at κ = 1 is not recomputed. sm:B1529's census is the banked record for κ = 1.

## 9. Reading rules, and what this arc will and will not claim

- **The routes must agree**:
  - E and N, class by class and on the interior dimension;
  - T and G wherever both read;
  - rank and pairing in Part C.

  A disagreement withholds the verdict and goes to ERROR_LEDGER first (the owner's rule, NO NEGATIVE FROM A BUG).
- **The verdict.**
  - **If P2 holds** (both routes), the verdict is **PROVED**: the first generation-shaped member of B1515's frame, at m135's
    interior class. W₁ carries one 10′ + 5̄′ and W₂ the anti-generation. It is read with the caveats below.
  - **If P2 fails, and no κ = −1 member is generation-shaped, and P7 holds**, the verdict is **NEGATIVE**: B1515's frame carries no
    generation-shaped member at the hyperbolic point of any word state to length 12 or of M₁–M₆. That goes to the kill graph.
  - **If P7 fails at some χ**, the simple members there are read directly (both routes) before any verdict, after the run and
    disclosed.
  - **A κ = −1 member** is read as §4 says. If one is generation-shaped, the verdict is PROVED on that member.
- **Caveats for any non-zero count** (as sm:B1515 §6 and §8).
  - The cusp is not sealed (t1 > 0): the count comes with continuous spectrum (B1392), and the twisted operator is not Fredholm.
  - The count is main's interior index. Proposition E's ranges are reported and not used. sL-8's rule (B1392:115) forbids choosing
    an end condition because it rescues a count.
  - In case (a), L = 1, so W₁ = [[V, c], [0, 1]] is an affine extension of V by the trivial line, and W₁* has an invariant vector
    (b0 = 1).
- **What the arc will not claim:**
  - a mass or a coupling;
  - that m135, the hyperbolic point or any member is selected by dynamics;
  - anything off the hyperbolic point, beyond length 12, or for non-unitary twists;
  - anything about I-26;
  - anything bearing on the experiential question (GENESIS FK12, under Gate 5-Q; nothing here bears on it).
- **0 of 19 stays 0.** A generation-shaped member is a matter-content statement. It prices no parameter.

## 10. What this arc does not decide (the next questions)

- **The coincidence loci** near ρ_hyp (sm:B1529 §9; sL-10 item 10 (b)).
- **Off the hyperbolic point.** Along the eigenvalue-one locus, the members' classes deform. Whether a generation-shaped reading
  survives is a separate, sealed question.
- **The geometric origin of m135's interior classes.** Are they bending along a surface in ker ν (Bart–Scannell, Monroe)? Remark B′
  ties μ to that.
- **The levels above 6** (sm:B1515 lead 2) and the word states beyond length 12.
