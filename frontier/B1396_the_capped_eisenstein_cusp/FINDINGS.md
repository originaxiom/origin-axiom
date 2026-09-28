# B1396 — THE CAPPED EISENSTEIN CUSP: at a cusp rotated by an order-3 isometry, the lift's weights at the rotation's three fixed points are balanced when the bulk character is non-trivial on the cusp torus, and all equal when it is trivial (the cusp's own Hopf trace). An acyclic character is non-trivial on every cusp (half lives, half dies). So a symmetric flux cap over an acyclic bulk has flux n ≡ 0 mod 3 and zero-mode content (n/3)·Reg, three times one. The same theorem explains B1394's kill test exactly: its 54 non-regular source threes are the characters trivial on the rotated cusps. The kill test drafted for this arc was a theorem, so it was not sealed; the census verifies the theorems on all 213 pairs and 444 rotated-cusp rows.

**Date:** 2026-09-28 · **Seat:** cc (the SM-derivation branch) · **Occasion:** B1395's menu, whose one finite-energy charge-odd datum is
a flux on a capped cusp torus, and B1394's P3, which fired. · **Status:**
- PROVED: Theorems A and B, Corollaries C–E. Elementary: the Hopf trace formula with local coefficients, Poincaré–Lefschetz duality,
  and the holomorphic Lefschetz formula.
- COMPUTED: the verification census, over B1394's members and characters, with the cusp's character found independently of the arcs.

**Not sealed** (§1). **Fence:** the seat's frame; order-3 characters; the continuity assumption (C); the flux an input of the completion
(B1395). · **Price:** unchanged, 0 of 19 · **Numbering:** B1396.

## 0. Seen from above

B1395 found that no finite-energy field at a free cusp knows the sign of the charge. A completion has to supply the datum; the one it can
put on a cusp at finite energy is a flux on a capped cusp torus. At an Eisenstein cusp rotated by an order-3 isometry, a cap that
respects the rotation gives its zero modes a ℤ/3 action. The question is whether that can be a three that is not three times one.
- **What the cusp sees.** The rotation fixes three points on the cusp torus, the ends of B1390's fixed arcs. The lift of the rotation
  acts on the charged line at each of them by a cube root of unity. Which three roots appear is decided by one thing: whether the bulk
  Wilson line has holonomy around the cusp torus.
  - With holonomy, the three are 1, ω, ω², and the cap's modes are three times one.
  - Without holonomy, the three are equal. The cap's modes at flux 3 are then (2, 0, 1): a non-regular three.
- **When does the Wilson line see a cusp?** Always, when the bulk is clean. A character with no massless bulk mode has holonomy around
  every cusp. More precisely, h¹ is at least the number of cusps the character does not see.
- **B1394, explained.** Its 54 non-regular source threes are exactly the characters that do not see the rotated cusps. On k = 3 both
  rotated cusps share all three arcs, so the three arcs carry one weight.
- **For the programme.** Over a clean bulk, every symmetric three in m004's class is three times one, whether it is made by sources on
  the fixed arcs (B1394) or by a flux cap at the rotated cusps (here). A non-regular three needs a Wilson line invisible at the rotated
  cusps, and that brings massless bulk modes of the same charge.

## 1. The seal that was not made

- **The draft.** After B1395 a preregistration was drafted for this arc. Its kill test (P2) asked: for some acyclic non-trivial χ, does
  some rotated cusp carry unbalanced weights? Prior SOME, about 45%. The expected mechanism was an arc from a cusp back to itself.
- **Why it was withdrawn.** While the draft's theorem was being checked, the cusp's own Hopf trace (Theorem A) and duality (Theorem B)
  decided P2: NONE, on every member, with no computation. A test whose outcome is a theorem is not an open test, so the draft was
  withdrawn uncommitted.
- **What had been computed by then.** The arithmetic of (C) and the m202 case, the lane's published R32 control. Nothing from the census.
- **The draft's mechanism.** It is Corollary D. An arc returning to its own cusp forces the character to be trivial there. It occurs
  nowhere in the class.
