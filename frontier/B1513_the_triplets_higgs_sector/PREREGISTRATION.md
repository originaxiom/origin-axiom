# B1513 PREREGISTRATION — THE TRIPLET'S HIGGS SECTOR: main's B1443 question asked of B1511's projective triplet in the harmonic frame. Each member carries one 10′. Which 5′_H and 5̄′_H classes does it carry, does one of them lift the member's own class, and does the member's 10′·10′ couple to it?

**Sealed 2026-10-01, before any cohomology of Λ²ρ_q at any q ≠ 1, any cohomology of Λ²W_k or Λ²W_k*, and any coupling of either
population below is computed (exactly or over GF(p)). Seat: cc (the SM-derivation branch). Occasion: the owner's "go" on the
recommendation after main's S32. That recommendation was: record main's two commits, then B1512, then "B1443's question asked of the
projective triplet: does each of its three backgrounds couple to its own Higgs class?" (B1511 lead 6).**

## 0. The question

B1511 found a projective triplet on s961 = M₃. The three order-2 fibre characters ν_k = (0, 2), (2, 2), (2, 0) mod 4, with
λ₃ = ν(z) = −1, each carry B1509's 10′ at q⁶ − 34q³ + 1 = 0 (q³ = 17 ± 12√2). Main's B1443 proved, in the rank-two Standard-Model
frame, that each member of a deck orbit couples only to its own Higgs class, with one strength for the orbit:
Y(i, j; k) = y·[i = j]·[η_i = η_k].

This arc asks the same of the projective triplet, in B1509's harmonic frame:
- **Q1 (the Higgs classes).** What are h¹(Λ²W_k) (the 5′_H) and h¹(Λ²W_k*) (the 5̄′_H) for each member? Does a 5′_H class lift the
  member's own class c_k, and is c_k* a 5̄′_H? *(Partly decided at design time: Lemmas 1–5, §3.)*
- **Q2 (the coupling).** Is the up-type coupling of the member's 10′ to its own 5′_H, Y_k = ⟨h_k ∪ a_k ∪ a_k⟩, non-zero?
  *(Open: §6.2.)*
- **Q3 (no joining form).** Does any invariant up-type form join two different members? *(Open: §6.2.)*

The same questions are asked of B1509's own join, on m004 at q² − 34q + 1 = 0 with μ = −1, where the 10′ was found (population II).

## 1. Setting and notation

- **The frame** (B1509 §1, FINDINGS:69–73): E₈ ⊃ (SU(5) × SU(5)′)/ℤ₅,
  248 = (24,1) + (1,24) + (10,5) + (10̄,5̄) + (5,10̄) + (5̄,10), with W in the first factor.
  - The 10′ comes with W*, so N(10′) = −I(W) (B1511).
  - The 5′ comes with Λ²W and the 5̄′ with Λ²W*.
  - The up-type Yukawa 10′·10′·5′_H is (5̄,10)·(5̄,10)·(10,5). Its first-factor form is
    **T(ω, f, g) = (f ∧ g)(ω)** on Λ²W ⊗ W* ⊗ W*, which is antisymmetric in (f, g).
  - The audit lane's R40 (and main's B1438/B1440, citing it) reads tens from H¹(W) and five-bars from H¹(Λ²W). That is the mirror
    convention, W ↔ W*. It conjugates every SU(5)′ representation and changes nothing here.
- **The levels** (own presentation): G_n = ⟨x, y, t | t g t⁻¹ = φⁿ(g)⟩ with t = mⁿ, x = nm⁻¹, y = mnm⁻², φ(x) = y, φ(y) = yx⁻¹y².
  - The fibre's boundary is **ℓ = yx⁻¹y⁻¹x**: the longitude nMNmmNMn written in x, y (K1, by matrices).
  - φ fixes ℓ as a reduced word, so P = ⟨t, ℓ⟩ ≅ ℤ² on every level.
