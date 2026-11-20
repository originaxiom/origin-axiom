# Card AGY-C5: Bulk-to-boundary derivation of `X:HOL` (`B1936` resolution and doublet-triplet splitting) and holomorphic `(S, S)` Yukawa structure at `tau_* = (+-2 + i) / 5`

*Seat: `agy` (`agy/cusp-action-2026-11-20`, extending `7fda1d1c8` from `origin/main` `60a52d359`). Date: `2026-11-20`. Pre-registered before any script or run (`expectations committed first`). Data-free: `0 of 19`.*

---

## One. Package and question

Register rows `P-847`, `P-866`, `P-776`, `B1936`, and `B1938`: does the `E_8 -> SO(10) x SU(4)` Clifford algebra with `B1955`'s meridian parity `P = rho_W(minus I_2)` and holomorphic cusp involution `iota_inv : z -> minus z` (`iota_inv^*(dz) = minus dz`) derive `X:HOL` (`excluding S_tilde` and killing `3_{-2} (+) 3_bar_{+2}` while keeping `(H_u, H_d)`), and how do `(S, S)` mass ratios, CKM alignment, and geometric Jarlskog CP behave at `m * tau_*` (`m` in `{1, 5, 8, 40}`) for `tau_* = (+-2 + i) / 5`?

## Two. Deliverables and what done means

- Explicit `32 x 32` `Spin(10)` Clifford script on `Lambda*(C^5)` verifying `B(Psi_L, (eps(H_5) + iota(H_5bar)) Psi_R)` (`showing B1936's (up S_tilde, down S) comes solely from H_5 = conj(H_5bar)`), gauge breaking `su(5) -> G_SM` (`dim 12`) and `so(10) -> Pati-Salam` (`dim 21`, intersecting `u(5)` in `dim 13 = G_SM x U(1)_{B-L}`), `(1, 0)`-form doublet-triplet projection `P Phi_H = minus Phi_H` (`n_H = 2, n_T = 0`, matching `ker(B)` of `B1955`'s `3 x 5` cusp-sheet incidence matrix), and Kawamura's bulk-`16` splitting (`16 = 6 (+) 10`).
- `50`-digit `mpmath` evaluation of `(S, S)` vs `(S_tilde, S)` singular-value ratios `(m_1 / m_2, m_2 / m_3)`, CKM diagonal alignment `min_k |V_kk|`, and basis-invariant CP commutator `Im det[Y_u Y_u^dag, Y_d Y_d^dag]` across `m * tau_*` (`m` in `{1, 5, 8, 40}`) for `tau_*^{+-} = (+-2 + i) / 5`, checked under Guardrail three Haar basis scrambling (`< ten to the minus twelve`).
- Zero-shared-code independent countercheck script (`recomputed independently` + `tested against planted errors`) and mask-clean result relay.

## Three. Pre-committed expectations and how it could come out wrong

- **E1 (`X:HOL` Clifford derivation, doublet-triplet projection, and bulk-`16` obstruction):** Under `iota_inv : z -> minus z` (`[d_bar_z, iota_inv^*] = 0` on `H`), holomorphic `(1, 0)`-modes `Phi_H dz` in `10_{SO(10)} = 5 (+) 5_bar` must satisfy `P Phi_H = minus Phi_H`, killing `3_{-2} (+) 3_bar_{+2}` (`n_T = 0`) and retaining `(H_u, H_d)` (`n_H = 2`, slope `9 / 5`, `(up S, down S, leptons S)`), while `P_hat` on `16 = Lambda^even(C^5)` splits `(Q_L, L_L)` from `(u^c, d^c, e^c, nu^c)` (`forcing unsplit 16 families onto the cusp boundary`).
- **E2 (cover-depth hierarchy vs shallow base at `tau_* = (+-2 + i) / 5`):** On the shallow base `m = 1` (`Im = 1 / 5`) and five-sheeted cover `m = 5` (`Im = 1`), `(S, S)` ratios are expected to be non-cuspidal (`order one-hundredth to one`), whereas on `AGY-C3`'s cusp-unwrapping cover `m = 8` (`Im = 8 / 5`) and joint level-forty cover `m = 40` (`Im = 8`), `(S, S)` must enter `B1945`'s exponential hierarchy regime with `min_k |V_kk| > 99 / 100` at `m = 40`.
- **E3 (spontaneous geometric CP conjugation across `tau_*^{+-}`):** For purely real Higgs directions `(h_u, h_d)` in `R^3` on row-marks `(a, 0)`, integer-real cover moduli `m` in `{5, 40}` (`Re(m tau_*)` in `Z`) must conserve CP (`J_CP = 0` to `< ten to the minus thirty`), whereas fractional-real moduli `m` in `{1, 8}` (`Re(m tau_*)` not in `(1 / 2) Z`) must satisfy exact Fricke CP conjugation `J_CP(tau_*^-) = minus J_CP(tau_*^+)` while preserving all singular values and `|V_ij|` to `< ten to the minus thirty`.

## Four. Premises and firewall boundaries

- Rests on `B1936`, `B1938`, `B1940`, `B1945`, `B1951`, `B1955`, and `AGY-C1` through `AGY-C4`; Guardrails one through six enforced throughout.
- Must **never** read, compute, or compare any of the nineteen empirical Standard Model targets (`0 of 19`), and must leave `origin/agy/audit-2026-11-02` untouched at `4319f47e2`.

## Five. Mandatory planted negative control

1. **Scalar parity and `B1936` reality plant:** Flip `iota_inv^*(dz) = minus dz` to `+dz`: the surviving modes in `10_{SO(10)}` **must** invert to `(n_H, n_T) = (0, 2)` (`color triplets only, gauge slope 56 / 25 != 9 / 5`), and imposing `B1936`'s non-holomorphic identification `H_5 = conj(H_5bar)` **must** restore `(S_tilde, S)` CKM derangement at `m = 40`.
2. **Guardrail three right-handed basis-leakage plant:** Apply independent Haar random unitaries `U_L, U_{R,u}, U_{R,d}` in `U(3)` (`Y_u -> U_L Y_u U_{R,u}^dag`, `Y_d -> U_L Y_d U_{R,d}^dag`): `|V_CKM|`, `|J_CP|`, and `Im det[Y_u Y_u^dag, Y_d Y_d^dag]` **must** stay invariant to `< ten to the minus twelve`, whereas the planted right-handed commutator `Im det[Y_u^dag Y_u, Y_d^dag Y_d]` **must** vary by order one and be caught.

## Six. What is needed from main or other seats

Nothing needed to run; offered as a data-free continuation on `agy/cusp-action-2026-11-20` addressing the open premises in Section Four of our synthesis relay (`7fda1d1c8`).

0 of 19.
