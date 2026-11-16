# `AGY-002_ENDGAME-V2-G3` — Gate 3 Results (`0 of 19`)

## 1. Check Labels and Tracked Evidence (`docs/seats/README.md` § 12)

- **expectations committed first:**
  - Card commit `c99a383b9`: `relays/cards/AGY-002_ENDGAME-V2-G3_radiative-ewsb-scale-closure-and-blind-seal.md`
  - First script seal `b13e8173c`: `relays/agy002_endgame_v2_g3/verify_endgame_v2_g3.py`, `relays/agy002_endgame_v2_g3/SCRIPT_SHA256.txt`
  - First output seal `477b68948` (committed unread): `relays/agy002_endgame_v2_g3/verify_endgame_v2_g3_out.json`, `relays/agy002_endgame_v2_g3/OUTPUT_SHA256.txt`
- **recomputed independently:**
  - Second script seal `d8c956680` (built from the card and published literature alone without reading or importing any verifier script, while checking all `14` campaign SHA-256 manifests): `relays/agy002_endgame_v2_g3_referee/referee_endgame_v2_g3.py`, `relays/agy002_endgame_v2_g3_referee/SCRIPT_SHA256.txt`
  - Second output seal `54628fecb` (committed unread): `relays/agy002_endgame_v2_g3_referee/referee_endgame_v2_g3_out.json`, `relays/agy002_endgame_v2_g3_referee/OUTPUT_SHA256.txt`
- **tested against planted errors:**
  - `5 of 5` planted cases caught in `relays/agy002_endgame_v2_g3/verify_endgame_v2_g3_out.json` (`PF3.1` `0.2802 > 0.1`, `PF3.2` `0.6102 > 0.1`, `PF3.3` `0.0304 > 0.01`, `PF3.4` `-0.0946 < -0.01`, `PF3.5` `2 > 1`);
  - `5 of 5` planted cases caught in `relays/agy002_endgame_v2_g3_referee/referee_endgame_v2_g3_out.json` (`PF3.1` `0.2802`, `PF3.2` `0.6102`, `PF3.3` `0.0304`, `PF3.4` `-0.0943`, `PF3.5` `2 > 1`). Note: `section_2_passed` in `referee_endgame_v2_g3_out.json` applied an internal `1e-12` bar to `dop853_vs_mpmath45_muH2_ir_rel_err = 1.354e-12`, which is `7.4` times tighter than the card's `< 1e-11` `Picard-Lindelof` lock (`DOP853` integral error `3.46e-15`, `mpmath` integral error `4.69e-13`).

## 2. Numerical Summary (`0 of 19`)

| Check | First Computation (`verify_endgame_v2_g3_out.json`) | Second Computation (`referee_endgame_v2_g3_out.json`) | Bound |
|---|---|---|---|
| AST zero float literals & `14` campaign SHA-256 manifests | `0` floats, `True` | `0` floats, `14 / 14` SHA-256 manifests matched (`0` mismatches) | Exact |
| `Buttazzo et al. (2013)` `2`-loop `gamma_{mu_H^2}` polynomial | Exact rational match (`367247879/65865514`, `-886154046205665125/503238848400166736`) | Exact match across `10` rational tuples & `SO(3)^5` rotations; matches first computation | Exact |
| `Picard-Lindelof` homogeneous integral & non-crossing | `rel_err = 8.21e-14`; `min mu_H^2 = +0.6102` (`zero crossing = False`) | `DOP853` `3.46e-15`, `mpmath` `4.69e-13`, cross-solver `1.35e-12`; `min mu_H^2 = +0.6102` | `< 1e-11` |
| `Coleman-Weinberg` curvature `d^2 V_CW / dH^2` (`mu_H^2 = 0, lambda = 0`) | Gauge-only `beta_lam = +1.26e-3 > 0`; top-dominated `beta_lam = -2.36e-2 < 0` (`maximum`) | Gauge-only `+5.04e-3 v^2 > 0`; top-dominated `-9.43e-2 v^2 < 0` (`maximum`) | Exact sign |
| `Vissani (1998)` `N_R` `MSbar` `RG` invariance & downward shift | `RG` residual `0.0`; downward shift `+0.04559 > 0` (`stabilizes unbroken phase`) | `50`-digit `2 x 2` seesaw `mp.diff` `RG` residual `6.90e-24`; downward shift `+0.04559 > 0` | `< 1e-12` |
| `Pati-Salam` scalar portal zero-crossing & `v_EW` ledger | `t_cross = -1.95017760`, `Barbieri-Giudice` `4.24e23`, `1` anchor (`v_EW`), Haar `1.67e-16` | `t_cross = -1.95017764` (`diff 4.68e-8`), `Barbieri-Giudice` `1.47e24`, `1` anchor (`v_EW`), Haar `9.73e-16` | `< 1e-12` |

## 3. Result for Gate 3

1. **Pure-`SM` `MSbar` Homogeneous & `Coleman-Weinberg` Obstructions Proved:** Below heavy thresholds, `d mu_H^2 / d ln(mu) = gamma_{mu_H^2} mu_H^2` preserves `sgn(mu_H^2)` identically (`Picard-Lindelof`), while scale-invariant `Coleman-Weinberg` (`mu_H^2 = 0, lambda(mu_CW) = 0`) yields a local **maximum** (`beta_lambda < 0`) whenever top Yukawa dominates gauge couplings.
2. **Heavy-Threshold Sign Dichotomy & Dimensionless `v_EW` Ledger:** In `MSbar`, heavy right-handed Majorana neutrinos shift `mu_H^2` **positively** downward (`d mu_H^2 / d ln(mu)|_{N_R} < 0`), whereas heavy `Pati-Salam` portal scalars (`lambda_{HS} > 0`) drive genuine downward radiative zero-crossing `mu_H^2(t_cross) = 0`, but achieving `v_EW^2 / M_PS^2 = exp(-2 Delta_SM)` from a high threshold requires `> 1e23` `Barbieri-Giudice` tuning. Thus `v_EW` remains the sole unfixed dimensionful IR anchor (`1` dimensionful unit, `1` dimensionless UV quadratic tuning parameter), with all `12` particle masses expressed as Haar-invariant dimensionless ratios `m_i / v_EW`. Gate 3 is locked. `0 of 19.`
