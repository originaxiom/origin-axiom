# R16 — B1120/B1133 Kashaev tower coefficients — VERDICT: MATCH

Ring R2 recomputation cell, 2026-09-01. Script: `blind_kashaev.py` (this dir). Runtime ~5 s.

## Blind discipline record

**Read BEFORE writing code:** only the cell brief (claim + banked rationals C0..C4 as
stated in the R16 tasking). Nothing from `frontier/B1120_*` or `frontier/B1133_*`, no
arc FINDINGS.md, no `b1120_verify.py`, no lock tests.

**Read AFTER my code ran:** `frontier/B1120_L180_makeorbreak/FINDINGS.md`,
`frontier/B1133_c4_single_end/FINDINGS.md`, `tests/test_b1120_L180.py`,
`tests/test_b1133_c4.py`, and the pooled values in `b1120_results.json` /
`b1124_results.json`. Convention check (E23): the arcs use
J_N ~ N^{3/2} e^{Vol N/2pi}(C0 + C1/N + C2/N^2 + ...) — identical to my blind ansatz;
no convention translation was needed.

## My independent route

- Kashaev invariant from the standard closed form
  J_N = sum_{k=0}^{N-1} prod_{j=1}^{k} (2 sin(pi j/N))^2, mpmath dps=620.
- Vol(4_1) computed independently as 3*Im Li2(e^{2 pi i/3}) = 2.02988321281930725004...
- Ladder N = 900..4200 (step 300); S(N) = J_N e^{-NV/2pi} N^{-3/2}; coefficients by
  exact Vandermonde solve in 1/N over 10 nodes (full Richardson), with three
  overlapping node subsets to bound honest digits.

## Numbers (my fit vs banked)

| k | my fit (fit A) | banked closed form | stable digits | matching digits |
|---|---|---|---|---|
| 0 | 0.759835685651592547331187742959 | 3^{-1/4} = 0.7598356856515925473311877506... | ~26 | ~25 |
| 1 | 0.421113453309184034982919... | (11/108) sqrt3 pi C0 = 0.42111345330918403498274615... | ~21 | ~21 |
| 2 | 0.672196052747757281324... | (697/7776) pi^2 C0 = 0.6721960527477572830467... | ~17 | ~17 |
| 3 | 2.34643068450598127... | (724351/12597120) sqrt3 pi^3 C0 = 2.3464306845059712932... | ~14 | ~14 |
| 4 | 11.3590928632862... | (278392949/1813985280) pi^4 C0 = 11.35909286332349310... | ~11 | ~11 |

Every coefficient matches the banked rational closed form to exactly the stability
limit of my own fit — zero disagreement at my honest precision. The banked pooled
values in `b1120_results.json` / `b1124_results.json` (C0..C4) also match my fit to
the same digit counts.

**Honest precision statement:** my N <= 4200 ladder supports 11 digits at C4 rising
to 25 at C0. That is above the 6-10-digit pass bar for this budget, and far below
the arcs' banked ~30 digits (they used N up to 35M with pooled windows) — I do NOT
independently confirm 30 digits, only 11-25 depending on order.

## Reality-parity law (independently reproduced)

Fitted ratios c_k/(C0 pi^k), odd k further divided by sqrt3:

- k=1: 0.1018518518518518518518... = 11/108 (21 digits)
- k=2: 0.0896347736625514400996... = 697/7776 (17 digits)
- k=3: 0.0575013177615203380... = 724351/12597120 (14 digits)
- k=4: 0.1534703462417771754... = 278392949/1813985280 (11 digits)

Odd -> rational x sqrt3, even -> plain rational, exactly as banked.

## Control (planted negative)

Perturbing C1's rational 11/108 -> 12/108 produces a relative mismatch of 9.1e-2
against my fit, vs agreement ~1e-21 for the banked value: a wrong rational is
rejected by ~19 orders of magnitude. The banked check could have failed; not vacuous.

## Notes on the banked locks

`tests/test_b1120_L180.py` and `tests/test_b1133_c4.py` validate closed forms
against POOLED values stored in the arcs' own JSONs — internally consistent but not
independent of the arc bench. This cell's recomputation IS independent (own J_N
implementation, own volume, own fit) and agrees.

## VERDICT: MATCH

All five banked coefficients (C0-C4) and the odd/even reality-parity law confirmed
independently to 11-25 digits (order-dependent), limited only by this cell's
N <= 4200 budget. C3/C4 were cheap at this precision and were included. Gate 5
untouched: no measured SM value enters anywhere (inputs are pi, sqrt3, Li2 at a
root of unity, and integers).
