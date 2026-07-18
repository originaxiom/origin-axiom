# TRIFOCAL VALUES REPORT — the three Ramanujan CFs at the metallic cusp parameters

B674 generation leg / `ramanujan_trifocal`. Executes the web-seat handoff as
corrected by the main-seat adjudication: golden cusp τ = 2√3·i (disc −48,
h = 2, CM — j ≠ 0), silver cusp τ = 2i (disc −16, CM), bronze leg NOT RUN
(pre-adjudicated: cusp field certified non-abelian S₄ degree 8, B675
addendum — no CM/Duke algebraicity guarantee, the bronze column of the
proposed trifocal value table cannot run as proposed).

Conventions: nome q = e^{2πiτ} (real, 0 < q < 1 at both cusps); all values
real positive; working precision dps 200 with an independent dps-320
recomputation as junk guard; PSLQ identification caps: degree ≤ 8,
|coeff| ≤ 10²⁴ (effective reliable height ceiling at degree 8, dps 200:
~10²²), maxsteps 20000. Stated candidate fields ℚ(√2,√3,√5,φ,ζ₅,ζ₆,i);
values are real, so field membership is tested as a linear factor of the
found minpoly over ℚ(√2,√3,√5). Anything that fails these gates is reported
UNIDENTIFIED — never forced. Full numbers: `values_output.txt`.

## Controls (all in-sandbox, all PASS)