- **Population I (the triplet).** G₃ over K_I = ℚ[q]/(q⁶ − 34q³ + 1), which is irreducible over ℚ. Members:
  V_k = ν_k ⊗ ρ_q with V_k(x) = ±ρ_q(x), V_k(y) = ±ρ_q(y) and V_k(t) = −ρ_q(m)³, all rational over ℚ(q).
  - h¹(V_k) = h¹(V_k*) = 1, with classes c_k and c_k*.
  - W_k = [[V_k, c_k], [0, 1]], with I(W_k) = −1, (a0, a1, t0, r1) = (0, 1, 1, 1) and dual (1, 2, 1, 1). These are B1511's banked rows,
    reproduced on G₃ in K2.
  - The deck τ (conjugation by m) permutes the three members cyclically.
- **Population II (B1509's join).** G₁ over K_II = ℚ[q]/(q² − 34q + 1), V = −ρ_q, W = [[V, c], [0, 1]] (B1509's W₁, I = −1).
- **The 10′** is the interior class a_k of H¹(W_k*). It is the kernel of the restriction to P, one-dimensional by the banked
  b1 − q1 = 1.
- **The 5′_H** are the classes of H¹(Λ²W_k). Λ²W_k ⊃ Λ²V_k, with quotient V_k (the components e_i ∧ e₅, map q).
  - A 5′_H class is **own** if q maps it onto c_k in H¹(V_k).
  - The **own 5̄′_H** is the image of c_k* under V_k* → Λ²W_k*, f ↦ f ∧ f₀, where f₀ = e₅* spans W_k*'s invariant line.
- **The coupling** is Y_k = Y(h_k, a_k, a_k; T), the relative triple product (§1.1).

### 1.1 The relative triple product (own derivation; the instrument)

- A relative 1-cocycle is (h, e): h ∈ Z¹(G; H) and e ∈ H with h(p) = p·e − e on P.
- (h, e) ∪ a ∪ b = (h ∪ a ∪ b, e ∪ a ∪ b), paired with the relative fundamental class (C, z) by ⟨(Ω, E), (C, z)⟩ = Ω(C) − E(z):
  Y(h, a, b) = Σ_C T(h(g₁), g₁a(g₂), g₁g₂b(g₃)) − Σ_z T(e, a(p), p·b(q)).
- The chains:
  - z = [t|ℓ] − [ℓ|t].
  - C = h(σ) + K(Φ*σ − σ).
  - σ = Σ_j [w₁…w_j | w_{j+1}] − Σ_{inverse letters h⁻¹} [h|h⁻¹], for any reduced word w in the commutator subgroup, has ∂σ = −[w].
  - h is the prism for conjugation by t.
  - K fills 2-cycles of the free fibre group from Fox terms.
- ∂C = z is asserted as an identity of integer chains on levels 1–6 (K1).
- Main's B1435 built the same pairing on ⟨x, y, t⟩ with boundary word [x, y]. That word is not fixed by our φ, so the general σ is
  used here.

## 2. Computed before the seal (disclosed)

`verification/controls.py --record` → `verification/controls_run.txt`. K1–K10 ran in 36 s, and all 87 checks hold.
- **K1 (the chains).**
  - ℓ = yx⁻¹y⁻¹x is the longitude, by matrices over ℚ(q).
  - Its characteristic polynomial is (s − q)³(s − q⁻³), as in B1510's Lemmas C and R.
  - φ fixes ℓ as a word.
  - ∂σ = −[ℓ], ∂K(w) = w, ∂C = z and ∂z = 0 hold on levels 1–6 (25, 44, 87, 199, 492 and 1259 cells).
  - The prism identity holds on test chains.
- **K2 (G_n is π_n).**
  - ρ_q satisfies G_n's relators over ℚ(q), for n = 1–4.
  - B1511's banked triplet rows are reproduced exactly on G₃ over K_I for all three members: h¹(V) = h¹(V*) = 1, W (0, 1, 1, 1),
    W* (1, 2, 1, 1) and I(W) = −1.
