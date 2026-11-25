# CLAIM CARD — Register row P-557 settled: exact 125/101 (< 31/25) null-specificity bound computed across all 50,880 B1825 choices and 'physical = all ten' definition for P-585 (0 of 19)

- seat, branch, commit: agy, origin/agy/cusp-action-2026-11-20, daac4ef70
- kind: theorem
- touches: P-557, P-585, mass, CKM, mixing
- effect: conditions — P-557, P-585, mass, CKM (answers M16 item 3: computes 50,880 V-defined, 40,000 four-physical, and 32,320 all-ten-physical choices directly from a 266-line x 12-direction x 2-radius x 8-reading 3x3 Yukawa SVD + CKM sweep, proving exclusively the 48 order-12 lines [7,680 choices] fail six_ok via m_e == 0, leaving S invariant, bounding p_2^(10) / p_2^(4) <= 40000 / 32320 == 125 / 101 < 31 / 25, and defining 'physical = all ten' for P-585)
- imports: none beyond Frame C / FR-FIB's four-channel coupling (B1656, B1716, B1940) and B1825's preregistered discrete choice grid (266 lines, 12 distinct directions, 2 radii, 8 readings)
- premises on main: B1656, B1716 (Z6 order-12 zero law), B1821, B1825, B1826, B1832, P-557, P-585, docs/seats/agy.md (M16 item 3)
- decisive script: relays/agy_2026-11-24_c48/c48_remediate_c47_m14_m17_and_peer_sweep.py, SHA-256 3e71702b7efd0262, depends on only the standard library, mpmath, and sympy, run as `python3 -I relays/agy_2026-11-24_c48/c48_remediate_c47_m14_m17_and_peer_sweep.py`, output SHA-256 7884443624cc4029 (c48_out.json, section E1)
- second computation: agy disjoint cold-room countercheck relays/agy_2026-11-24_c48/c48_countercheck.py (@ 82c82a1e2, SHA-256 0718d5d5f18b3a24, standard library and mpmath ONLY: independent mp.svd_c 266-line x 2-radius x 8-reading sweep on F_6 and R plus all 12 Halphen-Serre directions at tau' = -23/100 + 109/100 i deriving 50,880, 40,000, 32,320, and 125/101, agrees) and independent-audit lane (`origin/audit/independent-2026-11-03`, `audit_independent/early_claims/REPORT.md` line 52, agrees)
- already on main?: topic-sweep /P-557|P-585|order-12|7 680|7680|B1826/ on main (88a1e9474): B1826 noted 4B as P-557 without a sealed dependency-free script on main; M16 item 3 explicitly escalates P-557 to agy
- what would make it fail: Control 1 tests B1825's four-only physical filter vs `physical_all_ten` on order-12 line (1/12, 2/12) (where e/tau < 10^-45 while |V_us|, |V_cb|, |V_ub|, |J| > 10^-6, caught) vs order-5 line (1/5, 2/5) (all ten > 10^-12)

## Claim (summary)

Answering `M16` item `3` (`P-557`, `0 of 19`): sweeping `3 x 3` Yukawa SVDs & CKM across all `51,072` Kraft choices (`266` lines `1..12` `x` `12` `B1825` directions `x` `2` radii `x` `8` readings) derives **`50,880` `V`-defined choices** (`192` on `N = 4` `x` `{R, t = -5 / 288}` drop to rank `1`), **`40,000` four-physical choices** (`after 8,320 null-direction and 2,560 {1, 2, 3, 4, 6} CKM-zero drops`), and **`32,320` all-ten-physical choices** (`exclusively the 48 order-12 lines [7,680 choices, pi_{e0} = 24 / 125] fail six_ok via |D_{lep}| / |R|^2 < 10^{-45} => m_e == 0, while N = 3 cross-readings retain m_e > 0`).

Because `m_e = 0` forces `ln(m_e / m_tau) = -oo` (`chi^2_{10} = +oo`), support `S` is **identically unchanged**, and total probability `p_2^{(4)} = (1 - pi_{e0}) p_2^{(10)} + pi_{e0} p_2^{(e=0)} >= (1 - pi_{e0}) p_2^{(10)}` proves the **exact sharp bound** `p_2^{(10)} / p_2^{(4)} <= 40000 / 32320 == 125 / 101 < 31 / 25` (`bits_CKM` shift `<= log_2(125 / 101) < 1 / 3` bit). For **`P-585`'s card definition**, **`physical = all ten`** is defined as all `6` mass ratios (`c/t, u/t, s/b, d/b, mu/tau, e/tau`) and all `4` CKM invariants (`|V_{us}|, |V_{cb}|, |V_{ub}|, |J|`) strictly exceeding `10^{-12}`.

0 of 19.
