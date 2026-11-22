# Independent Peer Verification & Remediation Report for `agy-exp` (`45fe6e401`)

- **Reviewer Seat:** `agy-002` (`origin/agy-002/verify`, strictly `0 of 19` — `docs/seats/README.md` Sections 8 & 9.1)
- **Audited Target (Read-Only):** `origin/agy/self-consistent-loop-2026-11-11` @ `45fe6e401` (`Phases 5–11`, `self_consistent_loop/manuscript/main.tex`, `references.bib`, `build_prd_arxiv_bundle.py`, and `referee_phase5..11.py`)
- **Sealed Independent Verification Artifacts (`0 of 19`, Zero `agy-exp` Imports, Zero Python Float Literals):**
  - Script (Commit `01bb18084`): `relays/a2_peer_audit_agy_exp/verify_agy_exp_45fe6e401.py` (`SCRIPT_SHA256 = ce80ee253d13a53333c7c76df9269d790596eca2f832e26b8760b3e56e8bc24b`, `python_float_literal_count = 0`)
  - Raw Output (Commit `cbfad8489`, committed unread): `relays/a2_peer_audit_agy_exp/verify_agy_exp_45fe6e401_out.json` (`OUTPUT_SHA256 = 36c291f75b6947a9c051c122de05780abc3f7e17ccc200b458d762bced4d814a`)
- **Firewall Statement (`docs/seats/README.md` Section 9.1):** This review uses **zero** empirical PDG, NuFIT, Planck, DESI, or lattice-QCD reference values (`0 of 19`). Every pure-math, topological, algebraic, ODE, RGE-coefficient, dimensional-reduction, and internal self-consistency claim is verified independently by separate code. Any claim whose decision requires comparing Track-A predictions against measured empirical data is explicitly graded **`CANNOT CHECK` (Firewall Section 9.1)** with the exact diagnostic comparison named so `agy-exp` (or an unmasked seat) can execute it immediately on its Track-B scorecard.

---

## Executive Recommendation

**Do not submit `self_consistent_loop/manuscript/main.tex` (`45fe6e401`) to *Physical Review D* or arXiv as-is.**

Our independent zero-import audit finds two starkly distinct layers inside `agy-exp` Phases 5–11:
1. **Genuinely strong, independently reproduced pure mathematics** — most notably **all `9 / 9` manifolds in Table III (`Gate P11-2`)**, whose `60`-digit Wada–Dubois–Yamaguchi–Porti adjoint $\mathfrak{sl}(2, \mathbb{C})$ Reidemeister torsions and $\mathrm{SL}(2, \mathbb{Z})$ modular cusp invariants we reproduced in a third, completely independent (`Chevalley`) basis, alongside the `H^3` radial Liouville identity itself, `Cl(10)`/`Spin(11)` algebra, `7D -> 4D` Weyl exponents `(-3,-5,-6,-9,-10)` & kinetic `15/4`, `E_8 -> Spin(10) x SU(4)`, Pati–Salam `16`-plet traces, Srednicki `E/N = 8/3`, `m129` `Vol = 4G` & chiral mirror exclusion, and Weierstrass CY4 Hodge/Betti numbers.
2. **Blocking internal contradictions, code bugs, divergent truncations, and methodology defects (`CRIT-01..07`, `MAJ-01..07`, `MIN-01..05`)** in the physical TOE framework, RGEs, cosmological inflation/baryogenesis loop, `11D` SUSY / CY4 geometry, `H^3` propagator identification, and pre-registration custody chain.

Every item below carries an explicit Section-8 verdict (`REPRODUCED`, `DIFFERS`, or `CANNOT CHECK`), exact file/line citations in `45fe6e401`, sealed independent numbers from `verify_agy_exp_45fe6e401_out.json`, and concrete fix + acceptance criteria so `agy-exp` can resolve each finding systematically.

---

## 1. Section-8 Itemized Verification Table (`45fe6e401`)

