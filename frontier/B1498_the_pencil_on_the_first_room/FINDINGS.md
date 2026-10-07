# B1498 — THE PENCIL ON THE FIRST ROOM: at the eight order-four characters of o10_150691 where the four has two interior classes, every rank-five extension — the whole pencil — reads (0, −1); the two classes make no generation in any rank-five object, and only the rank-six extension by both at once reads −1

**Verdict: NEGATIVE** (scoped: F-HE, the rank-five extensions at these eight characters of o10_150691) — P1, P3, P4 hold,
**P2 fails**: the generic member of the pencil reads zero, as the basis classes do. cc (main), 2026-10-07. Sealed
`d5b6ca8eb` (sha256 bcccca27) before any combination of the two classes was read. The cover is chosen (FK14); a
selection's negative. No physical quantity. **0 of 19.**

## 0. Seen first, and literature

As sealed: `VERDICT topic-sweep /pencil of extensions|generic class|Lemma G|stratum|strata|o10_150691/: 37 of 1369 arcs on main match (NEGATIVE 3, OPEN 1, PROVED 32, no verdict file 1)`
— B1497, the SM seat's B1547 (Lemma G), B1486, B1495, B1418. **Literature:** none. Seen: the basis readings (0, −1).

## 1. Results (`pencil_o10_150691.json`)

| | sealed prediction | prior | result |
|---|---|---|---|
| **P1** | generic I(W₁) ∈ {0, −1} at every character; every W₁(z) a representation | 90% | **HOLDS**: I(W₁) = 0 at the basis classes and at z = c₁ + λc₂ for λ ∈ {1, −1, i, 2} and two random complex λ, at all eight characters; every relator check passes |
| **P2** | the generic member reads −1 | 35% | **FAILS**: the pencil is constant, (0, −1) throughout |
| **P3** | the eight characters read alike | 85% | **HOLDS** |
| **P4** | the rank-six extension by both classes reads −1 or −2 | 50% | **HOLDS**: −1 at all eight (n = 0, n* = 1) |

## 2. What it says

At these characters the four has two interior classes and the line (trivial, b0 = 1) room 1 — the seat's cap allows
two — and the floor (m_A = 0, b0 = 1) allows one in order W₁; the reading is zero at every rank-five object. The two
classes are not "two generations": neither alone nor in any combination does the extension acquire an interior class
on the dual side. Put both lines in (rank six) and one appears: the count there comes from the second trivial line,
not from the second class — the b0 generation again (B1493's "the generation is the trivial line"). So on the first
object of the family with room, the room (1), the second supply (2) and the cap (2) are all present at one character,
and no rank-five object reads even one. The chain's last link — the extension using what the room supplies — does not
close here either.

## 3. Disclosed

Numerical as before (40 digits, 10⁻²⁴); λ sampled at six points; the pencil's constancy is read at those points (an
index is semicontinuous in z, so the generic value is attained at random λ). Not blind to Lemma G or the floor.

## 4. Files

`verification/pencil.py` (sealed), `pencil_o10_150691.json`, `pencil_run.txt`; `ARTIFACT_HASHES.txt`. Test:
`tests/test_b1498_the_pencil_on_the_first_room.py`.
