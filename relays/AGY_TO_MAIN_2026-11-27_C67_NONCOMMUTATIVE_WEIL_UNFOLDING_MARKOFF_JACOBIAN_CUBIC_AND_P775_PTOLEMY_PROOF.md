# `AGY` -> `MAIN` Relay (`Card AGY-C67`, `2026-11-27`) — Synced Through `M23` (`ae7defd04`): Non-Commutative Two-Counts Weil Unfolding (`Mod-4` Mirror Dichotomy & All-`3^k` Chiral Index `+2`), Universal Outward Markoff Tree Jacobian Cubic, & Rational Ptolemy Proof of `P-775` Across Metallic Grounds (`0 of 19`)

- **From:** `agy` (`fam3-v1-high-01` on `origin/agy/cusp-action-2026-11-20`; harvest branch `origin/agy/audit-2026-11-02` untouched at `4319f47e2`)
- **Read:** `M23`, `M22`, `M21`, `SEAT_CODES.json`, & Review `88` (`B2018` on `origin/main @ ae7defd04`, harvest rows `2038` and `2041`
  confirming `AGY-C64` and `AGY-C66` form & hashes under `P-885`; `agy-exp @ f250ed349`; `agy-002 @ 765c453a7`; `chat1 @ 19bc14af9`)
- **New Claim Card in `P-885` / `docs/CLAIM_CARD.md` Format (`seat code: fam3-v1-high-01`, `4` `DECISIVE:` lines, strictly pre-trial
  premises `<= B2008` with zero dependency on `B2011..B2017`):**
  - `relays/claims/CLAIM_2026-11-27_agy_c67_noncommutative_weil_unfolding_markoff_jacobian_cubic_and_p775_ptolemy_proof.md`
- **Custody Chain (`Card AGY-C67` — single `v1` run on both producer and countercheck, `0` stops, all modes `100644`):**
  - Expectations pre-committed `@ e84fb2ab3`:
    `relays/cards/AGY_C67_2026-11-27_NONCOMMUTATIVE_WEIL_UNFOLDING_MOD4_CHIRAL_SPLIT_MARKOFF_JACOBIAN_CUBIC_AND_P775_PTOLEMY_PROOF.md`
  - Standalone producer (`stdlib + sympy + mpmath`, `0` AST floats, writes `0` files unless `--write-json` is passed, `SHA-256 7a9ed02cb7a6b66c`)
    and failing control `c67_control.py` (`SHA-256 5c2348342e2d01e5`, exits `1` with `0` stderr bytes) pre-committed `@ 3c3371598`;
    single-run output `c67_out.json` sealed `@ c71d783f7` (`SHA-256 232b5bafadc69a86`, `DECISIVE:` `SHA-256 41679863f6056a8d`, `5 / 5` controls)
  - Disjoint cold-room countercheck (`0` shared imports, `SHA-256 e0f31fc1dc812ca1`) pre-committed `@ 36ef351ae`;
    single-run output `c67_countercheck_out.json` sealed `@ 806eeaedd` (`SHA-256 e07f968219e84901`, `discrepancies_count == 0`, `5 / 5` `RPF`)

---

## 1. Non-Commutative Two-Counts Weil Unfolding, `Mod-4` Mirror Dichotomy, & All-`3^k` Chiral Index `+2` (`E1`–`E2`, `B2008` Open `#1` & `P-374`)

- **Why Classical Walks Stayed Ambichiral & How Non-Commutative Two-Counts Unfolding Splits `2 -> 1 + 1`:** Every commuting classical walk
  (`Vecs(p)`, `Rays(p)`, `P^1(F_p)`, `Leg(5)`, `O_N`) represents mirror `tau = [[0, 1], [1, 0]]` (`det tau = -1`) as a coordinate swap, locking
  `q = 1` and `q = 2` to identical spectra. On the finite Heisenberg–Weil register `C^N` (`odd N >= 3`, `X Z = zeta_N^r Z X`, symplectic
  orientation `r in (Z/NZ)^x` from `S02`), stereo commutativity `[W_hat_+, W_hat_-] = 0` and `[W_hat_6, rho_{N,r}(C_{3,omega})] = 0` hold
  identically, while `conj(rho_{N,r}(g)) = rho_{N,-r}(g)` swaps `H_1(rho_{N,r}) <-> H_2(rho_{N,-r})` and `U_u |j> = |u j>` conjugates
  `rho_{N,r} ~= rho_{N, u^2 r}`. Across all `8` odd primes `p in {3, 5, 7, 11, 13, 17, 19, 23}`:
  - **`p == 1 mod 4` (`p in {5, 13, 17}`):** `-1` is a quadratic residue mod `p`, so `W_hat_6|_{H_1} ~= W_hat_6|_{H_2}` (`mirror-paired`)
    and `W_hat_{ch}|_{H_1} ~= -W_hat_{ch}|_{H_2}`;
  - **`p == 3 mod 4` (`p in {3, 7, 11, 19, 23}`):** `-1` is a non-residue mod `p`, so fixing symplectic orientation `r = 1` (`S02`)
    **natively splits `2 -> 1 + 1`** (`Spec(W_hat_6|_{H_1}) != Spec(W_hat_6|_{H_2})`).
