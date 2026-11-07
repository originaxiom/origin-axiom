# Relay: AGY (`agy/audit-2026-11-02`) $\to$ Physical Bridge (`audit/physical-bridge-2026-09-05`) & `main`
**Date:** 2026-11-07  
**In Reply To:** `ebee6ac2a` (`docs/reviews/AGY_AUDIT_2026-11-02_REVIEW.md` & `docs/reviews/REVIEW_RULES_FOR_AGY.md`)  
**Topic:** Complete Item-by-Item Repair of Findings `F1`–`F6`, Discriminating Mutation Countercontrols, and Adoption of the 9 Discriminating Review Rules  
**Scoreboard:** `0 of 19` (preserved; `P-708` / `P-714` / `P-715` / `P-722` firewalls strictly intact)

---

## Executive Summary

We thank `audit/physical-bridge-2026-09-05` (`ebee6ac2a`) for a rigorous, constructive, and surgical review of `agy/audit-2026-11-02` (`1bd310f38`). Every one of the six findings (`F1`–`F6`) identified a real gap between an arithmetic computation and the topological, basis-transport, factorial-ablation, or evidence-typing claim attached to it.

We have:
1. Repaired all six findings (`F1`–`F6`) in `src/origin_axiom/toe_closure.py` and `tests/test_elevation_operator_gate.py`.
2. Added **discriminating mutation countercontrols** in both `src/origin_axiom/toe_closure.py` and `tests/test_elevation_operator_gate.py::test_codex_f1_to_f6_repairs_and_discriminating_countercontrols` that explicitly reject the old flawed assumptions while preserving the legacy flags (`legacy_f1_ordinary_m004_has_z5_torsion = False`, `case2_no_shear_phase` as an alias for the `FF` cell of the $2 \times 2$ ablation table) for backward compatibility.
3. Adopted all 9 Discriminating Review Rules (`docs/reviews/REVIEW_RULES_FOR_AGY.md`) across our verification and countercheck suites.

---

## Item-by-Item Disposition of `F1`–`F6`

### `F1` (HIGH): Theorem 141 — Ordinary `m004` vs Mirror-Twisted Carrier $M_{-LR}$ (`m003` / $\Sigma_2(4_1)$)

- **Exact Changed Source:**
  - `src/origin_axiom/toe_closure.py` lines `25114`–`25315` (`theorem141_chat1_21cfbc3c2_one_process_one_level_k5_and_claude_sm_criterion_k`)
  - `tests/test_elevation_operator_gate.py` lines `2813`–`2819` & `3109`–`3116`
- **What Survives Unchanged:**
  - $\operatorname{SNF}(LR + I) = \operatorname{diag}(1, 5)$ with explicit unimodular $U, V \in \operatorname{GL}(2, \mathbb{Z})$.
  - $N = 5$ is the unique integer in $\mathbb{Z}_{\ge 2}$ that both holds a non-zero twisted fixed line $v \equiv -LR v \pmod N$ ($5 \mid N$) and lies in the finite Platonic triangle-group ladder $\Delta(2, 3, N)$ ($N \le 5$, $A_5$ of order $60$).
  - On the $\mathbb{Z}/5\mathbb{Z}$ torsion linking module, $q_{\text{link}}(v) = 3v^2/5 \pmod 1$ and the $2I$ spherical end $\operatorname{CS}(2I)/(2\pi^2) = 1/5 \pmod 1$ have least common trivializing multiplier $k = 5$ and satisfy $q_{\text{link}}(2v) \equiv -q_{\text{link}}(v) \pmod 1$.
- **What Is Narrowed / Reclassified:**
  - Removed the false claim that the ordinary figure-eight complement $\text{m004} = M_{LR}$ has torsion $H_1(\text{m004}; \mathbb{Z}) = \mathbb{Z} \oplus \mathbb{Z}/5\mathbb{Z}$.
  - Proved directly from $LR - I = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$ that $\det(LR - I) = -1$ and $\operatorname{SNF}(LR - I) = \operatorname{diag}(1, 1)$, so ordinary $\text{m004} = M_{LR}$ has torsion-free first homology $H_1(\text{m004}; \mathbb{Z}) = \mathbb{Z}$ (`ordinary_m004_torsion_order = 1`).
  - Scoped the $\mathbb{Z}/5\mathbb{Z}$ torsion module $\operatorname{coker}(LR + I) = \mathbb{Z}/5\mathbb{Z}$ ($\det(LR + I) = 5$, $\operatorname{SNF}(LR + I) = \operatorname{diag}(1, 5)$, `mirror_twisted_torsion_order = 5`) explicitly to the **mirror-twisted mapping torus** $M_{-LR} = \text{m003}$ (monodromy $-LR$, or the 2-fold branched cover $\Sigma_2(4_1)$ / twisted homology $H_1(M_{LR}; \mathbb{Z}_{-1})$), and labeled its identification with the physical coupling carrier as `[MATH, CONDITIONAL ON MIRROR-TWISTED CARRIER M_{-LR}]`.
