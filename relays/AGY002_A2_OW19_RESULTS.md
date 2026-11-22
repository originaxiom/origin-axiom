# Card A2-OW19 Results & Combined Cold-Room Referee Verification: Exact 2D Punctured-Torus Hyperbolic Kahler Overlaps, E_6 Non-SUSY Hierarchy & Majorana Dark Matter, and Exhaustive Lie-Theoretic 6D s = 3 Twisted Casimir Classification (0 of 19)

- **Seat:** `agy-002` (`origin/agy-002/verify`)
- **Date:** `2026-11-22`
- **Firewall:** strictly `0 of 19` (zero empirical PDG, NuFIT, Planck, DESI, or lattice numbers anywhere; purely mathematical-physics and dimensionless)
- **Check Labels (§ `12`):** `expectations committed first`, `tested against planted errors`, `recomputed independently` (on cross-seat checks of `AGY-C30` `528ef1cf5` and `X-HARVEST-3S-1` `75cb20177`), `the same` / `differs` (note dated `2026-11-22` per `F-OW18-10`: `computed once` removed on multi-run `A2-OW19 v1 -> v2 -> v3` progression; `v1` and `v2` are preserved untouched with zero in-place overwrites; `referee_a2_ow19` passed on `v1`).
- **Dated `2026-11-22` Cross-Reference (`Card A2-OW20` & `F-C30-08`):** Section `2.3` below evaluated `3`-flavor leptogenesis (`Y_B^{3f}`); in `A2-OW20` (`d720bc7ff`, cold-room verified `78045a357`), exact `2`-flavor (`|tau>` vs `|e + mu>`) leptogenesis reduces radiative `Y_B(tau_*^+)` by `7.47x` (`+2.158e-9` flat, `+2.474e-9` `2D E[2]`, still `tau_*^+`) and flips tree `M_R(0, 0)` on BOTH flat (`-2.859e-11`) and `2D E[2]` (`-2.104e-11`) back to **`tau_*^-`**.

---

## 1. Custody Chain & Disjoint Cold-Room Countercheck

1. **Pre-Registration Card:** `relays/cards/AGY-002_A2-OW19_2d-liouville-flavor-e6-hierarchy-axion-dm-and-6d-casimir.md` committed prior to code at `5c11c21f4`.
2. **Non-Destructive Custody History (`v1` & `v2` preserved untouched):**
   - `v1` (`0d2246ff6` -> `b9101c210`, `OUTPUT_SHA256`: `3ceb23ac...`): frozen raw run caught `3` self-check issues (`Erratum 1`: Guardrail 3 conjugate `M_R` scrambling law `u_nr.conj() @ MR00 @ u_nr.conj().T`, SymPy `expand_log` substitution, and `O(h^2)` finite-difference truncation on `grad F_3`).
   - `v2` (`1f8db21dc` -> `22f8ebdaf`, `OUTPUT_SHA256`: `e8b86c3f...`): frozen raw run passed `OW19-B`, `OW19-C` (`|grad F_3| = 2.89e-33`), and `OW19-D` (`6/6`), catching only an IEEE-754 `float64` Takagi precision floor (`1.454e-11` vs `< 1e-12`) on near-degenerate `MR00` inside `eps_unflav` (`Erratum 2`).
   - **Final Clean `v3` Producer (`90338259c` -> `62f08b148`):** `relays/a2_ow19_v3/verify_a2_ow19_v3.py` (`SCRIPT_SHA256`: `494307e2f1fa58ea4cda2f42d8dc36c11edbf4c180d6ae2a623fbf652c7563ff`), `relays/a2_ow19_v3/a2_ow19_v3_results.json` (`OUTPUT_SHA256`: `e78dfc14616307c5b1906e8cf7d74fae25208905895a68277fcdae99de4fb946`), `0` AST `float`/`complex` literals, `0` forbidden imports, **`all_gates_passed = True`**, **`6 / 6` planted faults caught**, **`haar_10trial_max_drift = 1.99e-34`**.
