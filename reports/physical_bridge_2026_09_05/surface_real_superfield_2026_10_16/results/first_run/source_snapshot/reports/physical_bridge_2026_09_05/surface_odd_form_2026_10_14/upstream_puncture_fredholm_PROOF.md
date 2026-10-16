# A closed Dirac realization of the puncture index

Authored application of a primary analytic theorem; independent specialist acceptance remains owed. The statement concerns the already supplied finite-distance punctured elliptic curve, not the complete cusp or the whole moduli surface.

## Geometric and coefficient hypotheses

Let E be a compact complex elliptic curve, p its marked point and X=E minus p. Fix the extending odd spin line S, S^2=K_E, and a smooth nondegenerate metric in its conformal class. Begin with the flat metric. Let W be the rank-six unitary flat coefficient with three blocks chi_p tensor rho_Q, for parity exponents (2,0),(0,2),(2,2) as powers of i on a,b. Use rho_Q(a)=diag(i,-i) and rho_Q(b)=[[0,1],[-1,0]], as in the supplied producer.

Every generator has determinant one. Each block's commutator is -I, so the full puncture holonomy is -I6, and det W has a globally parallel nonzero section. These are properties of the actual coefficient, not just a rank-six replacement. There are no other deleted points or boundaries.

Let D be the ordinary unitary twisted spin Dirac operator with initial domain compactly supported smooth spinors on X. In a local flat Cartesian spin frame and multivalued flat coefficient frame,

    D = -i [[0, exp(-i theta)(partial_r-i/r partial_theta)],
            [exp(i theta)(partial_r+i/r partial_theta), 0]].

The gauge coefficients are antiperiodic in theta. Put

    U(theta)=diag(exp(-i theta/2),exp(i theta/2)) tensor I6
    psi_cart = r^(-1/2) U(theta) h.

U is also antiperiodic, so h is periodic. The transformation is unitary from the Cartesian L2 density r dr dtheta to dr dtheta. Direct differentiation gives

    A h = -i [[0, partial_r-i/r partial_theta],
              [partial_r+i/r partial_theta, 0]] h.

Missing the spin-frame half rotation would change the angular spectrum. Omitting the radial factor would change the density and indicial strip.

## The cone theorem applies to this operator

Blow up p to its circle of directions. The result is a compact smooth surface M with boundary, with interior X. The spin/gauge product extends as a smooth bundle over this circle in the periodic frame above. Away from p use ordinary elliptic charts. A belongs to r^-1 Diff_b^1(M); coefficients are smooth to r=0. Its principal c-symbol on a real nonzero covector (xi,eta) is

    [[0,xi-i eta],[xi+i eta,0]] tensor I6.

Its square is (xi^2+eta^2)I12. Thus it is c-elliptic. In the notation of Gil--Krainer--Mendoza the density dr dtheta is r^(-1/2)L2_b with b-density dr/r dtheta, since the squared weighted norm is integral r abs(h)^2 dr/r dtheta. Here the operator order is m=1 and the Sobolev order is s=0.

