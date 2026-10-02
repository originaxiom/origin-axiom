# B1513 — THE TRIPLET'S HIGGS SECTOR: each member of B1511's projective triplet, and B1509's join, carries exactly one 5′_H and one 5̄′_H, both its own; but its 10′ does not couple to them: the up-type coupling is zero exactly, and so is the whole 10′ sector's

**Date:** 2026-10-01 · **Seat:** cc (the SM-derivation branch) · **Verdict:** NEGATIVE (routed in the kill graph).
**Sealed** at 5e995321 (PREREGISTRATION.md, sha256 `6f3ff4803a777a524997215101706e7f87344627824570e3f798d16d76bc1065`), before
any Λ² cohomology at q ≠ 1 and any coupling was computed. **Run as sealed** (`verification/higgs_census.py --record`, 35.6 s).
**Price:** unchanged, 0 of 19.

## 0. Seen from above

**The question.** Main's B1443 proved, in the rank-two Standard-Model frame, that each member of a deck orbit couples only to its own
Higgs class, with one strength for the orbit. B1511 lead 6 asked the same of the projective triplet, in B1509's harmonic frame. The
populations:
- **I.** On s961, the three order-2 fibre characters ν_k = (0, 2), (2, 2), (2, 0) with λ₃ = −1, at q⁶ − 34q³ + 1 = 0. Each member
  carries one chiral 10′.
- **II.** B1509's own join, on m004 at q² − 34q + 1 = 0 with μ = −1.

The sectors, in B1509's dictionary (E₈ ⊃ SU(5) × SU(5)′):
- the 10′ is the interior class of H¹(W*);
- the 5′_H classes are H¹(Λ²W), and the 5̄′_H classes are H¹(Λ²W*);
- the up-type coupling is the relative triple product of 10′·10′·5′_H through the form (f ∧ g)(ω).

**The instrument.** A relative triple product written here for the fibred presentation
G_n = ⟨x, y, t | t g t⁻¹ = φⁿ(g)⟩, with the boundary word yx⁻¹y⁻¹x (the longitude). Before the seal it reproduced B1510's exact
κ̂_ℓ at all six of its points, with one sign, on levels 1, 2 and 3. That is the first chain-level check of B1510's Theorem B.

**The answer (the sealed run).**
- **The Higgs sector is exactly the own classes.** Every member of both populations has h¹(Λ²W) = h¹(Λ²W*) = 1. The 5′_H maps onto
  the member's own class c, and the 5̄′_H is c*'s image. There is no other Higgs class: Λ²ρ_q has no cohomology on the level.
  - Post-run this becomes a theorem for the whole family. For every q > 0 with q ≠ 1, Λ²ρ_q is acyclic on every cyclic cover Mₙ, for
    every n (T-HIGGS-BULK-ACYCLIC, §2).
- **The coupling is zero.** Y_k = ⟨h_k ∪ a_k ∪ a_k⟩ = 0 exactly, for all three members of the triplet and for B1509's join. It is
  also zero at all 16 prime–root pairs over GF(p).
  - Post-run the zero is stronger. The symmetric form B(a, a′) = Y(h, a, a′) vanishes on the whole of H¹(W*), so no end condition on
    the 10′, interior or not, gives a coupling.
  - The μ-type pairing ⟨h ∪ e ∪ h̄⟩ with the fibration modulus is zero too.
- **No form joins two members.** Invariant forms on Λ²W_k ⊗ W_i* ⊗ W_j* exist only for i = j = k, one each.
- **The zero is real, not an instrument artefact.** At B1510's four ±i points the same instrument gives Y(h, a, ef₀) = −λ_h κ̂_ℓ ≠ 0
  and ⟨h ∪ e ∪ h̄⟩ = λ_h κ̂_ℓ ≠ 0. Both are exactly Lemma 6's prediction, and both vanish exactly at μ = −1.
  - Post-bank, an independent audit (§9) re-derived every zero by a different method, in code that shares nothing with the
    instrument, exactly and mod p. Its positive controls fire at the same ±i points and on level 3.

**Reading.**
- In the harmonic frame, each member of the projective triplet has a Higgs pair of its own and nothing else. Its chiral 10′ has no
  tree-level up-type coupling to that pair.
- Main's B1443 tensor, y·[i = j]·[η_i = η_k] with y ≠ 0, does not carry over to this frame: here y = 0.
- The zero sits where the 10′ is chiral. The Jordan block of the fibre monodromy makes the 10′ chiral (B1509 T3) and kills the
  κ̂-type term (Lemma 6). At both populations the remaining product is zero too.
