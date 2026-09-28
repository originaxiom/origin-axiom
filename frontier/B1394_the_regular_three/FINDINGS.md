# B1394 — THE REGULAR THREE: across m004's arithmetic class, every acyclic invariant order-3 character gives balanced weights on the fixed arcs of an order-3 rotation, so sources placed there form copies of the regular representation of ℤ/3: three times one (P1, 96 of 96). Half of the non-trivial characters are acyclic (P2, 96 of 192). The sealed kill test P3 came out SOME, against the sealed prior: 54 non-acyclic non-trivial pairs, on s959, o10_150704, o10_150725, o10_150729 and cube~3.24, carry unbalanced weights (on k = 3, one weight on all three arcs). They are the only places in the class where a symmetric source three is not regular, and each of them has massless bulk modes of the same charge (h¹ = h² ≥ 2).

**Date:** 2026-09-28 · **Seat:** cc (the SM-derivation branch) · **Occasion:** sL-7 and sL-8 after B1393. The one computed completion
that keeps a count is sourced (the physical-bridge lane's R24), and on m202 its three sources give the regular representation of C₃
(the lane's R32). · **Status:**
- SEALED: `PREREGISTRATION.md` was committed at a4712e8d, with its sha256 in SEAL_LEDGER, before the census ran.
- PROVED: the theorem (the lane's R32 argument, generalised).
- COMPUTED: the census, exact over F₇ and F₁₃, with the m202 control. **Verdict as sealed:** P1 holds, P2 = 1/2, P3 SOME.

**Fence:** the seat's frame; order-3 characters; the lane's mode-module identification cited, not re-derived. · **Price:** unchanged,
0 of 19 · **Numbering:** B1394.

## 0. Seen from above

The question was whether a symmetric placement of the lane's sources anywhere in m004's class can give a three that is not three times
one. Here "symmetric" means sources on the fixed arcs of an order-3 rotation.
- **Where the bulk is clean, no.** An acyclic character (no massless bulk mode) forces the arc weights to balance: that is the
  theorem. The census confirms it on every one of the 96 acyclic pairs: each source three is ℤ/3's regular representation, and each
  lift keeps one invariant mode per three arcs.
- **Where the bulk is not clean, yes.** There are 54 such pairs, on five members. On k = 3 the three sources all carry the same weight,
  so their ℤ/3 content is three copies of one character, not the regular representation. Every one of these characters has h¹ = h² ≥ 2
  massless modes in the bulk.
- **The prior was wrong.** At the seal I expected NONE (about 60%), reasoning that a non-acyclic character's extra classes would come
  in g-orbits that keep the weights balanced. They do not.

## 1. The theorem

**Setting.**
- Q is the compact core of a member, and g an orientation-preserving isometry of order 3 whose fixed set is k arcs.
- B1390 makes them cusp-to-cusp arcs. Each rotated cusp torus has |det(R − I)| = 3 fixed points, and the arcs pair them (B1371), so
  k = 3m.
- L is a rank-one flat bundle with g*L ≅ L, and ĝ a lift. ĝ³ = 1, because g has fixed points.
- λ_i is the scalar by which ĝ acts on the fibre over arc i.

**Theorem.** Σ λ_i = L(ĝ; Q). If H*(Q; L) = 0, then:
- the weights are balanced (m of each cube root of unity);
- H¹(Q, N; L) ≅ ⊕ L_{arc_i} is m copies of the regular representation of ℤ/3;
- each lift keeps m invariant modes.

*Proof.*
- Use the Hopf trace formula on an equivariant cell structure. Cells off the fixed set are permuted freely and contribute 0; each
  contractible arc contributes λ_i.
- With H* = 0 the sum vanishes. For weights a + bω + cω² = 0 with ω² = −1 − ω, a = b = c.
- The pair sequence then gives H¹(Q, N; L) ≅ H⁰(N; L). ∎

The argument is the lane's R32 "fixed-fibre Hopf trace identity", stated for every member and every k.

**When H*(Q; L) ≠ 0.** The fibre module H⁰(N; L) = ⊕ L_{arc_i} still injects into H¹(Q, N; L), since h⁰ = 0 for a non-trivial
character. The source-mode module is then H⁰(N; L) ⊕ H¹(Q; L) as a ℤ/3-module, and Σ λ_i = tr(ĝ | H²) − tr(ĝ | H¹) need not vanish.
P3 asked whether it ever fails to vanish.

## 2. The census (`verification/regular_three.py`; record `census_run.txt`, output `census_stdout.txt`, data `census.json`)

**Method.** As sealed.
- Members: the 99 arithmetic census members and cube~3.24.
- Isometries: every orientation-preserving rotation subgroup of order 3.
- Characters: every g-invariant character to μ₃, found as the g*-fixed classes of H¹(spine; F₃).
- For each (member, ⟨g⟩, χ): the twisted Betti numbers of M on the dual spine over F₇ and F₁₃ (h² corrected for the retriangulation's
  finite vertices), and the lift φ from δφ = z − g*z. Each arc's weight is ω^{φ(t)} at an invariant tetrahedron, or taken along the
  walk around an invariant edge.

**Self-tests.** All passed: δ¹δ⁰ = 0, the Euler characteristic, the arc counts against B1390's instrument on all 100 members, weight
constancy along arcs, and agreement of the two primes. No anomalous fixed set.

**Control: m202 (the lane's R32).** `control_run.txt`.
- One rotation subgroup, k = 3.
- The invariant order-3 characters are the trivial one and two non-trivial ones.
- The trivial character: h = (1, 2, 1), not acyclic, weights (3, 0, 0).
- The two non-trivial characters: acyclic, weights (1, 1, 1). **R32 reproduced with own code.**

**The run, and one deviation of engineering.** Two attempts after the seal wrote no census number (`census_run.txt`).
- **07:15Z.** Its output went through a filter, and only the filter's exit status was recorded. The census prints only at the end, so
  it most likely died at the same member as the next attempt.
- **10:29Z.** This attempt printed a progress line per member: the member, its tetrahedra, and its number of (rotation, character)
  pairs. It completed the 99 arithmetic members and was killed at the last member, cube~3.24, for lack of memory (exit 137).
- **The cause.** B1385's `StateMember` computes a sympy H₁(M; ℚ) and a cusp analysis on construction. This instrument never reads
  them, and on the 90-tetrahedron cover they exhausted memory. Confirmed separately: `MemoryError` after 31 s under a 2.5 GB cap.
- **10:40Z, the run reported here.** It builds the cover without them (`LightStateMember`) and writes each member's rows as it goes.
  Nothing computed changed. cube~3.24 then took 2.9 s.

**The census.** 100 members; 9 have an order-3 rotation; 213 (rotation, character) pairs, 21 trivial and 192 non-trivial.

| member | rotation subgroups | k | pairs | acyclic, non-trivial | non-acyclic, balanced | non-acyclic, unbalanced | h of the non-acyclic |
|---|---|---|---|---|---|---|---|
| m202 | 1 | 3 | 3 | 2 | 0 | 0 | — |
| s959 | 1 | 3 | 3 | 0 | 0 | 2 | (0, 2, 2) |
| v3551 | 1 | 3 | 3 | 2 | 0 | 0 | — |
| o9_40999 | 1 | 3 | 3 | 2 | 0 | 0 | — |
| o10_150704 | 1 | 6 | 9 | 4 | 0 | 4 | (0, 2, 2) |
| o10_150725 | 1 | 3 | 9 | 6 | 0 | 2 | (0, 3, 3) |
| o10_150726 | 4 | 3 | 12 | 8 | 0 | 0 | — |
| o10_150729 | 10 | 3 | 90 | 60 | 0 | 20 | (0, 2, 2) |
| cube~3.24 | 1 | 3 | 81 | 12 | 42 | 26 | (0, 1, 1), (0, 2, 2) balanced; (0, 5, 5), (0, 6, 6), (0, 7, 7) unbalanced |
| **total** | 21 | | 213 | **96** | 42 | **54** | |

- **P1 (the theorem; must hold).** Holds: 0 failures. All 96 acyclic non-trivial pairs are balanced. The trivial character is never
  acyclic, as sealed.
- **P2 (read).** 96 of 192 non-trivial pairs are acyclic: exactly one half. The members differ: all on m202, v3551, o9_40999 and
  o10_150726; 6 of 8 on o10_150725; 60 of 80 on o10_150729; 4 of 8 on o10_150704; 12 of 80 on cube~3.24; none on s959.
- **P3 (the kill test).** **SOME.** 54 non-acyclic non-trivial pairs are unbalanced.
  - On k = 3 (s959, o10_150725, o10_150729, cube~3.24; 50 pairs) all three arcs carry the same weight: counts (3, 0, 0) up to the
    lift's normalisation.
  - On o10_150704 (k = 6; 4 pairs) the counts are (4, 1, 1) up to normalisation.
  - Every one has h¹ = h² ≥ 2.
  - On cube~3.24, 42 non-acyclic pairs (h = (0, 1, 1) and (0, 2, 2)) are balanced, and none of the non-acyclic pairs of the other
    members is.

## 3. What this settles, and what it does not

**Settled, as sealed.**
- **The clean case.** Every symmetric source three in m004's class over an acyclic order-3 character is three times one.
- **The kill test.** It fired: the non-regular source threes exist. They are registered here, with their members, characters and
  weights (`census.json`, rows with `acyclic` false and `balanced` false), as a lead for the lane and for sL-7.
- **What SOME means.** Each registered pair carries massless bulk modes of the same charge, so the source-mode module is the
  non-regular fibre module plus H¹(Q; L). The pair's count is not clean in the frame's sense before any source is placed.

**Not settled.**
- **Physics.** The sources and their completion remain unpaid (B1393, sL-8), and a regular three is a statement about symmetry.
- **Which three physics uses.** For the acyclic pairs, one versus three is the level question (sL-5). For the registered pairs, the
  bulk modes come first.
- **The mechanism of the imbalance.** It is not identified here. The census shows its shape: on k = 3, one weight on all three arcs.

0 of 19.

## 4. Fences

- **The frame's.** Order-3 characters only. Other finite orders and the continuous invariant families are outside the seal.
- **The mode module.** H¹(Q, N; L) is the lane's identification (R32, on R19's singular domain), cited, not re-derived.
- **Acyclicity is over F₇ and F₁₃.** The twisted complex is defined over ℤ[ω], and ranks can only drop modulo a prime. So a pair
  acyclic over F_p is acyclic over ℂ, and the 96 are acyclic over ℂ. A pair non-acyclic over F_p could in principle be acyclic over ℂ.
  The two primes agree on every pair.
- **Physics.** A regular three is a statement about symmetry. The sources and their completion remain unpaid (B1393, sL-8).

## 5. Prior art

The design-time sweep is in PREREGISTRATION.md.
- **Main.** B325 has a generation ℤ/3 acting as the regular representation, in a different setting.
- **This branch.**
  - B1356 (Y₃'s three 27s: the regular representation minus the trivial);
  - B1391 (the pullback three is regular);
  - B1384 (the induced triplet);
  - B1390 (the fixed sets are arcs);
  - B1371 (the pairing).
- **The lane.** R32 on m202, this arc's control.

Main (`987c0c8f`) and the audit lane (`aff8a569`) were fetched again at banking. Neither has moved since the last harvest.

*(Currency 2026-09-28, B1396.)* §3's open mechanism is now proved in B1396. The rotation's three fixed points on a rotated cusp carry
balanced weights when the character is non-trivial on that cusp, and equal weights when it is trivial (the cusp's own Hopf trace).
Twice the arc counts is the sum of the rotated cusps' counts. So a pair is unbalanced only if the character is trivial on a rotated
cusp, and on k = 3 exactly then. B1396's census finds the 54 pairs above to be exactly the non-trivial characters trivial on a rotated
cusp. Half lives, half dies then gives h¹ ≥ t, the number of cusps the character does not see, which is where the bulk modes come from.
This explains the P3 outcome after the fact; it was not a sealed prediction.
