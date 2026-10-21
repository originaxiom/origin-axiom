# B1702 — PREREGISTRATION: THE OTHER CUSP SHAPES (P-249) — with the weave's τ at the silver word state's cusp shape 2i or at the golden word's spin end curve ½ + √3 i, the end-data Higgs ∂R and any line of order dividing 24, do the six charged-fermion ratios come out, specifically?

cc (main), 2026-10-22, after S173 (B1701). **Sealed before `verification/the_cusp_shapes.py` and `verification/compare.py`
run.** A test of a structure (B1637's checklist), not a value derived. 0 of 19.

## Why

The scan for misses (B1697, item 5) found two τ-candidates the record carries and no test used: the silver word state's
cusp shape, τ = −2i exactly (B675; 2i up to orientation, SL₂(ℤ)-equivalent to SnapPy's 0.5 i), in the hierarchy band;
and the golden word's spin structures' end curves (B1483: −½ + √3 i and 4√3 i). B1696 tested the tick's own shape
2√3 i (NEGATIVE). P-249 tests the others in the same frame.

## The model and the cells

τ ∈ {2i, ½ + √3 i} (the second is −½ + √3 i moved by τ ↦ τ + 1; the line grid is closed under the moves); every flat line
w = α τ + b with (α, b) = (j/24, k/24), j, k = 0…23 (576 lines); the section ∂R (B1700: the unit's member with R's own
end condition); B1667's canonical end (both horocycles); B1656's four-channel coupling; B1660's three up readings. No
continuous number: 2 × 576 × 6 = 6 912 discrete choices. 4√3 i lies beyond B1667's canonical end (Im τ ≤ 4) and is not
tested; at large L the section gives m₂/m₃ ≈ 6 × 10⁻⁹ there (B1697), far below every sector's.

| cell | prediction | prior |
|---|---|---|
| **H1** | some τ, line and choice puts all six ratios within a factor of 3 | 12% |
| **H2, specific** | at most 1% of 4 000 random hierarchical target sets (B1695's prior) fit at least as well | 3% |
| **H3** | the minimum χ² is below 16.75 | 1% |

Read-outs: the best per τ; the best overall; the calibration's quantiles.

**The reading, written before the run.** If H2 fails: the other cusp shapes on record do not select τ in this frame, and
with B1696 no cusp shape of the record's word states does — P-249 closes for this frame. If H1 holds and H2 fails: a near
miss, recorded as such. If H2 holds: a cusp shape of the record would carry the masses' τ, graded a READING (Λ, the unit,
H-cov in R's module and 6 912 discrete choices tagged, inside the calibration), to be attacked first by the remaining
word states' shapes and an independent route.

## Seen first

`VERDICT topic-sweep /silver word state|silver cusp|silver's cusp|spin end curves?|end curves? of the spin|the spin structures' end/ (full text, aliases: the point i): 201 of 1473 arcs on main match (NEGATIVE 48, OPEN 7, PROVED 146, RETRACTED 2)` —
the alias table reads "silver" as the point i, so the sweep is broad; the arcs that bear: B675 (the silver cusp lattice,
τ = −2i), B485 (the metallic family), B1483 (the spin structures' end curves), B1696 (the tick's shape as τ, NEGATIVE),
B1697 (item 5: never tested). None tests these shapes as the weave's τ against masses. **Literature:** none beyond the
cited arcs.

## Disclosed

- **Known before the seal.** The six measured ratios; B1694's curve without a line (m₂/m₃ ≈ 0.038 at Im τ = 2, L = 2.5;
  ≈ 0.18 at 1.5) and B1692's line factors (up to about four) — the priors are informed by them; B1697's large-L values
  at these τ (∂R: m₂/m₃ ≈ 0.034 at 2i by 18∣q∣^{1/2}; 0.079 at −½ + √3 i). No value of this model at these τ has been
  computed.
- The instrument was import-tested before the seal (no computation), after B1699's first run failed at import.
- B1698's criterion is known: lines of order dividing 4 or 5 leave d and e degenerate; the grid contains lines of order
  dividing 24 (including 3, 6, 8, 12, 24, which split them).

## Instruments

`verification/the_cusp_shapes.py` (no data) → `the_cusp_shapes.json`; `verification/compare.py` (the comparison and the
calibration) → `comparison.json`; B1656's functions copied verbatim; hashes in `ARTIFACT_HASHES.txt`.
