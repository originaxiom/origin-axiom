# AGY Durable Handoff (`RESUME.md`) — Checkpoint `AGY-00b1`

**Date:** 2026-11-08
**Status:** **UNREVIEWED AUTHOR CHECKPOINT COMPLETED FOR `AGY-00b1` (`CLAIM_DEPENDENCIES.md` — `PARTIAL: PURE-H4-24 CLAIM ONLY`); STOPPED AWAITING PHYSICAL-SEAT REVIEW AND NEXT MICROTASK RELEASE**

---

## 1. Required `RESUME.md` Fields (`START_HERE.md` §Required RESUME.md fields)

1. **Current parent task and microtask; exact question and current status:**
   - **Parent task:** `AGY-00` ("Reuse inventory and common-model manifest")
   - **Released microtask:** `AGY-00b1` (released by physical dispatch commit `d1b2303969050925d4b548ed21ec862208107b9f`, Coordination revision 4, `RUN_TICKET_AGY_00B1.md`, following physical assessment `6fc5cdd0d05e8072f6a2a64f267772d06ee94976`)
   - **Exact question:** *"Precisely what supports the pure-h4 chi=0 reported 24 charged half-root coefficients, and which joins would be required before that could support a physical three-family claim?"*
   - **Current status:** `AGY-00b1` completed (`CLAIM_DEPENDENCIES.md` labelled `PARTIAL: PURE-H4-24 CLAIM ONLY` written with 12 principal nodes `N01`–`N12` and 5 consequential unresolved edges `E1`–`E5`; `RESUME.md` refreshed; return relay written); **STOPPED** per `START_HERE.md` and `RUN_TICKET_AGY_00B1.md` awaiting physical-seat review.
2. **Model/source commit pins; changed files and last pushed checkpoint:**
   - **Physical review & dispatch commit (`origin/audit/physical-bridge-2026-09-05`):** `d1b2303969050925d4b548ed21ec862208107b9f` (Coordination revision 4; physical review base `6fc5cdd0d05e8072f6a2a64f267772d06ee94976`; prior physical commits `4401782cfc682fc9068c5aa41eb9194a69384308`, `ee34f60fe1e12ca623f8bd6144fb8a6408e6587f`, `dd7490203c55bae043585f594af5a13afe634fa7`).
   - **AGY pinned producer baseline commit:** `21b293e87ff09fd64911267e9b4aa447fbfab2b9`.
   - **Prior AGY branch commits before this `AGY-00b1` checkpoint:**
     - `6552aec6894a4a94a2ced785ac3af8c25f801ba8` (`AGY-00a-r1` manifest/handoff revision, accepted for documentary source intake with reading notes in `REVIEW_AGY_00A_R1_655_2026_11_08.md`);
     - `75a0f8d357f71a20e1b8227d778b8fe85b485252` (initial `AGY-00a` intake checkpoint);
     - `51a5ffdad70b6a6208a5063f0dc4237a7fdf4190` (historical validator/flow-journal commit outside accepted physical evidence).
   - **Main canonical `GENESIS.md` commit (`origin/main`):** `217e37c4f37bd80998f3c3e10cad358023f58114` (`v1.62`, `0 of 19` unchanged).
   - **Files created/modified in this `AGY-00b1` checkpoint:**
     - `reports/physical_bridge_2026_09_05/agy_targeted_campaign_2026_11_08/CLAIM_DEPENDENCIES.md` (new, labelled `PARTIAL: PURE-H4-24 CLAIM ONLY`)
     - `reports/physical_bridge_2026_09_05/agy_targeted_campaign_2026_11_08/RESUME.md` (updated for `AGY-00b1` and the four reading notes of `REVIEW_AGY_00A_R1_655_2026_11_08.md`)
     - `relays/AGY_TO_PHYSICAL_2026-11-08_AGY_00B1_PURE_H4_24_CLAIM_DEPENDENCIES.md` (new short return relay)
