# Erratum 1: RK4 Discretization Refinement in `REF-A1` (`referee_a2_ow19.py`)

In sealed run `ef9300e61` (script `ee35bc6f9`), every cross-check against `A2-PEER-SYNTH v2` (`c161ef045`) and `A2-OW19 v3` (`62f08b148`) passed (`REF-0`, `REF-PS`, `REF-A2`, `REF-A3`, `REF-B`, `REF-C`, and `6 / 6` `REF-D` planted faults), including:
- `c_star_diff_vs_ow19 = 5.30e-12` (`< 1e-10`), `bc_diff_vs_ow19 = 2.37e-8` (`< 1e-7`), `curv_err = 4.93e-11` (`< 1e-8`);
- `gauss_bonnet_err = 9.42e-5` (`< 1e-3`), `K_e2_max_diff_vs_ow19 = 1.71e-4` (`< 2e-3`), `K_cim_eigs_max_diff_vs_ow19 = 3.07e-4` (`< 2e-3`).

However, `REF-A1`'s internal referee-side RK4 discretization checks tripped three self-consistency gates strictly due to step-size truncation in the referee's own RK4 integrator:
1. `tr_comm_err = 2.23e-12` and `max_im_R = 4.10e-12` (vs strict internal gate `< 1e-12`) from `na_fine = 192, nb_fine = 288` (`O(h^6)` Richardson-RK4 error on the $b$-cycle passing within $0.5$ of $z = 0$).
2. `per_1_err = 3.63e-8` and `per_tau_err = 1.15e-7` (vs strict internal gate `< 1e-10`) from non-Richardson 4th-order RK4 along the periodicity path passing within $0.3$ of the double pole $z = \tau_r$.

**Remediation (zero tolerance relaxation, zero change to any target):**
- Warm-start Newton-Raphson on `(96, 144)` Richardson-RK4, then polish on `(384, 576)` Richardson-RK4 (reducing `O(h^6)` monodromy truncation by `2^6 = 64x`, bringing `tr_comm_err` and `max_im_R` below `1e-13`).
- Apply Richardson step-halving (`(16 * M_{2N} - M_N) / 15`) to the `REF-A1` periodicity verification segments (`per_1_err`, `per_tau_err`) and refine the `rk4_log_cusp_mp` inward cusp integration (`320, 480` steps).

`0 of 19`.
