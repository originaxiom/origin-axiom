# CELL 9, RUNG (i) — PREREGISTRATION v2 (re-sealed after §16 STOP)

cc3 audit seat, 2026-07-29. SUPERSEDES v1 (da516046, byte-frozen per
house rules) following the §16 verdict STOP (defects 1–4 + minors,
verdict in cell9_sec16_verdict.md). Each required change is applied
below and marked [RC-n]. §16 re-review required on THIS file before
execution. Gate 5-Q.

## TARGET (unchanged; premises verified by the reviewer)

    lam_1  (r = 3.938916864, mult 2 — see [RC-4])
    lam_2  (r = 4.900085373, mult 1)
    parent (r = 7.072004187, mult 1)

refined to ≥ 25 significant digits (working DIGITS = 27, prec ≈ 116
bits).

## METHOD [RC-5: code must conform to THIS text]

arb/acb collocation at **Y = 0.75** [RC-3: the validated height —
banked artifact y080_rise_validation.txt: 200/200 rise, min t* =
0.868744, margin 0.1187; Y = 0.80's margin measured at 0.0503 is a
knife-edge and is NOT used]. Truncation x_cut = pi*r/2 + ln(10)*27;
mode disk |mu| <= x_cut/(2 pi Y); n from the formula, logged (approx:
lam_1 2290, lam_2 2390, parent 2630).

**Square-system JOINT Newton** on unknowns (a in C^n, r in C):
n collocation rows + 1 normalization row (a[j0] = 1); Jacobian
[[M(r), M'(r)a], [e_j0, 0]] with M'(r) by central difference
(h = 1e-9) in arb; iterate to |dr| < 1e-27 or 10 iterations.

PRECONDITIONS in code:
  P1 [RC-5]: acb.bessel_k orientation z.bessel_k(i*r) validated on
     >= 10 (r, x) samples against mpmath at dps 40, compared IN
     MPMATH (no float collapse), rel dev <= 1e-27 each.
  P2: Newton residual norm strictly decreasing over accepted steps;
     a non-decreasing step aborts with the iterate logged.
  P3 [RC-2]: DISPLACED CONTROL at the MIDPOINT OF THE GAP to the
     nearest certified neighbor (lam_1: start 4.42; lam_2: 5.29;
     parent: 7.21): the iteration must NOT converge to within 1e-20
     of the target value (convergence elsewhere or divergence =
     control passes). Behavior from r ± 0.02 is LOGGED, not fatal.
  P4: three perturbed starts (r, r ± 1e-7) converge to the same
     value to >= 26 digits.

VALIDATION GATE (abort): each refined value agrees with its certified
8-digit value to >= 7 overlapping digits; else the pipeline is
indicted, no PSLQ runs.

STABILITY CERT: recompute at second truncation (x_cut + ln(10)*5);
the OBSERVED |dr|_stab sets the certified digit count AND feeds the
tolerance formula [RC-1]. Requirement to proceed: |dr|_stab < 1e-26.

[RC-4] MULT-2 HANDLING (lam_1): after convergence, (i) assert
near-nullity 2 — the solve is repeated with a SECOND independent
normalization row j1 (chosen with |a_{j1}| within a factor 10 of
|a_{j0}| in the double-precision eigenvector); (ii) PRE-DECLARED
OUTCOMES: |r_{j0} − r_{j1}| < 1e-26 → a single well-defined parameter
(report it); >= 1e-26 → **NEAR-DEGENERATE PAIR DETECTED — report
(r_a, r_b) as the result**; this outcome is a FINDING about the
multiplicity structure, NOT an indictment of the pipeline and NOT
"precision unreachable". The λ₁ PSLQ stage then runs on BOTH values,
labelled.

## THE POWER BOX [RC-1: noise-floor-derived, convention fixed]

RESIDUAL CONVENTION (fixed): PSLQ verdicts use the MAX-NORMALIZED
residual: res(a; v) = |Σ a_i v_i| / (max_i |a_i v_i|).

TOLERANCE FORMULA (sealed; values filled at runtime from the
OBSERVED stability |dr|_stab, logged):
    for test vector v(x), x in {r, lam}: noise = max_i |d v_i/d r|
      · |dr|_stab / max_i |v_i|   (max-normalized propagated floor)
    tol_box = 10 × noise_box    (per box, per target; logged)
A relation is detectable only where H × noise < tol_box headroom —
so the LICENSED HEIGHT per box is recomputed at runtime:
    N_eff(box) = 25 − log10(dynamic range of v)
    H_max(box) = 10^( N_eff / (1.43 · d) ), capped at v1's H
      (deg-2: 1e4; deg-4/minpoly: 1e3), and the LOWER of the two
      caps governs; boxes with H_max < 10 are declared UNPOWERED and
      excluded from the verdict (logged as such, not run silently).
    (Note per the §16 finding: the lam-minpoly box for the parent is
    expected to be UNPOWERED at 25 digits — dynamic range 6.83
    digits; it is expected to survive only at rung (iii)/50 digits.
    Declaring it unpowered here is the honest outcome, not a
    failure.)
Coefficient provenance: 1.43 = one-point calibration off BSV
(100 digits / (d=10 × log10 H=7)); treated as an ESTIMATE with the
dynamic-range correction applied; any hit or exclusion near a box
boundary is re-checked at the raw law.

SURROGATES: 50 per (box, target-class); hit requires surrogate rate
< 0.02. Both r and lam tested where powered.

## VERDICT SEMANTICS (unchanged from v1, plus the unpowered clause)

Rung (i) = instrument validation + first power step; NOT the campaign
falsifier. Negative = "no relation within the POWERED boxes at 25
digits" — the powered boxes are enumerated in the output. Any hit →
cc adversarial re-derivation before any use. Gate failure / pair
detection / unpowered declarations are banked as instrument or
structure facts per [RC-4] and [RC-1].

## SEAL

Algorithm: SHA-256 of this file's bytes; digest in docs/SEAL_LEDGER.md
(never here). §16 re-review verdict on THIS file required in-arc
before execution.
