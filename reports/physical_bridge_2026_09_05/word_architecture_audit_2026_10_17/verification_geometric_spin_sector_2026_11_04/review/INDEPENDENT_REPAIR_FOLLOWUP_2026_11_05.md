# Independent source-repair follow-up — 2026-11-05

Exact review seal: `fca1ce32cc3b835716bc3c52adc653375ecd91ff`.

Original review target: `bfcff0e8099bed5289637c1b5b9cde24f20e88f4`. The original report and hash receipt, preserved by `dc4f2ba56`, retain their original verdict and bytes. This follow-up reviews the R1–R3 repairs recorded in `REPAIRS_AFTER_INDEPENDENT_REVIEW.md` and `SOURCE_REVIEW_INVENTORY_V2.json`; it does not replace or restart the earlier mathematical review.

**Verdict: the R1 and R2 coverage defects are addressed in the revised source. R3's intended coverage is substantially added, but two new, concrete algebraic bugs block acceptance of the transport source at this seal.** Both are established by source reading and hand calculation, not by a test run. The original conditional mathematical support remains; neither bug refutes the underlying conditional construction.

All thirteen new methods remain **UNRUN, UNIMPORTED AND UNCOLLECTED**. No scientific import, test, CAS, numerical calculation or new literature work was performed for this follow-up. Main's exact separate execution acceptance, complete runtime/infrastructure closure and strict prospective admission remain outstanding. This review grants no execution authorization.

## Disposition of the original findings

| Finding | Disposition at fca1ce32c |
|---|---|
| R1 — hand-assigned cancelling index expressions | **ADDRESSED IN SOURCE.** The assertion has been replaced by weighted formal adjoints and a variationally reconstructed spin Hessian on independent dual-charge fields. The bounded-end Chern one-form difference is checked explicitly. No runtime verdict is supplied. |
| R2 — frozen-symbol curve transport and incomplete surface comparison | **ADDRESSED IN SOURCE.** The method now uses variable fields and Omega, actual vertical derivatives, the C3 substitution and a wrong metric-derivative control. The antisymmetric W, rewritten bulk and primitive are compared as expressions. No runtime verdict is supplied. |
| R3 — vector-only word controls and proxy centralizer restriction | **COVERAGE ADDED, ACCEPTANCE STILL BLOCKED.** Five E8 summands, both compensation choices, full four-slot intertwiners and an actual colour-root source restriction are present. The new source-binding assertion uses the wrong carrier adjoint (F1), and the transport charge calculation uses an overwritten norm (F2). |

The eight-method transport package is **REVISION REQUIRED / UNRUN / NOT ADMITTED**. No further concrete algebraic blocker was found in the repaired five-method geometric package itself; its R1/R2 implementation gaps are addressed. The joint repaired packet remains **NOT ADMITTED**, including its shared transport source. The global bundle, domain, Fredholm, geometric and physical-interpretation conclusions retain the conditional scope of the original report.

## New concrete blockers

### F1 — The source-binding probe takes an ordinary adjoint in a non-orthonormal carrier

Priority: blocking source correctness defect.

Locations: `verification_transport_end_2026_11_04/checks.py:196–205` and `:463–469`; source coordinate definition `verification_register_flavour_joint_2026_11_03/checks.py:75–95`.

The representation-valued helper defines qdag and rdag by ordinary matrix conjugate transpose (line 199). This is appropriate for the newly constructed orthonormal E8 module carriers. The binding probe at lines 466–469 instead passes `OLD.ad2(probe_q)` and `OLD.ad2(probe_r)`. That old comparator uses the basis (E,F,H), whose positive trace Gram matrix is G=diag(1,1,2). In that basis,

    ad(q dagger) = G^-1 ad(q) dagger G,

and it generally differs from the unweighted matrix dagger used by the new helper. `OLD.physical_mass` correctly constructs `OLD.ad2(OLD.dagger(q))`, so the two matrices in the new equality assertion are different for the actual chosen probe.

This can be checked without any symbolic execution. The probe q=E+2F gives

    ad(q) = [[ 0, 0,-2],
             [ 0, 0, 4],
             [-2, 1, 0]],

    ad(q) dagger = [[ 0, 0,-2],
                    [ 0, 0, 1],
                    [-2, 4, 0]],

    ad(q dagger) = [[ 0, 0,-4],
                    [ 0, 0, 2],
                    [-1, 2, 0]].

For example, the last column entering the first-row u coupling differs by (2,-1,0) before multiplication by sqrt(2)*i/Omega. It cannot satisfy the zero-matrix assertion at line 469 for positive Omega. This assertion also precedes the new all-E8 word loop at line 471, so that loop would not be reached by the intended unittest method if execution were later admitted without repair.

