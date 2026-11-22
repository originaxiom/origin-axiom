# Pre-Registration Card A2-OW19: Exact 2D Punctured-Torus Hyperbolic Kahler Overlaps, E_6 Non-SUSY Hierarchy & Majorana Dark Matter, and Exhaustive Lie-Theoretic 6D s = 3 Twisted Casimir Classification (0 of 19)

- **Seat:** `agy-002`
- **Branch:** `agy-002/verify`
- **Date:** `2026-11-22`
- **Firewall:** strictly `0 of 19` (zero empirical PDG, NuFIT, Planck, DESI, or lattice values anywhere in card, script, output, or report; all computations purely mathematical-physics and dimensionless)
- **Custody Mode:** `expectations committed first`, `tested against planted errors`, pre-hashed script (`SCRIPT_SHA256.txt`) committed before execution, raw unread output (`a2_ow19_results.json` + `OUTPUT_SHA256.txt`) committed before analysis, followed by an isolated cold-room zero-shared-code referee countercheck covering both `A2-PEER-SYNTH v2` (`c161ef045`) and `A2-OW19`.
- **Parent Base:** `0aa02de30` (`Card A2-PEER-SYNTH` published on `origin/agy-002/verify`)
- **Peer Context:** `agy` `AGY-C30` (`528ef1cf5`), `agy-exp` `X-HARVEST-3S-1` (`75cb20177`)

---

## 1. Motivation & Open-Wall Targets

Across the three-seat verification synthesis (`A2-OW18`, `A2-OW16 v5`, `A2-PEER-SYNTH`, `AGY-C30`, `X-HARVEST-3S-1`), four sharp data-free mathematical-physics questions remain open at the heart of the framework:

1. **2D Punctured-Torus Hyperbolic Geometry & Flavor (`OBS-17` / `OBS-18` & Leptogenesis CP-Branch Sign):** Does the exact `2D` complete constant-curvature `K = -1` hyperbolic metric `e^{2 Omega_hyp(z)}` on `E_{tau_8^+} \ {0}` (beyond the `1D` cusp Robin parameter `b_c^*(tau) = pi - L_2(tau)`) produce an exponential hierarchy or an `O(1)` metric renormalization on three-generation torus zero-modes (`E[2]` even spin structures and `M = 3` magnetized-torus CIM modes), and what is the exact algebraic and washout origin of the `tau_*^+` (`AGY-C30`) vs `tau_*^-` (`A2-OW12`) leptogenesis sign split?
2. **`E_6` Non-SUSY Naturalness, `7D` CS Axion Multi-Sheet Invariance, & Majorana `psi_S` Dark-Matter Annihilation (`Bridge B-3S-02` & `AGY-C30` Open Boundary):** In the non-SUSY gauged `E_6 -> Spin(10) x U(1)_psi` completion (`AGY-C30`), what is the irreducible `1`-loop `Z'_psi` radiative Higgs mass shift `delta m_{H_{u,d}}^2`, does `7D` CS axion `f_a / M_{Pl,4}` remain strictly invariant under covering degree `d` (`agy-exp` `Theorem 2`), and what is the exact tree-level annihilation cross-section of the `P_M = -1` Majorana singlet `psi_S in 1_{+4,F}` with dim-`5` Majorana mass `m_{psi_S} = c_5 |<S_{+4}>|^2 / M_{11}`?
3. **Complete Lie-Theoretic `6D` `s = 3` `E[5]` & `Z_2` Twisted Casimir Classification (`OBS-06` & `F-A2-07`):** Given that `G_SM` under `6Y (mod 5)` flips the `6D` `s = 3` `E[5]`-twisted Fricke Casimir negative (`-3864/25`, `-1272/5` AdS maximum at `tau_*^pm`), which simple GUT gauge groups among `G_SM, SU(5), SO(10), E_6, E_7, E_8` and which order-`5` (`Z_5`) inner Wilson lines commuting with `G_SM` (or `Z_2` Scherk-Schwarz `(-1)^F`) can flip `C_6^{(s=3)} > 0` to rescue a genuine `6D` dS minimum at `tau_*^pm`?

---

## 2. Pre-Registered Tasks, Exact Mathematical Definitions, and Pass Gates

All scripts MUST satisfy `0` Python `float` and `0` Python `complex` AST literals (`ast.Constant`), `0` peer or `frontier/` imports, and all six mathematical-physics guardrails (zero hardcoded proof flags; direct matrix verification `< 1e-12`; `10`-trial Haar `U(3)^3` basis-scrambling invariance on all physical flavor observables).

