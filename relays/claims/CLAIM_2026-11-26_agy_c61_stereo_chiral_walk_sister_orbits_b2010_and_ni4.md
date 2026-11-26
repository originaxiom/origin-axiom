# CLAIM CARD — Universal stereo chiral walk decomposition ([W_+, W_-] = 0 in Z[PSL(2,Z)], answering B2008 Open #1), full Markoff congruence surface census & fixed-point-free 24-of-24 sister orbit (3,3,15), explicit S_3 x Z_3 character naming & all-3^k proof of B2010 E1–E2, and analytic X_omega mirror lock & Chowla–Selberg Gamma(1/3) periods (answering B2008 Open #2 / NI-4) (0 of 19)

- seat, branch, commit: agy, origin/agy/cusp-action-2026-11-20, 8aa6ee3c6
- kind: theorem
- touches: A01, A03, P-374, P-630, P-882
- effect: conditions — A01, A03, P-374, P-630, and P-882 (proves [W_+, W_-] = 0 in Z[PSL(2,Z)] with W_+ Pi_q = 3 omega^{-q} Pi_q sigma Pi_q so W_6 projects equal-modulus rays onto (1, -1/2, -1/2) while W_chiral = (W_+ - W_-)/i splits q = 1, 2 with 0 on q = 0; classifies all congruence orbits mod 9/27/81, proving Hensel selection of (3,3,3) and 24-of-24 zero-exception halving on sister (3,3,15); names all 9 characters of S_3 x Z_3 and proves B2010 E1-E2 for all 3^k, k >= 4; and derives exact Chowla-Selberg Gamma(1/3) closed forms and mirror lock on X_omega)
- imports: none (pure group-ring algebra in Z[PSL(2,Z)], congruence Markoff surface geometry, finite-group Frobenius character orthogonality and Hensel fixed-point induction, and modular periods on X_omega; zero Standard Model pass/fail cells; order-30 line kept on hold per M18; strictly 0 of 19)
- premises on main: B1983, B1991, B1992, B1994, B1995, B1999, B2000, B2001, B2002, B2003, B2004, B2005, B2006, B2007, B2008, B2009, B2010, P-374, P-630, P-882
- decisive script: relays/agy_2026-11-26_c61/c61_stereo_chiral_sisters_and_b2010_producer_v2.py, SHA-256 19a623a02bdb6f86, depends on only the standard library, sympy, and mpmath, run as `python3 -I relays/agy_2026-11-26_c61/c61_stereo_chiral_sisters_and_b2010_producer_v2.py`, output SHA-256 5edf6251f001b0a5 (c61_out.json)
- second computation: agy disjoint cold-room countercheck relays/agy_2026-11-26_c61/c61_countercheck.py (pre-committed @ cb2abf6e9, SHA-256 00b0f77812fd3861, output @ 8aa6ee3c6 SHA-256 897cb3f06162ddbc, 72x72 Z[omega] matrices, mp.eig/eighe star-ray & 5*W(alpha) checks, Danilevsky Frobenius companion over 712-bit prime, 19-irrep Burnside class-matrix table, Z-poly & mod 2187 Hensel lift, Jacobi eta^3*eta^1 + Beta(1/6,1/3), discrepancies_count == 0, agrees) and agy-exp X-NATURAL-INTERACTIONS (@ b41678f5d, SHA-256 f6586c83aa31be7d, agrees on NI-4)
- already on main?: topic-sweep /B200[7-9]|B2010|S3 x Z3|mirror|sister orbit|W_chiral|NI-4/ on main (87ba37576): B2007-B2010 prove mirror locking of W_6 and S_3 x Z_3 bottom-of-tower exceptions through mod 243 while leaving open B2008 Open #1 (orientation-picking operator), B2008 Open #2 (NI-4 analytic lock on X_omega), B2010 Open #1 (proof of E1-E2 for all 3^k, k >= 4), B2010 Open #2 (naming the 6 of 9 characters of S_3 x Z_3), and the non-(3,3,3) orbits of F == 0 mod 3^k
- what would make it fail: Controls 1-5 & RPF1-5 — non-cycle L+R+X fails [W, W^*] = 0 (8 terms); B2003's |Fix(C)| = 3 necessity fails on (3,3,15) (|Fix(C)| = 0 yet 24-of-24 exact halving) while 26 parabolic 24-pt orbits at mod 81 have |Fix(C)| = 0 yet gcd == 1; replacing diagonal <((0 1 2), 1)> by <(id, 1)> raises weighted mult from 8 to 12; dropping F == 0 mod 3^{k+1} triples fixed points from 3 to 9; P-odd weight breaks G_{+1} - G_{-1} > 1/2

