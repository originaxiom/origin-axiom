# B1497 — ROOM NEEDS GENUS: the room of the line is the lifted act's invariant closed homology of the fibre — a theorem — so it needs a non-abelian cover of the register; on the root's covers there is none to degree eight, on the sign-twin's it appears once by degree eight, at degree five, on o10_150691, where the four has its first member at the trivial character and every count is still one

**Verdict: PROVED** (the theorem, general on the family; the census and the readings single) — G1, G2, G4, G5 hold, G3
fails (no room beyond degree five on m003 by degree eight), G6 holds. Scope: the trivial line's room on every
cover of a word state (the theorem); the covers of m003 and m004 to degree eight and of +LLLR to degree six (the
census); o10_150691 at its sign and order-four characters in F-HE (the readings). cc (main), 2026-10-07. Sealed
`b7706bb61` before +LLLR's census, the degree-eight censuses and any reading on o10_150691. Toward the derivation,
not one: the cover that carries the room is chosen. No physical quantity. **0 of 19.**

**Credit.** B1418 for the class census row that placed o10_150691 (not a cover of m004); the SM seat for Theorem C's
cap, read here where it first exceeds one; B350 for the Lucas ladder the level-nine cover reproduces.

## 0. Seen first, and literature

As sealed: `VERDICT topic-sweep /o10_150691|otet10|fibre genus|fiber genus|invariant cycle|Alexander polynomial|non-abelian cover|genus 2|genus two/: 4 of 1368 arcs on main match (NEGATIVE 1, PROVED 3)`
— B287, B1263, B1321, B995; B1418's row; B298, B486; B1493–B1496. **Literature:** Wang's sequence, the coinvariant
sequence of an equivariant extension, the degree of the Alexander polynomial of a fibred one-cusped manifold (standard;
used as the genus check). The censuses to degree seven (m003) and six (m004) were seen before the seal and are on it.

## 1. The theorem

**T-ROOM-NEEDS-GENUS** (proof on the preregistration, §1): for a connected cover C of a word state with fibre F_C of
genus g and lifted monodromy φ̃, 0 ≤ n(1)(C) = b₁(C) − cusps(C) ≤ rank H₁(F̄_C; ℚ)^{φ̃}; for g = 1 the room is zero. The
room is the lifted act's invariant homology of the closed fibre, less a connecting term; a genus-one fibre carries an
Anosov iterate and has none. **Corollary:** the room needs a cover of the punctured torus of genus ≥ 2, i.e. a
non-abelian covering group (the puncture loop is a commutator; it acts trivially on the sheets iff the group is
abelian), of degree at least three.

**G1 — verified on every cover built** (`census_summary.json`): of m003's 35 covers to degree 8, 19 have fibre genus 1
and every one has room 0; of m004's 39, 15 at genus 1, all room 0; of +LLLR's 22 to degree 6, 17 at genus 1, all room
0. Every cover with room has genus ≥ 2. The instrument reproduces SnapPy's `covers(d)` by degree and homology on m003
to degree 5; the level-nine cover of m003 has Alexander polynomial t² + 5778t + 1 (L₁₈, genus 1) and N₄₅'s base d9.2 has
t⁴ + 21t³ + 56t² + 21t + 1 (genus 2, base degree 3) — `alexander.py`.

## 2. The census: where the family's room is

| | sealed prediction | prior | result |
|---|---|---|---|
| **G2** | m004 has no room on any cover to degree 8 | 70% | **HOLDS**: 39 covers, 24 of fibre genus 2–4, room 0 on all |
| **G3** | m003 has a room-carrying cover at degree ≤ 8 beyond degree 5 | 50% | **FAILS**: 35 covers, 16 of genus 2–4; the only room is the two degree-5 covers, both the census manifold **o10_150691** (fibre degree 5, three punctures, genus 2, two cusps, H₁ = ℤ³, room 1) |
| **G4** | +LLLR has no room to degree 6 | 65% | **HOLDS**: 22 covers, 5 of genus 2–3, room 0 on all |

