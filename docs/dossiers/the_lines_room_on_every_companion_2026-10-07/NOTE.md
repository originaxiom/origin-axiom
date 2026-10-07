# The line's room on every companion: n(1) = 0 on all 27, room up to 4 on the twelve-ended ones, and never room and ends enough for three together; no single member of order dividing 8 on any companion of the family carries three

cc (the SM-derivation seat), 2026-10-07. **Structure only: no holonomy, and no count of the frame.**

- **The rule came first.** The selection rule and the budget were named in the commit that added `room_census.py`
  (`f7431ba1`), before the run.
- **The run.** 2026-10-07, 08:00–08:03Z, one pass, rc 0. Every one of the 26,158 characters was read four ways, and all
  four agree.
- **Why it was run.**
  - Main's ask of 2026-10-07: "If you have the room of the line on m135's eight-ended companion and m136's four-ended one
    ... the cusp decomposition of n(χ) per character would complete the census on all four companions".
  - The owner's question of the same day: "what if the three generations dont emerge at once or in one place, but as a
    process in more steps".

## 1. What was read

- **The states.** Every word in L and R of length 2 to 8 that uses both letters and is primitive, up to rotation and the
  swap, with either sign, whose companion has at most 12 ends: 27 states.
- **The companion.** sm:B1538's fibre-direction cover with the lattice (M − 1)ℤ² and the class w̄ whose monodromy fixes
  every puncture. It is unique for every state (asserted in the code).
- **The characters.** Every sign character of π₁N: 26,158 in all.
- **The reading** at each character χ:
  - the room n(χ) = h¹(N; χ) − r¹(χ);
  - m_A(χ), the number of ends on which χ is trivial (on the other ends H*(T²; χ) = 0);
  - χ's orbit under the deck group.
- **The four ways.** Two routes, each over GF(p) for p = 1000003 and 998244353:
  - route P: sm:B1538's reader on N's own presentation;
  - route S: Shapiro on M, with Ind χ as signed permutation matrices and M's one cusp read for N's cusps.
- **Seen first.** The companions of +LLLR, −LR, +LLRR and −LLRR, in a scratch run the same morning. The rule's commit
  says so.

## 2. The census

| state | ends | sign characters | n(1) | rooms (n: characters) | largest min(n, m_A) |
|---|---|---|---|---|---|
| +LR | 1 | 2 | 0 | 0: 2 | 0 |
| −LR | 5 | 32 | 0 | 0: 32 | 0 |
| +LLR | 2 | 4 | 0 | 0: 4 | 0 |
| −LLR | 6 | 64 | 0 | 0: 61, 1: 3 | 0 |
| +LLLR | 3 | 8 | 0 | 0: 8 | 0 |
| −LLLR | 7 | 128 | 0 | 0: 114, 1: 14 | 1 |
| +LLRR | 4 | 16 | 0 | 0: 16 | 0 |
| −LLRR | 8 | 256 | 0 | 0: 248, 2: 8 | 0 |
| +LLLLR | 4 | 16 | 0 | 0: 16 | 0 |
| −LLLLR | 8 | 256 | 0 | 0: 208, 1: 48 | 1 |
| +LLLRR | 6 | 64 | 0 | 0: 64 | 0 |
| −LLLRR | 10 | 1024 | 0 | 0: 929, 1: 70, 2: 25 | 2 |
| +LLRLR | 8 | 256 | 0 | 0: 236, 1: 20 | 1 |
| −LLRLR | 12 | 4096 | 0 | 0: 3608, 1: 411, 2: 59, 3: 18 | 2 |
| +LLLLLR | 5 | 32 | 0 | 0: 32 | 0 |
| −LLLLLR | 9 | 512 | 0 | 0: 374, 1: 135, 2: 3 | 1 |
| +LLLLRR | 8 | 256 | 0 | 0: 251, 2: 5 | 0 |
| −LLLLRR | 12 | 4096 | 0 | 0: 3481, 1: 423, 2: 183, 4: 9 | 2 |
| +LLLRLR | 11 | 2048 | 0 | 0: 1850, 1: 187, 2: 11 | 1 |
| +LLLRRR | 9 | 512 | 0 | 0: 497, 1: 9, 2: 6 | 1 |
| +LLLLLLR | 6 | 64 | 0 | 0: 61, 1: 3 | 0 |
| −LLLLLLR | 10 | 1024 | 0 | 0: 664, 1: 340, 2: 20 | 1 |
| +LLLLLRR | 10 | 1024 | 0 | 0: 939, 1: 60, 2: 25 | 2 |
| +LLLLRRR | 12 | 4096 | 0 | 0: 3659, 1: 366, 2: 59, 3: 12 | 2 |
| +LLLLLLLR | 7 | 128 | 0 | 0: 114, 1: 14 | 1 |
| −LLLLLLLR | 11 | 2048 | 0 | 0: 1168, 1: 792, 2: 88 | 2 |
| +LLLLLLRR | 12 | 4096 | 0 | 0: 3496, 1: 408, 2: 183, 4: 9 | 2 |

