# B1510 PREREGISTRATION — THE TWO-SIDED DEFORMATION: the 16's and the 16*'s singlets switched on together. Do they hold without a source, can the trivial line keep its cusp eigenvalues, and what do they count?

**Sealed 2026-10-01, before the two-sided deformation is computed at any of the six points. Seat: cc (the SM-derivation branch).
Occasion: the owner's "do the recomendation for next", that is, B1509's lead 1 (FINDINGS §8).**

## 0. The question

B1509 switched on one singlet direction at a time on the audit lane's harmonic vacuum. Write ρ₀ = A ⊕ 1, with A = μρ_q Ballas'
projective holonomy of m004 with a central twist.
- c ∈ H¹(π; A), the 16's singlet, gives W₁ = [[A, c], [0, 1]], with main's index −1 at μ = −1. That is one 10′.
- c* ∈ H¹(π; A*), the 16*'s singlet, gives W₂ = [[A, 0], [c*ᵀA, 1]], with index +1.

A one-sided extension is F-flat but not D-flat. Its orbit is not closed, so it needs a source (B1509 §5). The partner that could make
the pair D-flat without a source is the other singlet. This arc switches both on together:

  ρ_ε(g) = (I + ε(s U_c + t U_{c*}) + ε² U₂ + …) ρ₀(g),   s t ≠ 0,

and asks four questions.
- **Q1 (without a source).** Does the formal two-sided deformation exist, with the end free? By Corollary A″ below, every member with
  s t ≠ 0 is irreducible, so its orbit is closed.
- **Q2 (with the end fixed).** Is it obstructed if the cusp holonomy is held fixed?
- **Q3 (the chiral branch).** Can the trivial line keep its peripheral eigenvalues (1, 1) along it? On an irreducible module, main's
  index can be nonzero only then.
- **Q4 (the count).** What is main's index on it?

Q2 and Q4 are decided at design time (§3, §6.1), and so is Q1 at ±i, by prior art. The sealed predictions are Q1 at μ = −1 and Q3
(§6.2).

## 1. Setting and notation

- **The group.** π = ⟨m, n | mnMNmNMnmN⟩. The meridian word is m and the longitude is ℓ = nMNmmNMn (index_lib and B1509 conventions).
  The field F is either Q(√2, √3, i) or GF(p), p ∈ {1009, 1033, 1129}.
- **The background.** A = μρ_q at the six points (17 ± 12√2, −1) and (7 ± 4√3, ±i), as in B1509. There h¹(π; A) = h¹(π; A*) = 1,
  spanned by c and c*.
- **The adjoint.** Under Ad ρ₀, gl(5) = gl(4) ⊕ A ⊕ A* ⊕ F:
  - the upper-right column is ≅ A;
  - the lower-left row is ≅ A* (by transpose);
  - the corner is trivial.
- **Deformations.** ρ_ε(g) = (I + Σ_k ε^k U_k(g)) ρ₀(g), with the left cocycle convention u(gh) = u(g) + Ad ρ₀(g) u(h).
  - The relator's order-k coefficient is R_k = J(U_k) + P_k. Here J is the Fox coboundary and P_k is a polynomial in U₁ … U_{k−1}.
  - H²(π; gl(5)) = coker J.
  - U_c puts c(g) in the upper-right column and U_{c*} puts c*(g)ᵀ in the lower-left row. The first-order term is
    U₁ = s U_c + t U_{c*}.
