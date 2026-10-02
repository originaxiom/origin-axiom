# B1515 PREREGISTRATION — THE HYPERBOLIC POINT: a 5̄′ needs a cusp where Λ²W has torus cohomology, and on m004's harmonic family that happens only at q = 1, the complete hyperbolic structure. Does any member there carry the 10′ and the 5̄′ of one generation on one harmonic background?

**Sealed 2026-10-02, before any cohomology of a twisted module at q = 1 on a level is computed beyond the banked values and the one
disclosed draft line (§2), and before any index of W₁, W₂, Λ²W₁ or Λ²W₂ at q = 1. Seat: cc (the SM-derivation branch). Occasion:
the owner's "go" on the recommendation after B1514: ask whether one configuration can carry both halves of a generation. Under the
owner's rule NO NEGATIVE FROM A BUG (WORKING_RULES), the arc names its independent route here and runs both before anything is
banked.**

## 0. The question

B1509 placed the chiral 10′ and the missing 5̄′ on different backgrounds:
- m004's projective family ρ_q (Ballas; the audit lane's harmonic vacuum) carries B1509's 10′. But for q ≠ 1, Λ²W is acyclic on the
  cusp, so I(Λ²W) = 0 and there is no 5̄′ (B1509 T1, Corollary C; B1511 Theorem A(vi)).
- R40's block on m010 has I(W) = I(Λ²W) = +1, an anomaly-free 10 + 5̄, but no harmonic background (the audit lane's F01).

B1509 §5 recorded where a 5̄′ could come from: I(Λ²W) ≠ 0 needs H*(T; Λ²W) ≠ 0. Generalized cusps (Ballas–Cooper–Leitner) give
Λ² torus cohomology only at type 0 (parabolic) or at type 2 and 3 with paired eigenvalues. Ballas' family has type-1 cusps for
q ≠ 1. So on m004's family the only candidate is **q = 1**, where ρ₁ is the hyperbolic holonomy in SO(3, 1) and the cusp is
parabolic. B1509, B1511 and the audit lane's R42–R56 all excluded that point.

