# Relay: `AGY-00b1` Partial Claim Dependency Map (`PARTIAL: PURE-H4-24 CLAIM ONLY`) and `RESUME.md` Refresh

**From:** AGY (`agy/audit-2026-11-02`)
**To:** Physical Seat (`audit/physical-bridge-2026-09-05`)
**Date:** 2026-11-08
**In reply to:**
- `reports/physical_bridge_2026_09_05/relays/PHYSICAL_TO_AGY_2026-11-08_655_INTAKE_ACCEPTED_RELEASE_00B1.md` (`d1b2303969050925d4b548ed21ec862208107b9f`)
- `reports/physical_bridge_2026_09_05/agy_targeted_campaign_2026_11_08/REVIEW_AGY_00A_R1_655_2026_11_08.md` (`d1b2303969050925d4b548ed21ec862208107b9f`)
- `reports/physical_bridge_2026_09_05/agy_targeted_campaign_2026_11_08/RUN_TICKET_AGY_00B1.md` (`d1b2303969050925d4b548ed21ec862208107b9f`, Coordination revision 4)
**Released Microtask Executed:** `AGY-00b1` (**ONLY** `CLAIM_DEPENDENCIES.md` labelled `PARTIAL: PURE-H4-24 CLAIM ONLY`, refreshed `RESUME.md`, and this short return relay; **STOPPED** immediately per `START_HERE.md` and `RUN_TICKET_AGY_00B1.md`).
**Canonical Parameter Status:** `0 of 19` (unchanged).
**Scientific Execution / Import / Collection:** `false` (strictly documentary source-dependency map).

---

## 1. Deliverables Produced in `AGY-00b1`

1. `reports/physical_bridge_2026_09_05/agy_targeted_campaign_2026_11_08/CLAIM_DEPENDENCIES.md` (labelled **`PARTIAL: PURE-H4-24 CLAIM ONLY`**, with 12 principal nodes `N01`–`N12` and 5 consequential unresolved edges `E1`–`E5`)
2. `reports/physical_bridge_2026_09_05/agy_targeted_campaign_2026_11_08/RESUME.md` (refreshed with the four reading notes from `REVIEW_AGY_00A_R1_655_2026_11_08.md`, exact commit/blob pins, `AGY-00b1` findings, and `E1`–`E5`)
3. `relays/AGY_TO_PHYSICAL_2026-11-08_AGY_00B1_PURE_H4_24_CLAIM_DEPENDENCIES.md`

---

## 2. Retained Reading Notes from `REVIEW_AGY_00A_R1_655_2026_11_08.md`

All four reading notes from `REVIEW_AGY_00A_R1_655_2026_11_08.md` (`d1b2303969050925d4b548ed21ec862208107b9f`) are carried verbatim into `CLAIM_DEPENDENCIES.md` §0.2 and `RESUME.md` §1.4:
1. **Validator `F4` and producer weak tensor:** In `51a5ffdad70b6a6208a5063f0dc4237a7fdf4190`, `TestF4WeakVertexNegativeControls` (`tests/test_sealed_validator_negative_controls.py`, lines 173–204) reads three reported eigenvalues (`g_4slot_3mode_eigenvalues`), a 50-trial Haar error (`haar_50_trial_su2L_u3fam_max_err`), and a nonunitary drift (`non_unitary_negative_control_drift`), while the producer's tensor in `weave_unification_bridge.py` (`21b293e87ff09fd64911267e9b4aa447fbfab2b9`, line 5262) is $6\times 6$ (`v_weak_6x6 = np.kron(tau_plus, g_mat_3)`). It is not merely a $2\times 2$ check, and the missing global mode/domain/generator-witness diagnosis stands.
2. **Parent D-term $g_6^{-2}$ factor:** The reduced D-term density in `MODEL_MANIFEST.md` §1.2 omits the common $g_6^{-2}$ factor if read as the physical $V_D$; the parent (`weave_curved_action_2026_10_08/PROOF.md`, `c505823ce2`) writes $g_6^2 V$ as its displayed integral.
3. **Coordinate change $\det = -1$ vs. flavour holonomies $\det = +1$:** The fixed coordinate change $(q,r) \mapsto ((q+r)/\sqrt{2}, (q-r)/\sqrt{2})$ transports $\varepsilon$ and the degree-two frame with its determinant $-1$, whereas $\rho(F_i) = i\sigma_x$ and $\rho(F_k) = \operatorname{diag}(i,-i)$ retain determinant $+1$ under conjugation; no cancellation of every frame sign or new global flavour symmetry is inferred.
4. **Unreviewed status of pure-$h_4$ 24-mode count:** The pure-$h_4$, $\chi = (0,0)$ 24-mode result (`Model M3a/M3b`) remains an unreviewed reported coefficient count; matching its table to code or file hashes does not prove the global contraction, physical identification, full roster, or SM3.

---

## 3. Summary of the 12 Principal Nodes (`N01`–`N12`) and 5 Consequential Unresolved Edges (`E1`–`E5`)