The correction must transport the carrier metric. One valid binding uses S=diag(1,1,sqrt(2)), forms S ad(q) S^-1 and S ad(r) S^-1, and conjugates the complete four-slot old source by diag(S,S,S,S). In the new coordinates ordinary dagger represents the source compact adjoint. An explicitly metric-aware helper/probe is another possibility. Merely removing the binding assertion would discard the source connection this repair is intended to establish.

This defect is in the probe's basis handling. It does not show that ordinary dagger is wrong on the actual orthonormal E8 summands, and it does not refute the trace-dual covariance theorem.

### F2 — The transport charge projection divides by the bump norm instead of the coefficient norm

Priority: blocking source correctness defect.

Locations: `verification_transport_end_2026_11_04/checks.py:550–551`, `:565–569` and `:593–599`.

At line 550, `norm` is the E8 colour-root coefficient norm from `centralizer_projection`; line 551 asserts that it is one. At line 568, the same name is overwritten by the integral of the squared radial bump. Line 594 then uses this overwritten name as the denominator of the colour charge trace projection.

For the actual coefficient and Cartan, [X,T]=2T on every summand and the source trace gives kappa(T dagger T)=1. Thus the numerator in lines 593–594 is 120 and the required denominator is 60. But the chosen bump is s^2(1-s)^2, whose squared integral is, by elementary integration,

    integral_0^1 s^4(1-s)^4 ds
      = 1/5 - 4/6 + 6/7 - 4/8 + 1/9
      = 1/630.

The implemented charge expression is consequently 1260, not 2. The equality assertion at line 595 cannot hold. The later normalized overlap integral cancels the bump normalization within the profile integral; it cannot repair a charge that was already computed with the wrong norm.

Preserve distinct names for the coefficient norm and bump norm, and use the coefficient norm in the trace charge quotient. The geometric package's counterpart already uses `actual_norm` in the charge denominator at `verification_geometric_spin_sector_2026_11_04/checks.py:328–330`; that counterpart does not have this collision.

## What the repairs now establish at source-review level

### R1: weighted adjoint, independent dual-charge variation and end connection

The revised index method at `verification_geometric_spin_sector_2026_11_04/checks.py:340–433` no longer inserts chi symbols or defines one index expression as the negative of another.

The local source connection is a genuinely general Hermitian 2-by-2 matrix connection with independent functions in Ax and Ay (lines 370–381). The noncommutation control prevents silently reducing it to independent scalar weights. The weighted-adjoint helper extracts the first-order and zeroth-order coefficients and differentiates the products of those coefficients, the target density and the target field (lines 383–391). Summing over both row and column components implements the transpose as well as complex conjugation of the matrix connection. For the displayed differential expressions, this is the correct formal-adjoint construction.

In particular, with Dbar=partial_x+i partial_y-i(Ax+iAy) and Dz=partial_x-i partial_y-i(Ax-iAy), the positive Hermitian connection implies Dz-adjoint=-Dbar before the slot weights. Applying the actual densities (Omega^2,1/2) yields the scalar/form adjoint rows

    (-Dbar a/(sqrt(2)*Omega^2), sqrt(2)*Dbar lambda).

The Omega factors cancel inside the differentiated density product; the code does not assume that Omega is constant. The slot map diag(1,sqrt(2)) is checked as an isometry to densities (Omega^2,1).

Lines 406–420 introduce independent opposite-charge fields and the correct dual connection `partial_x+i partial_y+i(Ax+iAy)^T`. The antisymmetric quadratic density has the source integration-by-parts transpose. Taking its Euler–Lagrange derivatives with respect to the independent dual fields gives Dbar V and -Dbar U. After division by the actual kinetic densities, the split mass is `(Omega^-2 Dbar V,-Dbar U)`. Its comparison with the negative, isometrically transported scalar/form adjoint is explicit at lines 421–424, and line 425 rejects the wrong overall sign. This is a meaningful operator comparison, not a symbolic index-accounting tautology.

The coefficient matrices represent V and its bilinear dual in their respective independent fields; no identification of a charged left field with its conjugate has been inserted. The target-density isometry is appropriate in the source trace-dual conjugate bundle types established by the original operator proof. This finite rank connection is a local universal algebra control; it is not a new physical replacement for an actual V_R bundle or its global domain.

The end connection check at lines 350–359 includes both coordinate components and the inhomogeneous -dJ J^-1 term. It reproduces the bounded traceless angular difference diag(-i,+i) dx/(2y) and vanishing radial difference. The old half-winding and beta=1 opposing controls remain. The original hand review of the global S3 extension, bounded homotopy and Fredholm continuity is still needed and is not replaced by these expressions.

