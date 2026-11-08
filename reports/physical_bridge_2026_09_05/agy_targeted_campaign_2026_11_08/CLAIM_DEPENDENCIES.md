# Partial Claim Dependency Map (`CLAIM_DEPENDENCIES.md`) — `PARTIAL: PURE-H4-24 CLAIM ONLY`

**Scope Label:** **`PARTIAL: PURE-H4-24 CLAIM ONLY`**
**Date:** 2026-11-08
**Parent Task:** `AGY-00` ("Reuse inventory and common-model manifest")
**Released Microtask:** `AGY-00b1-r1` (released by physical review/dispatch commit `92cd5ea930e82046a643b804b02f3fad5e1a5f0e`, Coordination revision 5, `REVIEW_AGY_00B1_2BED_2026_11_08.md`, reviewing `2bed9909170d1d523890e90947d07494ecb986d2` against physical source baseline `30f348e15755a3c5a824e75d5ed6ba354e200bb3`)
**Question:** *"Precisely what supports the pure-h4 chi=0 reported 24 charged half-root coefficients, and which joins would be required before that could support a physical three-family claim?"*
**Evidence Status:** **UNREVIEWED AUTHOR SOURCE-DEPENDENCY MAP REVISION ONLY; ZERO NEW PHYSICAL DERIVATION, SCIENTIFIC IMPORT, COLLECTION, OR EXECUTION (`0 of 19` UNCHANGED).**

---

## 0. Pinned Source Receipts & Reading Notes Retained from `REVIEW_AGY_00A_R1_655_2026_11_08.md`

### 0.1 Declared Source File Pins Inspected for `AGY-00b1` / `AGY-00b1-r1`

| Commit Pin | Repository Path | SHA256 |
|---|---|---|
| `92cd5ea930e82046a643b804b02f3fad5e1a5f0e` | `reports/physical_bridge_2026_09_05/agy_targeted_campaign_2026_11_08/REVIEW_AGY_00B1_2BED_2026_11_08.md` | `b1a70fc686e8b949a83cb4db1d4934761d8ff7231466bc0d03e73673454ef7e4` |
| `92cd5ea930e82046a643b804b02f3fad5e1a5f0e` | `reports/physical_bridge_2026_09_05/agy_targeted_campaign_2026_11_08/START_HERE.md` | `ddcd53f54c98381e290d054b3ab0d8d61f0fdede0cc094bd82cd4e2e341f8568` |
| `92cd5ea930e82046a643b804b02f3fad5e1a5f0e` | `reports/physical_bridge_2026_09_05/agy_targeted_campaign_2026_11_08/TASKS.json` | `ffe70fb06ed34e438121323efbf58fca9c132b9e7ff6d0fd3d8f0940828f9057` |
| `92cd5ea930e82046a643b804b02f3fad5e1a5f0e` | `reports/physical_bridge_2026_09_05/relays/PHYSICAL_TO_AGY_2026-11-08_2BED_MAP_REVIEW_AND_BOUNDED_REPAIR.md` | `157c36b2dc62c82e627ea13dbf16aa50c1ff0049c6b3c4fbc33abb9ac150a6f8` |
| `30f348e15755a3c5a824e75d5ed6ba354e200bb3` | `reports/physical_bridge_2026_09_05/word_architecture_audit_2026_10_17/COUPLED_UP_SECTOR_PARABOLIC_COUNT_2026_11_08.md` | `477743caf7f2edc91117ed9f7ef24efcb834c5a8968bfd19ffc46865d75d9ff9` |
| `d1b2303969050925d4b548ed21ec862208107b9f` | `reports/physical_bridge_2026_09_05/agy_targeted_campaign_2026_11_08/START_HERE.md` | `fc0c6b6bf65c6079ada3da05e0de6a65307819a44eb7e97baa4d9a0d80b4a7d5` |
| `d1b2303969050925d4b548ed21ec862208107b9f` | `reports/physical_bridge_2026_09_05/agy_targeted_campaign_2026_11_08/RUN_TICKET_AGY_00B1.md` | `25db6209bc513b93c8e213a5796dc6d85133979a4ada95e0247c382c01e05451` |
| `d1b2303969050925d4b548ed21ec862208107b9f` | `reports/physical_bridge_2026_09_05/agy_targeted_campaign_2026_11_08/REVIEW_AGY_00A_R1_655_2026_11_08.md` | `c6942f5f1516b7600765bcafafb991f4ec35375dda9f345367ae3b255aebb458` |
| `d1b2303969050925d4b548ed21ec862208107b9f` | `reports/physical_bridge_2026_09_05/agy_targeted_campaign_2026_11_08/TASKS.json` | `75337121ef917c905a8368396797c157133fdfe430907558099a3a5b641fcf7f` |
| `d1b2303969050925d4b548ed21ec862208107b9f` | `reports/physical_bridge_2026_09_05/relays/PHYSICAL_TO_AGY_2026-11-08_655_INTAKE_ACCEPTED_RELEASE_00B1.md` | `8c7539a51589f103b4b084544199ab4aa87552fcd563acfdb2ef5c00449f5e64` |
| `6fc5cdd0d05e8072f6a2a64f267772d06ee94976` | `reports/physical_bridge_2026_09_05/PROGRESS_SINCE_MAIN_217E_2026_11_08.md` | `d61af22b9e5388c278c2e6909ed750f2390ca4ba3e3f005345a3a939148c546c` |
| `6552aec6894a4a94a2ced785ac3af8c25f801ba8` | `reports/physical_bridge_2026_09_05/agy_targeted_campaign_2026_11_08/MODEL_MANIFEST.md` | `811956e0ffc5ca9f141c57e6eb5e98bc576aa5b8e7fe18909c4fc2cd9136ebdb` |
| `dd7490203c55bae043585f594af5a13afe634fa7` | `reports/physical_bridge_2026_09_05/weave_curved_action_2026_10_08/PROOF.md` | `c505823ce2b934b9737780acf3d6bbbeeb8482613b7ecc76a2ece58b1c2ebc4f` |
| `dd7490203c55bae043585f594af5a13afe634fa7` | `reports/physical_bridge_2026_09_05/weave_physical_mass_2026_10_08/PROOF.md` | `04fbb6b7ddc23fe2ae56aa24f3df6e9a710f6278363213b8a509b06ace83ef8d` |
| `dd7490203c55bae043585f594af5a13afe634fa7` | `reports/physical_bridge_2026_09_05/word_architecture_audit_2026_10_17/ELECTROWEAK_TWO_TRIPLE_PHYSICAL_KERNEL.md` | `871529dd81603e1a70126f6ee518ae5c2758c107cf7e9fff62ae96f646a0813f` |
| `dd7490203c55bae043585f594af5a13afe634fa7` | `reports/physical_bridge_2026_09_05/word_architecture_audit_2026_10_17/COUPLED_QUATERNION_STATIONARY_BUNDLE_AND_CUSP_LAW.md` | `221a7cd2dce2ff7dec0b135c348b7bb52e15bc27e5563d420756fbe31f9978a1` |
| `dd7490203c55bae043585f594af5a13afe634fa7` | `reports/physical_bridge_2026_09_05/word_architecture_audit_2026_10_17/CONFINED_HALF_ROOT_SECTOR_AND_SURVIVING_CONTINUUM.md` | `8436811ae3529f7fa78337a428f1e9c2d8af1414860fb2512db772a20879e4c4` |
| `dd7490203c55bae043585f594af5a13afe634fa7` | `reports/physical_bridge_2026_09_05/word_architecture_audit_2026_10_17/QUATERNION_SECTOR_INDEX_AND_WEAK_CURRENT_DUTY.md` | `11ddfae1996036673dc2bc08ec9b1ef26f92a4a91df98da379d539a529f93fc6` |
| `dd7490203c55bae043585f594af5a13afe634fa7` | `reports/physical_bridge_2026_09_05/word_architecture_audit_2026_10_17/FULL_E8_COMPENSATOR_LIFT_AND_REGISTER_TRANSPORT.md` | `6012816683f17ac83e7d3bdb4f6d8b987ec8155ee2caa09ce651dbf0b194ed4c` |
| `dd7490203c55bae043585f594af5a13afe634fa7` | `reports/physical_bridge_2026_09_05/word_architecture_audit_2026_10_17/PIN2_COMPENSATOR_COHERENCE_AND_ELECTROMAGNETIC_PHASE.md` | `fc67d4446b11f54c731b7e7aac56b496e501d5fa397040363de6c8074909a3b9` |
| `dd7490203c55bae043585f594af5a13afe634fa7` | `reports/physical_bridge_2026_09_05/word_architecture_audit_2026_10_17/COUPLED_HALF_ROOT_KERNEL_AND_CORE_LIFT_SENSITIVITY.md` | `789adf7544bf5c679305aa8b9ba7525b6375155b026c839e01c34c281be23875` |
| `dd7490203c55bae043585f594af5a13afe634fa7` | `reports/physical_bridge_2026_09_05/word_architecture_audit_2026_10_17/WEAK_CURRENT_GRADING_AND_DISCRETE_CHARGED_VECTORS.md` | `7ac2e6cc08a82d3c4ab34fbae52596da3b6171c48985b7c22729802e5f65db8e` |
| `dd7490203c55bae043585f594af5a13afe634fa7` | `reports/physical_bridge_2026_09_05/word_architecture_audit_2026_10_17/CENTRALIZER_KERNEL_WITH_THRESHOLD_CONTINUUM.md` | `a19e2c6c6b4faa0db3bbe16402499314f259a8db0ce590b0bcaf3ac4130970f5` |
| `dd7490203c55bae043585f594af5a13afe634fa7` | `reports/physical_bridge_2026_09_05/word_architecture_audit_2026_10_17/verification_transport_end_2026_11_04/checks.py` | `cb3d46f2a51c101f064116bd6d63998e6a8bc1c5e99e73ae1cb5bbf12f7d1e9b` |
| `3e58425f1e6560d9f078f306e724ed264d41884f` | `reports/physical_bridge_2026_09_05/word_architecture_audit_2026_10_17/verification_coupled_half_root_kernel_2026_11_07/checks.py` | `e72063d7b2a6b3ac8a6f83db4df693e79fec5d3a0f5b91fdf4931496567276f0` |
| `6290484f286cf82a58131acd99ec156339f1e3da` | `reports/physical_bridge_2026_09_05/word_architecture_audit_2026_10_17/verification_coupled_half_root_kernel_2026_11_07/review/INDEPENDENT_PROOF_CODE_REVIEW_2026_11_07.md` | `00fba6daf441dea71f9be642ac5e049e6b27de1f20ac25729a94d556631a2f4c` |
| `6f35dfefdabc9a6f932b27699cd02cb6863623cf` | `reports/physical_bridge_2026_09_05/word_architecture_audit_2026_10_17/verification_transport_joint_2026_11_05/review/INDEPENDENT_EXECUTION_READINESS_2026_11_07.md` | `e232654dc16e8b2a65d6b73810648044a020b5efa422cb4347e59fe6c6b3957d` |
| `1704f9e4153dea79d4d2ff2ea33cbe029fcb9481` | `reports/physical_bridge_2026_09_05/foundation_selection_2026_11_07/DISCRIMINANT_COVER_PERIPHERAL_AND_ORDER_THREE_WILSON_2026_11_08.md` | `5c056ae0d1a4cbc6ead0a9c1efa9f32719a1d013a290894fa70d5f31f2c66d46` |
| `dd7490203c55bae043585f594af5a13afe634fa7` | `reports/physical_bridge_2026_09_05/SM3_AND_GRAVITY_COMPLETION_CHECKLIST_2026_11_08.md` | `b3a04ab794beab0fce31b4365a011d2c3353f03932d22eef34469fd59b71729f` |
| `21b293e87ff09fd64911267e9b4aa447fbfab2b9` | `src/origin_axiom/weave_unification_bridge.py` | `73bb65f3c09a6511b9bbcfd3666c7e945ffd39aeab61fe23f589b91113d759c6` |
| `51a5ffdad70b6a6208a5063f0dc4237a7fdf4190` | `tests/test_sealed_validator_negative_controls.py` | `cba9748eb580ca4ea742bfad8ac622685d7b92211c330d93fcc4666253949cca` |
| `51a5ffdad70b6a6208a5063f0dc4237a7fdf4190` | `docs/audit/FLOW_JOURNAL_2026_11_08_WALLS_F1_F4_AND_OPEN_O1_O2.md` | `6a8b177083b463eb727f7c823f01242dc37877e0134b24a448db74845c346995` |
| `217e37c4f37bd80998f3c3e10cad358023f58114` | `GENESIS.md` | `ec8c3dba05a5c947416a18952bc40f99a32af5135c87987c6f7e6236bc34bad4` |

