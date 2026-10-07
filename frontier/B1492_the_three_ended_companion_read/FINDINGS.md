# B1492 — THE THREE-ENDED COMPANION READ: the harmonic frame on L8a15 (+LLLR's three-ended companion) and on m003's five-ended companion o10_150729 — every sealed prediction holds; every interior class at a sign character counts exactly one, on three ends and on five as on one; on L8a15 the members sit where no end carries the character and no character trivial on an end has a member at all — the ends enter the bound, not the value

**Verdict: PROVED** — D1, D2, D3, D4, D5 hold (D3 at its 40% prior: three members). Scope: frames F-HE (the SM seat's,
sign characters of the four, B1297's class index with every cusp stacked) and F-CI (B1418's definitions); objects
L8a15 = 8³₃ (the three-ended companion of +LLLR, B1491) and o10_150729 = S³ − L10n113 (the five-ended companion of
m003); reach single for the objects, with one census sentence across the four objects read on main (§3). cc (main),
2026-10-07. Sealed `872c082ec` (sha256 52dcd6db) before any reading of the harmonic frame on either companion. The
SM seat's Proposition 3 (its companions note) was a hypothesis here, read and not assumed. No physical quantity.
**0 of 19.**

**Credit.** The SM seat for the companions (its Proposition 1) and for the floor and ceiling the readings are measured
against; B1485 for the one-cusped instrument the multi-cusp one reproduces row for row.

## 0. Seen first, and literature

As sealed: `VERDICT topic-sweep /L8a15|8\^3_3|three-ended|three ends|L10n113|o10_150729/: 4 of 1363 arcs on main match (NEGATIVE 1, PROVED 3)`
— B1291, B1477, B1483, B1491. **Literature:** none. The controls (`control_m135.json`, `control_m136.json`) reproduce
B1485's exact census and member readings on m135 and m136 row for row — the two members of each, at (−1, −1) with the
class dead on the cusp, m135's boundary-type classes at (0, −1); the test locks them.

## 1. Results on L8a15 (`survey_L8a15.json`; the table from `summary.py`)

Presentation: three generators, two relators, three cusps; H₁ = ℤ³, so eight sign characters, written as the signs
of (a, b, c). "Trivial on cusp" marks the ends on which ν is trivial on both peripheral words (m_A is their number);
"dead on cusp" marks the ends on which the class restricts to a coboundary (k is the number where it does not).
Floor k − m_A − b0 and ceiling 2m_A + m_B − b0 as the seat's (B1491); the ceiling is given twice — the survey's column
set m_B = 0, and for a sign character ν⁴ = 1 on every cusp, so the seat's m_B is (cusps − m_A) and its ceiling the
larger number; both hold at every reading, the survey's being the stricter (§4).

| ν | trivial on cusp | m_A | class | dead on cusp | k | I(W₁) | I(Λ²W₁) | floor | ceiling (survey / seat) |
|---|---|---|---|---|---|---|---|---|---|
| +++ | 111 | 3 | other 0 | ··· | 3 | 0 | 0 | −1 | +5 / +5 |
| +++ | 111 | 3 | other 1 | ··· | 3 | 0 | 0 | −1 | +5 / +5 |
| +++ | 111 | 3 | other 2 | ··· | 3 | 0 | 0 | −1 | +5 / +5 |
| ++− | ··· | 0 | **interior 0** | ddd | 0 | **−1** | **−1** | −1 | −1 / +2 |
| +−+ | ·1· | 1 | other 0 | d·d | 1 | 0 | 0 | −1 | +1 / +3 |
| +−− | ··· | 0 | **interior 0** | ddd | 0 | **−1** | **−1** | −1 | −1 / +2 |
| −+− | 1·· | 1 | other 0 | ·dd | 1 | 0 | 0 | −1 | +1 / +3 |
| −−+ | ··· | 0 | **interior 0** | ddd | 0 | **−1** | **−1** | −1 | −1 / +2 |
| −−− | ··1 | 1 | other 0 | dd· | 1 | 0 | 0 | −1 | +1 / +3 |

The eighth character, −++, has h¹ = 0: no class to read.