3. **Accepted dependency/review artifact locations, with exact scope:**
   - **Accepted documentary source intake for `AGY-00a-r1` (`6552aec6894a4a94a2ced785ac3af8c25f801ba8`):** `reports/physical_bridge_2026_09_05/agy_targeted_campaign_2026_11_08/REVIEW_AGY_00A_R1_655_2026_11_08.md` and `REVIEW_AGY_00A_R1_655_SOURCE_RECEIPT.json` at `d1b2303969050925d4b548ed21ec862208107b9f` (`ACCEPT_SCOPED_RESULT for documentary source intake only`, with four explicit reading notes carried in §1.4 below; not a certificate of the underlying physics, 24-mode count, or scientific execution).
   - **Independent proof/code review of the November 7 coupled half-root kernel, weak-vector, and centralizer proofs (`3e58425f1e6560d9f078f306e724ed264d41884f`):** `reports/physical_bridge_2026_09_05/word_architecture_audit_2026_10_17/verification_coupled_half_root_kernel_2026_11_07/review/INDEPENDENT_PROOF_CODE_REVIEW_2026_11_07.md` at `6290484f286cf82a58131acd99ec156339f1e3da`. Supports the conditional hand proofs of: (1) $16$ bare / $18$ corrected half-root left-kernel coefficient dimensions at odd spin $\eta = \mathcal{O}$ with the **old nontrivial order-3 Wilson character $\chi_3 \neq 0$** (explicitly **excluding** the pure-$h_4$, $\chi = (0,0)$ 24-mode alternative); (2) odd $128$-sector grading of $Q_{\text{em}} = \pm 1$ vectors and $128 \leftrightarrow 120$ cross-grading weak-current selection; and (3) vanishing of the $A_3$ spin-field $L^2$ kernel alongside $9$ scalar + $9$ form modes and a spin threshold continuum. Marks the 9-method code package `REVISION REQUIRED / UNRUN / NOT ADMITTED` due to Finding `V1` (`checks.py:417-435` squares a generic finite Koszul matrix rather than binding the actual 4-slot source operator $M^\dagger M$).
   - **Independent source-complete execution-readiness reviews (both `APPROVE_EXECUTION` at the independent source-review layer, still `UNRUN` pending exact `main` acceptance and strict admission):**
     - 13-method joint transport/geometric-spin/sector-index packet (`bda89f04a94d09217551cef96056f375b21c260b`), reviewed at `6f35dfefdabc9a6f932b27699cd02cb6863623cf`;
     - 6-method same-action gauge-response packet (`d1a33e921d5cb16e4606b196fa970b91a2abfb6d`), reviewed at `8cad267b43827b8f9d6b5b63b19ba093b6795f52`.
4. **Four Reading Notes Retained from `REVIEW_AGY_00A_R1_655_2026_11_08.md` (`d1b2303969050925d4b548ed21ec862208107b9f`):**
   - **Reading Note 1 (Precise description of validator `F4` and producer weak tensor):** The historical validator `F4` branch (`tests/test_sealed_validator_negative_controls.py` at `51a5ffdad70b6a6208a5063f0dc4237a7fdf4190`, lines 173–204) actually reads three reported eigenvalues (`g_4slot_3mode_eigenvalues`), a 50-trial Haar error (`haar_50_trial_su2L_u3fam_max_err`), and a nonunitary drift (`non_unitary_negative_control_drift`), while the producer's later tensor in `src/origin_axiom/weave_unification_bridge.py` (`21b293e87ff09fd64911267e9b4aa447fbfab2b9`, line 5262) is $6\times 6$ (`v_weak_6x6 = np.kron(tau_plus, g_mat_3)`). It must not be oversimplified as checking merely a $2\times 2$ matrix; the missing global mode/domain/generator-witness diagnosis stands.
   - **Reading Note 2 (Parent D-term $g_6^{-2}$ normalization):** The manifest's D-term expression (`MODEL_MANIFEST.md` §1.2) omits the common $g_6^{-2}$ factor if read as the physical $V_D$; the parent (`weave_curved_action_2026_10_08/PROOF.md`, `c505823ce2`) writes $g_6^2 V$ as its displayed integral. Treat the manifest expression as that reduced density and retain the parent's overall $g_6^{-2}$ factor for any physical normalization.
   - **Reading Note 3 (Coordinate change $\det = -1$ vs. flavour holonomies $\det = +1$):** A fixed coordinate change $(q,r) \mapsto ((q+r)/\sqrt{2}, (q-r)/\sqrt{2})$ transports $\varepsilon$ and the degree-two frame with its determinant $-1$. The flavour holonomies $\rho(F_i) = i\sigma_x$ and $\rho(F_k) = \operatorname{diag}(i,-i)$ themselves retain determinant $+1$ under conjugation. Do not read the manifest's combined-factor wording as cancellation of every frame sign or a new global flavour symmetry. Use the exact original complex when computing.
   - **Reading Note 4 (Unreviewed status of the pure-$h_4$ 24-mode count):** The pure-$h_4$, $\chi = (0,0)$ 24-mode result is still an unreviewed reported coefficient count. Matching its table to code or file hashes does not prove the global contraction, physical identification, full roster, or SM3.