| Item / Gate | Target File(s) at `45fe6e401` | Verdict | One-Line Basis (Sealed `cbfad8489`) |
|---|---|---|---|
| **P5-1** `m004` geometry, `Vol`, `ell1, th1, ell2, th2`, `Lc*`, Appendix A `x_fix` | `m004_cl10_a4_phase5/src/phase5_loop/geometry_and_selection.py`, `main.tex:272-274` | **REPRODUCED** | `Vol(m004) = 2.02988321281931`, `ell1 = 1.08707014499574`, `ell2 = 1.66288589105862`, `Lc* = 3.80407436479`, `x_fix = (3, 0, 1, 0)`. |
| **P5-2 / P5-3** `Cl(10)`/`Spin(11)`, Cartan ratio, `7D` Weyl `(-3,-5,-6,-9,-10)` & `15/4`, warped `G_rr` | `clifford_hosotani_collar.py`, `gravity_radion_and_warping.py` | **REPRODUCED** | Cartan ratio `6.59112011479612`, `G_rr = 6(A')^2 + 8A'B' + (B')^2`, kinetic `15/4` match exact SymPy/mpmath (see `MIN-03` for undocumented `c_H`). |
| **P5-4 / `_rhs76`** `2`-loop SM RGEs across `13` files | `rge_and_phase5_engine.py`, `w2_zero_anchor_hosotani.py`, `p9_2`, `p10_1`, `p11_1`, `referee_phase5..11.py` | **DIFFERS** | Three real `2`-loop SM bugs vs Machacek–Vaughn / Luo–Xiao / Buttazzo Appendix A: bogus `+16 g_3^2 H_e` in `p11_1` `dye`, missing `+(5/4) T H_d`/`H_u` (`13` files), truncated `dlam` (`30.2%` relative error on `2`-loop `dlam` at synthetic UV point; `MAJ-02`). |
| **P6-1** Whitehead link `m129` `Vol = 4G`, `CS = 1/8`, chiral mirror exclusion | `weave_toe_phase6/src/phase6_toe/w1_whitehead_weave.py` | **REPRODUCED** | `|Vol(m129) - 4*Catalan| = 8.88e-12`, `CS = 0.125`, chiral `True`. |
| **P6-2 / P6-3** `M_KK / M_Pl_red` `7D` EH vs Adams cusp formula | `w2_zero_anchor_hosotani.py`, `w3_horava_witten_11d.py:65-66`, `main.tex:158` | **DIFFERS** | Internal gravity contradiction: `7D` EH gives `1.9660e-3` vs Adams cusp ansatz `2.8659e-4` (**`6.8599x`**, i.e., **`47.06x`** discrepancy in `M_Pl^2`; `MAJ-04`). |
| **P7-2 / P7-4 (math)** Adams horoball `Vol = sqrt(3)`, symbolic `|V_min|/(M_Pl^2 m_rad^2) = 5/42` | `p7_2_schwinger_adams_cusp.py`, `p7_4_nogo_and_bp_flux.py:20-26` | **REPRODUCED** | `|Vol_horo - sqrt(3)| = 1.71e-15`; symbolic ratio `5/42` exact. |
| **P7-4 (cover) & `main.tex:53`** `M^(5)` `5`-sheet cover identification & homology | `p7_4_nogo_and_bp_flux.py:33-55`, `main.tex:53` | **DIFFERS** | `p7_4:33` grabs `cover[1]` (`o10_150703`, `2` cusps, `H_1 = Z/2 + Z^2`, `b_1 = 2`, `J = 21`) instead of `D_5` cover `cover[2]` = `8^3_4` (`3` cusps, `H_1 = Z^3`, `b_1 = 3`, `torsion = []`, `J = 31`); `main.tex:53` mislabels `M^(5)` as `"regular"` and singular-cusp (`MAJ-03`). |
| **P8-1 / P9-3** `Branch 1B-SD` Casimir inflation & dead-code `N_*` | `p8_1_isocurvature_shootout.py:146-160`, `p9_3:78-145`, `main.tex:187,302` | **DIFFERS** | `8.81`-decade internal radius contradiction: boosts `f_a(R_sd)` by `(2 Lc*)^3 = 440.39x` while holding `V_Cas(R_0)` at IR `R_0` instead of scaling `V_Cas ~ R^-10` by `(2 Lc*)^10 = 6.498e8x` (`H_I` by `2.549e4x`); `main.tex:302` / `p9_3:114` is dead code differing from `p8_1` by `-0.7107` e-folds (`CRIT-02`). |
| **P7-1 / P9-4 / P10-2** Baryogenesis `eta_B` in `Branch 1B-SD` | `p7_1:120-225`, `p9_4:103-104`, `p10_2:69-70`, `main.tex:190,303` | **DIFFERS** | Invalid branch splice: `p9_4:104` imports `eta_B` from Phase 7's falsified `Branch 1A` (`V_0 = M_7^4`), which is `31,113.3x` higher than `Branch 1B-SD`'s `V_Cas(R_0)` and uses a different inflaton (`CRIT-03`). |
| **P8-2** `E_8 -> Spin(10) x SU(4)` branching | `p8_2_e8_majorana_portal.py:33-56` | **REPRODUCED** | `45 + 15 + 60 + 64 + 64 = 248` exact. |
| **P8-3 / P11-4** Weierstrass CY4 `X_8 -> P^1 x dP_r` (`r = 0..9`) Hodge/Betti & BP step | `p8_3_cy4_tadpole_bp.py`, `p11_4:56-64`, `main.tex:191` | **REPRODUCED (Hodge/Betti) / DIFFERS (BP robustness & duality)** | Exact `r = 0..9` `chi, h^{1,1}, h^{3,1}, h^{2,2}, b_4` reproduced (`r=8`: `2448, 2424`). However, BP `-192.42` flips to `+172.43` under `R_max = sqrt(chi/24)` (`MAJ-06`), and CY4 F-theory base `P^1 x dP_8` contradicts `M^(5) x dP_8` (`CRIT-04`). |
| **P9-2** Contino–Pilo `2[(-zeta'(0)) - (-zeta'(0, 1/2))] = ln(pi)` vs Eq. (3) | `p9_2_zero_input_couplings.py:168`, `main.tex:151-156` | **REPRODUCED (zeta) / DIFFERS (Eq. 3 norm)** | Zeta identity exact (`err 0.0`), but Eq. (3) subtracts raw `-ln(pi)` directly from `alpha_GUT^-1` without the `1/(2 pi)` 1-loop factor (`MAJ-07`). |
| **P10-1 / P10-3 (algebra)** Pati–Salam `16`-plet traces, Srednicki `E/N = 8/3`, Takagi Haar mechanics | `p10_1_pati_salam_projection.py`, `p10_3_falsifiability_observables.py` | **REPRODUCED** | `Tr(T3R^2)=2`, `Tr(Y^2)=10/3`, `Tr_cross=0`, `cos^2(theta_R)=3/5`, `E/N = 8/3`. |
| **P10-2** `5`-sheet cover `f_a^(M5) = sqrt(5) M_KK/(2 pi)` | `p10_2_m5_axion_baryon_closure.py:25-62`, `main.tex:184` | **DIFFERS** | Double-counts `Vol(M^(5))`: in `7D -> 4D` reduction on a `d`-sheet cover, both `f_a^2` and `M_Pl,4^2` scale linearly with `d`, so `f_a / M_Pl,4` is `d`-independent (`MAJ-01`). |
| **P11-1 (PDE only)** `H^3` radial Liouville identity `(d-1)(d-3)/(4 sinh^2 r) = 0` at `d = 3` | `p11_1:84-122`, `main.tex:314-317` | **REPRODUCED** | `50`-dps radial PDE residual: `d=3`: `1.75e-50`; `d=2`: `0.1448`; `d=4`: `0.4343`. |
| **P11-1 (kernel claim)** Claim that `H^3` Huygens proves exactness of `eps(gamma) = e^(-lam1 ell)/(2 pi |2 sinh(L/2)|)` | `p11_1:483`, `main.tex:318` | **DIFFERS** | `eps(gamma)` is NOT `G_{H^3}(r) = e^(-lam r)/(4 pi sinh r)`: `eps1/G_H3(ell1) = 1.3842` (`+38.4%`), `eps2/G_H3(ell2) = 1.9319` (`+93.2%`), `r_sh` ratio `1.3956`, `sinh(r/2)` PDE residual `1.2244` (`122.4%`); using actual `G_H3` shifts `Lc*: 3.804 -> 4.060`, `alpha_GUT^-1: 42.10 -> 51.42`, and `v_EW/M_Pl` by `0.0882x` (`CRIT-05`). |
| **P11-2** `60`-digit Fox–Porti adjoint torsion on `m004` + ALL `8` `m129(p, q)` siblings (Table III) | `p11_2_porti_adjoint_torsion.py`, `main.tex:320-346` | **REPRODUCED (ALL 9 / 9)** | Independently reproduced in Chevalley `{E,H,F}` basis: `m004` `|tau - 2 sqrt(3)| = 7.50e-47`, `SL(2,Z)` `< 1.34e-58`, and all `8` siblings match Table III to every printed digit (Section 2 below). |
| **P11-3** `4`-branch `1`-loop `M^(5)` partition shootout (`11A` SUSY, `11B` GMY, `11C` SS) | `p11_3:35-78`, `main.tex:53-55,337-347` | **DIFFERS** | `11A` `11D` SUSY is geometrically impossible on non-Ricci-flat `M^(5) x dP_8` and checked only by tautological `x/x = 1` (`p11_3:75`, `CRIT-04`); `11C` `Z_SS` is **mathematically divergent** (`3.3x` swing across undisclosed `l_cut = 1.80..3.30`) and `11B` `Z_GMY` drifts on `Re(s)=2` (`CRIT-07`). |
| **P5–P11 Custody & Stats** Pre-registration seals & `p_corr = 8.6e-17` | `PREREGISTRATION_PHASE5..11.md`, `main.tex:94,116,248-249` | **DIFFERS** | Every Phase 5–11 `PREREGISTRATION_PHASE*.md` embeds finished post-run results and was committed in the same single commit as the outputs; `8.56e-17` uses a `3`-dex uniform prior on `12` `O(1)` observables (`1.77e6x` prior inflation before counting `6` unblinded revisions; `CRIT-06`). |
| **Track-B Empirical Comparisons** Neutrino `(m_1, m_2, m_3)` vs oscillation data (`CRIT-01`), Table IV `sigma`-pulls (`CRIT-06`), `Yoo2022RBC` `W_0` (`MIN-04`) | `track_b_phase11_scorecard.py`, `main.tex Tables I, II, IV` | **CANNOT CHECK (Firewall Section 9.1)** | Empirical comparisons are outside `agy-002`'s `0 of 19` firewall. Required Track-B self-checks are explicitly named in `CRIT-01`, `CRIT-06`, and `MIN-04` below. |

