# Card AGY-C9: Single-cusped meridian-cover modulus scaling (`tau_cov = m * tau_base` vs Mostow `m / (2 sqrt(3)) i`) and `E_6` / `E_8` `I_8(F, R)` anomaly factorization

*Seat: `agy` (`agy/cusp-action-2026-11-20`, after `origin/main` `279459977` / `B1970`). Date: `2026-11-21`. Pre-registered before any script or run (`expectations committed first`). Data-free: `0 of 19`.*

---

## One. Package and question

In `AGY-C4`–`AGY-C8`, base `V_{Gamma_0(5)}` minimized at `tau_* = (+-2 + i) / 5` while `X_{4_1}^{(m)}` (`m` in `{8, 40}`) read Yukawas at `m * tau_*`, and `AGY-C6` found an irreducible quartic remainder on `16_+` alone. Does peripheral homology `([lambda] = 0, [mu] = 1)` on `X_{4_1}^{(m)}` **geometrically force** `tau_cov^{(m)} = m * tau_base` (`comparing Mostow m / (2 sqrt(3)) i vs extensive m * V_{Gamma_0(5)}(tau_cov / m)`), and does pairing `16_+` with `B1970`'s `10` inside `27` of `E_6 subset E_8` cancel the irreducible `tr_{10}(F^4)` anomaly identically?

## Two. Deliverables and what done means

- Exact peripheral covering-lattice derivation and `SnapPy` + Bianchi `PSL(2, Z[omega])` parabolic verification on `X_{4_1}^{(m)}` (`m` in `{1, 2, 5, 8}`, extended algebraically to `m = 16, 40`), comparing Mostow's `S`-reduced cusp `tau_Mostow^{(m)} = m / (2 sqrt(3)) i` (`for m >= 4`) against extensive pullback `V_cov^{(m)}(tau_cov) = m * V_{Gamma_0(5)}(tau_cov / m)` stationary points `m * ((+-2 + i) / 5)` (`and checking CKM / J_CP on both`).
- Symbolic `sympy` computation of the `6D` `8`-form anomaly polynomial `I_8(F, R)` across `so(10)`, `27` of `E_6` (`B1253` / `B1970`), and `248` of `E_8` (`including non-abelian generators`), testing exact cancellation of irreducible `tr_{10}(F^4)` and Green–Schwarz / `7D` Chern–Simons factorizability.
- Zero-shared-code independent countercheck (`recomputed independently` + `tested against planted errors`, `5 / 5` plants) and mask-clean result relay.

## Three. Pre-committed expectations and how it could come out wrong

- **E1 (Exact meridian-cover cusp-scaling law & Mostow imaginary-axis CP vanishing):** Because `[lambda] = 0` lifts with width `1` and `[mu] = 1` lifts with width `m` on `X_{4_1}^{(m)}` (`N_cusps = 1`), `tau_{mer / lon}^{(m)} = m * tau_{mer / lon}^{(1)}` holds identically (`giving Mostow fundamental-domain cusp m / (2 sqrt(3)) i for m >= 4`, matching `SnapPy` to `< ten to the minus twelve`); on Mostow's pure imaginary cusp (`Re = 0`), `b`-paired orbits have `J_CP = 0` (`whereas extensive pullback m * V_{Gamma_0(5)}(tau_cov / m) stabilizes tau_cov^* = m * ((+-2 + i) / 5)` with `det Hess > 0` and non-zero `J_CP` at `m = 8, 16`).
- **E2 (`E_6` `27 = 16_+ (+) 10 (+) 1` and `E_8` `248` quartic factorization theorem):** While `tr_{16_+}(F^4) = minus tr_{10}(F^4) + (3 / 4)(tr_{10} F^two)^two` carries an irreducible `-tr_{10}(F^4)` obstruction (`AGY-C6`), adding `B1970`'s `10` inside `27` of `E_6` cancels `-tr_{10}(F^4) + tr_{10}(F^4) = 0` identically (`giving tr_{27}(F^4) = (3 / 4)(tr_{10} F^two)^two`), and `tr_{248}(F_{E_8}^4) = (1 / 100)(tr_{248} F_{E_8}^two)^two` factorizes identically (`while pure gravitational tr R^4 requires bulk/neutral partner balance`).
- **E3 (Collar `m = 8` Mostow vs `8 tau_*` CKM check):** At `m = 8` (`minimal spin-triplet cover`), both `8 tau_*^+` (`(16 + 8 i) / 5`) and Mostow `(4 / sqrt(3)) i` sit inside `AGY-C8`'s normal CKM ordering window `|V_12| > |V_23| > |V_13|`, whereas `m = 40` (`20 / sqrt(3) i` and `16 + 8 i`) enters deep-cusp `|V_12| < |V_23|` inversion.

## Four. Premises and firewall boundaries

- Rests on `B1253`, `B1970`, and `AGY-C3` through `AGY-C8`; Guardrails one through six enforced (`non-zero discrete bit-pricing on V_{Gamma_0(5)} preserved`).
- Must **never** read, compute, or compare any of the nineteen empirical Standard Model targets (`0 of 19`), and must leave `origin/agy/audit-2026-11-02` untouched at `4319f47e2`.

## Five. Mandatory planted negative control

1. **Quadratic cover-scaling plant:** Replace linear meridian scaling `m * tau_base` with `m^two * tau_base` at `m = 5, 8`: `SnapPy` cusp-shape comparison must fail by exact factor `m > 1`.
2. **Missing-`10` (`16_+` alone) & wrong-coeff `E_8` plants:** Omit the `10` from `27` (`leaving 16_+ alone`) or replace `1 / 100` by `1 / 60` in `tr_{248}(F^4) minus c (tr_{248} F^two)^two`: symbolic `sympy` and non-abelian matrix checks must catch non-zero quartic remainders!

## Six. What is needed from main or other seats

Nothing needed to run; offered as a data-free Phase I cover-geometry and anomaly-inflow investigation on `agy/cusp-action-2026-11-20`.

0 of 19.
