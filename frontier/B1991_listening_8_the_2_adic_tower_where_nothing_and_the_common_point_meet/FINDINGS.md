# B1991 — Listening 8: at 2 the common point's group is the three (S₃), not the cube; the whole's two forced states stay distinct fixed points, while their levels, existence's and nothing's, coincide mod 4 and part only mod 8

**Verdict: PROVED (exact, every reading over the meeting point mod 2^k, k = 2 to 6).** Main, 2026-11-25, in the author's
/loop "continue the listening line". Data-free. Register row P-882. **0 of 19.**

## Seen first

- **B1988:** the whole fixes exactly the common point (0, 0, 0) and "nothing" (2, 2, 2), which coincide mod 2.
- **B1984:** the 2-adic tower splits further than any odd prime's.
- **B1985:** at odd p the moves act over the common point as the cube group.
- **B1600 (W1):** each move fixes a different nonzero parity of the records, and any two cycle all three.
- **The literature:** the reduction of SL(2, ℤ)'s action mod 2 to S₃ ≅ SL(2, 𝔽₂) (standard). No other source is used.
- **Swept:** `VERDICT topic-sweep /2-adic|mod 4|mod 8|parity|S_?3|the three/: 298 of 1732 arcs on main match (NEGATIVE 34, OPEN 19, PROVED 243, RETRACTED 2); 317 register rows match (DECLINED 6, DONE 195, LEAD 4, Q`. The record's parity results (W1, B1600) are the precedent. No arc follows the 2-adic tower over the
  meeting point.

## The results (`verification/listen8.py`, `listen8_run.txt`; exact)

- **Q1 holds:** over 𝔽₂ the linear group of dL and dR has order 6, and every element permutes the three coordinates.
  It is S₃, W1's three. The cube group's signs die mod 2.
- **Q2 holds:** from mod 4 on, (0, 0, 0) and (2, 2, 2) are separate orbits of size 1.

| level | readings over the meeting point | orbits | sizes (size × count, largest first) |
|---|---|---|---|
| mod 4 | 8 | 4 | 3 × 2, 1 × 2 |
| mod 8 | 64 | 12 | 24, 12, 6 × 2, 3 × 4, 1 × 4 |
| mod 16 | 512 | 40 | 96 × 2, 24 × 5, 12 × 7, 8 × 2, 6 × 12, 3 × 8, 1 × 4 |
| mod 32 | 4096 | 132 | 384 × 4, …, 1 × 4 |
| mod 64 | 32768 | 416 | 1536 × 8, …, 8 × 4 |

- **The fixed points.** From mod 8 on there are four at each level: the two forced states, and two shadows,
  (2^(k−1), …) and (2^(k−1) + 2, …), the extra solutions of x(x − 2) ≡ 0 mod 2^k. The shadows move with the level and do
  not persist up the tower.
- **The levels.** Mod 4 every reading over the meeting point lies on κ ≡ 2, because the cusp's level −2 and nothing's
  level 2 agree mod 4. Mod 8 they part: the leaf κ ≡ 2 carries 7 orbits and κ ≡ 6 ≡ −2 carries 5.

## What the whole does, read in its own terms

- **Its two primes carry its two finite structures.**
  - At 2, the common point's group is S₃: the three parities, W1's three.
  - At 3, and at every odd prime, it is the cube group S₄ (B1984, B1985). S₄ maps onto S₃: its quotient by the
    four-group is the three again.
- **At 2, existence and nothing are hardest to tell apart.** Their readings are distinct fixed points at every level,
  but their frustration levels agree mod 4 and part only mod 8. The cusp's κ − 2 = −4, so 2-adically existence at the
  cusp sits at distance ¼ from nothing. That is a reading.
- **No Standard Model shape was asked for or read.**

## What is open

- **The structure-not-values question,** asked of everything the listening line has found (B1983 to B1991): does the
  whole fix any continuous number, or only discrete structure and algebraic rates? If only the latter, that is GENESIS's
  alternative ending, to be proved, not assumed.