3. **Combined Cold-Room Zero-Shared-Code Independent Referee (`4ce599eaa` -> `54f6bc037`):**
   - `relays/a2_ow19_referee/referee_a2_ow19.py` (`SCRIPT_SHA256`: `ad5c241b6409c42db81c704e9cab1bf27a5f4160105824f282dc954d1af0cdbc`) and raw sealed `a2_ow19_referee_results.json` (`OUTPUT_SHA256`: `a9353f3b5a2171a0d1d8795c8eacdb8569ac04bd5d88aa2d0022571b0d5c0e1b`).
   - Never read or imported producer `.py` files (programmatic `ast.parse` only in `REF-0`); verified `10 / 10` SHA-256 manifests (`0` mismatches), **`all_referee_checks_passed = True`**, **`discrepancy_count = 0`**, **`6 / 6` referee planted faults caught** across BOTH `A2-PEER-SYNTH v2` (`c161ef045`) and `A2-OW19 v3` (`62f08b148`) using completely disjoint algorithms (`RK4` Lambert-`q` Fuchsian solver, Cartesian-excised + log-radial annulus quadrature, Weyl-chiral `4x4` Clifford rep, gauge-box RGE + Landau-gauge tadpole, direct `2D` Euclidean-ball lattice sum for `F_3`, and BFS Weyl-reflection orbit from Bourbaki simple roots for `E_8`).

---

## 2. Task `OW19-A`: Exact `2D` Punctured-Torus Hyperbolic Metric, Polar-Cusp Gauss-Bonnet, `2D` Hyperbolic Kahler Overlaps, & Three-Seat Leptogenesis Sign Resolution

### 2.1 Exact `2D` Developing-Map Hyperbolic Metric & `10`-Digit Polar-Cusp Gauss-Bonnet
- On `E_{tau_8^+} \ {0}` (`tau_8^+ = (16 + 8i)/5`, reduced to lattice-identical `tau_r = (1 + 8i)/5`), the exact `35`-dps Fuchsian ODE `u''(z) + (1/4)(wp(z; tau_r) - c^*) u(z) = 0` yields:
  - Accessory parameter `c^*(tau_8^+) = -1.60857746537943521865 + 0.0040084334104961180172 i` (`|tr([T_a, T_b]) + 2| = 7.27e-23`, `SL(2, R)` conjugation `max |Im R| = 6.36e-24`; cold-room Richardson-RK4 agrees to `1.63e-13`, `the same`).
  - Pullback metric `e^{2 Omega_hyp(z)} = 1 / [Im(u_1(z) conj(u_2(z)))]^2` satisfies exact double periodicity (`6.39e-17` along `1`, `2.28e-15` along `tau_r`), constant interior Gaussian curvature `K(z_1) = -0.99999999999881`, `K(z_2) = -1.00000000000208` (`max |K + 1| = 2.08e-12`; cold-room `1.02e-12`, `the same`), and exact cusp Robin constant `b_c^*(tau_8^+) = 0.6264045226538123` (`L_2 = pi - b_c^* = 2.515188130935981`, matching cold-room RK4 to `4.87e-10` and `A2-OW17` / `AGY-C30`, `the same`; also `b_c^*(i sqrt(3)) = 0.654597071490051`, `L_2(i sqrt(3)) = 2.486995582099742`).
- Applying the cusp-desingularizing polar substitution `t = 1 / (-ln r + b_c^*)` (`d^2z e^{2 Omega_hyp} = W(t, theta) dt dtheta` with `W(0, theta) = 1` smoothly) over the `4` smooth corner sectors of `P_{tau_r}` eliminates the `O(1 / ln M)` grid-FFT cusp loss completely:
  - **Gauss-Bonnet total hyperbolic area:** `Area_hyp / (2 pi) = 0.99999999988441` (`err = 1.16e-10` on `18x20`; cold-room Cartesian-excised + log-radial annulus quadrature `0.99990584`, `err = 9.42e-5`, `the same`).
  - **Flat-torus control:** `Area_flat = 1.00000000374431`, `max |K_{E[2]}^{flat} - I_3| = 6.84e-9`, `max |K_{CIM}^{flat} - I_3| = 1.14e-8`.

