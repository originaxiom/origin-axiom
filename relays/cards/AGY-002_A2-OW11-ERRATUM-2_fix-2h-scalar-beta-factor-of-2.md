# Pre-Registration Erratum 2: `AGY-002_A2-OW11-ERRATUM-2` — Correction of Factor-of-2 `2H` / `(1, 2, 2)_C` Scalar Beta Coefficient Caught by Cold-Room Referee (`0 of 19`)

- **Parent Card:** `AGY-002_A2-OW11` (`93246dcb0`) + `Erratum 1` (`d39b7129d`)
- **Preserved Custody:** `v1` (`6438776d5` / `320f31dfd`), `v2` (`7a8ab22d1` / `45cc93d3f`), and Cold-Room Referee (`e1d3f2365` / `a9d82818b`, which caught this exact factor-of-2 overcount from first-principles real-representation Cartan traces `Delta b_a = (1 / 6) Tr_R(T_a^2)`).
- **Exact Correction:**
  - `1` complex `(1, 2, 2)_C` bidoublet (`8` real scalars = `2H`, matching `N_S = 24, 39, 68` in FRG) contributes `(db_4, db_2L, db_2R) = (0, 1 / 3, 1 / 3)` (NOT `(0, 2 / 3, 2 / 3)`), maintaining exact `SU(2)_L` beta continuity `b_2L = -3` across `M_PS`.
  - Corrected exact Pati-Salam `1`-loop betas & `B = 5 / 7` unification ratios `r = ln(M_PS / M_Z) / ln(M_GUT / M_Z)`:
    - `PS_122_412` (`24` real S): `b_1_eff = -83 / 15`, `b_2L = -3`, `b_4 = -31 / 3`, `B_PS = -55 / 19`, **`r = 8 / 9`** (closes via `b_1_eff < b_2L`).
    - `PS_122_1511_412` (`39` real S): `b_1_eff = -79 / 15`, `b_2L = -3`, `b_4 = -29 / 3`, `B_PS = -50 / 17`, **`r = 29 / 33`** (closes via `b_1_eff < b_2L`).
    - `PS_122_1013` (`68` real S): `b_1_eff = -13 / 15`, `b_2L = -3`, `b_4 = -23 / 3`, **`B_PS = 35 / 16 > 5 / 7`**, **`r = 11 / 15`** (closes via positive slope `B_PS > 5 / 7`).
  - Similarly, `6D` `T^2 / Z_2` bulk `2H` (`8` real scalars per unordered pair) contributes `(1 / 5, 1 / 3, 0)` (NOT `(2 / 5, 2 / 3, 0)`), giving **`B_6D_KK_bulk_2H = 55 / 98`** (`5 / 9 < 55 / 98 < 5 / 7`, qualitative non-closure unchanged).
  - Authoritative Producer `v3` (`relays/a2_ow11_v3/`) implements these exact corrected coefficients and is cross-checked field-by-field against Cold-Room Referee `a9d82818b` (`0` discrepancies expected across all fields). `0 of 19.`
