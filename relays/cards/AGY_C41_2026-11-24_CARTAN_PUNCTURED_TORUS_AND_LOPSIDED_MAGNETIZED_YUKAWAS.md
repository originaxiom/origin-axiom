# Card `AGY-C41` — Layer 3: Cartan-Flux Punctured-Torus & Lopsided Magnetized Yukawas (`0 of 19`)

- **Seat / Branch:** `agy` on `agy/cusp-action-2026-11-20` (`origin/agy/audit-2026-11-02` untouched at `4319f47e2`).
- **Empirical Firewall (`docs/seats/README.md` section nine):** `0 of 19` — strictly data-free; zero empirical Standard-Model or experimental constants imported.
- **Section-Twelve Check Labels (`docs/seats/README.md` section twelve):** `computed once`, `expectations committed first`, `tested against planted errors`.

## Purpose & Layer-3 Role in the Top-Down Synthesis

Layer `1` (`AGY-C39`) fixed `D = 4`, `X_7 = m004 x (C^2 / 2T)`, and native rank-`16` `E_8^{(1)} x E_8^{(2)}`, and Layer `2` (`AGY-C40`) stabilized `tau_*^+ = (2 + i) / 5` (`tau_8^+ = (16 + 8 i) / 5`), `alpha_{GUT}^{-1} = |2T| = 24`, and `M_0 / M_{GUT} = exp(-16 pi / 5)` with unbroken `4D N = 1` supersymmetry.

Layer `3` (`AGY-C41`) constructs the complete ultraviolet `3 x 3` Yukawa and Majorana seesaw operators `(Y_u^{UV}, Y_d^{UV}, Y_e^{UV}, Y_nu^{UV}, M_R^{UV})` at `tau_8^+` with **zero continuous Froggatt-Nielsen sector scale parameters** (`eliminating all three continuous knobs ln_fn_scale_u, ln_fn_scale_d, ln_fn_scale_e of v7.json`).

## Pre-Committed Mathematical Expectations (`E1`–`E3`)

1. **`E1` — Three-Ray Cartan Degeneracy Theorem & Minimal `(a, b) = (1, 1)` Root Breaking (`r = 0`):**
   - On the `Spin(10)` chiral spinor `16_+ = (Q_L, u^c, d^c, L, e^c, nu^c)` and `40` roots (`built via 5 x 5 Bourbaki D_5 Weyl-BFS`), evaluate quantized puncture Cartan fluxes `Q_{flux}(a, b) = a (6 Y) + b Q_X` (`with Q_X = 5 (B - L) - 4 Y = (+1, +1, -3, -3, +1, +5)` and `6 Y = (+1, -4, +2, -3, +6, 0)`):
   - **Ray `1` (`(a, b) = (2, 3)`, `Q_{flux} = 15 (B - L)`):** Preserves `10` roots (`dim G_{LR} = 15`) and collapses `||W_u - W_d||_F == 0` & `||W_nu - W_e||_F == 0` (`V_{CKM} = I_3`, **Control `1`**).
   - **Ray `2` (`(a, b) = (0, 1)`, `Q_{flux} = Q_X`):** Preserves `20` roots (`dim SU(5) x U(1)_X = 25`) and forces exact `SU(5)` transpose singular-value degeneracy `max_i |sigma_i(W_e) - sigma_i(W_d)| < 10^{-40}` on `(K_5, K_6)` (**Control `2`**).
   - **Ray `3` (`(a, b) = (1, 0)`, `Q_{flux} = 6 Y`):** Sets `q_R(nu^c) == 0`, forcing `sigma_1(W_{hol, nu}) < 10^{-40}` on the bare holomorphic kernel (`rank < 3`, **Control `3`**), while the spin-structure-dependent Robin cusp norm `sqrt(A_G)` lifts `sigma_1(W_{Sz, nu}) > 10^{-3}` (`leaving Rays 1 & 2 unbroken until a, b != 0`).
   - **Minimal Generic Flux `(a, b) = (1, 1)` (`Q_{flux} = 6 Y + Q_X = (+2, -3, -1, -6, +7, +5)`):** Breaks `32 / 40` roots at `M_{KK}` (`r = 0`), leaving `8` roots + `5` Cartans (`13`-dim `G_{SM} x U(1)_X`), while lifting all three ray degeneracies simultaneously (`||W_u - W_d||_F > 1 / 100`, `|det W_e - det W_d| / |det W_d| > 1 / 2`, and `rank(W_nu) == rank(C_R) == 3`).

