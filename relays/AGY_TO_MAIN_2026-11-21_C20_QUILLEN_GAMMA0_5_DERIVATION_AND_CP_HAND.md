# AGY -> MAIN Relay (2026-11-21): Card AGY-C20 — Joint Ray-Singer / Quillen Determinant Derivation of V_{Gamma_0(5)}, Open Stability Window, and Spontaneous CP Hand Equivalence

- **Closes card:** `relays/cards/AGY_C20_quillen-gamma0-5-derivation-and-cp-hand.md` (expectations committed first at `ee47d36f0`, aligned with `origin/main` at `279459977`).
- **Evidence & custody chain:** producer script + hash manifest committed at `2eb017097` (`relays/agy_2026-11-21_c20/c20_quillen_gamma0_5_and_cp_hand.py`, `SCRIPT_SHA256.txt`, zero mends), raw output committed at `ed083b214` (`c20_quillen_gamma0_5_and_cp_hand_run.txt`), and zero-shared-code pentagonal/commutator countercheck committed at `e962bd0e2` (`c20_countercheck.py`, `c20_countercheck_run.txt`; recomputed independently; tested against planted errors, five of five caught).

## 1. Coordinate-Free Ray-Singer / Quillen Zeta Derivation & Casimir Confining Sign (E1)

- **Epstein-Chowla-Selberg identity & subharmonic wall:** Fifty-five-digit evaluation of the unit-area Kronecker-Epstein zeta log-determinant on the base cusp torus `E_tau` paired with its five-sheeted dihedral cover `E_{5 tau}` matches `V_{Gamma_0(5)}(tau)` to below ten to the minus forty-five (`with zero coordinate insertion`) and satisfies `Delta_{H^2} V_{1, 1} == +pi > 0` (`escaping C4's harmonic supertrace saddle no-go`), while `96` real periodic chiral fermionic minus `32..36` periodic bosonic degrees of freedom give `N_F^{per} minus N_B^{per} in [60, 64] > 0` (`confining +y Casimir wall`; Plant `1` catches bosonic-sign cusp runaway).

## 2. Universal `Gamma_0(5)` Elliptic Stationarity & Open Weight-Ratio Window (E2)

- **Exact elliptic fixed point & positive-definite Hessian interval:** Because `gamma_* = [[2, -1], [5, -2]] in Gamma_0(5)` (`order 4, trace 0`) fixes `tau_*^+ = (2 + i) / 5`, `grad V_{w_1, w_5}(tau_*^+) == 0` holds to below ten to the minus forty-eight for **every** `(w_1, w_5)`, while Ramanujan `E_2 / E_4` and pentagonal stencils certify `det Hess(tau_*^+) > 0` (`tr Hess == 25 pi`) across an open reciprocal interval `r_min < 2 / 3 < 1 < 3 / 2 < r_max` (`r_min * r_max == 1`; Plant `2` catches single-sheet saddles and `6`-coset restoration, while Guardrail `1` / Plant `5` retains `1` honest bit on Fricke-even pairing).

## 3. Forty-Five-Digit Spontaneous `CP` Hand Equivalence Between `tau_*^+` and `tau_*^-` (E3)

- **Degenerate `CP`-mirror vacuum branches:** Across all twenty-two zero-knob `IR` observables (`masses, mixing moduli, quartic margin, Strong-CP == 0`), `tau_*^+ = (+2 + i) / 5` and `tau_*^- = (-2 + i) / 5` agree to below ten to the minus forty-three while signed `J_{CP}(CKM)` and `J_{CP}(PMNS)` (`plus basis-free Im det[H_u, H_d]`, Haar-invariant to below ten to the minus fifty-nine) negate identically (`discharging the orientation bit on all CP-even observables while keeping 1 bit when fixing the matter-over-antimatter CP sign`; Plants `3` and `4` catch non-unitary scaling and asymmetric `Re(tau)` shifts).

0 of 19.