- **K3 (Shapiro at q = 1).** h¹(G₁; Λ²ρ₁) = h¹(G₃; Λ²ρ₁) = h¹(RS₃; Λ²ρ₁) = 2. This is the theorem h¹(M; Ad) = #cusps for each sl(2)
  factor of Λ²ρ₁ = so(3,1) ⊗ ℂ.
- **K4 (the banked identity, §4).** Y(c, e, c*) with B1509's cocycles and the fibration class equals B1510's exact κ̂_ℓ at all six
  points, with one global sign (+1):
  - 0 at (17 ± 12√2, −1);
  - 1024 + 1024√3 − 4096√3 i at (7 − 4√3, i), and the three conjugates.

  This is the first chain-level check of B1510's Theorem B, κ̂_ℓ = ±⟨e ∪ c, c*⟩. B1510 computed κ̂_ℓ from the deformation's longitude.
- **K5.** At (7 − 4√3, i):
  - coboundaries in each slot change nothing;
  - Y(c*, c, e) = Y(c, e, c*) (cyclic);
  - Y(c, c*, e) = −Y(c, e, c*) (transposition).
- **K6 (the levels).** B1510's classes pulled back to G₂ and G₃ give the same Y at all six points (the transfer, π*e = n·e_n).
- **K7.** The wedge form is GL(5)-invariant and antisymmetric in its W* slots.
- **K8 (the fibre monodromy).**
  - At q = 1, H⁰(F; Λ²ρ₁) = 0 and dim ker(S − 1) = 2.
  - For ρ_q at B1509's points, ker(S − μ)^j has dims (1, 2) at μ = −1 (B1509 T3's Jordan block) and (1, 1) at ±i.
- **K9 (the census's code paths on B1509's level-one W₁, banked).**
  - interior_classes(W₁*) finds 1 class at μ = −1 and 0 at ±i, as in B1509's table; the relative lifts are valid.
  - Λ²W₁ and Λ²W₁* satisfy the relators.
  - The projection Λ²W → V and the inclusion V* → Λ²W* commute with coboundaries.
  - c* includes to a cocycle.
  - A relative coboundary in the first slot gives Y = 0.
- **K10.** The interpolated fibre polynomial of ρ_q on m004 equals B1509's banked monic Q.

**Disclosures.**
- During design I computed ρ_q(ℓ) at q = 2, 3, which gave eigenvalues q (three times) and q⁻³, and the meridian's Jordan type (3, 1).
  That is the generalised cusp of Lemma 1, and it is banked in B1510.
- A timing profile computed h¹(V_(0,2)) = 1 and cohomology_data(W_(0,2)) = (0, 1, 1, 2, 1) at the triplet. These are banked values;
  t1 = 2 follows from B1511's r1 + q1 = t1.
- No cohomology of Λ²ρ_q at q ≠ 1 was computed, and no cohomology of a Λ²W or Λ²W* module. The only Λ² computations were at q = 1
  (K3, K8) and K9's relator, equivariance and coboundary checks, which compute no Λ² cohomology. No coupling of either population was
  computed.
- `verification/higgs_census.py` (the sealed run) was written and import-checked, not run.

## 3. Proved now (design time)

**Lemma 1 (the cusp is acyclic).** Take q > 0 with q ≠ 1. ρ_q(ℓ) has eigenvalues q, q, q, q⁻³ (K1; B1510 Lemmas C, R). ℓ lies in [F, F],
so every fibre character is 1 on it. So:
- V_k(ℓ) = ρ_q(ℓ) has no eigenvalue 1;
- Λ²ρ_q(ℓ) has eigenvalues q², q², q², q⁻², q⁻², q⁻², none equal to 1;
- the same holds for the duals.

