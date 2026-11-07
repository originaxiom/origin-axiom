# Independent half-root, weak-vector and centralizer review — 2026-11-07

Exact review target: `3e58425f1e6560d9f078f306e724ed264d41884f` on `audit/physical-bridge-2026-09-05`.

This non-authoring review covers the three target proofs, their nine-method implementation, original design and two addenda, receipts/status and declared dependencies at that seal. It uses hand mathematics, source reading and standard-library AST/hash inspection. **All nine methods remain UNRUN, UNIMPORTED AND UNCOLLECTED.** No scientific module, CAS, numerical producer, test collection or production admission gate was executed. No authored science was changed.

The later packages at `68bbb463f`, `c0d19629f` and `ae5e48184` are excluded. Current HEAD being later than the target does not extend this review's scope. The earlier thirteen-method execution review and prior proof/source dispositions do not supply execution admission for these nine methods.

## Verdict

No load-bearing mathematical refutation was found in the three stated conditional proofs. The equivariant reduction yields the stated half-root kernel counts, the charge-one vector and single-vector current have the stated grading constraints, and the A3 spin kernel vanishes while its scalar/form threshold kernel remains. These conclusions use the supplied parent, complete elliptic cusp, physical spin/flavour identification, Wilson data and graph realization.

**The executable package is REVISION REQUIRED / UNRUN / NOT ADMITTED.** Finding V1 identifies a concrete gap against the sealed eighth-control duty: its generic finite Koszul square is not a reconstruction of the actual physical mass-map gauge block and kinetic normalization. This does not refute the analytical block identity, which can be reviewed from the original source. It does prevent describing the current code as implementing every sealed source-control duty. No runtime failure or success is claimed.

| Component | Independent disposition |
|---|---|
| `COUPLED_HALF_ROOT_KERNEL_AND_CORE_LIFT_SENSITIVITY.md` | Conditional hand argument supported, including equivariant complete-domain reduction and 16 bare / 18 specified corrected left-kernel dimensions at the stated odd spin. These are coefficient dimensions, not generations. |
| `WEAK_CURRENT_GRADING_AND_DISCRETE_CHARGED_VECTORS.md` | Conditional charge/grading selection and strictly massive discrete charge-one vector block supported. Numerical masses, actual overlaps and weak chirality are not determined. Source implementation of the vector-square duty requires revision, V1. |
| `CENTRALIZER_KERNEL_WITH_THRESHOLD_CONTINUUM.md` | Conditional vanishing of the A3 spin-field L2 kernel and survival of nine scalar plus nine form modes supported. No Fredholm assumption at the spin threshold is used. |
| Nine-method `checks.py` | Substantial independent finite source/cohomology coverage; no concrete algebraic implementation bug found by hand in the other controls. V1 remains unresolved against the sealed design. Runtime, source-complete execution packet, exact main acceptance and strict prospective admission remain outstanding. |

## V1 — The vector-block control does not bind the actual physical operator

Priority: material design-to-source coverage gap, requiring revision or an explicit amended scope before exact implementation acceptance.

`DESIGN_ADDENDUM_WEAK_CURRENT.md`, control 8, requires: “Bind the scalar gauge kinetic metric, d and the source M†M block identity from their actual producers.” The implementation at `checks.py:417–435` instead checks a scalar factor using a declared qnorm, rescales the finite raising map by sqrt(2), constructs a new three-degree Hermitian Koszul Dirac matrix and squares that new matrix. Its leading-block identity and off-block zero follow from the construction and d1*d0=0. They do not compare the source's actual four-slot mass expression with its weighted Hermitian adjoint, real/dual structures, gauge Killing map or nonconstant gauge connection.

The issue is substantive because the actual complete source identity contains derivative/curvature cancellation at moment zero. A purely algebraic zero-derivative restriction need not have the physical gauge block. For example, the source scalar-gaugino column of the mass map contains the compact-adjoint Higgs operators. Its squared algebraic contribution contains q*q-dagger+r*r-dagger, whereas d-dagger*d from the holomorphic gauge tangent contains q-dagger*q+r-dagger*r. Their difference is a commutator term. In the actual stationary problem it is the covariant derivative commutator and D-flat moment relation that complete the identity. The new finite Koszul matrix contains none of those derivatives or curvature terms.

