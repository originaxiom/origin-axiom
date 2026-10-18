# Deriving an exterior response from a specified joined action

October 18, 2026. Conditional analytical continuation. The existing
source action determines interface momentum matching, and its actual
radial operator determines an evolution equation for a boundary response.
An exterior solution or state is still required to fix that response.
Eliminating exterior modes is legitimate only when the required inverse
exists; zero modes instead impose compatibility equations and remain
part of the joined configuration.

This uses the owner's whole-architecture question: relations can feed
back on the fields being related. It does not assume every mathematical
join physically occurs or derive the supplied gauge action from PF1.

## Source and existing positive results

Personally read in full at the current branch checkpoint `b33fe3dcc`:

- [The normal variational join](../surface_variational_join_2026_10_16/PROOF.md).
  Its specified compact gauge action admits a local noncommuting BPS
  family and a corresponding fermionic tangent with a supplied end
  subtraction. The subtraction and outer data are not selected there.
- [The actual source boundary variation](../surface_global_boundary_variation_2026_10_16/PROOF.md).
  It derives the seven-residual source momenta, the tilted normal,
  retained primitives and the real fermionic boundary pairing.
- [Same-action transmission](../surface_same_action_transmission_2026_10_16/PROOF.md)
  and its complete design. Matching across an artificial smooth cut
  already preserves the actual fields, currents, charges and remote
  domains. Removing such a cut preserves the kernel; it produces no
  generation count. This result is reused, not a newly found join.
- [All-angular response](../surface_all_angular_response_2026_10_16/PROOF.md)
  and [the normal Gaussian](../weave_end_gaussian_2026_10_09/PROOF.md).
  They retain existing regular solution planes, boundary work and
  charged endpoint factors. A vanishing overlap cannot be replaced
  by a pure phase through division by its modulus.

These are authored research sources with their own analytic and
execution qualifications. Reading them does not provide fresh
independent acceptance. No producer is imported or executed here.

## The action supplies the interface equation

Let a specified local action on a region Omega have first variation

    delta S_Omega = integral_Omega EL delta Phi + theta_boundary.

At a smooth interface Sigma, retain a fixed common identification of
all field and bundle traces from regions Omega_- and Omega_+. At this
stage the cut and metric are fixed; no moving-boundary derivative is
being assumed. For second-order bosonic fields write the boundary
potential as <pi_out,delta q>, including its actual source weights
and all other prescribed terms. Variation of S_-+S_+ gives

    q_-=q_+=q,
    pi_-^out+pi_+^out=0.                          (1)

It does not set both momenta separately to zero. In the actual
seven-residual potential V=2 sum_j B(C_j,C_j), the inherited momentum
is 4 L(n)^T C, integrated against the actual surface density. Using
rough-curvature energy while omitting its calibration primitive would
change (1). A separately added interface action W(q) would change it
to pi_-+pi_++dW=0 and must therefore be named as another input.

Suppose the exterior has a differentiable branch of stationary fields
Phi_+(q) for given trace q and fixed remote data. Substituting into
its action gives a boundary functional S_+^os(q). The chain rule and
the exterior Euler equation give

    d S_+^os(q)[delta q]=theta_+(Phi_+(q);delta q).  (2)

Its variation supplies precisely the response in (1). Existence,
uniqueness, smoothness and remote data are hypotheses of this
elimination, not consequences of the notation os. If there are several
stationary branches, (2) is a separate relation on each branch. If
the boundary work is not integrable on the admitted family, there
need not be a scalar S_+^os on that family at all. The old quantum
inverse-current nonintegrability result cannot be bypassed by (2).

For first-order fermions the corresponding data are the exterior
Cauchy traces with the actual Green pairing. A scalar Dirichlet
functional for every spinor component is not assumed. Matching the
full two-sided trace is already the supplied transmission result.
Selecting a one-sided subspace requires an actual exterior domain.

## The actual radial system induces a response equation

The same-action transmission source retains all 28 radial blocks in

    f'=-K(t) f,
    K=C0/t+g^2 t D/(1-g^2 t^2)
            +g Y/(1-g^2 t^2)+rho t A,
    K^dagger=K, K V+V K=0.                        (3)

Here C0 is the indicial matrix, distinct from the nonlinear residuals
C_j above. V is the fixed nondegenerate normal current matrix of the
block, and rho is the horizontal coefficient from that source.
All following statements are on a smooth finite interval avoiding
t=0 and 1/g, with the same fixed source parameters and full blocks.

If T(t,t0) is the fundamental solution, differentiation gives

    d(T^dagger V T)/dt=-T^dagger(K^dagger V+V K)T=0.

Thus a supplied exterior trace plane L0 at t0 has exactly transported
response L(t)=T(t,t0)L0. Nondegeneracy and invertibility preserve its
dimension; a maximal current-null plane stays maximal current-null.
This is the old transfer identity applied to the end-response duty.

For a fixed splitting f=(u,v), write

    K=[[A0,B0],[C0tilde,D0]], v=R(t)u.

Where projection of L(t) to the u coordinates is invertible,

    u'=-(A0+B0 R)u,
    R'=-C0tilde-D0 R+R A0+R B0 R.                 (4)

