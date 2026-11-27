# B1986 — Listening 4: the unweighted unfolding over the common point keeps two modes forever, the constant and an alternation that flips with every move and lives on the body diagonals, and damps the doublet at ½ and the triplets at ½ and 1/√2 per move, through ℚ(√−7)

**Verdict: PROVED (exact eigenvalues of finite permutation sums; two readings post hoc, labelled).** Main, 2026-11-25.
Unattended, on the listening line. Data-free. Register rows P-882 and P-694 (FK15). **0 of 19.**

## Seen first

- **B1984 and B1985:** the one structure the whole forces is the common point. Its neighbourhood carries the cube's
  rotation group at every scale and opens only along the body diagonals.
- **GENESIS's law:** every allowed history happens, unweighted.
- **B147:** ℚ(√−7) is the trace field of the chiral arithmetic pair RRL/RLL.
- **B235:** ℚ(√−7) does not appear on one ladder of trace fields.
- **The record's tick:** P-769, ruled; "even ticks are a condition the weight must deliver".
- **Swept:** `VERDICT topic-sweep /undamped|alternat.{0,20}every move|parity clock|sign character|even ticks|spectral gap|expander/: 23 of 1727 arcs on main match (NEGATIVE 4, OPEN 1, PROVED 18); 13 register rows match (DONE 6, QUEUED 7)`. None computes the unweighted unfolding's spectrum over the common point.
- **The literature:** the Markoff graphs mod p as possible expanders (Bourgain, Gamburd and Sarnak), cited from memory.

## The results (`verification/listen4.py`, `listen4_run.txt`; exact up to numpy's eigenvalues of small permutation sums)

- **The unfolding:** W₊ = P_L + P_R (positive words) and W± = P_L + P_L⁻¹ + P_R + P_R⁻¹ (inverses, GM5b, carried).

**By irreducible of the cube group, which has order 24** (the moves' linear parts; B1687's Aut(Q₈)):

| irreducible | W₊ eigenvalues | modulus relative to the top (per move) | W± eigenvalues |
|---|---|---|---|
| 1, the constant | 2 | 1 | 4 |
| sign | **−2** | **1: never decays, flips with every move** | −4 |
| 2, the doublet (S₃ on the three axes, W1) | ±1 | ½ | ±2 |
| 3, the rotation triplet | 1, (1 ± i√7)/2 | ½, 1/√2 | 2, 2, 0 |
| 3′ = 3 ⊗ sign | −1, (−1 ± i√7)/2 | ½, 1/√2 | −2, −2, 0 |

- **H1 holds:** the sign character is a mode of W₊ with eigenvalue −2.
- **H2 holds as worded,** and is weaker than it reads: the gap of W± below its top is positive at every prime run, but
  small and uneven (post hoc, below).
- **On the cusp's leaf's big orbit mod p,** W₊'s second modulus is √2 at p = 5 and 7, 1.69 at 11 and 1.78 at 13.

## Post hoc, labelled (`irreps_posthoc.py`, `irreps_posthoc_run.txt`; written after the run was read)

- **The irreducible content of each orbit over the common point,** read by characters. It is the same at mod 9, 25 and
  49:
  - centre: 1;
  - faces: 1 + 2 + 3;
  - **vertices: 1 + sign + 3 + 3′;**
  - edges: 1 + 2 + 3 + 2·3′;
  - free orbits of 24: the regular representation.

  **So the undamped alternation lives on the body-diagonal orbits,** and on the free orbits. It never lives on faces or
  edges. (The run's own "persistent mode" label was unreliable where ±2 tie numerically; this reading replaces it.)
- **The gap below the top of W±** on the cusp's leaf without the common point is 0.52, 0.34, 0.13, 0.097, 0.052 and
  0.13 at p = 5 to 19. It is positive and not monotone, and no uniform bound is claimed.

## What the whole does, read in its own terms

- **Two modes are never forgotten:** the constant, and an alternation that flips sign with every move.
  - The alternation lives exactly on the directions along which the whole opens outward (B1985's body diagonals), and
    on the generic orbits.
  - It is the whole's own parity clock. Nobody put it in.
- **Reading, not identification:** a read-out after an odd number of moves sees the alternation reversed, and one after
  an even number does not. This bears on the record's tick and its "even ticks" condition (P-769), which until now was a
  ruling, not a behaviour. Whether they are the same is open.
- **Everything else decays at rates the whole fixes,** with nothing chosen:
  - the doublet (W1's three axes) at ½ per move;
  - the triplets at ½ (their real mode) and at 1/√2 (their complex pair, roots of λ² ∓ λ + 2).
- **So the slowest-fading non-trivial structures are the triplets,** and their decay lives in ℚ(√−7), the trace field of
  the record's arithmetic chiral pair RRL/RLL (B147). That is an observation, not a reading.
- **No Standard Model shape was asked for or read.** The rates are not read as anything physical here.

## What is open

- **Higher levels.** The same spectrum on the tower (mod 27, 81; 125; 343), where the orbits grow beyond the cube.
- **The loop (PF5).** The whole read back on itself: does a self-consistent state exist in which the persistent modes
  feed the unfolding that produced them?

## Dated note (2026-11-26, the web seat's V1, harvest row 2018)

- **The committed output's mode label is corrected.** `listen4.py` took the constant mode as the first of a sort that floating
  noise reorders where +2 and −2 tie in modulus. It now removes the one eigenvalue nearest +2, the Perron root, which is simple
  on a connected orbit. The rerun changes exactly 14 lines, the 24-point orbits at mod 25 and 49, from 2.0000 to −2.0000.
  That is the reading this page already gave (the alternation lives on the free orbits). Found by the web seat's V1 and
  credited to it.

## Dated note (2026-11-27, the web seat's A84 § 2, harvest row 2033; checked by main on this arc's files)

`listen4_run.txt`'s mod-5 line prints "gap of W+- 7.7033": `listen4.py` sorts W+-'s eigenvalues by modulus, and at p = 5 the lowest, -3.7033, outweighs the second by value, 3.4812, so the printed number is 4 minus the lowest, not a gap. The gap below the top is 0.5188 (`irreps_posthoc_run.txt`), as this page says (0.52). If the gap is ever read as the decay per move, the two-sided gap at p = 5 is 0.30, the slowest non-constant mode of W+- sitting at the bottom of the spectrum; at p = 7 to 19 the two agree. No claim rests on 7.7033.
