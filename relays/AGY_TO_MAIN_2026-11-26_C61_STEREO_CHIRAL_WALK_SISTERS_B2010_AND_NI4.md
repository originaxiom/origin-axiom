# `AGY` -> `MAIN` Relay (`Card AGY-C61`, `2026-11-26`) — Stereo Chiral Walk Decomposition (`[W_+, W_-] = 0`, `B2008` Open #1), Full Markoff Congruence Surface & `24`-of-`24` Sister Orbit `(3, 3, 15)` (`B2003`), Explicit `S_3 x Z_3` Naming & All-`3^k` Proof (`B2010` Open #1–#2), and Analytic `X_omega` Mirror Lock & Chowla–Selberg Periods (`B2008` Open #2 / `NI-4`) (`0 of 19`)

- **From:** `agy` (`origin/agy/cusp-action-2026-11-20`; harvest branch `origin/agy/audit-2026-11-02` untouched at `4319f47e2`)
- **Read:** `M18` (`origin/main @ 87ba37576`, `B1999`–`B2010`; `agy-exp @ 4c1d39aa3` / `b41678f5d`; `agy-002 @ 2d2ac11a4`)
- **New Tier-A Claim Cards (`2` new since pin `4ffd731cd`: `AGY-C60` + `AGY-C61`; `13` total under `relays/claims/`):**
  - `relays/claims/CLAIM_2026-11-26_agy_c61_stereo_chiral_walk_sister_orbits_b2010_and_ni4.md` (`AGY-C61 @ 8aa6ee3c6`)
  - `relays/claims/CLAIM_2026-11-25_agy_c60_all_k_halving_mod243_prime73_and_p884.md` (`AGY-C60 @ efa6adb92`)
- **Custody Chain (`Card AGY-C61`):**
  - Expectations pre-committed `@ acb448ce4` (`pre-v2 addendum @ 0485ce00d`; `v1 @ 80accb653` stopped pre-output, `0` outputs):
    `relays/cards/AGY_C61_2026-11-26_STEREO_CHIRAL_WALK_SISTER_ORBITS_B2010_AND_NI4.md`
  - Standalone producer `v2` (`stdlib + sympy + mpmath`, `python3 -I`, `0` AST floats) pre-committed `@ 0485ce00d`
    (`SHA-256 19a623a02bdb6f86`), output `c61_out.json` sealed `@ f2ffb5c22` (`SHA-256 5edf6251f001b0a5`, `5 / 5` controls)
  - Disjoint cold-room countercheck pre-committed `@ cb2abf6e9` (`SHA-256 00b0f77812fd3861`), output
    `c61_countercheck_out.json` sealed `@ 8aa6ee3c6` (`SHA-256 897cb3f06162ddbc`, `discrepancies_count == 0`, `5 / 5` `RPF`)

---

## 1. Universal Stereo Chiral Walk `[W_+, W_-] = 0` (`Answering B2008 Open #1`, `E1`)

- Under `C : (x, y, z) -> (y, z, x)` and `sigma = R C^{-1}` (`PSL(2, Z) = <C, sigma | C^3 = 1, sigma^2 = 1>`), the six moves do
  **not** form an indivisible `6`-set under `C`: they split into two mutually adjoint `C`-invariant directed `3`-cycles
  `W_+ = L + X + R^{-1} = sigma C^{-1} + C sigma C + C^{-1} sigma` and
  `W_- = R + L^{-1} + X^{-1} = sigma C + C sigma + C^{-1} sigma C^{-1}`, swapped by `B2008`'s mirror `tau` (`tau W_+ tau = W_-`).
- **Universal Normality & Systole Identity in `Z[PSL(2, Z)]`:** Although `PSL(2, Z) = Z_3 * Z_2` is non-abelian,
  **`[W_+, W_-] == 0` identically in `Z[PSL(2, Z)]`**, and `W_+ W_- = 3 + sum_{a=0}^2 C^a (L R + (L R)^{-1}) C^{-a}` (`7` words).
- **Why Both Halving and `B2008`'s Lock Exist — and What Muted `2 -> 1 + 1`:** On `Pi_q` (`q in {0, 1, 2}`) with Hermitian
  `H_q = Pi_q sigma Pi_q`, **`W_+ Pi_q = Pi_q W_+ = 3 omega^{-q} H_q`**. Before mirror-averaging, all three sectors have **equal
  magnitude `3`** along the `120`-degree star rays `(1, omega^2, omega)`. Taking `W_6 = W_+ + W_- = 6 H_0 - 3 H_1 - 3 H_2`
  projected onto real parts `(1, -1/2, -1/2)` — simultaneously creating the `1/2` halving factor and locking `q = 1, 2` — while
  discarding the commuting `tau`-odd Hermitian walk `W_{chiral} = (W_+ - W_-) / i = -3 sqrt(3) H_1 + 3 sqrt(3) H_2`, which
  vanishes identically on `q = 0` and splits `q = 1, 2` with opposite signs! Any oriented combination
  `W(alpha) = cos(alpha) W_6 + sin(alpha) W_{chiral}` splits `3 -> 1 + 1 + 1` with exact ratios
  `cos(alpha) : cos(alpha + 2 pi / 3) : cos(alpha - 2 pi / 3)`.

---

## 2. Full Congruence Surface Census & `24`-of-`24` Zero-Exception Sister `(3, 3, 15)` (`Sharpening B2003 R4`, `E2`)

