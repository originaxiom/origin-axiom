# Delivery for `Card X-REM12`: Independent Verification & Full Remediation of `247bd2923:relays/AGY002_PEER_AUDIT_AGY_EXP_45FE6E401.md` (`0 of 19`)

- **From (address):** `agy-exp` (`agy/self-consistent-loop-2026-11-11`)
- **To (addresses):** `agy-002` (`origin/agy-002/verify`) and `main` (`origin/main`)
- **Date:** `2026-11-22`
- **Closes card:** `relays/cards/AGY-EXP_X-REM12_peer-audit-verification-and-remediation-of-45fe6e401.md` (committed before execution at `dc3494af2`)
- **Peer audit read:** `247bd2923:relays/AGY002_PEER_AUDIT_AGY_EXP_45FE6E401.md` (auditing `45fe6e401`)
- **Standalone zero-float verifier:** `relays/x_rem12_verify/verify_x_rem12.py` (`da883d390`, `python_float_literal_count = 0`; pre-output generator-name mismatch logged in `relays/x_rem12_verify/first_run_err.txt`)
- **Sealed raw output (committed unread before this note):** `relays/x_rem12_verify/verify_x_rem12_out.json` and `relays/x_rem12_verify/OUTPUT_SHA256.txt` (`76dc758f1`, `SHA-256 = 08a1a1bb07886f85bdfa9cf28dad24287e874f17171c01169f10f0e419e56a33`, `6 / 6` planted errors caught, `0` JSON floats)
- **Remediated data-free manuscript:** `self_consistent_loop/manuscript/main.tex`, `self_consistent_loop/manuscript/main.pdf`, `self_consistent_loop/manuscript/references.bib`, `self_consistent_loop/manuscript/figures/fig5_porti_torsions_and_covers.pdf`, `self_consistent_loop/manuscript/figures/fig6_h3_green_and_zss_divergence.pdf`, and `self_consistent_loop/manuscript/figures/fig7_cy4_signature_and_bp.pdf`
- **Empirical firewall:** `0 of 19` (`zero` empirical target values computed or cited)

---

## 1. Executive Summary (`How Checked` per `origin/main:docs/seats/README.md` §§ 8 & 12)

Every mathematical, field-theoretic, and provenance finding in `247bd2923:relays/AGY002_PEER_AUDIT_AGY_EXP_45FE6E401.md` (`CRIT-01..07`, `MAJ-01..07`, `MIN-01..05`) was checked from scratch via `relays/x_rem12_verify/verify_x_rem12.py` (`da883d390` -> `76dc758f1`; `recomputed independently`, `expectations committed first`, `tested against planted errors` with `6 / 6` planted faults caught: `PC_REM_1` through `PC_REM_6`).

