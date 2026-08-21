# P-TWOENDED — is the Kashaev-tower arithmetic two-ended (E6/√-3 AND E8/√5)?

Standalone bench (`twoended.py`; mpmath + sympy only, no repo imports), run against the
VALUE-PROBING WAVE charter's P-TWOENDED cell. Structure question, not a value match:
does the object's Kashaev-tower arithmetic carry evidence of the spherical Q(sqrt5)/E8 end,
alongside the already-established hyperbolic Q(sqrt(-3))/E6 end?

## PART A — the banked C_3, analysed cold (cheap; runs first in `twoended.py`)

Banked (frontier/B1124, `b1124_verify.py`/`b1124_supplementary.py`, confirmed to 36 digits
by direct comparison against the largest independent window):

```
C_0 = 3^(-1/4)
C_1 = (11/108)            * sqrt(3) * pi   * C_0     (den = 2^2*3^3,  108,   {2,3}-smooth)
C_2 = (697/7776)                    * pi^2 * C_0     (den = 2^5*3^5, 7776,   {2,3}-smooth)
C_3 = (724351/12597120)   * sqrt(3) * pi^3 * C_0     (den = 2^7*3^9*5, 12,597,120)
```

**Independent re-verification (not trusting the NOTES.md prose):** `sympy.factorint`
confirms 724351 = 53 x 79 x 173 (three distinct primes, none repeated, 724351 itself
composite) and 12,597,120 = 2^7 x 3^9 x 5 exactly (both reconstructed and checked equal
to the originals). C_1, C_2's denominators are independently re-confirmed as pure
{2,3}-smooth (108 = 2^2 3^3; 7776 = 2^5 3^5) — the "5" is new at C_3, nowhere before it.

**Denominator growth (no fitted pattern forced):** ratio C_2/C_1 = 72 = 2^3*3^2;
C_3/C_2 = 1620 = 2^2*3^4*5. No factorial or lcm(1..n) match found for 12,597,120 (checked
n=8..17; closest is lcm(1..17)=12,252,240, off by a non-trivial 2.8%, not an exact hit).
**No numerator shares a prime factor with either earlier numerator** (11 vs {17,41} vs
{53,79,173} — three fully disjoint prime sets). Denominator prime-exponent sequences
(2: 2,5,7 ; 3: 3,5,9 ; 5: 0,0,1) show no obvious closed-form pattern from 3 points — noted,
not force-fit.

**Prime-splitting behaviour of 724351's factors** (independent computation, Legendre-type
splitting rule for the two candidate quadratic fields):

| p | p mod 3 | in Q(sqrt-3) | p mod 5 | in Q(sqrt5) |
|---|---|---|---|---|
| 53 | 2 | inert | 3 | inert |
| 79 | 1 | **splits** | 4 | **splits** |
| 173 | 2 | inert | 3 | inert |

79 splits in BOTH fields; 53 and 173 are inert in BOTH. For 3 independent primes this
"same behaviour in both fields" pattern has probability ~1/8 under Chebotarev independence
— a mild coincidence, **not** a statistically meaningful fingerprint tying 724351 to Q(sqrt5)
specifically. Reported, not oversold.

**Transcendental-quantity context** (computed at 60 dps via mpmath Hurwitz-zeta
decomposition — `zeta_K(2) = zeta(2)*L(2,chi_-3)`, `L(2,chi_5) = 5^-2*[zeta(2,1/5) -
zeta(2,2/5) - zeta(2,3/5) + zeta(2,4/5)]`): q3 = 724351/12597120 = 0.05750131776...
is a **plain rational** (established via B1124's 36-digit direct closed-form confirmation)
— it cannot literally equal zeta_K(2), L(chi_5,2), or phi (all irrational/transcendental-type).
An explicit scan of q3 against 8 candidate ratios of these quantities (zeta_K(2)/pi^2,
L(2,chi5)/pi^2, L(2,chi5)/zeta(2), zeta_K(2)/zeta(2), 1/phi^2, 1/phi^3, 1/(5phi), sqrt5/pi^2)
found **no near-simple-rational coincidence** in any of the 8 ratios (all far from any small
integer). This positively rules out a hidden simple-multiple relation; it was not expected
to hit (a rational cannot equal a generic transcendental), but the scan closes that door
explicitly rather than leaving it merely "unlikely."

**The generic, two-ended-UNRELATED alternative mechanism (von Staudt–Clausen):**
Bernoulli-number denominators pick up a new prime p exactly when (p-1) | 2n (von
Staudt–Clausen) — a purely combinatorial rule, present in the perturbative/WKB expansion
of **every** hyperbolic knot invariant (Ohtsuki-type series), with **zero** connection to
any number field. Illustrative computation (B_2..B_12): prime 5 enters the Bernoulli
denominator at B_4, B_8, B_12 (n even, since (5-1)=4 | 2n iff 2n is a multiple of 4) — i.e.
5 "recurs" periodically in this totally mundane setting too. **C_3's bare 5 is fully
consistent with this generic mechanism** and equally consistent with a genuine E8/sqrt5
signal — a single data point cannot distinguish them.

### PART A VERDICT

The "5" in C_3 is a prime factor of a **plain rational coefficient** multiplying
sqrt(3)*pi^3*C_0 — the trace field itself is unchanged (Q(sqrt3), confirmed to 36 digits).
This is structurally **weaker** than a genuine sqrt5/E8 signal: no sqrt5 appears anywhere
in the closed form. The numerator's factorization shows no statistically meaningful
splitting-based fingerprint (~1/8-probability coincidence at best), no simple-rational-
multiple relation to zeta_K(2)/L(chi5,2)/phi, no factorial/lcm match, and no shared prime
factors with C_1 or C_2's numerators. **A single banked data point cannot distinguish**
"the E8 end entering" from "a generic Bernoulli/von-Staudt-Clausen-type combinatorial
prime." Part B is the actual discriminating test — see below.

## PART B — the tower extension (past N=35,000,000)

**Machinery**: reuses the b1124_verify.py precision discipline throughout (constants frozen
at DPS_VOL=700 as decimal strings before any lower-dps context; rescaled-Chebyshev
polynomial-in-1/N fits, never monomial; "trusted digits" = min(within-window K-convergence,
cross-window agreement), reported as both PRIMARY [all genuine windows incl. small-N W1]
and LARGE-WINDOW [big-N windows only] metrics, kept visibly separate). DPS_MAIN doubled to
400 (b1124 used 200) — calibrated cheap on this machine's gmpy2 backend (~11% slower than
dps=200, not the 2-4x one might expect). Windows W1-W5 deliberately match b1124_verify.py's
grids N-for-N (correctness cross-check target); W6 is the new extension.

