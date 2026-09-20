# R37 authored argument and limits of its controls

The [working note](SOURCE_SCALAR_WORKING_2026_09_20.md) supplies the
complete candidate action, mode formulas and interface identity. It
is frozen analytic prior. This supplement states why they follow and
which statements the finite symbolic tests cannot certify independently.

## Coupled variation and scalar domain

Write S=(x+i y)/sqrt(2) componentwise and Q=(X+iY)/sqrt(2).
Let N=S* dot S and n=Q*Q. Differentiation of

    C D^2 + sigma [r N + lambda_S N^2
                  - eta(Q* S dot S + Q S* dot S*)],
    D=div h-kappa sigma(4n+2N),

with respect to S* gives sigma times

    (r+2 lambda_S N-4 C kappa D)S-2 eta Q S*.

The Q* derivative of the new locking term is -sigma eta S dot S;
the full moment-map derivative is -8 C kappa sigma D Q. The h
variation is 2C integral[D div(delta h)+<dh,d(delta h)>]. Its source
includes N. For D_i=d_i+i q A_i, the derivative of |D_i S|^2 with
respect to A_i is 2 q Im(S* dot D_i S). The sign differs from R29's
connection coordinate because A_here=-A_R29, not because charge changed.
For an anti-Hermitian D5 generator T the analogous current is
2 sigma Re((D_i S)* dot T S). All new currents vanish at S=0.

Integration by parts of the weighted derivative term gives
-sigma^-1 D_i(sigma D^i S) and flux sigma D_n S. With free tube
boundary variation the natural condition is sigma D_n S=0. The
weighted Neumann quadratic form is nonnegative. On a connected compact
tube with positive bounded weight bounded away from zero, its zero
space consists of parallel constants when the connection is flat and
trivializable. Thus s0=W^-1/2 with W=integral sigma, not inverse square
root of unweighted volume. This is an analytic form-domain argument,
not an eigenvalue computation on a mesh.

At Q=f real, D=0 and S=0 the twenty real Hessian entries are
r-2 eta f (ten) and r+2 eta f (ten), after dividing by the positive
kinetic weight. First variations in all old/new fields vanish at the
R29 stationary point. No mixed S/old-field quadratic term remains
there. Hence this S block is positive when r>2 eta f. This does NOT
prove positivity of every other sector, a global minimum of the new
potential or quantum stability. At equality a scalar is light; below
it the stationary point is unstable in this block, not chirally gapped.

Substituting S=S4/sqrt(W), Q=Q4/sqrt(W) in the same action yields
unit kinetic coefficient, quartic lambda_S/W, locking eta/sqrt(W).
At Q4=sqrt(W) f it reproduces the displayed masses. Gauge symmetry
does not force the Yukawa density to equal this kinetic weight.

## Interface identity

For exact positive modes H0 u_i=lambda_i u_i and
v_i=d_q u_i/sqrt(lambda_i), set w=u_i u_j and b=sigma conjugate(s0).
Apply the R36 off-shell product identity on U and integrate twice.
The volume coefficient is (Delta b)/2-q<dF,Db>; the boundary term is

    b [(D_n w)/2+q F_n w] - w D_n b/2.

This gives the working note's formula with E=(lambda_i+lambda_j)/2.
Covariant derivatives have opposite charges on b and w. The symbolic
test retains arbitrary connection, F, sigma and volume density J in
one coordinate; tensorial divergence and Green's formula give the
stated manifold identity. That analytic extension is not certified by
testing one coordinate alone. Piecewise constant sigma is treated on
U with its boundary flux, not differentiated as a smooth zero extension.
Fermions transmit through this interface; outer Robin data do not
set its flux to zero. Sharp-corner flat controls use the Lipschitz
divergence theorem; no smoothness of their corners is asserted.

## Whole eigenspace control, not one favorable mode

On T2_(2pi) times [0,1] with trivial transport and F=0, Fourier/Neumann
eigenvalues are n_x^2+n_y^2+(k pi)^2. Eigenvalue two has k=0 and
|n_x|=|n_y|=1, giving exactly the four real basis functions in the
working note. Axial positive eigenvalues start above two. This is a
complete EIGENSPACE, not a complete low-energy spectrum: zero and
eigenvalue-one modes exist and are not divided by sqrt(lambda).

Every product integral factorizes into elementary one-dimensional
integrals, including off-diagonal products. With a=average cos^2,
b=average sin^2 on (-epsilon,epsilon), c=pi^-2, direct integration
gives M=c diag(a^2,ab,ab,b^2) and
P=c diag(ab,(a^2+b^2)/2,(a^2+b^2)/2,ab).
For 0<epsilon<pi/2, a>b>0, a+b=1. Consequently their operator norms
are c a^2 and c(a^2+b^2)/2. Their ratio tends to two, although the
first-entry ratio a/b diverges as 3/epsilon^2. The limiting ranks are
one and two. Neighbors, not a basis choice, carry unsuppressed P.

For u'=u U and v'=v U with U unitary, M'=U*^t M U* and
P'=U^t P U. These unitary congruences preserve singular values; the
tests use a complex mixing matrix rather than only rephasing. An entry
ratio is not invariant under this freedom, whereas the full norms are.
The explicit six-face calculation supplies flux=2(P-M), including
zero axial caps. Removing sigma from only the Yukawa density multiplies
both matrices by 4 epsilon^2, sending both to zero with the same scalar
kinetic normalization. This is a different action, not a convention.

These limits concern exact finite-width coefficients of a specified
flat comparator. They prove neither hyperbolic mirror selectivity nor
its impossibility, and construct no zero-width interacting theory.
UV, trace-domain, complete-end, anomaly and phase duties survive.
