# R47 authored neutral-tangent argument

Inputs: R42/R44's actual smooth complete finite-volume canonical
background at fixed q0>0, q0!=1; its explicit flat end and metric
comparisons; R45's complete coefficient complex and actual parent
branching. This is an authored application, not independent acceptance
of those global topology/PDE inputs. Work in E_ad=End0(E), a Spin(10)
singlet coefficient in the supplied parent, not its gauge-adjoint 45.

## 1. A global flat tangent with the prescribed finite-norm tail

Keep the smooth base N=N_q0 and its positive metrics FIXED. On a small
interval of k around k0, the actual matrices rho_exp(k) define smooth
flat bundles on this same N: take the quotient of
universal-cover(N) times interval times C4 by the diagonal Gamma action.
The action on the base is fixed; no differentiable choice of deformed
convex domains or base metrics is needed. This is a smooth vector
bundle over N times interval, with flat connection along each slice.

Choose a connection in the interval direction and use its parallel
transport to identify the slice bundles with the one at k0. On the
deep end choose this identification in the explicitly smooth peripheral
normal frame of R44. A partition of unity extends this prescribed
interval connection to the core. Transport on a compact parameter
interval is a linear ODE at each point, so yields smooth invertible
identifications; no bound uniform over the noncompact base is required
for this existence step. Determinant-one frames keep the derivative
trace-free. The unitary central line, when present, is fixed in k.

The resulting family C(k) of global flat connections has, on the end,

    Cx=N/sqrt R, Ct=kD+beta(k)P/R, CR=J/R,
    c=dot C=(D+bP/R)dt,   b=dot beta,
    beta=6/(q-q^-1),  b=q d beta/dq.

All coordinates and norms here are those of N_q0. Differentiating
flatness gives d_C c=0 globally. Directly on the tail the mixed radial
equation is partial_R c_t+[J/R,c_t]=0; the two terms involving P cancel.
This is not a tangential-only cocycle. A different smooth extension on
the compact core changes neither the following integrability nor the
detector value. The family exists before any harmonic gauge fixing.

In the comparison norm, |c|^2=12+b^2/R^2 and the volume density is
R^(-3/2)dR dx dt. Thus above R0 its comparison squared L2 norm is

    24/sqrt(R0)+(2 b^2/5) R0^(-5/2).                    (1)

Two-sided actual metric comparisons make the true norm finite, not
equal to (1). The same bounded pointwise tail gives c in L4. Smoothness
on the compact core finishes both integrability statements. In particular
c is in the maximal d_C graph domain with d_C c=0, which R45 identifies
with the complete domain. No scalar/neutral spectral gap is assumed.
The old hyperbolic norm has |dt|^2 proportional to z^2 and volume
proportional to z^-3 dz, giving a logarithmically divergent semisimple
tail. That previous result remains true for that DIFFERENT metric.

## 2. A compact detector prevents a false gauge kill

The end matrix D commutes with N,P,J and is trace-free. Under the
invariant bilinear trace End0(E) is its algebraic dual; D is parallel
on the end in that dual system too. Choose a smooth f supported in a
finite annulus (R1,R2), with integral f(R)dR=1, and put

    eta=D f(R)dR wedge dx.

Extend eta by zero to N. It is compactly supported and d_(C,dual)-closed:
the radial derivative wedges with dR, the x derivative with dx, and
the remaining coefficient commutator vanishes. It need not be a global
parallel coefficient outside its support. The bounded linear functional
on L2 one-forms

    L(v)=integral_N tr(v wedge eta)

has a smooth compactly supported metric Riesz representative h. Its
definition uses the bilinear invariant trace; the Hilbert norm and Riesz
identification use the ACTUAL positive metrics. They are not conflated.
With orientation dR wedge dx wedge dt,

    L(c)=tr(D^2)+b/R tr(PD), integrated against f = 12.   (2)

For any compact smooth zero-form s, L(d_C s)=0 by integration by parts.
The complete graph-domain density extends this to all s in Dom(d_C^0).
Continuity in L2 then makes L vanish on the CLOSURE of exact one-forms.
Thus c is not even a limit of L2 exact directions. This is stronger
than citing a nonzero ordinary group-cohomology class without a norm.

