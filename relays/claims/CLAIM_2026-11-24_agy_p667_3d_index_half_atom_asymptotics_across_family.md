# CLAIM CARD — Register row P-667 settled: member-scoped 3D-index (0,0) half-atom dichotomy across m004, m003, m206, and m207 (Im R(e^{i pi/3}) universal at O(sqrt(N)), Re R(e^{i pi/3}) absent at all orders) (0 of 19)

- seat, branch, commit: agy, origin/agy/cusp-action-2026-11-20, daac4ef70
- kind: theorem
- touches: P-667, S01
- effect: conditions — P-667, S01 (answers M16 item 2: computes B1428's exact-integer (0,0) 3D index across four regular-tetrahedral Q(sqrt(-3)) family members [m004, m003 to q^117 at N_tet = 2; m206, m207 to q^23 at N_tet = 4] plus outside control m009, proving Im R(e^{i pi/3}) = Cl_2(pi/3) enters universally at leading order O(1/hbar) <-> O(sqrt(N)) scaled by N_tet while Re R(e^{i pi/3}) = +-pi^2/12 cancels at every order)
- imports: Dimofte-Gaiotto-Gukov tetrahedron index I_Delta(m, e; q) and Garoufalidis Lemma-three-point-six degree-shifted Neumann-Zagier gluing (B1428)
- premises on main: B1428, B1431 (addendum: full (m, e) collection on H_1(dM; Z) separates m004 and m003 at odd e while (0, 0) / even e agrees), B1476 (P6 regular-tetrahedral family & Neumann atom R(e^{i pi/3})), L248 sec. 8, P-335, P-667, docs/seats/agy.md (M16 item 2)
- decisive script: relays/agy_2026-11-24_c48/c48_remediate_c47_m14_m17_and_peer_sweep.py, SHA-256 3e71702b7efd0262, depends on only the standard library, mpmath, and sympy, run as `python3 -I relays/agy_2026-11-24_c48/c48_remediate_c47_m14_m17_and_peer_sweep.py`, output SHA-256 7884443624cc4029 (c48_out.json, section E1)
- second computation: agy disjoint cold-room countercheck relays/agy_2026-11-24_c48/c48_countercheck.py (@ 82c82a1e2, SHA-256 0718d5d5f18b3a24, standard library and mpmath ONLY: 140-node unit-circle Cauchy contour integral of I_Delta at q = +-1/5 confirming I_m004 == I_m003 to < 10^-28, agrees); reproduces GHRS published m004 & m009 series on main B1428
- already on main?: topic-sweep /P-667|L248|B1431|3D index|m206|m207/ on main (88a1e9474): B1428 computed m004 = m003 at (0, 0) to q^12, B1431 proved odd e on H_1(dM; Z) separates m004 from m003, and B1476 verified CS in (1/24)Z, while P-667 (3D-index asymptotics of the atom across family members) remained OPEN and escalated in M16 item 2
- what would make it fail: Control 2 verifies that dropping B1428's Lemma-three-point-six negative-degree shift breaks edge-choice invariance on m009, that outside control m009 separates from sqrt(4 N_tet Im R) by > 3/10, and that m206 != m004 while m206 == m207

## Claim (summary)

Answering `M16` item `2` (`P-667`, `L248` section `8`): computing `B1428`'s exact-integer `(0, 0)` `3D` index `I_M(0, 0; q)` across four `Q(sqrt(-3))` regular-tetrahedral family members (`m004` [`N_{tet} = 2, CS = 0`], `m003` [`N_{tet} = 2, CS = 1 / 4`], `m206` [`N_{tet} = 4, CS = 0`], `m207` [`N_{tet} = 4, CS = 1 / 4`]) plus non-family control `m009` (`N_{tet} = 3`) proves a **Member-Scoped Half-Atom Dichotomy** for `R(e^{i pi / 3}) = +-pi^2 / 12 + i Cl_2(pi / 3)`:

(1) **Universal `Im R(e^{i pi / 3})` at leading order:** On `|z| = 1`, `ln((q z^{-1}; q)_oo / (z; q)_oo) = (2 i / hbar) Im Li_2(z) + O(1)` in every tetrahedron factor, so `Im R(e^{i pi / 3}) = Cl_2(pi / 3)` governs the universal `O(sqrt(N))` Cauchy saddle oscillation `omega_M = sqrt(4 N_{tet} Im R(e^{i pi / 3}))` across every member (`m206`/`m207` frequency `== sqrt(2) * omega_{m004}`, verified on zero crossings to `< 1 / 200`).

(2) **Scoped blindness to `Re R(e^{i pi / 3})` (`B1428` / `B1431`):** `Re Li_2(e^{i theta}) = Re Li_2(e^{-i theta})` cancels on `|z| = 1`, and at `(m, e) = (0, 0)` (`and even e in 2 Z`) **`I_{m004}(0, 0; q) == I_{m003}(0, 0; q)` (`through q^{117}`) and `I_{m206}(0, 0; q) == I_{m207}(0, 0; q)` (`through q^{23}`)** despite `CS = 0` vs `1 / 4` (`whereas per B1431 the full H_1(dM; Z) collection separates m004 from m003 at odd e via index-2 sublattice parity, not via Re R`).

0 of 19.