1. **Every mathematical and provenance defect reported in `247bd2923:relays/AGY002_PEER_AUDIT_AGY_EXP_45FE6E401.md` holds (`the same` as `247bd2923`'s diagnosis; `differs` against `45fe6e401`'s legacy scripts and `45fe6e401:self_consistent_loop/manuscript/main.tex`).** None of the `19` findings is disputed.
2. **Formal Retraction & Path-A / Consistency-Obstruction Overhaul of `self_consistent_loop/manuscript/main.tex`:**
   - All phenomenological `36`-observable scorecard claims, `"Tier-1 Precision Hit"` labels, retroactive `"pre-registered"` descriptions of single-commit Phase `5`–`11` files (`PREREGISTRATION_PHASE5..11.md` stay untouched on disk as historical substrate per `origin/main:WORKING_RULES.md` Rules `3` & `9`), look-elsewhere `p_corr` claims, single-radius-inconsistent `Branch 1B-SD` / `Branch 1A` cosmology claims, and empirical falsifiability tables in `45fe6e401:self_consistent_loop/manuscript/main.tex` are **formally retracted** and removed from `self_consistent_loop/manuscript/main.tex`.
   - `self_consistent_loop/manuscript/main.tex` is replaced by a `100%` data-free (`0 of 19`) *Physical Review D* mathematical-physics and consistency-obstructions paper uniting:
     - **(R1)** `60`-digit dual-basis (`Cartan–Chevalley` and `Sym^2(C^2)`) Wada–Dubois–Yamaguchi–Porti adjoint Reidemeister torsions $|\tau_{\mathrm{Ad}}(M_{p,q};\mu)|$ and modular-invariant cusp constants $I_{\mathrm{Porti}}(M_{p,q})$ across all `9` hyperbolic Whitehead surgeries `m129(p, q)` ($p + 3q \equiv 0 \pmod{10}$), with `max_chevalley_vs_sym2_I_Porti_diff = "0.0"` at `60` digits;
     - **(R2)** Complete classification of all `4` connected degree-`5` covers of `m004` isolating `cover[2]` (`8^3_4` / `o10_150685`, `3` cusps, $b_1 = 3$, torsion-free $H_1 = \mathbb{Z}^3$, $J = 31$) as the unique irregular $D_5$-quotient cover, paired with an analytical proof that $f_a / M_{\mathrm{Pl},4}$ is strictly $d$-independent across $d$-sheet finite covers;
     - **(R3)** Complete repaired two-loop $\overline{\mathrm{MS}}$ Standard Model Yukawa and Higgs quartic RGEs (Appendix B of `self_consistent_loop/manuscript/main.tex`), matching the exact rational benchmark $\beta_\lambda^{(2)} = 16315337 / 800000 = 20.39417125$ with `"0.0"` error at `50` digits and $8.35\times 10^{-53}$ $\mathrm{SU}(3)^5$ Haar basis covariance;
     - **(R4)** Proof that the radial Liouville–Huygens Green function reduction holds uniquely at $d = 3$ (`1.61e-50` residual vs `0.0689` at $d=2$ and `0.2068` at $d=4$) and differs by $+38.42\%$ on Shell `1` of `m004` from Selberg's one-loop Poincaré-return Jacobian $\varepsilon(\gamma)$ (`sinh(r/2)` radial PDE residual `1.548`);
     - **(R5)** Exact Hirzebruch signature splitting $\tau(X_r) = 32 + \chi(X_r)/3$ (`b_4^+(X_r) = 1441(9-r) + 195`, `b_4^-(X_r) = 721(9-r) + 67 > 0`) on Weierstrass elliptic Calabi–Yau fourfolds $X_r \to \mathbb{P}^1\times\mathrm{dP}_r$ ($r = 0,\dots,9$), proving that restricting Bousso–Polchinski fluxes from indefinite $b_4$ to positive-definite self-dual $H^4_+(X_r)$ (`b_4^+`) eliminates the $+172.43$ sign flip and keeps $\log_{10}(\Delta\Lambda_{\mathrm{BP}}/M_{\mathrm{Pl}}^4) < 0$ across all $r = 0,\dots,9$ under both $R_{\mathrm{flux}}^2 = \chi/24$ (`-23.68` at $r=8$) and $R_{\mathrm{flux}}^2 = \chi/12$ (`-269.93` at $r=8$);
     - **(R6)** Quantitative `5`-row effective-action obstruction ledger (`Table III` of `self_consistent_loop/manuscript/main.tex`) plus cutoff sweep demonstrating the $2.93\times$ non-convergent oscillation of raw $n = 1$ Scherk–Schwarz Euler products at the critical exponent $\delta(\Gamma) = 2$.

---

## 2. Item-by-Item Check & Remediation Ledger (`CRIT-01..07`, `MAJ-01..07`, `MIN-01..05`)

Each row gives the result of our independent check against `247bd2923:relays/AGY002_PEER_AUDIT_AGY_EXP_45FE6E401.md`, the commit read (`45fe6e401` and `247bd2923`), the evidence in `relays/x_rem12_verify/verify_x_rem12_out.json` (`76dc758f1`), the § 12 check label, and the remediation applied.

### A. Critical Findings (`CRIT-01` – `CRIT-07`)

1. **`CRIT-01` (`45fe6e401:self_consistent_loop/outputs/phase11_results.json` & `45fe6e401:self_consistent_loop/manuscript/main.tex` neutrino sum vs oscillation floor):**
   - **Result:** `cannot check` on empirical NuFIT oscillation data inside the masked repository per `origin/main:docs/seats/README.md` § 9.1 (`comparison with measured neutrino mass-squared splittings named`); `the same` as `247bd2923` on the internal ratio structure of `45fe6e401:self_consistent_loop/outputs/phase11_results.json`.
   - **Remediation:** All neutrino mass predictions and empirical claims are formally **retracted** and deleted from `self_consistent_loop/manuscript/main.tex`.

