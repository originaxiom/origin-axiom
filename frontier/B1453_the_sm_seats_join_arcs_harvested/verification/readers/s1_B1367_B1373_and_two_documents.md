# Reader s1 — a read-in-full report on the SM seat's arcs at 800ed4e5 (2026-10-02)

*A reader pass by a delegated reader instance: read only, nothing run. Its statements are a reader's, not main's; main's own checks are in the arc's FINDINGS.*

READ-ONLY REPORT on <pinned checkout of the seat's branch at 800ed4e5> (frontier B1367..B1373, docs/THE_VERDICT_OF_THE_OBJECT_2026-09-16.md, docs/THE_KILL_TESTS_2026-09-27.md).
Read in full: all 7 FINDINGS.md, 7 arc_verdict.json, all committed run logs (*_run.txt) for each arc, both docs. No PREREGISTRATION/PREDICTIONS/ADDENDUM files exist in any of the seven arc directories (each has only FINDINGS.md, arc_verdict.json, verification/{script,run.txt}; B1369 also controls.py/controls_run.txt/family_isometries.py). Scripts were only skimmed (pincer.py read for its construction). The tests/ lock files were not read. "0 of 19" appears at the end of every claim_one_line; it is the programme's scoreboard and is not computed or logged in any arc.
Note on ids: the seat's own range is B1300-B1399. Arcs below also call "main's" B1321 (inside the seat's range), B1417, B1418, B1415, B1297. B1321 being labelled main's inside the seat's own range is an ambiguity worth checking.

======================================================================
B1367 THE DOUBLET-TRIPLET PINCER
1. VERDICT: "NEGATIVE" (instrument: false)
2. HEADLINE: "THE DOUBLET-TRIPLET PINCER: in trinification form the E6 cubic det L + det Q + det Q^c + Tr(Q L Q^c) pairs N with (H_u, H_d) and with (D, Dbar), and nu^c with (L, H_u) and with (D, d^c), each pair with equal magnitude (one invariant each);"
3. COMPUTED / ARGUED / CITED:
 - Computed, verification/pincer.py (run: pincer_run.txt). (a) The E6-cubic pairings on unit slots: +-1/6 or 0. (b) The single-27 structure constants, with nonzero-entry counts 2/2 for the doublet block and 3/3 for the triplet block. (c) The rank test over n = 3, 4, 6 copies. The n-copy Hessian blocks are built in the script as np.kron(G,S^N)+np.kron(Gn,S^nu), with "light H_u = n - rD/2" and "light D = n - rT/3". The Kronecker form is hand-inserted from the single-27 constants, not the Hessian of an n-copy E6 cubic.
 - Argued in prose only: the theorem's "at every order (higher operators are E6-invariant too)", "27-bars do not couple to 27.27 (no E6 invariant)", "holonomy factor is one E6 element on all components of a 27, preserving ranks", "point-localised 27s never see E6-breaking", the proton-decay estimate "tau_p ~ 1e-12 s", and the exclusion of "every apex design".
 - Cited: B1276 par.3 (diquark/leptoquark rows) and the proton-decay bound 1e15 GeV (via B1276), B1302, B1351, B1352, B1355/B1360, B1365-66. The trinification form is cited as "the standard 27^3 invariant".
4. NUMBERS VS LOGS: all found. n=3: 960 configs, 193 with a light H_u, min light D 1, 0 violations. n=4: 3840, 273. n=6: 4500, 250. 960+3840+4500 = 9300. "15 patterns", "64/256/300 supports" are consistent with the script. Not in the log: "0 of 19", tau_p ~ 1e-12 s, 1e15 GeV (cited or prose).
5. SCOPE:
 - The rank identity is (b) general for one mechanism: only N and nu^c VEVs, E6-invariant couplings up to whole-27 holonomy factors. The arc's own premise sentence is caveat 1: "The couplings are taken E6-invariant up to whole-27 holonomy factors, which is what point-localisation gives; a coupling that acts differently on the components of one 27 would need an E6-breaking field at the apex, and the design has none."
 - "Every apex design of the object is excluded" is (d), premise-dependent on that sentence.
 - Numerics: n=3 covers every VEV support. n=4 covers all 256. n=6 uses 300 random supports.
 - No 27-bars are in the numerics.
