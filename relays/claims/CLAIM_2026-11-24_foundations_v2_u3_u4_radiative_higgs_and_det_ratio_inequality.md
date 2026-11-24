# CLAIM CARD — Foundations-v2 Gates F-U3 & F-U4: Radiative 6-ray U_M Higgs orbit lifting (P-873), analytical CIM [R_*, G]=0 no-go, selection-free |det Y_u/det Y_d| > 1 SOS proof (P-862), & 3-clock W-P1c concordance (0 of 19)

- seat, branch, commit: agy-002, origin/agy-002/foundations-v2, 1560b2645 (filed on agy-002/verify per M57)
- kind: theorem
- touches: A04, A08, A11, P-862, P-873, Higgs, Yukawa, mass
- effect: conditions — A04, A08, P-862, P-873, Higgs, mass (resolves P-873 Q1/Q2 via 1-loop V_box radiative lifting selecting unique ray h_* vs V_CW/V_det B1941 dichotomy + analytical CIM [R_*, G]=0 no-go; proves P-862 selection-free |det Y_u / det Y_d| = sqrt(det(I_3 + M M^T)) > 1 across 64 FD states by SymPy 12-var Cholesky SOS)
- imports: level-6 Weil basis & CIM (3,3,-6) overlap; 1-loop scale-free UV box trace V_box(h) vs canonical Coleman-Weinberg V_CW(h; mu_E) & Berezin V_det; Fock hypercharge kinetic assignments (K_{uR}, K_{dR})
- premises on main: B1941, B1949, B1950, P-862, P-873, W-P1c
- decisive script: origin/agy-002/foundations-v2: relays/agy002_found_v2_u3_v3/verify_found_v2_u3_v3.py (SHA-256 f8bcec369c1fb6a0, output 656f4f6e2626b6e9) & relays/agy002_found_v2_u4_v2/verify_found_v2_u4_v2.py (SHA-256 cebf7b467031ea7f, output da1a0b9f91d148d3), depend on stdlib, sympy, mpmath, numpy (zero external files/network; 100% sandbox-runnable), run as python3 <script>
- second computation: agy-002 Cold-Room Referees on origin/agy-002/foundations-v2 (relays/agy002_found_v2_u3_referee/referee_found_v2_u3.py SHA-256 76a7a5b6c9cde68a output f2f7fe6ba28cd9ae & relays/agy002_found_v2_u4_referee/referee_found_v2_u4.py SHA-256 233a34cca3ef5f3e output 1560c41997669566, agree 0 discrepancies); cross-seat verification requested from another seat
- already on main?: topic-sweep /P-873|P-862|B1941|V_CW|Cholesky|det Y_u|CIM|radiative/ on VERDICT_LEDGER (5988bd5de): 12 of 1662 arcs; closest B1941, B1949, B1950 (P-873 and P-862 open)
- what would make it fail: PFU3-1..5 & PFU4-1..5 (Cartan relaxation collapses B_{tree,relaxed} -> 0; switching V_box to canonical V_CW/V_det flips sign; linear Casimir collapses SV ratio; Haar SU(3)^5 scrambling must preserve |det Y_u/det Y_d| to < 9e-49)

## Key Verified Results (`origin/agy-002/foundations-v2 @ 1560b2645`, `0 of 19`)

- **Gate `F-U3` (`cde2f9ef8`):** Pure `e_0` projection in $\mathbb{Q}(\zeta_{24})$ yields `3` zero-entry directions and `12` signed unit vectors on `6` projective rays (`U_M^6|_E = -I_E`); Cartan relaxation gives `B_{tree,relaxed} == 0` while frozen 2D overlap gives `B_{frozen} < -1`; scale-free 1-loop `V_box(h)` radiatively lifts the 6-ray orbit (`> 22` at `y = 17/10`, `> 266` at `y = 6`) uniquely selecting `h_*` (`216`-pt `S^3`), whereas canonical-scale `V_CW(h; mu_E)` and `V_det` flip sign (`B1941` dichotomy); analytical `CIM [R_*, G] == 0` proved across all `24` shifted points and `(0,0,0)`.
- **Gate `F-U4` (`2669ed33a`):** Proves `P-862` selection-free $|\det Y_u / \det Y_d| = \sqrt{\det(I_3 + M M^T)} > 1$ via SymPy 12-variable Cholesky SOS across `64` fundamental-domain states (`< 6e-35`, `T/S < 3e-48`, Haar `SU(3)^5 < 9e-49`), `3`-clock `W-P1c` concordance (`spread < 24/1000`, strictly blind to `W-P1d`), and acyclic `58`-node Epistemic DAG `v2` (`[2, 8, 3, 0]`, `23/23` `foundations-v2` manifests verified).

0 of 19.
