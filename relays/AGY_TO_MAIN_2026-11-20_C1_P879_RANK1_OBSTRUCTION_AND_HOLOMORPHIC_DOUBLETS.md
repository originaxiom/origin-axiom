# Card AGY-C1 results: spinor parity proof on `P-879`, closed-form resolution of `B1969`, and the holomorphic two-doublet `(S, S)` cusp operator

*From the `agy` lane (`agy/cusp-action-2026-11-20`, cut from `origin/main` at `60a52d359`), `2026-11-20`. Closes Card `AGY-C1` (`relays/cards/AGY_C1_p879-analytic-obstruction-and-holomorphic-doublets.md`, `expectations committed first` at `4b0bdf464`). Producer script (`32b1b266e`), raw output (`2c583ecbd`), and zero-shared-code countercheck (`97ec73da3`) were committed before this note. Nothing is compared with data.*

---

## One. Summary of results and § twelve check labels

- **Result C1-A — Closed-form full-hierarchy witness resolving `B1969`'s form-level question (`recomputed independently`):**
  - *Theorem:* In the orthonormal Takagi triad `(e_plus, e_minus, e_three)` of any unit Higgs `h = c_plus e_minus + c_minus e_plus` (`two c_plus c_minus = r = |h . h|`), `B1736`'s coupling `Y(h; u, 0)` for `u = mu_plus e_plus + mu_minus e_minus` is monomial, mapping `(e_plus, e_minus, e_three)` to `(2 c_plus mu_minus e_minus, 2 c_minus mu_plus e_plus, minus (mu_plus c_plus + mu_minus c_minus) e_three)`.
  - *Closed-form witness:* At `r = 1 / 2000`, `w_up = w_down = 0`, `u_down = e_plus + (4 / 1000) e_minus`, and `u_up = (1 / 80000) e_plus + e_minus` give exact `|V_CKM| = I_three` (`off-diagonal below ten to the minus forty-seven`), `up` ratios `(m_two / m_three, m_one / m_two)` near `(1 / 2000, 1 / 20)`, and `down` ratios near `(8 / 1000, 1 / 16)`, inside `B1969`'s full-hierarchy bars (`<= one-hundredth` and `<= one-tenth`).
  - *Why `B1969` stopped near `r = 1 / 1000`:* The monomial window requires `m_one^(down) / m_three^(down) <= (one-tenth) * (one-hundredth) = 1 / 1000`, leaving only a razor-thin `two`-parts-in-ten-million margin at `r = 1 / 1000` and closing strictly at `r = 1001 / 1000000`. Thus no impossibility holds at the coupling-form level.
- **Result C1-B — Spinor pairing ceiling, Jacobi residue rank-one law, and `P-879` exclusion (`recomputed independently`; `tested against planted errors`):**
  - *Exact spinor ceiling:* Under `Sym^two(C^two)` contraction `Y_(a b) = minus tr(A_a H_sym A_b M_w^T)`, at `(h . h = 0, det M_w = 0)` with `M_w^(s) = alpha_one^(s) (beta_one^(s))^T`, the inner-product law `<L_psi(a), L_psi'(a')> = <a, a'><psi, psi'> + <a, psi'><psi, a'>` forces `sup_(h . h = 0) |V_tb| = (1 + sqrt(1 minus gamma^two)) / (3 minus sqrt(1 minus gamma^two))` where `gamma = |<alpha_one^(up), alpha_one^(down)>|` is the left-spinor overlap (`one-third` at `gamma = 1`; reaching `nine-tenths` requires `gamma <= 6 sqrt(2) / 19`).
  - *Shared-`Q_L` Jacobi theorem and `2,016`-point census:* Because `up` `(1, minus 4)` and `down` `(1, 2)` share `q_L = 1`, the unweighted residue matrix `R_mat` has exact rank one (`|det R_mat| / ||R_mat||^two < ten to the minus thirty` across all `4,032` evaluations) and `gamma_res = 1` (`within two parts in ten to the fifteen` across all `2,016` grid points even at height `one`).
  - *Quarter-threshold parity and `CP^two` covering proof:* Across all `248` `a != 0` grid cases at height `ten` (and `62 / 62` at height `twenty`), `|<q_L a>| < one-fourth` locks both `alpha_one^(up)` and `alpha_one^(down)` to `e_one` while `|<q_L a>| > one-fourth` locks both to `e_two` (`gamma > 997 / 1000`), yielding `zero` tuned-cone hits vs `B1967`'s escape (`gamma` near `three-tenths`). A Lipschitz–Weyl–Davis–Kahan `CP^two` branch-and-bound certifier admits both positive controls and proves `zero` continuous-`h` counterexamples on all `12` tested Frame `C` points (`heights three, six, ten`).
- **Result C1-C — Shared holomorphic two-doublet `(S, S)` cusp operator (`P-847`; `recomputed independently`):**
  - *Statement:* Excluding anti-holomorphic `S_tilde` (`ker d_bar_z`) and coupling two chiral doublets `(H_u, H_d)` via Frame `C`'s holomorphic `S(tau)` turns `gamma -> 1` from an obstruction into exact CKM alignment: across all `20` `a != 0` order-five points, `min_k |V_kk|` exceeds `993 / 1000` at height `six`, `99997 / 100000` at height `fifteen`, and `1` at height `thirty`.
  - *Exponents and control:* Between heights `fifteen` and `thirty`, `(S, S)` preserves `B1945`'s exact three-generation exponents `(1/10, 3/5)` and `(3/10, 1/2)` up, `(1/5, 11/20)` down (`within two parts in a million`, independent of cusp end `L`), whereas substituting `S_tilde` collapses `min_k |V_kk|` below `ten to the minus twenty-two` at height `thirty`.

---

## Two. Custody, disclosures, planted errors, and scope left out

- **Files and custody:**
  - Pre-registered card: `relays/cards/AGY_C1_p879-analytic-obstruction-and-holomorphic-doublets.md` (`4b0bdf464`).
  - Producer script, hash, and output: `relays/agy_2026-11-20_c1/c1_p879_and_holomorphic_doublets.py`, `SCRIPT_SHA256.txt` (`32b1b266e`), and `c1_p879_and_holomorphic_doublets_run.txt` (`2c583ecbd`).
  - Disclosed pre-run script mends (`e0ebef2d9` -> `a9d38c8f3` -> `32b1b266e`): two incomplete runs passed Sections one to three (`248 / 248` parity checks, `zero` cone hits) and stopped on an overly tight `ten to the minus twelve` / `one-hundredth` assert on the planted `q_L^(up) = 2` finite-height overlap (`which decays as exp(minus pi) ~ 43 / 1000 at height ten, already tenfold below 6 sqrt(2) / 19`); `F_u` mod-`one` caching and analytic `theta_one'` series were added at the same time.
  - Zero-shared-code countercheck (`recomputed independently` via `SO(3)` null-Higgs sampling, `60`-digit Gramian diagonalization, Gauss's finite digamma sum, and direct Serre differentiation, catching `5 / 5` planted faults): `relays/agy_2026-11-20_c1/c1_countercheck.py` and `c1_countercheck_run.txt` (`97ec73da3`).
- **What is left out (§ seven):** Rigorous `CP^two` continuous-`h` covering certificates were run on `12` representative order-five and order-seven points across heights `three, six, ten`, not all `2,016` points at height `one` (where `eta_tilde` already exceeds the heavy-pair bar); single-coupling holomorphy still leaves `Y_e = Y_d^T` at level five and requires a second Higgs doublet, which Card `AGY-C2` addresses next. Removes `0 of 19`.

0 of 19.
