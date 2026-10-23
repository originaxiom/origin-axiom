# Exploration before commit (chat1, 2026-10-23, the attack's reconnaissance)

**Labelled.** These scripts were written and run in chat1's working area **before** any commit, while the attack was
being designed; they are committed here as they ran, with only their file paths made repository-relative. Their outputs
were read when printed. They are not tests and carry no cell; where one compares with data it is post hoc on grids
already compared with data (the zero-free census, TWO_HIGGS's grid, and the rows B1735, P-344 and TWO_HIGGS named).
`*_out.txt` beside each is a re-run of the committed script, made for the record after the commit.

| script | kind | what it does |
|---|---|---|
| `explore_dirs.py` | data-free | the record's Higgs directions on ρ(T)'s eigenlines (e₁, the null h₀ = (0, 1, i)/√2 and its conjugate) at four τ |
| `explore_rows.py` | post hoc rows | B1736's closed form checked against `coupling()`; the left states' geometry at TWO_HIGGS's best six-row, B1735's row and P-344's nine-best row |
| `g1_det.py` | data-free | det Y = (h·h)(u·h)(u·u + w²) by sympy (B1659's J1 in B1736's vector form) |
| `g2_light.py` | data-free | the first-order tilt of the light left state (β, γ), against SVD on 2 000 random draws |
| `g3_quartet.py` | data-free | V_cb and the m₂/m₃ under every null-led Higgs at five points |
| `e_common.py` | helper | the pinned targets (B1720's χ² definition) and a nine read-out |
| `e1_vcb_map.py` | post hoc | V_cb's spread over the null-led Higgs on the zero-free census; aligned two-Higgs six with the channel V_cb |
| `e4_nine_pairs.py` | post hoc | the nine recomputed at the best aligned pairs' rows |
| `e5_dr_pairs.py` | post hoc | the same with DR in one or both sectors |
| `e6_bands.py` | post hoc | the stored diagonal aligned rows' best nine by Im τ band |
| `e7_vcb_spread.py` | data-free | V_cb's spread on hierarchical rows by Im τ band |
| `g4_departures.py` | data-free | the record forms' departures from their leading null line, in units of r^½ and r |
| `g5_vcb_formula.py` | data-free | V_cb under the null Higgs against \|κ_u − κ_d\| at eight points |
| `g6_maass.py` | data-free | DR = qR′ + E₂R/24 (fit); R·DR = 0; the pencil DR + λR's departures |
| `g7_canonical.py` | data-free | the canonical matrix of §1.1 against F†YF on 200 random draws |