Changing a gaugino transpose coupling, the source gauge metric or a covariant-derivative sign in the actual physical producer would therefore leave the current lines 417–435 unchanged. The source-level wrong-Koszul-minus control at lines 432–434 is useful but only tests the newly constructed finite complex. It cannot detect these physical-operator defects.

`REVIEW_STATUS.md` and the comment at line 435 correctly acknowledge that this is not the curved complete M†M theorem. That honest limitation protects the wording of the result; it does not fulfill the stronger sealed requirement to bind the actual producer. A meaningful repair should reconstruct the appropriate source rows and weighted/trace-dual adjoints, retain variable gauge/metric terms needed by the moment identity and compare the actual gauge block, with an independently computed rejecting sign/metric/coupling case. The global form-domain theorem still needs hand review even after that finite/local source control is implemented.

No scientific execution is needed or authorized to record this coverage finding. It is not a negative verdict on the model or on the conditional proof below.

## Hand review of the half-root kernel argument

### Actual fibre cohomology and transitions

The source Spin10 restriction is V_(3/2) tensor V_(3/2) in each chirality. Its two commuting raising maps give the Koszul complex 16 -> 32 -> 16. For one raising string, the kernel is the top vector and its cokernel is the bottom vector. Tensoring the two complexes gives cohomology ranks (1,2,1), with top, the two mixed extremes and bottom as representatives. No internal spinor-product multiplicity is discarded by this reduction.

For the actual torus and source creation/annihilation convention, the total H-weight at a joint basis vector obtained by lowering p and q times is 6-2p-2q. In Koszul degree d its holomorphic S exponent is d-H/2. This gives -3 at the top, 1 on each middle extreme and 5 at the bottom, matching the proof and `checks.py:248–254`.

The flavour coordinate change has determinant -1, so transporting its epsilon pairing and final Koszul line is essential. With those factors retained, A has gauge action -i times the exchange of Eplus/Eminus, while D has phases -i,+i on them. Three compact lowering operators in one string give i^3=-i; both strings give i^6=-1. Thus the induced A actions on the reduced complex are alpha, alpha*sigma_x and -alpha. D is the identity in all three reduced degrees after the actual flavour factor. B=D*A has the same reduced action as A.

There is no assumption here that D is the gauge image of the based word ab. It is B*A^-1, corresponding to the flavour word b*a^-1. Keeping that relation avoids replacing the actual bare full group by its quaternion quotient. The degree-two relative minus and the determinant factor cannot be inferred merely from the dimensions.

For the source torus convention the two chiral highest lines can also be checked directly: the H=6 occupation states give alpha=exp(pi*i/4) in odd parity and alpha=exp(3*pi*i/4) in even parity. These phases have fourth power -1, as required. The root coefficient record has the matching five-coordinate parity. Multiplication by the actual electromagnetic h phase gives a highest-line square of one in each complementary charge. Its second permitted value multiplies all half-root actions by -1, exchanging the two middle eigencharacters rather than changing their unordered pair.

The code independently derives the weight frame from the joint kernel of the actual Clifford raising matrices and their lowering strings (`checks.py:51–95`). It computes the differentials, harmonic kernels and ranks before comparing them with the claimed representative frame. The assigned representative indices are therefore targets checked against actual nullspaces, not substitutes for computing cohomology. The code includes both chiralities and all eight complementary weights from the actual half-root set.

### Equivariant retraction and complete domains

The surviving subspaces are invariant under the combined finite transitions in all degrees. The middle pair may be exchanged, so a projection onto either middle line alone would not be a valid global projection. Projection onto their sum, and the degree-zero and final projections, do intertwine the transitions. The old local contraction is between identical holomorphic lines after the raising field's S factor is included. Its apparent coordinate powers cancel in the actual source and target norms; inverse raising coefficients are finite nonzero constants in these bundle maps.

