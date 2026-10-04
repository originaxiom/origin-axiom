# Smooth interior response with fixed boundary metric

This is an authored conditional application of known Dirichlet and
elliptic theory. Finite controls check its algebra and a separate explicit
example, not the general PDE theorem. Independent analytic review remains
owed. No original mathematical novelty or derived physical end law is claimed.

## A common smooth family on the actual silver coefficients

Let X be a fixed smooth connected compact truncation of one of the
specified silver carriers. Keep a smooth Riemannian metric. The recorded
nonzero extension class lies in the kernel of boundary restriction.
In the twisted de Rham model it has a closed representative alpha that
vanishes on a collar: start with a collar-exact representative and subtract
the covariant derivative of a cutoff primitive. This changes no absolute
extension class. The smooth bundle underlying an extension splits as
V plus a trivial line, whether or not its flat connection splits.

On that fixed smooth bundle define

    D_t = [[D_V,t alpha],[0,d]].

It is flat for all complex t: d_V alpha=0 and the upper off-block squares
to zero. Its extension class is t[alpha]; at nonzero t it is nonsplit,
while D_0 splits. The connection is literally independent of t near the
boundary in this chosen relative gauge. This is the differential-form
version of the previously verified peripherally zero cocycle, not a new
assumption that the nonsplit representation can be globally diagonalized.

Choose boundary metric K=K_V direct-sum 1, det K_V=1, fixed for every t.
This is a supplied boundary choice. Wu-Zhang Proposition 3.3 supplies a
unique harmonic metric H_t with boundary K. The parallel determinant
trivialization and scalar Dirichlet uniqueness give det H_t=1. At zero,
uniqueness makes H_0 the direct sum of V's Dirichlet harmonic metric and 1.
The chosen four-plane and line are orthogonal and parallel there.

## Smooth dependence is a Dirichlet statement

In an orthonormal frame at a harmonic metric write D=A+Psi, with A
unitary and Psi Hermitian. A metric perturbation H exp(epsilon s), with
s Hermitian trace-free, changes the orthonormal connection to first order by

    delta C=-D_C s/2,
    delta A=-[Psi,s]/2,   delta Psi=-d_A s/2,
    delta mu=-L s/2,
    L=d_A^*d_A+sum_i ad(Psi_i)^2.

The connection variation in d_A^* is essential to the last formula.
This convention differs by the stated factor and sign from varying a
complex gauge field by exp(epsilon s); it is not a different operator.
For zero Dirichlet values,

    integral tr(s Ls)=integral (|d_A s|^2+sum_i|[Psi_i,s]|^2).

Kato's inequality and the scalar Dirichlet Poincare inequality make this
strictly coercive. L is a real strongly elliptic self-adjoint operator on
Hermitian trace-free endomorphisms, with no Dirichlet kernel. Standard
Dirichlet elliptic theory makes it an isomorphism between the corresponding
zero-boundary C^(m+2,beta) and C^(m,beta) spaces, 0<beta<1. Use a smooth
metric chart and transport the output to a fixed Hermitian bundle. At a
zero of mu its derivative is the displayed isomorphism.

The implicit-function theorem therefore gives a smooth local H_t near
each parameter. Uniqueness identifies it with the metrics supplied above;
elliptic bootstrapping gives smooth parameter dependence in all fixed
finite regularity norms. This is on a compact core, with fixed K. It does
not assert smooth convergence on a complete cusp exhaustion or a uniform
estimate as the core grows. It also does not make our earlier cohomology
projector a full physical Cauchy-data projector.

## A normal response sees what peripheral holonomy does not

Let P_t be the H_t-orthogonal projection onto the flat invariant four-plane,
xi_t=5P_t-4Id and eta_t the upper off-block in an adapted orthonormal frame.
The existing rank-five flag identity at mu=0 gives

    F(t) := integral_boundary tr(xi_t Psi_t(n_out))
          = -(5/2) integral_X |eta_t|^2.

For nonzero t, eta_t cannot vanish identically: otherwise the orthogonal
complement is a flat splitting, contradicting t[alpha] nonzero. Hence
F(t)<0 for every nonzero t, and F(0)=0 with our split boundary metric.