- C1: j(2i) from the Eisenstein q-series = 287496 = 66³ exactly (|Δ| < 1e−192).
- C2: R(e^{−2π}) = √(φ√5) − φ to 200 digits (classical RR anchor).
- C3: adopted octic U(q) ≡ √(θ₂/θ₃) to 200 digits (two q's).
- C4: θ₂/θ₃ at e^{−2π} PSLQ → x² + 2x − 1, root **√2 − 1 = 1/δ** (the 4th
  singular value derived in-sandbox, not cited).
- C5: the handoff's literal octic product ≡ √2·q^{1/4}·η(τ)/η(4τ) to 200
  digits — it carries a bare q^{1/4}, hence is NOT a weight-0 modular
  function and has no CM algebraicity guarantee.
- C6/C7: the RR eta identity 1/R⁵−11−R⁵ = (η(τ)/η(5τ))⁶ and the cubic-CF
  eta-quotient identity verified to ~200 digits.
- C8: U(e^{−2π}) PSLQ → x⁴ + 2x² − 1, i.e. **U(e^{−2π}) = √(√2−1)** (unit).
- C9: handoff-literal octic at the anchor: UNIDENTIFIED (consistent with C5).

The guard has teeth: 13 near-cap spurious PSLQ candidates were found and
REJECTED by the dps-320 reverification (residuals ~1e−170 vs thresholds
~1e−258); 10 relations passed with residuals ≤ 1e−295.

## T1 — j at the golden cusp: EXACT

q_golden = e^{−4π√3} = 3.5263331351298313765784258778727625802079e−10.
Two Eisenstein truncations agree to working precision; cross-checked against
mpmath's kleinj (1e−185).

**j(2√3·i) = 1417905000 + 818626500·√3**
= 2835807690.4222835277298460524847570251971043651084035572131271…

Minimal polynomial (PSLQ on [1, j, j²], dps-320 residual 1.5e−295):
**H₋₄₈(x) = x² − 2835810000·x + 6549518250000** (monic; coefficient
factorizations 2⁴3⁶5⁴·389 and 2⁴3⁹5⁶11³). Conjugate-root check: j(2i/√3)
(the second form (3,0,4) of disc −48, computed independently) matches the
other root 1417905000 − 818626500√3 exactly. Exact-surd recheck at dps 320:
|Δ| = 5.2e−305 (VX5). h(−48) = 2 confirmed operationally. **j ≠ 0: the
handoff's j = 0 hypothesis is refuted** (adjudication point 1 confirmed).

## T2 — R(q_golden): UNIDENTIFIED under the stated caps

R_g = 0.012866625707817735868266114453058969166862015310374800271636532
(dps-200/320 agreement 8e−204). PSLQ deg ≤ 8 on R: spurious candidate
rejected → UNIDENTIFIED. Structured attempts: R⁵ (no relation), the level-5
eta variable t = 1/R⁵−11−R⁵ = 2835806940.4222141… (spurious rejected) →
UNIDENTIFIED. CM theory still guarantees R_g is algebraic (theory context,
not a computed fact); the computed fact is that its degree exceeds the caps
(expected: the level-5 ring class tower over disc −48; compare silver where
deg(R⁵) = 8 exactly). Explicit φ-checks: |R_g − {φ, 1/φ, 1/(2φ), φ²,
√(φ√5)−φ, 1/φ²}| all ≥ 0.27 — no φ-expression and no hearing-amplitude hit.

## T3 — V(q_golden): UNIDENTIFIED under the stated caps

V_g = 0.0007064928633617525545528992591430776276401511143081530638820143.
PSLQ deg ≤ 8 on V (spurious rejected) and on V³ (no relation) →
UNIDENTIFIED. √3/ζ₆-adjacent checks: |V_g − {√3−1, 2−√3, (√3−1)/2, 2√3−3,
1/2, √3/2}| all ≥ 0.26 — negative.

## T4 — U(q_golden): the octic leg lands (via U⁴)

Definition adjudication (the handoff's own escape clause invoked): the
literal product √2 q^{1/8}Π(1−q^{2n−1})/(1+q^{2n}) equals
√2·q^{1/4}·η(τ)/η(4τ) exactly (C5) — non-modular, so it is NOT the octic
CF's modular kernel. The unique modular sign-variant of the stated shape is
**U(q) = √2 q^{1/8} Π(1+q^{2n})/(1+q^{2n−1}) = √(θ₂/θ₃) = k(q)^{1/4}**,
adopted as the octic definition; its anchor value U(e^{−2π}) = √(√2−1) is
derived in-sandbox (C4+C8). Both variants are computed at every point; they
agree to ~3.5e−20 at golden and ~1.1e−11 at silver (VX6), so PSLQ failure on
the literal variant is consistent-with, not proof-of, transcendence — the
discriminating fact for the definition is the exact identity C5.

U_g = 0.093095870015021744307693221193904628057636279573364656305391968
= k₄₈^{1/4}. PSLQ on U and U² = √k₄₈: UNIDENTIFIED (deg ≤ 8). PSLQ on

**U_g⁴ = k₄₈ = 0.000075114133159418792211120176787673267583206010103023673583078972**,
minpoly (residual 2.8e−320, irreducible, algebraic UNIT, palindromic —
k₄₈ and 1/k₄₈ conjugate, VX4):

**x⁸ − 13320x⁷ + 92188x⁶ + 275400x⁵ + 340038x⁴ + 275400x³ + 92188x² − 13320x + 1**

No linear factor over ℚ(√2,√3,√5): k₄₈ is degree-8 algebraic outside the
stated candidate fields. So U_g is exactly algebraic (degree ≤ 32), with its
fourth power pinned at degree 8 — the p = 2 leg is the only golden leg that
lands inside the caps.

## T5 — ratios at golden: all UNIDENTIFIED

R/V = 18.211968407711303055781687971278521601883594566785832625474642
R/U = 0.13820834056055983487962246460419964557752135193107947528400234
V/U = 0.0075888743855957780291357392027025173209671918487471651221290467
PSLQ deg ≤ 8: spurious candidates rejected in all three → UNIDENTIFIED.
No banked-menu hits (T7).

## T6 — the silver cusp: fully identified through its power-variables

q_silver = e^{−4π}. The octic leg closes completely:

- **U_s = 0.29398509099253620491220742573042962548024975231697713589752431**,
  minpoly **x⁸ − 12x⁶ + 6x⁴ − 12x² + 1** (unit, irreducible);
- U_s² = √k₁₆: minpoly **x⁴ − 12x³ + 6x² − 12x + 1**; exact closed form
  proven by sympy minimal-polynomial match + 220-digit numeric identity
  (VX1): **U_s² = (2^{1/4}−1)/(2^{1/4}+1)**, i.e.
  **U_s = √((2^{1/4}−1)/(2^{1/4}+1)) = k₁₆^{1/4}**;
- U_s⁴ = k₁₆: minpoly **x⁴ − 132x³ − 250x² − 132x + 1** = exactly
  minpoly(((2^{1/4}−1)/(2^{1/4}+1))²) (VX2).
  The closed form needs 2^{1/4}: algebraic, unit, but OUTSIDE the stated
  candidate fields (2^{1/4} ∉ ℚ(√2,√3,√5,φ,ζ₅,ζ₆,i)).

RR at silver: R_s = 0.081002309675157651309972087839349591855116420038799608636123364,
itself UNIDENTIFIED at deg ≤ 8, but
**R_s⁵ minpoly (desc.): x⁸ + 286794x⁷ + 10807222x⁶ + 82016442x⁵ + 208205070x⁴ − 82016442x³ + 10807222x² − 286794x + 1**
(unit; satisfies P(x) = x⁸P(−1/x), the y ↔ −1/y RR unit structure, VX4), and
**t = 1/R_s⁵−11−R_s⁵ = (η/η₅)⁶(2i) minpoly: x⁴ − 286750x³ + 1343750x² + 50781250x + 244140625**
with constant term **244140625 = 5¹²** — the level-5 eta variable carries a
pure 5-power norm (the 5-vein shape; descriptive note only, no value claim).
VX3: the substitution lift y⁴·quart(1/y−11−y) EQUALS the R_s⁵ octic — the
two independent PSLQ results close exactly through the classical identity.

Cubic at silver: V_s = 0.015164566980325401797271841794362570977073245226720619105798468,
UNIDENTIFIED at deg ≤ 8, but **V_s³ minpoly (desc.):
2097152x⁸ − 134217728x⁷ − 354156544x⁶ − 239992832x⁵ + 29388800x⁴ + 47859712x³ − 3924928x² + 286768x − 1**
— leading coeff 2²¹, constant −1: not an algebraic integer, denominator a
pure 2-power (descriptive).

Silver-ratio checks: |U_s − (√2−1)| = 0.12, |U_s − √(√2−1)| = 0.35 — the
silver-δ quantities do NOT appear in the silver octic value itself (δ-related
numbers appear only at the anchor τ = i, which is not a cusp parameter here).

## T7 — cross-check against banked quantities: CLEAN NEGATIVE

Full table: {φ, 1/φ, 1/(2φ), φ², √5, 1/2, √3/2, √3, 2√3−3, √3−1, √2−1,
1+√2, 24, 1, √2, 2, D4-ceiling 1.7849887 (8-digit reference, near-miss-only
by construction), |h₃ roots| and their squares derived in-sandbox from the
banked minpoly 5x⁴+5x³+1 (norm check 1/5 reproduced)} × {j_g, R_g, V_g, U_g,
Uh_g, all six golden ratio orientations, R_s, V_s, U_s, Uh_s, √k₄₈, √k₁₆}:
**NO exact hits (1e−40) and NO near-misses (1e−6).** The one banked-name
appearance is structural, not positional: the octic CF's anchor value at
τ = i is θ₂/θ₃ = √2−1 = 1/δ exactly (C4) — reported as an anchor fact, NOT a
cusp-parameter hit.

## Honesty block

- Identification only via guard-verified integer minpolys (caps stated) and
  the stated fields; 15 targets returned UNIDENTIFIED and are reported so.
- UNIDENTIFIED ≠ transcendental: at CM points R, V, U are algebraic by
  theory; the computation pins what lies inside the caps (all of silver's
  power-variables; only the p = 2 leg at golden) and leaves the rest open.
- The 8-digit D4-ceiling reference cannot support an "exact hit" at 40
  digits by construction; it is flagged near-miss-only (none occurred).
- Self-audit: run 1 of the VX script misread the ascending PSLQ coefficient
  order as descending in VX3/VX4, producing a false "not divisible"; the
  contradiction with the guard-passed relations forced the recheck; corrected
  in run 2 (exact equality); run 1 preserved in `vx_run1_superseded.txt`.
- WORKING_RULES compliance notes: no git operations (cell constraint); all
  arithmetic exact/high-precision; script sha256 recorded in the output.

## Files

- `trifocal_values.py` — main computation (sha256 in values_output.txt;
  runtime 42 s).
- `vx_exact_checks.py` — exact sympy cross-checks (run 2, corrected).
- `values_output.txt` — full 60-digit values, PSLQ transcripts, VX appendix.
- `vx_run1_superseded.txt` — preserved superseded first VX append.
- `run_stdout.txt` — raw stdout of the main run.