6. LINKS TO MAIN: depends on B1276, B1283, B1300, B1302, B1351, B1352, B1355, B1360, B1365, B1366. Of these, B1276 and B1283 are below the seat's range. It says "B1276 par. 2 is a theorem, not a tree-level tension". It names no "main's" arc. Later currency note cites B1368.
7. OVERCLAIM CHECK:
 - Theorem and §0 say "in every vacuum" and "at every order"; the proof and numerics cover only vacua where only N, nu^c take VEVs, at cubic-Hessian level.
 - Headline: "so every apex design of the object is excluded, with or without 27-bars and whatever the line". The 27-bar part is not tested (the proof says only "27-bars do not couple to 27.27"). A 27.27-bar bilinear/mass-term is not addressed.

======================================================================
B1368 THE OBJECT'S OWN STANDARD-MODEL CONNECTIONS
1. VERDICT: "NEGATIVE" (instrument false)
2. HEADLINE: "THE OBJECT'S OWN STANDARD-MODEL CONNECTIONS: a flat E6(C) connection of m004 leaving the Standard Model unbroken has its non-abelian part in SL(2)_beta and a character on (Y, gamma); every bulk sector is an SL(2)_beta spin times a character."
3. COMPUTED / ARGUED / CITED:
 - Computed, verification/sm_connections_of_m004.py (exact over Q(omega), sympy). (A) Riley rep, relator holds, longitude trace -2, lambda+1 nilpotent. (B) The sector census of the 78 and 27 by SL(2)_beta spin; 6 distinct (Y,gamma) lines for the 22 non-SM roots. (C) Fox calculus: Alexander z^2-3z+1 (roots phi^+-2), Wada twisted z^2-4z+1 (roots 2+-sqrt3), spin-1 (0,1). (D) cusp-fixed dimensions. (F) the frame theorem by SU(5) type. (G) the Riley polynomial, the resultant m^6(m^2+1)^4(m^2-m-1)^2(m^2+m-1)^2, and 8 lambda-parabolic points.
 - Argued: the placement in SL(2)_beta x C*^2 via c(SM) (B1366), "spin-0 cusp-fixed only if trivial, hence no Higgs field, hence N=0", "no spin-1/2 sector fixed when tr rho(lambda) = -2", and the doublet-triplet split "available on the object itself". The last is bonus text in the log; no explicit point is computed.
 - Cited: Calegari 2006 (trace -2; also computed here for m004), Riley, Wada, Dunfield-Friedl-Jackson (t^2-4t+1 agreement), Pantev-Wijnholt 2009 and BCHS 2018 (the index frame), B1351.