Their Proposition3.5 and Theorem3.6 give the minimal/maximal closed extensions and finite-dimensional domain quotient. Their Section6 describes this quotient by indicial asymptotics in the open strip -1/2<Im(sigma)<1/2. These statements are the source input, not a conclusion inferred from finite matrices. [Primary text, Section3 and Section6](https://arxiv.org/html/math/0410176).

For angular mode exp(i n theta), n integer, our operator is

    -i [[0,partial_r+n/r],[partial_r-n/r,0]].

Its homogeneous zero solutions have normalized coefficients r^n in the plus slot and r^-n in the minus slot. With the convention r^(i sigma), the indicial roots are sigma=-i n and sigma=i n. Only n=0 lies in that strip. There are no roots on either boundary line. At n=0 the radial equation is just partial_r h=0; the inverse indicial family has a simple pole, so no logarithmic critical term occurs. The singular-function description therefore gives exactly

    Dom(A_max)/Dom(A_min) = C6_plus direct-sum C6_minus.

A class (u,v) is represented by a cutoff times the constant normalized spinor (u,v). In the original Cartesian frame these are precisely z^(-1/2)u and bar(z)^(-1/2)v. This proves that the earlier local coefficients exhaust the global domain quotient; it is not an assumed trace at an infinite-distance end. Proposition3.5 also gives Dom(A_min)=r^(1/2)H_b^1 here.

## Closed domains and selfadjointness

The boundary Green pairing on that quotient, up to a common nonzero imaginary factor and outward-normal sign, is

    G((u,v),(u',v')) = u dagger v' + v dagger u'.

The radial Clifford matrix and the boundary density r dtheta give this directly; the two r^-1/2 factors cancel r. The minimal domain has zero pairing with the maximal domain. Every quotient class is represented by a cutoff solution, so no untested global restriction reduces this nondegenerate pairing.

Given any complex subspace Lambda subset C6, define

    Dom(D_Lambda)=Dom(D_min) plus
        cutoff representatives of (Lambda direct-sum Lambda_perp).

The added subspace has dimension six, has zero Green pairing and equals its Green annihilator. The adjoint-domain criterion consequently gives D_Lambda selfadjoint. The domain is invariant under the chiral grading Gamma=diag(I6,-I6), and D anticommutes with Gamma. Conversely every grading-invariant selfadjoint extension of this minimal operator has this form: split its quotient by Gamma, use Green orthogonality, then maximality. Without the grading assumption there are other selfadjoint extensions; graph(v=i u) is one and is retained as a control.

The cone-domain theorem gives continuous inclusion of the graph domain into r^(-1/2+epsilon)H_b^1 for some epsilon>0. On r<delta, its L2 norm is bounded by delta^epsilon times that stronger weighted norm. On r>=delta, compact Rellich embedding applies. Tail control plus the compact core proves compact embedding of the full graph domain into L2. Selfadjointness makes D_Lambda-i invertible; composition with that compact embedding proves compact resolvent. In particular its kernel is finite and its range is closed. The graded chiral block D_Lambda^+ and its adjoint are Fredholm. Their index need not equal the zero index of the full selfadjoint operator.

This does not invoke the paper's separate parameter-dependent ray theorem without checking it. Smooth positive conformal factors extending across p preserve this conclusion. The two-dimensional formula D_g(Omega^-1/2 beta psi)=Omega^-3/2 beta(D_flat psi) identifies the graph domains by bounded invertible multiplications. The critical coefficient changes only by a common nonzero factor at p. The transformed operator has the same adjoint-domain law and compact graph embedding. No such argument applies when Omega diverges as at the complete cusp.

## Kernel and cokernel match the compact sheaves

In a flat coefficient frame e, the local single-valued canonical holomorphic frame is z^(1/2)e. Let E0 be that extension of W over p. Its determinant frame is z^3 e_det, where e_det is the globally parallel determinant section. Thus e_det extends meromorphically with a pole of order three and no other divisor. Hence deg E0=-3, directly for this coefficient.

For d=dim Lambda, let E_Lambda be the upper modification replacing z^(1/2)e by z^(-1/2)e in the Lambda directions. Constant vectors in the local flat frame define this locally free holomorphic extension because the puncture monodromy is scalar. There is an exact sequence

    0 -> E0 -> E_Lambda -> C_p^d -> 0.

The positive Dirac zero equation is the holomorphic section equation for S tensor W. Elliptic regularity applies away from p. Its Laurent series on the local double cover has half-integer powers in z. Square integrability excludes all powers below -1/2. The only remaining negative power is z^-1/2, whose coefficient is precisely the domain trace restricted to Lambda. All higher powers belong to the minimal domain. Therefore

    ker D_Lambda^+ = H0(E,S tensor E_Lambda).

For the cokernel, conjugation and the unitary coefficient metric identify the negative zero equation with the holomorphic dual spin equation. The Green law puts its critical coefficient in Lambda_perp, identified with the complex-linear annihilator of Lambda in W*. In the dual extension the Lambda directions have regular exponent+1/2, and the complementary directions have exponent-1/2. This is exactly E_Lambda^*, not the canonical extension of W*. Thus the usual spin identification S=K_E tensor S^-1 gives an antilinear bijection

    ker (D_Lambda^+)^* = H0(E,K_E tensor (S tensor E_Lambda)^*)

at the level of dimensions. Serre duality identifies the latter dimension with h1(E,S tensor E_Lambda). This checks the cokernel rather than equating an Euler characteristic with a kernel dimension.

Riemann--Roch on the compact genus-one curve, deg S=0 and deg E_Lambda=d-3 now prove

    ind D_Lambda^+ = h0-h1 = d-3.

As a consistency check, adding d critical plus coefficients changes the minimal chiral index by d. This also follows from the exact kernel/cokernel sequence for a finite-dimensional graph-domain enlargement; it is not an independent assumption about the index. The complementary dual domain has index3-d.

At the extreme d=0, every holomorphic section of E0 has norm tending to zero at p. In a unitary flat gauge its squared norm is subharmonic, extends subharmonically across p, and hence is constant on compact E. It must be zero. Therefore the two extreme domains have (dim ker D^+,dim ker (D^+)*)=(0,3) and(3,0), respectively, the second by the same argument on the dual canonical extension and Serre duality. For the intermediate subspaces only the index is asserted; individual multiplicities can depend on Lambda.

## What has and has not been derived

The finite-distance puncture formula is now an actual chiral Fredholm index for a specified ordinary-spinor domain, with finite positive norms and compact resolvent. It is not merely a sheaf analogy. The metric type, coefficient, spin and domain remain supplied; no mechanism selects d, Lambda or finite rather than infinite distance.

In particular the complete hyperbolic cusp has Omega=1/(r abs(log r)). The conformally transported critical spinor has norm proportional to integral dr/(r abs(log r)), which diverges. The bounded conformal comparison above fails, and the cone theorem's compact finite-distance realization is not that operator. The earlier complete-cusp Weyl-sequence result remains untouched.

Likewise this is a fixed fibre of the modular family. A family index over the modular base, its cusp extension, a four-dimensional spacetime interpretation, an interacting parent, anomaly acceptance and selection from genesis require further maps and hypotheses. No three-generation Standard Model or full theory follows from choosing an extreme domain here. This completes an existing analytic obligation without hiding its physical price.