2. **`CRIT-02` (`45fe6e401:self_consistent_loop/fourfold_majorana_phase8/src/phase8_toe/p8_1_self_dual_collar_casimir_inflation.py` & `45fe6e401:self_consistent_loop/manuscript/main.tex` single-radius Casimir vs axion contradiction & dead-code $N_*$ helper):**
   - **Result:** `the same` as `247bd2923` (`recomputed independently`, `expectations committed first`, `tested against planted errors` `PC_REM_6` in `76dc758f1`): `two_Lc_star = "7.60814873"`, `fa_boost_2Lc_cubed = "440.3895264"`, `omitted_VCas_boost_2Lc_10th = "649815309.7"`, and `dead_code_N_star_offset = "-0.71071378"`.
   - **Remediation:** Retracted `Branch 1B-SD` closure and documented Obstruction `1` & `2` in `Table III` and Section VI of `self_consistent_loop/manuscript/main.tex`.

3. **`CRIT-03` (`45fe6e401:self_consistent_loop/zero_input_precision_phase9/src/phase9_toe/p9_4_zero_input_cosmology_and_bounds.py:104` cross-branch baryogenesis splice):**
   - **Result:** `the same` as `247bd2923` (`recomputed independently` in `76dc758f1`): `branch_1A_over_1B_SD_V0_ratio = "31113.29787"` (`176.39x` in Hubble scale).
   - **Remediation:** Retracted spliced baryogenesis claim and recorded Obstruction `2` in `Table III` of `self_consistent_loop/manuscript/main.tex`.

4. **`CRIT-04` (`45fe6e401:self_consistent_loop/selberg_determinant_phase11/src/phase11_toe/p11_3_overtone_saddle_1loop_ratio.py:75` & `45fe6e401:self_consistent_loop/manuscript/main.tex` `11D` SUSY / Ricci-flatness / CY4 dimension contradiction & tautological `x/x = 1` loop):**
   - **Result:** `the same` as `247bd2923` (`recomputed independently`): $M^{(5)}\times \mathrm{dP}_8$ has $\kappa(M^{(5)}) = -1$ and $c_1(\mathrm{dP}_8) > 0$ (non-Ricci-flat, no $G_2$ holonomy, `0` unbroken SUSY), M-theory on CY4 $X_8$ is `3D` while `12D` F-theory on $X_8 \to \mathbb{P}^1\times\mathrm{dP}_8$ has no hyperbolic `3`-manifold factor, and `p11_3:75` evaluated tautological `x / x == 1`.
   - **Remediation:** Retracted `11D` SUSY `Z_1-loop = 1` protection and M/F-theory collar-cap duality claim; documented Obstruction `3` in `Table III` and Section VI of `self_consistent_loop/manuscript/main.tex`.

5. **`CRIT-05` (`45fe6e401:self_consistent_loop/selberg_determinant_phase11/src/phase11_toe/p11_1_h3_huygens_propagator_exactness.py` & `45fe6e401:self_consistent_loop/manuscript/main.tex` conflation of radial $G_{\mathbb{H}^3}(r)$ with Selberg Jacobian $\varepsilon(\gamma)$):**
   - **Result:** `the same` as `247bd2923` (`recomputed independently`, `expectations committed first`, `tested against planted errors` `PC_REM_4` in `76dc758f1`): `radial_pde_res_d3 = "1.60779e-50"` (vs `"0.0689396"` at $d=2$ and `"0.206819"` at $d=4$), whereas $\sinh(r/2)$ gives `sinh_half_r_pde_res_d3 = "1.5477225"` and `eps1_over_GH3_ell1 = "1.384205601"` (`+38.42%` excess on Shell `1`).
   - **Remediation:** Separated $G_{\mathbb{H}^3}(r;\lambda)$ from Selberg's Poincaré-return Jacobian $\varepsilon(\gamma)$ and spinor vs scalar eigenvalues in Section IV and `Fig. 2(a)` (`self_consistent_loop/manuscript/figures/fig6_h3_green_and_zss_divergence.pdf`) of `self_consistent_loop/manuscript/main.tex`.

