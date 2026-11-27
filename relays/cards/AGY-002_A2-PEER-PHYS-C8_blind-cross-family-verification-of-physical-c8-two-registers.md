# SCOPE CARD — Card A2-PEER-PHYS-C8: Blind Cross-Family Independent Verification of `physical` `C8_two_registers` (`P-876`, `SL(2, F_25)` Even Weil `13 + 3` in `Spin(16) -> Ss(16) subset E_8` & Dihedral Sheet Lift) (seat code: `fam3-v1-high-03`, `0 of 19`)

- **card id:** A2-PEER-PHYS-C8 (pre-registration; blind cross-family `fam3-v1-high-03` second computation of `fam2-v1-unset-01`'s `P-885` card `CLAIM_2026-11-27_C8_two_registers.md` on `origin/audit/physical-bridge-2026-09-05 @ 2de93d2e6` that carries `second computation: none`)
- **seat code:** `fam3-v1-high-03`
- **date:** 2026-11-27
- **touches:** `P-876`
- **imports:** `none` (pure exact integer, finite-field `F_25`, binary-dihedral `BD_5 subset SU(2)`, and `Spin(16) -> Ss(16) subset E_8` weight-lattice arithmetic in standard library only)
- **premises on main (zero trial arcs):** `P-876` (harvest row `1987`)
- **blindness & custody:** Strictly `0 of 19`. ZERO `origin/audit/physical-bridge-2026-09-05` scripts, proofs, or outputs (`c8_register/*`, `THE_TWO_REGISTERS*`) opened prior to committing this Scope Card, the independent verifier script, and its unread sealed outputs. Only `CLAIM_2026-11-27_C8_two_registers.md` was read.

## Pre-Registered Blind Expectations & Falsification Criteria

1. **Exact `F_25 = F_5[d]/(d^2 - 2)` & `SL(2, F_25)` Even Weil Module (`dim 13`):**
   - Construct exact `F_25` arithmetic (`25` elements, `Tr(a + b d) = 2 a mod 5`) and the `13`-dimensional even Weil module indexed by `x in F_25 / {+-1}` (`1` zero + `12` nonzero pairs) with `U(v)` additive-character eigenvalues `zeta_5^{Tr(2 v x^2)}`.
   - Verify `m_geo = U(1)` and `l_geo = Z U(-2 d)` commute in `SL(2, F_25)` (`order(m_geo) = 5`, `order(l_geo) = 10`, `Z = -I` acts as `+1` on `13`).
   - Verify the `12` nonzero pairs split into exactly `6` conjugate real `2`-planes `(w_m, w_l) in (Z/5Z)^2`, with `m_geo` weights `{1,1,1,2,2,2,3,3,3,4,4,4}` (`3` copies of each nonzero residue mod `5`) and `l_geo` weights matching exact `Tr(2 (-2d) x^2) mod 5`.

2. **Exact `Spin(13) x Spin(3) -> Spin(16) -> Ss(16) subset E_8` Adjoint Decomposition (`248 = 120 + 128`):**
   - Verify `dim Lambda^2(13 + 3) = 120` (`78 + 3 + 39`) and `dim(S_{13} (x) S_3) = 64 * 2 = 128`, total `248 = dim E_8`.
   - Verify exact central-multiplication kernel: `z_13 = (-1 in Spin(13))` and `z_3 = (-1 in Spin(3))` satisfy `z_13 z_3 = +1` identically on BOTH `120 = Lambda^2(16)` and `128 = 64 (x) 2` (so the two block minus scalars have the same image in `E_8`, while `(z_13, 1)` acts as `+1` on `120` and `-1` on `128`).
   - Verify exact `Spin(13)` half-weight sums `(1/2) sum_{j=1}^6 eps_j (w_m, w_l) mod 5` across all `64` states (`2` invertible mod `5`): exact multiplicity `4` at `(0, 0) mod 5` (out of `64`), yielding **`4 * 2 = 8`** states in `64 (x) 2` with `m_geo = +1, l_geo = -1` (periodic spin) and **`0`** with `m_geo = -1, l_geo = -1` (antiperiodic spin), and **`0`** in `Lambda^2(16)` for either spin!

3. **Exact Commuting Binary Dihedral Sheet Lift `BD_5 = <r, j> subset Spin(3) = SU(2)` (`r^5 = 1, j r j^{-1} = r^{-1}, j^2 = -1`):**
   - Verify explicit `BD_5` (`order 20`) inside `SU(2) = Spin(3)` commutes elementwise with `Spin(13)` and lifts `D_5 = <r, s>` via `r^a s^e -> r^a j^n` (`e == n mod 2`, `n` = oriented meridional exponent on `pi_1(m004)`), directly verifying explicit surjective homomorphisms `pi_1(m004) ->> D_5` lifting to `BD_5`!
   - In a sheet frame (`m -> m * j`, `l -> l * 1`), compute exact joint eigenvalues on ALL `248 = 120 + 128` adjoint weights:
     * On `120 = Lambda^2(16)`: `l_join` has only 5th roots of unity -> **`0`** (`l = -1` impossible).
     * On `128 = 64 (x) 2`: `m_join` carries eigenvalue `(+-i) * zeta_5^k`, so **`m_join^2` carries `(-1) * zeta_5^{2k}` (never `+1`!)**, forcing BOTH periodic (`m = +1, l = -1`) AND antiperiodic (`m = -1, l = -1`) peripheral spin kernels to drop from **`8 -> 0`** (`0` periodic, `0` antiperiodic)!

4. **Controls & Hygiene:** `5/5` independent planted fault controls (including omitting the sheet action restoring `8`), `0` AST float literals, `0` JSON float literals, standalone exit-1 control with `0` stderr bytes, `0` refused imports under `T7b Part 1`.
