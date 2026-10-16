# R28 pre-run argument: three different meanings of source cost

The domain is the one in [the design](SOURCE_ACTION_DESIGN.md).
All statements below concern the declared classical, fixed-metric,
commuting sector unless another domain is explicitly stated.

## 1. A stationary static bulk field already exists in this framework

Use the partially twisted SYM action in Braun et al. (2.13), with a
positive compact-algebra trace. Its internal potential is a sum of
squared complex-curvature and real moment-map residuals. For commuting
phi and W these become d phi, d W and twice div(phi). Thus, with
the stated form-norm convention,

    V_comm = (2/g7^2) integral (|d phi|^2+|delta phi|^2+|d W|^2).

R15's phi=u dF, flat commuting W and Delta F=0 on M minus the source
lines set all these residuals to zero. On any truncated/excised space
the static potential is zero; its limit on the open complement is
also zero. The same background is stationary under regular compactly
supported variations of the full positive-residual potential: at
residuals R_j=0, d/dt sum ||R_j(t)||^2 is zero. This argument has no
unaccounted integration-by-parts term at a singularity. Compact support
also makes every varied nonlinear residual integrable. It extends to
any differentiable admissible finite-residual path, if one is specified.

This does NOT evaluate a delta-function squared on the unexcised
manifold. It does not select a physical defect, variational domain at
the ends, fermion extension, or quantum measure. Choosing which fixed
singular data are admitted remains part of the model. Every admissible
R15 source configuration has this same zero bulk value, so this bulk
minimization does not select its count, residues or through-flux.

The kinetic term for promoting a parameter t to a four-dimensional
field instead contains

    G_tt = (1/g7^2) integral_M |partial_t phi|^2.

There is no identity V_comm=G_tt. An action for the auxiliary scalar
F with energy integral |dF|^2 would be a DIFFERENT action. The field
in the adopted theory is the one-form phi.

## 2. Residue variations: a logarithm in the actual kinetic metric

On an embedded geodesic-tube segment put w=sinh(r)cosh(r), with
theta period 2*pi and central-axis proper length L. The exact local
singular field is

    F=beta log(tanh r),  phi_r=beta/w,  div(phi)=(w phi_r)'/w=0.

Its one-form norm on epsilon<r<R is

    2*pi*L*beta^2 [log(tanh R)-log(tanh epsilon)].

For a residue variation replace beta by delta_beta. The leading
coefficient is 2*pi*L*(delta_beta)^2 log(1/epsilon). Smooth corrections
cannot cancel it: their radial component is bounded on a compact
segment, and their cross term with 1/r is locally integrable. The
positive algebra factor |u|^2 and 1/g7^2 multiply this result. Hence
any nonzero residue variation is nonnormalizable in this fixed-metric
kinetic term, regardless of cancellation of total charges at a cusp.

