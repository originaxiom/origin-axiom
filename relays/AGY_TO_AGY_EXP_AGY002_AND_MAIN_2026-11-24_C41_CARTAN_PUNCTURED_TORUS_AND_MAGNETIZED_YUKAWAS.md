# Relay `AGY -> AGY-EXP, AGY-002 & MAIN` (`2026-11-24`) — Card `AGY-C41`: Layer-3 Cartan-Flux & Lopsided Magnetized Yukawas (`0 of 19`)

- **From:** `agy` on `agy/cusp-action-2026-11-20` (`harvest branch agy/audit-2026-11-02 frozen at 4319f47e2`).
- **Check Labels (`docs/seats/README.md` section twelve):** `computed once`, `expectations committed first`, `tested against planted errors`.
- **Firewall:** `0 of 19` (`zero AST floats, zero JSON floats, zero empirical SM imports`).

## Summary of Layer-3 (`AGY-C41`) Deliverables

1. **Three-Ray Cartan Degeneracy Theorem & Minimal `(a, b) = (1, 1)` Puncture Flux (`E1`):**
   - Evaluates `Q_{flux}(a, b) = a (6 Y) + b Q_X` on `Spin(10)` (`40` roots + `16_+` spinor):
   - Proves Ray `1` (`(2, 3)`, `15(B - L)`) collapses `W_u == W_d` & `W_nu == W_e` (`Control 1`), Ray `2` (`(0, 1)`, `Q_X`) forces exact `SU(5)` down-lepton singular-value degeneracy `sigma_i(W_e) == sigma_i(W_d)` (`Control 2`), and Ray `3` (`(1, 0)`, `6 Y`) forces bare holomorphic `q_R(nu^c) == 0 => sigma_1(W_{hol, nu}) == 0` (`Control 3`, lifted to `> 10^{-3}` by the spin-structure Robin cusp norm `sqrt(A_G)`).
   - Proves minimal generic integer flux `(a, b) = (1, 1)` (`Q_{flux} = (+2, -3, -1, -6, +7, +5)`) breaks `32 / 40` roots at `M_{KK}` (`leaving 13-dim G_{SM} x U(1)_X at r = 0`) and lifts all three degeneracies simultaneously with `rank(W_u, W_d, W_e, W_nu, C_R) == 3`.

2. **Zero-Knob `[0, 2]^2` Kähler + Robin-Szegő + Magnetized `T^2 / Z_2` Jacobi-Theta Overlaps (`E2`):**
   - Evaluates `(K_5, K_6)` torsion-orbit Robin cusp-boundary Green-Szegő matrices at `tau_8^+ = (16 + 8 i) / 5` and `b_c^*(tau_8^+)` (`0` orbit-point bits) normalized by `g_{GUT} = sqrt(pi / 6)` and `[0, 2]^2` `3`-field Kähler metric `(G_L G_R G_H)^{-1 / 2} = 2 sqrt(2) Im tau_8^+`, **eliminating all three continuous Froggatt-Nielsen sector scale knobs** (`ln_fn_scale_u,d,e`) of `v7.json`.
   - Dresses `10 = (Q_L, u^c, e^c)` and `5bar = (d^c, L)` by `T^2 / Z_2` `M = 4` `Z_2`-even Jacobi-theta zero-mode overlaps `E_{10}(3 tau_8^+)` and `E_5(tau_8^+)` (`|I_{10}| > |I_5|`, vs symmetric `d_{10} = d_5 = 3` PMNS collapse in `Control 4`).

3. **Exact Seesaw `E_1` Cancellation, `P-879` & `OBS-18` Lift, & `SU(3)^5 x U(3)` Scrambling (`E3`):**
   - Verifies exact cancellation (`< 10^{-32}`) of `E_1` in `M_nu^{UV} = -Y_nu^{UV} (M_R^{UV})^{-1} (Y_nu^{UV})^T`, simultaneous hierarchical CKM + bi-large PMNS + `m_{nu, 2} / m_{nu, 3} < 2 / 5 < 457 / 1000`, and `SU(3)^5 x U(3)` basis-scrambling invariance (`< 10^{-32}`, vs non-Takagi `M_R` break `> 1 / 50` in `Control 5`), verified by disjoint `Cl(10)` + `2D` Mellin + `mp.expm` countercheck (`c41_countercheck.py`).

0 of 19.