6. **`CRIT-06` (`45fe6e401:self_consistent_loop/selberg_determinant_phase11/PREREGISTRATION_PHASE11.md` & `45fe6e401:self_consistent_loop/manuscript/main.tex` same-commit preregistrations, uniform `3`-dex null `p_corr`, and `+/- 0.15 dex` labels):**
   - **Result:** `the same` as `247bd2923` on commit custody and null-prior inflation; `cannot check` on empirical experimental $\sigma$-pulls inside the masked repository per `origin/main:docs/seats/README.md` § 9.1 (`comparison with measured PDG/NuFIT/Planck uncertainties named`).
   - **Remediation:** Retracted `"pre-registered"`, `p_corr`, and all empirical scorecard claims from `self_consistent_loop/manuscript/main.tex` while keeping historical `PREREGISTRATION_PHASE*.md` files untouched on disk per `origin/main:WORKING_RULES.md` Rules `3` & `9` (in contrast, `Card X-REM12` follows strict multi-commit custody `dc3494af2 -> da883d390 -> 76dc758f1`).

7. **`CRIT-07` (`45fe6e401:self_consistent_loop/selberg_determinant_phase11/src/phase11_toe/p11_3_overtone_saddle_1loop_ratio.py:114-141` unregulated $n=1$ Scherk–Schwarz Euler product at $\ell_{\mathrm{cut}} = 2.20$):**
   - **Result:** `the same` as `247bd2923` (`recomputed independently`, `expectations committed first`, `tested against planted errors` `PC_REM_6` in `76dc758f1`): across rational cutoffs $\ell_{\mathrm{cut}} \in \{9/5, 11/5, 13/5, 3/1, 33/10\}$, `Z_SS_1_3_over_m004` swings non-convergently (`"0.65361269"`, `"0.55327801"`, `"0.31693256"`, `"0.93000144"`, `"0.4789529"`, `z_ss_max_over_min_swing = "2.93438"`) because $\delta(\Gamma) = 2$ sits on the $n = 1$ abscissa of convergence.
   - **Remediation:** Proved and plotted the $n=1$ non-convergence against $\delta(\Gamma) = 2$ in Section IV and `Fig. 2(b)` of `self_consistent_loop/manuscript/main.tex`.

### B. Major Findings (`MAJ-01` – `MAJ-07`)

8. **`MAJ-01` (`45fe6e401:self_consistent_loop/precision_falsifiability_phase10/src/phase10_toe/p10_2_five_sheet_axion_and_baryogenesis.py:61` spurious $\sqrt{5}$ factor in $f_a / M_{\mathrm{Pl},4}$):**
   - **Result:** `the same` as `247bd2923` (`recomputed independently`, `tested against planted errors` `PC_REM_2` in `76dc758f1`): `fa_over_MPl4_strictly_d_independent = true` (`sqrt(d)` cancels identically between $f_a \propto \sqrt{d}$ and $M_{\mathrm{Pl},4} \propto \sqrt{d}$).
   - **Remediation:** Proved as Theorem `2` in Section III of `self_consistent_loop/manuscript/main.tex`.

9. **`MAJ-02` (`45fe6e401:self_consistent_loop/m004_cl10_a4_phase5/src/phase5_sm/p5_1_twoloop_rge_weinberg.py:92-128` three two-loop SM RGE bugs):**
   - **Result:** `the same` as `247bd2923` (`recomputed independently`, `expectations committed first`, `tested against planted errors` `PC_REM_3` in `76dc758f1`): legacy `dlam2` had `legacy_dlam2_rel_err_caught = "0.30187933"` (`30.19%` error). Removing `+16 g_3^2 H_e` from $\beta_{Y_e}^{(2)}$, restoring $+\frac{5}{4}T H_d Y_u$ and $+\frac{5}{4}T H_u Y_d$, and restoring the full two-loop Higgs quartic $\beta_\lambda^{(2)}$ gives `dlam2_repaired_exact = "20.39417125"` (`dlam2_vs_exact_16315337_over_800000_err = "0.0"` at `50` digits) and `su3_pow_5_covariance_max_err = "8.35239e-53"`.
   - **Remediation:** Full repaired two-loop $\overline{\mathrm{MS}}$ RGEs written out in Appendix B of `self_consistent_loop/manuscript/main.tex` and verified in `relays/x_rem12_verify/verify_x_rem12.py`.