4. NUMBERS VS LOGS: all found. 30+5, 40=20 doublets, 15/12, 8 points, the roots 0.268/3.732, the resultant, and Phi(m,y) all match the log. The log's (D) section shows spin-1/2 fixed dim 0 at z=7/3, 1, -1 and at the Wada roots.
5. SCOPE:
 - Computations are (c) m004 only (Riley rep, polynomials, 8 points).
 - Theorem (ii) "every flat connection of the family" is (b)/(d): general for any rep into SL(2)_beta x C*^2, but premised on the B1351 frame in its "whole-torus/annular conventions". The arc's own sentence: "L216 closed in the seat's frame (B1351 (ii), whole-torus/annular conventions; the disc-convention adjudication is the bridge lane's)".
 - Caveat 3: golden reducible points' partitions are not computed.
6. LINKS TO MAIN: depends on B1351, B1352, B1364-B1367, B1267, B1269, B1302 (B1267/B1269 are below the seat's range). It mentions the audit lane's R23/R24/R30/R31 and the physical-bridge lane; no "main's B..." tag. A later in-file currency note (B1389) scopes its own frame theorem.
7. OVERCLAIM CHECK: the FINDINGS title ends "with B1351 and B1367 the E6 route from m004 has no chirality mechanism compatible with the Standard Model anywhere in the record's frames". The arc's own B1389 currency note says the "one half of every generation is never chiral" statement "holds where spin-0 sectors cannot be chiral, as on m004", and that on a member with a cuspidal Higgs class the 15 gives whole generations. The title itself was not rewritten.

======================================================================
B1369 THE FAMILY IN THE STANDARD-MODEL FRAME (sL-1 first arc)
1. VERDICT: "NEGATIVE" (instrument: true)
2. HEADLINE: "THE FAMILY IN THE STANDARD-MODEL FRAME (sL-1, first arc): on a member of the figure-eight's commensurability class, a chiral generation from bulk matter with the Standard Model unbroken needs a FREE CUSP -- a cusp whose peripheral image in H_1(M; Q) has rank below b_1"
3. COMPUTED / ARGUED / CITED:
 - Computed, siblings_in_the_sm_frame.py + family_isometries.py (SnapPy 3.3.2; run: siblings_in_the_sm_frame_run.txt) and controls.py (controls_run.txt):
   - cusp counts;
   - H1, b1 and peripheral ranks on all 112 members;
   - the free-cusp census;
   - m202/s959 data;
   - the isometries' exact action on H1 via the canonical retriangulation (t3mlite);
   - parity per free cusp;
   - the residual's reduced moduli.
 - Controls: m004, m003, m129, L6a4, and |Aut|=|Isom| plus b1/ranks agreement against SnapPy on all 112.
 - Argued (proofs in prose): (i) the free-cusp theorem (a finite-order character is unitary, so there is no Higgs field and N=0); (ii) the region-swap lemma in general form. The leading-mode/Higgs-field reading rests on B1351/B1368.
 - Cited: B1351, B1368, B1281 sec. 2D (fc R71) and "main's B1417" (its verification), B1282, B1186 (census), Epstein-Penner, Calegari.
4. NUMBERS VS LOGS: all found:
 - 112 members; cusps {1:60, 2:38, 3:10, 4:3, 5:1};
 - 83 free cusps on 35 members; 77 without (54 one-cusped with b1=1, 23 multi-cusped); 6 one-cusped with b1=2 (t06828, o10_150688/713/714/716/724);
 - m202 P0 index 7, vectors (-2,3),(1,2); 12 isometries, 6 swap, 2 order-3; 266 of 1225 characters;
 - parity 79 of 83 (75 by +-I, 4 by the general lemma: o10_150684 c0,c1 and o10_150725 c0,c2); 4 residual cusps; moduli (5sqrt3/2)i, -1/2+(3sqrt3/2)i, |tau| = 4.33 / sqrt7 (2.6458); 108 of 112; 73 cusp-map cross-checks all agree; controls 8/8/8/48.
 - The §5.4 count (10 cusps without cusp-map cross-check, 8 closed by parity, 2 open) was not checked line by line.
 - Log header says "(B1186; 77 regular-tetrahedral)", which is a different 77 from the 77 no-free-cusp members. This is a possible reader confusion; the numbers are consistent.
5. SCOPE:
 - Free-cusp theorem: (a) general for cusped hyperbolic M, conditional on the (d) premise that the Higgs field = Re log chi_w and N is B1351(ii)'s index. The arc scopes it with "B1351 (ii) under the whole-torus/annular conventions, the R23 scoping stated". The first half (finite order, unitary, no partition) is stated to hold "in every convention".
 - Parity lemma: (a) general, with a transverse-zeros assumption (caveat 2).
 - Census/parity numbers: (c) over B1186's 112 members only.
 - Spin-1/2 part: assumes parabolic peripheral holonomy (caveat 3).
6. LINKS TO MAIN:
 - Depends on B1351, B1368, B1366, B1281, B1282, B1186, B1352.
 - "Complementary to main's B1418 (the class census, ...)"; "main's B1417" and "main's B1321".
 - Generalises fc R71 by dropping its "sigma = -1 on the torus" hypothesis.
 - Currency notes cite B1370, B1372, B1371.
7. OVERCLAIM CHECK:
 - Claim opens "on a member of the figure-eight's commensurability class" and the FINDINGS say "the figure-eight family's 112 members". The seat's own docs record (VERDICT doc §6 currency, B1390; KILL_TESTS "E4") that 13 of the 112 are non-arithmetic and not commensurable with m004. This arc's text is not annotated.
 - Verdict field is "NEGATIVE" although the arc leaves 4 cusps open (its own Status says "OPEN on four cusps").
 - "closed for every flat connection" is conditioned on the frame premise above.

======================================================================
B1370 THE RESIDUAL'S LEADING MODE
1. VERDICT: "OPEN" (instrument: true)
2. HEADLINE: "THE RESIDUAL'S LEADING MODE: on the four free cusps B1369's parity left open (o10_150688 c0, o10_150708 c0, o10_150716 c0, o10_150725 c1), each cusp torus is developed from the tetrahedra shapes (lattice checked against SnapPy's modulus) and every fixing isometry's affine action"
3. COMPUTED / ARGUED / CITED:
 - Computed, residual_cusp_modes.py (run: residual_cusp_modes_run.txt). Floating-point; rounding tolerance 1e-6. It computes the developed cusp tori, the lattice moduli vs SnapPy, the fixers' affine actions with translation parts, and the allowed Fourier shells with allowed dimension per class (linear algebra on the coefficient vectors).
 - Argued/cited: that the smallest present |k| dominates at infinity (Bessel decay exp(-2 pi |k| e^t); cited from B1351 (ii), the B1277 addendum and fc R71); that a single-direction mode gives annular partition, N=0; that a vanishing leading coefficient is non-generic. The coefficients themselves are NOT computed ("the record has no instrument").
4. NUMBERS VS LOGS: all found. 4/2/4/2 single-direction shells before the first two-direction shell. Lowest-shell |k|^2 = 0.013333 (x2 cusps) and 0.037037 (x2). Killed shell (+-1,0) on o10_150688 and o10_150716; none killed on 150708/150725 in the printed shells. Fixers: 2/4/2/12. Triangle counts 40/24/40/24, translation counts 26/18/26/18. Moduli agree with SnapPy.
 - Nuance: the headline says "(higher shells are killed by half-period translations, the first is not)". In the log a shell is killed only on 150688 and 150716, at (+-1,0), after four allowed single shells. The 150708/150725 lists show no killed shell.
5. SCOPE: (c) the four named cusps. Conclusion is explicitly conditional: "Conditional: the closure of the four cusps rests on the non-vanishing of the leading coefficient(s); this arc proves what the symmetries allow, not what the form does." Statement of leading-mode dominance is (d) premise.
6. LINKS TO MAIN: depends on B1369, B1351, B1281, B1368; cites the B1277 addendum and fc R71. No "main's" tag.
7. OVERCLAIM CHECK: Status line says "PROVED (...numerically...)" for floating-point developments; the verdict itself is correctly "OPEN, narrowed". Otherwise none seen.

======================================================================
B1371 THE WEB SEAT'S POST-CLOSURE PACKAGE, VERIFIED
1. VERDICT: "PROVED" (instrument: false)
2. HEADLINE: "THE WEB SEAT'S POST-CLOSURE PACKAGE, VERIFIED: chat1's four documents and thirteen scripts of 2026-09-15 (received from the owner) re-derived on this bench with its own instruments, negatives included. Verified: Humbert's volume 0.169156934 and the Bianchi indices"
3. COMPUTED / ARGUED / CITED:
 - Computed, verify_package.py (run: verify_package_run.txt, 12 sections):
   - Humbert volume and indices;
   - 200-bit shape-field PSLQ;
   - |Sym|/amphicheirality/order-3 counts/surjections onto SL(2,3) and SL(2,5);
   - Lefschetz tables (via B1369's instrument);
   - Fox calculus over F3 and Q(omega);
   - low-degree covers;
   - homomorphisms of pi1(m004(0,1)) into Dic_n;
   - the Chern-Simons gate and slope law;
   - kappa-2 = omega with Nielsen invariance;
   - census scans (first 4815 and the 1263 m+s).
 - Argued in prose: the parity theorem ("fixed points on cusp tori come in pairs", so no 1- or 3-cusped manifold has det=3), items 18/19 (Chern-Weil orthogonality, "unitary => vector-like", marked CONSISTENT/CORRECT).
 - NOT verified: item 20, "main has a certified Dirac operator on m004 with lambda_1 = 2.974550580".
 - Cited: Humbert, Neumann-Reid, Lefschetz, Riley; main's B1297 and B1321.
4. NUMBERS VS LOGS: all found, except the following:
 - "two conjugacy classes" of irreducible SU(2) reps (FINDINGS §3.2) is not in the log. The log shows 40 homomorphisms into Dic_5 and 4 characters with chi o A = chi^-1.
 - Headline says "Refuted: ... two are scoped" (s959's 5, and the 1263 census); the table also marks a third SCOPED (item 4: 13 manifolds at 36 v0 vs the package's 12, found as 13 incl. o10_030703). This is not in the claim line.
 - Found: Humbert 0.169156934402; indices 12/12/24/36/42/30; non-integral 39.343/41.260/44.817; shapes 2/2, 2/2, 4/4, 6/6, 7/7, 6/6 and 4/7, 2/8, 5/8, m129 0/4; surjections 48/0/192/192/96/576; Lefschetz (-1,1,3); h1 (2 vs 4) on m202 and {4,5} vs 6 on s959; covers (vol 4.059766, 6.089650); 40 homs; det(A+I)=5; slope law 8/8; census 1263; first 4815 gives m202/s959/v3461/v3551; hexagonal 11/5/4.
5. SCOPE:
 - Verification of the package's claims: (c)-style, specific manifolds and census depths (first 4815; 1263 m+s).
 - Refutation: general existence claim (a) (irreducible SU(2) reps exist on m004(0,1)).
 - Parity theorem: (a) in prose, stated for finite-order orientation-preserving isometries.
 - Own statement: "The 2T and 2I surjection counts are raw (not divided by automorphisms)"; field test numerical, "B1186's exact criterion is the reference and agrees".
6. LINKS TO MAIN: depends on B1186, B1281, B1282, B1351, B1368, B1369. Names "main's B1297" (the unitary => vector-like theorem), "main's B1321" (order-3 rotation count of three), and main's Dirac-operator claim (item 20, unverified). It says it contradicts only the web seat's package, and that nothing in the package "changes a verdict of the record".
7. OVERCLAIM CHECK:
 - "PROVED" is applied to a verification arc that includes 200-bit PSLQ numerics, items only CONSISTENT/CORRECT, and one item NOT VERIFIED. The claim line does not mention item 20.
 - The claim line's "Verified: ... class membership by the 200-bit shape field" uses the shape field as class membership. B1390 (via VERDICT doc §6 currency) later says shape field alone does not give commensurability (13 of 112 non-integral).

======================================================================
B1372 THE DOUBLET HALVES (door 2)
1. VERDICT: "NEGATIVE" (instrument: false)
2. HEADLINE: "THE DOUBLET HALVES (door 2): the third reading of a Standard-Model generation -- the 10 from the 78's SL(2)_beta doublets and the 5bar from the 27's, both halves carried by the non-abelian part of the flat E6(C) connection rather than by a character -- is closed by charge arithmetic at the cusp."
3. COMPUTED / ARGUED / CITED:
 - Computed, doublet_halves.py (run: doublet_halves_run.txt; exact over Q and Q(i,sqrt5)):
   - the SM weight tables for the 27 and 78 (beta.w, gamma, SU(5) type);
   - the unique both-doublet assignment;
   - Theorem B (0 of 32 sign patterns);
   - Theorem C (theta in {0,1/4,1/2,3/4});
   - Theorem C' (4 admissible patterns at theta=+-1/4, none uniform);
   - m004's order-4 points (4 reps, rho(lambda)=1, invariant definite Hermitian form).
 - Argued in prose: Lemma A (parabolic: dt-component of the coframe is Cartan with eigenvalues +-1/2, so partitions whole or empty), Lemma D (central), and the "abelianised reading at the cusp" (caveat 1) that makes C' translate into "opposite chiralities". The 77-member corollary uses B1369's free-cusp theorem.
 - Cited: B1368, B1369, B1351, B1365/B1366, B1281 sec. 2D, Riley, BCHS 2018.
4. NUMBERS VS LOGS: all numbers found, with one MISMATCH:
 - Mismatch: the claim line and FINDINGS §0/Thm C' say the opposite groupings are "the 10 against the 5bar, or {Q, d^c} against {u^c, e^c, L}". The log's four patterns (Q,u^c,e^c|d^c,L) are (+,+,+|-,-), (+,-,+|+,-), (-,+,-|-,+), (-,-,-|+,+). The two non-uniform ones therefore split as {Q,e^c,d^c} against {u^c,L}, not {Q,d^c} against {u^c,e^c,L}. The FINDINGS §2 table itself lists the log-consistent patterns, so the prose and the table disagree.
 - Also, the FINDINGS title says "then always on opposite eigenvectors"; in 2 of the 4 patterns the 10 and 5bar each split internally rather than being opposite as wholes.
 - Found: 0 of 32; {0,1/4,1/2,3/4}; 4 patterns; example (0,-15/4,3/4); order-4 points y = -5/2 -+ sqrt5/2 (4 points); the extra branch of the 5bar alone (+-12L/5, +-3L/5); "fifteen weights" (10+5).
5. SCOPE:
 - Theorems B, C, C' are (b): for the mixed frame (10 from the 78, 5bar from the 27), with one connection for both halves (caveat 3), under premise (d) abelianised cusp reading.
 - The m004 order-4 points: (c).
 - The 77 free-cusp-less members: (c) via B1369.
 - Own scope sentence: "Door 2 is closed on m004 and on the 77 members without a free cusp; it survives only at order-4 points with non-unitary global holonomy on the 35 free-cusp members, where the abelian Higgs field could reorder the partitions -- character-variety data the record does not have."
6. LINKS TO MAIN: depends on B1368, B1369, B1351, B1365, B1366, B1281. It sharpens B1368 (2)(i): "no spin-1/2 sector is cusp-fixed" becomes "no doublet sector carries an index at any parabolic point". It re-verifies B1368's four dihedral points. Currency note cites B1373. No "main's" arc named.
7. OVERCLAIM CHECK: the claim line's final sentence "The mixed frame itself ... is a reading the record had not adopted; it is closed regardless" sits beside the caveat that the closure uses the abelianised reading (caveat 1) and the order-4 survival on 35 members. The grouping error quoted in field 4 is in the headline text.

======================================================================
B1373 THE ORDER-4 POINTS ON THE GEOMETRIC COMPONENTS
1. VERDICT: "NEGATIVE" (instrument: false)
2. HEADLINE: "THE ORDER-4 POINTS ON THE GEOMETRIC PATH: door 2's residual (B1372) needs a point of a free-cusp member's character variety where both peripheral eigenvalues on the free cusp are fourth roots of unity with non-unitary holonomy."
3. COMPUTED / ARGUED / CITED:
 - Computed, order4_points.py (run: order4_points_run.txt; deterministic; SnapPy Newton continuation, eigenvalues read to 1e-6):
   - fillings (2p,0) or (0,2p) continued p=30 to 1 on each free-cusp curve (166 pairs);
   - 132 endpoints reached;
   - the other curve's holonomy read at each;
   - 34 meridian failures resolved on a fine path (step 1/64, original triangulation).
 - Argued: that Theorem B (from B1372) closes each reached point; that monotone growth of |Re H(other)| means "ideal points of the real path, no representation there"; the Culler-Shalen/boundary-slope remark ("recorded but not pursued").
 - Cited: B1372 Theorems B and C; SnapPy cone-manifold Dehn filling; the Ptolemy database (coverage checked for t06828 only).
4. NUMBERS VS LOGS: headline numbers all found:
 - 132 of 166 reached (83 longitude + 49 meridian) and 132 closed by Theorem B, 0 by C, 0 survivors.
 - |L| from 0.2505 to 9.0121.
 - 34 coarse-path failures, all resolved on the fine path.
 - Wall within 1/16 of p=1: 23; within 1/16 of p=3/2: 11; elsewhere 0.
 - |Re H(other)| monotone 34 of 34; last non-degenerate step from 10.22 to 27.00 ("10-27").
 - INTERNAL INCONSISTENCY, not a log mismatch: FINDINGS §0 still says "on 30 meridian cases the other holonomy grows without bound ... and on 4 the solver stalls at cone angle 2pi/3 (o10_150684 cusp 1, o10_150708 cusp 0, o10_150714 cusp 0, o10_150725 cusp 1)". Caveat 2 says "that 30/4 split ... is withdrawn", and §1 and the log give 23/11 (with 11 named). Also §0 says "cone angle 2pi/p" while the log header and §1 use cone angle pi/p.
5. SCOPE:
 - (c) real cone-manifold path of the geometric component, free cusps of the 35 candidates, floating-point.
 - Own sentence (claim line): "Not covered: points of the geometric components off the real path and other components of the character varieties, which need the A-polynomial or full Ptolemy solutions of ten-tetrahedron manifolds (the Ptolemy database does not reach them)."
 - Caveat 1 admits "whether the wall sits exactly at the rational angle or a hair before it is not decided (the last steps are 1/64 apart)".
6. LINKS TO MAIN: depends on B1372, B1369, B1186; no "main's" arc named.
7. OVERCLAIM CHECK:
 - "ideal points of the real path, no representation there" is inferred from numerical monotone growth to 10-27 at 1/64 resolution, not proved.
 - Several fine-path walls sit at p=1.0 or 1.0156, i.e. at the target angle within the step, so "degenerates before the point" is a numerical reading.
 - The FINDINGS title's "no candidate on the geometric path anywhere" is bounded by its own "the rest of the character variety untouched".
 - §0 retains the withdrawn 30/4 split.

======================================================================
DOC 1: docs/THE_VERDICT_OF_THE_OBJECT_2026-09-16.md
What it is: the SM-derivation seat's capstone for its E6 route. It restates what the figure-eight knot complement m004 fixes and withholds, lists three closing theorems (B1351, B1367, B1368), and sets the next mandate (sL-1, the family). Sections: 0 one paragraph, 1 table of what the object fixes, 2 the three theorems, 3 scope, 4 verdict, 5 "what the negative teaches", 6 mandate with in-file currency notes (reworded 2026-09-27; B1390; B1369, B1370, B1372, B1371 status), 7 pointers.
Conclusions as stated:
- §0: "The figure-eight knot complement fixes the Standard Model's structure and withholds its chirality." Plus: "No frame the record has gives three chiral generations together with a Higgs sector that survives."
- §1 table (all PROVED except B1355-B1360 "PROVED (geometry) / CITED (count) / DESIGNED (closing)"): E6 (B1268); the 27 and its cubic (B1276); unique SM embedding (B1366); centraliser SU(2)_beta x U(1)^2 and 13 = SM x U(1)' (B1269, B1364); Y3's Q8 line leaves SM x U(1)' (B1364); U(1)' = U(1)_eta (B1365); hollow texture refuted, breaking order one (B1273, B1361, B1362).
- §2 three theorems:
  1. Closed closings vector-like (B1351).
  2. Point-localised matter cannot split doublets from triplets (B1367: "9 300 configurations, no exception"; "Every apex design of the object is excluded").
  3. Bulk matter on the object is never a chiral generation with the SM unbroken (B1368).
- §4 verdict: "m004 fixes E6, the 27 and its coupling, the embedding of the Standard Model, its Wilson line, its Z' and the shape of its textures, and in every frame the record has it withholds a chiral generation that survives the Higgs sector." It adds "the paper's chirality section should carry it in these words."
- §6 status: sL-1 answered "on 108 of the 112 members" (B1369); 4 cusps remain (B1370: one Fourier coefficient per cusp); door 2 (B1372) closed on the object and on members without a free cusp; the web package (B1371) "brings no new door".
Names main's arcs:
- "main has verified B1356-B1365 with its own code (B1415)".
- §3: "the subject of main's sealed design B1418".
- §6 item 2 "main's cell 2"; "main's B1418 (which runs the class census, the reducible-locus index, the sibling and tower relations, and the exact half of the 27bar sector)".
- Cites B1291 (parity theorem), B1321 (count of three), B1417 (parity verification).
- §7: main's `frontier/B1415...` and `frontier/B1418...` (DESIGN), "main's L220/L221".
Observations (facts only):
- §0, §2, §4 and the §1 table are not annotated for the later kill-test results. Only §6 carries currency notes.
- §6 item 2 claims "the frame theorem and Calegari's trace -2 hold for every hyperbolic knot complement". B1369's longitude census says Calegari's -2 is "checked only where SnapPy's longitude lies in the commutator subgroup" (3 of 60 one-cusped members). B1369 closes the one-cusped b1=1 members by the free-cusp theorem instead.
- The B1415 verification range B1356-B1365 does not include B1366-B1368 used in the same paragraph.

DOC 2: docs/THE_KILL_TESTS_2026-09-27.md
What it is: a letter-style summary written for the owner after four sealed kill tests (B1388-B1391) plus B1392 on the Eisenstein chirality result B1386-B1387 (N(v+) = +-2 on cube~3.24, a degree-9 cover of o10_150725). It says where the mechanism is retired or scoped and where physics must enter. Currency notes B1393, B1394/B1396 and B1398/B1399 are appended.
Conclusions as stated:
- Test 1, cutoff (B1388): UNSTABLE; relative index moves with the cut (+4,+7,+8,+2,-1); "The physical reading of 'protected chirality' is retired."
- Test 2, full spectrum (B1389): MIXED; the 27's spin-0 15 gives whole anomaly-free generations for Higgs directions "round gamma, two on cube~3.24"; the 78's broken roots make the bulk anomalous in every direction (parity law, E8 included).
- Test 3, the three (B1390): "no protected, non-pullback three" (theorem; order-3 symmetry either rotates cusps or acts freely).
- Test 4, Yukawas (B1391): NEGATIVE for ratios; the geometry supplies a flavour group (D3 = S3 doublet at the symmetric point), not ratios.
- B1392: chirality is carried entirely by the free cusps; a Higgs class alive at every cusp gives a clean Fredholm problem and its count "is zero".
- Side findings: "The family is not the class (E4)" (13 of B1186's 112 have non-integral traces, non-arithmetic, class census part is 99; "No verdict changed"); "115 of B1186's 184 members have a free order-3 symmetry inverted by another isometry".
- Entry points: completion of the free cusps (sL-8), the level (sL-5), Higgs breaking of the flavour group. Next step: seal candidate completions against CPT, anomaly (odd SU(5)^3 per unit N), and count; "0 of 19".
- Record table: B1388 NEGATIVE, B1389 PROVED (MIXED), B1390 PROVED (+E4 correction), B1391 NEGATIVE (routed), B1392 PROVED.
- Currency: B1393 CPT lemma (+2 made by the flip at the free cusps); B1394/B1396 a sealed prediction (NONE) fired, 54 non-acyclic pairs give a non-regular source three; B1398 "no completion on the menu gives an anomaly-free three"; B1399 NONE on 102 of 109 covers (even count; odd terms need hexagonal cusps).
Names main's arcs: only "one reading of main's B1418" scoped by E4 (relayed) and "The letter to main carries the fiftieth to fifty-fourth notes." All B1385-B1399 are this seat's arcs.
Cross-document observations (facts only):
- The doc says E4 scopes "B1385's identification and one reading of main's B1418", and that 13 of 112 members are not commensurable with m004. B1369's claim line and FINDINGS, B1371's "class membership by the shape field", and this VERDICT doc's §6 original text speak of "the family"/"commensurability class" of 112.
- Test 1 retires the physical reading of the relative index N, while B1369/B1370/B1372/B1373 closures are statements that B1351(ii)'s N = -chi(boundary+) vanishes. The doc ties the asymptotic count to "minus the signed number of Higgs zeros on the whole manifold".
- I did not read arcs B1385-B1399, so these doc claims are unverified here.