## Claim (summary, plain words and exact integers/rationals/periods, `0 of 19`)

1. **`E1` — Universal Stereo Chiral Walk Decomposition `[W_+, W_-] = 0` in `Z[PSL(2, Z)]` & Simultaneous Origin of Halving and
   `2 -> 1 + 1` Splitting (`Answering B2008 Open #1`):** Under `C : (x, y, z) -> (y, z, x)` and `sigma = R C^{-1}` (`PSL(2, Z) =
   <C, sigma | C^3 = 1, sigma^2 = 1>`), the `6` moves split into two `C`-invariant directed `3`-cycles `W_+ = L + X + R^{-1} =
   sigma C^{-1} + C sigma C + C^{-1} sigma` and `W_- = R + L^{-1} + X^{-1} = sigma C + C sigma + C^{-1} sigma C^{-1} = W_+^*`,
   swapped by `B2008`'s orientation-reversing mirror `tau` (`tau W_+ tau = W_-`). In `Z[PSL(2, Z)]`, **`[W_+, W_-] == 0`
   identically**, with `W_+ W_- = 3 + sum_{a=0}^2 C^a (L R + (L R)^{-1}) C^{-a}` (`7` reduced words: `3` plus the `C`-orbit of
   the `m004` / `X_omega` systole). On `Pi_q = (1/3)(1 + omega^{-q} C + omega^{-2q} C^2)` (`q in {0, 1, 2}`) with Hermitian
   `H_q = Pi_q sigma Pi_q`, **`W_+ Pi_q = Pi_q W_+ = 3 omega^{-q} H_q`** and **`W_- Pi_q = 3 omega^{+q} H_q`**: before
   mirror-averaging, all three sectors have equal radial scale `3` along the `120`-degree star rays `(1, omega^2, omega)`.
   Mirror-averaging `W_6 = W_+ + W_- = 6 H_0 - 3 H_1 - 3 H_2` projects onto real parts `(1, -1/2, -1/2)` — creating both the
   `1/2` halving factor and `B2008`'s `q = 1, 2` lock — while muting the commuting `tau`-odd operator
   `W_{chiral} = (W_+ - W_-) / i = 0 * H_0 - 3 sqrt(3) H_1 + 3 sqrt(3) H_2` (`[W_6, W_{chiral}] = 0`, zero on `q = 0`, opposite
   signs on `q = 1, 2`). Any oriented Peierls phase `W(alpha) = cos(alpha) W_6 + sin(alpha) W_{chiral}` splits `3 -> 1 + 1 + 1`
   with exact ratios `cos(alpha) : cos(alpha + 2 pi / 3) : cos(alpha - 2 pi / 3)` (`sum = 0`, `sum_sq = 54` for `6 cos`).

2. **`E2` — Full Congruence Surface Census (`mod 9, 27, 81`), Hensel Selection of `(3, 3, 3)`, & `24`-of-`24` Zero-Exception
   Halving on Sister Orbit `(3, 3, 15)` (`Sharpening B2003 R4`):** Exhaustive `<L, R>` decomposition of `F = x^2 + y^2 + z^2 -
   x y z == 0 mod 3^k` yields `4` orbits `(12, 8, 6, 1)` on `27` points at `mod 9`, `7` orbits (`three 72-pt sisters (3,3,3),
   (3,3,12), (3,3,15)` plus `12, 8, 6, 1`) on `243` points at `mod 27`, and `42` orbits (`three 648-pt sisters (3,3,3),
   (3,3,30), (3,3,33)`, `26` parabolic `24`-pt orbits, plus `4` each of `12, 8, 6` and `1` of `1`) on `2,673` points at `mod 81`.
   The `<L, R, C, tau>`-invariant `nu_k = (F / 3^k) mod 3 in {0, 1, 2}` kills both obstructed sisters `nu_k in {1, 2}` at the
   next rung (`0` lifts), selecting `(3, 3, 3)` (`nu_k = 0` for all `k`) as the unique projective-limit `3`-adic orbit. At
   `mod 27`, because `a^2 (1 - a) mod 3 in {0, 2}` for `3` not dividing `a`, the `nu_3 = 1` sister `(3, 3, 15)` (`F == 27 mod
   81`) has `|Fix(C)| = 0` (`dims 24 + 24 + 24`), forcing `Stab_{G_3}((3,3,15)) <= ker(chi_C)` so `m(pi) = m'(pi)` on all `19`
   irreducibles of `G_3` (`0` exceptions) and **`p_{neutral}(2x) == 2^{24} S(x)` over `Z[x]`**, with
   `x S_{(3,3,15)}(x) == (x^2 - 9) S_{(3,3,3)}(x)` (`charged modes acquire +-3 = (1/2)(+-6)`). At `mod 81`, all three `648`-pt
   sisters share `nu_3 = 0`, `|Fix(C)| = 3`, and identical `S(x)` (`SHA-256 32bdae9d56a62d2c`), while all `26` parabolic `24`-pt
   orbits have `|Fix(C)| = 0` yet `gcd(p_{neutral}(2x), S(x)) == 1`.

