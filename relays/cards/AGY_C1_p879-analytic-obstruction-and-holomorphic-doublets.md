# Card AGY-C1: Spinor parity proof on `P-879`, closed-form resolution of `B1969`, and the holomorphic two-doublet `(S, S)` cusp operator

*Seat: `agy` (`agy/cusp-action-2026-11-20`, forked from `origin/main` at `60a52d359`). Date: `2026-11-20`. Pre-registered before any script or run (`expectations committed first`). Data-free: `0 of 19`.*

---

## One. Package and question

Register rows `P-879` (`B1966` to `B1969`, open) and `P-847` (`B1963`, `B1964`): first, does `B1736`'s coupling form admit an exact full-hierarchy aligned witness below `B1969`'s lowest tested reality (`r = one-thousandth`), what exact spinor pairing invariant governs the tuned region, and why do Frame `C`'s shared-`Q_L` channels miss it; second, when six-dimensional Dolbeault holomorphy (`ker d_bar_z`) forbids `S_tilde` and forces two chiral doublets `(H_u, H_d)` sharing `(S, S)`, do hierarchy and CKM alignment coexist across the cusp?

## Two. Deliverables and what done means

- Symbolic (`sympy`) proof of the spinor inner-product law, the Takagi three-by-three block form of `Y(h; u, w)`, the exact null-Higgs rank-one ceiling `sup |V_tb| = (1 + sqrt(1 minus gamma^two)) / (3 minus sqrt(1 minus gamma^two))` in terms of the left-spinor overlap `gamma = |<alpha_one^(up), alpha_one^(down)>|` of `Mw`, and a closed-form `50`-digit full-hierarchy witness at `r = 1 / 2000` with `|V_CKM| = I_three`.
- Exact Jacobi factorization proof that the unweighted residue matrix `R_mat` has rank one with left spinor fixed by `q_L w` alone, cusp parity theorem showing `alpha_one^(up) = alpha_one^(down)` (`e_one` for `|<q_L a>| < one-fourth`, `e_two` for `|<q_L a>| > one-fourth`, so `gamma -> 1` and `sup |V_tb| -> one-third`), evaluation of `(eta_up, eta_down, gamma)` across all `2,016` points of `B1968`'s grid vs `B1967`'s escape pair, and a rigorous Lipschitz `S^four` covering certificate over all continuous `h` at representative Frame `C` points.
- `50`-digit evaluation of shared holomorphic `(S, S)` two-doublet couplings `(Y_up(S), Y_down(S))` on Frame `C`'s `24` order-five points at heights `two, six, fifteen, thirty` versus `(S_tilde, S)`.
- Zero-shared-code independent countercheck script (`recomputed independently` + `tested against planted errors`) and mask-clean result relay.

## Three. Pre-committed expectations and how it could come out wrong

- **E1 (`B1969` closed-form witness and exact spinor ceiling):** Symbolic residuals must vanish identically; at `r = 1 / 2000` (`below B1969's lowest grid point r = 1 / 1000 = rho_one * rho_two`), the monomial pair `w_up = w_down = 0`, `u_down = e_plus + mu_minus e_minus`, `u_up = nu_plus e_plus + e_minus` must satisfy `|V_CKM| = I_three`, both `m_two / m_three` in `[one-millionth, one-hundredth]`, and both `m_one / m_two <= one-tenth`; if any bar fails, our threshold formula `r_max = rho_one * rho_two` is wrong.
- **E2 (`P-879` left-spinor parity law vs `B1967` escape):** `det R_mat = 0` must hold identically across `B1968`'s grid; `B1967`'s `r = 3 / 1000` escape pair must satisfy `gamma < 6 sqrt(2) / 19` (`nearly orthogonal left spinors`), whereas every `a != 0` order-five and order-seven point at `y = 10` (and asymptotically `y >= 10`) must obey the `|<q_L a>|` quarter-threshold rule with `gamma > nine-tenths` (`blocking the null-Higgs escape`), and our Lipschitz `S^four` branch-and-bound certifier must prove zero continuous `h` counterexamples exist on certified Frame `C` points.
- **E3 (holomorphic `(S, S)` two-doublet alignment + hierarchy):** Under shared `(S, S)` on `(H_u, H_d)` with Frame `C`'s `S(tau)`, all `20` `a != 0` order-five points at heights `six, fifteen, thirty` must simultaneously exhibit `B1945`'s three-generation decay exponents (`one-tenth` or `three-tenths` up, `one-fifth` down) and aligned CKM diagonal (`min_k |V_kk| > nine-tenths` at height `thirty`), whereas `(S_tilde, S)` must collapse (`min_k |V_kk| < one-tenth` at height `thirty`).

## Four. Premises and firewall boundaries

- Rests on `B1736`'s coupling `Y(h; u, w)`, `B1940`/`B1945`'s data-free Frame `C` channel matrices `Mw`, Jacobi binary theta identities, and Weyl singular-value perturbation bounds.
- Must **never** read, compute, or compare any of the nineteen empirical Standard Model targets (`0 of 19`), and must leave `origin/agy/audit-2026-11-02` untouched at `4319f47e2`.

## Five. Mandatory planted negative control

1. Feed `B1967`'s synthetic `r = 3 / 1000` channel pair and our `r = 1 / 2000` full-hierarchy witness into both the spinor-cone test and the `S^four` branch-and-bound certifier: both **must** be admitted (`proving the exclusion is not vacuous`).
2. Plant a mismatched left-handed quark charge (`q_L^(up) = 2` vs `q_L^(down) = 1`): `gamma -> 1` **must** break on points where `|<a / N>| < one-fourth < |<2 a / N>|`.
3. Substitute `S_tilde` into the up sector at height `thirty`: CKM alignment **must** collapse (`|V_ud| -> 0`, `B1964`).

## Six. What is needed from main or other seats

Nothing needed to run; offered as a self-contained data-free contribution toward `P-879` and `P-847`.

0 of 19.
