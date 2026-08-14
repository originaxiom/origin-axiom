All checks complete. Here is the verdict file content.

---

# §16 FACTUAL REVIEW VERDICT — CELL 9 RUNG (i) PREREG (seal da516046)

Reviewer: non-authoring §16 seat, 2026-07-29. Seal verified: sha256 of
`frontier/B796_coupling_campaign/CELL9_RUNG1_PREREGISTRATION.md` =
da516046... matches SEAL_LEDGER.md:441.

## VERDICT: STOP

Two sealed quantitative criteria are arithmetically defective (the PSLQ
tolerance and the P3 control), one sealed precondition is unvalidated and
is falsely claimed as validated in the execution vehicle, and one sealed
factual claim (mult-2 harmlessness) is unsupported by the repo's own
evidence. These are defects IN sealed numbers and sealed semantics, not
missing asserts — the prereg must be amended and re-sealed.

## DEFECT 1 (primary, arithmetic): the sealed power box cannot detect the relations it claims power over. Tolerance 1e-23 sits BELOW the propagated input-noise floor of every box.

Even at the prereg's own best-case accuracy (stability cert |Δr| < 1e-26),
a TRUE relation evaluated on the refined values has residual:

- deg-2 box [x,1,√k], H ≤ 1e4, x=r: up to 1e4·1e-26 = **1e-22** > 1e-23.
  Coefficients above ~1e3 are undetectable; the top decade of the sealed
  height range is dead.
- deg-2 box, x=λ (parent, λ=51.013, Δλ=2rΔr=1.4e-25): up to **1.4e-21**.
  Coefficients above ~70 undetectable — 2.2 of the 4 sealed height decades dead.
- MINPOLY box [1,x,x²,x³,x⁴], H ≤ 1e3, x=λ (parent): Δ(λ⁴)=4λ³Δλ =
  **7.5e-20 PER UNIT COEFFICIENT** — 7500× the tolerance at a₄=1. No true
  quartic relation for the parent λ, of ANY height, can ever pass the 1e-23
  gate. The box is fully vacuous for exactly the value the prereg calls
  "the sharpest available check on the G-H transcription."
- MINPOLY, x=r (parent): 1e3·1.4e-23 = 1.4e-20 > 1e-23. Also dead.

Consequence: executed as sealed, the PSLQ stage returns NEGATIVE by
construction, and the sealed verdict semantics would bank "no low-height
algebraicity at 25 digits in the named boxes" — an unsound claim, the exact
E31 shape (confident negative that is a tolerance artifact). The 50-surrogate
null check does NOT protect here: surrogates control false POSITIVES; this
defect is guaranteed false negatives. Note the prereg also never fixes the
residual convention (raw |Σaᵢvᵢ| vs max-normalized); under normalization the
numbers change by up to 6.8 orders (λ⁴=6.77e6) — a sealed numeric criterion
whose meaning is convention-dependent is not sealed.

Secondary on the same box: the coefficient 1.43 traces only to
MASTERPLAN.md:267 "chat1's calibration off BSV: d ≤ 10, H ≤ 1e7 at ~100
digits" — a one-point fit (100/(10·7) = 1.4286). Raw law licenses the boxes
(17.16 and 21.45 ≤ 25), but it ignores dynamic range: the λ-minpoly vector
spans 4·log10(51.013) = 6.83 digits, leaving 18.17 effective digits vs the
law's own 21.45 requirement. The λ-minpoly box is unlicensed by the
campaign's own power law once the spread is accounted.

## DEFECT 2 (arithmetic): P3, the displaced control, cannot function as sealed.

Certified spacings (eigenvalues_final.json): nearest other eigenvalue to
lam_1 is 0.9612 away; to lam_2, 0.7706; to parent, 0.2775. There is NO
eigenvalue within 0.26 of any displaced start r ± 0.02 — the sealed pass
branch "convergence to the displaced well" is impossible; no well exists.
The only way P3 can pass is Newton divergence from a point 2-10% of the
local spacing away from a genuine zero — i.e., the control rewards a
fragile solver. Conversely, a correct pipeline with a healthy basin
(basin ~ fraction of the 0.28-0.96 gaps; 0.02 is plausibly inside it, and
no repo artifact measures the basin) converges back and P3 ABORTS IT.
A precondition assert that a correct pipeline plausibly fails and that a
broken one can pass is not a control; as sealed it must-fail-on-correct
with unknown probability.

## DEFECT 3 (unvalidated precondition asserted as fact): Y = 0.80.

