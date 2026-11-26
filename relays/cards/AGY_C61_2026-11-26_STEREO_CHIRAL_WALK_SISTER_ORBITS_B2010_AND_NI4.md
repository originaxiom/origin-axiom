# `Card AGY-C61` (`2026-11-26`) — Pre-Execution Expectations: Stereo Chiral Walk (`[W_+, W_-] = 0`), Sister Orbits, `B2010` `S_3 x Z_3` Proof, & `X_omega` Periods (`0 of 19`)

- **Seat / Branch / Base Commit:** `agy` / `origin/agy/cusp-action-2026-11-20` / `5bdaced13`
  (frozen harvest branch `origin/agy/audit-2026-11-02` untouched at `4319f47e2`)
- **Synced Premises:** `origin/main @ 87ba37576` (`M18`, `B1999`–`B2010`, `P-882`, `P-374`),
  `agy-exp @ 4c1d39aa3` (`b41678f5d`, `NI-4`), `agy-002 @ 2d2ac11a4` (`A2-WHOLE-INSTRUMENT`)
- **Strict Scope (`0 of 19`):** Pure group-ring algebra in `Z[PSL(2, Z)]`, congruence Markoff surface
  decomposition, finite-group character orthogonality and Hensel fixed-point induction, and
  Chowla–Selberg modular periods on `X_omega`. Zero empirical constants, zero added parameters,
  zero Standard Model pass/fail cells; order-`30` line kept on hold per `M18` item `5`.

---

## Pre-Committed Expectations (`E1`–`E4`) and Falsification Controls (`Controls 1`–`5`)

