# All smooth zero-energy fields on the single fibre with the matched end

19 November 2026. Author proof for independent scrutiny. This upgrades the local quartic test at 2f3337de5 to a finite-amplitude result under a stated affine-domain hypothesis. The application is to the supplied classical action on a complete once-punctured elliptic curve. The metric and action remain inputs.

## Statement

Fix an extending spin structure and a smooth flat unitary reference with identity holonomy around the puncture. Require the spin fields to have finite physical kinetic norm. Require the gauge connection to differ from the reference by a one-form of finite kinetic norm in a common end identification, or equivalently require such an identification to exist. Only the tail needs this condition. Take a smooth solution of the parent's zero-energy equations on the open surface.

Then the gauge connection is flat, has trivial peripheral holonomy and extends as a flat local system over the filled torus. Both spin coefficients are parallel with respect to this gauge connection and the **auxiliary flat spin metric of the filled elliptic curve**. They commute with one another and their adjoints. Conversely flat torus holonomies with compatible parallel commuting normal spin coefficients give exact finite-norm zero-energy states in a matching end identification. Their physical spin norm uses the hyperbolic metric throughout. This is a classification in terms of flat local systems with compatible coefficients, before quotienting or imposing a base return.

## A positive density from the two coupled equations

Use the flat translation coordinate w=x+iy and flat square-root frames of dw, with constant sign transitions. As in 2f3337de5 the physical metric is Ω²|dw|², and each coefficient has norm squared integrated against Ω dxdy. Write Q,R for the full varying coefficients, m=[Q,Q†]+[R,R†], and F for the Hermitian coordinate curvature. The parent's three equations, with its fixed relative sign, are

    (D_x+iD_y)Q=(D_x+iD_y)R=0,     F=−Ω m,     [Q,R]=0.

Augment the pair by a constant scalar: s=(1,Q,R) in the orthogonal sum of a trivial line and the two unitary gauge/spin coefficient bundles with their auxiliary flat spin metric. Write N=||s||²≥1, u=log N, e=s/sqrt(N), and Π=1−ee†. The constant line carries the trivial connection. It keeps u regular at simultaneous zeros and will fix the scalar component when equality occurs.

The first equation gives D_y s=iD_x s and (D_x²+D_y²)s=−ad(F)s on the two adjoint slots, zero on the scalar. Since
Re<s,ad(F)s>=κ(Fm), differentiation gives

    ΔN = 4||D_x s||² + 2Ω||m||²,
    |∇N|² = 4|<s,D_x s>|²,
    Δu = 4||ΠD_x s||²/N + 2Ω||m||²/N ≥ 0.              (1)

Here Δ is the ordinary positive-second-derivative sum in w, and inner products use the same positive invariant trace as the parent. The complex inner product is conjugate-linear in the first slot. Translation and constant-sign transitions make u and Δu dxdy global. The two real horizontal derivatives of the unit ray [s] have total squared covariant norm 2||ΠD_x s||²/N, which is bounded by Δu/2. Nothing in (1) requires the gauge connection to start flat.

## Finite matter norm caps the total at 2π

Center the affine coordinate at the puncture, take r=|w|, t=log(1/r), and put U(t) equal to the angular average of u. The physical cusp factor in this regular coordinate is comparable to 1/(r log(1/r)) as r→0, by the smooth change from the distinguished cusp coordinate. The finite kinetic norm and finiteness of ∫Ω dxdy imply

    ∫^∞ (exp(−t)/t) average_θ N(t,θ) dt < ∞.

Periodicity cancels opposite edges of the affine parallelogram. On the compact surface with this disk removed, the outward normal points towards smaller r. Green's identity gives exactly

    2π U′(t) = ∫_{surface outside disk} Δu dxdy.

The integral is increasing and nonnegative by (1). If U′ ever exceeded 1 on the tail, convex growth and Jensen's inequality average N ≥ exp U would contradict the displayed norm bound. The limit exists and the total T=∫ Δu dxdy lies in [0,2π]. This argument allows unbounded coefficients. A pointwise boundedness assumption would bypass the main domain issue.

## The same total belongs to 4π times the integers

Trivialize the flat reference gauge in a parallel frame on the puncture annulus. The extending spin square-root frame is also single-valued there in the auxiliary flat spin metric. The actual unitary connection matrix in the two coefficient slots is square integrable in these frames: its norm is bounded by a representation constant times the norm of the adjoint-valued difference connection. The latter one-form norm is conformally invariant in two dimensions. In particular its angular component has finite squared norm integrated over dt dθ. The covariant angular speed of the ray [s] has finite squared norm in this cylinder by (1) and finiteness of T. Its ordinary angular speed is bounded by the covariant speed plus the angular connection norm. Hence there exists a sequence t_j→∞ on whose circles the integrals of both squared ordinary ray speed and squared connection norm tend to zero. This uses simultaneous integrability of their sum.