- **Order of work.** Theorems A and B were derived before B1394's census summary was read. So Corollary E's account of B1394's P3 was
  not fitted to that outcome. It was not sealed either, and it counts as an explanation, not a prediction.

## 2. The theorems

**Setting.**
- M is a member, and g an orientation-preserving isometry of order 3 with fixed arcs.
- A cusp c is *rotated* if g(c) = c and g has fixed points on T_c. It then acts on T_c = ℂ/ℤ[ω] as a rotation R of order 3 with
  |det(R − I)| = 3 fixed points, each the end of exactly one arc (B1390, B1371). So the rotated cusps number 2k/3.
- χ: H₁(M) → μ₃ is g-invariant, L_χ its flat line, ĝ a lift (ĝ³ = 1). λ_p is ĝ's scalar on the fibre at a fixed point p. It is the
  weight of the arc ending at p, constant along the arc by flatness.
- Since χ∘R = χ on H₁(T_c) = ℤ[ω], χ|T_c factors through ℤ[ω]/(1 − ω) ≅ ℤ/3.

**Theorem A (the cusp's Hopf trace).** At a rotated cusp c, Σ_{p ∈ Fix(g|T_c)} λ_p = L(ĝ; T_c; L_χ). Hence:
- if χ|T_c ≠ 1, the three weights are balanced (1, ω, ω²);
- if χ|T_c = 1, the three weights are equal, to the scalar ζ_c by which ĝ acts on the parallel sections over T_c.

*Proof.*
- Take a g-equivariant cell structure on T_c with the three fixed points as 0-cells. Free cells contribute 0 to every trace, and each
  fixed point contributes λ_p.
- If χ|T_c ≠ 1, a non-trivial rank-one local system on T² is acyclic, so the sum is 0. Three cube roots of unity sum to 0 only as
  1, ω, ω².
- If χ|T_c = 1, L_χ|T_c has a parallel frame, and ĝ multiplies it by a constant ζ_c. At each fixed point the scalar is ζ_c. As a check,
  L(ĝ) = ζ_c(1 − tr(R | H¹(T²)) + det R) = 3ζ_c. ∎

**Theorem B (half lives, half dies).** Over ℂ, h¹(M; χ) ≥ t(χ), the number of cusps on which χ is trivial. In particular an acyclic χ
is non-trivial on every cusp.

*Proof.*
- A non-trivial rank-one local system on a torus is acyclic, so H¹(∂M; L_χ) has dimension 2t.
- By Poincaré–Lefschetz duality, the images of H¹(M; L_χ) and H¹(M; L_χ̄) in H¹(∂M; ·) annihilate each other under the cup pairing,
  so their dimensions add to 2t. Complex conjugation makes them equal, so each is t, and h¹(M; χ) ≥ t. ∎
- The census computes over F₇ and F₁₃. The twisted complex is defined over ℤ[ω] and its ranks can only drop modulo a prime, so the
  F_p Betti numbers bound the complex ones from above. The inequality therefore holds for them too, and F_p-acyclic implies ℂ-acyclic.

**Corollary C (the capped cusp).** A completion caps a rotated cusp c and carries on T_c a ℤ/3-equivariant line bundle of degree n
whose fixed-point weights are the arc weights: the charged sector continues from the bulk to the cap. Then:
- **n ≡ 0 mod 3.** The holomorphic Lefschetz multiplicities m_j = [n + ω^{−j}χ(R) + ω^{−2j}χ(R²)]/3 are integers exactly when
  n ≡ Σ_p a_p mod 3 (λ_p = ω^{a_p}, in one sense of rotation; −Σ a_p in the other), and by A the exponent sum is 0 + 1 + 2 or 3a.
- **If χ|T_c ≠ 1**, the ℤ/3 content of H⁰ − H¹ is (n/3)·Reg. At n = 3 that is one copy of each character: three times one.
- **If χ|T_c = 1**, the content is (n/3)·Reg + (+1 on ζ_c, −1 on ζ_c ω^{∓1}), the sign fixed by the sense of the rotation at c. At
  n = 3 the multiplicities are (2, 0, 1): a non-regular three. At n = 0 it is the virtual pair ℂ_{ζ_c} − ℂ_{ζ_c ω^{∓1}} (the constants
  and H^{0,1}).
- **By B**, an acyclic bulk puts every rotated cusp in the first case.

**Corollary D (an arc that returns).** If an arc of g runs from a rotated cusp c back to c, every g-invariant order-3 character is
trivial on c, so none is acyclic. Two of c's three weights are equal, which A allows only in the trivial case.

**Corollary E (B1394's weights from the cusps).** Each arc has its two ends on rotated cusps, so

  2 · counts(arcs) = Σ_{rotated c} counts(c) = (r − t_rot)·(1, 1, 1) + 3·Σ_{c trivial} e_{ζ_c},

with r rotated cusps of which t_rot are trivial.
- B1394's weights are balanced whenever χ is non-trivial on every rotated cusp, which is weaker than acyclicity.
- An unbalanced pair has a rotated cusp where χ is trivial.
- On k = 3 without a returning arc, the three arcs all join the two rotated cusps. Both cusps then see the same three weights, so χ is
  trivial on both or on neither. The pair is balanced exactly when χ sees the rotated cusps, and otherwise all three arcs carry one
  weight. With a returning arc, D gives the second case.

## 3. The verification census (`verification/capped_cusp.py`; record `capped_run.txt`, output `capped_stdout.txt`, data `capped_census.json`)

**The banked identity** runs first and stops the run if it fails. It passed.
- The arithmetic of (C), exact in ℚ(ω), for n from −3 to 6:
  - weights (1, ω, ω²) are integral for n ≡ 0 with (n/3)(1, 1, 1);
  - (1, 1, 1) for n ≡ 0 with (n/3 + 1, n/3 − 1, n/3);
  - (1, 1, ω) for n ≡ 1.
- m202, the lane's R32 case: both rotated cusps balanced at the two non-trivial characters and all equal at the trivial one, with the
  cusp's character agreeing. No returning arc.

**Method.**
- Members and characters are B1394's: the 99 arithmetic census members and cube~3.24, every order-3 rotation subgroup, every invariant
  character to μ₃.
- Arcs, their end cusps and their weights come from B1394's instrument, used unchanged. Each arc's weight is recomputed arc by arc and
  checked against it.
- **The cusp's character is computed separately**, with no arc and no lift. The corners of the retriangulation at c triangulate T_c.
  Crossing a face changes the holonomy by ± the character's face cocycle. χ|T_c is trivial exactly when that cocycle is a coboundary
  on the corner graph, whose loops generate π₁(T_c).

**Checks.** Every one holds on every pair and every rotated cusp: 0 failures.
- V0: the fixed sets are arcs (B1390).
- V1: three arc ends per rotated cusp.
- V2: the weights at each rotated cusp are all equal or balanced (A).
- V3: balanced ⟺ χ non-trivial on the cusp, the latter computed separately (A).
- V4: acyclic ⇒ non-trivial on every cusp (B).
- V5: 2·counts(arcs) = Σ counts(c) (E).
- V6: h¹ ≥ t(χ) (B).

**The numbers.** 100 members, 9 with a rotation, and 213 pairs, 21 of them trivial. There are 444 rotated-cusp rows, 400 of them at
non-trivial characters: 292 balanced, 152 all equal, and none neither.
- **Acyclic pairs (96).** Every rotated cusp is balanced, and χ is non-trivial on every cusp of M.
- **Non-trivial pairs trivial on a rotated cusp: 54.** These are exactly B1394's P3 pairs, with the same members, Betti numbers and
  weight counts: s959 2, o10_150704 4, o10_150725 2, o10_150729 20, cube~3.24 26. The census confirms both directions: each unbalanced
  pair has a trivial rotated cusp, and each such pair is unbalanced. At their trivial rotated cusps the three weights are equal, and
  the trivial rotated cusps of one pair carry the same constant.
- **Where those characters are trivial.**
  - On s959, o10_150704 and o10_150729: exactly on the rotated cusps (2 of 2, 2 of 4 and 2 of 5 cusps).
  - On o10_150725: on all three cusps.
  - On cube~3.24: on all four.
- **Non-acyclic but balanced (42, all on cube~3.24).** h = (0, 1, 1) or (0, 2, 2). They see every cusp and are balanced: acyclicity is
  more than balance needs (E).
- **No returning arc.** No arc returns to its own cusp anywhere in the class, so D is never triggered.
- **The bound.** h¹ ≥ t holds on every pair, with equality on 144 of 213. Equality holds on:
  - the 96 acyclic pairs;
  - 20 of the 21 trivial characters;
  - the 28 registered pairs off cube~3.24 (h¹ = t = 2, 2, 3, 2 on s959, o10_150704, o10_150725, o10_150729).

  On cube~3.24 the 26 registered pairs have t = 4 and h¹ = 5, 6 or 7, and its trivial character has t = 4, b₁ = 5.

## 4. What this settles, and what it does not

**Settled.**
- **The capped-cusp route.** B1395's menu named a flux on a capped cusp. Under continuity, a symmetric cap over an acyclic bulk carries
  n ≡ 0 mod 3 and (n/3)·Reg. It cannot make a non-regular three from a clean bulk.
- **B1394's kill test, explained.** The non-regular source threes are the characters that do not see the rotated cusps. Every one of
  them carries massless bulk modes, h¹ ≥ t.
- **Across m004's class.** A symmetric three from an acyclic order-3 character is three times one, sourced or capped. The one-or-three
  question for those is the level question (sL-5).

**Not settled.**
- **The continuity assumption.** A cap whose own ℤ/3 structure is non-trivial at the fixed points shifts every weight, and n with it.
  That is an input of the completion, like the flux itself (B1395).
- **Physics.** Neither the cap nor the flux is derived. A regular three is a statement about symmetry.

0 of 19.

## 5. Fences

- **The frame's.** Order-3 characters and rotations; the cap is a closed torus carrying a line bundle; zero modes are counted by
  H⁰ − H¹ on the cap.
- **The spin structure.** Its weight at the fixed points is one shift applied to all three, which cannot change balance.
- **The Hořava–Witten reading of the cap** (B1395 §3) is not used.
- **B holds over ℂ.** Over F_p it holds wherever F_p Betti numbers bound the complex ones, which they do (§2).

## 6. Prior art

Swept before banking.
- `scripts/checks/already_banked.py "capped cusp flux fixed point weights Lefschetz rotated cusp character trivial"`: settled arcs
  B1390, B1280, B1282, B1351, B1368, B1371, B1379 and B1391. None has the cusp dichotomy or a capped cusp.
- `git grep` on main (`987c0c8f`), the audit lane (`aff8a569`) and this branch, for "Hopf trace", "half lives", "holomorphic
  Lefschetz", "capped cusp" and "flux cap":
  - The lane's R32 fixed-fibre Hopf trace is on the arcs in Q, not on the cusp torus.
  - Half-lives-half-dies is used throughout: main's B1418 (t₀ and r₁; B1374 here) and Menal-Ferrer–Porti for the geometric local
    systems.
  - No capped cusp or flux cap.
- **The literature.** Standard, no novelty claimed for the mathematics:
  - the Lefschetz fixed-point formula with local coefficients;
  - the holomorphic Lefschetz formula (Atiyah–Bott);
  - half lives, half dies;
  - line bundles on the (3, 3, 3) orbifold sphere T/ℤ₃, whose pullback degrees are fixed mod 3 by the local weights.
- **This branch.** B1390 (the fixed sets are arcs), B1371 (the pairing), B1394 (the weights, the census), B1395 (the menu).
