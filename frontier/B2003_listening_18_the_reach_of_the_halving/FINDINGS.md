# B2003 — Listening 18: the half-scale copy of the neutral sector is the whole's prime 3's own — it holds exactly up the 3-tower from mod 27 (mod 27, 81, 243), exactly where ω's exchange fixes three points, and nowhere else run (mod 9, 25, 49, 15, 45)

**Verdict: PROVED (exact by FLINT up to 1,372 points; mod 243 to 10⁻⁸ by the symmetric eigensolver; R1 and R3 failed as
worded).** Main, 2026-11-25, in the author's /loop "continue the listening line". Data-free. Register row P-882. **0 of 19.**

## Seen first

- **B2002:** p_neutral(2x) = 2^d (x² − 9) x S(x) at mod 27 and 81; it fails on the leaf mod 5 and 7.
- **B2001:** the covariant whole is the symmetric walk on three move pairs.
- **B1984 and B1985:** composite levels are CRT products, and the 3-tower is self-similar.
- **Swept:** `VERDICT topic-sweep /halving|half-scale|C-fixed|fixed points of omega|orbit of \(3,3,3\)/: 5 of 1744 arcs on main match (NEGATIVE 1, OPEN 1, PROVED 2, RETRACTED 1); 1 register rows match (QUEUED 1)`. Only B2001 and B2002 read this halving.
- **The literature (standard):** characteristic polynomials over ℤ (FLINT); symmetric eigensolvers.

## The results (`verification/reach.py`, `reach_run.txt`)

| level | orbit of (3,3,3) | C-fixed points | identity | neutral non-top modes paired by halving (multiplicity-aware) | charged-sector dimension |
|---|---|---|---|---|---|
| mod 9 | 8 | 2 | fails | 0 of 2 | 2 |
| mod 27 | 72 | 3 | **holds (exact)** | 23 of 24 | 23 |
| mod 81 | 648 | 3 | **holds (exact)** | 215 of 216 | 215 |
| mod 243 | 5,832 | 3 | **holds (10⁻⁸)** | 1,943 of 1,944 | 1,943 |
| mod 25 | 1,000 | 1 | fails | 0 of 333 | 333 |
| mod 49 | 1,372 | 1 | fails | 0 of 457 | 457 |
| mod 15 | 40 | 1 | fails | 0 of 13 | 13 |
| mod 45 | 320 | 2 | fails | 4 of 106 | 106 |

- **R1 fails as worded.** The identity holds at mod 243, every eigenvalue to 10⁻⁸, but not at mod 9. That level is an 8-point
  orbit with two C-fixed points, and it pairs nothing.
- **R2 holds:** at mod 25 and 49 no mode pairs.
- **R3 fails as worded:** mod 15 pairs nothing; mod 45 pairs 4 of 106.
- **R4 holds:** wherever the identity holds, C fixes exactly three points of the orbit, and wherever C fixes one or two, it
  fails.
- **The charged pair's polynomial is a perfect square at every level** (exactly up to 1,372 points): the two charged members
  are always equal.
- **The multiplicity-aware count is exact where B2002's was not:** every charged mode is paired, and one null mode of the
  neutral sector is left over, matching the identity's factor x.

## What the whole does, read in its own terms

- **The exact half-scale copy is the whole's prime 3's own.**
  - It holds up the 3-tower from mod 27 on, to mod 243 as far as run, where ω's exchange fixes three points.
  - It is absent at the prime squares 25 and 49, at the mixed level 15, and at the first rung, mod 9.
  - At mod 45, which carries 9 = 3², only 4 of 106 modes pair.
- **The three fixed points are the identity's own count.** The identity leaves out exactly three neutral modes: the constant,
  the alternation and one null mode. It holds exactly where there are three.
- **So the three, ω's exchange, and the prime 3 meet here.** At the whole's own prime, once three points are fixed, the
  charged pair becomes an exact half-scale copy of the neutral member.
- **No rate or ratio is read as physical, and nothing is compared with data.**

## What is open

- **The mechanism:** a map from the neutral sector to the charged pair, through the three fixed points, with W K = ½ K W.
- **A proof for every 3ᵏ with k ≥ 3.** The 3-tower is self-similar (B1985), which suggests an induction.
- **Mod 45's four paired modes:** what they are, and whether mod 135 = 27 · 5 pairs more.
