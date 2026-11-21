# Card AGY-C12: Joint `s = 2` Selberg weave crossover across cover degrees, `t = 4` Majorana see-saw twist, and hyperbolic radial cusp profiling

*Seat: `agy` (`agy/cusp-action-2026-11-20`, after `origin/main` `279459977` / `B1970`). Date: `2026-11-21`. Pre-registered before any script or run (`expectations committed first`). Data-free: `0 of 19`.*

---

## One. Package and question

Cards `AGY-C8` to `AGY-C11` isolated a sharp single-modulus tension on `P_5` alone: collar `m` in `{8, 16}` gives normal `CKM` (`|V_12| > |V_23| > |V_13|`) and `O(1)` `3`-angle `PMNS`, whereas `m = 40` (`16 + 8 i`) gives `5`–`7` decade hierarchies and `Delta_{P_d} = +1` Strong-CP. Does combining the `s = 2` Selberg weave (`t = 3` + `t = 4`), `t = 4`'s `U_R U_R^T != I_3` Majorana twist, `H^3` radial cusp profiling, or Fricke-paired vacua reconcile both regimes without new parameters?

## Two. Deliverables and what done means

- `65`-digit evaluation of the **joint `s = 2` Selberg-weighted weave (`t = 3` weight `w_3` + `t = 4` weight `w_4`)** across `m` in `{8, 12, 16, 20, 24, 40}` for all four sectors `(u, d, e, nu)`, tracking intra-family mass ratios, `Y_e != Y_d^T` splitting, `CKM` ordering, and **`t = 4`'s non-orthogonal right-handed Majorana twist `U_R(w) U_R(w)^T != I_3` inside `m_nu(w) propto Y_nu(w) Y_nu(w)^T`**.
- Exact audit of **(a) `H^3` Breitenlohner–Freedman radial horocycle averaging** `integral_{y_col}^{y_deep} (dy / y^3) y^{2 Delta} ...` across `[8 / 5, 8]` vs single-slice evaluation, and **(b) Fricke / `CP`-conjugate orbit pairing** `Delta_{P_d}(m tau_*^+) * Delta_{P_d}(m tau_*^-)` across all `m` in `{8, 12, 16, 40}`.
- Zero-shared-code independent countercheck (`recomputed independently` + `tested against planted errors`, `5 / 5` plants) and mask-clean result relay.

## Three. Pre-committed expectations and how it could come out wrong

- **E1 (`t = 4` Dirac-transparency vs Majorana see-saw twist & joint `s = 2` weave):** Although `G_nu(w) = G_e(w)` (`Dirac`) holds to `< ten to the minus sixty` across all `35` `t = 4` points (`AGY-C11`), `q_{R, nu} = 0` vs `q_{R, e} = +6` induces `U_R(w)` in `U(3) \ O(3)` on odd-`6 a` points of `P_6` with `U_R(w) U_R(w)^T != I_3`, **twisting `Y_nu(w) Y_nu(w)^T` away from `Y_e(w) Y_e(w)^T`**! Adding `t = 4` at `s = 2` Selberg weight splits `e` from `d` at every `m` while preserving normal `CKM` for `m <= 16` and testing whether non-commuting log-Gramians shift the `|V_12| = |V_23|` crossover.
- **E2 (`H^3` radial cusp integral convexity vs sector localization):** Under uniform `H^3` measure `(dy / y^3)` on `[8 / 5, 8]`, linear radial integration is collar-dominated (`keeping normal CKM and O(1) PMNS but shallower mass ratios`), whereas log-Yukawa radial averaging `exp(integral mu(y) ln Y dy)` acts at a single effective height `y_eff` (`proving an exact convexity no-go unless radial localization y_f or sheet multiplicity m_T = 8 vs m_5 = 40 differs by sector!`).
- **E3 (Exact Fricke-pair Strong-CP product `+1` at every `m`):** Pairing `m tau_*^+` and `m tau_*^- = minus conj(m tau_*^+)` yields `|Delta_{P_d}(m tau_*^+) * Delta_{P_d}(m tau_*^-) minus 1| < ten to the minus forty-five` at **every** `m` (`including collar m = 8, 12, 16`), while parity-symmetric averaging kills CKM `J_CP` (`requiring spontaneous selection of one vacuum for J_CP != 0`).

## Four. Premises and firewall boundaries

- Rests on `B1970` and `AGY-C7` through `AGY-C11`; Guardrails one through six enforced (`Haar U(3) x O(3) invariance < ten to the minus twelve`).
- Must **never** read, compute, or compare any of the nineteen empirical Standard Model targets (`0 of 19`), and must leave `origin/agy/audit-2026-11-02` untouched at `4319f47e2`.

## Five. Mandatory planted negative control

1. **Fake `O(3)` assumption on `t = 4` Majorana see-saw:** Replace `Y_nu(w) Y_nu(w)^T` on `P_6` by `Y_e(w) Y_e(w)^T`: must fail on odd-`6 a` points of `P_6` where `||U_R(w) U_R(w)^T minus I_3|| > 1`!
2. **Broken Fricke pairing & unnormalized radial weight plants:** Perturb `tau_*^-` from `(minus 2 + i) / 5` to `(minus 1 + i) / 5` at `m = 8` (`breaking Delta^+ * Delta^- == 1`), and flip `s = 2` to `s = 1 / 2` (`inverting w_3 / w_4 < 1`).

## Six. What is needed from main or other seats

Nothing needed to run; opens the four-card Phase III blind closure sequence (`AGY-C12` to `AGY-C15`) on `agy/cusp-action-2026-11-20`.

0 of 19.