5. **What was actually read / proved / implemented / run, separately labelled:**
   - **Read (static text inspection only, zero scientific code execution):**
     - `START_HERE.md`, `RUN_TICKET_AGY_00B1.md`, `REVIEW_AGY_00A_R1_655_2026_11_08.md`, `REVIEW_AGY_00A_R1_655_SOURCE_RECEIPT.json`, `TASKS.json`, and `reports/physical_bridge_2026_09_05/relays/PHYSICAL_TO_AGY_2026-11-08_655_INTAKE_ACCEPTED_RELEASE_00B1.md` at `d1b2303969050925d4b548ed21ec862208107b9f`;
     - `PROGRESS_SINCE_MAIN_217E_2026_11_08.md` at `6fc5cdd0d05e8072f6a2a64f267772d06ee94976`;
     - `ELECTROWEAK_TWO_TRIPLE_PHYSICAL_KERNEL.md`, `CONFINED_HALF_ROOT_SECTOR_AND_SURVIVING_CONTINUUM.md`, `QUATERNION_SECTOR_INDEX_AND_WEAK_CURRENT_DUTY.md`, `FULL_E8_COMPENSATOR_LIFT_AND_REGISTER_TRANSPORT.md`, `PIN2_COMPENSATOR_COHERENCE_AND_ELECTROMAGNETIC_PHASE.md`, `COUPLED_HALF_ROOT_KERNEL_AND_CORE_LIFT_SENSITIVITY.md`, `WEAK_CURRENT_GRADING_AND_DISCRETE_CHARGED_VECTORS.md`, `CENTRALIZER_KERNEL_WITH_THRESHOLD_CONTINUUM.md`, and `verification_transport_end_2026_11_04/checks.py` at `dd7490203c55bae043585f594af5a13afe634fa7`;
     - `verification_coupled_half_root_kernel_2026_11_07/checks.py` at `3e58425f1e6560d9f078f306e724ed264d41884f` and its independent review `INDEPENDENT_PROOF_CODE_REVIEW_2026_11_07.md` at `6290484f286cf82a58131acd99ec156339f1e3da`;
     - `INDEPENDENT_EXECUTION_READINESS_2026_11_07.md` at `6f35dfefdabc9a6f932b27699cd02cb6863623cf`;
     - `src/origin_axiom/weave_unification_bridge.py` lines 4350–4618 and 4830–5342 at `21b293e87ff09fd64911267e9b4aa447fbfab2b9`.
   - **Proved:** None claimed in `AGY-00b1` (bounded source-dependency map only).
   - **Implemented:** Markdown documentation only (`CLAIM_DEPENDENCIES.md` labelled `PARTIAL: PURE-H4-24 CLAIM ONLY`, refreshed `RESUME.md`, and return relay). Zero Python producer or test edits.
   - **Run:** **NONE** during `AGY-00b1` (`scientific_imports = false`, `scientific_collection = false`, `scientific_execution = false`).
