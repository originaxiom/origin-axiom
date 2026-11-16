# Forced cusp response and its actual core-matching data

2026-11-16. P-C3d author hand derivation. Independent review pending.
No scientific code, CAS, collection or tests ran. This reuses the actual
free centralizer-spin radial block and the source's complete-domain
and transmission laws. Elementary half-line solution formulae carry
no novelty claim. All coefficients below are in the inherited unitary
canonical frame with radial measure dt and curvature radius ell.

## 1. Keep the physical zero-threshold operators

The source doubled Dirac block is unitarily a finite sum of

    D0=-(i/ell) J partial_t, J=J^dagger, J^2=I, t>=T.    (1)

One two-component copy uses J=sigma1. The actual squared-spin operator
and the bosonic spin Hessian at the zero-residual background are

    P0=-(1/ell^2) partial_t^2.                           (2)

Equation (2) uses the same-action scalar/fermion square, not an added
bosonic end law. Translated slow profiles still show zero essential
spectrum. No bounded inverse on the entire physical L2 source space
is claimed.

For delta>0 define a class of sources by

    ||f||_delta=||exp(delta(t-T)) f||_L2(dt)<infinity.

This is an estimate on a specified source. It changes neither the
physical norm nor the original operator domain.

## 2. Exact forced Dirac response at zero

For D0 psi=f in that source class, the unique L2 tail solution is

    psi_f(t)=-i ell J integral_t^infinity f(s) ds.        (3)

Its derivative is i ell J f, so direct substitution in (1) gives f.
Any difference of two solutions is constant and fails L2 unless zero.
The decaying integral has its original H1 graph domain. A weighted
Young inequality for the future Volterra integral gives

    ||psi_f||_delta <= (ell/delta)||f||_delta,
    ||partial_t psi_f||_delta=ell||f||_delta,
    |psi_f(T)| <= ell/sqrt(2delta) ||f||_delta.            (4)

The complete core trace must equal (3) at T in this same unitary
frame. In the old chart Gamma0=a, Gamma1=i b, with J=sigma1,
the forced trace is

    a=-i ell integral f_b, b=-i ell integral f_a.

There is no independent homogeneous L2 boundary vector to add at zero.
This is an affine source-dependent trace relation, not a replacement
constant Weyl function in a real spectral gap.

## 3. Exact forced squared-spin response at zero

For P0 u=f the unique L2 solution in the stated class is

    u_f(t)=-ell^2 integral_t^infinity (s-t) f(s) ds,
    u_f'(t)=ell^2 integral_t^infinity f(s) ds.            (5)

Differentiating twice gives -ell^-2 u_f''=f. Homogeneous solutions
are a+b(t-T), and neither nonzero combination belongs to L2.
The estimates from two Volterra integrations are

    ||u_f||_delta <= ell^2/delta^2 ||f||_delta,
    ||u_f'||_delta <= ell^2/delta ||f||_delta,
    ||u_f''||_delta=ell^2 ||f||_delta.                    (6)

Put M0=integral_T^infinity f(s)ds and
M1=integral_T^infinity(s-T)f(s)ds. The outward momentum of the
tail at its lower cut, in the actual quadratic form, is

    u_f(T)=-ell^2 M1, pi_tail=-ell^-2 u_f'(T)=-M0.       (7)

The real boundary work is 2 Re<pi_tail,delta u>. The core outward
momentum points in the opposite direction. Same-action transmission
therefore requires, on this angular block,

    gamma u_core=-ell^2 M1, pi_core=M0.                  (8)

Both value and momentum are fixed by the end source. They must agree
with the solution of the actual compact-core problem, including its
mixing with all other angular blocks and its gauge constraints. They
are not two separately adjustable boundary conditions.

For reference the trace estimates are

    |M0| <= ||f||_delta/sqrt(2delta),
    |M1| <= ||f||_delta/(2delta^(3/2)).

## 4. The same action gives a momentum-dependent boundary functional

At Euclidean external momentum magnitude k>0 the quadratic equation
is (P0+k^2)u=f. Put m=ell k and prescribe the actual cut value a.
Its unique L2 solution is

    u(t)=a exp[-m(t-T)]+integral_T^infinity G_m(t,s)f(s)ds,

    G_m(t,s)=ell^2/(2m){exp[-m|t-s|]
                                  -exp[-m(t+s-2T)]}.    (9)

Direct differentiation at the cut gives the exact response

    pi_tail(k)=(k/ell)a
                     -integral_T^infinity exp[-m(s-T)]f(s)ds.         (10)

For the canonical complex-field functional

    S_tail=integral {ell^-2|u'|^2+k^2|u|^2-2 Re<f,u>}dt,

the on-shell a-dependent terms are

    S_tail^os(a;k)=(k/ell)|a|^2
                -2 Re<a,integral exp[-m(s-T)]f(s)ds>+C(f;k).        (11)

C is fixed by the Dirichlet Green response. Equations (10)-(11)
derive the quadratic boundary work from the same action. Its homogeneous
kernel is proportional to |p|/ell in Euclidean momentum, rather than
a chosen constant stiffness or local mass. Lorentzian response requires
its actual state/causal prescription and is not selected here.

For f=0 the norm is |a|^2/(2ell k), diverging as k approaches zero
when a is fixed nonzero. The limiting zero coefficient in (10) cannot
be used to admit a nonzero constant tail at k=0. For a weighted source,
G_m tends to ell^2 min(t-T,s-T). The resulting zero-energy field tends
to a+ell^2 M1 at infinity. L2 therefore requires a=-ell^2 M1, recovering
exactly (5)-(8). The derivative then gives -M0. The source-free and
source-dependent limits agree with the original complete domain.

## 5. Scope of the source estimates

Unweighted L2 alone is insufficient. For example f=(1+t-T)^-1 is
L2, but a Dirac primitive grows logarithmically and has no L2 solution.
For f=(1+t-T)^-p, the Dirac integral is L2 precisely when p>3/2,
and the double integral is L2 precisely when p>5/2. The exponential
class above is sufficient, not a necessary new physical restriction.

The actual compact-frame charged spin profiles have canonical cusp
decay of the form exp[-pi exp(t)] times fixed polynomial factors.
The neutral compact connection profile and the allowed charged form
profiles also decay faster than any exp(-delta t). Finite products
and fixed-order derivatives of these explicit modes, with the source's
polynomial cusp coefficients, generate sources in every class used
above. General nonlinear reconstructed fields need their own decay
proof. Their response is not certified by this observation alone.

Graph admission and nonlinear boundedness are separate checks. In this
spin block the physical orthonormal profile has an extra factor
proportional to exp(t/2) relative to the canonical dt coefficient.
Choosing delta>1/2 and using the weighted H1 estimate makes that
profile bounded and decaying by the one-dimensional Sobolev estimate.
The displayed explicit charged sources permit every such delta.
This proves a useful sufficient nonlinear tail class; it does not
assert boundedness for every unweighted L2 graph-domain field.

The companion source calculation identifies when this neutral spin
forcing is actually zero. If different permitted fields source it,
(3)-(11) give their tail response and compatibility test without
erasing the continuum. A full stationary construction must still
solve the core, normal and real Gauss equations with that very source.
No source is supplied externally or fitted here.

Independent review must check the physical radial/canonical reduction,
all ell and orientation factors, the graph domain, weighted estimates,
momentum Green kernel, matching conventions and the difference between
a source-specific solution and a whole-parent inverse.