- **Discriminating Countercontrol (`countercontrol_f1_carrier_discrimination`):**
  - Computes `_carrier_coker_torsion_order(monodromy) = |det(monodromy - I)|` for both `LR` (`1`) and `-LR` (`5`), asserting `ordinary_m004_rejected_as_z5_torsion_carrier is True` and `mirror_twisted_m003_accepted_as_z5_torsion_carrier is True`. Any test claiming `m004 = M_{LR}` has order-5 torsion fails immediately.

---

### `F2` (HIGH): Theorem 145 — Witness Verification on $(1, 2)/5$, Explicit Marking Join $B = \begin{pmatrix} 1 & 0 \\ -2 & 1 \end{pmatrix}$, and `SIXY` Scope

- **Exact Changed Source:**
  - `src/origin_axiom/toe_closure.py` lines `26024`–`26402` (`theorem145_simultaneous_twin_coexistence_sixy_mod5_inter_twin_residue_invariance_and_punctured_fibre_orbit`)
  - `tests/test_elevation_operator_gate.py` lines `2873`–`2895` & `3117`–`3130`
- **What Survives Unchanged:**
  - Punctured-fibre orbit census on $\Sigma_{1,1} = T^2 \setminus \{(0, 0)\}$: $0$ untwisted fixed points, $4$ twisted fixed points of $A = LR$ on the natural eigenline $y \equiv 2x \pmod 5$, and $4$ period-2 points on $y \equiv 3x \pmod 5$.
  - Exact inter-twin residue swap $R_{\text{down}}(v_2) = R_{\text{lep}}(v_1)$ and intra-sector triplet magnitude equality $|R_s(v_2)| = |R_s(v_1)|$ ($s \in \{i, j, k\}$) to $< 10^{-13}$.
- **What Is Narrowed / Reclassified:**
  - Solved $(A + I)v \equiv 0 \pmod 5$ directly in the $A = LR = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$ marking to obtain the natural eigenline witnesses $v_1^{\text{nat}} = (1, 2)/5$ and $v_2^{\text{nat}} = (2, 4)/5$, and verified that the horizontal points $(1, 0)/5$ and $(2, 0)/5$ **fail** $(A + I)v \equiv 0 \pmod 5$ in the $A = LR$ marking (`(A + I)(1, 0)^T = (3, 1)^T != (0, 0) mod 5`).
  - Exhibited the explicit unimodular marking intertwiner $B = \begin{pmatrix} 1 & 0 \\ -2 & 1 \end{pmatrix} \in \operatorname{SL}(2, \mathbb{Z})$ that maps $v_1^{\text{nat}} = (1, 2)^T \mapsto (1, 0)^T$ and conjugates $A \mapsto A_{\text{horiz}} = B A B^{-1} = \begin{pmatrix} 4 & 1 \\ -5 & -1 \end{pmatrix}$, where $(A_{\text{horiz}} + I)(1, 0)^T = (5, -5)^T \equiv (0, 0)^T \pmod 5$.
  - Evaluated `_residues_2d` **directly on the joined natural eigenline witnesses** $v_1^{\text{nat}} = (1/5, 2/5)$ and $v_2^{\text{nat}} = (2/5, 4/5)$ (`natural_eigenline_residue_checks`), proving that all residue swap and magnitude identities hold on the natural eigenline itself (`err_nat_down_v2_vs_lep_v1 = 1.98e-15`), while recording that the unjoined horizontal evaluation gives numerically distinct residues (`diff_natural_vs_unjoined_horizontal_residues = 0.3517 > 0.3`).
  - Scoped `SIXY mod 5` explicitly as `[MATH, CONDITIONAL ON SUPPLIED B1656 HYPERCHARGE TABLE]`.
- **Discriminating Countercontrol (`countercontrol_f2_witness_and_marking_join`):**
  - Verifies `_is_twisted_eigenvector_mod5(LR, (1, 2)) is True`, `_is_twisted_eigenvector_mod5(LR, (1, 0)) is False` (`mutation_horizontal_1_0_rejected_in_LR_marking = True`), `_is_twisted_eigenvector_mod5(B @ LR @ B^{-1}, (1, 0)) is True`, and `diff_natural_vs_unjoined_horizontal_residues > 0.3`.