A ℤ²-module on which one generator has no eigenvalue 1 is acyclic. So V_k, V_k*, Λ²ρ_q and, by their filtrations, Λ²W_k and Λ²W_k*
are acyclic on P. Consequences:
- (i) every class of their H¹ is interior, with a unique relative lift;
- (ii) for them main's index is I = a1 − b1 (r1 = q1 = 0);
- (iii) with B1511's banked I(Λ²W_k) = 0 (its I_L2) and B1509's I(Λ²W₁) = 0: **h¹(Λ²W_k) = h¹(Λ²W_k*)** in both populations.

**Lemma 2 (Euler characteristic).**
- χ(M_n) = 0 and h³ = 0 (M_n has non-empty boundary), so h⁰ − h¹ + h² = 0 for every local system.
- With H⁰(F; Λ²ρ_q) = 0, checked in the run, h¹(M_n; Λ²ρ_q) = h²(M_n; Λ²ρ_q).

**Lemma 3 (the own 5′_H).**
- Λ²V_k = ν_k² ⊗ Λ²ρ_q = Λ²ρ_q (ν_k² = 1, λ₃² = 1; in II, μ² = 1). This is the same module for every member.
- With H⁰(V_k) = 0, the sequence 0 → Λ²ρ_q → Λ²W_k → V_k → 0 gives
  0 → H¹(Λ²ρ_q) → H¹(Λ²W_k) → H¹(V_k) →δ H²(Λ²ρ_q).
- The cocycle of an extension of c_k satisfies δh′ = c_k ∪_∧ c_k, so δ(c_k) = [c_k ∪_∧ c_k]. An own 5′_H exists iff this class
  vanishes.
- **If h¹(M_n; Λ²ρ_q) = 0**, then H² = 0 (Lemma 2). So the own class exists, H¹(Λ²W_k) ≅ H¹(V_k) is one-dimensional, and every 5′_H
  is the own one. By Lemma 1(iii), h¹(Λ²W_k*) = 1 too.

**Lemma 4 (the own 5̄′_H always exists).**
- f ↦ f ∧ f₀ embeds V_k* = W_k*/⟨f₀⟩ in Λ²W_k*, with quotient Λ²ρ_q*.
- H⁰(Λ²ρ_q*) = 0, so H¹(V_k*) → H¹(Λ²W_k*) is injective. So c_k* is a 5̄′_H for every member.

**Lemma 5 (Shapiro and the fibre polynomial).**
- h¹(M_n; Λ²ρ_q) = Σ_{μⁿ=1} h¹(m004; μ ⊗ Λ²ρ_q). Conjugate μ give equal terms, because Λ²ρ_q is defined over ℚ(q).
- With H⁰(F; Λ²ρ_q) = 0, the Wang sequence gives h¹(m004; μ ⊗ Λ²ρ_q) = dim ker(S_Λ − μ) on H¹(F; Λ²ρ_q). This space has dimension 6,
  and (S_Λc)(g) = Λ²ρ_q(m)⁻¹c(φ(g)).
- So that number is positive iff **P_Λ(q, μ) = 0**, where P_Λ(q, s) = det(s − S_Λ) on H¹(F; Λ²ρ_q).
- Also P_Λ(1/q, s) = P_Λ(q, s). By B1512's Lemma D, ρ_q^{−T} ≅ ρ_{1/q}, and Λ² of SL(4) is self-dual through Λ² ⊗ Λ² → Λ⁴, so
  Λ²ρ_{1/q} ≅ Λ²ρ_q.

**Lemma 6 (the 10′, and the Jordan lemma).**
- **The 10′.** b1(M_n) = 1 and b2 = 0. So H¹(W_k*) = ⟨e f₀, ã_k⟩, with e the fibration class (e(t) = 1, e(F) = 0) and ã_k any lift of
  c_k*. The 10′ is a_k = ã_k + α e f₀ for one α.
