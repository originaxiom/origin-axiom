# Card AGY-C20: Joint Ray-Singer / Quillen Determinant Derivation of V_{Gamma_0(5)}, Open Weight-Ratio Stability Window, and Spontaneous CP Hand Equivalence

1. **The package and the question, in a sentence:** Under wave two's source-dynamics (`WP-2` fifth), modulus (`WP-4` first), and hand (`WP-1` fourth) packages, does the zeta-regularized Ray-Singer / Quillen Laplacian determinant on the base cusp torus `E_tau` paired with its five-sheeted dihedral cover `E_{5 tau}` derive `V_{Gamma_0(5)}(tau)` with confining fermionic Casimir sign (`N_F^{per} > N_B^{per}`), stabilize `tau_* = (+-2 + i) / 5` over a finite open interval of cover-to-base weight ratios `w_5 / w_1`, and establish exact `CP`-mirror equivalence between `tau_*^+` and `tau_*^-` across all twenty-two observables?

2. **What will be delivered, and what done means:** A pre-registered, hashed `0 of 19` script `relays/agy_2026-11-21_c20/c20_quillen_gamma0_5_and_cp_hand.py`, raw output, a zero-shared-code countercheck `c20_countercheck.py` with five planted negative controls, and a mask-clean relay testing:
   - **Expectation E1 (Coordinate-Free Ray-Singer / Quillen Derivation & Fermionic Casimir Sign):** Verify from Kronecker's limit law `det' Delta_{E_tau} = (2 pi)^two y^two |eta(tau)|^4` (`Quillen norm y |eta(tau)|^4`) that `(N_F^{per} minus N_B^{per}) * [-1 / 2 ln(det'_{E_tau} det'_{E_{5 tau}})]` yields `(N_F^{per} minus N_B^{per}) * [-ln(y sqrt(5) |eta(tau) eta(5 tau)|^two)]` (`zero coordinate insertion`), with `96` real fermionic minus `32` periodic bosonic DoF giving `+64 > 0` (`confining +y Casimir wall, Delta_{H^2} > 0`).
   - **Expectation E2 (`Gamma_0(5)` Elliptic Stationarity & Open Stability Window `w_5 / w_1 in (r_min, r_max)`):** Prove `gamma_* = [[2, -1], [5, -2]] in Gamma_0(5)` (`order 4, trace 0`) fixes `tau_*^+ = (2 + i) / 5`, forcing `grad V_{w_1, w_5}(tau_*^+) == 0` identically for **every** `(w_1, w_5)` on `-w_1 ln(y |eta(tau)|^4) - w_5 ln(5 y |eta(5 tau)|^4)`, and compute the exact open interval `(r_min, r_max)` around Fricke-self-dual `w_5 / w_1 = 1` where `det Hess(tau_*^+) > 0` (`retaining 1 honest Guardrail-1 bit`).
   - **Expectation E3 (`50`-Digit Spontaneous `CP` Hand Equivalence Between `tau_*^+` and `tau_*^-`):** Run the full zero-knob `UV` (`AGY-C16` collar + `s = 2` weave) and `IR` (`AGY-C17` `2`-loop `GHU`) pipeline on both `tau_*^+ = (+2 + i) / 5` and `tau_*^- = (-2 + i) / 5`, verifying all `20` `CP`-even mass/angle/quartic observables agree identically while `J_{CP}(CKM)` and `J_{CP}(PMNS)` negate (`J(tau_*^-) == -J(tau_*^+)`, `Strong-CP == 0` on both).

3. **How it could come out wrong, written before any run:**
   - **F1:** Periodic bosonic degrees of freedom could outnumber periodic fermionic degrees of freedom (`N_B^{per} >= N_F^{per}`), flipping `-ln(y |eta|^4)` into `+ln(y |eta|^4)` and causing cusp runaway `y -> infinity`.
   - **F2:** Positive-definite Hessian `det Hess > 0` at `tau_*` could require fine-tuning `w_5 / w_1` to a measure-zero point rather than holding across a finite open interval `(r_min, r_max)` containing `1`, or symmetrizing over all `6` cosets of `SL(2, Z) / Gamma_0(5)` without a fixed dihedral cover mark could move the minimum to `exp(pi i / 3)`.
   - **F3:** Subleading `2`-loop or `t = 4` weave BCH terms could break `CP` mirror symmetry between `tau_*^+` and `tau_*^-` on one of the `CP`-even mass ratios or mixing moduli.

4. **What it rests on, and what it must not touch:** Rests on `AGY-C1` through `AGY-C19` on `agy/cusp-action-2026-11-20`, aligned with `origin/main` at `279459977`. Must not touch `main`, `agy/audit-2026-11-02`, or any measured Standard Model datum (`0 of 19`).

5. **Controls that must fail if the work is broken:**
   - **Control 1 (Pure-bosonic sign flip `N_F = 0, N_B = 32`):** Must invert `V` so `tau_*` becomes a local maximum (`tr Hess < 0`) and `V -> -infinity` toward the cusp.
   - **Control 2 (Single-sheet `(w_1, w_5) = (1, 0)` or `(0, 1)` saddle & `6`-coset `SL(2, Z)` restoration):** At `(1, 0)` and `(0, 1)`, `tau_*` is `SL(2, Z)`-equivalent to `i` and must be a saddle (`det Hess < 0`); summing all `6` cosets shifts the minimum to `exp(pi i / 3)`.
   - **Control 3 (Asymmetric `Re(tau)` shift `+2 / 5 -> -3 / 10` or `0`-bit post-inspection claim):** Breaking mirror conjugacy `tau_*^- != -conj(tau_*^+)` breaks `CP`-even observable equality, and claiming `0` bits on `V_{Gamma_0(5)}` must trigger Guardrail `1`.

6. **What is needed from main or from another seat:** `main` (`wave two's source-dynamics, modulus, and hand packages`) can verify the exact `(r_min, r_max)` Hessian stability window and carry both `CP`-conjugate branches `tau_*^{+-}` (`0 of 19`).

0 of 19.