6. **Summary of `AGY-00b1` Findings (`CLAIM_DEPENDENCIES.md` §1–§4):**
   - **Exact provenance of the pure-$h_4$, $\chi = (0,0)$ 24-coefficient report (`N05`–`N07`):**
     - `src/origin_axiom/weave_unification_bridge.py` (`21b293e87`, lines 4357–4559 and 4841–4974) is a line-by-line NumPy translation of the physical seat's SymPy functions `spinor_complex`, `coefficient_records`, `corrected_reduced`, `pole_degree`, `line_h0`, and `total_cohomology` in `verification_coupled_half_root_kernel_2026_11_07/checks.py` (`3e58425f1`, lines 48–190).
     - Evaluating `_total_cohomology(rec, 0, chi=(0,0))` on the base curve $\Sigma_{1,1}$ (`Carrier C0`, `Model M3a/M3b`) changes the flat background from $\chi = (1,0)$ (`Model M2a/M2b`) to $\chi = (0,0)$. With $\alpha^2 = 1$ under $h_4 = \exp(i\frac{3\pi}{4}Q_{\text{em}})$ and odd spin $\eta = \mathcal{O}$ (`spin = (1,1)`), each of the 6 charge-$\pm 1/3$ colour-triplet records acquires the same 1D fixed subspace on the degree-1 middle Koszul action `(alpha * sigma_x, alpha * sigma_x)` that `checks.py` lines 308–310 already noted as a countercontrol (`fixed_columns((a[1], b[1])).cols == 1`). Consequently, every one of the 8 half-root records returns `(h0, h1, h2, h3) = (0, 3, 3, 0)` ($2$ from $H^1(S^{-3})$ + $1$ from $H^0(S^1)$), summing to $24 = 8 \times 3$ left-kernel and $24$ adjoint-kernel coefficient dimensions.
   - **Non-equivalence of Base `Model M3` ($2+1=3$ per record) and Discriminant Cover `Model M5` ($\dim W = 3$) (`N08`):**
     - Even though `weave_unification_bridge.py` line 4973 assigns `[_cohom_count_bvp(rec, 0, (0, 0)) for rec in records_8]` to a variable named `cover_3sheet_middle_counts`, that call evaluates the base-curve $\Sigma_{1,1}$ (`Carrier C0`) formula at $\chi = (0,0)$, where $3 = 2 + 1$ comes from $H^1(\Sigma_{1,1}, S^{-3}\otimes L_0) \oplus H^0(\Sigma_{1,1}, S^1\otimes L_{\text{triv}})$. It is **not** a pullback cohomology calculation on the degree-32, genus-9, 16-cusp discriminant cover $\Sigma_K$ (`Carrier C2`, `Model M5`), where $\dim W = 3$ is the dimension of the augmentation deck module under $A_{\text{disc}} \rtimes S_3$ (`1704f9e41`).
   - **Five Consequential Unresolved Edges (`E1`–`E5` in `CLAIM_DEPENDENCIES.md` §4):**
     1. **`E1` (Impact Rank 1):** Missing complete-domain $(10,6)$ up-type quark ($Q_{\text{em}} = \pm 2/3$) and $(45,1)$ zero-mode roster in the integer-root $120$ sector under pure-$h_4$, $\chi = (0,0)$ (all 8 half-root records carry only $Q_{\text{em}} \in \{\pm 1, \pm 1/3\}$).
     2. **`E2` (Impact Rank 2):** Missing cross-grading $128 \leftrightarrow 120$ physical weak current $g_{mn}(w) = g_6 \sum_i \int_\Sigma h_i\,\kappa(\psi_{i,m}^\dagger [w, \psi_{i,n}])$ computed from actual global 4-slot $M\psi = 0$ wavefunctions on $(16,4) \oplus (10,6)$ and binding the actual source gauge block $M^\dagger M$ (`V1`).
     3. **`E3` (Impact Rank 3):** Missing independent mathematical review of the complete-domain equivariant reduction at $\chi = (0,0)$ (`Model M3a/M3b` is outside `6290484f286cf82a58131acd99ec156339f1e3da`) and global all-sector coherent-lift consistency across all 248 $E_8$ sectors.
     4. **`E4` (Impact Rank 4):** Unresolved chiral vs. vector-like interpretation of the $24 = 12_{(16,4)} + 12_{(\overline{16},\overline{4})}$ left-kernel coefficients (which lie in conjugate unbroken-$U(3)$ representations $R \oplus \bar{R}$ with $\operatorname{ind} M_R = 0$ and equal adjoint-kernel counts `(0,3,3,0)`).
     5. **`E5` (Impact Rank 5):** Missing register-to-field family intertwiner separating base `Model M3` ($H^1(S^{-3}) \oplus H^0(S^1)$, dim $2+1=3$ on $\Sigma_{1,1}$) from cover `Model M5` ($A_{\text{disc}} \rtimes S_3$ augmentation deck module $W$, dim $3$ on $\Sigma_K$).