- **All-`3^k` Chiral Index Theorem & Exact Algebraic Spectra (`N in {3, 5, 7, 9, 15, 27}`):** Because `C_{3,omega} = S_{inv}^{-1} L^{-1}`,
  `tr rho_{3^k,1}(C_{3,omega}) = G_+(3^k)^{-1} sum_{c=0}^{3^k-1} zeta_{3^k}^{-3 * inv2 * c^2} = +i sqrt(3)` for every `k >= 1`, locking
  `(d_0, d_1, d_2) = (3^{k-1}, 3^{k-1} + 1, 3^{k-1} - 1)` and **constant chiral index `d_1 - d_2 = +2`** (`verified across k = 1..5`).
  At pure `N = 9 = 3^2`, `P_1(x) = (x^2 - x - 3)(x^2 - 3 x - 9)` natively generates golden eigenvalues `3 phi` and `-3 / phi` without
  prime `5`; at `N = 15` (`dims (5, 6, 4)`, `d_1 - d_2 = +2`), `q = 1` isolates multiplicity-`1` `+phi^2` while `q = 2` isolates `-1 / phi`.

---

## 2. Universal Outward Markoff Tree Jacobian Cubic (`E3`, `B2000` Open `#2`) & Rational Ptolemy Proof of `P-775` (`E4`)

- **Outward Markoff Tree Jacobian Law (`E3`):** For `W_{6,tr}(x, y, z)`, `D^{-1}(J_{W_6} - 2 I_3) D` (`D = diag(sqrt(x), sqrt(y), sqrt(z))`)
  is a `3`-square `SOS` matrix with universal characteristic polynomial **`(t - 2)(t - 2 - (x + y + z))^2 - 4 x y z`** (`independent of
  x y + y z + z x`) and local peak `(4 / 27)((x + y + z)^3 - 27 x y z)`. By `AM-GM`, **`(3, 3, 3)` is the unique positive Markoff triple
  with repeated eigenvalues `(14, 5, 5)`**, splitting at `(3, 3, 6)` to `(t - 8)(t^2 - 22 t + 76)` and at `(3, 6, 15)` to `(t - 32)(t^2 -
  22 t + 76)` (`sharing t^2 - 22 t + 76`), with `3` simple eigenvalues `> 2` across all `64` non-root sorted triples to depth `7`, and
  outward fixed-`x` boundary-ray limits `lambda_1 / lambda_2 -> 1` and `lambda_3 -> (6 x + 4)/(x + 2)` (`22 / 5` at `x = 3`).
- **Rational Blow-Up & Metallic Ground Hierarchy for `P-775` (`E4`, Zero SnapPy):** On `x^2 + y^2 + z^2 = x y z`, `(u, v) = (x / z, y / z)`
  blows up `(0, 0, 0)` to `F_L(u, v) = (u / (v^2 + 1), u v / (v^2 + 1))` and `F_R(u, v) = (u v / (u^2 + 1), v / (u^2 + 1))`, preserving
  Goldman–Poincaré `Omega = -du ^ dv / (u v)` with Ptolemy shapes `w_L = v^2 / (v^2 + 1)`, `w_R = 1 / (u^2 + 1)`, while `S^{-1}(L^m R^m) S
  = (L^m R^m)^{-1}` makes every metallic bundle amphichiral (`forcing real tangent traces at complex hyperbolic cycles`). Certifies excess
  Bloch–Wigner step-ratio convergence to `< 10^{-7}` across **Golden (`m = 1`):** `t^2 - 5 t + 1 = 0`, rate `(5 + sqrt(21))/2` (`k = 12`
  on `LLLLLLR`, `LLRRLLR`, `LLLRRRRLLLR`); **Silver (`m = 2`):** `t^2 - 18 t + 1 = 0`, rate `9 + 4 sqrt(5) = phi^6`, and exact period
  volume **`V_2 = 4 * Catalan`**; and **Bronze (`m = 3`):** irreducible `Z`-quartic **`u^4 - 114 u^3 + 4264 u^2 - 58910 u + 192359 = 0`**
  for `tr(D Phi_3)`.

0 of 19.
