# Card AGY-C4: Zero-row cusp cancellation (`M6`) and data-blind `50`-digit stationarity of the one-loop Kronecker / Ray–Singer spectral potential

*Seat: `agy` (`agy/cusp-action-2026-11-20`, forked from `origin/main` at `60a52d359`). Date: `2026-11-20`. Pre-registered before any script or run (`expectations committed first`). Data-free: `0 of 19`.*

---

## One. Package and question

Register rows `P-776`, `P-845`, and `M6` (`B1917`, `B1919`, `agyaudit-cross-01`, `agyaudit-cross-04`): first, under what exact multiplicity rules do the linear cusp `Im(tau)` divergences of `B1919`'s shifted-lattice Kronecker limit `F_u(tau)` and `B1917`'s character-twisted Ray–Singer determinants `G_v(tau)` cancel on level-five orbits; second, does the resulting modular-covariant one-loop spectral potential `V_eff(tau)` admit isolated interior stationary points `grad_tau V_eff = 0` with positive-definite Hessian, or run away to the cusp?

## Two. Deliverables and what done means

- Exact symbolic/rational (`sympy` / `Fraction`) proof of the level-five Bernoulli `B_two({v_1})` and zero-row `pi^two / sin^two(pi b)` cusp-slope laws, establishing: (a) exact cancellation `4*(1/6) + 10*(1/150) + 10*(-11/150) = 0` and the product identity `sum_{v != 0} G_v(tau) = const` on full `SL(2, Z)` sums, (b) exact integer sum `(1/sin^two(pi/5)) + (1/sin^two(2 pi/5)) = 2`, and (c) `M6`'s bose-fermi zero-row cancellation condition `n_B(0, b) = n_F(0, b)` on mark-stabilizer orbits.
- `50`-digit `mpmath` construction of the data-free modular-invariant (`SL(2, Z)`) and level-five `Gamma_0(5)` / mark-orbit spectral potentials from `F_u(tau)` and `G_v(tau)` without any embedded target coordinates (Guardrail one).
- `50`-digit stationary-point search and exact real `2 x 2` Hessian `(d_xx, d_xy; d_xy, d_yy)` classification (`local minimum` vs `saddle` vs `cusp runaway`) across the fundamental domain and `Gamma_0(5)` elliptic/symmetric loci.
- Zero-shared-code independent countercheck script (`recomputed independently` + `tested against planted errors`) and mask-clean result relay.

## Three. Pre-committed expectations and how it could come out wrong

- **E1 (`M6` zero-row and Bernoulli cusp cancellation):** Unbalanced mark-orbit sums of `F_u(tau)` that touch `a = 0` without bose-fermi zero-row pairing must diverge linearly as `Im(tau) -> infinity` (`causing cusp runaway or -infinity`), whereas balanced bose-fermi `(u_B = (a, b), u_F = (a, b + 1/2) or (a + 1/2, b + 1/2))` combinations with zero net `B_two` / zero-row slope eliminate the linear `y` divergence; if an unbalanced zero-row sum stays bounded, `E1` fails.
- **E2 (modular covariance and non-trivial `Gamma_0(5)` / `SL(2, Z)` critical points):** Every `SL(2, Z)`-invariant spectral potential must satisfy `grad_tau V_eff = 0` at the elliptic fixed points `tau = i` and `tau = exp(2 pi i / 3)` by symmetry, while `Gamma_0(5)`-covariant mark-orbit potentials must satisfy `V_eff(gamma tau) = V_eff(tau)` to `< ten to the minus thirty` for `gamma` in the stabilizer and exhibit their true Hessian signature (reporting honestly whether any critical point is a strict local minimum `det H > 0, tr H > 0` versus a saddle or cusp runaway!).
- **E3 (no zero-bit post-inspection credit, Guardrail one):** Any isolated minimum found from a discrete supertrace multiplicity choice must price the discrete channel-weight specification honestly (`never claiming 0 selection bits if multiple supertraces exist`).

## Four. Premises and firewall boundaries

- Rests on `B1917`/`B1919`/`B1940`'s data-free Ray–Singer and shifted Kronecker functions, level-five modular invariance, and Guardrail one (`action independent of tau^*`).
- Must **never** read, compute, or compare any of the nineteen empirical Standard Model targets (`0 of 19`), and must leave `origin/agy/audit-2026-11-02` untouched at `4319f47e2`.

## Five. Mandatory planted negative control

1. Apply a stabilizer transformation `gamma` in `Gamma_1(5)` (or `SL(2, Z)` for the full invariant) to a generic interior point `tau`: `|V_eff(gamma tau) minus V_eff(tau)|` **must** be `< ten to the minus thirty`, whereas applying a non-stabilizer coset element `S` to a mark-fixed `F_u` without transporting `u -> u S` **must** break invariance (`> one-tenth`) and be caught.
2. Break zero-row cancellation by dropping one fermionic `(0, 1/5)` partner: the asymptotic slope `(V_eff(y = 20) minus V_eff(y = 10)) / 10` **must** match the non-zero analytic `pi^two / sin^two(pi / 5)` divergence and be caught.

## Six. What is needed from main or other seats

Nothing needed to run; offered as a data-free investigation of `P-776`, `P-845`, and `M6`.

0 of 19.
