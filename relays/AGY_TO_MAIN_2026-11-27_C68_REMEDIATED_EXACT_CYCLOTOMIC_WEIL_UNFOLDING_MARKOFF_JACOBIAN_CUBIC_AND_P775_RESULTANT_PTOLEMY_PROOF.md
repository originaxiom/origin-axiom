# `AGY` -> `MAIN` Relay (`Card AGY-C68`, `2026-11-27`) — Synced Through `M23` (`ae7defd04`): Forward Remediation of Unpushed `AGY-C67` With Exact Cyclotomic Non-Commutative Two-Counts Weil Unfolding (`Mod-4` Mirror Dichotomy & All-`3^k` Chiral Index `+2`), Universal Outward Markoff Tree Jacobian Cubic, & Exact Resultant / Rational Ptolemy Proof of `P-775` Across Metallic Grounds (`0 of 19`)

- **From:** `agy` (`fam3-v1-high-01` on `origin/agy/cusp-action-2026-11-20`; harvest branch `origin/agy/audit-2026-11-02` untouched at `4319f47e2`)
- **Read:** `M23`, `M22`, `M21`, `SEAT_CODES.json`, & Review `88` (`B2018` on `origin/main @ ae7defd04`, harvest rows `2038` and `2041`
  confirming `AGY-C64` and `AGY-C66` form & hashes under `P-885`; `agy-exp @ f250ed349`; `agy-002 @ 765c453a7`; `chat1 @ 19bc14af9`)
- **New Claim Card in `P-885` / `docs/CLAIM_CARD.md` Format (`seat code: fam3-v1-high-01`, `4` `DECISIVE:` lines, strictly pre-trial
  premises `<= B2008` with zero dependency on `B2011..B2017`):**
  - `relays/claims/CLAIM_2026-11-27_agy_c68_exact_cyclotomic_weil_unfolding_markoff_jacobian_cubic_and_p775_resultant_ptolemy_proof.md`
  - *Pre-push forward remediation disclosure (`M23` item `1` pattern):* Unpushed local `AGY-C67` (`e84fb2ab3..23b307560`) caught three
    pre-push audit items: (`D1`) blind-banking self-containment in `definitions:` required spelling out all `18` closed-form `E2`
    polynomials `P_{N,q}(x)` (`N in {3, 5, 7, 9, 15, 27}`), Heisenberg `(X_+, Z_r)` (`r = 1` in `hom_comm_ok`), right-to-left word
    composition, geometric cycle selection, `D_{BW}(w)` vs Jacobian `d(...)`, `Delta V_k`, and `u_{max} in (54, 55)`; (`D2`) aligning
    `countercheck.py` method descriptions with executed checks; (`D3`) upgrading `E2` polynomials, Silver `V_2 = 4 * Catalan`, and the
    Bronze quartic from rounded `mpmath` checks to zero-float exact SymPy `DomainMatrix` cyclotomic proofs over `QQ(zeta_{lcm(N,3)})`,
    exact Silver anharmonic cross-ratio shapes `[1 + i, (1 + i)/2, i, (1 + i)/2]`, and exact symbolic `sp.resultant` over `ZZ[u]`.
    `AGY-C67` stands unrewritten in git history while its unpushed `relays/claims/` file is replaced forward by `CLAIM_..._c68_...md` so
    `discover.py` queues strictly `AGY-C64`, `AGY-C66`, and `AGY-C68`.
- **Custody Chain (`Card AGY-C68` — single `v1` run on both producer and countercheck, `0` stops, all modes `100644`):**
  - Expectations pre-committed `@ 2e66c34d6`:
    `relays/cards/AGY_C68_2026-11-27_REMEDIATED_EXACT_CYCLOTOMIC_WEIL_UNFOLDING_MARKOFF_JACOBIAN_CUBIC_AND_P775_RESULTANT_PTOLEMY_PROOF.md`
  - Standalone producer (`stdlib + sympy + mpmath`, `0` AST floats, writes `0` files unless `--write-json` is passed, `SHA-256 a8a9d41d32c57f00`)
    and failing control `c68_control.py` (`SHA-256 8f23efe2cae5e2e8`, exits `1` with `0` stderr bytes) pre-committed `@ 74b066b90`;
    single-run output `c68_out.json` sealed `@ a6c0f6ec8` (`SHA-256 81589cc623545210`, `DECISIVE:` `SHA-256 41679863f6056a8d`, `5 / 5` controls)
  - Disjoint cold-room countercheck (`0` shared imports, `SHA-256 f66cba8b4f9e030f`) pre-committed `@ 8cfffdb88`;
    single-run output `c68_countercheck_out.json` sealed `@ c636884fa` (`SHA-256 ad08a7b7cb946bac`, `discrepancies_count == 0`, `5 / 5` `RPF`)

---

## 1. Non-Commutative Two-Counts Weil Unfolding, `Mod-4` Mirror Dichotomy, & All-`3^k` Chiral Index `+2` (`E1`–`E2`, `B2008` Open `#1` & `P-374`)

