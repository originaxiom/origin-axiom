# Card AGY-C2: `SL(2, F_5)` exterior-to-Weil join, linear no-go and quadratic/interference escapes for `Y_e != Y_d^T`, and the `9 / 5` two-doublet gauge slope

*Seat: `agy` (`agy/cusp-action-2026-11-20`, forked from `origin/main` at `60a52d359`). Date: `2026-11-20`. Pre-registered before any script or run (`expectations committed first`). Data-free: `0 of 19`.*

---

## One. Package and question

Register rows `P-866` (`B1953`, `B1955`), `M4` (`R1` traceless `B minus L`), `P-845`, and `B915`: first, how does `B1955`'s dihedral exterior algebra `Lambda^even(W)` join to `B1953`'s covariant `3 + 2` Weil operator `O(tau)`, and can a single linear `SU(3)_C x SU(2)_L`-singlet insertion of `O(tau)` or traceless `B minus L` split `Y_e` from `Y_d^T` generation-dependently at level five; second, how much does `AGY-C1`'s holomorphy-forced second Higgs doublet `(H_u, H_d)` shift `B915`'s one-loop and two-loop gauge unification slope?

## Two. Deliverables and what done means

- Exact `SL(2, F_5)` intertwiner and derivation computation on `W = C^five = W_plus (+) W_minus`: dimension of invariant Yukawa contractions `Lambda^two(W) (x) Lambda^four(W) (x) W^* -> C` with zero vs one `sl(W)^plus` adjoint insertion, testing `B1955` line `122`'s open question directly.
- Exact test of linear vs quadratic/two-channel `Y_e != Y_d^T` splitting: (a) linear singlet derivation `d_O` and single-channel `B minus L = diag(one-third, one-third, one-third, minus one)`, (b) quadratic `3 + 2` Weil-block Gramians `(1/3) tr_(W_+) (O_3 O_3^H)` vs `(1/2) tr_(W_-) (O_2 O_2^H)` under holomorphic `S` across bulk and cusp heights, and (c) two-channel `(1, 2, 2) (+) (15, 2, 2)` interference `Y_d = Y^(0) + (1/3) Y^(BL)` vs `Y_e^T = Y^(0) minus Y^(BL)` (and `E_8` decomposition checking whether `(10, 6)` carries `(15, 2, 2)`).
- Exact rational one-loop `(b_1, b_2, b_3)` and two-loop `B_ij` gauge-beta calculation (`sympy` / `Fraction`) for `n_H = 1` (`218 / 115`), holomorphy-forced `n_H = 2` (`9 / 5`), general `(n_H, n_T)` in `Lambda^one(W) = 3_(-2) (+) 2_(+3)`, plus two-loop RGE literature benchmark gate before integration.
- Zero-shared-code independent countercheck script (`recomputed independently` + `tested against planted errors`) and mask-clean result relay.

## Three. Pre-committed expectations and how it could come out wrong

- **E1 (linear adjoint no-go on `B1955` line `122` and `M4`):** Every `SU(3)_C x SU(2)_L`-invariant linear derivation of `O(tau)` in `sl(W)^plus` (and every single-channel `B minus L` factor) must collapse onto the one-dimensional hypercharge invariant `6Y` times `B1953`'s phased sum `F(tau)`, leaving `(m_two / m_three, m_one / m_three)` **identical** between `e` and `d` (`exact negative theorem at linear single-channel order`); furthermore `(10, 6)` of `SO(10) x SO(6)` must contain **zero** `(15, 2, 2)` doublets (`(15, 2, 2)` lives in `45`, not `10`).
- **E2 (quadratic Weil-block and two-channel escapes):** Under holomorphic `S`, `B1953`'s normalised `3`-block vs `2`-block Gramians must yield distinct generation eigenvalue ratios (`splitting e from d without level 25`), and two-channel `B minus L` interference (`using distinct modular channels such as order-ten / fifteen twists where (-3, 6) != (2, 1) mod N`) must split `m_two / m_three` between `e` and `d`; if `H_3` and `H_2` stay proportional everywhere, `E2` fails.
- **E3 (holomorphy-forced `9 / 5` gauge slope):** Replacing one Higgs doublet (`218 / 115`) by the holomorphy-forced pair `(H_u, H_d)` (`n_H = 2, n_T = 0`) must give exact one-loop `(b_1, b_2, b_3) = (21 / 5, minus 3, minus 7)` and exact slope `(b_1 minus b_2) / (b_2 minus b_3) = 9 / 5`, whereas keeping an unprojected colour triplet `n_T >= 1` from `Lambda^one(W)` must increase `(b_1 minus b_2) / (b_2 minus b_3)` above `218 / 115` (`requiring cusp boundary projection of 3_(-2)`).

## Four. Premises and firewall boundaries

- Rests on `B1951`/`B1953`/`B1955`'s level-five Weil algebra, compact `E_8 -> (Spin(10) x Spin(6)) / Z_4`, and Machacek–Vaughn two-loop gauge beta polynomials.
- Must **never** read, compute, or compare any of the nineteen empirical Standard Model targets (`0 of 19`, including empirical electroweak or strong gauge couplings at `M_Z`), and must leave `origin/agy/audit-2026-11-02` untouched at `4319f47e2`.

## Five. Mandatory planted negative control

1. Set the `B minus L` interference coefficient to `zero` (and compare `tr_(W_+)(O_3)` against `minus tr_(W_-)(O_2)`): generation singular-value ratios of `Y_e` and `Y_d^T` **must** revert to exact equality (`< ten to the minus thirty`).
2. Omit the `SU(5)` `3 / 5` hypercharge normalization factor in `b_1`: the `n_H = 1` slope **must** fail `B915`'s `218 / 115` benchmark and be caught.

## Six. What is needed from main or other seats

Nothing needed to run; offered as a data-free contribution toward `P-866`, `M4`, and `B915`.

0 of 19.
