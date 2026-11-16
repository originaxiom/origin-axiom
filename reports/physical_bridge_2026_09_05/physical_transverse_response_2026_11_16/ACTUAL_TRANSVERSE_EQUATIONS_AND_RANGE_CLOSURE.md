# Actual transverse equations and nonlinear source projections

2026-11-16. P-C3c author hand derivation, independent review pending.
No scientific producer, CAS, collection or test ran. The source is the
same supplied curved parent and complete field/domain law as P-C3b.
The old R83 frozen/relaxed residual distinction and full-complement
reconstruction are reused, without a novelty or absence claim.

## 1. Write the actual residual map

At fixed metric Omega the internal chiral configuration is X=(A,q,r),
with the parent's positive field metric

    ||delta X||_c^2=(1/G) integral kappa{
          |delta A|^2/2+Omega(|delta q|^2+|delta r|^2)} dxdy.

Use the underlying real pairing. With the common factor 1/G in its
residual norm, the full bosonic potential is ||R(X)||^2 for

    R(X)=(Omega^-1/2 Dbar_A q,
          Omega^-1/2 Dbar_A r,
          sqrt(2)[q,r],
          (F_A+Omega([q,q^dagger]+[r,r^dagger]))/(sqrt(2)Omega)). (1)

The final component is Hermitian/real. The first three are complex.
Their displayed weights reproduce the original action term by term.
At fixed Omega this is a polynomial of degree at most two in the
elementary fields and first derivatives. At a zero-residual background
X0, put L=DR_(X0) and B=one-half D^2R. For x=(a,u,v),

    Lx=(p_q/sqrt(Omega),p_r/sqrt(Omega),sqrt(2)t,
                                                    mu1/(sqrt(2)Omega)),
    B(x,x)=(-i[a,u]/sqrt(Omega),-i[a,v]/sqrt(Omega),
                          sqrt(2)[u,v],mu2/(sqrt(2)Omega)),             (2)

where p_q,p_r,t,mu1,mu2 are exactly those in the P-C3b connecting-field
proof. Both F and moment responses are included. A curvature-only
cochain obstruction is a different map.

## 2. An inverse is unnecessary for a bounded obstruction projection

Take an admitted twice differentiable field family with controlled
nonlinear products,

    X(epsilon)=X0+epsilon x+epsilon^2 beta+o(epsilon^2), Lx=0.

The remainder is in the actual graph and nonlinear residual topology.
Then

    R(X(epsilon))=epsilon^2(L beta+B(x,x))+o(epsilon^2),
    V(X(epsilon))=epsilon^4 ||L beta+B(x,x)||^2+o(epsilon^4). (3)

Use the closure L of the first-order linear residual on the weighted
compact-support core. Its formal adjoint has a dense such core, so
this operator is closable. Admitted corrections use its inherited
action on their stronger physical graph/product domain. No equality
between that nonlinear domain and the weaker residual graph closure
is needed. L can have nonclosed range. Its residual-space projection

    P_ob onto (closure Ran L)^perp = ker L^dagger          (4)

is nevertheless bounded. It gives for every admitted beta

    ||L beta+B||^2 >= ||P_ob B||^2.                      (5)

No inverse, finite-dimensional Fredholm index or absence of continuum
is assumed in (4)-(5). If the admitted regular corrections are graph
dense, the infimum of this quadratic coefficient is exactly
||P_ob B||^2. A minimizer in Dom L requires
-(I-P_ob)B in Ran L; exact cancellation requires -B in Ran L.
Membership in its closure alone is insufficient. A sequence of
unbounded correcting coefficients
also need not define a controlled nonlinear field family.

Thus a nonzero bounded dual projection rules out cancelling this
specific leading source by a second-order correction. A zero projection
does not prove an exact correction or stationary branch. The old R83
closed-range formula is recovered when that extra hypothesis holds.

## 3. The full connecting-field equation has a normal component

Let x be one external spatial coordinate, and let alpha(x) be its
compact-real gauge connection. The actual covariant velocity is

    v=partial_x X-k_X alpha.

The source kinetic metric is independent of X at fixed Omega. Gauge
transformations act by affine isometries. Variation on the complete
internal domain therefore gives the coupled equations

    -D_x v+(DR_X)^dagger R(X)=0,
    k_(X,R)^dagger v=0.                                 (6)

D_x is the corresponding gauge-covariant derivative on tangent fields.
The second equation is the real Gauss/longitudinal equation. Boundary
terms vanish under the source exhausting-cutoff and product hypotheses.
These equations retain all internal derivatives, moment and Higgs terms.

For a trial curve X_s with its Gauss response alpha_s, put
w_s=dot X_s-k_(X_s)alpha_s and alpha(x)=s'(x)alpha_s. Then

    v=s' w_s,
    D_x v=s'' w_s+s'^2 nabla_s^alpha w_s.

Let Q_N(s) project onto directions orthogonal to the closure of gauge
tangents and the actual horizontal w_s. On a smooth regular segment,
the missing normal equation is

    Q_N(s){-s'^2 nabla_s^alpha w_s
                     +(DR_(X_s))^dagger R(X_s)}=0.        (7)

The Euler equation of K(s)s'^2+V(X_s) controls the tangent component.
It does not imply (7). Normal acceleration, changing Gauss response
and all transverse potential sources are visible here. At gauge
enhancement the projection and choice of representative require the
additional regularity analysis already retained in P-C3b.

## 4. The response operator is not an endpoint mass inverse

Even before eliminating the real gauge field, the potential Hessian
at a general X has the real bilinear form

    one-half D^2V_X(Y,Z)
      =<DR_X Y,DR_X Z>+<R(X),D^2R_X(Y,Z)>.              (8)

At a vacuum the last term vanishes. At an interior trial-path point
it can have either sign. The external covariant derivatives, the
linearized real Gauss constraint and any gauge-fixing terms must also
be included in the actual normal Jacobi system.

Consequently the fixed-surface charged fermion inverse from P-C3b
cannot be substituted for this whole coupled transverse inverse.
It is useful endpoint input in its charged block. A normal solution
needs the actual source, spectrum and domain of (6)-(8). Neutral
continuum cannot be discarded. Conversely it does not invalidate
bounded dual projections such as (5).

The companion proof evaluates some of these projections using actual
normalizable physical modes. It gives a surviving nonlinear constraint
without asserting existence of a full stationary join. All other
first-order modes and possible non-smooth branches retain their own
questions. No whole-program exclusion or foundational input payment
is inferred.