### 0.2 Four Reading Notes Retained from `REVIEW_AGY_00A_R1_655_2026_11_08.md`

1. **Validator `F4` branch and producer $6\times 6$ weak tensor:** The `F4` branch of `validate_bridge_candidate` in `tests/test_sealed_validator_negative_controls.py` (`51a5ffdad70b6a6208a5063f0dc4237a7fdf4190`, lines 148–172; there is no `TestF4WeakVertexNegativeControls` class) reads three reported eigenvalues (`g_4slot_3mode_eigenvalues`), a Haar error (`haar_50_trial_su2L_u3fam_max_err`), and a nonunitary drift (`non_unitary_negative_control_drift`); the producer's later tensor in `verify_coupled_2d_surface_and_3sheet_cover_bvp` (`src/origin_axiom/weave_unification_bridge.py` at `21b293e87ff09fd64911267e9b4aa447fbfab2b9`, line 5262) is $6\times 6$ (`v_weak_6x6 = np.kron(tau_plus, g_mat_3)`). The missing mode/domain/generator-witness diagnosis stands.
2. **Parent D-term $g_6^{-2}$ normalization:** The manifest's D-term expression (`MODEL_MANIFEST.md` §1.2) omits the common $g_6^{-2}$ factor if read as the physical $V_D$. The parent (`weave_curved_action_2026_10_08/PROOF.md`, `c505823ce2...`) writes $g_6^2 V$ as its displayed integral. Treat the manifest expression as that reduced density and retain the parent's overall factor for any physical normalization.
3. **Coordinate change $\det = -1$ vs. flavour holonomies $\det = +1$:** A fixed coordinate change $(q,r) \mapsto ((q+r)/\sqrt{2}, (q-r)/\sqrt{2})$ transports $\varepsilon$ and the degree-two frame with its determinant $-1$. The flavour holonomies $\rho(F_i) = i\sigma_x$ and $\rho(F_k) = \operatorname{diag}(i,-i)$ themselves retain determinant $+1$ under conjugation. Do not read the manifest's combined-factor wording as cancellation of every frame sign or a new global flavour symmetry. Use the exact original complex when computing.
4. **Unreviewed status of the pure-$h_4$ 24-mode count:** The pure-$h_4$ 24-mode result is still an unreviewed reported coefficient count. Matching its table to code or file hashes does not prove the global contraction, physical identification, full roster, or SM3.

---

## 1. Four-Layer Separation Required Before Tracing Nodes

Per `RUN_TICKET_AGY_00B1.md` and `REVIEW_AGY_00B1_2BED_2026_11_08.md`, a reference to code is **not** simultaneous proof of all four mathematical layers below:

- **Layer L1 — Finite Fibre / Reduced-Matrix Construction:** Construction of the 32-component $D_5$ Fock spinor, chirality split $32 = 16_+ \oplus 16_-$, unitary $16\times 16$ joint weight frame (`p,q in {0,1,2,3}^2`), fibre Koszul differentials $d_0: \mathbb{C}^{16} \to \mathbb{C}^{32}$ and $d_1: \mathbb{C}^{32} \to \mathbb{C}^{16}$ with harmonic representatives of dimensions $(1,2,1)$ at indices $(0, \{12,19\}, 15)$, and restriction of the combined flavour-gauge core holonomies $(A, D, B=DA)$ to those $(1,2,1)$ representatives.
- **Layer L2 — Complete-Cusp Cohomology Count:** Extension of the local fibre chain homotopy $h$ by finite group averaging and Dolbeault totalization to the complete differential graph domain on $\Sigma_{1,1} = E_\tau \setminus \{p\}$ with the hyperbolic cusp metric $g = \Omega^2(dx^2 + dy^2)$, antiperiodic peripheral transition on all four slots in $128$, and strict radial $L^2$ pole bounds $n < a/2$ (or $n = a/2$ if $a < 1$) giving divisor degrees $(-2, 0, 2)$ for $S^{-3}, S^1, S^5$ and total cohomology tuple $(h^0, h^1, h^2, h^3)$.
- **Layer L3 — Physical Mass-Map Identification:** Identification of the complete-domain Dolbeault/Koszul cohomology $(h^1 + h^3)$ and $(h^0 + h^2)$ with the physical 4-slot left-handed Weyl fermion kernel $\ker M$ and adjoint kernel $\ker M^\dagger$ of $M = U_{\text{out}} T U_{\text{in}}$ on the actual weighted Hilbert spaces $(\Omega^2, 1/2, \Omega, \Omega)$ with trace-dual conjugate target.
- **Layer L4 — Actual Family & Physical Interaction Interpretation:** Completion of the full 248 $E_8$ fermion roster (including integer-root $(10,6)$ up-type quarks with $Q = \pm 2/3$, $(1,15) \oplus (45,1)$ neutral/adjoint sectors, and the $A_3$ spin threshold continuum), determination of chiral vs. vector-like structure under weak interactions, and computation of the cross-grading $128 \leftrightarrow 120$ weak current $g_{mn}(w)$ from actual global 4-slot solutions of $M\psi = 0$.

---

## 2. Twelve Principal Dependency Nodes (`N01`–`N12`)

### Node `N01` — Common 6D Curved Action, Kinetic Weights, and 4-Slot Mass Map $M = U_{\text{out}} T U_{\text{in}}$
1. **Exact Source & Concrete Claim:**
   - Commit `dd7490203c55bae043585f594af5a13afe634fa7`:
     - `reports/physical_bridge_2026_09_05/weave_curved_action_2026_10_08/PROOF.md` (§1–§3, SHA256 `c505823ce2...`);
     - `reports/physical_bridge_2026_09_05/weave_physical_mass_2026_10_08/PROOF.md` (§1–§4, SHA256 `04fbb6b7dd...`).
   - **Claim:** Defines the 6D gauge-Higgs-fermion curved action on $\mathbb{R}^{1,3} \times \Sigma$, kinetic density weights $G = \operatorname{diag}(\Omega^2, 1/2, \Omega, \Omega)$ on the 4 left-handed Weyl slots $(\lambda, a_{\bar{z}}, u, v)$, D-term potential (written as $g_6^2 V$ in the parent integral, so the physical $V_D$ carries the common $g_6^{-2}$ factor per Reading Note 2), and the isometric 4-slot mass operator factorization $M = U_{\text{out}} T U_{\text{in}}$ on the complete maximal graph domain.
2. **Evidence Type:** Source definition and classical parent-branch proof (Layer L3 foundation).
3. **Hypotheses Consumed:** Supplied compact $\mathfrak{e}_8$ with trace inner product $\kappa(X,Y) = -\operatorname{tr}(\operatorname{ad}_X \operatorname{ad}_Y)$, supplied complete punctured metric $g = \Omega^2(dx^2 + dy^2)$, supplied symplectic flavour bundle $(F, \varepsilon_F)$, and complete differential graph domains.
4. **What Follows vs. What Does Not:**
   - *Follows:* Fixes the exact 4-slot kinetic norms, gauge-covariant differential rows, and Hodge-isometry structure required by any zero-mode or weak-current claim. Also fixes the constant coordinate change $(q,r) \mapsto ((q+r)/\sqrt{2}, (q-r)/\sqrt{2})$ with $\det = -1$ transporting $\varepsilon$ and the degree-2 slot (Reading Note 3).
   - *Does not follow:* Does not specify the core/cusp holonomy lift, does not count kernels in any specific $E_8$ sector, and does not create a new global flavour symmetry from the $\det = -1$ coordinate change.

---