- **The form on the line.** T(ω, f₀, f₀) = 0, and T(ω, f, f₀) = ⟨πf, qω⟩, where π: W* → V* and q: Λ²W → V are the quotient maps.
  Graded commutativity makes the two cross terms equal. So, for every 5′_H class h with q(h) = c_k:
  Y(h, ã + αef₀, ã + αef₀) = Y(h, ã, ã) − 2α⟨c_k ∪ e ∪ c_k*⟩.
- **The Jordan block kills the cross term.**
  - At the triplet the level-3 fibre monodromy has a Jordan block at λ₃: B1511's banked kernel dimensions are (1, 2, 2, 2).
  - In II it has one at μ = −1 (B1509 T3; K8).
  - By the Wang identification e ∪ c_k = 0 in H²(M_n; V_k). The relative class vanishes as well, since V_k|_P is acyclic (Lemma 1).
  - So ⟨c_k ∪ e ∪ c_k*⟩ = 0. In II this is B1510's κ̂_ℓ = 0 (K4).
- **So Y_k does not depend on which lift of c_k* carries the 10′.** It is fixed by c_k, c_k* and the own class.

**Lemma 7 (the deck).**
- τ is an orientation-preserving automorphism of π₃ fixing t. It permutes the members ν ↦ ν∘φ.
- It carries V_ν, its classes, W, Λ²W, the forms and the relative fundamental class to the next member's.
- So every per-member reading here is the same for the three members: the dimensions, the ranks and whether Y vanishes.

