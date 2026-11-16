# `AGY-002_CLOSURE-G7` — Gate 7 Results (`0 of 19`)

## 1. Check Labels and Tracked Evidence (`docs/seats/README.md` § 12)

- **expectations committed first:**
  - Card commit `901a89de3`: `relays/cards/AGY-002_CLOSURE-G7_p862-kill-lines-epistemic-dag-and-master-handoff.md`
  - First script seal `42c2fbf38`: `relays/agy002_closure_g7/verify_closure_g7.py`, `relays/agy002_closure_g7/SCRIPT_SHA256.txt`
  - First output seal `a82f12e8a` (committed unread): `relays/agy002_closure_g7/verify_closure_g7_out.json`, `relays/agy002_closure_g7/OUTPUT_SHA256.txt`
- **recomputed independently:**
  - Cold-room second script seal `cd8f13049` & unread output `ce1aecc40` (`relays/agy002_closure_g7_referee/referee_closure_g7.py`, `relays/agy002_closure_g7_referee/referee_closure_g7_out.json`), plus immutable harness-alignment erratum `57ecbb424` & unread output `cd5e60af8` (`relays/cards/AGY-002_CLOSURE-G7-REFEREE-ERRATUM_gate6-key-and-rk4-grid.md`, `relays/agy002_closure_g7_referee_fixed/referee_closure_g7_fixed.py`, `relays/agy002_closure_g7_referee_fixed/referee_closure_g7_fixed_out.json`), built from the card and prior gate results alone without reading or importing `relays/agy002_closure_g7/verify_closure_g7.py`.
- **tested against planted errors:**
  - `5 of 5` planted cases caught in `a82f12e8a` (`PF7.1` unpriced `2`nd scale anchor raises `rank(D_dim)` from `1` to `2 > 1`; `PF7.2` back-edge `SM03:y_t -> G:m004_Mostow_Rigidity` caught by cycle detector; `PF7.3` child rank laundering `0 < 3` caught by monotone `max-plus` check; `PF7.4` unproved rank-`0` assignment on `S:Collar_Modulus_Delta_PS` caught by `Guardrail 1` seam check; `PF7.5` `1`-hex-digit `SHA-256` memory flip caught by custody check);
  - `5 of 5` planted cases caught independently in both `ce1aecc40` and `cd5e60af8` (`PF7.1` `rank = 2 > 1`; `PF7.2` caught by both Kahn topological sort and `3`-color `DFS`; `PF7.3` `3` monotone violations; `PF7.4` caught on both `S:Collar_Modulus_Delta_PS` and `S:Torsion_Tau_SU2R_Break`; `PF7.5` `tampered_mismatch_count = 1`).

## 2. Mask-Safe Rational Verification Summary (`0 of 19`)

| Check | First Computation (`a82f12e8a`) | Cold-Room Second Computation (`cd5e60af8`) | Sealed Rational Bar |
|---|---|---|---|
| `AST` source lock & `SHA-256` custody | `0` float literals, `0` complex literals, `0` repo imports; `36 / 36` prior manifests + self `SCRIPT_SHA256` matched | `0` float literals, `0` complex literals, `0` repo imports; `40 / 40` prior manifests + self `SCRIPT_SHA256` matched (`42 / 42` campaign-wide) | Exact (`0` mismatches) |
| `U(3)^5` `SM` & `Weinberg` `EFT` operator ranks | `SVD` `rank(J_SM) = 41` (`4` unbroken, `13` flavour, `19` `SM`); `rank(J_EFT) = 44` (`1` unbroken, `22` flavour+`nu`, `28` `EFT`) | Exact `SymPy` `DomainMatrix` over `QQ` + `5`-seed `SVD`: `41` (`ker = U(1)_B x U(1)_{L_e} x U(1)_{L_mu} x U(1)_{L_tau}`) & `44` (`ker = U(1)_B`); `19` `SM` & `28` `EFT` | Exact `(41, 44)` & `(19, 28)` |
| `Buckingham-Pi` rank-`1` scale lock (`Guardrail 5`) | `rank(D_dim) = 1` (`v_EW` sole anchor, `18` dimensionless ratios); `PF7.1` `rank = 2` | Exact `QQ` `rank(D_dim) = 1` (`11` dim-`1`, `8` dim-`0` -> `1` anchor `v_EW`, `18` ratios); `PF7.1` `rank = 2` | Exact `rank = 1` |
| `46`-node monotone `max-plus` epistemic `DAG` | `46` nodes (`5, 5, 7, 10, 19`), acyclic, `Guardrail 1` passed, `RELATION` hist `[2, 6, 2, 0]`, `SM_TARGET` hist `[0, 0, 1, 18]` | `46` nodes (`5, 5, 7, 10, 19`), Kahn + `DFS` acyclic, `Guardrail 1` passed, exact node-for-node `[2, 6, 2, 0]` & `[0, 0, 1, 18]` (`SM19:bar_theta_QCD` at `2`) | Exact histograms |
| `P-862` Step `3` `PR-1..PR-10` rational kill lines | `Z_6` & cubic polynomial `0`; `(23/134, 109/201, 506/201)`; `Delta = (+2, +2, -6)`; `I_TM1 = 2/3` | Re-derived all `10` relations from scratch (`SymPy` + `600/1200`-step `RK4` `< (1/10)^12` + `2D` quadrature + `30`-digit `mpmath` `Casimir`) | Exact rational bars |

## 3. Theorems Locked in Gate 7

1. **First-Principles `U(3)^5` & `Buckingham-Pi` Accounting (`Guardrail 5`):** Exact Gaussian elimination over `QQ` proves `rank(J_{U(3)^5}^{SM}) = 41` (`unbroken U(1)_B x U(1)_{L_e} x U(1)_{L_mu} x U(1)_{L_tau}`, leaving `54 - 41 = 13` flavour parameters and `13 + 3 + 2 + 1 = 19` total `SM` parameters) and `rank(J_{U(3)^5}^{EFT}) = 44` (`unbroken U(1)_B`, `66 - 44 = 22` flavour+neutrino parameters and `28` `Weinberg` `EFT` parameters), with `rank(D_dim) = 1` pricing `v_EW` as sole dimensionful anchor alongside `18` dimensionless `SM` ratios.
2. **`P-862` Step `3` Structural Dichotomy (`Relations vs Point Values`):** Monotone `max-plus` rank propagation on the `46`-node acyclic `DAG` proves that all `10` sealed `P-862` relations `PR-1..PR-10` hold at epistemic rank `<= 2` (`2` universal at rank `0`, `6` frame-wide at rank `1`, `2` `1`-bit discrete at rank `2`, `0` requiring continuous moduli), whereas among the `19` individual `SM` parameters only `SM19:bar_theta_QCD` closes without continuous moduli (`rank 2`, `1` discrete sign bit on `X_4`), and all `18` remaining point values (`SM01..SM18`) sit at rank `3` until a target-free `4D` stabilization functional (`d V / d x = 0`) is proved.
3. **Campaign-Wide Cryptographic Custody Lock:** All `42` `SCRIPT_SHA256.txt` and `OUTPUT_SHA256.txt` manifests across `ENDGAME-V2` (`Gates 0-3`) and `COMPLETE-CLOSURE` (`Gates 4-7`) match byte-for-byte with `0` float literals and `0` complex literals across all Gate `4-7` scripts. Gate 7 is locked. `0 of 19.`
