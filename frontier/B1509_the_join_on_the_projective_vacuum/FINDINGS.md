# B1509 — THE JOIN ON THE PROJECTIVE VACUUM: the minimal non-split SU(5) extension of the audit lane's harmonic vacuum carries main's index. At the two μ = −1 backgrounds (q = 17 ± 12√2), the extension along the light 16's SU(5)′-singlet direction has I = −1, and the opposite order has I = +1. The cause is a double root at s = −1 of the palindromic twisted Alexander polynomial, which gives the fibre monodromy a Jordan block. At the four ±i backgrounds the index is 0. On the whole family the 5̄′ sector is vector-like, because the projective four has no boundary cohomology. So the interior count is one 10′ with no 5̄′, which is SU(5)′-anomalous. Over all end conditions the 10′ count is 0, 1 or 2 and the 5̄′ count is always 0. A chiral generation in this join needs one 5̄′ from the end. It also needs a U(1)_X source, or the 16*'s partner direction, to hold the extension at finite energy. 0 of 19.

**Date:** 2026-10-01 · **Seat:** cc (the SM-derivation branch) · **Status:** PROVED. Theorems T1–T3 decide it at design time, together
with the twisted Alexander numerator that the control printed before the seal (disclosed, §7). Predictions D1–D6 were committed and
pushed at 3edaf1fa before the direct run. The run confirms all six, exactly and over three primes. · **Price: unchanged** ·
**Lead:** B1508 §6, lead 1.

