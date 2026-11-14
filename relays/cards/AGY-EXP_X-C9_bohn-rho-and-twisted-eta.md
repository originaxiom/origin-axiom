# CARD `X-C9` (`AGY-EXP`): SECOND INDEPENDENT COMPUTATION OF `SM-C9` — BOHN'S RHO INVARIANT, THE SEALED `Z(0)` NEGATIVE, THE TWISTED ETA IDENTITY ON `601` AND FRESH CHARACTERS, AND THE SYMPLECTIC FOURIER BRIDGE (`M16`)

- **Seat:** `agy-exp` (branch `origin/agy/self-consistent-loop-2026-11-11`)
- **Assigned by:** `M16` on `docs/seats/agy-exp.md` at `origin/main` `2a43ad52d` ("`X-C9`, first, at the author's word")
- **Target under test:** `SM-C9` (`relays/SM_C9_THE_L_VALUE_AS_A_RHO_INVARIANT.md` and `relays/cards/SM_C9_the-L-value-as-a-rho-invariant.md` on `origin` SM seat branch at `2e1b88a7d`)
- **Date:** `2026-11-14`
- **Protocol:** expectations, failure criteria, and planted controls are committed in this card before any script for `X-C9` is written or run; standalone script `relays/x_c9_verify/verify_x_c9.py` (`zero` imports from `main` or any other seat, `zero` reads of `SM-C7` or `SM-C9` `.py` or `.json` files) is committed with `SCRIPT_SHA256.txt` before its single execution; unread output `relays/x_c9_verify/verify_x_c9_out.json` is committed with `OUTPUT_SHA256.txt` before reading; closing report is written in words, exact integers, and exact fractions only (`0 of 19`).

---

## 1. Part `1` — Independent Transcription of Bohn's Rho Invariant (`Chapter IV, Section 4, Theorem 20`)

### Primary Source & Formulas Transcribed
Directly from Michael Bohn's primary dissertation source (*On rho invariants of fiber bundles*, `2009`, Chapter IV, Section `4`), for any hyperbolic monodromy `M = [[a, b], [c, d]]` in `SL(2, Z)` with `c != 0` and any non-integral torsion vector `nu = (nu_1, nu_2)` in `Q^2 \ Z^2` satisfying `m = (m_1, m_2)^T = (I - M^T) nu` in `Z^2`:
- Let `r` in `{0, ..., |c| - 1}` be the unique non-negative residue satisfying `m_1 ≡ r (mod |c|)`; let `delta(x)` equal `0` on `Z` and `1` on `R \ Z`; let `P_1(x)` equal `0` on `Z` and `{x} - 1/2` on `R \ Z`; and let `P_2(x) = {x}^2 - {x} + 1/6`.
- **Expanded formula (`Chapter IV, Section 4, Theorem 20`):**
  `rho_A(T^2_M) = ((2(a + d) - 4) / c) * (P_2(nu_1) - 1/6) - 4 * sum_{k=1}^{|c| - r} P_1(d k / c) + sgn(c(a + d)) - sgn(c) * delta(nu_1) * (1 - delta(m_1 / c)) - 2 * P_1(d m_1 / c) - 2 * delta(nu_1) * (P_1(m_1 / c) - P_1(d m_1 / c))`.
- **Generalized Dedekind-sum formula (`Chapter IV, Equation 67`):**
  `rho_A(T^2_M) = (2(a + d) / c) * (P_2(nu_1) - 1/6) - 4 * sgn(c) * (s_{nu_1, nu_2}(a, c) - s(a, c)) + sgn(c(a + d))`,
  where `s_{nu_1, nu_2}(a, c) = sum_{k=0}^{|c| - 1} P_1((k + nu_1) / c) * P_1(a * (k + nu_1) / c + nu_2)` and `s(a, c) = s_{0, 0}(a, c)`.
- **Untwisted eta invariant (`Chapter IV, Section 4, Theorem 12`, Atiyah–Hirzebruch–Meyer):**
  `eta(T^2_M) = (a + d) / (3 c) - 4 * sgn(c) * s(a, c) - sgn(c(a + d)) = Psi(M) / 3`.