Averaging that bounded holomorphic contraction over the finite combined transition image preserves the chain identity, inclusion/projection, holomorphicity and core support. The old order-three Wilson factor commutes with the construction; it supplies scalar unitary phases on a complementary coefficient and does not obstruct the average. This gives a global contraction on the new flatly glued bundle, without averaging the vacuum or changing its operator.

After Dolbeault totalization, the usual degree sign makes the contraction identity hold on compactly supported sections. Boundedness and the identity itself control the differential of the contracted approximants: if f_n -> f in the complete differential graph norm, delta*h*f_n= f_n-ip*f_n-h*delta*f_n converges. Thus h extends on the same minimal graph domains. Complete Dirac cutoffs identify the relevant complete adjoints, as in the original source. The antiperiodic reduced ends give closed ranges and finite harmonic cohomology; the already reviewed compact-resolvent result on the full 128 block provides an additional consistent Hodge realization. This is a domain-preserving retraction argument, not a deduction of a global kernel from finite fibre dimensions alone.

The code's Hodge homotopy (`checks.py:221–247`) is a meaningful finite comparator. It calculates both homotopy components from the differentials and regularized finite Laplacians, checks every degree of the contraction identity, checks covariance under both generators and checks an explicit finite average. It does not execute or prove the complete-domain passage; that passage is the hand argument just reviewed. The two displayed variable Omega ratios test the zero-form degree norms; the analogous (0,1)-form norm ratios have the common additional inverse-metric factor and hence the same boundedness. The full degree factors remain supplied by the source metric map.

### Exact pole endpoints, Hodge sides and core-lift counts

For a compact-spin Laurent term w^-n in S^a, the physical radial integrand is r^(a-1-2n)*log(1/r)^(a-2). With u=log(1/r), equality of the power to -1 converges precisely when a<1. The maximal pole degrees at a=-3,1,5 are therefore -2,0,2. The logarithmic equality is important at even powers; the code explicitly checks both admitted and excluded equality cases rather than rounding a/2.

The reduced degree-zero character is Lplus, the middle characters are Lplus and Lminus and the degree-two character is Lminus. All are unitary compact degree-zero lines because their flat commutators are identity. The odd S powers retain their extending-spin cusp sign; the reduced end is antiperiodic as required by the full 128 estimate.

On the compact elliptic curve, a degree -2 line has no sections, a degree 2 line has two, and a degree-zero unitary flat line has one section precisely when its unitary character is trivial. Hodge duality gives H1(S^-3 Lplus)=H0(S^5 Lplus^-1)=2, H1(S^5 Lminus)=0 and the same two delta exceptions for the middle H0/H1 sides. Totalization therefore gives H0=H3=0 and equal H1/H2 dimensions

    2 + delta(eta*Lplus) + delta(eta*Lminus).

Through the actual M=Uout*T*Uin isometry, H1+H3 is the left physical mass kernel and H0+H2 is its adjoint side. Here the gaugino/degree-three part vanishes; the nonzero degree-one connection/form modes are not gauge-vector or gaugino modes. Both opposite-charge left coefficient sectors remain present, without counting their right antiparticles again.

Bare alpha has order eight. Multiplying either core eigencharacter by any sign and any order-three Wilson phase cannot trivialize it. The two zero modes per complementary coefficient are consequently independent of extending spin and of the four independent bare central core signs. For the specified continuous-Pin2 corrections, alpha^2=1 and the two middle eigencharacters differ by simultaneous -1 on a and b. For the registering candidate eta=O and trivial singlet Wilson, exactly one is trivial. A nontrivial order-three triplet Wilson prevents either middle line from becoming trivial. The resulting counts are two per triplet component and three per singlet for either specified correction, versus two for every bare component. There are six triplet components and two singlet components across conjugates, giving 16 bare and 18 corrected left-kernel dimensions. The adjoint counts agree, recovering index zero while retaining the kernel difference.

For a general extending spin, the corrected singlet jump occurs exactly when eta(a)=eta(b) in this specified core prescription. Arbitrary independent additional corrected lift signs can change that condition and are correctly not identified with the two specified coherent corrections. The invariant statement is line triviality under transport of the complete marked data.