groundwork.txt validates horosphere rise only for Y ≤ 0.75 (min t* =
0.8687 at Y=0.75, monotonically FALLING from 0.9114 as Y rises 0.56→0.75).
Y = 0.80 appears in no validation artifact anywhere in the repo. The
execution script cell9_rung1.py:10 states "validated: 200/200 rise, floor
0.8503" — grep finds no artifact backing that number; a validation claim
that traces to nothing is a §16 stop-shape on its own. Y=0.80 is probably
below the Ford floor (≈ √3/2 = 0.8660, consistent with the measured
0.8687), but the margin is ≤ 0.066 and untested — and a non-rising point
silently degenerates its row (c(Y)=c(Y)) and drops rank. The entire saving
from Y=0.80 over the validated Y=0.75 is 14% of modes (2313 vs 2632).

## DEFECT 4 (unsupported sealed claim): "the eigenspace basis ambiguity does not affect r" for mult-2 lam_1.

(a) Multiplicity 2 is MEASURED at ~1e-10 resolution (two singular values at
noise floor; FINDINGS.md attributes doubles to a conjectured symmetry
"outside the coset action" — conjectured, not proven). A physical pair
split anywhere in (1e-25, 1e-10) makes "lam_1 to 25 digits" ill-posed as a
single number. (b) Even if exactly double, truncation perturbation ε ~ 1e-27
generically splits a double secular root by O(√ε) ~ 3e-14, and the single
normalization row a[j0]=1 selects which sheet Newton lands on — the
converged r then moves at the split scale, killing digits 14-25. The
stability cert would detect the instability but the sealed semantics would
mis-attribute it ("the arb pipeline is INDICTED" / precision unreachable),
banking a WRONG instrument fact.

## MINOR (fix at re-seal, none individually stopping)

- Sealed "n ≈ 2100-2400" is wrong for lam_1: formula gives n = 2013 (lam_2
  2103, parent 2313). Density factor 1/(2√3) itself is correct (= dual
  covolume; groundwork |μ|_min = 0.288675, SnapPy τ = 3.4641i).
- Validation gate ≥ 7 digits is sound both ways (correct pipeline agrees to
  9.7-9.9 digits given certified |Δr| ≈ 8.7e-10; nearest wrong eigenvalue
  fails instantly). Could tighten to ≥ 8; not required.
- Execution vehicle diverges from the seal: cell9_rung1.py implements a
  frozen-coefficient secant on ONE held-out row, not the sealed square-system
  Newton; P1 uses 4 points (sealed: ≥ 10) compared after collapsing to
  float64 (`abs(float(fv.real) - float(mpv))`), which cannot resolve 1e-25 —
  it passes only on exact double-rounding coincidence; P2/P3/P4, the gate,
  and the stability cert are absent from code. Code is outside the seal but
  §16 sits between seal and execution: this script may not run against this seal.

## REQUIRED CHANGES BEFORE RE-SEAL (each one line)

1. Fix the residual convention (max-normalized vector) and set the hit
   tolerance per box at 10× the propagated noise floor computed from the
   OBSERVED stability |Δr| (e.g. unnormalized: ≥ 1e-19 for λ-minpoly), and
   re-derive each box's licensed H from effective digits = certified digits
   minus the vector's log10 dynamic range.
2. Replace P3: displaced start at the midpoint of the gap to the nearest
   neighbor (e.g. parent: r=7.21) must NOT converge to any value within
   1e-20 of the target; convergence back from ±0.02 is logged, not fatal.
3. Validate Y=0.80 rise (200-point grid, min t* logged, assert t* − Y ≥
   0.05) as a banked artifact before use — or retreat to the validated
   Y=0.75 (+14% modes).
4. For lam_1: assert the SECOND singular value of the collocation matrix at
   converged r is ≤ tail bound (nullity 2 at working precision), and rerun
   with an independent normalization row asserting |Δr| < 1e-26; pre-declare
   the near-degenerate-pair outcome (splitting detected → report the pair,
   not an indictment of the pipeline).
5. Bring cell9_rung1.py into conformance with the sealed method (square-
   system Newton, P1 ≥ 10 points compared in arb/mpmath at ≥ 1e-27, P2-P4,
   gate, stability cert implemented), or re-seal the method the code
   actually implements.

Nothing above touches the target list, the certified starting values
(verified against eigenvalues_final.json to all printed digits), the
truncation formula's form, or the verdict-semantics firewall — those
premises check out.