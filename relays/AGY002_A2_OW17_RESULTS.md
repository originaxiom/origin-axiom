# Card `A2-OW17` Check Results: Probing the Three `AGY-C25` Physics Seams (`S2`, `S3`, `S1`) (`0 of 19`)

- **Seat / Branch:** `agy-002` on `agy-002/verify`
- **Date:** `2026-11-22`
- **Empirical Inputs:** `0 of 19` (strict blindness firewall per `docs/seats/README.md` Section 9;
  zero PDG, NuFIT, Planck, or lattice inputs)
- **Check Labels (`docs/seats/README.md` Section 12):** `expectations committed first` (`OW17-C`,
  `OW17-D`, and core `OW17-A`/`OW17-B` physics); `mended expectations` (`Erratum 2` `v2` RK4 step
  count and `r = 1` / pure-PS gate predicate); `recomputed independently`; `tested against planted
  errors`

## 1. Tracked Custody Chain

- **Pre-run card & pre-run erratum:** `f0b48f344` (`AGY-002_A2-OW17`), `89a3c6bbc` (`Erratum 1`,
  pre-run `c_log = 16` & `SU(3)` perturbative window).
- **Raw `v1` preserved unmodified:** script `40b48e55b`, raw output `e10bc011f` (`OW17-C` &
  `OW17-D` passed; `OW17-A` & `OW17-B` findings disclosed transparently in `Erratum 2`).
- **`Erratum 2` & `v2` producer (`0` mends on `v2`):** `Erratum 2` `e0ca8f383`, pre-hashed script
  `3da0330f0` (`SCRIPT_SHA256 = a0617fb5ac21474d1b2616d9eb3215ea10cf669ec580d54da65366f1ed1f5c1b`;
  `0` float AST), sealed output `595ff9434` (`OUTPUT_SHA256 =
  e500fe2833f0877a47b4716f99db853b1f3710519658092f05ede8f3099c293d`; `all_gates_passed = true`).
- **Zero-shared-code cold-room independent referee (`0` mends, zero reads of `verify_a2_ow17*`):**
  pre-hashed script `76494f69f` (`SCRIPT_SHA256 =
  4fddcba6163e34f6b186c8826e20882a7695052471fe944daa315e1eec8bd657`; `0` float AST), sealed output
  `fb561f6fb` (`OUTPUT_SHA256 = 6a033cdb0fc546f62d9fa04df4214e634012c11a13de67f690410f0fbbb57232`).
- **Transparent Cross-Check Note on `L_2` Precision (`OW17-C`):** All `4 / 4` producer custody
  hashes, all `OW17-A`, `OW17-B`, `OW17-D` physics/rational/FRG/RGE checks, and all `OW17-C`
  algebraic/orbit/Haar/physics conclusions matched **`the same`**. On `L_2((16 + 8i) / 5)`, the
  referee's Order-24 Weierstrass-Taylor solver (`>= 19` digits verified against `5` analytic
  identities including `L_2(i)` to `1.10e-21`, `L_2(rho)` to `2.50e-19`, and `S`-duality to
  `1.74e-19`) gives **`2.51518813088999688666884`**, catching a `-2.415e-7` `RK4` step-size offset
  in producer's `48`-step `L_2 = 2.515187889362887560279` (`differs` at `< 10^{-10}`, propagating
  `3e-9 .. 5e-9` into `samples[0..5]`). At identical `L_2`, `eval_yukawa` matches to `4.90e-13`,
  and every `OW17-C` physics conclusion (`min u s_1/s_3 = 0.04433 > 1/100`) is unchanged.

## 2. Task `OW17-A` (Seam `S2` Closed): `4D` Brane `2H` (`N_S = 8`) in `Spin(10)` & `E_6`