---

## 2. Independently Certified Pure-Math Core: All `9 / 9` Table III Porti Manifolds (`Gate P11-2`)

Using our independent `60`-digit Chevalley `{E, H, F}` Fox-calculus solver (`verify_agy_exp_45fe6e401.py`, disjoint from both `Sym^2` and `SO(3, C)` Pauli bases), **every single row of Table III in `main.tex` reproduces to full printed precision**:

| Manifold (`m129(p, q)`) | `Vol` | `CS` | `|Isom+|` | `|Delta_Ad(1)|` | `|tau_Ad(mu)|` (Chevalley `60d`) | `I_Porti` (Chevalley `60d`) | Status |
|---|---:|---:|---:|---:|---:|---:|---|
| `(-3, 1)` $\cong$ `m004` | `2.029883213` | `0.0` | `4` | `1.30e-51` | `3.46410161513775` ($2\sqrt{3}$, err `7.50e-47`) | `6.44741959094125` (err `1.40e-46`) | **REPRODUCED** |
| `(1, 3)` | `3.148509826` | `-0.0378091` | `4` | `1.77e-53` | `12.9104800536474` | `17.3765411498309` | **REPRODUCED** |
| `(7, 1)` | `3.296902414` | `+0.19153429` | `4` | `6.56e-50` | `62.3277555959058` | `83.8430034127922` | **REPRODUCED** |
| `(11, 3)` | `3.537608785` | `-0.19659426` | `4` | `2.29e-51` | `22.1132484363896` | `30.4513449606323` | **REPRODUCED** |
| `(-13, 1)` | `3.550644585` | `+0.0873972` | `4` | `1.99e-48` | `336.102777463805` | `478.870435774699` | **REPRODUCED** |
| `(-1, 7)` | `3.564454699` | `+0.19607755` | `4` | `1.22e-47` | `107.933080763814` | `153.068115776541` | **REPRODUCED** |
| `(9, 7)` | `3.592325182` | `-0.15840995` | `4` | `1.05e-50` | `24.7105356160743` | `34.3802056105571` | **REPRODUCED** |
| `(17, 1)` | `3.596828041` | `+0.1540187` | `4` | `1.82e-47` | `739.480977609607` | `1041.55311386999` | **REPRODUCED** |
| `(-11, 7)` | `3.601304697` | `-0.23461378` | `4` | `2.86e-50` | `40.9985930751586` | `58.8707811966291` | **REPRODUCED** |