The tempting local primitive tD is not periodic in t and is not a
global gauge parameter. A genuine periodic primitive has zero integral
of its t derivative; commutator contributions pair to zero since
[D,Ct]=0. Both distinctions are retained as explicit controls.
The number 12 is merely the chosen defining-trace detector value,
not a physical constant, dimension count or parameter prediction.

## 3. Nonzero harmonic projection without closed-range assumptions

Let Z=ker(d_C^1) in L2 and B=closure(Ran(d_C^0)). They are closed
subspaces and B is contained in Z because the connection is flat.
The orthogonal Hilbert decomposition is

    Z=B direct-sum (Z intersect ker((d_C^0)^dagger)).

The second summand is exactly the complete degree-one harmonic space:
its elements have both distributional d_C and d_C^dagger zero, hence
belong to the complete Q domain already earned in R45. Project c onto
this summand, writing c=b_exact+alpha. Equations (1)--(2) give

    L(alpha)=12,
    0<12/||h||_2 <= ||alpha||_2 <= ||c||_2 < infinity.     (3)

Here b_exact denotes a vector in the closure, not an asserted actual
primitive. This argument uses reduced cohomology and does NOT need a
Fredholm theorem, a closed-range claim at zero, or an ordinary/L2
isomorphism for the full neutral complex. It proves at least one
nonzero normalizable neutral harmonic direction for each fixed q!=1.
It does not compute the dimension, normalize its global profile or
claim that harmonic projection preserves L4.

In the supplied parent's fixed-background scalar Hessian, R46's
operator is 2 Delta. This alpha is therefore a zero direction of that
quadratic scalar block with finite positive L2 kinetic norm. The E8
trace is the already checked factor 60 times the defining SL4 trace;
the overall positive g7 normalization remains input. A kernel of this
quadratic block is not by itself a nonlinear flat direction, a gravity
modulus, a selected value of q or a stable quantum vacuum.

## 4. The q curve remains paired at the character level

New local F14, pin 46f42302, supplies an all-q symmetric matrix S(q):

    A=q/4, B=q/[2(q+1)], C=(q^2+1)/[2(q+1)],
    S=[[A,-A,B,C],[-A,A,-B,B],[B,-B,1,-1],[C,B,-1,1]].

Independently check on the literal R42 generators
M^T S=S M, N^T S=S N and
det S=-q(q^2+q+1)^3/[16(q+1)^4]. It is nonsingular for positive q.
Equivalently rho(g)^(-T)S=S rho(theta g), theta inverting both
generators. The already supplied faithful projective holonomy makes
theta descend to a group automorphism: the intertwining identity sends
each relation to the identity, faithfulness makes it a group relation,
and theta squared is the identity. Fixed scalar fourth-root characters
are inverted by theta, exactly as under dualization.

The whole q curve is therefore fixed by theta plus duality at the
CHARACTER level. Its differentiated matrix identity includes dot S;
dropping that compensating change gives the wrong infinitesimal test.
Consequently merely moving q on this curve does not supply a direction
that breaks this algebraic pairing. This is not a new sixteen-case
intertwiner census; the explicit incoming witness is credited.

F14's stronger actual-metric/whole-response equality uses its fixed
HYPERBOLIC base and F12/F13 uniqueness. It is not transferred here.
An actual canonical base isometry and compatible positive-metric map
still need their own construction or obstruction. Conversely, failure
of a particular end-coordinate formula would not be such an obstruction.
No physical CP/parity identification or universal chirality kill follows.

## 5. What remains

The result is a fixed-canonical-background neutral H1 LOWER BOUND and
finite quadratic norm, detected by the q holonomy tangent. The coupled
metric/field q-family, full neutral census, harmonic alpha's nonlinear
domain and obstruction/integrability remain to be checked. q=1 and
uniform-q limits are outside this cusp frame. The generic algebraic
pairing means an asymmetric route needs a genuinely different direction,
end/cover choice or phase, not an unsupported assertion that q broke it.
All physical parent/end selection, anomalies, chirality, scales and
gravity duties remain. R40/R41's distinct source route is preserved.
