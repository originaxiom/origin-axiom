# Origin Axiom programme question–answer map

**As of:** 2026-08-30

**Canonical questions:** 185

**Registry SHA-256:** `b076a175b9c20dd94103c5115cfb2450f4a9d399cffa8bca1a101e751653c52f`

This is the durable, source-linked map of every canonical question currently registered by
the independent closure campaign. It distinguishes a proved narrow theorem from a broader
physical interpretation. `OPEN` is a live obligation. `CONDITIONAL` and
`EXTERNAL_BLOCKER` mean the question is accounted for, not that the parameter-free
programme has answered it affirmatively.

## How to update this map

1. Edit the canonical JSON row, never only the rendered prose.
2. Give every new child question a stable `OA-C####` ID before closing its parent.
3. Preserve the narrowest proved scope and name every hidden input.
4. Rerun the renderer and campaign validator; commit the JSON, Markdown, and proof artifact
   together.

```text
python3 documents/program-question-map/render.py \
  --source documents/program-question-map/inventory/backbone.json \
  --markdown documents/PROGRAM_QUESTION_ANSWER_MAP.md \
  --as-of 2026-08-30
```

## Status dashboard

| status | count | meaning |
|---|---:|---|
| `OPEN` | 21 | Registered and typed, but its stated closure test has not yet been executed. |
| `PROVED` | 70 | A type-correct proof or reproducible exact computation establishes the scoped claim. |
| `REFUTED` | 55 | A proof, counterexample, or exact negative computation defeats the scoped claim. |
| `CONDITIONAL` | 15 | The claim follows only after the named underived input is assumed. |
| `EXTERNAL_BLOCKER` | 22 | The required construction or theorem is absent; the unblock condition is explicit. |
| `EMPIRICAL` | 2 | Only bounded numerical or observational evidence is available. |
| `OUT_OF_SCOPE` | 0 | A declared scope rule excludes the question from this campaign. |

## Domain dashboard

| domain | questions |
|---|---:|
| `arithmetic` | 12 |
| `carrier` | 3 |
| `cosmology` | 1 |
| `dynamics` | 4 |
| `flavor` | 10 |
| `framework` | 15 |
| `genesis` | 3 |
| `geometry` | 36 |
| `gravity` | 1 |
| `lie` | 28 |
| `physics_interface` | 6 |
| `process` | 1 |
| `qft` | 11 |
| `spectrum` | 13 |
| `vacuum` | 26 |
| `values` | 15 |

## Complete index

| ID | status | domain | question | direct answer |
|---|---|---|---|---|
| [OA-C0001](#oa-c0001) | `REFUTED` | `genesis` | Does bare not-nothing/minimal description select a unique formal seed independently of encoding? | No. For any computable x, the universal prefix machine U_x with U_x(0)=x and U_x(1p)=U(p) gives x a one-bit description; global minimizers are machine-dependent. |
| [OA-C0002](#oa-c0002) | `CONDITIONAL` | `genesis` | Do the declared primitive, aperiodic, unimodular substitution rules select Fibonacci at minimum lexicographic cost? | Conditionally. Exact enumeration leaves a->ab,b->a up to alphabet exchange/reversal; the category/cost remain an explicit axiom. |
| [OA-C0003](#oa-c0003) | `CONDITIONAL` | `carrier` | Does the Fibonacci substitution canonically determine the oriented punctured-torus mapping torus m004? | Conditionally. Squaring the determinant-minus-one incidence gives RL, but letter-to-Dehn-twist, puncture, orientation, and mapping-torus operations are extra typed data. |
| [OA-C0004](#oa-c0004) | `PROVED` | `arithmetic` | Given m004, does reduction at the ramified Eisenstein prime produce SL(2,F3)=2T? | Yes. Exact reduction and group-generation computation are banked; this is the genuine hyperbolic 2T entrance. |
| [OA-C0005](#oa-c0005) | `PROVED` | `lie` | Does binary tetrahedral 2T determine the affine E6 graph and finite E6 root-system type? | Yes. Classical affine McKay gives affine E6; deleting the trivial-representation node gives the finite E6 Cartan/root-system type, but not a global-group root datum. |
| [OA-C0006](#oa-c0006) | `CONDITIONAL` | `lie` | Does the object select the principal sl2 placement and charged E6 frame used downstream? | Conditionally. Whitehead rigidity does not select a class. B1146 corrects a frame conflation: the principal adjoint action is center-blind and factors 2T through A4, whereas the selected minimal A1 has 40 odd adjoint weights and 12 odd weights on the 27, so the 2T center is visible there. This distinguishes the embeddings but does not select the minimal A1; B1112 still leaves a nine-element projective menu and singles A2 only after SM-compatible filtering. |
| [OA-C0007](#oa-c0007) | `REFUTED` | `qft` | Does the mathematical E6 datum uniquely produce a compact four-dimensional quantum gauge theory? | No. A constructive family L(n,g,theta,...) gives infinitely many inequivalent 4d E6 theories sharing the same root datum, 27, and cubic. |
| [OA-C0008](#oa-c0008) | `REFUTED` | `spectrum` | Does the native structure provide three physical copies of a chiral 27? | No. B1033 retracts four internal threes; B876 is one vectorlike 16+bar16 pattern; E8 contains (27,3) and (bar27,bar3), and its sole A2 cannot be both electroweak and family. OA-C1126 exactly shows that the selected trinification order-three symmetry cycles three different 9-blocks rather than three gauge-identical copies inside one 27. OA-C1137 records the independent logical failure of using a degree-two trace field to bound multiplicity by two. |
| [OA-C0009](#oa-c0009) | `EXTERNAL_BLOCKER` | `geometry` | Does a native closure have net chiral index N_27-N_bar27=3? | Not yet. Closed doubles have equal 27/bar27 counts; B1084's flat loci intersect on lines; no current 4d Dirac/index functor exists. |
| [OA-C0010](#oa-c0010) | `REFUTED` | `lie` | Can the E8 host simultaneously supply electroweak gauge symmetry and three families? | No. E8\|E6xA2=(78,1)+(1,8)+(27,3)+(bar27,bar3); the one residual A2 is exactly both claimed slots. If used as EW, 3 becomes 2+1 rather than three gauge-identical families. |
| [OA-C0011](#oa-c0011) | `EXTERNAL_BLOCKER` | `vacuum` | Does the object select a rank-reducing Higgs representation, orbit, point, and vacuum? | Not yet. B632 v0 has N=-6, Jordan rank 3 and F4 stabilizer, not the rank-1 Spin10 direction. A Kato-Yukie semistable pencil contains no rank-1 direction; for two rank-1 endpoints N(sA+tB) is identically zero. OA-C1113 gives the direction-level parity/lock fork, and OA-C1119 now closes the selected finite SM-safe direction census: exactly two directions pass, but both destroy the selected gradings. Neither result supplies a potential, an actual VEV, stability or an object-selected orbit. |
| [OA-C0012](#oa-c0012) | `CONDITIONAL` | `spectrum` | Given the standard compact embedding and correct vacuum, is the unbroken global group (SU3xSU2xU1)/Z6? | Conditionally. The Z6 kernel is standard and B1080 computes it for chosen cascades; no branch derives the physical compact embedding/vacuum antecedent. |
| [OA-C0013](#oa-c0013) | `REFUTED` | `spectrum` | Does the object uniquely select a color-commuting Standard-Model hypercharge? | No. B1102 finds 18 rational target-matching directions and exactly zero commuting with a full color ideal. B1139 searches against preloaded SM Q/Y tables and is a reproduction, not a selector. OA-C1121 proves a narrower trinification-frame realization after imposing an SM-shaped 15-plet; OA-C1118 records the distinct full-spectrum rank-three selector still required. Neither repairs intrinsic selection of the physical embedding. |
| [OA-C0014](#oa-c0014) | `EXTERNAL_BLOCKER` | `vacuum` | Does the selected vacuum leave exactly the SM light fields and one viable Higgs sector while lifting all exotics? | Not yet. In a fixed D5 x U(1)_psi frame, 27=16_1+10_-2+1_4 and the exact E6 cubic has 40 supports of type (16,16,10) plus 5 of type (10,10,1), conserving the resulting parity. OA-C1112 proves the associated anomaly sums cancel and OA-C1113 classifies individual parity/lock-neutral directions. Both facts remain frame-conditional: support and anomaly arithmetic do not supply fields, gauging, a potential, stability or mass ranks. No vacuum or exotic-decoupling proof exists. |
| [OA-C0015](#oa-c0015) | `EXTERNAL_BLOCKER` | `flavor` | Does the object compute nondegenerate fermion masses and realistic inter-family mixing? | Not yet. The E6 cubic fixes support but not physical coefficients. The carrier tensor epsilon tensor C is an exact one-dimensional representation invariant, but no compactification/zero-mode intertwiner, Calabi-Yau trace or matter metric maps it to a physical Yukawa. On the conditional heterotic branch, R017 now versions the primary proof that the height-308 holomorphic up map is identically zero and remains zero throughout the same monad topology while exactly one audited H_u is retained. B1154 independently proves this cohomological emptiness is not the same arithmetic fact as period-value non-overlap. The down/lepton chain map, normalized metrics, thresholds and RG flow remain absent. |
| [OA-C0016](#oa-c0016) | `EXTERNAL_BLOCKER` | `values` | Does the object emit every dimensionless Standard-Model parameter after thresholds and RG running? | Not yet. Natural period searches return negative; regulator identification remains unconstructed; sin^2(theta_W)=3/8 is the conditional GUT normalization, not the measured prediction. B1154 distinguishes arithmetic non-overlap from the independent cohomological up-Yukawa emptiness: two walls support the same structure-versus-values diagnosis, but neither supplies a number. |
| [OA-C0017](#oa-c0017) | `EXTERNAL_BLOCKER` | `qft` | Does the object uniquely produce four-dimensional spacetime and a gravitational quantum dynamics? | Not yet. B1104 finds no canonical suspension section; filling is nonunique; S=-Vol*sigma is an on-shell value rather than a 4d gravitational action. B1157 and B1165 further classify the infinity-place constructions as generic spectral geometry: no 4d action, propagator or Ward identities are constructed. The exact Ruelle factorization OA-C1104 is mathematics, while OA-C1106--OA-C1108 remain specialist analytic residues. OA-C1132 registers the unrun arithmetic-versus-nonarithmetic ablation and OA-C1135 fences the proposed parity-by-dimension classifier. |
| [OA-C0018](#oa-c0018) | `EMPIRICAL` | `values` | Does the completed theory make a successful unused quantitative prediction? | Empirical evidence only. No current repo value claim satisfies this strict endpoint criterion; several sealed crossings are negative. |
| [OA-C0019](#oa-c0019) | `REFUTED` | `geometry` | Can a whole-group affine cocycle turn a transverse B1111 pair into an isolated order-24 enhancement point? | No. Averaging proves every affine 1-cocycle is a coboundary. All loci share one full-group fixed point, whose stabilizer has order 96. An order-24 pair is also the wrong E7 enhancement type. |
| [OA-C0020](#oa-c0020) | `EXTERNAL_BLOCKER` | `geometry` | Is there a unique object-selected compact singular geometry with exactly three same-sign E7-to-E6 enhancements and no others? | Not yet. The flat B1084 isotropy is not binary-octahedral and its intersections are lines. A trivial oriented rank-3 section on a closed oriented 3-manifold cannot have total signed zero count +3. |
| [OA-C1000](#oa-c1000) | `PROVED` | `arithmetic` | Does the marked conductor-four cusp reconstruct the ring class field Q(zeta_12), the product fan dP6 x dP6, and the published free C12 toric action? | Yes. The marked order O_4=Z[2 sqrt(-3)] has ring class field H=Q(zeta_12); its two Eisenstein eigensummands give dP6 x dP6, and an explicit determinant-one basis change identifies multiplication by zeta_12 with the published A_N and twelve-cycle. |
| [OA-C1001](#oa-c1001) | `CONDITIONAL` | `geometry` | Does the primitive multiplicative norm law select a smooth fixed-point-free anticanonical hypersurface in the reconstructed C12 toric family? | Conditionally. For H=Q(zeta_12), trace-dual field norms give invariant orbit weights 0,1,1,1,4 and exact computation proves smoothness and free C12 action; the load-bearing multiplicativity principle remains open. |
| [OA-C1002](#oa-c1002) | `REFUTED` | `qft` | Does the class-field and toric data themselves select the ten-dimensional heterotic physical-realisation functor and its compactification framework? | No. The same selected CY3 with h11=1,h21=4 has standard type-IIA and type-IIB compactifications with inequivalent 4d N=2 multiplet counts (1 vector,5 hypers) and (4 vectors,2 hypers), while heterotic E8xE8 requires extra left/right worldsheet, GSO and bundle data and gives N=1. Thus the arithmetic/toric antecedent has multiple physical-realisation functors. Retaining V_E8 in a c=16 chiral completion conditionally forces E8^2, but that retention and the heterotic worldsheet are additional physical premises, not properties of the CY3. |
| [OA-C1003](#oa-c1003) | `CONDITIONAL` | `lie` | Given a heterotic CY3 with full SU(3) holonomy and index-one standard embedding, does the McKay E6 type select the E8 x E8 gauge-lattice branch and active E8 commutant? | Conditionally. McKay gives finite E6; under the explicit assumptions, E8 x E8 has active commutant E6 while Spin(32)/Z2 gives so(26)+u(1). The result is an elimination theorem, not a derivation of heterotic theory or later bundle/vacuum data. |
| [OA-C1004](#oa-c1004) | `EXTERNAL_BLOCKER` | `geometry` | Does the class-field norm hypersurface select and stabilize one locally free stable equivariant SU(5) bundle map with the exact-MSSM branch kernel? | Not yet. The norm section selects coefficients but raw norm reuse has the wrong Euler kernel; the (3,4) BCDD branch is an 11-dimensional map family with ten genuine descended bundle-moduli directions. The marked height-308 pseudoinverse is dual-homed, passes the pointwise gates and has its Hoppe slope stability separately proved by OA-C1013. Minimality, branch-selection inputs and physical realization remain unproved. OA-C1123 adds an exact obstruction: the four surviving bundle/Wilson branches form a free transitive V4 Galois orbit, so no Galois-invariant datum can select one. No dynamical equation selects a unique point. |
| [OA-C1005](#oa-c1005) | `CONDITIONAL` | `spectrum` | Does the primitive cyclotomic source canonically force the hypercharge Wilson character to reuse the same odd-primary power as the bundle branch? | Conditionally. Primitive characters rho with bundle pair {rho^3,rho^4} reproduce exactly four Table-3 branches; reusing rho^4 selects one four-model orbit and rho^-4 the other. The primary construction treats the two Wilson factors as independent, so the rule remains conditional. |
| [OA-C1006](#oa-c1006) | `CONDITIONAL` | `spectrum` | Under the selected heterotic framework, smooth free quotient, stable SU(5) bundle branch, and Wilson character, does the visible charged massless sector equal three chiral MSSM generations plus one Higgs pair? | Conditionally. The audited BCDD branches have index three and exact visible charged MSSM massless content after Wilson projection, conditional on the heterotic realization and generic stable branch. Hidden E8, neutral moduli, couplings, and dynamics remain outside the phrase visible spectrum. |
| [OA-C1007](#oa-c1007) | `EXTERNAL_BLOCKER` | `vacuum` | Does the selected class-field heterotic construction determine an isolated stable vacuum and all normalized low-energy parameters? | Not yet. The selected section does not stabilize bundle, Kahler, dilaton, or other moduli; the BCDD branch has genuine P10 bundle deformations. On the strict CY branch the exact compact (0,2) GLSM lies in the Beasley--Witten vanishing class, so genus-zero worldsheet terms cannot select that P10. The class-field action now conditionally selects one hidden E8 lift and a combined order-three secondary class, but the no-B strict branch then fails level matching. A published large-radius Strominger theorem supplies a same-topology torsional solution preserving the visible spectrum, not the prescribed differential class or a vacuum. The exact height-308 up-type cup product is zero and remains zero along that fixed-holomorphic-data Strominger curve. The exact universal hidden threshold is negative, refuting the economical supersymmetric fractional-CS condensate solution; normalizer symmetry leaves three complex-structure equations, and no down Yukawa, normalized periods, subgroup thresholds, prefactors, all-moduli mass matrix, SUSY-breaking scale or RG output is derived. |
| [OA-C1008](#oa-c1008) | `REFUTED` | `flavor` | Does the Hesse/equianharmonic period shortcut furnish an intrinsic BCDD H3 invariant and a normalized MSSM Yukawa or flavor prediction? | No. The audited Hesse chain conflates the Schoen Z3xZ3 model with BCDD, does not construct a BCDD weight-three VHS map, and computes neither SU(5)-bundle cup products nor matter metrics; a Hesse connection coefficient is not a normalized MSSM Yukawa. |
| [OA-C1009](#oa-c1009) | `PROVED` | `lie` | Does the class-field trace/codifferent lattice determine one positive C12-equivariant E8 isomorphism class after completion? | Yes. Primitive positive trace forms on O_H and its codifferent give A2^4; eight tetracode glues complete to E8, exactly four are C12-invariant, and the positive-metric C12 centralizer is transitive on those four. Thus the completed positive C12-lattice has one structured isomorphism class. |
| [OA-C1010](#oa-c1010) | `REFUTED` | `lie` | Do the present class-field markings select one evaluation-preserving E8 glue representative and physical gauge embedding? | No. The four invariant glues are the graphs of plus-or-minus (1 plus-or-minus zeta)delta. Trace evaluation leaves two two-orbits and exact delta leaves four singleton choices; moreover zeta^4 has fixed rank zero on an A2^3 complement while the McKay E6 arm rotation has fixed rank two. |
| [OA-C1011](#oa-c1011) | `PROVED` | `qft` | Does the positive E8 lattice isomorphism class determine a unique holomorphic c=8 lattice-VOA isomorphism class with e8 level-one currents? | Yes. The even unimodular E8 lattice gives V_E8 with c=8 and 8+240=248 weight-one states; under the standard strong-rationality hypotheses this is the unique holomorphic c=8 VOA isomorphism class. |
| [OA-C1012](#oa-c1012) | `PROVED` | `geometry` | Does the marked equal-weight pseudoinverse define an equivariant locally-free rank-five bundle candidate with the certified pointwise base cohomology maps? | Yes. Exact Q(zeta12) linear algebra and good-prime unit/minor certificates prove equivariance, local freeness, H0(V)=0, the displayed matter cohomologies, and rank312. B1162 now dual-homes the height-308 witness, and OA-C1013 separately proves pointwise Hoppe slope stability. The construction still uses unforced target directions, coefficient metric and relative weight; minimality and unique physical selection are not established. |
| [OA-C1013](#oa-c1013) | `PROVED` | `geometry` | Does the arithmetic bundle candidate pass pointwise Hoppe stability, given that its exact wedge-square cohomology and MSSM Higgs projection are now certified? | Yes. At the exact norm-308 point, p=1 and p=4 vanish, the reconstructed Cech 18-to-21 map has rank 16 with determinant-twisted cohomology chi0+chi1, and the quotient map has rank312. The pointwise exterior certificates give induced ranks 27 on H0(Lambda2 G) and 68 on H0(Lambda3 G), hence H0(Lambda2 V)=H0(Lambda3 V)=0. Hoppe's criterion on the h11=1 quotient therefore proves slope stability at this named arithmetic point. |
| [OA-C1014](#oa-c1014) | `PROVED` | `qft` | Among positive even-unimodular rank-sixteen lattice or strongly rational holomorphic c=16 VOA completions that retain the selected E8 as a primitive orthogonal lattice subobject or full regular conformal factor, is E8 x E8 unique? | Yes. Because det(E8)=1, an isometric E8 inclusion in a unimodular rank-sixteen lattice splits integrally as E8 plus its orthogonal complement; that complement is the unique rank-eight E8 lattice. In the regular conformal-coset VOA setting, holomorphic V_E8 forces the c=8 commutant to be V_E8, so V_D16+ cannot contain it compatibly. Complement C12 action/lift data remain free. |
| [OA-C1015](#oa-c1015) | `CONDITIONAL` | `qft` | Given the conservative critical-worldsheet realization axiom, do the selected CY3 and V_E8 force a four-dimensional E8 x E8 heterotic parent? | Conditionally. For conventional heterotic matter, D+c_g=26 and 3D/2=15 give D=10 and c_g=16. A CY3 consumes six real target dimensions, leaving four; extension without erasure forces the c=16 gauge receiver to V_E8 tensor V_E8. All conclusions remain conditional on the composite physical-realization axiom. |
| [OA-C1016](#oa-c1016) | `REFUTED` | `geometry` | Do the no-source heterotic Bianchi identity, full SU(3) tangent holonomy, and McKay E6 compatibility force the visible index-one standard embedding V=TX with F=R? | No. BCDD construct stable irreducible rank-five SU(5) deformations of TX+O+O on the selected Z12 construction. Characteristic classes are preserved, and their anomaly equation is saturated with trivial hidden bundle and [C]=0. This witness has the same no-source c2 balance as TX but different rank and SU(5), so it is not gauge-equivalent to TX; full SU(3) is a property of TX and does not change that. A literal H=0 differential solution is additional data and is not inferred from the class equation. |
| [OA-C1017](#oa-c1017) | `REFUTED` | `vacuum` | Does one pure hidden-E8 gaugino condensate stabilize the dilaton and the single Kahler modulus of the selected quotient? | No. For K=-log(S+Sbar)-3log(T+Tbar), f_h=S and W=A exp(-2 pi S/30), exact no-scale cancellation gives V=\|A\|^2 exp(-a x)(a x+1)^2/(x y^3). Its logarithmic derivatives are strictly negative in x and y, and both axions are flat, on all 30 branches. The same x-stationarity obstruction holds for a selected positive linear threshold f_h=S+beta T. Extra condensates, fluxes, thresholds or corrections are new data. |
| [OA-C1018](#oa-c1018) | `REFUTED` | `vacuum` | Can an integral quantized heterotic H-flux class on the fixed C12 quotient supply a parameter-free W0 or stabilize the remaining moduli on the strict Calabi--Yau branch? | No. The integral quotient certificate gives H_2=Z and H^4=Z; UCT, Poincare duality, and b3=2(h21+1)=10 give H^3(X,Z)=Z^10 with no torsion. Thus integral topological flux has an infinite menu and no selected lattice vector. On the strict Kahler CY N=1 branch H=d^cJ=0; in the H-only 4d F-term truncation D_S W=0 and D_z W=0 force H=0. This does not exclude finite-order secondary characters in H^3(X,R/Z): OA-C1044 proves a conditional order-three class, which instead leaves the strict (0,2) CY branch and requires a fractional-CS/condensate or non-Kahler completion. |
| [OA-C1019](#oa-c1019) | `EXTERNAL_BLOCKER` | `vacuum` | Does the class-field C12 action select a hidden-E8 Wilson line with pure asymptotically-free factors, and does the resulting fractional-CS/condensate system isolate the heterotic vacuum? | Not yet. The old unrestricted problem has 270 Kac classes, but the retained class-field lattice automorphism now selects one Weyl class and one compact lift after the equivariant heterotic-retention clause. Its hidden centralizer is A2+A1^3+U1^3 and its universal c2 is 2 mod 12; the native rho^4-to-SU3-center alternative instead has c2=0. This closes the finite conjugacy menu conditionally, not the vacuum: tree-level factors share f=S, the exact parent hidden slope is -3/(2 pi^2), and the economical fractional-CS supersymmetry equation has no positive-volume solution. The large-radius Strominger theorem supplies a compatible local torsional geometry, but normalized periods, subgroup kinetic functions, determinant prefactors/phases, the global order-three lift and an isolated vacuum remain open. |
| [OA-C1020](#oa-c1020) | `REFUTED` | `flavor` | Do the certified C12 cohomology characters and SU(5) cubic force parameter-free three-family up/down/lepton Yukawa textures? | No. The exact character certificate gives three family copies and one Higgs pair but leaves Sym^2(C^3), dimension 6, for up Yukawas and C^3 tensor C^3, dimension 9, for down/lepton Yukawas; no C12 texture zeros occur. SU(5) supplies only up symmetry and the holomorphic transpose relation Y_e=Y_d^T. OA-C1127 gives the distinct selected-E6 45-support table, not evaluated heterotic cup products. Cup-product coefficients, the Hd line in the fourfold chi0 space, matter metrics, canonical normalization, vacuum, thresholds and RG data remain unfixed. |
| [OA-C1021](#oa-c1021) | `EXTERNAL_BLOCKER` | `vacuum` | Does the native order-three hidden Wilson line determine unequal Kahler thresholds and an isolated S,T racetrack vacuum? | Not yet. Tree level and level-one embedding give f_E6=f_SU3=S and b=(36,9). The broken (27,3)+(bar27,bar3) channel has unequal quadratic-index weights (18,54), so a differential threshold is allowed but not forced. The BCDD data contain no full (0,2) CFT partition function, HYM determinant, modular integral, corrected Kahler data, or object-derived A6/A3. A common f(T) can at most fix saxion ratios in the toy K truncation and leaves an orthogonal axion flat; non-proportional functions or another selected effect are required for isolation. |
| [OA-C1022](#oa-c1022) | `REFUTED` | `vacuum` | Can a continuous U(1) left by a faithful C12-to-E8 Wilson line generate a Green-Schwarz/FI D-term that fixes a Kahler or axion direction on the trivial hidden-bundle branch? | No. The exact faithful Kac census gives U(1)^r with r=1,2,3,4 in 30,125,76,5 classes. For every nontrivial Wilson character H1(X,L_chi)=H1(Y,O)_chi=0, so all hidden U(1)-nonabelian, gravitational, cubic and Tr Q anomalies vanish. Flat torsion holonomy and V_hid=O^8 give zero real c1, zero hidden curvature and zero continuous GS/FI source; hence D_Q=0 identically with no charged fields and no modulus is fixed. |
| [OA-C1023](#oa-c1023) | `PROVED` | `geometry` | Does exact short-vector descent produce a lower locally-free arithmetic `(3,4)` bundle candidate while retaining all certified pointwise base and Higgs-cohomology gates? | Yes. Complete enumeration of the 5,088 signed lattice moves through norm 32 gives a fourteen-step locally-free descent from 1580 to 552. The final exact vector has Euler kernel W34, augmented global-kernel dimension six, three unit chart ideals, and rank312 modulo 1009. It is a short-move local minimum, not a certified global minimum or stable point. |
| [OA-C1024](#oa-c1024) | `REFUTED` | `geometry` | For the selected norm hypersurface and marked `(3,4)` bundle candidate, what is the first-order Atiyah obstruction from the four complex-structure directions, and how many simultaneous moduli remain? | No. The restricted calculation used only the eleven dPhi columns tangent to the old fixed-f fibre and gave tuples (6,10,4) at marked/552 and (6,6,0) at 308/76. The full incidence tangent uses all 35 equivariant dPhi columns before imposing C_q(dPhi)-f dlambda_q-lambda_q df=0. Its exact and mod-1009 tuple is (30,30,0) at every tested point. The invariant hyperExt comparison gives Ext dimensions (1,12,12,1) and proves the abstract Atiyah map has rank zero on all four invariant complex-structure directions. Thus the rank-four obstruction interpretation is refuted. |
| [OA-C1025](#oa-c1025) | `PROVED` | `geometry` | Do the marked pseudoinverse and norm-552 arithmetic maps satisfy the pointwise Hoppe vanishing H0(Lambda^2 V)=0? | Yes. The exact GF(1009) certificate gives H0(Lambda2 B)=78, Euler-relation rank 51, H0(Lambda2 G)=27, and induced rank 27 for the marked pseudoinverse and independent norm-552 and norm-308 maps. The maximal minor proves characteristic-zero injectivity and hence H0(Lambda2 V)=0. |
| [OA-C1026](#oa-c1026) | `REFUTED` | `vacuum` | Can genus-zero heterotic worldsheet instantons in the exact equivariant BCDD `(3,4)` model generate a superpotential that selects an isolated point of the surviving bundle-map P10? | No. The exact U(1)^8 field table pairs the twelve Cox and one P chiral charges with identical Fermi charges, so the full gauge-anomaly matrix vanishes term by term. At the lower height-308 map, all six W34 Euler contractions vanish identically (lambda_mu=0), giving an exact off-shell E.J=0 GLSM over Q(zeta12). Here the monad target and hypersurface degrees obey m=d=H=-K_Z with H ample and d-m=0, satisfying the Bertolini--Plesser all-degree compactness criterion. Beasley--Witten then makes every positive-degree genus-zero coefficient vanish. H2(X,Z)=Z, free lifting and sectorwise cover cancellation remove torsion, quotient and multiple-cover loopholes. Hence W_ws is identically zero and cannot select the P10. |
| [OA-C1027](#oa-c1027) | `REFUTED` | `geometry` | Is the norm-552 point globally minimal among integral exact-six locally-free maps in the rank-44 (3,4) branch, and can trace height select the bundle point? | No. The KZ vector in BUNDLE_HEIGHT_308.md has exact trace-Hermitian height 308, Euler kernel W34, augmented H0(B) kernel dimension 6, quotient rank 312 for C372 -> C312 modulo 1009, and unit ideals on all three chart orbits. Properness/good reduction certifies characteristic-zero local freeness. Therefore the norm-552 point is not globally minimal. No claim is made that 308 is globally minimal or unique; the randomized discovery is not the proof. |
| [OA-C1028](#oa-c1028) | `REFUTED` | `vacuum` | Can the classical heterotic holomorphic Chern--Simons functional plus Hermitian--Yang--Mills D-flatness select one arithmetic map from the surviving bundle P10? | No. The exact variation is delta W_HCS=2 integral Omega wedge Tr(delta A wedge F_A^(0,2)), so W_HCS is locally constant on every connected family of holomorphic structures. Donaldson--Uhlenbeck--Yau supplies one HYM connection for each stable holomorphic bundle modulo gauge, not a unique holomorphic structure. The full invariant hyperExt calculation gives twelve bundle tangent directions and zero Atiyah rank on all four complex-structure directions at every tested arithmetic point, leaving a sixteen-dimensional first-order simultaneous tangent rather than selecting one arithmetic map. |
| [OA-C1029](#oa-c1029) | `REFUTED` | `vacuum` | Do the selected algebraic Calabi--Yau, bundle, index and finite Wilson-line data fix the Kähler size, heterotic dilaton and absolute physical scales? | No. For any Ricci-flat Kähler metric g on the selected CY3, c g is Ricci-flat for every c>0 because log det(cg)=3 log c+log det g; the volume scales as c^3 while the complex variety, C12 action, Chern data and Wilson line are unchanged. The quotient has h11=1, so its Kähler cone is a positive ray, not a point. The ten-dimensional dilaton is an additional continuous field and Re f_visible depends on it. On the strict-CY tree branch W=0, so the S,T potential vanishes identically; all tested economical corrections leave a runaway or flat direction. |
| [OA-C1030](#oa-c1030) | `EXTERNAL_BLOCKER` | `vacuum` | Does the conditional heterotic MSSM spectrum come with a selected isolated supersymmetry-breaking vacuum, mediation mechanism and low-energy Standard Model limit? | Not yet. The exact cohomology result is an unbroken N=1 MSSM spectrum. The strict-CY W=0 branch preserves supersymmetry, while the class-field secondary branch has a same-topology large-radius Strominger solution but no selected differential lift or vacuum. For K=-log(S+Sbar)-3log(T+Tbar) and any W(S), the old no-scale identity leaves an arbitrary T and breaking scale. With the newly exact negative universal threshold, the complete common-function F-term potential is strictly decreasing toward decompactification for every common axion phase, so even a nonsupersymmetric finite minimum is absent. Flat hidden Wilson lines supply no FI D-term. No isolated scale, soft Lagrangian or electroweak vacuum is derived. |
| [OA-C1031](#oa-c1031) | `PROVED` | `geometry` | Does the integral (3,4) branch contain a low-height point passing the exact-six, H0, local-freeness and Higgs quotient-rank gates, and what is its polynomial Atiyah response? | Yes. The KZ vector in BUNDLE_HEIGHT_76.md has exact height 76, Euler kernel W34, augmented H0(B) kernel dimension 6, quotient rank 312 modulo 1009, and unit ideals on all three chart orbits, giving characteristic-zero local freeness. The restricted fixed-fibre linearisation has rank 6 before and after adjoining df. The subsequent full hyperExt comparison gives full-incidence tuple (30,30,0), Ext dimensions (1,12,12,1), and abstract Atiyah rank zero. This is the lowest full base/cohomology-gate point found; no global-minimum or uniqueness claim is made. |
| [OA-C1032](#oa-c1032) | `PROVED` | `geometry` | Does the exact norm-308 arithmetic map satisfy the pointwise Hoppe vanishing H0(Lambda^3 V)=0? | Yes. The exact certificate gives H0(Lambda3 B)=340, source Euler relation rank 272, H0(Lambda3 G)=68, target H0(Lambda2 B(H))=4278 with relation rank 3030, and induced rank 68 modulo 1009. Hence H0(Lambda3 V_308)=0 by a characteristic-zero maximal minor. |
| [OA-C1033](#oa-c1033) | `PROVED` | `geometry` | Do the restricted polynomial ranks equal the full sheaf-theoretic Atiyah ranks, and what are Ext1 and Ext2 for the descended exact-six BCDD monad? | Yes. The full incidence matrix has exact and mod-1009 rank tuple (30,30,0) at marked, 552, 308 and 76, whereas the old (6,10,4) tuple restricted dPhi to the tangent of the old fixed-f fibre. The invariant hyperExt q=0 row has dimensions 8->41->24, ranks 7 and 24, and cohomology (1,10,0). Toric Cech/Koszul cohomology gives two invariant adjacent-pair classes in H1(End B) and two Serre-dual classes in H2(End B); all possible higher differentials have zero source or target. Thus Ext dimensions are (1,12,12,1), and every invariant hypersurface deformation lifts as a monad, proving full Atiyah rank zero. |
| [OA-C1034](#oa-c1034) | `CONDITIONAL` | `flavor` | Do the exact norm-308 monad and selected C12/Wilson sectors yield evaluated holomorphic up and down/lepton Yukawa cup-product maps with determined ranks and Higgs line? | Conditionally. At the exact height-308 stable bundle candidate, character arithmetic allows Sym2(C3) of dimension 6 and C3 tensor C3 of dimension 9, with no C12 texture zeros. R017 makes the primary up-type proof branch-local: H1(G_Y)=0 kills both matter images and H1(K1)=H2(K1)=0 lifts the Higgs input, so cup-product naturality forces the full 1x1806 map and the Wilson 1x6 slice to rank zero. Hu=C0 is one-dimensional, while B0 is a four-dimensional trivial module leaving an unselected P3 of Hd lines. The precursor campaign records exact 33-plus-5 down-sector presentation progress and a finite-field connecting-sector reduction to one missing 1x18 determinant/residue trace row, but that Sage chain stack is not branch-local. B1167 pays the up-type provenance debt but does not select the branch or Hd line. No completed Q(zeta12) down/lepton evaluator or P3 matrix pencil is versioned here. |
| [OA-C1035](#oa-c1035) | `PROVED` | `geometry` | Can quadratic or higher Kuranishi obstruction theory isolate the proved-stable height-308 bundle and its simultaneous complex-structure deformation? | Yes. The stable locally-free height-308 point lies on an actual P10 of inequivalent bundles, so no Kuranishi term can isolate those ten directions. The multiplicative hyperExt filtration makes the fixed-bundle symmetrized quadratic map Sym^2 Ext^1(V,V)->Ext^2(V,V) rank zero. Pure complex-structure directions and all forty P*C terms lift through the exact full-incidence rank (30,30). The two adjacent U orbit classes lift to the full ambient monad because H1_Z(Hom(A,B)+Hom(B,C))=0 and the invariant Hom(B,C)->Hom(A,C) ranks equal their target dimensions (5,4,4,4,4,4). These lifts are independent of the anticanonical equation, so all eight U*C End(V)-projected products vanish. The complete quadratic End(V) projection on P+U+C is therefore zero; higher U terms and the other tangent/hermitian/anomaly components of the full heterotic L3 remain uncomputed. |
| [OA-C1040](#oa-c1040) | `REFUTED` | `vacuum` | Can the selected visible C12 Wilson line on the MSSM branches generate a nonzero flat Cheeger--Chern--Simons class and thereby supply the missing fractional W0 or flux selector? | No. The fundamental SU5 weights are (-2k,-2k,-2k,3k,3k), with c1=0 and c2 coefficient -15 k^2 mod 12. For k=4 and k=8 this is zero. Since positive-degree real cohomology of finite C12 vanishes, the Bockstein H3(BC12,R/Z)->H4(BC12,Z)_tors is an isomorphism, so the associated flat Cheeger--Chern--Simons class is zero and remains zero after pullback to X. |
| [OA-C1041](#oa-c1041) | `REFUTED` | `vacuum` | Does the native class-field character rho^4 into the center of the regular SU3 subgroup of E8 generate a nonzero fractional hidden Chern--Simons class? | No. The defining SU3 weights are (4,4,4), so c2=e2(4,4,4)=48=0 mod 12. The regular SU3 in E8 has Dynkin index one, hence no hidden normalization changes the zero. The Bockstein flat Cheeger--Chern--Simons character is therefore zero. A full 270-class control census finds 249 nonzero alternatives, so the vanishing is specific rather than vacuous. |
| [OA-C1042](#oa-c1042) | `CONDITIONAL` | `geometry` | Does the explicit height-76 (3,4)-branch bundle candidate pass both pointwise Hoppe exterior gates, and is it selected or proved minimal by the available cyclotomic and lattice data? | Conditionally. The exact Lambda2 and Lambda3 exterior presentations give induced ranks 27 and 68 at height 76, proving both vanishings pointwise and hence Hoppe stability on the fixed h11=1 free quotient. The height-76 map is C12-fixed and fixed by the 12-element marked norm/C12 subgroup, but that subgroup fixes the full 35-dimensional equivariant map space; the candidate lies outside the rank-10 trace/power/Hermitian/norm tensor span. Exact norm-32 shell enumeration remains available, while the finite rank-44 domain 33<=q<76 was not exhaustively completed because PARI qfminim exceeded stack/memory limits and the independent Fincke--Pohst attempt was stopped. No global minimality or basis-free selector theorem is claimed. |
| [OA-C1043](#oa-c1043) | `PROVED` | `vacuum` | Does the retained class-field C12 lattice action determine a unique compact-E8 lift, and what hidden centralizer and secondary class does that lift have? | Yes. The complete W(E8) census has one order-twelve class with characteristic Phi12^2 and det(1-w)=1. Thus 1-w is a torus automorphism and all normalizer lifts are conjugate; an exact 248-dimensional check gives order 12. The unique Kac row (1,0,0,1,0,0,1,0,1) has centralizer A2+A1^3+U1^3 and basic c2=2 mod 12. The Cartan--Leray edge map H3(X)->Z/12 is onto, so its flat character pulls back with exact order six. The element cannot commute with the same-factor standard SU3 and is physically usable only in the hidden E8 on the conditional equivariant-retention branch. |
| [OA-C1044](#oa-c1044) | `CONDITIONAL` | `vacuum` | Do the successful visible bundle-equivariant branches and the class-field hidden E8 lift combine into a nonzero, same-source heterotic secondary Chern--Simons character? | Conditionally. For V0=L_t tensor (TX+L_n1+L_n2), all four successful pairs give c2hat(V0)-c2hat(TX)=2 mod 12, an order-six flat character. The hidden lift gives another +2. Hence c2(TX)-c2(Vvis)-c2(Vhid)=-4=8 mod 12, exact order three; reversing conventions changes only the sign. The primary H4 class still vanishes. For generic V308 the Chern--Weil difference need not be flat, but the holomorphic CS value is locally constant modulo periods along a connected integrable deformation. The nonzero secondary requires fractional CS/H flux and leaves the strict N=1/(0,2) CY branch unless another sector cancels or backreacts. |
| [OA-C1045](#oa-c1045) | `PROVED` | `vacuum` | What exact cycle functional does the class-field E8 secondary character define on H3(X), and does it determine a normalized holomorphic period or W0? | Yes. H3(X,Z)=Z^10 maps surjectively to H3(BC12,Z)=Z/12. In an adapted integral basis the map is n->n1 mod 12, and c2=2 evaluates as chi(n)=n1/6 mod 1, an exact primitive sixth-root phase. The conditional codifferent-norm law nominates an algebraic complex-structure basepoint and residue form up to scale, but no marked H3 chain/sLag basis, period vector or physical Omega normalization has been constructed. OA-C1124 proves that the unoriented amphichiral carrier cannot select an orientation or regulator sign, and OA-C1136 refutes the claim that CS=0 plus Mostow rigidity absorbs the independent U(1) rescaling of a Calabi--Yau holomorphic three-form. The topology fixes a phase/coset, not an additive parameter-free W0. |
| [OA-C1046](#oa-c1046) | `REFUTED` | `vacuum` | Does the conditional order-three secondary class and the selected hidden centralizer produce a weakly-coupled, large-volume supersymmetric vacuum on the fixed BCDD bundle allocation? | No. For K=-log(S+Sbar)-3log(T+Tbar) and one condensate depending on S+beta T, supersymmetry requires beta(T+Tbar)=3(S+Sbar); common thresholds also leave the orthogonal axion flat. OA-C1049 proves beta_hidden=-3/(2 pi^2) on the fixed positive Kahler ray, so the required equality is impossible for positive saxions. The naive 1/3 and 2/3 normalizations moreover place the selected SU3/SU2 factors at strong coupling for canonical prefactors. Subgroup-specific thresholds, altered instanton allocation, five-branes, non-Kahler corrections or extra terms are different branches and remain unselected. |
| [OA-C1047](#oa-c1047) | `REFUTED` | `vacuum` | Does the full finite normalizer symmetry of the codifferent-norm section force all complex-structure derivatives of the residue or Chern--Simons superpotential to vanish? | No. The order-48 fan normalizer acts on the four-dimensional projective tangent as three trivial characters plus one sign character. Both the residue three-form and the universal c2/CS character are invariant because every fan matrix has determinant +1 and every unit a mod 12 has a^2=1. Symmetry therefore kills only the odd derivative and leaves three invariant complex-structure derivatives unconstrained. |
| [OA-C1048](#oa-c1048) | `REFUTED` | `framework` | Can the nonzero combined class-field secondary character coexist with the strict zero-H BCDD Calabi--Yau `(0,2)` GLSM without an additional Green--Schwarz differential trivialization? | No. The conditional visible and selected hidden coefficients add to 4 mod 12, exact order three. H4(X,Z)=Z is torsion-free, so a Green--Schwarz/Wess--Zumino differential compensator can cancel the global determinant phase, but it introduces torsionful H and exits the certified strict-CY `(0,2)` GLSM. Ordinary cyclic discrete torsion cannot repair this because H2(C12,U(1))=0. Thus the smooth flat bundle is allowed, while the simultaneous no-B strict branch is not. |
| [OA-C1049](#oa-c1049) | `PROVED` | `vacuum` | What is the exact universal one-loop linear Kähler threshold on the selected quotient and fixed visible-standard/hidden-trivial bundle allocation? | Yes. Adjunction on the anticanonical hypersurface gives integral_Y D c2(TY)=144. Division by the free C12 action and primitivity of the descended divisor gives integral_X J c2(TX)=12. In the GKL convention and with c2(Vvis)=c2(TX), c2(Vhid)=0, the parent coefficients are beta_visible=+3/(2 pi^2) and beta_hidden=-3/(2 pi^2). The flat class-field Wilson changes only secondary data, not this primary pairing; subgroup-specific massive thresholds remain uncomputed. |
| [OA-C1050](#oa-c1050) | `REFUTED` | `vacuum` | Does the finite normalizer of the selected class-field E8 holonomy act transitively on the three hidden SU(2) factors and thereby force equal thresholds, determinants and condensate phases? | No. Exact Weyl computation gives \|N_W(<w>)\|=1152 and \|C_W(w)\|=288. Because det(1-w)=1 removes torus-lift ambiguity, N_E8(<g>)/C_E8(g) is (Z/12)^*=V4. Any homomorphism V4->Out(A1^3)=S3 has image at most C2, so it cannot act transitively on the three SU2 ideals. The parent E8 still proves the common tree-level f_i=S, but one-loop functions, determinant prefactors and condensate phases require explicit quantum data; symmetry-related noninvariant points are different backgrounds, not equal terms in one vacuum. |
| [OA-C1051](#oa-c1051) | `PROVED` | `framework` | Does the selected quotient and certified stable V308 admit a compact same-topology non-Kähler Strominger-system solution that preserves the visible charged spectrum? | Yes. The Andreas--Garcia-Fernandez implicit-function theorem applies to the compact Calabi--Yau X and degree-zero stable V308 with c1=0 and c2(V)=c2(TX). For sufficiently large radius it gives a curve of conformally balanced Strominger solutions while leaving the holomorphic structure of V fixed and the tangent holomorphic structure isomorphic to the original. Hence pi1, index, bundle cohomology, Wilson projection and the audited visible charged MSSM spectrum persist. The theorem does not prescribe the order-three Cheeger--Simons class, select the radius/moduli, or provide an all-orders string vacuum. |
| [OA-C1052](#oa-c1052) | `REFUTED` | `vacuum` | Can the full two-field F-term potential on the fixed negative-threshold branch possess a finite nonsupersymmetric stationary point even though its supersymmetric equations have no positive-volume solution? | No. With b=-beta>0, z=(S+Sbar)-b(T+Tbar)>0 and q=b(T+Tbar)/z, the potential factors as b^3\|W\|^2 z^-4 F(p,q)/((1+q)q^3). Its q derivative has numerator -(3+4q)(1+2 Re p)-K(q)\|p\|^2 with K(q)>3+4q. If the first bracket is negative, \|p\|^2+(1+2 Re p)=\|1+p\|^2>=0 still makes the numerator strictly negative. Thus every finite point has a descending decompactification direction, for arbitrary common axion phase; the canonical W0=1/3,2/3 branch has no simultaneous W=P=0. No finite nonsupersymmetric minimum or Hessian candidate exists, and the orthogonal axion is separately flat. |
| [OA-C1053](#oa-c1053) | `EXTERNAL_BLOCKER` | `framework` | Is the selected order-three differential Chern--Simons component explicitly realized and transported on the large-radius Strominger family? | Not yet. The order-three anomaly is a flat degree-four differential character in H3(X,R/Z), whereas a closed ordinary B-gerbe class is degree three with flat subgroup H2(X,R/Z); adding such a flat class does not alter the degree-four anomaly. Because the integral characteristic difference vanishes, abstract geometric trivializations exist and form an Hhat3(X)-torsor. Once a marked endpoint trivialization and connection path are supplied, transgression can continue it along the contractible family. What remains absent is the actual visible/tangent refinement, connection representatives, selected torsor member, marked H3 basis and period normalization. Seam A is therefore an operational wall for physics: OA-C1109 retains a narrowly specified arithmetic comparison problem, but even its positive solution would not select this heterotic realization or its missing geometric data. |
| [OA-C1054](#oa-c1054) | `PROVED` | `flavor` | Does the exact height-308 up-type cup-product zero persist on the same-X, fixed-holomorphic-V large-radius Strominger branch? | Yes. OA-C1034 proves that the entire height-308 holomorphic up map vanishes, not merely selected character components. The AGF existence curve keeps X and the holomorphic structure of V308 fixed and changes Hermitian/HYM/tangent-connection data. Dolbeault cohomology and its wedge/contraction maps are therefore transported isomorphically, so the full and Wilson-projected up tensor remain rank zero. Invertible matter-metric normalization cannot turn zero into nonzero. Thus all three up-type quarks receive no mass from this renormalizable operator along the proved branch; a different holomorphic bundle/complex structure, heavy-field mixing, torsional worldsheet effect, spacetime nonperturbative term or SUSY-breaking operator would be new data and must be computed separately. |
| [OA-C1055](#oa-c1055) | `PROVED` | `flavor` | Does retaining exactly one massless up-type Higgs inside the same BCDD monad topology force that Higgs into the ambient image and its renormalizable up Yukawa to remain zero under coefficient variation? | Yes. For every locally-free map in the same monad topology, H1(G_X)=0 and Serre duality from H2(K1*)=0 gives H1(K1)=0. Hence H1(Lambda2 G_X*) injects equivariantly into H1(Lambda2 V*) and, after the determinant twist, contains chi0+chi1. Wilson k=4 or8 selects the unique audited H_u from the injected chi0. Naturality sends both matter inputs to zero in H1(G_X), so every coupling to that Higgs vanishes. A rank jump can help only by adding a nonambient chi0, which gives at least a second massless H_u before a separately derived mass/mixing mechanism. Therefore coefficient variation alone cannot repair Y_u while preserving the exact cohomological MSSM spectrum. |
| [OA-C1056](#oa-c1056) | `PROVED` | `physics_interface` | For the specified m004 holonomy, Gieseking beat section and selected A1 embedding, does exactly one checked sign-lift admit the semilinear beat relation and does the 27 restrict as six doublets plus fifteen singlets? | Yes. At Golden commit 4a1e4cc3 all 46 top-level certificates independently exit zero. spin_payment proves the fixed-beat sign-target dimensions {(+,+):1, others:0}; sp2_seat proves weights 6(-1)+15(0)+6(+1), nontrivial central parity, relator +I and the three beat identities on the selected A1 module. Local B1145 at 9a4eca7e independently rebuilds the E6/27 matrices from banked B1102 machinery, verifies all 3003 brackets and reproduces the same identities; its five fast locks pass. B8132 shows that the count of two spin structures is shared by several family members. The ten-word inner-modification block is not exhaustive, no typed tangent-frame Pin/spin lift or four-dimensional spin/QFT/index is constructed, and the result does not establish physical fermions or generations. |
| [OA-C1057](#oa-c1057) | `PROVED` | `lie` | For the four accepted distinguished-nonregular E6 characteristics, do the exact triples have orbit dimensions 58, 64, 66 and 70 with parity even, odd, even and even on the 27, and do all eleven accepted odd representatives satisfy the selected-beat identities? | Yes. The locked cp1_strata.py rerun is byte-identical to its stored output and gives the four dimensions 58/64/66/70 with parity even/odd/even/even. The hostile SHA-pinned extension verify_cp1_all_odd.py recomputes all accepted odd rows; all 11/11 pass relator=I, Omega^2=A27 and both intertwiners exactly. This proves compatibility for the selected rational representatives but does not prove physical fermions or select a stratum. |
| [OA-C1058](#oa-c1058) | `CONDITIONAL` | `lie` | Does the outside-bench candidate sweep independently prove that its 20 accepted E6 characteristics exhaust every nonzero nilpotent orbit and hence that exactly nine of all 20 strata are projective on the 27? | Conditionally. Every accepted label has an exact positive sl2 witness, but is_characteristic makes only four seeded generic draws per label. Failed draws do not prove nonexistence. Completeness follows only after importing the standard fact that E6 has exactly 20 nonzero nilpotent orbits; the source assert len(chars)==20 uses that count as its false-negative control while calling the census literature-free. |
| [OA-C1059](#oa-c1059) | `REFUTED` | `values` | Can the untwisted m004 Ruelle zeta be a finite product or ratio of ordinary shifted Dirichlet L-functions in the same spectral variable, in particular factors built from zeta and L(chi_-3)? | No. The logarithm of the Ruelle product has first exponent the m004 systole l0, certified strictly between log(2) and log(3). Any finite shifted ordinary Dirichlet-L product has first surviving exponent log(N) for an integer N at least 2. Uniqueness of absolutely convergent generalized Dirichlet series rules out equality. The quadratic L-factor belongs to the scalar cusp scattering determinant, not to a finite geodesic Euler-product factorization. |
| [OA-C1060](#oa-c1060) | `EXTERNAL_BLOCKER` | `values` | Does the proposed n=2 m004 Ruelle/geodesic factor have a proved cutoff-independent value or analytic continuation at s=2? | Not yet. B8129 samples three length cutoffs and seven real s values and observes no visible breakdown at s=2, with increasing cutoff sensitivity below it. This is bounded numerical evidence only; it gives no limit, error bound, order-independence proof or analytic continuation. |
| [OA-C1061](#oa-c1061) | `REFUTED` | `qft` | Do the cited Fried, Park or Pfaff torsion formulae, or the scalar m004 cusp scattering determinant, directly equal the gauge-fixed cusped graviton one-loop determinant proposed by the programme? | No. Fried-type torsion at s=0, analytic torsion of flat bundles and the scalar cusp determinant are not the Einstein spin-2/vector/scalar determinant ratio. B1157 and the corrected paper add a decisive negative control: Sym^(2m) cohomology is nonzero, so the closed-Fried acyclic value step and its reflection predictions are withdrawn. The unconditional factorization OA-C1104 survives, but it is representation algebra; the Laurent, cusp-correction and functional-equation residues OA-C1106--OA-C1108 do not repair the type mismatch. |
| [OA-C1062](#oa-c1062) | `EXTERNAL_BLOCKER` | `qft` | Can one construct and evaluate a gauge-fixed spin-2/vector/scalar one-loop determinant for the finite-volume cusped m004 geometry with controlled boundary conditions and continuous spectrum? | Not yet. No audited theorem accepts the current m004 scalar cusp determinant and returns the required Einstein one-loop ratio. B1157 and B1165 show that the infinity-place proposal remains generic spectral geometry with no action, propagator or Ward identity. Existing Ruelle/torsion identities compute different objects; even closure of OA-C1106--OA-C1108 would not by itself construct the gauge-fixed gravity determinant. OA-C1132 records the proposed but unrun m004-versus-m015 ablation. The missing deliverable remains an actual cusp gravity construction. |
| [OA-C1063](#oa-c1063) | `REFUTED` | `values` | Does the current proposal define a Beilinson regulator of J3(O), the 27-reality classes or 64 fixed dimensions and a canonical map from it to Standard-Model values? | No. The real Albert Jordan algebra is not by itself the source of an ordinary Beilinson regulator; no arithmetic scheme/motive, class, degree, target or lattice is specified. '27-reality' is not a motivic class. The claimed 64 fixed dimensions are actually a count 2^6 of sign solutions, not a 64-dimensional space. No compactification/EFT map to normalized SM parameters is defined. |
| [OA-C1064](#oa-c1064) | `EXTERNAL_BLOCKER` | `values` | Does the object uniquely select an arithmetic Albert-associated scheme or motive, a motivic class and regulator normalization, and a physical functor taking that regulator to a normalized held-out Standard-Model observable? | Not yet. Arithmetic Albert algebras, twisted Cayley planes, norm varieties and motivic regulators are legitimate mathematical objects, but the current programme selects none of them and supplies no class or observable map. This is a new construction program, not an unperformed scalar calculation and not a present critical-path shortcut. |
| [OA-C1065](#oa-c1065) | `PROVED` | `lie` | Is the exactly constructed E6-invariant cubic on the 27 one-dimensional up to scale and covariant under the selected semilinear beat? | Yes. Two independent exact computations give a 45-dimensional weight-zero cubic ansatz, rank 44 under all E6 root equations, hence a one-dimensional invariant line. All 72 root generators and six Cartans annihilate the normalized 45-term cubic. For the fixed linearization Omega=exp(q rho(E)) o gal, exact coefficient comparison gives C(Omega v)=gal(C(v)). The scalar is not canonical under Omega -> lambda Omega: it changes by lambda^3. |
| [OA-C1066](#oa-c1066) | `PROVED` | `lie` | Does the specified rational map T act consistently on every vector of both spin-two quintuplets and the full colored sector of the banked 64-dimensional complement? | Yes. The exact rational map T has rank eight on the relevant sl3 basis, intertwines the bracket on every basis pair, maps both five-level spin-two strings bijectively, and passes all 54 colored-root actions with 3 exchanged with bar3. This is the full finite-basis computation requested by the row. |
| [OA-C1067](#oa-c1067) | `REFUTED` | `lie` | Does the specified semilinear beat Sigma preserve the banked 64-dimensional complement, and what exact action does it induce on its spin-two and colored summands? | No. R020 applies the principal semilinear Sigma to an exact Killing-orthogonal 64 basis in the source-locked B1140 compact-color frame. The images of the full 64, both five-dimensional spin-two strings and the colored 54 all leave the 64, so no restricted action exists. Sigma squared also leaves the 64, while the ambient identity Sigma^2=exp(ad E_principal) holds on all 78 Chevalley basis vectors. The result is selected-frame; covariance across all 24 B1140 hits is not claimed. |
| [OA-C1068](#oa-c1068) | `PROVED` | `geometry` | What exact integral matrix does the selected Gieseking beat induce on the marked peripheral homology basis of m004? | Yes. A SHA-pinned standalone exact calculation reconstructs mu=A and lambda=bABaaBAb over Q(q), proves beat(mu)=mu and beat(lambda)=lambda^-1, and solves equality with every peripheral normal form mu^r lambda^s algebraically rather than by a word cutoff. The induced matrix is diag(1,-1), with determinant -1 and order 2. The same certificate reproduces the distinct infinite-order fiber action and its square. |
| [OA-C1069](#oa-c1069) | `PROVED` | `physics_interface` | Does the Gieseking manifold admit the proposed Pin-minus structures, and what is their exact restriction map to spin structures on its orientable double cover m004? | Yes. R021 gives H1(N;Z)=Z<t> with a=b=2t, H1(M;Z)=Z<a=b>, H^2(N;F2)=0 and hence vanishing Pin-minus obstruction in the stated convention. Both Pin-minus and spin torsors have two elements, while p^*:H^1(N;F2)->H^1(M;F2) is zero, so affine restriction is constant onto one deliberately unnamed spin structure. Naming that image is separated as OA-C1140. |
| [OA-C1070](#oa-c1070) | `PROVED` | `lie` | Is the omega-one parity clause redundant once the E6 weighted Dynkin characteristic is even, both on the accepted 20-row census and by a general lattice argument? | Yes. Exact re-tabulation gives nine even/projective rows among the locked 20 and no mismatch. More generally, if a weighted-Dynkin characteristic c=A t is even and H is integral in the E6 coroot lattice, invertibility of the E6 Cartan matrix modulo 2 forces t even, hence every 27 weight, including omega1, pairs evenly. The vector c=(2,0,0,0,0,0) shows why the integral-characteristic hypothesis is necessary: t1=8/3. |
| [OA-C1071](#oa-c1071) | `REFUTED` | `lie` | Can the square of the invariant cubic C span the degree-four invariant component of the 27 representation? | No. The proposal defines C as a degree-three invariant. Its square is homogeneous of degree six, so it cannot span any degree-four subspace. The proposed degree-four cross-check is ill-typed independently of representation matrices. |
| [OA-C1072](#oa-c1072) | `PROVED` | `lie` | What are the exact E6-invariant multiplicities in the homogeneous polynomial degrees one, two, three and four of the selected 27 representation? | Yes. An independent exact symmetric-power calculation using the locked 27 gives invariant multiplicities in degrees 1,2,3,4 equal to 0,0,1,0. At degree three the Cartan-zero basis has dimension 45 and the 1080 exact root equations have rank 44; all 72 roots and six Cartans annihilate the resulting 45-term cubic. |
| [OA-C1073](#oa-c1073) | `PROVED` | `lie` | What are the exact trilinear invariant multiplicities of 27 tensor 27 tensor 27 under full E6 and under the programme's actual selected trinification subgroup? | Yes. The exact ordered tensor-cube calculation gives a 270-dimensional Cartan-zero basis and rank 269 for full E6, hence one invariant. On the selected trinification A2-cubed generators the exact ranks are 261 on the ordered basis and 41 on the 45-dimensional symmetric basis, hence nine ordered and four symmetric invariant lines. The unique full-E6 line is the symmetric cubic. |
| [OA-C1074](#oa-c1074) | `OPEN` | `values` | What exact leading coefficient and controlled error term follow from the completed Eisenstein Dedekind zeta function for the specified zero-counting function, and do the banked zeros satisfy that theorem? | Open. The source proposes a symbolic derivation from earlier scattering data and a bounded 108-zero check. Neither a derivation nor certified error bound is committed. |
| [OA-C1075](#oa-c1075) | `PROVED` | `arithmetic` | Do a precisely specified Habiro expansion and prime-power congruence law for the figure-eight knot hold exactly over a declared finite test domain? | Yes. Two exact finite computations settle the declared domain. The raw p-power level differences have v_pi=2 in all six tested (p,r) cells, refuting naive growing coherence. The corrected Taylor-at-one comparison computes twelve integer germ coefficients and gives v_pi(I(zeta)-Taylor_N)>=N in all 24 cells for levels 4,8,9,27,5,25 and N=4,6,8,10. |
| [OA-C1076](#oa-c1076) | `REFUTED` | `values` | Does a preregistered higher-precision asymptotic extraction of the figure-eight Kashaev sequence stabilize to the proposed first coefficient and a bounded-height exact recognition of the second? | No. The preregistered 120-digit continuation through N=4000 was executed. Only about 17 digits of the first coefficient and 13 digits of the second stabilized, far below the frozen 60-digit gate, and no bounded-height recognition of the second coefficient survived. This is an honest negative for this protocol, not a proof that no asymptotic constant exists. |
| [OA-C1077](#oa-c1077) | `REFUTED` | `values` | Does a preregistered, adequately powered high-zero spacing test support the proposed GUE statistic for the specified zeta-times-L zero sequence? | No. The later T=3000 run contains 2469 zeta zeros and 2990 L(chi_-3) zeros. Each factor is relatively close to the single Wigner surmise (D=0.04013 and 0.04867), but the merged sequence is not (D=0.13359), so the preregistered single-GUE proposal fails. The distinct two-component finite-data result is recorded separately as OA-C1093. |
| [OA-C1078](#oa-c1078) | `REFUTED` | `geometry` | Is the restriction from the selected m004 character-variety component to its peripheral character data generically degree one? | No. Exact elimination on the Riley component shows the peripheral trace coefficient beta(m) is identically zero while the component is generically quadratic in the Riley coordinate. The unoriented peripheral character map is therefore generically two-to-one and blind to the mirror bit, not degree one. Oriented longitude eigenvalues L versus L^-1 can still separate the two branches. |
| [OA-C1079](#oa-c1079) | `PROVED` | `lie` | For the selected minimal A1, is the central element of 2T visible on both the 27 and 78, in contrast with the center-blind principal-A1 adjoint action? | Yes. B1146 gives 27 weights {-1:6,0:15,1:6}, so 12 states see -I, and adjoint weights {-2:1,-1:20,0:36,1:20,2:1}, so 40 states see -I. The principal adjoint restriction has only even weights and therefore factors through A4. The earlier blanket A4 statement was principal-specific. |
| [OA-C1080](#oa-c1080) | `PROVED` | `arithmetic` | Does the fixed m004 holonomy have kappa=tr[a,b]=1+q, with the beat sending it to 2-q and with trace, norm, minimal polynomial and discriminant equal to 3, 3, X^2-3X+3 and -3? | Yes. The exact Q(q), q^2=q-1 calculation gives kappa=1+q and beat(kappa)=2-q. Both have trace and norm 3, minimal polynomial X^2-3X+3 and discriminant -3; 1+q is integral of norm 3 and generates the unique prime over 3 in Z[q]. |
| [OA-C1081](#oa-c1081) | `PROVED` | `geometry` | Does the selected fiber basis realize the displayed Galois-conjugate fixed pair on the level-zero Fricke surface, exchanged by the beat, with fiber characteristic polynomial X^2-3X+1? | Yes. The points (2-q,2-q,2-4q) and (1+q,1+q,-2+4q) lie on the level-zero Fricke surface, are fixed by the stipulated trace-map action and are exchanged by the beat. The induced fiber substitution has trace 3, determinant 1 and characteristic polynomial X^2-3X+1. |
| [OA-C1082](#oa-c1082) | `REFUTED` | `geometry` | Is the displayed Galois-conjugate pair the entire fixed locus of the stipulated trace map on the cusped Fricke surface? | No. Exact elimination gives z^2(z^2+12): the fixed scheme has three support points and length four, namely the displayed simple conjugate pair and the nonreduced origin of multiplicity two. The origin is also a genuine SL2 character, witnessed by U=diag(i,-i) and V=[[0,1],[-1,0]]. Thus the pair is the unique free orbit under conjugation, but not the entire fixed locus. |
| [OA-C1083](#oa-c1083) | `REFUTED` | `geometry` | Is tr(ab^-1)=gal(kappa) an identity on the relevant character component rather than only an equality at the selected holonomy point? | No. On the Riley component P=z^2-x^2 z+2x^2-z-1=0, exact reduction gives tr(ab^-1)+kappa-3=x^2-4. Hence the proposed constant conjugation is true on the parabolic divisor x^2=4 but false generically; x=0, z=(1+sqrt(5))/2 is an explicit same-component counterexample with defect -4. OA-C1092 records the correct global sheet involution. |
| [OA-C1084](#oa-c1084) | `PROVED` | `lie` | Does the supplied geometric involution preserve the 27 rather than exchange it with its dual, lie in the inner sl2-plus-sl6 involution class, and have the same adjoint trace class on all 24 enumerated hits? | Yes. For the supplied rational matrix T, the full 12-generator monomial intertwiner proves 27 o T is isomorphic to 27, not bar27, and tr_78(T)=-2 identifies the cited inner involution class. Every one of the 24 enumerated hits also has trace -2. |
| [OA-C1085](#oa-c1085) | `PROVED` | `lie` | Are the selected Lorentz-slot weights of the 27 and 78 all even, with their tensor algebra remaining even-weighted, while the selected minimal internal A1 retains odd weights? | Yes. For the two stipulated principal A1s in orthogonal A2 slots, every recorded 27 and 78 biweight is even, and parity remains even under tensor products. The selected minimal-A1 restriction is 6 copies of the doublet plus 15 singlets, giving the exact contrasting odd sector. |
| [OA-C1086](#oa-c1086) | `PROVED` | `lie` | Does the specified Psi=C2 tensor 27 form a 54-dimensional semilinear pi1-module with the claimed relator, beat-square, 24/30 lock split, Jordan-depth parity and longitude-lock identities? | Yes. All exact matrix checks pass for the chosen module. The meridian has Jordan type 6J3+15J2+6J1; the relative central operator has a 24-dimensional positive sector and 30-dimensional negative sector; beat and depth preserve the blocks, the longitude semisimple part equals the lock, and the joint cusp-fixed space has dimension 12. Wave 5 further identifies that lock with the image of central -I in the diagonal SL2 closure while finding a 297-dimensional linear commutant, so its distinction is group realization rather than uniqueness among commuting involutions. The beat is identity on the six-dimensional deepest graded layer, longitude-fixed equals joint-cusp-fixed, and OA-C1111 records the D5 class refinement. |
| [OA-C1087](#oa-c1087) | `REFUTED` | `lie` | Is Psi=C2 tensor 27 canonically selected or unique-minimal under the algebraic requirements actually stated by the carrier construction? | No. The holonomy C2 alone is already a smaller spinorial pi1-module satisfying the beat relation. If a nontrivial internal 27 is imposed, all eleven accepted odd A1 strata pass the selected-beat identities, so the minimal-A1 factor is not source-selected. OA-C1116 proves a narrower positive theorem after adding the category 'C2 tensor a nontrivial irreducible E6 module': dimension 54 is then minimal up to 27/dual-27. That extra category does not restore object-native canonical selection. |
| [OA-C1088](#oa-c1088) | `PROVED` | `lie` | For the fixed carrier, does the symmetry-restricted invariant chain 6615 to 4 to 1 leave Y=epsilon tensor C as a unique algebraic coupling with exactly the certified meridian-depth support pattern? | Yes. The seven certificates for memos 47-53 rerun byte-identically. Conditional on the hard-coded SL2, E6 27 and bridge, the relevant invariant line is generated by epsilon_C2 tensor C_E6. The reported 6615 to 4 to 1 count and seven allowed versus eleven forbidden support blocks are exact representation-theory results. |
| [OA-C1089](#oa-c1089) | `PROVED` | `lie` | In the fixed A2^4-in-E8 possibility-space embedding, does the selected family-channel trilinear factor as epsilon_family tensor C_Jordan with no same-family support? | Yes. For the chosen A2^4 embedding, the exact Chevalley bracket/Killing trilinear on the selected (3,27) block has 270 zero-sum triples, uses all three family labels and factorizes after the stated sign gauge as epsilon_family tensor C_Jordan. OA-C1128 adds the exact rank-two family-matrix consequence in the same observer-paid possibility space. The certificates do not derive the E8 host, identify these labels with zero modes, or produce physical mass matrices. |
| [OA-C1090](#oa-c1090) | `REFUTED` | `physics_interface` | Does the present beat construction define an involutive antiunitary real structure on the carrier Hilbert space? | No. The exact operation is Galois-semilinear and its square is the nontrivial unipotent meridian, not the identity. A nontrivial unipotent matrix cannot be unitary for a positive-definite Hermitian form because it is not diagonalizable. No positive metric is constructed. Thus semilinearity is proved but antiunitarity and an involutive real structure are not. |
| [OA-C1091](#oa-c1091) | `REFUTED` | `process` | Does the immutable B1147 tree satisfy its own clean-checkout reproduction lock without relying on an uncommitted artifact? | No. At main commit 9d6979db, a clean archived-tree run gives one failure and four passes. The failure is FileNotFoundError for frontier/B1147_clane_harvest/verification/reproduce.log, which the lock test requires but the commit does not contain. Independent reruns support the memo mathematics; the defect is self-containment of the B1147 record. |
| [OA-C1092](#oa-c1092) | `PROVED` | `geometry` | On the full nonabelian Riley component, does the quadratic deck involution exchange kappa with tr(ab^-1) by kappa mapping to x^2-1-kappa? | Yes. For P=z^2-x^2 z+2x^2-z-1, one has kappa=z-1 and tau=tr(ab^-1)=x^2-z modulo P. The involution z -> x^2+1-z preserves P and sends kappa to x^2-1-kappa=tau. Equivalently kappa satisfies K^2-(x^2-1)K+(x^2-1)=0. The familiar 3-kappa formula is its x^2=4 parabolic specialization. |
| [OA-C1093](#oa-c1093) | `EMPIRICAL` | `values` | On the committed T=3000 data, are the merged zeta-times-L spacings relatively closer to the fixed-fraction two-component Wigner-surmise renewal model than to one Wigner surmise, with factor-only controls discriminating the direction? | Empirical evidence only. A dependency-free rerun gives factor-versus-Wigner D=0.04013 and 0.04867, merged-versus-one-Wigner D=0.13359, merged-versus-two-component renewal D=0.02400, and factor controls D=0.18017 and 0.19138. B1158's exact sine-kernel Gaudin replacement leaves the merged two-component distance at 0.02441. The independently rerun corrected unfoldings in OA-C1110 still leave factor residuals about 0.041--0.051, refuting the proposed unfolding explanation. The relative fit remains finite and empirical, not an independence or exact two-GUE theorem. |
| [OA-C1094](#oa-c1094) | `PROVED` | `arithmetic` | For a hyperbolic nonnegative A in GL(2,Z), is pure continued-fraction period one of its dominant eigenvalue equivalent to det(A)=-1, with trace m giving the metallic mean lambda_m? | Yes. The characteristic polynomial at determinant -1 is X^2-mX-1; nonnegativity and hyperbolicity force m=tr(A)>=1, and its dominant root obeys x=m+1/x, hence x=[overline m]. Conversely a period-one quadratic root has that minimal polynomial, so an integral 2 by 2 matrix carrying it has trace m and determinant -1. The companion matrix attains every m. |
| [OA-C1095](#oa-c1095) | `PROVED` | `carrier` | For every determinant-minus-one A of trace m, does A^2-I=mA force the mapping torus of A^2 to have H1=Z plus Z/m plus Z/m and hence knot-complement homology only at m=1? | Yes. Cayley-Hamilton gives A^2-I=mA exactly. Since A is unimodular, (mA)Z^2=mZ^2, so coker(A^2-I)=(Z/m)^2 rather than merely a group of order m^2. The Wang sequence adds one free Z; torsion vanishes exactly at m=1. |
| [OA-C1096](#oa-c1096) | `PROVED` | `arithmetic` | Are the primitive full-GL binary-quadratic-form class counts for discriminants m^2+4 equal to 1,1,1,1,1,2,1,1,2,2,1,2 through m=12, with m=6 the first repetition and the old m=12 count three explained by proper equivalence? | Yes. Exact reduction gives proper counts 1,1,1,1,1,2,1,1,2,2,1,3 and full-GL counts 1,1,1,1,1,2,1,1,2,2,1,2. At discriminant 148, swapping x and y sends (-7,6,4) to (4,6,-7), merging two proper classes; the principal cycle remains, so three proper classes become two full classes. The first repeated class is still m=6. |
| [OA-C1097](#oa-c1097) | `PROVED` | `carrier` | For M(a,b)=[[ab+1,a],[b,1]] with a,b>=1, is the mapping-torus torsion Z/gcd(a,b) plus Z/lcm(a,b), making (1,1) the only torsion-free member of the full period-two family? | Yes. M(a,b)-I has entry gcd gcd(a,b) and determinant -ab, so its Smith factors are gcd(a,b) and ab/gcd(a,b)=lcm(a,b). Both are one only when a=b=1. The diagonal M(m,m)=X_m^2 recovers the period-one squared family. |
| [OA-C1098](#oa-c1098) | `PROVED` | `lie` | Given the specified principal-2T embedding, is its four-dimensional fixed algebra toral and is its complete characteristic-zero centralizer-dimension spectrum exactly the eleven values obtained from the 109-flat A2-perpendicular arrangement? | Yes. The fixed algebra C is abelian of dimension four with dim z(C)=12. Finite-group fixed algebras in characteristic zero are reductive, so C is toral. Its six zero roots form A2; all 120 A2 subsystems are one explicitly enumerated Weyl orbit. The rational A2-perpendicular arrangement has 30 nonzero weights with profile 12x1+18x3, exactly 109 flats, and spectrum {12,14,16,18,20,26,28,30,36,46,78}. Rational dependence is unchanged over Qbar. |
| [OA-C1099](#oa-c1099) | `PROVED` | `lie` | On the specified charge-coordinate (x8,x16) plane, does the centralizer jump from 30 to 46 exactly on an irreducible rational cubic whose generated cubic field is Q[u]/(u^3-12u-5)? | Yes. For Q=ad(x16)^(-1)ad(x8) on the 48-dimensional image, the characteristic polynomial is one irreducible cubic to the sixteenth power. The exponent derives the jump 46-30=16. Its discriminant has squarefree part 77 and it acquires a root in K=Q[u]/(u^3-12u-5), identifying the generated field. Rational directions therefore remain at 30 while the cubic directions attain 46 after base change. |
| [OA-C1100](#oa-c1100) | `PROVED` | `lie` | In the fixed D5 x U(1)_psi frame, does the E6 cubic have only the 40 (16,16,10) and 5 (10,10,1) supports with conserved frame parity, while the selected beat mixes that grading on exactly 6 of 27 basis states but preserves the tested lock? | Yes. Exact E6 arithmetic gives 27=16_1+10_-2+1_4 and 45 cubic supports split as 40 (16,16,10) plus 5 (10,10,1), all conserving (-1)^q. The separately selected bridge grading differs. The beat mixes family class and parity on 6 of 27 basis columns, leaves 21 unmixed, and preserves the tested lock. OA-C1111--OA-C1113 add the exact clock census, anomaly sums and direction-level parity/lock fork; OA-C1125 exhausts the selected Z2 grading space and surviving psi torus, while OA-C1127 resolves the measured-hypercharge support labels. None turns the fixed frame into a physical dark sector or vacuum. |
| [OA-C1101](#oa-c1101) | `REFUTED` | `geometry` | Does finite-cover nonuniqueness prove the literal claim that no function of normalized hyperbolic isometry type can distinguish a manifold from its finite covers? | No. Normalized hyperbolic volume is an isometry invariant and satisfies Vol(X_tilde)=d Vol(X) for a degree-d cover, so it distinguishes the covers and refutes the literal inference. The defensible physical statement is narrower: the normalized number does not provide an external conversion to SI length, area or volume. OA-C1029 remains the valid compactification-scale obstruction. |
| [OA-C1102](#oa-c1102) | `REFUTED` | `geometry` | Is the Paper-IV list of fourteen orientable cusped census manifolds exhaustive for the declared Q(sqrt(-3)) shape-field family? | No. The source scan stops at zero-based census index 1200 in a 212641-entry census, and its paper verifier hardcodes the fourteen names without gating the field result. The manifold s955 at index 1256 is an explicit counterexample: all six regular tetrahedron shapes satisfy q^2-q+1=0, and its vendored exact gluing data pass six edge and two cusp equations, placing its shape field in Q(sqrt(-3)). |
| [OA-C1103](#oa-c1103) | `REFUTED` | `geometry` | Over the complete exactly certified Q(sqrt(-3)) cusped-census family, is H1=Z still the unique one of the seven declared elementary invariants that isolates m004? | No. B1186 regenerates the Paper-IV shape-field family at declared census and denominator bounds and corrects its size to 112. The member o10_150700 is one-cusped, belongs to that family and has H1=Z, so H1=Z does not uniquely isolate m004. That single exact counterexample refutes the proposed seven-invariant separator claim; OA-C1134 keeps the stronger exact all-cusp comparison open because B1186's cusp-shape collisions were checked numerically rather than by an exact peripheral certificate. |
| [OA-C1104](#oa-c1104) | `PROVED` | `geometry` | In the common absolute-convergence region, does the Ruelle Euler product for rho_m=Sym^(2m)(C^2) factor exactly as the product over j=-m,...,m of R(s-j,sigma_j)? | Yes. If a holonomy element has complex length L=l+i theta, Sym^(2m) has eigenvalues exp(jL), j=-m,...,m, and exp(jL)exp(-s l)=exp(i j theta)exp(-(s-j)l). Termwise multiplication therefore gives R_rho_m(s)=product_j R(s-j,sigma_j) in Re(s)>m+2. The paper checks m=0,...,4 on m004 to 5e-18 with three live controls; main independently re-derived it two ways. |
| [OA-C1105](#oa-c1105) | `REFUTED` | `geometry` | Are the m004 local systems Sym^(2m)(C^2) acyclic for m>=1, so that the closed-manifold Fried value formula used in the proposed reflection derivation applies? | No. Exact Q(sqrt(-3)) computation gives (h0,h1,h2)=(0,1,1) for m=1,...,5, already refuting acyclicity; m=0 gives (1,1,0). The general peripheral mechanism is that the parabolic cusp fixes one line in every even symmetric power, planting cusp cohomology. The paper independently reproduced the result to n=40 and withdrew the numerical reflection predictions. |
| [OA-C1106](#oa-c1106) | `EXTERNAL_BLOCKER` | `geometry` | What are the exact order of vanishing and leading Laurent coefficient at s=0 of the cusped complex-orthogonal torsion/Ruelle object for rho_m=Sym^(2m)(C^2) on m004? | Not yet. Because H^1 and H^2 are nonzero, the relevant Ruelle object has a nonzero order at s=0 rather than the finite acyclic value used by the withdrawn Fried step. Neither main nor the paper computes its leading Laurent coefficient; both route this to cusped Park/Pfaff or Cappell-Miller theory. |
| [OA-C1107](#oa-c1107) | `EXTERNAL_BLOCKER` | `geometry` | Does the exact Park/Pfaff cusp, Borel-Serre and scattering correction for the declared twisted m004 torsion equal exp(-4m Vol(m004)/pi) under one fixed normalization? | Not yet. The volume damping is presently a structural target assembled from generic hyperbolic formulas. The closed-Fried shortcut is refuted, and the existing scalar scattering identity does not supply the spin-resolved cusped equation. |
| [OA-C1108](#oa-c1108) | `EXTERNAL_BLOCKER` | `geometry` | Does a correctly completed twisted Ruelle function for the rho_m family on cusped m004 satisfy the required s-to-2-s functional equation including every cusp and scattering term? | Not yet. The exact Sym-power factorization does not provide analytic continuation or a functional equation. The current scalar determinant relation and positive-integer M-character products do not establish the negative-argument values needed by residue 2. |
| [OA-C1109](#oa-c1109) | `EXTERNAL_BLOCKER` | `arithmetic` | Does a full Arakelov/archimedean arithmetic Chern-Simons construction over Q(sqrt(-3)) define a canonical normalized map from the finite order-six phase to Vol(m004), rather than merely placing both over the same Bloch/regulator class? | Not yet. B1156 verifies z^2-z+1=0 and 2D(z)=Vol(m004), and explains why a full Arakelov codomain can contain the real regulator, but constructs no finite-phase-to-volume map. B1159 correctly reframes Seam A as a wall in substance. OA-C1124 adds the orientation/sign obstruction and OA-C1136 separates the unrelated Calabi--Yau form phase. B1198 retrieves Dong Uk Lee's arXiv:2502.11950; direct reading confirms the mixed-Tate-motive/regulator theorem and Appendix A's four figure-eight ideal-point checks. B1201 corrects B1198's marking account: because \|a1\|=1 here, the admissible tangent at each ideal point is unique. B1209 confirms this from the source and independently from the A-polynomial's four L-thin Newton-polygon edges, so the tangent torsor is trivial and cannot be the orientation bit. The augmented-character choice lambda versus lambda^-1, ideal point/local parameter, Bloch representative and augmented lift are still not jointly selected; the paper leaves motivic canonicity caveats, contains no Dedekind-zeta normalization and never maps the finite Kim/Artin-Verdier order-six phase to volume. It sharpens the literature side of the wall without supplying the requested comparison or a heterotic selector. |
| [OA-C1110](#oa-c1110) | `REFUTED` | `values` | Does a preregistered corrected finite-height unfolding, including the omitted constant and oscillatory zero-count terms, account for the residual in the committed T=3000 zeta-times-L(chi_-3) spacing data? | No. Replacing the Wigner surmise by the exact sine-kernel Gaudin law leaves the two-component distance about 0.0244. The outside corrected-unfolding certificate was independently rerun: theta-exact and local-empirical variants leave zeta residuals about 0.0416/0.0406 and L residuals about 0.0502/0.0513. The proposed explanation therefore fails on the frozen finite data; this does not refute or prove an underlying asymptotic law. |
| [OA-C1111](#oa-c1111) | `PROVED` | `lie` | In the fixed D5 x U(1)_psi frame on Psi=C^2 tensor 27, does the meridian clock have only the stated 16-to-10 and 1-to-16 transitions with the certified six-chain and cusp-fixed class census? | Yes. The bundled exact computation finds five chains with 16 bottoms and 10 tops plus one with singlet bottom and 16 top; carrier class sizes are 32/20/2 and locked counts 12/10/2. The joint cusp-fixed class projection/intersection pairs are 16:(7,1), 10:(10,5), 1:(1,0). |
| [OA-C1112](#oa-c1112) | `PROVED` | `lie` | For the fixed branching 27=16_(+1)+10_(-2)+1_(+4), do the gravitational-U(1), cubic-U(1) and SO(10)^2-U(1) anomaly coefficients cancel exactly, with 10+1 carrying the negative of the 16 contribution? | Yes. Exact integer arithmetic gives sum dim*q=0, sum dim*q^3=0 and sum T*q=0 with T(16)=2 and T(10)=1. The 16 alone contributes 16 in the first two channels; 10+1 contributes -16. Main independently reproduces these sums. |
| [OA-C1113](#oa-c1113) | `PROVED` | `vacuum` | In the fixed D5 frame and carrier lock, which 27 directions kinematically preserve matter parity, the lock, or both, and what does the selected clock do to the simultaneous-preservation directions? | Yes. The exact ledger gives 11 parity-preserving directions, 15 lock-preserving directions and exactly five preserving both; all five are class-10 weight-zero states annihilated by E27. The E6 singlet preserves frame parity but breaks the carrier lock. |
| [OA-C1114](#oa-c1114) | `PROVED` | `arithmetic` | At the four frozen levels 3*p^r with p in {5,7} and r in {1,2}, does the cube-root embedding compatible with the fixed abstract zeta_3 restore the exact global resultant-valuation coherence table through Taylor order eight? | Yes. R016 fills B1158's missing discriminating computation. The compatible embedding gives rows 2,4,...,16 at levels 15 and 75 and 2,4,6,9,10,13,14,18 at levels 21 and 147. Deliberately using the conjugate root at level 15 reproduces [2,0,...,0] through order 11, proving the old collapse is an embedding artifact. |
| [OA-C1115](#oa-c1115) | `OPEN` | `arithmetic` | Does the compatible zeta_3 embedding give uniform Habiro germ transport for every admissible prime, power and Taylor order with a correctly normalized valuation at each chosen local prime? | Open. B1158 states uniform transport, but its reproducer checks only splitting and exponents. R016 proves the corrected global-norm table on four levels; it neither quantifies over all levels nor isolates a single normalized local valuation. The universal quantifier therefore remains unproved and feasible rather than silently inherited. |
| [OA-C1116](#oa-c1116) | `PROVED` | `lie` | Within the declared category {C^2 tensor V: V a nontrivial irreducible complex E6 module}, is the 54-dimensional carrier minimal up to the 27-versus-dual-27 tie? | Yes. Exact Weyl arithmetic enumerates all 84 dominant labels with coefficient sum at most three; every nontrivial dimension is at least 27 and equality occurs only at the two minuscule fundamentals. Standard dominance monotonicity extends the bound to all dominant weights, so tensoring by C^2 gives minimum 54 up to duality. |
| [OA-C1117](#oa-c1117) | `OPEN` | `physics_interface` | Can the conditional heterotic witness's Wilson Z2, bundle parities and Higgs directions be placed in a common typed representation with the carrier lock, beat, clock and longitude, and if so do they preserve those operators? | Open. Outside tip 60bcf01d labels D1 paid, but its alignment_audit.py checks anomaly identities, dimensions and a stack hash; it loads no Wilson, bundle, Higgs, lock, beat, clock or longitude matrices and constructs no intertwiner. R017 versions the up-Yukawa proof but not this comparison. The declared closure criterion therefore remains unmet despite the semantic five-line alignment table. |
| [OA-C1118](#oa-c1118) | `OPEN` | `spectrum` | In a precisely declared rank-three abelian charge sector with a complete candidate spectrum, does the anomaly Diophantine system uniquely select an SM-normalized hypercharge direction compatible with color and weak isospin? | Open. OA-C1121 proves that a selected trinification frame realizes the universal anomaly-ratio theorem after an SM-shaped 15-state subset and nonzero quark charge are imposed. OA-C1122 shows that, within a finite generic SM-visible alphabet, full anomalies plus rigidity select the minimal SM15/conjugate pair. B1170 independently confirms that this forcing is arena-generic: no object token enters the enumeration. The object-specific unpaid input is therefore the arena itself--a selected complete light spectrum and rank-three abelian sector--plus frame, gauging and normalization. The stronger full-sector selector remains open. |
| [OA-C1119](#oa-c1119) | `PROVED` | `vacuum` | Does the exhaustive selected-D5 direction test yield exactly two SM-safe singlets, a four-dimensional joint Cartan torus, and loss of both the psi grading and carrier lock? | Yes. The independently rerun exact certificate finds precisely two SM-safe directions, states 1 and 17. Their joint Cartan stabilizer is four-dimensional and contains color, T3 and Y. Both directions are lock-odd; neither the psi grading nor the lock survives. Fifteen nontrivial root-lattice Z2 gradings remain and are separately classified by OA-C1125. |
| [OA-C1120](#oa-c1120) | `REFUTED` | `physics_interface` | Does the fixed carrier admit a precisely graded odd operator Q satisfying the proposed Q^2=rho(meridian) relation and declared covariance conditions? | No. The independently rerun finite search finds no odd Q in either declared natural covariance class. Under pi1-equivariance, locked and unlocked irreducible spectra are disjoint, so no odd intertwiner exists. Under E6/gauge-equivariance, the commutant is gl2 tensor I27 and no such odd operator squares to the prescribed A2 tensor A27. The selected beat is even and semilinear, not the missing Q. |
| [OA-C1121](#oa-c1121) | `PROVED` | `spectrum` | Within the selected trinification A2^3 frame, do all enumerated 27-derived SM-shaped 15-state assignments satisfying the four standard anomaly equations carry only the SM hypercharge ratios up to antitriplet exchange and overall scale? | Yes. The outside certificate gives 36 of 36 SM-ratio solutions in each of two color frames. R019 reproduces the exact E6/27 stack, extends the control to all three color slots and again finds 36 solutions, all SM-pattern, with no non-SM or multidimensional result. On the chiral branch Y_q is nonzero, the anomaly equations reduce universally to Y_l/Y_q=-3, Y_e/Y_q=6, (Y_u+Y_d)/Y_q=-2 and -18(Y_u/Y_q-2)(Y_u/Y_q+4)=0. If Y_q=0 is allowed, an additional vectorlike branch exists and is outside the claimed SM-ratio theorem. |
| [OA-C1122](#oa-c1122) | `PROVED` | `spectrum` | Within the declared finite SM-visible representation alphabets, do the full gauge, mixed and global anomaly constraints plus chirality and rigidity select the SM 15-state content as the smallest solution up to conjugation? | Yes. The corrected exact scan examines 252 contents in the six-representation alphabet, kills 222 already by SU(3)^3, and leaves exactly the SM15 and its conjugate after the full system. Enlargements by adjoints and (3,3)-type representations leave 7 and 14 solutions respectively but no smaller one. The result is generic model-building arithmetic. The branch's arc_verdict.json is stale and still names the withdrawn 13-state counterexample; FINDINGS.md, results.json and steps 4--6 carry the corrected verdict. |
| [OA-C1123](#oa-c1123) | `REFUTED` | `geometry` | Can a Galois-invariant datum of Q(zeta12) select one branch from the four surviving bundle and Wilson-line branches? | No. The exact branch action of Gal(Q(zeta12)/Q)=V4 is free and transitive. Every invariant function is therefore constant on all four branches, so none can select one. A non-Galois-invariant archimedean marking or extra observer choice is outside the theorem. |
| [OA-C1124](#oa-c1124) | `REFUTED` | `geometry` | Does the unoriented amphichiral m004 object canonically select an orientation, a positive signed regulator volume, or one complex embedding of Q(sqrt(-3))? | No. m004 admits an orientation-reversing self-isometry. Complex conjugation exchanges the two embeddings and the Bloch--Wigner regulator changes sign, so an automorphism-invariant datum of the unoriented object cannot distinguish +Vol from -Vol. Paper B8154 independently verifies on its chosen holonomy model that t^2 is a primitive cube root and u->u^2 is the conjugation/root swap; its prime-order subgroup argument removes shrinking the two-element symmetry as a nontrivial escape, but it supplies no preferred root. The positive volume magnitude is mirror-even and is not refuted. |
| [OA-C1125](#oa-c1125) | `PROVED` | `spectrum` | Do the selected-chain centralizer and grading censuses leave no psi remnant, exactly fifteen nontrivial root-lattice Z2 gradings, and no all-matter-odd grading? | Yes. Independent reruns give joint torus exactly equal to the SM torus and surviving psi charges 1 and -2 with gcd one, hence no continuous or discrete psi remnant. Of 15 nontrivial root-lattice gradings, exactly one has the SM-torus shadow and 14 are additional; none is odd on all 15 multiplets and none is constant-odd on the psi-10 class. The z2 script's uc/dc labels are exchanged relative to the measured-Y texture script, but the counts are exchange-invariant. |
| [OA-C1126](#oa-c1126) | `PROVED` | `spectrum` | Does every size-three orbit of the selected order-three trinification action cross the three distinct 9-blocks, making it a sector cycle rather than an intra-27 family index? | Yes. The exact census finds 36 order-three slot cyclers and nine size-three orbits. Every orbit crosses all three distinct trinification 9-blocks; none gives three copies within one block. Thus the selected Z3 is a sector cycle, not an intra-27 family index. |
| [OA-C1127](#oa-c1127) | `PROVED` | `flavor` | Does the complete E6 cubic on the selected measured-hypercharge 27 roster have exactly the declared 45-support hypergraph? | Yes. The independently rerun exact certificate finds 45 supports, including six q-u^c-Hu, six q-d^c-Hd, two l-e^c-Hd and two S-Hu-Hd supports, together with exotic-mass and proton-decay-shaped supports. B1171 independently reruns the source certificate and stresses the discriminating fact: the object-level E6 tensor permits the six up-type supports while the conditional heterotic bundle cup product in OA-C1054 vanishes. These are different mechanisms, not one established value wall. |
| [OA-C1128](#oa-c1128) | `PROVED` | `flavor` | In the selected E8 family-channel possibility space, do all complete three-by-three family matrices induced by the cubic have rank two with kernel equal to the Higgs-family direction? | Yes. The independently rerun certificate checks all 810 full-tensor family matrices. Every matrix has rank exactly two and kernel equal to the declared Higgs family, as expected from the epsilon-family factor. B1171 reproduces the result and registers the open comparison with the heterotic cup-product zero and the live E6 up-support. The result remains a structural identity in an observer-paid E8 possibility-space embedding, not a physical fermion mass matrix. |
| [OA-C1129](#oa-c1129) | `PROVED` | `geometry` | In the declared finite cyclic-word ball for m004, do the holonomy traces lie in Z[omega] and exhibit the tested mirror-partner pattern? | Yes. The independently rerun computation enumerates 275 cyclic-word classes through length seven, with every trace in Z[omega]. Mirror pairing is certified for the 25-class inner ball through length four using a targeted search through length nine. It does not establish an all-word length-spectrum theorem. |
| [OA-C1130](#oa-c1130) | `PROVED` | `spectrum` | Does exact ablation in the selected finite assignment space show that the mixed gravitational anomaly cuts the solutions while the cubic equation is redundant in the realized sector? | Yes. The independently rerun exact ablation shows that deleting the mixed gravitational anomaly enlarges the admissible spaces, while deleting the cubic equation changes no V0 count in the realized sector. This attributes constraint strength inside the frozen finite model; it is not a theorem that physical gravity creates hypercharge. |
| [OA-C1131](#oa-c1131) | `PROVED` | `framework` | Is the programme's time-arrow datum already encoded by the oriented punctured-torus bundle and monodromy, or is it an independent observer-supplied discrete datum? | Yes. B1182 proves the unique frozen C4-prime isomorphism (c,r,theta)->(k11,k7,k5). The programme's algebraic arrow is reversal r, hence the finite-place mod-four form-class leg k7, and is distinct from the archimedean orientation leg c. The object types the torsor leg; selecting a label on it remains observer-side. |
| [OA-C1132](#oa-c1132) | `OPEN` | `qft` | Does a controlled m004-versus-nonarithmetic-m015 ablation show that the proposed spectral dynamics are generic while only the volume-to-L-value avatar is arithmetic-specific? | Open. B1165 proposes the comparison but does not run it. Existing Ruelle, torsion and Laplacian constructions are generic in type, while the m004 volume-to-Dedekind-L identity is arithmetic-specific and static. Neither side currently supplies a four-dimensional action. |
| [OA-C1133](#oa-c1133) | `REFUTED` | `framework` | Are the branch-selection, being-by-hearing and measurement V4 torsors equivariantly isomorphic with their three named actions and intended labels? | No. R022 proves abstract regular-action equivalence and the sqrt(3)-versus-sqrt(5) field-label separator. In B1175 the charter author freezes named-action preservation as the intended category and adjudicates the original three-way claim false: branch selection and being-by-hearing are nonisomorphic. The productive rescope drops being-by-hearing; B1182 then proves the surviving branch-to-measurement C4-prime pair uniquely, recorded separately as OA-C1147. |
| [OA-C1134](#oa-c1134) | `OPEN` | `geometry` | Over the complete corrected exact Q(sqrt(-3)) cusped census, does the full cusp-shape datum uniquely isolate m004 up to conjugation? | Open. B1186 regenerates a 112-member family at its declared census and denominator bounds and finds two one-cusped witnesses, o9_41001 and o9_41009, numerically sharing m004's 2*sqrt(3)i cusp shape. That is a sharp near-refutation, but the committed comparison casts cusp_info to complex and uses a 1e-6 tolerance; only tetrahedron shapes and gluing equations receive exact symbolic certification. The row therefore remains open until one witness receives an exact peripheral/cusp certificate. |
| [OA-C1135](#oa-c1135) | `CONDITIONAL` | `framework` | Under the declared unoriented scale-free archimedean object, is every object-canonical datum exactly mirror-even and dimensionless? | Conditionally. B1168's examples establish useful necessary filters: an automorphism-odd sign cannot be canonical on an unoriented object, and an absolute dimensionful value cannot be extracted from scale-free data. B1169 restates awareness=mirror-even and choice=mirror-odd as a firewalled reading and explicitly asks for the missing completeness/map theorem; it supplies no such map. The converse, exhaustion of datum classes and analytic-torsion parity remain unsettled. Globally the observer ledger is adelic because the VEV choice is finite-place rather than archimedean. |
| [OA-C1136](#oa-c1136) | `REFUTED` | `vacuum` | Do CS=0 and Mostow rigidity fix the U(1) phase of a Calabi--Yau holomorphic three-form, leaving only one positive real dilaton freedom? | No. No map from the three-manifold invariant to the Calabi--Yau canonical-bundle trivialization is supplied. Rescaling Omega by exp(i theta) leaves the m004 hyperbolic structure, CS=0 and Mostow rigidity unchanged, giving an explicit U(1) counterfamily. The claim that only an R+ physical dilaton remains therefore does not follow; even that physical interpretation assumes the heterotic functor. |
| [OA-C1137](#oa-c1137) | `REFUTED` | `spectrum` | Does a degree-two trace field force representation or family multiplicities to lie only in {1,2}, thereby excluding multiplicity three? | No. Field degree constrains scalar embeddings and Galois structure, not the number of repeated summands. If V is any admissible module over Q(sqrt(-3)), then V direct-sum V direct-sum V is defined over the same degree-two field and has multiplicity three. B1161's stronger sentence is therefore false without an additional irreducibility or object-selection theorem; OA-C1126 supplies the actual selected-27 family census. |
| [OA-C1138](#oa-c1138) | `PROVED` | `framework` | After erasing programme labels and allowing an automorphism of V4, are any two free transitive four-point V4 actions equivariantly isomorphic? | Yes. R022 enumerates the regular action: the identity has cycle type 1^4, each nonidentity element has 2^2 and no fixed point, and the permutation character decomposes as 1+chi_1+chi_2+chi_12. Choosing a basepoint identifies every such torsor with V4 acting on itself by translation. |
| [OA-C1139](#oa-c1139) | `PROVED` | `framework` | If admissible maps must preserve the displayed quadratic-field and subfield annotations, are the branch-selection and being-by-hearing V4 presentations nonisomorphic? | Yes. R022 computes discriminants 144 and 225 from the three quadratic subfields. Q(zeta_12) ramifies only at {2,3}, while the being-by-hearing compositum includes Q(sqrt(5)) and ramifies at {3,5}; hence no field-annotation-preserving identification exists. B1175 authoritatively freezes field/named-label preservation as the intended category, discharging the former conditional antecedent. |
| [OA-C1140](#oa-c1140) | `OPEN` | `physics_interface` | Is the unnamed spin structure in the constant Gieseking Pin-minus restriction image exactly the B1141 beat-selected holonomy sign lift? | Open. R021 proves that both Pin-minus structures restrict to one spin structure but the zero linear map cannot name the affine image. Deck generator t, tangent Pin data, the internal 2T center and semilinear holonomy are distinct objects. No explicit frame-lift comparison to B1141 exists. |
| [OA-C1141](#oa-c1141) | `PROVED` | `framework` | Are the QP-4 self-closure obstruction, the mirror-odd orientation class and the E6 real-form fork bit images of one explicitly constructed Z2 class? | Yes. B1183 constructs a c-equivariant isomorphism between the QP-4 chord-sign torsor and the orientation torsor. Together with B1174's mirror=chirality=Gal(c) identification and the banked E6 real-form typing, the named obstruction classes are one nontrivial Z2 class. One basepoint choice trivializes the class across these faces; the finite k7 arrow remains a different bit. |
| [OA-C1142](#oa-c1142) | `REFUTED` | `framework` | Does a typed object-native observer self-map exist with a fixed point that selects the mirror-odd orientation bit? | No. B1184 split-answers the quine. A census-scoped mirror-even self-name has a fixed point, but any object-native map that selected the mirror-odd sign would give an invariant section of the nontrivial c-torsor proved in B1183. Such a sign setter cannot exist. The requested conjunction is therefore false. |
| [OA-C1143](#oa-c1143) | `EXTERNAL_BLOCKER` | `values` | Can a phason-controlled Aubry-Andre-Harper experiment measure the preregistered number of edge modes in a labelled gap well enough to distinguish the predicted counts five and six? | Not yet. B1171 adopts B8146's full-text audit: existing 13--28-waveguide demonstrations provide the phason knob but report qualitative localization, no mode count and no uncertainty or resolution for this observable. The experimental route is testable in principle but its readout does not presently exist. |
| [OA-C1144](#oa-c1144) | `PROVED` | `flavor` | What exact typed maps, if any, relate the heterotic up-cup-product zero, the nonzero E6 up-type support and the rank-two E8 family-channel kernel? | Yes. B1185 proves the three mechanisms pairwise distinct by exact invariants: the heterotic up map has rank zero while the object E6 tensor has six nonzero supports; the first zero is selective whereas the E8 family kernel is universal rank two in all 810 channels; and the E8 family index has no object-level counterpart. There is no literal one-wall identification. OA-C1148 keeps the unevaluated heterotic down tail separate. |
| [OA-C1145](#oa-c1145) | `OPEN` | `arithmetic` | Can the full OA-C1000 conductor-four reconstruction from m004 arithmetic through Q(zeta_12), the dP6 times dP6 fan and the published C12 action be reproduced by one self-contained certificate? | Open. OA-C1000 records the mathematical construction and two partial experiment scripts, but B1171's banking audit finds no single rerunnable artifact covering the complete zeta_12/dP6 reconstruction chain. This is a proof-provenance debt, not a retraction of the scoped theorem. |
| [OA-C1146](#oa-c1146) | `CONDITIONAL` | `framework` | Across a complete typed observer-datum category, does availability of an arithmetic subgroup that breaks a continuous orbit exactly distinguish finite-label choices from full archimedean observer bits? | Conditionally. B1171 derives the current orientation/VEV split from two orbit-theorem escapes: the mirror remains an archimedean automorphism, while F4(R) can shrink to F4(Z) and leave finite orbits. It explicitly registers broader typing predictions; two examples do not prove the advertised iff or define a universal cost order. |
| [OA-C1147](#oa-c1147) | `PROVED` | `framework` | After freezing the B1024 H1 quotient and branch labels, is there a unique label-preserving V4 isomorphism between the branch and measurement frames? | Yes. B1182 proves the unique isomorphism (c,r,theta)->(k11,k7,k5). The c leg is forced by the orientation/Galois result, r is the unique K-fixing reversal leg k7, and theta follows by the V4 group law. This is the valid two-frame replacement for the refuted original three-way claim OA-C1133. |
| [OA-C1148](#oa-c1148) | `OPEN` | `flavor` | Can the normalized cyclic or Serre quasi-isomorphism over Q(zeta_12) be constructed exactly and used to evaluate the norm-308 down-type and lepton Yukawa cup products? | Open. B1185 closes only the pairwise distinction among the three suppression mechanisms. Its down-tail handoff names a characteristic-zero comparison T but the required certify_yukawa_down_tail_cech_308.sage load target is absent from the shared record. The outside one-27 calculation exactly finds one SU(2)-epsilon lambda invariant and one SU(3)-delta exotic invariant, and its finite H_d menu makes the down and lepton determinant cuts coincide only at that coefficient-shape level. B1208 leaves a generation-level three-outcome fork: the cuts may coincide, become independent, or the lepton operator may be absent. R024 correctly finds coarse physical character zero for e^c and l/H_d on both retained Wilson branches, while R025 corrects its tail interpretation and proves only the physical one-dimensional pure-tail square zero. R026 then constructs the exact ordered Q(zeta_12) Euler frame, determinant comparison det(G)->L, equivariant phase and sparse local connecting formula; its exact frame minor is -72*zeta_12^2. R027 constructs the exact canonical-weight Cech generator and cyclic dual trace for dP6 and a signed 384-simplex product trace on the actual 36-chart cover of Z=dP6 x dP6, normalized to one on the marked H4(K_Z) generator. R028 pins the exact C12 chart action, all 36 common Laurent frames and the 18-positive/18-negative local orientation census; it proves raw chart monomial = q_(D,sigma)*t^u for every relevant lattice monomial and exposes the prior unordered representative and tautological commutativity checks. The generalized SU(3) ambient-type theorem does not force this mixed SU(5) product to vanish. The ambient top trace and frame transport are therefore explicit, but the Q(zeta_12) Phi/Bezout payload, characteristic-zero refinement collapse and hypersurface connecting representative delta(ctilde)/f are still required for every connecting entry; the chain-level Serre map is additionally required for tail or mixed entries. No tensor rank or B1208 fork outcome follows yet. |
| [OA-C1149](#oa-c1149) | `OPEN` | `dynamics` | Can the continuous Powers weight lambda be placed or selected by an object-native arithmetic or dynamical construction rather than carried as an independent input? | Open. B1191 separates lambda from the sigma anchor but leaves it unplaced. B1192's correctness lens rejects the attempted Q(sqrt(5)) placement: the banked lambda is a free rational/Powers weight and no map ties it to the cat-map field. B1195 GC-22 proves only the narrow BTZ/KMS tautology: choosing a free BTZ mass and inverting q=exp(-2*pi/r_+) at lambda=0.4 reproduces B723's already defined modular period. The cell's own hostile lens marks survives=false, catches a ten-order numerical error in one control and rejects the inference from that one route to every object-native placement. B721 excludes the chosen tracial-core construction, not all possible maps. Placement remains open. |
| [OA-C1150](#oa-c1150) | `OPEN` | `vacuum` | Does the surviving projective Higgs-line freedom reduce to already priced finite labels or one normalization, or does it add up to three independent continuous vacuum inputs? | Open. B1193 catches an error in the v0 input floor: the P3 Higgs line is not covered by the earlier multiplicity-one argument. Outside tip bc9d381d sharpens the test: its four Higgs slots have four distinct crystal weights, so the line reduces to a finite menu in that frame unless main's B0 block is torus-isotypic. B1195 GC-25 does not settle that comparison because its rational regular-representation stand-in assumes the action on the actual four-dimensional multiplicity space. B1205 cuts a generic P3 by a determinant cubic only to a surface, while a skew-slice control shows that such a determinant can vanish identically; no actual object tensor was evaluated. B1206/B1208 prove the lambda block is either rank zero or two by full SU(2) invariance and that the one-27 H_d menu has only one canonical functional, so those named routes do not add a cut. R024 shows e^c and l share coarse character zero on both retained branches. R025 corrects the lepton tail equation and kills only its one-dimensional pure-tail square; it leaves the three connecting B_2 directions, all mixed terms and the full GL_4-isotypic Higgs/lepton ambiguity intact. B1208's same/independent/absent tensor fork and the exact quotient dimension therefore remain unresolved. |
| [OA-C1151](#oa-c1151) | `OPEN` | `gravity` | Does a genuine E6-lattice boundary character identify the stage's sigma normalization with the banked CFT or two-sixes structure and thereby delete sigma as an independent anchor? | Open. B1190 refutes the prior synthesis as a kind error. B1191 exhausts main's q-series fingerprint route and finds its only candidate fails the required kind/positivity map; the outside artifact survey extends that negative across its Habiro, zeta-count, dark-table and coupling holdings. Tip 9915068b constructs the generic level-one E6 lattice source exactly: an Eisenstein rank-three lattice with discriminant group F3, primaries {1,27,27bar}, vacuum opening 1,78,729 and 27 opening 27,378. It still supplies no normalized map from those characters to a record-side q-series and no identification with sigma. B1195 GC-23 rules out the tested raw/direct cusp Gram constructions, but its own hostile lens rejects the universal claim: interior, linking or Poincare-Lefschetz pairings can carry cross-cusp terms and were not classified. Its claimed tie through outside memo 100 also fails because OA-C1164 refutes that memo's Riley realization. The source object exists; the character-to-record bridge remains open. |
| [OA-C1152](#oa-c1152) | `OPEN` | `framework` | For which heterogeneous grammar partners does simultaneous mirror realization define a nontrivial relational c-class, and does the grammar canonically force one such partner? | Open. B1192 proves a genuine relational mirror-odd class for exhibited heterogeneous norm-positive pairs, including the sqrt(3)-side partner, with two-sided controls. B1195 GC-24 survives narrowly as PARTIAL: the partner-unit-norm conjecture is false, and the bounded exact sweep supports gen_det=-kappa/g^2 with kappa the joint Fricke invariant and g the intersection-lattice saturation index; equal kappa=121 can yield opposite outcomes. No symbolic universal proof or exhaustive partner classification is supplied. The outside relational-kappa and first-beat certificates reproduce the exhibited pair and the all-word SL2 trace-polynomial law, but neither forces a grammar partner. The general classifier and selection rule remain open. |
| [OA-C1153](#oa-c1153) | `OPEN` | `dynamics` | Do the volume-defined schedule and Chern-Simons or saddle-defined clock represent one coherently normalized time variable on their common domain? | Open. B1197 executes one sharply typed orientation-blind comparison. The selected (1,n) ladder is monotone for 29 rungs, but across the full 78-closing B289 census \|CS\| is not monotone in volume: 15 consecutive-order violations occur and every p>=2 family fails. OA-C1167 records that exact global proposal as REFUTED. Outside memo 130 and B1208 strengthen the negative: signed CS is already two-valued at fixed volume on all 156 mirror-paired rows, and even \|CS\| has a 541-fold spread-to-window witness. B1199 also rejects the proposed reconciliation of additive saddle periods with a multiplicative Reissner--Nordstrom ratio group as a type error. The parent remains open because trajectory selection is an extra premise, the owner's D2 scope choice is still expressly untaken, the alternate saddle clock is not compared and no normalized physical conversion is constructed. A monotone unselected subtrajectory is not a coherent clock theorem. |
| [OA-C1154](#oa-c1154) | `OPEN` | `framework` | Is the outside branch-selection Z2 class exactly the finite frame-reversal leg r=k7 under the proved C4-prime isomorphism? | Open. B1182 types r=k7 within the frozen branch/measurement pair. The outside grammar certificate does not reach the carrier in the banked representation: its b-matrix has the opposite Riley sign and fails the m004 relator, recorded as OA-C1164. OA-C1165 preserves only the useful local fact that the exact reverser and golden Galois induce the same swap of two projective eigenlines. Its finite controls are not an exhaustive involution census, and no level-crossing map sends that outside branch torsor into the frozen k7 frame. The named identification remains open. |
| [OA-C1155](#oa-c1155) | `REFUTED` | `spectrum` | Are B889's three pairwise distinguishable sectors canonically the trinification Z3 family orbit, so that they supply three physical generations rather than internal frames of one 27? | No. B1190 rejects GC-8's proposed identification: the B889 frames are the Galois S3 of an explicit external cubic, not the trinification Z3. B1196 GC-26 supplies the decisive carrier obstruction: every B891 foreign eigenspace has dimension 16 and its projector spreads across all three nine-dimensional trinification blocks, so it cannot equal any one block or any union of the 9+9+9 partition. The proposed canonical identification is refuted. This negative does not produce three chiral zero-mode copies; the parent physical-generation gate remains unclosed. |
| [OA-C1156](#oa-c1156) | `OPEN` | `genesis` | Can the programme's Kolmogorov or invariant-prior principle select a unique object or basepoint rather than only a symmetry-invariant probability class? | Open. B1191 formalizes the proved finite piece: symmetry can fix the prior where it cannot fix a point, and recovers the forgotten F2/F8 locks. B1196 GC-27 is explicitly PARTIAL: it organizes finite-transitive, compact and non-normalizable examples and proves that the exhibited relational epsilon is conjugation-invariant, but gives no uniform Kolmogorov-complexity theorem and has not even typed a (T,G) pair for lambda. B1199 and R023 independently verify the full 745-class finite selection cochain and that its trace-three value is pointwise constant on each of the nine SL(2,F5) shadow classes; this is a complete finite readout, not a unique basepoint. The outside sufficiency test produces six distinct admissible sets from eight proposed predicates, gives A5 five competitors and finds that the proposed phi-stability gate is itself unforced and fails on A5. Paper B8154 removes only the vacuous proper-subgroup escape for a two-element root-swap action. OA-C0001's unrestricted encoding no-go remains an independent warning. The Selector is open. |
| [OA-C1157](#oa-c1157) | `OPEN` | `cosmology` | Can the existing genesis, no-beginning, non-cancellation and Sakharov facts be assembled into a falsifiable cosmology specification that derives an initial condition and history rather than a metaphorical Big Bang? | Open. B1196 lands a useful eight-row COSMOLOGY_LEDGER and thereby completes the inventory subtask. B1208 independently strengthens one negative: for affine Cartan characters modulo n=2 through 6, no nontrivial character leaves at least 25 of the 27 weights neutral; the smallest charged set has size 11 and largest level set 16, with a planted-representation control succeeding. This closes only the ledger's tested character-level stabilizer route. It does not exclude broader abelian representations, nonabelian symmetry, kinematic mass-ordering stability or decay selection rules. No selected four-dimensional state space or action, transition law, calibrated scale/time, inflationary alternative, physical dark-matter candidate, baryogenesis rate, CMB spectrum or structure-formation history is derived. The ledger also must say two neutral slots per 27 rather than per physical generation, since the generation/4d-fermion realization is unproved. Documentation of missing dynamics is not cosmology closure. |
| [OA-C1158](#oa-c1158) | `OPEN` | `values` | Does the object-normalized weak-mixing trace identity reproduce exactly at the independent full-tower prime 40639 after the required square-root convention transport? | Open. B895 proves the 40639 hypercharge direction and resolves the 17-versus-11 support discrepancy, but B919's distinct Weinberg-trace run remains one-prime. Its first attempted second-prime flag was caught as a silent substitution failure; the correctly substituted chain reaches the Y anchor but rational reconstruction returns None. The follow-up is explicitly registered and has no later closing arc through B1196. |
| [OA-C1159](#oa-c1159) | `OPEN` | `values` | Does object-native arithmetic force the specific D2-twisted Hermitian gauge that carries the hierarchy rather than merely show that this twist is mirror-even and available? | Open. B928 proves that H_plus D2 is carried uniquely by the already specified composite phi*=tau o phi+ o phi- within its 128-representative census, while B923 proves only that the canonical gauge is generation-degenerate. B928 explicitly warns that the census alone does not pin D2: only 16 outer pairings are symmetric, and the other candidate Hermitian structures have not been tested for generation resolution. Outside memo 92 makes D2-tw mirror-even, but admissibility is not selection. The tip's proposed premise that physics must resolve generations therefore does not leave exactly one tested candidate. The physical gauge remains unforced. |
| [OA-C1160](#oa-c1160) | `EXTERNAL_BLOCKER` | `qft` | Is there a type-correct specialization or correspondence between an E6 Seiberg-Witten curve and the banked m004 A-polynomial that supplies a nontrivial first step toward a four-dimensional lift? | Not yet. Outside tip bc9d381d exhausts the corpus and its cited construction lane: no E6 Seiberg-Witten-curve/state-integral construction exists to instantiate the comparison, the available dimension-six shadow leans mismatch, and B528 corrects the earlier nonabelian easy slice because T_K[4_1] is abelian at every rank. Main B1194 confirms no canonical 4d filling. The row is blocked on a new specialist mathematical construction, not an unrun in-repo calculation. |
| [OA-C1161](#oa-c1161) | `REFUTED` | `qft` | Does the bare m004 arithmetic force the quartic phase, amplitude and associator fields required by the proposed Fibonacci-MTC Born-content construction? | No. B729 supplies that census. The object-native trace and Alexander data give Q(sqrt(-3)) and Q(sqrt(5)); the phase Q(zeta_5), amplitude Q(zeta_20)^+ and associator field appear only in imported Fibonacci-MTC data and have distinct quartic Galois/ramification types. The outside accounting is correct to price them as overlays, but they are already a theorem-level negative rather than an unclassified missing row. |
| [OA-C1162](#oa-c1162) | `PROVED` | `arithmetic` | Is the class group of the discriminant-6237 cubic field trivial, making every prime above 953 principal? | Yes. B1093 proves O_K=Z[theta] for theta^3-12theta-5, discriminant 6237 and h(K)=h+(K)=1 by exhibiting principal generators for every prime ideal below the Minkowski bound. The B931 twist field is this same cubic field. Thus the outside accounting's item 'compute the class group to decide whether P1(953) is principal' is stale. The first outside relation harvest has a p=5 valuation bug and is excluded, but successor principal_witnesses.py gives a disjoint valid proof by explicit generators for all eight prime ideals below the Minkowski bound; R023 independently rechecks their norms and discriminating valuations. OA-C1163 separately records the norm-953 exhibit. |
| [OA-C1163](#oa-c1163) | `PROVED` | `arithmetic` | Can one construct an explicit generator pi of the selected degree-one prime above 953 in the discriminant-6237 twist field? | Yes. Outside certificate class_group_953.py reproduces the discriminant, maximal order, source-field factor and small-prime splitting table, then exhibits alpha=-26-theta+2theta^2 with exact norm 953 in the sign convention f(theta)=theta^3-12theta+5. Because f mod 953 has one degree-one factor and one irreducible quadratic, this generates the unique degree-one prime above 953. Its separate class-number relation harvest has a p=5 valuation bug and is not evidence for this row; h=1 rests on B1093. Unit normalization and the full pipeline-free meaning question are separated as OA-C1166. |
| [OA-C1164](#oa-c1164) | `REFUTED` | `geometry` | Does the outside grammar_disc48 certificate instantiate the banked m004 Riley representation and thereby prove that baBAABab is a peripheral longitude with discriminant-48 translation lattice? | No. The certificate uses b=[[1,0],[-omega,1]], while the banked Riley realization uses lower-left +omega. Its own matrices send the banked relator abABaBAbaB to [[-1,0],[-4,-1]] rather than the identity, and the script never checks that relator. After correcting the sign, baBAABab is not the banked longitude; the established peripheral word is bABaaBAb. The later form enumeration is valid for the asserted translation but cannot repair the failed representation/word gate. The advertised grammar-to-disc-48 closure is therefore refuted. |
| [OA-C1165](#oa-c1165) | `PROVED` | `dynamics` | At the trivial fixed point of the declared trace-map dynamics, do the exact reverser and nontrivial Q(sqrt(5)) Galois automorphism induce the same swap of the two projective golden eigenlines? | Yes. Outside certificate gamma5_reverser.py proves DR(v_u)=(9-4sqrt(5))v_s and DR(v_s)=(9+4sqrt(5))v_u; the two factors are inverse golden units, and the stable and unstable eigenvectors are entrywise Galois conjugate. Thus the rational-linear reverser and field Galois induce the same permutation of these two projective eigenlines; they are not literally the same linear/semilinear map. Its short control list is not an exhaustive involution census. This is not a global thermodynamic arrow or the unpaid branch-to-r map. |
| [OA-C1166](#oa-c1166) | `OPEN` | `values` | Does the explicit norm-953 generator admit an object-native unit normalization and a pipeline-free derivation explaining why that associate enters the hierarchy invariant? | Open. Class number one and alpha=-26-theta+2theta^2 prove existence and principality. The successor eight-witness proof removes the first certificate's method defect but still neither chooses a unit associate nor proves the downstream divisor equality in a pipeline-independent construction. Outside memos 102/103 sharpen the old gap to the arithmetic meaning of this single element rather than completing a physical explanation. |
| [OA-C1167](#oa-c1167) | `REFUTED` | `dynamics` | Is the reduced orientation-blind quantity \|CS\| a globally monotone reparameterization of hyperbolic volume across the full B289 78-closing census? | No. B1197 and the independent R023 rerun find 78 unoriented hyperbolic closings, reproduce the Chern--Simons sign control on 156/156 oriented pairs and obtain 15 global monotonicity violations. Every fixed-p family from p=2 through p=8 contains a violation, while a shuffled control fires 36 times. The selected (1,n) ladder is monotone for 29 rungs, so only the global orientation-blind proposal is refuted; OA-C1153's signed/saddle and trajectory-selection question remains open. |
| [OA-C1168](#oa-c1168) | `OPEN` | `framework` | Do asymmetric, noncommuting relations between unlike trace-model elements suffice to instantiate an operational occupant or observer, rather than merely form a large class of necessary-type candidates? | Open. Outside pattern_ladder.py reproducibly counts 13,120 reduced words through length eight, 180 trace values and an unordered-pair fraction satisfying noncommutation plus unequal trace that rises from 0.7481 to 0.9355 through depth five. These are free reduced words rather than proved conjugacy classes, and the code uses unordered combinations despite its ordered-pair wording. The later exact uniqueness test is an explicit counter-pressure: eight proposed predicates yield six distinct admissible sets, A5 retains five competitors, and the proposed phi-stability gate is both unforced and false on A5. Noncommutation and unequal trace are broad necessary-pattern tests; no map to an operational observer, feedback law, token selection or phenomenal state is constructed. The exact supply and nonuniqueness counts expose rather than close the sufficiency bridge. |

## Detailed answer records

## Domain: `arithmetic`

<a id="oa-c0004"></a>
### OA-C0004 — `PROVED`

- **Question:** Given m004, does reduction at the ramified Eisenstein prime produce SL(2,F3)=2T?
- **Answer:** Yes. Exact reduction and group-generation computation are banked; this is the genuine hyperbolic 2T entrance.
- **Kind/domain:** `theorem` / `arithmetic`
- **Depends on:** [OA-C0003](#oa-c0003)
- **Leads to:** [OA-C0005](#oa-c0005)
- **Closure test:** Exact group presentation/image and order check.
- **Falsifier:** Failure of the reduced generators to generate SL(2,F3).
- **Scope:** Conditional on the m004 carrier.
- **Aliases:** `B266`, `mod-3 entrance`
- **Sources:** None registered.
- **Deepest artifacts:** None registered.

<a id="oa-c1000"></a>
### OA-C1000 — `PROVED`

- **Question:** Does the marked conductor-four cusp reconstruct the ring class field Q(zeta_12), the product fan dP6 x dP6, and the published free C12 toric action?
- **Answer:** Yes. The marked order O_4=Z[2 sqrt(-3)] has ring class field H=Q(zeta_12); its two Eisenstein eigensummands give dP6 x dP6, and an explicit determinant-one basis change identifies multiplication by zeta_12 with the published A_N and twelve-cycle.
- **Kind/domain:** `construction` / `arithmetic`
- **Depends on:** [OA-C0003](#oa-c0003)
- **Leads to:** [OA-C1001](#oa-c1001), [OA-C1009](#oa-c1009), [OA-C1145](#oa-c1145)
- **Closure test:** Exact class-polynomial, integral-lattice, fan, and SL(4,Z) intertwiner certificates identifying the reconstructed action with the published C12 action.
- **Falsifier:** A class-field computation yielding a different field/action, a nonintegral conjugacy, or failure of the twelve-ray product fan reconstruction.
- **Scope:** Marked, oriented conductor-four figure-eight cusp and ambient toric reconstruction; not yet a chosen hypersurface or physical compactification.
- **Aliases:** `conductor-four ring class field`, `cyclotomic toric reconstruction`, `C12 ambient bridge`
- **Sources:** `../tracks/CLASSFIELD_HETEROTIC_BRIDGE.md`
- **Deepest artifacts:** `../experiments/verify_ringclass_z12_action.py`, `../experiments/verify_c12_action_reconstruction.py`

<a id="oa-c1075"></a>
### OA-C1075 — `PROVED`

- **Question:** Do a precisely specified Habiro expansion and prime-power congruence law for the figure-eight knot hold exactly over a declared finite test domain?
- **Answer:** Yes. Two exact finite computations settle the declared domain. The raw p-power level differences have v_pi=2 in all six tested (p,r) cells, refuting naive growing coherence. The corrected Taylor-at-one comparison computes twelve integer germ coefficients and gives v_pi(I(zeta)-Taylor_N)>=N in all 24 cells for levels 4,8,9,27,5,25 and N=4,6,8,10.
- **Kind/domain:** `computation` / `arithmetic`
- **Depends on:** [OA-C0003](#oa-c0003)
- **Leads to:** [OA-C1114](#oa-c1114), [OA-C1115](#oa-c1115)
- **Closure test:** State the normalized colored Jones/Habiro formula and exact congruence ideal first, then prove symbolic equality with a direct definition and certify every preregistered prime-power case in its cyclotomic ring.
- **Falsifier:** One exact mismatch in the normalization cross-check or one failed preregistered congruence refutes the scoped assertion.
- **Scope:** Exactly the two frozen base-one finite tables and stated normalization. The first table is a negative for raw coherence and the second a positive for germ coherence. OA-C1114 is the distinct zeta3 finite extension and OA-C1115 its universal residue; neither is silently included here.
- **Aliases:** `outside-campaign C2`, `C-AD3 Habiro tower`, `4_1 prime-power congruences`
- **Sources:** [`../evidence/MAIN_B1146_B1147_DELTA_AUDIT.md`](program-question-map/evidence/MAIN_B1146_B1147_DELTA_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/dc937010d26773ef0b5137676da3a0efd4022490/outside_bench/memos/OHTSUKI_BRIDGE.md`](https://github.com/originaxiom/origin-axiom/blob/dc937010d26773ef0b5137676da3a0efd4022490/outside_bench/memos/OHTSUKI_BRIDGE.md)
- **Deepest artifacts:** None registered.

<a id="oa-c1080"></a>
### OA-C1080 — `PROVED`

- **Question:** Does the fixed m004 holonomy have kappa=tr[a,b]=1+q, with the beat sending it to 2-q and with trace, norm, minimal polynomial and discriminant equal to 3, 3, X^2-3X+3 and -3?
- **Answer:** Yes. The exact Q(q), q^2=q-1 calculation gives kappa=1+q and beat(kappa)=2-q. Both have trace and norm 3, minimal polynomial X^2-3X+3 and discriminant -3; 1+q is integral of norm 3 and generates the unique prime over 3 in Z[q].
- **Kind/domain:** `computation` / `arithmetic`
- **Depends on:** [OA-C0003](#oa-c0003), [OA-C1068](#oa-c1068)
- **Leads to:** [OA-C1081](#oa-c1081), [OA-C1083](#oa-c1083)
- **Closure test:** Recompute kappa directly and through the Fricke identity, apply the exact beat, and certify its quadratic arithmetic and ramified norm-three ideal.
- **Falsifier:** A direct/Fricke mismatch, a beat image other than the Galois conjugate, or any failed arithmetic invariant refutes the row.
- **Scope:** The stipulated chi=+1 Riley matrices and beat. Symmetric polynomials in this conjugate pair reduce to rational expressions in trace and norm; arbitrary beat-invariant functions are not thereby generated by the number 3.
- **Aliases:** `memo 41`, `KAPPA_MEETS_BEAT`, `kappa arithmetic`
- **Sources:** [`../evidence/OUTSIDE_MEMOS_41_53_AUDIT.md`](program-question-map/evidence/OUTSIDE_MEMOS_41_53_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/afcb6c2892b20bd01ab4bf6b0aa85416472fc2f6/outside_bench/memos/KAPPA_MEETS_BEAT.md`](https://github.com/originaxiom/origin-axiom/blob/afcb6c2892b20bd01ab4bf6b0aa85416472fc2f6/outside_bench/memos/KAPPA_MEETS_BEAT.md)
- **Deepest artifacts:** None registered.

<a id="oa-c1094"></a>
### OA-C1094 — `PROVED`

- **Question:** For a hyperbolic nonnegative A in GL(2,Z), is pure continued-fraction period one of its dominant eigenvalue equivalent to det(A)=-1, with trace m giving the metallic mean lambda_m?
- **Answer:** Yes. The characteristic polynomial at determinant -1 is X^2-mX-1; nonnegativity and hyperbolicity force m=tr(A)>=1, and its dominant root obeys x=m+1/x, hence x=[overline m]. Conversely a period-one quadratic root has that minimal polynomial, so an integral 2 by 2 matrix carrying it has trace m and determinant -1. The companion matrix attains every m.
- **Kind/domain:** `theorem` / `arithmetic`
- **Depends on:** [OA-C0002](#oa-c0002)
- **Leads to:** [OA-C1095](#oa-c1095), [OA-C1096](#oa-c1096), [OA-C1097](#oa-c1097)
- **Closure test:** Prove both implications under the exact nonnegativity and hyperbolicity hypotheses and exhibit an attained matrix for every m>=1.
- **Falsifier:** A determinant-minus-one matrix in scope whose dominant root is not [overline m], or a period-one matrix in scope with another determinant, refutes the equivalence.
- **Scope:** Hyperbolic 2 by 2 integral matrices with nonnegative entries. This characterizes eigenvalue/trace data, not a unique GL(2,Z) conjugacy class or a canonical substitution-to-manifold functor.
- **Aliases:** `Paper I period-one locus`, `metallic determinant characterization`, `B8135`
- **Sources:** [`../evidence/WAVE4_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE4_BRANCH_DELTA_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/61a243c65f1a84c700e3c3d9755b11c30a5f0699/papers/series/paper1_characterization/main.tex`](https://github.com/originaxiom/origin-axiom/blob/61a243c65f1a84c700e3c3d9755b11c30a5f0699/papers/series/paper1_characterization/main.tex)
- **Deepest artifacts:** None registered.

<a id="oa-c1096"></a>
### OA-C1096 — `PROVED`

- **Question:** Are the primitive full-GL binary-quadratic-form class counts for discriminants m^2+4 equal to 1,1,1,1,1,2,1,1,2,2,1,2 through m=12, with m=6 the first repetition and the old m=12 count three explained by proper equivalence?
- **Answer:** Yes. Exact reduction gives proper counts 1,1,1,1,1,2,1,1,2,2,1,3 and full-GL counts 1,1,1,1,1,2,1,1,2,2,1,2. At discriminant 148, swapping x and y sends (-7,6,4) to (4,6,-7), merging two proper classes; the principal cycle remains, so three proper classes become two full classes. The first repeated class is still m=6.
- **Kind/domain:** `computation` / `arithmetic`
- **Depends on:** [OA-C1094](#oa-c1094)
- **Leads to:** None.
- **Closure test:** Enumerate primitive reduced indefinite forms, form proper cycles, then quotient explicitly by a determinant-minus-one transformation and reproduce the threshold.
- **Falsifier:** A missed reduced cycle, a failed determinant-minus-one identification, or a different independently reproduced full-GL count in the stated range refutes the table.
- **Scope:** Primitive indefinite binary quadratic forms of discriminant m^2+4 for 1<=m<=12. It does not assert one conjugacy class at every metallic trace.
- **Aliases:** `Paper I class threshold`, `m=12 discrepancy`, `proper versus improper forms`, `R010`
- **Sources:** [`../../../memos/PAPER1_M12_CLASS_CORRECTION.md`](../memos/PAPER1_M12_CLASS_CORRECTION.md), [`../evidence/WAVE4_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE4_BRANCH_DELTA_AUDIT.md)
- **Deepest artifacts:** [`../../../certificates/r010_gl_class_m12.py`](../certificates/r010_gl_class_m12.py)

<a id="oa-c1109"></a>
### OA-C1109 — `EXTERNAL_BLOCKER`

- **Question:** Does a full Arakelov/archimedean arithmetic Chern-Simons construction over Q(sqrt(-3)) define a canonical normalized map from the finite order-six phase to Vol(m004), rather than merely placing both over the same Bloch/regulator class?
- **Answer:** Not yet. B1156 verifies z^2-z+1=0 and 2D(z)=Vol(m004), and explains why a full Arakelov codomain can contain the real regulator, but constructs no finite-phase-to-volume map. B1159 correctly reframes Seam A as a wall in substance. OA-C1124 adds the orientation/sign obstruction and OA-C1136 separates the unrelated Calabi--Yau form phase. B1198 retrieves Dong Uk Lee's arXiv:2502.11950; direct reading confirms the mixed-Tate-motive/regulator theorem and Appendix A's four figure-eight ideal-point checks. B1201 corrects B1198's marking account: because |a1|=1 here, the admissible tangent at each ideal point is unique. B1209 confirms this from the source and independently from the A-polynomial's four L-thin Newton-polygon edges, so the tangent torsor is trivial and cannot be the orientation bit. The augmented-character choice lambda versus lambda^-1, ideal point/local parameter, Bloch representative and augmented lift are still not jointly selected; the paper leaves motivic canonicity caveats, contains no Dedekind-zeta normalization and never maps the finite Kim/Artin-Verdier order-six phase to volume. It sharpens the literature side of the wall without supplying the requested comparison or a heterotic selector.
- **Kind/domain:** `existence` / `arithmetic`
- **Depends on:** [OA-C1045](#oa-c1045), [OA-C1053](#oa-c1053), [OA-C1075](#oa-c1075)
- **Leads to:** [OA-C1002](#oa-c1002), [OA-C1007](#oa-c1007)
- **Closure test:** Construct the compactified arithmetic-CS functional including the infinity place, prove a cusped m004 specialization or controlled closed-to-cusped limit, and derive an explicit normalization mapping the finite phase to the Borel/Bloch-Wigner regulator.
- **Falsifier:** A theorem that the completions admit no canonical comparison, or that every proposed comparison merely relabels the regulator without an m004-specific map, refutes this bridge.
- **Scope:** The finite Kim/Artin-Verdier phase and archimedean Borel regulator of the figure-eight Bloch class. This is a narrowly specified mathematical comparison problem but an operational wall, not a physics door: even a positive comparison would not select a heterotic realization, a four-dimensional theory or an SM value.
- **Aliases:** `B1156 SEAM-A floor`, `finite phase to archimedean volume`, `Arakelov arithmetic-CS bridge`
- **Sources:** [`../evidence/WAVE5_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE5_BRANCH_DELTA_AUDIT.md), [`../evidence/WAVE6_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE6_BRANCH_DELTA_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/bf580f45840d121a811d2b6606c48beac92c3057/frontier/B1156_seam_a_gate2/FINDINGS.md`](https://github.com/originaxiom/origin-axiom/blob/bf580f45840d121a811d2b6606c48beac92c3057/frontier/B1156_seam_a_gate2/FINDINGS.md), [`https://github.com/originaxiom/origin-axiom/blob/bf580f45840d121a811d2b6606c48beac92c3057/frontier/B1159_mssm_debt_ledger/FINDINGS.md`](https://github.com/originaxiom/origin-axiom/blob/bf580f45840d121a811d2b6606c48beac92c3057/frontier/B1159_mssm_debt_ledger/FINDINGS.md), [`https://github.com/originaxiom/origin-axiom/blob/31b4915657dae92a5cebda8cb15fcd1177854d97/frontier/B1198_lee_motives_retrieval/FINDINGS.md`](https://github.com/originaxiom/origin-axiom/blob/31b4915657dae92a5cebda8cb15fcd1177854d97/frontier/B1198_lee_motives_retrieval/FINDINGS.md), [`https://github.com/originaxiom/origin-axiom/blob/6bd7aeb8a6acb3fd4a1bb250d15f0e91c6fcf1a3/frontier/B1201_lee_verified_and_harvest/FINDINGS.md`](https://github.com/originaxiom/origin-axiom/blob/6bd7aeb8a6acb3fd4a1bb250d15f0e91c6fcf1a3/frontier/B1201_lee_verified_and_harvest/FINDINGS.md), [`https://github.com/originaxiom/origin-axiom/blob/4526eb49214cdc3c038191870421f32d6819b79d/frontier/B1209_lee_verification/FINDINGS.md`](https://github.com/originaxiom/origin-axiom/blob/4526eb49214cdc3c038191870421f32d6819b79d/frontier/B1209_lee_verification/FINDINGS.md), [`https://arxiv.org/abs/2502.11950`](https://arxiv.org/abs/2502.11950)
- **Deepest artifacts:** [`https://github.com/originaxiom/origin-axiom/blob/bf580f45840d121a811d2b6606c48beac92c3057/frontier/B1156_seam_a_gate2/verification/reproduce.sh`](https://github.com/originaxiom/origin-axiom/blob/bf580f45840d121a811d2b6606c48beac92c3057/frontier/B1156_seam_a_gate2/verification/reproduce.sh)

<a id="oa-c1114"></a>
### OA-C1114 — `PROVED`

- **Question:** At the four frozen levels 3*p^r with p in {5,7} and r in {1,2}, does the cube-root embedding compatible with the fixed abstract zeta_3 restore the exact global resultant-valuation coherence table through Taylor order eight?
- **Answer:** Yes. R016 fills B1158's missing discriminating computation. The compatible embedding gives rows 2,4,...,16 at levels 15 and 75 and 2,4,6,9,10,13,14,18 at levels 21 and 147. Deliberately using the conjugate root at level 15 reproduces [2,0,...,0] through order 11, proving the old collapse is an embedding artifact.
- **Kind/domain:** `computation` / `arithmetic`
- **Depends on:** [OA-C1075](#oa-c1075)
- **Leads to:** [OA-C1115](#oa-c1115)
- **Closure test:** Compute the stabilized zeta3 Taylor germ, evaluate the four cyclotomic levels with the compatible root embedding, certify every global norm valuation, and reproduce the conjugate-embedding failure as a negative control.
- **Falsifier:** One valuation below the declared finite bound, unstable Taylor coefficients, or failure of the conjugate control refutes the finite correction.
- **Scope:** Exactly four levels and Taylor order eight, plus the level-15 conjugate control through order eleven. The reported values are p-adic valuations of global norms/resultants, not automatically normalized valuations at one prime above p.
- **Aliases:** `outside memo 69`, `B1158 Habiro correction`, `R016 zeta3 embedding audit`
- **Sources:** [`../../../memos/HABIRO_ZETA3_EMBEDDING_SCOPE.md`](../memos/HABIRO_ZETA3_EMBEDDING_SCOPE.md), [`../evidence/WAVE5_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE5_BRANCH_DELTA_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/c54ae43328e38947241b3be33d11557d530db3bc/frontier/B1158_cloud_wave2_harvest/FINDINGS.md`](https://github.com/originaxiom/origin-axiom/blob/c54ae43328e38947241b3be33d11557d530db3bc/frontier/B1158_cloud_wave2_harvest/FINDINGS.md)
- **Deepest artifacts:** [`../../../certificates/r016_habiro_zeta3_embeddings.py`](../certificates/r016_habiro_zeta3_embeddings.py), [`../../../outputs/r016_habiro_zeta3_embeddings.txt`](../outputs/r016_habiro_zeta3_embeddings.txt)

<a id="oa-c1115"></a>
### OA-C1115 — `OPEN`

- **Question:** Does the compatible zeta_3 embedding give uniform Habiro germ transport for every admissible prime, power and Taylor order with a correctly normalized valuation at each chosen local prime?
- **Answer:** Open. B1158 states uniform transport, but its reproducer checks only splitting and exponents. R016 proves the corrected global-norm table on four levels; it neither quantifies over all levels nor isolates a single normalized local valuation. The universal quantifier therefore remains unproved and feasible rather than silently inherited.
- **Kind/domain:** `theorem` / `arithmetic`
- **Depends on:** [OA-C1075](#oa-c1075), [OA-C1114](#oa-c1114)
- **Leads to:** None.
- **Closure test:** Prove an all-level/all-order Habiro-local theorem, specify compatible embeddings and primes above p, normalize local valuations, and recover the finite tables as consequences.
- **Falsifier:** One admissible level/order violating the normalized local bound or an incompatibility in the proposed embedding tower refutes uniform transport.
- **Scope:** A universal local arithmetic theorem for the figure-eight Habiro element at the zeta3 germ. No physical parameter or archimedean crossing follows.
- **Aliases:** `B1158 universal Habiro transport`, `zeta3 all-level local germ`
- **Sources:** [`../../../memos/HABIRO_ZETA3_EMBEDDING_SCOPE.md`](../memos/HABIRO_ZETA3_EMBEDDING_SCOPE.md), [`../evidence/WAVE5_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE5_BRANCH_DELTA_AUDIT.md)
- **Deepest artifacts:** [`../../../certificates/r016_habiro_zeta3_embeddings.py`](../certificates/r016_habiro_zeta3_embeddings.py)

<a id="oa-c1145"></a>
### OA-C1145 — `OPEN`

- **Question:** Can the full OA-C1000 conductor-four reconstruction from m004 arithmetic through Q(zeta_12), the dP6 times dP6 fan and the published C12 action be reproduced by one self-contained certificate?
- **Answer:** Open. OA-C1000 records the mathematical construction and two partial experiment scripts, but B1171's banking audit finds no single rerunnable artifact covering the complete zeta_12/dP6 reconstruction chain. This is a proof-provenance debt, not a retraction of the scoped theorem.
- **Kind/domain:** `computation` / `arithmetic`
- **Depends on:** [OA-C1000](#oa-c1000)
- **Leads to:** None.
- **Closure test:** Ship a file-relative certificate that derives the ring class field, twelve-ray product fan, integral determinant-one intertwiner and action conjugacy from frozen inputs and reproduces from any checkout.
- **Falsifier:** Failure of any derivation, a hidden preloaded target matrix or a certificate requiring untracked machine-local artifacts defeats the provenance closure.
- **Scope:** Reproducibility and dual-homing of the already scoped arithmetic/toric construction. It does not derive a heterotic realization, hypersurface, bundle or vacuum.
- **Aliases:** `B1171 construction-cert ask`, `zeta12 dP6 dual-homing`, `OA-C1000 provenance debt`
- **Sources:** [`../evidence/WAVE6_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE6_BRANCH_DELTA_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/72ace1cf91abae1be356b17e947c08894f255a8b/frontier/B1171_seam_harvest/FINDINGS.md`](https://github.com/originaxiom/origin-axiom/blob/72ace1cf91abae1be356b17e947c08894f255a8b/frontier/B1171_seam_harvest/FINDINGS.md)
- **Deepest artifacts:** None registered.

<a id="oa-c1162"></a>
### OA-C1162 — `PROVED`

- **Question:** Is the class group of the discriminant-6237 cubic field trivial, making every prime above 953 principal?
- **Answer:** Yes. B1093 proves O_K=Z[theta] for theta^3-12theta-5, discriminant 6237 and h(K)=h+(K)=1 by exhibiting principal generators for every prime ideal below the Minkowski bound. The B931 twist field is this same cubic field. Thus the outside accounting's item 'compute the class group to decide whether P1(953) is principal' is stale. The first outside relation harvest has a p=5 valuation bug and is excluded, but successor principal_witnesses.py gives a disjoint valid proof by explicit generators for all eight prime ideals below the Minkowski bound; R023 independently rechecks their norms and discriminating valuations. OA-C1163 separately records the norm-953 exhibit.
- **Kind/domain:** `theorem` / `arithmetic`
- **Depends on:** [OA-C1099](#oa-c1099)
- **Leads to:** [OA-C1163](#oa-c1163)
- **Closure test:** Prove the full ring of integers and class number by an exact Minkowski-bound ideal calculation, not a database citation, and identify the field used by the twist construction.
- **Falsifier:** A nonprincipal ideal below the Minkowski bound or a nonisomorphic twist field refutes the claim.
- **Scope:** The exact cubic field and ideal-class obstruction. Class number one does not canonically choose a generator or explain the physical relevance of 953.
- **Aliases:** `B1093 class-number closure`, `disc-6237 class group`, `P1(953) principality`
- **Sources:** [`../evidence/WAVE6_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE6_BRANCH_DELTA_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/f8e839ca39671b1165bd247b93d2f90e20aab34e/frontier/B1093_route_a_arithmetic/FINDINGS.md`](https://github.com/originaxiom/origin-axiom/blob/f8e839ca39671b1165bd247b93d2f90e20aab34e/frontier/B1093_route_a_arithmetic/FINDINGS.md), [`https://github.com/originaxiom/origin-axiom/blob/9915068bdb44f88e7cca06961d15c8cd0f7d1d0a/outside_bench/memos/PRINCIPAL_WITNESSES.md`](https://github.com/originaxiom/origin-axiom/blob/9915068bdb44f88e7cca06961d15c8cd0f7d1d0a/outside_bench/memos/PRINCIPAL_WITNESSES.md)
- **Deepest artifacts:** [`../../../certificates/r023_wave6_outside_hostile.py`](../certificates/r023_wave6_outside_hostile.py), [`../../../outputs/r023_wave6_outside_hostile.txt`](../outputs/r023_wave6_outside_hostile.txt), [`https://github.com/originaxiom/origin-axiom/blob/9915068bdb44f88e7cca06961d15c8cd0f7d1d0a/outside_bench/certificates/principal_witnesses.py`](https://github.com/originaxiom/origin-axiom/blob/9915068bdb44f88e7cca06961d15c8cd0f7d1d0a/outside_bench/certificates/principal_witnesses.py)

<a id="oa-c1163"></a>
### OA-C1163 — `PROVED`

- **Question:** Can one construct an explicit generator pi of the selected degree-one prime above 953 in the discriminant-6237 twist field?
- **Answer:** Yes. Outside certificate class_group_953.py reproduces the discriminant, maximal order, source-field factor and small-prime splitting table, then exhibits alpha=-26-theta+2theta^2 with exact norm 953 in the sign convention f(theta)=theta^3-12theta+5. Because f mod 953 has one degree-one factor and one irreducible quadratic, this generates the unique degree-one prime above 953. Its separate class-number relation harvest has a p=5 valuation bug and is not evidence for this row; h=1 rests on B1093. Unit normalization and the full pipeline-free meaning question are separated as OA-C1166.
- **Kind/domain:** `computation` / `arithmetic`
- **Depends on:** [OA-C1099](#oa-c1099), [OA-C1162](#oa-c1162)
- **Leads to:** [OA-C1166](#oa-c1166)
- **Closure test:** Identify the unique degree-one prime used by the twist and exhibit an element of exact norm 953 in the maximal order, with the field-identification and splitting gates checked.
- **Falsifier:** A norm other than 953, a nonmaximal-order computation or selection of the degree-two prime refutes the exhibit.
- **Scope:** Constructive principality of the degree-one 953 prime. It does not canonically choose a unit associate, explain why physics uses 953 or derive a measured parameter.
- **Aliases:** `953 explicit generator`, `twist-prime divisor formula`, `B931 residual`
- **Sources:** [`../evidence/WAVE6_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE6_BRANCH_DELTA_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/bc9d381d0018cdc112ddac2373fe767ee4247531/outside_bench/certificates/class_group_953.py`](https://github.com/originaxiom/origin-axiom/blob/bc9d381d0018cdc112ddac2373fe767ee4247531/outside_bench/certificates/class_group_953.py), [`https://github.com/originaxiom/origin-axiom/blob/9915068bdb44f88e7cca06961d15c8cd0f7d1d0a/outside_bench/certificates/principal_witnesses.py`](https://github.com/originaxiom/origin-axiom/blob/9915068bdb44f88e7cca06961d15c8cd0f7d1d0a/outside_bench/certificates/principal_witnesses.py)
- **Deepest artifacts:** [`../../../certificates/r023_wave6_outside_hostile.py`](../certificates/r023_wave6_outside_hostile.py), [`../../../outputs/r023_wave6_outside_hostile.txt`](../outputs/r023_wave6_outside_hostile.txt), [`https://github.com/originaxiom/origin-axiom/blob/bc9d381d0018cdc112ddac2373fe767ee4247531/outside_bench/outputs/class_group_953_out.txt`](https://github.com/originaxiom/origin-axiom/blob/bc9d381d0018cdc112ddac2373fe767ee4247531/outside_bench/outputs/class_group_953_out.txt)

## Domain: `carrier`

<a id="oa-c0003"></a>
### OA-C0003 — `CONDITIONAL`

- **Question:** Does the Fibonacci substitution canonically determine the oriented punctured-torus mapping torus m004?
- **Answer:** Conditionally. Squaring the determinant-minus-one incidence gives RL, but letter-to-Dehn-twist, puncture, orientation, and mapping-torus operations are extra typed data.
- **Kind/domain:** `construction` / `carrier`
- **Depends on:** [OA-C0002](#oa-c0002)
- **Leads to:** [OA-C0004](#oa-c0004), [OA-C1000](#oa-c1000), [OA-C1068](#oa-c1068), [OA-C1074](#oa-c1074), [OA-C1075](#oa-c1075), [OA-C1076](#oa-c1076), [OA-C1077](#oa-c1077), [OA-C1078](#oa-c1078), [OA-C1164](#oa-c1164)
- **Closure test:** A unique natural functor from the admitted description category to oriented 3-manifold carriers.
- **Falsifier:** Two inequivalent admissible carrier functors from the same substitution.
- **Scope:** Current paper/repository carrier construction.
- **Aliases:** `carrier axiom`, `C3`, `C4`, `C5`
- **Sources:** `../tracks/GENESIS.md`
- **Deepest artifacts:** None registered.

<a id="oa-c1095"></a>
### OA-C1095 — `PROVED`

- **Question:** For every determinant-minus-one A of trace m, does A^2-I=mA force the mapping torus of A^2 to have H1=Z plus Z/m plus Z/m and hence knot-complement homology only at m=1?
- **Answer:** Yes. Cayley-Hamilton gives A^2-I=mA exactly. Since A is unimodular, (mA)Z^2=mZ^2, so coker(A^2-I)=(Z/m)^2 rather than merely a group of order m^2. The Wang sequence adds one free Z; torsion vanishes exactly at m=1.
- **Kind/domain:** `theorem` / `carrier`
- **Depends on:** [OA-C0003](#oa-c0003), [OA-C1094](#oa-c1094)
- **Leads to:** None.
- **Closure test:** Use Cayley-Hamilton over the integers and the Wang sequence to determine the full Smith invariants, not only the torsion order.
- **Falsifier:** A matrix in scope whose cokernel has different invariant factors, or a value m>1 with torsion-free mapping-torus H1, refutes the claim.
- **Scope:** The mapping torus after the once-punctured-torus realization and orientation choices are supplied. The arithmetic theorem does not derive those typed choices from the substitution.
- **Aliases:** `Paper I trace-only selection`, `A squared minus I equals mA`, `metallic mapping-torus torsion`
- **Sources:** [`../evidence/WAVE4_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE4_BRANCH_DELTA_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/61a243c65f1a84c700e3c3d9755b11c30a5f0699/papers/series/paper1_characterization/main.tex`](https://github.com/originaxiom/origin-axiom/blob/61a243c65f1a84c700e3c3d9755b11c30a5f0699/papers/series/paper1_characterization/main.tex)
- **Deepest artifacts:** None registered.

<a id="oa-c1097"></a>
### OA-C1097 — `PROVED`

- **Question:** For M(a,b)=[[ab+1,a],[b,1]] with a,b>=1, is the mapping-torus torsion Z/gcd(a,b) plus Z/lcm(a,b), making (1,1) the only torsion-free member of the full period-two family?
- **Answer:** Yes. M(a,b)-I has entry gcd gcd(a,b) and determinant -ab, so its Smith factors are gcd(a,b) and ab/gcd(a,b)=lcm(a,b). Both are one only when a=b=1. The diagonal M(m,m)=X_m^2 recovers the period-one squared family.
- **Kind/domain:** `theorem` / `carrier`
- **Depends on:** [OA-C1094](#oa-c1094)
- **Leads to:** None.
- **Closure test:** Compute the Smith invariants of M(a,b)-I symbolically for arbitrary positive integers a,b and solve the torsion-free condition.
- **Falsifier:** One positive pair with different invariant factors or one pair other than (1,1) with trivial torsion refutes the theorem.
- **Scope:** The declared two-parameter period-two matrices and their mapping-torus homology. Nothing is claimed for periods at least three or for a canonical carrier functor.
- **Aliases:** `Paper I period-two price`, `two-letter metallic relaxation`
- **Sources:** [`../evidence/WAVE4_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE4_BRANCH_DELTA_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/61a243c65f1a84c700e3c3d9755b11c30a5f0699/papers/series/paper1_characterization/main.tex`](https://github.com/originaxiom/origin-axiom/blob/61a243c65f1a84c700e3c3d9755b11c30a5f0699/papers/series/paper1_characterization/main.tex)
- **Deepest artifacts:** None registered.

## Domain: `cosmology`

<a id="oa-c1157"></a>
### OA-C1157 — `OPEN`

- **Question:** Can the existing genesis, no-beginning, non-cancellation and Sakharov facts be assembled into a falsifiable cosmology specification that derives an initial condition and history rather than a metaphorical Big Bang?
- **Answer:** Open. B1196 lands a useful eight-row COSMOLOGY_LEDGER and thereby completes the inventory subtask. B1208 independently strengthens one negative: for affine Cartan characters modulo n=2 through 6, no nontrivial character leaves at least 25 of the 27 weights neutral; the smallest charged set has size 11 and largest level set 16, with a planted-representation control succeeding. This closes only the ledger's tested character-level stabilizer route. It does not exclude broader abelian representations, nonabelian symmetry, kinematic mass-ordering stability or decay selection rules. No selected four-dimensional state space or action, transition law, calibrated scale/time, inflationary alternative, physical dark-matter candidate, baryogenesis rate, CMB spectrum or structure-formation history is derived. The ledger also must say two neutral slots per 27 rather than per physical generation, since the generation/4d-fermion realization is unproved. Documentation of missing dynamics is not cosmology closure.
- **Kind/domain:** `construction` / `cosmology`
- **Depends on:** [OA-C0017](#oa-c0017)
- **Leads to:** None.
- **Closure test:** Publish one typed cosmology ledger with state space, dynamics or transition law, scale and time inputs, inflation/dark-sector obligations and at least one discriminating observable, with every banked no-go respected.
- **Falsifier:** Absence of equations of motion, a noncanonical four-dimensional lift, an imported scale or only retrospective numerical matches prevents cosmological closure.
- **Scope:** A modern typed cosmology ledger for this programme. The object's internal Lambda=-1 and dimensionless tick do not by themselves give the observed four-dimensional cosmology.
- **Aliases:** `B1194 cosmology ledger`, `X3-X5 blind region`, `initial-condition audit`
- **Sources:** [`../evidence/WAVE6_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE6_BRANCH_DELTA_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/40916c36ddeb1eb1631097b3535c6a79a2658e23/docs/COSMOLOGY_LEDGER.md`](https://github.com/originaxiom/origin-axiom/blob/40916c36ddeb1eb1631097b3535c6a79a2658e23/docs/COSMOLOGY_LEDGER.md), [`https://github.com/originaxiom/origin-axiom/blob/40916c36ddeb1eb1631097b3535c6a79a2658e23/frontier/B1196_close_loop_batch5b/verification/batch5b_cells.json`](https://github.com/originaxiom/origin-axiom/blob/40916c36ddeb1eb1631097b3535c6a79a2658e23/frontier/B1196_close_loop_batch5b/verification/batch5b_cells.json), [`https://github.com/originaxiom/origin-axiom/blob/1f2a1012286ff00b86fca99395d07aae346ca69b/outside_bench/certificates/dm_census.py`](https://github.com/originaxiom/origin-axiom/blob/1f2a1012286ff00b86fca99395d07aae346ca69b/outside_bench/certificates/dm_census.py), [`https://github.com/originaxiom/origin-axiom/blob/b0d8f37c7205cf43520a0710f6b7c7c66634a0dc/frontier/B1208_cross_seat_harvest/FINDINGS.md`](https://github.com/originaxiom/origin-axiom/blob/b0d8f37c7205cf43520a0710f6b7c7c66634a0dc/frontier/B1208_cross_seat_harvest/FINDINGS.md)
- **Deepest artifacts:** None registered.

## Domain: `dynamics`

<a id="oa-c1149"></a>
### OA-C1149 — `OPEN`

- **Question:** Can the continuous Powers weight lambda be placed or selected by an object-native arithmetic or dynamical construction rather than carried as an independent input?
- **Answer:** Open. B1191 separates lambda from the sigma anchor but leaves it unplaced. B1192's correctness lens rejects the attempted Q(sqrt(5)) placement: the banked lambda is a free rational/Powers weight and no map ties it to the cat-map field. B1195 GC-22 proves only the narrow BTZ/KMS tautology: choosing a free BTZ mass and inverting q=exp(-2*pi/r_+) at lambda=0.4 reproduces B723's already defined modular period. The cell's own hostile lens marks survives=false, catches a ten-order numerical error in one control and rejects the inference from that one route to every object-native placement. B721 excludes the chosen tracial-core construction, not all possible maps. Placement remains open.
- **Kind/domain:** `construction` / `dynamics`
- **Depends on:** [OA-C0017](#oa-c0017)
- **Leads to:** None.
- **Closure test:** Define lambda in one typed dynamical category, derive its value or orbit from object data and prove uniqueness without importing a fitted thermal or measured parameter.
- **Falsifier:** A family of equally admissible lambda values, or a proposed field assignment with no source map from the object, refutes intrinsic placement.
- **Scope:** The declared continuous type-III/Powers parameter. It must not be confused with a Dirac or Laplace eigenvalue also denoted lambda.
- **Aliases:** `B1193 lambda placement`, `Powers weight`, `type-III clock datum`
- **Sources:** [`../evidence/WAVE6_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE6_BRANCH_DELTA_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/0f1c627e5c290439e4f6eeb3723fb5d9f83195d7/docs/GRAND_COMPUTATION_v0.md`](https://github.com/originaxiom/origin-axiom/blob/0f1c627e5c290439e4f6eeb3723fb5d9f83195d7/docs/GRAND_COMPUTATION_v0.md), [`https://github.com/originaxiom/origin-axiom/blob/40916c36ddeb1eb1631097b3535c6a79a2658e23/frontier/B1195_close_loop_batch5a/verification/batch5a_cells.json`](https://github.com/originaxiom/origin-axiom/blob/40916c36ddeb1eb1631097b3535c6a79a2658e23/frontier/B1195_close_loop_batch5a/verification/batch5a_cells.json)
- **Deepest artifacts:** None registered.

<a id="oa-c1153"></a>
### OA-C1153 — `OPEN`

- **Question:** Do the volume-defined schedule and Chern-Simons or saddle-defined clock represent one coherently normalized time variable on their common domain?
- **Answer:** Open. B1197 executes one sharply typed orientation-blind comparison. The selected (1,n) ladder is monotone for 29 rungs, but across the full 78-closing B289 census |CS| is not monotone in volume: 15 consecutive-order violations occur and every p>=2 family fails. OA-C1167 records that exact global proposal as REFUTED. Outside memo 130 and B1208 strengthen the negative: signed CS is already two-valued at fixed volume on all 156 mirror-paired rows, and even |CS| has a 541-fold spread-to-window witness. B1199 also rejects the proposed reconciliation of additive saddle periods with a multiplicative Reissner--Nordstrom ratio group as a type error. The parent remains open because trajectory selection is an extra premise, the owner's D2 scope choice is still expressly untaken, the alternate saddle clock is not compared and no normalized physical conversion is constructed. A monotone unselected subtrajectory is not a coherent clock theorem.
- **Kind/domain:** `comparison` / `dynamics`
- **Depends on:** [OA-C0017](#oa-c0017), [OA-C1124](#oa-c1124)
- **Leads to:** [OA-C1167](#oa-c1167)
- **Closure test:** Define both clocks as typed maps, fix orientation and normalization conventions, construct their comparison and test equality with a negative control.
- **Falsifier:** Incompatible domains, opposite transformation laws or a nonconstant conversion factor refute one-clock coherence.
- **Scope:** Internal dimensionless clock coordinates. Agreement would not calibrate seconds, produce a causal arrow or derive equations of motion.
- **Aliases:** `B1193 Vol-CS coherence`, `two-clock comparison`, `clock-coherence run`
- **Sources:** [`../evidence/WAVE6_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE6_BRANCH_DELTA_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/0f1c627e5c290439e4f6eeb3723fb5d9f83195d7/docs/GRAND_COMPUTATION_LEDGER.md`](https://github.com/originaxiom/origin-axiom/blob/0f1c627e5c290439e4f6eeb3723fb5d9f83195d7/docs/GRAND_COMPUTATION_LEDGER.md), [`https://github.com/originaxiom/origin-axiom/blob/31b4915657dae92a5cebda8cb15fcd1177854d97/frontier/B1197_clock_coherence/FINDINGS.md`](https://github.com/originaxiom/origin-axiom/blob/31b4915657dae92a5cebda8cb15fcd1177854d97/frontier/B1197_clock_coherence/FINDINGS.md), [`https://github.com/originaxiom/origin-axiom/blob/63c047059645fded83d8cdf4976139804df5c644/frontier/B1199_register_reads_and_L188/FINDINGS.md`](https://github.com/originaxiom/origin-axiom/blob/63c047059645fded83d8cdf4976139804df5c644/frontier/B1199_register_reads_and_L188/FINDINGS.md), [`https://github.com/originaxiom/origin-axiom/blob/287e8f75efa34141dfb00ff2c30215cd50036ee5/outside_bench/THE_D2_DECISION.md`](https://github.com/originaxiom/origin-axiom/blob/287e8f75efa34141dfb00ff2c30215cd50036ee5/outside_bench/THE_D2_DECISION.md), [`https://github.com/originaxiom/origin-axiom/blob/b0d8f37c7205cf43520a0710f6b7c7c66634a0dc/frontier/B1208_cross_seat_harvest/FINDINGS.md`](https://github.com/originaxiom/origin-axiom/blob/b0d8f37c7205cf43520a0710f6b7c7c66634a0dc/frontier/B1208_cross_seat_harvest/FINDINGS.md)
- **Deepest artifacts:** None registered.

<a id="oa-c1165"></a>
### OA-C1165 — `PROVED`

- **Question:** At the trivial fixed point of the declared trace-map dynamics, do the exact reverser and nontrivial Q(sqrt(5)) Galois automorphism induce the same swap of the two projective golden eigenlines?
- **Answer:** Yes. Outside certificate gamma5_reverser.py proves DR(v_u)=(9-4sqrt(5))v_s and DR(v_s)=(9+4sqrt(5))v_u; the two factors are inverse golden units, and the stable and unstable eigenvectors are entrywise Galois conjugate. Thus the rational-linear reverser and field Galois induce the same permutation of these two projective eigenlines; they are not literally the same linear/semilinear map. Its short control list is not an exhaustive involution census. This is not a global thermodynamic arrow or the unpaid branch-to-r map.
- **Kind/domain:** `theorem` / `dynamics`
- **Depends on:** [OA-C1094](#oa-c1094), [OA-C1131](#oa-c1131)
- **Leads to:** [OA-C1154](#oa-c1154)
- **Closure test:** Differentiate the exact trace-map reverser, construct both eigenlines over Q(sqrt(5)) and prove their exchange up to nonzero field units; compare with entrywise field conjugation without identifying linear and semilinear maps.
- **Falsifier:** Failure to exchange the two eigenspaces, or proportionality factors outside Q(sqrt(5)), refutes the scoped projective identification.
- **Scope:** The derivative at one fixed point and the two golden eigendirections. The programme name gamma5 and any physical arrow-of-time interpretation are not proved by this local algebra.
- **Aliases:** `outside memo 101`, `golden reverser`, `linearized time reversal`
- **Sources:** [`../evidence/WAVE6_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE6_BRANCH_DELTA_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/bc9d381d0018cdc112ddac2373fe767ee4247531/outside_bench/memos/GAMMA5_REVERSER.md`](https://github.com/originaxiom/origin-axiom/blob/bc9d381d0018cdc112ddac2373fe767ee4247531/outside_bench/memos/GAMMA5_REVERSER.md)
- **Deepest artifacts:** [`../../../certificates/r023_wave6_outside_hostile.py`](../certificates/r023_wave6_outside_hostile.py), [`../../../outputs/r023_wave6_outside_hostile.txt`](../outputs/r023_wave6_outside_hostile.txt), [`https://github.com/originaxiom/origin-axiom/blob/bc9d381d0018cdc112ddac2373fe767ee4247531/outside_bench/certificates/gamma5_reverser.py`](https://github.com/originaxiom/origin-axiom/blob/bc9d381d0018cdc112ddac2373fe767ee4247531/outside_bench/certificates/gamma5_reverser.py)

<a id="oa-c1167"></a>
### OA-C1167 — `REFUTED`

- **Question:** Is the reduced orientation-blind quantity |CS| a globally monotone reparameterization of hyperbolic volume across the full B289 78-closing census?
- **Answer:** No. B1197 and the independent R023 rerun find 78 unoriented hyperbolic closings, reproduce the Chern--Simons sign control on 156/156 oriented pairs and obtain 15 global monotonicity violations. Every fixed-p family from p=2 through p=8 contains a violation, while a shuffled control fires 36 times. The selected (1,n) ladder is monotone for 29 rungs, so only the global orientation-blind proposal is refuted; OA-C1153's signed/saddle and trajectory-selection question remains open.
- **Kind/domain:** `comparison` / `dynamics`
- **Depends on:** [OA-C1153](#oa-c1153)
- **Leads to:** None.
- **Closure test:** Recompute the complete deduplicated closing census with one versioned Chern--Simons convention, require global monotonicity after volume ordering and demonstrate the detector with both a banked positive and a shuffled negative control.
- **Falsifier:** One certified pair with increasing volume and increasing |CS| refutes global monotone reparameterization; a nonvacuous exhaustive census can close the scoped negative.
- **Scope:** The mod-one absolute Chern--Simons convention on the full B289 Dehn-filling census. It does not choose a physical trajectory, orient time, test the alternate saddle clock or calibrate seconds.
- **Aliases:** `B1197 global branch`, `orientation-blind Vol-CS census`, `clock-coherence narrowed negative`
- **Sources:** [`../evidence/WAVE6_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE6_BRANCH_DELTA_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/31b4915657dae92a5cebda8cb15fcd1177854d97/frontier/B1197_clock_coherence/FINDINGS.md`](https://github.com/originaxiom/origin-axiom/blob/31b4915657dae92a5cebda8cb15fcd1177854d97/frontier/B1197_clock_coherence/FINDINGS.md)
- **Deepest artifacts:** [`../../../certificates/r023_b1197_clock_coherence.py`](../certificates/r023_b1197_clock_coherence.py), [`../../../outputs/r023_b1197_clock_coherence.txt`](../outputs/r023_b1197_clock_coherence.txt), [`https://github.com/originaxiom/origin-axiom/blob/31b4915657dae92a5cebda8cb15fcd1177854d97/frontier/B1197_clock_coherence/verification/b4_global.py`](https://github.com/originaxiom/origin-axiom/blob/31b4915657dae92a5cebda8cb15fcd1177854d97/frontier/B1197_clock_coherence/verification/b4_global.py)

## Domain: `flavor`

<a id="oa-c0015"></a>
### OA-C0015 — `EXTERNAL_BLOCKER`

- **Question:** Does the object compute nondegenerate fermion masses and realistic inter-family mixing?
- **Answer:** Not yet. The E6 cubic fixes support but not physical coefficients. The carrier tensor epsilon tensor C is an exact one-dimensional representation invariant, but no compactification/zero-mode intertwiner, Calabi-Yau trace or matter metric maps it to a physical Yukawa. On the conditional heterotic branch, R017 now versions the primary proof that the height-308 holomorphic up map is identically zero and remains zero throughout the same monad topology while exactly one audited H_u is retained. B1154 independently proves this cohomological emptiness is not the same arithmetic fact as period-value non-overlap. The down/lepton chain map, normalized metrics, thresholds and RG flow remain absent.
- **Kind/domain:** `computation` / `flavor`
- **Depends on:** [OA-C0008](#oa-c0008), [OA-C0014](#oa-c0014)
- **Leads to:** [OA-C0016](#oa-c0016), [OA-C1117](#oa-c1117)
- **Closure test:** Derived Yukawa matrices, phases, threshold corrections and RG flow reproducing masses and CKM/PMNS data.
- **Falsifier:** Only operator support, family-diagonal trace couplings, or arbitrary family tensors.
- **Scope:** All current cubic/field proposals and the conditional C12 heterotic visible-spectrum branch.
- **Aliases:** `flavor`, `Yukawa`, `CKM`, `PMNS`, `cubic field K`
- **Sources:** [`../../../memos/YUKAWA_CUP_PRODUCTS_308.md`](../memos/YUKAWA_CUP_PRODUCTS_308.md), [`../../../memos/YUKAWA_EXACT_SPECTRUM_NO_GO.md`](../memos/YUKAWA_EXACT_SPECTRUM_NO_GO.md), [`../../../memos/YUKAWA_PRIMARY_PROVENANCE.md`](../memos/YUKAWA_PRIMARY_PROVENANCE.md), [`../evidence/WAVE5_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE5_BRANCH_DELTA_AUDIT.md)
- **Deepest artifacts:** None registered.

<a id="oa-c1008"></a>
### OA-C1008 — `REFUTED`

- **Question:** Does the Hesse/equianharmonic period shortcut furnish an intrinsic BCDD H3 invariant and a normalized MSSM Yukawa or flavor prediction?
- **Answer:** No. The audited Hesse chain conflates the Schoen Z3xZ3 model with BCDD, does not construct a BCDD weight-three VHS map, and computes neither SU(5)-bundle cup products nor matter metrics; a Hesse connection coefficient is not a normalized MSSM Yukawa.
- **Kind/domain:** `repair` / `flavor`
- **Depends on:** [OA-C1001](#oa-c1001), [OA-C1006](#oa-c1006)
- **Leads to:** None.
- **Closure test:** Construct a marked polarized integral VHS correspondence into the BCDD threefold, identify bundle-valued cup products and metrics, and derive the normalized Yukawa without target-data fitting.
- **Falsifier:** The existing Hesse argument continues to target the Schoen model, has a weight/type mismatch, or supplies only a connection coefficient/operator support without the BCDD VHS and physical normalization.
- **Scope:** The claimed Hesse/equianharmonic shortcut to BCDD flavor, Yukawas, masses, or parameter-free predictions.
- **Aliases:** `Hesse period shortcut`, `q_geom Yukawa claim`, `wrong VHS bridge`
- **Sources:** `../tracks/HESSE_PERIOD_AUDIT.md`
- **Deepest artifacts:** None registered.

<a id="oa-c1020"></a>
### OA-C1020 — `REFUTED`

- **Question:** Do the certified C12 cohomology characters and SU(5) cubic force parameter-free three-family up/down/lepton Yukawa textures?
- **Answer:** No. The exact character certificate gives three family copies and one Higgs pair but leaves Sym^2(C^3), dimension 6, for up Yukawas and C^3 tensor C^3, dimension 9, for down/lepton Yukawas; no C12 texture zeros occur. SU(5) supplies only up symmetry and the holomorphic transpose relation Y_e=Y_d^T. OA-C1127 gives the distinct selected-E6 45-support table, not evaluated heterotic cup products. Cup-product coefficients, the Hd line in the fourfold chi0 space, matter metrics, canonical normalization, vacuum, thresholds and RG data remain unfixed.
- **Kind/domain:** `computation` / `flavor`
- **Depends on:** [OA-C1006](#oa-c1006), [OA-C1013](#oa-c1013)
- **Leads to:** [OA-C0015](#oa-c0015), [OA-C1054](#oa-c1054), [OA-C1055](#oa-c1055), [OA-C1127](#oa-c1127)
- **Closure test:** Compute the C12-invariant trilinear tensor spaces after the Wilson projection, then prove that every surviving coefficient and physical normalization is fixed by the same-source data.
- **Falsifier:** A complete character calculation showing a unique family tensor, or an exact cup-product/metric/vacuum derivation fixing all normalized entries.
- **Scope:** Pointwise certified (3,4) character data with Wilson k=4 or 8; counts are symmetry-allowed tensor dimensions, not a claim of nonzero cup-product rank or physical normalization.
- **Aliases:** `C12 Yukawa selection`, `flavor tensor gate`, `(3,4), k=4/8`
- **Sources:** `../tracks/YUKAWA_SELECTION_RULES.md`, `../tracks/MARKED_PSEUDOINVERSE_PHI_POINTWISE_AUDIT.md`, `../sources/1112.1097/Three_gen_models.tex`
- **Deepest artifacts:** `../experiments/verify_yukawa_selection_rules.py`

<a id="oa-c1034"></a>
### OA-C1034 — `CONDITIONAL`

- **Question:** Do the exact norm-308 monad and selected C12/Wilson sectors yield evaluated holomorphic up and down/lepton Yukawa cup-product maps with determined ranks and Higgs line?
- **Answer:** Conditionally. At the exact height-308 stable bundle candidate, character arithmetic allows Sym2(C3) of dimension 6 and C3 tensor C3 of dimension 9, with no C12 texture zeros. R017 makes the primary up-type proof branch-local: H1(G_Y)=0 kills both matter images and H1(K1)=H2(K1)=0 lifts the Higgs input, so cup-product naturality forces the full 1x1806 map and the Wilson 1x6 slice to rank zero. Hu=C0 is one-dimensional, while B0 is a four-dimensional trivial module leaving an unselected P3 of Hd lines. The precursor campaign records exact 33-plus-5 down-sector presentation progress and a finite-field connecting-sector reduction to one missing 1x18 determinant/residue trace row, but that Sage chain stack is not branch-local. B1167 pays the up-type provenance debt but does not select the branch or Hd line. No completed Q(zeta12) down/lepton evaluator or P3 matrix pencil is versioned here.
- **Kind/domain:** `computation` / `flavor`
- **Depends on:** [OA-C1013](#oa-c1013), [OA-C1020](#oa-c1020)
- **Leads to:** [OA-C0015](#oa-c0015), [OA-C1054](#oa-c1054), [OA-C1055](#oa-c1055), [OA-C1148](#oa-c1148)
- **Closure test:** Construct a common exact multigraded toric Cech or hypercohomology model for A=H1(V), B=H1(Lambda2 V), C=H1(Lambda2 V*) and its multiplicative contraction maps to H3(O); restrict the evaluated tensors to k=4/8 Wilson sectors and either derive an Hd line or report the full P3 matrix pencil.
- **Falsifier:** A chain-level calculation proving a claimed rank/texture false, or an argument based only on characters, an index, a vanishing gate, or an unselected Hd line while asserting a concrete Yukawa matrix.
- **Scope:** The fixed norm hypersurface and exact height-308 (3,4) monad, descended with Wilson k=4 or k=8. This item concerns holomorphic cup products only; canonical matter metrics, moduli/vacuum selection, thresholds and RG evolution remain separate physical gates.
- **Aliases:** `norm-308 Yukawa cup products`, `holomorphic 10-10-5H map`, `Hd-line gate`
- **Sources:** [`../../../memos/YUKAWA_CUP_PRODUCTS_308.md`](../memos/YUKAWA_CUP_PRODUCTS_308.md), [`../../../memos/YUKAWA_EXACT_SPECTRUM_NO_GO.md`](../memos/YUKAWA_EXACT_SPECTRUM_NO_GO.md), [`../../../memos/YUKAWA_PRIMARY_PROVENANCE.md`](../memos/YUKAWA_PRIMARY_PROVENANCE.md), [`../evidence/WAVE5_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE5_BRANCH_DELTA_AUDIT.md)
- **Deepest artifacts:** [`../../../certificates/r017_yukawa_primary/verify_yukawa_cup_product_308_scope.py`](../certificates/r017_yukawa_primary/verify_yukawa_cup_product_308_scope.py), [`../../../certificates/r017_yukawa_primary/verify_yukawa_exact_spectrum_no_go.py`](../certificates/r017_yukawa_primary/verify_yukawa_exact_spectrum_no_go.py)

<a id="oa-c1054"></a>
### OA-C1054 — `PROVED`

- **Question:** Does the exact height-308 up-type cup-product zero persist on the same-X, fixed-holomorphic-V large-radius Strominger branch?
- **Answer:** Yes. OA-C1034 proves that the entire height-308 holomorphic up map vanishes, not merely selected character components. The AGF existence curve keeps X and the holomorphic structure of V308 fixed and changes Hermitian/HYM/tangent-connection data. Dolbeault cohomology and its wedge/contraction maps are therefore transported isomorphically, so the full and Wilson-projected up tensor remain rank zero. Invertible matter-metric normalization cannot turn zero into nonzero. Thus all three up-type quarks receive no mass from this renormalizable operator along the proved branch; a different holomorphic bundle/complex structure, heavy-field mixing, torsional worldsheet effect, spacetime nonperturbative term or SUSY-breaking operator would be new data and must be computed separately.
- **Kind/domain:** `theorem` / `flavor`
- **Depends on:** [OA-C1034](#oa-c1034), [OA-C1051](#oa-c1051)
- **Leads to:** [OA-C0015](#oa-c0015), [OA-C1007](#oa-c1007)
- **Closure test:** Type-check which holomorphic data the Andreas--Garcia-Fernandez deformation fixes, transport the charged Dolbeault cup/contraction map, and distinguish holomorphic vanishing from metric normalization and genuinely new nonperturbative operators.
- **Falsifier:** A change of the holomorphic bundle or complex structure within the claimed AGF curve, a failure of naturality for the certified cup-product factorization, or an explicit nonzero renormalizable up tensor generated while the same light cohomology classes and fixed holomorphic data are retained.
- **Scope:** The exact height-308 bundle, fixed complex quotient X, k=4 or k=8 Wilson projection, and the same-holomorphic-data large-radius AGF curve. It does not exclude a different holomorphic branch or independently derived nonrenormalizable/nonperturbative effective operators.
- **Aliases:** `Strominger Yukawa persistence`, `AGF up-Yukawa zero`, `fixed-holomorphic-data flavor no-go`
- **Sources:** `../tracks/YUKAWA_STROMINGER_PERSISTENCE_AUDIT.md`, `../tracks/YUKAWA_CUP_PRODUCTS_308.md`, `../tracks/STROMINGER_ORDER3_EXISTENCE_AUDIT.md`
- **Deepest artifacts:** `../experiments/verify_yukawa_cup_product_308_scope.py`, `../experiments/verify_yukawa_selection_rules.py`

<a id="oa-c1055"></a>
### OA-C1055 — `PROVED`

- **Question:** Does retaining exactly one massless up-type Higgs inside the same BCDD monad topology force that Higgs into the ambient image and its renormalizable up Yukawa to remain zero under coefficient variation?
- **Answer:** Yes. For every locally-free map in the same monad topology, H1(G_X)=0 and Serre duality from H2(K1*)=0 gives H1(K1)=0. Hence H1(Lambda2 G_X*) injects equivariantly into H1(Lambda2 V*) and, after the determinant twist, contains chi0+chi1. Wilson k=4 or8 selects the unique audited H_u from the injected chi0. Naturality sends both matter inputs to zero in H1(G_X), so every coupling to that Higgs vanishes. A rank jump can help only by adding a nonambient chi0, which gives at least a second massless H_u before a separately derived mass/mixing mechanism. Therefore coefficient variation alone cannot repair Y_u while preserving the exact cohomological MSSM spectrum.
- **Kind/domain:** `theorem` / `flavor`
- **Depends on:** [OA-C1006](#oa-c1006), [OA-C1034](#oa-c1034)
- **Leads to:** [OA-C0015](#oa-c0015), [OA-C1007](#oa-c1007)
- **Closure test:** Use the monad and exterior exact sequences to identify the unconditional ambient Higgs injection, prove naturality of the trilinear on that image, and type every rank-jump alternative against the exact one-Higgs massless spectrum.
- **Falsifier:** A locally-free map with exactly one Wilson-surviving H_u outside the ambient image, a nonzero cup product with the injected ambient H_u, or a failure of the map-independent H1(G_X)=H1(K1)=0 vanishings.
- **Scope:** The BCDD monad topology, (3,4) equivariant branch, k=4 or k=8 Wilson projection, and cohomological massless-spectrum counting. Different bundle topology, extra Higgs/vectorlike states with derived mixing, or new nonperturbative operators are outside this no-go.
- **Aliases:** `exact-spectrum up-Yukawa no-go`, `ambient Higgs naturality theorem`, `same-monad flavor repair no-go`
- **Sources:** [`../../../memos/YUKAWA_EXACT_SPECTRUM_NO_GO.md`](../memos/YUKAWA_EXACT_SPECTRUM_NO_GO.md), [`../../../memos/YUKAWA_CUP_PRODUCTS_308.md`](../memos/YUKAWA_CUP_PRODUCTS_308.md), [`../../../memos/YUKAWA_PRIMARY_PROVENANCE.md`](../memos/YUKAWA_PRIMARY_PROVENANCE.md), [`../evidence/WAVE5_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE5_BRANCH_DELTA_AUDIT.md)
- **Deepest artifacts:** [`../../../certificates/r017_yukawa_primary/verify_yukawa_exact_spectrum_no_go.py`](../certificates/r017_yukawa_primary/verify_yukawa_exact_spectrum_no_go.py), [`../../../certificates/r017_yukawa_primary/verify_yukawa_cup_product_308_scope.py`](../certificates/r017_yukawa_primary/verify_yukawa_cup_product_308_scope.py)

<a id="oa-c1127"></a>
### OA-C1127 — `PROVED`

- **Question:** Does the complete E6 cubic on the selected measured-hypercharge 27 roster have exactly the declared 45-support hypergraph?
- **Answer:** Yes. The independently rerun exact certificate finds 45 supports, including six q-u^c-Hu, six q-d^c-Hd, two l-e^c-Hd and two S-Hu-Hd supports, together with exotic-mass and proton-decay-shaped supports. B1171 independently reruns the source certificate and stresses the discriminating fact: the object-level E6 tensor permits the six up-type supports while the conditional heterotic bundle cup product in OA-C1054 vanishes. These are different mechanisms, not one established value wall.
- **Kind/domain:** `computation` / `flavor`
- **Depends on:** [OA-C1020](#oa-c1020), [OA-C1100](#oa-c1100), [OA-C1121](#oa-c1121)
- **Leads to:** [OA-C1144](#oa-c1144)
- **Closure test:** Reconstruct the normalized E6 cubic, label every selected 27 state by the measured hypercharge roster, and classify all support triples exactly.
- **Falsifier:** A missing or extra support, an inconsistent charge sum, or a different complete support count refutes the table.
- **Scope:** The selected observer-paid E6 frame and measured-Y roster. Nonzero algebraic support is not a nonzero normalized physical Yukawa, a vacuum prediction, a hierarchy or a proton-decay rate.
- **Aliases:** `outside Yukawa texture`, `45-support measured-Y table`, `selected E6 cubic roster`
- **Sources:** [`../evidence/WAVE5_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE5_BRANCH_DELTA_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/60bcf01db966ae0b13f18c73c24845040b59fd98/outside_bench/memos/THE_TEXTURE.md`](https://github.com/originaxiom/origin-axiom/blob/60bcf01db966ae0b13f18c73c24845040b59fd98/outside_bench/memos/THE_TEXTURE.md)
- **Deepest artifacts:** [`https://github.com/originaxiom/origin-axiom/blob/60bcf01db966ae0b13f18c73c24845040b59fd98/outside_bench/certificates/yukawa_texture.py`](https://github.com/originaxiom/origin-axiom/blob/60bcf01db966ae0b13f18c73c24845040b59fd98/outside_bench/certificates/yukawa_texture.py)

<a id="oa-c1128"></a>
### OA-C1128 — `PROVED`

- **Question:** In the selected E8 family-channel possibility space, do all complete three-by-three family matrices induced by the cubic have rank two with kernel equal to the Higgs-family direction?
- **Answer:** Yes. The independently rerun certificate checks all 810 full-tensor family matrices. Every matrix has rank exactly two and kernel equal to the declared Higgs family, as expected from the epsilon-family factor. B1171 reproduces the result and registers the open comparison with the heterotic cup-product zero and the live E6 up-support. The result remains a structural identity in an observer-paid E8 possibility-space embedding, not a physical fermion mass matrix.
- **Kind/domain:** `computation` / `flavor`
- **Depends on:** [OA-C1089](#oa-c1089)
- **Leads to:** [OA-C1144](#oa-c1144)
- **Closure test:** Enumerate every nonzero full-tensor family channel, construct the induced three-by-three matrices and certify their ranks and kernels exactly.
- **Falsifier:** One declared channel of rank other than two or with a kernel not equal to the Higgs-family vector refutes the finite theorem.
- **Scope:** The observer-paid A2^4-in-E8 possibility-space embedding and selected cubic channel. No three chiral zero modes, Higgs identification, physical mass, mixing angle or scale follows.
- **Aliases:** `outside family rank`, `E8 family-matrix kernel`, `rank-two epsilon channel`
- **Sources:** [`../evidence/WAVE5_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE5_BRANCH_DELTA_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/60bcf01db966ae0b13f18c73c24845040b59fd98/outside_bench/memos/FAMILY_RANK.md`](https://github.com/originaxiom/origin-axiom/blob/60bcf01db966ae0b13f18c73c24845040b59fd98/outside_bench/memos/FAMILY_RANK.md)
- **Deepest artifacts:** [`https://github.com/originaxiom/origin-axiom/blob/60bcf01db966ae0b13f18c73c24845040b59fd98/outside_bench/certificates/family_rank.py`](https://github.com/originaxiom/origin-axiom/blob/60bcf01db966ae0b13f18c73c24845040b59fd98/outside_bench/certificates/family_rank.py)

<a id="oa-c1144"></a>
### OA-C1144 — `PROVED`

- **Question:** What exact typed maps, if any, relate the heterotic up-cup-product zero, the nonzero E6 up-type support and the rank-two E8 family-channel kernel?
- **Answer:** Yes. B1185 proves the three mechanisms pairwise distinct by exact invariants: the heterotic up map has rank zero while the object E6 tensor has six nonzero supports; the first zero is selective whereas the E8 family kernel is universal rank two in all 810 channels; and the E8 family index has no object-level counterpart. There is no literal one-wall identification. OA-C1148 keeps the unevaluated heterotic down tail separate.
- **Kind/domain:** `comparison` / `flavor`
- **Depends on:** [OA-C1054](#oa-c1054), [OA-C1127](#oa-c1127), [OA-C1128](#oa-c1128)
- **Leads to:** None.
- **Closure test:** Type each of the three maps and prove literal identity or pairwise independence using discriminating invariants; a broader common factorization must be posed separately.
- **Falsifier:** The already observed nonzero E6 support versus zero heterotic cup map refutes literal identity of those two; a common mechanism requires a nontrivial typed factorization explaining that difference and the E8 kernel.
- **Scope:** Pairwise independence of three algebraic mechanisms in their stated conditional frames. No mass value, hierarchy, family identification, broader universal factorization or physical Yukawa matrix is asserted.
- **Aliases:** `B1171 L186`, `three Yukawa suppressions`, `support-zero-rank comparison`
- **Sources:** [`../evidence/WAVE6_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE6_BRANCH_DELTA_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/6bae72f460b539b40851fb8fb5cc3588f84faca8/frontier/B1185_yukawa_three_mechanisms/FINDINGS.md`](https://github.com/originaxiom/origin-axiom/blob/6bae72f460b539b40851fb8fb5cc3588f84faca8/frontier/B1185_yukawa_three_mechanisms/FINDINGS.md)
- **Deepest artifacts:** None registered.

<a id="oa-c1148"></a>
### OA-C1148 — `OPEN`

- **Question:** Can the normalized cyclic or Serre quasi-isomorphism over Q(zeta_12) be constructed exactly and used to evaluate the norm-308 down-type and lepton Yukawa cup products?
- **Answer:** Open. B1185 closes only the pairwise distinction among the three suppression mechanisms. Its down-tail handoff names a characteristic-zero comparison T but the required certify_yukawa_down_tail_cech_308.sage load target is absent from the shared record. The outside one-27 calculation exactly finds one SU(2)-epsilon lambda invariant and one SU(3)-delta exotic invariant, and its finite H_d menu makes the down and lepton determinant cuts coincide only at that coefficient-shape level. B1208 leaves a generation-level three-outcome fork: the cuts may coincide, become independent, or the lepton operator may be absent. R024 correctly finds coarse physical character zero for e^c and l/H_d on both retained Wilson branches, while R025 corrects its tail interpretation and proves only the physical one-dimensional pure-tail square zero. R026 then constructs the exact ordered Q(zeta_12) Euler frame, determinant comparison det(G)->L, equivariant phase and sparse local connecting formula; its exact frame minor is -72*zeta_12^2. R027 constructs the exact canonical-weight Cech generator and cyclic dual trace for dP6 and a signed 384-simplex product trace on the actual 36-chart cover of Z=dP6 x dP6, normalized to one on the marked H4(K_Z) generator. R028 pins the exact C12 chart action, all 36 common Laurent frames and the 18-positive/18-negative local orientation census; it proves raw chart monomial = q_(D,sigma)*t^u for every relevant lattice monomial and exposes the prior unordered representative and tautological commutativity checks. The generalized SU(3) ambient-type theorem does not force this mixed SU(5) product to vanish. The ambient top trace and frame transport are therefore explicit, but the Q(zeta_12) Phi/Bezout payload, characteristic-zero refinement collapse and hypersurface connecting representative delta(ctilde)/f are still required for every connecting entry; the chain-level Serre map is additionally required for tail or mixed entries. No tensor rank or B1208 fork outcome follows yet.
- **Kind/domain:** `computation` / `flavor`
- **Depends on:** [OA-C1034](#oa-c1034), [OA-C1144](#oa-c1144)
- **Leads to:** [OA-C0015](#oa-c0015)
- **Closure test:** Ship the missing file-relative load target, construct the normalized comparison map without preloaded ranks, evaluate every declared down/lepton product and certify its rank and normalization with exact controls.
- **Falsifier:** A type obstruction, noncanonical normalization, zero or rank different from the preregistered result refutes that proposed evaluator; a missing single-homed artifact withholds closure.
- **Scope:** The conditional norm-308 heterotic witness and its holomorphic cup products. Even closure would not normalize physical masses, select a vacuum or supply RG evolution.
- **Aliases:** `B1185 down evaluator`, `T-cal cyclic-Serre comparison`, `Yukawa down tail`
- **Sources:** [`../evidence/WAVE6_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE6_BRANCH_DELTA_AUDIT.md), [`../../../memos/LEPTON_CHARACTER_DATUM.md`](../memos/LEPTON_CHARACTER_DATUM.md), [`../../../memos/LEPTON_TAIL_SELECTION_CORRECTION.md`](../memos/LEPTON_TAIL_SELECTION_CORRECTION.md), [`../../../memos/YUKAWA_DETERMINANT_FRAME_308.md`](../memos/YUKAWA_DETERMINANT_FRAME_308.md), [`../../../memos/YUKAWA_TORIC_TOP_TRACE_308.md`](../memos/YUKAWA_TORIC_TOP_TRACE_308.md), [`../../../memos/YUKAWA_TORIC_CHART_FRAMES_308.md`](../memos/YUKAWA_TORIC_CHART_FRAMES_308.md), [`https://arxiv.org/abs/2103.10454`](https://arxiv.org/abs/2103.10454), [`https://github.com/originaxiom/origin-axiom/blob/6bae72f460b539b40851fb8fb5cc3588f84faca8/frontier/B1185_yukawa_three_mechanisms/FINDINGS.md`](https://github.com/originaxiom/origin-axiom/blob/6bae72f460b539b40851fb8fb5cc3588f84faca8/frontier/B1185_yukawa_three_mechanisms/FINDINGS.md), [`https://github.com/originaxiom/origin-axiom/blob/582c08d2c14017999fb55df2c2ca72fac0389cf5/outside_bench/memos/HD_EXHAUSTION.md`](https://github.com/originaxiom/origin-axiom/blob/582c08d2c14017999fb55df2c2ca72fac0389cf5/outside_bench/memos/HD_EXHAUSTION.md), [`https://github.com/originaxiom/origin-axiom/blob/b0d8f37c7205cf43520a0710f6b7c7c66634a0dc/frontier/B1208_cross_seat_harvest/FINDINGS.md`](https://github.com/originaxiom/origin-axiom/blob/b0d8f37c7205cf43520a0710f6b7c7c66634a0dc/frontier/B1208_cross_seat_harvest/FINDINGS.md)
- **Deepest artifacts:** [`../../../certificates/r025_lepton_tail_selection/lepton_tail_selection.py`](../certificates/r025_lepton_tail_selection/lepton_tail_selection.py), [`../../../outputs/r025_lepton_tail_selection.txt`](../outputs/r025_lepton_tail_selection.txt), [`../../../certificates/r026_yukawa_determinant_frame/determinant_frame.py`](../certificates/r026_yukawa_determinant_frame/determinant_frame.py), [`../../../outputs/r026_yukawa_determinant_frame.txt`](../outputs/r026_yukawa_determinant_frame.txt), [`../../../certificates/r027_toric_top_trace/toric_top_trace.py`](../certificates/r027_toric_top_trace/toric_top_trace.py), [`../../../outputs/r027_toric_top_trace.txt`](../outputs/r027_toric_top_trace.txt), [`../../../certificates/r028_toric_chart_frames/toric_chart_frames.py`](../certificates/r028_toric_chart_frames/toric_chart_frames.py), [`../../../outputs/r028_toric_chart_frames.txt`](../outputs/r028_toric_chart_frames.txt)

## Domain: `framework`

<a id="oa-c1048"></a>
### OA-C1048 — `REFUTED`

- **Question:** Can the nonzero combined class-field secondary character coexist with the strict zero-H BCDD Calabi--Yau `(0,2)` GLSM without an additional Green--Schwarz differential trivialization?
- **Answer:** No. The conditional visible and selected hidden coefficients add to 4 mod 12, exact order three. H4(X,Z)=Z is torsion-free, so a Green--Schwarz/Wess--Zumino differential compensator can cancel the global determinant phase, but it introduces torsionful H and exits the certified strict-CY `(0,2)` GLSM. Ordinary cyclic discrete torsion cannot repair this because H2(C12,U(1))=0. Thus the smooth flat bundle is allowed, while the simultaneous no-B strict branch is not.
- **Kind/domain:** `theorem` / `framework`
- **Depends on:** [OA-C1026](#oa-c1026), [OA-C1044](#oa-c1044)
- **Leads to:** [OA-C1007](#oa-c1007), [OA-C1051](#oa-c1051), [OA-C1053](#oa-c1053)
- **Closure test:** Compute the equivariant degree-four anomaly, its pullback as a flat differential character, and the available B/Wess--Zumino or discrete-torsion trivializations while preserving the claimed worldsheet supersymmetry.
- **Falsifier:** Cancellation of the combined class, a nontrivial ordinary C12 discrete-torsion class cancelling it, or a strict H=0 `(0,2)` construction carrying the same nonzero differential character.
- **Scope:** The simultaneous strict BCDD zero-H `(0,2)` presentation with the retained nonzero class. Torsional Strominger and other differential-trivialization branches are separate.
- **Aliases:** `class-field level matching`, `Green--Schwarz differential compensator`, `strict (0,2) incompatibility`
- **Sources:** `../tracks/CLASSFIELD_HETEROTIC_LEVEL_MATCHING.md`, `../tracks/RELATIVE_SECONDARY_CS_AUDIT.md`, `../tracks/HETEROTIC_INSTANTON_GATE.md`
- **Deepest artifacts:** `../experiments/verify_relative_secondary_cs.py`

<a id="oa-c1051"></a>
### OA-C1051 — `PROVED`

- **Question:** Does the selected quotient and certified stable V308 admit a compact same-topology non-Kähler Strominger-system solution that preserves the visible charged spectrum?
- **Answer:** Yes. The Andreas--Garcia-Fernandez implicit-function theorem applies to the compact Calabi--Yau X and degree-zero stable V308 with c1=0 and c2(V)=c2(TX). For sufficiently large radius it gives a curve of conformally balanced Strominger solutions while leaving the holomorphic structure of V fixed and the tangent holomorphic structure isomorphic to the original. Hence pi1, index, bundle cohomology, Wilson projection and the audited visible charged MSSM spectrum persist. The theorem does not prescribe the order-three Cheeger--Simons class, select the radius/moduli, or provide an all-orders string vacuum.
- **Kind/domain:** `theorem` / `framework`
- **Depends on:** [OA-C1001](#oa-c1001), [OA-C1027](#oa-c1027), [OA-C1048](#oa-c1048)
- **Leads to:** [OA-C1007](#oa-c1007), [OA-C1053](#oa-c1053), [OA-C1054](#oa-c1054)
- **Closure test:** Verify the hypotheses of a published Strominger-system existence theorem on the exact X and V308, distinguish local curvature/Bianchi existence from a prescribed differential character, and check which topological and cohomological spectrum data are preserved.
- **Falsifier:** Failure of stability, c1=0, c2(V)=c2(TX), strict SU3 holonomy, or a theorem conclusion that changes the holomorphic bundle/cohomology used for the visible spectrum.
- **Scope:** Published large-radius local-existence theorem applied to the fixed topology and holomorphic bundle. Realization of the selected global order-three differential cocycle, normalized periods, moduli stabilization and all-orders worldsheet consistency remain separate.
- **Aliases:** `large-radius Strominger completion`, `Andreas--Garcia-Fernandez branch`, `spectrum-preserving torsional deformation`
- **Sources:** `../tracks/STROMINGER_ORDER3_EXISTENCE_AUDIT.md`, `../tracks/HOPPE_LAMBDA3_GATE.md`, `../tracks/CLASSFIELD_HETEROTIC_LEVEL_MATCHING.md`
- **Deepest artifacts:** `../experiments/verify_hoppe_wedge.sage`, `../experiments/verify_hoppe_lambda3.sage`

<a id="oa-c1053"></a>
### OA-C1053 — `EXTERNAL_BLOCKER`

- **Question:** Is the selected order-three differential Chern--Simons component explicitly realized and transported on the large-radius Strominger family?
- **Answer:** Not yet. The order-three anomaly is a flat degree-four differential character in H3(X,R/Z), whereas a closed ordinary B-gerbe class is degree three with flat subgroup H2(X,R/Z); adding such a flat class does not alter the degree-four anomaly. Because the integral characteristic difference vanishes, abstract geometric trivializations exist and form an Hhat3(X)-torsor. Once a marked endpoint trivialization and connection path are supplied, transgression can continue it along the contractible family. What remains absent is the actual visible/tangent refinement, connection representatives, selected torsor member, marked H3 basis and period normalization. Seam A is therefore an operational wall for physics: OA-C1109 retains a narrowly specified arithmetic comparison problem, but even its positive solution would not select this heterotic realization or its missing geometric data.
- **Kind/domain:** `construction` / `framework`
- **Depends on:** [OA-C1044](#oa-c1044), [OA-C1048](#oa-c1048), [OA-C1051](#oa-c1051)
- **Leads to:** [OA-C1007](#oa-c1007), [OA-C1109](#oa-c1109), [OA-C1136](#oa-c1136)
- **Closure test:** Construct an endpoint visible/tangent differential refinement and twisted Green--Schwarz/String cocycle with the prescribed order-three component, then evaluate the actual connection transgression and marked normalized H3 periods along the Strominger family.
- **Falsifier:** An explicit chain-level construction for the actual AGF connections would close the item; a proof that the conditional universal order-three character cannot be realized by those connection refinements would refute this route.
- **Scope:** The explicit global differential refinement, selected geometric trivialization and marked periods on the actual large-radius branch. Abstract existence follows from vanishing integral characteristic class; local Strominger existence and spectrum retention are OA-C1051, while a normalized four-dimensional vacuum remains further downstream.
- **Aliases:** `order-three differential Strominger lift`, `twisted Green--Schwarz completion`, `AGF secondary-character transport`
- **Sources:** `../tracks/ORDER3_DIFFERENTIAL_STROMINGER_CLOSURE.md`, `../tracks/STROMINGER_ORDER3_EXISTENCE_AUDIT.md`, `../tracks/CLASSFIELD_HETEROTIC_LEVEL_MATCHING.md`
- **Deepest artifacts:** `../experiments/verify_order3_differential_strominger.py`, `../experiments/verify_relative_secondary_cs.py`

<a id="oa-c1131"></a>
### OA-C1131 — `PROVED`

- **Question:** Is the programme's time-arrow datum already encoded by the oriented punctured-torus bundle and monodromy, or is it an independent observer-supplied discrete datum?
- **Answer:** Yes. B1182 proves the unique frozen C4-prime isomorphism (c,r,theta)->(k11,k7,k5). The programme's algebraic arrow is reversal r, hence the finite-place mod-four form-class leg k7, and is distinct from the archimedean orientation leg c. The object types the torsor leg; selecting a label on it remains observer-side.
- **Kind/domain:** `uniqueness` / `framework`
- **Depends on:** [OA-C0003](#oa-c0003), [OA-C1124](#oa-c1124)
- **Leads to:** [OA-C1165](#oa-c1165)
- **Closure test:** Define the time-arrow object and equivalence relation, construct its map to or from bundle orientation/monodromy and prove equivalence or independence without importing thermodynamic data.
- **Falsifier:** An exact equivalence proves absorption; two models with the same oriented bundle data and opposite declared time arrows prove independence.
- **Scope:** The programme's finite algebraic frame-reversal arrow only. This proves no thermodynamic, causal or cosmological arrow and supplies no entropy-producing dynamics.
- **Aliases:** `B1164 time-arrow residue`, `observer-price time bit`, `bundle-orientation comparison`
- **Sources:** [`../evidence/WAVE6_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE6_BRANCH_DELTA_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/63a832252b3be5cd72820a7bfafab67ad4c7d998/frontier/B1182_c4prime_resolved/arc_verdict.json`](https://github.com/originaxiom/origin-axiom/blob/63a832252b3be5cd72820a7bfafab67ad4c7d998/frontier/B1182_c4prime_resolved/arc_verdict.json)
- **Deepest artifacts:** None registered.

<a id="oa-c1133"></a>
### OA-C1133 — `REFUTED`

- **Question:** Are the branch-selection, being-by-hearing and measurement V4 torsors equivariantly isomorphic with their three named actions and intended labels?
- **Answer:** No. R022 proves abstract regular-action equivalence and the sqrt(3)-versus-sqrt(5) field-label separator. In B1175 the charter author freezes named-action preservation as the intended category and adjudicates the original three-way claim false: branch selection and being-by-hearing are nonisomorphic. The productive rescope drops being-by-hearing; B1182 then proves the surviving branch-to-measurement C4-prime pair uniquely, recorded separately as OA-C1147.
- **Kind/domain:** `theorem` / `framework`
- **Depends on:** [OA-C1004](#oa-c1004), [OA-C1123](#oa-c1123)
- **Leads to:** [OA-C1138](#oa-c1138), [OA-C1139](#oa-c1139), [OA-C1147](#oa-c1147)
- **Closure test:** Write the three exact V4 actions on named sets, state the admissible label-preserving equivalences and construct an equivariant isomorphism or a complete invariant separating them.
- **Falsifier:** An explicit equivariant named-action isomorphism closes equivalence; a proved invariant such as incompatible fixed-point or character data refutes it.
- **Scope:** The three explicitly named finite V4 actions. Abstract unlabelled torsor isomorphism is automatic and is weaker than the programme's claimed identification.
- **Aliases:** `B1166 C4 torsor comparison`, `three V4 torsors`, `named-action equivalence`
- **Sources:** [`../../../memos/V4_NAMED_ACTION_AUDIT.md`](../memos/V4_NAMED_ACTION_AUDIT.md), [`../evidence/WAVE6_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE6_BRANCH_DELTA_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/ee38a87f48f40fa32e356f28d1eb4ea460d4de2f/frontier/B1175_charter_close_harvest/FINDINGS.md`](https://github.com/originaxiom/origin-axiom/blob/ee38a87f48f40fa32e356f28d1eb4ea460d4de2f/frontier/B1175_charter_close_harvest/FINDINGS.md)
- **Deepest artifacts:** [`../../../certificates/r022_v4_torsors/v4_named_action_audit.py`](../certificates/r022_v4_torsors/v4_named_action_audit.py), [`../../../outputs/r022_v4_torsors.txt`](../outputs/r022_v4_torsors.txt)

<a id="oa-c1135"></a>
### OA-C1135 — `CONDITIONAL`

- **Question:** Under the declared unoriented scale-free archimedean object, is every object-canonical datum exactly mirror-even and dimensionless?
- **Answer:** Conditionally. B1168's examples establish useful necessary filters: an automorphism-odd sign cannot be canonical on an unoriented object, and an absolute dimensionful value cannot be extracted from scale-free data. B1169 restates awareness=mirror-even and choice=mirror-odd as a firewalled reading and explicitly asks for the missing completeness/map theorem; it supplies no such map. The converse, exhaustion of datum classes and analytic-torsion parity remain unsettled. Globally the observer ledger is adelic because the VEV choice is finite-place rather than archimedean.
- **Kind/domain:** `classification` / `framework`
- **Depends on:** [OA-C0017](#oa-c0017), [OA-C1124](#oa-c1124)
- **Leads to:** [OA-C1141](#oa-c1141), [OA-C1146](#oa-c1146), [OA-C1152](#oa-c1152)
- **Closure test:** Define the complete class of admissible archimedean data, prove both necessity and sufficiency of mirror-evenness and dimensionlessness, and settle analytic-torsion parity under fixed normalization.
- **Falsifier:** One canonical mirror-odd datum or canonical dimensionful datum of the same unoriented scale-free object refutes necessity; one mirror-even dimensionless datum lacking canonical definition refutes sufficiency.
- **Scope:** Archimedean geometric data of the declared unoriented scale-free object only. This is a conditional classifier proposal, not a semantic completeness theorem or a statement about finite-place observer choices.
- **Aliases:** `B1168 C5 classifier`, `archimedean parity-by-dimension law`, `mirror-even dimensionless test`
- **Sources:** [`../evidence/WAVE6_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE6_BRANCH_DELTA_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/759f889c4f80c54ea09afc854f18b049a7b12b13/frontier/B1169_qualia_parity_synthesis/FINDINGS.md`](https://github.com/originaxiom/origin-axiom/blob/759f889c4f80c54ea09afc854f18b049a7b12b13/frontier/B1169_qualia_parity_synthesis/FINDINGS.md)
- **Deepest artifacts:** None registered.

<a id="oa-c1138"></a>
### OA-C1138 — `PROVED`

- **Question:** After erasing programme labels and allowing an automorphism of V4, are any two free transitive four-point V4 actions equivariantly isomorphic?
- **Answer:** Yes. R022 enumerates the regular action: the identity has cycle type 1^4, each nonidentity element has 2^2 and no fixed point, and the permutation character decomposes as 1+chi_1+chi_2+chi_12. Choosing a basepoint identifies every such torsor with V4 acting on itself by translation.
- **Kind/domain:** `theorem` / `framework`
- **Depends on:** [OA-C1133](#oa-c1133)
- **Leads to:** None.
- **Closure test:** Construct a basepoint-and-group-isomorphism equivariant bijection and verify the regular cycle and character tables exactly.
- **Falsifier:** Two free transitive four-point actions with inequivalent stabilizers, permutation characters or translation tables refute the abstract theorem.
- **Scope:** Unlabelled regular finite actions only. It forgets field, Dynkin, carrier and semantic annotations and therefore does not close OA-C1133.
- **Aliases:** `R022 abstract V4 theorem`, `regular four-point torsor equivalence`
- **Sources:** [`../../../memos/V4_NAMED_ACTION_AUDIT.md`](../memos/V4_NAMED_ACTION_AUDIT.md), [`../evidence/WAVE6_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE6_BRANCH_DELTA_AUDIT.md)
- **Deepest artifacts:** [`../../../certificates/r022_v4_torsors/v4_named_action_audit.py`](../certificates/r022_v4_torsors/v4_named_action_audit.py)

<a id="oa-c1139"></a>
### OA-C1139 — `PROVED`

- **Question:** If admissible maps must preserve the displayed quadratic-field and subfield annotations, are the branch-selection and being-by-hearing V4 presentations nonisomorphic?
- **Answer:** Yes. R022 computes discriminants 144 and 225 from the three quadratic subfields. Q(zeta_12) ramifies only at {2,3}, while the being-by-hearing compositum includes Q(sqrt(5)) and ramifies at {3,5}; hence no field-annotation-preserving identification exists. B1175 authoritatively freezes field/named-label preservation as the intended category, discharging the former conditional antecedent.
- **Kind/domain:** `implication` / `framework`
- **Depends on:** [OA-C1133](#oa-c1133), [OA-C1138](#oa-c1138)
- **Leads to:** None.
- **Closure test:** Declare field/subfield preservation as part of the morphism category and prove a complete invariant separates the two annotated actions.
- **Falsifier:** A field-annotation-preserving equivariant bijection, or rejection of field annotations from the intended morphism category, defeats the conditional conclusion.
- **Scope:** The programme's now-frozen field-annotated named-action category. Abstract unlabelled regular V4 torsors remain isomorphic.
- **Aliases:** `R022 field-labelled separator`, `sqrt3 versus sqrt5 V4 fence`
- **Sources:** [`../../../memos/V4_NAMED_ACTION_AUDIT.md`](../memos/V4_NAMED_ACTION_AUDIT.md), [`../evidence/WAVE6_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE6_BRANCH_DELTA_AUDIT.md)
- **Deepest artifacts:** [`../../../certificates/r022_v4_torsors/v4_named_action_audit.py`](../certificates/r022_v4_torsors/v4_named_action_audit.py)

<a id="oa-c1141"></a>
### OA-C1141 — `PROVED`

- **Question:** Are the QP-4 self-closure obstruction, the mirror-odd orientation class and the E6 real-form fork bit images of one explicitly constructed Z2 class?
- **Answer:** Yes. B1183 constructs a c-equivariant isomorphism between the QP-4 chord-sign torsor and the orientation torsor. Together with B1174's mirror=chirality=Gal(c) identification and the banked E6 real-form typing, the named obstruction classes are one nontrivial Z2 class. One basepoint choice trivializes the class across these faces; the finite k7 arrow remains a different bit.
- **Kind/domain:** `comparison` / `framework`
- **Depends on:** [OA-C0017](#oa-c0017), [OA-C1124](#oa-c1124), [OA-C1135](#oa-c1135)
- **Leads to:** None.
- **Closure test:** Type all three obstructions in explicit source and target groups, construct commuting maps between them and prove equality of the resulting Z2 class rather than equality of slogans.
- **Falsifier:** Different source groups with no natural comparison, a zero image on one leg, or two models agreeing on one obstruction and differing on another refute the one-bit identity.
- **Scope:** Equality of the named mathematical obstruction torsors under global c. It neither constructs their physical closing acts nor identifies a semantic or conscious observer.
- **Aliases:** `B1169 S1`, `qualia-parity cohomology map`, `one missing bit synthesis`
- **Sources:** [`../evidence/WAVE6_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE6_BRANCH_DELTA_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/b5fae722121d6a8fb009472c1ef2dece1e1727f3/frontier/B1183_one_class_theorem/arc_verdict.json`](https://github.com/originaxiom/origin-axiom/blob/b5fae722121d6a8fb009472c1ef2dece1e1727f3/frontier/B1183_one_class_theorem/arc_verdict.json)
- **Deepest artifacts:** None registered.

<a id="oa-c1142"></a>
### OA-C1142 — `REFUTED`

- **Question:** Does a typed object-native observer self-map exist with a fixed point that selects the mirror-odd orientation bit?
- **Answer:** No. B1184 split-answers the quine. A census-scoped mirror-even self-name has a fixed point, but any object-native map that selected the mirror-odd sign would give an invariant section of the nontrivial c-torsor proved in B1183. Such a sign setter cannot exist. The requested conjunction is therefore false.
- **Kind/domain:** `construction` / `framework`
- **Depends on:** [OA-C1124](#oa-c1124), [OA-C1141](#oa-c1141)
- **Leads to:** None.
- **Closure test:** Define the observer object, its self-map category and fixed-point equation, construct a nontrivial solution and prove that its image sets rather than assumes the orientation class.
- **Falsifier:** A no-fixed-point theorem, multiple inequivalent fixed points selecting opposite bits, or a map that takes orientation as input refutes the selector.
- **Scope:** The formal odd-sign selector is refuted. The weaker mirror-even census self-naming fixed point exists; neither statement implies physical consciousness.
- **Aliases:** `B1169 S4`, `observer quine fixed point`
- **Sources:** [`../evidence/WAVE6_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE6_BRANCH_DELTA_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/d83ffd82cefb0d50c5712daeff8e66999fee19cb/frontier/B1184_quine_synthesis/FINDINGS.md`](https://github.com/originaxiom/origin-axiom/blob/d83ffd82cefb0d50c5712daeff8e66999fee19cb/frontier/B1184_quine_synthesis/FINDINGS.md)
- **Deepest artifacts:** None registered.

<a id="oa-c1146"></a>
### OA-C1146 — `CONDITIONAL`

- **Question:** Across a complete typed observer-datum category, does availability of an arithmetic subgroup that breaks a continuous orbit exactly distinguish finite-label choices from full archimedean observer bits?
- **Answer:** Conditionally. B1171 derives the current orientation/VEV split from two orbit-theorem escapes: the mirror remains an archimedean automorphism, while F4(R) can shrink to F4(Z) and leave finite orbits. It explicitly registers broader typing predictions; two examples do not prove the advertised iff or define a universal cost order.
- **Kind/domain:** `classification` / `framework`
- **Depends on:** [OA-C1135](#oa-c1135)
- **Leads to:** None.
- **Closure test:** Define the datum category and cost order, prove both directions of the orbit-breaker criterion, and exhaust finite and archimedean counterexamples beyond the current orientation/VEV cases.
- **Falsifier:** An archimedean datum with a canonical arithmetic orbit breaker, or a finite-place datum whose admissible symmetry cannot be shrunk and costs a full continuous choice, refutes the classifier.
- **Scope:** A proposed classifier of observer-choice type and cost. It neither removes the choices nor derives physical gravity, gauge breaking or parameter values.
- **Aliases:** `B1171 adelic mechanism tests`, `orbit-breaker observer classifier`
- **Sources:** [`../evidence/WAVE6_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE6_BRANCH_DELTA_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/72ace1cf91abae1be356b17e947c08894f255a8b/frontier/B1164_cc_masterplan/ADDENDUM_adelic_mechanism.md`](https://github.com/originaxiom/origin-axiom/blob/72ace1cf91abae1be356b17e947c08894f255a8b/frontier/B1164_cc_masterplan/ADDENDUM_adelic_mechanism.md)
- **Deepest artifacts:** None registered.

<a id="oa-c1147"></a>
### OA-C1147 — `PROVED`

- **Question:** After freezing the B1024 H1 quotient and branch labels, is there a unique label-preserving V4 isomorphism between the branch and measurement frames?
- **Answer:** Yes. B1182 proves the unique isomorphism (c,r,theta)->(k11,k7,k5). The c leg is forced by the orientation/Galois result, r is the unique K-fixing reversal leg k7, and theta follows by the V4 group law. This is the valid two-frame replacement for the refuted original three-way claim OA-C1133.
- **Kind/domain:** `theorem` / `framework`
- **Depends on:** [OA-C1133](#oa-c1133), [OA-C1138](#oa-c1138)
- **Leads to:** [OA-C1154](#oa-c1154)
- **Closure test:** Freeze both four-point actions and their three named legs, enumerate all equivariant bijections and prove uniqueness under the declared labels.
- **Falsifier:** No label-preserving bijection or two inequivalent admissible bijections refute uniqueness.
- **Scope:** The two frozen finite V4 frames and their programme labels. It does not identify the discarded being-by-hearing frame or create a physical time arrow.
- **Aliases:** `B1182 C4-prime`, `branch-measurement V4 isomorphism`, `time-arrow leg typing`
- **Sources:** [`../evidence/WAVE6_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE6_BRANCH_DELTA_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/63a832252b3be5cd72820a7bfafab67ad4c7d998/frontier/B1182_c4prime_resolved/arc_verdict.json`](https://github.com/originaxiom/origin-axiom/blob/63a832252b3be5cd72820a7bfafab67ad4c7d998/frontier/B1182_c4prime_resolved/arc_verdict.json)
- **Deepest artifacts:** None registered.

<a id="oa-c1152"></a>
### OA-C1152 — `OPEN`

- **Question:** For which heterogeneous grammar partners does simultaneous mirror realization define a nontrivial relational c-class, and does the grammar canonically force one such partner?
- **Answer:** Open. B1192 proves a genuine relational mirror-odd class for exhibited heterogeneous norm-positive pairs, including the sqrt(3)-side partner, with two-sided controls. B1195 GC-24 survives narrowly as PARTIAL: the partner-unit-norm conjecture is false, and the bounded exact sweep supports gen_det=-kappa/g^2 with kappa the joint Fricke invariant and g the intersection-lattice saturation index; equal kappa=121 can yield opposite outcomes. No symbolic universal proof or exhaustive partner classification is supplied. The outside relational-kappa and first-beat certificates reproduce the exhibited pair and the all-word SL2 trace-polynomial law, but neither forces a grammar partner. The general classifier and selection rule remain open.
- **Kind/domain:** `classification` / `framework`
- **Depends on:** [OA-C1124](#oa-c1124), [OA-C1135](#oa-c1135)
- **Leads to:** None.
- **Closure test:** Classify all admissible partner norm classes, compute the simultaneous-realizer torsors and prove both existence and uniqueness or state the residual partner choice.
- **Falsifier:** Two inequivalent admissible partners carrying opposite or absent classes refute canonical forcing; a complete norm theorem can close the scoped classifier.
- **Scope:** Finite relational Z2 classes for declared grammar pairs. An exhibited carrier for c does not make the unoriented object self-orienting.
- **Aliases:** `B1192 relational bit`, `heterogeneous norm classification`, `relational c refinement`
- **Sources:** [`../evidence/WAVE6_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE6_BRANCH_DELTA_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/51516aae92910a522e25e8017cc6c5714f84873e/frontier/B1192_close_loop_batch4/arc_verdict.json`](https://github.com/originaxiom/origin-axiom/blob/51516aae92910a522e25e8017cc6c5714f84873e/frontier/B1192_close_loop_batch4/arc_verdict.json), [`https://github.com/originaxiom/origin-axiom/blob/40916c36ddeb1eb1631097b3535c6a79a2658e23/frontier/B1195_close_loop_batch5a/verification/batch5a_cells.json`](https://github.com/originaxiom/origin-axiom/blob/40916c36ddeb1eb1631097b3535c6a79a2658e23/frontier/B1195_close_loop_batch5a/verification/batch5a_cells.json), [`https://github.com/originaxiom/origin-axiom/blob/f6b96658b9edcf010b26579fe14b21fbeeabcb2b/outside_bench/memos/RELATIONAL_KAPPA.md`](https://github.com/originaxiom/origin-axiom/blob/f6b96658b9edcf010b26579fe14b21fbeeabcb2b/outside_bench/memos/RELATIONAL_KAPPA.md)
- **Deepest artifacts:** None registered.

<a id="oa-c1154"></a>
### OA-C1154 — `OPEN`

- **Question:** Is the outside branch-selection Z2 class exactly the finite frame-reversal leg r=k7 under the proved C4-prime isomorphism?
- **Answer:** Open. B1182 types r=k7 within the frozen branch/measurement pair. The outside grammar certificate does not reach the carrier in the banked representation: its b-matrix has the opposite Riley sign and fails the m004 relator, recorded as OA-C1164. OA-C1165 preserves only the useful local fact that the exact reverser and golden Galois induce the same swap of two projective eigenlines. Its finite controls are not an exhaustive involution census, and no level-crossing map sends that outside branch torsor into the frozen k7 frame. The named identification remains open.
- **Kind/domain:** `comparison` / `framework`
- **Depends on:** [OA-C1131](#oa-c1131), [OA-C1147](#oa-c1147)
- **Leads to:** None.
- **Closure test:** Version the branch action, map its generator into the frozen C4-prime frame and prove equality with k7 including all label conventions.
- **Falsifier:** An image equal to c, theta or the identity, or convention-dependent nonuniqueness, refutes the proposed identification.
- **Scope:** A finite label-identification across two banked programme frames. It creates neither a thermodynamic arrow nor a new physical bit.
- **Aliases:** `B1193 branch-to-r`, `outside branch Z2`, `finite reversal identification`
- **Sources:** [`../evidence/WAVE6_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE6_BRANCH_DELTA_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/0f1c627e5c290439e4f6eeb3723fb5d9f83195d7/docs/GRAND_COMPUTATION_LEDGER.md`](https://github.com/originaxiom/origin-axiom/blob/0f1c627e5c290439e4f6eeb3723fb5d9f83195d7/docs/GRAND_COMPUTATION_LEDGER.md)
- **Deepest artifacts:** None registered.

<a id="oa-c1168"></a>
### OA-C1168 — `OPEN`

- **Question:** Do asymmetric, noncommuting relations between unlike trace-model elements suffice to instantiate an operational occupant or observer, rather than merely form a large class of necessary-type candidates?
- **Answer:** Open. Outside pattern_ladder.py reproducibly counts 13,120 reduced words through length eight, 180 trace values and an unordered-pair fraction satisfying noncommutation plus unequal trace that rises from 0.7481 to 0.9355 through depth five. These are free reduced words rather than proved conjugacy classes, and the code uses unordered combinations despite its ordered-pair wording. The later exact uniqueness test is an explicit counter-pressure: eight proposed predicates yield six distinct admissible sets, A5 retains five competitors, and the proposed phi-stability gate is both unforced and false on A5. Noncommutation and unequal trace are broad necessary-pattern tests; no map to an operational observer, feedback law, token selection or phenomenal state is constructed. The exact supply and nonuniqueness counts expose rather than close the sufficiency bridge.
- **Kind/domain:** `sufficiency` / `framework`
- **Depends on:** [OA-C1142](#oa-c1142), [OA-C1156](#oa-c1156)
- **Leads to:** None.
- **Closure test:** Define occupant or observer in a typed operational category, construct a map from the proposed relation class to systems with the required dynamics, memory, feedback or measurement acts, and prove sufficiency with passive and relabeling controls rather than naming a broad necessary pattern.
- **Falsifier:** A type-eligible relation with no possible operational observer structure, or two indistinguishable eligible relations with different occupant status, refutes sufficiency of the proposed conditions.
- **Scope:** The declared finite Riley trace model and an operational observer notion yet to be defined. It makes no theorem about phenomenal consciousness and supplies no four-dimensional physics or Standard-Model parameter.
- **Aliases:** `outside pattern ladder`, `occupant sufficiency bridge`, `type-eligible seat gap`
- **Sources:** [`../evidence/WAVE6_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE6_BRANCH_DELTA_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/c82fff25ce5c284d1a7ae672aced6642d22d7a76/outside_bench/memos/PATTERN_LADDER.md`](https://github.com/originaxiom/origin-axiom/blob/c82fff25ce5c284d1a7ae672aced6642d22d7a76/outside_bench/memos/PATTERN_LADDER.md), [`https://github.com/originaxiom/origin-axiom/blob/7d4d3655506dba51858594374b06449a572e02f5/outside_bench/memos/UNIQUENESS_TEST.md`](https://github.com/originaxiom/origin-axiom/blob/7d4d3655506dba51858594374b06449a572e02f5/outside_bench/memos/UNIQUENESS_TEST.md)
- **Deepest artifacts:** [`https://github.com/originaxiom/origin-axiom/blob/c82fff25ce5c284d1a7ae672aced6642d22d7a76/outside_bench/certificates/pattern_ladder.py`](https://github.com/originaxiom/origin-axiom/blob/c82fff25ce5c284d1a7ae672aced6642d22d7a76/outside_bench/certificates/pattern_ladder.py), [`https://github.com/originaxiom/origin-axiom/blob/7d4d3655506dba51858594374b06449a572e02f5/outside_bench/certificates/uniqueness_test.py`](https://github.com/originaxiom/origin-axiom/blob/7d4d3655506dba51858594374b06449a572e02f5/outside_bench/certificates/uniqueness_test.py)

## Domain: `genesis`

<a id="oa-c0001"></a>
### OA-C0001 — `REFUTED`

- **Question:** Does bare not-nothing/minimal description select a unique formal seed independently of encoding?
- **Answer:** No. For any computable x, the universal prefix machine U_x with U_x(0)=x and U_x(1p)=U(p) gives x a one-bit description; global minimizers are machine-dependent.
- **Kind/domain:** `uniqueness` / `genesis`
- **Depends on:** None.
- **Leads to:** [OA-C0002](#oa-c0002)
- **Closure test:** An encoding-invariant unique seed theorem.
- **Falsifier:** Two universal description languages with different shortest outputs.
- **Scope:** Unrestricted computable recodings.
- **Aliases:** `C1`, `minimal-description philosophy`
- **Sources:** `../tracks/GENESIS.md`
- **Deepest artifacts:** None registered.

<a id="oa-c0002"></a>
### OA-C0002 — `CONDITIONAL`

- **Question:** Do the declared primitive, aperiodic, unimodular substitution rules select Fibonacci at minimum lexicographic cost?
- **Answer:** Conditionally. Exact enumeration leaves a->ab,b->a up to alphabet exchange/reversal; the category/cost remain an explicit axiom.
- **Kind/domain:** `theorem` / `genesis`
- **Depends on:** [OA-C0001](#oa-c0001)
- **Leads to:** [OA-C0003](#oa-c0003), [OA-C1094](#oa-c1094)
- **Closure test:** Exhaust the finite lower-cost substitution domain modulo declared symmetries.
- **Falsifier:** A lower/equal-cost inequivalent admissible substitution.
- **Scope:** The four-clause substitution category stated in tracks/GENESIS.md.
- **Aliases:** `description axiom`, `minimal-substitution theorem`
- **Sources:** None registered.
- **Deepest artifacts:** `../../physics_bridge/verify_bridge.py`

<a id="oa-c1156"></a>
### OA-C1156 — `OPEN`

- **Question:** Can the programme's Kolmogorov or invariant-prior principle select a unique object or basepoint rather than only a symmetry-invariant probability class?
- **Answer:** Open. B1191 formalizes the proved finite piece: symmetry can fix the prior where it cannot fix a point, and recovers the forgotten F2/F8 locks. B1196 GC-27 is explicitly PARTIAL: it organizes finite-transitive, compact and non-normalizable examples and proves that the exhibited relational epsilon is conjugation-invariant, but gives no uniform Kolmogorov-complexity theorem and has not even typed a (T,G) pair for lambda. B1199 and R023 independently verify the full 745-class finite selection cochain and that its trace-three value is pointwise constant on each of the nine SL(2,F5) shadow classes; this is a complete finite readout, not a unique basepoint. The outside sufficiency test produces six distinct admissible sets from eight proposed predicates, gives A5 five competitors and finds that the proposed phi-stability gate is itself unforced and fails on A5. Paper B8154 removes only the vacuous proper-subgroup escape for a two-element root-swap action. OA-C0001's unrestricted encoding no-go remains an independent warning. The Selector is open.
- **Kind/domain:** `uniqueness` / `genesis`
- **Depends on:** [OA-C0001](#oa-c0001), [OA-C0002](#oa-c0002)
- **Leads to:** [OA-C1168](#oa-c1168)
- **Closure test:** Define the admissible description category and prior, prove encoding and symmetry invariance, and show the selector has one equivalence class of minimizer without inserting the desired basepoint.
- **Falsifier:** Two equally admissible minimizers or a theorem that invariance fixes only a measure and not a point refutes unique selection.
- **Scope:** The declared restricted programme category. It cannot overturn the unrestricted description-language dependence already proved in OA-C0001.
- **Aliases:** `grand-computation H5`, `Kolmogorov Selector`, `selector seal`
- **Sources:** [`../evidence/WAVE6_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE6_BRANCH_DELTA_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/bb018041f2f9805fdd1c6328e89495c3373488c1/frontier/B1194_existence_audit/b1194_results.json`](https://github.com/originaxiom/origin-axiom/blob/bb018041f2f9805fdd1c6328e89495c3373488c1/frontier/B1194_existence_audit/b1194_results.json), [`https://github.com/originaxiom/origin-axiom/blob/40916c36ddeb1eb1631097b3535c6a79a2658e23/frontier/B1196_close_loop_batch5b/verification/batch5b_cells.json`](https://github.com/originaxiom/origin-axiom/blob/40916c36ddeb1eb1631097b3535c6a79a2658e23/frontier/B1196_close_loop_batch5b/verification/batch5b_cells.json), [`https://github.com/originaxiom/origin-axiom/blob/63c047059645fded83d8cdf4976139804df5c644/frontier/B1199_register_reads_and_L188/FINDINGS.md`](https://github.com/originaxiom/origin-axiom/blob/63c047059645fded83d8cdf4976139804df5c644/frontier/B1199_register_reads_and_L188/FINDINGS.md), [`https://github.com/originaxiom/origin-axiom/blob/7d4d3655506dba51858594374b06449a572e02f5/outside_bench/memos/UNIQUENESS_TEST.md`](https://github.com/originaxiom/origin-axiom/blob/7d4d3655506dba51858594374b06449a572e02f5/outside_bench/memos/UNIQUENESS_TEST.md), [`https://github.com/originaxiom/origin-axiom/blob/a31456d2d5e4f08723aa9cfabb7a8573cc2c13d4/frontier/B8154_mirror_is_c/FINDINGS.md`](https://github.com/originaxiom/origin-axiom/blob/a31456d2d5e4f08723aa9cfabb7a8573cc2c13d4/frontier/B8154_mirror_is_c/FINDINGS.md)
- **Deepest artifacts:** [`../../../certificates/r023_b1199_selection_recheck.py`](../certificates/r023_b1199_selection_recheck.py), [`../../../outputs/r023_b1199_selection_recheck.txt`](../outputs/r023_b1199_selection_recheck.txt)

## Domain: `geometry`

<a id="oa-c0009"></a>
### OA-C0009 — `EXTERNAL_BLOCKER`

- **Question:** Does a native closure have net chiral index N_27-N_bar27=3?
- **Answer:** Not yet. Closed doubles have equal 27/bar27 counts; B1084's flat loci intersect on lines; no current 4d Dirac/index functor exists.
- **Kind/domain:** `existence` / `geometry`
- **Depends on:** [OA-C0007](#oa-c0007)
- **Leads to:** [OA-C0019](#oa-c0019), [OA-C0020](#oa-c0020)
- **Closure test:** Compute a global signed index +3, exclude mirror modes and all additional enhancement points.
- **Falsifier:** Index zero, vectorlike pairing, or an unsigned count of labels/points.
- **Scope:** Native closed-double and flat-G2 routes are negative; genuinely new compact singular geometry remains.
- **Aliases:** `chirality`, `B1084`, `B1086`, `B1111`
- **Sources:** None registered.
- **Deepest artifacts:** None registered.

<a id="oa-c0019"></a>
### OA-C0019 — `REFUTED`

- **Question:** Can a whole-group affine cocycle turn a transverse B1111 pair into an isolated order-24 enhancement point?
- **Answer:** No. Averaging proves every affine 1-cocycle is a coboundary. All loci share one full-group fixed point, whose stabilizer has order 96. An order-24 pair is also the wrong E7 enhancement type.
- **Kind/domain:** `theorem` / `geometry`
- **Depends on:** [OA-C0009](#oa-c0009)
- **Leads to:** [OA-C0020](#oa-c0020)
- **Closure test:** A group cocycle satisfying all relations with the claimed point stabilizer.
- **Falsifier:** Vanishing H1 for the finite real representation.
- **Scope:** Affine actions of the finite stored group on real R7.
- **Aliases:** `B1111 affine cocycle feasibility`
- **Sources:** `../tracks/GEOMETRY.md`
- **Deepest artifacts:** None registered.

<a id="oa-c0020"></a>
### OA-C0020 — `EXTERNAL_BLOCKER`

- **Question:** Is there a unique object-selected compact singular geometry with exactly three same-sign E7-to-E6 enhancements and no others?
- **Answer:** Not yet. The flat B1084 isotropy is not binary-octahedral and its intersections are lines. A trivial oriented rank-3 section on a closed oriented 3-manifold cannot have total signed zero count +3.
- **Kind/domain:** `existence` / `geometry`
- **Depends on:** [OA-C0003](#oa-c0003), [OA-C0005](#oa-c0005), [OA-C0019](#oa-c0019)
- **Leads to:** [OA-C0007](#oa-c0007), [OA-C0009](#oa-c0009), [OA-C0011](#oa-c0011)
- **Closure test:** Construct the global unfolding object, prove the local E7 root embeddings, signed index +3, compactness, anomaly consistency, and uniqueness from m004 data.
- **Falsifier:** Wrong isotropy, line rather than point enhancements, conjugating monodromy, additional zeros, or a global zero-sum theorem.
- **Scope:** Nominated native G2/Acharya-Witten completion route.
- **Aliases:** `triple-defect theorem`, `X_OA`
- **Sources:** `../tracks/GEOMETRY.md`, `../../physics_bridge/FULL_CLOSURE.md`
- **Deepest artifacts:** None registered.

<a id="oa-c1001"></a>
### OA-C1001 — `CONDITIONAL`

- **Question:** Does the primitive multiplicative norm law select a smooth fixed-point-free anticanonical hypersurface in the reconstructed C12 toric family?
- **Answer:** Conditionally. For H=Q(zeta_12), trace-dual field norms give invariant orbit weights 0,1,1,1,4 and exact computation proves smoothness and free C12 action; the load-bearing multiplicativity principle remains open.
- **Kind/domain:** `uniqueness` / `geometry`
- **Depends on:** [OA-C1000](#oa-c1000)
- **Leads to:** [OA-C1002](#oa-c1002), [OA-C1004](#oa-c1004), [OA-C1008](#oa-c1008)
- **Closure test:** Derive the multiplicative coefficient law from the admitted minimal-description axioms, then retain the exact smoothness and freeness certificate for its norm section.
- **Falsifier:** A competing admissible coefficient law, failure of smoothness/freeness, or a proof that multiplicativity is not forced in the stated axiom category.
- **Scope:** The invariant P4 of the dP6 x dP6 anticanonical family, conditional on the primitive rational multiplicative scalar-law premise.
- **Aliases:** `norm section selector`, `smooth/free CY conditional`, `multiplicative coefficient law`
- **Sources:** `../tracks/SECTION_VACUUM_SELECTOR.md`, `../tracks/HETEROTIC_BRIDGE_AUDIT.md`
- **Deepest artifacts:** `../experiments/verify_norm_section.sage`, `../experiments/verify_norm_section_freeness.py`

<a id="oa-c1004"></a>
### OA-C1004 — `EXTERNAL_BLOCKER`

- **Question:** Does the class-field norm hypersurface select and stabilize one locally free stable equivariant SU(5) bundle map with the exact-MSSM branch kernel?
- **Answer:** Not yet. The norm section selects coefficients but raw norm reuse has the wrong Euler kernel; the (3,4) BCDD branch is an 11-dimensional map family with ten genuine descended bundle-moduli directions. The marked height-308 pseudoinverse is dual-homed, passes the pointwise gates and has its Hoppe slope stability separately proved by OA-C1013. Minimality, branch-selection inputs and physical realization remain unproved. OA-C1123 adds an exact obstruction: the four surviving bundle/Wilson branches form a free transitive V4 Galois orbit, so no Galois-invariant datum can select one. No dynamical equation selects a unique point.
- **Kind/domain:** `uniqueness` / `geometry`
- **Depends on:** [OA-C1001](#oa-c1001), [OA-C1003](#oa-c1003)
- **Leads to:** [OA-C1005](#oa-c1005), [OA-C1006](#oa-c1006), [OA-C1007](#oa-c1007), [OA-C1012](#oa-c1012), [OA-C1123](#oa-c1123)
- **Closure test:** Exhibit one stable locally free map on the selected norm member and prove that all ten residual Kodaira--Spencer bundle directions are lifted to a unique reduced point by an object-derived dynamical equation.
- **Falsifier:** A surviving stable inequivalent map, a continuous P10 deformation, instability/cohomology jump, or failure of the six-Euler-character kernel condition.
- **Scope:** The BCDD rank-five (3,4) equivariant bundle family over the selected norm hypersurface; distinct from generic branch existence.
- **Aliases:** `stable SU5 bundle point`, `Phi selector`, `bundle moduli blocker`
- **Sources:** `../tracks/NORM_BUNDLE_MAP_AUDIT.md`, `../tracks/PHI_MODULI_QUOTIENT_AUDIT.md`, `../tracks/MARKED_PSEUDOINVERSE_PHI_POINTWISE_AUDIT.md`, `../tracks/BUNDLE_HEIGHT_SELECTOR.md`, `../tracks/HETEROTIC_VACUUM_DYNAMICS.md`
- **Deepest artifacts:** `../experiments/verify_norm_bundle_map.sage`, `../experiments/verify_marked_pseudoinverse_phi.sage`, `../experiments/audit_l34_minimal_height.sage`

<a id="oa-c1012"></a>
### OA-C1012 — `PROVED`

- **Question:** Does the marked equal-weight pseudoinverse define an equivariant locally-free rank-five bundle candidate with the certified pointwise base cohomology maps?
- **Answer:** Yes. Exact Q(zeta12) linear algebra and good-prime unit/minor certificates prove equivariance, local freeness, H0(V)=0, the displayed matter cohomologies, and rank312. B1162 now dual-homes the height-308 witness, and OA-C1013 separately proves pointwise Hoppe slope stability. The construction still uses unforced target directions, coefficient metric and relative weight; minimality and unique physical selection are not established.
- **Kind/domain:** `computation` / `geometry`
- **Depends on:** [OA-C1001](#oa-c1001)
- **Leads to:** [OA-C1013](#oa-c1013)
- **Closure test:** Certify exact-six Euler kernel, H0(V)=0, local freeness, pointwise H1(V) and H1(V*), and surjectivity of the Phi-induced 372-to-312 map.
- **Falsifier:** A base point, extra Euler zero mode, wrong character decomposition, or rank below 312 on the induced map.
- **Scope:** Pointwise algebraic bundle-candidate gates only; OA-C1013 separately supplies the Higgs cohomology and slope stability, but neither row supplies unique selection or a physical vacuum.
- **Aliases:** `marked pseudoinverse Phi`, `arithmetic SU5 bundle candidate`, `pointwise base-map gates`
- **Sources:** `../tracks/MARKED_PSEUDOINVERSE_PHI_POINTWISE_AUDIT.md`
- **Deepest artifacts:** `../experiments/verify_marked_pseudoinverse_phi.sage`

<a id="oa-c1013"></a>
### OA-C1013 — `PROVED`

- **Question:** Does the arithmetic bundle candidate pass pointwise Hoppe stability, given that its exact wedge-square cohomology and MSSM Higgs projection are now certified?
- **Answer:** Yes. At the exact norm-308 point, p=1 and p=4 vanish, the reconstructed Cech 18-to-21 map has rank 16 with determinant-twisted cohomology chi0+chi1, and the quotient map has rank312. The pointwise exterior certificates give induced ranks 27 on H0(Lambda2 G) and 68 on H0(Lambda3 G), hence H0(Lambda2 V)=H0(Lambda3 V)=0. Hoppe's criterion on the h11=1 quotient therefore proves slope stability at this named arithmetic point.
- **Kind/domain:** `computation` / `geometry`
- **Depends on:** [OA-C1012](#oa-c1012), [OA-C1025](#oa-c1025), [OA-C1027](#oa-c1027), [OA-C1032](#oa-c1032)
- **Leads to:** [OA-C1006](#oa-c1006)
- **Closure test:** Prove H0(wedge^2 V)=H0(wedge^3 V)=0 at the exact candidate; the toric Cech 18-to-21 character-block computation is already closed with H1(wedge^2 V*)=chi0+chi1.
- **Falsifier:** A nonzero destabilizing wedge section, failure of a required character-block rank, a cohomology jump, or only a generic-semicontinuity argument that does not specialize to the candidate.
- **Scope:** Finite exact algebraic computation at norm 308 and its free C12 quotient. Stability of the marked, norm-552 and norm-76 points is not inferred.
- **Aliases:** `pointwise Hoppe gate`, `18-to-21 Cech map`, `special-point Higgs cohomology`
- **Sources:** `../tracks/MARKED_PSEUDOINVERSE_PHI_POINTWISE_AUDIT.md`, `../tracks/HOPPE_WEDGE_GATE.md`, `../tracks/HOPPE_LAMBDA3_GATE.md`, `../tracks/BUNDLE_HEIGHT_308.md`
- **Deepest artifacts:** `../experiments/verify_marked_pseudoinverse_cech.sage`, `../experiments/verify_hoppe_wedge.sage`, `../experiments/verify_hoppe_lambda3.sage`

<a id="oa-c1016"></a>
### OA-C1016 — `REFUTED`

- **Question:** Do the no-source heterotic Bianchi identity, full SU(3) tangent holonomy, and McKay E6 compatibility force the visible index-one standard embedding V=TX with F=R?
- **Answer:** No. BCDD construct stable irreducible rank-five SU(5) deformations of TX+O+O on the selected Z12 construction. Characteristic classes are preserved, and their anomaly equation is saturated with trivial hidden bundle and [C]=0. This witness has the same no-source c2 balance as TX but different rank and SU(5), so it is not gauge-equivalent to TX; full SU(3) is a property of TX and does not change that. A literal H=0 differential solution is additional data and is not inferred from the class equation.
- **Kind/domain:** `uniqueness` / `geometry`
- **Depends on:** [OA-C1001](#oa-c1001), [OA-C1015](#oa-c1015)
- **Leads to:** [OA-C1003](#oa-c1003)
- **Closure test:** Prove that every stable visible bundle with c2(V)=c2(TX), trivial hidden bundle, zero five-brane class, and full SU(3) tangent holonomy is the tangent bundle with its induced Levi--Civita connection, up to factor exchange and gauge conjugacy.
- **Falsifier:** One stable non-tangent no-source bundle on the selected quotient, or an argument that Bianchi/Chern--Weil equality cannot identify connections.
- **Scope:** Refutes only selection by anomaly/no-source data. The sufficient functorial premise that the visible principal bundle and connection are the tangent holonomy bundle and Levi--Civita connection is equivalent to imposing the standard embedding, not a derived naturality law.
- **Aliases:** `standard-embedding selector`, `no-five-brane uniqueness`, `F=R selection`
- **Sources:** `../tracks/STANDARD_EMBEDDING_SELECTOR.md`, `../tracks/HETEROTIC_BRIDGE_AUDIT.md`
- **Deepest artifacts:** `../experiments/verify_standard_embedding_selector.py`

<a id="oa-c1023"></a>
### OA-C1023 — `PROVED`

- **Question:** Does exact short-vector descent produce a lower locally-free arithmetic `(3,4)` bundle candidate while retaining all certified pointwise base and Higgs-cohomology gates?
- **Answer:** Yes. Complete enumeration of the 5,088 signed lattice moves through norm 32 gives a fourteen-step locally-free descent from 1580 to 552. The final exact vector has Euler kernel W34, augmented global-kernel dimension six, three unit chart ideals, and rank312 modulo 1009. It is a short-move local minimum, not a certified global minimum or stable point.
- **Kind/domain:** `computation` / `geometry`
- **Depends on:** [OA-C1001](#oa-c1001)
- **Leads to:** [OA-C1013](#oa-c1013)
- **Closure test:** Record exact integral coordinates and height, reproduce every descent step, and recertify the exact-six kernel, H0(V), local freeness and 372-to-312 quotient rank at the final point.
- **Falsifier:** A height other than 552, a nonunit chart ideal, augmented-kernel dimension other than six, or rank below 312 at the recorded coordinates.
- **Scope:** Exact arithmetic candidate improvement only. Global height minimality, pointwise Hoppe stability, unique selection, and vacuum dynamics remain open.
- **Aliases:** `norm-552 bundle candidate`, `short-vector height descent`, `lower arithmetic Phi`
- **Sources:** `../tracks/BUNDLE_HEIGHT_DESCENT_552.md`, `../tracks/MARKED_PSEUDOINVERSE_PHI_POINTWISE_AUDIT.md`
- **Deepest artifacts:** `../experiments/bundle_height_descent.sage`, `../experiments/bundle_low_height_scout.sage`

<a id="oa-c1024"></a>
### OA-C1024 — `REFUTED`

- **Question:** For the selected norm hypersurface and marked `(3,4)` bundle candidate, what is the first-order Atiyah obstruction from the four complex-structure directions, and how many simultaneous moduli remain?
- **Answer:** No. The restricted calculation used only the eleven dPhi columns tangent to the old fixed-f fibre and gave tuples (6,10,4) at marked/552 and (6,6,0) at 308/76. The full incidence tangent uses all 35 equivariant dPhi columns before imposing C_q(dPhi)-f dlambda_q-lambda_q df=0. Its exact and mod-1009 tuple is (30,30,0) at every tested point. The invariant hyperExt comparison gives Ext dimensions (1,12,12,1) and proves the abstract Atiyah map has rank zero on all four invariant complex-structure directions. Thus the rank-four obstruction interpretation is refuted.
- **Kind/domain:** `computation` / `geometry`
- **Depends on:** [OA-C1001](#oa-c1001), [OA-C1004](#oa-c1004), [OA-C1013](#oa-c1013), [OA-C1027](#oa-c1027)
- **Leads to:** [OA-C1033](#oa-c1033), [OA-C1042](#oa-c1042)
- **Closure test:** Construct the sheaf-theoretic comparison from the exact linearised monad incidence matrix to H^2(X,End V), compute the full End V tangent space, and certify the quotient rank.
- **Falsifier:** A full comparison showing that the fixed-fibre rank increase is not the abstract Atiyah rank or that the simultaneous tangent dimension differs from the restricted table.
- **Scope:** The restricted fixed-fibre matrix for the fixed codifferent-norm C12 hypersurface and equivariant BCDD `(3,4)` monad. Its ranks remain exact, but they are not the full Atiyah obstruction ranks.
- **Aliases:** `Atiyah holomorphy map`, `complex-structure obstruction`, `monad simultaneous moduli`
- **Sources:** `../tracks/ATIYAH_MODULI_MAP.md`, `../tracks/FULL_EXT_ATIYAH_COMPARISON.md`, `../tracks/PHI_MODULI_QUOTIENT_AUDIT.md`
- **Deepest artifacts:** `../experiments/verify_atiyah_map.sage.py`, `../experiments/verify_full_ext_atiyah.sage`

<a id="oa-c1025"></a>
### OA-C1025 — `PROVED`

- **Question:** Do the marked pseudoinverse and norm-552 arithmetic maps satisfy the pointwise Hoppe vanishing H0(Lambda^2 V)=0?
- **Answer:** Yes. The exact GF(1009) certificate gives H0(Lambda2 B)=78, Euler-relation rank 51, H0(Lambda2 G)=27, and induced rank 27 for the marked pseudoinverse and independent norm-552 and norm-308 maps. The maximal minor proves characteristic-zero injectivity and hence H0(Lambda2 V)=0.
- **Kind/domain:** `computation` / `geometry`
- **Depends on:** [OA-C1001](#oa-c1001), [OA-C1013](#oa-c1013), [OA-C1023](#oa-c1023), [OA-C1027](#oa-c1027)
- **Leads to:** None.
- **Closure test:** Construct the Lambda2 exterior complex in exact Cox bases and certify rank 27 on the 27-dimensional H0(Lambda2 G) source at both recorded arithmetic candidates.
- **Falsifier:** An exterior relation escaping the target relation space, an ambient quotient dimension other than 27, or induced rank below 27 at either candidate.
- **Scope:** Pointwise Lambda2 vanishing only. Lambda3, full Hoppe stability, HYM, and generic-family transfer remain open.
- **Aliases:** `pointwise Hoppe Lambda2 gate`, `exterior-power rank certificate`, `two-candidate stability gate`
- **Sources:** `../tracks/HOPPE_WEDGE_GATE.md`, `../tracks/MARKED_PSEUDOINVERSE_PHI_POINTWISE_AUDIT.md`
- **Deepest artifacts:** `../experiments/verify_hoppe_wedge.sage`

<a id="oa-c1027"></a>
### OA-C1027 — `REFUTED`

- **Question:** Is the norm-552 point globally minimal among integral exact-six locally-free maps in the rank-44 (3,4) branch, and can trace height select the bundle point?
- **Answer:** No. The KZ vector in BUNDLE_HEIGHT_308.md has exact trace-Hermitian height 308, Euler kernel W34, augmented H0(B) kernel dimension 6, quotient rank 312 for C372 -> C312 modulo 1009, and unit ideals on all three chart orbits. Properness/good reduction certifies characteristic-zero local freeness. Therefore the norm-552 point is not globally minimal. No claim is made that 308 is globally minimal or unique; the randomized discovery is not the proof.
- **Kind/domain:** `theorem` / `geometry`
- **Depends on:** [OA-C1001](#oa-c1001), [OA-C1023](#oa-c1023)
- **Leads to:** [OA-C1013](#oa-c1013), [OA-C1024](#oa-c1024), [OA-C1026](#oa-c1026)
- **Closure test:** Search the full integral branch lattice with exact height and local-freeness gates, or produce a lower certified locally-free exact-six point.
- **Falsifier:** A lower-height exact-six point whose three chart ideals are units in a good reduction, with exact H0 and quotient-rank certificates.
- **Scope:** The fixed saturated integral rank-44 (3,4) branch and prescribed good-prime chart test. Global minimality/uniqueness of 308, slope stability, physical quotienting and derivation of height minimisation remain open.
- **Aliases:** `norm-308 bundle candidate`, `global-height refutation`, `lower locally-free Phi`
- **Sources:** `../tracks/BUNDLE_HEIGHT_308.md`, `../tracks/BUNDLE_HEIGHT_DESCENT_552.md`, `../tracks/BUNDLE_LOW_HEIGHT_BOUND_FORMULATION.md`
- **Deepest artifacts:** `../experiments/bundle_random_below_552.sage`, `../experiments/bundle_low_height_scout.sage`

<a id="oa-c1031"></a>
### OA-C1031 — `PROVED`

- **Question:** Does the integral (3,4) branch contain a low-height point passing the exact-six, H0, local-freeness and Higgs quotient-rank gates, and what is its polynomial Atiyah response?
- **Answer:** Yes. The KZ vector in BUNDLE_HEIGHT_76.md has exact height 76, Euler kernel W34, augmented H0(B) kernel dimension 6, quotient rank 312 modulo 1009, and unit ideals on all three chart orbits, giving characteristic-zero local freeness. The restricted fixed-fibre linearisation has rank 6 before and after adjoining df. The subsequent full hyperExt comparison gives full-incidence tuple (30,30,0), Ext dimensions (1,12,12,1), and abstract Atiyah rank zero. This is the lowest full base/cohomology-gate point found; no global-minimum or uniqueness claim is made.
- **Kind/domain:** `computation` / `geometry`
- **Depends on:** [OA-C1001](#oa-c1001), [OA-C1013](#oa-c1013), [OA-C1027](#oa-c1027)
- **Leads to:** [OA-C1033](#oa-c1033)
- **Closure test:** Record exact integral coordinates and height, certify exact-six, H0(V)=0, local freeness and rank 312 for C372 -> C312, then compute the exact equivariant monad Atiyah rank at the same point.
- **Falsifier:** A coordinate, height, chart ideal, augmented-kernel, quotient-rank, or Atiyah-rank mismatch in the reproducible certificates.
- **Scope:** The fixed saturated integral rank-44 branch and exact pointwise base/Atiyah certificates. Lower-shell completeness, physical equivalence and any height-selector derivation remain open; the separate OA-C1042 child closes the named point's exterior Hoppe gates.
- **Aliases:** `norm-76 bundle candidate`, `full pointwise gate`, `zero Atiyah response`
- **Sources:** `../tracks/BUNDLE_HEIGHT_76.md`, `../tracks/ATIYAH_MODULI_MAP.md`, `../tracks/FULL_EXT_ATIYAH_COMPARISON.md`
- **Deepest artifacts:** `../experiments/bundle_low_height_scout.sage`, `../experiments/verify_atiyah_map.sage.py`, `../experiments/verify_full_ext_atiyah.sage`

<a id="oa-c1032"></a>
### OA-C1032 — `PROVED`

- **Question:** Does the exact norm-308 arithmetic map satisfy the pointwise Hoppe vanishing H0(Lambda^3 V)=0?
- **Answer:** Yes. The exact certificate gives H0(Lambda3 B)=340, source Euler relation rank 272, H0(Lambda3 G)=68, target H0(Lambda2 B(H))=4278 with relation rank 3030, and induced rank 68 modulo 1009. Hence H0(Lambda3 V_308)=0 by a characteristic-zero maximal minor.
- **Kind/domain:** `computation` / `geometry`
- **Depends on:** [OA-C1001](#oa-c1001), [OA-C1023](#oa-c1023), [OA-C1025](#oa-c1025), [OA-C1027](#oa-c1027)
- **Leads to:** None.
- **Closure test:** Construct the Lambda3 exterior complex in exact Cox bases and certify injective induced rank on H0(Lambda3 G) for the norm-308 map.
- **Falsifier:** A source relation escaping the target relation space, source dimension other than 68, target quotient rank failure, or induced rank below 68.
- **Scope:** Pointwise p=3 vanishing at norm 308. The marked and norm-552 p=3 maps remain untested; quotient stability and physical HYM consequences are downstream.
- **Aliases:** `pointwise Lambda3 Hoppe gate`, `norm-308 exterior-power certificate`, `full wedge stability gate`
- **Sources:** `../tracks/HOPPE_LAMBDA3_GATE.md`, `../tracks/HOPPE_WEDGE_GATE.md`
- **Deepest artifacts:** `../experiments/verify_hoppe_lambda3.sage`

<a id="oa-c1033"></a>
### OA-C1033 — `PROVED`

- **Question:** Do the restricted polynomial ranks equal the full sheaf-theoretic Atiyah ranks, and what are Ext1 and Ext2 for the descended exact-six BCDD monad?
- **Answer:** Yes. The full incidence matrix has exact and mod-1009 rank tuple (30,30,0) at marked, 552, 308 and 76, whereas the old (6,10,4) tuple restricted dPhi to the tangent of the old fixed-f fibre. The invariant hyperExt q=0 row has dimensions 8->41->24, ranks 7 and 24, and cohomology (1,10,0). Toric Cech/Koszul cohomology gives two invariant adjacent-pair classes in H1(End B) and two Serre-dual classes in H2(End B); all possible higher differentials have zero source or target. Thus Ext dimensions are (1,12,12,1), and every invariant hypersurface deformation lifts as a monad, proving full Atiyah rank zero.
- **Kind/domain:** `theorem` / `geometry`
- **Depends on:** [OA-C1001](#oa-c1001), [OA-C1013](#oa-c1013), [OA-C1024](#oa-c1024), [OA-C1025](#oa-c1025), [OA-C1027](#oa-c1027), [OA-C1031](#oa-c1031), [OA-C1032](#oa-c1032)
- **Leads to:** [OA-C1028](#oa-c1028)
- **Closure test:** Construct the invariant hyperExt spectral sequence of the locally-free monad, compute every surviving term and possible higher differential, and compare the full 35-column incidence tangent with the restricted eleven-column fixed-fibre matrix.
- **Falsifier:** A nonzero full-incidence rank increase after adjoining invariant df, an invariant Ext dimension different from twelve, or a nonzero abstract Atiyah image for one of the four invariant complex-structure directions.
- **Scope:** Locally-free equivariant exact-six BCDD `(3,4)` monads on the smooth free C12 norm hypersurface and their descended first-order deformation theory. Higher-order obstruction products, stability/HYM and other branches remain separate.
- **Aliases:** `full hyperExt Atiyah comparison`, `monad incidence correction`, `twelve bundle moduli`
- **Sources:** `../tracks/FULL_EXT_ATIYAH_COMPARISON.md`, `../tracks/ATIYAH_MODULI_MAP.md`, `../tracks/PHI_MODULI_QUOTIENT_AUDIT.md`
- **Deepest artifacts:** `../experiments/verify_full_ext_atiyah.sage`, `../experiments/verify_atiyah_map.sage.py`

<a id="oa-c1035"></a>
### OA-C1035 — `PROVED`

- **Question:** Can quadratic or higher Kuranishi obstruction theory isolate the proved-stable height-308 bundle and its simultaneous complex-structure deformation?
- **Answer:** Yes. The stable locally-free height-308 point lies on an actual P10 of inequivalent bundles, so no Kuranishi term can isolate those ten directions. The multiplicative hyperExt filtration makes the fixed-bundle symmetrized quadratic map Sym^2 Ext^1(V,V)->Ext^2(V,V) rank zero. Pure complex-structure directions and all forty P*C terms lift through the exact full-incidence rank (30,30). The two adjacent U orbit classes lift to the full ambient monad because H1_Z(Hom(A,B)+Hom(B,C))=0 and the invariant Hom(B,C)->Hom(A,C) ranks equal their target dimensions (5,4,4,4,4,4). These lifts are independent of the anticanonical equation, so all eight U*C End(V)-projected products vanish. The complete quadratic End(V) projection on P+U+C is therefore zero; higher U terms and the other tangent/hermitian/anomaly components of the full heterotic L3 remain uncomputed.
- **Kind/domain:** `theorem` / `geometry`
- **Depends on:** [OA-C1024](#oa-c1024), [OA-C1027](#oa-c1027), [OA-C1033](#oa-c1033)
- **Leads to:** [OA-C1007](#oa-c1007)
- **Closure test:** Separate integrated stable-family directions from transverse Ext classes, compute the symmetrized Yoneda products and mixed monad-incidence lifts, and state the smallest unresolved coupled block without promoting a projection to the full heterotic L3 obstruction.
- **Falsifier:** A nonzero Kuranishi term on the actual integrated stable P10, an incorrect hyperExt filtration product, failure of the ambient U-lift cohomology/surjectivity calculation, or a nonzero End(V)-projected U*C product.
- **Scope:** The fixed height-308 holomorphic pair, its invariant Ext groups and monad-incidence projection. The result proves non-isolation along P10 and zero of the complete quadratic End(V) projection; it does not compute higher transverse U terms or the complete heterotic L3 obstruction.
- **Aliases:** `height-308 Kuranishi gate`, `quadratic Yoneda non-isolation`, `U-by-C residual`
- **Sources:** `../tracks/KURANISHI_308_OBSTRUCTION_AUDIT.md`, `../tracks/FULL_EXT_ATIYAH_COMPARISON.md`, `../tracks/PHI_MODULI_QUOTIENT_AUDIT.md`
- **Deepest artifacts:** `../experiments/verify_kuranishi_308_nonclosure.sage`, `../experiments/verify_kuranishi_mixed_308.sage`, `../experiments/verify_kuranishi_uc_ambient_308.sage`

<a id="oa-c1042"></a>
### OA-C1042 — `CONDITIONAL`

- **Question:** Does the explicit height-76 (3,4)-branch bundle candidate pass both pointwise Hoppe exterior gates, and is it selected or proved minimal by the available cyclotomic and lattice data?
- **Answer:** Conditionally. The exact Lambda2 and Lambda3 exterior presentations give induced ranks 27 and 68 at height 76, proving both vanishings pointwise and hence Hoppe stability on the fixed h11=1 free quotient. The height-76 map is C12-fixed and fixed by the 12-element marked norm/C12 subgroup, but that subgroup fixes the full 35-dimensional equivariant map space; the candidate lies outside the rank-10 trace/power/Hermitian/norm tensor span. Exact norm-32 shell enumeration remains available, while the finite rank-44 domain 33<=q<76 was not exhaustively completed because PARI qfminim exceeded stack/memory limits and the independent Fincke--Pohst attempt was stopped. No global minimality or basis-free selector theorem is claimed.
- **Kind/domain:** `computation` / `geometry`
- **Depends on:** [OA-C1001](#oa-c1001), [OA-C1012](#oa-c1012), [OA-C1023](#oa-c1023), [OA-C1027](#oa-c1027)
- **Leads to:** None.
- **Closure test:** Certify H0(Lambda2 V)=H0(Lambda3 V)=0 at height 76, then exhaust every integral branch vector of lower height or publish a completeness bound; separately identify an object-native covariant selector.
- **Falsifier:** A nonzero exterior section, a lower locally-free full-gate point, or a proved cyclotomic/norm formula selecting a different inequivalent map.
- **Scope:** The named height-76 integral KZ map in the fixed (3,4) branch, pointwise exterior certificates, and the explicitly stated finite lower-shell search domain. The result does not select a unique stable bundle or a physical vacuum.
- **Aliases:** `height-76 Hoppe certificate`, `height-76 lower-shell audit`, `cyclotomic covariance recognition`
- **Sources:** `../tracks/BUNDLE_HEIGHT_76.md`, `../tracks/HOPPE_LAMBDA3_GATE.md`
- **Deepest artifacts:** `../experiments/verify_hoppe_wedge.sage`, `../experiments/verify_hoppe_lambda3.sage`, `../experiments/bundle_height_76_fp.sage`, `../experiments/inspect_height76_covariance.sage`

<a id="oa-c1068"></a>
### OA-C1068 — `PROVED`

- **Question:** What exact integral matrix does the selected Gieseking beat induce on the marked peripheral homology basis of m004?
- **Answer:** Yes. A SHA-pinned standalone exact calculation reconstructs mu=A and lambda=bABaaBAb over Q(q), proves beat(mu)=mu and beat(lambda)=lambda^-1, and solves equality with every peripheral normal form mu^r lambda^s algebraically rather than by a word cutoff. The induced matrix is diag(1,-1), with determinant -1 and order 2. The same certificate reproduces the distinct infinite-order fiber action and its square.
- **Kind/domain:** `computation` / `geometry`
- **Depends on:** [OA-C0003](#oa-c0003)
- **Leads to:** None.
- **Closure test:** Derive the marked meridian and longitude matrices, compute both exact conjugate-beat images, identify their peripheral words without an arbitrary search cutoff, and certify the resulting integral matrix, determinant and order.
- **Falsifier:** Any exact meridian-longitude mixing or image different from the predicted fixed-meridian/inverted-longitude action refutes the proposed diagonal matrix.
- **Scope:** The specified holonomy marking and peripheral Z-squared basis. It is distinct from the fiber-homology monodromy.
- **Aliases:** `outside-campaign A3`, `peripheral beat matrix`, `cusp-torus H1 beat action`
- **Sources:** [`../evidence/A3_gieseking_peripheral_beat.md`](program-question-map/evidence/A3_gieseking_peripheral_beat.md), [`../evidence/WAVE2_CAMPAIGN_INTAKE.md`](program-question-map/evidence/WAVE2_CAMPAIGN_INTAKE.md), [`https://github.com/originaxiom/origin-axiom/blob/0fe97f9070384d9a5a98c625b1b70131de2556f1/outside_bench/CAMPAIGN_CELLS.json`](https://github.com/originaxiom/origin-axiom/blob/0fe97f9070384d9a5a98c625b1b70131de2556f1/outside_bench/CAMPAIGN_CELLS.json)
- **Deepest artifacts:** [`../evidence/a3_gieseking_peripheral_beat.py`](program-question-map/evidence/a3_gieseking_peripheral_beat.py)

<a id="oa-c1078"></a>
### OA-C1078 — `REFUTED`

- **Question:** Is the restriction from the selected m004 character-variety component to its peripheral character data generically degree one?
- **Answer:** No. Exact elimination on the Riley component shows the peripheral trace coefficient beta(m) is identically zero while the component is generically quadratic in the Riley coordinate. The unoriented peripheral character map is therefore generically two-to-one and blind to the mirror bit, not degree one. Oriented longitude eigenvalues L versus L^-1 can still separate the two branches.
- **Kind/domain:** `computation` / `geometry`
- **Depends on:** [OA-C0003](#oa-c0003)
- **Leads to:** None.
- **Closure test:** Define the exact character-variety component and peripheral eigenvalue quotient, construct the restriction morphism, and certify its generic degree and exceptional fibers by elimination or a function-field calculation.
- **Falsifier:** Generic degree greater than one, a positive-dimensional generic fiber, or an unresolved Weyl/sign quotient refutes the claimed boundary-determines-interior statement as typed.
- **Scope:** The specified beat-selected component and precisely quotiented peripheral restriction. Generic degree one does not imply global injectivity at exceptional or reducible points.
- **Aliases:** `outside-campaign C5`, `QP-1 boundary determines interior`, `peripheral restriction degree`
- **Sources:** [`../evidence/WAVE2_CAMPAIGN_INTAKE.md`](program-question-map/evidence/WAVE2_CAMPAIGN_INTAKE.md), [`https://github.com/originaxiom/origin-axiom/blob/0fe97f9070384d9a5a98c625b1b70131de2556f1/outside_bench/CAMPAIGN_CELLS.json`](https://github.com/originaxiom/origin-axiom/blob/0fe97f9070384d9a5a98c625b1b70131de2556f1/outside_bench/CAMPAIGN_CELLS.json)
- **Deepest artifacts:** None registered.

<a id="oa-c1081"></a>
### OA-C1081 — `PROVED`

- **Question:** Does the selected fiber basis realize the displayed Galois-conjugate fixed pair on the level-zero Fricke surface, exchanged by the beat, with fiber characteristic polynomial X^2-3X+1?
- **Answer:** Yes. The points (2-q,2-q,2-4q) and (1+q,1+q,-2+4q) lie on the level-zero Fricke surface, are fixed by the stipulated trace-map action and are exchanged by the beat. The induced fiber substitution has trace 3, determinant 1 and characteristic polynomial X^2-3X+1.
- **Kind/domain:** `computation` / `geometry`
- **Depends on:** [OA-C1068](#oa-c1068), [OA-C1080](#oa-c1080)
- **Leads to:** [OA-C1082](#oa-c1082), [OA-C1083](#oa-c1083)
- **Closure test:** Rebuild the selected U,V matrices, verify the Fricke level, fixed-point equations, conjugate point, beat exchange and induced abelianized characteristic polynomial.
- **Falsifier:** A failed fixed-point equation, wrong Fricke level, failed beat exchange or different characteristic polynomial refutes the row.
- **Scope:** The selected basis and stipulated trace-map formula. Equality found in one nonfaithful 2 by 2 representation does not by itself prove free-group word equality or uniqueness of the substitution.
- **Aliases:** `memo 43`, `memo 49`, `FIXED_POINT_TWIN`, `TRACE_THREE`
- **Sources:** [`../evidence/OUTSIDE_MEMOS_41_53_AUDIT.md`](program-question-map/evidence/OUTSIDE_MEMOS_41_53_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/631f3477dbfa1bc14d430ed726c61f3bf0722fc5/outside_bench/memos/FIXED_POINT_TWIN.md`](https://github.com/originaxiom/origin-axiom/blob/631f3477dbfa1bc14d430ed726c61f3bf0722fc5/outside_bench/memos/FIXED_POINT_TWIN.md), [`https://github.com/originaxiom/origin-axiom/blob/e4775ee82355ae23c6661a47195d2fcd931b7317/outside_bench/memos/TRACE_THREE.md`](https://github.com/originaxiom/origin-axiom/blob/e4775ee82355ae23c6661a47195d2fcd931b7317/outside_bench/memos/TRACE_THREE.md)
- **Deepest artifacts:** None registered.

<a id="oa-c1082"></a>
### OA-C1082 — `REFUTED`

- **Question:** Is the displayed Galois-conjugate pair the entire fixed locus of the stipulated trace map on the cusped Fricke surface?
- **Answer:** No. Exact elimination gives z^2(z^2+12): the fixed scheme has three support points and length four, namely the displayed simple conjugate pair and the nonreduced origin of multiplicity two. The origin is also a genuine SL2 character, witnessed by U=diag(i,-i) and V=[[0,1],[-1,0]]. Thus the pair is the unique free orbit under conjugation, but not the entire fixed locus.
- **Kind/domain:** `uniqueness` / `geometry`
- **Depends on:** [OA-C1081](#oa-c1081)
- **Leads to:** None.
- **Closure test:** Eliminate the full fixed-point ideal on the Fricke surface and prove that it has exactly the two displayed points.
- **Falsifier:** One additional genuine fixed character refutes the two-point claim.
- **Scope:** The exact polynomial trace map and level-zero Fricke surface stated in memo 43.
- **Aliases:** `memo 43 fixed-locus uniqueness`, `fixed locus is a conjugate pair`
- **Sources:** [`../evidence/WAVE4_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE4_BRANCH_DELTA_AUDIT.md), [`../evidence/OUTSIDE_MEMOS_41_53_AUDIT.md`](program-question-map/evidence/OUTSIDE_MEMOS_41_53_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/f1a7e0c4b0faf11956cf25698d6192eef8f75b67/outside_bench/memos/PERIPHERAL_IDENTITY.md`](https://github.com/originaxiom/origin-axiom/blob/f1a7e0c4b0faf11956cf25698d6192eef8f75b67/outside_bench/memos/PERIPHERAL_IDENTITY.md)
- **Deepest artifacts:** None registered.

<a id="oa-c1083"></a>
### OA-C1083 — `REFUTED`

- **Question:** Is tr(ab^-1)=gal(kappa) an identity on the relevant character component rather than only an equality at the selected holonomy point?
- **Answer:** No. On the Riley component P=z^2-x^2 z+2x^2-z-1=0, exact reduction gives tr(ab^-1)+kappa-3=x^2-4. Hence the proposed constant conjugation is true on the parabolic divisor x^2=4 but false generically; x=0, z=(1+sqrt(5))/2 is an explicit same-component counterexample with defect -4. OA-C1092 records the correct global sheet involution.
- **Kind/domain:** `theorem` / `geometry`
- **Depends on:** [OA-C1080](#oa-c1080), [OA-C1081](#oa-c1081)
- **Leads to:** [OA-C1092](#oa-c1092)
- **Closure test:** Write both trace functions in the component coordinate ring and prove their equality modulo the exact component ideal, including exceptional/reducible loci.
- **Falsifier:** One point on the same component at which the trace functions differ refutes the proposed identity.
- **Scope:** The full nonabelian Riley component. The narrowed equality on the parabolic scheme remains exact.
- **Aliases:** `memo 43 component identity`, `trace(ab^-1)=gal(kappa)`
- **Sources:** [`../../../memos/PERIPHERAL_SHEET_CONJUGACY.md`](../memos/PERIPHERAL_SHEET_CONJUGACY.md), [`../evidence/OUTSIDE_MEMOS_41_53_AUDIT.md`](program-question-map/evidence/OUTSIDE_MEMOS_41_53_AUDIT.md)
- **Deepest artifacts:** [`../../../certificates/r008_peripheral_sheet_conjugacy.py`](../certificates/r008_peripheral_sheet_conjugacy.py)

<a id="oa-c1092"></a>
### OA-C1092 — `PROVED`

- **Question:** On the full nonabelian Riley component, does the quadratic deck involution exchange kappa with tr(ab^-1) by kappa mapping to x^2-1-kappa?
- **Answer:** Yes. For P=z^2-x^2 z+2x^2-z-1, one has kappa=z-1 and tau=tr(ab^-1)=x^2-z modulo P. The involution z -> x^2+1-z preserves P and sends kappa to x^2-1-kappa=tau. Equivalently kappa satisfies K^2-(x^2-1)K+(x^2-1)=0. The familiar 3-kappa formula is its x^2=4 parabolic specialization.
- **Kind/domain:** `theorem` / `geometry`
- **Depends on:** [OA-C1080](#oa-c1080), [OA-C1081](#oa-c1081)
- **Leads to:** None.
- **Closure test:** Derive the component equation and both trace functions in its coordinate ring, exhibit the deck involution, and verify its action without specializing to the geometric point.
- **Falsifier:** A point of the component where the deck transform of kappa differs from tr(ab^-1), or failure of the proposed map to preserve the component, refutes the theorem.
- **Scope:** Exact character-ring algebra on the named Riley component. It supplies no spacetime, dynamics or physical parameter.
- **Aliases:** `global Riley sheet conjugacy`, `peripheral identity replacement`, `R008`
- **Sources:** [`../../../memos/PERIPHERAL_SHEET_CONJUGACY.md`](../memos/PERIPHERAL_SHEET_CONJUGACY.md), [`../evidence/WAVE4_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE4_BRANCH_DELTA_AUDIT.md)
- **Deepest artifacts:** [`../../../certificates/r008_peripheral_sheet_conjugacy.py`](../certificates/r008_peripheral_sheet_conjugacy.py)

<a id="oa-c1101"></a>
### OA-C1101 — `REFUTED`

- **Question:** Does finite-cover nonuniqueness prove the literal claim that no function of normalized hyperbolic isometry type can distinguish a manifold from its finite covers?
- **Answer:** No. Normalized hyperbolic volume is an isometry invariant and satisfies Vol(X_tilde)=d Vol(X) for a degree-d cover, so it distinguishes the covers and refutes the literal inference. The defensible physical statement is narrower: the normalized number does not provide an external conversion to SI length, area or volume. OA-C1029 remains the valid compactification-scale obstruction.
- **Kind/domain:** `theorem` / `geometry`
- **Depends on:** [OA-C1029](#oa-c1029)
- **Leads to:** None.
- **Closure test:** Formalize the claimed function class and either prove cover-invariance for all such functions or exhibit one isometry invariant with nontrivial cover scaling.
- **Falsifier:** A valid normalized isometry invariant that changes under a finite cover refutes the literal cover-indistinguishability claim.
- **Scope:** Only the paper's literal cover-distinguishability inference. It does not refute the need for an external physical unit or curvature scale.
- **Aliases:** `Paper IV cover-scale theorem`, `no isometry invariant distinguishes covers`, `R014`
- **Sources:** [`../../../memos/PAPER4_SCALE_FAMILY_AUDIT.md`](../memos/PAPER4_SCALE_FAMILY_AUDIT.md), [`../evidence/WAVE4_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE4_BRANCH_DELTA_AUDIT.md)
- **Deepest artifacts:** [`../../../certificates/r014_paper4_counterexamples.py`](../certificates/r014_paper4_counterexamples.py)

<a id="oa-c1102"></a>
### OA-C1102 — `REFUTED`

- **Question:** Is the Paper-IV list of fourteen orientable cusped census manifolds exhaustive for the declared Q(sqrt(-3)) shape-field family?
- **Answer:** No. The source scan stops at zero-based census index 1200 in a 212641-entry census, and its paper verifier hardcodes the fourteen names without gating the field result. The manifold s955 at index 1256 is an explicit counterexample: all six regular tetrahedron shapes satisfy q^2-q+1=0, and its vendored exact gluing data pass six edge and two cusp equations, placing its shape field in Q(sqrt(-3)).
- **Kind/domain:** `computation` / `geometry`
- **Depends on:** [OA-C0003](#oa-c0003)
- **Leads to:** [OA-C1103](#oa-c1103)
- **Closure test:** Run an exact complete-census field test over the declared census and show that every hit is one of the fourteen listed manifolds.
- **Falsifier:** One certified family member beyond the list refutes exhaustiveness.
- **Scope:** The claimed exhaustive fourteen-member census family. The existing fourteen-row table remains a bounded sample, and no unverified full-census hit count is asserted.
- **Aliases:** `Paper IV 14-member family`, `B8128 census cutoff`, `s955 counterexample`, `R014`
- **Sources:** [`../../../memos/PAPER4_SCALE_FAMILY_AUDIT.md`](../memos/PAPER4_SCALE_FAMILY_AUDIT.md), [`../evidence/WAVE4_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE4_BRANCH_DELTA_AUDIT.md)
- **Deepest artifacts:** [`../../../certificates/r014_paper4_counterexamples.py`](../certificates/r014_paper4_counterexamples.py)

<a id="oa-c1103"></a>
### OA-C1103 — `REFUTED`

- **Question:** Over the complete exactly certified Q(sqrt(-3)) cusped-census family, is H1=Z still the unique one of the seven declared elementary invariants that isolates m004?
- **Answer:** No. B1186 regenerates the Paper-IV shape-field family at declared census and denominator bounds and corrects its size to 112. The member o10_150700 is one-cusped, belongs to that family and has H1=Z, so H1=Z does not uniquely isolate m004. That single exact counterexample refutes the proposed seven-invariant separator claim; OA-C1134 keeps the stronger exact all-cusp comparison open because B1186's cusp-shape collisions were checked numerically rather than by an exact peripheral certificate.
- **Kind/domain:** `computation` / `geometry`
- **Depends on:** [OA-C1102](#oa-c1102)
- **Leads to:** [OA-C1134](#oa-c1134)
- **Closure test:** Reconstruct the entire family by an exact shape-field test, state triangulation conventions, compute all seven invariants with exact or certified comparisons, and prove the separator claim over every hit.
- **Falsifier:** A second full-family invariant that uniquely isolates m004, or another family member with H1=Z, refutes the proposed uniqueness; an incomplete field census withholds closure.
- **Scope:** The corrected full family and exactly the seven named elementary invariants. This is a feasible census computation, not an external theorem blocker.
- **Aliases:** `Paper IV corrected family separator`, `full Eisenstein-shape census`, `seven-invariant uniqueness`
- **Sources:** [`../../../memos/PAPER4_SCALE_FAMILY_AUDIT.md`](../memos/PAPER4_SCALE_FAMILY_AUDIT.md), [`../evidence/WAVE6_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE6_BRANCH_DELTA_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/1662dcb2ee6b7f2518cc55ce2409d455b2bb833f/frontier/B1186_family_is_112/FINDINGS.md`](https://github.com/originaxiom/origin-axiom/blob/1662dcb2ee6b7f2518cc55ce2409d455b2bb833f/frontier/B1186_family_is_112/FINDINGS.md)
- **Deepest artifacts:** [`../../../certificates/r014_paper4_counterexamples.py`](../certificates/r014_paper4_counterexamples.py)

<a id="oa-c1104"></a>
### OA-C1104 — `PROVED`

- **Question:** In the common absolute-convergence region, does the Ruelle Euler product for rho_m=Sym^(2m)(C^2) factor exactly as the product over j=-m,...,m of R(s-j,sigma_j)?
- **Answer:** Yes. If a holonomy element has complex length L=l+i theta, Sym^(2m) has eigenvalues exp(jL), j=-m,...,m, and exp(jL)exp(-s l)=exp(i j theta)exp(-(s-j)l). Termwise multiplication therefore gives R_rho_m(s)=product_j R(s-j,sigma_j) in Re(s)>m+2. The paper checks m=0,...,4 on m004 to 5e-18 with three live controls; main independently re-derived it two ways.
- **Kind/domain:** `theorem` / `geometry`
- **Depends on:** [OA-C0003](#oa-c0003)
- **Leads to:** [OA-C1105](#oa-c1105), [OA-C1106](#oa-c1106), [OA-C1108](#oa-c1108)
- **Closure test:** Derive the identity termwise from the Sym^(2m) holonomy eigenvalues, state a common absolute-convergence half-plane, and verify nonvacuous finite controls.
- **Falsifier:** One primitive geodesic factor with a different eigenvalue/twist decomposition, or a mismatch inside the common convergence domain, refutes the identity.
- **Scope:** An exact M-character Euler-product identity in the shared convergence region. Sigma_j is an M-character, not generally a Gamma representation. No analytic continuation, functional equation, Fried identity, graviton determinant or physics follows.
- **Aliases:** `B8142 Sym-power identity`, `B1157 bank-grade factorization`, `Ruelle twist-family decomposition`
- **Sources:** [`../evidence/WAVE5_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE5_BRANCH_DELTA_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/d0ad0e960b71ca743e6f8c0a20348edf54b97e8e/frontier/B8142_residue2_bridge/FINDINGS.md`](https://github.com/originaxiom/origin-axiom/blob/d0ad0e960b71ca743e6f8c0a20348edf54b97e8e/frontier/B8142_residue2_bridge/FINDINGS.md), [`https://github.com/originaxiom/origin-axiom/blob/c54ae43328e38947241b3be33d11557d530db3bc/frontier/B1157_dynamics_null/FINDINGS.md`](https://github.com/originaxiom/origin-axiom/blob/c54ae43328e38947241b3be33d11557d530db3bc/frontier/B1157_dynamics_null/FINDINGS.md)
- **Deepest artifacts:** [`https://github.com/originaxiom/origin-axiom/blob/d0ad0e960b71ca743e6f8c0a20348edf54b97e8e/frontier/B8142_residue2_bridge/bridge.py`](https://github.com/originaxiom/origin-axiom/blob/d0ad0e960b71ca743e6f8c0a20348edf54b97e8e/frontier/B8142_residue2_bridge/bridge.py)

<a id="oa-c1105"></a>
### OA-C1105 — `REFUTED`

- **Question:** Are the m004 local systems Sym^(2m)(C^2) acyclic for m>=1, so that the closed-manifold Fried value formula used in the proposed reflection derivation applies?
- **Answer:** No. Exact Q(sqrt(-3)) computation gives (h0,h1,h2)=(0,1,1) for m=1,...,5, already refuting acyclicity; m=0 gives (1,1,0). The general peripheral mechanism is that the parabolic cusp fixes one line in every even symmetric power, planting cusp cohomology. The paper independently reproduced the result to n=40 and withdrew the numerical reflection predictions.
- **Kind/domain:** `theorem` / `geometry`
- **Depends on:** [OA-C1104](#oa-c1104)
- **Leads to:** [OA-C1106](#oa-c1106), [OA-C1107](#oa-c1107), [OA-C1108](#oa-c1108)
- **Closure test:** Compute the twisted cohomology with exact holonomy data and verify every hypothesis of the stated Fried theorem in the cusped setting.
- **Falsifier:** One nonzero twisted cohomology group refutes acyclicity and invalidates the proposed use of the closed-Fried value formula.
- **Scope:** The geometric m004 representation and its even symmetric powers. The finite exact counterexamples suffice to refute the universal acyclicity claim; the all-m mechanism is a separately cited topology statement.
- **Aliases:** `B1157 acyclicity refutation`, `B8142b withdrawal`, `closed-Fried antecedent`
- **Sources:** [`../evidence/WAVE5_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE5_BRANCH_DELTA_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/c54ae43328e38947241b3be33d11557d530db3bc/frontier/B1157_dynamics_null/FINDINGS.md`](https://github.com/originaxiom/origin-axiom/blob/c54ae43328e38947241b3be33d11557d530db3bc/frontier/B1157_dynamics_null/FINDINGS.md), [`https://github.com/originaxiom/origin-axiom/blob/d0ad0e960b71ca743e6f8c0a20348edf54b97e8e/frontier/B8142_residue2_bridge/FINDINGS.md`](https://github.com/originaxiom/origin-axiom/blob/d0ad0e960b71ca743e6f8c0a20348edf54b97e8e/frontier/B8142_residue2_bridge/FINDINGS.md)
- **Deepest artifacts:** [`https://github.com/originaxiom/origin-axiom/blob/d0ad0e960b71ca743e6f8c0a20348edf54b97e8e/frontier/B8142_residue2_bridge/acyclicity.py`](https://github.com/originaxiom/origin-axiom/blob/d0ad0e960b71ca743e6f8c0a20348edf54b97e8e/frontier/B8142_residue2_bridge/acyclicity.py), [`https://github.com/originaxiom/origin-axiom/blob/c54ae43328e38947241b3be33d11557d530db3bc/frontier/B1157_dynamics_null/verification/reproduce.sh`](https://github.com/originaxiom/origin-axiom/blob/c54ae43328e38947241b3be33d11557d530db3bc/frontier/B1157_dynamics_null/verification/reproduce.sh)

<a id="oa-c1106"></a>
### OA-C1106 — `EXTERNAL_BLOCKER`

- **Question:** What are the exact order of vanishing and leading Laurent coefficient at s=0 of the cusped complex-orthogonal torsion/Ruelle object for rho_m=Sym^(2m)(C^2) on m004?
- **Answer:** Not yet. Because H^1 and H^2 are nonzero, the relevant Ruelle object has a nonzero order at s=0 rather than the finite acyclic value used by the withdrawn Fried step. Neither main nor the paper computes its leading Laurent coefficient; both route this to cusped Park/Pfaff or Cappell-Miller theory.
- **Kind/domain:** `computation` / `geometry`
- **Depends on:** [OA-C1104](#oa-c1104), [OA-C1105](#oa-c1105)
- **Leads to:** [OA-C1107](#oa-c1107)
- **Closure test:** Define the cusped Cappell-Miller normalization and canonical cusp-cohomology basis, then derive the order and leading coefficient with a reproducible exact or certified calculation.
- **Falsifier:** A different order or coefficient under the fixed normalization, or proof that no canonical normalization exists for the declared object, refutes the proposed value.
- **Scope:** Finite-volume cusped m004 and the complex-orthogonal rho_m family. This is a specialist analytic-torsion construction, not a graviton determinant or physical dynamics.
- **Aliases:** `B1157 specialist residue 1`, `Cappell-Miller Laurent coefficient`
- **Sources:** [`../evidence/WAVE5_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE5_BRANCH_DELTA_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/c54ae43328e38947241b3be33d11557d530db3bc/frontier/B1157_dynamics_null/FINDINGS.md`](https://github.com/originaxiom/origin-axiom/blob/c54ae43328e38947241b3be33d11557d530db3bc/frontier/B1157_dynamics_null/FINDINGS.md)
- **Deepest artifacts:** None registered.

<a id="oa-c1107"></a>
### OA-C1107 — `EXTERNAL_BLOCKER`

- **Question:** Does the exact Park/Pfaff cusp, Borel-Serre and scattering correction for the declared twisted m004 torsion equal exp(-4m Vol(m004)/pi) under one fixed normalization?
- **Answer:** Not yet. The volume damping is presently a structural target assembled from generic hyperbolic formulas. The closed-Fried shortcut is refuted, and the existing scalar scattering identity does not supply the spin-resolved cusped equation.
- **Kind/domain:** `theorem` / `geometry`
- **Depends on:** [OA-C1062](#oa-c1062), [OA-C1105](#oa-c1105), [OA-C1106](#oa-c1106)
- **Leads to:** [OA-C1108](#oa-c1108)
- **Closure test:** Derive all parabolic, scattering, zero-mode and cusp-boundary terms and prove the exponential volume factor with its normalization.
- **Falsifier:** An additional or missing cusp term, a different exponent, or failure after the correct completion is fixed refutes the proposed identity.
- **Scope:** The exact cusped m004 geometry and rho_m family. Even a positive identity would remain generic spectral geometry and would not construct four-dimensional Einstein dynamics.
- **Aliases:** `B1157 specialist residue 2`, `Park-Pfaff cusp correction`
- **Sources:** [`../evidence/WAVE5_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE5_BRANCH_DELTA_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/c54ae43328e38947241b3be33d11557d530db3bc/frontier/B1157_dynamics_null/FINDINGS.md`](https://github.com/originaxiom/origin-axiom/blob/c54ae43328e38947241b3be33d11557d530db3bc/frontier/B1157_dynamics_null/FINDINGS.md)
- **Deepest artifacts:** None registered.

<a id="oa-c1108"></a>
### OA-C1108 — `EXTERNAL_BLOCKER`

- **Question:** Does a correctly completed twisted Ruelle function for the rho_m family on cusped m004 satisfy the required s-to-2-s functional equation including every cusp and scattering term?
- **Answer:** Not yet. The exact Sym-power factorization does not provide analytic continuation or a functional equation. The current scalar determinant relation and positive-integer M-character products do not establish the negative-argument values needed by residue 2.
- **Kind/domain:** `theorem` / `geometry`
- **Depends on:** [OA-C1104](#oa-c1104), [OA-C1105](#oa-c1105), [OA-C1107](#oa-c1107)
- **Leads to:** None.
- **Closure test:** State the completed twisted-Ruelle object, derive its cusp/scattering completion and prove the s-to-2-s equation with exact normalizations.
- **Falsifier:** A certified counterexample after completion, or proof that the equation applies only to a different compact or loxodromic object, refutes the proposed reflection.
- **Scope:** The completed M-character/twisted-Ruelle family on finite-volume cusped m004. No direct Einstein spin-two determinant or physical law is implied.
- **Aliases:** `B1157 specialist residue 3`, `B8101 twisted-Ruelle reflection`
- **Sources:** [`../evidence/WAVE5_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE5_BRANCH_DELTA_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/c54ae43328e38947241b3be33d11557d530db3bc/frontier/B1157_dynamics_null/FINDINGS.md`](https://github.com/originaxiom/origin-axiom/blob/c54ae43328e38947241b3be33d11557d530db3bc/frontier/B1157_dynamics_null/FINDINGS.md), [`../../../memos/PAPER3_RUELLE_SCOPE_AUDIT.md`](../memos/PAPER3_RUELLE_SCOPE_AUDIT.md)
- **Deepest artifacts:** [`../../../certificates/r011_ruelle_scope.py`](../certificates/r011_ruelle_scope.py)

<a id="oa-c1123"></a>
### OA-C1123 — `REFUTED`

- **Question:** Can a Galois-invariant datum of Q(zeta12) select one branch from the four surviving bundle and Wilson-line branches?
- **Answer:** No. The exact branch action of Gal(Q(zeta12)/Q)=V4 is free and transitive. Every invariant function is therefore constant on all four branches, so none can select one. A non-Galois-invariant archimedean marking or extra observer choice is outside the theorem.
- **Kind/domain:** `uniqueness` / `geometry`
- **Depends on:** [OA-C1004](#oa-c1004), [OA-C1012](#oa-c1012)
- **Leads to:** None.
- **Closure test:** Exhibit an invariant function on the four-branch set with a unique value-minimizing or distinguished branch.
- **Falsifier:** A Galois-invariant branch datum taking a different value on one member would refute the obstruction.
- **Scope:** Exactly the four surviving height-308 bundle/Wilson branches with their named V4 Galois action. This does not classify selectors that explicitly break Galois symmetry.
- **Aliases:** `B1161 free V4 orbit`, `Galois branch selector obstruction`, `four-branch torsor`
- **Sources:** [`../evidence/WAVE5_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE5_BRANCH_DELTA_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/bf580f45840d121a811d2b6606c48beac92c3057/frontier/B1161_frontier_sweep/FINDINGS.md`](https://github.com/originaxiom/origin-axiom/blob/bf580f45840d121a811d2b6606c48beac92c3057/frontier/B1161_frontier_sweep/FINDINGS.md)
- **Deepest artifacts:** [`https://github.com/originaxiom/origin-axiom/blob/bf580f45840d121a811d2b6606c48beac92c3057/frontier/B1161_frontier_sweep/verification/reproduce.sh`](https://github.com/originaxiom/origin-axiom/blob/bf580f45840d121a811d2b6606c48beac92c3057/frontier/B1161_frontier_sweep/verification/reproduce.sh)

<a id="oa-c1124"></a>
### OA-C1124 — `REFUTED`

- **Question:** Does the unoriented amphichiral m004 object canonically select an orientation, a positive signed regulator volume, or one complex embedding of Q(sqrt(-3))?
- **Answer:** No. m004 admits an orientation-reversing self-isometry. Complex conjugation exchanges the two embeddings and the Bloch--Wigner regulator changes sign, so an automorphism-invariant datum of the unoriented object cannot distinguish +Vol from -Vol. Paper B8154 independently verifies on its chosen holonomy model that t^2 is a primitive cube root and u->u^2 is the conjugation/root swap; its prime-order subgroup argument removes shrinking the two-element symmetry as a nontrivial escape, but it supplies no preferred root. The positive volume magnitude is mirror-even and is not refuted.
- **Kind/domain:** `uniqueness` / `geometry`
- **Depends on:** [OA-C0003](#oa-c0003), [OA-C1045](#oa-c1045)
- **Leads to:** [OA-C1135](#oa-c1135)
- **Closure test:** Construct a selector invariant under every automorphism of the unoriented object that distinguishes the two orientations or conjugate embeddings.
- **Falsifier:** An automorphism-invariant orientation or embedding selector would refute the obstruction.
- **Scope:** The carrier regarded as an unoriented amphichiral hyperbolic object. Supplying an orientation externally changes the object and evades, rather than disproves, the no-selector theorem.
- **Aliases:** `B1163 orientation obstruction`, `amphichiral W0 sign wall`, `regulator-sign selector`
- **Sources:** [`../evidence/WAVE5_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE5_BRANCH_DELTA_AUDIT.md), [`../evidence/WAVE6_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE6_BRANCH_DELTA_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/bf580f45840d121a811d2b6606c48beac92c3057/frontier/B1163_w0_attempt/ADDENDUM_orientation_theorem.md`](https://github.com/originaxiom/origin-axiom/blob/bf580f45840d121a811d2b6606c48beac92c3057/frontier/B1163_w0_attempt/ADDENDUM_orientation_theorem.md), [`https://github.com/originaxiom/origin-axiom/blob/a31456d2d5e4f08723aa9cfabb7a8573cc2c13d4/frontier/B8154_mirror_is_c/FINDINGS.md`](https://github.com/originaxiom/origin-axiom/blob/a31456d2d5e4f08723aa9cfabb7a8573cc2c13d4/frontier/B8154_mirror_is_c/FINDINGS.md)
- **Deepest artifacts:** [`https://github.com/originaxiom/origin-axiom/blob/bf580f45840d121a811d2b6606c48beac92c3057/frontier/B1163_w0_attempt/verification/reproduce.sh`](https://github.com/originaxiom/origin-axiom/blob/bf580f45840d121a811d2b6606c48beac92c3057/frontier/B1163_w0_attempt/verification/reproduce.sh)

<a id="oa-c1129"></a>
### OA-C1129 — `PROVED`

- **Question:** In the declared finite cyclic-word ball for m004, do the holonomy traces lie in Z[omega] and exhibit the tested mirror-partner pattern?
- **Answer:** Yes. The independently rerun computation enumerates 275 cyclic-word classes through length seven, with every trace in Z[omega]. Mirror pairing is certified for the 25-class inner ball through length four using a targeted search through length nine. It does not establish an all-word length-spectrum theorem.
- **Kind/domain:** `computation` / `geometry`
- **Depends on:** [OA-C0003](#oa-c0003), [OA-C1075](#oa-c1075)
- **Leads to:** None.
- **Closure test:** Enumerate cyclic word classes through the declared length, compute exact traces in the Eisenstein ring and run the stated bounded partner search with no missing class.
- **Falsifier:** A trace outside Z[omega], a wrong class count, or a missing partner within the declared search domain refutes the corresponding bounded claim.
- **Scope:** Cyclic word classes through length seven and the explicitly targeted mirror search for the length-four inner ball. Universal spectral symmetry and physical dynamics are not claimed.
- **Aliases:** `outside geodesic tongue`, `finite trace-language census`, `bounded mirror partners`
- **Sources:** [`../evidence/WAVE5_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE5_BRANCH_DELTA_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/60bcf01db966ae0b13f18c73c24845040b59fd98/outside_bench/memos/GEODESIC_TONGUE.md`](https://github.com/originaxiom/origin-axiom/blob/60bcf01db966ae0b13f18c73c24845040b59fd98/outside_bench/memos/GEODESIC_TONGUE.md)
- **Deepest artifacts:** [`https://github.com/originaxiom/origin-axiom/blob/60bcf01db966ae0b13f18c73c24845040b59fd98/outside_bench/certificates/geodesic_tongue.py`](https://github.com/originaxiom/origin-axiom/blob/60bcf01db966ae0b13f18c73c24845040b59fd98/outside_bench/certificates/geodesic_tongue.py)

<a id="oa-c1134"></a>
### OA-C1134 — `OPEN`

- **Question:** Over the complete corrected exact Q(sqrt(-3)) cusped census, does the full cusp-shape datum uniquely isolate m004 up to conjugation?
- **Answer:** Open. B1186 regenerates a 112-member family at its declared census and denominator bounds and finds two one-cusped witnesses, o9_41001 and o9_41009, numerically sharing m004's 2*sqrt(3)i cusp shape. That is a sharp near-refutation, but the committed comparison casts cusp_info to complex and uses a 1e-6 tolerance; only tetrahedron shapes and gluing equations receive exact symbolic certification. The row therefore remains open until one witness receives an exact peripheral/cusp certificate.
- **Kind/domain:** `computation` / `geometry`
- **Depends on:** [OA-C1102](#oa-c1102), [OA-C1103](#oa-c1103)
- **Leads to:** None.
- **Closure test:** Regenerate the complete family by a certified exact field criterion, compute every cusp shape exactly up to the declared equivalences and compare m004 against every hit including s955.
- **Falsifier:** Another family member with the same full cusp-shape datum, or an incomplete/rounded census, refutes or withholds the uniqueness claim.
- **Scope:** The complete corrected exact Eisenstein trace/shape-field family, every cusp and cusp shape up to conjugation. Cusp shape 2*sqrt(3)*i for m004 is mirror-fixed and cannot select orientation.
- **Aliases:** `Paper IV cusp-shape extension`, `corrected Eisenstein family cusp census`, `s955-complete cusp test`
- **Sources:** [`../evidence/WAVE6_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE6_BRANCH_DELTA_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/1662dcb2ee6b7f2518cc55ce2409d455b2bb833f/frontier/B1186_family_is_112/FINDINGS.md`](https://github.com/originaxiom/origin-axiom/blob/1662dcb2ee6b7f2518cc55ce2409d455b2bb833f/frontier/B1186_family_is_112/FINDINGS.md)
- **Deepest artifacts:** None registered.

<a id="oa-c1164"></a>
### OA-C1164 — `REFUTED`

- **Question:** Does the outside grammar_disc48 certificate instantiate the banked m004 Riley representation and thereby prove that baBAABab is a peripheral longitude with discriminant-48 translation lattice?
- **Answer:** No. The certificate uses b=[[1,0],[-omega,1]], while the banked Riley realization uses lower-left +omega. Its own matrices send the banked relator abABaBAbaB to [[-1,0],[-4,-1]] rather than the identity, and the script never checks that relator. After correcting the sign, baBAABab is not the banked longitude; the established peripheral word is bABaaBAb. The later form enumeration is valid for the asserted translation but cannot repair the failed representation/word gate. The advertised grammar-to-disc-48 closure is therefore refuted.
- **Kind/domain:** `repair` / `geometry`
- **Depends on:** [OA-C0003](#oa-c0003), [OA-C1068](#oa-c1068)
- **Leads to:** [OA-C1154](#oa-c1154)
- **Closure test:** Verify the banked m004 relator in the exact matrices before searching words, then prove the claimed word is a nontrivial peripheral element and compute its translation lattice.
- **Falsifier:** Failure of the banked relator in the certificate's matrices, or a nonperipheral claimed word after correcting the representation, refutes the certificate-level bridge.
- **Scope:** The outside certificate's exact representation and claimed word. This does not refute the already banked discriminant-48 cusp lattice; it refutes the claimed derivation from that script and leaves the swap choice open.
- **Aliases:** `outside memo 100`, `grammar-to-disc-48 closure`, `claimed longitude word baBAABab`
- **Sources:** [`../evidence/WAVE6_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE6_BRANCH_DELTA_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/bc9d381d0018cdc112ddac2373fe767ee4247531/outside_bench/memos/GRAMMAR_DISC48.md`](https://github.com/originaxiom/origin-axiom/blob/bc9d381d0018cdc112ddac2373fe767ee4247531/outside_bench/memos/GRAMMAR_DISC48.md)
- **Deepest artifacts:** [`../../../certificates/r023_wave6_outside_hostile.py`](../certificates/r023_wave6_outside_hostile.py), [`../../../outputs/r023_wave6_outside_hostile.txt`](../outputs/r023_wave6_outside_hostile.txt), [`https://github.com/originaxiom/origin-axiom/blob/bc9d381d0018cdc112ddac2373fe767ee4247531/outside_bench/certificates/grammar_disc48.py`](https://github.com/originaxiom/origin-axiom/blob/bc9d381d0018cdc112ddac2373fe767ee4247531/outside_bench/certificates/grammar_disc48.py)

## Domain: `gravity`

<a id="oa-c1151"></a>
### OA-C1151 — `OPEN`

- **Question:** Does a genuine E6-lattice boundary character identify the stage's sigma normalization with the banked CFT or two-sixes structure and thereby delete sigma as an independent anchor?
- **Answer:** Open. B1190 refutes the prior synthesis as a kind error. B1191 exhausts main's q-series fingerprint route and finds its only candidate fails the required kind/positivity map; the outside artifact survey extends that negative across its Habiro, zeta-count, dark-table and coupling holdings. Tip 9915068b constructs the generic level-one E6 lattice source exactly: an Eisenstein rank-three lattice with discriminant group F3, primaries {1,27,27bar}, vacuum opening 1,78,729 and 27 opening 27,378. It still supplies no normalized map from those characters to a record-side q-series and no identification with sigma. B1195 GC-23 rules out the tested raw/direct cusp Gram constructions, but its own hostile lens rejects the universal claim: interior, linking or Poincare-Lefschetz pairings can carry cross-cusp terms and were not classified. Its claimed tie through outside memo 100 also fails because OA-C1164 refutes that memo's Riley realization. The source object exists; the character-to-record bridge remains open.
- **Kind/domain:** `construction` / `gravity`
- **Depends on:** [OA-C0017](#oa-c0017)
- **Leads to:** None.
- **Closure test:** Construct a boundary character in the correct representation, prove its transformation and positivity properties, and derive the sigma normalization without matching unrelated q-series exponents or measured values.
- **Falsifier:** Nonexistence of the required character or a normalization still containing a free scale refutes the deletion route.
- **Scope:** The internal dimensionless sigma normalization. Even success would not derive a physical length unit or Newton constant in SI units.
- **Aliases:** `L154`, `sigma deletion bridge`, `E6 boundary character`
- **Sources:** [`../evidence/WAVE6_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE6_BRANCH_DELTA_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/1e1aa1d0c04c61dcb2c0d99b08faf80f63021ae9/docs/GRAND_COMPUTATION_v0.md`](https://github.com/originaxiom/origin-axiom/blob/1e1aa1d0c04c61dcb2c0d99b08faf80f63021ae9/docs/GRAND_COMPUTATION_v0.md), [`https://github.com/originaxiom/origin-axiom/blob/9915068bdb44f88e7cca06961d15c8cd0f7d1d0a/outside_bench/memos/E6_BOUNDARY.md`](https://github.com/originaxiom/origin-axiom/blob/9915068bdb44f88e7cca06961d15c8cd0f7d1d0a/outside_bench/memos/E6_BOUNDARY.md), [`https://github.com/originaxiom/origin-axiom/blob/40916c36ddeb1eb1631097b3535c6a79a2658e23/frontier/B1195_close_loop_batch5a/verification/batch5a_cells.json`](https://github.com/originaxiom/origin-axiom/blob/40916c36ddeb1eb1631097b3535c6a79a2658e23/frontier/B1195_close_loop_batch5a/verification/batch5a_cells.json)
- **Deepest artifacts:** [`https://github.com/originaxiom/origin-axiom/blob/9915068bdb44f88e7cca06961d15c8cd0f7d1d0a/outside_bench/certificates/e6_boundary.py`](https://github.com/originaxiom/origin-axiom/blob/9915068bdb44f88e7cca06961d15c8cd0f7d1d0a/outside_bench/certificates/e6_boundary.py)

## Domain: `lie`

<a id="oa-c0005"></a>
### OA-C0005 — `PROVED`

- **Question:** Does binary tetrahedral 2T determine the affine E6 graph and finite E6 root-system type?
- **Answer:** Yes. Classical affine McKay gives affine E6; deleting the trivial-representation node gives the finite E6 Cartan/root-system type, but not a global-group root datum.
- **Kind/domain:** `theorem` / `lie`
- **Depends on:** [OA-C0004](#oa-c0004)
- **Leads to:** [OA-C0006](#oa-c0006), [OA-C0007](#oa-c0007), [OA-C1010](#oa-c1010), [OA-C1065](#oa-c1065), [OA-C1071](#oa-c1071), [OA-C1072](#oa-c1072), [OA-C1073](#oa-c1073)
- **Closure test:** Compute tensoring by the defining two-dimensional representation and delete the affine node.
- **Falsifier:** A non-E6 McKay adjacency graph.
- **Scope:** Abstract complex type only; no gauge theory.
- **Aliases:** `McKay E6`
- **Sources:** None registered.
- **Deepest artifacts:** None registered.

<a id="oa-c0006"></a>
### OA-C0006 — `CONDITIONAL`

- **Question:** Does the object select the principal sl2 placement and charged E6 frame used downstream?
- **Answer:** Conditionally. Whitehead rigidity does not select a class. B1146 corrects a frame conflation: the principal adjoint action is center-blind and factors 2T through A4, whereas the selected minimal A1 has 40 odd adjoint weights and 12 odd weights on the 27, so the 2T center is visible there. This distinguishes the embeddings but does not select the minimal A1; B1112 still leaves a nine-element projective menu and singles A2 only after SM-compatible filtering.
- **Kind/domain:** `uniqueness` / `lie`
- **Depends on:** [OA-C0005](#oa-c0005)
- **Leads to:** [OA-C1020](#oa-c1020), [OA-C1079](#oa-c1079), [OA-C1098](#oa-c1098)
- **Closure test:** An object-native invariant distinguishing one sl2 conjugacy class without SM-target filtering.
- **Falsifier:** Several reachable projective strata or a selection criterion defined by desired SM compatibility.
- **Scope:** The repo's principal/stratum constructions.
- **Aliases:** `C6`, `principal placement`, `B854`, `B1112`
- **Sources:** None registered.
- **Deepest artifacts:** None registered.

<a id="oa-c0010"></a>
### OA-C0010 — `REFUTED`

- **Question:** Can the E8 host simultaneously supply electroweak gauge symmetry and three families?
- **Answer:** No. E8|E6xA2=(78,1)+(1,8)+(27,3)+(bar27,bar3); the one residual A2 is exactly both claimed slots. If used as EW, 3 becomes 2+1 rather than three gauge-identical families.
- **Kind/domain:** `uniqueness` / `lie`
- **Depends on:** [OA-C0005](#oa-c0005)
- **Leads to:** None.
- **Closure test:** Two independent commuting A2 resources or an alternative type-correct allocation.
- **Falsifier:** The same unique E6 commutant A2 is assigned both roles.
- **Scope:** The fixed A2^4 embedding used by B1138.
- **Aliases:** `B1138`, `relative exceptional host theorem`
- **Sources:** None registered.
- **Deepest artifacts:** None registered.

<a id="oa-c1003"></a>
### OA-C1003 — `CONDITIONAL`

- **Question:** Given a heterotic CY3 with full SU(3) holonomy and index-one standard embedding, does the McKay E6 type select the E8 x E8 gauge-lattice branch and active E8 commutant?
- **Answer:** Conditionally. McKay gives finite E6; under the explicit assumptions, E8 x E8 has active commutant E6 while Spin(32)/Z2 gives so(26)+u(1). The result is an elimination theorem, not a derivation of heterotic theory or later bundle/vacuum data.
- **Kind/domain:** `uniqueness` / `lie`
- **Depends on:** [OA-C0005](#oa-c0005), [OA-C1015](#oa-c1015)
- **Leads to:** [OA-C1004](#oa-c1004), [OA-C1006](#oa-c1006)
- **Closure test:** Prove the typed commutant comparison under the stated heterotic, full-holonomy, standard-embedding, and active-factor assumptions, including global-form and factor-label qualifications.
- **Falsifier:** A Spin(32)/Z2 candidate with the same active E6 commutant, an alternate E8 global form, or failure of one of the imposed physical hypotheses.
- **Scope:** Unlabelled active-factor root type under the stated conditional standard-embedding fiber; no node orientation, CY, bundle point, Wilson line, or vacuum selection.
- **Aliases:** `conditional McKay E8 selector`, `standard-embedding commutant`, `active E8 factor`
- **Sources:** `../tracks/MCKAY_HETEROTIC_SELECTOR_AUDIT.md`
- **Deepest artifacts:** None registered.

<a id="oa-c1009"></a>
### OA-C1009 — `PROVED`

- **Question:** Does the class-field trace/codifferent lattice determine one positive C12-equivariant E8 isomorphism class after completion?
- **Answer:** Yes. Primitive positive trace forms on O_H and its codifferent give A2^4; eight tetracode glues complete to E8, exactly four are C12-invariant, and the positive-metric C12 centralizer is transitive on those four. Thus the completed positive C12-lattice has one structured isomorphism class.
- **Kind/domain:** `theorem` / `lie`
- **Depends on:** [OA-C1000](#oa-c1000)
- **Leads to:** [OA-C1010](#oa-c1010), [OA-C1011](#oa-c1011)
- **Closure test:** Exhaust all maximal-isotropic glues and prove that the C12-invariant completions are one orbit under positive-lattice isometries commuting with C12.
- **Falsifier:** Two nonisometric positive C12-lattice completions, a completion not of E8 type, or more than one centralizer orbit.
- **Scope:** Uniqueness up to positive C12-lattice isometry, conditional only on asking for an even-unimodular positive completion; it does not derive heterotic theory or a marked gauge embedding.
- **Aliases:** `class-field E8 glue orbit`, `A2^4 tetracode completion`, `positive C12-E8 completion`
- **Sources:** `../tracks/CLASSFIELD_E8_GLUE.md`
- **Deepest artifacts:** `../experiments/verify_classfield_e8_glue.py`

<a id="oa-c1010"></a>
### OA-C1010 — `REFUTED`

- **Question:** Do the present class-field markings select one evaluation-preserving E8 glue representative and physical gauge embedding?
- **Answer:** No. The four invariant glues are the graphs of plus-or-minus (1 plus-or-minus zeta)delta. Trace evaluation leaves two two-orbits and exact delta leaves four singleton choices; moreover zeta^4 has fixed rank zero on an A2^3 complement while the McKay E6 arm rotation has fixed rank two.
- **Kind/domain:** `uniqueness` / `lie`
- **Depends on:** [OA-C0005](#oa-c0005), [OA-C1009](#oa-c1009)
- **Leads to:** None.
- **Closure test:** Derive one glue, sign, and compatible E6 or SU3 embedding while preserving every marking claimed to be physical.
- **Falsifier:** Several evaluation- or delta-marked invariant glues survive, or the class-field C3 action has the wrong fixed-space type for the McKay arm action.
- **Scope:** The stronger marked/natural-transformation claim. Its failure does not create four inequivalent unmarked E8 gauge lattices, but it blocks identifying the class-field action with the McKay or bundle embedding.
- **Aliases:** `marked E8 glue selector`, `delta-marked tetracode`, `evaluation-preserving E8 glue`
- **Sources:** `../tracks/CLASSFIELD_E8_GLUE.md`
- **Deepest artifacts:** `../experiments/verify_classfield_e8_glue.py`

<a id="oa-c1057"></a>
### OA-C1057 — `PROVED`

- **Question:** For the four accepted distinguished-nonregular E6 characteristics, do the exact triples have orbit dimensions 58, 64, 66 and 70 with parity even, odd, even and even on the 27, and do all eleven accepted odd representatives satisfy the selected-beat identities?
- **Answer:** Yes. The locked cp1_strata.py rerun is byte-identical to its stored output and gives the four dimensions 58/64/66/70 with parity even/odd/even/even. The hostile SHA-pinned extension verify_cp1_all_odd.py recomputes all accepted odd rows; all 11/11 pass relator=I, Omega^2=A27 and both intertwiners exactly. This proves compatibility for the selected rational representatives but does not prove physical fermions or select a stratum.
- **Kind/domain:** `theorem` / `lie`
- **Depends on:** [OA-C0005](#oa-c0005)
- **Leads to:** [OA-C0006](#oa-c0006), [OA-C0007](#oa-c0007), [OA-C0009](#oa-c0009), [OA-C1058](#oa-c1058), [OA-C1070](#oa-c1070)
- **Closure test:** Independently reproduce the exact sl2 witnesses, orbit dimensions and 27 spectra, then evaluate the relator, Omega square and both intertwiners on every accepted odd row.
- **Falsifier:** Failure of an exact bracket witness, dimension or parity mismatch, or failure of any selected-beat identity on one of the eleven accepted odd representatives.
- **Scope:** The 20 accepted characteristics produced by the locked outside-bench certificate and its selected rational JM witnesses. It does not by itself prove that the accepted list is exhaustive, classify all semilinear sections, or supply a four-dimensional spin/QFT functor.
- **Aliases:** `outside-bench memo 30`, `C-P1 distinguished parities`, `all-odd selected-beat extension`
- **Sources:** `../tracks/WAVE1_DELTA_ADJUDICATION.md`
- **Deepest artifacts:** `../experiments/verify_cp1_all_odd.py`

<a id="oa-c1058"></a>
### OA-C1058 — `CONDITIONAL`

- **Question:** Does the outside-bench candidate sweep independently prove that its 20 accepted E6 characteristics exhaust every nonzero nilpotent orbit and hence that exactly nine of all 20 strata are projective on the 27?
- **Answer:** Conditionally. Every accepted label has an exact positive sl2 witness, but is_characteristic makes only four seeded generic draws per label. Failed draws do not prove nonexistence. Completeness follows only after importing the standard fact that E6 has exactly 20 nonzero nilpotent orbits; the source assert len(chars)==20 uses that count as its false-negative control while calling the census literature-free.
- **Kind/domain:** `computation` / `lie`
- **Depends on:** [OA-C0005](#oa-c0005), [OA-C1057](#oa-c1057)
- **Leads to:** [OA-C0006](#oa-c0006), [OA-C1070](#oa-c1070)
- **Closure test:** Either give a deterministic algebraic nonexistence certificate for every rejected label or cite and type-check a precise classification theorem proving the exact 20-orbit upper bound used with the 20 positive witnesses.
- **Falsifier:** An additional valid characteristic missed by the four random trials, a duplicate-orbit identification among accepted labels, or a wrong external orbit count.
- **Scope:** Conditional completeness of the accepted characteristic list and the resulting 9/20 total. The four distinguished positive rows and all-odd beat identities are independently exact in OA-C1057.
- **Aliases:** `C-P1 full 20-row dictionary`, `nine projective E6 strata`, `Bala-Carter count control`
- **Sources:** `../tracks/WAVE1_DELTA_ADJUDICATION.md`
- **Deepest artifacts:** `../experiments/verify_cp1_all_odd.py`

<a id="oa-c1065"></a>
### OA-C1065 — `PROVED`

- **Question:** Is the exactly constructed E6-invariant cubic on the 27 one-dimensional up to scale and covariant under the selected semilinear beat?
- **Answer:** Yes. Two independent exact computations give a 45-dimensional weight-zero cubic ansatz, rank 44 under all E6 root equations, hence a one-dimensional invariant line. All 72 root generators and six Cartans annihilate the normalized 45-term cubic. For the fixed linearization Omega=exp(q rho(E)) o gal, exact coefficient comparison gives C(Omega v)=gal(C(v)). The scalar is not canonical under Omega -> lambda Omega: it changes by lambda^3.
- **Kind/domain:** `computation` / `lie`
- **Depends on:** [OA-C0005](#oa-c0005)
- **Leads to:** [OA-C1072](#oa-c1072), [OA-C1073](#oa-c1073)
- **Closure test:** Construct the weight-zero symmetric-cubic tensor space from the locked 27 matrices, prove the invariant nullspace is one-dimensional under all Chevalley generators, and verify the exact semilinear covariance and beat-square identities on a basis.
- **Falsifier:** Invariant dimension other than one, a failed generator equation, or one exact beat-covariance failure refutes the corresponding proposed statement.
- **Scope:** The selected 27 representation and exactly fixed beat linearization. This is an algebraic invariant theorem, not a physical Yukawa coupling or value; the covariance scalar is phase-convention dependent until that linearization is fixed.
- **Aliases:** `outside-campaign A1`, `Jordan cubic beat covariance`, `C-S2 cubic extension`
- **Sources:** [`../evidence/MAIN_B1146_B1147_DELTA_AUDIT.md`](program-question-map/evidence/MAIN_B1146_B1147_DELTA_AUDIT.md), [`../../../memos/E6_27_EXACT_INVARIANTS.md`](../memos/E6_27_EXACT_INVARIANTS.md), [`https://github.com/originaxiom/origin-axiom/blob/51e8920bc355c40589628ea7a36a4eb1c5cb352b/outside_bench/memos/JORDAN_BEAT.md`](https://github.com/originaxiom/origin-axiom/blob/51e8920bc355c40589628ea7a36a4eb1c5cb352b/outside_bench/memos/JORDAN_BEAT.md)
- **Deepest artifacts:** [`../../../certificates/r006_e6_invariants/jordan_beat.py`](../certificates/r006_e6_invariants/jordan_beat.py), [`../../../certificates/r006_e6_invariants/tensor_invariant_counts.py`](../certificates/r006_e6_invariants/tensor_invariant_counts.py)

<a id="oa-c1066"></a>
### OA-C1066 — `PROVED`

- **Question:** Does the specified rational map T act consistently on every vector of both spin-two quintuplets and the full colored sector of the banked 64-dimensional complement?
- **Answer:** Yes. The exact rational map T has rank eight on the relevant sl3 basis, intertwines the bracket on every basis pair, maps both five-level spin-two strings bijectively, and passes all 54 colored-root actions with 3 exchanged with bar3. This is the full finite-basis computation requested by the row.
- **Kind/domain:** `computation` / `lie`
- **Depends on:** [OA-C1056](#oa-c1056)
- **Leads to:** None.
- **Closure test:** Rebuild the exact 64-dimensional basis, apply T to all basis vectors, and certify the induced level-by-level quintuplet bijection and the complete color-three/color-antithree action.
- **Falsifier:** One basis vector leaving the asserted target subspace, a rank defect, or a different color or weight image refutes the advertised full-gluing statement.
- **Scope:** The locked E6 basis, selected spacetime branch and specified rational operator T. This does not construct a spacetime field or graviton.
- **Aliases:** `outside-campaign A2 rational T`, `full spacetime-64 gluing`, `spin-two and colored-sector completion`
- **Sources:** [`../evidence/MAIN_B1146_B1147_DELTA_AUDIT.md`](program-question-map/evidence/MAIN_B1146_B1147_DELTA_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/3a57fed5a9754955689ff88f3d7bfcf62c71afe6/outside_bench/memos/THE_64_GLUED.md`](https://github.com/originaxiom/origin-axiom/blob/3a57fed5a9754955689ff88f3d7bfcf62c71afe6/outside_bench/memos/THE_64_GLUED.md)
- **Deepest artifacts:** None registered.

<a id="oa-c1067"></a>
### OA-C1067 — `REFUTED`

- **Question:** Does the specified semilinear beat Sigma preserve the banked 64-dimensional complement, and what exact action does it induce on its spin-two and colored summands?
- **Answer:** No. R020 applies the principal semilinear Sigma to an exact Killing-orthogonal 64 basis in the source-locked B1140 compact-color frame. The images of the full 64, both five-dimensional spin-two strings and the colored 54 all leave the 64, so no restricted action exists. Sigma squared also leaves the 64, while the ambient identity Sigma^2=exp(ad E_principal) holds on all 78 Chevalley basis vectors. The result is selected-frame; covariance across all 24 B1140 hits is not claimed.
- **Kind/domain:** `computation` / `lie`
- **Depends on:** [OA-C1056](#oa-c1056)
- **Leads to:** None.
- **Closure test:** Apply the exact pair-field semilinear operator to a complete basis, certify preservation or mixing, decompose its action by the banked weights, and compare its square with the restricted tick action.
- **Falsifier:** A single image outside the 64-dimensional complement refutes preservation; a certified action differing from the predicted swap refutes the stronger coherence reading.
- **Scope:** One source-locked B1140 compact-color representative, its selected semilinear beat and 64-dimensional algebraic complement. Frame-covariance, physical spin, locality and QFT do not follow.
- **Aliases:** `outside-campaign A2 semilinear Sigma`, `beat on the spacetime 64`, `64-complement beat action`
- **Sources:** [`../../../memos/BEAT64_PRINCIPAL_SCOPE.md`](../memos/BEAT64_PRINCIPAL_SCOPE.md), [`../evidence/WAVE6_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE6_BRANCH_DELTA_AUDIT.md)
- **Deepest artifacts:** [`../../../certificates/r020_beat64/r020_beat64_principal.py`](../certificates/r020_beat64/r020_beat64_principal.py), [`../../../outputs/r020_beat64_principal.txt`](../outputs/r020_beat64_principal.txt)

<a id="oa-c1070"></a>
### OA-C1070 — `PROVED`

- **Question:** Is the omega-one parity clause redundant once the E6 weighted Dynkin characteristic is even, both on the accepted 20-row census and by a general lattice argument?
- **Answer:** Yes. Exact re-tabulation gives nine even/projective rows among the locked 20 and no mismatch. More generally, if a weighted-Dynkin characteristic c=A t is even and H is integral in the E6 coroot lattice, invertibility of the E6 Cartan matrix modulo 2 forces t even, hence every 27 weight, including omega1, pairs evenly. The vector c=(2,0,0,0,0,0) shows why the integral-characteristic hypothesis is necessary: t1=8/3.
- **Kind/domain:** `theorem` / `lie`
- **Depends on:** [OA-C1057](#oa-c1057), [OA-C1058](#oa-c1058)
- **Leads to:** None.
- **Closure test:** Tabulate both exact parities for every accepted characteristic and either prove the implication in the E6 root/weight lattice or exhibit a counterexample; state separately the dependence on completeness of the 20-row census.
- **Falsifier:** An even weighted-Dynkin row with odd omega-one pairing refutes redundancy; a case table without a lattice proof does not establish the proposed general lemma.
- **Scope:** The locked 20 accepted characteristics and the general implication for integral E6 coroot-lattice characteristics. Completeness of the 20-row orbit census remains separately conditional in OA-C1058; no physical stratum is selected.
- **Aliases:** `outside-campaign A5`, `omega1 parity redundancy`, `projective-menu criterion sharpening`
- **Sources:** [`../../../memos/OMEGA1_PARITY_REDUNDANCY.md`](../memos/OMEGA1_PARITY_REDUNDANCY.md), [`../evidence/MAIN_B1146_B1147_DELTA_AUDIT.md`](program-question-map/evidence/MAIN_B1146_B1147_DELTA_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/3a57fed5a9754955689ff88f3d7bfcf62c71afe6/outside_bench/memos/PARITY_LEMMA.md`](https://github.com/originaxiom/origin-axiom/blob/3a57fed5a9754955689ff88f3d7bfcf62c71afe6/outside_bench/memos/PARITY_LEMMA.md)
- **Deepest artifacts:** [`../../../certificates/oa_c1070_omega1_parity.py`](../certificates/oa_c1070_omega1_parity.py)

<a id="oa-c1071"></a>
### OA-C1071 — `REFUTED`

- **Question:** Can the square of the invariant cubic C span the degree-four invariant component of the 27 representation?
- **Answer:** No. The proposal defines C as a degree-three invariant. Its square is homogeneous of degree six, so it cannot span any degree-four subspace. The proposed degree-four cross-check is ill-typed independently of representation matrices.
- **Kind/domain:** `theorem` / `lie`
- **Depends on:** [OA-C0005](#oa-c0005)
- **Leads to:** [OA-C1072](#oa-c1072)
- **Closure test:** Respect polynomial grading and compare the degree of C squared with the claimed homogeneous component.
- **Falsifier:** A grading in which the source's C is not cubic, or an explicit degree-four equality with a homogeneous square of C, would overturn the refutation.
- **Scope:** Only the stated degree-four-equals-span-of-C-squared assertion. The corrected invariant census remains open in OA-C1072.
- **Aliases:** `outside-campaign B1 degree-four C-squared claim`, `quartic spanned by cubic square`
- **Sources:** [`../evidence/WAVE2_CAMPAIGN_INTAKE.md`](program-question-map/evidence/WAVE2_CAMPAIGN_INTAKE.md), [`https://github.com/originaxiom/origin-axiom/blob/0fe97f9070384d9a5a98c625b1b70131de2556f1/outside_bench/CAMPAIGN_CELLS.json`](https://github.com/originaxiom/origin-axiom/blob/0fe97f9070384d9a5a98c625b1b70131de2556f1/outside_bench/CAMPAIGN_CELLS.json)
- **Deepest artifacts:** [`../evidence/WAVE2_CAMPAIGN_INTAKE.md`](program-question-map/evidence/WAVE2_CAMPAIGN_INTAKE.md)

<a id="oa-c1072"></a>
### OA-C1072 — `PROVED`

- **Question:** What are the exact E6-invariant multiplicities in the homogeneous polynomial degrees one, two, three and four of the selected 27 representation?
- **Answer:** Yes. An independent exact symmetric-power calculation using the locked 27 gives invariant multiplicities in degrees 1,2,3,4 equal to 0,0,1,0. At degree three the Cartan-zero basis has dimension 45 and the 1080 exact root equations have rank 44; all 72 roots and six Cartans annihilate the resulting 45-term cubic.
- **Kind/domain:** `computation` / `lie`
- **Depends on:** [OA-C0005](#oa-c0005)
- **Leads to:** [OA-C1073](#oa-c1073)
- **Closure test:** Construct each graded symmetric-power invariant kernel using the locked representation, certify dimensions with exact rank/nullspace witnesses, and verify the cubic generator independently; do not compare different degrees.
- **Falsifier:** Any exact nonzero linear or bilinear invariant refutes the no-linear/no-bilinear expectation; any multiplicity different from the preregistered values refutes the broader census prediction.
- **Scope:** Homogeneous polynomial invariants of one selected algebraic 27. Absence of a bilinear here is not by itself absence of physical mass operators involving conjugate fields or other representations.
- **Aliases:** `corrected outside-campaign B1`, `27 invariant census degrees one through four`, `no-bilinear test`
- **Sources:** [`../../../memos/E6_27_EXACT_INVARIANTS.md`](../memos/E6_27_EXACT_INVARIANTS.md), [`../evidence/MAIN_B1146_B1147_DELTA_AUDIT.md`](program-question-map/evidence/MAIN_B1146_B1147_DELTA_AUDIT.md)
- **Deepest artifacts:** [`../../../certificates/r006_e6_invariants/jordan_beat.py`](../certificates/r006_e6_invariants/jordan_beat.py), [`../../../certificates/r006_e6_invariants/tensor_invariant_counts.py`](../certificates/r006_e6_invariants/tensor_invariant_counts.py)

<a id="oa-c1073"></a>
### OA-C1073 — `PROVED`

- **Question:** What are the exact trilinear invariant multiplicities of 27 tensor 27 tensor 27 under full E6 and under the programme's actual selected trinification subgroup?
- **Answer:** Yes. The exact ordered tensor-cube calculation gives a 270-dimensional Cartan-zero basis and rank 269 for full E6, hence one invariant. On the selected trinification A2-cubed generators the exact ranks are 261 on the ordered basis and 41 on the 45-dimensional symmetric basis, hence nine ordered and four symmetric invariant lines. The unique full-E6 line is the symmetric cubic.
- **Kind/domain:** `computation` / `lie`
- **Depends on:** [OA-C0005](#oa-c0005)
- **Leads to:** None.
- **Closure test:** Fix the actual embedded subgroup and tensor symmetry, decompose the selected 27 exactly, compute invariant Hom-space dimensions with independent character or generator checks, and distinguish the full tensor cube from its symmetric part.
- **Falsifier:** A certified full-E6 multiplicity other than the proposed one, or a trinification multiplicity different from the source prediction, settles the respective assertion negatively.
- **Scope:** Algebraic invariant multiplicity for a fixed representation and embedded subgroup. It is only an upper-level structural count, not a physical Yukawa matrix, rank or value.
- **Aliases:** `outside-campaign B2`, `trinification Yukawa multiplicity`, `27-cubed invariant count`
- **Sources:** [`../../../memos/E6_27_EXACT_INVARIANTS.md`](../memos/E6_27_EXACT_INVARIANTS.md), [`../evidence/MAIN_B1146_B1147_DELTA_AUDIT.md`](program-question-map/evidence/MAIN_B1146_B1147_DELTA_AUDIT.md)
- **Deepest artifacts:** [`../../../certificates/r006_e6_invariants/jordan_beat.py`](../certificates/r006_e6_invariants/jordan_beat.py), [`../../../certificates/r006_e6_invariants/tensor_invariant_counts.py`](../certificates/r006_e6_invariants/tensor_invariant_counts.py)

<a id="oa-c1079"></a>
### OA-C1079 — `PROVED`

- **Question:** For the selected minimal A1, is the central element of 2T visible on both the 27 and 78, in contrast with the center-blind principal-A1 adjoint action?
- **Answer:** Yes. B1146 gives 27 weights {-1:6,0:15,1:6}, so 12 states see -I, and adjoint weights {-2:1,-1:20,0:36,1:20,2:1}, so 40 states see -I. The principal adjoint restriction has only even weights and therefore factors through A4. The earlier blanket A4 statement was principal-specific.
- **Kind/domain:** `theorem` / `lie`
- **Depends on:** [OA-C0004](#oa-c0004), [OA-C0005](#oa-c0005), [OA-C1056](#oa-c1056)
- **Leads to:** [OA-C0006](#oa-c0006), [OA-C1085](#oa-c1085)
- **Closure test:** Compute the complete selected minimal-A1 weight spectra on 27 and 78 and compare central parity with the principal-A1 restriction.
- **Falsifier:** No odd selected-minimal-A1 weights on either representation, or odd principal-A1 adjoint weights, would refute the stated contrast.
- **Scope:** The two fixed internal E6 embeddings and their algebraic central actions. This neither selects the minimal A1 nor identifies its center with four-dimensional fermion parity.
- **Aliases:** `B1146`, `SEAM-B`, `minimal-A1 central visibility`, `2T versus A4 correction`
- **Sources:** [`../evidence/MAIN_B1146_B1147_DELTA_AUDIT.md`](program-question-map/evidence/MAIN_B1146_B1147_DELTA_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/tree/9d6979db424c0b878c62541a3f21e0a2ca39f274/frontier/B1146_seam_b`](https://github.com/originaxiom/origin-axiom/tree/9d6979db424c0b878c62541a3f21e0a2ca39f274/frontier/B1146_seam_b)
- **Deepest artifacts:** None registered.

<a id="oa-c1084"></a>
### OA-C1084 — `PROVED`

- **Question:** Does the supplied geometric involution preserve the 27 rather than exchange it with its dual, lie in the inner sl2-plus-sl6 involution class, and have the same adjoint trace class on all 24 enumerated hits?
- **Answer:** Yes. For the supplied rational matrix T, the full 12-generator monomial intertwiner proves 27 o T is isomorphic to 27, not bar27, and tr_78(T)=-2 identifies the cited inner involution class. Every one of the 24 enumerated hits also has trace -2.
- **Kind/domain:** `computation` / `lie`
- **Depends on:** [OA-C0005](#oa-c0005), [OA-C1066](#oa-c1066)
- **Leads to:** [OA-C1085](#oa-c1085), [OA-C1090](#oa-c1090)
- **Closure test:** Verify the exact 78-dimensional involution and bracket action, construct a full 27 intertwiner rather than a weight-only match, and enumerate the adjoint trace class on every locked hit.
- **Falsifier:** A failed 27 intertwiner, an outer-class trace, or a hit with a different trace class refutes the relevant assertion.
- **Scope:** The fixed E6 implementation and locked 24-hit enumeration. Equality of outer classes modulo inner automorphisms is not equality of real structures or a physical mirror operation.
- **Aliases:** `memo 44`, `ONE_BIT`, `common inner mirror class`
- **Sources:** [`../evidence/OUTSIDE_MEMOS_41_53_AUDIT.md`](program-question-map/evidence/OUTSIDE_MEMOS_41_53_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/6f76f95bad0cba9eeba55a6d782be3a9d3679435/outside_bench/memos/ONE_BIT.md`](https://github.com/originaxiom/origin-axiom/blob/6f76f95bad0cba9eeba55a6d782be3a9d3679435/outside_bench/memos/ONE_BIT.md)
- **Deepest artifacts:** None registered.

<a id="oa-c1085"></a>
### OA-C1085 — `PROVED`

- **Question:** Are the selected Lorentz-slot weights of the 27 and 78 all even, with their tensor algebra remaining even-weighted, while the selected minimal internal A1 retains odd weights?
- **Answer:** Yes. For the two stipulated principal A1s in orthogonal A2 slots, every recorded 27 and 78 biweight is even, and parity remains even under tensor products. The selected minimal-A1 restriction is 6 copies of the doublet plus 15 singlets, giving the exact contrasting odd sector.
- **Kind/domain:** `theorem` / `lie`
- **Depends on:** [OA-C1056](#oa-c1056), [OA-C1079](#oa-c1079), [OA-C1084](#oa-c1084)
- **Leads to:** [OA-C1086](#oa-c1086)
- **Closure test:** Compute both joint weight multisets exactly and prove tensor-parity closure, while checking the contrasting minimal-A1 restriction.
- **Falsifier:** An odd Lorentz-slot weight in the claimed modules or tensor tower, or absence of the minimal-A1 odd sector, refutes the contrast.
- **Scope:** Internal complex-Lie representation weights. The labels 'Lorentz' and 'spinor' do not construct Spin(3,1), a tangent spin bundle, spin statistics or a four-dimensional Dirac field.
- **Aliases:** `memo 45`, `ONLY_SPINOR`, `integer-spin representation no-go`
- **Sources:** [`../evidence/OUTSIDE_MEMOS_41_53_AUDIT.md`](program-question-map/evidence/OUTSIDE_MEMOS_41_53_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/522c04a1da83a26cccfe848fafde8a1ee1199952/outside_bench/memos/ONLY_SPINOR.md`](https://github.com/originaxiom/origin-axiom/blob/522c04a1da83a26cccfe848fafde8a1ee1199952/outside_bench/memos/ONLY_SPINOR.md)
- **Deepest artifacts:** None registered.

<a id="oa-c1086"></a>
### OA-C1086 — `PROVED`

- **Question:** Does the specified Psi=C2 tensor 27 form a 54-dimensional semilinear pi1-module with the claimed relator, beat-square, 24/30 lock split, Jordan-depth parity and longitude-lock identities?
- **Answer:** Yes. All exact matrix checks pass for the chosen module. The meridian has Jordan type 6J3+15J2+6J1; the relative central operator has a 24-dimensional positive sector and 30-dimensional negative sector; beat and depth preserve the blocks, the longitude semisimple part equals the lock, and the joint cusp-fixed space has dimension 12. Wave 5 further identifies that lock with the image of central -I in the diagonal SL2 closure while finding a 297-dimensional linear commutant, so its distinction is group realization rather than uniqueness among commuting involutions. The beat is identity on the six-dimensional deepest graded layer, longitude-fixed equals joint-cusp-fixed, and OA-C1111 records the D5 class refinement.
- **Kind/domain:** `computation` / `lie`
- **Depends on:** [OA-C1056](#oa-c1056), [OA-C1068](#oa-c1068), [OA-C1085](#oa-c1085)
- **Leads to:** [OA-C1087](#oa-c1087), [OA-C1088](#oa-c1088), [OA-C1090](#oa-c1090), [OA-C1111](#oa-c1111), [OA-C1113](#oa-c1113), [OA-C1117](#oa-c1117), [OA-C1120](#oa-c1120)
- **Closure test:** Verify the complete 54 by 54 relator and beat intertwinings, the 24/30 central split, meridian Jordan type, depth parity, longitude factorization and joint cusp-fixed dimension.
- **Falsifier:** A relator or beat failure, lock leakage, wrong Jordan type, failed longitude factorization or incorrect fixed-space dimension refutes the corresponding identity.
- **Scope:** The fixed pair-field module and peripheral matrices. 'Matter', 'clock', 'lock' and 'fermion-shaped' are interpretations; no field, propagation, Dirac operator, chirality or physical spectrum is constructed.
- **Aliases:** `memos 46 and 49-52`, `THE_CARRIER`, `carrier lock-clock-longitude`
- **Sources:** [`../evidence/OUTSIDE_MEMOS_41_53_AUDIT.md`](program-question-map/evidence/OUTSIDE_MEMOS_41_53_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/5b387bcc8d98009b12760626dc28c767a2d21e7b/outside_bench/memos/THE_CARRIER.md`](https://github.com/originaxiom/origin-axiom/blob/5b387bcc8d98009b12760626dc28c767a2d21e7b/outside_bench/memos/THE_CARRIER.md), [`https://github.com/originaxiom/origin-axiom/blob/20587ce67aec67fd3b17840b51b0a7a1b175b025/outside_bench/memos/YUKAWA_READS_THE_CLOCK.md`](https://github.com/originaxiom/origin-axiom/blob/20587ce67aec67fd3b17840b51b0a7a1b175b025/outside_bench/memos/YUKAWA_READS_THE_CLOCK.md)
- **Deepest artifacts:** None registered.

<a id="oa-c1087"></a>
### OA-C1087 — `REFUTED`

- **Question:** Is Psi=C2 tensor 27 canonically selected or unique-minimal under the algebraic requirements actually stated by the carrier construction?
- **Answer:** No. The holonomy C2 alone is already a smaller spinorial pi1-module satisfying the beat relation. If a nontrivial internal 27 is imposed, all eleven accepted odd A1 strata pass the selected-beat identities, so the minimal-A1 factor is not source-selected. OA-C1116 proves a narrower positive theorem after adding the category 'C2 tensor a nontrivial irreducible E6 module': dimension 54 is then minimal up to 27/dual-27. That extra category does not restore object-native canonical selection.
- **Kind/domain:** `uniqueness` / `lie`
- **Depends on:** [OA-C1057](#oa-c1057), [OA-C1086](#oa-c1086)
- **Leads to:** [OA-C1116](#oa-c1116)
- **Closure test:** Define the admissible carrier category and minimization order, then prove every admissible object is isomorphic to the proposed 54-dimensional module.
- **Falsifier:** A smaller admissible module or an inequivalent equally compatible internal stratum refutes uniqueness under the stated conditions.
- **Scope:** The algebraic conditions stated in memo 46. A future physical functor could impose additional requirements, but those would be new inputs.
- **Aliases:** `memo 46 unique-minimal carrier`, `canonical carrier claim`
- **Sources:** [`../evidence/OUTSIDE_MEMOS_41_53_AUDIT.md`](program-question-map/evidence/OUTSIDE_MEMOS_41_53_AUDIT.md)
- **Deepest artifacts:** None registered.

<a id="oa-c1088"></a>
### OA-C1088 — `PROVED`

- **Question:** For the fixed carrier, does the symmetry-restricted invariant chain 6615 to 4 to 1 leave Y=epsilon tensor C as a unique algebraic coupling with exactly the certified meridian-depth support pattern?
- **Answer:** Yes. The seven certificates for memos 47-53 rerun byte-identically. Conditional on the hard-coded SL2, E6 27 and bridge, the relevant invariant line is generated by epsilon_C2 tensor C_E6. The reported 6615 to 4 to 1 count and seven allowed versus eleven forbidden support blocks are exact representation-theory results.
- **Kind/domain:** `computation` / `lie`
- **Depends on:** [OA-C1065](#oa-c1065), [OA-C1073](#oa-c1073), [OA-C1086](#oa-c1086)
- **Leads to:** [OA-C1089](#oa-c1089), [OA-C0015](#oa-c0015)
- **Closure test:** Compute all three invariant-space dimensions on the fixed modules and verify symmetry, beat covariance and every allowed/forbidden chain-depth block exactly.
- **Falsifier:** A different invariant dimension, failed covariance, nonzero forbidden block or zero required block refutes the corresponding claim.
- **Scope:** Finite-dimensional invariant tensors and support rules. There is no compactification, zero-mode space, cohomological cup product, Calabi-Yau trace, matter metric, physical Yukawa value, mass or mixing matrix.
- **Aliases:** `memos 47,48,52`, `YUKAWA_ON_CARRIER`, `UNIQUENESS_CHAIN`, `YUKAWA_READS_THE_CLOCK`
- **Sources:** [`../evidence/OUTSIDE_MEMOS_41_53_AUDIT.md`](program-question-map/evidence/OUTSIDE_MEMOS_41_53_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/7e89344a2c14d42fdcbf0f379ebecd9e05bc684e/outside_bench/memos/YUKAWA_ON_CARRIER.md`](https://github.com/originaxiom/origin-axiom/blob/7e89344a2c14d42fdcbf0f379ebecd9e05bc684e/outside_bench/memos/YUKAWA_ON_CARRIER.md), [`https://github.com/originaxiom/origin-axiom/blob/20587ce67aec67fd3b17840b51b0a7a1b175b025/outside_bench/memos/YUKAWA_READS_THE_CLOCK.md`](https://github.com/originaxiom/origin-axiom/blob/20587ce67aec67fd3b17840b51b0a7a1b175b025/outside_bench/memos/YUKAWA_READS_THE_CLOCK.md)
- **Deepest artifacts:** None registered.

<a id="oa-c1089"></a>
### OA-C1089 — `PROVED`

- **Question:** In the fixed A2^4-in-E8 possibility-space embedding, does the selected family-channel trilinear factor as epsilon_family tensor C_Jordan with no same-family support?
- **Answer:** Yes. For the chosen A2^4 embedding, the exact Chevalley bracket/Killing trilinear on the selected (3,27) block has 270 zero-sum triples, uses all three family labels and factorizes after the stated sign gauge as epsilon_family tensor C_Jordan. OA-C1128 adds the exact rank-two family-matrix consequence in the same observer-paid possibility space. The certificates do not derive the E8 host, identify these labels with zero modes, or produce physical mass matrices.
- **Kind/domain:** `computation` / `lie`
- **Depends on:** [OA-C0005](#oa-c0005), [OA-C0010](#oa-c0010), [OA-C1073](#oa-c1073), [OA-C1088](#oa-c1088)
- **Leads to:** [OA-C0008](#oa-c0008), [OA-C0015](#oa-c0015), [OA-C1128](#oa-c1128)
- **Closure test:** Rebuild the selected E8 root decomposition, enumerate the support triples, verify full-generator invariance and antisymmetry, and certify the sign-gauged factorization.
- **Falsifier:** A same-family support triple, failed invariance or factorization, or non-unique selected family invariant refutes the row.
- **Scope:** The fixed E8 possibility-space embedding and basis/sign convention. E8 is not object-paid, and the external A2 triplet is not three massless chiral generations or a physical Yukawa matrix.
- **Aliases:** `memo 53`, `FAMILY_YUKAWA`, `E8 family-channel tensor`
- **Sources:** [`../evidence/OUTSIDE_MEMOS_41_53_AUDIT.md`](program-question-map/evidence/OUTSIDE_MEMOS_41_53_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/0fcdb66cd57edeb13c8703b7f05717fcc2609893/outside_bench/memos/FAMILY_YUKAWA.md`](https://github.com/originaxiom/origin-axiom/blob/0fcdb66cd57edeb13c8703b7f05717fcc2609893/outside_bench/memos/FAMILY_YUKAWA.md)
- **Deepest artifacts:** None registered.

<a id="oa-c1098"></a>
### OA-C1098 — `PROVED`

- **Question:** Given the specified principal-2T embedding, is its four-dimensional fixed algebra toral and is its complete characteristic-zero centralizer-dimension spectrum exactly the eleven values obtained from the 109-flat A2-perpendicular arrangement?
- **Answer:** Yes. The fixed algebra C is abelian of dimension four with dim z(C)=12. Finite-group fixed algebras in characteristic zero are reductive, so C is toral. Its six zero roots form A2; all 120 A2 subsystems are one explicitly enumerated Weyl orbit. The rational A2-perpendicular arrangement has 30 nonzero weights with profile 12x1+18x3, exactly 109 flats, and spectrum {12,14,16,18,20,26,28,30,36,46,78}. Rational dependence is unchanged over Qbar.
- **Kind/domain:** `theorem` / `lie`
- **Depends on:** [OA-C0006](#oa-c0006)
- **Leads to:** [OA-C1099](#oa-c1099)
- **Closure test:** Prove torality, identify the six zero roots as one A2 subsystem, prove all E6 A2 subsystems Weyl-conjugate, and enumerate the resulting rational flat lattice exactly.
- **Falsifier:** A nonsemisimple fixed algebra, another A2 Weyl orbit, a characteristic-zero dependency missed by the rational enumeration, or an additional centralizer dimension refutes the chain.
- **Scope:** The explicitly specified principal-2T placement in complex E6. OA-C0006 remains conditional because the object has not selected that placement; the dimensions are not gauge groups, fields or particles.
- **Aliases:** `Paper II Qbar closure`, `toral A2 transfer`, `109-flat rung spectrum`, `R013`
- **Sources:** [`../../../memos/PAPER2_RUNG_TRANSFER.md`](../memos/PAPER2_RUNG_TRANSFER.md), [`../evidence/WAVE4_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE4_BRANCH_DELTA_AUDIT.md)
- **Deepest artifacts:** [`../../../certificates/r013_rung_transfer.py`](../certificates/r013_rung_transfer.py)

<a id="oa-c1099"></a>
### OA-C1099 — `PROVED`

- **Question:** On the specified charge-coordinate (x8,x16) plane, does the centralizer jump from 30 to 46 exactly on an irreducible rational cubic whose generated cubic field is Q[u]/(u^3-12u-5)?
- **Answer:** Yes. For Q=ad(x16)^(-1)ad(x8) on the 48-dimensional image, the characteristic polynomial is one irreducible cubic to the sixteenth power. The exponent derives the jump 46-30=16. Its discriminant has squarefree part 77 and it acquires a root in K=Q[u]/(u^3-12u-5), identifying the generated field. Rational directions therefore remain at 30 while the cubic directions attain 46 after base change.
- **Kind/domain:** `computation` / `lie`
- **Depends on:** [OA-C1098](#oa-c1098)
- **Leads to:** [OA-C1162](#oa-c1162), [OA-C1163](#oa-c1163)
- **Closure test:** Restrict both commuting adjoint matrices to the relevant image, factor the exact characteristic polynomial, prove the cubic irreducible, derive the multiplicity sixteen, and identify its field.
- **Falsifier:** A rational root, a different jump multiplicity, a nonisomorphic cubic field, or another exceptional direction outside the cubic locus refutes the scoped classification.
- **Scope:** The fixed charge basis and distinguished two-plane. It is an arithmetic centralizer enhancement, not a selected physical scale or particle threshold.
- **Aliases:** `Paper II distinguished cubic`, `30-to-46 enhancement`, `B8078 plane`
- **Sources:** [`../evidence/WAVE4_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE4_BRANCH_DELTA_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/61a243c65f1a84c700e3c3d9755b11c30a5f0699/papers/series/paper2_rung_spectrum/main.tex`](https://github.com/originaxiom/origin-axiom/blob/61a243c65f1a84c700e3c3d9755b11c30a5f0699/papers/series/paper2_rung_spectrum/main.tex)
- **Deepest artifacts:** [`https://github.com/originaxiom/origin-axiom/blob/61a243c65f1a84c700e3c3d9755b11c30a5f0699/papers/series/paper2_rung_spectrum/verify/rung_attained.py`](https://github.com/originaxiom/origin-axiom/blob/61a243c65f1a84c700e3c3d9755b11c30a5f0699/papers/series/paper2_rung_spectrum/verify/rung_attained.py)

<a id="oa-c1100"></a>
### OA-C1100 — `PROVED`

- **Question:** In the fixed D5 x U(1)_psi frame, does the E6 cubic have only the 40 (16,16,10) and 5 (10,10,1) supports with conserved frame parity, while the selected beat mixes that grading on exactly 6 of 27 basis states but preserves the tested lock?
- **Answer:** Yes. Exact E6 arithmetic gives 27=16_1+10_-2+1_4 and 45 cubic supports split as 40 (16,16,10) plus 5 (10,10,1), all conserving (-1)^q. The separately selected bridge grading differs. The beat mixes family class and parity on 6 of 27 basis columns, leaves 21 unmixed, and preserves the tested lock. OA-C1111--OA-C1113 add the exact clock census, anomaly sums and direction-level parity/lock fork; OA-C1125 exhausts the selected Z2 grading space and surviving psi torus, while OA-C1127 resolves the measured-hypercharge support labels. None turns the fixed frame into a physical dark sector or vacuum.
- **Kind/domain:** `computation` / `lie`
- **Depends on:** [OA-C0014](#oa-c0014), [OA-C1087](#oa-c1087)
- **Leads to:** [OA-C1111](#oa-c1111), [OA-C1112](#oa-c1112), [OA-C1113](#oa-c1113), [OA-C1117](#oa-c1117), [OA-C1119](#oa-c1119), [OA-C1125](#oa-c1125), [OA-C1127](#oa-c1127)
- **Closure test:** Rebuild the 27 branching and normalized cubic, classify every nonzero support, compare the two gradings, and apply the selected beat to all basis columns with a lock-preservation control.
- **Falsifier:** An additional cubic support type, parity violation, a different beat-mixing count, or leakage across the tested lock refutes the relevant assertion.
- **Scope:** Two explicitly selected internal frames and two tested Z2 gradings. The word portal denotes support only; no full-action symmetry, stable dark particle, mass, abundance or phenomenology follows, and no exhaustive uniqueness among all Z2 gradings is claimed.
- **Aliases:** `Memo 56 dark ledger`, `fixed D5 cubic hypergraph`, `beat-unstable matter parity`, `R012`
- **Sources:** [`../../../memos/DARK_LEDGER_SCOPE_AUDIT.md`](../memos/DARK_LEDGER_SCOPE_AUDIT.md), [`../evidence/WAVE4_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE4_BRANCH_DELTA_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/59680460721a0b9e4f672ad6e997724c226ceb56/outside_bench/memos/DARK_LEDGER.md`](https://github.com/originaxiom/origin-axiom/blob/59680460721a0b9e4f672ad6e997724c226ceb56/outside_bench/memos/DARK_LEDGER.md)
- **Deepest artifacts:** [`../../../certificates/r012_dark_ledger_scope.py`](../certificates/r012_dark_ledger_scope.py)

<a id="oa-c1111"></a>
### OA-C1111 — `PROVED`

- **Question:** In the fixed D5 x U(1)_psi frame on Psi=C^2 tensor 27, does the meridian clock have only the stated 16-to-10 and 1-to-16 transitions with the certified six-chain and cusp-fixed class census?
- **Answer:** Yes. The bundled exact computation finds five chains with 16 bottoms and 10 tops plus one with singlet bottom and 16 top; carrier class sizes are 32/20/2 and locked counts 12/10/2. The joint cusp-fixed class projection/intersection pairs are 16:(7,1), 10:(10,5), 1:(1,0).
- **Kind/domain:** `computation` / `lie`
- **Depends on:** [OA-C1086](#oa-c1086), [OA-C1100](#oa-c1100)
- **Leads to:** [OA-C1112](#oa-c1112), [OA-C1113](#oa-c1113)
- **Closure test:** Rebuild the carrier and D5 branching, classify every nonzero clock transition, and certify the chain ranks, class sizes, locked counts and classwise cusp-fixed projections.
- **Falsifier:** An additional transition type or any different exact rank, class count or fixed-space intersection refutes the corresponding census.
- **Scope:** The selected carrier and observer-paid D5 frame. The class table was measured rather than preregistered, and labels such as family or dark do not establish physical fields, masses, stability or abundance.
- **Aliases:** `outside memo 57`, `FAMILY_ESCALATOR`, `carrier D5 chain census`
- **Sources:** [`../evidence/WAVE5_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE5_BRANCH_DELTA_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/10848a98f3338c75c7c7f1538aac6e6c6cd7e7f9/outside_bench/memos/FAMILY_ESCALATOR.md`](https://github.com/originaxiom/origin-axiom/blob/10848a98f3338c75c7c7f1538aac6e6c6cd7e7f9/outside_bench/memos/FAMILY_ESCALATOR.md)
- **Deepest artifacts:** [`https://github.com/originaxiom/origin-axiom/blob/10848a98f3338c75c7c7f1538aac6e6c6cd7e7f9/outside_bench/certificates/dark_carrier.py`](https://github.com/originaxiom/origin-axiom/blob/10848a98f3338c75c7c7f1538aac6e6c6cd7e7f9/outside_bench/certificates/dark_carrier.py)

<a id="oa-c1112"></a>
### OA-C1112 — `PROVED`

- **Question:** For the fixed branching 27=16_(+1)+10_(-2)+1_(+4), do the gravitational-U(1), cubic-U(1) and SO(10)^2-U(1) anomaly coefficients cancel exactly, with 10+1 carrying the negative of the 16 contribution?
- **Answer:** Yes. Exact integer arithmetic gives sum dim*q=0, sum dim*q^3=0 and sum T*q=0 with T(16)=2 and T(10)=1. The 16 alone contributes 16 in the first two channels; 10+1 contributes -16. Main independently reproduces these sums.
- **Kind/domain:** `computation` / `lie`
- **Depends on:** [OA-C1100](#oa-c1100), [OA-C1111](#oa-c1111)
- **Leads to:** [OA-C0014](#oa-c0014), [OA-C1118](#oa-c1118)
- **Closure test:** Compute all three standard anomaly sums with declared dimensions, charges and Dynkin-index normalization, and verify the blockwise cancellation.
- **Falsifier:** One nonzero full-27 anomaly sum or a dark-block contribution not equal to minus the 16 contribution refutes the identity.
- **Scope:** A representation-theoretic identity in a fixed observer-paid D5 x U(1)_psi frame. The U(1) is not object-selected or proved physically gauged, so 'dark block required' is conditional and this is not a complete SM anomaly calculation.
- **Aliases:** `outside memo 58`, `ANOMALY_PAYMENT`, `D5 U(1)_psi anomaly identity`
- **Sources:** [`../evidence/WAVE5_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE5_BRANCH_DELTA_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/c54ae43328e38947241b3be33d11557d530db3bc/frontier/B1158_cloud_wave2_harvest/FINDINGS.md`](https://github.com/originaxiom/origin-axiom/blob/c54ae43328e38947241b3be33d11557d530db3bc/frontier/B1158_cloud_wave2_harvest/FINDINGS.md), [`https://github.com/originaxiom/origin-axiom/blob/10848a98f3338c75c7c7f1538aac6e6c6cd7e7f9/outside_bench/memos/ANOMALY_PAYMENT.md`](https://github.com/originaxiom/origin-axiom/blob/10848a98f3338c75c7c7f1538aac6e6c6cd7e7f9/outside_bench/memos/ANOMALY_PAYMENT.md)
- **Deepest artifacts:** None registered.

<a id="oa-c1116"></a>
### OA-C1116 — `PROVED`

- **Question:** Within the declared category {C^2 tensor V: V a nontrivial irreducible complex E6 module}, is the 54-dimensional carrier minimal up to the 27-versus-dual-27 tie?
- **Answer:** Yes. Exact Weyl arithmetic enumerates all 84 dominant labels with coefficient sum at most three; every nontrivial dimension is at least 27 and equality occurs only at the two minuscule fundamentals. Standard dominance monotonicity extends the bound to all dominant weights, so tensoring by C^2 gives minimum 54 up to duality.
- **Kind/domain:** `theorem` / `lie`
- **Depends on:** [OA-C1087](#oa-c1087)
- **Leads to:** None.
- **Closure test:** Apply the exact Weyl dimension formula to every fundamental minimum and prove monotonicity for arbitrary nonzero dominant weights, keeping the dual minimum explicit.
- **Falsifier:** A nontrivial irreducible E6 module of dimension below 27 or a third inequivalent dimension-27 minimum refutes the category theorem.
- **Scope:** Only the explicitly declared representation category. Requiring a nontrivial internal irreducible factor is a modelling input; the object still does not select the 27, its dual, or the odd A1 stratum, so OA-C1087 remains refuted.
- **Aliases:** `outside memo 66`, `MINIMAL_FACTOR`, `category-restricted carrier minimality`
- **Sources:** [`../evidence/WAVE5_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE5_BRANCH_DELTA_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/10848a98f3338c75c7c7f1538aac6e6c6cd7e7f9/outside_bench/memos/MINIMAL_FACTOR.md`](https://github.com/originaxiom/origin-axiom/blob/10848a98f3338c75c7c7f1538aac6e6c6cd7e7f9/outside_bench/memos/MINIMAL_FACTOR.md)
- **Deepest artifacts:** [`https://github.com/originaxiom/origin-axiom/blob/10848a98f3338c75c7c7f1538aac6e6c6cd7e7f9/outside_bench/certificates/minimal_factor.py`](https://github.com/originaxiom/origin-axiom/blob/10848a98f3338c75c7c7f1538aac6e6c6cd7e7f9/outside_bench/certificates/minimal_factor.py)

## Domain: `physics_interface`

<a id="oa-c1056"></a>
### OA-C1056 — `PROVED`

- **Question:** For the specified m004 holonomy, Gieseking beat section and selected A1 embedding, does exactly one checked sign-lift admit the semilinear beat relation and does the 27 restrict as six doublets plus fifteen singlets?
- **Answer:** Yes. At Golden commit 4a1e4cc3 all 46 top-level certificates independently exit zero. spin_payment proves the fixed-beat sign-target dimensions {(+,+):1, others:0}; sp2_seat proves weights 6(-1)+15(0)+6(+1), nontrivial central parity, relator +I and the three beat identities on the selected A1 module. Local B1145 at 9a4eca7e independently rebuilds the E6/27 matrices from banked B1102 machinery, verifies all 3003 brackets and reproduces the same identities; its five fast locks pass. B8132 shows that the count of two spin structures is shared by several family members. The ten-word inner-modification block is not exhaustive, no typed tangent-frame Pin/spin lift or four-dimensional spin/QFT/index is constructed, and the result does not establish physical fermions or generations.
- **Kind/domain:** `theorem` / `physics_interface`
- **Depends on:** None.
- **Leads to:** [OA-C0007](#oa-c0007), [OA-C0008](#oa-c0008), [OA-C0009](#oa-c0009), [OA-C0014](#oa-c0014), [OA-C1066](#oa-c1066), [OA-C1067](#oa-c1067), [OA-C1069](#oa-c1069)
- **Closure test:** Independently rerun the self-contained certificates, verify the sign-lift/intertwiner and module identities, and separate them from uncomputed Pin, four-dimensional spinor, index and generation assertions.
- **Falsifier:** Failure of any exact certificate identity at the locked commit, a second fixed sign-target intertwiner, or a mismatch in the A1 weight multiset would refute the narrow theorem; a genuine Pin/Dirac-index construction would close a downstream physics gate rather than this algebraic item.
- **Scope:** The fixed matrix holonomy and beat section and the explicitly selected ROOTS[0] A1 embedding. It is a semilinear holonomy/module theorem, not a Pin, fermion, chirality, family or Standard-Model theorem.
- **Aliases:** `Golden SP-2 close-out`, `Gieseking beat lift on the A1 27`, `cloud-seat memos 28--29 audit`
- **Sources:** `../tracks/GOLDEN_CLOUDSEAT_CLOSEOUT_AUDIT.md`, `../tracks/WAVE1_DELTA_ADJUDICATION.md`, `../inventory/SOURCE_LOCK.md`
- **Deepest artifacts:** `../tracks/GOLDEN_CLOUDSEAT_CLOSEOUT_AUDIT.md`, `../tracks/WAVE1_DELTA_ADJUDICATION.md`

<a id="oa-c1069"></a>
### OA-C1069 — `PROVED`

- **Question:** Does the Gieseking manifold admit the proposed Pin-minus structures, and what is their exact restriction map to spin structures on its orientable double cover m004?
- **Answer:** Yes. R021 gives H1(N;Z)=Z<t> with a=b=2t, H1(M;Z)=Z<a=b>, H^2(N;F2)=0 and hence vanishing Pin-minus obstruction in the stated convention. Both Pin-minus and spin torsors have two elements, while p^*:H^1(N;F2)->H^1(M;F2) is zero, so affine restriction is constant onto one deliberately unnamed spin structure. Naming that image is separated as OA-C1140.
- **Kind/domain:** `computation` / `physics_interface`
- **Depends on:** [OA-C1056](#oa-c1056)
- **Leads to:** [OA-C1140](#oa-c1140)
- **Closure test:** Verify the relevant Pin-minus obstruction, compute the integral and mod-two homology from a checked group/cellular presentation, construct the covering restriction map, and identify the restricted spin torsor elements without choosing an unproved affine origin.
- **Falsifier:** A nonzero Pin-minus obstruction, a different torsor rank, or a nonzero restriction linear part refutes the source prediction; ambiguity of affine origins blocks the stronger identification claim.
- **Scope:** Pin-minus structures on the nonorientable Gieseking three-manifold and their restriction to the orientable cover. This alone is not a four-dimensional fermion construction.
- **Aliases:** `outside-campaign A4`, `Gieseking Pin-minus torsor`, `Pin-to-spin restriction`
- **Sources:** [`../../../memos/GIESEKING_PINMINUS_RESTRICTION.md`](../memos/GIESEKING_PINMINUS_RESTRICTION.md), [`../evidence/WAVE6_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE6_BRANCH_DELTA_AUDIT.md)
- **Deepest artifacts:** [`../../../certificates/r021_gieseking_pinminus/gieseking_pinminus_restriction.py`](../certificates/r021_gieseking_pinminus/gieseking_pinminus_restriction.py), [`../../../outputs/r021_gieseking_pinminus.txt`](../outputs/r021_gieseking_pinminus.txt)

<a id="oa-c1090"></a>
### OA-C1090 — `REFUTED`

- **Question:** Does the present beat construction define an involutive antiunitary real structure on the carrier Hilbert space?
- **Answer:** No. The exact operation is Galois-semilinear and its square is the nontrivial unipotent meridian, not the identity. A nontrivial unipotent matrix cannot be unitary for a positive-definite Hermitian form because it is not diagonalizable. No positive metric is constructed. Thus semilinearity is proved but antiunitarity and an involutive real structure are not.
- **Kind/domain:** `theorem` / `physics_interface`
- **Depends on:** [OA-C1084](#oa-c1084), [OA-C1086](#oa-c1086)
- **Leads to:** [OA-C0007](#oa-c0007)
- **Closure test:** Construct a positive-definite Hermitian form preserved antiunitarily by the beat and prove that its square is the identity real structure on the physical carrier.
- **Falsifier:** A nontrivial nonunitarizable square or absence of any selected positive Hermitian form refutes the typed claim.
- **Scope:** The current finite-dimensional carrier matrices. This does not rule out a future indefinite form or a different physical completion, neither of which would establish the claimed antiunitary Hilbert-space structure as written.
- **Aliases:** `memo 44 antiunitary claim`, `carrier real-structure claim`
- **Sources:** [`../evidence/OUTSIDE_MEMOS_41_53_AUDIT.md`](program-question-map/evidence/OUTSIDE_MEMOS_41_53_AUDIT.md)
- **Deepest artifacts:** None registered.

<a id="oa-c1117"></a>
### OA-C1117 — `OPEN`

- **Question:** Can the conditional heterotic witness's Wilson Z2, bundle parities and Higgs directions be placed in a common typed representation with the carrier lock, beat, clock and longitude, and if so do they preserve those operators?
- **Answer:** Open. Outside tip 60bcf01d labels D1 paid, but its alignment_audit.py checks anomaly identities, dimensions and a stack hash; it loads no Wilson, bundle, Higgs, lock, beat, clock or longitude matrices and constructs no intertwiner. R017 versions the up-Yukawa proof but not this comparison. The declared closure criterion therefore remains unmet despite the semantic five-line alignment table.
- **Kind/domain:** `computation` / `physics_interface`
- **Depends on:** [OA-C1002](#oa-c1002), [OA-C1006](#oa-c1006), [OA-C1086](#oa-c1086), [OA-C1100](#oa-c1100)
- **Leads to:** [OA-C0014](#oa-c0014), [OA-C0015](#oa-c0015)
- **Closure test:** Version the witness's discrete matrices, construct an explicit common comparison/intertwiner, and test every claimed commutator, covariance relation and Higgs-direction eigenvalue with exact controls.
- **Falsifier:** A type obstruction to any common representation, one nonzero forbidden commutator, or one Higgs direction violating a claimed preservation law refutes alignment; exact full alignment would close the scoped test.
- **Scope:** The one conditional BCDD/class-field witness and the fixed carrier operators. Alignment would be a discrete structural fact, not derivation of the heterotic functor, physical fields, a vacuum or parameter values.
- **Aliases:** `THE_MSSM_DEBT D1`, `heterotic-carrier alignment audit`
- **Sources:** [`../evidence/WAVE5_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE5_BRANCH_DELTA_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/60bcf01db966ae0b13f18c73c24845040b59fd98/outside_bench/THE_MSSM_DEBT.md`](https://github.com/originaxiom/origin-axiom/blob/60bcf01db966ae0b13f18c73c24845040b59fd98/outside_bench/THE_MSSM_DEBT.md), [`https://github.com/originaxiom/origin-axiom/blob/60bcf01db966ae0b13f18c73c24845040b59fd98/outside_bench/certificates/alignment_audit.py`](https://github.com/originaxiom/origin-axiom/blob/60bcf01db966ae0b13f18c73c24845040b59fd98/outside_bench/certificates/alignment_audit.py), [`../../../memos/YUKAWA_PRIMARY_PROVENANCE.md`](../memos/YUKAWA_PRIMARY_PROVENANCE.md)
- **Deepest artifacts:** None registered.

<a id="oa-c1120"></a>
### OA-C1120 — `REFUTED`

- **Question:** Does the fixed carrier admit a precisely graded odd operator Q satisfying the proposed Q^2=rho(meridian) relation and declared covariance conditions?
- **Answer:** No. The independently rerun finite search finds no odd Q in either declared natural covariance class. Under pi1-equivariance, locked and unlocked irreducible spectra are disjoint, so no odd intertwiner exists. Under E6/gauge-equivariance, the commutant is gl2 tensor I27 and no such odd operator squares to the prescribed A2 tensor A27. The selected beat is even and semilinear, not the missing Q.
- **Kind/domain:** `computation` / `physics_interface`
- **Depends on:** [OA-C1086](#oa-c1086), [OA-C1090](#oa-c1090)
- **Leads to:** [OA-C0017](#oa-c0017)
- **Closure test:** Define the Z2 grading and admissible operator space, solve Q^2=rho(meridian) with every required covariance/intertwining relation, quotient equivalences and certify existence or nonexistence exactly.
- **Falsifier:** An exact nonexistence proof in the declared operator space refutes the candidate; any proposed solution failing its square, grading or covariance relation is invalid.
- **Scope:** A finite-dimensional algebraic square-root/covariance no-go in the two declared carrier operator spaces. It is not a no-go theorem for super-Poincare symmetry, spacetime supersymmetry, spin statistics or physical supermultiplets.
- **Aliases:** `THE_MSSM_DEBT D5`, `carrier odd-square test`, `algebraic SUSY candidate`
- **Sources:** [`../evidence/WAVE5_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE5_BRANCH_DELTA_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/60bcf01db966ae0b13f18c73c24845040b59fd98/outside_bench/memos/SUSY_NO_GO.md`](https://github.com/originaxiom/origin-axiom/blob/60bcf01db966ae0b13f18c73c24845040b59fd98/outside_bench/memos/SUSY_NO_GO.md)
- **Deepest artifacts:** [`https://github.com/originaxiom/origin-axiom/blob/60bcf01db966ae0b13f18c73c24845040b59fd98/outside_bench/certificates/susy_test.py`](https://github.com/originaxiom/origin-axiom/blob/60bcf01db966ae0b13f18c73c24845040b59fd98/outside_bench/certificates/susy_test.py)

<a id="oa-c1140"></a>
### OA-C1140 — `OPEN`

- **Question:** Is the unnamed spin structure in the constant Gieseking Pin-minus restriction image exactly the B1141 beat-selected holonomy sign lift?
- **Answer:** Open. R021 proves that both Pin-minus structures restrict to one spin structure but the zero linear map cannot name the affine image. Deck generator t, tangent Pin data, the internal 2T center and semilinear holonomy are distinct objects. No explicit frame-lift comparison to B1141 exists.
- **Kind/domain:** `comparison` / `physics_interface`
- **Depends on:** [OA-C1069](#oa-c1069)
- **Leads to:** None.
- **Closure test:** Construct an explicit tangent-frame Pin-minus lift on m000, restrict it to a Spin(3) lift on m004, compare both named hyperbolic-holonomy lifts in one convention and identify the affine origin.
- **Falsifier:** Restriction to the opposite named holonomy lift refutes the proposed identification; absence of a typed tangent-to-holonomy comparison withholds it.
- **Scope:** A named comparison between a three-dimensional tangent spin structure and the two fixed holonomy lifts. It does not establish four-dimensional chirality or fermion dynamics.
- **Aliases:** `R021 named Pin image`, `B1141 spin-lift comparison`
- **Sources:** [`../../../memos/GIESEKING_PINMINUS_RESTRICTION.md`](../memos/GIESEKING_PINMINUS_RESTRICTION.md), [`../evidence/WAVE6_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE6_BRANCH_DELTA_AUDIT.md)
- **Deepest artifacts:** [`../../../certificates/r021_gieseking_pinminus/gieseking_pinminus_restriction.py`](../certificates/r021_gieseking_pinminus/gieseking_pinminus_restriction.py)

## Domain: `process`

<a id="oa-c1091"></a>
### OA-C1091 — `REFUTED`

- **Question:** Does the immutable B1147 tree satisfy its own clean-checkout reproduction lock without relying on an uncommitted artifact?
- **Answer:** No. At main commit 9d6979db, a clean archived-tree run gives one failure and four passes. The failure is FileNotFoundError for frontier/B1147_clane_harvest/verification/reproduce.log, which the lock test requires but the commit does not contain. Independent reruns support the memo mathematics; the defect is self-containment of the B1147 record.
- **Kind/domain:** `repair` / `process`
- **Depends on:** None.
- **Leads to:** None.
- **Closure test:** Run the exact B1147 verification test from a clean archive of the immutable commit and require every referenced artifact to exist there.
- **Falsifier:** A clean archive with the missing log committed and all tests passing would repair the record prospectively but would not change the immutable commit's result.
- **Scope:** Only the clean-checkout self-containment claim of immutable B1147. It does not refute the separately reproduced mathematical verdicts in memos 31-40.
- **Aliases:** `B1147 clean-lock defect`, `missing reproduce.log`
- **Sources:** [`../evidence/MAIN_B1146_B1147_DELTA_AUDIT.md`](program-question-map/evidence/MAIN_B1146_B1147_DELTA_AUDIT.md), [`../../../memos/B1147_LOCK_SELF_CONTAINMENT.md`](../memos/B1147_LOCK_SELF_CONTAINMENT.md), [`https://github.com/originaxiom/origin-axiom/tree/9d6979db424c0b878c62541a3f21e0a2ca39f274/frontier/B1147_clane_harvest`](https://github.com/originaxiom/origin-axiom/tree/9d6979db424c0b878c62541a3f21e0a2ca39f274/frontier/B1147_clane_harvest)
- **Deepest artifacts:** [`../../../certificates/check_b1147_lock.py`](../certificates/check_b1147_lock.py)

## Domain: `qft`

<a id="oa-c0007"></a>
### OA-C0007 — `REFUTED`

- **Question:** Does the mathematical E6 datum uniquely produce a compact four-dimensional quantum gauge theory?
- **Answer:** No. A constructive family L(n,g,theta,...) gives infinitely many inequivalent 4d E6 theories sharing the same root datum, 27, and cubic.
- **Kind/domain:** `construction` / `qft`
- **Depends on:** [OA-C0005](#oa-c0005)
- **Leads to:** [OA-C0008](#oa-c0008), [OA-C0009](#oa-c0009), [OA-C0011](#oa-c0011), [OA-C0016](#oa-c0016), [OA-C1002](#oa-c1002)
- **Closure test:** Construct and prove unique an object-selected compact background/action with spacetime, Hilbert space, spin-statistics, compact gauge fields, and matter.
- **Falsifier:** Two inequivalent QFT completions with the same antecedent data.
- **Scope:** All inference using only the current abstract arithmetic/Lie package.
- **Aliases:** `T[m004;E6]`, `physical functor`, `P0`
- **Sources:** `../tracks/PHYSICS_NO_GO.md`
- **Deepest artifacts:** None registered.

<a id="oa-c0017"></a>
### OA-C0017 — `EXTERNAL_BLOCKER`

- **Question:** Does the object uniquely produce four-dimensional spacetime and a gravitational quantum dynamics?
- **Answer:** Not yet. B1104 finds no canonical suspension section; filling is nonunique; S=-Vol*sigma is an on-shell value rather than a 4d gravitational action. B1157 and B1165 further classify the infinity-place constructions as generic spectral geometry: no 4d action, propagator or Ward identities are constructed. The exact Ruelle factorization OA-C1104 is mathematics, while OA-C1106--OA-C1108 remain specialist analytic residues. OA-C1132 registers the unrun arithmetic-versus-nonarithmetic ablation and OA-C1135 fences the proposed parity-by-dimension classifier.
- **Kind/domain:** `construction` / `qft`
- **Depends on:** [OA-C0003](#oa-c0003)
- **Leads to:** [OA-C0007](#oa-c0007), [OA-C1062](#oa-c1062), [OA-C1106](#oa-c1106), [OA-C1107](#oa-c1107), [OA-C1108](#oa-c1108), [OA-C1120](#oa-c1120), [OA-C1132](#oa-c1132), [OA-C1135](#oa-c1135), [OA-C1149](#oa-c1149), [OA-C1153](#oa-c1153), [OA-C1157](#oa-c1157), [OA-C1160](#oa-c1160)
- **Closure test:** A unique 4d spacetime/compactification, off-shell action, state space, and controlled quantum dynamics.
- **Falsifier:** No-section/nonuniqueness or an on-shell number mislabeled as an action.
- **Scope:** A physical Standard Model coupled to spacetime/gravity.
- **Aliases:** `fourth dimension`, `gravity`, `B1104`
- **Sources:** None registered.
- **Deepest artifacts:** None registered.

<a id="oa-c1002"></a>
### OA-C1002 — `REFUTED`

- **Question:** Does the class-field and toric data themselves select the ten-dimensional heterotic physical-realisation functor and its compactification framework?
- **Answer:** No. The same selected CY3 with h11=1,h21=4 has standard type-IIA and type-IIB compactifications with inequivalent 4d N=2 multiplet counts (1 vector,5 hypers) and (4 vectors,2 hypers), while heterotic E8xE8 requires extra left/right worldsheet, GSO and bundle data and gives N=1. Thus the arithmetic/toric antecedent has multiple physical-realisation functors. Retaining V_E8 in a c=16 chiral completion conditionally forces E8^2, but that retention and the heterotic worldsheet are additional physical premises, not properties of the CY3.
- **Kind/domain:** `construction` / `qft`
- **Depends on:** [OA-C1001](#oa-c1001), [OA-C0007](#oa-c0007), [OA-C1014](#oa-c1014)
- **Leads to:** [OA-C1003](#oa-c1003), [OA-C1006](#oa-c1006), [OA-C1007](#oa-c1007), [OA-C1015](#oa-c1015)
- **Closure test:** Construct from the admitted object data a unique ten-dimensional supersymmetric string framework, compactification interpretation, action, state space, and gauge-factor identification.
- **Falsifier:** Two inequivalent physical realisations sharing the arithmetic/toric antecedent, or reliance on an unproved heterotic/CY/standard-embedding premise.
- **Scope:** From the class-field/toric package to a physical heterotic compactification; excludes the conditional results after assuming that framework.
- **Aliases:** `heterotic framework selection`, `E8xE8 realisation premise`, `10d physics functor`
- **Sources:** `../tracks/PHYSICAL_REALIZATION_NONUNIQUENESS.md`, `../tracks/HETEROTIC_BRIDGE_AUDIT.md`, `../tracks/MCKAY_HETEROTIC_SELECTOR_AUDIT.md`, `../tracks/LATTICE_VOA_HETEROTIC_BRIDGE.md`
- **Deepest artifacts:** `../experiments/verify_realization_nonuniqueness.py`, `../experiments/verify_lattice_voa_heterotic_bridge.py`

<a id="oa-c1011"></a>
### OA-C1011 — `PROVED`

- **Question:** Does the positive E8 lattice isomorphism class determine a unique holomorphic c=8 lattice-VOA isomorphism class with e8 level-one currents?
- **Answer:** Yes. The even unimodular E8 lattice gives V_E8 with c=8 and 8+240=248 weight-one states; under the standard strong-rationality hypotheses this is the unique holomorphic c=8 VOA isomorphism class.
- **Kind/domain:** `theorem` / `qft`
- **Depends on:** [OA-C1009](#oa-c1009)
- **Leads to:** [OA-C1014](#oa-c1014)
- **Closure test:** Apply the lattice-VOA construction and small-central-charge classification, checking central charge, holomorphicity, roots, and weight-one current algebra.
- **Falsifier:** A second nonisomorphic strongly rational holomorphic c=8 receiver, failure of unimodularity/holomorphicity, or a weight-one algebra other than e8 at level one.
- **Scope:** Canonical unmarked chiral-algebra receiver only. It supplies neither a canonical marked C12 lift nor the second c=8 factor, right movers, GSO/ghost data, ten-dimensional spacetime, or a heterotic physical interpretation.
- **Aliases:** `E8 lattice VOA receiver`, `V_E8`, `c=8 chiral algebra`
- **Sources:** `../tracks/LATTICE_VOA_HETEROTIC_BRIDGE.md`
- **Deepest artifacts:** `../experiments/verify_lattice_voa_heterotic_bridge.py`

<a id="oa-c1014"></a>
### OA-C1014 — `PROVED`

- **Question:** Among positive even-unimodular rank-sixteen lattice or strongly rational holomorphic c=16 VOA completions that retain the selected E8 as a primitive orthogonal lattice subobject or full regular conformal factor, is E8 x E8 unique?
- **Answer:** Yes. Because det(E8)=1, an isometric E8 inclusion in a unimodular rank-sixteen lattice splits integrally as E8 plus its orthogonal complement; that complement is the unique rank-eight E8 lattice. In the regular conformal-coset VOA setting, holomorphic V_E8 forces the c=8 commutant to be V_E8, so V_D16+ cannot contain it compatibly. Complement C12 action/lift data remain free.
- **Kind/domain:** `theorem` / `qft`
- **Depends on:** [OA-C1011](#oa-c1011)
- **Leads to:** [OA-C1002](#oa-c1002)
- **Closure test:** Use unimodularity to split every retained E8 lattice inclusion, classify its rank-eight complement, and apply the c=8/c=16 holomorphic-VOA and regular-commutant arguments.
- **Falsifier:** A D16+ lattice containing an isometric E8 sublattice, a second positive even-unimodular rank-eight complement, or a compatible regular conformal V_E8 inclusion in V_D16+.
- **Scope:** A mathematical classification conditional on retaining the existing receiver. It neither selects that preservation premise nor derives a heterotic worldsheet, ten-dimensional target, CY sigma model, bundle, or vacuum.
- **Aliases:** `extension without erasure`, `E8-preserving c16 completion`, `primitive E8 factor`
- **Sources:** `../tracks/LATTICE_VOA_HETEROTIC_BRIDGE.md`
- **Deepest artifacts:** `../experiments/verify_lattice_voa_heterotic_bridge.py`

<a id="oa-c1015"></a>
### OA-C1015 — `CONDITIONAL`

- **Question:** Given the conservative critical-worldsheet realization axiom, do the selected CY3 and V_E8 force a four-dimensional E8 x E8 heterotic parent?
- **Answer:** Conditionally. For conventional heterotic matter, D+c_g=26 and 3D/2=15 give D=10 and c_g=16. A CY3 consumes six real target dimensions, leaving four; extension without erasure forces the c=16 gauge receiver to V_E8 tensor V_E8. All conclusions remain conditional on the composite physical-realization axiom.
- **Kind/domain:** `construction` / `qft`
- **Depends on:** [OA-C1001](#oa-c1001), [OA-C1014](#oa-c1014)
- **Leads to:** [OA-C1003](#oa-c1003), [OA-C1004](#oa-c1004), [OA-C1007](#oa-c1007), [OA-C1016](#oa-c1016)
- **Closure test:** State the conventional heterotic worldsheet data and retention rule explicitly, then derive the critical target dimension, gauge central charge, external dimension, and unique retained rank-sixteen chiral factor.
- **Falsifier:** Incorrect central-charge balance, a retained-E8 c=16 completion other than E8 squared, a target dimension other than ten, or an extra unpriced continuous choice in these classification steps.
- **Scope:** Conditional classification of dimension and ten-dimensional gauge parent only; it does not select the worldsheet axiom, standard embedding, special bundle, Wilson line, vacuum, gravity completion, or couplings.
- **Aliases:** `conservative critical-worldsheet bridge`, `conditional four dimensions`, `CY3 plus V_E8 receiver`
- **Sources:** `../tracks/LATTICE_VOA_HETEROTIC_BRIDGE.md`
- **Deepest artifacts:** `../experiments/verify_lattice_voa_heterotic_bridge.py`

<a id="oa-c1061"></a>
### OA-C1061 — `REFUTED`

- **Question:** Do the cited Fried, Park or Pfaff torsion formulae, or the scalar m004 cusp scattering determinant, directly equal the gauge-fixed cusped graviton one-loop determinant proposed by the programme?
- **Answer:** No. Fried-type torsion at s=0, analytic torsion of flat bundles and the scalar cusp determinant are not the Einstein spin-2/vector/scalar determinant ratio. B1157 and the corrected paper add a decisive negative control: Sym^(2m) cohomology is nonzero, so the closed-Fried acyclic value step and its reflection predictions are withdrawn. The unconditional factorization OA-C1104 survives, but it is representation algebra; the Laurent, cusp-correction and functional-equation residues OA-C1106--OA-C1108 do not repair the type mismatch.
- **Kind/domain:** `theorem` / `qft`
- **Depends on:** [OA-C1059](#oa-c1059), [OA-C1060](#oa-c1060)
- **Leads to:** [OA-C0017](#oa-c0017), [OA-C1062](#oa-c1062), [OA-C1105](#oa-c1105), [OA-C1106](#oa-c1106), [OA-C1107](#oa-c1107), [OA-C1108](#oa-c1108)
- **Closure test:** Type-match the evaluation points, bundles/K-types, boundary conditions and determinant complexes in one cited theorem.
- **Falsifier:** A primary theorem identifying the exact spin-2/vector/scalar determinant ratio on m004 with the named torsion or scalar scattering input would overturn this negative.
- **Scope:** The proposed direct substitutions using the cited theorems and existing scalar cusp datum. It is not a no-go for constructing a new cusped graviton determinant theorem.
- **Aliases:** `B8133`, `Fried/Park/Pfaff graviton feed`, `scalar cusp determinant substitution`
- **Sources:** `../tracks/SPECIALIST_RELAYS_2_3_AUDIT.md`, `../tracks/WAVE1_DELTA_ADJUDICATION.md`
- **Deepest artifacts:** `../tracks/SPECIALIST_RELAYS_2_3_AUDIT.md`

<a id="oa-c1062"></a>
### OA-C1062 — `EXTERNAL_BLOCKER`

- **Question:** Can one construct and evaluate a gauge-fixed spin-2/vector/scalar one-loop determinant for the finite-volume cusped m004 geometry with controlled boundary conditions and continuous spectrum?
- **Answer:** Not yet. No audited theorem accepts the current m004 scalar cusp determinant and returns the required Einstein one-loop ratio. B1157 and B1165 show that the infinity-place proposal remains generic spectral geometry with no action, propagator or Ward identity. Existing Ruelle/torsion identities compute different objects; even closure of OA-C1106--OA-C1108 would not by itself construct the gauge-fixed gravity determinant. OA-C1132 records the proposed but unrun m004-versus-m015 ablation. The missing deliverable remains an actual cusp gravity construction.
- **Kind/domain:** `construction` / `qft`
- **Depends on:** [OA-C0003](#oa-c0003)
- **Leads to:** [OA-C0017](#oa-c0017), [OA-C1107](#oa-c1107), [OA-C1108](#oa-c1108), [OA-C1132](#oa-c1132)
- **Closure test:** Define the gravity ensemble and cusp boundary conditions; construct renormalized determinants and spin-resolved scattering for K-types 0, 1 and 2; include parabolic terms, gauge/negative/zero modes and counterterms; then prove gauge and truncation control.
- **Falsifier:** A proof of an unavoidable negative mode or nonrenormalizable gauge dependence for the specified ensemble would refute that branch; an explicit theorem and evaluated certificate would close it.
- **Scope:** Euclidean one-loop gravity on the exact finite-volume cusped m004 background. This is downstream of, and cannot by itself derive, the programme's four-dimensional gravitational theory.
- **Aliases:** `cusped boundary-graviton one-loop`, `spin-resolved cusp determinant`, `relay 3 external deliverable`
- **Sources:** `../tracks/SPECIALIST_RELAYS_2_3_AUDIT.md`, `../tracks/WAVE1_DELTA_ADJUDICATION.md`
- **Deepest artifacts:** `../tracks/SPECIALIST_RELAYS_2_3_AUDIT.md`

<a id="oa-c1132"></a>
### OA-C1132 — `OPEN`

- **Question:** Does a controlled m004-versus-nonarithmetic-m015 ablation show that the proposed spectral dynamics are generic while only the volume-to-L-value avatar is arithmetic-specific?
- **Answer:** Open. B1165 proposes the comparison but does not run it. Existing Ruelle, torsion and Laplacian constructions are generic in type, while the m004 volume-to-Dedekind-L identity is arithmetic-specific and static. Neither side currently supplies a four-dimensional action.
- **Kind/domain:** `computation` / `qft`
- **Depends on:** [OA-C1062](#oa-c1062)
- **Leads to:** None.
- **Closure test:** Freeze matched geometric and spectral observables, cusp and volume normalizations and a nonarithmetic control; run both constructions and identify exactly which identities track arithmeticity.
- **Falsifier:** A proposed dynamical invariant that survives only on m004 and is proved to depend on its arithmetic field would refute genericity; unmatched normalizations withhold closure.
- **Scope:** A matched finite diagnostic between two cusped hyperbolic manifolds. Even a clean ablation classifies mathematical provenance; it does not construct gravitational or Standard-Model dynamics.
- **Aliases:** `B1165 gravity ablation`, `m004 versus m015`, `arithmetic-specific dynamics test`
- **Sources:** [`../evidence/WAVE5_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE5_BRANCH_DELTA_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/bf580f45840d121a811d2b6606c48beac92c3057/frontier/B1165_gravity_terminal/FINDINGS.md`](https://github.com/originaxiom/origin-axiom/blob/bf580f45840d121a811d2b6606c48beac92c3057/frontier/B1165_gravity_terminal/FINDINGS.md)
- **Deepest artifacts:** None registered.

<a id="oa-c1160"></a>
### OA-C1160 — `EXTERNAL_BLOCKER`

- **Question:** Is there a type-correct specialization or correspondence between an E6 Seiberg-Witten curve and the banked m004 A-polynomial that supplies a nontrivial first step toward a four-dimensional lift?
- **Answer:** Not yet. Outside tip bc9d381d exhausts the corpus and its cited construction lane: no E6 Seiberg-Witten-curve/state-integral construction exists to instantiate the comparison, the available dimension-six shadow leans mismatch, and B528 corrects the earlier nonabelian easy slice because T_K[4_1] is abelian at every rank. Main B1194 confirms no canonical 4d filling. The row is blocked on a new specialist mathematical construction, not an unrun in-repo calculation.
- **Kind/domain:** `comparison` / `qft`
- **Depends on:** [OA-C0005](#oa-c0005), [OA-C0017](#oa-c0017)
- **Leads to:** [OA-C0007](#oa-c0007)
- **Closure test:** Specify the four-dimensional theory, Coulomb-branch parameters, curve/differential and the A-polynomial component, then construct a map preserving the relevant symplectic or period data with a nonarithmetic/control manifold comparison.
- **Falsifier:** Dimension, genus, parameter or differential incompatibility refutes the proposed route; a visual polynomial resemblance cannot pass.
- **Scope:** One sharply typed mathematical comparison toward a 4d lift. Even a positive curve map would not by itself give a local 4d action, spectrum, chirality or vacuum.
- **Aliases:** `gravity S1`, `E6 Seiberg-Witten versus A-polynomial`, `4d lift first computation`
- **Sources:** [`../evidence/WAVE6_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE6_BRANCH_DELTA_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/bc9d381d0018cdc112ddac2373fe767ee4247531/outside_bench/THE_NINE_CELLS.md`](https://github.com/originaxiom/origin-axiom/blob/bc9d381d0018cdc112ddac2373fe767ee4247531/outside_bench/THE_NINE_CELLS.md)
- **Deepest artifacts:** None registered.

<a id="oa-c1161"></a>
### OA-C1161 — `REFUTED`

- **Question:** Does the bare m004 arithmetic force the quartic phase, amplitude and associator fields required by the proposed Fibonacci-MTC Born-content construction?
- **Answer:** No. B729 supplies that census. The object-native trace and Alexander data give Q(sqrt(-3)) and Q(sqrt(5)); the phase Q(zeta_5), amplitude Q(zeta_20)^+ and associator field appear only in imported Fibonacci-MTC data and have distinct quartic Galois/ramification types. The outside accounting is correct to price them as overlays, but they are already a theorem-level negative rather than an unclassified missing row.
- **Kind/domain:** `existence` / `qft`
- **Depends on:** [OA-C0003](#oa-c0003), [OA-C0016](#oa-c0016)
- **Leads to:** None.
- **Closure test:** Derive Q(zeta_5), Q(zeta_20)^+ and the associator extension from a canonical m004 invariant without importing the Fibonacci modular tensor category.
- **Falsifier:** A complete native-invariant census locating only the two quadratic fields and proving the quartics arise solely after the MTC import refutes native forcing.
- **Scope:** The specific Fibonacci-MTC Born-content route. This does not prove that no other quantum-probability construction can exist.
- **Aliases:** `B729 Born overlay decision`, `zeta5 phase`, `zeta20-real amplitudes`
- **Sources:** [`../evidence/WAVE6_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE6_BRANCH_DELTA_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/2f59628d60aa58f34fff98146da95ea22e95eed7/frontier/B729_amplitude_sector/FINDINGS.md`](https://github.com/originaxiom/origin-axiom/blob/2f59628d60aa58f34fff98146da95ea22e95eed7/frontier/B729_amplitude_sector/FINDINGS.md)
- **Deepest artifacts:** None registered.

## Domain: `spectrum`

<a id="oa-c0008"></a>
### OA-C0008 — `REFUTED`

- **Question:** Does the native structure provide three physical copies of a chiral 27?
- **Answer:** No. B1033 retracts four internal threes; B876 is one vectorlike 16+bar16 pattern; E8 contains (27,3) and (bar27,bar3), and its sole A2 cannot be both electroweak and family. OA-C1126 exactly shows that the selected trinification order-three symmetry cycles three different 9-blocks rather than three gauge-identical copies inside one 27. OA-C1137 records the independent logical failure of using a degree-two trace field to bound multiplicity by two.
- **Kind/domain:** `existence` / `spectrum`
- **Depends on:** [OA-C0007](#oa-c0007), [OA-C0009](#oa-c0009)
- **Leads to:** [OA-C0015](#oa-c0015), [OA-C1034](#oa-c1034), [OA-C1126](#oa-c1126), [OA-C1137](#oa-c1137), [OA-C1155](#oa-c1155)
- **Closure test:** A zero-mode/cohomology/Dirac index yielding three independent gauge-isomorphic 27s.
- **Falsifier:** A decomposition of one 27, a vectorlike pair, or a gauge-active triplet.
- **Scope:** All family-count routes presently in the fetched repositories.
- **Aliases:** `three generations`, `B876`, `B1033`, `E8 family A2`
- **Sources:** None registered.
- **Deepest artifacts:** None registered.

<a id="oa-c0012"></a>
### OA-C0012 — `CONDITIONAL`

- **Question:** Given the standard compact embedding and correct vacuum, is the unbroken global group (SU3xSU2xU1)/Z6?
- **Answer:** Conditionally. The Z6 kernel is standard and B1080 computes it for chosen cascades; no branch derives the physical compact embedding/vacuum antecedent.
- **Kind/domain:** `theorem` / `spectrum`
- **Depends on:** [OA-C0011](#oa-c0011), [OA-C0013](#oa-c0013)
- **Leads to:** [OA-C0014](#oa-c0014)
- **Closure test:** Group-level kernel computation for the selected compact embedding.
- **Falsifier:** A different kernel or residual extra U1 factor.
- **Scope:** Conditional subgroup theorem, not a selection theorem.
- **Aliases:** `SM/Z6`, `B1080`
- **Sources:** None registered.
- **Deepest artifacts:** None registered.

<a id="oa-c0013"></a>
### OA-C0013 — `REFUTED`

- **Question:** Does the object uniquely select a color-commuting Standard-Model hypercharge?
- **Answer:** No. B1102 finds 18 rational target-matching directions and exactly zero commuting with a full color ideal. B1139 searches against preloaded SM Q/Y tables and is a reproduction, not a selector. OA-C1121 proves a narrower trinification-frame realization after imposing an SM-shaped 15-plet; OA-C1118 records the distinct full-spectrum rank-three selector still required. Neither repairs intrinsic selection of the physical embedding.
- **Kind/domain:** `uniqueness` / `spectrum`
- **Depends on:** [OA-C0007](#oa-c0007)
- **Leads to:** [OA-C0012](#oa-c0012), [OA-C1118](#oa-c1118), [OA-C1121](#oa-c1121)
- **Closure test:** One intrinsic direction with the SM charge table that commutes with the selected full color ideal.
- **Falsifier:** Multiple imported-target solutions or no color-commuting solution.
- **Scope:** The A2 holonomy landing currently claimed.
- **Aliases:** `hypercharge`, `B1102`, `B1139`
- **Sources:** None registered.
- **Deepest artifacts:** None registered.

<a id="oa-c1005"></a>
### OA-C1005 — `CONDITIONAL`

- **Question:** Does the primitive cyclotomic source canonically force the hypercharge Wilson character to reuse the same odd-primary power as the bundle branch?
- **Answer:** Conditionally. Primitive characters rho with bundle pair {rho^3,rho^4} reproduce exactly four Table-3 branches; reusing rho^4 selects one four-model orbit and rho^-4 the other. The primary construction treats the two Wilson factors as independent, so the rule remains conditional.
- **Kind/domain:** `uniqueness` / `spectrum`
- **Depends on:** [OA-C1000](#oa-c1000), [OA-C1003](#oa-c1003), [OA-C1004](#oa-c1004)
- **Leads to:** [OA-C1006](#oa-c1006)
- **Closure test:** Derive the covariant same-source law from the physical heterotic functor and prove it is invariant under allowed bundle, E8, orientation, and Wilson-line equivalences.
- **Falsifier:** An equally admissible inverse-source rule, or a physical/equivariant construction treating bundle and hypercharge characters as independent commuting choices.
- **Scope:** The discrete BCDD bundle/Wilson relative-sign choice after a marked cyclotomic constituent is supplied.
- **Aliases:** `same-source Wilson rule`, `orientation branch selector`, `relative sign bit`
- **Sources:** `../tracks/ORIENTATION_BRANCH_SELECTOR.md`, `../tracks/CLASSFIELD_HETEROTIC_BRIDGE.md`
- **Deepest artifacts:** `../experiments/verify_orientation_branch_selector.py`

<a id="oa-c1006"></a>
### OA-C1006 — `CONDITIONAL`

- **Question:** Under the selected heterotic framework, smooth free quotient, stable SU(5) bundle branch, and Wilson character, does the visible charged massless sector equal three chiral MSSM generations plus one Higgs pair?
- **Answer:** Conditionally. The audited BCDD branches have index three and exact visible charged MSSM massless content after Wilson projection, conditional on the heterotic realization and generic stable branch. Hidden E8, neutral moduli, couplings, and dynamics remain outside the phrase visible spectrum.
- **Kind/domain:** `computation` / `spectrum`
- **Depends on:** [OA-C1001](#oa-c1001), [OA-C1003](#oa-c1003), [OA-C1004](#oa-c1004), [OA-C1005](#oa-c1005), [OA-C1013](#oa-c1013)
- **Leads to:** [OA-C1007](#oa-c1007), [OA-C1008](#oa-c1008), [OA-C1020](#oa-c1020), [OA-C1055](#oa-c1055)
- **Closure test:** Recompute the equivariant bundle cohomology and Wilson projection at a selected stable point, including the global (SU(3)xSU(2)xU(1))/Z6 group and absence of charged exotics.
- **Falsifier:** A failed stability/locally-free condition, cohomology jump, extra charged multiplet, wrong chirality, or an unaccounted hidden/neutral sector being mislabeled as the full theory.
- **Scope:** Visible gauge-charged massless sector only; conditional on all upstream geometric, bundle, framework, and Wilson premises.
- **Aliases:** `conditional charged MSSM spectrum`, `three-family heterotic output`, `visible spectrum`
- **Sources:** `../tracks/HETEROTIC_BRIDGE_AUDIT.md`, `../tracks/CLASSFIELD_HETEROTIC_BRIDGE.md`
- **Deepest artifacts:** None registered.

<a id="oa-c1118"></a>
### OA-C1118 — `OPEN`

- **Question:** In a precisely declared rank-three abelian charge sector with a complete candidate spectrum, does the anomaly Diophantine system uniquely select an SM-normalized hypercharge direction compatible with color and weak isospin?
- **Answer:** Open. OA-C1121 proves that a selected trinification frame realizes the universal anomaly-ratio theorem after an SM-shaped 15-state subset and nonzero quark charge are imposed. OA-C1122 shows that, within a finite generic SM-visible alphabet, full anomalies plus rigidity select the minimal SM15/conjugate pair. B1170 independently confirms that this forcing is arena-generic: no object token enters the enumeration. The object-specific unpaid input is therefore the arena itself--a selected complete light spectrum and rank-three abelian sector--plus frame, gauging and normalization. The stronger full-sector selector remains open.
- **Kind/domain:** `computation` / `spectrum`
- **Depends on:** [OA-C0013](#oa-c0013), [OA-C1112](#oa-c1112)
- **Leads to:** [OA-C0012](#oa-c0012)
- **Closure test:** Specify the three abelian generators and complete charged spectrum without preloading hypercharge, solve all linear, cubic and mixed anomaly equations over the declared lattice, impose color/weak commutation and normalization, and prove uniqueness modulo sign/equivalence.
- **Falsifier:** No admissible solution, multiple inequivalent solutions, dependence on preloaded SM charges, or incompatibility with the color/weak ideals refutes intrinsic uniqueness.
- **Scope:** A finite discrete selector test in B892's declared sector or another explicitly complete candidate sector. It must include every state treated as light and cannot assume an SM-shaped subset is the physical spectrum. It does not derive gauge fields or the running hypercharge coupling.
- **Aliases:** `THE_MSSM_DEBT D2`, `L132 hypercharge Diophantine route`
- **Sources:** [`../evidence/WAVE6_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE6_BRANCH_DELTA_AUDIT.md), [`../../../memos/HYPERCHARGE_TRINIFICATION_SCOPE.md`](../memos/HYPERCHARGE_TRINIFICATION_SCOPE.md), [`https://github.com/originaxiom/origin-axiom/blob/a6592e7b487d8fae482c00cfb9ba994f4c15723f/frontier/B1170_arena_rescope/FINDINGS.md`](https://github.com/originaxiom/origin-axiom/blob/a6592e7b487d8fae482c00cfb9ba994f4c15723f/frontier/B1170_arena_rescope/FINDINGS.md)
- **Deepest artifacts:** None registered.

<a id="oa-c1121"></a>
### OA-C1121 — `PROVED`

- **Question:** Within the selected trinification A2^3 frame, do all enumerated 27-derived SM-shaped 15-state assignments satisfying the four standard anomaly equations carry only the SM hypercharge ratios up to antitriplet exchange and overall scale?
- **Answer:** Yes. The outside certificate gives 36 of 36 SM-ratio solutions in each of two color frames. R019 reproduces the exact E6/27 stack, extends the control to all three color slots and again finds 36 solutions, all SM-pattern, with no non-SM or multidimensional result. On the chiral branch Y_q is nonzero, the anomaly equations reduce universally to Y_l/Y_q=-3, Y_e/Y_q=6, (Y_u+Y_d)/Y_q=-2 and -18(Y_u/Y_q-2)(Y_u/Y_q+4)=0. If Y_q=0 is allowed, an additional vectorlike branch exists and is outside the claimed SM-ratio theorem.
- **Kind/domain:** `computation` / `spectrum`
- **Depends on:** [OA-C0013](#oa-c0013), [OA-C1112](#oa-c1112)
- **Leads to:** [OA-C1118](#oa-c1118)
- **Closure test:** Construct the A2^3 frame and rank-three Cartan complement exactly; enumerate every declared 15-state assignment and weak-root choice; solve all four anomaly equations; and certify the ratio classes, solution dimensions and frame controls.
- **Falsifier:** One accepted assignment with a non-SM ratio, a multidimensional charge family, failure in a color-slot control, or a missing declared assignment refutes the finite theorem.
- **Scope:** Conditional on an observer-supplied trinification frame, color/weak orientation, an assumed left-handed SM-shaped 15-state subset, nonzero Y_q and the standard anomaly equations. The ratios are universal consequences of those multiplet multiplicities, not an E6-specific selector. The theorem excludes the Y_q=0 vectorlike branch by scope and does not select the physical spectrum, treat the other twelve 27 states, gauge U(1), derive Y_q=1/6, or supply a coupling, vacuum or dynamics.
- **Aliases:** `outside memo 70`, `HYPERCHARGE_FALLS_OUT`, `trinification anomaly-ratio theorem`, `R019`
- **Sources:** [`../../../memos/HYPERCHARGE_TRINIFICATION_SCOPE.md`](../memos/HYPERCHARGE_TRINIFICATION_SCOPE.md), [`../evidence/WAVE5_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE5_BRANCH_DELTA_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/60bcf01db966ae0b13f18c73c24845040b59fd98/outside_bench/memos/HYPERCHARGE_FALLS_OUT.md`](https://github.com/originaxiom/origin-axiom/blob/60bcf01db966ae0b13f18c73c24845040b59fd98/outside_bench/memos/HYPERCHARGE_FALLS_OUT.md), [`https://github.com/originaxiom/origin-axiom/blob/bf580f45840d121a811d2b6606c48beac92c3057/frontier/B1160_hypercharge_forced/FINDINGS.md`](https://github.com/originaxiom/origin-axiom/blob/bf580f45840d121a811d2b6606c48beac92c3057/frontier/B1160_hypercharge_forced/FINDINGS.md)
- **Deepest artifacts:** [`../../../certificates/r019_hypercharge/hypercharge_trinification_scope.py`](../certificates/r019_hypercharge/hypercharge_trinification_scope.py), [`https://github.com/originaxiom/origin-axiom/blob/60bcf01db966ae0b13f18c73c24845040b59fd98/outside_bench/certificates/l132_trinification.py`](https://github.com/originaxiom/origin-axiom/blob/60bcf01db966ae0b13f18c73c24845040b59fd98/outside_bench/certificates/l132_trinification.py)

<a id="oa-c1122"></a>
### OA-C1122 — `PROVED`

- **Question:** Within the declared finite SM-visible representation alphabets, do the full gauge, mixed and global anomaly constraints plus chirality and rigidity select the SM 15-state content as the smallest solution up to conjugation?
- **Answer:** Yes. The corrected exact scan examines 252 contents in the six-representation alphabet, kills 222 already by SU(3)^3, and leaves exactly the SM15 and its conjugate after the full system. Enlargements by adjoints and (3,3)-type representations leave 7 and 14 solutions respectively but no smaller one. The result is generic model-building arithmetic. The branch's arc_verdict.json is stale and still names the withdrawn 13-state counterexample; FINDINGS.md, results.json and steps 4--6 carry the corrected verdict.
- **Kind/domain:** `computation` / `spectrum`
- **Depends on:** [OA-C0013](#oa-c0013)
- **Leads to:** [OA-C1118](#oa-c1118)
- **Closure test:** Enumerate the declared representation multisets, impose SU(3)^3, SU(3)^2-U(1), SU(2)^2-U(1), gravitational-U(1), U(1)^3, Witten parity, chirality and rigidity, and identify every minimum exactly.
- **Falsifier:** A smaller admissible chiral rigid content, or a nonconjugate minimum in the declared alphabets, refutes the finite claim.
- **Scope:** The finite declared representation alphabets and supplied SM gauge group. No E6, m004, trace-field or object-selection datum enters the executable scan; uniqueness outside the tested alphabets and derivation of the physical spectrum are not claimed.
- **Aliases:** `paper B8143 corrected anomaly lane`, `finite SM-shape census`, `full-anomaly minimality`
- **Sources:** [`../evidence/WAVE5_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE5_BRANCH_DELTA_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/a6c35d083e9bd7610045093d682afce827034932/frontier/B8143_anomaly_lane/FINDINGS.md`](https://github.com/originaxiom/origin-axiom/blob/a6c35d083e9bd7610045093d682afce827034932/frontier/B8143_anomaly_lane/FINDINGS.md)
- **Deepest artifacts:** [`https://github.com/originaxiom/origin-axiom/blob/a6c35d083e9bd7610045093d682afce827034932/frontier/B8143_anomaly_lane/step4_full.py`](https://github.com/originaxiom/origin-axiom/blob/a6c35d083e9bd7610045093d682afce827034932/frontier/B8143_anomaly_lane/step4_full.py), [`https://github.com/originaxiom/origin-axiom/blob/a6c35d083e9bd7610045093d682afce827034932/frontier/B8143_anomaly_lane/step5_robust.py`](https://github.com/originaxiom/origin-axiom/blob/a6c35d083e9bd7610045093d682afce827034932/frontier/B8143_anomaly_lane/step5_robust.py)

<a id="oa-c1125"></a>
### OA-C1125 — `PROVED`

- **Question:** Do the selected-chain centralizer and grading censuses leave no psi remnant, exactly fifteen nontrivial root-lattice Z2 gradings, and no all-matter-odd grading?
- **Answer:** Yes. Independent reruns give joint torus exactly equal to the SM torus and surviving psi charges 1 and -2 with gcd one, hence no continuous or discrete psi remnant. Of 15 nontrivial root-lattice gradings, exactly one has the SM-torus shadow and 14 are additional; none is odd on all 15 multiplets and none is constant-odd on the psi-10 class. The z2 script's uc/dc labels are exchanged relative to the measured-Y texture script, but the counts are exchange-invariant.
- **Kind/domain:** `computation` / `spectrum`
- **Depends on:** [OA-C1100](#oa-c1100), [OA-C1119](#oa-c1119)
- **Leads to:** [OA-C0014](#oa-c0014)
- **Closure test:** Compute the joint torus centralizer, primitive psi charges and all nontrivial GF(2) root-lattice gradings on the declared 15-plet roster.
- **Falsifier:** A surviving independent psi generator, a nontrivial psi remnant, a missed grading, or a grading odd on every declared matter multiplet refutes the corresponding census.
- **Scope:** The selected frame, 27, two declared breaking directions and finite root-lattice grading space. No full-action R parity, stable dark particle or phenomenology is established.
- **Aliases:** `outside Z2 census`, `psi survival`, `selected-chain discrete remnant ledger`
- **Sources:** [`../evidence/WAVE5_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE5_BRANCH_DELTA_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/60bcf01db966ae0b13f18c73c24845040b59fd98/outside_bench/memos/Z2_CENSUS.md`](https://github.com/originaxiom/origin-axiom/blob/60bcf01db966ae0b13f18c73c24845040b59fd98/outside_bench/memos/Z2_CENSUS.md), [`https://github.com/originaxiom/origin-axiom/blob/60bcf01db966ae0b13f18c73c24845040b59fd98/outside_bench/memos/PSI_SURVIVAL.md`](https://github.com/originaxiom/origin-axiom/blob/60bcf01db966ae0b13f18c73c24845040b59fd98/outside_bench/memos/PSI_SURVIVAL.md)
- **Deepest artifacts:** [`https://github.com/originaxiom/origin-axiom/blob/60bcf01db966ae0b13f18c73c24845040b59fd98/outside_bench/certificates/z2_census.py`](https://github.com/originaxiom/origin-axiom/blob/60bcf01db966ae0b13f18c73c24845040b59fd98/outside_bench/certificates/z2_census.py), [`https://github.com/originaxiom/origin-axiom/blob/60bcf01db966ae0b13f18c73c24845040b59fd98/outside_bench/certificates/psi_survival.py`](https://github.com/originaxiom/origin-axiom/blob/60bcf01db966ae0b13f18c73c24845040b59fd98/outside_bench/certificates/psi_survival.py)

<a id="oa-c1126"></a>
### OA-C1126 — `PROVED`

- **Question:** Does every size-three orbit of the selected order-three trinification action cross the three distinct 9-blocks, making it a sector cycle rather than an intra-27 family index?
- **Answer:** Yes. The exact census finds 36 order-three slot cyclers and nine size-three orbits. Every orbit crosses all three distinct trinification 9-blocks; none gives three copies within one block. Thus the selected Z3 is a sector cycle, not an intra-27 family index.
- **Kind/domain:** `computation` / `spectrum`
- **Depends on:** [OA-C0006](#oa-c0006), [OA-C0008](#oa-c0008)
- **Leads to:** None.
- **Closure test:** Enumerate every order-three slot cycler on the selected 27 and determine the block membership of every size-three orbit.
- **Falsifier:** One complete size-three orbit contained in a single gauge-identical 9-block, or a missed slot cycler, refutes the finite census.
- **Scope:** The selected trinification frame, 27 and declared slot-cycling actions. The result strengthens the current generation no-go but does not exclude every conceivable family mechanism in a different geometry or representation.
- **Aliases:** `outside family census`, `trinification Z3 orbit census`, `one-27 family no-go`
- **Sources:** [`../evidence/WAVE5_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE5_BRANCH_DELTA_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/60bcf01db966ae0b13f18c73c24845040b59fd98/outside_bench/memos/FAMILY_CENSUS.md`](https://github.com/originaxiom/origin-axiom/blob/60bcf01db966ae0b13f18c73c24845040b59fd98/outside_bench/memos/FAMILY_CENSUS.md)
- **Deepest artifacts:** [`https://github.com/originaxiom/origin-axiom/blob/60bcf01db966ae0b13f18c73c24845040b59fd98/outside_bench/certificates/family_census.py`](https://github.com/originaxiom/origin-axiom/blob/60bcf01db966ae0b13f18c73c24845040b59fd98/outside_bench/certificates/family_census.py)

<a id="oa-c1130"></a>
### OA-C1130 — `PROVED`

- **Question:** Does exact ablation in the selected finite assignment space show that the mixed gravitational anomaly cuts the solutions while the cubic equation is redundant in the realized sector?
- **Answer:** Yes. The independently rerun exact ablation shows that deleting the mixed gravitational anomaly enlarges the admissible spaces, while deleting the cubic equation changes no V0 count in the realized sector. This attributes constraint strength inside the frozen finite model; it is not a theorem that physical gravity creates hypercharge.
- **Kind/domain:** `computation` / `spectrum`
- **Depends on:** [OA-C1112](#oa-c1112), [OA-C1121](#oa-c1121)
- **Leads to:** None.
- **Closure test:** Enumerate the identical assignment domain with each declared anomaly equation removed in turn and compare exact solution spaces and ratio classes.
- **Falsifier:** A different V0--V4 count, a cubic removal changing the claimed realized-sector count, or failure of gravitational removal to enlarge the solution space refutes the table.
- **Scope:** The enumerated 27/frame/SM-shaped charge-assignment set and its declared algebraic anomaly equations. It does not derive a gravitational action, quantum anomaly cancellation or an object-selected gauge theory.
- **Aliases:** `outside gravitational-anomaly ablation`, `finite anomaly mechanism table`, `V0-V4 ablation`
- **Sources:** [`../evidence/WAVE5_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE5_BRANCH_DELTA_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/60bcf01db966ae0b13f18c73c24845040b59fd98/outside_bench/memos/GRAVITY_LOAD_BEARING.md`](https://github.com/originaxiom/origin-axiom/blob/60bcf01db966ae0b13f18c73c24845040b59fd98/outside_bench/memos/GRAVITY_LOAD_BEARING.md)
- **Deepest artifacts:** [`https://github.com/originaxiom/origin-axiom/blob/60bcf01db966ae0b13f18c73c24845040b59fd98/outside_bench/certificates/grav_ablation.py`](https://github.com/originaxiom/origin-axiom/blob/60bcf01db966ae0b13f18c73c24845040b59fd98/outside_bench/certificates/grav_ablation.py)

<a id="oa-c1137"></a>
### OA-C1137 — `REFUTED`

- **Question:** Does a degree-two trace field force representation or family multiplicities to lie only in {1,2}, thereby excluding multiplicity three?
- **Answer:** No. Field degree constrains scalar embeddings and Galois structure, not the number of repeated summands. If V is any admissible module over Q(sqrt(-3)), then V direct-sum V direct-sum V is defined over the same degree-two field and has multiplicity three. B1161's stronger sentence is therefore false without an additional irreducibility or object-selection theorem; OA-C1126 supplies the actual selected-27 family census.
- **Kind/domain:** `implication` / `spectrum`
- **Depends on:** [OA-C0008](#oa-c0008), [OA-C1075](#oa-c1075)
- **Leads to:** None.
- **Closure test:** Prove a theorem relating field degree to multiplicity for the exact module category, excluding arbitrary direct sums and base change.
- **Falsifier:** For any nonzero module over the degree-two field, its direct sum with itself three times has multiplicity three and refutes the unrestricted implication.
- **Scope:** The unrestricted claimed implication from trace-field degree to representation/family multiplicity. It does not assert that the current object supplies three physical generations.
- **Aliases:** `B1161 trace-field multiplicity claim`, `degree-two generation bound`, `multiplicity-field no-go`
- **Sources:** [`../evidence/WAVE5_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE5_BRANCH_DELTA_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/bf580f45840d121a811d2b6606c48beac92c3057/frontier/B1161_frontier_sweep/FINDINGS.md`](https://github.com/originaxiom/origin-axiom/blob/bf580f45840d121a811d2b6606c48beac92c3057/frontier/B1161_frontier_sweep/FINDINGS.md)
- **Deepest artifacts:** None registered.

<a id="oa-c1155"></a>
### OA-C1155 — `REFUTED`

- **Question:** Are B889's three pairwise distinguishable sectors canonically the trinification Z3 family orbit, so that they supply three physical generations rather than internal frames of one 27?
- **Answer:** No. B1190 rejects GC-8's proposed identification: the B889 frames are the Galois S3 of an explicit external cubic, not the trinification Z3. B1196 GC-26 supplies the decisive carrier obstruction: every B891 foreign eigenspace has dimension 16 and its projector spreads across all three nine-dimensional trinification blocks, so it cannot equal any one block or any union of the 9+9+9 partition. The proposed canonical identification is refuted. This negative does not produce three chiral zero-mode copies; the parent physical-generation gate remains unclosed.
- **Kind/domain:** `comparison` / `spectrum`
- **Depends on:** [OA-C0008](#oa-c0008), [OA-C1128](#oa-c1128)
- **Leads to:** [OA-C0009](#oa-c0009)
- **Closure test:** Construct the exact action on both three-element sets, identify their representation carriers and prove a label-preserving equivalence that produces three chiral copies rather than three views of one copy.
- **Falsifier:** Different acting groups, an external cubic carrier, or one underlying 27 with no replicated zero modes refutes the physical-generation interpretation.
- **Scope:** The B889/B891 finite carriers and generation-count interpretation. Three internal sectors are not three chiral zero modes without an explicit replication/index theorem.
- **Aliases:** `grand-computation D2`, `generation-three adjudication`, `B889 frame trit`
- **Sources:** [`../evidence/WAVE6_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE6_BRANCH_DELTA_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/af8564bd38c7dababf649591339d06e99e9cbaf0/frontier/B1190_close_loop_batch2/FINDINGS.md`](https://github.com/originaxiom/origin-axiom/blob/af8564bd38c7dababf649591339d06e99e9cbaf0/frontier/B1190_close_loop_batch2/FINDINGS.md), [`https://github.com/originaxiom/origin-axiom/blob/40916c36ddeb1eb1631097b3535c6a79a2658e23/frontier/B1196_close_loop_batch5b/verification/batch5b_cells.json`](https://github.com/originaxiom/origin-axiom/blob/40916c36ddeb1eb1631097b3535c6a79a2658e23/frontier/B1196_close_loop_batch5b/verification/batch5b_cells.json)
- **Deepest artifacts:** [`../../../certificates/r023_b1196_generation_obstruction.py`](../certificates/r023_b1196_generation_obstruction.py), [`../../../outputs/r023_b1196_generation_obstruction.txt`](../outputs/r023_b1196_generation_obstruction.txt)

## Domain: `vacuum`

<a id="oa-c0011"></a>
### OA-C0011 — `EXTERNAL_BLOCKER`

- **Question:** Does the object select a rank-reducing Higgs representation, orbit, point, and vacuum?
- **Answer:** Not yet. B632 v0 has N=-6, Jordan rank 3 and F4 stabilizer, not the rank-1 Spin10 direction. A Kato-Yukie semistable pencil contains no rank-1 direction; for two rank-1 endpoints N(sA+tB) is identically zero. OA-C1113 gives the direction-level parity/lock fork, and OA-C1119 now closes the selected finite SM-safe direction census: exactly two directions pass, but both destroy the selected gradings. Neither result supplies a potential, an actual VEV, stability or an object-selected orbit.
- **Kind/domain:** `existence` / `vacuum`
- **Depends on:** [OA-C0007](#oa-c0007)
- **Leads to:** [OA-C0012](#oa-c0012), [OA-C0014](#oa-c0014), [OA-C1113](#oa-c1113), [OA-C1119](#oa-c1119), [OA-C1150](#oa-c1150)
- **Closure test:** An object-selected scalar sector and solved stable vacuum with the required rank drop.
- **Falsifier:** Candidate lies in the wrong invariant orbit or only specifies an orbit/condition rather than a point and potential.
- **Scope:** Known repo VEV shortcuts are refuted; F4(Z) pair-orbit and full potential remain open.
- **Aliases:** `rank-closing VEV`, `B632`, `B969`, `B1043`, `L176`
- **Sources:** None registered.
- **Deepest artifacts:** None registered.

<a id="oa-c0014"></a>
### OA-C0014 — `EXTERNAL_BLOCKER`

- **Question:** Does the selected vacuum leave exactly the SM light fields and one viable Higgs sector while lifting all exotics?
- **Answer:** Not yet. In a fixed D5 x U(1)_psi frame, 27=16_1+10_-2+1_4 and the exact E6 cubic has 40 supports of type (16,16,10) plus 5 of type (10,10,1), conserving the resulting parity. OA-C1112 proves the associated anomaly sums cancel and OA-C1113 classifies individual parity/lock-neutral directions. Both facts remain frame-conditional: support and anomaly arithmetic do not supply fields, gauging, a potential, stability or mass ranks. No vacuum or exotic-decoupling proof exists.
- **Kind/domain:** `computation` / `vacuum`
- **Depends on:** [OA-C0011](#oa-c0011), [OA-C0012](#oa-c0012)
- **Leads to:** [OA-C0015](#oa-c0015), [OA-C0016](#oa-c0016), [OA-C1100](#oa-c1100), [OA-C1112](#oa-c1112), [OA-C1113](#oa-c1113), [OA-C1117](#oa-c1117), [OA-C1119](#oa-c1119)
- **Closure test:** Explicit scalar potential/vacuum and mass matrices with proved ranks in every charge sector.
- **Falsifier:** Any massless colored exotic, mirror family, extra U1, or unselected light-doublet multiplicity.
- **Scope:** Strict low-energy SM spectrum.
- **Aliases:** `Higgs`, `exotic decoupling`, `doublet-triplet splitting`
- **Sources:** [`../../../memos/DARK_LEDGER_SCOPE_AUDIT.md`](../memos/DARK_LEDGER_SCOPE_AUDIT.md), [`../evidence/WAVE4_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE4_BRANCH_DELTA_AUDIT.md), [`../evidence/WAVE5_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE5_BRANCH_DELTA_AUDIT.md)
- **Deepest artifacts:** [`../../../certificates/r012_dark_ledger_scope.py`](../certificates/r012_dark_ledger_scope.py)

<a id="oa-c1007"></a>
### OA-C1007 — `EXTERNAL_BLOCKER`

- **Question:** Does the selected class-field heterotic construction determine an isolated stable vacuum and all normalized low-energy parameters?
- **Answer:** Not yet. The selected section does not stabilize bundle, Kahler, dilaton, or other moduli; the BCDD branch has genuine P10 bundle deformations. On the strict CY branch the exact compact (0,2) GLSM lies in the Beasley--Witten vanishing class, so genus-zero worldsheet terms cannot select that P10. The class-field action now conditionally selects one hidden E8 lift and a combined order-three secondary class, but the no-B strict branch then fails level matching. A published large-radius Strominger theorem supplies a same-topology torsional solution preserving the visible spectrum, not the prescribed differential class or a vacuum. The exact height-308 up-type cup product is zero and remains zero along that fixed-holomorphic-data Strominger curve. The exact universal hidden threshold is negative, refuting the economical supersymmetric fractional-CS condensate solution; normalizer symmetry leaves three complex-structure equations, and no down Yukawa, normalized periods, subgroup thresholds, prefactors, all-moduli mass matrix, SUSY-breaking scale or RG output is derived.
- **Kind/domain:** `computation` / `vacuum`
- **Depends on:** [OA-C1004](#oa-c1004), [OA-C1006](#oa-c1006)
- **Leads to:** [OA-C1017](#oa-c1017), [OA-C1019](#oa-c1019), [OA-C1026](#oa-c1026), [OA-C1028](#oa-c1028), [OA-C1029](#oa-c1029), [OA-C1030](#oa-c1030), [OA-C1046](#oa-c1046), [OA-C1047](#oa-c1047), [OA-C1048](#oa-c1048), [OA-C1049](#oa-c1049), [OA-C1050](#oa-c1050), [OA-C1051](#oa-c1051), [OA-C1052](#oa-c1052), [OA-C1053](#oa-c1053), [OA-C1054](#oa-c1054)
- **Closure test:** Derive the complete effective data, solve all F- and D-terms to one reduced point modulo equivalence, prove a positive physical mass matrix, and compute normalized Yukawas, thresholds, SUSY breaking, scales, and RG observables.
- **Falsifier:** Any surviving bundle, complex-structure, Kahler, dilaton, hidden-sector, or other continuous modulus; two inequivalent vacua; or missing normalization/RG/dynamical data.
- **Scope:** Full four-dimensional heterotic vacuum and parameter-free Standard Model output, beyond visible charged-spectrum existence.
- **Aliases:** `heterotic vacuum stabilization`, `parameter-free vacuum blocker`, `moduli dynamics`
- **Sources:** `../tracks/HETEROTIC_VACUUM_DYNAMICS.md`, `../tracks/HETEROTIC_INSTANTON_GATE.md`, `../tracks/HETEROTIC_FLUX_GATE.md`, `../tracks/CLASSFIELD_E8_WILSON_LIFT.md`, `../tracks/RELATIVE_SECONDARY_CS_AUDIT.md`, `../tracks/CLASSFIELD_HETEROTIC_LEVEL_MATCHING.md`, `../tracks/FRACTIONAL_CS_VACUUM_AUDIT.md`, `../tracks/BETA_THRESHOLD_AUDIT.md`, `../tracks/NORMALIZER_CS_CRITICALITY.md`, `../tracks/STROMINGER_ORDER3_EXISTENCE_AUDIT.md`, `../tracks/YUKAWA_STROMINGER_PERSISTENCE_AUDIT.md`, `../tracks/CLASSICAL_BUNDLE_MODULI_NO_GO.md`, `../tracks/SUSY_BREAKING_SCALE_GATE.md`
- **Deepest artifacts:** None registered.

<a id="oa-c1017"></a>
### OA-C1017 — `REFUTED`

- **Question:** Does one pure hidden-E8 gaugino condensate stabilize the dilaton and the single Kahler modulus of the selected quotient?
- **Answer:** No. For K=-log(S+Sbar)-3log(T+Tbar), f_h=S and W=A exp(-2 pi S/30), exact no-scale cancellation gives V=|A|^2 exp(-a x)(a x+1)^2/(x y^3). Its logarithmic derivatives are strictly negative in x and y, and both axions are flat, on all 30 branches. The same x-stationarity obstruction holds for a selected positive linear threshold f_h=S+beta T. Extra condensates, fluxes, thresholds or corrections are new data.
- **Kind/domain:** `computation` / `vacuum`
- **Depends on:** [OA-C1007](#oa-c1007)
- **Leads to:** None.
- **Closure test:** Derive the four-dimensional F-term potential and exhibit a finite supersymmetric or metastable stationary point with all participating saxions and axions fixed.
- **Falsifier:** A strictly monotone potential, a runaway, a flat axion, or a missing selected kinetic function/prefactor.
- **Scope:** The economical tree-level one-condensate model and its positive linear-threshold refinement; not a no-go for racetracks, flux superpotentials, D-terms, or corrected Kahler potentials.
- **Aliases:** `single hidden-E8 condensate`, `economical heterotic vacuum`, `pure-E8 runaway`
- **Sources:** `../tracks/SINGLE_CONDENSATE_VACUUM.md`, `../tracks/HETEROTIC_INSTANTON_GATE.md`
- **Deepest artifacts:** `../experiments/verify_single_condensate_vacuum.py`

<a id="oa-c1018"></a>
### OA-C1018 — `REFUTED`

- **Question:** Can an integral quantized heterotic H-flux class on the fixed C12 quotient supply a parameter-free W0 or stabilize the remaining moduli on the strict Calabi--Yau branch?
- **Answer:** No. The integral quotient certificate gives H_2=Z and H^4=Z; UCT, Poincare duality, and b3=2(h21+1)=10 give H^3(X,Z)=Z^10 with no torsion. Thus integral topological flux has an infinite menu and no selected lattice vector. On the strict Kahler CY N=1 branch H=d^cJ=0; in the H-only 4d F-term truncation D_S W=0 and D_z W=0 force H=0. This does not exclude finite-order secondary characters in H^3(X,R/Z): OA-C1044 proves a conditional order-three class, which instead leaves the strict (0,2) CY branch and requires a fractional-CS/condensate or non-Kahler completion.
- **Kind/domain:** `computation` / `vacuum`
- **Depends on:** [OA-C1001](#oa-c1001), [OA-C1015](#oa-c1015), [OA-C1016](#oa-c1016)
- **Leads to:** [OA-C1007](#oa-c1007), [OA-C1044](#oa-c1044), [OA-C1045](#oa-c1045), [OA-C1048](#oa-c1048), [OA-C1051](#oa-c1051)
- **Closure test:** Reconstruct integral H^3 including torsion, distinguish differential Chern--Simons data, and either derive a marked finite flux selector plus an isolated SUSY vacuum or prove the exact no-go on the strict CY branch.
- **Falsifier:** A certified object-selected H^3 class, nonzero supersymmetric CY H-flux, or a complete flux-plus-condensate solution fixing all remaining moduli without imported parameters.
- **Scope:** Integral H^3 flux on the fixed smooth free C12 quotient and the strict N=1 Kahler-CY/H-only truncation. Secondary differential Chern--Simons characters are tracked separately by OA-C1043--OA-C1045 and do not inherit this refutation.
- **Aliases:** `quantized H-flux gate`, `H3 flux menu`, `heterotic CY flux no-go`
- **Sources:** `../tracks/HETEROTIC_FLUX_GATE.md`, `../tracks/RELATIVE_SECONDARY_CS_AUDIT.md`, `../tracks/HETEROTIC_INSTANTON_GATE.md`, `../tracks/HETEROTIC_VACUUM_DYNAMICS.md`
- **Deepest artifacts:** `../experiments/verify_heterotic_flux_gate.py`, `../experiments/verify_heterotic_bridge_scope.py`

<a id="oa-c1019"></a>
### OA-C1019 — `EXTERNAL_BLOCKER`

- **Question:** Does the class-field C12 action select a hidden-E8 Wilson line with pure asymptotically-free factors, and does the resulting fractional-CS/condensate system isolate the heterotic vacuum?
- **Answer:** Not yet. The old unrestricted problem has 270 Kac classes, but the retained class-field lattice automorphism now selects one Weyl class and one compact lift after the equivariant heterotic-retention clause. Its hidden centralizer is A2+A1^3+U1^3 and its universal c2 is 2 mod 12; the native rho^4-to-SU3-center alternative instead has c2=0. This closes the finite conjugacy menu conditionally, not the vacuum: tree-level factors share f=S, the exact parent hidden slope is -3/(2 pi^2), and the economical fractional-CS supersymmetry equation has no positive-volume solution. The large-radius Strominger theorem supplies a compatible local torsional geometry, but normalized periods, subgroup kinetic functions, determinant prefactors/phases, the global order-three lift and an isolated vacuum remain open.
- **Kind/domain:** `uniqueness` / `vacuum`
- **Depends on:** [OA-C1007](#oa-c1007), [OA-C1015](#oa-c1015)
- **Leads to:** [OA-C1021](#oa-c1021), [OA-C1022](#oa-c1022), [OA-C1041](#oa-c1041), [OA-C1043](#oa-c1043), [OA-C1044](#oa-c1044), [OA-C1046](#oa-c1046), [OA-C1049](#oa-c1049), [OA-C1050](#oa-c1050), [OA-C1051](#oa-c1051)
- **Closure test:** Derive an object-native homomorphism C12 -> E8, its hidden bundle/zero-mode sector, threshold functions and prefactors, then prove an isolated finite vacuum for all participating moduli.
- **Falsifier:** A unique selected Kac class with certified pure multi-factor hidden sector and a solved racetrack fixing S,T without imported continuous data.
- **Scope:** The selected smooth free C12 quotient and conventional heterotic hidden-sector branch; non-Kahler, flux, corrected-Kahler and additional matter branches require separate data.
- **Aliases:** `hidden E8 Wilson census`, `C12-to-E8 Kac classes`, `E6xSU3 racetrack`
- **Sources:** `../tracks/HIDDEN_E8_WILSON_RACETRACK.md`, `../tracks/CLASSFIELD_E8_WILSON_LIFT.md`, `../tracks/CLASSFIELD_E8_LIFT_AUDIT.md`, `../tracks/RELATIVE_SECONDARY_CS_AUDIT.md`, `../tracks/BETA_THRESHOLD_AUDIT.md`, `../tracks/FRACTIONAL_CS_VACUUM_AUDIT.md`, `../tracks/STROMINGER_ORDER3_EXISTENCE_AUDIT.md`
- **Deepest artifacts:** `../experiments/verify_hidden_e8_wilson_racetrack.py`, `../experiments/verify_classfield_e8_wilson_lift.sage`, `../experiments/verify_classfield_cs_pullback.py`

<a id="oa-c1021"></a>
### OA-C1021 — `EXTERNAL_BLOCKER`

- **Question:** Does the native order-three hidden Wilson line determine unequal Kahler thresholds and an isolated S,T racetrack vacuum?
- **Answer:** Not yet. Tree level and level-one embedding give f_E6=f_SU3=S and b=(36,9). The broken (27,3)+(bar27,bar3) channel has unequal quadratic-index weights (18,54), so a differential threshold is allowed but not forced. The BCDD data contain no full (0,2) CFT partition function, HYM determinant, modular integral, corrected Kahler data, or object-derived A6/A3. A common f(T) can at most fix saxion ratios in the toy K truncation and leaves an orthogonal axion flat; non-proportional functions or another selected effect are required for isolation.
- **Kind/domain:** `computation` / `vacuum`
- **Depends on:** [OA-C1019](#oa-c1019), [OA-C1017](#oa-c1017)
- **Leads to:** None.
- **Closure test:** Compute the regulated (0,2) worldsheet charge-insertion determinant for the selected bundle/HYM connection and C12 flat bundle, derive both holomorphic threshold functions and condensate prefactors/branches, and prove an isolated finite F- and D-flat S,T solution.
- **Falsifier:** A source-backed modular integral yielding selected non-proportional E6 and SU3 threshold functions together with a unique branch and isolated vacuum without imported continuous constants.
- **Scope:** Fixed BCDD smooth free C12 Calabi-Yau quotient, trivial hidden bundle, no five-branes, conventional weakly coupled E8xE8 heterotic branch, and the displayed two-condensate K truncation; non-Kahler/flux/corrected-Kahler branches are separate gates.
- **Aliases:** `hidden E6xSU3 threshold gate`, `Wilson-line Kahler thresholds`, `common-f racetrack axion gate`
- **Sources:** `../tracks/HIDDEN_E8_THRESHOLD_GATE.md`, `../tracks/HIDDEN_E8_WILSON_RACETRACK.md`, `../tracks/HETEROTIC_VACUUM_DYNAMICS.md`, `../sources/1112.1097/Three_gen_models.tex`
- **Deepest artifacts:** `../experiments/verify_hidden_e8_threshold_gate.py`

<a id="oa-c1022"></a>
### OA-C1022 — `REFUTED`

- **Question:** Can a continuous U(1) left by a faithful C12-to-E8 Wilson line generate a Green-Schwarz/FI D-term that fixes a Kahler or axion direction on the trivial hidden-bundle branch?
- **Answer:** No. The exact faithful Kac census gives U(1)^r with r=1,2,3,4 in 30,125,76,5 classes. For every nontrivial Wilson character H1(X,L_chi)=H1(Y,O)_chi=0, so all hidden U(1)-nonabelian, gravitational, cubic and Tr Q anomalies vanish. Flat torsion holonomy and V_hid=O^8 give zero real c1, zero hidden curvature and zero continuous GS/FI source; hence D_Q=0 identically with no charged fields and no modulus is fixed.
- **Kind/domain:** `theorem` / `vacuum`
- **Depends on:** [OA-C1019](#oa-c1019), [OA-C1015](#oa-c1015)
- **Leads to:** None.
- **Closure test:** Enumerate all faithful centralizer torus ranks, prove the charged Wilson sectors have vanishing H1, and evaluate the continuous anomaly, FI and Stückelberg sources under V_hid=O^8 and zero five-brane class.
- **Falsifier:** A surviving charged hidden zero mode or nonzero object-derived continuous FI/axionic gauging on the fixed flat trivial-bundle branch, followed by a finite D-flat solution.
- **Scope:** Fixed smooth free C12 quotient, flat hidden Wilson line, V_hid=O^8, zero five-brane/flux sources and no added hidden matter. Nontrivial bundles, five-branes, flux and corrected effective actions are separate branches.
- **Aliases:** `hidden Wilson U(1) D-term`, `flat-line FI gate`, `no charged hidden zero modes`
- **Sources:** `../tracks/HIDDEN_WILSON_DTERM_GATE.md`, `../tracks/HIDDEN_E8_WILSON_RACETRACK.md`, `../tracks/HETEROTIC_BRIDGE_AUDIT.md`
- **Deepest artifacts:** `../experiments/verify_hidden_wilson_dterm.py`

<a id="oa-c1026"></a>
### OA-C1026 — `REFUTED`

- **Question:** Can genus-zero heterotic worldsheet instantons in the exact equivariant BCDD `(3,4)` model generate a superpotential that selects an isolated point of the surviving bundle-map P10?
- **Answer:** No. The exact U(1)^8 field table pairs the twelve Cox and one P chiral charges with identical Fermi charges, so the full gauge-anomaly matrix vanishes term by term. At the lower height-308 map, all six W34 Euler contractions vanish identically (lambda_mu=0), giving an exact off-shell E.J=0 GLSM over Q(zeta12). Here the monad target and hypersurface degrees obey m=d=H=-K_Z with H ample and d-m=0, satisfying the Bertolini--Plesser all-degree compactness criterion. Beasley--Witten then makes every positive-degree genus-zero coefficient vanish. H2(X,Z)=Z, free lifting and sectorwise cover cancellation remove torsion, quotient and multiple-cover loopholes. Hence W_ws is identically zero and cannot select the P10.
- **Kind/domain:** `theorem` / `vacuum`
- **Depends on:** [OA-C1007](#oa-c1007), [OA-C1024](#oa-c1024), [OA-C1027](#oa-c1027)
- **Leads to:** [OA-C1048](#oa-c1048)
- **Closure test:** Construct the complete anomaly-free `(0,2)` GLSM, verify all off-shell E.J identities at the named map, prove compactness of every instanton sector, control the free C12 quotient/torsion/multiple-cover effects, and determine whether the resulting superpotential has an isolated critical point.
- **Falsifier:** A failed E.J identity or gauge anomaly, a noncompact effective instanton sector, quotient curve torsion with inequivalent phases, or a nonzero certified genus-zero superpotential coefficient on the nonsingular branch.
- **Scope:** Genus-zero worldsheet contributions to the spacetime singlet superpotential on the nonsingular strict-CY, zero-H equivariant BCDD `(0,2)` GLSM branch. The fractional-CS/torsional Strominger branch is a different worldsheet background and does not inherit this vanishing theorem without a new model. Higher F-terms, spacetime nonperturbative effects, and a full vacuum are separate gates.
- **Aliases:** `worldsheet instanton selector`, `explicit BCDD GLSM`, `Beasley-Witten P10 no-go`
- **Sources:** `../tracks/HETEROTIC_INSTANTON_GATE.md`, `../sources/1112.1097/Three_gen_models.tex`
- **Deepest artifacts:** `../experiments/verify_worldsheet_instanton_gate.sage`, `../experiments/bundle_low_height_scout.sage`

<a id="oa-c1028"></a>
### OA-C1028 — `REFUTED`

- **Question:** Can the classical heterotic holomorphic Chern--Simons functional plus Hermitian--Yang--Mills D-flatness select one arithmetic map from the surviving bundle P10?
- **Answer:** No. The exact variation is delta W_HCS=2 integral Omega wedge Tr(delta A wedge F_A^(0,2)), so W_HCS is locally constant on every connected family of holomorphic structures. Donaldson--Uhlenbeck--Yau supplies one HYM connection for each stable holomorphic bundle modulo gauge, not a unique holomorphic structure. The full invariant hyperExt calculation gives twelve bundle tangent directions and zero Atiyah rank on all four complex-structure directions at every tested arithmetic point, leaving a sixteen-dimensional first-order simultaneous tangent rather than selecting one arithmetic map.
- **Kind/domain:** `theorem` / `vacuum`
- **Depends on:** [OA-C1007](#oa-c1007), [OA-C1024](#oa-c1024), [OA-C1033](#oa-c1033)
- **Leads to:** None.
- **Closure test:** Differentiate the holomorphic Chern--Simons functional on the integrable bundle locus, combine it with the stable-bundle/HYM correspondence, and test whether the surviving projective tangent is lifted to an isolated critical point.
- **Falsifier:** A derived classical term with nonzero tangent derivative or a proved classical critical scheme consisting of one reduced stable bundle point.
- **Scope:** Classical perturbative holomorphic Chern--Simons and HYM equations on the fixed CY/monad branch. Higher-order obstructions, worldsheet instantons, spacetime nonperturbative effects and corrected supergravity potentials remain separate gates.
- **Aliases:** `classical bundle-moduli selector`, `holomorphic Chern-Simons P10 gate`, `HYM uniqueness no-go`
- **Sources:** `../tracks/CLASSICAL_BUNDLE_MODULI_NO_GO.md`, `../tracks/ATIYAH_MODULI_MAP.md`, `../tracks/FULL_EXT_ATIYAH_COMPARISON.md`, `../tracks/PHI_MODULI_QUOTIENT_AUDIT.md`
- **Deepest artifacts:** `../experiments/verify_atiyah_map.sage.py`, `../experiments/verify_full_ext_atiyah.sage`

<a id="oa-c1029"></a>
### OA-C1029 — `REFUTED`

- **Question:** Do the selected algebraic Calabi--Yau, bundle, index and finite Wilson-line data fix the Kähler size, heterotic dilaton and absolute physical scales?
- **Answer:** No. For any Ricci-flat Kähler metric g on the selected CY3, c g is Ricci-flat for every c>0 because log det(cg)=3 log c+log det g; the volume scales as c^3 while the complex variety, C12 action, Chern data and Wilson line are unchanged. The quotient has h11=1, so its Kähler cone is a positive ray, not a point. The ten-dimensional dilaton is an additional continuous field and Re f_visible depends on it. On the strict-CY tree branch W=0, so the S,T potential vanishes identically; all tested economical corrections leave a runaway or flat direction.
- **Kind/domain:** `theorem` / `vacuum`
- **Depends on:** [OA-C1007](#oa-c1007), [OA-C1015](#oa-c1015)
- **Leads to:** None.
- **Closure test:** Exhibit the continuous metric/dilaton family preserving every admitted discrete datum, or derive and solve a complete potential that fixes it to one duality class with positive physical masses.
- **Falsifier:** An object-derived isolated finite S,T solution with all branches, axions, kinetic normalizations and scale matching fixed without measured input.
- **Scope:** The fixed smooth C12 Calabi--Yau quotient and its selected algebraic/discrete data before a derived full quantum effective potential. A later isolated quantum vacuum is the exact positive hatch.
- **Aliases:** `Kahler scale gate`, `dilaton/gauge-coupling modulus`, `absolute-scale no-go`
- **Sources:** `../tracks/KAHLER_DILATON_SCALE_GATE.md`, `../tracks/HETEROTIC_VACUUM_DYNAMICS.md`, `../tracks/HETEROTIC_BRIDGE_AUDIT.md`
- **Deepest artifacts:** `../experiments/verify_kahler_scale_gate.py`

<a id="oa-c1030"></a>
### OA-C1030 — `EXTERNAL_BLOCKER`

- **Question:** Does the conditional heterotic MSSM spectrum come with a selected isolated supersymmetry-breaking vacuum, mediation mechanism and low-energy Standard Model limit?
- **Answer:** Not yet. The exact cohomology result is an unbroken N=1 MSSM spectrum. The strict-CY W=0 branch preserves supersymmetry, while the class-field secondary branch has a same-topology large-radius Strominger solution but no selected differential lift or vacuum. For K=-log(S+Sbar)-3log(T+Tbar) and any W(S), the old no-scale identity leaves an arbitrary T and breaking scale. With the newly exact negative universal threshold, the complete common-function F-term potential is strictly decreasing toward decompactification for every common axion phase, so even a nonsupersymmetric finite minimum is absent. Flat hidden Wilson lines supply no FI D-term. No isolated scale, soft Lagrangian or electroweak vacuum is derived.
- **Kind/domain:** `computation` / `vacuum`
- **Depends on:** [OA-C1006](#oa-c1006), [OA-C1007](#oa-c1007), [OA-C1019](#oa-c1019), [OA-C1029](#oa-c1029)
- **Leads to:** [OA-C1046](#oa-c1046), [OA-C1052](#oa-c1052)
- **Closure test:** Derive the complete SUSY-breaking sector and mediation data, solve for one metastable vacuum with fixed moduli/axions and positive masses, and compute the soft spectrum, mu/Bmu, electroweak vacuum, thresholds and RG observables without imported scales.
- **Falsifier:** A fully selected finite vacuum and mediation calculation producing a viable low-energy spectrum and all scales from the admitted antecedent object.
- **Scope:** The current weakly-coupled N=1 heterotic branch and all economical SUSY-breaking mechanisms explicitly constructed in the campaign. More elaborate controlled sectors remain possible but unconstructed/unselected.
- **Aliases:** `supersymmetry-breaking gate`, `soft-scale/mediation blocker`, `MSSM-to-SM dynamics`
- **Sources:** `../tracks/SUSY_BREAKING_SCALE_GATE.md`, `../tracks/NEGATIVE_BETA_FULL_POTENTIAL.md`, `../tracks/STROMINGER_ORDER3_EXISTENCE_AUDIT.md`, `../tracks/ORDER3_DIFFERENTIAL_STROMINGER_CLOSURE.md`, `../tracks/HIDDEN_WILSON_DTERM_GATE.md`
- **Deepest artifacts:** `../experiments/verify_susy_breaking_scale_gate.py`, `../experiments/verify_single_condensate_vacuum.py`

<a id="oa-c1040"></a>
### OA-C1040 — `REFUTED`

- **Question:** Can the selected visible C12 Wilson line on the MSSM branches generate a nonzero flat Cheeger--Chern--Simons class and thereby supply the missing fractional W0 or flux selector?
- **Answer:** No. The fundamental SU5 weights are (-2k,-2k,-2k,3k,3k), with c1=0 and c2 coefficient -15 k^2 mod 12. For k=4 and k=8 this is zero. Since positive-degree real cohomology of finite C12 vanishes, the Bockstein H3(BC12,R/Z)->H4(BC12,Z)_tors is an isomorphism, so the associated flat Cheeger--Chern--Simons class is zero and remains zero after pullback to X.
- **Kind/domain:** `theorem` / `vacuum`
- **Depends on:** [OA-C1001](#oa-c1001), [OA-C1005](#oa-c1005), [OA-C1015](#oa-c1015), [OA-C1018](#oa-c1018)
- **Leads to:** [OA-C1007](#oa-c1007)
- **Closure test:** Compute the universal c2 class of the exact C12-to-SU5 hypercharge representation, identify its flat differential-character lift, and pull it back to the quotient threefold.
- **Falsifier:** A nonzero c2 coefficient in H4(BC12,Z)=Z/12 for k=4 or k=8, or a nonzero flat secondary class despite the Bockstein isomorphism.
- **Scope:** The selected visible SU5 Wilson representations k=4,8 only. Non-flat bundle/tangent relative invariants, hidden-E8 Wilson lines, thresholds and other differential trivializations remain separate.
- **Aliases:** `visible Wilson flat Chern-Simons class`, `C12 fractional W0 gate`, `hypercharge Wilson c2`
- **Sources:** `../tracks/VISIBLE_WILSON_CS_GATE.md`, `../tracks/HETEROTIC_FLUX_GATE.md`, `../sources/1112.1097/Three_gen_models.tex`
- **Deepest artifacts:** `../experiments/verify_visible_wilson_cs.py`

<a id="oa-c1041"></a>
### OA-C1041 — `REFUTED`

- **Question:** Does the native class-field character rho^4 into the center of the regular SU3 subgroup of E8 generate a nonzero fractional hidden Chern--Simons class?
- **Answer:** No. The defining SU3 weights are (4,4,4), so c2=e2(4,4,4)=48=0 mod 12. The regular SU3 in E8 has Dynkin index one, hence no hidden normalization changes the zero. The Bockstein flat Cheeger--Chern--Simons character is therefore zero. A full 270-class control census finds 249 nonzero alternatives, so the vanishing is specific rather than vacuous.
- **Kind/domain:** `theorem` / `vacuum`
- **Depends on:** [OA-C1000](#oa-c1000), [OA-C1015](#oa-c1015), [OA-C1019](#oa-c1019)
- **Leads to:** None.
- **Closure test:** Compute the basic E8 degree-four class of the exact C12 representation, including the subgroup Dynkin index, and identify its flat differential-character lift.
- **Falsifier:** A nonzero basic c2 coefficient in H^4(BC12,Z)=Z/12 for the specified rho^4-to-center representation.
- **Scope:** Only the native order-three rho^4 representation through Z(SU3). The separately selected full class-field order-twelve E8 lift is OA-C1043 and has nonzero c2.
- **Aliases:** `native rho4 hidden Wilson CS`, `E6xSU3 center class`, `hidden order-three flat invariant`
- **Sources:** `../tracks/HIDDEN_E8_WILSON_CS_GATE.md`, `../tracks/HIDDEN_E8_WILSON_RACETRACK.md`
- **Deepest artifacts:** `../experiments/verify_hidden_e8_wilson_cs.py`

<a id="oa-c1043"></a>
### OA-C1043 — `PROVED`

- **Question:** Does the retained class-field C12 lattice action determine a unique compact-E8 lift, and what hidden centralizer and secondary class does that lift have?
- **Answer:** Yes. The complete W(E8) census has one order-twelve class with characteristic Phi12^2 and det(1-w)=1. Thus 1-w is a torus automorphism and all normalizer lifts are conjugate; an exact 248-dimensional check gives order 12. The unique Kac row (1,0,0,1,0,0,1,0,1) has centralizer A2+A1^3+U1^3 and basic c2=2 mod 12. The Cartan--Leray edge map H3(X)->Z/12 is onto, so its flat character pulls back with exact order six. The element cannot commute with the same-factor standard SU3 and is physically usable only in the hidden E8 on the conditional equivariant-retention branch.
- **Kind/domain:** `theorem` / `vacuum`
- **Depends on:** [OA-C1009](#oa-c1009), [OA-C1014](#oa-c1014), [OA-C1015](#oa-c1015)
- **Leads to:** [OA-C1044](#oa-c1044), [OA-C1045](#oa-c1045), [OA-C1047](#oa-c1047), [OA-C1048](#oa-c1048), [OA-C1049](#oa-c1049), [OA-C1050](#oa-c1050)
- **Closure test:** Identify the Weyl class, prove normalizer-lift uniqueness and exact order, determine the Kac row/centralizer and basic c2, then type-check same-factor versus hidden-factor compatibility and quotient pullback.
- **Falsifier:** A second Weyl class with order 12 and characteristic Phi12^2, a nonconjugate normalizer lift, a different exact Kac type, or vanishing of the pulled-back secondary class.
- **Scope:** The compact group conjugacy theorem and secondary topology are unconditional after the positive E8 lattice action is fixed. Treating that action as an equivariantly retained hidden heterotic Wilson line remains part of the physical-realization interface.
- **Aliases:** `class-field E8 Weyl lift`, `Phi12-squared hidden Wilson`, `unique order-twelve Kac class`
- **Sources:** `../tracks/CLASSFIELD_E8_WILSON_LIFT.md`, `../tracks/CLASSFIELD_E8_LIFT_AUDIT.md`, `../tracks/LATTICE_VOA_HETEROTIC_BRIDGE.md`
- **Deepest artifacts:** `../experiments/verify_classfield_e8_wilson_lift.sage`, `../experiments/verify_classfield_cs_pullback.py`

<a id="oa-c1044"></a>
### OA-C1044 — `CONDITIONAL`

- **Question:** Do the successful visible bundle-equivariant branches and the class-field hidden E8 lift combine into a nonzero, same-source heterotic secondary Chern--Simons character?
- **Answer:** Conditionally. For V0=L_t tensor (TX+L_n1+L_n2), all four successful pairs give c2hat(V0)-c2hat(TX)=2 mod 12, an order-six flat character. The hidden lift gives another +2. Hence c2(TX)-c2(Vvis)-c2(Vhid)=-4=8 mod 12, exact order three; reversing conventions changes only the sign. The primary H4 class still vanishes. For generic V308 the Chern--Weil difference need not be flat, but the holomorphic CS value is locally constant modulo periods along a connected integrable deformation. The nonzero secondary requires fractional CS/H flux and leaves the strict N=1/(0,2) CY branch unless another sector cancels or backreacts.
- **Kind/domain:** `theorem` / `vacuum`
- **Depends on:** [OA-C1005](#oa-c1005), [OA-C1018](#oa-c1018), [OA-C1043](#oa-c1043)
- **Leads to:** [OA-C1007](#oa-c1007), [OA-C1045](#oa-c1045), [OA-C1046](#oa-c1046), [OA-C1048](#oa-c1048), [OA-C1051](#oa-c1051)
- **Closure test:** Compute the differential c2 difference for the split visible bundle in every spectrum-surviving branch, add the hidden basic class with the heterotic trace/sign convention, and separate split-locus flat topology from deformed-bundle HCS persistence and normalized flux dynamics.
- **Falsifier:** A successful branch with a different relative coefficient, a non-index-one embedding normalization, cancellation of the two classes, or failure of the connected holomorphic deformation needed to transport the HCS value.
- **Scope:** Exact at the split connection with the marked C12 characters and index-one traces; conditional for transport to the named stable bundle and for the equivariant hidden heterotic realization. It fixes a fractional class, not a normalized W0 or vacuum.
- **Aliases:** `relative split-bundle CS class`, `order-three heterotic secondary`, `visible-plus-hidden differential anomaly`
- **Sources:** `../tracks/RELATIVE_SECONDARY_CS_AUDIT.md`, `../tracks/HETEROTIC_FLUX_GATE.md`, `../tracks/CLASSFIELD_E8_WILSON_LIFT.md`, `../sources/1112.1097/Three_gen_models.tex`
- **Deepest artifacts:** `../experiments/verify_relative_secondary_cs.py`, `../experiments/verify_classfield_cs_pullback.py`, `../experiments/verify_heterotic_bridge_scope.py`

<a id="oa-c1045"></a>
### OA-C1045 — `PROVED`

- **Question:** What exact cycle functional does the class-field E8 secondary character define on H3(X), and does it determine a normalized holomorphic period or W0?
- **Answer:** Yes. H3(X,Z)=Z^10 maps surjectively to H3(BC12,Z)=Z/12. In an adapted integral basis the map is n->n1 mod 12, and c2=2 evaluates as chi(n)=n1/6 mod 1, an exact primitive sixth-root phase. The conditional codifferent-norm law nominates an algebraic complex-structure basepoint and residue form up to scale, but no marked H3 chain/sLag basis, period vector or physical Omega normalization has been constructed. OA-C1124 proves that the unoriented amphichiral carrier cannot select an orientation or regulator sign, and OA-C1136 refutes the claim that CS=0 plus Mostow rigidity absorbs the independent U(1) rescaling of a Calabi--Yau holomorphic three-form. The topology fixes a phase/coset, not an additive parameter-free W0.
- **Kind/domain:** `theorem` / `vacuum`
- **Depends on:** [OA-C1001](#oa-c1001), [OA-C1043](#oa-c1043)
- **Leads to:** [OA-C1007](#oa-c1007), [OA-C1046](#oa-c1046), [OA-C1047](#oa-c1047), [OA-C1109](#oa-c1109), [OA-C1124](#oa-c1124), [OA-C1136](#oa-c1136)
- **Closure test:** Determine the classifying-map homomorphism H3(X,Z)->Z/12 up to integral basis, evaluate the pulled-back E8 character exactly, and state which marked-cycle, period and normalization data are not implied.
- **Falsifier:** A non-surjective Cartan--Leray edge map, a different order for the pulled-back character, or an existing marked toric/sLag H3 basis and period evaluation contradicting the stated residual.
- **Scope:** The abstract integral normal form and universal level-one E8 phase. Geometric cycle marking, normalized periods, integral-lift/B-field choice and four-dimensional dynamics remain separate tasks.
- **Aliases:** `classifying H3 functional`, `order-six E8 phase`, `CS period marking gate`
- **Sources:** `../tracks/CLASSFIELD_CS_PERIOD_FUNCTIONAL.md`, `../tracks/SECTION_VACUUM_SELECTOR.md`, `../tracks/CLASSFIELD_E8_WILSON_LIFT.md`
- **Deepest artifacts:** `../experiments/verify_classfield_period_functional.py`, `../experiments/verify_classfield_cs_pullback.py`

<a id="oa-c1046"></a>
### OA-C1046 — `REFUTED`

- **Question:** Does the conditional order-three secondary class and the selected hidden centralizer produce a weakly-coupled, large-volume supersymmetric vacuum on the fixed BCDD bundle allocation?
- **Answer:** No. For K=-log(S+Sbar)-3log(T+Tbar) and one condensate depending on S+beta T, supersymmetry requires beta(T+Tbar)=3(S+Sbar); common thresholds also leave the orthogonal axion flat. OA-C1049 proves beta_hidden=-3/(2 pi^2) on the fixed positive Kahler ray, so the required equality is impossible for positive saxions. The naive 1/3 and 2/3 normalizations moreover place the selected SU3/SU2 factors at strong coupling for canonical prefactors. Subgroup-specific thresholds, altered instanton allocation, five-branes, non-Kahler corrections or extra terms are different branches and remain unselected.
- **Kind/domain:** `computation` / `vacuum`
- **Depends on:** [OA-C1044](#oa-c1044), [OA-C1045](#oa-c1045), [OA-C1049](#oa-c1049)
- **Leads to:** [OA-C1007](#oa-c1007), [OA-C1030](#oa-c1030), [OA-C1052](#oa-c1052)
- **Closure test:** Normalize the secondary class into the four-dimensional superpotential, compute the exact gauge kinetic slopes and condensate prefactors, solve all F-terms at positive weak coupling and large volume, and verify the axion and mass matrices.
- **Falsifier:** A positive-volume solution of the exact fixed-allocation equations with object-derived prefactors and normalization, or a sign error in the primitive topological threshold coefficient.
- **Scope:** The economical supersymmetric fractional-CS plus condensate model on the fixed visible-standard/hidden-trivial allocation, including its universal linear threshold. It is not a no-go for every non-universal, five-brane, non-Kahler or nonsupersymmetric completion.
- **Aliases:** `fractional-CS condensate vacuum`, `order-three W0 toy`, `fixed-allocation sign obstruction`
- **Sources:** `../tracks/FRACTIONAL_CS_VACUUM_AUDIT.md`, `../tracks/BETA_THRESHOLD_AUDIT.md`, `../tracks/RELATIVE_SECONDARY_CS_AUDIT.md`
- **Deepest artifacts:** `../experiments/verify_fractional_cs_vacuum.py`, `../experiments/verify_beta_threshold.py`

<a id="oa-c1047"></a>
### OA-C1047 — `REFUTED`

- **Question:** Does the full finite normalizer symmetry of the codifferent-norm section force all complex-structure derivatives of the residue or Chern--Simons superpotential to vanish?
- **Answer:** No. The order-48 fan normalizer acts on the four-dimensional projective tangent as three trivial characters plus one sign character. Both the residue three-form and the universal c2/CS character are invariant because every fan matrix has determinant +1 and every unit a mod 12 has a^2=1. Symmetry therefore kills only the odd derivative and leaves three invariant complex-structure derivatives unconstrained.
- **Kind/domain:** `theorem` / `vacuum`
- **Depends on:** [OA-C1001](#oa-c1001), [OA-C1043](#oa-c1043), [OA-C1045](#oa-c1045)
- **Leads to:** [OA-C1007](#oa-c1007)
- **Closure test:** Compute the normalizer action on the projective complex-structure tangent and on the residue and secondary characters, then determine the invariant cotangent dimension at the norm point.
- **Falsifier:** A different exact tangent character decomposition or a nontrivial scalar character forcing all four covector components to vanish.
- **Scope:** Finite normalizer constraints at the codifferent-norm complex-structure point. Additional dynamical period equations may still fix the three even directions.
- **Aliases:** `normalizer criticality`, `order-48 norm-section symmetry`, `complex-structure symmetry selector`
- **Sources:** `../tracks/NORMALIZER_CS_CRITICALITY.md`, `../tracks/SECTION_VACUUM_SELECTOR.md`
- **Deepest artifacts:** `../experiments/verify_normalizer_cs_criticality.py`

<a id="oa-c1049"></a>
### OA-C1049 — `PROVED`

- **Question:** What is the exact universal one-loop linear Kähler threshold on the selected quotient and fixed visible-standard/hidden-trivial bundle allocation?
- **Answer:** Yes. Adjunction on the anticanonical hypersurface gives integral_Y D c2(TY)=144. Division by the free C12 action and primitivity of the descended divisor gives integral_X J c2(TX)=12. In the GKL convention and with c2(Vvis)=c2(TX), c2(Vhid)=0, the parent coefficients are beta_visible=+3/(2 pi^2) and beta_hidden=-3/(2 pi^2). The flat class-field Wilson changes only secondary data, not this primary pairing; subgroup-specific massive thresholds remain uncomputed.
- **Kind/domain:** `theorem` / `vacuum`
- **Depends on:** [OA-C1001](#oa-c1001), [OA-C1016](#oa-c1016), [OA-C1043](#oa-c1043)
- **Leads to:** [OA-C1007](#oa-c1007), [OA-C1046](#oa-c1046), [OA-C1050](#oa-c1050), [OA-C1052](#oa-c1052)
- **Closure test:** Identify the primitive quotient Kähler generator, compute its pairing with c2(TX), insert the fixed visible and hidden Chern classes into the normalized heterotic threshold formula, and keep subgroup-specific determinants separate.
- **Falsifier:** A nonprimitive descended generator, a different exact intersection number, or a convention-consistent positive hidden parent-E8 slope on the positive Kähler ray.
- **Scope:** The universal parent-E8 linear term in the primitive one-Kähler-modulus normalization on the fixed no-five-brane allocation. It does not compute broken-subgroup determinant thresholds.
- **Aliases:** `BCDD universal threshold`, `primitive Kahler c2 pairing`, `negative hidden beta`
- **Sources:** `../tracks/BETA_THRESHOLD_AUDIT.md`, `../tracks/CLASSFIELD_HETEROTIC_LEVEL_MATCHING.md`
- **Deepest artifacts:** `../experiments/verify_beta_threshold.py`

<a id="oa-c1050"></a>
### OA-C1050 — `REFUTED`

- **Question:** Does the finite normalizer of the selected class-field E8 holonomy act transitively on the three hidden SU(2) factors and thereby force equal thresholds, determinants and condensate phases?
- **Answer:** No. Exact Weyl computation gives |N_W(<w>)|=1152 and |C_W(w)|=288. Because det(1-w)=1 removes torus-lift ambiguity, N_E8(<g>)/C_E8(g) is (Z/12)^*=V4. Any homomorphism V4->Out(A1^3)=S3 has image at most C2, so it cannot act transitively on the three SU2 ideals. The parent E8 still proves the common tree-level f_i=S, but one-loop functions, determinant prefactors and condensate phases require explicit quantum data; symmetry-related noninvariant points are different backgrounds, not equal terms in one vacuum.
- **Kind/domain:** `theorem` / `vacuum`
- **Depends on:** [OA-C1043](#oa-c1043), [OA-C1049](#oa-c1049)
- **Leads to:** [OA-C1007](#oa-c1007)
- **Closure test:** Compute the exact Weyl and compact-group normalizer quotient, bound its permutation action on A1^3, and distinguish tree-level parent-E8 equality from quantum determinant equivariance at a fixed background.
- **Falsifier:** A larger normalizer quotient with a transitive S3 image, or an explicit equivariant determinant theorem identifying all three factor thresholds and phases at the selected background.
- **Scope:** The finite normalizer and its possible permutations of the three isomorphic A1 factors. The marked GL(3,Z) action on U1^3 and the actual one-loop determinant functions remain uncomputed.
- **Aliases:** `class-field E8 normalizer`, `hidden A1^3 condensate symmetry`, `quantum-prefactor equality gate`
- **Sources:** `../tracks/CLASSFIELD_E8_NORMALIZER_CONDENSATES.md`, `../tracks/CLASSFIELD_E8_WILSON_LIFT.md`, `../tracks/HIDDEN_E8_THRESHOLD_GATE.md`
- **Deepest artifacts:** `../experiments/verify_classfield_e8_normalizer.sage`, `../experiments/verify_classfield_e8_wilson_lift.sage`

<a id="oa-c1052"></a>
### OA-C1052 — `REFUTED`

- **Question:** Can the full two-field F-term potential on the fixed negative-threshold branch possess a finite nonsupersymmetric stationary point even though its supersymmetric equations have no positive-volume solution?
- **Answer:** No. With b=-beta>0, z=(S+Sbar)-b(T+Tbar)>0 and q=b(T+Tbar)/z, the potential factors as b^3|W|^2 z^-4 F(p,q)/((1+q)q^3). Its q derivative has numerator -(3+4q)(1+2 Re p)-K(q)|p|^2 with K(q)>3+4q. If the first bracket is negative, |p|^2+(1+2 Re p)=|1+p|^2>=0 still makes the numerator strictly negative. Thus every finite point has a descending decompactification direction, for arbitrary common axion phase; the canonical W0=1/3,2/3 branch has no simultaneous W=P=0. No finite nonsupersymmetric minimum or Hessian candidate exists, and the orthogonal axion is separately flat.
- **Kind/domain:** `theorem` / `vacuum`
- **Depends on:** [OA-C1044](#oa-c1044), [OA-C1046](#oa-c1046), [OA-C1049](#oa-c1049)
- **Leads to:** [OA-C1007](#oa-c1007), [OA-C1030](#oa-c1030)
- **Closure test:** Evaluate the complete S,T F-term potential with arbitrary common axion phase and the exact negative slope, then prove or disprove existence of any finite critical point in the physical Re(f)>0 domain.
- **Falsifier:** A finite critical point of the certified potential, failure of the monotonicity inequality for a complex condensate sum, or a canonical branch with simultaneous W=P=0.
- **Scope:** The tree-level K=-log(S+Sbar)-3log(T+Tbar) model whose condensates all share the fixed linear kinetic function S+beta T and the canonical positive prefactors. Unequal subgroup thresholds, corrected K, additional superpotentials, five-branes and other branches can invalidate the common-function theorem.
- **Aliases:** `negative-beta full potential`, `common-threshold decompactification theorem`, `nonsupersymmetric fractional-CS escape`
- **Sources:** `../tracks/NEGATIVE_BETA_FULL_POTENTIAL.md`, `../tracks/BETA_THRESHOLD_AUDIT.md`, `../tracks/FRACTIONAL_CS_VACUUM_AUDIT.md`
- **Deepest artifacts:** `../experiments/verify_negative_beta_full_potential.py`, `../experiments/verify_beta_threshold.py`

<a id="oa-c1113"></a>
### OA-C1113 — `PROVED`

- **Question:** In the fixed D5 frame and carrier lock, which 27 directions kinematically preserve matter parity, the lock, or both, and what does the selected clock do to the simultaneous-preservation directions?
- **Answer:** Yes. The exact ledger gives 11 parity-preserving directions, 15 lock-preserving directions and exactly five preserving both; all five are class-10 weight-zero states annihilated by E27. The E6 singlet preserves frame parity but breaks the carrier lock.
- **Kind/domain:** `computation` / `vacuum`
- **Depends on:** [OA-C0011](#oa-c0011), [OA-C1086](#oa-c1086), [OA-C1100](#oa-c1100)
- **Leads to:** [OA-C1119](#oa-c1119)
- **Closure test:** Enumerate all 27 directions with their D5 class, charge and clock weight; compute both Z2 eigenvalues and the clock action exactly.
- **Falsifier:** A different preservation count, a singlet preserving the lock, or one simultaneous-preservation direction moved by the stated clock refutes the corresponding result.
- **Scope:** Necessary kinematic conditions for individual directions in two selected internal gradings. No scalar potential, VEV orbit, stable vacuum, breaking dynamics or mass spectrum is constructed.
- **Aliases:** `outside memo 61`, `VEV_LEDGER`, `parity-lock VEV fork`
- **Sources:** [`../evidence/WAVE5_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE5_BRANCH_DELTA_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/10848a98f3338c75c7c7f1538aac6e6c6cd7e7f9/outside_bench/memos/VEV_LEDGER.md`](https://github.com/originaxiom/origin-axiom/blob/10848a98f3338c75c7c7f1538aac6e6c6cd7e7f9/outside_bench/memos/VEV_LEDGER.md)
- **Deepest artifacts:** [`https://github.com/originaxiom/origin-axiom/blob/10848a98f3338c75c7c7f1538aac6e6c6cd7e7f9/outside_bench/certificates/vev_ledger.py`](https://github.com/originaxiom/origin-axiom/blob/10848a98f3338c75c7c7f1538aac6e6c6cd7e7f9/outside_bench/certificates/vev_ledger.py)

<a id="oa-c1119"></a>
### OA-C1119 — `PROVED`

- **Question:** Does the exhaustive selected-D5 direction test yield exactly two SM-safe singlets, a four-dimensional joint Cartan torus, and loss of both the psi grading and carrier lock?
- **Answer:** Yes. The independently rerun exact certificate finds precisely two SM-safe directions, states 1 and 17. Their joint Cartan stabilizer is four-dimensional and contains color, T3 and Y. Both directions are lock-odd; neither the psi grading nor the lock survives. Fifteen nontrivial root-lattice Z2 gradings remain and are separately classified by OA-C1125.
- **Kind/domain:** `computation` / `vacuum`
- **Depends on:** [OA-C0011](#oa-c0011), [OA-C1100](#oa-c1100), [OA-C1113](#oa-c1113)
- **Leads to:** [OA-C0014](#oa-c0014)
- **Closure test:** Enumerate every color-singlet, weak-singlet, Y-neutral direction in the declared 27, compute the joint Cartan centralizer and both selected Z2 survivals, and certify completeness.
- **Falsifier:** A missed SM-safe direction, a different joint-Cartan dimension, or survival of matter parity or the carrier lock refutes the finite ledger.
- **Scope:** The selected D5/trinification frame, declared 27 roster and necessary algebraic direction tests. This proves no scalar potential, actual VEV, stable vacuum, mass matrix or phenomenology.
- **Aliases:** `THE_MSSM_DEBT D3`, `two-U1 breaking-chain ledger`
- **Sources:** [`../evidence/WAVE5_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE5_BRANCH_DELTA_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/60bcf01db966ae0b13f18c73c24845040b59fd98/outside_bench/memos/UNIQUE_CHAIN.md`](https://github.com/originaxiom/origin-axiom/blob/60bcf01db966ae0b13f18c73c24845040b59fd98/outside_bench/memos/UNIQUE_CHAIN.md)
- **Deepest artifacts:** [`https://github.com/originaxiom/origin-axiom/blob/60bcf01db966ae0b13f18c73c24845040b59fd98/outside_bench/certificates/breaking_chains.py`](https://github.com/originaxiom/origin-axiom/blob/60bcf01db966ae0b13f18c73c24845040b59fd98/outside_bench/certificates/breaking_chains.py)

<a id="oa-c1136"></a>
### OA-C1136 — `REFUTED`

- **Question:** Do CS=0 and Mostow rigidity fix the U(1) phase of a Calabi--Yau holomorphic three-form, leaving only one positive real dilaton freedom?
- **Answer:** No. No map from the three-manifold invariant to the Calabi--Yau canonical-bundle trivialization is supplied. Rescaling Omega by exp(i theta) leaves the m004 hyperbolic structure, CS=0 and Mostow rigidity unchanged, giving an explicit U(1) counterfamily. The claim that only an R+ physical dilaton remains therefore does not follow; even that physical interpretation assumes the heterotic functor.
- **Kind/domain:** `implication` / `vacuum`
- **Depends on:** [OA-C1045](#oa-c1045), [OA-C1053](#oa-c1053)
- **Leads to:** None.
- **Closure test:** Construct a typed map from the m004 CS/Mostow data to the C-star rescaling torsor of the heterotic holomorphic three-form and prove that its U(1) subgroup is fixed.
- **Falsifier:** A family Omega->exp(i theta)Omega preserving all m004 CS and Mostow data refutes phase absorption.
- **Scope:** The attempted inference from m004 CS/Mostow data to the phase of a separately supplied Calabi--Yau holomorphic form. A distinct compactification theorem could add a coupling, but none is present here.
- **Aliases:** `B1166 C3 phase claim`, `CS-Mostow Omega phase`, `one-dilaton reduction`
- **Sources:** [`../evidence/WAVE5_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE5_BRANCH_DELTA_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/bf580f45840d121a811d2b6606c48beac92c3057/frontier/B1166_charter_attack/FINDINGS.md`](https://github.com/originaxiom/origin-axiom/blob/bf580f45840d121a811d2b6606c48beac92c3057/frontier/B1166_charter_attack/FINDINGS.md)
- **Deepest artifacts:** None registered.

<a id="oa-c1150"></a>
### OA-C1150 — `OPEN`

- **Question:** Does the surviving projective Higgs-line freedom reduce to already priced finite labels or one normalization, or does it add up to three independent continuous vacuum inputs?
- **Answer:** Open. B1193 catches an error in the v0 input floor: the P3 Higgs line is not covered by the earlier multiplicity-one argument. Outside tip bc9d381d sharpens the test: its four Higgs slots have four distinct crystal weights, so the line reduces to a finite menu in that frame unless main's B0 block is torus-isotypic. B1195 GC-25 does not settle that comparison because its rational regular-representation stand-in assumes the action on the actual four-dimensional multiplicity space. B1205 cuts a generic P3 by a determinant cubic only to a surface, while a skew-slice control shows that such a determinant can vanish identically; no actual object tensor was evaluated. B1206/B1208 prove the lambda block is either rank zero or two by full SU(2) invariance and that the one-27 H_d menu has only one canonical functional, so those named routes do not add a cut. R024 shows e^c and l share coarse character zero on both retained branches. R025 corrects the lepton tail equation and kills only its one-dimensional pure-tail square; it leaves the three connecting B_2 directions, all mixed terms and the full GL_4-isotypic Higgs/lepton ambiguity intact. B1208's same/independent/absent tensor fork and the exact quotient dimension therefore remain unresolved.
- **Kind/domain:** `classification` / `vacuum`
- **Depends on:** [OA-C0011](#oa-c0011), [OA-C1034](#oa-c1034)
- **Leads to:** [OA-C0014](#oa-c0014)
- **Closure test:** Write the exact projective Higgs parameter space modulo all proved gauge, automorphism and normalization actions, then compute the dimension and identify every surviving input coordinate.
- **Falsifier:** A positive-dimensional quotient refutes absorption into finite labels; a zero-dimensional quotient with a canonical orbit closes the extra input.
- **Scope:** The already selected conditional Higgs sector. This is input accounting, not a derivation of electroweak symmetry breaking, its scale or the observed Higgs mass.
- **Aliases:** `B1193 P3 correction`, `Higgs projective line`, `input-floor adjudication`
- **Sources:** [`../evidence/WAVE6_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE6_BRANCH_DELTA_AUDIT.md), [`../../../memos/LEPTON_CHARACTER_DATUM.md`](../memos/LEPTON_CHARACTER_DATUM.md), [`../../../memos/LEPTON_TAIL_SELECTION_CORRECTION.md`](../memos/LEPTON_TAIL_SELECTION_CORRECTION.md), [`https://github.com/originaxiom/origin-axiom/blob/0f1c627e5c290439e4f6eeb3723fb5d9f83195d7/docs/GRAND_COMPUTATION_v0.md`](https://github.com/originaxiom/origin-axiom/blob/0f1c627e5c290439e4f6eeb3723fb5d9f83195d7/docs/GRAND_COMPUTATION_v0.md), [`https://github.com/originaxiom/origin-axiom/blob/40916c36ddeb1eb1631097b3535c6a79a2658e23/frontier/B1195_close_loop_batch5a/verification/batch5a_cells.json`](https://github.com/originaxiom/origin-axiom/blob/40916c36ddeb1eb1631097b3535c6a79a2658e23/frontier/B1195_close_loop_batch5a/verification/batch5a_cells.json), [`https://github.com/originaxiom/origin-axiom/blob/6bd7aeb8a6acb3fd4a1bb250d15f0e91c6fcf1a3/frontier/B1205_the_dimension_ledger/FINDINGS.md`](https://github.com/originaxiom/origin-axiom/blob/6bd7aeb8a6acb3fd4a1bb250d15f0e91c6fcf1a3/frontier/B1205_the_dimension_ledger/FINDINGS.md), [`https://github.com/originaxiom/origin-axiom/blob/b0d8f37c7205cf43520a0710f6b7c7c66634a0dc/frontier/B1208_cross_seat_harvest/FINDINGS.md`](https://github.com/originaxiom/origin-axiom/blob/b0d8f37c7205cf43520a0710f6b7c7c66634a0dc/frontier/B1208_cross_seat_harvest/FINDINGS.md)
- **Deepest artifacts:** [`../../../certificates/r025_lepton_tail_selection/lepton_tail_selection.py`](../certificates/r025_lepton_tail_selection/lepton_tail_selection.py), [`../../../outputs/r025_lepton_tail_selection.txt`](../outputs/r025_lepton_tail_selection.txt)

## Domain: `values`

<a id="oa-c0016"></a>
### OA-C0016 — `EXTERNAL_BLOCKER`

- **Question:** Does the object emit every dimensionless Standard-Model parameter after thresholds and RG running?
- **Answer:** Not yet. Natural period searches return negative; regulator identification remains unconstructed; sin^2(theta_W)=3/8 is the conditional GUT normalization, not the measured prediction. B1154 distinguishes arithmetic non-overlap from the independent cohomological up-Yukawa emptiness: two walls support the same structure-versus-values diagnosis, but neither supplies a number.
- **Kind/domain:** `computation` / `values`
- **Depends on:** [OA-C0007](#oa-c0007), [OA-C0014](#oa-c0014), [OA-C0015](#oa-c0015)
- **Leads to:** [OA-C0018](#oa-c0018), [OA-C1158](#oa-c1158), [OA-C1161](#oa-c1161)
- **Closure test:** A unique UV solution with stabilized moduli and a complete renormalized observable table.
- **Falsifier:** Free continuous normalization/scale/modulus, post-hoc matching, or a missing threshold/RG map.
- **Scope:** All SM gauge, Higgs, Yukawa, mixing, neutrino, and theta parameters.
- **Aliases:** `parameter-free values`, `B1126`, `B1137`
- **Sources:** None registered.
- **Deepest artifacts:** None registered.

<a id="oa-c0018"></a>
### OA-C0018 — `EMPIRICAL`

- **Question:** Does the completed theory make a successful unused quantitative prediction?
- **Answer:** Empirical evidence only. No current repo value claim satisfies this strict endpoint criterion; several sealed crossings are negative.
- **Kind/domain:** `empirical` / `values`
- **Depends on:** [OA-C0016](#oa-c0016)
- **Leads to:** [OA-C1143](#oa-c1143)
- **Closure test:** Preregister an observable and uncertainty before comparison, then pass independent data.
- **Falsifier:** Miss outside the preregistered band or a comparison used during model construction.
- **Scope:** At least one genuinely held-out observable, followed by the full parameter table.
- **Aliases:** `sealed prediction`
- **Sources:** None registered.
- **Deepest artifacts:** None registered.

<a id="oa-c1059"></a>
### OA-C1059 — `REFUTED`

- **Question:** Can the untwisted m004 Ruelle zeta be a finite product or ratio of ordinary shifted Dirichlet L-functions in the same spectral variable, in particular factors built from zeta and L(chi_-3)?
- **Answer:** No. The logarithm of the Ruelle product has first exponent the m004 systole l0, certified strictly between log(2) and log(3). Any finite shifted ordinary Dirichlet-L product has first surviving exponent log(N) for an integer N at least 2. Uniqueness of absolutely convergent generalized Dirichlet series rules out equality. The quadratic L-factor belongs to the scalar cusp scattering determinant, not to a finite geodesic Euler-product factorization.
- **Kind/domain:** `theorem` / `values`
- **Depends on:** [OA-C0003](#oa-c0003)
- **Leads to:** [OA-C1060](#oa-c1060), [OA-C1061](#oa-c1061), [OA-C1062](#oa-c1062)
- **Closure test:** Compare the generalized-Dirichlet exponent supports in a common half-plane of absolute convergence.
- **Falsifier:** A valid finite factorization whose first nonzero exponent matches the certified m004 systole and all subsequent length-spectrum coefficients.
- **Scope:** Finite products or ratios of ordinary shifted Dirichlet L-functions in the same spectral variable. Rescaled arguments, infinite automorphic products or a separately proved trace-formula transform are different claims.
- **Aliases:** `B8130`, `Ruelle through L(chi_-3)`, `finite shifted Dirichlet-L factorization`
- **Sources:** `../tracks/RUELLE_LFACTOR_AUDIT.md`, `../tracks/WAVE1_DELTA_ADJUDICATION.md`
- **Deepest artifacts:** `../experiments/verify_ruelle_lfactor_no_go.sage`

<a id="oa-c1060"></a>
### OA-C1060 — `EXTERNAL_BLOCKER`

- **Question:** Does the proposed n=2 m004 Ruelle/geodesic factor have a proved cutoff-independent value or analytic continuation at s=2?
- **Answer:** Not yet. B8129 samples three length cutoffs and seven real s values and observes no visible breakdown at s=2, with increasing cutoff sensitivity below it. This is bounded numerical evidence only; it gives no limit, error bound, order-independence proof or analytic continuation.
- **Kind/domain:** `theorem` / `values`
- **Depends on:** [OA-C0003](#oa-c0003)
- **Leads to:** [OA-C1061](#oa-c1061), [OA-C1062](#oa-c1062), [OA-C1104](#oa-c1104), [OA-C1106](#oa-c1106), [OA-C1108](#oa-c1108)
- **Closure test:** Supply a convergence or meromorphic-continuation theorem with the exact twist, normalization and evaluation point, and prove the finite cutoff computation converges to it independently of ordering.
- **Falsifier:** A rigorous divergence/pole theorem at s=2 or cutoff sequences with incompatible limits would refute the claimed finite value.
- **Scope:** The exact n=2 twisted factor and normalization proposed in B1107/B8129, not general existence theory for Ruelle zeta functions.
- **Aliases:** `B8129`, `Ruelle n=2 abscissa scan`, `positive-integer product convergence`
- **Sources:** `../tracks/WAVE1_DELTA_ADJUDICATION.md`, `../tracks/SPECIALIST_RELAYS_2_3_AUDIT.md`
- **Deepest artifacts:** None registered.

<a id="oa-c1063"></a>
### OA-C1063 — `REFUTED`

- **Question:** Does the current proposal define a Beilinson regulator of J3(O), the 27-reality classes or 64 fixed dimensions and a canonical map from it to Standard-Model values?
- **Answer:** No. The real Albert Jordan algebra is not by itself the source of an ordinary Beilinson regulator; no arithmetic scheme/motive, class, degree, target or lattice is specified. '27-reality' is not a motivic class. The claimed 64 fixed dimensions are actually a count 2^6 of sign solutions, not a 64-dimensional space. No compactification/EFT map to normalized SM parameters is defined.
- **Kind/domain:** `repair` / `values`
- **Depends on:** [OA-C0005](#oa-c0005)
- **Leads to:** [OA-C0016](#oa-c0016), [OA-C1064](#oa-c1064)
- **Closure test:** Exhibit a valid arithmetic source object, motivic/K-class, degree and weight, Deligne target and lattice, then a normalized physical observable map selected by the programme.
- **Falsifier:** A standard regulator construction with all those data already present in the claimed OA objects would overturn the type refutation.
- **Scope:** The current OA Tier-B proposal as written. It does not rule out a newly specified arithmetic Albert variety and motivic class.
- **Aliases:** `B8131 Tier B`, `J3(O) Beilinson regulator`, `27-reality and 64-fixed-dimensions regulator`
- **Sources:** `../tracks/TIER_B_REGULATORS.md`, `../tracks/WAVE1_DELTA_ADJUDICATION.md`
- **Deepest artifacts:** `../tracks/TIER_B_REGULATORS.md`

<a id="oa-c1064"></a>
### OA-C1064 — `EXTERNAL_BLOCKER`

- **Question:** Does the object uniquely select an arithmetic Albert-associated scheme or motive, a motivic class and regulator normalization, and a physical functor taking that regulator to a normalized held-out Standard-Model observable?
- **Answer:** Not yet. Arithmetic Albert algebras, twisted Cayley planes, norm varieties and motivic regulators are legitimate mathematical objects, but the current programme selects none of them and supplies no class or observable map. This is a new construction program, not an unperformed scalar calculation and not a present critical-path shortcut.
- **Kind/domain:** `construction` / `values`
- **Depends on:** [OA-C0005](#oa-c0005), [OA-C1063](#oa-c1063)
- **Leads to:** [OA-C0016](#oa-c0016)
- **Closure test:** Construct the number-field model, arithmetic variety/motive, class, degree/weight, Deligne regulator and integral lattice from existing OA data, then derive the compactification/EFT normalization and predict a frozen held-out observable without fitting.
- **Falsifier:** Two inequivalent equally natural motives, classes or physical normalizations from the same antecedent would refute uniqueness; a zero regulator on the only selected class would refute the proposed value mechanism.
- **Scope:** A source-derived replacement for the refuted Tier-B proposal. Arbitrary choice of a motive or fitting a regulator combination to known SM values does not close the item.
- **Aliases:** `well-typed Albert arithmetic replacement`, `twisted Cayley-plane regulator`, `regulator-to-observable functor`
- **Sources:** `../tracks/TIER_B_REGULATORS.md`, `../tracks/WAVE1_DELTA_ADJUDICATION.md`
- **Deepest artifacts:** `../tracks/TIER_B_REGULATORS.md`

<a id="oa-c1074"></a>
### OA-C1074 — `OPEN`

- **Question:** What exact leading coefficient and controlled error term follow from the completed Eisenstein Dedekind zeta function for the specified zero-counting function, and do the banked zeros satisfy that theorem?
- **Answer:** Open. The source proposes a symbolic derivation from earlier scattering data and a bounded 108-zero check. Neither a derivation nor certified error bound is committed.
- **Kind/domain:** `theorem` / `values`
- **Depends on:** [OA-C0003](#oa-c0003)
- **Leads to:** None.
- **Closure test:** Define whether zeros, scattering poles or resonances are counted and with what multiplicity, derive the main term by the argument principle with all conductor/Gamma terms, prove an explicit error bound, and compare the frozen dataset without fitting the coefficient.
- **Falsifier:** A different derived coefficient or a frozen zero count outside the proved error bound refutes the proposed formula; mere visual O(log T) behavior cannot pass.
- **Scope:** The explicitly defined completed zeta/scattering zero count. It is not a graviton determinant or Standard-Model parameter.
- **Aliases:** `outside-campaign C1`, `VI.3(a) Weyl coefficient`, `Dedekind-zeta zero-count main term`
- **Sources:** [`../evidence/WAVE2_CAMPAIGN_INTAKE.md`](program-question-map/evidence/WAVE2_CAMPAIGN_INTAKE.md), [`https://github.com/originaxiom/origin-axiom/blob/0fe97f9070384d9a5a98c625b1b70131de2556f1/outside_bench/CAMPAIGN_CELLS.json`](https://github.com/originaxiom/origin-axiom/blob/0fe97f9070384d9a5a98c625b1b70131de2556f1/outside_bench/CAMPAIGN_CELLS.json)
- **Deepest artifacts:** None registered.

<a id="oa-c1076"></a>
### OA-C1076 — `REFUTED`

- **Question:** Does a preregistered higher-precision asymptotic extraction of the figure-eight Kashaev sequence stabilize to the proposed first coefficient and a bounded-height exact recognition of the second?
- **Answer:** No. The preregistered 120-digit continuation through N=4000 was executed. Only about 17 digits of the first coefficient and 13 digits of the second stabilized, far below the frozen 60-digit gate, and no bounded-height recognition of the second coefficient survived. This is an honest negative for this protocol, not a proof that no asymptotic constant exists.
- **Kind/domain:** `computation` / `values`
- **Depends on:** [OA-C0003](#oa-c0003)
- **Leads to:** None.
- **Closure test:** Freeze the asymptotic convention, sample sizes, precision, extrapolation order, held-out validation points, candidate constant basis and height bound before running; then supply interval/error control strong enough to distinguish the proposed constants.
- **Falsifier:** Failure of the first coefficient on held-out points or absence of a stable second-coefficient relation in the preregistered basis and height bound defeats the scoped recognition claim.
- **Scope:** The declared asymptotic sequence and frozen numerical protocol. A numerical recognition is not an exact theorem without a separate proof.
- **Aliases:** `outside-campaign C3`, `C-D4 C-V2`, `Ohtsuki c1 c2 recognition`
- **Sources:** [`../evidence/WAVE2_CAMPAIGN_INTAKE.md`](program-question-map/evidence/WAVE2_CAMPAIGN_INTAKE.md), [`https://github.com/originaxiom/origin-axiom/blob/0fe97f9070384d9a5a98c625b1b70131de2556f1/outside_bench/CAMPAIGN_CELLS.json`](https://github.com/originaxiom/origin-axiom/blob/0fe97f9070384d9a5a98c625b1b70131de2556f1/outside_bench/CAMPAIGN_CELLS.json)
- **Deepest artifacts:** None registered.

<a id="oa-c1077"></a>
### OA-C1077 — `REFUTED`

- **Question:** Does a preregistered, adequately powered high-zero spacing test support the proposed GUE statistic for the specified zeta-times-L zero sequence?
- **Answer:** No. The later T=3000 run contains 2469 zeta zeros and 2990 L(chi_-3) zeros. Each factor is relatively close to the single Wigner surmise (D=0.04013 and 0.04867), but the merged sequence is not (D=0.13359), so the preregistered single-GUE proposal fails. The distinct two-component finite-data result is recorded separately as OA-C1093.
- **Kind/domain:** `empirical` / `values`
- **Depends on:** [OA-C0003](#oa-c0003)
- **Leads to:** [OA-C1093](#oa-c1093)
- **Closure test:** Freeze the zero sequence, unfolding formula, scan/verification method, sample size, test statistics, alternatives, significance and multiplicity correction before computing thousands of independently checked zeros and reporting power and uncertainty.
- **Falsifier:** A preregistered rejection of the GUE null or a result whose power cannot distinguish it from stated alternatives refutes or withholds the scoped support claim.
- **Scope:** Statistical evidence for one unfolded arithmetic zero sequence. A positive test would not prove a universal random-matrix law or physical quantum chaos.
- **Aliases:** `outside-campaign C4`, `PR-4 large-T GUE`, `high-zero spacing test`
- **Sources:** [`../../../memos/C4_SUPERPOSITION_SCOPE.md`](../memos/C4_SUPERPOSITION_SCOPE.md), [`../evidence/WAVE4_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE4_BRANCH_DELTA_AUDIT.md), [`../evidence/WAVE2_CAMPAIGN_INTAKE.md`](program-question-map/evidence/WAVE2_CAMPAIGN_INTAKE.md)
- **Deepest artifacts:** [`../../../certificates/r009_c4_superposition/superposition_stdlib.py`](../certificates/r009_c4_superposition/superposition_stdlib.py)

<a id="oa-c1093"></a>
### OA-C1093 — `EMPIRICAL`

- **Question:** On the committed T=3000 data, are the merged zeta-times-L spacings relatively closer to the fixed-fraction two-component Wigner-surmise renewal model than to one Wigner surmise, with factor-only controls discriminating the direction?
- **Answer:** Empirical evidence only. A dependency-free rerun gives factor-versus-Wigner D=0.04013 and 0.04867, merged-versus-one-Wigner D=0.13359, merged-versus-two-component renewal D=0.02400, and factor controls D=0.18017 and 0.19138. B1158's exact sine-kernel Gaudin replacement leaves the merged two-component distance at 0.02441. The independently rerun corrected unfoldings in OA-C1110 still leave factor residuals about 0.041--0.051, refuting the proposed unfolding explanation. The relative fit remains finite and empirical, not an independence or exact two-GUE theorem.
- **Kind/domain:** `empirical` / `values`
- **Depends on:** [OA-C1077](#oa-c1077)
- **Leads to:** [OA-C1110](#oa-c1110)
- **Closure test:** Recompute the frozen zero data, unfolding and both CDF distances; require the preregistered relative-distance gate and the factor-only negative controls to pass.
- **Falsifier:** Failure of D_superposition<0.06, failure of D_superposition<D_single/2, or factor controls fitting the two-component model as well as their one-component model refutes the scoped compatibility claim.
- **Scope:** Finite deterministic zero lists, the stated unfolding and a Wigner-surmise renewal approximation. No exact GUE process law, independence theorem, universality or object-specific physics is established.
- **Aliases:** `C4 two-component replacement`, `Memo 55`, `Wigner-surmise renewal superposition`, `R009`
- **Sources:** [`../../../memos/C4_SUPERPOSITION_SCOPE.md`](../memos/C4_SUPERPOSITION_SCOPE.md), [`../evidence/WAVE4_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE4_BRANCH_DELTA_AUDIT.md)
- **Deepest artifacts:** [`../../../certificates/r009_c4_superposition/superposition_stdlib.py`](../certificates/r009_c4_superposition/superposition_stdlib.py), [`../../../certificates/r009_c4_superposition/data/c4_zeros_zeta.txt`](../certificates/r009_c4_superposition/data/c4_zeros_zeta.txt), [`../../../certificates/r009_c4_superposition/data/c4_zeros_L.txt`](../certificates/r009_c4_superposition/data/c4_zeros_L.txt)

<a id="oa-c1110"></a>
### OA-C1110 — `REFUTED`

- **Question:** Does a preregistered corrected finite-height unfolding, including the omitted constant and oscillatory zero-count terms, account for the residual in the committed T=3000 zeta-times-L(chi_-3) spacing data?
- **Answer:** No. Replacing the Wigner surmise by the exact sine-kernel Gaudin law leaves the two-component distance about 0.0244. The outside corrected-unfolding certificate was independently rerun: theta-exact and local-empirical variants leave zeta residuals about 0.0416/0.0406 and L residuals about 0.0502/0.0513. The proposed explanation therefore fails on the frozen finite data; this does not refute or prove an underlying asymptotic law.
- **Kind/domain:** `empirical` / `values`
- **Depends on:** [OA-C1093](#oa-c1093)
- **Leads to:** None.
- **Closure test:** Freeze the completed unfolding formula and error convention, recompute the committed data, and show under held-out controls whether the residual disappears or remains without fitted parameters.
- **Falsifier:** A corrected unfolding that leaves the residual unchanged, needs fitted parameters, or fails factor-only controls refutes the proposed explanation.
- **Scope:** Only the committed finite T=3000 zero lists and a preregistered deterministic re-unfolding. No exact GUE process, independence theorem, universality or physics follows.
- **Aliases:** `B1158 C4 residual`, `finite-height unfolding suspect`, `Gaudin residual`
- **Sources:** [`../evidence/WAVE5_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE5_BRANCH_DELTA_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/bf580f45840d121a811d2b6606c48beac92c3057/frontier/B1158_cloud_wave2_harvest/FINDINGS.md`](https://github.com/originaxiom/origin-axiom/blob/bf580f45840d121a811d2b6606c48beac92c3057/frontier/B1158_cloud_wave2_harvest/FINDINGS.md), [`https://github.com/originaxiom/origin-axiom/blob/60bcf01db966ae0b13f18c73c24845040b59fd98/outside_bench/memos/RESIDUAL_CHARACTERIZED.md`](https://github.com/originaxiom/origin-axiom/blob/60bcf01db966ae0b13f18c73c24845040b59fd98/outside_bench/memos/RESIDUAL_CHARACTERIZED.md)
- **Deepest artifacts:** [`https://github.com/originaxiom/origin-axiom/blob/60bcf01db966ae0b13f18c73c24845040b59fd98/outside_bench/certificates/unfold_close.py`](https://github.com/originaxiom/origin-axiom/blob/60bcf01db966ae0b13f18c73c24845040b59fd98/outside_bench/certificates/unfold_close.py)

<a id="oa-c1143"></a>
### OA-C1143 — `EXTERNAL_BLOCKER`

- **Question:** Can a phason-controlled Aubry-Andre-Harper experiment measure the preregistered number of edge modes in a labelled gap well enough to distinguish the predicted counts five and six?
- **Answer:** Not yet. B1171 adopts B8146's full-text audit: existing 13--28-waveguide demonstrations provide the phason knob but report qualitative localization, no mode count and no uncertainty or resolution for this observable. The experimental route is testable in principle but its readout does not presently exist.
- **Kind/domain:** `empirical` / `values`
- **Depends on:** [OA-C0018](#oa-c0018)
- **Leads to:** None.
- **Closure test:** Commission a labelled-gap mode-count observable with declared site number, error model and held-out phason setting, then distinguish five from six without using the result in model construction.
- **Falsifier:** A measured incompatible count refutes the prediction; inability to identify or count the modes keeps the test blocked rather than confirmed.
- **Scope:** One preregistered condensed-matter analogue count. Passing it would test a structural prediction, not establish the Standard Model or its parameter table.
- **Aliases:** `B8146 L173 readout`, `commissioned edge-mode count`, `5 versus 6 gap test`
- **Sources:** [`../evidence/WAVE6_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE6_BRANCH_DELTA_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/72ace1cf91abae1be356b17e947c08894f255a8b/docs/EDGE_PREREG_SPEC_ADDENDUM_B8146.md`](https://github.com/originaxiom/origin-axiom/blob/72ace1cf91abae1be356b17e947c08894f255a8b/docs/EDGE_PREREG_SPEC_ADDENDUM_B8146.md)
- **Deepest artifacts:** None registered.

<a id="oa-c1158"></a>
### OA-C1158 — `OPEN`

- **Question:** Does the object-normalized weak-mixing trace identity reproduce exactly at the independent full-tower prime 40639 after the required square-root convention transport?
- **Answer:** Open. B895 proves the 40639 hypercharge direction and resolves the 17-versus-11 support discrepancy, but B919's distinct Weinberg-trace run remains one-prime. Its first attempted second-prime flag was caught as a silent substitution failure; the correctly substituted chain reaches the Y anchor but rational reconstruction returns None. The follow-up is explicitly registered and has no later closing arc through B1196.
- **Kind/domain:** `computation` / `values`
- **Depends on:** [OA-C0013](#oa-c0013), [OA-C1121](#oa-c1121)
- **Leads to:** [OA-C0016](#oa-c0016)
- **Closure test:** Transport the full 40639 tower and Y anchor under a versioned per-prime square-root convention, rationally reconstruct all three traces and reproduce Tr(T3^2)=3, Tr(Y^2)=5 and Tr(T3Y)=0 with a deliberately wrong-label control.
- **Falsifier:** A different rational trace triple or failure after a correct convention transport refutes two-prime robustness; silently reusing the first prime withholds closure.
- **Scope:** Robustness of the internal GUT-normalized structural relation sin^2(theta_W)=3/8. It is not the measured low-energy weak angle and does not perform RG running.
- **Aliases:** `B919 second-prime debt`, `40639 Weinberg traces`, `two-prime 3/8 check`
- **Sources:** [`../evidence/WAVE6_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE6_BRANCH_DELTA_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/7a4447d78ce92d3db6e04152105cb841ca163657/frontier/B919_weinberg_traces/FINDINGS.md`](https://github.com/originaxiom/origin-axiom/blob/7a4447d78ce92d3db6e04152105cb841ca163657/frontier/B919_weinberg_traces/FINDINGS.md)
- **Deepest artifacts:** None registered.

<a id="oa-c1159"></a>
### OA-C1159 — `OPEN`

- **Question:** Does object-native arithmetic force the specific D2-twisted Hermitian gauge that carries the hierarchy rather than merely show that this twist is mirror-even and available?
- **Answer:** Open. B928 proves that H_plus D2 is carried uniquely by the already specified composite phi*=tau o phi+ o phi- within its 128-representative census, while B923 proves only that the canonical gauge is generation-degenerate. B928 explicitly warns that the census alone does not pin D2: only 16 outer pairings are symmetric, and the other candidate Hermitian structures have not been tested for generation resolution. Outside memo 92 makes D2-tw mirror-even, but admissibility is not selection. The tip's proposed premise that physics must resolve generations therefore does not leave exactly one tested candidate. The physical gauge remains unforced.
- **Kind/domain:** `uniqueness` / `values`
- **Depends on:** [OA-C1135](#oa-c1135)
- **Leads to:** [OA-C0015](#oa-c0015)
- **Closure test:** Enumerate every admissible Hermitian gauge in the fixed representation, state an object-native invariant independent of desired hierarchy output and prove that it uniquely selects D2-tw; then assemble B928, B923 and the mirror-parity result into one checked theorem.
- **Falsifier:** A second equally admissible gauge, or a selector that references the target hierarchy, refutes forcing; mirror-evenness alone is insufficient.
- **Scope:** Selection of the hierarchy-carrying Hermitian form in the fixed algebraic frame. It does not supply observed mass ratios, RG evolution or a physical vacuum.
- **Aliases:** `B928 twist forcing`, `mirror-even hierarchy carrier`, `hierarchy selection theorem`
- **Sources:** [`../evidence/WAVE6_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE6_BRANCH_DELTA_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/da446a7569e5536c18d0ce1b4605b995d017d3b2/frontier/B928_d2_decode/arc_verdict.json`](https://github.com/originaxiom/origin-axiom/blob/da446a7569e5536c18d0ce1b4605b995d017d3b2/frontier/B928_d2_decode/arc_verdict.json), [`https://github.com/originaxiom/origin-axiom/blob/2d45267727fd34e1ff3f63b735075253b8e66eb5/outside_bench/memos/TWIST_PARITY.md`](https://github.com/originaxiom/origin-axiom/blob/2d45267727fd34e1ff3f63b735075253b8e66eb5/outside_bench/memos/TWIST_PARITY.md), [`https://github.com/originaxiom/origin-axiom/blob/bc9d381d0018cdc112ddac2373fe767ee4247531/outside_bench/THE_SELECTION_THEOREM.md`](https://github.com/originaxiom/origin-axiom/blob/bc9d381d0018cdc112ddac2373fe767ee4247531/outside_bench/THE_SELECTION_THEOREM.md)
- **Deepest artifacts:** None registered.

<a id="oa-c1166"></a>
### OA-C1166 — `OPEN`

- **Question:** Does the explicit norm-953 generator admit an object-native unit normalization and a pipeline-free derivation explaining why that associate enters the hierarchy invariant?
- **Answer:** Open. Class number one and alpha=-26-theta+2theta^2 prove existence and principality. The successor eight-witness proof removes the first certificate's method defect but still neither chooses a unit associate nor proves the downstream divisor equality in a pipeline-independent construction. Outside memos 102/103 sharpen the old gap to the arithmetic meaning of this single element rather than completing a physical explanation.
- **Kind/domain:** `construction` / `values`
- **Depends on:** [OA-C1162](#oa-c1162), [OA-C1163](#oa-c1163)
- **Leads to:** None.
- **Closure test:** Fix the unit orbit of norm-953 generators by an invariant independent of the desired hierarchy, transport the chosen element into the Hermitian divisor calculation and derive the 953 occurrence without preloading source eigenline coordinates.
- **Falsifier:** Several unit associates with no object-native preference, or unavoidable dependence on the already computed hierarchy pipeline, refutes canonical explanation.
- **Scope:** Canonicity and explanatory transport of the exact 953 element. It is not a measured mass ratio or parameter prediction.
- **Aliases:** `953 pipeline-free residue`, `alpha unit normalization`, `B931 sharpened residue`
- **Sources:** [`../evidence/WAVE6_BRANCH_DELTA_AUDIT.md`](program-question-map/evidence/WAVE6_BRANCH_DELTA_AUDIT.md), [`https://github.com/originaxiom/origin-axiom/blob/bc9d381d0018cdc112ddac2373fe767ee4247531/outside_bench/memos/CLASS_GROUP_953.md`](https://github.com/originaxiom/origin-axiom/blob/bc9d381d0018cdc112ddac2373fe767ee4247531/outside_bench/memos/CLASS_GROUP_953.md)
- **Deepest artifacts:** None registered.

## Reading the map correctly

- A `PROVED` row proves only its recorded scope; inspect its dependencies before using it
  downstream.
- An `OPEN` row is a live, typed task; it is neither evidence nor a blocker declaration.
- A `REFUTED` row closes the named route, not every imaginable replacement.
- A `CONDITIONAL` row exposes the exact unpaid input rather than hiding it.
- An `EXTERNAL_BLOCKER` is terminal for the present campaign state but becomes active when
  its stated construction or theorem is supplied.
- New questions discovered during verification must be added before the parent can be called
  exhausted.
