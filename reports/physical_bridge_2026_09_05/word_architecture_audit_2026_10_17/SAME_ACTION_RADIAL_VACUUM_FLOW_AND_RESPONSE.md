# Same-action radial vacuum flow and its nonconstant fermion block

October 25, 2026. UNREVIEWED analytical derivation, not a scientific run,
new numbered arc, main acceptance or physical chirality result. No module
was imported, collected or executed. Frozen test packages are unchanged.

## Reused theory and declared quantifier

The [curved action](../weave_curved_action_2026_10_08/PROOF.md),
[graded condensate](../weave_graded_condensate_2026_10_08/PROOF.md),
[SM parallel phase](../weave_sm_parallel_2026_10_08/PROOF.md) and
[neutral stability analysis](../weave_neutral_stability_2026_10_08/PROOF.md)
were reread in full. The latter already contains a stationary NONPARALLEL
neutral SM-gauge minimum; its amplitude is genuine, and its charged
index remains zero by decaying-perturbation invariance. Nonparallel
stationarity is therefore not missing in the existing theory.

The local [cusp solution](../weave_cusp_condensate_2026_10_08/PROOF.md)
already derives the fixed nonzero amplitude, connection and logarithmic
dressing. The [actual graded response](ACTUAL_GRADED_CUSP_RESPONSE_AND_STATE_SCOPE.md)
already derives the constant-background Cauchy plane. These are recovery
controls, not new constructions here. Targeted code/source searches
used radial, nonparallel, gradient flow, Nahm, H_dot and E_dot; they
are not a complete absence sweep or a claim of novelty for the general
matrix-flow method.

This note restricts the SAME supplied action to zero-residual,
x-independent cusp configurations in radial gauge. It does not cover
every stationary point (the magnetic mu!=0 solutions are outside),
every angular/nonlinear profile, every bundle, or every physical end.
Boundedness below is an explicit additional hypothesis, NOT a consequence
claimed here of finite energy on a finite-area cusp.

## Derive the radial equations from all vacuum residuals

On the old curvature-minus-one cusp put t=log y, Omega=1/y. Use
Hermitian H(t) and complex Lie-algebra matrices E(t),G(t), with

    A_x=-H(t)/(4y), A_y=0,
    q=E(t)/(2 sqrt(y)), r=G(t)/(2 sqrt(y)).        (1)

These q,r are the source's holomorphic spin coefficients. The
orthonormal coefficients are E/2,G/2. Retain the old peripheral
transition p with H even and E,G odd, so the extending spin sign
and gauge transition agree. This is a sector choice, not a proof
that all backgrounds can be made x-independent by gauge.

Direct differentiation in Dbar=partial_x+i partial_y-i ad A gives

    Dbar q = i(4 dot E-2E+[H,E])/(8 y^(3/2)),
    Dbar r = i(4 dot G-2G+[H,G])/(8 y^(3/2)),
    F_xy = (dot H-H)/(4y^2).

The actual moment residual and F term therefore give exactly

    dot H = H-[E,E dagger]-[G,G dagger],
    dot E = E/2-[H,E]/4,
    dot G = G/2-[H,G]/4,
    [E,G]=0.                                    (2)

No independent radial mass or endpoint functional has been inserted.
Hermiticity of H, tracelessness and the p parities are preserved.
The algebraic constraint is preserved because

    d[E,G]/dt = [E,G]-[H,[E,G]]/4.

The fixed points recover the old parallel equations H=[E,E dagger]+
[G,G dagger], [H,E]=2E, [H,G]=2G and [E,G]=0. Both the old one-triple
and genuine two-field examples retain their original scopes.

## An elementary monotonicity control, not a selected potential

Use the same positive invariant trace in a faithful compact matrix
realization. Define the real auxiliary function

    P=Tr(H^2)/2-Tr(H([E,E dagger]+[G,G dagger]))
        +2 Tr(E dagger E+G dagger G).            (3)

Cyclicity gives its real differential

    dP=Tr((H-[E,E dagger]-[G,G dagger]) dH)
       +2 Re Tr((2E-[H,E]) dagger dE)
       +2 Re Tr((2G-[H,G]) dagger dG).

On (2), with the induced positive trace norms,

    dot P=||dot H||^2+8||dot E||^2+8||dot G||^2 >= 0.  (4)

P is an auxiliary radial monotone. It is NOT an added four-dimensional
energy, an observer-selection law or a replacement for the parent
potential, which vanishes on these residual-zero solutions.

For a bounded forward trajectory, P is bounded and the integral of
the right side of (4) is finite. The vector field and its derivative
are bounded on the compact closure of that trajectory, so its speed
is uniformly continuous. If it did not tend to zero, bounded derivative
would give disjoint intervals of uniformly positive integrated squared
speed, contradicting finiteness. Hence the speed tends to zero and
every accumulation point satisfies the old parallel equations.
Equivalently, distance to their closed critical set tends to zero.
No nonconstant bounded periodic radial orbit is possible by (4).

This does not prove convergence to one fixed point, choose its gauge
algebra, force a uniform spectral gap, or classify unbounded finite-
norm trajectories. It does not extend the old parallel charged-index
statement to every nonparallel physical end. Different limiting
equilibria, enhanced end symmetries and nonzero angular fields remain
distinct possibilities.

## A one-triple nonconstant sector and its remaining freedom

For a fixed compact triple (H0,E0,E0 dagger), set

    H=h(t)H0, E=f(t)E0, G=0, h,f real.

Then (2) reduces, with no new coefficients, to

    dot h=h-f^2,      dot f=(1-h)f/2.            (5)

The nonzero parallel control is (h,f)=(1,1). In variables
eta=h-1, xi=f-1 the exact linearization is

    (dot eta,dot xi)^T = [[1,-2],[-1/2,0]](eta,xi)^T
                         +(-xi^2,-eta xi/2)^T.  (6)