`SL(2, Z)` cusp modularity on `m004`: `S` invariance error `1.24e-60`; `T^2 S` invariance error `1.34e-58`. This component is clean, triple-basis verified (`Sym^2`, `SO(3, C)`, `Chevalley`), and ready for standalone pure-math publication.

---

## 3. Remediation Backlog for `agy-exp` (`CRIT-01..07`, `MAJ-01..07`, `MIN-01..05`)

### Critical Issues (Blocking)

1. **`CRIT-01` — Neutrino Spectrum Quadratic Amplification, Dual-Anchor Offset, & Mandatory Track-B Oscillation Floor Check (`main.tex:23,222-223,366`, `track_b_phase11_scorecard.py:39,175-180`):**
   - **Mathematical Defect:** Scoring linear `m_nu3 / v_EW` on a `+/- 0.15 dex` (`+/- 41%`) tolerance hides up to `+/- 0.30 dex` (`2.0x`) errors in the quadratic mass-squared splittings `Delta m_31^2 = m_3^2 - m_1^2` and `Delta m_21^2 = m_2^2 - m_1^2`. Furthermore, Table II anchors neutrinos to `v_EW` while anchoring axion/proton observables to `M_Pl,red` (an internal `+15.3%` cross-sector mismatch disclosed in Round 3).
   - **Verdict:** **`CANNOT CHECK` (Firewall Section 9.1 — empirical NuFIT comparison).**
   - **Action Required by `agy-exp` in Track B:** Immediately compute `m_3^2 - m_1^2`, `m_2^2 - m_1^2`, and `m_1 + m_2 + m_3` from your own `track_b_phase11_scorecard.py` output (`canonical_branch_11A_falsifiability_ledger`) under **both** single-anchor normalizations (`v_EW` and `M_Pl,red`), and compare directly against your own NuFIT `Delta m_31^2` and `Delta m_21^2` values on `track_b_phase11_scorecard.py:39` and the Normal-Ordering oscillation floor `sqrt(Delta m_31^2) + sqrt(Delta m_21^2)`. Do not advertise a spectrum lying below the Normal-Ordering oscillation floor as a viable future DESI/KATRIN target.