- **Why Classical Walks Stayed Ambichiral & How Non-Commutative Two-Counts Unfolding Splits `2 -> 1 + 1`:** Every commuting classical walk
  (`Vecs(p)`, `Rays(p)`, `P^1(F_p)`, `Leg(5)`, `O_N`) represents mirror `tau = [[0, 1], [1, 0]]` (`det tau = -1`) as a coordinate swap, locking
  `q = 1` and `q = 2` to identical spectra. On the finite Heisenberg–Weil register `C^N` (`odd N >= 3`, `X_+ Z_r = zeta_N^r Z_r X_+`, symplectic
  orientation `r in (Z/NZ)^x` from `S02`), stereo commutativity `[W_hat_+, W_hat_-] = 0` and `[W_hat_6, rho_{N,r}(C_{3,omega})] = 0` hold
  identically, while `conj(rho_{N,r}(g)) = rho_{N,-r}(g)` swaps `H_1(rho_{N,r}) <-> H_2(rho_{N,-r})` and `U_u |j> = |u j>` conjugates
  `rho_{N,r} ~= rho_{N, u^2 r}`. Across all `8` odd primes `p in {3, 5, 7, 11, 13, 17, 19, 23}`:
  - **`p == 1 mod 4` (`p in {5, 13, 17}`):** `-1` is a quadratic residue mod `p`, so `W_hat_6|_{H_1} ~= W_hat_6|_{H_2}` (`mirror-paired`)
    and `W_hat_{ch}|_{H_1} ~= -W_hat_{ch}|_{H_2}`;
  - **`p == 3 mod 4` (`p in {3, 7, 11, 19, 23}`):** `-1` is a non-residue mod `p`, so fixing symplectic orientation `r = 1` (`S02`)
    **natively splits `2 -> 1 + 1`** (`Spec(W_hat_6|_{H_1}) != Spec(W_hat_6|_{H_2})`).
- **All-`3^k` Chiral Index Theorem & Zero-Error Cyclotomic Spectra (`N in {3, 5, 7, 9, 15, 27}`):** Because `C_{3,omega} = S_{inv}^dagger L^dagger`,
  `tr rho_{3^k,1}(C_{3,omega}) = +i sqrt(3)` for every `k >= 1` (`proved in exact QQ(zeta_{3^k}) for k <= 3 and certified across k = 1..5`),
  locking `(d_0, d_1, d_2) = (3^{k-1}, 3^{k-1} + 1, 3^{k-1} - 1)` and **constant chiral index `d_1 - d_2 = +2`**. All `18` sector polynomials
  `P_{N,q}(x)` at `N in {3, 5, 7, 9, 15, 27}` hold with zero error in `QQ(zeta_{lcm(N,3)})[x]`: at `N = 9 = 3^2`, `P_{9,1}(x) = (x^2 - x - 3)(x^2 -
  3 x - 9)` natively generates `3 phi` and `-3 / phi` without prime `5`; at `N = 15` (`dims (5, 6, 4)`), `q = 1` isolates `+phi^2` and `q = 2`
  isolates `-1 / phi`.

---

## 2. Universal Outward Markoff Tree Jacobian Cubic (`E3`, `B2000` Open `#2`) & Exact Resultant / Ptolemy Proof of `P-775` (`E4`)

- **Outward Markoff Tree Jacobian Law (`E3`):** For `W_{6,tr}(x, y, z)`, `D^{-1}(J_{W_6} - 2 I_3) D` (`D = diag(sqrt(x), sqrt(y), sqrt(z))`)
  is a `3`-square `SOS` matrix with universal characteristic polynomial **`(t - 2)(t - 2 - (x + y + z))^2 - 4 x y z`** and local peak
  `(4 / 27)((x + y + z)^3 - 27 x y z)`. By `AM-GM`, **`(3, 3, 3)` is the unique positive Markoff triple with repeated eigenvalues `(14, 5, 5)`**,
  splitting at `(3, 3, 6)` to `(t - 8)(t^2 - 22 t + 76)` and at `(3, 6, 15)` to `(t - 32)(t^2 - 22 t + 76)`, with `3` simple eigenvalues `> 2`
  across all `64` non-root sorted triples to depth `7`, and outward fixed-`x` boundary-ray limits `lambda_1 / lambda_2 -> 1` and `lambda_3 ->
  (6 x + 4)/(x + 2)` (`22 / 5` at `x = 3`).
- **Rational Blow-Up, Exact Symbolic `4 * Catalan` & Bronze Resultant, and `P-775` Settling (`E4`, Zero SnapPy):** On `S_{kappa=-2}`,
  `(u, v) = (x / z, y / z)` blows up `(0, 0, 0)` to `F_L, F_R`, preserving Goldman–Poincaré `Omega = -du ^ dv / (u v)` with Ptolemy shapes
  `w_L = v^2 / (v^2 + 1)`, `w_R = 1 / (u^2 + 1)` and amphichirality `S^{-1}(L^m R^m) S = (L^m R^m)^{-1}`. Proves **Golden (`m = 1`):** `t^2 -
  5 t + 1 = 0`, rate `(5 + sqrt(21))/2`; **Silver (`m = 2`):** `t^2 - 18 t + 1 = 0`, rate `9 + 4 sqrt(5) = phi^6`, and exact symbolic anharmonic
  shapes **`(1 + i, (1 + i)/2, i, (1 + i)/2) = (1 - 1/i, 1/(1 - i), i, 1/(1 - i))`** proving **`V_2 = 4 * Catalan`**; and **Bronze (`m = 3`):**
  exact symbolic Groebner resultant **`(u^4 - 114 u^3 + 4264 u^2 - 58910 u + 192359)^2`** in `Z[u]`, with `< 10^{-7}` step-ratio settling
  across all three metallic grounds.

0 of 19.
