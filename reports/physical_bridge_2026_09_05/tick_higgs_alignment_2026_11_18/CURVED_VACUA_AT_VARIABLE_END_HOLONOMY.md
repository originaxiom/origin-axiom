# Curved zero-energy solutions at prescribed puncture holonomy

19 November 2026. C8 author hand proof, for independent review. The matched-identity result at c1d2bde1e depends on the end sector. Here the end angle is specified and the original global bosonic equations determine a curvature profile and the integrated matter norm. This is a sufficient construction in the complete single-fibre parent. No change of action or numerical fit.

## A sector of the actual E8 field equations

Use the principal compact SO(3) in SU(3) from weave_graded_condensate_2026_10_08/PROOF.md, with H=diag(2,0,−2), E=sqrt(2)(E12+E23), [H,E]=2E and [E,E†]=H. The curvature −1 metric on the punctured elliptic fibre is Ω²|dw|² in the compact torus translation coordinate w=x+iy. Write *dx=dy, *dy=−dx for its oriented one-form star. For an extending spin square root of dw, match its two signs with flat gauge transitions in the H circle: use I for a positive sign and exp(iπH/2) for a negative sign. The latter negates E and has order two. These commuting transitions cost no extra continuous modulus. The trivial-spin case needs none. Keep all spectators trivial.

Take q=exp(u/2) E in the holomorphic spin frame, r=0 and gauge potential A=−H *du/4 in this flat atlas. With Dbar=D_x+iD_y the term −i[A_x+iA_y,q] cancels the derivative of exp(u/2). The F-term [q,r] vanishes. The curvature is −H Δu dx∧dy/4 and [q,q†]=exp(u) H. Thus the moment equation is exactly

    Δu = 4 Ω exp(u)                           on the punctured surface.

Here Δ is the sum of ordinary second derivatives. Solving this scalar equation kills every residual in the full action. Orthogonal E8 variations have zero first variation because all residuals vanish. The reduction selects an embedded triple and an ansatz. It does not force this triple from genesis.

## Existence for the entire open interval

Let 0<α<1/2 and ask for u=2α log(1/|w|)+a bounded remainder at the puncture (center w there). Let L be the flat area of the compact torus. On its compactification the distributional equation reads Δu=4Ω exp(u)−4πα δ. The delta specifies the asymptotic in the filled chart. No source is inserted on the physical open surface.

Take the mean-zero periodic Green solution u0 of Δu0=c−4παδ, c=4πα/L. It equals 2α log(1/|w|) plus a smooth bounded remainder. This follows by cutting off the plane logarithm and solving the remaining smooth mean-zero Poisson equation on the torus (Fourier inversion on nonconstant modes). Set h=4Ω exp(u0). Near the puncture h is comparable to |w|^(−1−2α)/log(1/|w|). Consequently h is positive and lies in L^p for some p>1 precisely as needed when 2α<1. Put k=cL/∫h. Solve Δv0=kh−c with mean zero on the compact reference torus. The ordinary elliptic L^p estimate and two-dimensional Sobolev embedding give v0 in W^(2,p), bounded and continuous. Write u=u0+v0+b.

For clarity the remaining existence argument uses the explicit convex functional

    J(b)=∫ ( |∇b|²/2 + h (exp(v0+b)−k b) ) dxdy.

Choose finite constants l≤U with exp(v0+l)≤k≤exp(v0+U) everywhere. Clipping b into [l,U] lowers both the gradient term and the pointwise potential. In this interval a minimizing sequence is bounded in H¹. Weak compactness, compactness into L² and dominated convergence of the potential give a minimizer. By clipping competitors this is an unrestricted minimizer against smooth bounded variations. Its weak equation is Δb=h(exp(v0+b)−k). Its right side lies in L^p, so the same elliptic estimate gives W^(2,p) regularity, followed by smoothness off the puncture. This gives the advertised asymptotic. A second bounded-remainder solution of the same distributional problem has W^(2,p) remainder by the Poisson equation. Subtract the equations and test by their bounded difference. The negative gradient-square integral equals the integral of a positive weight times (exp(u_1−u0)−exp(u_2−u0)) times their difference. Both vanish. This proves uniqueness of u within this normalized scalar ansatz and specified asymptotic.