### Node `N02` — Balanced Two-Triple $D_5 \subset E_8$ Stationary State, Embedded $D_5 + A_3$ Root Branching, and Local Fibre Koszul Retraction
1. **Exact Source & Concrete Claim:**
   - Commit `dd7490203c55bae043585f594af5a13afe634fa7`:
     - `reports/physical_bridge_2026_09_05/word_architecture_audit_2026_10_17/ELECTROWEAK_TWO_TRIPLE_PHYSICAL_KERNEL.md` (§1–§4, SHA256 `871529dd81...`);
     - `reports/physical_bridge_2026_09_05/word_architecture_audit_2026_10_17/COUPLED_QUATERNION_STATIONARY_BUNDLE_AND_CUSP_LAW.md` (§1–§4, SHA256 `221a7cd2dc...`);
     - `reports/physical_bridge_2026_09_05/word_architecture_audit_2026_10_17/FULL_E8_COMPENSATOR_LIFT_AND_REGISTER_TRANSPORT.md` (§2–§3, SHA256 `6012816683...`).
   - **Claim (Corrected per `REVIEW_AGY_00B1_2BED_2026_11_08.md` Item 1):** On $\Sigma_{1,1} = E_\tau \setminus \{p\}$ (`Carrier C0`), the balanced stationary state $\Phi_0 = (\hat{q}, \hat{r}) = (E, G)/(2\sqrt{2}\ell)$ embeds two commuting principal $\mathfrak{su}(2)$ triples $E_\pm = \frac{1}{2}(E \pm G)$ into compact $D_5 \subset E_8$, decomposes the root/Lie representation under the embedded $D_5 + A_3$ subalgebra as
     $$248 = (45,1) \oplus (1,15) \oplus (10,6) \oplus (16,4) \oplus (\overline{16},\overline{4}),$$
     and constructs the bounded local fibre Koszul chain homotopy $\delta h + h\delta = I - i p$ onto surviving line powers $(S^{-3}, S^1 \oplus S^1, S^5)$ on each $16 = V_{3/2} \otimes V_{3/2}$. In the full $E_8$ representation (`FULL_E8_COMPENSATOR_LIFT_AND_REGISTER_TRANSPORT.md` §3 and `PIN2_COMPENSATOR_COHERENCE_AND_ELECTROMAGNETIC_PHASE.md` §5), the central elements of the simply connected compact $\operatorname{Spin}(10)$ subgroup and the $A_3$ electromagnetic phase satisfy the order-4 full-centre identity $C_{D_5} h_4^2 = 1$ in $E_8$ ($C_{D_5}^2 = \mathrm{Zeta}$, $C_{D_5}^4 = 1$, and on the defining $A_3$ four, $h_4^2 = -i I_4$, so $C_{D_5}^{-1} = h_4^2$); no unearned global subgroup quotient label $\operatorname{Spin}(10) \times \operatorname{SU}(4)/\mathbb{Z}_2$ is asserted from the Lie module branching alone.
2. **Evidence Type:** Imported authored argument (classical parent-branch proof for the two-triple Koszul complex; unreviewed post-`8cad267b4` hand derivation for the coupled quaternion stationary bundle; 13-method packet `bda89f04a94d09217551cef96056f375b21c260b` has independent source-complete execution-readiness approval at `6f35dfefdabc9a6f932b27699cd02cb6863623cf`, still **UNRUN**; Layer L1 & peripheral setup).
3. **Hypotheses Consumed:** Balanced stationary background $\Phi_0$, quaternion flavour holonomy $\rho(a) = F_i, \rho(b) = F_j$ with peripheral $\operatorname{Hol}_F(c) = [F_i, F_j] = -I_2$, and embedded $D_5 + A_3 \subset \mathfrak{e}_8$ root decomposition with full-centre relation $C_{D_5} h_4^2 = 1$.
4. **What Follows vs. What Does Not:**
   - *Follows:* Establishes the 8 half-root $A_3$ coefficient records ($1_{+1} \oplus 3_{-1/3}$ in $(16,4)$ and $1_{-1} \oplus \bar{3}_{+1/3}$ in $(\overline{16},\overline{4})$), the surviving fibre Koszul representatives of dimensions $(1,2,1)$, and the flat gauge compensator commutator $[A,B] = \mathrm{Zeta}\,P$.
   - *Does not follow:* Does not establish a bare $\mathbb{Z}_2$ global subgroup quotient, does not fix the flat core transport on the middle Koszul lines $S^1 \oplus S^1$, and does not count global $L^2$ zero modes.

---

### Node `N03` — Flat vs. Total Peripheral Cusp Law (`\mathrm{Zeta}\,P` vs. `\mathrm{Zeta}`), Confined $128$ Sector, $A_3$ Continuum, and $\operatorname{ind} M_R = 0$
1. **Exact Source & Concrete Claim:**
   - Commit `dd7490203c55bae043585f594af5a13afe634fa7`:
     - `reports/physical_bridge_2026_09_05/word_architecture_audit_2026_10_17/COUPLED_QUATERNION_STATIONARY_BUNDLE_AND_CUSP_LAW.md` (§4–§5, Eq. (3), SHA256 `221a7cd2dc...`);
     - `reports/physical_bridge_2026_09_05/word_architecture_audit_2026_10_17/CONFINED_HALF_ROOT_SECTOR_AND_SURVIVING_CONTINUUM.md` (§1–§4, SHA256 `8436811ae3...`);
     - `reports/physical_bridge_2026_09_05/word_architecture_audit_2026_10_17/QUATERNION_SECTOR_INDEX_AND_WEAK_CURRENT_DUTY.md` (§1–§5, Eqs. (1)–(5), SHA256 `11ddfae199...`).
   - **Claim (Corrected per `REVIEW_AGY_00B1_2BED_2026_11_08.md` Item 2):**
     1. In the extending-spin cusp frame (`COUPLED_QUATERNION_STATIONARY_BUNDLE_AND_CUSP_LAW.md` §4), $\mathrm{Zeta}\,P$ is the **flat** gauge compensator commutator ($[A,B] = \mathrm{Zeta}\,P$). The spin-induced gauge connection $A_{\text{spin}} = s H/2$ contributes an additional peripheral factor $P = \exp(i\pi H/2)$ with $P^2 = 1$, so the **total gauge peripheral** is
        $$\operatorname{Hol}_{G,\text{total}}(c) = P(\mathrm{Zeta}\,P) = \mathrm{Zeta}.$$
     2. Consequently, the scalar and form Weyl slots $(\lambda, a_{\bar{z}})$ see $\operatorname{Ad}(\mathrm{Zeta})$ directly (`+1` on $120$, `-1` on $128$). The spin Weyl slots $(u, v)$ also carry the extending cusp spin sign `-1` and the flat flavour commutator $[F_i, F_j] = -I_2$ (`-1`), which cancel each other (`(-1)(-1) = +1`), so $(u, v)$ likewise see $\operatorname{Ad}(\mathrm{Zeta})$. All four Weyl slots $(\lambda, a_{\bar{z}}, u, v)$ therefore see **$+1$ (periodic, integer angular frequencies) on $120$** and **$-1$ (antiperiodic, half-integer angular frequencies) on $128$**.
     3. Because all four slots in $128$ have peripheral transition $-1$, the $128$ half-root sector has a discrete Fredholm spectrum with net unbroken-$U(3)$ index $\operatorname{ind} M_R = 0$ for every lift and marking, whereas the $A_3 = (1,15) \subset 120$ centralizer retains an essential spin threshold continuum reaching $0$.
2. **Evidence Type:** Imported authored argument (included in the 13-method packet `bda89f04a94d09217551cef96056f375b21c260b` with independent source-complete execution-readiness approval at `6f35dfefdabc9a6f932b27699cd02cb6863623cf`, **UNRUN**; Layer L2/L3 Fredholm & index foundation).
3. **Hypotheses Consumed:** Extending cusp spin $\operatorname{Hol}_S(c) = -1$, spin-induced gauge peripheral $P = \exp(i\pi H/2)$, flat flavour peripheral $[F_i, F_j] = -I_2$, flat gauge commutator $[A,B] = \mathrm{Zeta}\,P$ combining with $P$ to give total gauge peripheral $\mathrm{Zeta}$ across all four slots, and complete hyperbolic cusp domain.
4. **What Follows vs. What Does Not:**
   - *Follows:* Every $128$-sector representation $R$ has antiperiodic boundary behavior across all four slots $(\lambda, a_{\bar{z}}, u, v)$ and a finite-dimensional $L^2$ kernel with $\dim\ker M_R = \dim\ker M_R^\dagger$ ($\operatorname{ind} M_R = 0$).
   - *Does not follow:* $\operatorname{ind} M_R = 0$ does **not** imply $\ker M_R = \{0\}$, does **not** compute the individual kernel dimensions ($16$, $18$, or $24$), and does **not** decide whether the theory is weak-chiral or vector-like (§5 of `11ddfae199...`).

---

### Node `N04` — Full Compact $E_8$ Bare Compensator Lift ($A_{\text{bare}}^4 = \mathrm{Zeta}$) vs. Continuous-$\operatorname{Pin}_2$ Coherent Lifts ($\tilde{A} = A_{\text{bare}} h_4$ and $\mathrm{Zeta}\tilde{A}$)
1. **Exact Source & Concrete Claim:**
   - Commit `dd7490203c55bae043585f594af5a13afe634fa7`:
     - `reports/physical_bridge_2026_09_05/word_architecture_audit_2026_10_17/FULL_E8_COMPENSATOR_LIFT_AND_REGISTER_TRANSPORT.md` (§3–§6, SHA256 `6012816683...`);
     - `reports/physical_bridge_2026_09_05/word_architecture_audit_2026_10_17/PIN2_COMPENSATOR_COHERENCE_AND_ELECTROMAGNETIC_PHASE.md` (§4–§6, Eqs. (7)–(9), SHA256 `fc67d4446b...`).
   - **Claim:** Lifting $A_{\text{vec}} = (-iN)\exp(-i\pi H/4)$ to simply connected $\operatorname{Spin}(10) \subset E_8$ via $x = (1/4, 0, -1/4, -1/2, -3/4)$ yields $A_{\text{bare}}^2 = C_{D_5}^{-1}P$ and $A_{\text{bare}}^4 = \mathrm{Zeta} \neq 1$ (`Model M1`), which fails the reflection identity $\tilde{A}^2 = K_\pi = D^2$ on the $128$ half-roots. Multiplying by $h(\theta) = \exp(i\theta Q_{\text{em}})$ and requiring $h(\theta)^2 = C_{D_5}^{-1}$ on the $A_3$ defining $4$ fixes $\theta \equiv 3\pi/4 \pmod{3\pi}$, leaving two continuous-$\operatorname{Pin}_2$ coherent lifts $\tilde{A} = A_{\text{bare}}h_4$ (`correction = 0`) and $\mathrm{Zeta}\tilde{A}$ (`correction = 1`) with $h_4 = \exp(i\frac{3\pi}{4}Q_{\text{em}})$.