This follows by differentiating v=Ru and substituting both component
equations. It is the exact Riccati evolution of the response, with
the source's noncommuting coefficients retained. If the projection
becomes singular, the plane T L0 remains meaningful; changing graph
charts, rather than declaring the exterior nonexistent, is required.
No angular mode is removed by a chart choice.

Equation (4) determines evolution from L0. It does not select L0.
As an algebraic control take K=diag(m,-m), m>0, and
V=[[0,1],[1,0]]. For every real c the line

    L_c(t)=span{(exp(-mt),i c exp(mt))}

is current-null, has graph R=i c exp(2mt), and satisfies (4).
On a finite interval all c are admissible at this algebraic level.
If the exterior is specifically the half-line t->+infinity with
ordinary L2 norm, only c=0 is square-integrable. The global norm and
end can therefore remove the local freedom once specified. This
control neither transfers that norm to the actual cusp nor excludes
the possibility that a derived global architecture supplies it.

## Eliminating modes preserves feedback only with its hypotheses

The following is an exact finite-dimensional Hessian statement,
useful for diagnosing reductions of any specified action. It does
not assert a bounded inverse for the full noncompact field operator.
Use real coordinates on the independent field components, after
any necessary constraints/gauge fixing have actually been justified.
At a stationary configuration write the quadratic form

    Q(x,y)=1/2 x^T A x+x^T B y+1/2 y^T C y,
    A=A^T, C=C^T.                                (5)

x denotes retained variations and y exterior variations. If C is
invertible, exterior stationarity gives y=-C^-1 B^T x. Direct
completion of the square yields

    Q=1/2 (y+C^-1 B^T x)^T C (y+C^-1 B^T x)
          +1/2 x^T (A-B C^-1 B^T)x.              (6)

The induced Hessian is A_eff=A-B C^-1 B^T. The second term is the
feedback through the joined exterior. It is determined by the same
Hessian; it cannot be obtained by averaging copies of A in unrelated
frames. The invertible triangular change of variables in (6) proves
that the numbers of positive, negative and zero directions of the
full Hessian equal the corresponding sums for C and A_eff. In
particular, a negative exterior mode cannot be hidden by observing
only a positive A_eff.

If C is singular, let P project orthogonally onto ker C and C^+
be its inverse on (ker C)^perp. Exterior stationarity is possible
precisely when

    P B^T x=0,
    y=-C^+ B^T x+k, k in ker C.                   (7)

Substitution gives the partially eliminated action

    Q_red(x,k)=1/2 x^T(A-B C^+ B^T)x+x^T B k.     (8)

Varying k retains the compatibility equation in (7). The remaining
equation is (A-B C^+ B^T)x+B k=0. Hence full zero modes are in
bijection with pairs (x,k) satisfying these two equations, by the
displayed reconstruction of y. Retaining only A-B C^+ B^T while
discarding k loses this equivalence and can create or remove apparent
zero modes. No pseudoinverse is a license to delete an endpoint
field, an auxiliary constraint or a gauge mode without its actual
constraint analysis.

In infinite dimension an inverse may also be unbounded or absent
because of continuous spectrum, even when the kernel is zero.
Equations (6)--(8) alone give no convergence, Fredholm statement,
quantum determinant, index or physical mass theorem in that setting.

## What a sufficient relational record must preserve

For this linearized joining duty, the retained record needs at least
the common interface identification, the allowed boundary variations,
the exterior response relation and any retained exterior kernel data.
Two descriptions producing different pi_+(q), different Cauchy trace
planes or different compatibility equations in (7) cannot be identified
merely because their isolated bulk read-outs agree.

Conversely a common change of frames, with the metrics and action
transported, does not supply new feedback. For orthogonal field-frame
maps U,W, the blocks transform as

    A'=U A U^T, B'=U B W^T, C'=W C W^T,
    A_eff'=U A_eff U^T,

and the kernel equations transform with them. In complex notation
replace transposes by daggers and retain the kinetic metric. Relative
interface transport is part of B, rather than independent changes of
the two blocks silently erased before joining.

This supplies a concrete future-interaction test for the owner's
information-loss concern. The test depends on a specified action and
exterior; it does not prove that every based word difference must be
physically observable. The theta pairing's limited quotient and the
full fermionic/exterior response can require different registers.

## The remaining derivation and verification duties

The recovered source already supplies interface matching, local
noncommuting stationary examples and response transport. The present
reduction identifies what has to come next: a justified exterior/state
and its full response on the same admitted global fields, with kernel
and continuous-spectrum issues retained. Then one can test stationary
solutions, stability, charged spectrum, interactions and anomalies.
An arbitrary response chosen for a desired index would supply the
missing ingredient rather than derive it.

The response in (4) and feedback in (6) are conditional composition
laws within the chosen theory. They do not derive E8, the field roster,
the global end ensemble, a boundary Higgs law or a three-generation
Standard Model from non-cancellation. The family control does not
establish a programme-wide impossibility of selecting an end.

This note awaits separate non-authoring review and source-complete
experimental admission. It changes no frozen verification package.
Controls for a successor include reversed-normal failure, retained
zero modes and constraint equations, singular graph-chart passage,
full-block response covariance, negative exterior Hessian directions,
and the distinction between finite intervals and actual physical ends.