2. **`E2` — Zero-Knob `[0, 2]^2` Kähler Normalization, Robin-Szegő Kernel, & Magnetized Jacobi-Theta Overlaps:**
   - Evaluate the `(K_5, K_6)` torsion-orbit Robin cusp-boundary Green-Szegő Yukawa matrices `W_f^{(1, 1)}(tau_8^+)` and symmetric Majorana kernel `C_R^{(1, 1)}(tau_8^+)` at exact `b_c^*(tau_8^+)` (`0` orbit-point selection bits by `p ~ -p` antipodal symmetry), normalized by `g_{GUT} = sqrt(pi / 6)` and `[0, 2]^2` spin-cover `3`-field Kähler metric `(G_L G_R G_H)^{-1 / 2} = 2 sqrt(2) Im tau_8^+` (`verified via Poisson-Gaussian integral < 10^{-40}`, with `0` continuous Froggatt-Nielsen sector knobs).
   - Construct the magnetized `T^2 / Z_2` `M = 4` `Z_2`-even zero-mode Jacobi-theta overlap matrices `E_F(d_F tau_8^+) = diag(|theta[1/2, 0](0 | d_F tau_8^+)|, |theta[1/4, 0](0 | d_F tau_8^+)|, |theta[0, 0](0 | d_F tau_8^+)|) / |theta[0, 0](0 | d_F tau_8^+)|` at quantized intersection integers `(d_{10}, d_5) = (3, 1)` (`|I_{10}| > |I_5|`, priced explicitly in the discrete bit ledger; vs symmetric `d_{10} = d_5 = 3` PMNS collapse `|U_{e2}| < 1 / 8` in **Control `4`**).

3. **`E3` — Exact Seesaw `E_1` Cancellation, `P-879` & `OBS-18` Lift, & `SU(3)^5 x U(3)` Basis Scrambling:**
   - Verify exact cancellation of any invertible right-handed neutrino localization `E_1` (`condition number 10^8`) in `M_nu^{UV} = -Y_nu^{UV} (M_R^{UV})^{-1} (Y_nu^{UV})^T` (`relative Frobenius difference < 10^{-32}`), while achieving simultaneous hierarchical CKM (`|V_{cb}| < 1 / 4`, `|V_{ub}| < 1 / 20`), bi-large PMNS (`|U_{e2}| > 1 / 4`, `|U_{mu 3}| > 1 / 4`), and `m_{nu, 2} / m_{nu, 3} < 2 / 5 < 457 / 1000` (`lifting P-879 and OBS-18`).
   - Verify `SU(3)^5 x U(3)` unitary basis-scrambling invariance (`< 10^{-32}`) across all `19` UV mass-ratio, CKM/Jarlskog, PMNS, and neutrino invariants, while catching omitted Takagi `M_R -> U_N^* M_R U_N^H` (`break > 1 / 50`, **Control `5`**).

## Disjoint Cold-Room Countercheck (`c41_countercheck.py`)

- Re-derives `Spin(10)` via `32 x 32` `Cl(10)` Fock matrices, evaluates all Robin-Szegő kernels via Jacobi heat-equation `jtheta` + `2D` Riemann-Mellin `expint` (`zero shared digamma or q-sum lines`), scrambles via `mp.expm(i H)` (`zero Cayley maps`), and verifies `5 / 5` planted-fault controls.

0 of 19.