- Post-run (d): the longitude component of every c*-lift's boundary class equals κ̂_ℓ exactly (Stokes). So an interior 10′ exists
  exactly where κ̂_ℓ = 0.

## 1. Setting

As in PREREGISTRATION §1.
- The frame: E₈ ⊃ (SU(5) × SU(5)′)/ℤ₅ with W in the first factor (B1509 FINDINGS:69–73). The 10′ comes with W*, the 5′ with Λ²W and the
  5̄′ with Λ²W*.
- The levels: G_n = ⟨x, y, t | t g t⁻¹ = φⁿ(g)⟩ with t = mⁿ, x = nm⁻¹, y = mnm⁻², and P = ⟨t, ℓ⟩ with ℓ = yx⁻¹y⁻¹x.
- The members: V = ν ⊗ ρ_q, rational over ℚ(q). W = [[V, c], [0, 1]], with c the unique class of H¹(V).
- The relative triple product (§1.1 of the preregistration):
  - Y(h, a, b) = Σ_C T(h(g₁), g₁a(g₂), g₁g₂b(g₃)) − Σ_z T(e_h, a(p), p·b(q));
  - e_h is h's relative lift, z = [t|ℓ] − [ℓ|t], and C = h(σ) + K(Φ*σ − σ), with ∂C = z asserted on levels 1–6.

## 2. The lemmas (proved at the seal) and the theorem (post-run)

Proofs of Lemmas 1–7 are in PREREGISTRATION §3. Every one was checked inside the run (D1–D9, §3).
- **Lemma 1 (the cusp is acyclic).** ρ_q(ℓ) has eigenvalues q, q, q, q⁻³, and every fibre character is trivial on ℓ. So V, V*,
  Λ²ρ_q, Λ²W and Λ²W* are acyclic on P. Every Higgs class is interior, and h¹(Λ²W) = h¹(Λ²W*), by the banked I(Λ²W) = 0.
- **Lemma 2.** h¹ = h² for Λ²ρ_q on a level.
- **Lemma 3 (the own 5′_H).** It exists iff [c ∪_∧ c] = 0. It is the only 5′_H when h¹(Λ²ρ_q) = 0.
- **Lemma 4.** c* is always a 5̄′_H.
- **Lemma 5.** Shapiro, and the fibre polynomial P_Λ, with P_Λ(1/q, s) = P_Λ(q, s).
- **Lemma 6 (the Jordan lemma).** For the own class h and any lift ã of c*:
  Y(h, ã + αef₀, ã + αef₀) = Y(h, ã, ã) − 2α⟨c ∪ e ∪ c*⟩.
  At Jordan points ⟨c ∪ e ∪ c*⟩ = 0, so Y does not depend on the lift.
- **Lemma 7 (the deck).** The three members agree on every reading.