The first six code methods genuinely compute the Clifford reductions and fixed spaces feeding the final counts. The compact elliptic H0/H1 and pole formulae remain mathematical inputs, not independent PDE solves. The code checks all eight nontrivial C3 characters and all four spin characters, both chiralities, all four bare sign choices and the two stipulated corrections. The counts 16 and 18 are comparison targets reached from those computations, not values returned directly by an assigned counting function. No runtime outcome is asserted.

## Hand review of the weak-current and vector argument

The actual charge Q=(2/3)(e1+e2+e3) gives 0,+/-2/3,+/-4/3 on integer roots and +/-1,+/-1/3 on half roots. Cartans are neutral. Hence every adjoint coefficient of charge +/-1 is odd under Zeta=exp(3*pi*i*Q). Because all background fields and transitions are even and preserve Q, these are global grading and charge subbundles, not only a local root naming convention.

For odd w and fermion coefficient parities p,q, invariance of the Hermitian trace changes the vertex by -p*q. The vertex therefore vanishes when p=q, slot by slot, with the actual positive densities Omega^2,1/2,Omega,Omega. Integrating or normalizing does not remove that pointwise zero. Opposite parities are allowed, not guaranteed to have a nonzero physical overlap.

The displayed w and d are actual E8 roots, have inner product -1, and sum to e1+e4. The root-string relation then supplies a nonzero algebraic bracket, with charge flow 1+(-1/3)=2/3. The opposite root supplies the nonzero Cartan bracket. These are algebraic channel examples; no low-mode overlap or coupling magnitude is inferred. Adding the source T3 and Y Cartans gives Q directly. The old weak root therefore supplies a consistent local reference, without selecting a normalized global vector profile in the new core bundle.

The seventh method enumerates the actual root charge/parity sets and available root sums. Its kinetic-slot check is a character/sign orthogonality control, not evaluation of a nonzero normalized vertex. Its opposite-root/root-length checks use the standard root-space bracket theorem; they do not independently construct E8 structure constants or normalize an overlap. This is a bounded scope consistent with the analytical claim of algebraic availability.

For the vector mass theorem, I read the source `SAME_ACTION_REAL_GAUGE_FIXING_AND_ONE_LOOP_WEIGHTS.md:20–35,43–65,107–135` and the physical mass rows/metrics. At the stipulated F/D-flat background, gauge invariance of W gives H*d=0 with the actual bilinear transpose and retained surface pairing. The source Kahler moment identity makes d-dagger*d commute with compact conjugation at moment zero: the imaginary pairing of two real gauge tangents is the moment paired with their Lie bracket and vanishes. With the actual sqrt(2) gauge normalization, this yields the stated gauge block of M-dagger*M. Closure of the equal nonnegative quadratic forms on the same compact-support core gives the same complete gauge form domain; no spectral boundary condition is assigned independently.

The new unitary gauge/flavour transitions preserve those structures. Complete cutoffs eliminate the same first-order pairing errors and the local residuals still vanish. The identity therefore transports to this new bundle; no old heat trace or threshold formula is needed. The already reviewed compact-resolvent doubled 128 operator gives a compact-resolvent square and its reducing gauge block. The charge blocks are preserved as well.

A real zero of Pv=d-dagger*d has d*epsilon=0. Compact conjugation then yields both holomorphic and antiholomorphic derivative equations and both raising and lowering Higgs commutators. It is parallel and belongs to the compact common triple centralizer. The actual decomposition gives only the fifteen-dimensional A3, all even. Thus the odd Pv kernel vanishes. Splitting a complex kernel element into real and imaginary parts is legitimate because Pv commutes with compact conjugation, even though that conjugation exchanges charge +1 and -1. This proves the zero-kernel claim without requiring the new half-root fermion kernel count. Compact resolvent and zero kernel imply a strictly positive first eigenvalue on each fixed admitted charge-one carrier; no uniform bound through degeneration follows.

The eighth method's stacked full-module raising/lowering kernels are an independent finite check of that compact centralizer and of the nine Wilson-fixed A3 directions. Omitting the adjoints gives a strictly larger holomorphic kernel, a useful rejecting comparison. Its remaining finite block-square code does not meet the actual-source requirement, as V1 explains. The hand source-domain argument supports the theorem but does not convert that code into a different control.