### 2.2 Exact `2D` Hyperbolic Kahler Overlap Metrics & Impact on `OBS-17` (`Synergy S-1`)
- **`E[2]` even spin-structure basis (`[q_j, q_i, q_k] = [theta_4, theta_2, theta_3]`):**
  - `K_{E[2]}^{hyp}(tau_8^+) = diag(1.3651658547, 0.7607115701, 1.3993044433)`, condition number `kappa_{E[2]} = 1.8394678067` (cold-room disjoint quadrature agrees to `1.71e-4`, `the same`).
- **`M = 3` magnetized-torus CIM basis (`psi^{j, 3}(z; tau_r)`, `j = 0, 1, 2`):**
  - Eigenvalues `(0.5356118561, 0.5406193597, 2.0280687074)`, condition number `kappa_{CIM} = 3.7864522307`, exact `Z_2` parity `K[1,1] = K[2,2]` (`5.02e-11`), `K[0,1] = K[0,2]` (`1.25e-11`), off-diagonal `|K[0,1]| = 0.2377836697`, CP phase `arg K[0,1] = 0.2126356742 rad` (cold-room eigenvalues agree to `3.07e-4`, `the same`).
- **`Synergy S-1` canonicalized `Y^{2D} = (K^{hyp})^{-1/2} Y^{hol} (K^{hyp})^{-1/2}` (`10`-trial `45`-dps Haar `U(3)^3` drift `= 1.99e-34`; cold-room `5`-trial `= 5.88e-39`):**
  - `CKM |V_{12}|`: `0.54003235` (flat) -> **`0.43135272`** (`2D E[2]`, `-20.1%`) -> **`0.35732486`** (`2D CIM`, `-33.8%`).
  - `Y_u` `s_2 / s_3`: `6.6672e-4` (flat) -> **`1.0113e-3`** (`2D E[2]`, `+51.7%`).
  - `Y_e` `s_1 / s_2`: `7.7916e-4` (flat) -> **`7.9258e-4`** (`2D E[2]`, `+1.72%`) -> **`6.4281e-4`** (`2D CIM`, `-17.5%`).
- **Structural Theorem on `OBS-17`:** `2D` hyperbolic Kahler renormalization produces genuine, parameter-free `O(15%-52%)` flavor and CKM shifts that cannot be neglected in precision `Synergy S-1` predictions, while the exact Ostrowski bound `kappa^{-2} <= (s_1/s_3)^{2D} / (s_1/s_3)^{flat} <= kappa^2` (`kappa_{E[2]} = 1.839`, `kappa_{CIM} = 3.786`) simultaneously proves that finite-area `2D` hyperbolic Kahler overlaps alone cannot manufacture multi-order exponential hierarchies.

### 2.3 Exact Three-Seat Leptogenesis CP-Branch Sign Resolution (`tau_*^+` vs `tau_*^-`)
- **Theorem A4 (Exact Unflavored Vanishing Under `1`-Loop Radiative `M_R` Splitting):** For UV-degenerate `M_R(Lambda) = M_0 I_3`, the `1`-loop Antusch RGE shift `delta M_R proportional to -(Y_nu^T Y_nu^* + Y_nu^dag Y_nu) = -2 Re(Y_nu^dag Y_nu)` is purely real-symmetric (`max |Im M_R| = 0.0`). Its Takagi matrix `O_R in O(3)` is therefore real orthogonal, forcing `Hhat_{0j} = i (O_R^T Im(H_nu) O_R)_{0j}` to be purely imaginary, `(Hhat_{0j})^2` purely real, and the **unflavored asymmetry `sum_alpha eps_{1, alpha}` to vanish identically** (`-2.48e-36` flat, `+4.49e-36` `2D E[2]`; cold-room `2.04e-40`, `the same`).
- Thus `100%` of `AGY-C30`'s `Y_B(tau_*^+) > 0` is purely **flavored leptogenesis**: at `tau_*^+`, `eps_{1, tau} = +3.8126e-5 > 0` carries `90.36%` branching ratio (strongest washout, smallest `eta_tau`), whereas `eps_{1, e} + eps_{1, mu} = -3.8126e-5 < 0` carries only `9.64%` branching ratio (weakest washout), so `Y_B = -(8/23) n_eq sum_alpha eps_{1, alpha} eta_alpha = +1.611e-8 > 0` selects **`tau_*^+ = (+2 + i)/5`**.
- **Unification with Tree `M_R(0, 0)` (`A2-OW12`):** On `Synergy S-1` with tree `M_R(0, 0)`, the **unflavored** asymmetry `eps_1(tau_*^+) = +3.7427e-6 > 0` has the **exact same positive sign** as `A2-OW12` (`+5.4538e-6 > 0`, which gives unflavored `Y_B < 0` -> `tau_*^-`), yet strong-washout **flavored** conversion flips the net baryon sign to `Y_B(tau_*^+) > 0` (`+6.11e-14` flat, `+1.31e-11` `2D E[2]`, `+1.06e-8` `2D E[2]` radiative), with exact CP-mirror antisymmetry `Y_B(tau_*^+) + Y_B(tau_*^-) = 0` (`<= 3.14e-42`). Both seats are mathematically `the same` once flavored vs unflavored washout is distinguished!