**T-HIGGS-BULK-ACYCLIC (post-run (e), proved from Part A's exact P_Λ).** For every q > 0 with q ≠ 1, every unitary twist μ and every
cyclic cover:
- H*(m004; μ ⊗ Λ²ρ_q) = 0;
- H*(Mₙ; Λ²ρ_q) = 0 for every n.

*Proof.*
- **The polynomial.** Part A gives, with w = q + 1/q,
  **P_Λ(q, s) = s⁶ − 12s⁵ + 48s⁴ − (w² − w + 72)s³ + 48s² − 12s + 1.**
- **The reduction.** With u = s + 1/s, s⁻³P_Λ = f(u) − (w² − w), where f(u) = u³ − 12u² + 45u − 48 (checked symbolically).
- **f never meets w² − w.** On the unit circle, u ∈ [−2, 2]. f′ = 3(u − 3)(u − 5) > 0 there, so f ≤ f(2) = 2. For real q > 0,
  w² − w ≥ 2, with equality only at q = 1. So P_Λ(q, μ) ≠ 0 unless q = μ = 1.
- **The fibre has no invariants.** H⁰(F; Λ²ρ_q) = 0 for every q > 0. The fibre coboundary matrix B (12 × 6) times 4q has polynomial
  entries. The gcd of twelve of its 6 × 6 minors is 1024q³(q + 1)⁴, which has no positive root. So B has rank 6 at every q > 0.
- **Conclusion.** Wang gives h¹(m004; μ ⊗ Λ²ρ_q) = dim ker(S_Λ − μ) = 0. Shapiro gives the covers, and Lemma 2 gives h² = h¹ = 0. ∎
- **At q = 1,** P_Λ = (s − 1)²(s² − 5s + 1)², which is K3's two classes.

So, for any member whose character squares to 1, the own 5′_H and 5̄′_H are its only Higgs classes, on every level (Lemmas 3 and 4).

## 3. The sealed run (`verification/higgs_census.py`, record `higgs_census_run.txt`, log `higgs_census_log.txt`, 35.6 s)

**Part 0, the banked identity,** passed first. The run's triple product of B1509's cocycles with the fibration class equals B1510's
exact κ̂_ℓ at all six points: 0 at (17 ± 12√2, −1), and 1024 + 1024√3 − 4096√3 i at (7 − 4√3, i), with the three conjugates.

**Part A — the Higgs sector's fibre polynomial on the whole family** (52 interpolation points, fresh points agreeing).
- P_Λ is the polynomial above. Its value at s = 0 is 1, and the B¹ part is (s − 1)⁶.
- D7a (q ↦ 1/q) holds, and so does D7b (palindromy).
- The loci at the roots of unity of orders 1–6, none identically zero:

  | order | the locus in q |
  |---|---|
  | 1 | (q − 1)²(q² + q + 1) |
  | 2 | q⁴ − q³ + 196q² − q + 1 |
  | 3 | (q⁴ − q³ + 108q² − q + 1)² |
  | 4 | (q⁴ − q³ + 50q² − q + 1)² |
  | 5 | an octic, squared |
  | 6 | (q⁴ − q³ + 16q² − q + 1)² |

  No positive real root other than q = 1. The gcd with both populations' polynomials is 1 at every order.

**Part B — exact counts** (over ℚ[q]/(g), all conjugate points at once).
- **The bulk.** The fibre coboundary has rank 6. Λ²ρ_q has h¹ = 0 on G₁ and on G₃ (and on RS₃ for I), with (a0, a1, t0, t1, r1) =
  (0, 0, 0, 0, 0).
- **Every member of both populations:**
  - h¹(V) = h¹(V*) = 1;
  - h¹(Λ²W) = h¹(Λ²W*) = 1, each with (a0, a1, t0, t1, r1) = (0, 1, 0, 0, 0);
  - the rank of H¹(Λ²W) → H¹(V) is 1, so the own 5′_H is the only one;
  - c* is non-zero in H¹(Λ²W*), so the own 5̄′_H is the only one;
  - H¹(W*) has one interior class (the 10′).

**Part C — the couplings, exactly.** Y(h, a, a) = 0 for the one class h, at all three members of I and at II. All of D6's checks hold
at every member:
- Y(a, a, h) = Y and Y(a, h, a) = −Y;
- coboundaries in each slot change nothing;
- the lift independence, Y(h, a + ef₀, a + ef₀) = Y;
- the cross term ⟨c ∪ e ∪ c*⟩ = 0.

**Part D — over GF(p).**
- **I:** p = 1031, 1033, 1049, 10 prime–root pairs.
- **II:** p = 1031, 1033, 1039, 6 pairs.

Every pair gives the same dimensions as Part B, h¹(Λ²ρ_q) = 0, and Y = 0 for every member. There were no rank drops.

**Part E — invariant forms** (p = 1031, q ≡ 695). The dimension is 1 for (k, i, j) = (0, 0, 0), (1, 1, 1) and (2, 2, 2), and 0 for the
other 24.

## 4. The predictions, read

| | Prediction (prior) | Result |
|---|---|---|
| P1 | the Higgs bulk is generically acyclic at every root of unity of order ≤ 6 (~85%) | **YES**, stronger: no positive real exceptional q ≠ 1 at all; post-run a theorem for every unitary twist and every cover |
| P2 | acyclic at the triplet (~80%), on M₆ (~75%), at B1509's join (~80%) | **YES**, all three |
| P3 | one 5′_H and one 5̄′_H per member, both its own (~78%) | **YES**, both populations, exactly |
| P4 | each member couples to its own Higgs class: Y_k ≠ 0 for every member (~50% each) | **NO**: Y_k = 0 exactly for every member of both populations |
| P5 | no form joins different members (~90%) | **YES**: one form iff i = j = k |

D1–D9 hold. One note on D7b: it was recorded as reported, not relied on, and it holds.

## 5. Post-run checks (`verification/post_run_checks.py`, record `post_run_checks_run.txt`; not predictions)

- **(a) The positive control.** The wedge-form triple product had never been seen non-zero before the run, so a zero needed one.
  - At all six of B1510's points, Y(h, a, ef₀) = −λ_h κ̂_ℓ and ⟨h ∪ e ∪ h̄⟩ = λ_h κ̂_ℓ, exactly. Here a is a lift of B1509's c* and h
    is the own class with q(h) = λ_h c.
  - Both are non-zero exactly at the four ±i points. For example, at (7 − 4√3, −i), λ_h = (3350912 + 12796032√3 − 28353408 i +
    23047296√3 i)/673.
  - So the instrument produces non-zero values where Lemma 6 says it must, of exactly the predicted size.
- **(b) The whole 10′ sector.** At every member of both populations the symmetric form B(a, a′) = Y(h, a, a′) is zero on the basis of
  H¹(W*), which is 2 × 2. The own 5′_H decouples from every 10′ end condition, interior or not.
- **(c) The μ-type pairing.** ⟨h ∪ e ∪ h̄⟩ = 0 at both populations. The fibration modulus gives the Higgs pair no mass term.
- **(d) The boundary class of the 10′ sector.**
  - A lift a of c* restricts to the cusp as x_t (e_t f₀) + x_ℓ (e_ℓ f₀) mod coboundaries. **x_ℓ = κ̂_ℓ exactly** at all six of
    B1510's points, and x_ℓ = 0 at both populations.
  - This is Stokes' theorem applied to the line component β of the lift, which satisfies δβ = ⟨c, c*⟩. So an interior 10′ (x_t = x_ℓ =
    0 for some lift) exists exactly where κ̂_ℓ = 0, which is B1509 T3's Jordan condition, read from the boundary.
  - At the ±i points Y is affine in the lift, with slope −2λ_h κ̂_ℓ. It vanishes on exactly one lift there, and that lift is not
    interior. At the Jordan points it vanishes on every lift.