2. **Evidence Type:** Imported authored conditional hand derivation (8-method transport controls included in `bda89f04a94d09217551cef96056f375b21c260b`, reviewed for source-complete execution readiness at `6f35dfefdabc9a6f932b27699cd02cb6863623cf`, **UNRUN**; Layer L1 group/compensator datum).
3. **Hypotheses Consumed:** Conditional requirement that the core gauge compensation factor through the continuous stabilizer $\operatorname{Pin}_{2,x} \to E_8$ (`\tilde{A}^2 = K_\pi`) using the unbroken electromagnetic generator $Q_{\text{em}} = \frac{2}{3}(e_1 + e_2 + e_3)$.
4. **What Follows vs. What Does Not:**
   - *Follows:* Fixes the exact phase factor $h_4 = \exp(2\pi i \cdot \frac{3}{8} Q_{\text{em}})$ (and its $\mathrm{Zeta}$-partner) on every $E_8$ root/weight space, so that on highest spinor weight $v_{\text{top}}$, $\tilde{A}$ has eigenvalue $\alpha$ satisfying $\alpha^2 = 1$ (whereas $A_{\text{bare}}$ has $\alpha_{\text{bare}}^4 = -1$).
   - *Does not follow:* Does not prove that every allowed free-group register lift must factor through continuous $\operatorname{Pin}_2$ (arbitrary independent central $\mathrm{Zeta}$ signs $(s_a, s_b) \in \{\pm 1\}^2$ remain allowed in the free based group $F_2$), and does not by itself eliminate the independent Wilson input $\chi$.

---

### Node `N05` — Equivariant Complete-Domain Reduction and $16$-Bare / $18$-Corrected Half-Root Left-Kernel Formula (`Model M1` and `Model M2a/M2b`)
1. **Exact Source & Concrete Claim:**
   - Commit `dd7490203c55bae043585f594af5a13afe634fa7`, `reports/physical_bridge_2026_09_05/word_architecture_audit_2026_10_17/COUPLED_HALF_ROOT_KERNEL_AND_CORE_LIFT_SENSITIVITY.md` (§2–§5, Eqs. (1)–(4), SHA256 `789adf7544...`);
   - Commit `6290484f286cf82a58131acd99ec156339f1e3da`, `reports/physical_bridge_2026_09_05/word_architecture_audit_2026_10_17/verification_coupled_half_root_kernel_2026_11_07/review/INDEPENDENT_PROOF_CODE_REVIEW_2026_11_07.md` (SHA256 `00fba6daf4...`, reviewing `3e58425f1e6560d9f078f306e724ed264d41884f`).
   - **Claim:** On each of the 8 half-root records $R$, the combined flavour-gauge core holonomies $(A, D, B=DA)$ act on the $(1,2,1)$ fibre Koszul cohomology representatives by $(\alpha, \alpha\sigma_x, -\alpha)$ for $A$ and $(1, I_2, 1)$ for $D$. Averaging the local homotopy $h$ over the finite combined transition image passes to the complete differential graph domain and yields
     $$\dim\ker M_R = 2 + \delta(\eta L_+) + \delta(\eta L_-), \qquad L_\pm: (\pm\alpha\chi_R(a), \pm\alpha\chi_R(b)),$$
     where $2 = h^1(\Sigma_{1,1}, S^{-3}\otimes L_0)$ from divisor degree $-2$ (trace-dual $h^0$ of degree $+2$) and $\delta(\eta L_\pm) \in \{0,1\}$ counts triviality of the degree-$0$ middle lines $S^1 \otimes L_\pm$. With odd spin $\eta = \mathcal{O}$ (`spin = (1,1)`) and the old nontrivial order-3 Wilson character $\chi_3$ retained:
     - Bare lift (`Model M1`, $\alpha^4 = -1$): $\delta = 0$ on all 8 records $\implies 16$ left-kernel coefficient dimensions ($2$ per record);
     - Coherent lifts $\tilde{A}, \mathrm{Zeta}\tilde{A}$ (`Model M2a/M2b`, $\alpha^2 = 1$): $\delta = 0$ on the 6 colour-triplet records ($\chi_R = \chi_3^{\pm 1} \neq 1$) and $\delta(\eta L_+) + \delta(\eta L_-) = 1$ on the 2 colour-singlet records ($\chi_R = 1$) $\implies 18 = 6\times 2 + 2\times 3$ left-kernel coefficient dimensions.
2. **Evidence Type:** Independent review at its exact scope (`6290484f286cf82a58131acd99ec156339f1e3da` supports the conditional hand proof of Layers L1–L3 for `Model M1` ($16$) and `Model M2a/M2b` ($18$) with $\chi_3 \neq 0$, while marking the 9-method code package `3e58425f1e6560d9f078f306e724ed264d41884f` `REVISION REQUIRED / UNRUN / NOT ADMITTED` due to `V1`).
3. **Hypotheses Consumed:** All hypotheses of `N01`–`N04`, plus conditional odd spin identification $\eta = \mathcal{O}$ (`(1,1)` in the elliptic marking), supplied nontrivial order-3 Wilson character $\chi_3$ on $A_3$, and independent central signs $(s_a, s_b) = (1,1)$ via the continuous-$\operatorname{Pin}_2$ prescription.
4. **What Follows vs. What Does Not:**
   - *Follows:* Independently supports the conditional reduction formula Eq. (3) and the $16$ bare / $18$ corrected coefficient counts at $\chi_3 \neq 0$.
   - *Does not follow:* Explicitly **excludes** the pure-$h_4$, $\chi = (0,0)$ 24-mode alternative (`PROGRESS_SINCE_MAIN_217E_2026_11_08.md` §1: *"The pure-h4 chi=0 24-mode alternative is outside this review"*), and explicitly states that coefficient dimensions are **not** family counts.

---

### Node `N06` — Parent Symbolic Cohomology Producer (`spinor_complex`, `corrected_reduced`, `pole_degree`, `line_h0`, `total_cohomology`)
1. **Exact Source & Concrete Claim:**
   - Commit `3e58425f1e6560d9f078f306e724ed264d41884f` (and `dd7490203c55bae043585f594af5a13afe634fa7`):
     - `reports/physical_bridge_2026_09_05/word_architecture_audit_2026_10_17/verification_coupled_half_root_kernel_2026_11_07/checks.py` (lines 48–190 and 284–355, SHA256 `e72063d7b2...`);
     - `reports/physical_bridge_2026_09_05/word_architecture_audit_2026_10_17/verification_transport_end_2026_11_04/checks.py` (lines 58–145, SHA256 `cb3d46f2a5...`).
   - **Claim:** Implements in SymPy the exact 32-component Fock spinor (`creators`, `spin_lie`), the $16\times 16$ unitary joint weight frame and $(1,2,1)$ harmonic representatives at indices `(0, (12, 19), 15)` (`spinor_complex`), the 8 half-root records (`coefficient_records`), the reduced cohomology actions `corrected_reduced(record, correction, signs=(1,1))`, the cusp pole bound `pole_degree(a)` returning `(-2, 0, 2)` for `a in (-3, 1, 5)`, and `total_cohomology(record, correction, chi=(1,0), spin=(1,1), signs=(1,1))` returning `(h0[0], h1[0]+h0[1], h1[1]+h0[2], h1[2])`. At lines 308–310, `test_actual_wilson_and_spin_line_triviality_population` also includes the finite countercontrol:
     ```python
     if abs(record["charge"]) == Fraction(1, 3):
         a, b = corrected_reduced(record, 0)
         self.assertEqual(fixed_columns((a[1], b[1])).cols, 1)
     ```
     showing that if the order-3 Wilson character is omitted on a charge-$\pm 1/3$ triplet record at `correction = 0`, `(a[1], b[1]) = (alpha * sigma_x, alpha * sigma_x)` with $\alpha^2 = 1$ fixes one column of the 2D middle Koszul space.
2. **Evidence Type:** Source definition (unrun SymPy producer/test code inspected by hand/AST in `6290484f286cf82a58131acd99ec156339f1e3da`; package status is `REVISION REQUIRED / UNRUN / NOT ADMITTED`; Layer L1 finite algebra + Layer L2 formula encoding).
3. **Hypotheses Consumed:** Finite $D_5$ matrices `ep, em, hp, hm`, torus weights `x = (1/4, 0, -1/4, -1/2, -3/4)`, and the formula `line_h0` encoding Eq. (3) of `N05`.
4. **What Follows vs. What Does Not:**
   - *Follows:* Provides the exact upstream symbolic algorithm from which AGY's `_total_cohomology` and `_cohom_count_bvp` in `weave_unification_bridge.py` (`N07`) were translated line-by-line into NumPy.
   - *Does not follow:* Because `line_h0` is a finite algebraic encoding of the divisor-degree formula `(-2, 0, 2)`, calling `total_cohomology` in code tests only Layer L1 matrix eigenvalues plus the encoded Layer L2 integer rule; it does not independently execute a PDE/Fredholm solver on $\Sigma_{1,1}$ or prove Layer L3/L4.

---

