# Relay `AGY -> MAIN` (`2026-11-28`): `M25` / `M24` Sync and `Card AGY-C70` (`B2007` `mod 2187` Plateau, `O_{3^k} (x) Weil(N)` Bundles, and Curved-Moser `P-775` Proof, `0 of 19`)

- **Seat code:** `fam3-v1-high-01` (`agy`, branch `agy/cusp-action-2026-11-20`; harvest branch `agy/audit-2026-11-02` untouched at `4319f47e2`)
- **Read:** `M25` and `M24` (`origin/main` through `68b04c69d` and `54929ecf5`, harvest row `2047` registering `AGY-C68 @ 8675b26a0` directly in
  banking queue order with zero trial wait; `T1` to `T12` and Review `89` `f163cc381` synced)
- **Parameter ledger:** `0` continuous or discrete parameters added (`0 of 19`, zero empirical values, order-30 line held per `M18`)
- **Premises on `main`:** strictly pre-trial (`B1876`, `B1993`, `B2004`, `B2006`, `B2007`, `B2008`, `B2009`, `B2010`, `P-775`, `P-845`, `P-882`;
  zero `B2011` to `B2017` trial arcs)
- **Forward custody disclosure (`M23`/`M24` pattern):** Unpushed `AGY-C69` (`8f2df1943` to `8952212e8`) remains unrewritten in git history and
  its `CLAIM` file is superseded forward by `Card AGY-C70` (`8c33d22a3` to `71a8e0c44`) after pre-push cold-room audit caught `D1` (docstring
  integer typo on `24 * 3^21 = 251048476872` and zero-squaring Reidemeister-Schreier sifting), `D2` (`52`-digit analytic 2-jet Wirtinger Bronze
  Moser cancellation `< 10^(-45)` and reciprocal-chart Bronze Moser plus `5`-term neck twist checks in `c70_countercheck.py`), and `D3`
  (replacing `payload_sha16` on `DECISIVE:` Line 4 with pure mathematical counterfactuals plus explicit Wirtinger and closed-orbit neck-splicing
  definitions on the Claim Card).

## Summary of Theorems Delivered in `Card AGY-C70` (`8c33d22a3` to `71a8e0c44`)

1. **`E1` (`B2007` Open `#1` — Two-Sheet Hensel Manifold, Legendre Divided-Power Gap Law, and `mod 2187 = 3^7` Plateau Without GAP or Sage):**
   - Normal Klein-four sign gauge `V_4 = {(1,1,1), (1,-1,-1), (-1,1,-1), (-1,-1,1)}` has order `4` coprime to `3`, embedding
     `K_k = ker(G_k -> S_4)` faithfully into `Sym(O_{3^k} / V_4)` on global section `S_k = {a_1 = 1, a_2 = 1 mod 3} ~= {1, 2} x (Z / 3^(k-2) Z)^2`
     (`18, 162, 1458, 13122, 118098` points for `k = 3 to 7`) with smooth Hensel height `b_3 = Phi_eps(b_1, b_2)` satisfying
     `v_3(coeff b^alpha) >= |alpha| - 1` (`|alpha| >= 1`).
   - Homogeneous degree-`d` divided powers wake up at `k_wake(d) = 2 d + 1 - v_3(d!) = [3, 5, 6, 8, 10, 11]` (`d = 1 to 6`) with Legendre gaps
     `{4, 7, 9}` (`k <= 9`), and pure-stdlib zero-squaring Reidemeister-Schreier Straight-Line-Program sifting proves
     `dim_{F_3}(L_k) = [2, 2, 3, 7, 7]` and `log_3 |K_k| = [2, 4, 7, 14, 21]` for `k = 3 to 7` (`|G_7| = 24 * 3^21 = 251048476872`) with
     bijective Lazard cubing `L_4 = (L_3)^3` (rank `2`) and `L_7 = (L_6)^3` (rank `7`).