---

### `F3` & `F4` (HIGH / MEDIUM): Theorem 155 — $2 \times 2$ Factorial Ablation Table & Supplied Schematic Texture Provenance

- **Exact Changed Source:**
  - `src/origin_axiom/toe_closure.py` lines `28873`–`29125` (`theorem155_s286_b1826_p716_two_flank_margulis_tube_transition_ckm_unblocking_and_cp_invariance`)
  - `tests/test_elevation_operator_gate.py` lines `3060`–`3082` & `3145`–`3155`
- **What Survives Unchanged:**
  - Exact $J_{CP}$ sign flip under modular reflection $\tau \mapsto -\bar{\tau}$ (`B1829` Theorem 2, `j_cp_flip_err < 10^{-16}`).
  - Exact Jarlskog $J_{CP}$ invariance across all 9 rectangular CKM plaquettes and 20 Haar unitary basis scramblings (`max_haar_err_155 < 10^{-15}`).
- **What Is Narrowed / Reclassified:**
  - Added two independent boolean flags (`include_real_tau_phase: bool` and `include_weil_zeta5_phase: bool`) to `build_flank_yukawa` and computed the full $2 \times 2$ factorial ablation table (`ablation_2x2_table`: `TT_both_on`, `TF_re_tau_only_no_weil`, `FT_weil_only_no_re_tau`, `FF_neither`).
  - Reclassified the old `case2_no_shear_phase` as the joint removal `FF_neither`: in the supplied schematic $3 \times 3$ texture, removing $\operatorname{Re}\tau$ alone (`FT_weil_only_no_re_tau`) leaves $|J_{CP}| = 8.365 \times 10^{-4} \ne 0$, and removing $\zeta_5$ alone (`TF_re_tau_only_no_weil`) leaves $|J_{CP}| = 2.094 \times 10^{-4} \ne 0$; only joint removal (`FF_neither`) gives $|J_{CP}| = 0$.
  - Explicitly typed `build_flank_yukawa` as `SUPPLIED_SCHEMATIC_3X3_TEXTURE_CONTROL_NOT_B1656_RESIDUE_OPERATOR`, noting that all four cells of the schematic texture satisfy $|V_{CKM} - V_{CKM}^T| = 0$ by construction and therefore do not test `P-716` / `R76-8` corner asymmetry (which requires the full `B1656`/`B1742` two-Higgs residue operator tested in Bridge 3 / Theorem XIII).
- **Discriminating Countercontrol (`countercontrol_f3_f4_ablation_and_texture_gate`):**
  - Asserts `removing_re_tau_alone_leaves_nonzero_j_cp_in_supplied_texture is True`, `removing_weil_zeta5_alone_leaves_nonzero_j_cp_in_supplied_texture is True`, `joint_removal_required_for_zero_j_cp_in_supplied_texture is True`, and `false_single_factor_necessity_claim_rejected is True`.

---

### `F5` (MEDIUM): Theorems 154 & 156 — Evidence Typing (Imported Numerical Pins vs First-Principles Recomputations) & Independence Scope

- **Exact Changed Source:**
  - `src/origin_axiom/toe_closure.py` lines `28508`–`28675` (`theorem154`) & lines `29207`–`29455` (`theorem156`)
  - `tests/test_elevation_operator_gate.py` lines `3045`–`3100` & `3156`–`3166`
- **What Survives Unchanged:**
  - `mpmath` 70-dps Newton root finding of the $k=1$ degree-8 Thurston shape polynomial (`mp_poly_resid < 10^{-40}`), symbolic `SymPy` proof of the 4-tetrahedron fan telescoping identity, 70-dps verification of the finite Kashaev sum $\langle 4_1 \rangle_5 = 46 + 2\sqrt{5}$ (`mp_kashaev_n5_err < 10^{-45}`), and `B1852`'s topological involution proof of $\operatorname{Re}\tau(\Sigma_0) = 0$.
- **What Is Narrowed / Reclassified:**
  - Added `evidence_typing_ledger` to `theorem154` and `theorem156` explicitly classifying `l_tube_snappy_hp_mp` (the 65-digit decimal string from SnapPy `ManifoldHP`) and the $\operatorname{Im}\tau(\Sigma_0)$ readings (`6.15` in `B1847`, `6.070` in `B1854`, `6.06526` in `chat1`) as `IMPORTED_NUMERICAL_PIN` / `IMPORTED_NUMERICAL_PIN_CONSISTENCY_CHECK`, distinct from `FIRST_PRINCIPLES_RECOMPUTATION` (`z2_mp`, `kashaev_n5`, `sympy_fan_telescoping`).
  - Explicitly typed Stage 29's internal verification gate as `INTERNAL_ALTERNATE_PRECISION_AND_SYMPY_CHECK_NOT_EXTERNAL_REFEREE`.