- **(e) T-HIGGS-BULK-ACYCLIC** (§2).

## 6. The physical reading

**What holds.**
- In B1509's harmonic frame each member of the projective triplet, and B1509's join, carries one chiral 10′, one 5′_H and one 5̄′_H.
- The Higgs pair is the member's own: the classes c and c* of its own background, lifted. By T-HIGGS-BULK-ACYCLIC there is no other
  Higgs class on any cyclic cover.
- No invariant up-type form joins two members. This is the harmonic frame's version of main's B1443 (E).

**What fails.**
- The member's 10′ does not couple to its own 5′_H. The tree-level up-type Yukawa of the triplet is the zero matrix, and no 10′ end
  condition changes that (post-run (b)).
- So B1443's "each member couples to its own Higgs class" holds in the SM frame (y ≠ 0) but not in the harmonic frame (y = 0).
- The zero sits exactly where the 10′ is chiral (the Jordan points). Where κ̂_ℓ ≠ 0 the coupling can be non-zero, but there the 10′ is
  not chiral (B1509: I = 0 at ±i).

**What it is not.**
- Not a statement about non-perturbative couplings. In M-theory language, a classical cup-product zero can be lifted by membrane
  instantons, and the record has no instanton computation.
- Not a statement about Higgs classes from outside the member: another background or state, or an end with an inflow.
- Not a mass or a ratio. The down-type coupling still needs a 5̄′ matter mode, which no level carries (B1511 Theorem A(vi)). With one
  5̄′ class per member, 10′·5̄′·5̄′ vanishes on it identically by symmetry.

**I-26 stays UNEARNED. 0 of 19.**

## 7. Record and disclosures

