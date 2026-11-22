# Pre-Registration Card A2-PEER-LINK23: Zero-Trust Independent Audit & Harvest of `agy-exp` `Card X-E6PS-LINK23` (`dd74b56c1`) & Remediation of `Card R-OW19-EX12` (`OW19-F1`..`F3`) (`0 of 19`)

- **Seat / Branch:** `agy-002` on `origin/agy-002/verify`
- **Date:** `2026-11-22`
- **Targets:** `agy-exp` `origin/agy/self-consistent-loop-2026-11-11` @ `dd74b56c1` (`Card R-OW19-EX12` at `0b13397b7` & `Card X-E6PS-LINK23` + *PRD* `main.tex` Section VII at `dd74b56c1`).
- **Firewall:** strictly `0 of 19` (zero empirical PDG, NuFIT, Planck, DESI, or CODATA numbers anywhere).
- **Coding & Custody Standard:** `0` Python `float`/`complex` AST literals, `0` binary64 `float()`/`complex()` casts, `0` peer/`frontier/` imports, pre-hashed `SCRIPT_SHA256.txt` committed before execution, raw unread `OUTPUT_SHA256.txt` committed before analysis, zero in-place overwrites, followed by an isolated cold-room zero-shared-code referee (`relays/a2_peer_link23_referee/referee_a2_peer_link23.py`).

---

## Pre-Registered Modules & Acceptance Gates (`L23-0`, `L23-A`..`L23-D`)

### Module `L23-0`: Custody, SHA-256 Manifests, AST Scan, & Verbatim Quotes (`dd74b56c1`)
1. Verify all `7 / 7` new SHA-256 manifests (`r_ow19_ex12_verify`, `x_e6ps_link23_verify`, `x_e6ps_link23_v2_verify`, `x_e6ps_link23_referee`) directly against `git show dd74b56c1:...`.
2. Confirm `0` AST `float`/`complex` literals and `0` binary64 casts across all `3` new `agy-exp` Python scripts.
3. Verify `6 / 6` exact verbatim quotes in `dd74b56c1` (`verify_x_e6ps_link23_v2.py` & `main.tex` Section VII).

### Module `L23-A`: Independent Verification of `X-E6PS-LINK23` Valid Theorems (`the same`)
1. Recompute `E_8 -> E_6 x SU(3)_fam`, exact `351'_H = Sym^2(27bar) (-) 27` (`dim 351`, `Tr Q_psi = 0`), and `6D` `E_6` quartic trace factorization `Tr_{27} F^4 = (1/12)(Tr_{27} F^2)^2`, `Tr_{78} F^4 = (1/2)(Tr_{27} F^2)^2`.
2. Recompute `E3` chiral & `D`-parity `G_LR` `1`-loop betas `b_1 = (11/2, -8/3, -2, -7)`, exact `r_LR = 2/5` (`chiral`) and `8/25` (`D-parity`), `4x4` `2`-loop Machacek-Vaughn `b_2`, and independent `2`-loop `GL4` running from `alpha_GUT^{-1} = 40`, `L = 32` (`matching dd74b56c1 to < 1e-10`; also record `2`-loop `B_eff = 0.74912` vs `1`-loop `5/7 = 0.71429`).
3. Recompute `E5` symbolic `3x3` CP-odd pseudoscalar mass matrix (`exact single EW Goldstone`, `det M_phys^2 = 3 kap_S mu_SH v_S^2 (v_u^2 + v_d^2) / (2 v_u v_d)`) and explicit `4x4` Majorana pseudoscalar `s`-wave cross-section `N_c g_{ca}^2 g_{fa}^2 m sqrt(m^2 - m_f^2) / (2 pi (4 m^2 - M_med^2)^2)`.

### Module `L23-B`: Five First-Principles Mathematical-Physics Catches on `dd74b56c1` (`differs`, `LINK23-F1`..`F5`)
1. **`LINK23-F1` [CRITICAL — Lie-Algebraic Impossibility of `Z_2^{C_psi}` Preserving `G_LR` inside `Aut(E_6)`]:**
   - Prove `verify_x_e6ps_link23_v2.py:149` (`+ 5`) and `:806` (`= 0`) hard-coded `U(1)_psi` removal without implementing any `Z_2^{C_psi}` operator (Guardrail 2).
   - Prove the unique orthogonal reflection `r_{u1}` fixing rank-`5` `g_LR` and inverting `u_1 -> -u_1` maps **`32 / 72` roots of `E_6`** (`16_{-3} + 16bar_{+3}`) strictly outside `Phi(E_6)`.
   - Exhaustively scan all `32` sign flips on the `6` orthogonal `G_LR x U(1)_psi` Cartan generators with `H_psi -> -H_psi`: prove all `8` valid `Phi(E_6)`-preserving sign involutions ALSO flip `H_{B-L} -> -H_{B-L}` and have fixed Cartan dimension `<= 3 < 5 = rank(G_LR)` (and asymmetric `Q_psi(27) = {+1^16, -2^10, +4^1}` forbids any inner involution).
