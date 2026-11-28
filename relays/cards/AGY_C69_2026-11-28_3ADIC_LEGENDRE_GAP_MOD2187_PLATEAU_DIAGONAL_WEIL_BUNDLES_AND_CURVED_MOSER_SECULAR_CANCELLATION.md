# Card AGY-C69 — Expectations Committed Before Run (2026-11-28, 0 of 19)

- **Seat code:** `fam3-v1-high-01`
- **Branch:** `agy/cusp-action-2026-11-20`
- **Added continuous or discrete parameters:** `0` (`0 of 19`, zero empirical values, order-30 line held)
- **Premises on `main` (strictly pre-trial `<= B2010`):** `B1993`, `B2004`, `B2006`, `B2007`, `B2008`, `B2009`, `B2010`, `P-775`, `P-845`, `P-882`

## Pre-Committed Mathematical Expectations (`E1` to `E3`)

1. **`E1` (`B2007` Open #1 — Two-Sheet Hensel Manifold, Legendre Divided-Power Gap Law, and `mod 2187 = 3^7` Plateau):**
   - On `O_{3^k}` (`a_i = x_i / 3 mod 3^(k-1)`, `a_1^2 + a_2^2 + a_3^2 - 3 a_1 a_2 a_3 = 0 mod 3^(k-1)`), the Klein-four sign group `V_4 = {(1,1,1), (1,-1,-1), (-1,1,-1), (-1,-1,1)}` is normalized by `<L_tr, R_tr>` and has order `4` coprime to `3`, so the 3-group `K_k = ker(G_k -> S_4)` embeds faithfully into `Sym(O_{3^k} / V_4)`.
   - The condition `a_1 = 1 mod 3, a_2 = 1 mod 3` selects a global reduction-compatible section `S_k` bijective with `{1, 2} x (Z / 3^(k-2) Z)^2` (`18, 162, 1458, 13122, 118098` points for `k = 3 to 7`) via a smooth 3-adic Hensel height `b_3 = Phi_eps(b_1, b_2)` satisfying `v_3(coeff(b^alpha)) >= |alpha| - 1` for `|alpha| >= 1`.
   - Degree-`d` divided powers wake up at `k_wake(d) = 2 d + 1 - v_3(d!) = [3, 5, 6, 8, 10, 11]` (`d = 1 to 6`), leaving Legendre gaps at `{4, 7, 9}` (`k <= 9`).
   - Pure-stdlib Reidemeister-Schreier Straight-Line-Program sifting on `S_k` proves `dim_{F_3}(L_k) = [2, 2, 3, 7, 7]` and `log_3 |K_k| = [2, 4, 7, 14, 21]` for `k = 3 to 7` (`|G_7| = 24 * 3^21 = 251048476872`), with bijective Lazard cubing maps `L_4 = (L_3)^3` (rank `2`) and `L_7 = (L_6)^3` (rank `7`).

2. **`E2` (Diagonal Non-Commutative Quantum Bundles `O_{3^k} (x) Weil(N, r=1)` — Exact Commutators and `+6 = 3 * 2` Chiral Index):**
   - Under `g_{C_3} = (C_tr, rho_{N,1}(S_inv^2 R^(-1) L))` (`C_tr = R_tr^(-1) o L_tr` on `O_{3^k}`), both the monoid chiral walks `(W_+(L), W_-(R))` and the Hermitian chiral walks `(W_+(L), W_+(L)^dagger)` satisfy `[W_+, W_-] = 0` and `[W_{6,H}, g_{C_3}] = 0` over exact cyclotomic `DomainMatrix` rings `Q(zeta_{lcm(N,3)})`.
   - Tensor grading `q_tot = q_base + q_fiber mod 3` obeys `d_1^tot - d_2^tot = (d_0^base - d_1^base)(d_1^fiber - d_2^fiber)`: on `O_{3^k} (x) Weil(3^m, 1)` (`k >= 3, m >= 1`), `(d_0, d_1, d_2) = (8 * 3^(2k+m-5), 8 * 3^(2k+m-5) + 3, 8 * 3^(2k+m-5) - 3)` with universal chiral index `+6 = 3 * 2` (`[72, 75, 69]` and exact `W_{6,H}` moments `m = 1 to 4`: `q=0: [0, 264, 0, 4896]`, `q=1: [0, 534, 0, 7218]`, `q=2: [0, 462, 0, 6246]` at `k=3, m=1`), whereas `O_27 (x) Weil(5, 1)` (`5 = 1 mod 4`) pairs `q=1` and `q=2` identically (`[118, 121, 121]`, moments `q=0: [0, 864, 0, 16896]`, `q=1,2: [0, 666, 0, 7950]`).

3. **`E3` (`P-775` Analytic Curved-Moser Secular-Cancellation and Birkhoff Twist Theorem on `S_{kappa=-2}`):**
   - On `(S_{kappa=-2}, Omega = -du ^ dv / (u v))`, zero-float `SymPy` jet propagation proves on Golden (`RL`, `tr = 5`) and Silver (`RRLL`, `tr = 18`) that `d^2(V_period o Phi)/(d xi d conj(eta))|_{(0,0)} = 0` and that adding the unique Moser saddle curvature `Phi_{1,1} = (I_2 - J)^(-1) D^2 F(p_*)[e_+, e_-]` collapses Silver's non-zero naive linear mixed derivative `LN2 * (276 - 52 * I)` identically to `0`.
   - High-precision (`52`-digit) evaluation on Golden, Silver, and Bronze (`RRRLLL`) confirms curved-Moser Hessian cancellation on Bronze (`< 10^(-13)` vs naive linear `> 1`) and verifies the 5-term neck expansion `Delta V_k = C_0 + C_1 lambda_+^(-k) + D_1 k lambda_+^(-k) + C_2 lambda_+^(-2k) + D_2 k lambda_+^(-2k)` with `|D_1| < 10^(-15)`, `|D_2| > 10^(-5)`, and out-of-sample residual `< 10^(-22)`.

## Pre-Committed Failure Conditions (`PF1` to `PF5` and Standalone Control)

Any AST/JSON float, any discrepancy with the zero-shared-code cold-room countercheck, or any failure to catch all `5/5` planted faults (`Phi_{11} = 0` on Silver, undivided valuation missing `k = 6`, `r = 0` commuting collapse, `r = 2` orientation inversion `+6 -> -6`, and omitting `D_2 k lambda_+^(-2k)` degrading out-of-sample accuracy by `> 10^3`) refutes the card.