This construction solves a weighted exponential equation with Ω to the first power. Direct substitution of a constant-curvature cone metric would require its own check. It is unnecessary here. For related prescribed-curvature equations see [Troyanov, Transactions of the AMS 324 (1991)](https://www.ams.org/journals/tran/1991-324-02/S0002-9947-1991-1005085-9/S0002-9947-1991-1005085-9.pdf).

## Physical norm, limiting holonomy and controls

Integrating the compactified equation gives ∫Ω exp(u) dxdy=πα. Thus the parent's spin kinetic norm of q is κ(E†E)πα in its unscaled field metric. The integrated Cartan curvature on the open surface is −πα H. A small counterclockwise circle about the omitted point has limiting gauge holonomy

    Pα=exp(iπα H),   with SU(3) eigenvalues exp(2πiα), 1, exp(−2πiα).

The sign uses the opposite orientation on the boundary of the compact core. It also follows directly from A=(α/2)H dθ plus the star of a gradient of finite L² norm on the annulus. Existence of the full circular integral limit follows by Stokes and absolute integrability of Ω exp(u). The difference from the flat reference (α/2)H dθ is square integrable because the remainder has gradient in L². Hyperbolic and flat one-form norms agree after integration. The orthonormal spin density exp(u)/Ω is bounded and tends to zero as |w|^(1−2α)log(1/|w|). The orthonormal curvature has the same bound. Hence curvature, quartic products and matter norms are finite. Multiplying by complete-end cutoffs approximates the fields relative to the reference in their first-order graph norms: the connection difference is co-closed on the tail, its derivative is the integrable-square curvature, and the reference spin derivative differs from zero by the product of that L² one-form and a bounded orthonormal spin field. Fermionic expectation values and external gauge fields vanish in this classical vacuum. Metric stationarity under Einstein dynamics is a separate duty.

At α=1/2 take u=log(Ω/4). Since Δ log Ω=Ω² this solves the same equation. Its gauge difference from H dθ/4 has finite norm (the cusp correction is of order dθ/log(1/|w|) in the canonical chart plus regular coordinate changes). It gives orthonormal q=E/2 and ∫Ω exp(u)=Area/4=π/2, exactly the October graded solution. Its subleading logarithm differs from the bounded remainder for the open interval. At α=0 the integrated norm vanishes for the corresponding zero-flux ansatz and q=0 gives the flat control. These endpoint checks do not assume norm-continuity between different affine sectors.

As a check against the finite-amplitude rigidity proof put N=1+κ(E†E) exp(u). The circle mean of log N has asymptotic slope 2α in t=log(1/|w|), also at the endpoint. Its derivative tends to this slope because the mean is convex by c1d2bde1e, and its quotient by t tends to 2α. The resulting integrated positive density is 4πα. This recovers zero at identity and 2π at the October condensate. For nonzero α the gauge connection has a nontrivial limiting parallel transport on E; it is precisely the assumption distinguishing these solutions from the matched-identity proof.

The centralizer calculation for the October principal triple carries over on the open interval. A parallel gauge symmetry must commute with H because the curvature is nonzero everywhere in the interior. Preserving q and compact reality also requires commuting with E and E†. Conversely the entire E6 commutant is parallel since the transitions lie in the triple. The connected unbroken gauge algebra is e6. No spectrum of three chiral families or gravitational field equation follows from the choice of α.

## What has been derived

Fixing the metric, spin, triple and α determines this scalar curvature profile and the norm of the matter field. In particular the ansatz needs no extra freely specified condensate strength. The solution exists for every interior α. Its construction therefore does not select an end angle or weight the vacua. The theorem concerns a single internal surface. Lifting a curved solution through a monodromy requires the metric, fields and operators to return together. Only the related flat history at bf72f2a1e has that two-tick verification.

Please check the normalization of the moment equation, elliptic variational argument, affine kinetic domain and orientation of Pα. Unreviewed hand proof. No scientific code execution, data comparison or foundational parameter credited.