### R2: variable fields, the C3 cancellation and the full primitive identity

At `verification_geometric_spin_sector_2026_11_04/checks.py:177–209`, the fields and metric are now functions of independent real fibre coordinates and Dbar/Dz apply actual derivatives. The constant J and flavour matrices act before those derivatives are taken. This implements the variable-field version of the previously frozen-symbol comparison while retaining the input/trace-dual target distinction.

The C3 coefficient is explicitly sigma=i Omega^2 lambda/sqrt(2). The code differentiates Omega^-2 sigma, includes both commutator components of D2-adjoint and maps the result back to all three physical rows. The wrong expression that differentiates sigma first and only divides by Omega^2 afterwards is rejected for the general metric. This is the derivative cancellation absent from the original source coverage.

Lines 211–224 construct the bulk density, the primitive derivative density and the antisymmetric superpotential separately from the variable matrices. The product rule and cyclic trace give `bulk + primitive = antisymmetric` on both sides. Their transformed sum is compared after the Jacobian measure factor. The last assertion leaves the old primitive contribution with the transformed bulk and rejects that inconsistent expression for general flavour. The derivative primitive is the local Stokes form of the same surface term; the fixed surface orientation and integration-by-parts coefficient remain those of the source action.

These are relevant new expression controls. They do not certify nonlinear weak-solution integrability, a new boundary ensemble, a global domain or a runtime result.

### R3: actual five-summand construction and source trace

The new helpers at `verification_transport_end_2026_11_04/checks.py:66–90` differentiate the exterior-square representation and use a trace-orthonormal A3 adjoint basis. The off-diagonal matrix units have unit norm and the three displayed normalized traceless diagonals are orthonormal. Thus the A3 action preserves the compact dagger. The wedge basis and Clifford exterior-algebra bases are also orthonormal carriers.

`full_parent_modules` at lines 152–193 builds (45,1), (1,15), (10,6), (16,4) and the conjugate product with the appropriate Lie and group actions. The conjugate A3 Lie action has the required negative transpose, and the corrected gauge transport uses h4, its exterior square, its adjoint phases and its conjugate on the appropriate summands. A central correction is not silently erased on the half-root products. The full dimensions and fourth powers are asserted before the word loops. The full four-slot word intertwiners at lines 471–493 use the conjugate flavour target on the same coefficient carrier. Their intended coverage is materially stronger than the old vector-only state check. F1 must be fixed to make that method reach these comparisons.

The centralizer helper at lines 216–243 now restricts the actual balanced E,G background on all five E8 modules to the actual A3 colour generator. It keeps lambda,a,u,v, reconstructs the source commutators and projects only with the full positive trace. The companion checks at lines 532–552 verify commutation with E,G,H, the adjoint Higgs directions and bare/corrected gauge transports before projection. This supplies the actual-parent connection absent from the earlier toy example.

The normalization kappa=Tr_ad(E8)/60 is compatible with the old D5 vector trace/2 convention. Restricting the adjoint E8 trace to D5 gives 30 times the vector trace; hence the source E norm 20 is unchanged. For the selected A3 colour root, the adjoint15, ten copies of the exterior6, and the 16 copies of each fundamental/conjugate four contribute total root norm 60 before division. The normalized coefficient norm is therefore one, and its Cartan charge is two. This is a hand check of the normalization used in F2, not an executed trace calculation.

The geometric periodic method now calls the same actual restriction and projection at `verification_geometric_spin_sector_2026_11_04/checks.py:294–299` and uses its coefficient norm for the source gauge vertex at lines 328–338. It no longer relies only on the zero-background reference to claim that the actual centralizer channel remains. These geometric repairs do not inherit the local-variable collision in the transport test method.

## Review envelope

The two repaired source files, the exact source diff from the original review seal, the repair record and the V2 inventory were read. The unchanged original source definitions of the comparator basis and compact adjoint were rechecked for F1. The original target proofs and mathematical verdict were retained rather than re-reviewed as a new task. No primary literature lookup or new agent was used.

The accompanying follow-up receipt pins the current source, historical review files, AST method populations and unchanged staged-state digest. It is a source/hash record, not an execution seal. No author proof/code or Git index was changed by this reviewer, and review outputs are confined to this review directory.

Required next disposition is a new source correction and exact review of F1 and F2. The code at fca1ce32c must retain this blocked verdict; a later correction cannot make these exact historical bytes accepted retroactively. No pass count, runtime success or admitted execution may be inferred from either review.