| | sealed prediction | prior | result |
|---|---|---|---|
| **D1** | at the trivial character h¹ = 3, one boundary-type class per end, no interior class; floor and ceiling hold at every reading | 85% | **HOLDS**: h¹ = 3, interior 0, three boundary-type classes each alive on all three ends (k = 3) and counting (0, 0); floor −1 ≤ 0 ≤ 5 |
| **D2** | at every sign character and class, −I(W₁) ≤ 1 — no three, no two | 75% | **HOLDS**: I(W₁) ∈ {−1, 0} over the nine readings; the largest count is one |
| **D3** | some sign character carries an interior class (a member) | 40% | **HOLDS**, three times: ++−, +−−, −−+ — each at m_A = 0, the class dead on all three ends, reading (−1, −1) |
| **D5** | F-CI: 12 isometries, none orientation-reversing, the order-3 ones fixing no cusp, cusp counts {0, 4} — no three | 95% (seen) | **HOLDS** under the seal (`fci_L8a15.json`): 12, chiral, acting on the three ends as S₃ (the kernel one involution, −I on every cusp, det 4); the four order-3 elements fix no cusp; cusp-fixing values {0: 6, 4: 6}; the three cusps have shape 0.642 + 2.365i — neither hexagonal nor rectangular |

**What the table says, read as the seal asked (the cusp decomposition of every count).** The members are exactly
the characters trivial on *no* end (m_A = 0), as m136's are (B1485: both members at m_A = 0); there the class dies on
every end (k = 0) and the floor is −b0 = −1, attained — the one generation is the b0 one, the trivial direction of
ν⁴, not an end. The three characters trivial on exactly one end — one per end, ·1·, 1··, ··1, the S₃ orbit of the
ends in the characters — carry no interior class: one boundary-type class each, alive on the two other ends, counting
zero. **No character trivial on any end has an interior class.** So the three ends of L8a15 never enter a count: where
an end could count, there is no member; where there is a member, no end is special. On the first three-ended object
born of a word state, the harmonic frame counts one, from the same source as on the one-cusped members.

## 2. Results on o10_150729 (`survey_o10_150729.json`)

Five generators, five cusps, H₁ = ℤ⁵, thirty-two sign characters. The full table (64 readings, every cusp decomposition) is `summary.py`'s output on `survey_o10_150729.json`;
the thirty-two characters sort exactly by the number of ends on which the character is trivial:

| characters | m_A | h¹ | interior | boundary-type | the interior reading | the boundary-type readings |
|---|---|---|---|---|---|---|
| +++++ | 5 | 5 | 0 | 5, each alive on all five ends (k = 5) | — | (0, 0) ×5 |
| 10 characters, trivial on two ends | 2 | 3 | 1, dead on every end (k = 0) | 2, alive exactly on the two trivial ends (k = 2) | **(−1, −1)**; floor −3 | (+1, −1) ×2; floor −1, ceiling 3 / 6 |
| 15 characters, trivial on one end | 1 | 2 | 1, dead on every end | 1, alive exactly on the trivial end (k = 1) | **(−1, −1)**; floor −2 | (0, −1); floor −1, ceiling 1 / 5 |
| 6 characters, trivial on no end | 0 | 0 | — | — | — | — |

Each end is trivial for exactly eight of the thirty-two characters. Here h¹ = m_A + 1 at every non-trivial character
with an end, and the one interior class is the member — the opposite arrangement from L8a15, where the members sit at
m_A = 0 and the characters with a trivial end have no interior class.

| | sealed prediction | prior | result |
|---|---|---|---|
| **D4** | at the trivial character h¹ = 5, no interior class, no reading with −I(W₁) ≥ 3 | 75% | **HOLDS**: h¹ = 5, interior 0, five boundary-type classes each alive on all five ends (k = 5) counting (0, 0); at every one of the 64 readings over all 32 characters −I(W₁) ≤ 1 — no three anywhere, and no two; I(W₁) ∈ {−1, 0, +1} |

