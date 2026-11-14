# Card `A2-NEG`: Independent Second Computations of Load-Bearing Negatives (`M21` / `M24` Item One)

- **Seat:** `agy-002` (`origin/agy-002/verify`)
- **Card ID:** `A2-NEG` (assigned in `M21` and placed first in `M24`'s ordered queue on `docs/seats/agy-002.md`)
- **Commit of `main` at card creation:** `660daba8d` (`M25` read)
- **Files of `main` read for `A2-NEG` prior to this card commit:** **ONLY** prose specification and statement files (`docs/seats/agy-002.md`, `docs/POINT_REGISTER.md` rows `P-720` and `P-842`–`P-844`, `docs/HARVEST_LEDGER.md` rows `945` and `949`, and the sealed `PREREGISTRATION.md` / `FINDINGS.md` prose statements of `B1839`, `B1841`, `B1656`, `B1691`, `B1724`, `B1919`, `B1921`, `B1923`). **Zero** Python scripts (`.py`) of `B1839`, `B1841`, `P-720`, `B1656`, `B1724`, `B1919`, `B1921`, `W29`, or `W31` have been opened (`expectations committed first`, `docs/seats/README.md` § 7 and § 12).
- **Firewall (`docs/seats/README.md` § 9 item one and `M21`):** `0 of 19`. Every value is committed before any comparison with measured data, and **zero** values are set beside any measured number in this card or its scripts (`HZ2021` and `data.json` are never opened).

---

## 1. Scope and Question, in One Sentence

Across the three load-bearing negative clusters assigned in `M21` — (`1`) the matched look-elsewhere null and level counts of `B1839` cell D (`twenty-three` levels) and `B1841` cell D (`four` principled levels) over `one million` synthetic hierarchies at a `one percent` gate, (`2`) `P-720`'s modular weight of `B1656`'s normed four-channel frame with `B1921`'s invariant end coordinate across `three` points of the upper half-plane and `three` flat hypercharge lines, and (`3`) `HARVEST_LEDGER` rows `945` and `949` (`W29` and `W31`: the order-six and order-five twist-eater fluxes in `E_8`, their centralisers, and their chiral anomaly counts) — do independent zero-shared-code derivations on another family of model confirm or overturn each negative, and what does each wall teach?

---

## 2. Deliverables and Definition of Done

Done means committing inside `relays/` on `origin/agy-002/verify` in strict three-commit order:

1. **Commit 1 (this card + `relays/STATUS_AGY-002.md`):** Committed and pushed **before** running any computation or opening any data-free norm array, locking explicit mathematical expectations, failure conditions, and planted-error controls.
2. **Commit 2 (`relays/a2_neg/verify_a2_neg.py`, `relays/a2_neg/verify_a2_neg_out.txt`, `relays/a2_neg/verify_a2_neg_results.json`):** Standalone zero-import Python verification suite and raw run output covering all three sub-tasks plus adversarial planted-fault controls (`CTL-NEG-*`) that provably fail.
3. **Commit 3 (`relays/AGY002_TO_CC_2026-11-14_M21_LOAD_BEARING_NEGATIVES.md` + `relays/STATUS_AGY-002.md`):** Mask-resilient plain-word report stating every integer, sign, inequality, and outcome in words, carrying `"What the wall teaches"` on each negative (`WORKING_RULES.md`, `P-842`), and advancing `STATUS_AGY-002.md` to the second queue item (`B1924`).

---

## 3. Pre-Registered Analytical Expectations and Failure Criteria

### Sub-task 1: `B1839` Cell D (`twenty-three` levels) and `B1841` Cell D (`four` principled entries)

- **Purely data-free formulation (strictly enforcing `M21`'s firewall):**
  - Verify the exact row and level geometry directly on the data-free norm tables (`B1839`: `two hundred twenty-three` reduced apexes times `two hundred sixty-six` lines times `twenty-three` ends — `twenty-two` finite horoball offsets `delta` plus `one` scale-free cusp limit `delta = infinity` — equals `one million three hundred sixty-four thousand three hundred fourteen` rows, all finite; `B1841`: `two hundred twenty-three` apexes times `two hundred sixty-six` lines times `four` principled entries `E1 = L_2`, `E2 = ln 2`, `E3 = L_max`, `E4 = L_2 - pi/2`, all strictly embedded above `L_max`, equals `two hundred thirty-seven thousand two hundred seventy-two` rows, all finite).
  - Build a zero-shared-code four-channel Yukawa engine (`Y_{pq}(a; u) = a_p u_q + u_p a_q - (a . u) delta_{pq} +/- u_1 eps_{pqr} a_r` with sign pinned by `B1653` U4's shared left-null-state theorem, weight-three-halves Serre section `a = dR`, covariant readings `S` and `S~`, and Higgs-twist class indexing) and cross-check our independently computed six-ratio log-features against rows built from the data-free `norms.npz` tables.
  - Generate `one million` synthetic six-ratio hierarchies on our own PRNG from `B1695`'s sealed prior (`log_10(m_2/m_3)` in `[-3, -1]`, `log_10(m_1/m_3)` in `[-6, -2.5]` with `m_1 < m_2` per sector; checking both uniform-on-trapezoid rejection sampling and conditional sampling, and data-free uniform ten-percent log-allowance `sigma = 0.10`), re-minimising `chi^2_six` for every synthetic target over all `(apex, line, reading_triple_in_SEAT, level, c)` under (`i`) continuous `c` in `[1/3, 5]` (exact closed-form constrained quadratic optimum per row), (`ii`) the nine-point `c` grid `{1/3, 1/2, 2/3, 1, 3/2, 2, 3, 4, 5}`, and (`iii`) discrete `c` in `{1, 3}`.
  - Evaluate the purely data-free null survival curve `F_null(theta)` and exact one-sided ninety-seven-point-five percent Clopper–Pearson upper bound `r_97.5(theta)` across a grid of abstract scalar thresholds `theta`, including the abstract numbers `4.613885` (`B1839`'s reported minimum) and `4.726887` (`B1841`'s reported minimum), **never opening or loading any measured SM mass file**.
- **Expected outcomes:**
  - `B1839` cell D **fails** the `one percent` (`0.01`) gate decisively in all three `c` modes (`r_97.5` near `two point four six percent`, well above `one percent`, with hits spread across finite `delta` levels and zero hits at the cusp limit).
  - `B1841` cell D **passes narrowly** under continuous `c` (`r_97.5` near `zero point eight eight five percent`, below `one percent` by roughly `one tenth of a percentage point`) and under the nine-point `c` grid, while **failing** (`r_97.5` slightly above `one percent`) under discrete `c` in `{1, 3}` at its own abstract threshold `11.977974`.
- **How this could fail / overturn the record:** If an independent null implementation on `one million` hierarchies gives `r_97.5 < 0.01` on `B1839` at `theta = 4.613885`, or gives `r_97.5 >= 0.01` on `B1841` continuous-`c` at `theta = 4.726887` under the exact sealed definition.

### Sub-task 2: `P-720` Modular Weight of `B1656`'s Normed Frame with `B1921`'s Invariant End

- **Analytical derivation before computing:**
  - The theta triplet `R(tau) = (-theta_2^2, -theta_4^2, i theta_3^2)/(2 pi eta^3)` transforms with modular weight `minus one half`, so its Serre derivative `a(tau) = d_{-1/2} R(tau)` transforms with modular weight `plus three halves` (`|tau|^{3/2}` under `S: tau -> -1/tau` up to unitary rotation `rho(S)`).
  - Each twisted channel residue `R_s = kappa c_s theta_s(u_bar) theta_s(delta) / theta_1'(0)` (in the flat holonomy / elliptic-factor-cancelled convention of `B1653` U0–U1) transforms with modular weight `minus one half` (`1/2 + 1/2 - 3/2 = -1/2`).
  - Under `B1919` and `B1921`, `2 pi L + c_s = 2 pi L_tilde + F_u(tau)` where `L_tilde = L + (1/2) log Im tau - (gamma + log pi)` is `SL(2, Z)`-invariant and `F_u(tau)` (the Kronecker constant term of the weight-zero real-analytic shifted Eisenstein series at `s = 1`, `u = c - (1/2, 1/2)`) has modular weight **zero** (`F_{u'}(-1/tau) = F_u(tau)` with `c' = (b, -a)`).
  - Therefore `u_s = sqrt(2 pi L_tilde + F_u) R_s` has modular weight `minus one half`, and the bilinear Yukawa matrix `Y(a; u)` has **exact modular weight one** (`k = 3/2 - 1/2 = 1`): for every singular value `sigma_m`, sector, and covariant reading (`S` or `S~`),
    `sigma_m(Y(-1/tau, v S^{-1}, L_tilde)) / sigma_m(Y(tau, v, L_tilde)) = |tau|^1`,
    while every singular-value ratio `sigma_m / sigma_3` has **exact modular weight zero** (`k_ratio = 0`).
  - Minimal Kähler normalisation (`P-259`) therefore supplies `(2 Im tau)^{1/2}` on `Y` (weight `one` in `Im tau` on squared couplings), far short of `w >= 8`.
- **Expected outcome:** Numerical agreement with `k = 1` on all raw singular values and `k_ratio = 0` on all singular-value ratios to `< 10^{-10}` across `three` generic `tau` points, `three` flat lines of distinct orders, all `three` sectors, and both covariant readings `S` and `S~`.
- **How this could fail:** If any channel norm shift, elliptic multiplier phase, or zero-mode normalization introduces a non-zero modular weight shift away from `k = 1` (or non-zero ratio weight).

### Sub-task 3: `HARVEST_LEDGER` Rows `945` (`W29`, `Z_6`) and `949` (`W31`, `Z_5`) Twist-Eater Fluxes in `E_8`

- **Analytical expectations before computing:**
  - **`W29` (`Z_6` twist-eater in `E_8`):** Deleting the unique Kac-mark-six node `alpha_4` of the extended `E_8^{(1)}` diagram yields `(SU(3) x SU(2) x SU(6)) / Z_6 < E_8`, decomposing `248 = (8,1,1) + (1,3,1) + (1,1,35) + (3,2,6) + (3_bar,2,6_bar) + (3_bar,1,15) + (3,1,15_bar) + (1,2,20)`. Embedding the irreducible qubit-tensor-qutrit clock-and-shift pair `(P_6, Q_6)` into `SU(6)` breaks `SU(6)` completely (trivial centraliser in `su(6)` by Schur's lemma), leaving centraliser in `e_8` of dimension **exact eleven** (`su(3) + su(2)`, **no `u(1)_Y`** — exact lemma: the `Z_6` twist-eater kills hypercharge!), with **zero** chiral lepton doublets because `(1, 2, 20)` at `Z_6`-charge three is self-conjugate, and `SU(3)^3`-free quark generation counts taking multiple values (`-1, 1, 3, 5`) rather than forcing `three`.
  - **`W31` (`Z_5` twist-eater in `E_8`):** Deleting the Kac-mark-five node `alpha_5` of `E_8^{(1)}` yields `(SU(5)_g x SU(5)_b) / Z_5 < E_8`, decomposing `248 = (24,1) + (1,24) + (5,10) + (5_bar,10_bar) + (10,5_bar) + (10_bar,5)`. Embedding the irreducible `Z_5` clock-and-shift pair `(P_5, Q_5)` into `SU(5)_b` leaves centraliser **exact `su(5)_g`** of dimension **twenty-four** (and with the compensating `Z_5` hypercharge flux `e^{2 pi i Y}` in `SU(5)_g`, centraliser `su(3) + su(2) + u(1)_Y` of dimension **twelve**, keeping the full Standard Model gauge algebra!). The normaliser in `SU(5)_b` with `+-I` is the `Z_5` Clifford group of order **three thousand** (`25` Heisenberg translations times `120 = |SL(2, F_5)|` modulo scalar phases, checked explicitly), acting on `C^5_b` via the Weil representation `3 + 2` of `2I = SL(2, F_5)` and on `Lambda^2(C^5_b)` as `3 + 1 + 2' + 4`; swap conjugates the central character / flux; and **zero** flux-and-move or locality combinations give `three` `SU(5)_g^3`-anomaly-free generations (`N(10_g) = N(5_bar_g) = 3` never occurs; anomaly-free net generation counts sit in `{-1, 2}` or `{-2, 1}`, and `zero` under locality).

---

## 4. Planted-Error Controls Required to Fail

1. **`CTL-NEG-1` (Unpriced level-scan cheat on `B1839`):** Fixing `delta = 0.15` in the null while letting the target pick `delta` across `twenty-three` levels artificially suppresses the null rate below `one percent`; our look-elsewhere consistency check must flag and fail it.
2. **`CTL-NEG-2` (Raw-`L` unshifted end under `S` on `P-720`):** Passing `L` unchanged instead of `L + log|tau|` (i.e. breaking `L_tilde` invariance) under `tau -> -1/tau` destroys weight-one scaling (`error > 10^{-2}`); our modular-weight check must catch and fail it.
3. **`CTL-NEG-3` (Non-covariant `S*` reading under `S` on `P-720`):** Evaluating `S*` under `tau -> -1/tau` breaks weight-one covariance by `O(1)`; our check must catch and fail it.
4. **`CTL-NEG-4` (Abelian commuting `Z_6` / `Z_5` subgroup in `E_8`):** Replacing the non-commuting clock-and-shift pair with a commuting diagonal subgroup leaves extra `u(1)` Cartan centraliser generators (`dim > 11` in `W29`, `dim > 24` in `W31`); our centraliser rank/dimension assertion must fail it.
5. **`CTL-NEG-5` (One-sector `10_g`-only count ignoring `SU(5)^3` anomaly cancellation in `W31`):** Counting `dim = 3` from `3 < 5_bar_b` while ignoring the mismatched `5_bar_g` multiplicity violates `A(10) + A(5_bar) = 0`; our anomaly detector must fail it.

0 of 19.
