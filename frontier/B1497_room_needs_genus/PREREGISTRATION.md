# B1497 — PREREGISTRATION: ROOM NEEDS GENUS — the room of the line is the act-invariant closed homology of the fibre, so it needs a cover of the register of genus at least two (a theorem), the family's first room sits on m003's degree-five cover o10_150691 and not on any cover of m004 to degree six (seen), and on that cover the cap reaches two — read there

cc (main), 2026-10-07. The research (B1496) specified three as an index of closed-cycle cohomology on a cover cut by
characters; B1493–B1494 found the room absent on the states and their companions and present on N₄₅. This arc asks
*where in the grammar the room comes from*, proves the answer for the trivial line, maps the first room of the family,
and reads the first place where Theorem C's cap exceeds one on an object reached by a cover of a state. Toward the
derivation, not a derivation: the cover that carries the room is still chosen. **Sealed before +LLLR's census, before
the degree-8 censuses are read, and before anything is read on o10_150691 beyond its homology, shapes and B1418's row.**
No physical quantity is predicted. 0 of 19.

## 1. The theorem (proved at design time)

**T-ROOM-NEEDS-GENUS.** Let C → M be a connected cover of a word state (fibre F a once-punctured torus, monodromy φ
Anosov), with fibre F_C (a cover of F of degree d/k, k the base degree, p punctures, genus g) and lifted monodromy φ̃.
Then the room of the trivial line, n(1)(C) = b₁(C) − cusps(C), satisfies 0 ≤ n(1)(C) ≤ rank H₁(F̄_C; ℚ)^{φ̃}, where F̄_C is
the closed surface of genus g; in particular **g = 1 ⇒ n(1)(C) = 0**.
*Proof.* b₁(C) = 1 + rank H₁(F_C; ℚ)_{φ̃} (Wang). The punctures give 0 → P → H₁(F_C) → H₁(F̄_C) → 0 with P ≅ ℚ^{p−1}
(the puncture classes modulo their sum), φ̃-equivariant; the coinvariant sequence H₁(F̄_C)^{φ̃} → P_{φ̃} → H₁(F_C)_{φ̃} →
H₁(F̄_C)_{φ̃} → 0 is exact. rank P_{φ̃} = (number of φ̃-orbits on the punctures) − 1 = cusps(C) − 1, since each cusp of C
is one orbit. Hence b₁(C) − cusps(C) = rank H₁(F̄_C)_{φ̃} − rank(image of the connecting map) ∈ [0, rank H₁(F̄_C)^{φ̃}]
(invariants and coinvariants of an automorphism of a lattice have equal rank). For g = 1, F̄_C is a torus and φ̃ acts
on H₁(F̄_C) = ℤ² by an iterate of φ conjugated by the covering — Anosov, no eigenvalue one — so the bound is 0. ∎
Corollary: a cover of the punctured torus has genus 1 iff its punctures number its degree iff the puncture loop
[x, y] acts trivially on the sheets iff the covering group is abelian; so **the room needs a non-abelian cover of the
register**, of degree at least three (S₃ on three points is the smallest).
What the theorem does not say: the room at a non-trivial character (m135's companion has room 2 at sign characters
with a genus-1 fibre — B1494), and whether genus ≥ 2 suffices (it does not: see the seen census).

## 2. Seen first

`VERDICT topic-sweep /o10_150691|otet10|fibre genus|fiber genus|invariant cycle|Alexander polynomial|non-abelian cover|genus 2|genus two/: 4 of 1368 arcs on main match (NEGATIVE 1, PROVED 3)`
— B287 (the fibre slope of the figure-eight), B1263, B1321 (the sibling's localized count), B995; and B1418's class
census row for o10_150691 (arithmetic, two cusps, chiral, **not a cover of m004**, no three in F-CI, cusp counts {0, 4});
B298 and B486 (m004 forces no three); B1493–B1496. **Literature:** Wang's sequence and the coinvariant sequence are
standard; the Alexander polynomial of a fibred one-cusped manifold has degree twice the fibre's genus (used as a check).

**Seen before the seal (disclosed; `seen_fibre_census_m003_D7.json`, `seen_fibre_census_m004_D6.json`):** the census
instrument (`fibre_census.py`: every connected cover by sympy's low-index subgroups, built by `cover(perms)`, its base
degree from the fibre group's orbits, its fibre's punctures from the puncture loop's orbits, its genus, its H₁)
reproduces SnapPy's own `covers(d)` list by degree and homology on m003 to degree 5. **m003 to degree 7: 25 covers; the
only room is at degree 5 — two covers, both the census manifold o10_150691 (fibre degree 5, three punctures, genus 2,
two cusps, H₁ = ℤ³, room 1); m004 to degree 6: 20 covers, eight with fibre genus 2 or 3, none with room.** The theorem
holds on every row (genus 1 ⇒ room 0). N₄₅'s intermediate cover d9.2 has Alexander polynomial t⁴ + 21t³ + 56t² + 21t + 1
— fibre genus 2, base degree 3 — and m003's level-9 cover has t² + 5778t + 1 (the Lucas number, B350's ladder), genus 1
(`alexander.py`). Nothing has been read on o10_150691 beyond this.

## 3. Disclosed

The censuses to degree 8 were launched before the seal and are unread. Numerical ranks as in B1492–B1493; the covers'
permutation representations are the coset tables' right action (checked against SnapPy's homologies). o10_150691 is a
cover of m003 chosen by a subgroup — under FK14 a selection; this arc reads it as the first object in the family with
room, not as an object the genesis produced.

## 4. Cells, predictions, priors

| | prediction | prior |
|---|---|---|
| **G1** | the theorem's inequality on every cover of m003 and m004 to degree 8 and of +LLLR to degree 6: room 0 whenever the fibre has genus 1; room ≤ rank of the invariant closed homology wherever it can be read | 95% |
| **G2** | m004 has no room on any cover to degree 8 | 70% |
| **G3** | m003 has a room-carrying cover at degree 8 beyond degree 5 (the census reaches more than o10_150691) | 50% |
| **G4** | +LLLR (the three-ended word) has no room to degree 6 | 65% |
| **G5** | o10_150691 at its eight sign characters (B1492's instrument): the line's room is 1 at the trivial character and 0 at the others, and the four's members count at most one | 60% |
| **G6** | o10_150691 at its order-4 characters (ν⁴ = 1, so b0 = 1 and the cap is 1 + n(1) = 2): no class reads −I(W₁) = 2 — the cap of two is not attained | 60% |

**Reading rules.** G6 false — a count of two on a degree-five cover of a state, with its cusp decomposition — is the
headline, relayed to the SM seat before anything is built on it, graded as a selection (the cover is chosen) under
THE_BAR; it would be the first two in the family's reach. G2 false: m004 has room after all — reported with the cover.
G1 false anywhere: the theorem's proof has a gap, reported as such. If G1–G4 hold as stated, the arc records at FK14:
*the room of the family lives on the sign-twin's covers and needs a non-abelian cover of the register; the root's
covers have none to degree eight.*

## 5. Instruments

`verification/fibre_census.py` (the census; sympy low-index + SnapPy), `verification/alexander.py` (the Alexander
polynomial by Fox calculus, the fibre genus check), B1492's `multicusp.py` and B1493's `room.py` on o10_150691's
isosig; the seen censuses; hashes in `ARTIFACT_HASHES.txt`.