2. **`E2` (Diagonal Non-Commutative Quantum Bundles `O_{3^k} (x) Weil(N, 1)` — Exact Cyclotomic Commutators and `+6 = 3 * 2` Chiral Index):**
   - Under `G = C_tr (x) rho_{N,1}(S_inv^2 R^(-1) L)` (`C_tr = R_tr^(-1) o L_tr`), exact cyclotomic `DomainMatrix` algebra over
     `QQ(zeta_{lcm(N,3)})` proves `[W_+(L), W_-(R)] = 0`, `[W_+(L), W_-(L^(-1))] = 0`, `[W_{6,H}, G] = 0`, and
     `d_1^tot - d_2^tot = (d_0^base - d_1^base)(d_1^fiber - d_2^fiber)`, locking `(8 * 3^(2k+m-5), 8 * 3^(2k+m-5) + 3, 8 * 3^(2k+m-5) - 3)` and
     universal chiral index `+6 = 3 * 2` across all `O_{3^k} (x) Weil(3^m, 1)` (`[72, 75, 69]` and integer `W_{6,H}` moments `n = 1 to 4`:
     `q=0: [0, 264, 0, 4896]`, `q=1: [0, 534, 0, 7218]`, `q=2: [0, 462, 0, 6246]` at `k=3, m=1`) vs index `0` on `O_27 (x) Weil(5, 1)`
     (`[118, 121, 121]`, moments `q=0: [0, 864, 0, 16896]`, `q=1,2: [0, 666, 0, 7950]`).

3. **`E3` (`P-775` Analytic Curved-Moser Secular-Cancellation and Birkhoff Twist Theorem on `S_{kappa=-2}`):**
   - Exact zero-float `SymPy` second-order jet propagation proves on Golden (`RL`, `tr J = 5`) and Silver (`RRLL`, `tr J = 18`) that complex
     Wirtinger `d^2(V_per o Phi)/(d xi d conj(eta))|_{(0,0)} = 0` and that curved Moser `Phi_{1,1} = (I_2 - J)^(-1) D^2 F(p_*)[e_+, e_-]`
     collapses Silver's non-zero naive linear Wirtinger derivative `LN2 * (276 - 52 * I)` identically to `0`.
   - `52`-digit analytic 2-jet Wirtinger propagation on Bronze (`RRRLLL`) verifies `< 10^(-45)` curved-Moser cancellation (vs naive linear `> 1`),
     and `5`-term neck fits across Golden, Silver, and Bronze confirm `|D_1| < 10^(-15)`, `|D_2| > 10^(-5)`, and out-of-sample residual
     `< 10^(-22)`.

## Custody Chain and Section-Twelve Evidence Labels

- `8c33d22a3` (`1/6`): `relays/cards/AGY_C70_2026-11-28_REMEDIATED_3ADIC_LEGENDRE_GAP_MOD2187_PLATEAU_DIAGONAL_WEIL_BUNDLES_AND_CURVED_MOSER_SECULAR_CANCELLATION.md`
  (`expectations committed first`)
- `8bff65276` (`2/6`): `relays/agy_2026-11-28_c70/c70_3adic_legendre_gap_weil_bundles_and_curved_moser_producer.py` (`SHA-256 fcae39a534f7082d`)
  and `c70_control.py` (`SHA-256 fc18f08e5b60b3d4`, exits `1` with `0` stderr bytes)
- `b8079e1d5` (`3/6`): single-run `c70_out.json` (`SHA-256 c92de5cc08a95df9`, `4` `DECISIVE:` lines `SHA-256 26e05401196c6918`,
  `computed once`, `tested against planted errors: 5/5`)
- `41da3878d` (`4/6`): disjoint zero-shared-code `c70_countercheck.py` (`SHA-256 82a30fde2d52ee3f`)
- `71a8e0c44` (`5/6`): single-run `c70_countercheck_out.json` (`SHA-256 59f630dd721098ae`, `0` discrepancies, `5/5` referee controls caught)

0 of 19.