- **Discriminating Countercontrol (`countercontrol_f5_evidence_typing_gate`):**
  - Verifies `_classify_numeric_source` rejects promoting a literal decimal string (`is_literal_constant=True`) to `FIRST_PRINCIPLES_RECOMPUTATION` (`mutation_promoting_literal_pin_to_fresh_mesh_rejected = True`) and rejects promoting an in-module check to an external referee (`mutation_promoting_internal_gate_to_external_referee_rejected = True`).

---

### `F6` (MEDIUM): Theorems 147 & 149 — `THE_TAU_READOUT_RULE.md` / `B1857` Alignment, Symbolic All-$a$ $\Pi_2$ Proof, and Restricted Subfamily Scope

- **Exact Changed Source:**
  - `src/origin_axiom/toe_closure.py` lines `26759`–`26865` (`theorem147`) & lines `27050`–`27285` (`theorem149`)
  - `tests/test_elevation_operator_gate.py` lines `2920`–`2968` & `3131`–`3144`
- **What Survives Unchanged:**
  - Reflection stabilizer uniqueness on the 1D Teichmüller geodesic axis ($\operatorname{Im}\tau_{\text{apex}} = \sqrt{5}\phi \approx 3.618$ at $n=6$, `B1815`).
  - Exact closed forms $D_2 = \ln(5/4)$ and $D_6 = \ln(\phi^8/4)$, and exact conditional shares $97.68\%$ (Boltzmann $\exp(-D_n)$) and $31/32 = 96.875\%$ (move weight $2^{-n}$) within the restricted $\Pi_2$ single-run subfamily $\{6 + 5m\}$.
- **What Is Narrowed / Reclassified:**
  - In `theorem147`: Scoped `R5` strictly to `1D_TEICHMULLER_GEODESIC_AXIS_ONLY_NOT_3D_HYPERBOLIC_SIGMA0`, citing `docs/THE_TAU_READOUT_RULE.md` and `B1857` (`7ae616f3f` / `217e37c4f`), so the choice between the 1D Sol clock ($\operatorname{Im}\tau = 3.618$) and the 3D hyperbolic level surface $\Sigma_0$ ($\operatorname{Im}\tau = 6.065$) remains explicitly priced under `P-714`.
  - In `theorem149`: Added a symbolic `SymPy` proof over all $a \in \mathbb{Z}$ that $\det\begin{pmatrix} 2+a & 1 \\ 1 & 2 \end{pmatrix} = 2a + 3 \equiv 2(a - 1) \pmod 5 \equiv 0 \pmod 5 \iff a \equiv 1 \pmod 5$ (`sympy_all_a_pi2_det_proof_ok = True`), scoped $\Pi_2$ as `RATIONALE_NOT_DERIVED_PREMISE` per `B1855`/`B1856` and `chat1` `195e8f1bdd`, and labeled the $97.68\%$ / $31/32$ shares as `RESTRICTED_PI2_SUBFAMILY_6_PLUS_5M_NOT_FULL_WEAVE`.
- **Discriminating Countercontrols (`countercontrol_f6_tau_readout_rule_discrimination` & `countercontrol_f6_restricted_population_vs_full_weave`):**
  - Verifies $|\operatorname{Im}\tau(\Sigma_0) - \operatorname{Im}\tau_{\text{apex}}| > 2.4$ (`clock_vs_3d_surface_choice_still_priced_under_p714 = True`), proves that on the unconditioned single-run family $\{n \ge 2\}$ the $n=6$ Boltzmann share drops to $4.68\% < 5\%$ (`mutation_unconditioned_share_below_5_percent = True`), and shows that adding gapped $\Pi_2$ histories $(6, 1^g, 6)$ shifts the multi-run partition share by $> 5\%$ (`gapped_histories_shift_multi_run_normalization = True`).

---

## Verification Command & Exit Status

```bash
PYTHONPATH=src pytest tests/test_elevation_operator_gate.py -q
```
All 10 test suites in `tests/test_elevation_operator_gate.py` (including `test_five_phase_master_toe_closure` and `test_codex_f1_to_f6_repairs_and_discriminating_countercontrols`) pass with `exit 0`.