3. **`E3` — Canonical Naming of All `9` Characters of `S_3 x Z_3` & All-`3^k` (`k >= 4`) Proof of `B2010` `E1`–`E2` (`Closing
   Both Open Questions of B2010`):** `pi_18 = (pi_{PSL(2, F_2)}, chi_C) : G_k ->> PSL(2, F_2) x Z_3 ~= S_3 x Z_3` (`common
   exception kernel order 12 at mod 27`, verified independently via Burnside class-multiplication diagonalization of all `19`
   irreducibles of `G_3`: `13` paired + `6` unpaired) maps `S_k = Stab_{G_k}((3, 3, 3))` onto the diagonal subgroup
   `<((0 1 2), 1)>`. Writing `psi_0(1) = rho(C) = omega`, the `9` irreducibles `chi_alpha (x) psi_0^r` split into `3`
   neutral-excess exceptions `(m, m') = (1, 0)` with `C`-neutral dim `1` (`1 x 1` constant `+6`, `sgn x 1` alternation `-6`,
   `2 x psi_0` null `0`), `3` charged-excess exceptions `(m, m') = (0, 1)` with `C`-neutral dim `0` (`1 x psi_0`, `sgn x psi_0`,
   `2 x 1`), and `3` paired characters `m = m'` (`1 x bar{psi}_0` `[0=0]`, `sgn x bar{psi}_0` `[0=0]`, `2 x bar{psi}_0` `[1=1]`).
   Since `|S_k|` is a `3`-power, `rho|_{S_k} = chi_C|_{S_k}`; by Frobenius reciprocity and character orthogonality, `B2010` `E1`
   and `E2` hold at level `3^k` iff `|Fix_{O_{3^k}}(g)| == |Fix_{O_{27}}(g mod 27)|` for all `g in G_k` with `chi_C(g) != 1`.
   Conjugating any fixed-point element to `n * C^{+-1}` (`n_{red}(b) = b + 9 Phi(b)`), base `k = 4` holds across all `1,296`
   charged elements of `G_4`; for `k >= 5`, `9 * 3^{k-3} = 3^{k-1}`, `F_{red}` invariance (`w_1 + w_2 + w_3 == 0 mod 3`), and
   `sum_i d_{b_i} F_{red} == -3 mod 9` (`kills 2 of 3 base t's while preserving all 3 diagonal s's`) force `|Fix_{O_{3^k}}(n * C)|
   == 3` for all `k >= 4` (`exhaustively verified across all 243 elements of N_5 at mod 243 and Hensel-checked through mod 2,187`).

4. **`E4` — Analytic `X_omega` Mirror Lock, Exact Chowla–Selberg `Gamma(1/3)` Periods, & Disjoint `NI-4` Second Computation
   (`Closing B2008 Open #2`):** On `X_omega = H / [SL(2, Z), SL(2, Z)]`, hyperbolic reflection `w -> -conj(w)` sends
   `z(w) -> -e^{-i pi / 3} conj(z(w))` (`< 10^{-39}`), reversing `omega`'s `Z_3` charge and locking `G_{+1, +1} == G_{-1, -1}`
   (`0` diff at `38` digits). Proves exact Chowla–Selberg closed forms (`< 10^{-37}`) upgrading `agy-exp` `NI-4`:
   `Omega_{LR} = e^{i pi / 6} B(1/6, 1/3) / (4 pi) = e^{i pi / 6} (sqrt(3) / (2^{7/3} pi^2)) Gamma(1/3)^3`,
   `|eta(e^{i pi / 3})|^4 = (sqrt(3) / (16 pi^4)) Gamma(1/3)^6`,
   `L_2(omega) = pi + 3 ln Gamma(1/3) - ln pi - (1/2) ln 3 - (7/3) ln 2 = pi - ln(12 / B(1/6, 1/3))`, and
   `e^{2 varphi(z_+-)} = (2^{16/3} pi^4) / (3 Gamma(1/3)^6)`, while disjoint pentagonal and Jacobi `eta^3 * eta^1` quadratures
   independently verify `NI-4`'s area `2 pi` (`< 10^{-20}`) and even/odd/trilinear overlaps (`< 10^{-10}` vs `agy-exp`).

0 of 19.