7. **Remaining proof steps and concrete next action:**
   - Await physical-seat review of `AGY-00b1` (`CLAIM_DEPENDENCIES.md` — `PARTIAL: PURE-H4-24 CLAIM ONLY`).
   - Once released by the physical seat, execute the next bounded source-only microtask **`AGY-00b2`**: complete the remaining sections of `CLAIM_DEPENDENCIES.md` (covering boundary/period response and cover transport claims) and write `INPUT_LEDGER.md` (classifying axioms, conditional model inputs, conventions, and fitted data across carrier, representation, spin, metric, normalization, boundary condition, state, measure, and field assignment), before proceeding to `AGY-01` (`LIFT_AND_DOMAIN.md`).
8. **Relevant source/proof file locations and why they are needed next:**
   - For **`AGY-00b2` (Remaining `CLAIM_DEPENDENCIES.md` & `INPUT_LEDGER.md`)**:
     - `GENESIS.md` (`217e37c4f`) and `docs/THE_TAU_READOUT_RULE.md` (`217e37c4f`): canonical statuses of `PF1`–`PF3`, `GM1`–`GM5d`, `FK1`–`FK15`;
     - `SM3_AND_GRAVITY_COMPLETION_CHECKLIST_2026_11_08.md` (`dd7490203`) and `PROGRESS_SINCE_MAIN_217E_2026_11_08.md` (`6fc5cdd0d`): independent-input categories and post-`217e37c4f` harvest scope;
     - `FREQUENCY_CORE_ANGULAR_TAIL_AND_GAUGE_WARD_RESPONSE_2026_11_08.md` and `FOUR_CONNECTION_TAIL_VERTEX_WITH_GAUSS_EXCHANGE_2026_11_08.md` (`dd7490203`): boundary/period/Gauss-exchange dependency nodes.
   - For **`AGY-01` (`LIFT_AND_DOMAIN.md`)**:
     - `FULL_E8_COMPENSATOR_LIFT_AND_REGISTER_TRANSPORT.md` (`60128166`), `PIN2_COMPENSATOR_COHERENCE_AND_ELECTROMAGNETIC_PHASE.md` (`fc67d444`), and `COUPLED_HALF_ROOT_KERNEL_AND_CORE_LIFT_SENSITIVITY.md` (`789adf75`).
9. **Scientific-execution authorization status:**
   - **NONE** (`scientific_execution_authorized = false` in `TASKS.json` at `d1b2303969050925d4b548ed21ec862208107b9f`). No scientific code was imported, collected, or executed for `AGY-00b1`.