---

## 3. Task `OW19-B`: `E_6` Non-SUSY Radiative Hierarchy, `7D` CS Axion `Theorem 2`, & Majorana `psi_S` Planck-Suppressed `p`-Wave Dark Matter

1. **`OW19-B1` (`E_6` Non-SUSY Irreducible `1`-Loop `Z'_psi` Higgs Hierarchy Theorem):**
   - On `27 = 16_{+1} + 10_{-2} + 1_{+4}` of `E_6 -> Spin(10) x U(1)_psi`: `Tr_{27}(Q_psi) = 0`, `Tr_{27}(Q_psi^2) = 72`, `T(27) = 3`, fixing GUT normalization `Q_psi^{GUT} = Q_psi / (2 sqrt(6))` (`N_psi^2 = 24`, `(Q_S^{GUT})^2 = 2/3`, `(Q_H^{GUT})^2 = 1/6`, `(Q_{16}^{GUT})^2 = 1/24`) and `M_{Z'_psi}^2 = (4/3) g_{GUT}^2 |<S_{+4}>|^2`.
   - Exact symbolic Coleman-Weinberg differentiation (and disjoint cold-room gauge-box RGE + Landau-gauge `d = 4 - 2 eps` tadpole matching, `the same`) gives `16 pi^2 beta_{lambda_{HS}}|_{Z'_psi} = +(4/3) g_{GUT}^4` and the irreducible `1`-loop shift (present even when tree portals `kappa_S, lambda_{HS}(Lambda) -> 0`):
     `delta m_{H_{u,d}}^2|_{Z'_psi} = -(g_{GUT}^4 / (24 pi^2)) |<S_{+4}>|^2 [ln(Lambda^2 / M_{Z'_psi}^2) + 1/3] = -(g_{GUT}^2 / (32 pi^2)) M_{Z'_psi}^2 [ln(Lambda^2 / M_{Z'_psi}^2) + 1/3] < 0`.
   - Because `Q_psi(H_{u,d}) = -2 != 0` is locked by `E_6` gauge invariance, GUT-scale `<S_{+4}> ~ M_X` incurs a ~`10^{25}` `1`-loop radiative hierarchy wall on `m_{H_{u,d}}^2`, whereas naturalness without SUSY bounds `M_{Z'_psi} <= O(4 pi sqrt(2) / g_{GUT}) v_{EW}`.
2. **`OW19-B2` (`7D` CS Axion `d`-Sheet Invariance — `agy-exp` `Theorem 2`):**
   - Verified symbolically (`ratio_d - ratio_1 == 0`) and at `35` dps across `d in {1, 5, 15}` (`drift = 0.0`; cold-room `d in {1, 2, 5, 7, 15}` `1.43e-42`, `the same`): `f_a^{(d)} / M_{Pl,4}^{(d)} = f_a^{(1)} / M_{Pl,4}^{(1)}` strictly, alongside the exact `11D` Einstein-frame radial exponents `f_a / M_{Pl,4} proportional to R^{-3}` vs `V_Cas proportional to R^{-10}`.