### Node `N07` — AGY NumPy Port of `_total_cohomology(rec, 0, chi=(0,0))` Reporting $24 = 8 \times 3$ Half-Root Coefficients (`Model M3a/M3b` on Base Carrier `C0`)
1. **Exact Source & Concrete Claim (Corrected per `REVIEW_AGY_00B1_2BED_2026_11_08.md` Item 4):**
   - Commit `21b293e87ff09fd64911267e9b4aa447fbfab2b9`, `src/origin_axiom/weave_unification_bridge.py` (SHA256 `73bb65f3c0...`):
     - `verify_wall3_coupled_half_root_kernel_pv_eigenmode_and_weak_vertex` (lines 4206–4791): specifically lines 4357–4441 (`_spin_lie_32`, `_build_spinor_complex`), lines 4443–4464 (`_pole_degree`, `_line_h0`), lines 4467–4481 (`records_list`), lines 4483–4507 (`_total_cohomology`), and lines 4531, 4543–4559, 4767 (`pure_h4_cohomologies.append(_total_cohomology(rec, 0, chi=(0, 0)))`, `pure_h4_kernel_dim == 24`, `all(c_t == (0, 3, 3, 0) for c_t in pure_h4_cohomologies)`, `"control5_pure_h4_chi00_kernel_dim_24": pure_h4_kernel_dim`);
     - `verify_coupled_2d_surface_and_3sheet_cover_bvp` (lines 4794–5345): specifically lines 4841–4974 (`_reduced_spinor_bvp`, `_pole_deg_bvp`, `_line_h0_bvp`, `records_8`, `_cohom_count_bvp(rec, 0, (0, 0))`) and lines 5315–5318 (`"pure_h4_chi00_record_counts_sum_24": [cover_3sheet_middle_counts, sum(cover_3sheet_middle_counts)]`).
   - **Claim:** Evaluates the NumPy translation of `N06` at `correction = 0` (`Model M3a`, $\tilde{A} = A_{\text{bare}}h_4$; likewise `correction = 1` gives `Model M3b`, $\mathrm{Zeta}\tilde{A}$) with the order-3 Wilson character set to $\chi = (0,0)$ on the base punctured torus $\Sigma_{1,1}$ (`Carrier C0`). Because $\alpha^2 = 1$ on all 8 half-root records ($Q \in \{\pm 1, \pm 1/3\}$) and $\chi_R(a) = \chi_R(b) = 1$ when $\chi = (0,0)$, the middle degree-1 Koszul action `(a_red[1], b_red[1]) = (alpha * sigma_x, alpha * sigma_x)` has exactly one joint $+1$ eigenvector (the $\sigma_x = +1$ or $\sigma_x = -1$ line depending on $\alpha \in \{+1, -1\}$) on **every** record. Adding `h1_list[0] = 2` (from `pow_a = -3`, dual `2 - (-3) = 5`, `pole_degree(5) = 2`) and `h0_list[1] = 1` (from `pow_a = 1`, `pole_degree(1) = 0`, 1 fixed column) gives `(0, 3, 3, 0)` on each of the 8 records, summing to $24 = 8 \times 3$ left-kernel (`h1 + h3`) and $24$ adjoint-kernel (`h0 + h2`) coefficient dimensions.
2. **Evidence Type:** Imported authored code definition and **unreviewed reported coefficient count** (Reading Note 4; Layer L1 calculation + Layer L2 formula evaluation, outside the `6290484f286cf82a58131acd99ec156339f1e3da` review).
3. **Hypotheses Consumed:**
   - Base carrier `C0` ($\Sigma_{1,1}$, genus $1$, $1$ cusp) with complete hyperbolic cusp metric $g = \Omega^2(dx^2 + dy^2)$;
   - Conditional odd spin $\eta = \mathcal{O}$ (`spin = (1,1)` implicit in `_total_cohomology`, which omits the `spin` parameter of `N06` by fixing `eta = (1,1)`);
   - Continuous-$\operatorname{Pin}_2$ coherent lift $\tilde{A} = A_{\text{bare}}h_4$ with independent central signs fixed to `signs = (1,1)`;
   - **Explicit change of flat background** from $\chi = (1,0)$ (`Model M2a/M2b`) to $\chi = (0,0)$ (`Model M3a/M3b`);
   - Assuming that the complete-domain equivariant reduction of `N05` (`789adf7544...`) holds unaltered at $\chi = (0,0)$.
4. **What Follows vs. What Does Not:**
   - *Follows:* Within the reduced-action formula of `N05`–`N06`, setting $\chi = (0,0)$ at $\eta = \mathcal{O}$ and `signs = (1,1)` changes the 6 colour-triplet records from $(0,2,2,0)$ to $(0,3,3,0)$, shifting the half-root left-kernel coefficient sum from $18 = 6\times 2 + 2\times 3$ (`Model M2a/M2b`) to $24 = 8\times 3$ (`Model M3a/M3b`).
   - *Does not follow:* Does **not** trivialize the old order-3 Wilson character $\chi_3$ on the discriminant cover (`N08`), does **not** prove global all-sector compatibility (`E3`), does **not** by itself certify the integer-root $(10,6)$ up-quark ($Q = \pm 2/3$) zero-mode roster (`E1`), does **not** establish chiral vs. vector-like family structure (`E4`), and does **not** compute the physical $128 \leftrightarrow 120$ weak current (`E2`).

---

### Node `N08` — Discriminant Cover $\Sigma_K$ (`Carrier C2`), Coprime-Degree Persistence of $\chi_3$, and Separation of Base `Model M3` from Cover `Model M5`
1. **Exact Source & Concrete Claim:**
   - Commit `1704f9e4153dea79d4d2ff2ea33cbe029fcb9481` (and `dd7490203c55bae043585f594af5a13afe634fa7`), `reports/physical_bridge_2026_09_05/foundation_selection_2026_11_07/DISCRIMINANT_COVER_PERIPHERAL_AND_ORDER_THREE_WILSON_2026_11_08.md` (§1–§7, SHA256 `5c056ae0d1...`);
   - Commit `21b293e87ff09fd64911267e9b4aa447fbfab2b9`, `src/origin_axiom/weave_unification_bridge.py` (`verify_coupled_2d_surface_and_3sheet_cover_bvp`, lines 4975–5010, SHA256 `73bb65f3c0...`).
   - **Claim:**
     1. The discriminant subgroup $K = (P|_N)^{-1}(2D_4^*) \triangleleft F_2$ defines a normal cover $\Sigma_K \to \Sigma_{1,1}$ (`Carrier C2`) of degree $32 = 8 \times 4$ with deck group $G_{\text{disc}} = F_2/K$, compact genus $g(\Sigma_K) = 9$, and $16$ spatial cusps (each of branching degree $2$ over $p$).
     2. Because $\gcd(32, 3) = 1$, pulling back the order-3 Wilson character $\chi_3$ to $\Sigma_K$ (`Model M4`) remains a nontrivial order-3 character on $\Sigma_K$; moreover, multiplying $\omega_3 = e^{2\pi i/3}$ by a $\mathbb{Z}_2$ deck sign $s \in \{\pm 1\}$ cannot produce a $+1$ eigenvalue on $\sigma_x$ ($\dim\ker(s\omega_3\sigma_x - I_2) = 0$, verified at `weave_unification_bridge.py` lines 4978–4985).
     3. All four characters of $A_{\text{disc}} = D_4/(2D_4^*) \cong \mathbb{Z}_2 \times \mathbb{Z}_2$ are **trivial on the 16 spatial cusps** because $P_{c^2} = 0$; presentation-relator signs on $r_2, r_3$ are core data on $\Sigma_{Q_8}$, not spatial cusp signs.
     4. On the 3D augmentation module $W = \bigoplus_{\psi \neq 1} \mathbb{C}_\psi$, pure $S_3$ permutations split as $1 \oplus 2$ (commutant $a I_3 + b J_3$), whereas the combined order-24 group $A_{\text{disc}} \rtimes S_3$ (retaining deck signs $D_2 = \operatorname{diag}(-1,+1,-1)$, $D_3 = \operatorname{diag}(+1,-1,-1)$) acts irreducibly.
2. **Evidence Type:** Imported authored hand proof (`1704f9e4153dea79d4d2ff2ea33cbe029fcb9481`, unreviewed post-`8cad267b4`) and counterexample.
3. **Hypotheses Consumed:** Affine $Q_8$-doublet translation map $P: N \to D_4$, discriminant quotient $A_{\text{disc}} = D_4/(2D_4^*)$, and Hurwitz/cusp-branching formulas on $\Sigma_K$.
4. **What Follows vs. What Does Not:**
   - *Follows:* Strictly separates **base `Model M3a/M3b`** on $\Sigma_{1,1}$ (where the count $3 = 2 + 1$ per record comes from $h^1(S^{-3}) = 2$ plus $h^0(S^1) = 1$ on a single genus-1 curve with $\chi = (0,0)$) from **cover `Model M5`** on $\Sigma_K$ (where $\dim W = 3$ is the dimension of the non-trivial deck-character augmentation module under $A_{\text{disc}} \rtimes S_3$ on a genus-9, 16-cusp surface).
   - *Does not follow:* One **cannot** infer a base/cover equivalence from the numerical coincidence $3 = 3$, nor claim that `verify_coupled_2d_surface_and_3sheet_cover_bvp` (`weave_unification_bridge.py` line 4973, which calls `_cohom_count_bvp(rec, 0, (0,0))` on the base curve $\Sigma_{1,1}$ and names the variable `cover_3sheet_middle_counts`) actually solved the Dolbeault cohomology on the genus-9, 16-cusp cover $\Sigma_K$.

---