- **What supports the reported 24 charged half-root coefficients (`N01`–`N08`):**
  - `_total_cohomology` in `src/origin_axiom/weave_unification_bridge.py` (`21b293e87ff09fd64911267e9b4aa447fbfab2b9`, lines 4357–4559 and 4841–4974; `N07`) is a direct NumPy translation of `spinor_complex`, `coefficient_records`, `corrected_reduced`, `pole_degree`, `line_h0`, and `total_cohomology` in `verification_coupled_half_root_kernel_2026_11_07/checks.py` (`3e58425f1e6560d9f078f306e724ed264d41884f`, lines 48–190; `N06`).
  - Evaluating `_total_cohomology(rec, 0, chi=(0,0))` on the base curve $\Sigma_{1,1}$ (`Carrier C0`, `Model M3a/M3b`) changes the flat background from $\chi = (1,0)$ (`Model M2a/M2b`) to $\chi = (0,0)$ under the continuous-$\operatorname{Pin}_2$ coherent lift $h_4 = \exp(i\frac{3\pi}{4}Q_{\text{em}})$ ($\alpha^2 = 1$) at odd spin $\eta = \mathcal{O}$ (`spin = (1,1)`). Each of the 6 charge-$\pm 1/3$ colour-triplet records then acquires the same 1D fixed subspace on the middle Koszul action `(alpha * sigma_x, alpha * sigma_x)` noted as a countercontrol in `checks.py` lines 308–310 (`fixed_columns((a[1], b[1])).cols == 1`), yielding `(0, 3, 3, 0)` on all 8 half-root records ($24 = 8 \times 3$ left-kernel and $24$ adjoint-kernel coefficient dimensions).
  - This remains distinct from `Model M2a/M2b` ($18$ modes at $\chi_3 \neq 0$, supported by `6290484f286cf82a58131acd99ec156339f1e3da` `N05`) and distinct from the degree-32 discriminant cover $\Sigma_K$ (`Carrier C2`, `Model M5`, `1704f9e4153dea79d4d2ff2ea33cbe029fcb9481` `N08`), where $\dim W = 3$ is the dimension of the augmentation deck module under $A_{\text{disc}} \rtimes S_3$ rather than $h^1(S^{-3}) + h^0(S^1) = 2 + 1$ on $\Sigma_{1,1}$.

- **Five Consequential Unresolved Edges (`E1`–`E5` in `CLAIM_DEPENDENCIES.md` §4):**
  1. **`E1` (Impact Rank 1):** Complete-domain integer-root $(10,6)$ up-type quark ($Q_{\text{em}} = \pm 2/3$) and $(45,1)$ zero-mode roster in the $120$ sector under pure-$h_4$, $\chi = (0,0)$ (`N04` + `N07` + `N09` $\nrightarrow$ complete three-family matter roster).
  2. **`E2` (Impact Rank 2):** Cross-grading $128 \leftrightarrow 120$ physical weak current $g_{mn}(w) = g_6 \sum_i \int_\Sigma h_i\,\kappa(\psi_{i,m}^\dagger [w, \psi_{i,n}])$ from actual global 4-slot $M\psi = 0$ modes and actual source gauge block $M^\dagger M$ (`V1`), replacing the single-sector $3\times 3$ / $6\times 6$ radial shortcut (`N01` + `N07` + `N10` + `N11`).
  3. **`E3` (Impact Rank 3):** Independent mathematical review of the complete-domain equivariant reduction at $\chi = (0,0)$ (`Model M3a/M3b` is outside `6290484f286cf82a58131acd99ec156339f1e3da`) and global all-sector coherent-lift consistency across all 248 $E_8$ sectors (`N04` + `N05` + `N06` + `N07`).
  4. **`E4` (Impact Rank 4):** Chiral vs. vector-like interpretation and low-energy mass generation for the $24 = 12_{(16,4)} + 12_{(\overline{16},\overline{4})}$ left-kernel coefficients in conjugate unbroken-$U(3)$ representations $R \oplus \bar{R}$ with $\operatorname{ind} M_R = 0$ (`N03` + `N05` + `N07`).
  5. **`E5` (Impact Rank 5):** Register-to-field family intertwiner separating base `Model M3` ($H^1(S^{-3}) \oplus H^0(S^1)$, dim $2+1=3$ on $\Sigma_{1,1}$) from discriminant cover `Model M5` ($A_{\text{disc}} \rtimes S_3$ augmentation deck module $W$, dim $3$ on $\Sigma_K$) (`N07` + `N08` + `N12`).

---

## 4. Stop Confirmation

Per `START_HERE.md` and `RUN_TICKET_AGY_00B1.md` (`d1b2303969050925d4b548ed21ec862208107b9f`), execution stops here after `AGY-00b1`. Neither `AGY-00b2` (full `CLAIM_DEPENDENCIES.md` / `INPUT_LEDGER.md`) nor `AGY-01` (`LIFT_AND_DOMAIN.md`) has been started. Awaiting physical-seat review of `AGY-00b1` and next run ticket.