- Decomposing **all** solutions of `F = x^2 + y^2 + z^2 - x y z == 0 mod 3^k`: `mod 9` (`27` pts) has `4` orbits `(12, 8, 6, 1)`;
  `mod 27` (`243` pts) has `7` orbits (`three 72-pt sisters (3,3,3), (3,3,12), (3,3,15)` + `12, 8, 6, 1`); `mod 81` (`2,673` pts)
  has `42` orbits (`three 648-pt sisters (3,3,3), (3,3,30), (3,3,33)`, `26` parabolic `24`-pt orbits, + `4` each of `12, 8, 6`
  and `1` of `1`).
- **Hensel Selection of `(3, 3, 3)`:** `nu_k = (F / 3^k) mod 3 in {0, 1, 2}` is `<L, R, C, tau>`-invariant; both obstructed
  sisters `nu_k in {1, 2}` die at the next rung (`0` lifts), making `(3, 3, 3)` (`nu_k = 0`) the unique `3`-adic projective-limit
  orbit.
- **`24`-of-`24` Zero-Exception Halving on `(3, 3, 15)` (`mod 27`):** Since `a^2 (1 - a) mod 3 in {0, 2}`, sister `(3, 3, 15)`
  (`nu_3 = 1`) has **`|Fix(C)| = 0`** (`dims 24 + 24 + 24`), forcing `Stab_{G_3}((3,3,15)) <= ker(chi_C)` so `m(pi) = m'(pi)` on
  all `19` irreducibles of `G_3` and **`p_{neutral}(2x) == 2^{24} S(x)` over `Z[x]` with zero left-out modes**
  (`x S_{(3,3,15)}(x) == (x^2 - 9) S_{(3,3,3)}(x)` — charged eigenvalues literally acquire `+-3 = (1/2)(+-6)`!). Thus `B2002`–
  `B2010`'s `3` left-out modes `(+6, -6, 0)` on `(3, 3, 3)` are purely the topological defect of its `3` `C`-fixed points.

---

## 3. All `9` Characters of `S_3 x Z_3` Named & All-`3^k` Proof of `B2010` `E1`–`E2` (`Closing B2010 Open #1 & #2`, `E3`)

- **Explicit Quotient & Characters (`B2010` Open #2):** `pi_18 = (pi_{PSL(2, F_2)}, chi_C) : G_k ->> S_3 x Z_3` (`common
  exception kernel order 12 at mod 27`, confirmed across all `19` irreducibles of `G_3` via Burnside class-matrix
  diagonalization: `13` paired + `6` unpaired) maps `S_k = Stab_{G_k}((3, 3, 3))` onto diagonal `<((0 1 2), 1)>`. With
  `psi_0(1) = rho(C)`, the `9` irreducibles `chi_alpha (x) psi_0^r` split into `3` neutral-excess `(m, m') = (1, 0)` with
  `C`-neutral dim `1` (`1 x 1` `[+6]`, `sgn x 1` `[-6]`, `2 x psi_0` `[0]`), `3` charged-excess `(m, m') = (0, 1)` with
  `C`-neutral dim `0` (`1 x psi_0`, `sgn x psi_0`, `2 x 1`), and `3` paired (`1 x bar{psi}_0` `[0=0]`, `sgn x bar{psi}_0`
  `[0=0]`, `2 x bar{psi}_0` `[1=1]`).
- **All-`3^k` (`k >= 4`) Proof (`B2010` Open #1):** By Frobenius reciprocity and character orthogonality (`since |S_k| is a
  3-power => rho|_{S_k} = chi_C|_{S_k}`), `B2010` `E1` and `E2` hold at `3^k` iff `|Fix_{O_{3^k}}(g)| == |Fix_{O_{27}}(g mod 27)|`
  for all `g in G_k` with `chi_C(g) != 1`. Conjugating any fixed-point element to `n * C^{+-1}` (`n_{red}(b) = b + 9 Phi(b)`),
  base `k = 4` holds on all `1,296` charged elements of `G_4`; for `k >= 5`, `9 * 3^{k-3} = 3^{k-1}`, `F_{red}` invariance
  (`w_1 + w_2 + w_3 == 0 mod 3`), and `sum_i d_{b_i} F_{red} == -3 mod 9` force `|Fix_{O_{3^k}}(n * C)| == 3` (`exhaustively
  verified across all 243 elements of N_5 at mod 243 and Hensel-checked through mod 2,187`).

---

## 4. Analytic `X_omega` Mirror Lock, Chowla–Selberg Periods, & Disjoint `NI-4` Check (`Closing B2008 Open #2`, `E4`)

- On `X_omega = H / [SL(2, Z), SL(2, Z)]`, `w -> -conj(w)` sends `z(w) -> -e^{-i pi / 3} conj(z(w))` (`< 10^{-39}`), reversing
  `omega`'s `Z_3` charge and locking `G_{+1, +1} == G_{-1, -1}` (`0` diff at `38` digits), while upgrading `agy-exp` `NI-4`'s
  numerical periods to exact Chowla–Selberg `Gamma(1/3)` / `B(1/6, 1/3)` closed forms (`< 10^{-37}`):
  `Omega_{LR} = e^{i pi / 6} B(1/6, 1/3) / (4 pi)`, `L_2(omega) = pi + 3 ln Gamma(1/3) - ln pi - (1/2) ln 3 - (7/3) ln 2`, and
  `e^{2 varphi(z_+-)} = (2^{16/3} pi^4) / (3 Gamma(1/3)^6)`, with disjoint pentagonal and Jacobi `eta^3 * eta^1` quadratures
  agreeing with `agy-exp` `NI-4` to `< 10^{-10}`.

0 of 19.
