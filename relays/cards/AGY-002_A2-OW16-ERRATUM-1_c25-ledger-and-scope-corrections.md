# Erratum 1 to Card `AGY-002_A2-OW16`: `AGY-C25` Ledger, Status, and Scope Corrections (`v3`)

- **Seat / Branch:** `agy-002` on `agy-002/verify`
- **Date:** `2026-11-22`
- **Trigger:** Cross-seat verification and review `Relay AGY-C25` (`0e4506d59`), findings `S1`-`S6`
  and `P1`-`P4`
- **Historical Sealed Card (unmodified):**
  `relays/cards/AGY-002_A2-OW16_blind-prediction-seal-cross-card-audit-input-ledger-and-seat-reconciliation.md`
- **Empirical Inputs:** `0 of 19` (zero PDG, NuFIT, Planck, or lattice inputs)

## 1. Purpose

`Relay AGY-C25` independently recomputed all `137 / 137` SHA-256 manifests and every mathematical
computation across `F-U1..F-U4`, `A2-P879`, `A2-WG96`, and `A2-OW1..A2-OW15` as `the same`, and
identified six substantive ledger/scope overclaims (`S1`-`S6`) plus four process/hygiene gaps
(`P1`-`P4`). Rather than modifying historical sealed `v2` outputs, this pre-registered erratum
specifies `relays/a2_ow16_v3/verify_a2_ow16_v3.py` and its zero-shared-code independent referee
`relays/a2_ow16_v3_referee/referee_a2_ow16_v3.py` to enforce every correction mechanically.

## 2. Pre-Registered Specifications and Failure Conditions (`v3`)

### Task `OW16v3-A`: Custody Manifests (`64 / 64`) and `10 / 10` Cross-Card Locks

- Re-verify all `60` `A2-OW1..A2-OW15` manifests PLUS the `4` historical `A2-OW16` (`v2` + referee)
  manifests (`64 / 64`, `0` mismatches), confirming zero historical hashes were altered.
- Re-verify all `10 / 10` cross-card consistency locks (`LOCK-1..LOCK-10`).
- **Failure condition:** Any manifest mismatch (`!= 64 / 64`) or any lock failure (`!= 10 / 10`).

### Task `OW16v3-B`: Machine-Verified Algebraic Checks for `S1`, `S2`, `S3`, `S4`, `S5`, `S6`

1. **`S1` (`m004` Transitive `3`-Cycle on `E[2] \ {0}` & Discrete Bits):**
   - Compute explicitly that `m004 = [[2, 1], [1, 1]] mod 2` acts as a transitive `3`-cycle on
     `E[2] \ {0} = {(1, 0), (0, 1), (1, 1)}`, so diagonal `D_{R, f} = diag(eps_f^2, eps_f, 1)`
     breaks `m004` symmetry and collides with `OW11-C`'s uniform bulk generation assumption.
   - Reclassify `OBS-12` (`A2-OW7` quark hierarchies/CKM) as `CONDITIONAL_ANSATZ` (withdrawing
     "zero-parameter" for `eps_f = phi^(-2 |6 Y_R|)` and noting `E[6]` `t = 4` omission).
   - Update discrete flavor selection count to `log_2(6) + log_2(3) = log_2(18)` (`6` perms x
     `3` cusp levels `m_L in {8, 24, 40}`) BEFORE pricing the un-derived `D_{R, f}` ansatz.
2. **`S2` (`10_R` vs `2H = 10_C` Orbifold Seam):**
   - Compute explicitly that `-P_{PS} = diag(-1^6, +1^4)` keeps exactly `4` real even components
     in real `10_R` (`1H`), NOT `8` real scalars (`2H = H_u, H_d = 10_C`), while `OW11-A`
     excludes bulk `10_C` (`+4` AdS). Document this explicitly in `OBS-05`, `OBS-06`, `OBS-09`.
