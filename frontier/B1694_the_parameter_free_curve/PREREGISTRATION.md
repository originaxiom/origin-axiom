# B1694 — PREREGISTRATION: THE PARAMETER-FREE CURVE (P-242) — does the one covariant Higgs with no free coefficient, at the record's canonical end, relate each sector's first-generation ratio to its second-generation ratio as nature does?

cc (main), 2026-10-21, after S164. **Sealed before `verification/the_curve.py` and `verification/compare.py` run.**
A test of a structure (B1637's value-contact checklist), not a value derived. 0 of 19.

## The question

B1691 (with its correction of S164): the weight-3/2 section ∂R is the unique covariant Higgs direction of its weight, so
it carries no free coefficient. At the canonical end radius (B1667: two horocycles, L_max ≈ 0.64–0.69 and L₂ ≈ 2.3–2.8,
functions of Im τ alone to 10⁻³), B1656's four-channel coupling gives all three masses, so (m₂/m₃, m₁/m₃) is a function
of τ alone, and eliminating τ gives a curve m₁/m₃ = F(m₂/m₃) — **with no free number**, in Λ's frame, under H-cov, with
no line (so the curve is the same for every sector). Four curves: Re τ = 0 and ½ (the CP-invariant lines) × the two
horocycles. Does a sector's measured (m₂/m₃, m₁/m₃) lie on a curve?

## Cells, predictions, priors

For each curve and sector: ρ = (m₁/m₃)_measured / F((m₂/m₃)_measured); PASS if the 3σ band of log ρ meets
[−log 3, log 3] (a factor-3 theory tolerance: B1654's formula against the exact canonical lift differed by 17–25% on
B1667's grid, the end is one of two discrete horocycles, the masses are compared at M_Z), FAIL otherwise, OUT if the
measured m₂/m₃ lies outside the curve's range. σ: the data's errors on both ratios (m₂/m₃'s through the curve's local
slope) and B1637's 10% allowance on each, in quadrature.

| cell | prediction | prior |
|---|---|---|
| **C0, the curve** | on each CP line and horocycle, m₂/m₃ decreases monotonically from about 0.2–0.3 at Im τ = 1.2 to below 10⁻³ at Im τ = 3.6, and m₁/m₃ falls faster | 85% |
| **C1, the leptons** | PASS on at least one curve | 55% |
| **C2, the up quarks** | PASS on at least one curve | 40% |
| **C3, the down quarks** | FAIL on every curve | 85% |
| **C4, the whole** | no curve passes all three sectors | 90% |

**The reading, written before the run.** If C4 holds: the program's one fully parameter-free mass relation does not
describe all three charged sectors at once in this frame; the sectors that fail need what the parameter-free case lacks
(a line, a second Higgs, a higher weight — each a choice). If a curve passed all three, it would be the first
parameter-free relation between the first and second generations' masses on the record, graded a READING (Λ, H-cov and
the weight are choices; the look-elsewhere count is four curves).

## Seen first

`VERDICT topic-sweep /near the cusp|near omega|near ω|q-expansion|residual (charge|symmetr)|exponents? (of|fixed by)|hierarch(y|ies) (from|as) (powers|exponents)|Froggatt|modular weight|discrete exponents/
(full text): 28 of 1462 arcs on main match` (B1691's sweep), and B1654 (the lift), B1656 (the four channels; the
electron's zero at ω), B1660 (the one-Higgs census at ω, NEGATIVE: fitted L, a free Higgs), B1667 (the canonical end),
B1691–B1693. None tests a curve with no free number. **Literature:** the Gatto–Sartori–Tonin and Georgi–Jarlskog
relations as the classical first-to-second-generation patterns (context, not tested).

## Disclosed

- **Seen before the seal (main's, this session).** The curve's first points were computed while exploring (∂R, no line,
  L = 2.5: (m₂/m₃, m₁/m₃) = (0.183, 4.9 × 10⁻⁴), (0.038, 6.5 × 10⁻⁵), (0.0082, 5.3 × 10⁻⁶) at Im τ = 1.5, 2, 2.5) and
  set beside recalled running masses (m₁/m₃: up ≈ 7 × 10⁻⁶, down ≈ 1 × 10⁻³, leptons ≈ 2.8 × 10⁻⁴): roughly the leptons
  within a factor 2, the up quarks about 5, the down quarks about 50 off. The priors are informed by this. The seal fixes
  the curves' construction (both horocycles, both CP lines), the tolerance and the uncertainty treatment.
- **The data file** is B1637's pinned transcription, read in B1693; its m₁ values were not read in this arc before the
  seal.
- **The scope.** One section (∂R), no line, no second Higgs; L from B1667's column at Re τ = 0.25.

## Instruments

`verification/the_curve.py` (no data) → `the_curve.json`; `verification/compare.py` (the comparison); B1656's functions
copied verbatim (`verification/b1656_funcs.py`); hashes in `ARTIFACT_HASHES.txt`.
