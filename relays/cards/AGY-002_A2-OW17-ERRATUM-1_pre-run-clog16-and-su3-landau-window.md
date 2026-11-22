# Pre-Run Erratum 1 to Card `AGY-002_A2-OW17`: Exact `c_log = 16` (`3` RHN) and `SU(3)` Perturbative Window

- **Seat / Branch:** `agy-002` on `agy-002/verify`
- **Date:** `2026-11-22` (committed BEFORE writing or running any `a2_ow17` script; `expectations
  committed first` under `docs/seats/README.md` Section 12)
- **Target Card (unmodified):**
  `relays/cards/AGY-002_A2-OW17_c25-physics-seams-brane-2h-unification-and-m004-equivariance.md`
- **Empirical Inputs:** `0 of 19`

## 1. Two Pre-Run Arithmetic Clarifications

1. **`OW17-A` Item 4 (`c_log` with `3` RHN + `8` Conformal Brane `2H` Scalars):**
   - At conformal coupling `xi = 1 / 6`, real scalars have `w_S_tot(1 / 6) = 1 / 6 - xi = 0`, so
     replacing `10_R` by `4D` brane `2H` (`8` conformal scalars) leaves the scalar contribution to
     `c_log` identically `0`.
   - With `33` massive `Spin(10)` Proca vectors (`w_P_tot = -1 / 2` -> `+33 / 2`) and `3` heavy
     right-handed Weyl neutrinos `nu^c` (`w_W_tot = +1 / 6` -> `-3 / 6 = -1 / 2`), the exact total
     is **`c_log = 33 / 2 - 1 / 2 = 16`** (`c_log_ent = -55 / 3`, `c_log_contact = +103 / 3`,
     sum `= +16`), matching `A2-OW8` and `A2-OW15` identically (rather than `33 / 2`, which omitted
     the `3` RHN `-1 / 2` term).
2. **`OW17-B` Item 2 (`SU(3)` Asymptotic-Freedom Landau Scale on Downward `2`-Loop Integration):**
   - Because `b_3 = -7 < 0`, running downward from unified `1 / alpha_UV` hits `SU(3)` confinement
     (`1 / alpha_3 -> 0`) at `|t_Landau| ~ (2 pi / 7) * (1 / alpha_UV)` (`~ 17.95` for `1/alpha_UV
     = 20` up to `~ 35.9` for `1/alpha_UV = 40`).
   - Therefore `OW17-B` integrates all five blind couplings `1 / alpha_UV in {20, 25, 30, 35, 40}`
     cleanly over the strictly perturbative common window `t = 0 -> -12` (where `1 / alpha_3 > 6`
     for every curve), AND integrates `1 / alpha_UV in {40, 45, 50}` down to `t = -30` / `-35`
     (stopping safely whenever `1 / alpha_3 < 2` and recording exact `B_eff^{(2-loop)}(t)`).

0 of 19.