### Node `N09` — Centralizer $A_3 = (1,15)$ Adjoint Action $\operatorname{Ad}_{h_4}$ ($15 \to 9$) and Finite Exterior-Square $\Lambda^2(h_4)$ Witness vs. Full Integer-Root $120$ Sector
1. **Exact Source & Concrete Claim (Corrected per `REVIEW_AGY_00B1_2BED_2026_11_08.md` Item 3):**
   - Commit `dd7490203c55bae043585f594af5a13afe634fa7`, `reports/physical_bridge_2026_09_05/word_architecture_audit_2026_10_17/CENTRALIZER_KERNEL_WITH_THRESHOLD_CONTINUUM.md` (§1–§3, SHA256 `a19e2c6c6b...`);
   - Commit `6290484f286cf82a58131acd99ec156339f1e3da`, `INDEPENDENT_PROOF_CODE_REVIEW_2026_11_07.md` (SHA256 `00fba6daf4...`);
   - Commit `21b293e87ff09fd64911267e9b4aa447fbfab2b9`, `src/origin_axiom/weave_unification_bridge.py` (`verify_wall3_coupled_half_root_kernel_pv_eigenmode_and_weak_vertex`, lines 4561–4620, SHA256 `73bb65f3c0...`).
   - **Claim:**
     1. In `CENTRALIZER_KERNEL_WITH_THRESHOLD_CONTINUUM.md` (supported by `6290484f286cf82a58131acd99ec156339f1e3da` with the old order-3 Wilson $\chi_3 \neq 0$), the $A_3 = (1,15)$ spin-field $L^2$ kernel vanishes identically due to the logarithmic cusp endpoint ($n = -1$ forbidden in $\int r^{2n+1}/\ln(1/r)\,dr$), while $9$ scalar/gaugino and $9$ connection/form zero modes survive in the unbroken $\mathfrak{su}(3)_c \oplus \mathfrak{u}(1)_{\text{em}} \subset A_3$, coexisting with a spin threshold continuum reaching $0$.
     2. In `weave_unification_bridge.py` lines 4576–4601 (ported from `verification_transport_end_2026_11_04/checks.py`), the explicit $4\times 4$ diagonal $h_4 = \operatorname{diag}(e^{3\pi i/4}, e^{-\pi i/4}, e^{-\pi i/4}, e^{-\pi i/4})$ has:
        - **On the $15$-dimensional $A_3$ adjoint $\operatorname{Ad}_{h_4}$ (`h15_mat`):** $9$ unbroken $\mathfrak{u}(3)$ directions with eigenvalue $+1$ and $6$ broken directions ($h_{4,1}h_{4,j}^{-1} = e^{\pi i} = -1$ and $h_{4,j}h_{4,1}^{-1} = e^{-\pi i} = -1$ for $j \in \{2,3,4\}$) with eigenvalue **$-1$** (`scalar_gaugino_zero_modes = _line_h0(0, (h15_mat, h15_mat)) == 9`);
        - **On the $6$-dimensional exterior square $\Lambda^2(h_4)$ (`ext2_h4_mat`):** **three $+i$ eigenvalues** ($h_{4,1}h_{4,j} = e^{3\pi i/4}e^{-\pi i/4} = +i$ for $j \in \{2,3,4\}$) and **three $-i$ eigenvalues** ($h_{4,j}h_{4,k} = e^{-\pi i/4}e^{-\pi i/4} = -i$ for $2 \le j < k \le 4$). None of those six eigenvalues is $+1$, so the finite fixed-column check `ext2_6_zero_modes = _line_h0(0, (ext2_h4_mat, ext2_h4_mat)) == 0` rules out parallel constant coefficients on the bare $6$ without computing the physical fermion kernel of the complete coupled $D_5$/spin/flavour/Higgs $(10,6)$ complex (`E1`).
2. **Evidence Type:** Independent review at its exact scope (`6290484f286cf82a58131acd99ec156339f1e3da` for $A_3$ with old $\chi_3$) plus imported authored finite-matrix check (`weave_unification_bridge.py` lines 4576–4601 for $\operatorname{Ad}_{h_4}$ and $\Lambda^2(h_4)$ at $\chi = (0,0)$).
3. **Hypotheses Consumed:** Hyperbolic cusp metric weights ($\Omega$ for spin, $\Omega^2$ for scalar, conformal for 1-form), peripheral $\operatorname{Hol}_F(c) = -I_2$, and $h_4 = \exp(i\frac{3\pi}{4}Q_{\text{em}})$.
4. **What Follows vs. What Does Not:**
   - *Follows:* Even at $\chi = (0,0)$ (`Model M3a/M3b`), $\operatorname{Ad}_{h_4}$ has eigenvalue $+1$ on the $9$ unbroken $\mathfrak{u}(3)$ directions and $-1$ on the $6$ broken $A_3$ directions, while $\Lambda^2(h_4)$ has three $+i$ and three $-i$ eigenvalues (no $+1$ fixed column).
   - *Does not follow:* The finite $\Lambda^2(h_4)$ fixed-column zero (`ext2_6_zero_modes == 0`) is **not** the physical fermion kernel of the coupled $(10,6)$ complex (`E1`), and `CENTRALIZER_KERNEL_WITH_THRESHOLD_CONTINUUM.md` §2 does not calculate the $(10,6)$ or $(45,1)$ sectors.

---

### Node `N10` — Cross-Grading $128 \leftrightarrow 120$ Charged Weak Current Duty, Conditional Global Vector Proof vs. Finite Controls, and Finding `V1`
1. **Exact Source & Concrete Claim (Corrected per `REVIEW_AGY_00B1_2BED_2026_11_08.md` Item 5):**
   - Commit `dd7490203c55bae043585f594af5a13afe634fa7`, `reports/physical_bridge_2026_09_05/word_architecture_audit_2026_10_17/WEAK_CURRENT_GRADING_AND_DISCRETE_CHARGED_VECTORS.md` (§1–§4, Eqs. (1)–(2), SHA256 `7ac2e6cc08...`);
   - Commit `3e58425f1e6560d9f078f306e724ed264d41884f`, `reports/physical_bridge_2026_09_05/word_architecture_audit_2026_10_17/verification_coupled_half_root_kernel_2026_11_07/checks.py` (lines 356–435, SHA256 `e72063d7b2...`);
   - Commit `6290484f286cf82a58131acd99ec156339f1e3da`, `INDEPENDENT_PROOF_CODE_REVIEW_2026_11_07.md` (§Verdict & §V1, SHA256 `00fba6daf4...`).
   - **Claim:**
     1. **Analytical proof scope (`WEAK_CURRENT_GRADING_AND_DISCRETE_CHARGED_VECTORS.md`, supported by `6290484f286cf82a58131acd99ec156339f1e3da`):** Every $Q_{\text{em}} = \pm 1$ vector $w$ lies in the odd $\mathrm{Zeta} = -1$ half-root sector $128$. Because $\operatorname{ad}_w$ reverses the $\mathrm{Zeta}$-grading ($[128,128] \subset 120$, $[128,120] \subset 128$) and the 4-slot kinetic inner product is $\mathrm{Zeta}$-orthogonal, any single-vector fermion bilinear
        $$g_{mn}(w) = g_6 \sum_{i \in (\lambda, a, u, v)} \int_\Sigma h_i\,\kappa\!\left(\psi_{i,m}^\dagger [w, \psi_{i,n}]\right)$$
        vanishes identically on $128 \times 128$ and $120 \times 120$ and **must** cross $128 \leftrightarrow 120$. Furthermore, the conditional hand proof establishes that the charge-one vector block is globally discrete with strictly positive lowest eigenvalue on each fixed stipulated carrier.
     2. **Finite control code scope (`checks.py` lines 356–435) and Finding `V1` (`6290484f28`):** In `checks.py`, `test_full_charge_grading_and_actual_cubic_selection` (lines 356–393) checks finite root/charge grading and algebraic cubic-selection witnesses, while `test_actual_compact_centralizer_and_vector_block_duties` (lines 395–435) checks finite centralizer kernels and squares a generic finite 3-degree Hermitian Koszul matrix rather than binding the actual 4-slot source operator $M^\dagger M$ with derivative/curvature cancellation (`Finding V1`). The finite control code does **not** independently solve or prove the global Sturm–Liouville problem.
2. **Evidence Type:** Independent review at its exact scope (`6290484f286cf82a58131acd99ec156339f1e3da`, supporting the conditional hand proof while issuing `V1` on the unrun code `3e58425f1e6560d9f078f306e724ed264d41884f`; Layer L4 constraint).
3. **Hypotheses Consumed:** Exact $E_8$ root/charge decomposition, $\mathrm{Zeta}$-invariance of the Killing form $\kappa$, antiperiodic $128$ cusp end, and the 4-slot kinetic metric $h_i = (\Omega^2, 1/2, \Omega, \Omega)$.
4. **What Follows vs. What Does Not:**
   - *Follows:* No overlap computed solely within the $128$ half-root sector can represent a single-vector $W^\pm$ weak current, and the conditional hand proof supports a discrete strictly positive $Q = \pm 1$ vector spectrum.
   - *Does not follow:* The finite control code in `checks.py` does not solve the global Sturm–Liouville problem or bind the actual 4-slot source gauge block (`V1`), and `WEAK_CURRENT_GRADING_AND_DISCRETE_CHARGED_VECTORS.md` does not compute the $128 \leftrightarrow 120$ overlap matrix $g_{mn}(w)$ or establish V-A weak chirality.

---

### Node `N11` — AGY Radial-Spinor Overlap Shortcut (`compute_4slot_weak_vertex_overlap`) and Historical Validator/Journal Scope Boundary
1. **Exact Source & Concrete Claim (Corrected per `REVIEW_AGY_00B1_2BED_2026_11_08.md` Item 4):**
   - Commit `21b293e87ff09fd64911267e9b4aa447fbfab2b9`, `src/origin_axiom/weave_unification_bridge.py` (`compute_4slot_weak_vertex_overlap` inside `verify_coupled_2d_surface_and_3sheet_cover_bvp`, lines 5185–5303 and 5335–5342, plus `solve_chebyshev_pv_eigenmode` inside `verify_wall3_coupled_half_root_kernel_pv_eigenmode_and_weak_vertex`, lines 4647–4745, SHA256 `73bb65f3c0...`);
   - Commit `51a5ffdad70b6a6208a5063f0dc4237a7fdf4190`:
     - `tests/test_sealed_validator_negative_controls.py` (`F4` branch `# 4. Instance BVP Task 3 & Wall 3 (F4 gate)` of `validate_bridge_candidate` at lines 148–172, SHA256 `cba9748eb5...`);
     - `docs/audit/FLOW_JOURNAL_2026_11_08_WALLS_F1_F4_AND_OPEN_O1_O2.md` (SHA256 `6a8b177083...`).
   - **Claim & Actual Scope (Reading Note 1):**
     1. In `weave_unification_bridge.py` lines 5185–5263 (`verify_coupled_2d_surface_and_3sheet_cover_bvp`), `compute_4slot_weak_vertex_overlap` solves a 1D Chebyshev radial Sturm–Liouville problem on $t \in [0, 4]$ (`H_int = -D2_t + diag(0.25 + pi^2 * exp(2*t) + 1.0)`) for a scalar profile `w0_full`, imposes three radial functions $f_1(t) \propto e^{-t/2}$, $f_2(t) \propto e^{-3t/2}$, and Gram–Schmidt orthogonalized $f_3(t)$ placed into the 32-component harmonic spinor slots `(12, 19)` (`v_mid_32`) and `15` (`v_ext_32`) of a single half-root record, integrates $\int_0^4 dt\,w_t w_0(t) (\Phi_a(t)^\dagger \Phi_b(t))$ to form a $3\times 3$ matrix `g_mat_3`, and forms the $6\times 6$ Kronecker product `v_weak_6x6 = np.kron(tau_plus, g_mat_3)` at line 5262.
     2. In `51a5ffdad70b6a6208a5063f0dc4237a7fdf4190`, the `F4` branch of `validate_bridge_candidate` (`tests/test_sealed_validator_negative_controls.py`, lines 148–172) reads the three reported eigenvalues (`g_4slot_3mode_eigenvalues`), the 50-trial random $SU(2)_L \times U(3)_{\text{fam}}$ Haar singular-value error (`haar_50_trial_su2L_u3fam_max_err`), and the nonunitary diagonal-scaling drift (`non_unitary_negative_control_drift`), while `validate_bridge_candidate` also checks AST literal-return and disclosure flags.