**Occasion.** This is B1508's lead 1, taken on the owner's *"do as u recomend, u know the endgoal"*. The first missing bridge (a
physical vacuum that carries a chiral generation) has both halves in the record, but on different backgrounds:
- the audit lane (codex's second lane) has a finite-energy harmonic vacuum family on m004's convex-projective deformation, which is
  vector-like (R42–R56);
- main's index fires on non-split backgrounds (B1297, B1418; this seat's B1374–B1378 and B1506), which have no harmonic metric
  without a source (B1378; the audit lane's R41).

This arc puts the second on the first.

## 0. Seen from above

- **The background.** A = μρ_q, Ballas' holonomy with a central twist μ ∈ μ₄, at the audit lane's four exceptional backgrounds:
  q = 17 ± 12√2 with μ = −1, and q = 7 ± 4√3 with μ = ±i. There h¹(A) = h¹(A*) = 1. In the E₈ parent the light content is "one
  singlet + one 16 + one 16*" (R55, AUD NEUTRAL_CENSUS.md:7, :52).
- **The join.** W₁ = [[A, c], [0, 1]], with c generating H¹(M; A). It has rank five and determinant one, and it is the minimal
  non-split extension. Its off-diagonal block is the SU(5)′-singlet direction of the light 16, with U(1)_T = U(1)_X charge 5. W₂ is the
  opposite order, the 16*'s singlet.
- **The count.**
  - I(W₁) = −1 and I(W₂) = +1 at q = 17 ± 12√2.
  - Both are 0 at the four ±i points.
  - I(Λ²W) = 0 at all six points.
  - In E₈ ⊃ (SU(5) × SU(5)′)/ℤ₅ this gives N(10′) = 1 and N(5̄′) = 0.
- **Why.**
  - T1: the projective four, its dual and Λ² have no boundary cohomology when q ≠ 1. So only the trivial line can carry a count, and it
    sits in W, not in Λ²W.
  - T3: e ∪ c = 0 exactly when the fibre monodromy has a Jordan block at 1. At μ = −1 it does, because the twisted Alexander
    polynomial is palindromic, so s = −1 is a double root.
- **The end decides.** For W₁, an end condition W ⊂ H¹(T; W₁) ≅ ℂ² gives N_W = dim W − 2 (Proposition E).
  - The 10′ count is therefore 2, 1 or 0.
  - Main's interior index is the middle value: W is a complement of the restriction image.
  - The 5̄′ count is 0 under every end condition.
  - The only anomaly-free choice is the vector-like one.
- **Classification (Corollary C).** Take every determinant-one extension of a character by μρ_q, or of μρ_q by a character, on the
  whole family (q > 0, q ≠ 1, any μ). Main's index is nonzero only for W₁ and W₂ at the two μ = −1 points, and I(Λ²W) = 0 for all of
  them.
- **Reading.**
  - The harmonic family gives a definite chiral 10′ once a non-split direction is switched on, but not a generation.
  - The missing 5̄′ and the D-term source are both end or source data, and the record has not derived either.
  - This is B1392's "the ends carry the chirality", met on the audit lane's vacuum, and B1508's "the join is what is missing", now
    with the missing part named.
- **The contrast with R40.** The audit lane's R40 took the rank-five enlargement of R27's m010 coefficient and found
  I(W) = I(Λ²W) = +1: a formal 10 + 5̄ whose SU(5) cubic anomaly cancels. But it has no harmonic background, and R41 found its block
  U(1) to be the wrong source direction. Here the harmonic background exists, but there is no 5̄′. The two defects sit on different
  backgrounds, and the record has not yet put the cancelling count and the vacuum in one configuration.

## 1. Setting

- **The family.** Ballas' convex-projective deformation of the figure-eight complement, as the audit lane transcribes it. t = q/2,
  - m = [[1,0,1,t−1],[0,1,1,t],[0,0,1,t+½],[0,0,0,1]],
  - n = [[1,0,0,0],[2+1/t,1,0,0],[2,1,1,0],[1,1,0,1]],
  - relator mnMNmNMnmN,
  - longitude nMNmmNMn, with characteristic polynomial (X − q)³(X − q⁻³). The control checks the relator and this polynomial.
- **R42** (AUD AFFINE_BACKGROUND.md:8–13) gives this holonomy a complete Blaschke metric and a positive coefficient metric that solve the
  harmonic-flat equations with finite Higgs norm. **R44** (AUD CANONICAL_CUSP.md:49–54, :93) puts the exceptional one/one H¹ modes on
  that same background. Its peripheral argument is the defining four's and its dual's acyclicity.
- **Main's index.** I(V) = n(V) − n(V*), with n(V) = dim ker(H¹(M; V) → H¹(T; V)) (B1297; B1418). This seat's index_lib (B1374)
  computes the data (a0, a1, t0, t1, r1) of V and (b0, b1, s0, s1, q1) of V*. It checks r1 + q1 = t1 = s1 and the B1297 identity
  I = (a0 − b0) + s0 − r1.
- **The extension.** W₁ = [[A, c], [0, 1]] on the generators. It is a representation because c is a cocycle; the run checks the
  relator exactly. W₁[A*] = [[A*, c*], [0, 1]], and W₂ = (W₁[A*])*. W₂ has the trivial line as a sub and A as the quotient.
- **The SU(5) dictionary.** R40 computed (AUD COEFFICIENT_PARENT.md §2):
  > E₈ ⊃ (SU(5) × SU(5)′)/ℤ₅, 248 = (24,1)+(1,24)+(10,5)+(10̄,5̄)+(5,10̄)+(5̄,10), center kernel (ζ, ζ⁻²).

  With W in the first factor, the 10′ comes with W* and the 5̄′ comes with Λ²W*. So N(10′) = n(W*) − n(W) = −I(W) and
  N(5̄′) = −I(Λ²W). The overall sign is a convention: R40 reads its (+1, +1) as "10 + 5̄". What matters here is whether
  I(W) = I(Λ²W), and that holds in both conventions.

## 2. The theorems

**T1 (the matter is boundary-acyclic).** Let q > 0 and q ≠ 1.
- The longitude's eigenvalues are q and q⁻³ on 4, q⁻¹ and q³ on 4̄, and q² and q⁻² on 6 = Λ²4. None of them is 1.
- A character of H₁(m004) = ℤ is trivial on the longitude, which bounds the fibre. So the same holds after any twist.
- On T² the longitude commutes with the meridian and λ − 1 is invertible, so the Koszul complex is exact: H*(T; V) = 0 for every such
  sector V.

Hence:
- H*(M; V) = H*(M, ∂M; V), and every end condition is the same one, W = 0.
- H⁰(M; V) ⊂ H⁰(T; V) = 0, and the same holds for V*.
- The B1297 identity gives I(V) = 0 − 0 + 0 − 0 = 0.
- Poincaré–Lefschetz duality and χ(M) = 0 give h¹(V) = h¹(V*).

So the matter is vector-like in every count. For the defining four and its dual, this is R44's acyclicity.

**T2 (the extension's index).** Let A satisfy H⁰(A) = H⁰(A*) = 0 and H*(T; A) = 0, and let h¹(A) = 1 with generator c. Let
W₁ = [[A, c], [0, 1]].
- On T, c is a coboundary, so W₁|_T ≅ A ⊕ 1 and H*(T; W₁) = H*(T; 1) = (1, 2, 1). So t0 = 1 and t1 = 2, and likewise s0 = 1.
- The connecting map H⁰(1) → H¹(A) sends 1 to c, so a0 = 0 and the map H¹(A) → H¹(W₁) is zero. Hence
  H¹(W₁) = ker(∪c : H¹(M; 1) → H²(M; A)), and H¹(M; 1) = ℂe.
- The restriction factors as H¹(M; W₁) → H¹(M; 1) → H¹(T; 1), and the second map is injective (e is nonzero on the meridian). So
  r1 = a1 ∈ {0, 1}, with r1 = 1 iff e ∪ c = 0.
- Dually, 0 → 1 → W₁* → A* → 0 gives b0 = 1.
- The B1297 identity: **I(W₁) = (0 − 1) + 1 − r1 = −r1**. So I(W₁) = −1 iff e ∪ c = 0.
- For the opposite order, I(W₂) = −I(W₁[A*]) ∈ {0, +1}, by the same argument for A*.
- Λ²W₁ is filtered by Λ²A and A ⊗ 1, both boundary-acyclic by T1. So I(Λ²W₁) = 0, and likewise I(Λ²W₂) = 0.
- **Twists outside μ₄ cannot fire.** Determinant one forces the line to be μ⁻⁴. If μ⁴ ≠ 1, that line is nontrivial on the meridian. Then
  W is boundary-acyclic and I(W) = 0.

**T3 (when e ∪ c vanishes).** The fibration is checked in `wang_monodromy.py`.
- **The fibre group.** With u_k = mᵏ(nm⁻¹)m⁻ᵏ, the Reidemeister–Schreier rewrite of the relator is u₁u₀⁻²u₋₁u₀⁻¹. So
  F = ⟨u₀, u₁⟩ is free of rank two, and the monodromy is φ(u₀) = u₁, φ(u₁) = u₁u₀⁻¹u₁². Its abelianisation has characteristic
  polynomial x² − 3x + 1.
- **The Wang sequence.** Assume H⁰(F; A) = 0, which holds on the whole family (§4). Then H¹(M; A) = ker(S_A − 1) and
  H²(M; A) = coker(S_A − 1), where S_A is the stable letter's action on H¹(F; A) ≅ ℂ⁴. Cup with the fibration class e is the natural
  map ker → coker.
- So e ∪ c = 0 iff S_A has a Jordan block of size ≥ 2 at eigenvalue 1. When h¹ = 1, that happens iff μ is a root of multiplicity
  ≥ 2 of the characteristic polynomial of S_ρ.
- **That polynomial is the monic Q.** Q(q, s) = −q s⁴ + 8q s³ + (q² − 16q + 1)s² + 8q s − q (checked symbolically in §4). Q is
  palindromic: Q = s²·P(s + 1/s), with P(x) = −q x² + 8q x + q² − 14q + 1.
  - s = −1 is a ramification point of s ↦ s + 1/s. At q = 17 ± 12√2, P(−2) = 0 and P′(−2) = 12q ≠ 0, so s = −1 is a double root.
  - At s = ±i the map is unramified (P′(0) = 8q ≠ 0), so those roots are simple.

**Proposition E (every end condition).** Let V be flat on M with torus boundary T. An end condition is a subspace
W ⊂ H¹(T; V), paired with its annihilator W^⊥ ⊂ H¹(T; V*). Its count is
N_W = dim{x ∈ H¹(M; V) : x|_T ∈ W} − dim{y ∈ H¹(M; V*) : y|_T ∈ W^⊥}. Then

    N_W = dim W − h⁰(T; V) + h⁰(M; V) − h⁰(M; V*).

Proof:
- Let R and R* be the two restriction images. They are mutual annihilators: r1 + q1 = t1.
- The first term is (a1 − r1) + dim(R ∩ W). The second is (b1 − q1) + dim((R + W)^⊥).
- (R + W)^⊥ has dimension t1 − r1 − dim W + dim(R ∩ W).
- So N_W = a1 − b1 − r1 + dim W. The B1297 identity and t1 = t0 + s0 (χ(T) = 0, with Poincaré duality on T) turn this into the
  formula.

Consequences:
- N_W depends on dim W only.
- Main's index is N_W for a complement W of R, where dim W = q1.
- The extremes are W = 0, with N = (a1 − r1) − b1, and W = all, with N = a1 − (b1 − q1).
- For W₁ (a0 = 0, b0 = 1, t0 = 1), N_W = dim W − 2.

**Corollary C (the rank-five extensions of the family).** Let q > 0, q ≠ 1 and μ ∈ ℂ*. Let W be a determinant-one extension of a
character by μρ_q, or of μρ_q by a character.
- I(Λ²W) = 0 always (T1).
- I(W) ≠ 0 exactly when W is non-split, μ = −1 and q = 17 ± 12√2. Then I = −1 with the line as quotient (W₁) and +1 with the line as
  sub (W₂).

Proof:
- If μ⁴ ≠ 1, T2's last point gives I(W) = 0.
- If μ⁴ = 1 and W splits, I(W) = I(A) + I(1) = 0.
- A non-split W needs h¹(A) ≠ 0 or h¹(A*) ≠ 0, and these are equal by T1. Under the Wang sequence, h¹(A) ≠ 0 iff μ is a root of the monic
  Q (S_A = μ⁻¹S_ρ).
  - Q(q, 1) = (q − 1)², which has no root with q ≠ 1.
  - Q(q, −1) = q² − 34q + 1 and Q(q, ±i) = −(q² − 14q + 1). Their positive roots are the six points.
- There h¹ = 1, so W₁ and W₂ are unique up to isomorphism, since rescaling c is a conjugation. T2 and T3 give their indices.

All of this is checked in §4.

## 3. The direct run against the predictions

`verification/extension_index.py` → `extension_index_run.txt` uses two routes at all six (q, μ):
- **exact:** DomainMatrix over ℚ(√2, √3, i), porting index_lib's `cohomology_data` and asserting both identities;
- **mod p:** index_lib itself over GF(1009), GF(1033) and GF(1129). Each is ≡ 1 mod 24, so √2, √3 and i exist. Both square-root choices
  are taken, and the relator is checked for A, W₁ and W₁[A*].

| (q, μ) | h¹(A), h¹(A*) | W₁ (a0, a1, t0, r1) | W₁* (b0, b1, s0, q1) | I(W₁) | I(W₂) | I(Λ²W₁), I(Λ²W₂) | N(10′), N(5̄′) | mult. of μ in Q |
|---|---|---|---|---|---|---|---|---|
| (17 ± 12√2, −1) | 1, 1 | (0, 1, 1, 1) | (1, 2, 1, 1) | **−1** | **+1** | 0, 0 | **1, 0** | **2** |
| (7 ± 4√3, ±i), all four | 1, 1 | (0, 0, 1, 0) | (1, 2, 1, 2) | 0 | 0 | 0, 0 | 0, 0 | 1 |

The mod-p route agrees at every point and prime, for I(W₁), I(W₂), both Λ² indices, h¹(A) and h¹(A*). The extension block's U(1)_T
charge is 5 at every point.

| | prediction | outcome |
|---|---|---|
| D1 | I(W₁) = −1 at (17 ± 12√2, −1) | **holds** (exact and three primes) |
| D2 | I(W₁) = 0 at the four ±i pairs | **holds** |
| D3 | I(W₂) = +1 at (17 ± 12√2, −1); 0 at the four ±i pairs | **holds** |
| D4 | I(Λ²W₁) = I(Λ²W₂) = 0 at all six pairs | **holds** |
| D5 | N(10′) = 1, N(5̄′) = 0 at μ = −1; an end contribution is required | **holds** as a count; the anomaly reading is §5 |
| D6 | the block lies in (4, 1₅) ⊂ (4, 16); F-flat, not polystable; needs a source or the 16̄ partner | **holds**: T-charge 5 computed; the rest is §5 |

## 4. Post-run checks

These were computed after `extension_index_run.txt`. They check the proofs' mechanisms and Corollary C. No open outcome rests on them.

**`wang_monodromy.py`** → `wang_monodromy_run.txt` checks T3 directly on the fibre.
- The Reidemeister–Schreier rewrite holds letter by letter. The relation u₂ = u₁u₀⁻¹u₁² holds in ρ_q symbolically. The abelianised
  monodromy's polynomial is x² − 3x + 1.
- The stable letter acts on B¹ as A(m)⁻¹. On Z¹ = A² its characteristic polynomial is (s − 1)⁴ times the monic Q, so on
  H¹(F; ρ_q) it is exactly the monic Q. The control's D(q, s) is q times the polynomial on Z¹.
- At the six points H⁰(F; A) = 0. On H¹(F; A), dim ker(S_A − 1) = 1 everywhere. dim ker(S_A − 1)² is **2 at μ = −1** (a Jordan block
  of size exactly two, since the cube's kernel is also 2) and 1 at ±i.
- The block appears exactly where the run has a1(W₁) = 1. The two routes to e ∪ c = 0 agree at all six points.
- Generic control: at q = 2, all four central twists have ker(S_A − 1) = 0.

**`family_classification.py`** → `family_classification_run.txt` supplies Corollary C's inputs.
- The 70 maximal minors of [ρ(u₀) − 1; ρ(u₁) − 1] over ℚ(q) have numerators with gcd 1. For the dual the gcd is q² + q + 1, so 66 of
  its 70 minors are nonzero. Neither gcd has a positive root, so H⁰(F; ρ_q) = H⁰(F; ρ_q*) = 0 for every q > 0.
- Q at the central twists is (q − 1)², q² − 34q + 1 and −(q² − 14q + 1) (twice). The positive roots other than 1 are exactly
  17 ± 12√2 and 7 ± 4√3.

**`end_conditions.py`** → `end_conditions_run.txt` reads the run's data for W₁.
- At all six points N_W = {0: −2, 1: −1, 2: 0}, and the formula of Proposition E matches.
- The interior choice dim W = q1 gives −1 at μ = −1 (q1 = 1) and 0 at ±i (q1 = 2).
- The 10′ count over all end conditions is {0, 1, 2} at every point.

**`balance_transpose.py`** → `balance_transpose_run.txt` reads R41's balance on this flag.
- **Irreducibility.** A is irreducible at all six points: the algebra generated by A(m) and A(n) is all of M₄ (dimension 16). So the
  only proper invariant subspace of the non-split W₁ is A. There is one flag and one balance; R40's single-Jordan-block four has
  three.
- **The local identity.** In an adapted orthonormal frame, a flat connection that preserves A has ω = [[a, b], [0, d]]. With
  ω_A = (ω − ω⁺)/2, Ψ = (ω + ω⁺)/2 and ξ = 5P − 4 = diag(1, 1, 1, 1, −4) = T, it satisfies tr(Ψ[ω_A, ξ]) = −(5/2)|b|². This is
  R41 §2's "whole-rank projector identity is −5|alpha|^2/2" (AUD CURRENT_BALANCE.md:92–93). Its rank-four form, −2|η_k|² for
  ξ_k = 4P_k − k, reproduces as a control, checked exactly on random Gaussian-rational data.
- **The balance.** With I = −2 d_A^*Ψ = S on a boundaryless finite-energy domain, ∫ tr(T S) = 5 ∫ |b|² > 0.
- **The pairings.**
  - R41's own table for R40's three flags reproduces: T → (0, 0, 0), U → (12, 8, 4), [E₀₄, E₀₄⁺] → (3, 2, 1).
  - For this flag: **T → 20, U → 0**, [E₀₄, E₀₄⁺] → 5.
  - E₀₄'s T-charge is 5.

## 5. The physical reading

**The extension is a vev along the light 16's singlet.**
- E₈ ⊃ SU(4) × Spin(10): 248 = (15,1) + (1,45) + (6,10) + (4,16) + (4̄,16̄). The dimensions check: 15 + 45 + 60 + 64 + 64 = 248.
- The 4 of SU(4) occurs only in (4, 16).
- W₁'s block transforms as g·c, a 4. It lies in su(5), which commutes with SU(5)′, so it is an SU(5)′ singlet. Its T-charge is 5.
- So the block is the (4, 1) component of (4, 16), where 16 = 1 + 5 + 10 under SU(5)′ (up to conjugation of the labels). The class
  c ⊗ v is R55's light 16 along its singlet v.
- su(4) ⊕ su(5)′ has rank 7, so its commutant in E₈ is at most one-dimensional. T and Spin(10)'s U(1)_X both lie in it, so
  U(1)_T = U(1)_X up to normalisation.
- Switching the extension on breaks Spin(10) to SU(5)′. This is the ν^c-like direction of the 16.

**It is F-flat but not D-flat.**
- W₁ is a representation for every multiple of c, because conjugation by diag(1, 1, 1, 1, t) rescales c. So the direction is flat to
  all orders.
- Its orbit is not closed: as t → ∞ the conjugates tend to the split A ⊕ 1.
- A non-semisimple flat bundle has no harmonic metric (B1378, Corlette–Donaldson). R41's balance says what a source must supply:
  ∫ tr(T S) = 5 ∫ |b|² > 0 for the one flag.
- T pairs to 20 with this flag. So a U(1)_X source with positive sign meets the necessary condition. This is the direction R41 found
  wrong for R40's four, and R41's positive U direction pairs to 0 here.
- R41's cautions carry over:
  - a charged commutator already belongs to the bulk moment equation and must not be counted again as a source;
  - the boundary term 2∫_∂ tr(ξΨ(n)) can compensate, and its allowed values must come from the same action.
- In four-dimensional language this is the familiar statement that one charged singlet needs a Fayet–Iliopoulos term, or a partner of
  opposite charge, to be D-flat. Here the partner is the 16*'s singlet (lead 1).

**The count is anomalous in the bulk.**
- Main's interior count gives one net 10′ and no 5̄′. The SU(5)′ cubic anomaly is then 1 ≠ 0, so the bulk count is not a consistent
  spectrum by itself.
- By Proposition E no end condition repairs this inside the bulk. The 10′ count runs over {0, 1, 2}, and the 5̄′ count is 0 under every
  end condition, because Λ²W₁ has no boundary cohomology.
- A chiral generation therefore needs one 5̄′ from outside this sector: from the end, as inflow at a completed cusp, or from another
  state of the architecture (the owner's reframe).
- The record has no model that supplies it:
  - the end's chirality is an input (B1500, B1504);
  - Witten's cubic inflow is zero in both of this seat's local models (B1502 §5);
  - the audit lane's R70 lists what an end with its fixed-period law must add.

**Where a 5̄′ could come from.**
- By T1's argument, I(Λ²W) ≠ 0 needs H*(T; Λ²W) ≠ 0, that is, a joint eigenvalue (1, 1) of meridian and longitude on Λ²W.
- No building block made of the twisted projective four and characters has one: the longitude's eigenvalues are q^{±2} on Λ²A and q,
  q⁻³ on A ⊗ χ.
- So a nonzero 5̄′ count on this family needs a different block. R40's four, on m010, has boundary cohomology in Λ² (its
  I(Λ²W) = +1) but no harmonic metric.

**One per background.** Each of the two μ = −1 backgrounds carries one 10′ (note (17 − 12√2)(17 + 12√2) = 1). Three would need covers
or several states (lead 4).

## 6. What this establishes, and what it does not

**It establishes the following.**
- A nonzero value of main's index on the audit lane's harmonic family, with its mechanism and a classification within the rank-five
  extension shape (Corollary C).
- Sweep for this claim: main (6093e23c), this branch, the audit lane (4a374f4a) and the other four branches (sep16-branch,
  paper-review, physics seat, outside-bench) were searched for Ballas' family. Only the audit lane works on it.
  - The audit lane's R41 §2 (AUD CURRENT_BALANCE.md:92–96) has the local identity for an upper off-block extension of R40's four
    and says the source-free splitting argument still applies. It computes no index for such an extension. Its "No existence or
    chirality claim is made for it" refers to the lower off-block map.
  - Its R40 computes the rank-five index on a different coefficient (m010's).
  - R42–R56 are vector-like.
  - The audit lane cites three other forks (61055575, fe0c2d71, 4b0180ad) as distinct rank-five hyperbolic or commuting models. They
    are not in this repository and were not read.
- Within this frame, the end condition decides the 10′ count (Proposition E), and main's interior index is one choice among them.

**It does not establish the following.**
- No finite-energy background carries W₁: the source and the end are open. **I-26 stays UNEARNED.**
- There is no 5̄′, so the spectrum is anomalous unless the end supplies one.
- No selection of q, μ or the end condition.
- No three.
- **0 of 19.**

## 7. Record and disclosures

- **Order.** `PREDICTIONS.md` (sha256 1c34a70c9da368645811cee52f0f2988e7c88085f65f64b61690d6bb694bcf5a) was committed at 3edaf1fa
  (11:01:34 UTC) and pushed before `extension_index.py` existed. That file was written at 11:02 and run with `--record` at 11:03.
- **The control's slip.** `control_exceptional.py` was meant to reproduce the lane's exceptional points and read nothing sealed. It
  also printed the two-variable numerator D(q, s). Its palindromic form decides D1–D3 through T3. So the direct run verifies the
  predictions and is not a blind test. This arc is banked as decided at design time, as B1500, B1502 and B1504 were. ERROR_LEDGER has a
  rule-slip row.
- **What kind of record PREDICTIONS.md is.** It is an order record, as it says itself ("Its git hash is the order of record").
  It is not a blind preregistration, and it does not carry the seal-provenance rule's BANKED IDENTITY and PRIOR ART markers
  (ERROR_LEDGER, rule slip). In substance:
  - **banked identity:** index_lib's identities (r1 + q1 = t1 = s1, and B1297's I = (a0 − b0) + s0 − r1) are asserted at every point
    before any index is read, exactly and over each prime. The control reproduced the lane's exceptional points before the run;
  - **prior art:** the design-time sweep is B1508 §2 (the audit lane read to R70; main; the other branches). It is repeated in §6
    for this arc's claim.
- **Post-run material.** Proposition E's formula, Corollary C and the four §4 scripts were written after the run. They prove or check
  mechanisms, and none of them changes D1–D6.
- **Instrument repairs before recording.**
  - `balance_transpose.py` first stopped on an API error (DomainMatrix has no `reshape`), with no output.
  - Its second run printed `"local_identity_rank4_flags_control(R41)": false`. sympy's `nsimplify` had rewritten one trial's exact
    rational, −4753/72, as a product of fractional powers, so the equality test failed. The trace of a rational matrix is already
    exact. `nsimplify` was removed and the run was recorded.
  - The failing output had been printed but not saved. It was regenerated byte-for-byte from the deterministic pre-repair script and is
    kept as `balance_transpose_prerepair_run.txt` (ERROR_LEDGER, E7 instance). Only that one key differs from the record.

## 8. Leads (registered, not run; each sealed before computing)

1. **The two-sided deformation.** Switch on c and c* together: the 16's singlet and the 16*'s, with equal norms the D-flat
   direction. It is flat to first order.
   - The second-order obstruction lies in H²(M; sl(5)). Its ℂ part vanishes because H²(M; ℂ) = 0. Its sl(4) part lies in a space of
     dimension 3 (R55: h¹ of the adjoint is 3, and χ = 0).
   - Is the deformation unobstructed, is its orbit closed, and what is its index?
2. **The 5̄′ from the end.** An end or apex model at a completion of the cusp with an SU(5)′ inflow of one 5̄′. Read against the audit
   lane's R60–R71 and this seat's B1500–B1505.
3. **The source from the action.** Derive the U(1)_X source, or the boundary variation law, in the same parent and action. This is R41's
   open duty; for this flag the needed direction is T itself.
4. **Three.** Pull W₁ back to the family's finite covers (R42 covers them) and read the index and the deck orbit in B1506's frame.

> **Note (2026-10-01, B1510):** lead 1 above was taken and run as sealed. The two-sided pair holds in the bulk without a source, is obstructed with the end held fixed (R56's F-term), and counts zero on every two-sided deformation (Theorem C). `frontier/B1510_the_two_sided_deformation`.

## Verification

- `verification/control_exceptional.py` → `control_exceptional_run.txt`: pre-seal; about 6 s.
- `verification/extension_index.py` → `extension_index_run.txt`: the direct run; about 30 s.
- `verification/end_conditions.py` → `end_conditions_run.txt`: reads the run.
- `verification/wang_monodromy.py` → `wang_monodromy_run.txt`: about 9 s.
- `verification/family_classification.py` → `family_classification_run.txt`: about 5 s.
- `verification/balance_transpose.py` → `balance_transpose_run.txt`: about 4 s. The pre-repair output is kept as
  `balance_transpose_prerepair_run.txt`.
- Lock: `tests/test_b1509_the_join_on_the_projective_vacuum.py`.

Quotations from the audit lane were re-read with `git show origin/audit/physical-bridge-2026-09-05:<path>` at the lines cited. AUD
means `reports/physical_bridge_2026_09_05/` on that branch.

0 of 19; the price is unchanged.
