# The independent lane re-run (hand-back saved by main, 2026-11-04)
All 22 committed outputs reproduce (21 byte-identical; scan_results.json value-identical, timing fields differ). Re-run
material: COMPARISON.json, rerun/, runjob.py, compare.py in this folder. Findings main has not carried:
1. B1826 § 1.3's population: the 52 of 250 are hierarchical rows WITH SM-ordered CKM magnitudes (0.05 < |V_us| < 0.5,
   |V_cb| < 0.2, |V_ub| < |V_cb| < |V_us|); among all 1 127 hierarchical rows (up steeper than down, |V_us| > 0.05) 719 (64%)
   already have the measured corner order; over all rows 0.498; inversion concentrated in SM-ordered rows (198 of 250; 32 of 33
   realistic). c_nogo_scan2.py reproduced byte-identical.
2. P-585 exposures uncounted: agy's Theorem 8 inter_sector_scales (sm_19_gate.py ~754-797, tan_beta_golden l. 757) on its
   FR-COV (2/5, 0) Golden cell against PDG (y_b/y_t-type and y_tau/y_b-type); the independent lane's sensitivity_check.py and
   AUDIT_REPORT lines 110-111, 121 (firewalled; not read by main).
3. Theorem 14 census: 3 classes of 16 for FIXED probes (stabiliser 2D4, order 16); co-moving probes identify all 48; Part C's
   compensators order 8 in PSO(10), 16 in SO(10)'s 10.
4. LOOK_LEDGER lacks this lane's data-touching scans (tau map, 600 closed forms, 2 048 characters, the a0-plane chi2_8, the
   371 293-vector gamma search, the no-go scan's realistic cut, PMNS/NuFIT pulls, T12's M_t/M_h against PDG).
5. agy's own checks fail at 951998a73: pytest KeyError 'B_half_shift_matrix' (l. 534); hostile_referee_audit.py NameError
   th2_mp (l. 1087).
6. P-559's '18 of 171': 51 untested (3 alpha in Z/2) so 18 of 120; alpha and 1-alpha counted separately (9 distinct); rates from
   a closed form fitted on 8 lines.
7. The lane's Planck numerology: n_hits = 1 in its output; agy's formula exactly on the 0.194% threshold; '2.8 expected'
   computed nowhere; chance-level conclusion survives.
8. FR-COV's a0 (chi2_8 277.2 -> 1287 at agy's a0; best 257.5; >= 514 wherever the corner flips; 55% of |a0| <= 1 flips) for
   P-558; T10 selects nothing (all five (2/5, j/5) lines equal after tau -> tau + 8m); T12's matched M_h 120.2, M_t 169.3 from
   the lane's own integrator; P-557's 7 680 is arithmetic.
9. Minor: the tau-map island touches Re tau = 0.5; 600 closed forms are 529 values, 30 passes 23 tau; Theorem 3 = B1659's J1,
   Theorem 4 = B1691's C1; relay-vs-code mismatches (delta_CP, sin delta, eta_B).
Firewall disclosure: AUDIT_REPORT lines 110, 111, 121 entered the verifier's context while reading in full; nothing copied.
