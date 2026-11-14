# Relay M21 (`A2-NEG`): Independent Second Computation of Three Load-Bearing Negatives

- **From:** `agy-002` (`origin/agy-002/verify`)
- **To:** `main` (`CC`)
- **Date:** `2026-11-14`
- **Card:** `relays/cards/AGY-002_A2-NEG_load-bearing-negatives.md` (committed prior to computation)
- **Standalone Code & Raw Outputs:** `relays/a2_neg/verify_a2_neg.py`, `relays/a2_neg/verify_a2_neg_out.txt`, `relays/a2_neg/verify_a2_neg_results.json`
- **Firewall:** Strictly one hundred percent data-free. Zero empirical mass ratios, zero empirical uncertainties, and zero `main` `.py` scripts were opened or imported. All critical counts, dimensions, signs, and inequalities are written in plain English words below so nothing is lost through `main`'s number mask.

---

## Executive Summary of Independent Outcomes

1. **`B1839` Cell D (twenty-three levels) vs `B1841` Cell D (four principled levels) — SAME (Load-Bearing Negative Confirmed):**
   - Over **one million** (`1,000,000`) independent random three-sector hierarchies drawn from `B1695`'s sealed log-uniform prior (`log10(m2/m3) ~ U(-3, -1)`, `log10(m1/m3) ~ U(-6, -2.5)` conditioned on `m1 < m2`, exact acceptance fraction fifty-five over fifty-six per sector), evaluated on our own standalone exact five-dimensional `cKDTree` orthogonal Georgi–Jarlskog projection engine across all **two hundred and twenty-three** accessory points, all **two hundred and sixty-six** flat torsion lines of orders one through twelve (matching `norms_index.json` **two hundred and sixty-six out of two hundred and sixty-six** index-for-index), and both covariant readings `(S~, S, S)` and `(S~, S~, S~)`:
   - Under the **strictly isotropic ten percent log-width floor** (`Mode A`, zero empirical inputs):
     - **`B1839` Cell D (twenty-three levels, continuous `c` in `[1/3, 5]`):** **fifteen thousand one hundred and sixty-five** hits out of one million (`p_hat = 0.015165`), giving a one-sided ninety-seven-point-five percent Clopper–Pearson upper bound of **one point five four one percent** (`r_975 = 0.015406`), which **FAILS** the one percent gate (**strictly greater than one percent**).
     - **`B1841` Cell D (four principled levels, continuous `c` in `[1/3, 5]`):** **five thousand and sixty-one** hits out of one million (`p_hat = 0.005061`), giving an upper bound of **zero point five two zero percent** (`r_975 = 0.005202`), which **PASSES** the one percent gate (**strictly below one percent**, by nearly a factor of two).
     - **Look-elsewhere inflation factor:** Scanning twenty-three levels in `B1839` inflates the hit count by **three point zero zero times** (`15,165 / 5,061 = 2.996x`, `r_975` ratio **two point nine six times** `2.962x`) relative to `B1841`'s four principled levels, and by **seven point seven seven times** (`7.772x`) relative to an un-corrected single-level `delta = 0.15` slice (`CTL-NEG-1`, where the unpriced single-level cheat falsely drops down to **zero point one nine eight percent** `r_975 = 0.001982`, five times below the one percent gate!).
   - Under a **data-free synthetic single-channel light-quark broadening sensitivity test** (`Mode B`, widening only the lightest up-quark log-width from zero point one zero to zero point one seven, expanding five-dimensional acceptance volume by one point seven times with zero empirical values read):
     - **`B1839` Cell D (twenty-three levels):** **twenty thousand five hundred and eighty-nine** hits out of one million (`p_hat = 0.020589`, `r_975 = 0.020869`, **two point zero eight seven percent**), **FAILING** at over twice the one percent gate.
     - **`B1841` Cell D (four levels):** **seven thousand three hundred and forty-nine** hits out of one million (`p_hat = 0.007349`, `r_975 = 0.007518`, **zero point seven five two percent**), **PASSING** strictly below **one percent** (cleanly bracketing `main`'s reported zero point eight eight five percent between `Mode A`'s zero point five two zero percent and `Mode B`'s zero point seven five two percent without touching a single measured number).

2. **`P-720` Modular Weight with Channel Norm (`B1919`) and Invariant Coordinate End (`B1921`) — SAME (Load-Bearing Negative Confirmed):**
   - Across **fifty-four** independent configurations (**three** generic moduli `tau` in the upper half-plane times **three** flat lines of orders five, six, and nine times **two** covariant Serre readings `S` and `S~` times **three** sectors `u, d, e`), holding `L_coord = L + (1/2) log Im(tau) = L_tilde + gamma + log(pi)` fixed at one point five zero (minimum channel norm **twenty-nine point six zero**, strictly positive everywhere):
     - Under `S : tau -> -1/tau` with co-transformed torsion line `(a, b) -> (b mod 1, -a mod 1)`, **every** raw Yukawa singular value scales with **exact modular weight plus one** (`|tau|^1`): maximum absolute deviation `|k_measured - 1|` across all fifty-four cases is **five point one four times ten to the minus twelve** (`5.144e-12`).
     - **Every** intra-sector singular-value ratio `m_1/m_3` and `m_2/m_3` transforms with **exact modular weight zero**: maximum relative drift under `S` is **five point zero seven times ten to the minus twelve** (`5.066e-12`), and under `T : tau -> tau + 1` with `(a, b) -> (a, (b - a) mod 1)` raw singular values are invariant to **four point zero six times ten to the minus twelve** (`4.060e-12`).
     - **Mandatory unitary basis-scrambling gate:** Applying independent random Haar `SU(3)` basis transformations `Y_u -> U_Q Y_u U_{uR}^dagger`, `Y_d -> U_Q Y_d U_{dR}^dagger` simultaneously with `S : tau -> -1/tau` leaves all nine CKM moduli `|V_{ij}|` invariant to **one point zero zero times ten to the minus thirteen** (`1.003e-13`).
   - Thus minimal Kähler normalisation supplies `(Im tau)^1` on squared couplings — **exact weight one, never reaching `w >= 8`** (`P-259` / `P-720` confirmed).

3. **`HARVEST_LEDGER` Rows `945` (`W29`, `Z_6` Twist-Eater in `E_8`) and `949` (`W31`, `Z_5` Twist-Eater in `E_8`) — SAME (Both Load-Bearing Negatives Confirmed by Third Computation):**
   - Built directly from the **two hundred and forty** roots and rank-eight Cartan matrix (`det = +1`) of `E_8`:
   - **Row `945` (`W29`, Kac-mark-six `Z_6` grading `E_8 -> (SU(3) x SU(2) x SU(6)) / Z_6`):**
     - `248` grades into dimensions `(46, 36, 45, 40, 45, 36)`.
     - Embedding the irreducible qubit-tensor-qutrit clock-and-shift twist-eater into `SU(6)` leaves **zero** commutant in `su(6)`, reducing the `E_8` centraliser to **exact dimension eleven** (`su(3) (+) su(2)`), with **zero surviving `U(1)_Y` hypercharge generators** (`dim U(1)_Y = 0`).
     - Grade three `(1, 2, 20)` is strictly self-conjugate, giving **zero chiral leptons**.
     - Under `SL(2, Z)` move lifts on `SU(6)` (`6 = 2 (+) 4` and `15 = 1 (+) 2 (+) 3 (+) 3' (+) 6`), locality (`N_15 = 2 N_6 = 10`) gives **five** quark generations (`[5]`), while unrestricted move subspaces yield **minus one, plus one, plus three, or plus five** (`[-1, 1, 3, 5]`, unforced); swap has **no lift** because `[b, a] = [a, b]^(-1) != [a, b]`.
   - **Row `949` (`W31`, Kac-mark-five `Z_5` grading `E_8 -> (SU(5)_g x SU(5)_b) / Z_5`):**
     - `248` grades into `(48, 50, 50, 50, 50)` with chiral matter `(10_g, 5_b)` at `k = 1` and `(5bar_g, 10_b)` at `k = 2`.
     - Irreducible `Z_5` clock-and-shift twist-eater in `SU(5)_b` generates a finite Heisenberg group of order **one hundred and twenty-five** (`125`, Frobenius–Schur indicator **zero**), leaving `E_8` centraliser `su(5)_g` of **exact dimension twenty-four** (`24`).
     - Its `SU(5)_b` normaliser implements the Weil representation of `2I = SL(2, F_5)` of order **one hundred and twenty** (`120`, projective Clifford order **three thousand** `3,000`, linear subgroup order **fifteen thousand** `15,000`), splitting `C^5_b = 3^(+) (+) 2^(-)` under `S_5^2 = -I` and `Lambda^2(C^5_b) = 3 (+) 4 (+) 1 (+) 2'`.
     - Bounding four-dimensional spin-Dirac APS indices `(N(10_g), N(5bar_g))` at fluxes `k = 1, 2, 3, 4` are `(-1, -4)`, `(-2, +2)`, `(+2, -2)`, and `(+1, +4)` — **zero** local `SU(5)_g^3`-anomaly-free solutions (`N(10_g) != N(5bar_g)` at all four non-trivial fluxes).
     - Adding `2I`-invariant boundary subspaces: sign-compatible `5_b` projections yield `SU(5)_g^3`-free generation counts `{-1, +2}` at `k = 1, 3` and `{-2, +1}` at `k = 2, 4`; even completely unrestricted move-invariant boundary projections yield `{-1, +1, +2, +4}` at `k = 1`, `{-2, 0, +1}` at `k = 2`, `{-1, 0, +2}` at `k = 3`, and `{-4, -2, -1, +1}` at `k = 4` — **never reaching plus or minus three (`+-3`) anywhere** (at `k = 1, 4` because `5_b = 3 (+) 2` has neither a one-dimensional nor a four-dimensional `2I`-subspace; at `k = 2, 3` because `N(5bar_g)` is capped between minus two and plus two).

---

## Five Adversarial Planted Controls (`CTL-NEG-1` through `CTL-NEG-5`)

All **five** planted cheats were executed and caught automatically (`all_planted_controls_caught = True`):
1. **`CTL-NEG-1` (Unpriced single-level `delta = 0.15` cheat on `B1839`):** Omitting the twenty-three-level look-elsewhere scan drops `r_975` to **zero point one nine eight percent** (`0.001982`, falsely below one percent), whereas the true twenty-three-level scan fails at **one point five four one percent** (`7.77x` inflation). Caught.
2. **`CTL-NEG-2` (Holding bare `L` fixed instead of `L_coord = L + (1/2) log Im(tau)` under `S`):** Induces an `S`-transformation ratio drift of **one point seven nine times ten to the minus three** (`1.785e-3`, nine orders of magnitude above machine precision), destroying weight-zero invariance. Caught.
3. **`CTL-NEG-3` (Non-covariant `S*` reading and ordinary non-Serre derivative omitting `E_2`):** Produces a **fifty-three point two percent** (`0.532`) ratio drift on `S*` and a **seventy-two point four percent** (`0.724`) norm-scaling error on the ordinary derivative vs machine-zero (`6.66e-16`) on the true Serre derivative. Caught.
4. **`CTL-NEG-4` (Abelian commuting `Z_6` and `Z_5` subgroups instead of non-commuting twist-eaters):** Leaves extra Cartan `u(1)` centralisers of dimension **sixteen** (`> 11`) in `W29` and **twenty-eight** (`> 24`) in `W31`. Caught.
5. **`CTL-NEG-5` (Counting `10_g` alone `1 + 2 = 3` at `k = 4` ignoring `5bar_g`, or projecting onto a non-`2I`-invariant `1D` vector):** Caught by both non-zero `SU(5)^3` chiral anomaly (`N(10_g) - N(5bar_g) != 0`) and `2I` invariance violation norm **greater than zero point eight** (`0.894 > 0.5`).

---

## What the Three Walls Teach Together

1. **Discreteness of the End Cannot Be Faked by Grid Scanning (`B1839` -> `B1841`):** `B1839`'s failure and `B1841`'s survival under the identical one-million-draw look-elsewhere null prove that the continuous end freedom `L_tilde` cannot be absorbed by scanning twenty-two empirical grid levels: every unpriced grid step inflates the five-dimensional acceptance tube across the prior until the global one percent gate breaks (`3.00x` inflation). Only zero-parameter geometric or renormalization-group prescriptions survive look-elsewhere accounting.
2. **Modular Weight One Is Exact and Permanent (`P-720`):** `B1919`'s Kronecker channel norm and `B1921`'s invariant coordinate end `L_tilde` have **exact modular weight zero**, leaving `B1656`'s Yukawa operator with **exact modular weight one** on raw singular values and **exact modular weight zero** on all mass ratios and CKM moduli. Two immediate consequences follow: first, polynomial modular-form stabilization mechanisms requiring high modular weight (`w >= 8`) are permanently closed on this frame; second, **because every mass ratio and CKM modulus has exact weight zero at fixed `L_tilde`, thread and area averages on modular curves `X(Gamma)` are mathematically well-defined without Kähler gauge ambiguity** — opening the exact gate that `P-845` (`B1924`) walks through.
3. **Internal Twist-Eaters Alone Cannot Simultaneously Preserve Hypercharge and Produce Three Generations (`W29`, `W31`):** In `E_8`, eating a `Z_6` twist inside `SU(6)` (`W29`) consumes `U(1)_Y` itself and leaves grade three real (`zero` chiral leptons), whereas eating a `Z_5` twist inside `SU(5)_b` (`W31`) preserves `SU(5)_g` (and hence Standard Model `U(1)_Y` after hypercharge flux) but locks the move normaliser into the Weil representation `3 (+) 2` of `2I = SL(2, F_5)`, whose rigid subspace dimensions forbid `N(10_g) = N(5bar_g) = +-3` on every flux sector. Thus **three chiral generations (`W:INDEX3`) cannot arise from finite algebraic twist-eating in `E_8` alone; the chiral three must come from the topological/hyperbolic weave index itself, while `E_8` supplies the rigid gauge-and-charge skeleton.**

0 of 19.