- **Sealed at 5e995321 and run as sealed.** No instrument change after the seal; the run took 35.6 s.
- **The seal's own disclosures** (PREREGISTRATION §2):
  - ρ_q(ℓ) was computed at q = 2, 3 during design;
  - a timing profile computed banked values at the triplet (h¹(V) and W's data);
  - no Λ² cohomology at q ≠ 1 and no coupling was computed before the seal.
- **Self-caught before the seal (ERROR_LEDGER).**
  - The census draft's interpolation took n(hi − lo) + 1 points. That left the three extra-point checks of the top coefficient
    empty: a vacuous check. It was corrected to n(hi − lo) + 4 before the seal.
  - The first K2 relator check used plain symbolic matrices and swelled. It was replaced by DomainMatrices over ℚ(q); no number
    changed.
- **Currency at the seal.** Main closed L235(a) in S32 (B1444). B1511 lead 6 and its harvest block carry the note, with a relay row.
- **After the run, every check named in §5 is post-run.** None changes a sealed reading.
- **Read against the audit lane's R75** (60aeb7ea, seen at banking; CROSS_BRANCH_POSITIVES.md:28–76, and its relay to this seat).
  - **What R75 confirms.** It independently re-verifies B1511's triplet, with its own word-cocycle code:
    - P = Q(q³, s) for all three members;
    - nullities (1, 2, 2, 2) at both positive roots of q⁶ − 34q³ + 1;
    - I(W) = −1 and I(W*) = +1, with the split background at 0;
    - the deck's transport.

    These are B1513's population I inputs, confirmed on a second bench. R75's exterior longitude determinant,
    (q − 1)¹⁰(q + 1)⁶(q² + q + 1)/q⁹ ≠ 0 for q > 0, q ≠ 1, is B1513's Lemma 1 for Λ²W.
  - **Its type distinctions, applied here.**
    - The split harmonic background is not the non-split W. B1513's couplings are cup products of the flat non-split W, the
      topological part of the Yukawa. No harmonic metric on W is claimed.
    - A bulk product zero does not exclude relative or end terms. B1513's zero is the relative interior pairing (with its boundary
      term), and B ≡ 0 covers every 10′ class. An end or inflow term at a completion of the cusp is outside it: it is the hatch.
  - R75's suggested next calculation is to put the verified triplet, its source/end balance and the parent's interactions on one
    admitted configuration. It is registered as lead 5 (§8).

## 8. Leads (registered, not run; each sealed before computing)

1. **Why the coupling vanishes at Jordan points.** Prove B ≡ 0 on H¹(W*) whenever ⟨c ∪ e ∪ c*⟩ = 0; equivalently,
   [a ∪_∧ a] = 0 in H²(M; Λ²W*). Post-run (d)'s boundary identity x_ℓ = κ̂_ℓ is the natural first step. Test the claim on B1511's
   case-(b) points (M₄–M₆, the opposite sign, 10̄′) before proving it.
2. **Is "chiral ⟹ zero own up-type coupling" a law of the harmonic frame?** It holds at all four algebraic points read here, and
   B1509 T3 makes chirality and the Jordan block one condition.
3. **A Higgs from outside the member.** By T-HIGGS-BULK-ACYCLIC, no cyclic cover supplies one in the bulk for order-2 members. That
   leaves another state or background, an end or apex inflow (B1509 lead 2), or a non-perturbative coupling.
4. **The 5̄′** (unchanged, decisive).
5. **One admitted configuration** (the audit lane's R75 suggestion, with B1511 lead 5 and B1506's fence). Put the triplet, its
   source/end balance and the parent's interactions on one positive-norm configuration, and recompute the spectrum and the couplings
   there rather than transporting labels.

> **Leads 1 and 2 taken (2026-10-02, B1514; PROVED).** On B1511's case-(b) points, as lead 1 asked, the chiral 10̄′ does not couple:
> it lives in the sub-bundle V, and its wedge lands in the twisted Higgs bulk ν² ⊗ Λ²ρ_q, which is acyclic at all 184 members.
> Two routes that share no code agree. With this arc, no chiral state of the harmonic tower through level 6 couples to a Higgs class
> of its background (lead 2, through level 6). Lead 1's Jordan zero, this arc's case (a), is still only computed.
> `frontier/B1514_the_decoupling_law`.

## 9. Independent audit (post-bank, 2026-10-01; the owner's rule)

The owner, after the banking, verbatim: **"aleays verify, make sure we dont hit negatives because of bugs"** (adopted as a standing
rule, WORKING_RULES "NO NEGATIVE FROM A BUG"). `verification/independent_audit.py` → `independent_audit_run.txt` (273 s). It shares
no code with `higgs_lib.py`, B1511's `tower_lib.py` or B1509's `extension_index.py`. It has its own words, its own build of Ballas'
matrices from their definition, and its own linear algebra mod p.

**A different method.**
- A cup product μ(a ∪ b) of 1-cocycles vanishes in H² iff the block map R(g) = [[C(g), N(g), β(g)], [0, B(g), b(g)], [0, 0, 1]],
  with N(g)v = μ(a(g) ⊗ g·v), is a homomorphism for some cochain β.
