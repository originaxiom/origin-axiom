# B1494 — PREREGISTRATION: NO ROOM ON ANY COMPANION — a theorem for the trivial line on every fixed-point companion of the generated family, the census of the line's sign characters on m136's and m135's companions, and N₄₅ rebuilt on main as the positive control of the room (part of R60-5)

cc (main), 2026-10-07. B1493 found the line without room on two companions by census. The reading of the pile (the
owner's exercise of the same day): the room is closed surfaces — n(1) = b₁ − (ends) — and every object the grammar
determines is fibred by a punctured torus. **Sealed before the room is read on m136's or m135's companion and before
N₄₅ is rebuilt.** No physical quantity is predicted. 0 of 19.

## 1. The theorem (proved at design time; the run tests it where it could fail)

**T-COMPANION-NO-ROOM.** Let M be a word state (a once-punctured-torus bundle with Anosov monodromy φ), T = coker(φ − I)
its torsion (|T| = |2 − tr φ|), N its fixed-point companion — the cover with deck group T in which the cusp lifts to |T|
cusps (the characters of T are exactly the characters of π₁(M) trivial on the peripheral subgroup, since μ is a
commutator and λ carries the ℤ summand). Then b₁(N) = |T| and the trivial line has no interior class on N: n(1) = 0.
*Proof.* By Shapiro, H¹(N; ℂ) = ⊕_{χ ∈ T̂} H¹(M; χ). For χ = 1 the term is b₁(M) = 1. For χ ≠ 1, χ is non-trivial on
π₁(F) (ℤ² → T is onto), so the long exact sequence of (F, ∂F) with coefficients χ reads
0 → H⁰(∂F; χ) ≅ ℂ → H¹(F, ∂F; χ) → H¹(F; χ) → H¹(∂F; χ) ≅ ℂ → H²(F, ∂F; χ) ≅ H₀(F; χ̄)* = 0, with H¹(F, ∂F; χ) and
H¹(F; χ) both one-dimensional (−χ(F) = 1), so the restriction H¹(F; χ) → H¹(∂F; χ) is an isomorphism; φ fixes the
puncture circle pointwise, so φ* = 1 on H¹(F; χ), and the Wang sequence gives h¹(M; χ) = 1 with the class restricting
isomorphically to the cusp. Hence b₁(N) = 1 + (|T| − 1) = |T|. Finally n(1) = b₁(N) − (cusps) for any cusped hyperbolic
N (the image of H¹(N) → H¹(∂N) has dimension cusps, by Poincaré–Lefschetz), so n(1) = 0. ∎
What the theorem does not say: the room at a non-trivial sign character χ′ of N. There the same sequence on the fibre
F̃ (a torus with |T| punctures, all fixed by the lifted monodromy) leaves a kernel of dimension |T| − p (p the punctures
on which χ′ is trivial) on which the monodromy's action is not forced. That is the census below.

## 2. Seen first

`VERDICT topic-sweep /companion|fixed-point|b_1 = |closed surface|room|N₄₅|d9.2|degree 45|degree-45/: 42 of 1366 arcs on main match (NEGATIVE 7, OPEN 2, PROVED 33)`
— on point: B1291 (three excluded on one cusp; the escape is ≥ 2 cusps), B1493 (the room on two companions), B350 (NEGATIVE, 2026-06: the torsion orders of m004's cyclic covers are the Lucas ladder |L₂ₙ − 2| — the same |2 − tr| at the levels; no forced choice in them), B1491/B1492; the rest other senses.
On the seats: the SM seat's companions note (Proposition 1; "no three on m003's and m136's companions" by its
Proposition 3), sm:B1540 (room ≥ 3 on seven cyclic covers of m003 — N₄₅ with room 5 at the trivial character and six of
degree 60), sm:B1547. On main: B1491 (the companions), B1492, B1493. **Literature:** Shapiro's lemma and the Wang
sequence (standard); the half-lives lemma with twisted coefficients (Menal-Ferrer–Porti 2012 for the symmetric powers;
the Lagrangian-kernel form for any self-dual system).

**Seen before the seal (structure; and one count that is the theorem's hypothesis):** the four companions rebuilt on
main — the unique cover of degree |T| with |T| cusps in each case: m136 → ℤ⁴ (|Sym| 32), m135 → ℤ⁸ (|Sym| 256), m003 →
ℤ⁵ (240, cyclic), +LLLR → L8a15 (ℤ³): b₁ = ends on all four, as the theorem says. And h¹(M; χ) = 1 with the class
boundary at every cusp-trivial χ ≠ 1 of m003, m136, m135 (read numerically with B1492's instrument), and the exact mod-p
instrument `torsion_characters.py` agrees on all eight states to length 4 (`seen_torsion_characters_len4.json`: |T| =
1, 5, 2, 6, 3, 7, 4, 8; b₁(companion) = |T| by Shapiro on every one); the companion builder's four outputs are in
`seen_companions_named.json` (+LLLR's is chiral, the other three amphichiral).
**No sign character of m136's or m135's companion has been read; N₄₅ has not been built on this bench.**

## 3. Disclosed

Numerical ranks as in B1493. N₄₅ is rebuilt from the seat's recipe (m003 → a one-cusped degree-9 cover d9.2 → its
5-fold cyclic cover along the restriction of m003's ℤ/5 character), identified by degree 45, five cusps, and
H₁ = ℤ⁹ ⊕ (ℤ/2)²; if several degree-9 covers qualify, every one is reported. The seat's room values (n(1) = 4; among the
order-2 characters that are fourth powers of cusp-trivial order-8 ones, ten at 1 and five at 3) are known to main
and are the control's targets. Not blind.

## 4. Cells, predictions, priors

| | prediction | prior |
|---|---|---|
| **R0** | the theorem's inputs on every own-level word state to length 12 (`architecture_census.states(12)`, both signs): h¹(M; χ) = 1 at every cusp-trivial χ ≠ 1 at two primes, hence b₁(companion) = |T|; and the companion built in SnapPy for every state with |T| ≤ 12 has b₁ = |T| | 90% |
| **R1** | m136's companion (ℤ⁴, 16 sign characters): room 0 at every one | 70% |
| **R2** | m135's companion (ℤ⁸, 256 sign characters): room 0 at every one | 60% |
| **R3** | N₄₅ rebuilt: degree 45 over m003, 5 cusps, H₁ = ℤ⁹ ⊕ (ℤ/2)², n(1) = 4 | 85% |
| **R4** | N₄₅'s order-2 characters (the fourth powers of the cusp-trivial order-8 ones): rooms {1 ×10, 3 ×5}, the room-3 ones trivial on every cusp — the seat's numbers reproduced by main's instrument | 75% |

**Reading rules.** R1 or R2 false — a companion with a line with room — is the headline: the first state-born object
on which Theorem C's cap exceeds one, to be read in full (the extension by the line) in a separate sealed arc before
anything is built on it. R3/R4 false: the instrument or the seat's recipe is wrong — resolve by integer homology of
the double covers (h¹(χ) = b₁(Ñ_χ) − b₁(N)) before anything else. R0 false on any state: the theorem's proof has a gap
at that state — reported as a NEGATIVE on the theorem, not patched. If all hold: T-COMPANION-NO-ROOM is registered
(creates_law: true; THEOREM_REGISTRY + CLAIM_CANDIDATES rows), and "a line with room" is recorded at FK14 as living
only off the companions, on covers chosen by characters.

## 5. Instruments

`verification/companions.py` (the companion of a word state by SnapPy's bundle name: the unique degree-|T| cover with |T|
cusps; `--census MAXLEN TMAX`), `verification/torsion_characters.py` (R0, exact mod p, the census's algebraic presentation),
`verification/room_on.py` (R1, R2, R4: B1493's `room.py` on an isosig), `verification/n45.py` (R3: the recipe); the
state list is `architecture_census.states(12)` (the own-level words, both signs); hashes in `ARTIFACT_HASHES.txt`.