10. **Which next task is proposed, and whether the physical seat released it:**
    - **Proposed next microtask:** `AGY-00b2` — complete `CLAIM_DEPENDENCIES.md` and `INPUT_LEDGER.md` for parent task `AGY-00`.
    - **Released by physical seat yet?** **`false`** (`next_microtask_released = false` in `TASKS.json` at `d1b2303969050925d4b548ed21ec862208107b9f`). Waiting for physical-seat review of `AGY-00b1` and next run ticket.

---

## 2. `REVIEW_FORM.md` Author Return Block for `AGY-00b1`

- **Run ticket/microtask ID, released scope and `RESUME.md` handoff path:**
  - Microtask `AGY-00b1` (`RUN_TICKET_AGY_00B1.md` at `d1b2303969050925d4b548ed21ec862208107b9f`); scope limited strictly to writing `CLAIM_DEPENDENCIES.md` (`PARTIAL: PURE-H4-24 CLAIM ONLY`, at most 12 principal nodes and 5 consequential open edges), refreshing `reports/physical_bridge_2026_09_05/agy_targeted_campaign_2026_11_08/RESUME.md` with the reading notes from `REVIEW_AGY_00A_R1_655_2026_11_08.md`, and writing a short return relay.
- **Local task ID and exact question:**
  - `AGY-00` / `AGY-00b1`: *"Precisely what supports the pure-h4 chi=0 reported 24 charged half-root coefficients, and which joins would be required before that could support a physical three-family claim?"*
- **Author branch, full commit and immutable source/design/spec hashes:**
  - Author branch: `agy/audit-2026-11-02`
  - Physical dispatch commit: `d1b2303969050925d4b548ed21ec862208107b9f` (review base: `6fc5cdd0d05e8072f6a2a64f267772d06ee94976`; physical base: `dd7490203c55bae043585f594af5a13afe634fa7`)
  - AGY accepted intake commit: `6552aec6894a4a94a2ced785ac3af8c25f801ba8` (producer baseline: `21b293e87ff09fd64911267e9b4aa447fbfab2b9`)
  - Main baseline commit: `217e37c4f37bd80998f3c3e10cad358023f58114`
  - All 28 inspected source file SHA256 hashes are tabulated in `CLAIM_DEPENDENCIES.md` §0.1.
- **Object manifest and changes from the previous accepted object:**
  - Builds directly on the accepted intake manifest `MODEL_MANIFEST.md` (`6552aec6894a4a94a2ced785ac3af8c25f801ba8`, `811956e0ff...`) and its reading notes (`REVIEW_AGY_00A_R1_655_2026_11_08.md`, `c6942f5f15...`). Adds `CLAIM_DEPENDENCIES.md` (`PARTIAL: PURE-H4-24 CLAIM ONLY`) tracing the 24-coefficient claim across 12 principal nodes (`N01`–`N12`) and 5 consequential unresolved edges (`E1`–`E5`).
- **Claim, quantifier, hypotheses and claimed evidence type:**
  - Source-dependency map only (typed as **author source/dependency trace; zero new theorem or execution certified**).
- **Reused results and exact source locations; why their domains apply:**
  - `N01`–`N05`, `N09`, `N10`: parent proofs in `weave_curved_action_2026_10_08`, `weave_physical_mass_2026_10_08`, and `word_architecture_audit_2026_10_17` (`dd7490203c55bae043585f594af5a13afe634fa7`), together with independent reviews `6290484f286cf82a58131acd99ec156339f1e3da` (for `3e58425f1e6560d9f078f306e724ed264d41884f`) and `6f35dfefdabc9a6f932b27699cd02cb6863623cf` (for `bda89f04a94d09217551cef96056f375b21c260b`) at their exact scopes;
  - `N06`–`N07`: `verification_coupled_half_root_kernel_2026_11_07/checks.py` (`3e58425f1e6560d9f078f306e724ed264d41884f`, lines 48–190 and 308–310) and its NumPy translation in `src/origin_axiom/weave_unification_bridge.py` (`21b293e87ff09fd64911267e9b4aa447fbfab2b9`, lines 4357–4559 and 4841–4974);
  - `N08`: `DISCRIMINANT_COVER_PERIPHERAL_AND_ORDER_THREE_WILSON_2026_11_08.md` (`1704f9e4153dea79d4d2ff2ea33cbe029fcb9481`).