Let α=Im<e,De>. From D_y s=iD_x s one gets α_x=−u_y/2 and α_y=u_x/2. On the positively counterclockwise circle α integrates to π r times the radial derivative of the mean, i.e. −π U′(t). On the selected circles, replacing D by the ordinary derivative changes the integral by o(1) by Cauchy–Schwarz.

The distance of ∮Im<e,de> from 2π times the integers tends to zero on these circles. Here is the explicit phase argument. The ray loop has length tending to zero, so it stays in a fixed small projective ball around its starting ray. In that ball choose the unit lift by projecting the starting unit vector onto each ray and normalizing. The normalization denominator stays bounded away from zero. Its derivative is bounded by a universal constant times the derivative of the orthogonal ray projector, hence by a constant times ray speed. This lift is periodic and its connection integral tends to zero. The actual periodic unit vector e differs by a smooth circle-valued phase. That phase contributes exactly 2π times an integer. No assumption that e itself has small angular speed is needed.

Consequently −T/2, the limit of ∮α, belongs to 2π times the integers. Combined with 0≤T≤2π this forces T=0. The factor of two between unit-vector phase and squared norm is essential. As a local normalization control a holomorphic scalar pole of order one with s=(1,1/w) has ∮α→−2π, mean log N asymptotic to 2t and flux magnitude 4π. That pole violates precisely the physical kinetic bound.

## Equality and the physical scope

Equation (1) now gives m=0 and ΠD_x s=0 everywhere. The first component of D_x s is zero, whereas the first component of s is one, so D_x s=0. The other derivative also vanishes. The moment equation forces F=0. The two parallel coefficients commute by the remaining vacuum equation. The elementary simultaneous triangularization argument in 2f3337de5, now for two matrices, uses m=0 to make them jointly normal. Parallel here refers to the stated auxiliary metric, and permits decay of the orthonormal hyperbolic spin amplitude.

For a flat connection, the conjugacy class of the circular gauge holonomy is constant along the end. Its distance to the identity is bounded by the integral of the angular connection size in the reference parallel frame, which tends to zero along a sequence. This last bound is applied to the original gauge connection, whose difference norm was assumed finite. Therefore the flat holonomy is the identity. The two handles commute and define a flat system on the compactified torus. Conversely such a representation extended to the punctured surface is flat-trivial on the annulus. A matched identification gives zero difference on the tail. Its compatible spin coefficients have sign s on transport and finite norm ∝ ∫Ω dxdy, and each residual vanishes pointwise. With simply connected E8 an annular frame identification has no winding obstruction to a global smooth gauge choice. All arguments identifying curvature and holonomy are gauge invariant in the stated, transported domain.

This accounts for both candidate zero-field backgrounds, for their allowed spin amplitudes, and for arbitrary smooth excursions solving the zero-energy equations in this same affine sector. Their classical energies remain exactly equal. The return may restrict which flat pairs and spin data form histories. A connection of nonzero curvature cannot be obtained from a smooth zero-energy bifurcation in this sector, even at finite amplitude. Neither finite-normness of a variation alone nor just naming a limiting conjugacy class proves that a distant configuration belongs to this affine sector. Check the difference norm or a valid end identification before transferring the conclusion.

The October spin-compensating solution carries different limiting gauge holonomy and therefore is outside these assumptions. The earlier puncture-deforming flat history also changes this holonomy, and its flat tangent has infinite kinetic norm. Both remain valid in their stated problems. Positive-energy stationary points, nonsmooth sources, other spin extensions, other end sectors, dynamical metrics, fermion determinants and quantum weights require separate treatment. The theorem gives a reason to stop searching for a smooth classical zero-energy matter selector *inside this particular matched end*. It leaves the selection of that sector and the full physical vacuum open.

Source trail: the curved action, signs and norms are in weave_curved_action_2026_10_08/PROOF.md, and the affine graph comparison is explicit in weave_global_condensate_2026_10_08/PROOF.md. The compactification and cusp factors are in the companion at 2f3337de5 and [Wolpert, equation (1)](https://www.math.umd.edu/~saw/preprints/Cusps.pdf). The earlier ACTUAL_ZERO_MODE_CURRENT_AND_RANK_ONE_VECTOR_2026_11_08.md uses a subharmonic norm on a flat auxiliary background. Here (1) uses the unknown nonlinear curvature, and the phase quantization removes the need to assume boundedness. Independent review should focus on the curvature sign, factor of two, inclusion of the original difference connection in L², and simultaneous small-circle sequence. No run, data reading, independent acceptance or banking.