- On the relators that is one linear condition: the corners at β = 0 lie in the image of d¹.
- Only products of block matrices along relator words enter. There is no bar chain, fundamental class, relative lift or
  triple-product formula.
- Λ²W is acyclic on the cusp (checked at every member). So, by duality, B ≡ 0 is equivalent to [a ∧ b] = 0 in H²(M; Λ²W*) for all
  a, b in H¹(W*), and the μ-pairing's zero is equivalent to [h̄ ∪ e] = 0.

**Arithmetic.**
- **Exact,** over the number fields (sympy's AlgebraicField): ℚ(q) with q⁶ − 34q³ + 1 = 0, then ℚ(√2), then ℚ(√3, i). One
  computation covers every conjugate point.
- **Mod p,** at three primes per population and every root: 54 member–root readings for I, 6 for II, and 12 for the ±i points (both
  signs of i).

**Re-derived, all holding at every member, exactly and mod p:**
- **Z1.** [a ∧ a′] = 0 for every pair from a basis of H¹(W*), at all three members of I and at II. So B ≡ 0, and P4's NO is not a
  bug.
- **Z2.** [h̄ ∪ e] = 0 at both populations.
- **Z3.** Invariant forms on Λ²W_k ⊗ W_i* ⊗ W_j*: one iff i = j = k, and it is the wedge form (four roots mod p). This is rigorous
  one way, since invariants can only gain dimension mod p.
- **Z4.** h¹(V) = h¹(V*) = 1, h¹(W*) = 2 (ef₀ and a lift of c*), h¹(Λ²W) = h¹(Λ²W*) = 1, and Λ²V is acyclic.
- **The bulk theorem's inputs.**
  - The reduction s⁻³P_Λ = f(u) − (w² − w), with f′ = 3(u − 3)(u − 5) and f(2) = 2.
  - Mod p, h¹(G₁; s ⊗ Λ²ρ_q) is 1 at each root s of P_Λ(q, ·) and 0 at random non-roots, for four values of q.
  - Λ²ρ_q is acyclic on M₁–M₆ at five rational q > 0.
- **The family.**
  - The m004 relator holds, φ is conjugation by m, and ℓ = yx⁻¹y⁻¹x is the longitude, with eigenvalues q, q, q, q⁻³.
  - At q = 1 there is an invariant form of signature (3, 1), the hyperbolic point.

**Positive controls, all firing:**
- **C1.** At B1510's ±i points the same code finds B ≠ 0 and [h̄ ∪ e] ≠ 0, exactly. These are post-run (a)'s −λ_h κ̂_ℓ and
  λ_h κ̂_ℓ. B(ã, ef₀) ≠ 0 for every lift ã of c*, and B(ef₀, ef₀) = 0.
- **C2.** Those classes, pulled back to G₃, stay non-zero. So the level-3 code path that population I runs on sees a coupling when
  there is one.
- **C3.** Further checks of the method:
  - B is symmetric where it is non-zero;
  - a coboundary in either slot changes nothing;
  - a non-cocycle is caught, and so is a random corner.

**One wording note.**
- Over 40 random 6 × 6 minors of 4q·B the gcd is 1024q²(q + 1)³. That is a proper divisor of the twelve-minor gcd 1024q³(q + 1)⁴
  quoted in §2.
- The gcd of all the minors divides both, and has no positive root either. The theorem's step is unchanged.
- The banking log's shorthand, "the gcd of the minors", overstated it (ERROR_LEDGER, E11 instance).

**The audit's verdict.** The NEGATIVE is not an instrument artefact: two methods, two arithmetics and live positive controls agree.
Its scope is unchanged (§6): tree-level cup products in B1509's frame.

## Verification

- `verification/independent_audit.py` → `independent_audit_run.txt`: the post-bank independent audit (§9). It shares no code with
  the instrument.
- `verification/higgs_lib.py`:
  - the fibred presentation and its bar-complex chains;
  - modules, cocycles and the relative triple product;
  - the Higgs-sector maps;
  - the fibre polynomial over ℚ(q).
- `verification/controls.py` → `controls_run.txt`: K1–K10, run before the seal.
- `verification/higgs_census.py` → `higgs_census_run.txt` and `higgs_census_log.txt`: the sealed run, Parts 0 and A–E.
- `verification/post_run_checks.py` → `post_run_checks_run.txt`: post-run checks (a)–(e).
- `tests/test_b1513_the_triplets_higgs_sector.py`: the lock.
