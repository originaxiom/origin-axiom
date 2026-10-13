# Zero mode transport for global flag metrics

October 13, 2026. Authored analytic argument before execution. The general bounded-norm argument is already present in F11 and F12; this application binds it to the new nonsplit rank-five coefficient and its tensor representations. A further radial transport compares different positive flag amplitudes. Neither argument computes a generation count or derives the supplied parent theory.

## Fixed data and inherited results

Keep the complete smooth base M, its fixed hyperbolic metric g, flat bundle W and differential D from [noncompact admission](../noncompact_admission/PROOF.md). There is no physical boundary at a finite cusp cut. For each fixed b>0 let K_b be a smooth reference metric with the prescribed exact end, and H_b the harmonic metric admitted in its mutual-boundedness class, conditional on that authored existence application. The underlying flat bundle and D do not change when b or the fibre metric changes. Splitting D into a unitary part and a self-adjoint Higgs part does change.

The earlier [F11 proof](../../projective_cusp_spectrum_2026_09_21/PROOF.md) and [F12 proof](../../projective_global_metric_2026_09_21/PROOF.md) already use equivalent norms to identify closed complexes. Their peripheral acyclicity and cohomology counts concern a different coefficient and are not transferred here. The [complete-domain argument](../../complete_domain_2026_09_20/PROOF.md) applies to a smooth complex connection on a complete base even with unbounded Higgs field. It uses cutoffs whose commutator with the differential is exterior multiplication by d chi; compactly supported graph approximation then gives the unique complete-space realization. No boundary condition is selected to target a count.

Use E=W, W dual, exterior-square W or its dual, with their induced flat differentials and Hermitian norms. The same comparison works for fixed finite tensor constructions, including the parent adjoint sectors, without discarding their neutral components.

## Bounded metrics preserve the actual differential domains

Suppose m K <= H <= M K on W, with positive finite constants. On exterior-square W the bounds are m squared and M squared. On W dual they are 1/M and 1/m, and on End W they are m/M and M/m. These follow by diagonalizing the positive relative metric at each point and taking products or inverse products of eigenvalues; no derivative of the relative metric enters. The fixed base metric then gives uniform equivalence in every form degree.

For any one such E, write L_K^k and L_H^k for its square-integrable k-forms. These are the same sets of measurable sections with equivalent norms. The maximal differential has domain

    Dom D_k = {u in L^k : D u in L^(k+1) distributionally}.

It is the same set for K and H, with equivalent graph norms. The graph closures of the same compactly supported smooth domain also coincide. On this complete manifold minimal equals maximal: cutoff commutators are bounded by |d chi|, and local first-order graph regularization handles compact support. This is a statement about D, not an assertion that its adjoint is unchanged.

In particular the two complexes have the same closed forms Z^k, exact forms B^k and closure of B^k. Therefore identity induces an isomorphism, with bounded inverse, on

    reduced H^k_(2) = Z^k / closure(B^k).

The unreduced algebraic quotient also agrees. Closedness of ranges, and the Fredholm property if established for either complex, are preserved. Equivalence itself does not prove that these properties hold. In particular no finite-dimensionality or spectral gap is inferred solely from a bounded relative metric.

The Hilbert-space statement used here is elementary: a closed subspace has an orthogonal complement, so its quotient is represented by that complement. [Arnold, Falk and Winther, section 3.1.3](https://arxiv.org/html/0906.4325v3#S3.SS1.SSS3) explicitly identify harmonic forms with reduced cohomology, without assuming closed range; the stronger unreduced identification requires closed range.

## Harmonic representatives move even when their counts do not

Let G_k be the positive bounded relative norm operator in degree k, defined by the H inner product equalling the K inner product with G_k on one entry. The exact Hilbert-adjoint relation is

    D_H^* = G_(k-1)^(-1) D_K^* G_k,
    Dom D_H^* = {u : G_k u belongs to Dom D_K^*}.

Thus adjoint domains and harmonic wavefunctions need not be identical. For either metric, harmonic k-forms are Z^k intersect the orthogonal complement of closure(B^k). If P_H and P_K are harmonic projections, the map

    T : harmonic_K -> harmonic_H,    T u = P_H u

has inverse P_K on harmonic_H. Indeed u-P_H u lies in the common closure(B^k); projecting it with P_K removes that difference. This argument uses reduced cohomology and does not claim the difference has an actual primitive unless the range is closed.

On the complete space, the Hodge operator Q=D+D^* has its unique self-adjoint closure. On compactly supported forms, flatness gives

    ||Q u|| squared = ||D u|| squared + ||D^* u|| squared.

Graph approximation extends this identity to its closed domain. Consequently its global zero modes are closed and coclosed degree by degree. The local mixed-degree zero Cauchy columns of the joining calculation do not contradict this: they live on an exterior with an artificial lower boundary, where the global no-boundary norm identity is not available without its boundary term.

It follows that the unknown mixing in H_b cannot change any degree's harmonic multiplicity relative to K_b. This does not identify Q_H with Q_K, preserve positive eigenvalues, normalize interactions or give a count before K_b's global cohomology has been computed. It also does not transport a separately imposed finite-cut boundary law. The physical interpretation remains conditional on the supplied field/operator dictionary and a compatible complete-space domain.

## The literal end in a common temporal frame

In Gate3's unit coefficient frame the exact connection is

    C_b,r = A - b exp(2r/ell) Xi,
    C_b,X = exp(-r/ell) N_X,
    C_b,Y = exp(-r/ell) N_Y,
    Xi = diag(1,1,1,1,-4).

Here A has entries A_03=A_30=1/ell and all other entries zero in the ordered Pauli basis extended by the fifth line. N_X and N_Y are the actual Hermitian-matrix lifts of -N and -iN, where N is the upper triangular elementary two-by-two matrix. They commute with Xi, and [A,N_X]=N_X/ell and [A,N_Y]=N_Y/ell. Their peripheral periods are those already checked in Gate3. These are the nonabelian coefficient matrices, not a replacement by five independent global line bundles.

Put

    F_b(r) = ell b [exp(2r/ell)-1]/2,
    S_b(r) = exp(-r A + F_b(r) Xi).

Changing frame by S_b removes the radial connection. The tangential coefficients become the r-independent N_X and N_Y. Thus this temporal frame presents the same flat D for every b, initialized identically at r=0. Its fibre metric is

    K_b(r) = S_b(r)^* S_b(r)
           = exp(-2r A + ell b [exp(2r/ell)-1] Xi).

A and Xi are commuting Hermitian matrices, with A eigenvalues (1,0,0,-1,0)/ell. The frame is periodic on the cusp torus; it is not claimed to be a globally parallel frame or a global splitting of W. The literal peripheral split suffices for this end calculation.

## A bounded cochain map between all positive amplitudes

For b,b'>0 choose c=(ell/2) log(b'/b). On a sufficiently high cusp use the radial translation phi(r,x)=(r+c,x). It extends to a smooth diffeomorphism of all M, equal to identity on a compact core: take the time-c flow of chi(r) partial_r, where chi vanishes near the core and equals one high on the end. Above a sufficiently high cut the flow is the exact translation; below it all comparisons occur on a compact set. There is no demand that the translation fix an artificial seam.