## Hand review of the centralizer threshold kernel

On the A3 block, every Higgs commutator and transpose gaugino coupling vanishes. The source mass map separates the scalar/form pair from the epsilon_F Dolbeault pair. The latter has kernel exactly the L2 holomorphic sections of S tensor F tensor L; invertibility of epsilon_F and positivity of the metric suffice. No Fredholm index at the free spin threshold is assumed.

In a compact puncture coordinate, the physical spin density is Omega*r*dr*dtheta, comparable to dr*dtheta/log(1/r). F has peripheral -I, so its flat frame gives half-integer Laurent powers. The n-th term has radial factor r^(2n+1)/log(1/r). The first excluded exponent n=-1 gives the divergent primitive log(log(1/r)); more negative terms diverge as well. Laurent orthogonality excludes the negative tail. Hence an admitted section is w^(1/2) times a holomorphic function extending over the puncture, and its norm in the auxiliary smooth flat S/F/L metric tends uniformly to zero there.

Because the tensor connection is unitary flat on the punctured elliptic curve, that auxiliary squared norm is a globally defined subharmonic function. The maximum principle on the compact curve minus a small disc bounds its interior by the shrinking boundary maximum. Taking the radius to zero forces the section to vanish everywhere. S is a compact flat order-two holomorphic line specifically because the compact genus is one. The proof does not replace the physical cusp norm by its auxiliary comparison metric or assume the flat F extends over the puncture.

The scalar zero equation and the adjoint form equation have their different source densities. The scalar density dr/(r*log(1/r)^2) admits a bounded constant and excludes poles. The form density is conformally invariant and excludes a simple pole. After extension to the compact elliptic curve, each gives one zero mode for a trivial unitary L and none otherwise. The old Wilson fixes nine A3 directions and gives nontrivial characters on the other six. Thus there are nine scalar gaugino and nine connection/form left modes, with zero spin modes. They coexist with the spin essential spectrum reaching zero. Complete Dirac self-adjointness ensures an L2 distributional zero solution belongs to the actual complete kernel; no extra boundary projector or closed-range assumption was used.

If F is trivial and S tensor L trivial, the constant spin sections have finite physical norm. Their auxiliary flat norm does not tend to zero at the puncture, so the maximum-principle vanishing step fails as it should. This is a discriminating countercase.

The ninth method checks the actual density substitution, half-power radial exponent, exact critical logarithmic primitive and inherited scalar/form flat-line endpoints. Its untwisted comparison is an elementary integrability comparison, not a global section construction. The global maximum principle and exact complete-kernel interpretation are the hand proof just reviewed, not conclusions derived from a finite cutoff.

## Evidence, boundaries and next required disposition

All three target proofs and all nine method bodies were read at the exact seal. Declared dependency source sections for the old two-triple retraction, physical mass/weighted complex, compact real gauge identity and old charge embedding were inspected as needed. Source imports close through the pinned transport module and its old comparator/root helpers; no new external mathematical package is declared beyond SymPy and its inherited runtime requirements. The current inventory is a review inventory, not a complete command/runtime/output/admission specification.

The accompanying source receipt verifies all 23 inventory entries against their sealed hashes and current bytes, the exact nine static method names and the unchanged inherited staged-state digest. Additional dependency reads are recorded as such. Historical receipts retain their earlier design-only statuses. No later excluded package or independent received verdict was used to fill a proof gap.

Resolve V1, preserve this exact blocked implementation verdict and seal the corrected source before any execution-review request. A complete execution packet must still specify runtime, wrapper, exact population, dependencies, command and fresh outputs, obtain genuine main acceptance and pass strict prospective admission. This report creates no execution approval object.

The resulting within-model kernel counts, spectral grading and centralizer kernel do not select the supplied physical parent, yield three SM generations, give normalized weak currents or W/Z masses, settle continuum interactions or quantum stability, or derive foundational input payment, measured parameters or gravity. Those limitations are part of the conditional result, not missing scientific outcomes silently supplied by this review.

Only this package's review directory contains new outputs from this review. No authored proof/code, inherited staging, commit or remote was changed.