- **Derivation and witness locations:**
  - `reports/physical_bridge_2026_09_05/agy_targeted_campaign_2026_11_08/CLAIM_DEPENDENCIES.md` §0–§4.
- **Full before/after independent-input table:**
  - Deferred to `INPUT_LEDGER.md` (`AGY-00b2`) per `RUN_TICKET_AGY_00B1.md` ("No new derivation of the lift, new roster calculation, INPUT_LEDGER.md..."). Canonical count remains `0 of 19`.
- **Physical identification supplied, derived, or still missing:**
  - Supplied: compact $\mathfrak{e}_8$, hyperbolic cusp metric $g = \Omega^2(dx^2 + dy^2)$, quaternion flavour bundle $F$, conditional odd spin $\eta = \mathcal{O}$, continuous-$\operatorname{Pin}_2$ phase $h_4 = \exp(i\frac{3\pi}{4}Q_{\text{em}})$, and changed flat background $\chi = (0,0)$ in `Model M3a/M3b`.
  - Still missing (`E1`–`E5`): integer-root $(10,6)$ up-type quark ($Q = \pm 2/3$) complete-domain zero-mode roster (`E1`), cross-grading $128 \leftrightarrow 120$ physical weak current from global 4-slot $M\psi = 0$ modes (`E2`), independent review of the $\chi = (0,0)$ complete-domain reduction and all-sector consistency (`E3`), chiral vs. vector-like mass/coupling differentiation of $R \oplus \bar{R}$ (`E4`), and register-to-field family intertwiner separating base `Model M3` from cover `Model M5` (`E5`).
- **Countercontrols and the mistake each must reject:**
  - Preserved in `CLAIM_DEPENDENCIES.md` §1–§4:
    1. Reject extending the `6290484f2` review of $16/18$ modes ($\chi_3 \neq 0$) to the $\chi = (0,0)$ 24-mode claim (`N05`, `N07`);
    2. Reject equating base `Model M3` ($2+1=3$ per record from $H^1(S^{-3}) \oplus H^0(S^1)$ on $\Sigma_{1,1}$) with cover `Model M5` ($\dim W = 3$ on $\Sigma_K$) merely because $3 = 3$ or because `weave_unification_bridge.py` line 4973 names a base-curve list `cover_3sheet_middle_counts` (`N08`, `E5`);
    3. Reject claiming three complete families from half-root records that carry only $Q_{\text{em}} \in \{\pm 1, \pm 1/3\}$ without solving $(10,6)$ ($Q_{\text{em}} = \pm 2/3$) (`N09`, `E1`);
    4. Reject treating a single-sector $128 \times 128$ radial inner product (`g_mat_3`) or $6\times 6$ Kronecker product `np.kron(tau_plus, g_mat_3)` as the cross-grading $128 \leftrightarrow 120$ Lie-bracket weak current (`N10`, `N11`, `E2`).
- **Required source-complete reviewer, main acceptance and admission pins:**
  - Physical seat (`audit/physical-bridge-2026-09-05`) for checkpoint review of `AGY-00b1` and release of `AGY-00b2`; no scientific execution admission requested.
- **Actual command/environment and raw first output, if admitted and run:**
  - Not applicable (`scientific_execution = false`).
- **Failed attempts, limitations and unresolved alternatives:**
  - Documented in `CLAIM_DEPENDENCIES.md` §2 (`N07`–`N11`) and §4 (`E1`–`E5`).
- **What downstream statements would become justified if accepted:**
  - Acceptance of the partial dependency trace `AGY-00b1` and release of `AGY-00b2` (remaining `CLAIM_DEPENDENCIES.md` sections and `INPUT_LEDGER.md`).
