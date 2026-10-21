# B1698 — PREREGISTRATION: THE ORDER-5 LINES (P-248) — with the flat line at one of the eight lines the tick fixes up to sign, the end-data Higgs ∂R and one continuous number (Im τ), do the six charged-fermion ratios come out, specifically?

cc (main), 2026-10-21, after S169 (B1697, the scan for misses). **Sealed before `verification/the_order5_lines.py` and
`verification/compare.py` run.** A test of a structure (B1637's checklist), not a value derived. 0 of 19.

## Why

The scan (B1697, item 3) found what the newest fits never imposed: the tick fixes no non-zero flat line (det(LR − I) = −1)
but exactly four lines up to sign — charge conjugation — all of order 5 (det(LR + I) = 5; B591, B489; the SM seat's row
1209). On a line w = α τ + b the moves act as L: (α, b) ↦ (α, b − α) and R: (α, b) ↦ (α − b, b) (derived here from
τ ↦ τ + 1 and τ ↦ τ/(τ + 1)); the sign-fixed sets are S₁ = {(1/5, 2/5), (2/5, 4/5), (3/5, 1/5), (4/5, 3/5)} for L·R and
its swap S₂ for R·L. The line becomes a discrete datum the tick supplies; the fits' continuous α (B1695, B1696) landed
beside 2/5 with b = 0.

## The model and the cells

Each of the eight lines; the section ∂R (one unit of end data on v₊; B1697's scope); B1667's canonical end; B1656's
four-channel coupling; Re τ ∈ {0, ½}, Im τ = 1.5–3.5 (step 0.02) — **one continuous number** — and the discrete
choices: 8 lines × 2 Re τ × 2 horocycles × 3 up readings = 96.

| cell | prediction | prior |
|---|---|---|
| **H1** | some point puts all six ratios within a factor of 3 | 40% |
| **H2, specific** | at most 1% of 4 000 random hierarchical target sets (B1695's prior) fit at least as well | 8% |
| **H3** | the minimum χ² is below 16.75 | 3% |

Read-outs: the best point; the best worst-factor per line; whether the best line contains α = 2/5.

**The reading, written before the run.** If H2 holds, the tick's own order-5 lines with the end-data Higgs reproduce the
six ratios better than random hierarchies with one continuous number — the strongest structural result on the record,
graded a READING (Λ, H-cov with end data on v₊, the weight and 96 discrete choices tagged, inside the calibration), to be
attacked first: by β's role at the canonical end, by the unit-free Higgs, by an independent route. If H2 fails, the
tick's lines do not select the line in this frame.

## Seen first

`VERDICT topic-sweep /order.?5|five.torsion|5.torsion|fixed up to sign|det\(LR ?\+ ?I\)|charge conjugation|closing lines|closes around/ (full text): 37 of 1469 arcs on main match (NEGATIVE 4, PROVED 33)` — and B1697's scan (its item 3: B591, B489, B1438, B1444, the SM seat's rows 1209–1213); none tests the
order-5 lines against masses. **Literature:** none beyond the cited arcs.

## Disclosed

- **Known before the seal.** The six measured ratios; B1694–B1696's results; that B1695's (α = 37/96) and B1696's
  (75/192) best lines lie beside 2/5 with b = 0. No model value on any order-5 line has been computed.
- **The identification of the line's coordinates** (α the coefficient of τ, b = β/2) follows B1656's convention; both
  composition orders (S₁, S₂) are included rather than chosen.
- **The Higgs carries end data on v₊** (∂R), the assumption B1697 made explicit (P-245).

## Instruments

`verification/the_order5_lines.py` (no data) → `the_order5_lines.json`; `verification/compare.py` (the comparison and the
calibration) → `comparison.json`; B1656's functions copied verbatim; hashes in `ARTIFACT_HASHES.txt`.