**Correctness control (before trusting anything new, done by hand ahead of the real run,
not wired up as an in-script flag)**: fresh, independently-written `twoended.py` code
(`compute_vol_fig8`/`J_N_trig_fast`/`freeze_strings`) reproduces the banked b1124 R_N
values EXACTLY (all ~40 reported digits) at N=1000, 2000, 20000. Quick-mode dry run
(tiny grids) exercised the full pipeline end-to-end and correctly re-derived the KNOWN
C_3 = 724351/12597120 relation via PSLQ on the `pi/sqrt3` base, with zero contamination on
Q(sqrt5)/Q(sqrt15) — the machinery is trustworthy before being pointed at the new C_4/C_5
targets (`negative_control` in results.json).

**Extension beyond b1124**: new window W6, N from 38,000,000 to 110,000,000 (~3.1x past
b1124's N=35M ceiling), 10 log-spaced points, plus a DPS_CROSS=600 precision-doubling
subset. (Originally planned larger — 38M-150M/12pt — but scaled down mid-run after this
machine's REAL measured throughput on W3/W4 came in far below initial calibration: ambient
load average climbed from ~2.3 to ~6-8 partway through this session, another long-running
process on this shared machine pinning a full core throughout. Sized to keep the run
bounded rather than committing blindly to a multi-hour block.)

**PSLQ sweep extended beyond b1124**: recognition types extended from {Q, Q(sqrt3)} to
{Q, Q(sqrt3), Q(sqrt5), Q(sqrt15)} (sqrt15 = sqrt3*sqrt5, the multiplicative-compositum
signature) for C_3 (control), C_4, C_5. Candidate BASE family extended from the original 11
{1,3}-flavoured bases with 6 new sqrt5/sqrt15-flavoured bases (pi/sqrt5, pi*sqrt5, sqrt5,
1/sqrt5, pi/sqrt15, pi*sqrt15) — the SAME "flip" mechanism that revealed C_1/C_2's sqrt3
structure via sqrt3-carrying bases, now also probing for a sqrt5 flip. Two bugs caught and
fixed BEFORE trusting the PSLQ stage on the real targets (both would have produced false
readings, caught by unit-testing the fixed logic against known cases before the real run):

1. **Degenerate zero-padding**: for 3-term recognition types, PSLQ can return a relation
   with the irrational coefficient equal to zero whenever the true value is genuinely
   rational — a valid but content-free "hit" that would have misclassified an honest
   single-end null (C_4 landing cleanly on plain Q, as predicted) as a false two-ended
   signal. Fixed: 3-term hits require a NONZERO irrational coefficient to count as `found`.
   Verified in isolation against both a genuinely-rational and a genuinely-Q(sqrt5) test
   value before trusting it on C_4/C_5.
2. **Artificially low maxcoeff cap**: an early version capped the PSLQ search ceiling at
   3,000,000 regardless of achieved precision — the SAME ceiling b1124 itself found
   insufficient for C_3 (whose true canonical-basis height is 12,597,120; b1124 had to
   extend to 20,000,000 to find it). Fixed: maxcoeff now scales with achieved trusted
   digits (capped only by a generous 2-billion runtime-safety bound), so under-searching
   would not silently reproduce the same miss at C_4/C_5's (plausibly much larger) height.

## RESULTS (Part B)

<!-- FILLED IN AFTER THE BACKGROUND RUN COMPLETES -->

## VERDICT

<!-- FILLED IN AFTER THE BACKGROUND RUN COMPLETES -->