Smoothness gives eta_t=t eta_1+O(t^2) along the real parameter. The first
coefficient is not zero. Infinitesimally changing the orthogonal splitting
replaces alpha by alpha+d_V u; if eta_1 vanished, [alpha] would vanish in
absolute cohomology. The recorded interior class is nonzero there.
Consequently

    F(t)=-C t^2+O(t^4),   C=(5/2) integral_X |eta_1|^2 > 0.

The order-four remainder uses evenness: the constant unitary block phase
conjugates D_t to D_-t while preserving K, so uniqueness and invariant
norms imply F(-t)=F(t). More generally the determinant-one unitary matrix
diag(exp(i theta/5) I4,exp(-4i theta/5)) sends t to exp(i theta)t.
Thus the response depends only on |t| and has the corresponding quadratic
expansion. C depends on the supplied metric, K and the normalization of
the extension parameter. It is NOT a predicted dimensionless constant.

D_t is fixed on the collar and H_t has fixed boundary value K. Its
tangential connection and tangential Hermitian data at the boundary are
therefore unchanged. Its normal derivative, and hence normal Psi and
F(t), respond to the interior. This is an actual conditional way for
global data to reach an end even when the holonomy data alone are unchanged.
It does not say what boundary dynamics would select or match that response.

## The response does not select a vacuum

The retained supplied bare potential is

    V=c integral_X (|F_D|^2+|mu|^2), c>0.

For every admitted member above it is zero, including the split limit.
The whole relaxed restriction of V to this smooth flat family is zero.
The normal flag flux is not its potential derivative: harmonic-map energy
integral |Psi|^2 is a different functional. There is no barrier or preferred
amplitude from this bare restriction, and no computed fermion mass.
This earns the flat-family premise in R83's conditional zero-energy
statement for THESE one-parameter extensions; it does not settle the
different mixed nonlinear family discussed in that report.

Dualizing D and H gives orthonormal connection -C^T. The dual invariant
line has projection 1-P^T and xi_dual=5(1-P^T)-Id=-xi^T. The two minus
signs give the same scalar flag flux. Thus this scalar response alone
does not pick the generation order over its dual. No physical parity
map or classification of the full boundary response is asserted.

## Explicit fixed metric comparator

On unit-area T2 times [-L,L], let N=E04, J=diag(1,0,0,0,-1),
|k|L<pi/2, t=k/cos(kL), h=cos(kL)/cos(kr). Set

    D=d+t N dx,  H=diag(h,1,1,1,h^-1),
    C_r=-k tan(kr) J/2,   C_x=k sec(kr) N,   C_y=0.

The metric is positive, determinant one and equal to Id at both boundary
tori for every k. The full curvature is zero and I=-2mu is zero since
the derivative of k tan(kr) is k^2 sec(kr)^2. For k nonzero the loop
holonomy Id-tN is a nonsplit extension, despite the fixed boundary metric.
It is NOT the silver coefficient: its peripheral matrices vary with k.
Its purpose is to check normal flux, smoothness, signs and the bare energy.

For the invariant first four coordinates, xi=diag(1,1,1,1,-4),

    integral |eta|^2=2k tan(kL),   flux=-5k tan(kL).

The derivative identity verifies the integral with both endpoints, and
the full flag balance follows. Near zero, t=k+O(k^3), flux=-5L t^2+O(t^4).
The dual has the same scalar flux. Reversing the radial sign destroys
flatness and harmonicity; reversing the normals destroys the balance;
freezing H=Id at nonzero t keeps flatness but leaves a nonzero moment.
Those are discriminating controls, not alternatives silently discarded.

## Reading and remaining duties

[Wu and Zhang, Proposition 3.3](https://arxiv.org/html/2109.01776v1)
is the imported compact Dirichlet existence and uniqueness input.
The preceding fork's free-boundary PROOF supplies the Jacobi/coercivity
argument; R81 supplies the flag balance and its rank-two comparator.
R83 supplies the relaxed-energy warning. These are extended here, not
rebranded as missing results. The supplied g, K, physical parent/action
and compact core are not derived by this analysis. A physical end law,
charged domain, stable light spectrum and parameter-free prediction remain
to be constructed in one model.