- **n(1) = 0 on all 27.** Main's B1494 states it as a theorem for every companion; here it is read on each one.
- **Room 0 at every sign character on 8 companions**, among them +LLLR's (L8a15), m003's (o10_150729) and m136's.
- **The largest rooms** are on twelve-ended companions:
  - 3 on −LLRLR's and +LLLLRRR's;
  - 4 on −LLLLRR's and +LLLLLLRR's.
- **Where the room is large, the ends are few.** Every character with room ≥ 3 is trivial on at most one end:
  - −LLRLR: room 3 at an orbit of 12 characters trivial on one end, and at an orbit of 6 trivial on none;
  - +LLLLRRR: room 3 at an orbit of 12 trivial on one end;
  - −LLLLRR and +LLLLLLRR: room 4 at 9 characters trivial on no end, in orbits of 6, 2 and 1.
- **The converse also holds.** Every character trivial on three or more ends has room at most 2.

## 3. Main's ask: the four companions, with the cusp decomposition

The cells give (m_A, h¹, r¹, n) and the number of characters.

| companion | (m_A, h¹, r¹, n): characters |
|---|---|
| L8a15 (+LLLR, 3 ends) | (0, 0, 0, 0): 4; (1, 1, 1, 0): 3; (3, 3, 3, 0): 1 |
| o10_150729 (−LR, 5 ends) | (0, 0, 0, 0): 6; (1, 1, 1, 0): 15; (2, 2, 2, 0): 10; (5, 5, 5, 0): 1 |
| m136's (+LLRR, 4 ends) | (0, 0, 0, 0): 9; (2, 2, 2, 0): 6; (4, 4, 4, 0): 1 |
| m135's (−LLRR, 8 ends) | (0, 0, 0, 0): 37; **(0, 2, 0, 2): 8**; (2, 2, 2, 0): 168; (4, 4, 4, 0): 42; (8, 8, 8, 0): 1 |

- **L8a15 and o10_150729** match main's B1493 exactly.
- **m136's companion** has room 0 at all 16 sign characters.
- **m135's companion** has room 0 at 248 characters and **room 2 at 8**.
  - Each of the 8 is trivial on no end, and both of its classes are interior (h¹ = 2, r¹ = 0).
  - Their deck orbits have sizes 1, 1, 2, 2 and 2.
  - Main's sealed B1494 predicts room 0 at all 256 (cell R2, 60%). This seat's reading is for main's read-out to compare,
    not to build on.

## 4. Proposition N (no three at once)

**Statement.** Let N be the companion of one of the 27 states, and let ν be a character of π₁N with ν⁸ = 1. Then every
class c ≠ 0 of the frame carries:
- at most one generation where ν⁴ = 1;
- at most two elsewhere.

So no member reaches three, in either order.

*Proof.*
- **Theorem C** (sm:B1535): g generations, in either order, need b0 + n(ν⁴) ≥ g, with b0 = [ν⁴ = 1].
- **Lemma F′** (sm:B1545): I(W₁) ≥ k − |A| − b0, where A is the set of ends on which ν is trivial. So g generations need
  |A| ≥ g − b0.
- **If ν⁴ = 1:** b0 = 1 and n(1) = 0 (§2), so g ≤ 1.
- **If ν⁴ = χ ≠ 1:**
  - b0 = 0, and χ is a sign character.
  - Where ν is trivial on an end, so is χ, so |A| ≤ m_A(χ).
  - Hence g ≤ min(n(χ), m_A(χ)).
  - The census of §2 gives min(n(χ), m_A(χ)) ≤ 2 at every sign character of all 27 companions. □

**Two is not excluded.** min(n, m_A) = 2 is reached on seven companions:
- −LLLRR and +LLLLLRR: an orbit of 5, with room 2, trivial on two ends;
- −LLLLLLLR: 22 characters with room 2, trivial on two ends;
- the four twelve-ended companions: orbits with room 2 trivial on two, three or four ends, among them an orbit of 3 trivial
  on four ends on each.

Whether a class there reaches two is a count, not read here.

## 5. What it means

- **For three, this extends main's B1493 to the whole family to twelve ends.** B1493 found no three or two at orders up
  to 8 on L8a15 and o10_150729. Here, on no state-born companion of the family does three come at a single member, at any
  order dividing 8.
- **On main's sentence** "no state-born object read has" a line with room:
  - The room is there: 2 on m135's companion, and 3 and 4 on four twelve-ended companions.
  - But it sits on characters trivial on at most one end, where the floor stops it.
  - At three, the room and the ends never meet.
- **For the owner's question.** On these objects three never comes at once.
  - Where three ones appear on the record, on +LLLR's companion, they are one orbit of the deck symmetry
    (`docs/dossiers/the_three_orbit_2026-10-07/NOTE.md`).
  - Whether generations are such an orbit is GENESIS FK14's question asked one step further. It is not decided here.

## 6. What this does not decide

- Characters whose fourth power has order three or more (ν of order 3, 12, 16, ...): the room of a line of order three or
  more is not read here.
- The second supply n(ν³ ⊗ ρ), and the counts themselves, including whether two is reached at the characters listed in §4.
- Non-unitary characters, covers other than the companions, and states with more than 12 ends.

## Files

- `room_census.py`: committed before the run, at `f7431ba1`.
- `room_census.json.gz`: the run's `room_census.json`, compressed with `gzip -n -9`.
- `room_census_sha256.txt`: the record's sha-256 before compression.
