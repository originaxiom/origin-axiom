# B1996 — Listening 12: up the tower of the whole's own prime 3 the slowest forgetting settles at one number, 1.915298…/2 ≈ 0.9576 per move, at mod 81, 243 and 729; on the 5-tower it keeps rising

**Verdict: PROVED (numerical, sparse Arnoldi, with dense eigenvalues at mod 81; the identification of the number is
open).** Main, 2026-11-25, in the author's /loop "continue the listening line". Data-free. Register rows P-882 and P-630.
**0 of 19.**

## Seen first

- **B1987:** over the common point, the large outward orbits decay more slowly at each level than the cube's 1/√2:
  0.707 (mod 27), 0.958 (81), 0.839 (125), 0.928 (343).
- **B1992:** what the whole selects by finitely many conditions is algebraic. A tower limit could escape that.
- **B1983, B1984, B1991:** the whole's own primes are 2 and 3.
- **Swept:** `VERDICT topic-sweep /spectral gap|slowest decay|mixing rate|expander|1\.9153|0\.957/: 4 of 1737 arcs on main match (PROVED 4); 1 register rows match (QUEUED 1)`. B451 (one thread's escape rate) and the record's expander mentions. None follows the unfolding's
  slow decay up the tower.
- **The literature:** the expansion of the Markoff graphs mod p, an open question in Bourgain, Gamburd and Sarnak's
  programme. Cited from memory; nothing here rests on it.

## The results (`verification/tower_decay.py`, `tower_decay_run.txt`)

| level | points over the common point | largest orbit | W₊'s largest moduli (after 2, 2) | slowest decay per move | W±'s gap below 4 |
|---|---|---|---|---|---|
| mod 27 | 243 | 72 | 1.4142 | 0.7071 | 0.354 |
| mod 81 | 2,673 | 648 | **1.9153** | **0.9576** | 0.041 |
| mod 243 | 24,057 | 5,832 | **1.9153** | **0.9576** | 0.041 |
| mod 125 | 3,125 | 120 | 1.6779 | 0.8389 | 0.130 |
| mod 625 | 90,625 | 3,000 | 1.9894 | 0.9947 | 0.0053 |

- **D1 holds:** the control reproduces B1987 at mod 27, 81 and 125.
- **D2 holds at 5 and fails at 3:**
  - on the 5-tower the slowest decay rises (0.839, then 0.995);
  - **on the 3-tower it does not rise:** 0.9576 at mod 81 and at mod 243.

## Post hoc, labelled (`settle_posthoc.py`, `settle_posthoc_run.txt`; written after the run was read)

- **(c) The next level holds it.** Mod 729: 229,635 points over the common point; the largest orbit has 52,488 points; the
  slowest decay is again **0.9576**. That is three levels running (81, 243, 729), while the orbit grows ninefold each
  time.
- **(a) The number's eigenvalues are real:** +1.915298 (twice) and −1.915298 (twice) at mod 81, the same ± alternation
  as the undamped modes.
- **(b) It is algebraic,** an eigenvalue of a 648 × 648 integer matrix, but not identified. The polynomial search at
  double precision returned candidates with coefficients near its search limit, which that precision cannot support.
  They are not trusted, and the number is reported unidentified.

## What the whole does, read in its own terms

- **At its own prime the whole forgets at one fixed rate.**
  - Along the 3-tower, beyond the cube's 1/√2, the slowest non-undamped mode decays at λ*/2 per move, with
    λ* = 1.915298…, the same at every level from mod 81 to mod 729.
  - As the orbits unfold outward, no slower mode appears.
- **At 5, which is not one of the whole's primes, nothing settles** in the levels run.
- **This is the first number the whole fixes by its own dynamics** rather than by symmetry alone. It is algebraic (at a
  finite level), as B1992 requires.
- **It is not read as anything physical,** and no Standard Model shape was asked for.

## What is open

- **λ*'s exact identity:** its minimal polynomial, through the orbit's quotient by its symmetries at high precision.
- **Whether the 3-tower stays settled beyond mod 729.**
- **Whether the 5-tower settles later.**
- **Whether the 2-tower** (B1991) has its own settled rate.