All three formulas are evaluated in exact `fractions.Fraction` rational arithmetic.

### Literature Benchmark Gate (`Guardrail 4`) & Transcription Checks (`T1`–`T4`)
Before evaluating any character of the `601`-character population, the script enforces:
- **`G1` (Bohn worked example one):** `M = [[-2, 1], [1, -1]]` at `nu = (1/5, 3/5), (2/5, 1/5), (3/5, 4/5), (4/5, 2/5)` produces exact rationals `8/5, 12/5, 12/5, 8/5` in both `Theorem 20` and `Equation 67`.
- **`G2` (Bohn worked example two):** `M = [[3, 2], [4, 3]]` at `nu = (0, 1/2), (1/2, 0), (1/2, 1/2)` produces exact rationals `0, 0, 1` in both forms.
- **`G3` (Untwisted Meyer–Rademacher benchmark):** On all `16` levels of `B1737`, `eta(T^2_M)` equals `0` on the eight `LR` levels and `-LLRR 1`, `+1` on `+LLR 3` and `-LLR 3`, `+2` on `+LLLR 3`, `+2/3` on `+LLRLR 2`, `-LLLRLR 1`, and `-LLR 2`, and `+1/3` on `-LLRLR 1` (matching `-4` times `B1737` Section `2`'s `-Psi(M)/12` on all `16` levels).
- **`T1` (`Theorem 20` vs `Equation 67`):** Exact rational difference equal to `0` on `100%` of the `601` population characters and `100%` of the fresh out-of-sample characters (`nu = -c`).
- **`T2` (`Chapter IV, Section 4, Corollary 21`, Chern–Simons fractional part):** `rho_A(T^2_M) - 2(nu_2 m_1 - nu_1 m_2)` is an exact integer (`denominator == 1`) on `100%` of tested characters.
- **`T3` (Orientation reversal):** `rho_A(M^{-1}, nu) + rho_A(M, nu) = 0` in exact rationals on `100%` of tested characters.
- **`T4` (`SL(2, Z)` fibre-basis invariance):** Under `M -> P M P^{-1}` and `nu -> P^{-T} nu` for `P = [[1, 1], [0, 1]]` and `P = [[2, 1], [1, 1]]` (whenever `(P M P^{-1})_{2,1} != 0`), `rho_A` is strictly invariant (`exact rational difference == 0`) on `100%` of tested characters.

---

## 2. Part `2` — Independent Recomputation of `Z(0, chi_c)` and the Sealed Affine-Fit Negative

### Independent Two-Route Recomputation of `Z(0, chi_c)`
Without reading `SM-C7` or `SM-C9`'s JSON tables, `verify_x_c9.py` generates all `16` signed word levels of `B1737` (`+LR 2..5`, `+LLR 3`, `+LLLR 3`, `+LLRLR 2`, `-LR 1..4`, `-LLRLR 1`, `-LLLRLR 1`, `-LLR 2..3`, `-LLRR 1`, expected total `601` non-trivial characters fixed by `M`: `(i, j) M ≡ (i, j) mod N`) from `L = [[1, 1], [0, 1]]`, `R = [[1, 0], [1, 1]]`, `M(+w, k) = M(w)^k`, `M(-w, k) = (-M(w))^k`, and computes `Z(0, chi_c)` by **two** independent methods on every character:
1. **Shintani cone parallelogram lattice sum (`B1737` Section `1`):** Choose two independent primitive lattice vectors `w_1, w_2` in the positive eigen-covector cone `C_+ = {v in Z^2 : v_0 beta + v_1 > 0 and v_0 beta' + v_1 > 0}` of `gamma = M^T` with `chi_c(w_r) != 1`, enumerate all `|det(w_r, gen * w_r)|` lattice points `p` in the half-open parallelogram `Pi(w_r, gen * w_r)` (`gen = M` if `tr(M) > 0`, `gen = M^2` with value halved if `tr(M) < 0`), verify `|Z_{w_1}(0, chi_c) - Z_{w_2}(0, chi_c)| < one part in ten to the twelfth`, and verify that `Z(0, chi_c) - (1/2) * #(-I)` matches `B1438` Theorem D's letter-by-letter algebraic slope `s(chi_c)` wherever the `sigma(x) = 0` gauge is non-singular.
2. **Geodesic period quadrature (`SM-C7` Step `1`):** Integrate `(1 / (4 pi^2)) * int_{z_0}^{gamma z_0} G^{(Jc)*}(z) dz` along the invariant hyperbolic semicircle of `gamma = M^T` using the closed-form geometric-summed Lipschitz `q`-series (`48`-node vs `96`-node Gauss–Legendre quadrature), verifying agreement with the Shintani cone sum to better than one part in ten to the eleventh on all `601` characters.

### Committed Expectation for Part `2`
- **Population counts:** Exactly `16` levels and `601` non-trivial `M`-fixed characters (`4, 15, 44, 120, 49, 107, 95, 4, 4, 19, 44, 11, 14, 11, 53, 7`).
- **Distinct-value levels:** Exactly `13` of the `16` levels carry `3` or more distinct values of `Z(0, chi_c)` (the three `4`-character levels `+LR 2`, `-LR 1`, `-LR 2` each carry `2` distinct values because `Z(0, chi_c)` is even under `c -> -c`).
- **Affine-fit negative (`REPRODUCED` expected):** On **`12` of the `13` levels** with `3` or more distinct values of `Z(0, chi_c)`, `rho_A(T^2_M, -c)` is **not** an affine function of `sqrt(D) * Z(0, chi_c)` (maximum absolute residual exceeding one tenth on every one of those `12` levels, with `12` distinct least-squares slopes). The unique exception among the `13` levels is **`+LR 3`** (`N = 4`, `15` characters, `3` distinct values `{-1, 0, +1}`), where `rho_A = -Z(0, chi_c)` (`slope = -1 / sqrt(320)` against `sqrt(D) * Z(0)`) holds with `zero` residual because `M ≡ I (mod 4)` and `Z(0, chi_c)` on `(Z/4Z)^2` happens to lie in a single eigenspace of the `2`D symplectic Fourier transform.

---

## 3. Part `3` — The Twisted Eta Identity `eta_A = rho_A + eta(T^2_M) = -L_odd(1, chi_c) / pi^2` on `601` In-Sample and `> 500` Fresh Out-of-Sample Characters

### Independent Two-Route Computation of `L_odd(1, chi_c)`
For each character `c = (i/N, j/N)` (`Jc = (-c_2, c_1) mod 1`, `nu = -c`), `verify_x_c9.py` computes `L_odd(1, chi_c)` independently via:
1. **Closed-form Lipschitz `q`-series contour quadrature:** `int_{z_0}^{gamma z_0} G_c(z) dz` (`48`-node vs `96`-node Gauss–Legendre quadrature, plus basepoint-independence check at a second point `z_1 != z_0`);
2. **Continuous Siegel theta phase winding:** `-2 pi i * Delta_gamma log g_{Jc}(z)` tracked continuously along `z(t)` from `z_0` to `gamma z_0`.

### Fresh Out-of-Sample Population (Committed Before Any Run)
In addition to all `601` characters of `B1737` / `SM-C7`, we seal an out-of-sample test suite of **`10` fresh hyperbolic levels (`529` unseen characters)** outside the `601`-character population:
1. `+LR 6` (`319` characters, trace `322`, `N = 80`);
2. `-LR 5` (`124` characters, trace `-123`, `N = 25` or `125` — exact `|det(I - M^T)| - 1 = 124`);
3. `+LLR 2` (`11` characters, trace `14`);
4. `+LLLR 2` (`20` characters, trace `23`);
5. `+LLRR 2` (`31` characters, trace `34`);
6. `+LLLRLR 1` (`10` characters, trace `13`);
7. `-LLLR 1` (`6` characters, trace `-5`);
8. `+LLLLR 1` (`3` characters, trace `6`);
9. `Bohn_Ex1` (`M = [[-2, 1], [1, -1]]`, `4` characters, trace `-3`);
10. `Bohn_Ex2` (`M = [[3, 2], [4, 3]]`, `3` characters, trace `6`).
*(Total fresh unseen characters: `319 + 124 + 11 + 20 + 31 + 10 + 6 + 3 + 4 + 3 = 531` characters across `10` unseen matrices!)*

### Committed Expectations for Part `3` & Symplectic Fourier Bridge
1. **In-sample (`601` of `601`) and out-of-sample (`531` of `531`) twisted-eta identity:** On **every single character** (`1,132` of `1,132`), `|eta_A(T^2_M) + L_odd(1, chi_c) / pi^2|` is smaller than one part in ten to the eleventh, and the nearest bounded-denominator rational to `-L_odd(1, chi_c) / pi^2` equals `eta_A(T^2_M) = rho_A(T^2_M) + eta(T^2_M)` in **exact rational arithmetic (`zero` discrepancy on `1,132` of `1,132`)**.
2. **Unconditional analytical theorem (written out in the closing report):** Combining Dieter's transformation formula for generalized Dedekind eta functions (`Bohn, Chapter IV, Section 4, Theorem 16`), `Proposition 19`, `Theorem 12`, and `Equation 67` cancels all three untwisted Dedekind/trace/sign terms identically and proves `eta_A(T^2_M) = -L_odd(1, chi_c) / pi^2` unconditionally for **every** hyperbolic `M in SL(2, Z)` and **every** non-trivial `M`-fixed torsion character `c`.
3. **Symplectic Fourier bridge (`What the wall teaches`, verified numerically on principal congruence levels `+LR 3` and `+LR 5`):** On every principal congruence level `M ≡ I (mod N)`, verify to better than one part in ten to the eleventh that `-eta_A(T^2_M, c) / 4 = L_odd(1, chi_c) / (4 pi^2)` equals the exact `2`D symplectic discrete Fourier transform `(1 / N^2) * (-Psi(M) / 12 + sum_{c' != 0} exp(2 pi i N (c_2 c'_1 - c_1 c'_2)) * Z(0, chi_{c'}))`, demonstrating directly why `rho_A` mixes distinct `M`-orbits of `Z(0, chi_{c'})` whenever `N` supports multiple even orbits (and why on non-congruence levels `M != I mod N`, `eta_A` additionally couples to slopes of higher cyclic covers `M^r` through non-fixed torsion shifts `u` in `((1/N)Z/Z)^2`).

---

## 4. Five Planted Controls (`P1`–`P5`, Committed First)

1. **`P1` (Orientation flip `M -> M^{-1}`):** Replacing `M` by `M^{-1}` flips the sign of `eta_A(T^2_M)` and breaks `eta_A + L_odd(1, chi_c) / pi^2 = 0` on `100%` of characters where `eta_A != 0` (expected `561` of `601` in-sample characters, `40` vanishing).
2. **`P2` (Within-level cyclic permutation of `Z(0, chi_c)`):** Deterministic cyclic shift of `Z(0)` among a level's ordered characters breaks the affine fit on all `13` of `13` levels with `3` or more distinct values (including `+LR 3`).
3. **`P3` (Omitting untwisted `eta(T^2_M)`):** Testing `rho_A + L_odd(1, chi_c) / pi^2 = 0` without `+ eta(T^2_M)` fails by exact `-eta(T^2_M) != 0` on all `7` of `7` non-zero-`eta` levels in the `16`-level population (`240` characters).
4. **`P4` (Replacing `c` by `Jc` on one side only):** Comparing `eta_A(T^2_M, -c)` against `-L_odd(1, chi_{Jc}) / pi^2` fails on every character where `eta_A(-c) != eta_A(-Jc)`.
5. **`P5` (Bracket misreading `2(a + d) - 4/c` in `Theorem 20`):** Replacing `(2(a + d) - 4) / c` with `2(a + d) - 4 / c` breaks `T1` (`Theorem 20 == Equation 67`) on a large majority of the `601` characters (`540` expected).

0 of 19.