3. **`S3` (Guardrail-5 `M_{PS} / M_X` & Extra PS Scalars):**
   - Compute explicitly that pure `2H` `SM` gives `B(2) = 5 / 9 != 5 / 7` (no-threshold IR
     non-unification) and that closing `B_{eff} = 5 / 7` requires extra PS scalars outside
     `16 + 10 + 45` plus the continuous threshold ratio `M_{PS} / M_X`.
   - Move `OBS-08` (Pati-Salam `B = 5 / 7` closure) from `DERIVED_EXACT` to
     `CONDITIONAL_OR_QUALITATIVE` (`CONDITIONAL_THRESHOLD`).
   - Report BOTH Guardrail-5 continuous SM/UV counts explicitly:
     - Without PS threshold (`B = 5 / 9`, non-unified): **`3`** (`g_UV`, `tan(beta)`, `M_R / M_X`).
     - With PS `B = 5 / 7` closure: **`4`** (`g_UV`, `tan(beta)`, `M_R / M_X`, `M_{PS} / M_X`),
       net `delta = 0` vs Campaign 1, plus extra PS scalar rep choice.
4. **`S4` (Ordered `D = 4` Clifford `(3, 1)` Parity & Fibered Towers):**
   - Explicitly construct all `5` ordered `D = 4` Clifford even algebras `Cl^0(t, s)` (`t + s = 4`)
     and verify that BOTH `(1, 3)` and `(3, 1)` have `vol^2 = -1` and `Weyl = C (L^* = R)`.
   - Verify that ruling out `(3, 1)` uses `t = 1` hyperbolicity / Dirac norm positivity OR
     Euclidean fiber addition `(1, 3) + (0, 2) = (1, 5)` vs `(3, 1) + (0, 2) = (3, 3)`.
   - Distinguish the `5` fiber-consistent ordered `D = 4 -> 6 -> 7` towers from the `48 = 3 x 4 x 4`
     unordered Cartesian product in `OBS-02`.
5. **`S5` (`OBS-11` Unimodular / Kaloper-Padilla Status):**
   - Move `OBS-11` (`A2-OW14` unimodular `det g = -1` / KP `a_0 = -64` radiative decoupling) from
     `DERIVED_EXACT` to `CONDITIONAL_OR_QUALITATIVE` (`CONDITIONAL_GRAVITY_POSTULATE`), because
     the modified-gravity postulate is imported rather than derived from `OW4`/`OW8`.
6. **`S6` (`A2-OW14` `28 / 13` Exact Arithmetic & `6` Post-`v1` Mended Cards):**
   - Verify exact rational `Fraction(2 * (22 - 8), 21 - 8) == Fraction(28, 13) != Fraction(7, 3)`.
   - Record all `6` cards with dated post-`v1` threshold errata as `mended expectations` under
     `docs/seats/README.md` section 12.

### Task `OW16v3-C`: Updated `24`-Observable Partition

- `DERIVED_EXACT`: **`9`** (`OBS-01..07`, `OBS-09..10`; down from `11`).
- `CONDITIONAL_OR_QUALITATIVE`: **`6`** (`OBS-08`, `OBS-11`, `OBS-12..15`; up from `4`).
- `INTERNAL_WALL_OR_TENSION`: **`6`** (`OBS-16..21`).
- `OPEN_EXTERNAL_BOUNDARY`: **`3`** (`OBS-22..24`).
- Total: `9 + 6 + 6 + 3 = 24`. Failure condition: any bucket count mismatch or missing ID.

### Task `OW16v3-D`: `6 / 6` Planted Fault Controls (`PF-OW16v3-1..6`)

1. `PF-OW16v3-1`: `1`-byte tamper on `a2_ow15_results.json` -> manifest check MUST fail.
2. `PF-OW16v3-2`: Perturb `OW15` `c_log` from `16` to `15` -> `LOCK-6` MUST fail.
3. `PF-OW16v3-3`: Keep `OBS-08` or `OBS-11` in `DERIVED_EXACT` -> `S3`/`S5` partition check MUST fail.
4. `PF-OW16v3-4`: Omit `M_{PS} / M_X` from unified PS ratio count (`3` instead of `4`) -> `S3` ledger MUST fail.
5. `PF-OW16v3-5`: Claim `10_R` gives `8` even real scalars -> `S2` check MUST fail.
6. `PF-OW16v3-6`: Substitute `7 / 3` for `28 / 13` in traceless `cap = 22` -> `S6` check MUST fail.

## 3. Coding & Firewall Rules

- Strictly `0` Python `float` or `complex` AST literals in both producer and referee scripts.
- Zero imports from `frontier/` or between producer and referee.
- Every line of every new card, erratum, and results relay strictly `<= 680` characters.
- Section-12 neutral check labels only; zero empirical data (`0 of 19`).

0 of 19.