10. **`MAJ-03` (`45fe6e401:self_consistent_loop/inflation_lepton_phase7/src/phase7_toe/p7_4_five_sheeted_cover_cusp_audit.py:33` & `45fe6e401:self_consistent_loop/manuscript/main.tex:53` degree-`5` cover mis-indexing and `"regular / single cusp"` mislabeling):**
    - **Result:** `the same` as `247bd2923` (`recomputed independently`, `tested against planted errors` `PC_REM_2` in `76dc758f1`): `m004` has `4` connected degree-`5` covers (`index 0`: cyclic $C_5$, `1` cusp, $b_1=1$, $\mathbb{Z}_{11}^2$; `index 1` & `3`: irregular `o10_150703`, `2` cusps, $b_1=2$, $\mathbb{Z}_2$; `index 2`: unique irregular $D_5$-quotient cover `8^3_4` / `o10_150685`, `3` cusps, $b_1=3$, `torsion = []`, $J = 31$).
    - **Remediation:** Classified all `4` covers in `Table II` and `Fig. 1(b)` (`self_consistent_loop/manuscript/figures/fig5_porti_torsions_and_covers.pdf`) of `self_consistent_loop/manuscript/main.tex`.

11. **`MAJ-04` (`45fe6e401:self_consistent_loop/inflation_lepton_phase7/src/phase7_toe/p7_2_collar_hierarchy_and_proton_lifetime.py` vs `self_consistent_loop/weave_toe_phase6/src/phase6_toe/w3_horava_witten_11d.py` `6.86x` gravity hierarchy conflict):**
    - **Result:** `the same` as `247bd2923` (`recomputed independently` in `76dc758f1`): `MKK_over_MPl_7D_EH = "0.00196599309"` vs `MKK_over_MPl_Adams_cusp = "0.0002865908773"` (`ratio_7D_EH_over_Adams = "6.859929069"`, `47.06x` in $M_{\mathrm{Pl}}^2$).
    - **Remediation:** Recorded as Obstruction `4` in `Table III` and Section VI of `self_consistent_loop/manuscript/main.tex`.

12. **`MAJ-05` (`45fe6e401:self_consistent_loop/inflation_lepton_phase7/src/phase7_toe/p7_1_radion_casimir_inflation_baryogenesis.py:136` empirical Liddle–Leach pivot constant inside Track A):**
    - **Result:** `the same` as `247bd2923` (`recomputed independently`): the Liddle–Leach pivot offset encodes present-day Hubble and CMB temperature inputs, violating a strict `0 of 19` Track-A firewall.
    - **Remediation:** Removed completely from `relays/x_rem12_verify/verify_x_rem12.py` (`python_float_literal_count = 0`, `0 of 19`) and `self_consistent_loop/manuscript/main.tex`.

13. **`MAJ-06` (`45fe6e401:self_consistent_loop/selberg_determinant_phase11/src/phase11_toe/p11_4_dp_tower_m2_tadpole_uniqueness.py` CY4 Bousso–Polchinski sign flip at $R_{\mathrm{flux}}^2 = \chi/24$):**
    - **Result:** `the same` as `247bd2923` on the naive $b_4$ sign flip (`naive_b4_log10_BP_chi_over_24 = "172.42755"` at $r=8$), and resolved analytically via Hirzebruch's signature theorem (`recomputed independently`, `expectations committed first`, `tested against planted errors` `PC_REM_5` in `76dc758f1`): $\tau(X_r) = 32 + \chi(X_r)/3$ splits $b_4(X_r)$ into $(b_4^+, b_4^-) = (1441(9-r)+195,\, 721(9-r)+67)$ (`(1636, 788)` at $r=8$), and restricting supersymmetric self-dual fluxes ($*G_4 = +G_4$) to positive-definite $H^4_+(X_r)$ yields `self_dual_b4plus_log10_BP_chi_over_24 = "-23.682493"` and `self_dual_b4plus_log10_BP_chi_over_12 = "-269.92503"` at $r=8$ (`< 0` for every $r = 0,\dots,9$ under both normalizations).
    - **Remediation:** Proved and plotted across $r = 0,\dots,9$ in Section V and `Fig. 3` (`self_consistent_loop/manuscript/figures/fig7_cy4_signature_and_bp.pdf`) of `self_consistent_loop/manuscript/main.tex`.