### Task `OW19-A`: Exact `2D` Fuchsian Developing-Map Hyperbolic Metric, Polar-Cusp Gauss-Bonnet Quadrature, `2D` Hyperbolic Kahler Overlaps, and Three-Seat Leptogenesis Sign Resolution

1. **Exact `2D` Developing-Map Metric `e^{2 Omega_hyp(z)}`:**
   - Solve the punctured-torus Fuchsian ODE `u''(z) + (1/4)(wp(z; tau) - c^*(tau)) u(z) = 0` at `35` decimal digits on `tau_8^+ = (16 + 8i)/5` (reduced to the lattice-identical fundamental modulus `tau_r = (1 + 8i)/5`) and on `tau = i sqrt(3)` via the `3`-equation `PSU(1,1)` condition `Im tr(T_a) = Im tr(T_b) = Im tr(T_a T_b) = 0`.
   - Explicitly construct the `SL(2, C)` conjugator `P` (`det P = 1`) mapping `(T_a, T_b)` into `SL(2, R)` (`max |Im(P^{-1} T_{a,b} P)| < 1e-20`), verify `|tr([T_a, T_b]) + 2| < 1e-20`, and evaluate `e^{2 Omega_hyp(z)} = 1 / [Im(u_1(z) conj(u_2(z)))]^2`.
   - **Gates `A1`:** Verify double periodicity `|e^{2 Omega}(z + 1) - e^{2 Omega}(z)| < 1e-12` and `|e^{2 Omega}(z + tau_r) - e^{2 Omega}(z)| < 1e-12`, interior Gaussian curvature `|K(z) + 1| = |e^{-2 Omega} Delta Omega - 1| < 1e-10` at interior test points, and cusp Robin limit `|pi - b_c^*(tau_8^+) - L_2(tau_8^+)| < 1e-6` at `r = 10^{-4}`.
2. **Desingularized Polar-Cusp `2D` Quadrature & Exact Gauss-Bonnet Area:**
   - Parametrize the centered fundamental parallelogram `P_tau = {a + b tau : a, b in [-1/2, 1/2]}` in polar coordinates `(r, theta)` split across its `4` smooth corner sectors, and apply the cusp-desingularizing substitution `t = 1 / (-ln r + b_c^*(tau))` so `d^2z e^{2 Omega_hyp(z)} = W(t, theta) dt dtheta` with `W(t, theta) = (r^2 / t^2) e^{2 Omega_hyp(r e^{i theta})} -> 1` smoothly as `t -> 0^+`.
   - **Gates `A2`:** Verify grid-refined (`12x14` vs `18x20` Gauss-Legendre per sector) flat area `|Area_flat - 1| < 1e-7`, **Gauss-Bonnet total hyperbolic area `|Area_hyp / (2 pi) - 1| < 1e-8`**, and flat-torus mode orthonormality `max |K_{E[2]}^{flat} - I_3| < 1e-7`, `max |K_{CIM}^{flat} - I_3| < 1e-7`.
3. **Exact `2D` Hyperbolic Kahler Overlap Matrices & `Synergy S-1` Flavor Shifts:**
   - Compute `K_{E[2]}^{hyp}(tau_8^+) = diag(K_4, K_2, K_3)` for the three doubly-periodic `E[2]` even spin-structure densities `rho_k(z) = sqrt(2 Im tau) exp(-2 pi (Im z)^2 / Im tau) |theta_k(pi z, q)|^2` (`k = 4, 2, 3` matching `[q_j, q_i, q_k]`), and `K_{CIM}^{hyp}(tau_8^+)` (`3x3` Hermitian positive definite) for the `M = 3` magnetized-torus CIM modes `psi^{j,3}(z; tau)` (`j = 0, 1, 2`).
   - Verify exact Hermiticity, positive definiteness, `Z_2` reflection symmetry `|K_{CIM}[1,1] - K_{CIM}[2,2]| < 1e-8` and `|K_{CIM}[0,1] - K_{CIM}[0,2]| < 1e-8`, and finite `O(1)` condition numbers (`1 < kappa(K_{E[2]}^{hyp}) < 5`, `1 < kappa(K_{CIM}^{hyp}) < 10`).
   - Canonicalize the `Synergy S-1` Yukawa matrices (`Y_u, Y_d, Y_e, Y_nu`) via `Y^{2D} = (K^{hyp})^{-1/2} Y^{hol} (K^{hyp})^{-1/2}`, verify Ostrowski singular-value bounds `kappa^{-1} <= s_i(Y^{2D}) / s_i(Y^{hol}) <= kappa` for all sectors and singular values, and verify **`10`-trial Haar `U(3)^3` basis-scrambling invariance `< 1e-12`** on all extracted mass ratios, CKM/PMNS moduli, Jarlskog invariants, and leptogenesis asymmetries.