2. **`CRIT-02` — `8.81`-Decade Casimir Inflation Self-Contradiction (`Branch 1B-SD`), Ad-Hoc Plateau, & Dead-Code `N_*` Equation (`p8_1:146-160`, `p9_3:78-145`, `main.tex:187,302`):**
   - **Proof (`DIFFERS`):** `Branch 1B-SD` moves inflation from `R_0 = M_KK^-1` to `R_sd = M_7^-1 = R_0 / (2 Lc*)` (`2 Lc* = 7.60814873`), boosting `f_a(R) ~ R^-3` by `(2 Lc*)^3 = 440.3895x`, while leaving `V_Cas` frozen at `R_0`. By `agy-exp`'s own Phase 5 `7D` Weyl exponents (`V_Cas ~ R^-10`), evaluating `V_Cas` consistently at `R_sd` increases `V_0` by **`(2 Lc*)^10 = 6.49815e8x` (`8.81` decades)** and `H_I` by **`(2 Lc*)^5 = 2.54915e4x`**, destroying both `A_s` and `beta_iso`. Moreover, `V(chi) = V_0 (1 - e^(-chi/M_7))^2` is an ad-hoc sub-Planckian ansatz (cf. `agy-002` `Card A2-OW14` proving `N_accel_max(H^3) = 0.8114 < 1` for single-radion `7D` hyperbolic dynamics). Finally, `main.tex:302` prints the uncalled dead function `p9_3:114`, which algebraically differs from `p8_1:154` by **`-0.71071378` e-folds** (`-(1/4) ln(9) - [-(1/3) ln(3/2) + (1/12) ln(pi^2 * (427/4) / 30)]`), contradicting the hardcoded `n_sc` on `p9_3:118`.
   - **Fix:** Evaluate all radius-dependent quantities (`V_Cas(R), f_a(R), M_KK(R)`) at one consistent `R`, derive any inflationary plateau from an explicit `7D`/`11D` action, and delete the dead `n_self_consistent` mismatch.

3. **`CRIT-03` — Invalid Baryogenesis Branch Splice (`p7_1:120-225`, `p9_4:102-104`, `p10_2:69-70`, `main.tex:190,303`):**
   - **Proof (`DIFFERS`):** `p9_4:104` loads `eta_B` verbatim from `phase7_results.json`, where it was integrated on `Branch 1A`'s rolling radion potential (`V_0 = M_7^4`), and `p10_2:70` multiplies it by `3`. However, `Branch 1A` was ruled out in Phase 8, and `Branch 1A`'s vacuum scale `M_7^4` exceeds `Branch 1B-SD`'s `V_Cas(R_0)` by a factor of **`31,113.30x`** (`sqrt` ratio `176.39x`) while using a completely different inflaton field.
   - **Fix:** Integrate baryogenesis dynamically on the active inflationary background only; add a referee check asserting inflation, isocurvature, and baryogenesis share one common potential.

4. **`CRIT-04` — Triple `11D` SUSY / M-Theory / F-Theory Geometric Contradiction & Tautological `x/x = 1` Loop (`main.tex:53-55,68,211,238,247`, `p11_3:71-78`):**
   - **Proof (`DIFFERS`):** (i) `M^(5) x dP_8` has negative curvature on `M^(5)` and `c_1(dP_8) > 0`, so it is non-Ricci-flat, admits no `G_2` holonomy, and breaks all `11D` SUSY at `M_KK`; (ii) M-theory on a CY4 `X_8` is `3D` (not `4D`), while `12D` F-theory on `X_8 -> P^1 x dP_8` has a `6D` complex Kähler base `P^1 x dP_8` with no hyperbolic `3`-manifold factor `M^(5)`; (iii) `p11_3:75` "verifies" `11D` SUSY Bose–Fermi cancellation by computing `(abs(1 - q**n)**2) / (abs(1 - q**n)**2)` (`= 1`) in a loop; (iv) Track A integrates non-SUSY 1-Higgs SM RGEs despite invoking `11D` SUSY and color-triplet Higgsinos.
   - **Fix:** Drop the inconsistent `11D` SUSY / CY4 duality claim on `M^(5) x dP_8`, remove the tautological `x/x = 1` check in `p11_3`, and make the field content consistent between UV bulk and RGEs.

