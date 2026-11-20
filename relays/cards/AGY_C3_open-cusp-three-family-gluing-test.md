# Card AGY-C3: Parabolic Milnor–Wood bound and open-cusp chiral boundary index on `T (x) Lambda^even(C^5)` (`MC:GEN`)

*Seat: `agy` (`agy/cusp-action-2026-11-20`, forked from `origin/main` at `60a52d359`). Date: `2026-11-20`. Pre-registered before any script or run (`expectations committed first`). Data-free: `0 of 19`.*

---

## One. Package and question

Register row `MC:GEN` (`B1952`, `B1955`, `B1866`, `Stage 4` `R2`): on the once-punctured torus `Sigma_(1,1)` and open torus cusp of `X_(4_1)`, does tensoring `B1955`'s flux-free level-five dihedral matter module `Lambda^even(C^5)` with the three-dimensional half-form metaplectic family representation `T` (`levels two, four, eight, coprime to five`) earn `three` net chiral four-dimensional families with `zero` inserted `U(1)` magnetic flux, or what exact parabolic-versus-boundary index law governs `N_gen`?

## Two. Deliverables and what done means

- Exact proof and symbolic/numerical check of the Mehta–Seshadri parabolic Riemann–Roch index `N_par(rho) = sum theta_j` (`theta_j in [0, 1)`) for flat unitary bundles on `Sigma_(1,1)` with commutator cusp holonomy `U_infty = [rho(alpha), rho(beta)]`, proving the strict Milnor–Wood bound `N_par in {0, 1, 2}` (`never 3`) for every rank-three flat unitary bundle without `U(1)` flux.
- Explicit evaluation of `U_infty`, its eigenphases `theta_j`, parabolic degree `N_par`, and boundary zero-mode multiplicity `d_infty = dim ker(U_infty minus I)` on `T`, `Lambda^even(C^5)`, and `T (x) Lambda^even(C^5)` across: (a) the base modular punctured torus `H / Gamma'`, (b) the knot-complement Seifert fiber / peripheral longitude (`B1955` Part B), and (c) the level-forty Chinese-Remainder congruence cusp cover `Gamma(8) cap Gamma(5) = Gamma(40)`.
- Exact chiral half-rank cusp Lagrangian (`X:CUSP`) projection and all seven gauge/gravitational anomaly sums on the surviving boundary zero modes.
- Zero-shared-code independent countercheck script (`recomputed independently` + `tested against planted errors`) and mask-clean result relay.

## Three. Pre-committed expectations and how it could come out wrong

- **E1 (parabolic `L^two` no-go at zero flux):** For every pair of unitary `3 x 3` matrices `(U_alpha, U_beta)` in `U(3)`, the canonical parabolic Chern sum `sum_{j=1}^3 theta_j` (`theta_j in [0, 1)`) of `U_infty = [U_alpha, U_beta]` must be an integer in `{0, 1, 2}` and **never** equal `3`; if any flat `U(3)` commutator yields `3`, `E1` is refuted.
- **E2 (base-cusp vs trivialized-cusp dichotomy on `T (x) Lambda^even(C^5)`):** On `Lambda^even(C^5)`, `B1955`'s dihedral longitude holonomy must equal `I_16` (`all sixteen states boundary-massless`); on `T`, non-trivial base-puncture holonomy `U_infty^(T) != I_3` must leave `d_infty < 3`, whereas whenever peripheral holonomy on `T` trivializes (`U_infty^(T) = I_3`, as on the unbranched congruence cusp cover), `ker(U_infty minus I)` on `T (x) Lambda^even(C^5)` has exact complex dimension `3 x 16 = 48` (`signature (48, 48)`) and one family-blind chiral half-rank Lagrangian `X:CUSP` selects `3` anomaly-free `16`-state chiral families at `zero` `U(1)` flux.
- **E3 (Chinese Remainder coprime independence):** On `SL(2, Z / 40 Z) = SL(2, Z / 8 Z) x SL(2, Z / 5 Z)`, the `T`-sector action mod `8` and `W`-sector action mod `5` must commute and factorize with exact group order `|SL(2, Z / 8 Z)| * |SL(2, Z / 5 Z)| = 384 * 120 = 46,080`.

## Four. Premises and firewall boundaries

- Rests on `B1952`/`B1955`'s coprime level-five and half-form modules, Mehta–Seshadri parabolic bundles on `Sigma_(1,1)`, and `X:CUSP` boundary Lagrangian reduction.
- Must **never** read, compute, or compare any of the nineteen empirical Standard Model targets (`0 of 19`), and must leave `origin/agy/audit-2026-11-02` untouched at `4319f47e2`.

## Five. Mandatory planted negative control

1. Close the torus without boundary (`p = 0`, zero curvature) or remove the chiral cusp Lagrangian (`vector-like APS pairing`): the net chiral index **must** vanish identically (`N_chiral = 0`).
2. Drop `nu_R^c` (or corrupt one hypercharge weight) on the surviving `3 x 16` boundary modes: `U(1)_(B-L)^three` (or `U(1)_Y^three`) anomaly cancellation **must** fail (`non-zero residual -3` instead of `0`).

## Six. What is needed from main or other seats

Nothing needed to run; offered as an exact earns-versus-inserts boundary theorem on `MC:GEN`.

0 of 19.