Here, unlike on L8a15, the characters trivial on one or two ends *do* carry an interior class (m_A = 1 or 2, the class
dead on every end, k = 0), where the floor allows two or three generations (k − m_A − b0 = −2, −3) — **and the reading
is (−1, −1), one, at every one of them.** The slack in the floor is never taken. The boundary-type classes at those
characters read (+1, −1) when alive on two ends and (0, −1) when alive on one: no generation shape, and in the opposite
order one again.

## 3. The census sentence, and what it says for FK14

On every object the harmonic frame has been read on by main's instruments — m135 and m136 (B1485, one end),
L8a15 (three ends), o10_150729 (five ends) — **every interior class of the four at a sign character reads
(I(W₁), I(Λ²W₁)) = (−1, −1) with the class dead on every end: the count is one wherever it is not zero,** whatever the
number of ends and whatever m_A (0, 1 or 2 across the four objects). The floor's room, m_A + b0 − k, is 1 on m136
and L8a15's members, 2 on m135's and on o10_150729's one-end characters, 3 on its two-end characters; the value is 1
throughout. On o10_150729 the boundary-type classes alive on two trivial ends read I(W₁) = +1 — the only positive value on the four objects — and I(Λ²W₁) = −1 with it: not generation-shaped, and one in the opposite order.

For FK14 ("does the genesis generate states with several ends, or are generations not ends?"), the first read of a
companion gives evidence to the second half: ends raise the floor's room and the value does not follow. The
companions are several-ended and the count at sign characters is the one-cusped states' count. What the sign
characters do not reach, and this arc does not rule: characters of order four and eight on the companions (b0 = 0 and
m_B ≠ cusps − m_A there, so the ceiling and floor change shape), and the seat's non-unitary characters (its P9,
recorded under FK14 and not adopted as a programme). A three on a companion is not excluded by this arc; it is not
reached by the ends alone, which is what the companions were registered to test. In F-CI (D5) the same object says
the same thing in the other frame: an order-3 symmetry cycling the ends exists and fixes no cusp, and the cusps are not
hexagonal — B1490's two conditions both fail, and the three is absent.

## 4. Disclosed

- **Not blind to the shape of the answer:** B1485's one-cusped readings and the seat's Proposition 3 had been read.
  Nothing on either companion was read before the seal; D5's facts were seen unsealed in B1491's landing and are
  recomputed here.
- **The ceiling column.** The survey wrote the ceiling with m_B = 0 (`multicusp.py:166`); for sign characters the
  seat's m_B is cusps − m_A. `summary.py` checks both: the survey's number is the smaller, every reading satisfies
  it, so the seat's ceiling holds a fortiori. The floor column is the seat's exactly.
- Numerical (HP holonomy, 40 digits; SVD ranks at 10⁻²⁴ relative), not exact; the one-cusped controls agree with
  B1485's exact numbers row for row. A reading at a boundary-type class is at a representative of a complement.
- The F-CI cell (`fci_L8a15.py`) is B1490's loop (B1418's definition) on L8a15, with the order of each isometry's
  action on the ends added.
- The five-ended survey ran 53 minutes; the three-ended one seven.

## 5. Files

`verification/multicusp.py` (sealed), `summary.py`, `fci_L8a15.py`; `survey_L8a15.json`, `survey_o10_150729.json`,
`summary.json`, `fci_L8a15.json`, the run logs; the controls; `ARTIFACT_HASHES.txt` (the sealed instrument and
controls). Test: `tests/test_b1492_the_three_ended_companion_read.py`.

**Addendum (S84, 2026-10-08; B1604).** The instrument's validity condition, found by the Euler-characteristic control: at its 40 digits (SnapPy's high-precision holonomy, ~60) the stacked index is reliable only where the four's relator residual max |four(r) − I| sits well below the rank tolerance (10⁻²⁴ relative) — in practice below 10⁻²⁸; on covers with relators of hundreds of letters the residual reaches 10⁻¹⁸…10², the Fox matrices are noise and the ranks are not established. Check the residual (and χ = 0, T-NO-INDEX-IN-THREE) before any reading on a cover; for long covers use a polished holonomy at higher precision. The sign of SnapPy's SL(2, ℂ) lift on a cover's relators (a residual of exactly 2.83 = ‖−2I‖) is harmless: it cancels in the four.