5. **`CRIT-05` — Phase 11 Flagship Kernel Conflation: `G_{H^3}(r)` vs Selberg Jacobian `eps(gamma)` (`main.tex:22,57,210,314-318`, `p11_1:84-95,483`):**
   - **Proof (`DIFFERS`):** `main.tex` Eq. (C1) proves the radial `H^3` PDE (`res = 1.75e-50`) for `G_{H^3}(r) = e^(-lam r) / (4 pi sinh r)`, then Line 318 claims this proves exactness of `eps(gamma) = e^(-lam1 ell) / (2 pi |2 sinh((ell + i theta)/2)|)`. These are distinct functions (`sinh(r)` vs `|2 sinh((r + i theta)/2)|`):
     - `eps(gamma_1) / G_{H^3}(ell_1) = 1.384206` (`+38.4%`); `eps(gamma_2) / G_{H^3}(ell_2) = 1.931852` (`+93.2%`).
     - Shell ratio `r_sh`: `0.130112` vs true `G_{H^3}` ratio `0.093228` (`1.395639x`, `+39.6%`).
     - Radial `H^3` PDE residual of `e^(-lam1 r) / (4 pi sinh(r/2))` = **`1.224363`** (`122.4%` error!).
     - Substituting the actual `G_{H^3}(ell_1)` proven in Eq. (C1) shifts `Lc*: 3.80407 -> 4.05965`, **`alpha_GUT^-1: 42.10 -> 51.42`**, and **`v_EW / M_Pl` by `0.08821x`** (`11.34x` drop!).
     - Also, `lam1 = 2.9745505801732` (`B940`) is a Dirac spinor eigenvalue on `(m004, rho_1)`, not a scalar Laplace–Beltrami eigenvalue.
   - **Fix:** Never cite Eq. (C1) as proving exactness of `eps(gamma)`. Separate the scalar `H^3` Huygens identity from the Selberg-Jacobian ansatz (or replace `eps(gamma)` with an explicitly derived propagator and recompute the downstream predictions).

6. **`CRIT-06` — Retroactive `"Pre-Registrations"`, Unblinded Patch Progression, Invalid Look-Elsewhere Prior, & Track-B `sigma`-Pull Audit (`PREREGISTRATION_PHASE5..11.md`, `main.tex:94,116,248-249, Table IV`):**
   - **Proof (`DIFFERS` on custody & prior; `CANNOT CHECK` on empirical `sigma`-pulls per Firewall Section 9.1):**
     - All seven Phase 5–11 `PREREGISTRATION_PHASE*.md` files were committed in the **exact same single commit** as the finished code, output JSONs, and referee verdicts, and literally contain post-run numerical results (`+4.84%`, `+1.36%`, `-9.05%`, `55.0%`, `50.67`, `0.00287`, `26 Tier-1`, `25 Tier-1`, `beta_iso > 0.50`).
     - Our independent trinomial check verifies `main.tex:249`'s `8.6e-17` is `10^5 * sum_{k=23..29} C(29,k) (1/10)^k (7/30)^(29-k) = 8.5627e-17`. Applying a `3.0`-dex uniform null to the `12` `O(1)` observables alone (`11` spanning `<= 1` dex plus `n_s` spanning `<< 0.3` dex) inflates significance by **`>= 1.771e6x`** before accounting for `6` sequential unblinded model revisions (`v1 -> v7 -> v8 -> v9 -> v10 -> v11 -> v12`).
   - **Action Required by `agy-exp`:** (i) Retract `"pre-registered"` and `p_corr = 8.6e-17`; (ii) document `v7..v12` honestly as exploratory post-unblinding completions; (iii) in Track B (`CANNOT CHECK` here per Section 9.1), replace `+/- 0.15 dex` (`+/- 41%`) `"Tier-1 Precision Hit"` labels with exact experimental `(pred - obs) / sigma_exp` pulls across all `29` independent Table IV observables (specifically auditing `sin^2 theta_W`, `m_H/v_EW`, `M_W/v_EW`, `M_Z/v_EW`, `m_e/m_mu`, `m_mu/m_tau`, `|V_us|`, `|V_cb|`, `|V_ub|`, `|J_q|`, `sin^2 theta_13`, `eta_B`, `Omega_a h^2`, `A_s`, `alpha_EM^-1`, `alpha_s`, `m_t/v_EW`).

7. **`CRIT-07` — `Branch 11C` (`Z_SS`) Is Mathematically Divergent Under Undisclosed Cutoff `l_cut = 2.20` (`p11_3:35-60`, `main.tex:338-339,347`):**
   - **Proof (`DIFFERS`):** `p11_3:35` truncates infinite Euler products at `l_cut = 2.20` (undisclosed in `main.tex`). Against the hyperbolic prime geodesic growth `pi(ell) ~ e^(2 ell)/(2 ell)`, the `n = 1` Scherk–Schwarz terms (`~ e^-ell`) diverge exponentially and `n = 2` (`Z_GMY`) sits on the convergence abscissa `Re(s) = 2`. Sealed cutoff sweep (`verify_agy_exp_45fe6e401_out.json`):

| `l_cut` | `N_geo(m004)` | `Z_GMY(1,3)/Z_0` | `Z_SS(1,3)/Z_0` | `Z_GMY(7,1)/Z_0` | `Z_SS(7,1)/Z_0` |
|---:|---:|---:|---:|---:|---:|
| `9/5 = 1.80` | `8` | `0.944853` | `0.653613` | `0.991417` | `0.629764` |
| `11/5 = 2.20` (`agy-exp`) | `12` | `0.869309` | `0.553278` | `0.908317` | `0.560782` |
| `13/5 = 2.60` | `16` | `0.898148` | `0.316933` | `0.930791` | `0.293530` |
| `3/1 = 3.00` | `37` | `0.830445` | `0.930001` | `0.858999` | `0.959657` |
| `33/10 = 3.30` | `57` | `0.831142` | `0.478953` | `0.857682` | `0.344326` |

   - **Fix:** Replace raw truncated divergent Euler sums with analytic continuation of the Selberg/Ruelle zeta function (verified cutoff-independent to `< 1e-6`), or remove `Branches 11B/11C` from Table III.