3. **`OW19-B3` (Explicit `4x4` Majorana Clifford Algebra & Dim-`5` Planck-Suppressed `p`-Wave Theorem):**
   - Verified in BOTH Dirac representation (`OW19-B3`) and disjoint Weyl-chiral representation (`REF-B`, `the same`): `(C^{-1} gamma^mu)^T = +(C^{-1} gamma^mu)` forces the Grassmann vector current `bar{psi}_S gamma^mu psi_S == 0` identically, while `(C^{-1} gamma^mu gamma^5)^T = -(C^{-1} gamma^mu gamma^5)` leaves pure axial coupling.
   - Explicit `4x4` CM-frame traces yield `32 E^2 p^2 (cos^2 theta + 1)`, proving the `s`-wave (`v^0`) vanishes identically at `m_f = 0` and yielding exact `p`-wave annihilation cross-sections:
     `sigma v_rel(psi_S psi_S -> 3 x 15_SM) = (5 / (48 pi)) g_{GUT}^4 m_{psi_S}^2 v_rel^2 / (4 m_{psi_S}^2 - M_{Z'_psi}^2)^2`
     and `1 / (9 pi)` for `3 x 16` (`SM + N_R`).
   - **Exact Dim-`5` Cancellation Theorem:** Substituting `M_{Z'_psi}^2 = (4/3) g_{GUT}^2 |<S_{+4}>|^2` and the dim-`5` Majorana mass `m_{psi_S} = c_5 |<S_{+4}>|^2 / M_{11}` (`AGY-C30 E1`, away from the pole `2 m_{psi_S} ~= M_{Z'_psi}`) **cancels BOTH `g_{GUT}^4` and `|<S_{+4}>|^4` identically**:
     `sigma v_rel(3 x 15_SM) = (15 / (256 pi)) (c_5^2 / M_{11}^2) v_rel^2`, `sigma v_rel(3 x 16) = (1 / (16 pi)) (c_5^2 / M_{11}^2) v_rel^2`.
   - **Cosmological Consequence (advancing `AGY-C30` DM open boundary):** Off-resonance `Z'_psi`-mediated thermal WIMP freeze-out of dim-`5` `psi_S` is structurally ruled out (purely `M_{11}^{-2}` Planck-suppressed at every `<S_{+4}>`), pointing directly to freeze-in / super-WIMP or `2 m_{psi_S} ~= M_{Z'_psi}` resonant-pole cosmology.

---

## 4. Task `OW19-C`: Exhaustive Lie-Theoretic `6D` `s = 3` `E[5]` & `Z_2` Twisted Casimir Classification (`OBS-06`, `F-A2-07`)

1. **Exact `2D` Positive-Definite Hessian of `F_3(tau) = E_3(tau) + E_3(5 tau)` at `tau_*^pm = (+-2 + i)/5`:**
   - Analytic `35`-dps Chowla-Selberg (`E3_modular_S_err = 6.02e-36`, `F3_mirror_err = 0.0`) gives `F_3(tau_*^pm) = 9.317827231207686880322`, `|grad F_3(tau_*^+)| = 2.89e-33`, and positive-definite Hessian eigenvalues `lambda_min = +61.11146248`, `lambda_max = +1336.562622`, `det H = +81679.2965` (cold-room direct `2D` Euclidean-ball lattice sum matches `F_3` to `8.12e-9` and Hessian eigenvalues to `6.09e-7`, `the same`). Thus `tau_*^pm` is a genuine `6D` dS minimum iff `C_6^{(E[5], s=3)} = 4(n_F^{(0)} - n_B^{(0)}) - (24/25)(n_F^{(tw)} - n_B^{(tw)}) > 0` (`n_B^{(tw)} - n_F^{(tw)} > (25/6)(n_B^{(0)} - n_F^{(0)})`).
2. **Exhaustive `E_8` Root-Lattice `Z_5` Wilson-Line Census (`3905` tuples across `SU(5), SO(10), E_6, E_7, E_8`; verified independently by cold-room BFS Weyl-reflection orbit from Bourbaki simple roots, `the same`):**

