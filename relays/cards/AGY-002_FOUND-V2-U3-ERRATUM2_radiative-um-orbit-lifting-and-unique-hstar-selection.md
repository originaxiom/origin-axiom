# Erratum `2` to Card `AGY-002_FOUND-V2-U3` — Radiative `U_M`-Orbit Lifting & Unique `h_*` Selection (`0 of 19`)

## 1. Immutable History

- Original Card (`2a7447548`), `v1` (`53d240cbc`), Erratum `1` (`f8d66057b`), and `v2` (`e56653dc7`) remain immutable in git history.
- `e56653dc7` halted on Clarification `2`'s assumption that the `6` projective rays $\{[U_M^k h_*]\}$ take identical values in `V_box`: at fixed $\tau \in \{13/100 + 17/10\,i,\; 13/100 + 6\,i\}$ (`not fixed by [T, S] in SL_2(Z)`), `V_box` **radiatively lifts** the `6`-ray `U_M` degeneracy (`orbit_6_spread_box > 20` at `y = 17/10` and `> 200` at `y = 6`) and **uniquely selects $h_*$ (`idx == 0`)**.

## 2. Exact Companion `v3` & Referee Expectations

1. **Retained (`Erratum 1` Clarification `1`):** `um_signed_vector_count == 12` (`S^3 subset E`) and `um_projective_ray_count == 6` (`CP^5`, under `U_M^6|_E = -I_E`).
2. **Supersedes Clarification `2` of `Erratum 1` (`Unique Radiative Selection of h_*`):**
   - At `y = 17/10`: `B_box(v_+) > 15`, `B_box(v_-) > 15`, `orbit_6_spread_box > 20`, `halfstep_barrier_box > 1`, `box_circ_min_idx == 0`, `s3_box_argmin == (4, 0)` (`unique 216-pt S^3 minimum at h_*`), `V_cw_muE(v_+) - V_cw_muE(h_*) < -40`, `V_det(h_*) - min_{circle} V_det > 60`.
   - At `y = 6`: `B_box(v_+) > 100`, `B_box(v_-) > 15`, `orbit_6_spread_box > 200`, `halfstep_barrier_box > 40`, `box_circ_min_idx == 0`, `V_cw_mu1(v_+) - V_cw_mu1(h_*) > 150`, `cw1_circ_min_idx == 0`, `V_cw_muE(v_+) - V_cw_muE(h_*) < -200`, `V_det(h_*) - min_{circle} V_det > 250`.

## 3. Firewall

Strict `0 of 19`; `v1` (`53d240cbc`) and `v2` (`e56653dc7`) remain unmodified.