The isotopy gives a flat identification phi^* E with E by parallel transport along its paths. On the temporal frame this is identity on coefficient vectors. Pullback with this identification commutes with D in every degree and has its inverse from the reversed isotopy. This statement uses flatness, not an arbitrary gauge transformation assumed to commute with D.

The exact end metric comparison is

    K_b(r+c) = K_b'(r) exp(-2c A + ell(b'-b) Xi).

The final factor is a constant positive matrix commuting with K_b'. It and its inverse have finite norm for every fixed b,b'>0. Meanwhile phi^*g=dr squared + exp(-2c/ell) exp(-2r/ell) h_T on the high cusp. Pulling back a component with j torus covectors changes its base squared-norm density by exp((2j-2)c/ell); the presence of dr does not change that factor. Hence all degree-wise norm comparisons are bounded, with bounded inverse. On the compact transition, smooth positivity and the nonsingular diffeomorphism give the remaining bounds.

Pullback therefore defines a bounded cochain isomorphism between the complete L2 complexes for K_b and K_b'. It also maps compactly supported forms onto compactly supported forms and preserves their graph closures. Taking tensor powers and duals gives the same result for both charged slots and the other fixed coefficient constructions. Combining it with the preceding H_b versus K_b comparison yields

    reduced H^k_(2)(M;E,H_b) isomorphic to reduced H^k_(2)(M;E,H_b')

for every k and every b,b'>0 in this supplied family. To map harmonic representatives, compose the cochain map with the destination harmonic projection. Finite zero-mode multiplicities, if finite, cannot depend on b within this positive family. Closed range and Fredholmness are equivalent between its members, not established from this comparison alone.

This is a chain isomorphism, not an isometry or a gauge equivalence of physical backgrounds. The fixed hyperbolic base metric is not preserved by phi. At the same base coordinates the identity comparison between K_b and K_b' is unbounded for b!=b', because Xi has both signs and the difference grows as exp(2r/ell). The radial transport is essential. Current, localization, kinetic normalization and positive spectrum may differ. The transformation does not select b or make it a normalizable modulus; the already-computed amplitude tangent has infinite kinetic norm.

No finite translation relates b>0 to zero or changes its sign. No uniform bounds as b tends to zero are asserted. For the wedge-square representation the flag weights are +2 six times and -3 four times, not the defining representation's +1 four times and -4 once. Those weights, their duals and all sectors are retained. Their appearance in this proof is not a family count.

## What this removes and what remains

For this supplied complete end class, computing a closed-form global H_b is not a prerequisite for computing reduced L2 cohomology or its harmonic multiplicities. Gate4's compulsory mixing cannot change those multiplicities within the bounded class. Further, the magnitude of a positive b is not an independent zero-mode-count choice. These are conditional deductions from the actual end and the global comparison, not from a target of three families.

The next mathematical calculation is the full weighted complex for K_b, including the peripheral representation and its map to the compact core in W and exterior-square W. Their neutral/conjugate partners and any gaugino modes must remain. Neither F11's unrelated peripheral acyclicity nor the compact selective boundary count can replace that calculation. The genesis duties remain prior: derive the physical dictionary, justify this end class or a different one, and obtain its physical index without inserting a desired projection. Couplings, empirical adequacy and gravity are not delivered by a cohomology isomorphism.