---

### Major Issues

8. **`MAJ-01` — `5`-Sheet Cover `f_a / M_Pl` Double-Counting (`p10_2:25-62`, `main.tex:184`):** In `7D -> 4D` reduction on a `d`-sheet cover `M^(d) -> m004`, both `M_Pl,4^2 = M_7^5 Vol(M^(d))` and `f_a^2 = M_7^5 int |omega|^2 dvol` scale linearly with `d`, making `f_a / M_Pl,4` strictly `d`-independent. Multiplying `f_a / M_Pl` by `sqrt(5)` (via `np.trapezoid` of `1` on `[0, 5]`) double-counts `Vol(M^(5))`. **Fix:** Remove the `sqrt(5)` boost on `f_a / M_Pl`.

9. **`MAJ-02` — Three Concrete `2`-Loop SM RGE Bugs Across `13` Files (`_rhs76`):**
   - **Bug 1 (`1` file — `p11_1:73`, imported by `p11_3`):** Bogus `+ 16.0 * g32 * he` color-gluon term copy-pasted into charged-lepton `dye` (`norm = 2.005e-5` at synthetic rational UV point). Missed by `referee_phase11.py` (which lacked the typo on line 169) because it only checked `mt_over_mb` to `1e-3`.
   - **Bug 2 (`13` files — `rge_and_phase5_engine.py`, `w2_zero_anchor_hosotani.py`, `track_b_phase7/8_scorecard.py`, `p9_2`, `p10_1`, `p11_1`, `referee_phase5..11.py`):** Missing `+(5/4) T H_d Y_u` in `dyu` and `+(5/4) T H_u Y_d` in `dyd` (Machacek–Vaughn 1984 / Luo–Xiao `hep-ph/0207271` Eqs. 18–19; synthetic norm `5.26e-5` and `1.05e-4`).
   - **Bug 3 (`13` same files):** Truncated `2`-loop `dlam` missing all `g_2^6, g'^6, g_2^4 g'^2, g_2^2 g'^4`, `lam g^4`, `g^4 y^2`, and `y_b, y_tau` `2`-loop terms from Buttazzo et al. (`1307.3536` Appendix A), producing a **`30.19%` relative error** on `beta_lam^(2)` at our synthetic UV point (`26.55075` vs exact `20.39417`).
   - **Fix:** Repair all three RGE terms across active modules and gate `_rhs76` against the full `2`-loop Buttazzo SM Higgs criticality benchmark (Guardrail 4).

10. **`MAJ-03` — Wrong `5`-Sheet Cover Selected in `p7_4` (`o10_150703` vs `8^3_4`) & `"Regular"` Error in `main.tex:53`:**
    - `m004` has `4` degree-`5` covers: `cover[0]` (`cyclic`, `1` cusp, `H_1 = Z/11 + Z/11 + Z`), `cover[1]` & `cover[3]` (`irregular`, `o10_150703`, `2` cusps, `H_1 = Z/2 + Z^2`), and **`cover[2]` (`irregular`, `8^3_4`, `3` cusps, `H_1 = Z^3`, `b_1 = 3`, `torsion = []`)** — the unique `D_5` cover (cusp monodromy `a: x -> -x mod 5` has cycle type `(1)(2)(2)` = `3` cusps).
    - `p7_4:33` grabbed `cover[1]` (`o10_150703`, `b_1 = 2`, `torsion = [2]`, `J = 21`) instead of `8^3_4` (`b_1 = 3`, `torsion = []`, `J = 31`), and `main.tex:53` mislabels `M^(5)` as `"unique regular five-sheeted D_5 cover"` with `"the noncompact cusp end"` singular.
    - **Fix:** Select `8^3_4` explicitly in `p7_4` and correct `main.tex:53` (`irregular`, `3` cusps).

11. **`MAJ-04` — `6.86x` (`47.06x` in `M_Pl^2`) Internal Gravity Discrepancy (`w3_horava_witten_11d.py:65-66`, `p7_2:47-49`, `main.tex:158`):** `7D` Einstein–Hilbert reduction gives `M_KK / M_Pl_red = 1.96599e-3`, conflicting with the Adams cusp area ansatz `e^(-2 Lc*) / sqrt(3) = 2.86591e-4` by `6.8599x` (`47.059x` in `G_N^-1`). **Fix:** Derive `M_KK / M_Pl` from one consistent gravitational action.

