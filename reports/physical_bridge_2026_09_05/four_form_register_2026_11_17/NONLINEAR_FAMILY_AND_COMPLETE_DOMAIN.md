# Extending the four-form construction to stationary source fields

2026-11-17. PHYSICAL-C7 author hand derivation, pending independent
review. This continuation assumes P-C3e's complete-cusp Banach inverse
lemma and its analytic moment map in the stated weighted spaces.
Those analytic results retain independent review. No scientific
producer, CAS or test ran here.

## 1. Use all directions in the existing pure-form family

Let H_+(u) and H_-(v) be the actual harmonic form sections for u,v in
C^2, in the canonically normalized bases of P-C3e. At the coherent
background X_0=(A_0,q_0,r_0), the four form modes obey

    [H_+(u)+H_-(v),q_0]=[H_+(u)+H_-(v),r_0]=0,
    Re k_0^dagger(H_+(u)+H_-(v),0,0)=0.               (1)

They have bounded physical profiles and the original strict cusp
decay. A finite linear combination retains all the source estimates
uniformly on a bounded coefficient set.

For ||u||=||v||=1 introduce one relative real scale lambda and set

    X_raw(t,lambda,u,v)
       =(A_0+t[exp(lambda)H_+(u)+exp(-lambda)H_-(v)],
                                                          q_0,r_0). (2)

This is exactly F-flat, by the same literal holomorphic equations
used in P-C3e. The constant complex Q transformation changes lambda
and leaves the invariant matrix

    Z=t^2 u v^t                                      (3)

unchanged. The symbol lambda here denotes a relative scale, with no
relation to the light cubic coefficients lambda_+,lambda_-.

## 2. The two implicit-function steps hold uniformly in direction

Keep P-C3e's gauge spaces X_delta and Y_delta,0, its global Q kernel
convention, compact bump and residual projection Pi. The fixed linear
inverse off Q is the same at t=0 for every u,v,lambda. The map

    Pi m(t,lambda,u,v,psi)

is real analytic with derivative -P_v in psi at t=0,psi=0. Its first
t derivative vanishes because the four modes are physical zero modes.
The implicit-function theorem gives

    psi(t,lambda,u,v)=O(t^2), Pi m=0.                 (4)

The constants and fixed-order direction derivatives can be chosen
uniformly for ||u||=||v||=1 and lambda in a sufficiently small compact
interval. There are finitely many profile coordinates, the inverse
is fixed, and S^3 x S^3 is compact. A finite cover of direction charts
therefore gives one common sufficiently small amplitude range.

Let h be the remaining Q moment. The exact normalized current gives

    h(t,lambda,u,v)/t^2
          =e_Q[exp(2lambda)-exp(-2lambda)]+O(t).       (5)

The quotient by t^2 is removable analytically. Its lambda derivative
at t=0,lambda=0 is 4e_Q, which is nonzero. A second implicit-function
theorem gives a unique small

    lambda(t,u,v)=O(t).                               (6)

Combining (2),(4),(6) gives an actual source field family

    X(t,u,v)=exp[-psi(t,lambda(t,u,v),u,v)]
                                  .X_raw(t,lambda(t,u,v),u,v),
    F(X)=mu(X)=0.                                    (7)

The dot means the original holomorphic complex gauge action, with
the unitary connection reconstructed as in P-C3e. It changes the
physical field while preserving F-flatness. The original complete
variation law, spin structure, core character and end frame are retained.
All static members are stationary in the supplied parent, since all
its residuals vanish. Its colour-preserving E6 consistency proof then
retains the full E8 bosonic variations outside that sector.

## 3. Equivariance and what the parameter quotient identifies

The projection Pi, its bump times Q and its kernel convention commute
with the constant unitary Q action. Uniqueness in (4)-(6) therefore
implies equivariance of (7) under

    (u,v)->(exp(i phi)u,exp(-i phi)v).                 (8)

The family descends from its parameter space by that effective circle
action to a stationary family labelled by the smooth part of the
rank-one matrix cone (3). This is a map into physical gauge classes.
Claiming a classification of the entire local vacuum space would
require a full gauge-slice and deformation-complex theorem, including
other neutral fields and possible branches. None is supplied by (7).

At nonzero small t the differential is injective on the six real
parameter directions modulo (8), locally within this family. The
harmonic projection of its leading variation is the original four-mode
variation modulo its radial balance and one phase. Its quotient metric
is positive away from that phase. Uniform small corrections preserve
this local immersion on compact direction patches. Additional discrete
identifications that change a marked state or spin/core frame must be
transported explicitly before any further quotient.