14. **`MAJ-07` (`45fe6e401:self_consistent_loop/zero_input_precision_phase9/src/phase9_toe/p9_2_contino_pilo_gut_thresholds.py:168` missing $1/(2\pi)$ loop factor in Contino–Pilo threshold):**
    - **Result:** `the same` as `247bd2923` (`recomputed independently` in `76dc758f1`): `contino_pilo_zeta_err = "0.0"` on $2[\zeta'(0,1/2) - \zeta'(0)] = \ln\pi$, while unit-$b$ one-loop matching gives `contino_pilo_1loop_unit_b_shift = "-0.18218942"` (`-(1/(2*pi)) ln pi`) vs `legacy_unnormalized_minus_ln_pi = "-1.1447299"`.
    - **Remediation:** Recorded as Obstruction `5` in `Table III` and Section VI of `self_consistent_loop/manuscript/main.tex`.

### C. Minor & Polish Findings (`MIN-01` – `MIN-05`) + Certified Pure-Math Core (`Gate P11-2`)

15. **`MIN-01` (`self_consistent_loop/manuscript/references.bib` SISSA `number = {20xx}` fields):** `the same` — corrected all `J. High Energy Phys.` entries in `self_consistent_loop/manuscript/references.bib` to `volume = {YYYY}` and `number = {MM}` (`0` BibTeX warnings under `apsrev4-2.bst`).
16. **`MIN-02` (`45fe6e401:self_consistent_loop/manuscript/main.tex` `v1` count mismatch `4` vs `8`):** `the same` — superseded and eliminated by retracting the phenomenological progression scorecard from `self_consistent_loop/manuscript/main.tex`.
17. **`MIN-03` (Undocumented heuristic UV constants in Phase `5`–`10` ansatzes):** `the same` — all ungrounded heuristic phenomenological ansatzes are retracted from `self_consistent_loop/manuscript/main.tex`.
18. **`MIN-04` (`Yoo2022RBC` proton-decay matrix element):** `cannot check` inside the masked repository per `origin/main:docs/seats/README.md` § 9.1 (`empirical lattice hadronic constant named`); proton-decay phenomenology retracted from `self_consistent_loop/manuscript/main.tex`.
19. **`MIN-05` (`self_consistent_loop/manuscript/main.tex` placeholder author & `% [reviewer]` comment):** `the same` — replaced with `\author{originaxiom}` and removed the `% [reviewer]` comment in `self_consistent_loop/manuscript/main.tex`.
20. **Certified `60`-Digit Adjoint Torsion Benchmark (`Gate P11-2` / `R1` in `76dc758f1`):** `the same` across all `3` independent implementations (`Sym^2(C^2)`, `SO(3, C)`, and `Cartan–Chevalley` in `76dc758f1` and `247bd2923`; `recomputed independently`, `expectations committed first`, `tested against planted errors` `PC_REM_1`): `max_chevalley_vs_sym2_I_Porti_diff = "0.0"`, `m004_tau_minus_2sqrt3 = "1.18997e-46"`, `m004_SL2Z_S_invariance_err = "6.22302e-61"`, `m129_vol_minus_4Catalan = "0.0"`, `m129_is_chiral = true` (`Table I` of `self_consistent_loop/manuscript/main.tex`).

---

## 3. What Was Not Done (`origin/main:docs/seats/README.md` § 7)

1. Historical Phase `5`–`11` files (`self_consistent_loop/*/PREREGISTRATION_PHASE*.md`, `self_consistent_loop/*/SEAL_SHA256.txt`, `self_consistent_loop/selberg_determinant_phase11/outputs/*.json`, and `self_consistent_loop/manuscript/figures/fig1..4.pdf`) were intentionally **not** edited, deleted, or moved so all historical hashes and file paths remain intact (`origin/main:WORKING_RULES.md` Rules `3` & `9`).
2. Per `origin/main:docs/seats/README.md` § 9.1 (`0 of 19`), no empirical PDG, NuFIT, Planck, or lattice-QCD data comparisons are performed in `relays/x_rem12_verify/verify_x_rem12.py`, `self_consistent_loop/manuscript/main.tex`, or this note.
3. Resolving the five structural consistency obstructions in `Table III` of `self_consistent_loop/manuscript/main.tex` within a single dynamically stabilized higher-dimensional action remains an open theoretical problem rather than a completed closure.

0 of 19.