**What the lemmas leave open.**
- Whether h¹(M_n; Λ²ρ_q) = 0 at either population, which is Lemma 3's hypothesis.
- The coupling itself. Lemma 6 removes the term that vanishes at Jordan points (B1510 Theorem B's κ̂). What remains is a product of four
  classes, c_k, c_k, c_k* and c_k*: it passes through h′ with δh′ = c_k ∪_∧ c_k and through the line component β of ã with
  δβ = c_k ∪ c_k*. No lemma here decides it.

## 4. BANKED IDENTITY:

Before any new number is read, the sealed run reproduces B1510's exact κ̂_ℓ at its six points through this arc's relative triple
product, Y(c, e, c*) with B1509's cocycles:
- 0 at (17 ± 12√2, −1);
- 1024 + 1024√3 − 4096√3 i at (7 − 4√3, i), and its three conjugates.

The run stops if any value differs, up to one global sign. The controls have already reproduced:
- this identity on levels 1, 2 and 3 (K4, K6);
- B1511's triplet rows on G₃ (K2);
- B1509's Q (K10);
- B1509's Jordan block (K8).

## 5. PRIOR ART:

### 5.1 The repository

A sweep covered main (d3b50c0f, unchanged since S32), this branch (977dcfcc) and the audit lane (audit/physical-bridge-2026-09-05 at
472a9595, unchanged).
- **The question.** Main's B1443 (PROVED, 2026-10-01; FINDINGS:1–40) is the source of this question.
  - Its frame is the rank-two Standard-Model frame on SL(2)_β, with abelian Higgs characters.
  - It found invariant functionals by linear algebra, and triple products through B1435's sealed instrument. One non-zero coupling
    per member (48 of 48, its own character); all 16 s961 orbits with three distinct Higgs classes.
  - This arc asks the same of B1509's harmonic objects: the projective rank-four background, 10′ = H¹(W*) and 5′_H = H¹(Λ²W), with a
    new instrument on the fibred presentation with boundary word yx⁻¹y⁻¹x.
- **Joining the members.** Main's L235(a) was closed in S32 (B1444, OPEN_LEADS L235 "Run 2026-10-01"). The cubic joining an orbit's
  three Higgs classes has no group to live in: h²(M; k) = 0 on a level, the pairwise products vanish (equal slopes), and the triple
  product lands in H²(M; k) = 0.
  - B1511 lead 6 cited L235(a) as open. The currency note is made at this seal.
  - P5 asks the harmonic frame's version, for the up-type form: is there any invariant form joining two members at all?
- **The instrument.** Main's B1435 relcup.py: the relative triple product on ⟨x, y, t⟩, with the boundary word [x, y] fixed by Φ.
  - Here the derivation is redone, and the code is written fresh for a general boundary word.
  - It is validated against B1510's κ̂_ℓ (K4). B1510 has no chain-level product.
- **The sectors.**
  - B1509: the frame and its conventions, FINDINGS:69–73; T1, that Λ²W is boundary-acyclic, so I(Λ²W) = 0.
  - B1511: the triplet; its I_L2 = 0; Theorem A(vi), that no level carries a 5̄′.
  - B1512: Lemma D.
  - The audit lane's R40 (the mirror convention, on m010), and main's B1438/B1440 citing it.
- **Λ²ρ_q's cohomology and the Higgs dimensions.** These are computed on no ref. The sweep's Λ²W hits (B1509, B1511, B1512; main's
  B1438/B1440/OPEN_LEADS; the audit lane's coefficient_parent.py) are all indices, I(Λ²W), never h¹(Λ²W) or h¹(Λ²W*) separately.
- **Yukawa couplings in other frames.**
  - This branch: B1269 (a forced-zero Yukawa in the E₆ chain), B1276 (the E₆ cubic's operators), B1361/B1362 (the deck's texture,
    circulant), B1391 (the texture at the symmetric point).
  - The outside bench's THE_TEXTURE (an operator's shape).
  - None computes a triple product of twisted cohomology classes in the harmonic frame.

*Novelty, as far as this sweep reaches:*
- Lemmas 1–7 for Ballas' family;
- P_Λ;
- every number in §6.

### 5.2 The literature

- **Couplings as triple products.**
  - T. Pantev and M. Wijnholt, "Hitchin's equations and M-theory phenomenology", arXiv:0905.1968. Zero modes on the associative
    3-manifold are twisted harmonic 1-forms; the Yukawa couplings are their triple overlaps, and the topological part is the cup
    product.
  - A. P. Braun, S. Cizel, M. Hübner and S. Schäfer-Nameki, "Higgs bundles for M-theory on G₂-manifolds", arXiv:1812.06072.
- **The family and its cusp.**
  - S. Ballas, "Finite volume properly convex deformations of the figure-eight knot", arXiv:1403.3314.
  - S. Ballas, D. Cooper and A. Leitner, "Generalized cusps in real projective manifolds: classification", arXiv:1710.03132. A
    longitude with eigenvalues q, q, q, q⁻³ is a generalised cusp, and Lemma 1 is its acyclicity.
- **Rigidity at q = 1 (K3).**
  - A. Weil, "Remarks on the cohomology of groups", Ann. Math. 80 (1964).
  - H. Garland, "A rigidity theorem for discrete subgroups", Trans. AMS 129 (1967).
  - J. Porti and P. Menal-Ferrer, "Twisted cohomology for hyperbolic three manifolds", Osaka J. Math. 49 (2012), arXiv:1001.2242.
- **Reciprocity (D7b, reported, not relied on).**
  - P. Kirk and C. Livingston, Topology 38 (1999).
  - J. Hillman, D. Silver and S. Williams, AGT 10 (2010), arXiv:0905.2574.
- **The relative cup product** through the mapping cone, and its pairing with the relative fundamental class: standard (e.g. K. Brown,
  *Cohomology of Groups*, for the bar resolution).

## 6. What the sealed run reads

### 6.1 Decided at design time (computed as checks; a failure refutes a step above)

- **D1 (Lemma 1).**
  - t0 = t1 = r1 = 0 for Λ²ρ_q on each level.
  - r1 = q1 = 0, with t0 = t1 = 0, for Λ²W_k and Λ²W_k*.
  - H⁰(F; Λ²ρ_q) = 0: the fibre coboundary has rank 6.
- **D2 (Lemma 1(iii)).** h¹(Λ²W_k) = h¹(Λ²W_k*) for every member of both populations.
- **D3 (Lemma 4).** c_k* is non-zero in H¹(Λ²W_k*) for every member.
- **D4 (Lemma 3).** If h¹(M_n; Λ²ρ_q) = 0, then h¹(Λ²W_k) = 1 and the rank of H¹(Λ²W_k) → H¹(V_k) is 1.
- **D5 (Lemma 5).**
  - h¹(G₃; Λ²ρ_q) = h¹(RS₃; Λ²ρ_q).
  - The exact h¹ at each population is zero iff Part A's loci of the relevant orders miss its polynomial.
- **D6 (Lemma 6).** At each population:
  - the cross term ⟨c_k ∪ e ∪ c_k*⟩ = 0;
  - Y(h, a + ef₀, a + ef₀) = Y(h, a, a);
  - Y(a, a, h) = Y and Y(a, h, a) = −Y;
  - coboundaries change nothing.
- **D7 (Lemma 5).** P_Λ(1/q, s) = P_Λ(q, s). Reported, not relied on: s⁶P_Λ(q, 1/s) = P_Λ(q, 0)·P_Λ(q, s).
- **D8 (Lemma 7).** The three members agree on every dimension and on the vanishing of Y, exactly and at every prime–root pair. A
  GF(p) rank drop is the only allowed exception.
- **D9.** The GF(p) dimensions equal the exact ones at every prime–root pair. A rank drop is reported if one occurs.

### 6.2 Sealed predictions (open)

Priors are mine at the seal.
- **P1 — the Higgs bulk is generically acyclic** (~85%). For every root of unity μ of order ≤ 6, P_Λ(q, μ) ≢ 0. So
  h¹(m004; μ ⊗ Λ²ρ_q) = 0 for all but finitely many q.
  - *Reason:* at q = 1 the two classes come from the parabolic cusp (half of H¹(T)). Ballas' deformation makes the cusp acyclic
    (Lemma 1), and nothing else is known to force a class.
- **P2 — the populations' Higgs bulk is acyclic.**
  - I: h¹(M₃; Λ²ρ_q) = 0 at q⁶ − 34q³ + 1 = 0. That is, the sextic misses the loci of orders 1 and 3 (~80%).
  - I′: on M₆ too, orders 1, 2, 3 and 6 (~75%).
  - II: h¹(m004; Λ²ρ_q) = 0 at q² − 34q + 1 = 0 (~80%).
  - *Reason:* the populations are special for ν ⊗ ρ_q's fibre monodromy. Λ²V_k forgets ν_k.
- **P3 — one 5′_H and one 5̄′_H per member, both its own** (I ~78%; II ~78%). h¹(Λ²W_k) = h¹(Λ²W_k*) = 1, the 5′_H maps onto c_k,
  and the 5̄′_H is c_k*'s image. This follows from P2 by Lemmas 3, 4 and 1(iii).
- **P4 — each member couples to its own Higgs class: Y_k ≠ 0 exactly, for every member** (I ~50%; II ~50%).
  - *Reason for an even prior:*
    - Neither the deck nor the fibre's hyperelliptic involution (B1512 Lemma I, which fixes each member) gives an evident selection
      rule.
    - Lemma 6 removes the κ̂-type term, which vanishes exactly at Jordan points, and both populations sit at Jordan points.
    - At B1510's μ = −1 Jordan points the two-sided branch's longitude stayed at 1 through order 14 (its P5, NO). That is a hint
      that more vanishes at Jordan points than a naive count suggests.
- **P5 — no form joins different members** (~90%). Invariant forms on Λ²W_k ⊗ W_i* ⊗ W_j* exist only for i = j = k, one each.
  - *Reason:* on the associated graded pieces an invariant needs ν_iν_j = 1 (the Λ²ρ ⊗ ρ* ⊗ ρ* piece), or ν_k = ν_j or ν_k = ν_i
    (the pieces through the trivial line).
  - The non-split extensions (H⁰(W) = 0) should block the second kind.

## 7. The instrument (after the seal)

`verification/higgs_census.py --record` → `verification/higgs_census_run.txt` and `higgs_census_log.txt`. The library is
`verification/higgs_lib.py`, which imports B1511's `tower_lib`.
- **Part 0.** The banked identity (§4).
- **Part A.** P_Λ(q, s) over ℚ(q), computed as follows:
  - exact characteristic polynomials of S_Λ (12 × 12) at integer points, by flint;
  - Newton interpolation of each coefficient, within its Laurent bound;
  - three extra points per coefficient and two fresh rational points;
  - division by the coboundary part, asserted exact.

  Then its value at every root of unity of order ≤ 6 (resultants with the cyclotomic polynomials), the factors, their positive real
  roots, and the gcd with each population's polynomial. D7.
- **Part B.** Exact over K_I and K_II (sympy FiniteExtension; all conjugate points at once):
  - H⁰ of the fibre;
  - h¹(Λ²ρ_q) on the level (I: also on G₁ and RS₃), with boundary data;
  - for every member: h¹ and (a0, a1, t0, t1, r1) of Λ²W_k and Λ²W_k*; the own-5′_H rank; the own-5̄′_H test; the interior 10′
    classes.
- **Part C.** Exact couplings Y(h, a_k, a_k) for every basis class h of H¹(Λ²W_k), and D6's checks.
- **Part D.** Part B's dimensions and Part C's vanishing over GF(p), at the three smallest primes above 1009 where the population's
  polynomial has roots, at every root.
- **Part E.** Invariant forms on Λ²W_k ⊗ W_i* ⊗ W_j* for all 27 (i, j, k), over GF(p) at the first such prime.

## 8. Reading rules, and what this arc will and will not claim

- **Reading rules.**
  - P2 and P3 are read from Part B's exact counts. Part A must agree (D5). Part D must agree, up to reported rank drops.
  - **P4** reads YES for a population iff, for every member, Y(h, a_k, a_k) ≠ 0 exactly for some class h of H¹(Λ²W_k). With
    h¹(Λ²W_k) = 1 that class is the own one (P3).
    - If h¹ > 1, the own classes form an affine hyperplane not through 0. A linear functional vanishing on it vanishes identically,
      so YES iff Y is not identically zero on H¹(Λ²W_k).
    - NO iff Y = 0 for every member. Lemma 7 makes it all or none.
  - Y's value depends on how the classes are normalised. Only its vanishing is claimed, and the values are recorded.
  - **P5** is read over GF(p), which gives an upper bound on the exact dimension. If the pattern matches, it holds exactly: the
    explicit form gives at least one for i = j = k.
- **Will claim:**
  - Lemmas 1–7;
  - P_Λ exactly;
  - the Higgs-sector dimensions of both populations;
  - whether each coupling vanishes, exactly;
  - the reading in B1509's dictionary: whether each member's 10′ has a non-zero up-type coupling to its own 5′_H.
- **Will not claim:**
  - a mass or a mass ratio: the Higgs values are uncomputed (main's L235);
  - a generation, since there is no 5̄′ (B1511 Theorem A(vi));
  - the down-type coupling. It needs a 5̄′ matter mode, and none exists. With one 5̄′ class per member, the form 10′·5̄′·5̄′
    (W* ⊗ Λ²W* ⊗ Λ²W* → Λ⁵W*) vanishes on it identically, by symmetry;
  - a selection of q, of the level or of an orbit;
  - that the triplet is one configuration (B1506's fence; B1511 lead 5);
  - anything beyond B1509's SU(5)′ dictionary.
  - **I-26 stays UNEARNED; 0 of 19** unless a result here earns otherwise, which none of P1–P5 can.