If a physical source regards a constant phase as an observable reference,
its own fields and charge are part of the relational state. The gauge
quotient above uses the redundancy of the specified parent, with all
sources transformed covariantly. It cannot erase a fixed external
measuring datum for free.

## 4. The real Gauss connection extends the leading coefficient formula

On the family (7), use the full real source tangent k_X and both original
physical metrics. For a parameter variation Y=dX, solve

    Re(k_X^dagger k_X) alpha=Re(k_X^dagger Y).          (9)

Work in the E6 gauge directions. The colour stabilizer annihilates
the fields and is kept in the full parent. At the origin the only
E6 gauge kernel is Q, and its complement has the old isolated positive
gap. The coefficients in (7) perturb that elliptic quadratic form
continuously, with the same complete cusp asymptote. The off-Q inverse
thus remains bounded for small amplitude. This uses the vector gauge
operator. It assumes no gap for the fermion continuum.

Choose the effective circle generator so it acts as (iP,-iR).
Its tangent has norm squared 2t^2+O(t^3). Pairing that tangent with
the old off-Q image has no linear term, by (1). The off-diagonal
block in (9) is therefore O(t^2), and its Schur contribution to the
circle block is O(t^4). The circle Schur block is

    2t^2+O(t^3)>0                                    (10)

for small t>0. All effective E6 gauge directions in (9) are then
invertible. The inverse is not uniform as t tends to zero, where
the Q symmetry is restored.

For direction variations at fixed t, Y=t d[H_+(u)+H_-(v)]+O(t^2).
Their leading off-Q source vanishes by (1). The effective circle
part of the full connection on a fixed-t link consequently obeys

    A_t=(a_u-a_v)/2+O(t).                             (11)

It transforms by A_t -> A_t+d phi exactly. The induced direction
metric is the metric of the preceding note plus higher-order source
corrections. Those corrections are determined by (7)-(9), rather than
new independent kinetic weights.

The difference A_t-A_0 is basic on the circle bundle over Y. Its
curvature difference is exact on Y. Therefore on the primitive sphere
of the preceding note

    (1/(2pi)) integral_(S^2) dA_t=1                   (12)

whenever the family and gauge inverse above are admitted. The primitive
period survives the nonlinear correction. Pointwise holonomies and
the full nonlinear metric can change. Full E8 descent carries the
additional centre qualification in the third note.

## 5. Retain the complete fermion realization on this family

The original first-order four-slot fermion map has fixed geometry,
fixed kinetic weights and the same bundle transitions. For (7), the
connection difference divided by Omega and the spin differences divided
by sqrt(Omega) are bounded, uniformly for small parameters. On the
cusp, the constant Q asymptote in psi commutes with the limiting
background. Its other coefficients and physical derivatives decay.
Thus the difference of the full first-order fermion operators has
bounded zeroth-order coefficients

    D_X=D_0+V_X, ||V_X||=O(t).                        (13)

The same statement holds for the adjoint and for the Hermitian doubled
operator on all retained source slots. If D_0 has its stated complete
closed graph domain, then D_X has that same domain. If the original
Hermitian doubling is selfadjoint, its bounded Hermitian perturbation
is selfadjoint on that domain. This is the usual bounded-perturbation
argument applied to the actual source profiles and metric.

Under a unitary gauge transition, the full field, operator, adjoint,
norm and domain travel together. Equation (13) does not isolate a
finite physical family from a continuum at zero. A finite spectral
projection and a light-mode transport law need the actual complementary
resolvent or an appropriate Fredholm statement in that sector. The
unbroken colour and other massless modes remain in the comparison.

The fermionic transport cannot be replaced by a scalar phase from
(11) while discarding its colour centre or the other field response.
The complete E8 lift, kernel multiplicity, chirality and anomaly
calculation retain their own mathematical and physical duties.

## 6. Exact scope of the reduction

The chosen parent, metric, spin/core data, harmonic basis and amplitude
directions enter as the earlier premises. Under those premises the
moment response, relative balance and Gauss connection are outputs.
Equations (7),(9),(12),(13) connect a whole permitted family to the
same action and its operator domains. They do not select its state,
its history weighting or its embedding into the foundational register.

The quartic-free stationary family and its kinetic geometry supply
one constructive setting for the joining-law question. A spacetime-
dependent path through it still needs its normal equations and source
law. Static stationarity of every point does not prove that a moving
or spatially varying interpolation is a full field solution.