- **Line eigenvalues.** λ_g(ε) is the eigenvalue of ρ_ε(g) that continues the corner's 1. It is the Schur fixed point
  λ = X₅₅ + X₅A (λ − X_AA)⁻¹ X_A5. It is defined for g = m and g = ℓ, because neither A(m) (μ times a unipotent) nor A(ℓ)
  (eigenvalues q, q, q, q⁻³; B1509's control) has eigenvalue 1.
- **Free classes.** e: π → F is the abelianisation, with e(m) = e(n) = 1. The other free classes are:
  - the twist T = e · diag(1, 1, 1, 1, −4);
  - the centre e · I₅;
  - the adjoint classes H¹(π; sl(4)_{Ad A}).
- **Main's index.** I(W) = n(W) − n(W*), where n(V) = dim ker(H¹(M; V) → H¹(T; V)).
  - The data are (a0, a1, t0, r1) for V and (b0, b1, s0, q1) for V*.
  - Over F((ε)) the index is read from ranks alone (deform_lib.index_laurent): n(V) = 2d − rank[[J, 0], [Res, −B_T]] − t0 + a0.
    Each rank is taken by full pivoting on minimal ε-valuation, with the precision left reported.

## 2. Computed before the seal (disclosed)

`verification/two_sided.py --controls` → `verification/controls_run.txt`. No control computes adjoint cohomology at the six points,
and none computes a two-sided term there.

**C0 — rank over F((ε)).** Four valuation-rank unit cases pass.

**C1–C3 — the one-sided and split families (the banked identity).** These are the exact families [[A, εc], [0, 1]],
[[A, 0], [εc*ᵀA, 1]] and A ⊕ 1 at all six points over the three primes.
- All 54 rows reproduce B1509's I(W₁), I(W₂) and the split 0: −1/+1 at μ = −1, 0/0 at ±i.
- The relator holds exactly to order 6.
- The least precision left is 6.

**C4 — GL(2) on m004.** ρ₀ = diag(α, 1), with α(m) = α(n) = t₀ a root of t² − 3t + 1. GF(1033) has no √5 and was skipped. This is
Burde, de Rham, and Heusener–Porti–Suárez's setting at a simple root.
- At all four roots the two-sided branch exists to order 8.
- It is parity-symmetric.
- Its index over F((ε)) is 0, with (a0, b0, a1, b1, t0, s0, r1, q1) = 0 and precision left 7.
- A character is 1 on the longitude, so the line is not separated there and there is no chiral reading.

**C5 — the chiral solver on the one-sided direction.** (s, t) = (1, 0) at the six μ = −1 pairs, with the named classes only.
- The solver returns the exact family: every choice is zero and U_k = 0 for k ≥ 2.
- The line stays at (1, 1) to order 6.
- I = −1.

**C6 — the adjoint machinery in rank three, outside the sealed population.** ρ₀ = (t ρ_geo) ⊕ 1, with ρ_geo m004's geometric
representation mod p (m = [[1, 1], [0, 1]], n = [[1, 0], [z, 1]], z² + z + 1 = 0) and t = 2 ± √3, the roots of the hyperbolic torsion
polynomial t² − 4t + 1, where h¹(t ρ_geo) = 1. This is Heusener–Porti's setting at a simple root. At all six (p, t):
- h¹(gl(3)) = 5 (c, c*, the twist, the centre and one adjoint class), the restriction H¹(π; sl(2)) → H¹(T; sl(2)) is injective, and
  h⁰(T; gl(2)) = 2;
- the order-two obstruction is 0;
- the free-end branch (GL mode) exists to order 8 and is parity-symmetric;
- at every odd order the A- and A*-obstructions are both nonzero, and the free classes reach them along one line: the rank is 1 on the
  A rows, 1 on the A* rows and 1 in total. The obstruction lies on that line;
- the fixed-end class has o_rel_sl = 1, its line part equals κ̂_ℓ ≠ 0, and the block trace at ℓ is −κ̂_ℓ;
- I = 0, with a1 = b1 = r1 = q1 = 0 and precision left 7.

**Design inputs about A alone.** These concern the background, not a sealed quantity, and are computed exactly.
- m − 1 has rank 2, (m − 1)² has rank 1 with (1,4) entry (q + 1)/2 ≠ 0, and (m − 1)³ = 0, at all six points. So the meridian is
  μ times a unipotent of Jordan type (3, 1).
- B1509's control record gives the longitude's characteristic polynomial (X − q)³(X − q⁻³).

**Disclosures.**
- The design-time sweep (§5.1) found the audit lane's F15 and R55. They decide two items that an earlier draft of this preregistration
  carried as open predictions: cusp rigidity, and the fixed end's sl(4) part. Both moved to §6's decided list before the seal.
- The solver was redesigned after the design analysis of §3 (Theorem D) and before any sealed quantity was computed. It got projected
  particular solutions and the shifted longitude condition.
- C6 caught a defect in the adjoint-basis routine (a transposed product). It was fixed before the seal.
- At the six points nothing was computed except:
  - the one-sided exact families (B1509's banked quantities);
  - the relator of those families over Q(√2, √3, i) to order 3 (exact plumbing);
  - the shape of the adjoint Fox matrix there (no rank or class read).

## 3. Proved now (design time)

**Lemma 0 (the blocks of H²).** H²(π; F) = 0, because J at the trivial representation is (1, −1). Hence
H²(π; gl(5)) = H²(sl(4)) ⊕ H²(A) ⊕ H²(A*), with h²(A) = h²(A*) = 1 (χ = 0 and h⁰ = 0). Also H*(T; A) = H*(T; A*) = 0, because A(m)
has no eigenvalue 1.

**Theorem A (the sl(4) obstructions are detected at the cusp, and vanish).** Assume:
- **(R)** res: H¹(π; sl(4)) → H¹(T; sl(4)) is injective;
- **(C)** h⁰(T; gl(4)_{Ad A}) = 4.

Then for every formal deformation of ρ₀, given modulo ε^k, the sl(4)-component of the order-k obstruction vanishes. In particular
o(c, c*) = 0 at order two.

*Proof.*
1. **Injectivity on H².** Ad A is self-dual through the Killing form. Use the sequence H¹(M) → H¹(T) → H²(M, T) → H²(M) → H²(T), with
   H²(M, T) ≅ H¹(M)^∨. The map H¹(T) → H²(M, T) is dual to res. So res is injective iff H²(M; sl(4)) → H²(T; sl(4)) is injective.
2. **The cusp is smooth.** By naturality, the restriction of the obstruction to T is the obstruction of ρ_ε|_T. Under (C),
   h⁰(T; gl(5)) = 4 + 0 + 0 + 1 = 5. Since dim B¹ = 25 − h⁰ and h¹ = 2h⁰ on the torus, dim Z¹(T; gl(5)) = 25 + h⁰ = 30. That is
   the dimension of the commuting variety of gl(5), which is irreducible of dimension n² + n. So the local ring of Hom(ℤ², GL(5))
   at ρ₀|_T is regular, every jet extends, and the restricted obstruction vanishes.
3. **Conclusion.** Combine 1 and 2. □

**Lemma R (cusp rigidity holds here).** Assume the audit lane's exact data (F15, R55):
- h¹(π; sl(4)) = 3;
- the meridian restriction has rank 2;
- its kernel is spanned by the q-tangent of Ballas' family.

Then (R) holds.

*Proof.*
1. The q-tangent restricts non-trivially to ⟨ℓ⟩. tr ρ_q(ℓ) = 3q + q⁻³ has derivative 3 − 3q⁻⁴ ≠ 0 at every q with q⁴ ≠ 1. A coboundary
   on ⟨ℓ⟩ keeps the characteristic polynomial to first order. The twist does not touch ℓ, since e(ℓ) = 0.
2. If res(z) = 0, then res_m(z) = 0, so z = α·(q-tangent). Then res_ℓ(z) = 0 forces α = 0. □

**Lemma C (the cusp pair is regular).** h⁰(T; gl(4)) = 4.

*Proof.*
1. ℓ has the generalised eigenspaces V_q (dimension 3) and V_{q⁻³} (dimension 1), with q ≠ q⁻³. m commutes with ℓ, so it preserves
   both.
2. m's Jordan type is (3, 1) (§2). Its 3-block must lie in V_q, so m|V_q is regular.
3. The joint centraliser is block diagonal: polynomials in m|V_q (dimension 3), plus scalars on V_{q⁻³}. That makes 4. □

*So Theorem A's hypotheses hold at all six points.* The sl(4) obstructions vanish at every order, and in particular o(c, c*) = 0. This
is decided at design time, given F15/R55's cited numbers; the sealed run recomputes them.

*Corollary A′.* Given (R) and (C), the only possible obstructions to any deformation of ρ₀ lie in H²(A) ⊕ H²(A*), which is
two-dimensional. Neither is seen by the cusp (Lemma 0).

*Corollary A″ (irreducibility).* Every formal deformation whose first-order term has s t ≠ 0 is absolutely irreducible over F((ε)).
- Over F̄, the only ρ₀-invariant subspaces are 0, the line, A and everything, so a limiting invariant subspace must be the line or A.
- An invariant line continuing e₅ forces s c to be a coboundary (compare the order-one A-components).
- An invariant hyperplane continuing A forces t c* to be a coboundary (dually).
- Hence a0 = b0 = 0, and the orbit is closed. □

**Theorem B (the line's longitude at order two).** For U₁ = s U_c + t U_{c*},

  λ_ℓ(ε) = 1 + s t κ̂_ℓ ε² + O(ε³),  κ̂_ℓ = Φ(ℓ) + r̂(ℓ)(I − A(ℓ))⁻¹ ĉ(ℓ),

where r̂(g) = c*(g)ᵀA(g), ĉ = c, and Φ is any 1-cochain with δΦ = −(c* ⌣ c), which exists by Lemma 0. Moreover:
- κ̂_ℓ = ±⟨e ∪ c, c*⟩, the pairing H²(M; A) × H¹(M, T; A*) → F;
- κ̂_ℓ = 0 iff e ∪ c = 0 iff the fibre monodromy has a Jordan block at eigenvalue 1 (B1509 T3);
- so κ̂_ℓ = 0 at μ = −1 (q = 17 ± 12√2) and κ̂_ℓ ≠ 0 at ±i.

*Proof.*
1. **The order-two eigenvalue.** The Schur formula with λ = 1 + O(ε²) gives the order-two coefficient as the stated expression. Φ is
   the corner of U₂ extended along words: Φ(gh) = Φ(g) + Φ(h) + r̂(g)ĉ(h). Adding x·e to Φ changes nothing at ℓ, since e(ℓ) = 0.
2. **A homomorphism on the cusp.** Since H*(T; A) = 0, c|_T = δv with v = (A(ℓ) − 1)⁻¹ c(ℓ). Then Ψ(g) = Φ(g) − r̂(g)v is a
   homomorphism T → F, by direct expansion. Its value Ψ(ℓ) = κ̂_ℓ.
3. **The cup product.** Ψ is the boundary term of the relative cup product [c* ∪ c]_rel ∈ H²(M, T; F) ≅ H¹(M; F)^∨, which lies in the
   image of H¹(T; F) because H²(M; F) = 0. Pairing with e (e|_T = (1, 0)) reads off Ψ(ℓ). So κ̂_ℓ = ±⟨e ∪ c* ∪ c, [M, ∂M]⟩.
4. **The pairing is perfect.** H²(M; A) ≅ F pairs perfectly with H¹(M, T; A*) ≅ H¹(M; A*) = F c* (Poincaré–Lefschetz and
   boundary acyclicity). B1509 T3 gives the equivalence with the Jordan block. □

**Proposition F (the fixed-end class).** Gauge the first-order cusp term to zero; this is possible since c|_T and c*|_T are
coboundaries. The second-order cusp term then has a class o_rel in H¹(T; gl(5)) / res H¹(M; gl(5)), which is the image of
H¹(T) → H²(M, T). Its components are:
- **the sl(4) part,** which corresponds under duality to the functional a ↦ ⟨[a ⌣ c], c*⟩ on H¹(π; sl(4)), up to the factor 2st and
  sign. Given (R), this is an isomorphism H¹(T; sl(4)) / res ≅ H¹(π; sl(4))^∨. So o_rel,sl ≠ 0 iff the triple product
  τ(a) = ⟨[a ⌣ c], c*⟩ is not identically zero;
- **the line part** at ℓ, which equals s t κ̂_ℓ;
- **the block trace** at ℓ, which equals −s t κ̂_ℓ, because det ρ_ε(ℓ) = 1.

The off-diagonal parts are coboundaries (boundary acyclicity).

*Proof.* The relative second-order obstruction pairs with z ∈ H¹(M; gl(5)) through the trace form as ⟨z ∪ u ∪ u⟩. The off-diagonal
z pair to zero, the adjoint z give τ, and e·(twist) and e·(centre) give multiples of ⟨e ∪ c, c*⟩ (Theorem B). □

*Decided by F15.* The audit lane's F15 computes the first-order matter-retention obstruction [u ⌣ c] ∈ H²(π; A) (one-dimensional)
for every u ∈ H¹(π; sl(4)). It finds both sector rows, for c and for c*, nonzero and proportional, with joint rank one and a kernel of
dimension two. H²(A) pairs perfectly with F c*, so "row nonzero" is τ ≢ 0. Hence o_rel,sl ≠ 0 at all six points.

In R56's language, this is F_S = λ Q·Q̃ ≠ 0 on the singlet pair, with the end held fixed.

Two further facts follow.
- τ ≠ 0 is also what makes the jumping locus D = {H¹(β ⊗ λ⁻¹) ≠ 0} a smooth hypersurface in the reducible locus near ρ₀, with
  tangent ker τ.
- At μ = −1, where e ∪ c = 0, the order-three odd obstruction can only be met by the adjoint choice through τ.

**Theorem C (the index of a two-sided deformation is zero).** Let W_ε be a representation of π over F[[ε]] with W₀ = ρ₀ and, over
F((ε)), a0 = b0 = 0. This includes every deformation with s t ≠ 0 (Corollary A″). Then
- I(W_ε) = 0;
- a1 = b1 ≤ 1;
- t0 = s0 ∈ {0, 1} and r1 = q1 = t0;
- if the line keeps (1, 1), then a1 = b1 = r1 = q1 = 1.

*Proof.*
1. **Upper semicontinuity.** rank J_ε ≥ rank J₀ = 4, since H²(π; A ⊕ 1) = H²(A) ⊕ H²(F) = F. So a2(ε) ≤ 1, and likewise b2(ε) ≤ 1.
2. **Euler characteristic.** The presentation complex is aspherical (Lyndon), so a1 = a0 + a2 = a2 ≤ 1 and b1 ≤ 1.
3. **The cusp splits.** A(m) − 1 stays invertible over F[[ε]], so W_ε|_T splits by Hensel as B_ε ⊕ L_ε, with B_ε(m) − 1 invertible
   and L_ε a character. Hence H*(T; W_ε) = H*(T; L_ε), t0 = s0 = [L_ε trivial], and t1 = 2 t0.
4. **The two cases.** Poincaré–Lefschetz duality gives r1 + q1 = t1.
   - If t0 = 0: then r1 = q1 = 0, and a2 = b1 via H²(M; V) ≅ H¹(M, T; V*)^∨ ≅ H¹(M; V*)^∨. So a1 = b1.
   - If t0 = 1: then r1 + q1 = 2 with r1 ≤ a1 ≤ 1 and q1 ≤ b1 ≤ 1, which forces r1 = q1 = a1 = b1 = 1.

   In both cases I = (a1 − r1) − (b1 − q1) = 0. □

*So Q4 is decided: switching on both singlets counts zero.* B1509's one 10′ belongs to the one-sided extension alone. The partner
that could make the pair D-flat pairs it away.

**Theorem D (parity, and the shifted longitude condition).**
- **(i) Parity.** Let D = diag(I₄, −1). If ρ_ε is a deformation with first-order term U₁, so is D ρ_{−ε} D⁻¹, with the same U₁. The
  solver's normal form has block-diagonal even orders and off-diagonal odd orders; this is checked in verify(), parity flag.
- **(ii) Lemma L.** The order-k coefficient of λ_ℓ does not depend on U_k. The corner of u_k(ℓ) is the exponent-sum-weighted corner of
  U_k, and ℓ is null-homologous.
- **(iii) The dependence one order down.** Changing the order-k free choice by δ changes λ_ℓ at order k + 1 by the polarisation of
  u ↦ s t κ̂_ℓ at (U₁, δ). That is (s δt + t δs) κ̂_ℓ for odd δ, and zero for even δ: block × off-diagonal is off-diagonal, so there is
  no corner and no Schur term at that order.

So where κ̂_ℓ = 0, at μ = −1, the order-(k+1) longitude condition cannot be met by the order-k choice. The chiral solver imposes it at
the order-(k−1) step, read with U_k equal to the projected particular solution. There it enters through the trilinear term
⟨c*, a, c⟩(ℓ) of the adjoint choice a.

This scheme is sufficient, not necessary.
- **Success** is certified by verify(): the relator to order N, det = 1, and λ_m, λ_ℓ ≡ 1 to order N.
- **A stop** is reported with its order and rank data. It is not read as an obstruction theorem.

**Prior art decides ±i.** μ = ±i is a simple root (B1509 T3), and Δ₀ ≠ 0 there (B1509 Corollary C(i): H⁰(F; ρ_q) = 0).
- A is infinitesimally regular (h¹ = 3 = a − 1: F15, R55; checked as D1). So Heusener–Porti 2015, Thm 1.4 says ρ₀ deforms to
  irreducible representations.
- Their Thm 1.5 says χ₀ lies on exactly two components of dimension 4 that meet transversally along dimension 3: Y (irreducible
  characters) and Z (reducible).
- Here n = 5. Our ρ₀ differs from their ρ_λ = (λ^φ ⊗ α) ⊕ λ^{−4φ} by a central character, with λ⁵ = μ.
- μ = −1 is a double root, outside their hypotheses. There existence along s c + t c* is open.

## 4. BANKED IDENTITY:

Before any new number is read, the sealed run reproduces inside itself:
- B1509's banked indices: I(W₁) = −1 and I(W₂) = +1 at μ = −1, 0 and 0 at ±i, and the split 0, at all 18 point–prime pairs (54 rows).
  These go through this pipeline's own F((ε)) ranks-only index on the exact one-sided families (C1–C3).
- If any row fails, the run stops and reads nothing sealed.

In every index reading the identities r1 + q1 = t1 = 2t0 (annihilator) and I = (a0 − b0) + s0 − r1 (B1297) are recorded alongside.

## 5. PRIOR ART:

The design-time sweep of the repository is in §5.1, and the literature is in §5.2.

### 5.1 The repository

The sweep covered main (6085218c), this branch, the audit lane (audit/physical-bridge-2026-09-05, R41–R74 at f7cdf281) and the
paper-review lane (…/paper-review-verification-kaz3f5 at 5d58b935). Patterns searched: Heusener, Porti, Burde, de Rham, Suárez,
double root, semicontinu, Massey, cup product, infinitesimally rigid/regular, D-flat, polystable, tadpole, fixed end, relative
obstruction, two-sided, both directions.

**The audit lane.** AUD = reports/physical_bridge_2026_09_05/.
- **F15** (received there: received_r54/…/projective_deformation_tangent_2026_09_25/FINDINGS_SOURCE.txt, from the line "The result is
  exact at BOTH real embeddings").
  - h¹(π; sl(4)) = 3 at all six points (rank B 15, relator rank 12).
  - §2, the matter-retention condition: "Both sector obstruction rows are nonzero and proportional, with joint rank one on the
    three-dimensional deformation quotient. Therefore the first-order simultaneous matter-retention kernel has complex dimension two.
    … The q direction has a nonzero obstruction on BOTH sides."
  - This is τ (Proposition F), and it decides the fixed end's sl(4) part.
- **R55** (AUD NEUTRAL_CENSUS.md, the table of the first section).
  - Ordinary adjoint H¹ = 3; the meridian restriction rank on H¹ = 2; the meridian-preserving kernel is 1, spanned by q. These feed
    Lemma R.
  - In the finite-norm domain the adjoint harmonic space is one-dimensional (the q mode). The other classes "change asymptotic data
    outside this fixed finite-norm domain".
  - The light census is "one singlet + one 16 + one 16*".
- **R56** (AUD LIGHT_CUBIC.md). W₃ = λ S_c Σ Q_{c,A} Q̃_c^A with λ ≠ 0, "finite, but numerically UNEVALUATED"; it is conditional
  authored analysis.
  - S is the neutral q-mode. Q and Q̃ are the 16 and the 16*, whose SU(5)′-singlet components are B1509's c and c*.
  - On the two-sided singlet direction F_S = λ Q₁Q̃₁ ≠ 0: in the fixed finite-norm domain the pair sources S. This is the fixed-end
    reading of Proposition F.
  - R56 does not switch Q and Q̃ on together, and says gauge and D-term completion "cannot be inferred".
- **R54** (AUD NEUTRAL_MATTER.md). The nonzero neutral–matter coupling, and a positive lower bound on the order-four mixed (S, Q)
  residual potential. It is about one matter side with the neutral mode, not the pair.
- **R41** (AUD CURRENT_BALANCE.md:92–96) treats one-sided off-block extensions only.
- **R57–R74.** Nothing on two-sided deformations, D-flatness of the pair, Fayet–Iliopoulos terms, closed orbits or their index.
  R74 (sealed 2026-10-01, not yet run) studies the split 4 + line at μ = −1 and says it "is not B1509's nonsplit rank-five extension".

**Main.**
- **B1440** (the rank bound). On once-punctured-torus bundles, |I(V)| ≤ min(r, n − r) when V^F = (V*)^F = 0, with
  r = rank(ρ(λ) − 1). On a chiral two-sided branch r = 4, so |I| ≤ 1. Theorem C is sharper here (I = 0) and uses neither the fibre
  nor that hypothesis. L233(f) (index ±3 in rank five) is closed by B1440.
- **B1334** (the deformation proof). I(W ⊗ χ) = 0 on the identity component of the cusp-trivial characters when W|∂M is self-dual.
  It argues by lower semicontinuity of r1 with the cusp matrices fixed.
  - The audit lane questions that step (R27 §5, FINITE_TWIST.md:204–213): restriction to a varying kernel need not be lower
    semicontinuous.
  - Theorem C uses no semicontinuity of r1. It uses only rank J_ε ≥ rank J₀, the Euler characteristic, r1 ≤ a1 and the annihilator
    identity.
- **B1438.** The slope law, |I| ≤ 1 on rank-two sectors.
- No "a2(ε) ≤ a2(0)" argument and no index-zero theorem for two-sided deformations appears on main.

**This branch.**
- **B1509** (the one-sided extensions, T3's e ∪ c and Jordan block, lead 1 = this arc).
- **B1384** (FINDINGS §S5): a rank-two two-sided analogue on M₆. "Turning on both directions moves the longitude's eigenvalues off 1
  at first order." That is Theorem B's simple-root case, in another setting.
- **B1350/B1352/B1354:** formal branches keeping cusp-fixed vectors (E₆, the V₁₀ direction), solved order by order with obstruction
  classes, Smith exponents and Gröbner bases. B1354's tuned branches keep the vectors but are formally self-dual, so they carry no net
  count. That is the analogue of Theorem C there.
- **B1268, B1393:** semicontinuity of h¹ as a bound, not as a vanishing.

**The paper-review lane.** Its "R56" is Review 56, which is unrelated. Its 2026-10-01 sweep has nothing on two-sided deformations.

*Novelty, as far as this sweep reaches:*
- Theorem C (the index of a two-sided deformation of A ⊕ 1 vanishes);
- Theorem D (the shifted longitude condition at a double root);
- Proposition F's identification of the fixed-end class with F15's row and R56's F-term;
- every computation in §6.

### 5.2 The literature

- **Heusener–Porti 2015** (Pacific J. Math. 277, 313–354; arXiv:1407.3705). ρ_λ = (λ^{bφ} ⊗ α) ⊕ (λ^{−aφ} ⊗ β) with α and β
  irreducible and infinitesimally regular, where infinitesimally regular means h¹(Γ; sl_a(ℂ)_{Ad α}) = a − 1.
  - Thm 1.3 (necessary): Δ₁⁺(λⁿ) = Δ₁⁻(λ⁻ⁿ) = 0.
  - Thm 1.4 (sufficient): Δ₀⁺(λⁿ) ≠ 0 and λⁿ a simple root of Δ₁⁺.
  - Thm 1.5 (local structure): two components Y (irreducible) and Z (reducible) of dimension n − 1, meeting transversally along
    dimension n − 2.
  - The double-root case is not covered.
- **Heusener–Medjerab** (arXiv:1402.4294). Metabelian reducible representations at a simple root of the Alexander polynomial: smooth
  points, with irreducible deformations.
- **Heusener–Porti–Suárez** (J. reine angew. Math. 530, 2001), **Burde** (1967) and **de Rham** (1967). The SL(2) case at a simple
  root.
- **Ballas.** The projective family ρ_q of m004 (B1508/B1509).

None of these computes main's index, which is this program's invariant. None treats the double root, or the condition that the trivial
line keeps its cusp eigenvalues.

## 6. What the sealed run reads

The data are read at all 18 point–prime pairs mod p and at the six points exactly at order two.

### 6.1 Decided at design time

These are computed as checks. A failure would refute a step above, and the arc would say which.
- **D1 — cusp rigidity and the regular cusp pair.** h¹(π; sl(4)) = 3, restriction rank 3 (injective), and h⁰(T; gl(4)) = 4
  (Lemmas R and C, with F15/R55).
- **D2 — no sl(4) obstruction.** The order-two obstruction is zero, mod p and exactly over Q(√2, √3, i) (Theorem A). The coker of J
  has blocks sl(4)³ + A + A*.
- **D3 — the longitude at order two.** κ̂_ℓ = 0 exactly at the two μ = −1 points, and ≠ 0 at the four ±i points, mod p and exactly
  (Theorem B).
- **D4 — the fixed end is obstructed.** o_rel,sl = 1 at all 18 pairs (F15 + Proposition F). The line part at ℓ equals κ̂_ℓ, and the
  block trace at ℓ equals −κ̂_ℓ.
- **D5 — no chiral branch at ±i.** The chiral branch stops at order two at the ±i points (Theorem B).
- **D6 — the count is zero.** On every branch reached, I = 0 at N = 8 and N = 10, with a0 = b0 = 0 and r1 = q1 = t0 (Theorem C and
  Corollary A″). On a chiral branch, (a1, b1, r1, q1) = (1, 1, 1, 1). A reading needs precision left ≥ 1.

### 6.2 Sealed predictions (open)

Priors are mine at the seal.
- **P1 — the free-end two-sided branch exists to order N = 10,** passing verify() (relator to order 10, det = 1; parity reported).
  - At ±i, ~90%: Heusener–Porti's Theorems 1.4–1.5 apply, given D1.
  - At μ = −1, ~70%: the double root is outside every known theorem.
- **P2 — one line at the odd orders** (~70%). At order three the A- and A*-obstructions are both nonzero. The free classes reach them
  with rank 1 on the A rows, 1 on the A* rows and 1 on the odd rows together, the twist included at ±i. The obstruction lies on that
  line, so the step is solvable.
  - The adjoint columns of this map are F15's matter-retention rows, which are nonzero, proportional and of rank one. What is open is
    the twist's column, whether the obstruction is nonzero, and whether it lies on the line.
  - The rank-three control C6 behaves this way at simple roots.
- **P3 — the chiral branch at μ = −1** (~65%). Theorem D's scheme reaches order 10 at the six μ = −1 pairs, passing verify() with
  λ_m ≡ λ_ℓ ≡ 1 to order 10. Its first nontrivial step needs the adjoint choice at order two to meet both τ and the trilinear
  ⟨c*, a, c⟩(ℓ): rank 4 at step three.
- **P4 — on the free-end branch, a1 = b1 = 0** at all 18 pairs (~65%). Theorem C allows 0 or 1 when t0 = 0.
- **P5 — at μ = −1 the free-end branch moves the line's longitude first at order four** (~70%). On that branch λ_ℓ − 1 has
  ε-valuation exactly 4: order two is killed by κ̂_ℓ = 0, and order three by parity. At ±i the valuation is 2 (D3).

## 7. The instrument (after the seal)

`verification/two_sided.py --sealed --record` → `verification/two_sided_run.txt`. It runs, in order:
1. the banked identity (§4);
2. the exact order-two cross-check;
3. at each of the 18 pairs:
   - the H¹ basis and the rigidity data;
   - the free-end solver to N = 10 (det = 1);
   - the fixed-end class, κ̂_ℓ and verify();
   - the index at N = 8 and 10;
   - where κ̂_ℓ = 0, the chiral solver and its index.

The library is `verification/deform_lib.py`. The controls are `--controls`.

## 8. Reading rules, and what this arc will and will not claim

- **Reading rules.**
  - A YES on P1 or P3 needs verify() true.
  - A solver stop reports the order and the per-block ranks, and is read as "this scheme stops at order k". It is not a no-go theorem.
    A no-go claim would need the obstruction shown to be independent of every earlier choice; that is not attempted here, and it would
    be registered as a lead.
  - An index reading needs precision left ≥ 1 and agreement between N = 8 and 10.
  - Where D1 fails at a point, Theorem A is not invoked there, and the order-two obstruction is read as computed.
  - A NO half is routed to the kill graph as a NEGATIVE arc.
- **Will claim:**
  - Theorems A–D, Corollaries A′ and A″, and Proposition F, as proved;
  - the computed existence to order 10, or the stop;
  - the fixed-end class;
  - the index readings.
- **Will not claim:**
  - existence to all orders at μ = −1;
  - a finite-energy background, or the end;
  - a selection of q, μ or the end condition;
  - a 5̄′;
  - any physics beyond the closed-orbit (D-flat) reading.

I-26 stays UNEARNED. 0 of 19.