So genus ≥ 2 is necessary and far from sufficient: the root reaches genus 4 by degree 8 with no act-invariant closed
cycle; the sign-twin has exactly one, at degree five. o10_150691 (B1418: arithmetic, chiral, |Sym| = 4, no three in
F-CI; one cusp of shape ½ + (3√3/2)i — an index-three sublattice of the hexagonal ℤ[ω] — and one square cusp, shape i)
is **not a cover of m004**: the room enters the family on m003's side only, as the hexagonal end did.

## 3. o10_150691 read

| | sealed prediction | prior | result |
|---|---|---|---|
| **G5** | at its eight sign characters the line's room is 1 at the trivial one and 0 elsewhere; the four's members count at most one | 60% | **HOLDS** (`room_o10_150691.json`, `survey_o10_150691.json`): the line has room 1 at the trivial character, h¹ = m_A at the seven others. **The four has a member at the trivial character** — h¹ = 3 = two ends + one interior class, reading (−1, −1): the first interior class at a trivial character on any object read on main (every state and companion had h¹ = cusps there, all boundary); four more members at sign characters, each (−1, −1); the boundary-type classes read (0, −1) or (1, −1). Every count one, where the floor allows three (m_A = 2, b0 = 1) and the cap two |
| **G6** | at its order-four characters (b0 = 1, cap 1 + n(1) = 2) no class reads two | 60% | **HOLDS** (`order4_o10_150691.json`): 56 characters, 28 readings, no count above one. Eight characters (ν = (i, 1, 1) and its conjugates and deck images) carry **two** interior classes of the four — the second supply n(ν³ ⊗ four) = 2, the first time on any object read on main — and each reads (0, −1): zero on the 10′ side; two characters trivial on one end carry one member reading (−1, −1); two trivial on both ends carry one member (−1, −1) with two boundary-type classes (0, −1); two boundary-type classes read (−1, 0). The cap of two is there and not taken |

## 4. What it says toward the derivation

The chain is now explicit at every link: three in the smooth mechanism needs room; room is the act-invariant closed
homology of the fibre of a cover; such homology needs a non-abelian cover of the register (genus ≥ 2) that the act
preserves; on the family the root has none to degree eight, the sign-twin one at degree five, and there the count is
still one — the room has turned a boundary class interior but the count has not grown. What the genesis would have to
supply for a derivation: the register's non-abelian cover (FK14's move), on the sign-twin's side (FK4's sign), with
invariant cycles enough for the cap and ends enough for the floor at one character. None of that is supplied yet; all
of it is now named. On o10_150691 at order four the room (1) and the ends (m_A up to 2) and the four's classes (up to 2) are all present, and the count is one or zero at every class: both supplies are at hand and the extension does not use them together. The next computation toward the derivation is the glued module on this object (B1495's hatch), where two members at one character exist for the first time.

## 5. Disclosed

- The censuses to degree 7 (m003) and 6 (m004), o10_150691's identification and B1418's row were seen before the seal
  and are on it; the degree-8 censuses ran before the seal and were read after.
- Numerical ranks as in B1492–B1493; the covers' permutation representations are the coset tables' right action; the
  fibre's genus from the permutation representation agrees with the Alexander polynomial's degree where both exist.
- Not blind to the seat's cap or to B1493's instrument.

## 6. Files

`verification/fibre_census.py`, `alexander.py` (sealed), `order4_o10_150691.py`; `fibre_census_m003_D8.json`,
`fibre_census_m004_D8.json`, `fibre_census_b++LLLR_D6.json`, `census_summary.json`, `room_o10_150691.json`,
`survey_o10_150691.json`, `order4_o10_150691.json`, the run logs, the seen censuses; `ARTIFACT_HASHES.txt`.
Test: `tests/test_b1497_room_needs_genus.py`.