4. **Three-Seat Leptogenesis CP-Branch Sign Resolution (`tau_*^+` vs `tau_*^-`):**
   - Prove algebraically and numerically that for UV-degenerate `M_R(Lambda) = M_0 I_3`, the `1`-loop Antusch shift `delta M_R proportional to -(Y_nu^T Y_nu^* + Y_nu^dag Y_nu)` is purely real-symmetric, forcing its Takagi matrix `O_R in O(3)` to be real orthogonal and making the unflavored asymmetry `sum_alpha eps_{1, alpha}` vanish identically (`< 1e-13`), so `AGY-C30`'s `Y_B(tau_*^+) > 0` is purely flavored (`eps_{1, tau} > 0` strongly washed out vs `eps_{1, e} + eps_{1, mu} < 0` weakly washed out).
   - Compare with tree-level `M_R(0,0)` on `Synergy S-1` (both flat and `2D` hyperbolic `E[2]` Kahler), verifying that unflavored `eps_1(tau_*^+) > 0` (matching `A2-OW12`'s unflavored sign) flips sign under flavored strong-washout conversion `Y_B = -(8/23) n_eq sum_alpha eps_{1, alpha} eta_alpha > 0` at `tau_*^+`, with exact CP-mirror antisymmetry `|Y_B(tau_*^+) + Y_B(tau_*^-)| < 1e-13`.

### Task `OW19-B`: `E_6` Non-SUSY Radiative Hierarchy, `7D` CS Axion `d`-Sheet Invariance, and Exact `4x4` Majorana `psi_S` `p`-Wave Dark-Matter Annihilation Theorem

1. **`OW19-B1` (`E_6` Non-SUSY `1`-Loop `Z'_psi` Radiative Higgs Mass Shift):**
   - From `27 = 16_{+1} + 10_{-2} + 1_{+4}` of `E_6 -> Spin(10) x U(1)_psi`, verify `Tr_{27}(Q_psi) = 0`, `Tr_{27}(Q_psi^2) = 72`, `T(27) = T(16) + T(10) + T(1) = 3`, GUT normalization `Q_psi^{GUT} = Q_psi / (2 sqrt(6))` (`(Q_S^{GUT})^2 = 2/3`, `(Q_H^{GUT})^2 = 1/6`, `(Q_{16}^{GUT})^2 = 1/24`), and `M_{Z'_psi}^2 = (4/3) g_{GUT}^2 |<S_{+4}>|^2`.
   - Derive symbolically from the `1`-loop Coleman-Weinberg potential `V_CW = (3 / (64 pi^2)) M_{Z'}(H, S)^4 [ln(M_{Z'}^2 / mu^2) - 5/6]` BOTH the gauge-box mixed-quartic beta function `16 pi^2 beta_{lambda_{HS}}|_{Z'_psi} = +12 g_{GUT}^4 (Q_S^{GUT})^2 (Q_H^{GUT})^2 = +(4/3) g_{GUT}^4` and the irreducible `1`-loop Higgs mass-squared shift:
     `delta m_{H_{u,d}}^2|_{Z'_psi} = -(g_{GUT}^4 / (24 pi^2)) |<S_{+4}>|^2 [ln(Lambda^2 / M_{Z'_psi}^2) + 1/3] = -(g_{GUT}^2 / (32 pi^2)) M_{Z'_psi}^2 [ln(Lambda^2 / M_{Z'_psi}^2) + 1/3] < 0`.
2. **`OW19-B2` (`7D` CS Axion Multi-Sheet Invariance — `agy-exp` `Theorem 2`):**
   - Verify symbolically and at `35` decimal digits across covering degrees `d in {1, 5, 15}` that under a `d`-sheet Riemannian covering `M^{(d)} -> M^{(1)}` with `Vol(M^{(d)}) = d Vol(M^{(1)})` and pullback harmonic `p`-form `omega_d = pi^* omega_1` (`int_{M^{(d)}} omega_d ^ *omega_d = d int_{M^{(1)}} omega_1 ^ *omega_1`), the dimensionless ratio `f_a^{(d)} / M_{Pl,4}^{(d)} = f_a^{(1)} / M_{Pl,4}^{(1)}` is strictly invariant (`0` drift), and verify the exact `11D` radial scaling obstruction `f_a(R) proportional to R^{-3}` vs `V_Cas(R) proportional to R^{-10}`.
3. **`OW19-B3` (Explicit `4x4` Majorana Clifford Algebra & Dim-`5` Planck-Suppressed `p`-Wave Theorem):**
   - Construct explicit `4x4` Dirac gamma matrices `gamma^mu` (`mu = 0..3`), `gamma^5`, and `C = i gamma^2 gamma^0` in `SymPy`; verify `{gamma^mu, gamma^nu} = 2 eta^{mu nu} I_4`, `C gamma^mu C^{-1} = -(gamma^mu)^T`, `C^T = -C`, `(C^{-1} gamma^mu)^T = +(C^{-1} gamma^mu)` (proving Grassmann vector current `bar{psi}_S gamma^mu psi_S == 0` identically), and `(C^{-1} gamma^mu gamma^5)^T = -(C^{-1} gamma^mu gamma^5)` (non-vanishing axial current).
   - Compute the exact tree-level spin-averaged squared amplitude and phase-space cross-section `sigma v_rel` for Majorana `psi_S psi_S -> f_L bar{f}_L` via s-channel `Z'_psi` exchange in the CM frame using explicit `4x4` matrix traces (no hand-coded trace tables!).
   - Prove the `s`-wave (`v^0`) term vanishes identically at `m_f = 0`, derive the exact `p`-wave coefficients `5 / (48 pi)` (`3 x 15` SM Weyl fermions) and `1 / (9 pi)` (`3 x 16` SM+`N_R` Weyl fermions), and prove that substituting `M_{Z'_psi}^2 = (4/3) g_{GUT}^2 |<S_{+4}>|^2` and the dim-`5` Majorana mass `m_{psi_S} = c_5 |<S_{+4}>|^2 / M_{11}` (for `4 m_{psi_S}^2 << M_{Z'_psi}^2`) **cancels both `g_{GUT}^4` and `|<S_{+4}>|^4$ identically**, leaving purely Planck-suppressed `sigma v_rel(3x15) = (15 / (256 pi)) (c_5^2 / M_{11}^2) v_rel^2` and `sigma v_rel(3x16) = (1 / (16 pi)) (c_5^2 / M_{11}^2) v_rel^2`.

### Task `OW19-C`: Exhaustive Lie-Theoretic `6D` `s = 3` `E[5]` and `Z_2` Twisted Casimir Rescue-vs-No-Go Classification (`OBS-06`, `F-A2-07`)

1. **Exact `2D` Positive-Definite Hessian of `F_3(tau) = E_3(tau) + E_3(5 tau)` at `tau_*^pm`:**
   - Directly evaluate the `6D` `s = 3` Epstein-Eisenstein Fricke sum `F_3(tau) = E_3(tau) + E_3(5 tau)` at `35` decimal digits around `tau_*^+ = (2 + i)/5` using Chowla-Selberg / K-Bessel Fourier expansion (completely independent of any direct lattice truncation!).
   - Verify `|grad F_3(tau_*^+)| < 1e-22`, positive-definite `2D` Hessian (`lambda_1 > 0`, `lambda_2 > 0`, `det H > 0`), and `F_3(tau_*^+) = F_3(tau_*^-)` to `< 1e-25`, proving `tau_*^pm` is a genuine `6D` dS minimum iff `C_6^{(E[5], s=3)} > 0`.
2. **Explicit `E_8` Root-Lattice Construction & Exhaustive `Z_5` Wilson-Line Census:**
   - Construct all `240` roots of `E_8` in `Q^8` from scratch (`112` integer + `128` half-integer roots), carve out the nested root subsystems `SU(5)` (`20`), `SO(10)` (`40`), `E_6` (`72`), `E_7` (`126`), `E_8` (`240`), and extract explicit weight systems for `16` of `SO(10)` (`16` weights) and `27` of `E_6` (`27` weights).
   - Exhaustively enumerate ALL order-`5` (`Z_5`) toral Wilson lines commuting with `SU(3)_C x SU(2)_L` across `SU(5)` (`5` valid), `SO(10)` (`25`), `E_6` (`125`), `E_7` (`625`), and `E_8` (`3125`) — `3905` total configurations — and compute exact rational `C_6^{(E[5], s=3)} = 4 (n_F^{(0)} - n_B^{(0)}) - (24/25) (n_F^{(tw)} - n_B^{(tw)})`.
   - **Gates `C1-C4`:** Verify exact theorems:
     - **Pure YM No-Go & `E_8` Kac-Mark-`5` Criticality:** `max C_6^{YM} < 0` for `G_SM (-192)`, `SU(5) (-384)`, `SO(10) (-2128/25)`, `E_6 (-448/25)`, `E_7 (-624/25)`, and **`max C_6^{YM}(E_8) == 0` identically** (`48` untwisted `SU(5) x SU(5)`, `200` twisted, `200/48 = 25/6` exact!).
     - **Pure `6Y (mod 5)` Hypercharge No-Go:** For pure `6Y (mod 5)`, `C_6 < 0` across ALL six groups (`G_SM .. E_8`) with `3 x 16` or `3 x 27` (`2` DOF/Weyl).
     - **Universal `G_SM / SU(5) / SO(10)` No-Go & Exceptional Matter-Assisted Rescues:** Even over ALL `Z_5` Wilson lines, `SU(5)` has `0` breaking solutions to `G_SM`, `SO(10) + 3 x 16` has `max C_6 = -1456/25 < 0`, while **`E_6 + 3 x 27` (`+376/25`), `E_7 + 3 x 16` (`+544/25`), `E_8 + 3 x 16` (`+432/5`), and `E_8 + 3 x 27` (`+1568/25`)** flip strictly positive (`> 0`), with none of `E_6, E_8` breaking cleanly to `G_SM x U(1)^k` under a single `Z_5` twist (leaving larger unbroken subgroups requiring a secondary orbifold twist).
     - **`Z_2` Scherk-Schwarz `(-1)^F` Universal No-Go:** Verify `2^{1-3} - 1 = -3/4` so `C_6^{(Z_2-SS)} = -n_B - (3/4) n_F < 0` for all non-empty spectra.

### Task `OW19-D`: `6 / 6` Planted Fault Controls (`tested against planted errors`)

1. **`PF-OW19-1` (`2D` Metric Curvature Sign Flip):** Inverting `e^{2 Omega} -> e^{-2 Omega}` flips Gaussian curvature `K = -1` to `K = +1` and destroys `K = -1` and Gauss-Bonnet area `2 pi`.
2. **`PF-OW19-2` (Flat-Kahler Overwrite on `Synergy S-1`):** Replacing `K_{E[2]}^{hyp}` with `I_3` erases the `20.1%` CKM `|V_{12}|` and `51.7%` `Yu` `s_2/s_3` `2D` hyperbolic Kahler shifts.
3. **`PF-OW19-3` (Wrong `E_6` `Q_psi` Normalization):** Using unnormalized `Q_psi` (or wrong `N_psi^2 = 20` instead of `24`) violates `Tr_{27}((Q^{GUT})^2) = T(27) = 3` and alters the `1`-loop `Z'_psi` radiative shift coefficient `1/24`.
4. **`PF-OW19-4` (Dirac Vector Instead of Majorana Axial Coupling):** Replacing `gamma^mu gamma^5` with vector `gamma^mu` generates a non-vanishing `s`-wave (`v^0`) term `E^2 / (2 pi) != 0` instead of pure `p`-wave `E^2 v^2 / (12 pi)`.
5. **`PF-OW19-5` (Spurious `sqrt(d)` Axion Rescaling):** Multiplying `f_a^{(1)} / M_{Pl,4}^{(1)}` by `sqrt(d)` at `d = 5` breaks `Theorem 2` `d`-invariance by factor `sqrt(5) - 1 > 1.23`.
6. **`PF-OW19-6` (Naive Untwisted `236/12` `E_8` `6Y` Miscount vs Exact Root-Lattice `200/48`):** Claiming `236` twisted / `12` untwisted `E_8` vectors under `6Y (mod 5)` gives a false positive `C_6^{YM} = +2752/5 > 0`, whereas the exact `E_8` root lattice has `48` untwisted / `200` twisted (`C_6^{YM} == 0`), catching any hand-waving root miscount!

---

## 3. Non-Negotiable Acceptance Gates

`A2-OW19` passes iff:
- `verify_a2_ow19.py` has `0` AST `float` / `complex` literals, `0` peer or `frontier/` imports, pre-hashed in `SCRIPT_SHA256.txt` before execution, raw output sealed in `OUTPUT_SHA256.txt` before inspection;
- All four task gates (`gate_a`, `gate_b`, `gate_c`, `gate_d`) and all `6 / 6` planted faults evaluate to `True` with `all_gates_passed == True`;
- An independent cold-room zero-shared-code referee (`relays/a2_ow19_referee/referee_a2_ow19.py`) reproduces every theorem in BOTH `A2-PEER-SYNTH v2` (`c161ef045`) and `A2-OW19` with `0` substantive discrepancies and `6 / 6` referee planted faults caught.