- **Exact Lie-Algebraic Supertrace Identity (`the same`):** Both `Spin(10)` (`45` gauge, `3 x 16 =
  48` Weyl) and `E_6` (`78` gauge, `3 x 27 = 81` Weyl; matching `main`'s `B1970` `27` two-Higgs
  dictionary) satisfy `N_V - N_W = -3`. With `4D` brane `2H` (`0` bulk Higgs scalars, `N_S = 8` on
  the `4D` brane), BOTH give `6D` bulk Casimir `n_B - n_F = -6` (de Sitter stabilizing `tau_*^{+-}`,
  `6x` deeper than `10_R`'s `-1`), whereas bulk `10_C` (`+4`) and bulk `27_H` (`+21`) are AdS.
- **`4D` Litim FRG (`the same`, direct `2D` Newton referee match `< 3.73e-18` rel):** At blind UV
  benchmark `g_UV = 13 / 25` (`f_crit = 0.0404323345429`), `4D` brane `2H` (`N_S = 8`) lies far
  above `f_crit` in BOTH `Type II` and `Type I` (`dD` and `LDW` gauges, FD err `< 1.2e-29`):
  - `Spin(10) + brane 2H` `T2`: `g_* = 0.250823`, `lam_* = 0.042825`, `f_lam = 0.63665` (`dD`) /
    `0.35824` (`LDW`) (`8.9x - 15.7x` above `f_crit`).
  - `Spin(10) + brane 2H` `T1`: `g_* = 0.359987`, `lam_* = 0.067396`, `f_lam = 1.02048` (`dD`) /
    `0.57172` (`LDW`).
  - `E_6 + brane 2H` `T2`: `g_* = 0.152169`, `lam_* = 0.024258`, `f_lam = 0.35668` (`dD`) /
    `0.20133` (`LDW`) (`5.0x - 8.8x` above `f_crit`).
  - `E_6 + brane 2H` `T1`: `g_* = 0.224609`, `lam_* = 0.037615`, `f_lam = 0.55734` (`dD`) /
    `0.31389` (`LDW`).
- **`2H` Quartic UV Irrelevance, RGE, & `c_log = 16` (`the same`):** All `5` coupled `4`-quartic
  UV fixed points are UV-irrelevant (`max rel err 4.58e-14`); downward `1`-loop RGE (`t = 0 -> -38`)
  converges to `lam_UV = 0` within `0.00279 < 3 / 1000` (`yb_high`, `bfb = True`, referee `GL4`
  match `7.42e-14`) and `0.00825 < 1 / 100` (`yb_low`, match `6.29e-16`). Conformal `xi = 1 / 6`
  BH entropy remains exact `c_log = -55/3 + 103/3 = 16` (`8` conformal scalars contribute `0`),
  with asymptotically free `b_Spin10(brane 2H) = -76 / 3 < 0` and `b_E6(brane 2H) = -38 < 0`.
- **Conclusion for Seam `S2`:** Replacing bulk `10_R` (`1H` only) with `4D` brane `2H` (`N_S = 8`)
  simultaneously satisfies `2H` `X:HOL`, `6D` de Sitter Casimir stabilization (`-6`), `4D` FRG
  `lam_0 -> 0` UV irrelevance, and `c_log = 16` in BOTH `Spin(10)` and `E_6`.

## 3. Task `OW17-B` (Seam `S3` Exact Theorem): `2`-Loop `2H` SM, `6D` KK, & `45` / Pure-PS Census

- **First-Principles `2`-Loop `2H` SM No-Go (`the same`):** Derived `b_i` and Machacek-Vaughn
  `B_{ij}` directly from `(SU(3), SU(2), U(1)_Y)` Dynkin/Casimir sums (`0` diff vs textbook
  `n_H = 1, 2`). Across all `8` blind trajectories (`1/alpha_UV in {20..40}` to `t = -12` and
  `{40, 45, 50}` to `t = -30 / -35`, referee `GL4` match `<= 4.08e-11`), `max B_eff^{(2-loop)} =
  0.59600 < 62 / 100 < 5 / 7` (`max |B_eff - 5/9| = 0.04044 < 5 / 100`). Exact `2`-loop running
  alone cannot close `B = 5 / 7`.
- **`6D` Complete-Multiplet KK Universality (`the same`):** Complete `Spin(10)` (`45 -> -80/3`,
  `16 -> 8/3`) and `E_6` (`78 -> -40`, `27 -> 4`) KK levels shift `(b_1, b_2, b_3)` equally (`0`
  shift to `B`).
- **Exact `45` & Pure-PS Closure Results (`the same`, exact rational match on all `15 / 15` rows):**
  1. **Zero Extra Scalars Needed for Pati-Salam `B_{eff} = 5 / 7`:** Pure `PS(4, 2, 2) + 3 x 16 +
     (1, 2, 2)_C` (using ONLY the gauge `45`, matter `3 x 16`, and Higgs `2H`, zero representations
     outside `45 + 3 x 16 + 2H`) has `(b_4, b_{2L}, b_{2R}, b_{1,eff}) = (-32/3, -3, -3, -91/15)`
     and closes `B_{eff} = 5 / 7` **EXACTLY at `r = 8 / 77`** (`x = ln(M_{PS}/M_Z)/ln(M_X/M_Z) =
     69 / 77`; adding `(15, 1, 1)_R` from `45` shifts to `r = 8 / 71`, `x = 63 / 71`).
  2. **Guardrail-5 Ratio Still Forced:** Because `B_{IR} = 5 / 9 != 5 / 7` and `0 < 8 / 77 < 1`,
     this Pati-Salam closure STILL requires `1` continuous dimensionless threshold ratio
     `M_{PS} / M_X` (confirming `AGY-C25` `S3`'s `4`-ratio Guardrail-5 count unless `M_{PS}/M_X` is
     dynamically fixed).
  3. **Exact `r = 1` Boundary Discovery in `45`:** No single SM split multiplet inside `45` closes
     strictly in `0 < r < 1`, while **`2 x (1, 3, 0)_R = (1, 3, 0)_C`** (`A_5 + i A_6` complex
     `SU(2)_L` adjoint triplet inside `45`) hits **`B = 5 / 7` EXACTLY at `r = 1`** (`M_{int} = M_Z`,
     `0` intermediate ratio, at the cost of a light EW-scale weak triplet scalar).

## 4. Task `OW17-C` (Seam `S1` Exact Dichotomy): `m004` Equivariance & `E[n]` Orbits

- **Exact Commutant & Degeneracy Theorem (`the same`):** On `E[2] \ {0}`, the `m004 = [[2,1],[1,1]]`
  `3`-cycle `P` has `3D` circulant commutant `{a I + b P + c P^2}` (diagonal commutant dim `= 1`,
  `a I_3`; exact `3 x 3` DFT err `<= 6.53e-56`). Every real symmetric circulant (`b = c in R`)
  enforces exact `m_1 == m_2` (`split = 0.0`). Complex circulants require `O(10^{-4})` tuning of
  `a + b omega^2 + c omega -> 0` to reach `m_1 / m_3 = 2.98852175166e-5` (err `3.86e-17`).
- **Natural Complex Circulant Test on `E[5] + E[6]` (`m_L = 8`):** Across `6` natural `O(1)`
  `m004`-equivariant complex circulants (plus `4` independent referee pairs), `min u s_1/s_3 =
  0.04433 > 1 / 100` (`min d s_1/s_3 = 0.10745`; independent referee ensemble `0.07178` / `0.10112`),
  with `10`-trial Haar `U(3)_L x U(3)_R` invariance drift `1.73e-55` (producer) / `1.63e-55`
  (referee). **Dichotomy established:** exponential flavor hierarchies require explicitly breaking
  `m004`'s `3`-cycle on `E[2] \ {0}`.
- **Exact `m004` Orbit Histograms (`the same`, `6 / 6`):** `E[2]: {1:1, 3:1}`, `E[3]: {1:1, 4:2}`,
  `E[4]: {1:1, 3:5}`, `E[5]: {1:1, 2:2, 10:2}` (invariant `1D` eigenline `span((1, 2))` of order
  `2`), `E[6]: {1:1, 3:1, 4:2, 12:2}`, `E[8]: {1:1, 3:5, 6:8}`.

## 5. Task `OW17-D` (`4 / 4` Planted Fault Controls — `the same`)

- `PF-OW17-1` (bulk `10_C` `h_pt = 10` -> `n_B - n_F = +4` AdS): **CAUGHT**.
- `PF-OW17-2` (`2 * B_{ij}` corrupted `2`-loop matrix): **CAUGHT**.
- `PF-OW17-3` (non-commuting `diag(1, 2, 4)` vs `P_{m004}`): **CAUGHT**.
- `PF-OW17-4` (non-unitary `U_L = diag(2, 1, 1)` -> drift `0.243067 > 1 / 10`): **CAUGHT**.

0 of 19.