The characteristic polynomial is lambda^2-lambda-1. Its one negative
and one positive root supply one decaying and one growing direction.
These are dimensionless RADIAL linearization rates in the supplied
metric, not particle masses, a new genesis selector, or observational
evidence from a familiar polynomial.

Small exact decaying half-line solutions can be obtained locally by
the usual integral construction, stated here to expose the freedom.
In the real eigenbasis let lambda_s<0<lambda_u and N be the quadratic
term. Prescribe a small stable coefficient c at t=T and solve

    z_s(t)=c exp(lambda_s(t-T))
       + integral_T^t exp(lambda_s(t-s)) N_s(z(s)) ds,
    z_u(t)=-integral_t^infinity exp(lambda_u(t-s)) N_u(z(s)) ds. (7)

For 0<alpha<-lambda_s, the weighted sup norm
sup exp(alpha(t-T))|z(t)| bounds both integrals of quadratic terms
by a constant times the squared norm. On a sufficiently small ball
their Lipschitz constants are less than one. This gives a decaying
solution of (6), hence (5), for each sufficiently small c. For c!=0
it is nonconstant. This is a tail construction, not a core-matching
theorem or a new global stationary phase. The amplitude c is boundary/
matching data; it has NOT become forced by solving the end equations.
Bounded decaying tails have finite end kinetic and residual norms by
the same finite-area/graph estimates as the existing cusp control.

## Derive the actual varying fermion block

Keep every Weyl slot and the old normalized kinetic measure dt.
For weight m in a spin-j module of H0 and even m in a paired
zero-angular channel, let

    a=1/2+h m/2,    b=h(m+1)/2,
    k=f sqrt((j-m)(j+m+1)/2).

The old normalization of the gauge Killing map and superpotential
Hessian now gives

    D1=(partial_t+a,-k)^T,  D2=(k,partial_t+b).

The scalar/form gauge slot contributes 1/2 from its sqrt(y) kinetic
rescaling; the spin slot does not acquire that same term. The
background equation (5) supplies

    dot k=(a-b)k,
    D2 D1=k(a-b)-dot k=0.                      (8)

Thus the background and the actual linearized complex check each
other. Setting a=b away from h=1 would violate (8). The R slot
remains trace-dual at weight -m-1, not a deleted second spin field.
The complete singular block, using adjoints in dt, is

    B=(D1,D2 dagger)
      =[[partial_t+a,k],[-k,-partial_t+b]]
      =J(partial_t+K(t)),
    J=diag(1,-1), K=[[a,k],[k,-b]]=K dagger.    (9)

With the SAME constant unitary transport as the old response proof,
the self-adjoint doubled fermion block becomes

    D=-i sigma1 partial_t-sigma2 tensor K(t).

But its square is NOT the old scalar threshold with parameters
replaced by h(t),f(t):

    B dagger B=-partial_t^2+K^2-dot K,
    B B dagger=J(-partial_t^2+K^2+dot K)J.      (10)

Also tr K=(1-h)/2, so K^2 need not be scalar. Both this trace and
dot K must be retained. The upper A extreme has scalar K=a at
m=j; the lower Q extreme has scalar K=h j/2. Dropping the extreme
slots would again change the operator.

At h=f=1, a=b=(m+1)/2, dot K=0 and (9)--(10) recover the old exact
blocks and gaps. For the small tails (7), K-K_infinity decays, so
the gap at infinity of a chosen gapped graded phase is unchanged.
This is not a new zero-mode count.

## The response follows the full profile, not its instantaneous sign

At zero energy x'=-K(t)x, v'=K(t)v. For a specified tail with
exponentially gapped limit, its L2 stable spaces determine the
Cauchy plane. Their pairing x dagger v is constant, so the two
stable spaces are orthogonal complements. If P(t) is the orthogonal
projector onto the x-stable space, differentiating its evolving
subspace gives

    dot P=-(I-P)KP-PK(I-P),
    P(t) -> P_+(K_infinity).                   (11)

The exterior Cauchy plane is P(t) in x and I-P(t) in v. In general
P(t) is NOT the instantaneous spectral projector P_+(K(t)); the
matrices K at different radii need not commute. The same-action
profile fixes (11), rather than supply a freely chosen boundary plane.
Its positive exterior norm is the integral of the actual transported
profiles, not simply 1/(2|K(T)|). The old formula is recovered for a
constant tail. Initial profile/core data are still independent until
the stationary global matching problem fixes them.

On the same charged SM blocks, bundle and graph domain, an actual
global background differing from the old gapped phase only by bounded
decaying zeroth-order coefficients has a graph-compact fermion
perturbation: compact-core Rellich plus uniformly small tail norm.
Its charged Fredholm indices therefore remain those of that phase.
This reuses the old compact/decaying perturbation argument, not a
new exclusion of changed asymptotic states, bundles or end laws.

## Input accounting and review duties

The radial transport, varying mass block, derivative term and boundary
response evolution are derived CONDITIONALLY from the old action and
ansatz, not independently supplied normal masses or metrics. This
does not derive the action, metric, embedding, physical field map,
spin choice, background selection or core matching from genesis.
No complete priced-input row is paid; no observed mass, SM3 spectrum,
gravity or physical vacuum has been obtained.

Independent review must check the signs and factors directly against
the source action, both spin/dual slots and the actual kinetic frames;
the bounded-flow scope; the half-line contraction and not globalize it;
the derivative term in (10); the stable-projector rather than local-
sign rule; and the fixed-domain hypotheses in the index statement.
Any executable successor needs its own complete sealed sources,
independent/main review and genuine prospective admission. The ten
P210 controls and all other frozen packages remain unrun here.