The exact radial Hessian entries are F'', coth(r)F', tanh(r)F'. With
Ric=-2g, Bochner's identity here is directly the scalar identity

    w (|Hess F|^2-2|dF|^2) = (w F' F'')'.

Thus the integrated rough-plus-curvature energy is a boundary term.
The Hodge residual energy remains zero. Keeping the divergent rough
piece and dropping its boundary/curvature companions would create a
false static-action obstruction. This identity is checked directly,
not imported with closed-manifold boundary conditions.

## 3. Cusp parameters: divergence even without the local source test

In ds^2+exp(-2s)g_T, with flat torus area A,

    F=V+exp(2s)(bs+c)+v,
    Delta_T V=-2b off sources,
    Delta F=exp(2s)Delta_T V+F_ss-2F_s=0.

The high-cusp harmonic L2 corrector v has constant torus average: its
zero mode solves v_ss-2v_s=0 and the exp(2s) solution is not L2. The
nonzero Fourier modes have zero average. This is the R15 growth class,
not an assertion about arbitrary end data.

For a differentiable family in that class, Jensen's inequality on
each torus bounds the radial norm of partial_t phi below by

    A integral_S^R exp(2s) (2 delta_b s+delta_b+2 delta_c)^2 ds
      = (A/2) [exp(2s)(4(delta_b s+delta_c)^2+delta_b^2)]_S^R.

It diverges if (delta_b,delta_c) is nonzero. In particular the
homogeneous through-flux delta_b=0 has divergence
2 A delta_c^2(exp(2R)-exp(2S)); it is not a finite-modulus direction.
If both coefficients vanish the lower bound is zero, not a theorem
about all tangential or source variations. Section 2 still detects
individual nonzero residues whose total variations cancel.

No compact gauge compensation removes this lower bound. Invariance
of the algebra inner product gives <u,[epsilon,u]>=0, while these
variations have a nonzero u component. A gauge-induced field velocity
is orthogonal to that component pointwise. This fixes the metric and
source positions; diffeomorphism compensation, boundary kinetic terms
and a resolved UV theory are outside the statement. Nonnormalizable
background parameters are not forbidden backgrounds and are not
ordinary four-dimensional scalar moduli in the stated kinetic metric.

## 4. A sharp price for resolving a specified abelian core

Consider a finite geodesic cylinder of radius epsilon and length L,
with zero flux through its axial end caps. Specify the radial total
flux 2*pi*L*beta, as in the exterior logarithmic field. The cylinder
volume is pi*L*sinh(epsilon)^2. For a smooth commuting one-form in
the bare, unshifted theory, Stokes and Cauchy--Schwarz give

    integral_core |div phi|^2 >=
       (2*pi*L*beta)^2/(pi*L*sinh(epsilon)^2)
       = 4*pi*L*beta^2/sinh(epsilon)^2.

This is a lower bound on the D-residual part, before its positive
action/algebra factors. It is not based on guessing one profile.
The axially invariant regular profile

    phi_r=beta tanh(r)/sinh(epsilon)^2

attains it, with uniform divergence 2 beta/sinh(epsilon)^2, and matches
the exterior field at r=epsilon. It is smooth at the axis. The joined
field is continuous and piecewise smooth, not C-infinity across the
join; no delta jump appears in its first-order divergence. The bound
holds for smooth cores, and this matched piecewise profile gives the
exact local saturation/control. Refining the join is a separate issue.

For beta nonzero the bound grows as epsilon^-2. Therefore a bounded-
cost zero-radius resolution with these fluxes cannot use only this
bare commuting D-square. It must change some specified input: add a
source moment map or boundary subtraction, alter the core/field theory,
allow cap flux, or keep finite radius. This is NOT a universal no-go
for nonabelian defects, renormalized sources or a complete theory.

For an explicit opposite control, adding a prescribed density rho
changes the potential to ||delta phi+rho||^2. The above core then has
zero residual for rho=2 beta/sinh(epsilon)^2. This is a finite regulated
stationary minimum with an EXTERNAL source, not a derivation of rho
or its missing fields. Removing the shift restores the sharp cost.

## 5. The action-scope control on the new trace-map claim

For an autonomous regular discrete L(a,b), the DEL equation
L_2(a,b)+L_1(b,c)=0 preserves omega=L_12(a,b) da wedge db. On a
connected invariant real domain with L_12 nonzero, this fixes orientation.
It does not require the coordinate Jacobian to be one: it is
L_12(a,b)/L_12(b,c). For L=exp(a)b the map is (b,-exp(a-b)); its
Jacobian is exp(a-b), and its area density is preserved exactly.

The actual half-step reverses the stated invariant leaf form; that
obstructs a regular autonomous same-state real DEL description on
such a domain. The extension to NO stationary action is false:

    L_n(a,b)=(-1)^n (ab-a^2/2)

has regular mixed derivative (-1)^n and DEL equation
(-1)^n(c-b-a)=0, the Fibonacci half-step. A time-dependent symplectic
form is transported; no fixed-form preservation theorem is violated.

There is also a stationary action for the entire nonlinear map T,
without a linearized leaf substitution:

    S=sum_n p_(n+1) . (x_(n+1)-T(x_n)).

Its p equation is the map, and its interior x equation is
p_n-DT(x_n)^T p_(n+1)=0. Every orbit lifts with p_n=0. This uses an
enlarged state and is a saddle-type multiplier action, not least
action, a same-state regular autonomous L, or a physical field theory.
The actual trace-map invariant and anti-Poisson property remain true;
the half-monodromy's square remains the geometric monodromy. Action
existence alone, without its restrictions, does not select that tick.

## 6. What this can pay

It can establish classical static bulk compatibility of the existing
sourced background with the already adopted action, locate which
source changes are frozen end data, and impose a quantitative local
requirement on a chosen resolution. It cannot pay source activation,
the physical fermion domain, quantum anomaly completion or the neutral
four-dimensional limit. The same-source three/zero result is retained
conditionally, not identified with a new index or declared a full TOE.
