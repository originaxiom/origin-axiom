# Verification of B1672 (2026-10-20). Scripts: v1..v8.py, logs *_run.txt in this folder. Nothing outside this folder touched.

| Thm | Grade | Reason | Evidence |
|---|---|---|---|
| Sec.0 shears | B (with a notation fix) | L_ab^-1 o L_ba = conj(a^-1) (b -> a^-1 b a), R_ba^-1 o R_ab = conj(b^-1) (a -> b^-1 a b), both orders and composition conventions. Four shears all have det H1 = +1, L_ab, R_ab give SL2(Z), Inn(F2) is generated, so the group is SAut(F2)=Aut+(F2). "Aut+(F2) = Mod(M_{1,2})" is ill-typed: M_{1,2} is a moduli space; correct is Aut+(F2) = Mod(S_{1,2}) = pi_1^orb(M_{1,2}) (Birman), not recomputed here | v1_run.txt |
| 1 | A (scoped) | L_6 ~ (chi_eta^3 rho_T) (x) V_2 holds: Hom dim 2 at k=3 (1 at k=15); level-2 theta doublet (theta_3(2t), -i theta_2(2t)) has T = diag(1,i), S fit residual 1e-31, eigenvalues match chi^3 x V_2. New relative to B1641 Cell H (which tested only sub/quotient). But the module is still 2+4 under Mp2(Z); the sequence is of holomorphic bundles with a tau-dependent subbundle, pointwise exact for any nonzero Theta; it fixes no invariant Lambda_+ | v6_run.txt, v5b_run.txt |
| 2 | D (asserted); B for the count | "Leray E2 degeneration" is hard-coded True (script line ~ results["Theorem_2"]); it is automatic anyway for a base of complex dimension 1. No 4D Dolbeault-Dirac operator, no GRR on M_{1,2}, no boundary treatment is computed. What is computed: -chi(T,3/2+12n)+chi(sub,1+12n) = n(dim-3) from the modular-form dimension formula, i.e. B1606/W22 on the modular curve. "H^2(Mbar_{1,2},Z) = Z" is false (rank 2: lambda and delta_{0,{1,2}}) | w45.chi inspection |
| 3 | D for irreducibility and "forced"; A (minor) for the sign lifts | On W10's V=T+Tbar: RL^2R = P_a, LR^2L = P_b exactly; <M_L,M_R> has order 96 and already contains P_a, P_b (so adding them changes nothing). But this module has T invariant, commutant dim 2, <chi,chi>=2: REDUCIBLE. On the puncture module L_6 (the arc's own blocks_action), the positive-word group is 2O (order 48, commutant 2) and RL^2R acts as diag(i,-i,...), not P_a. Irreducibility (order 192, commutant 1) appears only when P_a, P_b are added by hand: that is B1606 P4 and paper Prop. 24. The arc's "Pa_breaks_V2 = 1.333" and its lock test (hand-typed matrices) mix the two modules. Irreducible would force {0,6} only if Lambda_+ is required invariant under the grading: stated in the record as undecided | v1_run.txt, v2_run.txt, v7_run.txt |
| 4 | A (small), with a choice | chi_eta^3(Delta^4) = -1, Delta^4 = -I_3 on T, [P_a,P_b^-1] = I (P_a, P_b commute, so trivial). Twisting L,R by e^{+-i pi/4} gives Delta^4 = I, order 24. Stronger than the arc: I checked well-definedness over all words in the 8 shears to length 7 (67,284 distinct automorphisms): untwisted 2,950 conflicts, twisted 0. So Gate 12 (P-074) closes to that length. Choice: every odd k works for coherence; k=3 selected for order 24, and "= K^{1/2} of Y" is a reading | v3_run.txt, v3_N7_run.txt, v4_run.txt |
| 5 | B/C | Branching of 248 under SU6xSU2xSU3 is classical (Slansky 1981, Table; dims 248). Z6 generator (zeta6,-1,omega3) acts trivially on every piece, cube = (-I6,-I2,+I3): correct. But central elements act trivially on the adjoint, so "su(2)_w stays unbroken" is empty. Here 6 = family T+Tbar and SU(3) factor = colour; Thm 6 uses SU(3) factor = family and colour inside the 6: incompatible frames. J = diag(1^3,-1^3)/6 is not Y | v4_run.txt |
| 6 | C | (E6 x SU3_T)/Z3: 248 = (78,1)+(1,8)+(27,3)+(27b,3b) is classical (Slansky; Adams). Y=diag(1/6^3,-1/2,1/2,-1/2) is traceless; on 27=(15bar,1)+(6,2) it gives exactly SM 16 plus 10+1 exotics (checked). That is textbook E6; "polarising V_2 along Theta_2(inf)" is never computed, y_6 is typed in; the "5 charges" are sums of typed entries. Matter in (27,3_T) and S4 inside SU(3)_T are identifications | v4_run.txt |
| 7 | D/C | The "non-Sturmian" det-1 pairs are mostly non-invertible endomorphisms (16 of 55 pairs, length<=4, are not bases), not Aut+(F2); T is invariant under all four shears (leak 0), so the "T to Tbar" mixing comes from these. Splitting by M1+M2 with coefficient 1 is generic and no mass is derived | v7_run.txt, v8_run.txt |

Lock test: passes (5), but no bite. Live tests never import the verifier or repo code; they test hand-typed matrices and constants (comm = np.eye(3), Delta4 = -np.eye(3), BL/T3R arrays). Stored tests read booleans from an editable JSON. Would pass if the claims were false.

Banking rules: no PREREGISTRATION, no seal, no ARTIFACT_HASHES, no "Seen first", no "Disclosed"; verdict.identifications = [] although it uses several; depends_on lists B1600-line arcs but not B1600. WORKING_RULES sections "Hash first", "SEE THE REPO AND THE LITERATURE FIRST". Register P-184 was flipped to DONE.

## What can be banked, scoped
- Sec.0: shears generate Aut+(F2); the two inner relations (B).
- T3 sign lift only: RL^2R, LR^2L lift to P_a, P_b on W10's V; order 96 (extends B1600/B1641 O1).
- T1: Mp2(Z)-isomorphism L_6 ~ (chi_eta^3 rho_T) (x) V_2 and the theta-doublet bundle sequence; no invariant-domain consequence.
- T4: lifts cohere on Aut+(F2) after an odd eta-character twist, tested to shear length 7 (a theorem would need the presentation). Closes P-074 at that scope.
- Verdict: PARTIAL (A and B items), creates_law false, identifications listed. Not PROVED.

## What Table 1 may say
- grammar GM1-GM5a: keep "postulated"; add "four shears generate Aut+(F2) (B1672)".
- positivity: restore old row (the B1673 wording is unexamined here).
- triplet postulate: keep old row. Not derived (choice: matter in (27,3_T), S4 in SU(3)_T).
- one cusp unit: keep old row.
- extreme boundary domain: keep "chosen". The 192-group irreducibility needs the parity grading (B1606 P4).
- M_{1,2} as surface: "a reading; coherence of lifts on Aut+(F2) closed by an odd eta twist (B1672 T4, to word length 7)".
- index as generation count: keep old row.
- hypercharge dictionary: keep old row (Y is typed; E6 branching classical).
- index formula: keep "taken as stated (B1606)".
- s07 F3 sentence and s06 "recent resolution": remove.
- B1673 rows in the same diff (positivity, end condition, modulus, s08 subsection): not examined; hold.
