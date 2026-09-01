# R28 — Kashaev tower (4_1), large-N deepening of R16 — VERDICT: MATCH

Ring R3 recomputation cell, 2026-09-01. Scripts: `deep_kashaev.py` (J_N ladder, ~60 s),
`extrap.py` (Richardson/Vandermonde in 1/N). Data: `S_values.json` (S(N) to 120 digits).

## Blind discipline record
**Read BEFORE writing code:** the cell brief and `R16_kashaev/FINDINGS.md` (claim,
banked rationals C0..C4, R16's achieved digit counts 25/21/17/14/11 at N<=4200).
**Read AFTER my own code ran:** `R16_kashaev/blind_kashaev.py` — only to run its
`kashaev41(50)` against my `J(50)`: agreement to 7e-191 relative at dps=200 (190 digits).
No arc directories, arc scripts or lock tests were opened. Convention: J_N ~ N^{3/2}
e^{Vol N/2pi} sum C_k N^{-k}, Vol(4_1)=3 Im Li2(e^{2pi i/3}); same as R16/arcs (E23 clear).

## Method
J_N = sum_{k<N} prod_{j<=k} (2 sin(pi j/N))^2 via running product (O(N) per N, not
O(N^2)), mpmath dps=700. Ladder N = 2000, 4000, ..., 60000 (30 nodes).
S(N) = J_N e^{-NV/2pi} N^{-3/2}. Coefficients from exact Vandermonde solves in x=1/N
over M nodes (Richardson of order M-1), M = 12..30. Honest digits = agreement across
three distinct node subsets at the same M, and between M=28 and M=30 fits.

## Results (fit with all 30 nodes, acceleration order 29)
| k | fit | stable digits (subset spread, M=28) | M28 vs M30 | digits agreeing with banked closed form |
|---|---|---|---|---|
| 0 | 0.759835685651592547331187750655... | 88 | 91 | 95 (3^{-1/4}) |
| 1 | 0.42111345330918403498274615299... | 82 | 85 | 88 ((11/108) sqrt3 pi C0) |
| 2 | 0.672196052747757283046700658138... | 77 | 79 | 83 ((697/7776) pi^2 C0) |
| 3 | 2.34643068450597129325487040517... | 72 | 74 | 78 ((724351/12597120) sqrt3 pi^3 C0) |
| 4 | 11.3590928633234931030491875274... | 67 | 70 | 73 ((278392949/1813985280) pi^4 C0) |

Claimed honest precision (conservative column): C1 to 82 digits, C2 to 77, C3 to 72,
C4 to 67 — all matching the banked rationals to at least that many digits. The
brief's target (C3 >= 4 digits) is exceeded by ~68 digits. Digit count was still
rising with M when the ladder ended (limited by the 30-node ladder and the 120-digit
storage of S), so this is a floor, not a ceiling; per budget, stopped here.

Ratio c3/(C0 sqrt3 pi^3) = 0.0575013177615200934816847025351826449220 = 724351/12597120
to all 40 printed digits.

## Control (planted negative)
Perturbing the banked C1 by a relative 1e-30 yields a 1.0e-30 mismatch against the
fit, versus 1.3e-89 for the true banked value: a 30th-digit error is rejected by
~59 orders of magnitude. The check could have failed; not vacuous.

## Diff vs R16
R16: N<=4200, 10 nodes, 25/21/17/14/11 digits. R28: N<=60000, 30 nodes,
88/82/77/72/67 digits. All R16 digits contained in R28's values; no discrepancy.
Note R16's FINDINGS table was correct in stating C1 ...4982919 differed from banked
...49827461 at its 21st digit — R28 confirms the banked digits.

Gate 5: no measured SM value enters (inputs: pi, sqrt3, Li2 at a root of unity, integers).

## VERDICT: MATCH
