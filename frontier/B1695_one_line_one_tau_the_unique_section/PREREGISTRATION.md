# B1695 — PREREGISTRATION: ONE LINE, ONE τ, THE UNIQUE SECTION (P-243) — can the weight-3/2 covariant Higgs ∂R, at the canonical end, with one flat hypercharge line and one τ shared by the three charged sectors, give all six measured mass ratios?

cc (main), 2026-10-21, after S165. **Sealed before `verification/the_grid.py` and `verification/compare.py` run.** A test
of a structure (B1637's checklist), not a value derived. 0 of 19.

## The question

B1694 (sealed): with no line, the parameter-free curve passes the up quarks on every curve and the leptons on three of
four, but no curve passes all three sectors, and each sector sat at its own τ. One fibre has one τ; what splits the
sectors in this frame is a flat hypercharge line (B1653, B1656; B1692: the line splits the sectors' m₂/m₃ by factors up to
four and changes their first-generation channel). So: one τ, one line w = α τ, the section ∂R (no free coefficient),
B1667's canonical end — six ratios (m₂/m₃ and m₁/m₃ for up, down, leptons) from two continuous numbers (α, Im τ) and
discrete choices (Re τ ∈ {0, ½}; the horocycle; B1660's three readings of the up sector).

## Cells, predictions, priors

χ² over the six log-ratios with σ² = the data's relative errors² + (B1637's 10%)²; the grid α = j/96 (j = 0…48),
Im τ = 1.5–3.5 (step 0.05), β = 0.

| cell | prediction | prior |
|---|---|---|
| **G1, strict** | FAILS: the grid's minimum χ² is above 14.86 (4 degrees of freedom at 99.5%, an allowance for the 12 discrete choices) | 85% |
| **G2, tolerant** | FAILS: no grid point puts all six ratios within a factor of 3 | 65% |

Read-outs (no criterion): the best point per choice, its six ratios, the worst miss.

**The reading, written before the run.** If both fail: in this frame the unique section with one line and one τ does not
give the six charged-fermion ratios; what the data need beyond it is a further choice (a second Higgs, a higher weight,
another line per sector), each adding free numbers. If G2 passes and G1 fails: the frame reproduces the six ratios to the
factor-3 accuracy of its own approximations but not to the data's precision — a near-miss, graded a READING (Λ, H-cov,
the weight, the line and the horocycle are choices; the look-elsewhere count is 12 discrete choices × the grid). If G1
passes: a parameter-free fit of six ratios by two numbers, graded a READING with the same count; the strongest
structural result on the record, to be attacked before anything else.

## Seen first

`VERDICT topic-sweep /Georgi|Jarlskog|d.e wall|down quarks? (from|and) (the )?(charged )?leptons|cross.sector|two Higgs|2HDM|H_u|second.to.third|2.3 hierarch/
(full text): 37 of 1464 arcs on main match` (B1693's sweep), and B1660 (the one-Higgs census at ω on W59's lines with a
free Higgs and a fitted L: NEGATIVE, χ² 34.4 at best), B1656 (the twisted frame), B1691–B1694. None fits the six ratios
with the unique section at the canonical end near the cusp. **Literature:** none beyond B1694's.

## Disclosed

- **What main knows before the seal.** The six measured ratios (B1693, B1694 printed them: m₂/m₃ = 0.00368, 0.0187,
  0.0589; m₁/m₃ = 7.0 × 10⁻⁶, 9.4 × 10⁻⁴, 2.8 × 10⁻⁴ for up, down, leptons); B1694's misses (the down quarks and the
  leptons in opposite directions without a line); B1692's line factors for m₂/m₃. The grid's model values have not been
  computed (one point was timed, its values not printed). The priors are informed by B1694.
- **β = 0 only** (B1692: the line's real part never moved m₂/m₃; its effect on m₁ is not checked); the grid is a grid,
  so a FAIL is a statement about it, and a near pass would be refined in a post-seal step, labelled.

## Instruments

`verification/the_grid.py` (no data) → `the_grid.json`; `verification/compare.py` → `comparison.json`; B1656's functions
copied verbatim (`verification/b1656_funcs.py`); hashes in `ARTIFACT_HASHES.txt`.