2. **Evidence Type:** Unresolved join / diagnosed shortcut (historical validator/journal commit `51a5ffdad70b6a6208a5063f0dc4237a7fdf4190` is outside accepted physical evidence).
3. **Hypotheses Consumed:** Imposed radial profiles on $t \in [0,4]$, single-sector spinor inner product $\Phi_a^\dagger \Phi_b$ without an odd-$128$ Lie bracket $[w, \cdot]$, and external $2\times 2$ weak raising matrix `tau_plus`.
4. **What Follows vs. What Does Not:**
   - *Follows:* Confirms only quadrature convergence on $[0,4]$ of the imposed 3-profile radial integral and unitary singular-value invariance of the resulting $3\times 3$ and $6\times 6$ matrices.
   - *Does not follow:* Does **not** solve the 2D elliptic PDE $M\psi = 0$ on $\Sigma_{1,1}$, does **not** use the integer-root $(10,6)$ up-type quark modes, and violates `N10` by computing an inner product within a single sector rather than the cross-grading $128 \leftrightarrow 120$ Lie bracket $\kappa(\psi_{120}^\dagger [w_{128}, \psi_{128}])$. Also, the historical journal's `O2` identity $[Q_{\text{em}}, T^\pm] = \pm T^\pm$ merely states that $W^\pm$ has electric charge $\pm 1$ and neither proves an independent weak-chirality no-go theorem nor requires an extra supplied Higgs VEV $H_0$ beyond $(q,r)$.

---

### Node `N12` — Canonical `GENESIS.md` (`217e37c4f`) and SM3 Completion Checklist (`dd7490203`) Premise Status
1. **Exact Source & Concrete Claim:**
   - Commit `217e37c4f37bd80998f3c3e10cad358023f58114`, `GENESIS.md` (`PF1`–`PF3`, `GM1`–`GM5d`, `FK1`–`FK15`, SHA256 `ec8c3dba05...`);
   - Commit `dd7490203c55bae043585f594af5a13afe634fa7`, `reports/physical_bridge_2026_09_05/SM3_AND_GRAVITY_COMPLETION_CHECKLIST_2026_11_08.md` (§1–§4, SHA256 `b3a04ab794...`);
   - Commit `6fc5cdd0d05e8072f6a2a64f267772d06ee94976`, `reports/physical_bridge_2026_09_05/PROGRESS_SINCE_MAIN_217E_2026_11_08.md` (§1–§5, SHA256 `d61af22b9e...`).
   - **Claim:** Canonical confirmed Standard Model parameter count is `0 of 19`. Even when conditional fibre/cohomology counts (`16`, `18`, or candidate `24`) are established within a supplied model, promoting them to a physical three-generation Standard Model (`SM3`) requires discharging the supplied parent/carrier/spin/flavour/lift premises and completing the full charge-resolved fermion roster, cross-grading weak interaction, and family map.
2. **Evidence Type:** Supplied canonical ledger and completion gate (Layer L4 governance).
3. **Hypotheses Consumed:** Repository-wide evidence and non-dimensional input accounting rules.
4. **What Follows vs. What Does Not:**
   - *Follows:* Prevents promoting the 24-coefficient count (`N07`) to a derived 3-generation theorem or changing `0 of 19` before the five consequential open joins (`E1`–`E5`) are resolved and independently reviewed.
   - *Does not follow:* Does not withdraw the scoped conditional mathematical results in `N01`–`N05` and `N08`–`N10`.

---

## 3. Summary Dependency Flow (`N01`–`N12` $\to$ `E1`–`E5`)

```
[N01: Common 6D Action & 4-Slot Mass Map M (dd7490203)]
       |
       v
[N02: Balanced Two-Triple D5+A3 Branching, C_D5*h4^2=1 & (1,2,1) Koszul Retraction (dd7490203)]
       |
       +---> [N03: Flat Zeta*P + Spin P -> Total Peripheral Zeta on All 4 Slots; ind M_R = 0 (dd7490203 / 6f35dfefd)]
       |
       v
[N04: Full E8 Bare Lift (A^4=Zeta) vs. Coherent Pin2 Lifts A_tilde, Zeta*A_tilde (dd7490203)]
       |
       +---> (chi = chi_3 != 0) ---> [N05: 16 Bare / 18 Corrected Left-Kernel Proof (dd7490203 / 6290484f2)]
       |                                    |
       |                                    v
       |                             [N06: Parent SymPy total_cohomology & Line 308 Countercontrol (3e58425f1)]
       |                                    |
       +---> (chi = (0,0) change) ----------+---> [N07: AGY NumPy _total_cohomology(rec,0,chi=(0,0)) -> 24 = 8*3 (21b293e87)]
                                                         |
       +-------------------------------------------------+-------------------------------------------------+
       |                                                 |                                                 |
       v                                                 v                                                 v
[N09: Ad_{h4} (9 of +1, 6 of -1) & Lambda^2(h4) (3 +i, 3 -i)]   [N10/N11: 128<->120 Weak Current vs. 6x6 Shortcut]   [N08: Cover Sigma_K (deg 32) vs. Base M3]
       |                                                 |                                                 |
       v                                                 v                                                 v
  {Open Edge E1 (with 30f348e15 candidate)}         {Open Edge E2}                                  {Open Edges E3, E4, E5}
```

---

## 4. Five Consequential Unresolved Edges (`E1`–`E5`), Ordered by Downstream Impact

### Edge `E1` (Impact Rank 1) — Complete-Domain Integer-Root `(10,6)` Up-Quark ($Q = \pm 2/3$) and Remaining $120$-Sector Zero-Mode Roster (`30f348e15` Unreviewed Candidate)
- **Missing Join:** `N04` + `N07` + `N09` $\nrightarrow$ Independently Certified Complete Three-Family Matter Roster (Layer L2/L3/L4).
- **Why Consequential:** All 8 half-root records in $(16,4) \oplus (\overline{16},\overline{4}) = 128$ carry only electric charges $Q_{\text{em}} \in \{\pm 1, \pm 1/3\}$ ($e^\pm, d, \bar{d}$ candidates). Up-type quarks ($Q_{\text{em}} = \pm 2/3$) reside exclusively in the integer-root sector $(10,6) \subset 120$, while neutral/adjoint modes and an essential spin threshold continuum reside in $(1,15) \oplus (45,1) \subset 120$.
- **Existing Producers / Proofs Bearing on This Edge (Corrected per `REVIEW_AGY_00B1_2BED_2026_11_08.md` Items 3 & 6):**
  - **Unreviewed physical-seat candidate for the $(10,6)$ up-sector (`30f348e15755a3c5a824e75d5ed6ba354e200bb3`):** `reports/physical_bridge_2026_09_05/word_architecture_audit_2026_10_17/COUPLED_UP_SECTOR_PARABOLIC_COUNT_2026_11_08.md` (§1–§8, SHA256 `477743caf7...`, accompanied by `UP_SECTOR_EXPLORATORY_NEUTRAL_NOTES_2026_11_08.md` and prospective design `verification_up_sector_2026_11_08/DESIGN.md`) is an **UNREVIEWED / UNRUN authored hand derivation** on the paired $(10,6)$ vector modules $V_{(2,0)} \oplus V_{(0,2)}$. Retaining the rank-two unitary flat peripheral transition $-I$ on the two middle packages $S^3$ and $S^{-1}$, it derives a compact parabolic extension generated by $w^{1/2}$ times a flat frame of compact degree $-1$ (giving middle compact sheaves $\mathcal{E}_3(p)$ and $\mathcal{E}_{-1}$ with cohomology $(1,0)$ and $(0,1)$ and extreme packages $(0,2)$ and $(2,0)$), yielding a candidate total $(H^0, H^1, H^2, H^3) = (0, 3, 3, 0)$ (three coefficients per colour-up representation and its conjugate, $18$ Weyl coefficients). Its explicit review duties—actual $A,D$/flavour transition signs, bounded equivariant contraction over the paired modules, strict $a=3$ and $a=-1$ cusp endpoints, compact parabolic degree $-1$ and dual $-p$ twist, complete Hodge/operator transfer, and closed range—remain open, and it does **not** resolve the complete neutral $(45,1) \oplus (1,15)$ spectrum or certify the charged count.
  - **Finite carrier and exterior-square controls:** `ELECTROWEAK_TWO_TRIPLE_PHYSICAL_KERNEL.md` (`dd7490203`, `871529dd81...`) and `verification_transport_end_2026_11_04/checks.py` (`dd7490203`, `cb3d46f2a5...`, `exterior_square`, `exterior_lie`, `full_parent_modules`) construct the finite $(10,6)$ and $(45,1)$ carriers, and `weave_unification_bridge.py` (`21b293e87`, lines 4590–4601) checks that $\Lambda^2(h_4)$ has **three $+i$ and three $-i$** eigenvalues (none equal to $+1$, so `ext2_6_zero_modes == 0`). As `30f348e15` notes, that finite six-to-zero fixed-column check rules out parallel constant coefficients on the bare $6$ without being the physical fermion kernel of the complete $D_5$/spin/flavour/Higgs complex.