1. **`E1` (`Universal Stereo Chiral Decomposition [W_+, W_-] = 0 & Origin of Halving / 2 -> 1 + 1 Split`):**
   - Under `C : (x, y, z) -> (y, z, x)` and `sigma : (x, y, z) -> (y, x, x y - z)`
     (`PSL(2, Z) = <C, sigma | C^3 = 1, sigma^2 = 1>`), the six moves factor as `L = sigma C^{-1}`,
     `X = C sigma C`, `R^{-1} = C^{-1} sigma` (`forming W_+ = L + X + R^{-1}`) and `R = sigma C`,
     `L^{-1} = C sigma`, `X^{-1} = C^{-1} sigma C^{-1}` (`forming W_- = R + L^{-1} + X^{-1}`),
     swapped by `B2008`'s orientation-reversing mirror `tau : (x, y, z) -> (y, x, z)` (`tau W_+ tau = W_-`).
   - **Expectation `E1a`:** In the universal integral group ring `Z[PSL(2, Z)]`, `[C, W_+] == 0`,
     `[C, W_-] == 0`, and **`[W_+, W_-] == 0` identically**, with
     `W_+ W_- = W_- W_+ = 3 + sum_{a=0}^2 C^a (L R + (L R)^{-1}) C^{-a}`.
   - **Expectation `E1b`:** On `Pi_q = (1/3)(1 + omega^{-q} C + omega^{-2q} C^2)` (`q in {0, 1, 2}`)
     with Hermitian `H_q = Pi_q sigma Pi_q`, `W_+ Pi_q = Pi_q W_+ = 3 omega^{-q} H_q` and
     `W_- Pi_q = Pi_q W_- = 3 omega^{+q} H_q`. Hence `W_6 = W_+ + W_- = 6 H_0 - 3 H_1 - 3 H_2`
     projects equal-modulus rays `(1, omega^2, omega)` onto real parts `(1, -1/2, -1/2)` — creating
     both the `1/2` halving scale and `B2008`'s `q = 1, 2` lock — while commuting with
     `W_{chiral} = (W_+ - W_-) / i = 0 * H_0 - 3 sqrt(3) H_1 + 3 sqrt(3) H_2`, which vanishes on `q = 0`
     and splits `q = 1, 2` with opposite signs (`verified on O_27, O_81, and O_243`). Any oriented walk
     `W(alpha) = cos(alpha) W_6 + sin(alpha) W_{chiral}` splits `3 -> 1 + 1 + 1` with exact ratios
     `cos(alpha) : cos(alpha + 2 pi / 3) : cos(alpha - 2 pi / 3)` (`B2008` Open #1).
   - **Control 1 (Planted Non-`C`-Cycle Walk):** Replacing `W_+ = L + X + R^{-1}` by `W_{bad} = L + R + X`
     breaks `[C, W_{bad}] = 0` and `[W_{bad}, W_{bad}^*] = 0` (`8 non-zero terms in Z[PSL(2, Z)]`).

2. **`E2` (`Full Congruence Surface Census, Hensel Selection of (3,3,3), & 24-of-24 Sister Orbit`):**
   - **Expectation `E2a`:** Counting all `N^3` solutions of `F(x, y, z) = x^2 + y^2 + z^2 - x y z == 0 mod 3^k`:
     `mod 9` (`27` solutions) splits into `4` `<L, R>`-orbits `(12, 8, 6, 1)`; `mod 27` (`243` solutions)
     splits into `7` orbits (`three 72-point sisters (3,3,3), (3,3,12), (3,3,15) plus 12, 8, 6, 1`);
     `mod 81` (`2,673` solutions) splits into `42` orbits (`three 648-point sisters (3,3,3), (3,3,30),`
     `(3,3,33), 26 parabolic 24-point orbits, and 4 each of 12, 8, 6 plus 1 of 1`).
   - **Expectation `E2b`:** On the smooth `3`-locus of `F == 0 mod 3^k` (`k >= 3`),
     `nu_k(x, y, z) = (F(x, y, z) / 3^k) mod 3 in {0, 1, 2}` is `<L, R, C, tau>`-invariant; both
     obstructed sisters `nu_k in {1, 2}` have `0` lifts to `F == 0 mod 3^{k+1}`, selecting `(3, 3, 3)`
     (`nu_k = 0` for all `k`) as the unique projective-limit `3`-adic orbit.
   - **Expectation `E2c`:** At `mod 27`, because `a^2 (1 - a) mod 3 in {0, 2}` for `3` not dividing `a`,
     the `nu_3 = 1` sister `(3, 3, 15)` (`F == 27 mod 81`) has `|Fix(C)| = 0` (`dims 24 + 24 + 24`),
     `Stab_{G_3}((3,3,15)) <= ker(chi_C)`, and satisfies **`p_{neutral}(2x) == 2^{24} S(x)` over `Z[x]`
     with ZERO left-out exceptions**, with `x S_{(3,3,15)}(x) == (x^2 - 9) S_{(3,3,3)}(x)`. At `mod 81`,
     all three `648`-point sisters (`all having nu_3 = 0` and `|Fix(C)| = 3`) satisfy
     `p_{neutral}(2x) == 2^{218} x (x^2 - 9) S(x)` over `Z[x]` with identical `S(x)`.
   - **Control 2 (Planted Fixed-Point / Parabolic Counterchecks):** Asserting `|Fix(C)| = 3` is required
     for halving (`B2003` `R4`) is refuted by `(3, 3, 15)`, whereas all `26` parabolic `24`-point orbits
     at `mod 81` have `|Fix(C)| = 0` (`dims 8 + 8 + 8`) yet give `gcd(p_{neutral}(2x), S(x)) == 1`.

3. **`E3` (`Explicit Naming of All 9 Characters of S_3 x Z_3 & All-3^k Proof of B2010 E1–E2`):**
   - **Expectation `E3a` (`B2010` Open #2):** `pi_18 = (pi_{PSL(2, F_2)}, chi_C) : G_k ->> S_3 x Z_3`
     (`kernel orders 12, 108, 2,916 at mod 27, 81, 243`) maps `S_k = Stab_{G_k}((3, 3, 3))` onto the
     diagonal subgroup `<((0 1 2), 1)>`. Naming all `9` irreducibles `chi_alpha (x) psi_0^r`
     (`alpha in {1, sgn, 2}`, `r in {0, 1, 2}`, `psi_0(1) = rho(C)`): `(m, m') = (1, 0)` on
     `{1 (x) 1, sgn (x) 1, 2 (x) psi_0}` (`C-neutral dim 1: +6, -6, 0`); `(m, m') = (0, 1)` on
     `{1 (x) psi_0, sgn (x) psi_0, 2 (x) 1}` (`C-neutral dim 0`); and paired `m = m'` on
     `{1 (x) bar{psi}_0 (0=0), sgn (x) bar{psi}_0 (0=0), 2 (x) bar{psi}_0 (1=1)}`.
   - **Expectation `E3b` (`B2010` Open #1):** By Frobenius reciprocity and character orthogonality, `E1`
     and `E2` hold at level `3^k` iff `|Fix_{O_{3^k}}(g)| == |Fix_{O_{27}}(g mod 27)|` for all `g in G_k`
     with `chi_C(g) != 1`. Every fixed-point element outside `ker(chi_C)` conjugates to `n * C^{+-1}`
     (`n_{red}(b) = b + 9 Phi(b)`). Base `k = 4` holds on all `1,296` charged elements of `G_4`; for
     `k >= 5`, `9 * 3^{k-3} = 3^{k-1}`, `F_{red}` invariance (`w_1 + w_2 + w_3 == 0 mod 3`), and
     `sum_i d_{b_i} F_{red} == -3 mod 9` force `|Fix_{O_{3^k}}(n * C)| == 3` (`exhaustively verified on
     all 243 elements of N_5 at mod 243 and symbolically/fiber-tested at mod 729`).
   - **Control 3 & Control 4:** Replacing `<((0 1 2), 1)>` by `<(id, 1)>` in `S_3 x Z_3` gives `9`
     exceptions instead of `6`; dropping `F_{red} == 0 mod 3^{k-1}` triples fixed points from `3` to `9`.

4. **`E4` (`Analytic X_omega Mirror Lock, Exact Chowla–Selberg Periods, & Disjoint NI-4 Check`):**
   - **Expectation `E4a`:** On `X_omega = H / [SL(2, Z), SL(2, Z)]`, reflection `w -> -conj(w)` sends
     `z(w) -> -conj(z(w))`, locking `G_{+1, +1} == G_{-1, -1}` (`< 10^{-28}`) while `NI-4`'s numerical
     periods equal exact Chowla–Selberg closed forms (`< 10^{-32}`):
     `Omega_{LR} = e^{i pi / 6} (sqrt(3) / (2^{7/3} pi^2)) Gamma(1/3)^3`,
     `|eta(e^{i pi / 3})|^4 = (sqrt(3) / (16 pi^4)) Gamma(1/3)^6`,
     `L_2(omega) = pi + 3 ln Gamma(1/3) - ln pi - (1/2) ln 3 - (7/3) ln 2`, and
     `e^{2 varphi(z_+-)} = (2^{16/3} pi^4) / (3 Gamma(1/3)^6)`.
   - **Expectation `E4b` & Control 5:** Disjoint Euler pentagonal `q`-series + `20`-point Gauss–Legendre
     quadrature independently reproduces `NI-4`'s area `2 pi`, even/odd `G_{00} / G_{11}`, and trilinear
     `C_{0, +, -}` (`< 10^{-11}` vs `agy-exp`), while a `P`-odd chiral weight splits `G_{+1} - G_{-1} > 1/2`.

0 of 19.
