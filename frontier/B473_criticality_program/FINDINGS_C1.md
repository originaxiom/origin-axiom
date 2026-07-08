# B473 C1 — first pass: the collapse prediction fires at (1,3), and the second control catches the confound

**Numeric-exact first pass (`c1_seam_controls.py`); prereg'd predictions adjudicated
honestly. The gate: the (1,2) critical seam's architecture reproduces (121 cells, ~39
distinct magnitudes, 59.5% zeros).**

| pair | level | κ | seam profile |
|---|---|---|---|
| (1,2) critical | 15 = 3·5 | −2 | RICH: ~39 distinct values, 59.5% zeros |
| (1,3) off-critical | 27 = 3³ | −34 | **COLLAPSED: ~2 distinct magnitudes** (≈ 1/12, √3/12 — one surviving character) |
| (2,3) off-critical | 63 = 3²·7 | **−34 (the same!)** | RICH: ~105 distinct values, 33.3% zeros |

**The adjudication**: P-C1 ("off-critical seams collapse") fires at (1,3) and FAILS at
(2,3) — and the two controls share κ exactly (mn(n−m) = 6 for both: equal squares, equal
tears). **The seam architecture is driven by the LEVEL's prime factorization** (number of
available quadratic characters: 27 has one, 15 and 63 have several), **not by κ.** The
criticality question is therefore NOT answered by architecture richness; it moves to the
finer registers: the selection-rule/field comparison of the two rich seams ((1,2) vs
(2,3)) and the spectral cell C2. This is the control system working: the confound
(level arithmetic vs criticality) was separated BEFORE the narrative banked. Exactness
upgrade (the 4-channel decomposition of the (2,3) seam at ζ₂₅₂...) = the next C1 wave.