2. **`LINK23-F2` [CRITICAL — `(v_1, v_2, v_3)` Splits `16` into `4` Disjoint Sectors (`0/27` Untwisted) & `Q_psi(S in 27) = +4 == +1 mod 3`]:**
   - Prove `0 / 27` weights of `27` have `(0, 0, 0)` phase under `(v_1, v_2, v_3)`, and `16` splits into `4` distinct sectors: `Q (1/6, 1/2, 15/16)`, `Q^c (1/6, 0, 1/16)`, `L (1/6, 1/2, 3/16)`, `L^c (1/6, 0, 13/16)` (`verify_x_e6ps_link23_v2.py:160` never applied `(v_1, v_2, v_3)` to fermions!).
   - Prove `S subset 27` has `Q_psi = +4 === +1 (mod 3)` (giving `17 * 3 = 51 === 6 != 0 mod 9`, NOT `15 * 3 = 45 === 0 mod 9` unless `chi_S` comes from `27bar`), while ALL `5` UV-insensitive `Z_3` anomalies (`SU(3)^2, SU(2)_L^2, SU(2)_R^2, (B-L)^2, grav^2`) ALREADY vanish at `N_gen = 3` without `chi_S` (`16 * 3 = 48 === 0 mod 3`), and `10_{-2}` masses `D_3 D_3bar` carry `Q_psi = -4 === -1 != 0 mod 3` (breaking `Z_3^{tau_3}`).
3. **`LINK23-F3` [HIGH — Irreducible `~4.5 x 10^{14} v_EW^2` `1`-Loop `W_R, Z_R` & `SU(2)_R` Scalar-Portal Higgs Hierarchy Wall at `M_LR = e^{19.2} v_EW`]:**
   - Compute exact `1`-loop Coleman-Weinberg `W_R, Z_R` radiative Higgs mass shift on `H_{u1}, H_{d2} subset Phi_{1,2} = (1, 2, 2)_0` at `r_LR = 2/5, L = 32` (`M_LR / v_EW = e^{19.2} = 2.18e8`), proving `|delta m_H^2| / v_EW^2 > 10^{14}` (and `1`-loop `SU(2)_R` gauge-box regeneration `16 pi^2 beta_{lam_{Phi Delta}} supset +6 g_{2R}^4` of the zeroed-out portal).
4. **`LINK23-F4` [HIGH — `6D` Twisted Casimir Sign Flip (`-6 -> +82.72` at `tau_* = (2+i)/5`) & `b_1(T^2) = 2 < 3`]:**
   - Compute the exact `6D` `s = 3` twisted Epstein Casimir `2(S_B - S_F)/E_3(0,0)` of `E_6 + 3 x 27` under `T^2`-compatible `(v_1 + v_2, v_3)` at `tau_* = (2 + i)/5`, `tau_8 = (1 + 8i)/5`, and `i`, proving `E6`'s untwisted `-6` flips to **`+82.72`** (AdS runaway) at `tau_* = (2 + i)/5` and `-12.52` at `tau_8`.
5. **`LINK23-F5` [MEDIUM — `E4` Toy Matrices vs Scope Card & `E5` Exact `Z_3` Cosmological Domain Walls]:**
   - Confirm `verify_x_e6ps_link23_v2.py:554-580` uses hand-typed rational toy matrices (not punctured-torus Szego matrices as stated in Scope Card `E4`), and confirm `E5`'s `S^3` carries `Q_psi(S^3) = +12 != 0` and breaks exact `Z_3` spontaneously at `v_S` (`Z_3` domain-wall obstruction).

### Module `L23-C`: Full Remediation of `agy-exp` `Card R-OW19-EX12` (`OW19-F1`..`F3`)
1. **`OW19-F1`:** Verify and explicitly disclose the `5` in-place commits on `relays/a2_ow19_referee/SCRIPT_SHA256.txt` and `3` on `OUTPUT_SHA256.txt`.
2. **`OW19-F2`:** Confirm `A2-OW20` (`d720bc7ff`) & `referee_a2_ow20` (`78045a357`) already closed `2`-flavor leptogenesis (`+2.1579e-9`, `7.47x` reduction) and `Z_4` `M_R == 0` / `overline{126}_{-2}`.
3. **`OW19-F3`:** Compute the exact `48`-digit Frobenius-series limit `bc_star(tau_8^+) = pi - L_2(tau_8^+) = 0.62640452269979635179...` directly in `55`-dps `mpmath` with `0` `float`/`complex` AST literals AND `0` binary64 casts, closing `OW19-A`'s `4.60e-11` finite-radius residual to `< 1e-40`!

### Module `L23-D`: `6 / 6` Planted Fault Controls
1. **`PF-L23-1`:** Claiming `r_{u1}` preserves `Phi(E_6)` fails (`32 / 72` roots broken).
2. **`PF-L23-2`:** Assigning `Q_psi(chi_S) = +4` (`tau_3 = +1` from `27`) fails `mod-9` `[Z_3]^3` at `N_gen = 3` (`51 === 6 != 0 mod 9`).
3. **`PF-L23-3`:** Using `1` bidoublet instead of `2` in `G_LR` shifts `r_LR` from `2/5` to `8/17`.
4. **`PF-L23-4`:** Setting `kap_S = 0` in `E5` collapses `det M_phys^2` to `0` (massless axion/Goldstone).
5. **`PF-L23-5`:** Evaluating `6D` twisted Casimir at `tau_* = (2+i)/5` rejects untwisted `-6` (`+82.72 > 0`).
6. **`PF-L23-6`:** Using `OW19-A`'s finite-radius `bc_star_rich = 0.6264045226538123` fails the `< 1e-12` gate against exact `48`-digit Frobenius `bc_star` (`4.60e-11` discrepancy caught).
