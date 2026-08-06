# CELL 9, RUNG (i) — PREREGISTRATION (sealed before compute)

cc3 audit seat, 2026-07-29. B796 keystone ladder, first rung. Owner
greenlight; §16 non-authoring review REQUIRED between this seal and
execution. Gate 5-Q. Rung-1 comparison class (algebraicity,
falsifiable-to-precision, LISTENING_PROTOCOL §8.1).

## TARGET

Three eigenvalues of m004, refined from the certified 8-digit values
to ≥ 25 significant digits (working dps 30, 2 guard digits beyond the
25 used):

    lam_1  (r = 3.938916864, mult 2 — refine the PARAMETER; the
            eigenspace basis ambiguity does not affect r)
    lam_2  (r = 4.900085373, mult 1)
    parent (r = 7.072004187, mult 1 — the Bianchi ground state; its
            25-digit value is ALSO the sharpest available check on
            the G-H 51.014 transcription)

## METHOD (instrument)

arb/acb (python-flint, C-speed) collocation at Y = 0.80: truncation
for 27-digit tails (x_cut = pi*r/2 + ln(10)*27), giving n ≈ 2100-2400
modes (computed at runtime from the formula, logged); K_{ir} at acb
precision via the exponentially convergent trapezoid (h from the
Poisson bound for 27 digits; validated against mpmath.besselk at
dps 40 on ≥ 10 sample points to ≤ 1e-27 relative BEFORE use); Newton
refinement on the square system (n+1 rows: collocation + one
normalization row) starting from the certified value; pullback points
recomputed at dps 40 in mpmath (exact-translate property makes any
converged pullback valid; precision only enters matrix entries).

PRECONDITION ASSERTS, in code (E31 discipline):
  P1 Bessel validation ≤ 1e-27 rel on all samples;
  P2 overdetermination check on the scan matrix that seeds Newton
     (rows ≥ 1.3 × cols) OR square-system residual monotone decrease
     over Newton steps;
  P3 DISPLACED CONTROL that must FAIL: Newton started at r ± 0.02
     must NOT converge back to the target value (convergence to the
     displaced well or divergence = control passes);
  P4 three perturbed starts (r ± 1e-7, r) converge to the SAME value
     to ≥ 27 digits.

VALIDATION GATE (abort condition): each 25-digit value must agree
with its certified 8-digit value in the overlapping digits (≥ 7
digits). Disagreement ⇒ the arb pipeline is INDICTED; NO PSLQ runs;
banked as an instrument fact.

STABILITY CERT: each value recomputed at a second truncation
(x_cut + ln(10)*5); |Δr| must be < 1e-26; the certified digit count
is set by the observed |Δr|, not assumed.

## THE SEALED POWER BOX (rung i)

PSLQ at working dps 30 on 25 certified digits, per the power law
N ≥ 1.43·d·log10(H):

    B1-B3 (deg-2 fields; 3-vector [x, 1, sqrt(k)]):    d=3, H ≤ 10^4
    B4-B6 (deg-4 fields; 5-vector [x, 1, b, b^2, b^3]): d=5, H ≤ 10^3
    MINPOLY box (5-vector [1, x, x^2, x^3, x^4]):       d=5, H ≤ 10^3

Both r_n and lam_n = 1 + r_n^2 tested. Surrogate nulls: 50 per basis
per digit-class (B743); a relation is a HIT only if the surrogate
rate < 0.02. Tolerance 1e-23.

## VERDICT SEMANTICS (fixed now)

- Rung (i) is INSTRUMENT VALIDATION + the first power step. A clean
  negative here = "no low-height algebraicity at 25 digits in the
  named boxes" — it does NOT fire the campaign falsifier (that is
  the 50-digit box, rung iii) and is not evidence for H2 or H0.
- Any PSLQ hit → cc adversarial re-derivation BEFORE any use or
  write-up. A hit surviving cc would be extraordinary (literature
  prior against) and still establishes only "the BC/CM route is not
  closed at this height" — never an SM value.
- Validation-gate failure or unreachable precision → banked as an
  instrument fact; the ladder pauses; the exploratory-interpretive
  fallback governs only if the 50-digit rung proves unreachable
  after the symmetrization/arb alternatives are exhausted.

## SEAL

Algorithm: SHA-256 of this file's bytes; digest recorded in
docs/SEAL_LEDGER.md (never in this file). §16 review verdict file
required in-arc before execution.