| Group (`dim`, `rank`) | `Z_5` Tuples | Strict `G_SM x U(1)^k` | Pure `6Y` `C_6` (YM / `+3x16` / `+3x27`) | Max Pure-YM `C_6` (`untw, tw`) | Max `+3x16` (`4D` chiral) | Max `+3x27` (`4D` chiral) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `G_SM (12, 4)` | `1` | — | `-192` / `-1272/5` / `-288` | `-192` `(12, 0)` | `-1272/5` | — |
| `SU(5) (24, 4)` | `5` | `0` | `-384` / `-2232/5` / `-480` | `-384` `(24, 0)` | — | — |
| `SO(10) (45, 5)` | `25` | **`8`** | `-1616/5` / `-1928/5` / `-2096/5` | `-2128/25` `(13, 32)` | `-1456/25` | — |
| `E_6 (78, 6)` | `125` | `0` | `-256` / `-1592/5` / `-352` | `-448/25` `(16, 62)` | `-2008/25` | **`+376/25`** |
| `E_7 (133, 7)` | `625` | `0` | `-144` / `-1032/5` / `-240` | `-624/25` `(27, 106)` | **`+544/25`** | `-792/25` |
| `E_8 (248, 8)` | `3125` | `0` | **`0`** / `-312/5` / `-96` | **`0`** `(48, 200)` | **`+432/5`** | **`+1568/25`** |

3. **Four Exact Lie-Theoretic Theorems Proven:**
   - **Pure-YM No-Go & `E_8` Kac-Mark-`5` Criticality:** `max C_6^{YM} <= 0` for every GUT group through `E_8`, with **`E_8 -> SU(5) x SU(5)` (`48` untwisted, `200` twisted, `200 / 48 = 25 / 6` exact!) uniquely saturating `C_6^{YM} == 0`**.
   - **Pure `6Y (mod 5)` Universal No-Go:** Because `6Y(5) === 3 (mod 5)` is central in `SU(5)`, pure `6Y (mod 5)` leaves all `24` `SU(5)` vectors untwisted and keeps `C_6 < 0` across ALL six groups with `3 x 16` or `3 x 27`.
   - **Exceptional Matter-Assisted Rescues vs Clean-Breaking Trade-Off:** `G_SM`, `SU(5)`, and `SO(10) + 3 x 16` (`max -1456/25`) remain strictly `< 0` for EVERY `Z_5` Wilson line; **only exceptional groups `E_6 + 3x27` (`+376/25`), `E_7 + 3x16` (`+544/25`), and `E_8 + 3x16 / 3x27` (`+432/5`, `+1568/25`)** flip strictly positive (`> 0`) under non-hypercharge `Z_5` Wilson lines, while leaving unbroken subgroups strictly larger than `G_SM x U(1)^k` (requiring a secondary `Z_2`/`Z_3` orbifold twist to finish breaking to `G_SM`, whereas `SO(10)` uniquely admits `8` strict `G_SM x U(1)_X` `Z_5` Wilson lines).
   - **`Z_2` Scherk-Schwarz `(-1)^F` Universal No-Go:** At `s = 3`, `2^{1-3} - 1 = -3/4`, so `C_6^{(Z_2-SS)} = -n_B - (3/4) n_F < 0` for every non-empty spectrum.

---

## 5. Planted Fault Controls (`6 / 6` Producer + `6 / 6` Cold-Room Referee)

- **Producer `OW19-D` (`6 / 6` caught):** `PF-OW19-1` metric inversion (`K_inv = +2.936`), `PF-OW19-2` flat-Kahler overwrite (`20.1%` `|V_{12}|`, `51.7%` `Yu s_2/s_3`), `PF-OW19-3` wrong `Q_psi` norm (`Tr = 18/5 != 3`, `CW = 3/50 != 1/24`), `PF-OW19-4` Dirac vector coupling (`s`-wave `E^2 / (2 pi) != 0`), `PF-OW19-5` spurious `sqrt(d)` axion rescaling (`+1.236` at `d = 5`), `PF-OW19-6` naive `E_8` `236/12` miscount (`+17856/25` vs exact `0`).
- **Cold-Room Referee `REF-D` (`6 / 6` caught):** `PF_REF_1` SHA-256 tamper, `PF_REF_2` `EX-S2` `T_2` `3x` bug, `PF_REF_3` Weyl-rep vector `s`-wave, `PF_REF_4` `E_8` `236/12` miscount, `PF_REF_5` positive curvature flip (`+3.743`), `PF_REF_6` inverted `F_3` AdS maximum (`-1336.56, -61.11`).

0 of 19.
