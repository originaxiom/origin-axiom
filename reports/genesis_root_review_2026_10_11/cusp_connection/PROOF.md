# Curvature realizes an end unit without selecting it

## The automorphic line and its metric

Let B=PSL(2,Z)\H be the effective modular orbifold with curvature minus one. For even integer k define L_k by the fibre action v -> (cz+d)^k v. Since Im(gamma z)=y/|cz+d|², the squared norm y^k|v|² is invariant. The norm is smooth in orbifold charts; this does not mean the metric is smooth in the coarse coordinate at elliptic points.

There is a direct Hodge interpretation of the factor y. On E_z=C/(Z+zZ), write w=u+zv with 0<=u,v<=1. Then (i/2) dw wedge dbar(w)=y du wedge dv, so the squared L² norm of dw is y. Tensor powers give y^k. Choosing this Hodge metric is natural given the elliptic family; selecting the tensor power as a physical coupling is a further choice.

At z=i the S stabilizer acts on the fibre by i^k. At z=exp(2pi i/3), ST acts by exp(i pi k/3). Both are trivial exactly when 4 and 6 divide k, hence when 12 divides k. The generic minus identity already acts trivially at these weights. Thus 12 is the least positive integral weight with these trivial isotropies within this family. This is not a proof that a physical twist must be positive, nonzero or trivial under elliptic isotropy.

## Curvature and effective flux

For a holomorphic line frame with h=exp(phi), the Chern connection has (1,0) form partial phi and curvature

    F = -partial bar-partial phi
      = (i/2)(phi_xx + phi_yy) dx wedge dy.

The unitary-frame connection is A=(i/2)(phi_x dy - phi_y dx), whose exterior derivative gives the same F. For phi=k log y,

    A = -ik/(2y) dx,
    F = -ik/(2y²) dx wedge dy = -ik/2 dA_hyp.

In the stated fundamental region,

    Area(B) = integral[-1/2,1/2] dx/sqrt(1-x²) = pi/3.

Consequently for k=12n,

    (i/(2pi)) integral_B F = n.

The curvature is smooth everywhere on the open orbifold. No delta-function source is present there. The compactifying cusp is not a point of this open base, and its extension data have not disappeared.

All integrals above use the effective quotient. If the same pulled-back form is integrated with stack weights over SL(2,Z)\H, generic isotropy of order two divides these integrals by two. The metaplectic quotient has generic kernel of order four over PSL(2,Z), dividing them by four. Local equations are unchanged. None of these normalizations is automatically a physical charge, and no base flux is identified with the index on M_1,2 by matching integers.

## Source-free bulk equation and the price of a sector

Write F=-if dA_hyp with real f. The Abelian bulk Yang–Mills equation d star F=0 says df=0. Thus the Hodge connection obeys it. Its energy is

    E_n = (1/(2g²)) (6n)² (pi/3) = 6pi n²/g².

For any square-integrable f with integral f dA=2pi n, let fbar=2pi n/Area=6n. Expanding the square gives

    integral f² dA = Area fbar² + integral (f-fbar)² dA.

This proves the fixed-flux lower bound, including its equality condition. Compactly supported connection variations have no end boundary term and give the stated bulk equation. Variations allowed to change end flux are a different problem: boundary terms need not vanish. Finite energy alone does not impose that boundary condition.

Within the integer sectors, n=0 has lower energy than every nonzero n. Only after imposing nonzero integer flux do |n|=1 minimize this particular energy. Orientation and sign are not selected. This limited conclusion says nothing against other actions, coupled fields or boundary mechanisms.

Under g_metric -> ell² g_metric, the flux stays n and energy becomes E_n/ell². Thus no physical coupling or length is obtained from the numerical normalization of this two-dimensional calculation.

## The discriminant frame and continuous open flux

Assume HDelta as declared in PREREGISTRATION.md. On compact subsets of |q|<1, the sum of |q|^m converges. The logarithm of product (1-q^m) converges locally uniformly, so Delta has no zeros in H. At the cusp Delta=q(1+O(q)). Therefore Delta^n trivializes L_12n on the open base, and its simple zero identifies the compactified extension with O(nD), D the cusp divisor. This identification uses the declared modularity hypothesis, not a new index computation.

In this global frame the squared metric is

    h_n = y^(12n) |Delta|^(2n).

log |Delta|² is locally harmonic, so this metric has the same curvature as above. It also shows why holomorphic triviality does not imply a chosen connection is flat. Setting the metric equal to one in this frame instead gives a flat connection on the same open holomorphic line. The isomorphism of holomorphic bundles does not identify those Hermitian connections.

More strongly, h_s=(y^12 |Delta|²)^s is a globally positive smooth orbifold metric on the open trivial line for every real s. The logarithm is single-valued because its argument is positive. Its curvature is -6is dA and its effective flux is s; the same fixed-flux energy argument applies. A noninteger s is not claimed to define the integral extension O(sD). This witnesses exactly what unrestricted smoothness and finite action on the open base do not quantize. Keeping a particular compactification extension with suitable end growth is an additional restriction.

For y=Y>1, Delta's winding along x from -1/2 to 1/2 is one: its q factor winds once and each (1-q^m) factor has zero winding. In the global unitary frame,

    integral_(x increasing) A_s = is(2pi - 6/Y).

The top boundary of the truncated oriented fundamental region runs with x decreasing. Paired edges cancel. Stokes gives

    (i/(2pi)) integral_(B truncated at Y) F_s
      = s (1 - 3/(pi Y)),

equal to the direct curvature integral with Area=pi/3-1/Y. Taking Y to infinity recovers s. This is an end contribution, not a hidden compactly supported bulk source.

## The norm changes with the connection

For a section of original modular weight k0 represented as f=Fmod/Delta^n, the O(nD) frame metric above gives

    |f|² y^k0 h_n dA_hyp
      = |Fmod|² y^(k0+12n) dA_hyp.

This is a pointwise isometry of the specified Hermitian holomorphic descriptions. Near the cusp, Fmod=O(q^lambda), lambda>0, yields a bound by C exp(-4pi lambda y) y^(k0+12n-2) dx dy, integrable for every finite polynomial exponent. By contrast, with the unchanged weight-k0 norm, a nonzero leading term of f at q^(lambda-n) is not integrable when lambda-n<0. For integer n and the noninteger exponents in W47, these distinguish the canonical and pole-admitting conditions.

This does not contradict W47's normalizability test at every polynomial weight: h_n in the original trivialization changes the exponential end behavior, not just the polynomial weight. It supplies a concrete Hermitian interpretation of an already-chosen extension, not a proof that the original operator admits extra modes without changing its metric or domain.

## What is and is not carried upstream

The inference from a torsion Picard group or an available flat trivialization to the absence of nonflat connections is invalid. The explicit metrics above distinguish the claims. W47's enumerated flat characters and its fixed-metric cusp-exponent calculation are not overturned by this distinction.

The positive output is a smooth source-free bulk solution and a finite-action representative for each supplied unit on the effective modular base. It does not establish a full finite-action solution after pullback to the real-four-dimensional total space: the total metric, fibre volume, boundary conditions, matter coupling and backreaction matter. Nor does it establish a Fredholm Dirac operator there or its physical particle spectrum. Those are separate analytic and physical obligations.

No genesis assumption selecting n=1 has been removed. The realized unit remains conditional, but “it must be an added bulk singular source” is not justified by open-bundle triviality. The remaining selection question concerns the allowed end sector and its physical coupling.
