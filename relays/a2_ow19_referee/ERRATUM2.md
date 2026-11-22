# Erratum 2: Richardson-RK4 on Path `v0 -> z_mid -> z1` in `REF-A1` (`referee_a2_ow19.py`)

In sealed run `cc1f9b6dd` (script `884076890`), `REF-0`, `REF-PS`, `REF-A2`, `REF-A3`, `REF-B`, `REF-C`, `REF-D` (`6 / 6`), and all `REF-A1` monodromy/cusp/curvature gates passed (`c_star_diff = 1.63e-13`, `tr_comm_err = 6.68e-14`, `max_im_R = 1.26e-13`, `curv_err = 4.93e-11`, `bc_diff = 4.87e-10`), leaving ONLY `per_1_err = 3.65e-8` and `per_tau_err = 1.14e-7` unchanged from run `ef9300e61`.

**Root cause:** Lines 817–818 (`v0 -> z_mid -> z1`) still used non-Richardson 4th-order `rk4_segment_mp(..., 120, ...)`, injecting a complex `O(h^4) ~ 3.6e-8` error matrix `I + E` into `psi_z1 = M_exact(v0 -> z1) P (I + E)`. Under exact period translation `z1 -> z1 + 1`, the monodromy of `psi_z1` becomes `(I + E)^{-1} R_a (I + E)`, inheriting an `O(Im E) ~ 3.65e-8` imaginary part independent of the integration accuracy on `z1 -> z1 + 1`.

**Remediation (zero tolerance relaxation):** Apply `rk4_seg_rich(..., 160, ...)` to `v0 -> z_mid -> z1` as well.

`0 of 19`.