---

### Edge `E2` (Impact Rank 2) — Cross-Grading $128 \leftrightarrow 120$ Physical Weak Current and Actual Global 4-Slot $M\psi = 0$ Mode Overlaps (Including `V1`)
- **Missing Join:** `N01` + `N07` + `N10` + `N11` $\nrightarrow$ Certified Physical $W^\pm$ Coupling Matrix $g_{mn}(w)$ (Layer L3/L4).
- **Why Consequential:** Because every $Q_{\text{em}} = \pm 1$ vector $w$ lies in the odd sector $128$ ($\mathrm{Zeta} = -1$), `WEAK_CURRENT_GRADING_AND_DISCRETE_CHARGED_VECTORS.md` (`N10`) proves that the same-action weak vertex $g_{mn}(w) = g_6 \sum_i \int_\Sigma h_i\,\kappa(\psi_{i,m}^\dagger [w, \psi_{i,n}])$ vanishes identically between any two $128$ modes and must couple a $128$ mode ($Q = -1/3$ or $-1$) to a $120$ mode ($Q = +2/3$ or $0$) via the $E_8$ Lie bracket $[w_{128}, \psi_{128}] \in 120$, using actual global 4-slot solutions of $M\psi = 0$ on $\Sigma_{1,1}$ and binding the actual source gauge block $M^\dagger M$ (resolving Finding `V1` of `6290484f28`). The AGY producer's $3\times 3$ single-sector overlap `g_mat_3` on $t \in [0,4]$ and $6\times 6$ Kronecker product `v_weak_6x6 = np.kron(tau_plus, g_mat_3)` in `verify_coupled_2d_surface_and_3sheet_cover_bvp` (`N11`) do not discharge this join.
- **Existing Producers / Proofs Bearing on This Edge (Corrected per `REVIEW_AGY_00B1_2BED_2026_11_08.md` Item 5):**
  - **Conditional analytical proof (`dd7490203`, `7ac2e6cc08...`, supported by `6290484f28`, `00fba6daf4...`):** `WEAK_CURRENT_GRADING_AND_DISCRETE_CHARGED_VECTORS.md` establishes the cross-grading selection rule and supports the global discrete, strictly positive charged-vector Sturm–Liouville statement on each fixed stipulated carrier;
  - **Finite control code and unresolved `V1` (`3e58425f1`, `e72063d7b2...`):** `verification_coupled_half_root_kernel_2026_11_07/checks.py` (`test_full_charge_grading_and_actual_cubic_selection`, lines 356–393, and `test_actual_compact_centralizer_and_vector_block_duties`, lines 395–435) checks finite root/charge grading and algebraic cubic-selection witnesses and carries the unresolved Finding `V1` (`6290484f28`, squaring a generic finite Koszul matrix rather than binding the actual 4-slot source operator $M^\dagger M$ from `weave_physical_mass_2026_10_08/PROOF.md`, `04fbb6b7dd...`); it does **not** independently solve or prove the global Sturm–Liouville problem.

---

### Edge `E3` (Impact Rank 3) — Independent Mathematical Review of Pure-$h_4$, $\chi = (0,0)$ Complete-Domain Reduction and All-Sector Lift Compatibility
- **Missing Join:** `N04` + `N05` + `N06` + `N07` $\nrightarrow$ Independently Certified 24-Mode Half-Root Kernel Theorem and Global All-Sector Consistency (Layer L2/L3).
- **Why Consequential:** The completed independent review `6290484f286cf82a58131acd99ec156339f1e3da` certified only the $16$ bare (`Model M1`) and $18$ corrected (`Model M2a/M2b`) half-root left-kernel counts with the old nontrivial order-3 Wilson character $\chi_3 \neq 0$. Extending the complete-domain equivariant chain-homotopy reduction of `COUPLED_HALF_ROOT_KERNEL_AND_CORE_LIFT_SENSITIVITY.md` (`789adf7544...`) to the changed flat background $\chi = (0,0)$ (`Model M3a/M3b`), and proving that setting $\chi = (0,0)$ under $h_4 = \exp(i\frac{3\pi}{4}Q_{\text{em}})$ (for both continuous-$\operatorname{Pin}_2$ lifts $\tilde{A}$ and $\mathrm{Zeta}\tilde{A}$ and against arbitrary free-group central signs $(s_a, s_b)$) is globally consistent across all 248 $E_8$ sectors and peripheral cusp laws, remains an unreviewed conditional claim (task `AGY-01` once released).
- **Existing Producers / Proofs Bearing on This Edge:**
  - `COUPLED_HALF_ROOT_KERNEL_AND_CORE_LIFT_SENSITIVITY.md` (`dd7490203`, `789adf7544...`), `FULL_E8_COMPENSATOR_LIFT_AND_REGISTER_TRANSPORT.md` (`dd7490203`, `6012816683...`), and `PIN2_COMPENSATOR_COHERENCE_AND_ELECTROMAGNETIC_PHASE.md` (`dd7490203`, `fc67d4446b...`);
  - `verification_coupled_half_root_kernel_2026_11_07/checks.py` (`3e58425f1`, `e72063d7b2...`, lines 169–190 and 308–310);
  - `weave_unification_bridge.py` (`21b293e87`, `73bb65f3c0...`, `verify_wall3_coupled_half_root_kernel_pv_eigenmode_and_weak_vertex` lines 4483–4620 and `verify_coupled_2d_surface_and_3sheet_cover_bvp` lines 4841–4974).

---

### Edge `E4` (Impact Rank 4) — Chiral vs. Vector-Like Interpretation of the $24 = 12_{(16,4)} + 12_{(\overline{16},\overline{4})}$ Left-Kernel Coefficients
- **Missing Join:** `N03` + `N05` + `N07` $\nrightarrow$ Three Chiral Standard Model Families with Nonzero Low-Energy Charged Fermion Masses (Layer L3/L4).
- **Why Consequential:** In `Model M3a/M3b`, the 24 left-kernel coefficient dimensions split equally between conjugate unbroken-$U(3)$ representations: $3 \times (1_{+1} \oplus 3_{-1/3})$ in $(16,4)$ (`12` dimensions) and $3 \times (1_{-1} \oplus \bar{3}_{+1/3})$ in $(\overline{16},\overline{4})$ (`12` dimensions), with net unbroken-$U(3)$ index $\operatorname{ind} M_R = 0$ (`N03`) and equal adjoint-kernel dimensions `(0,3,3,0)` on every record. As `COUPLED_HALF_ROOT_KERNEL_AND_CORE_LIFT_SENSITIVITY.md` §6 and `QUATERNION_SECTOR_INDEX_AND_WEAK_CURRENT_DUTY.md` §5 prove, left-handed 4D Weyl zero modes in $R \oplus \bar{R}$ under unbroken $SU(3)_c \times U(1)_{\text{em}}$ do not by themselves distinguish a weak-chiral Standard Model spectrum (where $R$ and $\bar{R}$ have inequivalent couplings to $W^\pm$) from a vector-like spectrum, nor explain how these classical zero modes of $M$ acquire the observed nonzero charged-lepton and quark masses.
- **Existing Producers / Proofs Bearing on This Edge:**
  - `QUATERNION_SECTOR_INDEX_AND_WEAK_CURRENT_DUTY.md` (`dd7490203`, `11ddfae199...`, §5);
  - `COUPLED_HALF_ROOT_KERNEL_AND_CORE_LIFT_SENSITIVITY.md` (`dd7490203`, `789adf7544...`, §4–§6);
  - `WEAK_CURRENT_GRADING_AND_DISCRETE_CHARGED_VECTORS.md` (`dd7490203`, `7ac2e6cc08...`, §2–§4).

---

### Edge `E5` (Impact Rank 5) — Register-to-Field Family Intertwiner Separating Base `Model M3` ($2+1=3$ per Record on $\Sigma_{1,1}$) from Discriminant Cover `Model M5` ($\dim W = 3$ on $\Sigma_K$)
- **Missing Join:** `N07` + `N08` + `N12` $\nrightarrow$ Physical Register-to-Field Family Map (Layer L4).
- **Why Consequential:** On the base curve $\Sigma_{1,1}$ (`Carrier C0`, `Model M3a/M3b`), the 3 modes per record arise as $2$ modes from $H^1(\Sigma_{1,1}, S^{-3} \otimes L_{\text{deg }0})$ (degree-0 Koszul extreme line) plus $1$ mode from $H^0(\Sigma_{1,1}, S^1 \otimes L_{\text{triv}})$ (degree-1 Koszul middle line); those two Dolbeault groups live in different Koszul degrees with different spin weights ($S^{-3}$ vs. $S^1$) and are not permuted by a surface deck group. Conversely, on the degree-32 discriminant cover $\Sigma_K$ (`Carrier C2`, `Model M5`), the order-24 group $A_{\text{disc}} \rtimes S_3$ acts irreducibly on the 3-dimensional augmentation deck module $W = \bigoplus_{\psi \neq 1} \mathbb{C}_\psi$, whose characters are trivial on all 16 spatial cusps ($P_{c^2} = 0$). Neither an operator intertwiner on $\Sigma_{1,1}$ nor a complete-domain pullback spectral calculation of $M$ on the genus-9, 16-cusp surface $\Sigma_K$ has been constructed; equating them via $3 = 3$ is invalid.
- **Existing Producers / Proofs Bearing on This Edge:**
  - `DISCRIMINANT_COVER_PERIPHERAL_AND_ORDER_THREE_WILSON_2026_11_08.md` (`1704f9e41`, `5c056ae0d1...`, §1–§7);
  - `FULL_E8_COMPENSATOR_LIFT_AND_REGISTER_TRANSPORT.md` (`dd7490203`, `6012816683...`, §1 & §6);
  - `weave_unification_bridge.py` (`21b293e87`, `73bb65f3c0...`, `verify_coupled_2d_surface_and_3sheet_cover_bvp` lines 4987–5090, which checks finite $S_3$ commutation on a tensored $36\times 36$ matrix $I_3 \otimes M_{12}$ rather than pulling back the 2D differential operator $M$ to $\Sigma_K$).
