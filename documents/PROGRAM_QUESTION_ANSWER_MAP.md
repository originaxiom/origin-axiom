# Origin Axiom programme question–answer map

**As of:** 2026-08-25

**Canonical questions:** 81

**Registry SHA-256:** `38b145bfd7a42209a7cdfd700e5995b7358f42b750eabf7e89a34279855f3afe`

This is the durable, source-linked map of every canonical question currently registered by
the independent closure campaign. It distinguishes a proved narrow theorem from a broader
physical interpretation. `CONDITIONAL` and `EXTERNAL_BLOCKER` mean the question is accounted
for, not that the parameter-free programme has answered it affirmatively.

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
  --as-of 2026-08-25
```

## Status dashboard

| status | count | meaning |
|---|---:|---|
| `PROVED` | 22 | A type-correct proof or reproducible exact computation establishes the scoped claim. |
| `REFUTED` | 29 | A proof, counterexample, or exact negative computation defeats the scoped claim. |
| `CONDITIONAL` | 13 | The claim follows only after the named underived input is assumed. |
| `EXTERNAL_BLOCKER` | 16 | The required construction or theorem is absent; the unblock condition is explicit. |
| `EMPIRICAL` | 1 | Only bounded numerical or observational evidence is available. |
| `OUT_OF_SCOPE` | 0 | A declared scope rule excludes the question from this campaign. |

## Domain dashboard

| domain | questions |
|---|---:|
| `arithmetic` | 2 |
| `carrier` | 1 |
| `flavor` | 6 |
| `framework` | 3 |
| `genesis` | 2 |
| `geometry` | 17 |
| `lie` | 8 |
| `physics_interface` | 1 |
| `qft` | 8 |
| `spectrum` | 5 |
| `vacuum` | 22 |
| `values` | 6 |

## Complete index

| ID | status | domain | question | direct answer |
|---|---|---|---|---|
| [OA-C0001](#oa-c0001) | `REFUTED` | `genesis` | Does bare not-nothing/minimal description select a unique formal seed independently of encoding? | No. For any computable x, the universal prefix machine U_x with U_x(0)=x and U_x(1p)=U(p) gives x a one-bit description; global minimizers are machine-dependent. |
| [OA-C0002](#oa-c0002) | `CONDITIONAL` | `genesis` | Do the declared primitive, aperiodic, unimodular substitution rules select Fibonacci at minimum lexicographic cost? | Conditionally. Exact enumeration leaves a->ab,b->a up to alphabet exchange/reversal; the category/cost remain an explicit axiom. |
| [OA-C0003](#oa-c0003) | `CONDITIONAL` | `carrier` | Does the Fibonacci substitution canonically determine the oriented punctured-torus mapping torus m004? | Conditionally. Squaring the determinant-minus-one incidence gives RL, but letter-to-Dehn-twist, puncture, orientation, and mapping-torus operations are extra typed data. |
| [OA-C0004](#oa-c0004) | `PROVED` | `arithmetic` | Given m004, does reduction at the ramified Eisenstein prime produce SL(2,F3)=2T? | Yes. Exact reduction and group-generation computation are banked; this is the genuine hyperbolic 2T entrance. |
| [OA-C0005](#oa-c0005) | `PROVED` | `lie` | Does binary tetrahedral 2T determine the affine E6 graph and finite E6 root-system type? | Yes. Classical affine McKay gives affine E6; deleting the trivial-representation node gives the finite E6 Cartan/root-system type, but not a global-group root datum. |
| [OA-C0006](#oa-c0006) | `CONDITIONAL` | `lie` | Does the object select the principal sl2 placement and charged E6 frame used downstream? | Conditionally. Whitehead rigidity does not select a class; the principal adjoint action has only even weights and factors 2T through A4; B1112 leaves a nine-element projective menu and singles A2 only after SM-compatible filtering. |
| [OA-C0007](#oa-c0007) | `REFUTED` | `qft` | Does the mathematical E6 datum uniquely produce a compact four-dimensional quantum gauge theory? | No. A constructive family L(n,g,theta,...) gives infinitely many inequivalent 4d E6 theories sharing the same root datum, 27, and cubic. |
| [OA-C0008](#oa-c0008) | `REFUTED` | `spectrum` | Does the native structure provide three physical copies of a chiral 27? | No. B1033 retracts four internal threes; B876 is one vectorlike 16+bar16 pattern; E8 contains (27,3) and (bar27,bar3), and its sole A2 cannot be both electroweak and family. |
| [OA-C0009](#oa-c0009) | `EXTERNAL_BLOCKER` | `geometry` | Does a native closure have net chiral index N_27-N_bar27=3? | Not yet. Closed doubles have equal 27/bar27 counts; B1084's flat loci intersect on lines; no current 4d Dirac/index functor exists. |
| [OA-C0010](#oa-c0010) | `REFUTED` | `lie` | Can the E8 host simultaneously supply electroweak gauge symmetry and three families? | No. E8\|E6xA2=(78,1)+(1,8)+(27,3)+(bar27,bar3); the one residual A2 is exactly both claimed slots. If used as EW, 3 becomes 2+1 rather than three gauge-identical families. |
| [OA-C0011](#oa-c0011) | `EXTERNAL_BLOCKER` | `vacuum` | Does the object select a rank-reducing Higgs representation, orbit, point, and vacuum? | Not yet. B632 v0 has N=-6, Jordan rank 3 and F4 stabilizer, not the rank-1 Spin10 direction. A Kato-Yukie semistable pencil contains no rank-1 direction; for two rank-1 endpoints N(sA+tB) is identically zero. |
| [OA-C0012](#oa-c0012) | `CONDITIONAL` | `spectrum` | Given the standard compact embedding and correct vacuum, is the unbroken global group (SU3xSU2xU1)/Z6? | Conditionally. The Z6 kernel is standard and B1080 computes it for chosen cascades; no branch derives the physical compact embedding/vacuum antecedent. |
| [OA-C0013](#oa-c0013) | `REFUTED` | `spectrum` | Does the object uniquely select a color-commuting Standard-Model hypercharge? | No. B1102 finds 18 rational target-matching directions and exactly zero commuting with a full color ideal. B1139 searches against preloaded SM Q/Y tables and is a reproduction, not a selector. |
| [OA-C0014](#oa-c0014) | `EXTERNAL_BLOCKER` | `vacuum` | Does the selected vacuum leave exactly the SM light fields and one viable Higgs sector while lifting all exotics? | Not yet. 27=16+10+1 gives one family plus vectorlike exotics/singlet; existing cubic tables give allowed support only. No vacuum or mass-rank proof exists. |
| [OA-C0015](#oa-c0015) | `EXTERNAL_BLOCKER` | `flavor` | Does the object compute nondegenerate fermion masses and realistic inter-family mixing? | Not yet. The E6 cubic fixes support but not coefficients. Restriction through the non-Galois cubic K yields three unordered summands and a diagonal trace cubic. On the stronger heterotic branch, C12 characters permit six symmetric up coefficients and nine down/lepton coefficients, but the actual height-308 holomorphic up map is identically zero. That zero persists under the same-X, fixed-holomorphic-V large-radius Strominger deformation. More strongly, throughout the same BCDD monad topology the unique exact-spectrum H_u is the ambient-injected class, so coefficient variation cannot make its up coupling nonzero without adding Higgs/mixing data or changing the construction. The down/lepton map, Hd line, normalized metrics, thresholds and RG flow remain absent. |
| [OA-C0016](#oa-c0016) | `EXTERNAL_BLOCKER` | `values` | Does the object emit every dimensionless Standard-Model parameter after thresholds and RG running? | Not yet. Natural period searches return negative; regulator identification remains unconstructed; sin^2(theta_W)=3/8 is the conditional GUT normalization, not the measured prediction. |
| [OA-C0017](#oa-c0017) | `EXTERNAL_BLOCKER` | `qft` | Does the object uniquely produce four-dimensional spacetime and a gravitational quantum dynamics? | Not yet. B1104 finds no canonical suspension section; filling is nonunique; S=-Vol*sigma is an on-shell value rather than a 4d gravitational action. |
| [OA-C0018](#oa-c0018) | `EMPIRICAL` | `values` | Does the completed theory make a successful unused quantitative prediction? | Empirical evidence only. No current repo value claim satisfies this strict endpoint criterion; several sealed crossings are negative. |
| [OA-C0019](#oa-c0019) | `REFUTED` | `geometry` | Can a whole-group affine cocycle turn a transverse B1111 pair into an isolated order-24 enhancement point? | No. Averaging proves every affine 1-cocycle is a coboundary. All loci share one full-group fixed point, whose stabilizer has order 96. An order-24 pair is also the wrong E7 enhancement type. |
| [OA-C0020](#oa-c0020) | `EXTERNAL_BLOCKER` | `geometry` | Is there a unique object-selected compact singular geometry with exactly three same-sign E7-to-E6 enhancements and no others? | Not yet. The flat B1084 isotropy is not binary-octahedral and its intersections are lines. A trivial oriented rank-3 section on a closed oriented 3-manifold cannot have total signed zero count +3. |
| [OA-C1000](#oa-c1000) | `PROVED` | `arithmetic` | Does the marked conductor-four cusp reconstruct the ring class field Q(zeta_12), the product fan dP6 x dP6, and the published free C12 toric action? | Yes. The marked order O_4=Z[2 sqrt(-3)] has ring class field H=Q(zeta_12); its two Eisenstein eigensummands give dP6 x dP6, and an explicit determinant-one basis change identifies multiplication by zeta_12 with the published A_N and twelve-cycle. |
| [OA-C1001](#oa-c1001) | `CONDITIONAL` | `geometry` | Does the primitive multiplicative norm law select a smooth fixed-point-free anticanonical hypersurface in the reconstructed C12 toric family? | Conditionally. For H=Q(zeta_12), trace-dual field norms give invariant orbit weights 0,1,1,1,4 and exact computation proves smoothness and free C12 action; the load-bearing multiplicativity principle remains open. |
| [OA-C1002](#oa-c1002) | `REFUTED` | `qft` | Does the class-field and toric data themselves select the ten-dimensional heterotic physical-realisation functor and its compactification framework? | No. The same selected CY3 with h11=1,h21=4 has standard type-IIA and type-IIB compactifications with inequivalent 4d N=2 multiplet counts (1 vector,5 hypers) and (4 vectors,2 hypers), while heterotic E8xE8 requires extra left/right worldsheet, GSO and bundle data and gives N=1. Thus the arithmetic/toric antecedent has multiple physical-realisation functors. Retaining V_E8 in a c=16 chiral completion conditionally forces E8^2, but that retention and the heterotic worldsheet are additional physical premises, not properties of the CY3. |
| [OA-C1003](#oa-c1003) | `CONDITIONAL` | `lie` | Given a heterotic CY3 with full SU(3) holonomy and index-one standard embedding, does the McKay E6 type select the E8 x E8 gauge-lattice branch and active E8 commutant? | Conditionally. McKay gives finite E6; under the explicit assumptions, E8 x E8 has active commutant E6 while Spin(32)/Z2 gives so(26)+u(1). The result is an elimination theorem, not a derivation of heterotic theory or later bundle/vacuum data. |
| [OA-C1004](#oa-c1004) | `EXTERNAL_BLOCKER` | `geometry` | Does the class-field norm hypersurface select and stabilize one locally free stable equivariant SU(5) bundle map with the exact-MSSM branch kernel? | Not yet. The norm section selects coefficients but raw norm reuse has the wrong Euler kernel; the (3,4) BCDD branch is an 11-dimensional map family with ten genuine descended bundle-moduli directions. A marked pseudoinverse map is now proved equivariant, locally free, H0(V)=0, and pointwise-surjective on the 372-to-312 map, but its Hoppe wedge vanishings, 18-to-21 Cech blocks, and selector inputs remain unproved. No stabilizing equation selects it. |
| [OA-C1005](#oa-c1005) | `CONDITIONAL` | `spectrum` | Does the primitive cyclotomic source canonically force the hypercharge Wilson character to reuse the same odd-primary power as the bundle branch? | Conditionally. Primitive characters rho with bundle pair {rho^3,rho^4} reproduce exactly four Table-3 branches; reusing rho^4 selects one four-model orbit and rho^-4 the other. The primary construction treats the two Wilson factors as independent, so the rule remains conditional. |
| [OA-C1006](#oa-c1006) | `CONDITIONAL` | `spectrum` | Under the selected heterotic framework, smooth free quotient, stable SU(5) bundle branch, and Wilson character, does the visible charged massless sector equal three chiral MSSM generations plus one Higgs pair? | Conditionally. The audited BCDD branches have index three and exact visible charged MSSM massless content after Wilson projection, conditional on the heterotic realization and generic stable branch. Hidden E8, neutral moduli, couplings, and dynamics remain outside the phrase visible spectrum. |
| [OA-C1007](#oa-c1007) | `EXTERNAL_BLOCKER` | `vacuum` | Does the selected class-field heterotic construction determine an isolated stable vacuum and all normalized low-energy parameters? | Not yet. The selected section does not stabilize bundle, Kahler, dilaton, or other moduli; the BCDD branch has genuine P10 bundle deformations. On the strict CY branch the exact compact (0,2) GLSM lies in the Beasley--Witten vanishing class, so genus-zero worldsheet terms cannot select that P10. The class-field action now conditionally selects one hidden E8 lift and a combined order-three secondary class, but the no-B strict branch then fails level matching. A published large-radius Strominger theorem supplies a same-topology torsional solution preserving the visible spectrum, not the prescribed differential class or a vacuum. The exact height-308 up-type cup product is zero and remains zero along that fixed-holomorphic-data Strominger curve. The exact universal hidden threshold is negative, refuting the economical supersymmetric fractional-CS condensate solution; normalizer symmetry leaves three complex-structure equations, and no down Yukawa, normalized periods, subgroup thresholds, prefactors, all-moduli mass matrix, SUSY-breaking scale or RG output is derived. |
| [OA-C1008](#oa-c1008) | `REFUTED` | `flavor` | Does the Hesse/equianharmonic period shortcut furnish an intrinsic BCDD H3 invariant and a normalized MSSM Yukawa or flavor prediction? | No. The audited Hesse chain conflates the Schoen Z3xZ3 model with BCDD, does not construct a BCDD weight-three VHS map, and computes neither SU(5)-bundle cup products nor matter metrics; a Hesse connection coefficient is not a normalized MSSM Yukawa. |
| [OA-C1009](#oa-c1009) | `PROVED` | `lie` | Does the class-field trace/codifferent lattice determine one positive C12-equivariant E8 isomorphism class after completion? | Yes. Primitive positive trace forms on O_H and its codifferent give A2^4; eight tetracode glues complete to E8, exactly four are C12-invariant, and the positive-metric C12 centralizer is transitive on those four. Thus the completed positive C12-lattice has one structured isomorphism class. |
| [OA-C1010](#oa-c1010) | `REFUTED` | `lie` | Do the present class-field markings select one evaluation-preserving E8 glue representative and physical gauge embedding? | No. The four invariant glues are the graphs of plus-or-minus (1 plus-or-minus zeta)delta. Trace evaluation leaves two two-orbits and exact delta leaves four singleton choices; moreover zeta^4 has fixed rank zero on an A2^3 complement while the McKay E6 arm rotation has fixed rank two. |
| [OA-C1011](#oa-c1011) | `PROVED` | `qft` | Does the positive E8 lattice isomorphism class determine a unique holomorphic c=8 lattice-VOA isomorphism class with e8 level-one currents? | Yes. The even unimodular E8 lattice gives V_E8 with c=8 and 8+240=248 weight-one states; under the standard strong-rationality hypotheses this is the unique holomorphic c=8 VOA isomorphism class. |
| [OA-C1012](#oa-c1012) | `PROVED` | `geometry` | Does the marked equal-weight pseudoinverse define an equivariant locally-free rank-five bundle candidate with the certified pointwise base cohomology maps? | Yes. Exact Q(zeta12) linear algebra and good-prime unit/minor certificates prove equivariance, local freeness, H0(V)=0, the displayed matter cohomologies, and rank312. The construction still uses unforced target directions, coefficient metric, and relative weight. |
| [OA-C1013](#oa-c1013) | `PROVED` | `geometry` | Does the arithmetic bundle candidate pass pointwise Hoppe stability, given that its exact wedge-square cohomology and MSSM Higgs projection are now certified? | Yes. At the exact norm-308 point, p=1 and p=4 vanish, the reconstructed Cech 18-to-21 map has rank 16 with determinant-twisted cohomology chi0+chi1, and the quotient map has rank312. The pointwise exterior certificates give induced ranks 27 on H0(Lambda2 G) and 68 on H0(Lambda3 G), hence H0(Lambda2 V)=H0(Lambda3 V)=0. Hoppe's criterion on the h11=1 quotient therefore proves slope stability at this named arithmetic point. |
| [OA-C1014](#oa-c1014) | `PROVED` | `qft` | Among positive even-unimodular rank-sixteen lattice or strongly rational holomorphic c=16 VOA completions that retain the selected E8 as a primitive orthogonal lattice subobject or full regular conformal factor, is E8 x E8 unique? | Yes. Because det(E8)=1, an isometric E8 inclusion in a unimodular rank-sixteen lattice splits integrally as E8 plus its orthogonal complement; that complement is the unique rank-eight E8 lattice. In the regular conformal-coset VOA setting, holomorphic V_E8 forces the c=8 commutant to be V_E8, so V_D16+ cannot contain it compatibly. Complement C12 action/lift data remain free. |
| [OA-C1015](#oa-c1015) | `CONDITIONAL` | `qft` | Given the conservative critical-worldsheet realization axiom, do the selected CY3 and V_E8 force a four-dimensional E8 x E8 heterotic parent? | Conditionally. For conventional heterotic matter, D+c_g=26 and 3D/2=15 give D=10 and c_g=16. A CY3 consumes six real target dimensions, leaving four; extension without erasure forces the c=16 gauge receiver to V_E8 tensor V_E8. All conclusions remain conditional on the composite physical-realization axiom. |
| [OA-C1016](#oa-c1016) | `REFUTED` | `geometry` | Do the no-source heterotic Bianchi identity, full SU(3) tangent holonomy, and McKay E6 compatibility force the visible index-one standard embedding V=TX with F=R? | No. BCDD construct stable irreducible rank-five SU(5) deformations of TX+O+O on the selected Z12 construction. Characteristic classes are preserved, and their anomaly equation is saturated with trivial hidden bundle and [C]=0. This witness has the same no-source c2 balance as TX but different rank and SU(5), so it is not gauge-equivalent to TX; full SU(3) is a property of TX and does not change that. A literal H=0 differential solution is additional data and is not inferred from the class equation. |
| [OA-C1017](#oa-c1017) | `REFUTED` | `vacuum` | Does one pure hidden-E8 gaugino condensate stabilize the dilaton and the single Kahler modulus of the selected quotient? | No. For K=-log(S+Sbar)-3log(T+Tbar), f_h=S and W=A exp(-2 pi S/30), exact no-scale cancellation gives V=\|A\|^2 exp(-a x)(a x+1)^2/(x y^3). Its logarithmic derivatives are strictly negative in x and y, and both axions are flat, on all 30 branches. The same x-stationarity obstruction holds for a selected positive linear threshold f_h=S+beta T. Extra condensates, fluxes, thresholds or corrections are new data. |
| [OA-C1018](#oa-c1018) | `REFUTED` | `vacuum` | Can an integral quantized heterotic H-flux class on the fixed C12 quotient supply a parameter-free W0 or stabilize the remaining moduli on the strict Calabi--Yau branch? | No. The integral quotient certificate gives H_2=Z and H^4=Z; UCT, Poincare duality, and b3=2(h21+1)=10 give H^3(X,Z)=Z^10 with no torsion. Thus integral topological flux has an infinite menu and no selected lattice vector. On the strict Kahler CY N=1 branch H=d^cJ=0; in the H-only 4d F-term truncation D_S W=0 and D_z W=0 force H=0. This does not exclude finite-order secondary characters in H^3(X,R/Z): OA-C1044 proves a conditional order-three class, which instead leaves the strict (0,2) CY branch and requires a fractional-CS/condensate or non-Kahler completion. |
| [OA-C1019](#oa-c1019) | `EXTERNAL_BLOCKER` | `vacuum` | Does the class-field C12 action select a hidden-E8 Wilson line with pure asymptotically-free factors, and does the resulting fractional-CS/condensate system isolate the heterotic vacuum? | Not yet. The old unrestricted problem has 270 Kac classes, but the retained class-field lattice automorphism now selects one Weyl class and one compact lift after the equivariant heterotic-retention clause. Its hidden centralizer is A2+A1^3+U1^3 and its universal c2 is 2 mod 12; the native rho^4-to-SU3-center alternative instead has c2=0. This closes the finite conjugacy menu conditionally, not the vacuum: tree-level factors share f=S, the exact parent hidden slope is -3/(2 pi^2), and the economical fractional-CS supersymmetry equation has no positive-volume solution. The large-radius Strominger theorem supplies a compatible local torsional geometry, but normalized periods, subgroup kinetic functions, determinant prefactors/phases, the global order-three lift and an isolated vacuum remain open. |
| [OA-C1020](#oa-c1020) | `REFUTED` | `flavor` | Do the certified C12 cohomology characters and SU(5) cubic force parameter-free three-family up/down/lepton Yukawa textures? | No. The exact character certificate gives three family copies and one Higgs pair but leaves Sym^2(C^3), dimension 6, for up Yukawas and C^3 tensor C^3, dimension 9, for down/lepton Yukawas; no C12 texture zeros occur. SU(5) supplies only up symmetry and the holomorphic transpose relation Y_e=Y_d^T. Cup-product coefficients, the Hd line in the fourfold chi0 space, matter metrics, canonical normalization, vacuum, thresholds and RG data remain unfixed. |
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
| [OA-C1034](#oa-c1034) | `CONDITIONAL` | `flavor` | Do the exact norm-308 monad and selected C12/Wilson sectors yield evaluated holomorphic up and down/lepton Yukawa cup-product maps with determined ranks and Higgs line? | Conditionally. At the exact height-308 stable point, character arithmetic allows Sym2(C3) of dimension 6 and C3 tensor C3 of dimension 9, with no C12 texture zeros. The actual up-type map is nevertheless identically zero: H1(G_Y)=0 makes every matter class map to zero in the ambient extension, while H1(K1)=H2(K1)=0 uniquely lifts the Higgs class, so cup-product naturality forces mu_u=0. Thus all renormalizable holomorphic up-quark Yukawas vanish on this exact-six factorisation locus. The old down-sector 33-versus-38 gap is closed: the connecting quotient has dimension 33 and H1(Y,Lambda2G) supplies the five-dimensional Serre-dual tail with raw characters chi0+chi2+chi4+chi6+chi8. An exact good-prime construction gives a 672x33 representative matrix, proves invariance of the 27-dimensional image, and diagonalizes the quotient; adding the tail gives raw 3Reg+chi1+chi2, whose chi_-2 determinant twist is exactly physical 3Reg+chi0+chi11. The five-dimensional term now also has explicit dual-cokernel/Serre-dual functionals at GF(1009), with inverse-phase labels 0,2,4,6,8; these are not yet raw Lambda2G-valued Cech-one cocycles. A common connecting-sector chain model reduces the first physical Q8 x dc4 x Hd0 slice to one explicit missing determinant/residue trace row of shape 1x18. Hu=C0 is one-dimensional, but B0 is a four-dimensional trivial module, leaving an unselected P3 of Hd lines. The evaluator still lacks a completed Q(zeta12) chain model, chain-level Serre trace for the five tail classes, the determinant/residue row and the resulting P3 matrix pencil. |
| [OA-C1035](#oa-c1035) | `PROVED` | `geometry` | Can quadratic or higher Kuranishi obstruction theory isolate the proved-stable height-308 bundle and its simultaneous complex-structure deformation? | Yes. The stable locally-free height-308 point lies on an actual P10 of inequivalent bundles, so no Kuranishi term can isolate those ten directions. The multiplicative hyperExt filtration makes the fixed-bundle symmetrized quadratic map Sym^2 Ext^1(V,V)->Ext^2(V,V) rank zero. Pure complex-structure directions and all forty P*C terms lift through the exact full-incidence rank (30,30). The two adjacent U orbit classes lift to the full ambient monad because H1_Z(Hom(A,B)+Hom(B,C))=0 and the invariant Hom(B,C)->Hom(A,C) ranks equal their target dimensions (5,4,4,4,4,4). These lifts are independent of the anticanonical equation, so all eight U*C End(V)-projected products vanish. The complete quadratic End(V) projection on P+U+C is therefore zero; higher U terms and the other tangent/hermitian/anomaly components of the full heterotic L3 remain uncomputed. |
| [OA-C1040](#oa-c1040) | `REFUTED` | `vacuum` | Can the selected visible C12 Wilson line on the MSSM branches generate a nonzero flat Cheeger--Chern--Simons class and thereby supply the missing fractional W0 or flux selector? | No. The fundamental SU5 weights are (-2k,-2k,-2k,3k,3k), with c1=0 and c2 coefficient -15 k^2 mod 12. For k=4 and k=8 this is zero. Since positive-degree real cohomology of finite C12 vanishes, the Bockstein H3(BC12,R/Z)->H4(BC12,Z)_tors is an isomorphism, so the associated flat Cheeger--Chern--Simons class is zero and remains zero after pullback to X. |
| [OA-C1041](#oa-c1041) | `REFUTED` | `vacuum` | Does the native class-field character rho^4 into the center of the regular SU3 subgroup of E8 generate a nonzero fractional hidden Chern--Simons class? | No. The defining SU3 weights are (4,4,4), so c2=e2(4,4,4)=48=0 mod 12. The regular SU3 in E8 has Dynkin index one, hence no hidden normalization changes the zero. The Bockstein flat Cheeger--Chern--Simons character is therefore zero. A full 270-class control census finds 249 nonzero alternatives, so the vanishing is specific rather than vacuous. |
| [OA-C1042](#oa-c1042) | `CONDITIONAL` | `geometry` | Does the explicit height-76 (3,4)-branch bundle candidate pass both pointwise Hoppe exterior gates, and is it selected or proved minimal by the available cyclotomic and lattice data? | Conditionally. The exact Lambda2 and Lambda3 exterior presentations give induced ranks 27 and 68 at height 76, proving both vanishings pointwise and hence Hoppe stability on the fixed h11=1 free quotient. The height-76 map is C12-fixed and fixed by the 12-element marked norm/C12 subgroup, but that subgroup fixes the full 35-dimensional equivariant map space; the candidate lies outside the rank-10 trace/power/Hermitian/norm tensor span. Exact norm-32 shell enumeration remains available, while the finite rank-44 domain 33<=q<76 was not exhaustively completed because PARI qfminim exceeded stack/memory limits and the independent Fincke--Pohst attempt was stopped. No global minimality or basis-free selector theorem is claimed. |
| [OA-C1043](#oa-c1043) | `PROVED` | `vacuum` | Does the retained class-field C12 lattice action determine a unique compact-E8 lift, and what hidden centralizer and secondary class does that lift have? | Yes. The complete W(E8) census has one order-twelve class with characteristic Phi12^2 and det(1-w)=1. Thus 1-w is a torus automorphism and all normalizer lifts are conjugate; an exact 248-dimensional check gives order 12. The unique Kac row (1,0,0,1,0,0,1,0,1) has centralizer A2+A1^3+U1^3 and basic c2=2 mod 12. The Cartan--Leray edge map H3(X)->Z/12 is onto, so its flat character pulls back with exact order six. The element cannot commute with the same-factor standard SU3 and is physically usable only in the hidden E8 on the conditional equivariant-retention branch. |
| [OA-C1044](#oa-c1044) | `CONDITIONAL` | `vacuum` | Do the successful visible bundle-equivariant branches and the class-field hidden E8 lift combine into a nonzero, same-source heterotic secondary Chern--Simons character? | Conditionally. For V0=L_t tensor (TX+L_n1+L_n2), all four successful pairs give c2hat(V0)-c2hat(TX)=2 mod 12, an order-six flat character. The hidden lift gives another +2. Hence c2(TX)-c2(Vvis)-c2(Vhid)=-4=8 mod 12, exact order three; reversing conventions changes only the sign. The primary H4 class still vanishes. For generic V308 the Chern--Weil difference need not be flat, but the holomorphic CS value is locally constant modulo periods along a connected integrable deformation. The nonzero secondary requires fractional CS/H flux and leaves the strict N=1/(0,2) CY branch unless another sector cancels or backreacts. |
| [OA-C1045](#oa-c1045) | `PROVED` | `vacuum` | What exact cycle functional does the class-field E8 secondary character define on H3(X), and does it determine a normalized holomorphic period or W0? | Yes. H3(X,Z)=Z^10 maps surjectively to H3(BC12,Z)=Z/12. In an adapted integral basis the map is n->n1 mod 12, and c2=2 evaluates as chi(n)=n1/6 mod 1, an exact primitive sixth-root phase. The conditional codifferent-norm law nominates an algebraic complex-structure basepoint and residue form up to scale, but no marked H3 chain/sLag basis, period vector or physical Omega normalization has been constructed. The topology therefore fixes a phase/coset, not an additive parameter-free W0. |
| [OA-C1046](#oa-c1046) | `REFUTED` | `vacuum` | Does the conditional order-three secondary class and the selected hidden centralizer produce a weakly-coupled, large-volume supersymmetric vacuum on the fixed BCDD bundle allocation? | No. For K=-log(S+Sbar)-3log(T+Tbar) and one condensate depending on S+beta T, supersymmetry requires beta(T+Tbar)=3(S+Sbar); common thresholds also leave the orthogonal axion flat. OA-C1049 proves beta_hidden=-3/(2 pi^2) on the fixed positive Kahler ray, so the required equality is impossible for positive saxions. The naive 1/3 and 2/3 normalizations moreover place the selected SU3/SU2 factors at strong coupling for canonical prefactors. Subgroup-specific thresholds, altered instanton allocation, five-branes, non-Kahler corrections or extra terms are different branches and remain unselected. |
| [OA-C1047](#oa-c1047) | `REFUTED` | `vacuum` | Does the full finite normalizer symmetry of the codifferent-norm section force all complex-structure derivatives of the residue or Chern--Simons superpotential to vanish? | No. The order-48 fan normalizer acts on the four-dimensional projective tangent as three trivial characters plus one sign character. Both the residue three-form and the universal c2/CS character are invariant because every fan matrix has determinant +1 and every unit a mod 12 has a^2=1. Symmetry therefore kills only the odd derivative and leaves three invariant complex-structure derivatives unconstrained. |
| [OA-C1048](#oa-c1048) | `REFUTED` | `framework` | Can the nonzero combined class-field secondary character coexist with the strict zero-H BCDD Calabi--Yau `(0,2)` GLSM without an additional Green--Schwarz differential trivialization? | No. The conditional visible and selected hidden coefficients add to 4 mod 12, exact order three. H4(X,Z)=Z is torsion-free, so a Green--Schwarz/Wess--Zumino differential compensator can cancel the global determinant phase, but it introduces torsionful H and exits the certified strict-CY `(0,2)` GLSM. Ordinary cyclic discrete torsion cannot repair this because H2(C12,U(1))=0. Thus the smooth flat bundle is allowed, while the simultaneous no-B strict branch is not. |
| [OA-C1049](#oa-c1049) | `PROVED` | `vacuum` | What is the exact universal one-loop linear Kähler threshold on the selected quotient and fixed visible-standard/hidden-trivial bundle allocation? | Yes. Adjunction on the anticanonical hypersurface gives integral_Y D c2(TY)=144. Division by the free C12 action and primitivity of the descended divisor gives integral_X J c2(TX)=12. In the GKL convention and with c2(Vvis)=c2(TX), c2(Vhid)=0, the parent coefficients are beta_visible=+3/(2 pi^2) and beta_hidden=-3/(2 pi^2). The flat class-field Wilson changes only secondary data, not this primary pairing; subgroup-specific massive thresholds remain uncomputed. |
| [OA-C1050](#oa-c1050) | `REFUTED` | `vacuum` | Does the finite normalizer of the selected class-field E8 holonomy act transitively on the three hidden SU(2) factors and thereby force equal thresholds, determinants and condensate phases? | No. Exact Weyl computation gives \|N_W(<w>)\|=1152 and \|C_W(w)\|=288. Because det(1-w)=1 removes torus-lift ambiguity, N_E8(<g>)/C_E8(g) is (Z/12)^*=V4. Any homomorphism V4->Out(A1^3)=S3 has image at most C2, so it cannot act transitively on the three SU2 ideals. The parent E8 still proves the common tree-level f_i=S, but one-loop functions, determinant prefactors and condensate phases require explicit quantum data; symmetry-related noninvariant points are different backgrounds, not equal terms in one vacuum. |
| [OA-C1051](#oa-c1051) | `PROVED` | `framework` | Does the selected quotient and certified stable V308 admit a compact same-topology non-Kähler Strominger-system solution that preserves the visible charged spectrum? | Yes. The Andreas--Garcia-Fernandez implicit-function theorem applies to the compact Calabi--Yau X and degree-zero stable V308 with c1=0 and c2(V)=c2(TX). For sufficiently large radius it gives a curve of conformally balanced Strominger solutions while leaving the holomorphic structure of V fixed and the tangent holomorphic structure isomorphic to the original. Hence pi1, index, bundle cohomology, Wilson projection and the audited visible charged MSSM spectrum persist. The theorem does not prescribe the order-three Cheeger--Simons class, select the radius/moduli, or provide an all-orders string vacuum. |
| [OA-C1052](#oa-c1052) | `REFUTED` | `vacuum` | Can the full two-field F-term potential on the fixed negative-threshold branch possess a finite nonsupersymmetric stationary point even though its supersymmetric equations have no positive-volume solution? | No. With b=-beta>0, z=(S+Sbar)-b(T+Tbar)>0 and q=b(T+Tbar)/z, the potential factors as b^3\|W\|^2 z^-4 F(p,q)/((1+q)q^3). Its q derivative has numerator -(3+4q)(1+2 Re p)-K(q)\|p\|^2 with K(q)>3+4q. If the first bracket is negative, \|p\|^2+(1+2 Re p)=\|1+p\|^2>=0 still makes the numerator strictly negative. Thus every finite point has a descending decompactification direction, for arbitrary common axion phase; the canonical W0=1/3,2/3 branch has no simultaneous W=P=0. No finite nonsupersymmetric minimum or Hessian candidate exists, and the orthogonal axion is separately flat. |
| [OA-C1053](#oa-c1053) | `EXTERNAL_BLOCKER` | `framework` | Is the selected order-three differential Chern--Simons component explicitly realized and transported on the large-radius Strominger family? | Not yet. The order-three anomaly is a flat degree-four differential character in H3(X,R/Z), whereas a closed ordinary B-gerbe class is degree three with flat subgroup H2(X,R/Z); adding such a flat class does not alter the degree-four anomaly. Because the integral characteristic difference vanishes, Redden's differential-cocycle theorem guarantees abstract geometric trivializations even when the differential character q is nonzero; they form an Hhat3(X)-torsor. Thus q obstructs only a stricter parallel zero-target trivialization, not a Green--Schwarz/String structure in the standard geometric sense. A pathwise result further shows that, once one marked endpoint trivialization and actual connection path are supplied, differential Chern--Weil transgression continues it along the contractible AGF interval with no additional loop/monodromy obstruction. What AGF does not supply is the visible/tangent differential refinement realizing the conditional universal q, gauge-fixed connection representatives, a selected member of the trivialization torsor, a marked H3 basis, or period normalization. The blocker is explicit realization and normalization, not abstract existence. |
| [OA-C1054](#oa-c1054) | `PROVED` | `flavor` | Does the exact height-308 up-type cup-product zero persist on the same-X, fixed-holomorphic-V large-radius Strominger branch? | Yes. OA-C1034 proves that the entire height-308 holomorphic up map vanishes, not merely selected character components. The AGF existence curve keeps X and the holomorphic structure of V308 fixed and changes Hermitian/HYM/tangent-connection data. Dolbeault cohomology and its wedge/contraction maps are therefore transported isomorphically, so the full and Wilson-projected up tensor remain rank zero. Invertible matter-metric normalization cannot turn zero into nonzero. Thus all three up-type quarks receive no mass from this renormalizable operator along the proved branch; a different holomorphic bundle/complex structure, heavy-field mixing, torsional worldsheet effect, spacetime nonperturbative term or SUSY-breaking operator would be new data and must be computed separately. |
| [OA-C1055](#oa-c1055) | `PROVED` | `flavor` | Does retaining exactly one massless up-type Higgs inside the same BCDD monad topology force that Higgs into the ambient image and its renormalizable up Yukawa to remain zero under coefficient variation? | Yes. For every locally-free map in the same monad topology, H1(G_X)=0 and Serre duality from H2(K1*)=0 gives H1(K1)=0. Hence H1(Lambda2 G_X*) injects equivariantly into H1(Lambda2 V*) and, after the determinant twist, contains chi0+chi1. Wilson k=4 or8 selects the unique audited H_u from the injected chi0. Naturality sends both matter inputs to zero in H1(G_X), so every coupling to that Higgs vanishes. A rank jump can help only by adding a nonambient chi0, which gives at least a second massless H_u before a separately derived mass/mixing mechanism. Therefore coefficient variation alone cannot repair Y_u while preserving the exact cohomological MSSM spectrum. |
| [OA-C1056](#oa-c1056) | `PROVED` | `physics_interface` | For the specified m004 holonomy, Gieseking beat section and selected A1 embedding, does exactly one checked sign-lift admit the semilinear beat relation and does the 27 restrict as six doublets plus fifteen singlets? | Yes. At Golden commit 4a1e4cc3 all 46 top-level certificates independently exit zero. spin_payment proves the fixed-beat sign-target dimensions {(+,+):1, others:0}; sp2_seat proves weights 6(-1)+15(0)+6(+1), nontrivial central parity, relator +I and the three beat identities on the selected A1 module. Local B1145 at 9a4eca7e independently rebuilds the E6/27 matrices from banked B1102 machinery, verifies all 3003 brackets and reproduces the same identities; its five fast locks pass. B8132 shows that the count of two spin structures is shared by several family members. The ten-word inner-modification block is not exhaustive, no typed tangent-frame Pin/spin lift or four-dimensional spin/QFT/index is constructed, and the result does not establish physical fermions or generations. |
| [OA-C1057](#oa-c1057) | `PROVED` | `lie` | For the four accepted distinguished-nonregular E6 characteristics, do the exact triples have orbit dimensions 58, 64, 66 and 70 with parity even, odd, even and even on the 27, and do all eleven accepted odd representatives satisfy the selected-beat identities? | Yes. The locked cp1_strata.py rerun is byte-identical to its stored output and gives the four dimensions 58/64/66/70 with parity even/odd/even/even. The hostile SHA-pinned extension verify_cp1_all_odd.py recomputes all accepted odd rows; all 11/11 pass relator=I, Omega^2=A27 and both intertwiners exactly. This proves compatibility for the selected rational representatives but does not prove physical fermions or select a stratum. |
| [OA-C1058](#oa-c1058) | `CONDITIONAL` | `lie` | Does the outside-bench candidate sweep independently prove that its 20 accepted E6 characteristics exhaust every nonzero nilpotent orbit and hence that exactly nine of all 20 strata are projective on the 27? | Conditionally. Every accepted label has an exact positive sl2 witness, but is_characteristic makes only four seeded generic draws per label. Failed draws do not prove nonexistence. Completeness follows only after importing the standard fact that E6 has exactly 20 nonzero nilpotent orbits; the source assert len(chars)==20 uses that count as its false-negative control while calling the census literature-free. |
| [OA-C1059](#oa-c1059) | `REFUTED` | `values` | Can the untwisted m004 Ruelle zeta be a finite product or ratio of ordinary shifted Dirichlet L-functions in the same spectral variable, in particular factors built from zeta and L(chi_-3)? | No. The logarithm of the Ruelle product has first exponent the m004 systole l0, certified strictly between log(2) and log(3). Any finite shifted ordinary Dirichlet-L product has first surviving exponent log(N) for an integer N at least 2. Uniqueness of absolutely convergent generalized Dirichlet series rules out equality. The quadratic L-factor belongs to the scalar cusp scattering determinant, not to a finite geodesic Euler-product factorization. |
| [OA-C1060](#oa-c1060) | `EXTERNAL_BLOCKER` | `values` | Does the proposed n=2 m004 Ruelle/geodesic factor have a proved cutoff-independent value or analytic continuation at s=2? | Not yet. B8129 samples three length cutoffs and seven real s values and observes no visible breakdown at s=2, with increasing cutoff sensitivity below it. This is bounded numerical evidence only; it gives no limit, error bound, order-independence proof or analytic continuation. |
| [OA-C1061](#oa-c1061) | `REFUTED` | `qft` | Do the cited Fried, Park or Pfaff torsion formulae, or the scalar m004 cusp scattering determinant, directly equal the gauge-fixed cusped graviton one-loop determinant proposed by the programme? | No. Fried-type torsion evaluates at s=0, the cited Pfaff ratios use k at least 3, and the proposed tower begins at n=2. Analytic torsion of flat bundles is not the Einstein spin-2/vector/scalar determinant ratio. The weight-zero scalar scattering determinant lacks the weight-one and weight-two channels and parabolic terms required by the cusp trace problem. The cited compact/loxodromic gravity derivation excludes cusp groups. |
| [OA-C1062](#oa-c1062) | `EXTERNAL_BLOCKER` | `qft` | Can one construct and evaluate a gauge-fixed spin-2/vector/scalar one-loop determinant for the finite-volume cusped m004 geometry with controlled boundary conditions and continuous spectrum? | Not yet. No audited theorem accepts the current m004 scalar cusp determinant and returns the required Einstein one-loop ratio. Existing Ruelle/torsion identities compute different objects and evaluation points. The missing deliverable is an actual cusp gravity construction, not one constant or a routine literature lookup. |
| [OA-C1063](#oa-c1063) | `REFUTED` | `values` | Does the current proposal define a Beilinson regulator of J3(O), the 27-reality classes or 64 fixed dimensions and a canonical map from it to Standard-Model values? | No. The real Albert Jordan algebra is not by itself the source of an ordinary Beilinson regulator; no arithmetic scheme/motive, class, degree, target or lattice is specified. '27-reality' is not a motivic class. The claimed 64 fixed dimensions are actually a count 2^6 of sign solutions, not a 64-dimensional space. No compactification/EFT map to normalized SM parameters is defined. |
| [OA-C1064](#oa-c1064) | `EXTERNAL_BLOCKER` | `values` | Does the object uniquely select an arithmetic Albert-associated scheme or motive, a motivic class and regulator normalization, and a physical functor taking that regulator to a normalized held-out Standard-Model observable? | Not yet. Arithmetic Albert algebras, twisted Cayley planes, norm varieties and motivic regulators are legitimate mathematical objects, but the current programme selects none of them and supplies no class or observable map. This is a new construction program, not an unperformed scalar calculation and not a present critical-path shortcut. |

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
- **Leads to:** [OA-C1001](#oa-c1001), [OA-C1009](#oa-c1009)
- **Closure test:** Exact class-polynomial, integral-lattice, fan, and SL(4,Z) intertwiner certificates identifying the reconstructed action with the published C12 action.
- **Falsifier:** A class-field computation yielding a different field/action, a nonintegral conjugacy, or failure of the twelve-ray product fan reconstruction.
- **Scope:** Marked, oriented conductor-four figure-eight cusp and ambient toric reconstruction; not yet a chosen hypersurface or physical compactification.
- **Aliases:** `conductor-four ring class field`, `cyclotomic toric reconstruction`, `C12 ambient bridge`
- **Sources:** `../tracks/CLASSFIELD_HETEROTIC_BRIDGE.md`
- **Deepest artifacts:** `../experiments/verify_ringclass_z12_action.py`, `../experiments/verify_c12_action_reconstruction.py`

## Domain: `carrier`

<a id="oa-c0003"></a>
### OA-C0003 — `CONDITIONAL`

- **Question:** Does the Fibonacci substitution canonically determine the oriented punctured-torus mapping torus m004?
- **Answer:** Conditionally. Squaring the determinant-minus-one incidence gives RL, but letter-to-Dehn-twist, puncture, orientation, and mapping-torus operations are extra typed data.
- **Kind/domain:** `construction` / `carrier`
- **Depends on:** [OA-C0002](#oa-c0002)
- **Leads to:** [OA-C0004](#oa-c0004), [OA-C1000](#oa-c1000)
- **Closure test:** A unique natural functor from the admitted description category to oriented 3-manifold carriers.
- **Falsifier:** Two inequivalent admissible carrier functors from the same substitution.
- **Scope:** Current paper/repository carrier construction.
- **Aliases:** `carrier axiom`, `C3`, `C4`, `C5`
- **Sources:** `../tracks/GENESIS.md`
- **Deepest artifacts:** None registered.

## Domain: `flavor`

<a id="oa-c0015"></a>
### OA-C0015 — `EXTERNAL_BLOCKER`

- **Question:** Does the object compute nondegenerate fermion masses and realistic inter-family mixing?
- **Answer:** Not yet. The E6 cubic fixes support but not coefficients. Restriction through the non-Galois cubic K yields three unordered summands and a diagonal trace cubic. On the stronger heterotic branch, C12 characters permit six symmetric up coefficients and nine down/lepton coefficients, but the actual height-308 holomorphic up map is identically zero. That zero persists under the same-X, fixed-holomorphic-V large-radius Strominger deformation. More strongly, throughout the same BCDD monad topology the unique exact-spectrum H_u is the ambient-injected class, so coefficient variation cannot make its up coupling nonzero without adding Higgs/mixing data or changing the construction. The down/lepton map, Hd line, normalized metrics, thresholds and RG flow remain absent.
- **Kind/domain:** `computation` / `flavor`
- **Depends on:** [OA-C0008](#oa-c0008), [OA-C0014](#oa-c0014)
- **Leads to:** [OA-C0016](#oa-c0016)
- **Closure test:** Derived Yukawa matrices, phases, threshold corrections and RG flow reproducing masses and CKM/PMNS data.
- **Falsifier:** Only operator support, family-diagonal trace couplings, or arbitrary family tensors.
- **Scope:** All current cubic/field proposals and the conditional C12 heterotic visible-spectrum branch.
- **Aliases:** `flavor`, `Yukawa`, `CKM`, `PMNS`, `cubic field K`
- **Sources:** `../tracks/YUKAWA_SELECTION_RULES.md`, `../tracks/YUKAWA_CUP_PRODUCTS_308.md`, `../tracks/YUKAWA_STROMINGER_PERSISTENCE_AUDIT.md`, `../tracks/YUKAWA_EXACT_SPECTRUM_NO_GO.md`, `../tracks/PHYSICS_GATES.md`
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
- **Answer:** No. The exact character certificate gives three family copies and one Higgs pair but leaves Sym^2(C^3), dimension 6, for up Yukawas and C^3 tensor C^3, dimension 9, for down/lepton Yukawas; no C12 texture zeros occur. SU(5) supplies only up symmetry and the holomorphic transpose relation Y_e=Y_d^T. Cup-product coefficients, the Hd line in the fourfold chi0 space, matter metrics, canonical normalization, vacuum, thresholds and RG data remain unfixed.
- **Kind/domain:** `computation` / `flavor`
- **Depends on:** [OA-C1006](#oa-c1006), [OA-C1013](#oa-c1013)
- **Leads to:** [OA-C0015](#oa-c0015), [OA-C1054](#oa-c1054), [OA-C1055](#oa-c1055)
- **Closure test:** Compute the C12-invariant trilinear tensor spaces after the Wilson projection, then prove that every surviving coefficient and physical normalization is fixed by the same-source data.
- **Falsifier:** A complete character calculation showing a unique family tensor, or an exact cup-product/metric/vacuum derivation fixing all normalized entries.
- **Scope:** Pointwise certified (3,4) character data with Wilson k=4 or 8; counts are symmetry-allowed tensor dimensions, not a claim of nonzero cup-product rank or physical normalization.
- **Aliases:** `C12 Yukawa selection`, `flavor tensor gate`, `(3,4), k=4/8`
- **Sources:** `../tracks/YUKAWA_SELECTION_RULES.md`, `../tracks/MARKED_PSEUDOINVERSE_PHI_POINTWISE_AUDIT.md`, `../sources/1112.1097/Three_gen_models.tex`
- **Deepest artifacts:** `../experiments/verify_yukawa_selection_rules.py`

<a id="oa-c1034"></a>
### OA-C1034 — `CONDITIONAL`

- **Question:** Do the exact norm-308 monad and selected C12/Wilson sectors yield evaluated holomorphic up and down/lepton Yukawa cup-product maps with determined ranks and Higgs line?
- **Answer:** Conditionally. At the exact height-308 stable point, character arithmetic allows Sym2(C3) of dimension 6 and C3 tensor C3 of dimension 9, with no C12 texture zeros. The actual up-type map is nevertheless identically zero: H1(G_Y)=0 makes every matter class map to zero in the ambient extension, while H1(K1)=H2(K1)=0 uniquely lifts the Higgs class, so cup-product naturality forces mu_u=0. Thus all renormalizable holomorphic up-quark Yukawas vanish on this exact-six factorisation locus. The old down-sector 33-versus-38 gap is closed: the connecting quotient has dimension 33 and H1(Y,Lambda2G) supplies the five-dimensional Serre-dual tail with raw characters chi0+chi2+chi4+chi6+chi8. An exact good-prime construction gives a 672x33 representative matrix, proves invariance of the 27-dimensional image, and diagonalizes the quotient; adding the tail gives raw 3Reg+chi1+chi2, whose chi_-2 determinant twist is exactly physical 3Reg+chi0+chi11. The five-dimensional term now also has explicit dual-cokernel/Serre-dual functionals at GF(1009), with inverse-phase labels 0,2,4,6,8; these are not yet raw Lambda2G-valued Cech-one cocycles. A common connecting-sector chain model reduces the first physical Q8 x dc4 x Hd0 slice to one explicit missing determinant/residue trace row of shape 1x18. Hu=C0 is one-dimensional, but B0 is a four-dimensional trivial module, leaving an unselected P3 of Hd lines. The evaluator still lacks a completed Q(zeta12) chain model, chain-level Serre trace for the five tail classes, the determinant/residue row and the resulting P3 matrix pencil.
- **Kind/domain:** `computation` / `flavor`
- **Depends on:** [OA-C1013](#oa-c1013), [OA-C1020](#oa-c1020)
- **Leads to:** [OA-C0015](#oa-c0015), [OA-C1054](#oa-c1054), [OA-C1055](#oa-c1055)
- **Closure test:** Construct a common exact multigraded toric Cech or hypercohomology model for A=H1(V), B=H1(Lambda2 V), C=H1(Lambda2 V*) and its multiplicative contraction maps to H3(O); restrict the evaluated tensors to k=4/8 Wilson sectors and either derive an Hd line or report the full P3 matrix pencil.
- **Falsifier:** A chain-level calculation proving a claimed rank/texture false, or an argument based only on characters, an index, a vanishing gate, or an unselected Hd line while asserting a concrete Yukawa matrix.
- **Scope:** The fixed norm hypersurface and exact height-308 (3,4) monad, descended with Wilson k=4 or k=8. This item concerns holomorphic cup products only; canonical matter metrics, moduli/vacuum selection, thresholds and RG evolution remain separate physical gates.
- **Aliases:** `norm-308 Yukawa cup products`, `holomorphic 10-10-5H map`, `Hd-line gate`
- **Sources:** `../tracks/YUKAWA_CUP_PRODUCTS_308.md`, `../tracks/YUKAWA_SELECTION_RULES.md`, `../tracks/MARKED_PSEUDOINVERSE_PHI_POINTWISE_AUDIT.md`, `../tracks/HOPPE_LAMBDA3_GATE.md`
- **Deepest artifacts:** `../experiments/verify_yukawa_cup_product_308_scope.py`, `../experiments/certify_yukawa_down_obstruction_308.sage`, `../experiments/certify_yukawa_down_tail_cech_308.sage`, `../experiments/evaluate_yukawa_down_connecting_308.py`, `../experiments/attempt_yukawa_cech_308.sage`, `../experiments/verify_yukawa_selection_rules.py`, `../experiments/verify_marked_pseudoinverse_cech.sage`, `../experiments/verify_hoppe_lambda3.sage`

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
- **Sources:** `../tracks/YUKAWA_EXACT_SPECTRUM_NO_GO.md`, `../tracks/YUKAWA_CUP_PRODUCTS_308.md`, `../sources/1112.1097/Three_gen_models.tex`
- **Deepest artifacts:** `../experiments/verify_yukawa_exact_spectrum_no_go.py`, `../experiments/verify_yukawa_cup_product_308_scope.py`

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
- **Answer:** Not yet. The order-three anomaly is a flat degree-four differential character in H3(X,R/Z), whereas a closed ordinary B-gerbe class is degree three with flat subgroup H2(X,R/Z); adding such a flat class does not alter the degree-four anomaly. Because the integral characteristic difference vanishes, Redden's differential-cocycle theorem guarantees abstract geometric trivializations even when the differential character q is nonzero; they form an Hhat3(X)-torsor. Thus q obstructs only a stricter parallel zero-target trivialization, not a Green--Schwarz/String structure in the standard geometric sense. A pathwise result further shows that, once one marked endpoint trivialization and actual connection path are supplied, differential Chern--Weil transgression continues it along the contractible AGF interval with no additional loop/monodromy obstruction. What AGF does not supply is the visible/tangent differential refinement realizing the conditional universal q, gauge-fixed connection representatives, a selected member of the trivialization torsor, a marked H3 basis, or period normalization. The blocker is explicit realization and normalization, not abstract existence.
- **Kind/domain:** `construction` / `framework`
- **Depends on:** [OA-C1044](#oa-c1044), [OA-C1048](#oa-c1048), [OA-C1051](#oa-c1051)
- **Leads to:** [OA-C1007](#oa-c1007)
- **Closure test:** Construct an endpoint visible/tangent differential refinement and twisted Green--Schwarz/String cocycle with the prescribed order-three component, then evaluate the actual connection transgression and marked normalized H3 periods along the Strominger family.
- **Falsifier:** An explicit chain-level construction for the actual AGF connections would close the item; a proof that the conditional universal order-three character cannot be realized by those connection refinements would refute this route.
- **Scope:** The explicit global differential refinement, selected geometric trivialization and marked periods on the actual large-radius branch. Abstract existence follows from vanishing integral characteristic class; local Strominger existence and spectrum retention are OA-C1051, while a normalized four-dimensional vacuum remains further downstream.
- **Aliases:** `order-three differential Strominger lift`, `twisted Green--Schwarz completion`, `AGF secondary-character transport`
- **Sources:** `../tracks/ORDER3_DIFFERENTIAL_STROMINGER_CLOSURE.md`, `../tracks/STROMINGER_ORDER3_EXISTENCE_AUDIT.md`, `../tracks/CLASSFIELD_HETEROTIC_LEVEL_MATCHING.md`
- **Deepest artifacts:** `../experiments/verify_order3_differential_strominger.py`, `../experiments/verify_relative_secondary_cs.py`

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
- **Leads to:** [OA-C0003](#oa-c0003)
- **Closure test:** Exhaust the finite lower-cost substitution domain modulo declared symmetries.
- **Falsifier:** A lower/equal-cost inequivalent admissible substitution.
- **Scope:** The four-clause substitution category stated in tracks/GENESIS.md.
- **Aliases:** `description axiom`, `minimal-substitution theorem`
- **Sources:** None registered.
- **Deepest artifacts:** `../../physics_bridge/verify_bridge.py`

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
- **Answer:** Not yet. The norm section selects coefficients but raw norm reuse has the wrong Euler kernel; the (3,4) BCDD branch is an 11-dimensional map family with ten genuine descended bundle-moduli directions. A marked pseudoinverse map is now proved equivariant, locally free, H0(V)=0, and pointwise-surjective on the 372-to-312 map, but its Hoppe wedge vanishings, 18-to-21 Cech blocks, and selector inputs remain unproved. No stabilizing equation selects it.
- **Kind/domain:** `uniqueness` / `geometry`
- **Depends on:** [OA-C1001](#oa-c1001), [OA-C1003](#oa-c1003)
- **Leads to:** [OA-C1005](#oa-c1005), [OA-C1006](#oa-c1006), [OA-C1007](#oa-c1007), [OA-C1012](#oa-c1012)
- **Closure test:** Exhibit one stable locally free map on the selected norm member and prove that all ten residual Kodaira--Spencer bundle directions are lifted to a unique reduced point by an object-derived dynamical equation.
- **Falsifier:** A surviving stable inequivalent map, a continuous P10 deformation, instability/cohomology jump, or failure of the six-Euler-character kernel condition.
- **Scope:** The BCDD rank-five (3,4) equivariant bundle family over the selected norm hypersurface; distinct from generic branch existence.
- **Aliases:** `stable SU5 bundle point`, `Phi selector`, `bundle moduli blocker`
- **Sources:** `../tracks/NORM_BUNDLE_MAP_AUDIT.md`, `../tracks/PHI_MODULI_QUOTIENT_AUDIT.md`, `../tracks/MARKED_PSEUDOINVERSE_PHI_POINTWISE_AUDIT.md`, `../tracks/BUNDLE_HEIGHT_SELECTOR.md`, `../tracks/HETEROTIC_VACUUM_DYNAMICS.md`
- **Deepest artifacts:** `../experiments/verify_norm_bundle_map.sage`, `../experiments/verify_marked_pseudoinverse_phi.sage`, `../experiments/audit_l34_minimal_height.sage`

<a id="oa-c1012"></a>
### OA-C1012 — `PROVED`

- **Question:** Does the marked equal-weight pseudoinverse define an equivariant locally-free rank-five bundle candidate with the certified pointwise base cohomology maps?
- **Answer:** Yes. Exact Q(zeta12) linear algebra and good-prime unit/minor certificates prove equivariance, local freeness, H0(V)=0, the displayed matter cohomologies, and rank312. The construction still uses unforced target directions, coefficient metric, and relative weight.
- **Kind/domain:** `computation` / `geometry`
- **Depends on:** [OA-C1001](#oa-c1001)
- **Leads to:** [OA-C1013](#oa-c1013)
- **Closure test:** Certify exact-six Euler kernel, H0(V)=0, local freeness, pointwise H1(V) and H1(V*), and surjectivity of the Phi-induced 372-to-312 map.
- **Falsifier:** A base point, extra Euler zero mode, wrong character decomposition, or rank below 312 on the induced map.
- **Scope:** Pointwise algebraic bundle-candidate gates only; the child gate now supplies the Higgs cohomology, but not slope stability, unique selection, or a physical vacuum.
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

## Domain: `lie`

<a id="oa-c0005"></a>
### OA-C0005 — `PROVED`

- **Question:** Does binary tetrahedral 2T determine the affine E6 graph and finite E6 root-system type?
- **Answer:** Yes. Classical affine McKay gives affine E6; deleting the trivial-representation node gives the finite E6 Cartan/root-system type, but not a global-group root datum.
- **Kind/domain:** `theorem` / `lie`
- **Depends on:** [OA-C0004](#oa-c0004)
- **Leads to:** [OA-C0006](#oa-c0006), [OA-C0007](#oa-c0007), [OA-C1010](#oa-c1010)
- **Closure test:** Compute tensoring by the defining two-dimensional representation and delete the affine node.
- **Falsifier:** A non-E6 McKay adjacency graph.
- **Scope:** Abstract complex type only; no gauge theory.
- **Aliases:** `McKay E6`
- **Sources:** None registered.
- **Deepest artifacts:** None registered.

<a id="oa-c0006"></a>
### OA-C0006 — `CONDITIONAL`

- **Question:** Does the object select the principal sl2 placement and charged E6 frame used downstream?
- **Answer:** Conditionally. Whitehead rigidity does not select a class; the principal adjoint action has only even weights and factors 2T through A4; B1112 leaves a nine-element projective menu and singles A2 only after SM-compatible filtering.
- **Kind/domain:** `uniqueness` / `lie`
- **Depends on:** [OA-C0005](#oa-c0005)
- **Leads to:** [OA-C1020](#oa-c1020)
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
- **Leads to:** [OA-C0006](#oa-c0006), [OA-C0007](#oa-c0007), [OA-C0009](#oa-c0009), [OA-C1058](#oa-c1058)
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
- **Leads to:** [OA-C0006](#oa-c0006)
- **Closure test:** Either give a deterministic algebraic nonexistence certificate for every rejected label or cite and type-check a precise classification theorem proving the exact 20-orbit upper bound used with the 20 positive witnesses.
- **Falsifier:** An additional valid characteristic missed by the four random trials, a duplicate-orbit identification among accepted labels, or a wrong external orbit count.
- **Scope:** Conditional completeness of the accepted characteristic list and the resulting 9/20 total. The four distinguished positive rows and all-odd beat identities are independently exact in OA-C1057.
- **Aliases:** `C-P1 full 20-row dictionary`, `nine projective E6 strata`, `Bala-Carter count control`
- **Sources:** `../tracks/WAVE1_DELTA_ADJUDICATION.md`
- **Deepest artifacts:** `../experiments/verify_cp1_all_odd.py`

## Domain: `physics_interface`

<a id="oa-c1056"></a>
### OA-C1056 — `PROVED`

- **Question:** For the specified m004 holonomy, Gieseking beat section and selected A1 embedding, does exactly one checked sign-lift admit the semilinear beat relation and does the 27 restrict as six doublets plus fifteen singlets?
- **Answer:** Yes. At Golden commit 4a1e4cc3 all 46 top-level certificates independently exit zero. spin_payment proves the fixed-beat sign-target dimensions {(+,+):1, others:0}; sp2_seat proves weights 6(-1)+15(0)+6(+1), nontrivial central parity, relator +I and the three beat identities on the selected A1 module. Local B1145 at 9a4eca7e independently rebuilds the E6/27 matrices from banked B1102 machinery, verifies all 3003 brackets and reproduces the same identities; its five fast locks pass. B8132 shows that the count of two spin structures is shared by several family members. The ten-word inner-modification block is not exhaustive, no typed tangent-frame Pin/spin lift or four-dimensional spin/QFT/index is constructed, and the result does not establish physical fermions or generations.
- **Kind/domain:** `theorem` / `physics_interface`
- **Depends on:** None.
- **Leads to:** [OA-C0007](#oa-c0007), [OA-C0008](#oa-c0008), [OA-C0009](#oa-c0009), [OA-C0014](#oa-c0014)
- **Closure test:** Independently rerun the self-contained certificates, verify the sign-lift/intertwiner and module identities, and separate them from uncomputed Pin, four-dimensional spinor, index and generation assertions.
- **Falsifier:** Failure of any exact certificate identity at the locked commit, a second fixed sign-target intertwiner, or a mismatch in the A1 weight multiset would refute the narrow theorem; a genuine Pin/Dirac-index construction would close a downstream physics gate rather than this algebraic item.
- **Scope:** The fixed matrix holonomy and beat section and the explicitly selected ROOTS[0] A1 embedding. It is a semilinear holonomy/module theorem, not a Pin, fermion, chirality, family or Standard-Model theorem.
- **Aliases:** `Golden SP-2 close-out`, `Gieseking beat lift on the A1 27`, `cloud-seat memos 28--29 audit`
- **Sources:** `../tracks/GOLDEN_CLOUDSEAT_CLOSEOUT_AUDIT.md`, `../tracks/WAVE1_DELTA_ADJUDICATION.md`, `../inventory/SOURCE_LOCK.md`
- **Deepest artifacts:** `../tracks/GOLDEN_CLOUDSEAT_CLOSEOUT_AUDIT.md`, `../tracks/WAVE1_DELTA_ADJUDICATION.md`

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
- **Answer:** Not yet. B1104 finds no canonical suspension section; filling is nonunique; S=-Vol*sigma is an on-shell value rather than a 4d gravitational action.
- **Kind/domain:** `construction` / `qft`
- **Depends on:** [OA-C0003](#oa-c0003)
- **Leads to:** [OA-C0007](#oa-c0007)
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
- **Answer:** No. Fried-type torsion evaluates at s=0, the cited Pfaff ratios use k at least 3, and the proposed tower begins at n=2. Analytic torsion of flat bundles is not the Einstein spin-2/vector/scalar determinant ratio. The weight-zero scalar scattering determinant lacks the weight-one and weight-two channels and parabolic terms required by the cusp trace problem. The cited compact/loxodromic gravity derivation excludes cusp groups.
- **Kind/domain:** `theorem` / `qft`
- **Depends on:** [OA-C1059](#oa-c1059), [OA-C1060](#oa-c1060)
- **Leads to:** [OA-C0017](#oa-c0017), [OA-C1062](#oa-c1062)
- **Closure test:** Type-match the evaluation points, bundles/K-types, boundary conditions and determinant complexes in one cited theorem.
- **Falsifier:** A primary theorem identifying the exact spin-2/vector/scalar determinant ratio on m004 with the named torsion or scalar scattering input would overturn this negative.
- **Scope:** The proposed direct substitutions using the cited theorems and existing scalar cusp datum. It is not a no-go for constructing a new cusped graviton determinant theorem.
- **Aliases:** `B8133`, `Fried/Park/Pfaff graviton feed`, `scalar cusp determinant substitution`
- **Sources:** `../tracks/SPECIALIST_RELAYS_2_3_AUDIT.md`, `../tracks/WAVE1_DELTA_ADJUDICATION.md`
- **Deepest artifacts:** `../tracks/SPECIALIST_RELAYS_2_3_AUDIT.md`

<a id="oa-c1062"></a>
### OA-C1062 — `EXTERNAL_BLOCKER`

- **Question:** Can one construct and evaluate a gauge-fixed spin-2/vector/scalar one-loop determinant for the finite-volume cusped m004 geometry with controlled boundary conditions and continuous spectrum?
- **Answer:** Not yet. No audited theorem accepts the current m004 scalar cusp determinant and returns the required Einstein one-loop ratio. Existing Ruelle/torsion identities compute different objects and evaluation points. The missing deliverable is an actual cusp gravity construction, not one constant or a routine literature lookup.
- **Kind/domain:** `construction` / `qft`
- **Depends on:** [OA-C0003](#oa-c0003)
- **Leads to:** [OA-C0017](#oa-c0017)
- **Closure test:** Define the gravity ensemble and cusp boundary conditions; construct renormalized determinants and spin-resolved scattering for K-types 0, 1 and 2; include parabolic terms, gauge/negative/zero modes and counterterms; then prove gauge and truncation control.
- **Falsifier:** A proof of an unavoidable negative mode or nonrenormalizable gauge dependence for the specified ensemble would refute that branch; an explicit theorem and evaluated certificate would close it.
- **Scope:** Euclidean one-loop gravity on the exact finite-volume cusped m004 background. This is downstream of, and cannot by itself derive, the programme's four-dimensional gravitational theory.
- **Aliases:** `cusped boundary-graviton one-loop`, `spin-resolved cusp determinant`, `relay 3 external deliverable`
- **Sources:** `../tracks/SPECIALIST_RELAYS_2_3_AUDIT.md`, `../tracks/WAVE1_DELTA_ADJUDICATION.md`
- **Deepest artifacts:** `../tracks/SPECIALIST_RELAYS_2_3_AUDIT.md`

## Domain: `spectrum`

<a id="oa-c0008"></a>
### OA-C0008 — `REFUTED`

- **Question:** Does the native structure provide three physical copies of a chiral 27?
- **Answer:** No. B1033 retracts four internal threes; B876 is one vectorlike 16+bar16 pattern; E8 contains (27,3) and (bar27,bar3), and its sole A2 cannot be both electroweak and family.
- **Kind/domain:** `existence` / `spectrum`
- **Depends on:** [OA-C0007](#oa-c0007), [OA-C0009](#oa-c0009)
- **Leads to:** [OA-C0015](#oa-c0015), [OA-C1034](#oa-c1034)
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
- **Answer:** No. B1102 finds 18 rational target-matching directions and exactly zero commuting with a full color ideal. B1139 searches against preloaded SM Q/Y tables and is a reproduction, not a selector.
- **Kind/domain:** `uniqueness` / `spectrum`
- **Depends on:** [OA-C0007](#oa-c0007)
- **Leads to:** [OA-C0012](#oa-c0012)
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

## Domain: `vacuum`

<a id="oa-c0011"></a>
### OA-C0011 — `EXTERNAL_BLOCKER`

- **Question:** Does the object select a rank-reducing Higgs representation, orbit, point, and vacuum?
- **Answer:** Not yet. B632 v0 has N=-6, Jordan rank 3 and F4 stabilizer, not the rank-1 Spin10 direction. A Kato-Yukie semistable pencil contains no rank-1 direction; for two rank-1 endpoints N(sA+tB) is identically zero.
- **Kind/domain:** `existence` / `vacuum`
- **Depends on:** [OA-C0007](#oa-c0007)
- **Leads to:** [OA-C0012](#oa-c0012), [OA-C0014](#oa-c0014)
- **Closure test:** An object-selected scalar sector and solved stable vacuum with the required rank drop.
- **Falsifier:** Candidate lies in the wrong invariant orbit or only specifies an orbit/condition rather than a point and potential.
- **Scope:** Known repo VEV shortcuts are refuted; F4(Z) pair-orbit and full potential remain open.
- **Aliases:** `rank-closing VEV`, `B632`, `B969`, `B1043`, `L176`
- **Sources:** None registered.
- **Deepest artifacts:** None registered.

<a id="oa-c0014"></a>
### OA-C0014 — `EXTERNAL_BLOCKER`

- **Question:** Does the selected vacuum leave exactly the SM light fields and one viable Higgs sector while lifting all exotics?
- **Answer:** Not yet. 27=16+10+1 gives one family plus vectorlike exotics/singlet; existing cubic tables give allowed support only. No vacuum or mass-rank proof exists.
- **Kind/domain:** `computation` / `vacuum`
- **Depends on:** [OA-C0011](#oa-c0011), [OA-C0012](#oa-c0012)
- **Leads to:** [OA-C0015](#oa-c0015), [OA-C0016](#oa-c0016)
- **Closure test:** Explicit scalar potential/vacuum and mass matrices with proved ranks in every charge sector.
- **Falsifier:** Any massless colored exotic, mirror family, extra U1, or unselected light-doublet multiplicity.
- **Scope:** Strict low-energy SM spectrum.
- **Aliases:** `Higgs`, `exotic decoupling`, `doublet-triplet splitting`
- **Sources:** None registered.
- **Deepest artifacts:** None registered.

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
- **Answer:** Yes. H3(X,Z)=Z^10 maps surjectively to H3(BC12,Z)=Z/12. In an adapted integral basis the map is n->n1 mod 12, and c2=2 evaluates as chi(n)=n1/6 mod 1, an exact primitive sixth-root phase. The conditional codifferent-norm law nominates an algebraic complex-structure basepoint and residue form up to scale, but no marked H3 chain/sLag basis, period vector or physical Omega normalization has been constructed. The topology therefore fixes a phase/coset, not an additive parameter-free W0.
- **Kind/domain:** `theorem` / `vacuum`
- **Depends on:** [OA-C1001](#oa-c1001), [OA-C1043](#oa-c1043)
- **Leads to:** [OA-C1007](#oa-c1007), [OA-C1046](#oa-c1046), [OA-C1047](#oa-c1047)
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

## Domain: `values`

<a id="oa-c0016"></a>
### OA-C0016 — `EXTERNAL_BLOCKER`

- **Question:** Does the object emit every dimensionless Standard-Model parameter after thresholds and RG running?
- **Answer:** Not yet. Natural period searches return negative; regulator identification remains unconstructed; sin^2(theta_W)=3/8 is the conditional GUT normalization, not the measured prediction.
- **Kind/domain:** `computation` / `values`
- **Depends on:** [OA-C0007](#oa-c0007), [OA-C0014](#oa-c0014), [OA-C0015](#oa-c0015)
- **Leads to:** [OA-C0018](#oa-c0018)
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
- **Leads to:** None.
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
- **Leads to:** [OA-C1061](#oa-c1061), [OA-C1062](#oa-c1062)
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

## Reading the map correctly

- A `PROVED` row proves only its recorded scope; inspect its dependencies before using it
  downstream.
- A `REFUTED` row closes the named route, not every imaginable replacement.
- A `CONDITIONAL` row exposes the exact unpaid input rather than hiding it.
- An `EXTERNAL_BLOCKER` is terminal for the present campaign state but becomes active when
  its stated construction or theorem is supplied.
- New questions discovered during verification must be added before the parent can be called
  exhausted.