This arc asks, on the levels M₁–M₆ (B1511's tower), at q = 1:
- **Q1.** Which characters carry B1509's rank-five extensions W₁ = [[V, c·L], [0, L]] at q = 1?
- **Q2.** What are I(W₁), I(Λ²W₁), and the mirror's I(W₂), I(Λ²W₂)?
- **Q3 (the question).** Does any member carry both a non-zero I(W₁) (a 10̄′, or 10′ in W₂) and a non-zero I(Λ²W₁) (a 5′, or 5̄′ in
  W₂)? If they are equal, the SU(5)′ cubic anomaly cancels and the member is generation-shaped.

## 1. Setting and notation

- **The frame** (B1509 FINDINGS:69–73): E₈ ⊃ (SU(5) × SU(5)′)/ℤ₅ with W in the first factor. The 10′ comes with W* and the 5̄′
  with Λ²W*, so N(10′) = −I(W) and N(5̄′) = −I(Λ²W). The SU(5)′ cubic anomaly is I(Λ²W) − I(W). It cancels iff I(W) = I(Λ²W)
  (either sign convention; B1509 FINDINGS:72).
- **The index** (main's, B1297/B1418): I(E) = n(E) − n(E*), with n(E) = dim ker(H¹(M; E) → H¹(T; E)). This is the end condition
  B1509, B1511 and main use. The B1297 identity is I = (a0 − b0) + s0 − r1, where a0 = h⁰(M; E), b0 = h⁰(M; E*), t0 = h⁰(T; E),
  s0 = h⁰(T; E*), and r1 is the rank of the restriction. Also r1 + q1 = t1 = t0 + s0.
- **The point.** ρ₁ is Ballas' ρ_q at q = 1 (t = 1/2), with rational matrices. It preserves one symmetric form, of signature (3, 1)
  (control S1). So it is the vector representation of SO(3, 1) composed with the hyperbolic holonomy: the audit lane's "geometric
  four" (PARENT_CUSP_PROOF:24–34; AFFINE_BACKGROUND:95–97). Λ²ρ₁ ⊗ ℂ ≅ so(3, 1) ⊗ ℂ ≅ Sym²h ⊕ Sym²h̄.
- **The levels** (B1511 §1): M_n = F ⋊ ⟨t⟩, t = mⁿ, with fibre F = ⟨x, y⟩ and cusp P = ⟨t, ℓ⟩. ℓ is a commutator in F.
- **A member** (B1511 §1, B1514 §1): a character ν = (ν_F, λ), with ν_F a character of T_n and |λ| = 1, plus a class
  c ≠ 0 in H¹(M_n; V_η).
  - V = ν ⊗ ρ₁, L = ν⁻⁴, V_η = ν⁵ ⊗ ρ₁ = V ⊗ L*, V ⊗ L = ν⁻³ ⊗ ρ₁, and Λ²V = ν² ⊗ Λ²ρ₁ (the Higgs bulk).
  - W₁ = [[V, c·L], [0, L]], with det W₁ = 1.
  - W₂ is the opposite order (L the sub), read through W₂* = [[V*, c′·L⁻¹], [0, L⁻¹]] with c′ ∈ H¹(V_η*), and
    I(W₂) = −I(W₂*), I(Λ²W₂) = −I(Λ²W₂*) (B1511's construction).
  - **Case (a):** L = 1 on π₁(M_n), i.e. ν_F⁴ = 1 and λ⁴ = 1. **Case (b):** otherwise.
- **The background** of a member is V ⊕ L = ν ⊗ ρ₁ ⊕ ν⁻⁴. It is unitary-twisted geometric, hence reductive, and carries the
  hyperbolic metric's harmonic map. This is the audit lane's "balanced geometric four" (F08), twisted by flat unitary lines.
- **Simple member:** λ = 1 and h¹(V) = h¹(V_η) = h¹(V ⊗ L) = 1.
- **The populations.**
  - **A (λ = 1):** every character of T_n on M₁–M₆, all members (Lemma 6). That is 508 characters (1, 5, 16, 45, 121, 320) in
    106 deck orbits: 36 case (a), 472 case (b). For 76 of the case-(b) characters, ν⁵ lies in ν's deck orbit: M₄'s eight 3-torsion
    characters, M₅'s twenty eigenline characters and M₆'s forty-eight order-8 characters (B1511 Theorem F).
  - **B (λ ∈ {−1, ±i, ω, ω²}):** the members found by the run (Lemma 6). These are the only λ ≠ 1 at which any index can be non-zero
    (Lemma 5).

## 2. Computed before the seal (disclosed)

- **`verification/controls.py` → `controls_run.txt`** (13 s). Banked data and structure only:
  - **S1.** ρ₁ has one invariant symmetric form, of signature (3, 1).
  - **S2–S6 (the cusp torus at q = 1, exact over ℚ, levels 1–6; no cohomology of a level).**
    - h*(T; ρ₁) = h*(T; ρ₁*) = (1, 2, 1) and h*(T; Λ²ρ₁) = (2, 4, 2).
    - **T1:** every 1-cocycle of P in ρ₁ takes values in e^⊥ (e spans ρ₁^P).
    - **The torus table**, for every non-zero class c_P ∈ H¹(T; ρ₁) over ℚ̄: [[ρ₁, c_P], [0, 1]] has (t0, s0) = (1, 2), and its
      exterior square has (t0, s0) = (2, 3). This is certified on the chart z₁ + k z₂ by a gcd of determinants (a non-zero constant,
      so the rank never drops) and on the point z₂.
    - **T-deck:** m centralises P and acts as the identity on H¹(P; ρ₁) and H¹(P; Λ²ρ₁).
    - **The parabolic part:** π_A, the classes of cocycles valued in (Λ²ρ₁)^P, has dimension 2. e ∧ c_P is valued in (Λ²ρ₁)^P, and it
      is non-zero mod coboundaries for every c_P ≠ 0 (by the torus table).
  - **S7.** B1509's Q: Q(1, s) = −(s − 1)²(s² − 6s + 1), Q(q, 1) = (q − 1)², Q(q, −1) = q² − 34q + 1.
  - **K1–K6 (banked identities), by both routes:**
    - K1: B1513 K3's h¹(G₁; Λ²ρ₁) = h¹(G₃; Λ²ρ₁) = 2.
    - K2: the audit lane's h¹(m004; ρ₁) = h¹(m004; ρ₁*) = 1 at q = 1.
    - K3: B1509's first row: I(W₁) = −1, I(W₂) = +1, I(Λ²W₁) = 0. Two primes per route, every root.
    - K4: B1511 C1's eight M₄ members: I(W₁) = +1, I(W₂) = −1.
    - K5: B1511 Part B's level-6 pullback: I(W₁) = −1, I(W₂) = +1.
    - K6: **the positive control, R40 on m010**, exactly over ℚ(√−3) (both u) and over GF(p) (two primes per route, both u):
      I(V) = I(Λ²V) = I(W) = I(Λ²W) = +1, n(Λ²W) = 2, n(Λ²W*) = 1. Both routes agree entry by entry: route T's a1 − r1 equals
      route L's joint-system n.
  - **C (code checks on banked modules).** Route T's Fox restriction reproduces index_lib's r1. Its wedge vectors follow tower_lib's
    Λ² convention. The two routes enumerate the same 508 characters, with the same deck action.
- **Design drafts (scratchpad).** The torus computations above, in draft form, and both census scripts dry-run on *synthetic* rows
  (no cohomology computed), to test their loops, records, Part C and the cross-route comparison. A planted disagreement was caught.
- **Disclosed draft line.** A route-L draft test printed h¹(G₃; ρ₁) = h¹(G₃; ρ₁*) = 1 for the *trivial* character at level 3 (λ = 1),
  meant as K1's companion. It is banked only at level 1. It follows from banked data, by Lemma 10's derivation (Shapiro and Wang with
  Q(1, s) and K2). No other q = 1 quantity of a level was computed.
- **Not computed:**
  - any other h¹ of a twisted module at q = 1 on a level;
  - any index of W₁, W₂, Λ²W₁, Λ²W₂ at q = 1;
  - the population-B member test;
  - the mechanism quantities ρ, bit, Λ_A.

## 3. Proved now (design time)

**Lemma 1 (the cusp at q = 1).** ρ₁|_P is unipotent with a one-dimensional fixed line ℂe.
- S2–S6 hold on every level: T1, the torus table, T-deck and the parabolic part.
- For λ = 1, every module V, V_η, V ⊗ L, L, Λ²V restricts to ρ₁|_P, ρ₁|_P, ρ₁|_P, 1 and Λ²ρ₁|_P respectively. ν_F is trivial on ℓ.
- So at a λ = 1 member with c|_P ≠ 0:
  - W₁ has (t0, s0, t1) = (1, 2, 3);
  - Λ²W₁ has (t0, s0, t1) = (2, 3, 5).

**Lemma 2 (conjugate self-duality).** For ν unitary of finite order, V* ≅ V̄ (ρ₁ is real and orthogonal; ν⁻¹ = ν̄).
- The same holds for χ ⊗ ρ₁, χ ⊗ Λ²ρ₁ and every character χ.
- Complex conjugation (over ℚ(ζ_K), the automorphism ζ ↦ ζ⁻¹) preserves n, so I = 0 for each of V, L, V_η, V ⊗ L, Λ²V.
- And q1 = r1, so r1 = t1/2 for each.
- Hence any non-zero index of W₁ or Λ²W₁ comes from the extension.

**Lemma 3 (the Higgs bulk has no interior classes).** n(ν² ⊗ Λ²ρ₁) = 0 for every ν of finite order.
- Proof: Λ²ρ₁ ⊗ ℂ = Sym²h ⊕ Sym²h̄. Apply Menal-Ferrer–Porti Theorem 0.1 (main's C55; B1409) on the finite cover ker ν², and take
  the ν²-isotypic part, since restriction commutes with the transfer.
- So h¹(Λ²V) = r1 = t1/2: it is 2 at λ ∈ {±1} and 0 otherwise (Λ²V is then acyclic on P).

**Lemma 4 (the index identity; acyclic ends carry nothing).** I = (a0 − b0) + s0 − r1 (B1297).
- If E|_P is acyclic, then a0 = b0 = 0 (invariants restrict injectively to the boundary) and s0 = r1 = 0, so I(E) = 0.
- This is B1392's "sealed cusps contribute 0" and B1511 Theorem A(vi).

**Lemma 5 (where an index can live).** On P, V has t-eigenvalue λ, L has λ⁻⁴, Λ²V has λ², and V ⊗ L has λ⁻³, all times
unipotents (ℓ acts unipotently).
- So W₁ and W₂ are boundary-acyclic unless λ ∈ μ₄, and Λ²W₁ and Λ²W₂ unless λ ∈ μ₂ ∪ μ₃.
- By Lemma 4, I(W) ≠ 0 needs λ ∈ μ₄ and I(Λ²W) ≠ 0 needs λ ∈ μ₂ ∪ μ₃. **Both need λ = ±1.**
- Every index vanishes at every other unitary λ.

**Lemma 6 (the populations).**
- At λ = 1, ν⁵ is trivial on P, so by Lemma 2 r1(V_η) = 1 and h¹(V_η) ≥ 1: every character is a member.
- At λ ∈ μ₅ \ {1} the same holds, but every index vanishes (Lemma 5); these are not read.
- At λ ∈ {−1, ±i, ω, ω²}, V_η is boundary-acyclic, so a member needs an interior class: h¹(V_η) = n(V_η) ≥ 1. Equivalently, by
  Wang (H⁰(F) = 0), λ⁵ must be an eigenvalue of the twisted fibre monodromy at q = 1.

**Lemma 7 (the mirror).**
- W₂(ν, c′)* is an extension of L* = L(ν̄) by V* ≅ V(ν̄), so W₂(ν, c′)* ≅ W₁(ν̄, c″).
- Conjugation gives W₁(ν̄, c″) = conj W₁(ν, c̄″).
- Hence I(W₂) = −I(W₁) and I(Λ²W₂) = −I(Λ²W₁) under the class correspondence, exactly when h¹(V_η) = 1.
- W₂ is read as a check; at a generation-shaped W₁, W₂ carries a 10′ + 5̄′.

**Lemma 8 (the mechanism at a simple member).** Let λ = 1 and the member be simple. Write v for a generator of H¹(V), x for a
generator of H¹(L) (case (a): x = e, the fibration class; case (b): h¹(L) = 1 by Wang and Lemma 2), b for a generator of
H¹(V ⊗ L), κ for the class of Λ²W₁ (the image of c in H¹(Hom(V ⊗ L, Λ²V))), and β = e ∧ l for the generator of H⁰(T; V ⊗ L).
- **(i) The 10̄′:** I(W₁) = 1 − b0 − ρ, where b0 = [L = 1] and ρ = [v|_P ∉ ℂ·c|_P].
  - The proof uses Lemma 1's torus table and the B1297 identity.
  - x ∪ c = 0 always: H²(M; V) → H²(T; V) is an isomorphism (both are one-dimensional; it is surjective because
    H³(M, ∂M; V) = H⁰(M; V*)^∨ = 0), and the torus cup H¹(T; L) → H²(T; V) with c|_P vanishes (t1(W₁) = 3).
  - So r1(W₁) = ρ + 1. In case (a), c ∝ v and ρ = 0.
  - **So I(W₁) = 0 in case (a), and I(W₁) ∈ {0, 1} in case (b), with I(W₁) = 1 iff the boundary lines of H¹(V) and H¹(V_η)
    coincide.**
- **(ii) The 5′:** I(Λ²W₁) = bit := [e ∧ c|_P lies in Λ_A], where Λ_A is the image of H¹(Λ²V) (a 2-plane, Lemma 3).
  - The same argument applies one step up. H²(M; Λ²V) → H²(T; Λ²V) is an isomorphism (2 = 2).
  - The torus cup H¹(T; V ⊗ L) → H²(T; Λ²V) with κ_P vanishes (t1(Λ²W₁) = 5), so κ ∪ b = 0.
  - δ_Tβ = e ∧ c|_P ≠ 0 (t0 = 2), and s0 = 3.
  - Then r1 = 3 − dim(Λ_A ∩ ℂ e ∧ c|_P), so I(Λ²W₁) = dim(Λ_A ∩ ℂ e ∧ c|_P).
- **(iii)** So at a simple member A = I(Λ²W₁) − I(W₁) ∈ {−1, 0, 1}. A generation-shaped simple member is a case-(b) member where both
  coincidences hold.
- **(iv)** If ν⁵ is in ν's deck orbit, then ρ = 0. The deck carries H¹(V) to H¹ of the deck-moved character, and by T-deck acts as the
  identity on H¹(P; ρ₁), so the boundary lines of a deck orbit coincide. **So I(W₁) = 1 at every simple member among the 76
  deck-coincident case-(b) characters.**

**Remark 9 (the expected mechanism for the 5′; cited, not used as a proof).** By T1, e ∧ c|_P is valued in (Λ²ρ₁)^P, the
nilradical n ⊕ n̄ of the parabolic. So its class lies in the parabolic part π_A, and it is non-zero (S6).
- Suppose no non-zero class of H¹(N; sl₂) on a complete finite-volume hyperbolic N restricts into the parabolic part at every cusp.
  This is the infinitesimal form of the rigidity of complete structures among those whose cusps stay parabolic (Weil–Garland type).
- Then, applied on the finite cover ker ν² to both factors Sym²h and Sym²h̄, Λ_A ∩ π_A = 0. So bit = 0, and I(Λ²W₁) = 0 at every
  simple member.
- This arc does not re-prove that rigidity statement. It sets P4's prior, and route T computes Λ_A ∩ π_A at every simple member
  (P4's second half).

**Lemma 10 (the trivial fibre character, from banked data).**
- Q(1, s) = −(s − 1)²(s² − 6s + 1) (S7) and h¹(m004; ρ₁) = 1 (K2). So the fibre monodromy at q = 1 has one Jordan block J₂ at
  eigenvalue 1, and real eigenvalues 3 ± 2√2.
- Sⁿ keeps J₂ and has eigenvalues (3 ± 2√2)ⁿ, none of them a root of unity. So on every level:
  - the trivial fibre character is simple and case (a), with I(W₁) = 0 (Lemma 8 (i));
  - it has no population-B member.

## 4. BANKED IDENTITY:

Each route's Part 0 must reproduce:
- K2 exactly: h¹(m004; ρ₁) = h¹(m004; ρ₁*) = 1 at q = 1;
- K1 at level 1: h¹(Λ²ρ₁) = 2;
- **the positive control** R40 on m010, exactly: I(V) = I(Λ²V) = I(W) = I(Λ²W) = +1.

If either route's Part 0 fails, that route stops and nothing of the census is read. K1–K6 already passed by both routes (§2).

## 5. PRIOR ART:

### 5.1 The repository (fetched 2026-10-02: main @ 5a0ca0c4, the audit lane @ b2925dac, this branch @ e2577c13)

- **This branch** (sweep of every arc and the four docs).
  - Nothing computes I(W), I(Λ²W) or a Proposition E count at q = 1.
  - q = 1 is fenced out: B1511 PREREGISTRATION:39–40; B1509 FINDINGS:77, :138; B1509 control_exceptional.py:100.
  - The only q = 1 computations are B1513's controls on Λ²ρ₁: K3 h¹ = 2, K8 dim ker(S − 1) = 2, and FINDINGS:90
    P_Λ = (s − 1)²(s² − 5s + 1)². B1513 PREREGISTRATION:278–279 notes that "at q = 1 the two classes come from the parabolic cusp
    (half of H¹(T))".
  - The cohomology of the four-dimensional SO(3, 1) representation was never computed here.
  - B1351, B1385, B1392, B1395, B1397 and B1504 work in the E₆ Pantev–Wijnholt frame. B1392:115 is sL-8's rule.
- **Main.**
  - C55 (THEOREM_LEDGER:533–541): Sym^m(h) ⊗ F has index identically zero (Menal-Ferrer–Porti Theorem 0.1, verified in B1413:12).
  - B1409: zero interior moduli for Sym² and Sym⁴ at L14n63694's geometric representation.
  - B1297 T3: a self-dual V has I = 0.
  - B1446 and B1447: index 0 at irreducible boundary-parabolic points, in main's rank-two frame.
  - B1440: rank five gives |I| ≤ 2 on once-punctured-torus bundles. R40 is read there, not re-run (B1440:86).
  - **S35 (read at this seal):** Review 58; B1450 sealed (the Gang–Yonekura index on m004's 87 filling slopes; not run); B1451 sealed
    (the κ = −2 points on 16 levels). B1451's run result, relayed by main's cc on 2026-10-02: class index zero at 188 of 188 doubly
    parabolic points (476 with the root's three-fold cover). So on main chirality lives only at the reducible, non-split end.
  - Not on main: any rank-five extension at the geometric representation; Λ² of the SO(3, 1) four.
- **The audit lane.**
  - R27 (FINITE_TWIST:19–25, :134–146): m010's witness is a single Jordan block, not reductive, with no harmonic-metric claim.
  - R40 (COEFFICIENT_PARENT:12–17, :74–86, :129–140): I(W) = I(Λ²V) = I(Λ²W) = +1, and no harmonic background (F01).
  - The harmonic family R42–R56 excludes q = 1 (CANONICAL_CUSP_PROOF:309–322; FLAT_VACUUM_PROOF:91–102). At q = 1 it is "the
    SO(3,1) vector representation" (PARENT_CUSP_PROOF:24–34), "ordinary H1: 1 and 1" (PROJECTIVE_MODE_RECEPTION:73).
  - R74 and R75 have the Λ² torus acyclic for q ≠ 1.
  - "One configuration" is a recorded duty only (FLAT_VACUUM_PROOF:180–187).
  - Not on the lane: any statement that Λ²W gains torus cohomology at q = 1, or any Ballas–Cooper–Leitner citation.
- **Absence sweeps** (`scripts/checks/absence_sweep.py --regex`, after `git fetch --all`, 9 heads, 2026-10-02).
  - **ABSENT** on every head, in deleted history and in the working tree:
    - `type.0 cusp|type 0 cusp`;
    - `Lambda.?2 ?W.{0,40}(q ?= ?1|hyperbolic)`;
    - `generation.shaped.{0,60}(q ?= ?1|hyperbolic|harmonic)`.
  - **PRESENT, and read:**
    - `hyperbolic point`: B1509 and B1511's exclusions; B1090 and THE_LADDER in other senses.
    - `geometric four` and `SO\(3, ?1\) vector`: the audit lane's AFFINE_BACKGROUND and PARENT_CUSP_PROOF, cited above.
    - `infinitesimal(ly)? rigid`: B1510 PREREGISTRATION and B429, other objects.
    - `parabolic part`: this arc's own files only.
- **Already-banked sweeps** (`scripts/checks/already_banked.py`) on "hyperbolic point Lambda^2 W index q=1", "SO(3,1) vector
  representation twisted cohomology interior", "5bar harmonic vacuum parabolic cusp generation", "rank-five extension geometric
  representation index" and "parabolic cohomology rigidity Lambda^2". The hits are keyword matches (B1078, B1089, B1187, B1198,
  B1378, B1389, B1397, B1502, B1509, B1514). None computes an index at q = 1.
- **Built on:**
  - B1509 (the frame, Proposition E, §5's "where a 5̄′ could come from");
  - B1511 (the tower, its fields and members, Theorem F);
  - B1513 (Λ²ρ₁ at q = 1);
  - B1514 (two routes, the independent audit's backends);
  - B1297, B1392, B1440 and main's C55.

### 5.2 The literature

- **Ballas–Cooper–Leitner,** *Generalized cusps in real projective manifolds: classification* (arXiv:1710.03132). In dimension 3 the
  types are 0–3; type 0 is unipotent.
- **Ballas,** *Constructing convex projective 3-manifolds with generalized cusps* (arXiv:1805.09274), Theorem 0.1. The figure-eight
  complement carries type-1 structures; the family's q ≠ 1 points are of this kind.
- **Menal-Ferrer and Porti,** *Twisted cohomology for hyperbolic three manifolds* (Osaka J. Math. 49, 2012), Theorem 0.1 (Lemma 3).
- **Heusener and Porti** (arXiv:0908.2863): infinitesimal projective rigidity under Dehn filling. This is the hypothesis behind
  Ballas' family.
- **Johnson and Millson** (bending): an embedded totally geodesic surface gives classes in H¹(Γ; ℝ^{3,1}). This is the known source of
  interior classes of the vector representation, and it is why P1 is not certain.

## 6. What the sealed run reads

### 6.1 Decided at design time (computed as checks; a failure refutes a step above)

- **D1.** Each route's Part 0 (§4).
- **D2.** Lemma 2: every piece has index 0 and r1 = t1/2.
- **D3.** Lemma 3: n(Λ²V) = n(Λ²V*) = 0; h¹(Λ²V) = 2 at λ = ±1 and 0 otherwise.
- **D4.** Lemma 5: off μ₄, I(W₁) = I(W₂) = 0; off μ₂ ∪ μ₃, I(Λ²W₁) = I(Λ²W₂) = 0, for every class read.
- **D5.** Lemma 1 in the census: at simple members, (t0, s0) = (1, 2) for W₁ and (2, 3) for Λ²W₁.
- **D6.** Lemma 7: I(W₂) = −I(W₁) and I(Λ²W₂) = −I(Λ²W₁) wherever h¹(V_η) = h¹(V_η*) = 1.
- **D7.** Lemma 8 at every simple member (route T computes ρ and bit):
  - I(W₁) = 1 − b0 − ρ and I(Λ²W₁) = bit;
  - case (a) gives I(W₁) = 0;
  - deck-coincident case (b) gives ρ = 0 and I(W₁) = 1.
  - Remark 9's proved half: e ∧ c|_P lies in π_A.
- **D8.** Readings are constant on deck orbits, and on Galois orbits at λ = 1 (complex conjugation included).
- **D9.** Lemma 10: the trivial fibre character is simple and case (a) on every level, with I(W₁) = 0 and no population-B member.
- **D10.** Within each route every field reads the same: route T's two primes and the exact field at levels 1 and 3; route L's three
  primes and its exact field.
- **D11.** **The routes agree** key by key (level, character, λ) on every dimension (a0, h¹, t0, n, b0, h¹*, s0, n*) and every index,
  zero and non-zero (route L's Part C).

### 6.2 Sealed predictions (open)

| | prediction | prior |
|---|---|---|
| P1 | every λ = 1 member on M₁–M₆ is simple: h¹(V) = h¹(V_η) = h¹(V ⊗ L) = 1 (no interior class of a cusp-trivial twisted geometric four) | 70% |
| P2 | population B is empty: no member at λ ∈ {−1, ±i, ω, ω²} on M₁–M₆ | 65% |
| P3 | at every simple case-(b) member whose ν⁵ is not in ν's deck orbit, I(W₁) = 0 (the two boundary lines differ) | 55% |
| P4 | **the 5′ sector:** I(Λ²W₁) = 0 at every member and every class read; and Λ_A ∩ π_A = 0 at every simple member (Remark 9's mechanism) | 85% |
| P5 | **the question:** no member carries both a non-zero I(W₁) and a non-zero I(Λ²W₁) | 88% |

P5 is implied by P4. At a simple member, "both" means both are +1, which is generation-shaped (Lemma 8 (iii)).

## 7. The instruments (after the seal)

- **Route T, `verification/census_t.py --record` → `census_t_run.txt`, `census_t_log.txt`.**
  - B1511's tower_lib: Reidemeister–Schreier presentations, Fox calculus, and r1 as the rank of the restriction.
  - Exactly by tower_lib.index over ℚ(ζ₁₂)[q]/(q − 1) at levels 1 and 3 (one character per deck orbit).
  - Over GF(p) by B1374's index_lib at two primes per level in (2²³, 2²⁴), every character.
  - Part 0, Parts A and B (§1), and Part C (D2–D10, P1–P5). It computes Lemma 8's ρ and bit and Remark 9's π_A checks at every
    simple member.
- **Route L, `verification/census_l.py --record` → `census_l_run.txt`, `census_l_log.txt`.** The owner's rule's independent route.
  - It shares no code with route T, B1511's tower_lib or B1374's index_lib.
  - From B1513's independent audit it takes only the arithmetic backends, m004's words and its build of Ballas' matrices.
  - Its own presentation (the mapping torus G_n = ⟨x, y, t⟩), its own character enumeration and its own elimination.
  - **A different method for the interior dimension:** the nullity of one joint system K = {(z, v)}, n = dim K − (d + t0 − a0), with
    the duality self-check n(E*) = h¹(E) − a0 + b0 − s0 asserted at every reading.
  - Three primes per level below 2²² (disjoint from route T's), and exactly over ℚ(ζ₁₂) at levels 1 and 3.
  - Its Part C compares with route T's record, key by key.
- **Classes.** Where h¹(V_η) = 1 the class is unique. Where h¹ ≥ 2 each route reads every basis class, c₁ + c₂, and the fixed
  combination Σ (k + 1) c_k. The routes are compared on the c-independent readings and the fixed combination; the class dependence is
  reported.
- **The positive control** (R40 on m010) runs in each route's Part 0.
- **Order:** route T first, then route L. Both run before anything is banked.

## 8. Reading rules, and what this arc will and will not claim

- **The routes must agree** (D11). A disagreement withholds the verdict and is logged in ERROR_LEDGER before anything else is banked
  (the owner's rule).
- **The positive control must fire** in both routes (D1). If it does not, the run is void.
- **The verdict.**
  - **If P5 fails**, the member (confirmed by both routes) is the first configuration in the harmonic frame carrying both a 10̄′ and a
    5′ (a 10′ and a 5̄′ in W₂). If they are equal, it is generation-shaped and anomaly-free. That is the arc's headline, verdict
    PROVED, read with the caveats below.
  - **If P5 holds**, the verdict is **NEGATIVE**: the hyperbolic point, the one point of m004's harmonic family where Λ²W meets the
    cusp, does not supply the 5̄′ with the 10′ through level 6. If P4 holds, the mechanism is stated: Lemma 8 (ii) and Remark 9.
    The NEGATIVE then goes to the kill graph.
  - P1–P3 are reported in both cases. A failure of P1 or P2 enlarges the population read; it does not change the rule.
- **Caveats that hold for any non-zero count here.**
  - At λ = 1 every W₁ and Λ²W₁ has torus cohomology (t1 = 3 and 5), so the cusp is not sealed. By B1392 a non-zero count there comes
    with continuous spectrum, and the twisted operator is not Fredholm.
  - The count is main's interior index. By Proposition E other end conditions give other counts: the ranges
    [a0 − b0 − t0, a0 − b0 + s0] are reported for W₁ and Λ²W₁ and **not used**. sL-8's rule (B1392:115): no end condition is chosen
    because it rescues a count.
- **What the arc will not claim:**
  - a mass or a coupling;
  - that q = 1 is selected by dynamics;
  - anything beyond level 6, or beyond unitary characters;
  - that any end condition is physical;
  - anything about I-26.
- **0 of 19 stays 0.**
