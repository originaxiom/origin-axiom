# Card AGY-C6: `7D` Clifford audit of `X:CUSP`, commutator vs meridian cover cusp-multiplicity theorems, and `6D` pillowcase anomaly inflow

*Seat: `agy` (`agy/cusp-action-2026-11-20`, extending `ba82741a6` from `origin/main` `60a52d359`). Date: `2026-11-20`. Pre-registered before any script or run (`expectations committed first`). Data-free: `0 of 19`.*

---

## One. Package and question

Register rows `MC:GEN`, `B1677`, `B1938`, and `AGY-C3`: first, can `X:CUSP` arise as a `Spin(3, 1)`-invariant self-adjoint Lagrangian boundary condition of a free `7D` Dirac operator on `M_4 x X_{4_1}`, or does `Gamma^r = Gamma_{4D} Gamma_{T^2}` force net chiral index `0` without `6D` orbifold / `7D` Chern–Simons anomaly inflow; second, does unwrapping the level-eight / level-forty cusp holonomy multiply the number of cusps (`inflating 3 families by N_cusps`) or collapse back to `1` under Shapiro deck transfer?

## Two. Deliverables and what done means

- Explicit `8 x 8` `Spin(6, 1)` Clifford and Sylvester-inertia script proving that `[Gamma_{4D}, Gamma^r] = 0` and `Gamma^r = eps_{7D} Gamma_{4D} Gamma_{T^2}` (`correcting AGY-C3's off-diagonal Gamma^r toy basis`), so every `Spin(3, 1)`-invariant self-adjoint Lagrangian `L = L_L (+) L_R` in `7D` satisfies `dim L_L = dim L_R` (`net 4D chiral index 0`).
- Exhaustive permutation-cover census on `Sigma_{1, 1}` (`1 <= d <= 6`, plus congruence covers `Gamma(8)` and `Gamma(40)`) alongside `SnapPy` / homology cyclic covers `X_{4_1}^{(m)}` (`m` in `{2, 5, 8, 40}`), proving both the **Even-Cycle Commutator Cusp Theorem** on `Sigma_{1, 1}` (`N_cusps` is even `>= 2`, while deck-invariant Shapiro transfer collapses back to `1`) and the **Single-Cusp Meridian Cover Theorem** on `X_{4_1}^{(m)}` (`N_cusps = 1` for every `m`).
- Explicit `6D` pillowcase `T^2 / Z_2` (`iota_inv : z -> minus z`) spin-lift and `I_8` anomaly-inflow computation showing how spin eigenvalues `(+i, minus i)` on `K^{1/2} (+) K_bar^{1/2}` select `4D_L (x) ker d_bar_z` (`+48` Weyl states on `1` cusp at `0` flux) while requiring non-zero `7D` Chern–Simons / Green–Schwarz inflow (`tr_{16}(F^4) != 0`).
- Zero-shared-code independent countercheck (`recomputed independently` + `tested against planted errors`) and mask-clean result relay.

## Three. Pre-committed expectations and how it could come out wrong

- **E1 (`7D` self-adjoint index-zero theorem):** Across all `Spin(3, 1)`-invariant maximal isotropic subspaces `L` of `S_{7D} (x) V` under `Gamma^r = Gamma_{4D} Gamma_{T^2}`, `dim L_L minus dim L_R` must equal `0` identically (`refuting any free self-adjoint 7D origin of X:CUSP`); if any `Spin(3, 1)`-invariant Lagrangian achieves `dim L_L != dim L_R`, `E1` fails.
- **E2 (commutator cusp-evenness vs `1`-cusped knot cyclic covers, plus Shapiro collapse):** On `Sigma_{1, 1}`, every `d`-sheeted connected cover whose cusp cycles all have even length (`trivializing order-2 U_inf^(T)`) must have an **even** number of cusps `N_cusps >= 2` (`24` on `X(8)`, `576` on `X(40)`), and deck-invariant projection `(H^0(d Sigma_tilde, pi^* T))^{G_deck}` must have dimension `1` (`not 3`); conversely, on `m004` (`X_{4_1}`), every cyclic meridian cover `X_{4_1}^{(m)}` (`m` in `{2, 5, 8, 40}`) must have `N_cusps = 1`.
- **E3 (`6D` pillowcase spin-lift chirality and non-zero `I_8` inflow debt):** On `T^2 / Z_2`, the spin-lift `hat_iota = (minus i) diag(+i, minus i)` on `(4D_L (x) K^{1/2}) (+) (4D_R (x) K_bar^{1/2})` must yield `+3 x 16 = 48` `4D` left-handed states at `0` `U(1)` flux on a single cusp, while the `6D` quartic gauge trace `tr_{16_+}(F^4)` and gravitational `I_8` coefficient must be non-zero (`proving 7D inflow is a genuine required datum, not free`).

## Four. Premises and firewall boundaries

- Rests on `B1677`, `B1938`, `B1952`, `B1955`, `AGY-C3`, and `AGY-C5`; Guardrails one through six enforced throughout.
- Must **never** read, compute, or compare any of the nineteen empirical Standard Model targets (`0 of 19`), and must leave `origin/agy/audit-2026-11-02` untouched at `4319f47e2`.

## Five. Mandatory planted negative control

1. **Lorentz-breaking boundary plant:** Drop `Spin(3, 1)` invariance by allowing a planted boundary subspace `L_plant = (4D_L (x) K^{1/2}) (+) 0` (`ignoring Gamma^r = +I_48 > 0` or pairing `(4D_L, +)` with `(4D_R, +)`): the isotropy check `L^dag Gamma^r L = 0` or `[Sigma^{mu nu}, P_L] = 0` **must** fail (`> one-half`) and be caught.
2. **Shapiro / naive congruence-cusp plant:** Put `3` families independently on every cusp of `X(8)` (`or X(40)`), or project a `Q_8` cover of `Sigma_{1, 1}` onto deck invariants: the resulting family count **must** equal `72` (`or 1728`) in the unquotiented plant and `1` in the deck-invariant plant (`both != 3`), catching both multiplicity traps.

## Six. What is needed from main or other seats

Nothing needed to run; offered as a data-free audit closing the open `X:CUSP` and cover-multiplicity items in Section Four of our synthesis relay (`ba82741a6`).

0 of 19.
