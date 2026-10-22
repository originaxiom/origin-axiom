# B1712 — PREREGISTRATION: THE WEAVE CENSUS OF LINES (P-260) — with every flat line of exact order 8–12 (all splitting the three charged sectors), the end-data Higgs ∂R and Im τ free, does any line give the six charged-fermion ratios, specifically, once the look-elsewhere is counted?

cc (main), 2026-10-22, at the owner's choice of 2026-10-22 ("Weave census of lines", after B1711). **Sealed before
`verification/the_line_census_masses.py` and `verification/compare.py` run.** A test of a structure, not a value derived.
0 of 19.

## Why

The record's selected lines both failed in this frame: the tick's order-5 lines (B1698: best 2.33, but d = e) and W59's
order-9 lines (B1711: best 4.17, 9.8% of random hierarchies as good). B1703: every line of order ≥ 8 splits all three
sectors, and nothing on record selects among them. The SM seat's weave form of W73 (its relay §196): take every order
N ≥ 8 up to a stated bound together, none hand-picked. P-260 does that, with the bound N ≤ 12 (W88's range).

## The model and the cells

Every line w = ατ + b of exact order 8 ≤ N ≤ 12, up to sign (w and −w give the same spectra in every sector: B1703's law,
checked before the seal on two lines to 5 × 10⁻¹⁴): **204 lines** (24, 36, 36, 60, 48 of orders 8–12); the section ∂R;
B1667's canonical end; B1656's coupling; Re τ ∈ {0, ½}, Im τ = 1.5–3.5 (step 0.1); both horocycles; three up readings:
one continuous number on a grid, 204 × 2 × 6 = 2 448 discrete choices. The calibration fits each random target with the
same 51 408 rows, so the look-elsewhere count is inside H2.

| cell | prediction | prior |
|---|---|---|
| **H1** | some point puts all six ratios within a factor of 3 | 55% |
| **H2, specific** | at most 1% of 4 000 random hierarchical target sets (B1695's prior) fit at least as well | 3% |
| **H3** | the minimum χ² is below 16.75 | 3% |

Read-outs: the best point and its line's order; the best per order; d and e at the best point.

**The reading, written before the run.** If H2 holds: some line of order 8–12 with the end-data Higgs fits the six ratios
better than random hierarchies even with the whole census counted — then the line's order and its coordinates become
the question, graded a READING (Λ, the unit, H-cov in R's module, the census's 2 448 choices tagged), to be attacked first
by a principle that would select that line and by an independent route. If H2 fails: no flat line of order ≤ 12 gives the
masses specifically in this frame; the line is not where the frame's missing number lives.

## Seen first

`VERDICT topic-sweep /line census|every (line )?order|orders? 8|W73|weave form|look.elsewhere/ (full text): 81 of 1483 arcs on main match (NEGATIVE 25, OPEN 2, PROVED 54)` — B1656 (W73's per-sector lines), B1698, B1703, B1711 and the SM seat's relays §195–§196 (the weave form). None
tests the census against data. **Literature:** none beyond the cited arcs.

## Disclosed

- **Known before the seal.** The six measured ratios; B1694–B1711's results (best factors 2.33 on order 5, 4.17 on order
  9; the up quarks' floor at Im τ = 2); B1703's laws.
- **Model values on these lines seen before the seal:** the sign check computed all six ratios on two of the lines,
  (3/11, 5/11) and (1/8, 3/8), at τ = 0.37 + 2.2 i (off this test's grid), at L_max, and compared them only between w
  and −w; B1703's census JSON holds unread values for every line of order ≤ 16 at three off-grid τ.
- The instruments import-tested before the seal (no computation beyond the sign check above).

## Instruments

`verification/the_line_census_masses.py` (no data) → `the_line_census_masses.json`; `verification/compare.py` (as
B1711's) → `comparison.json`; B1656's functions copied verbatim; hashes in `ARTIFACT_HASHES.txt`.