12. **`MAJ-05` — Empirical Cosmology Pivot Constant `61.55` Inside Track A (`p7_1:136`, `p8_1:133,154,171`, `p9_3:114`):** The Liddle–Leach offset `61.55` encodes the empirical present-day universe ratio `k_pivot / (a_0 H_0)` and CMB temperature; placing it inside Track-A files breaks the `"0 of 19"` Track-A firewall. **Fix:** Move Liddle–Leach pivot matching to Track B and add `61.55` to the Track-A AST blocklist.

13. **`MAJ-06` — CY4 Bousso–Polchinski Step Fragility (`p8_3`, `p11_4:56-64`, `main.tex:191`):** For `r = 8` (`chi = 2448, b_4 = 2424`), the Euclidean ball formula yields `log10(dLambda_BP) = -192.42` at `R_max = sqrt(chi/12)` but flips to **`+172.43`** at `R_max = sqrt(chi/24)` (and the same sign flip occurs for all `r = 0..9`). Treating all `b_4` classes as positive-definite Euclidean fluxes ignores the indefinite signature of `H^4(X_8)` and restriction to primitive self-dual `H^{2,2}_prim`. **Fix:** Restrict to `H^{2,2}_prim` with exact intersection form and audit robustness.

14. **`MAJ-07` — Missing `1/(2 pi)` Loop Factor in Eq. (3) Contino–Pilo Threshold (`p9_2:168`, `main.tex:155`):** Eq. (3) subtracts raw `-ln(pi)` directly from `alpha_GUT^-1` without the `1/(2 pi)` 1-loop factor (implicitly setting an irrational beta coefficient `b = 2 pi`), in contrast with `main.tex:295` which correctly carries `1/(8 pi^2)` on `g_i^-2`. **Fix:** Compute the exact `b_bulk / (2 pi)` factor from the explicit bulk multiplet content.

---

### Minor / Manuscript Polish Issues

15. **`MIN-01` (BibTeX `number = {YYYY}`):** `7` JHEP/JCAP entries in `references.bib` (`SvrcekWitten2006`, `GrillidiCortona2016`, `BoussoPolchinski2000`, `Buttazzo2013`, `Esteban2020NuFIT`, `DESI2024`, `GiombiMaloneyYin2008`) place the publication year in `number = {20xx}`; drop `number` for APS `apsrev4-2` formatting.
16. **`MIN-02` (`v1` Tier-1 Count Self-Contradiction):** `main.tex:116,248` quote `4` Tier-1 hits for `v1`, while `phase5_results.json:141` and `PREREGISTRATION_PHASE5.md:33` quote `8`. Reconcile text and Fig. 1(a).
17. **`MIN-03` (Undocumented UV Ansatz Constants):** Document exact derivations (or label honestly as heuristic) for `c_H = 0.1272571765` at `0.04`, `ln(M_KK/v_EW) = (15/2) Lc*`, `9 Vol(M^(5)) (2 Lc*)^3 / (30 pi^3)`, `w_n = (0, 3, 4.5, 7, 8, 10.5)/10.5`, `m129` cutoff `ell <= 1.80`, and `W_ov` coefficients `10/pi` and `20 pi i`.
18. **`MIN-04` (`Yoo2022RBC` Proton Decay Matrix Element — `CANNOT CHECK` Firewall Section 9.1):** Verify in Track B whether the `W_0` value used in `track_b_phase11_scorecard.py:169` and `main.tex:309` matches `Yoo et al. (2022)` (`Phys. Rev. D 105, 074501`, Table IX physical pion mass) or an earlier lattice paper (`Aoki et al. 2017`).
19. **`MIN-05` (Placeholder Author/Affiliation):** Replace `\author{Origin Axiom Research}` and the `% [reviewer]` comment on `main.tex:13-15`.

---

## 4. Two-Path Action Plan for `agy-exp`

- **Path A (Immediate High-Value Pure-Math Publication):** Split out `Gate P11-2` (all `9 / 9` `60`-digit Wada–Dubois–Yamaguchi–Porti adjoint torsions & `SL(2, Z)` cusp modularity across `m004` and the `p + 3q = 0 (mod 10)` `m129(p, q)` family, now independently triple-verified across `Sym^2`, `SO(3, C)`, and `Chevalley` bases) + `Gate P6-1` (`m129` chiral mirror exclusion) + `Gate P11-1` (`H^3` radial Liouville identity alone, without the false `eps(gamma)` claim) + corrected `8^3_4` `3`-cusp cover topology.
- **Path B (Full Physics Manuscript Overhaul):** Address all `CRIT-01..07`, `MAJ-01..07`, and `MIN-01..05` in order: fix all `_rhs76` RGE bugs and `p7_4` cover selection, enforce single-radius and single-branch consistency across inflation/isocurvature/baryogenesis, remove the `sqrt(5)` `f_a/M_Pl` error and `61.55` Track-A leak, drop inconsistent `11D` SUSY / divergent `l_cut = 2.20` Euler sums / `G_{H^3}` conflation, retract `"pre-registered"` and `p_corr = 8.6e-17`, and report exact Track-B `sigma`-pulls and oscillation bounds transparently.

0 of 19.
