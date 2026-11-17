# The same action determines the cost of a constrained phase link

2026-11-17. PHYSICAL-C7 author hand continuation under the original
connection and path-dependence scope. Not independently checked.
No scientific script, CAS or test ran. This is the leading effective
Abelian sector of the actual four-mode kinetic term, with all earlier
full-group and normal-field qualifications retained.

The first version of FOUR_FORM_QUOTIENT_AND_CONNECTION.md said that
an independent phase link would change the kinetic theory. That was
too broad. A fixed holonomy can instead constrain the admissible
variations of the same theory. The original wording remains in Git
history. The corrected statement and response are given here.

## 1. Retain the longitudinal field before imposing its constraint

Fix a smooth coefficient path gamma(x) over 0<=x<=L, away from the
vertex. Let N(x)=||P(x)||^2+||R(x)||^2>0, and let a(x) be the pullback
of the derived mechanical connection on a chosen local path lift.
The actual source kinetic energy is the exact completion of a square

    E[gamma,b]=E_horizontal[gamma]
                         +integral_0^L N(x)(b(x)-a(x))^2 dx.        (1)

Here b=e_Q B_x. The horizontal term is the full leading quotient
energy, including its metric and charge signs. In one external
coordinate there is no F_xx gauge kinetic term. Additional external
directions and their field strengths change this reduction.

For arbitrary local variations of b, the last term is minimized by
b=a. This gives the earlier horizontal transport law. Fixed endpoint
frames alone do not require a particular integrated b. A physical
condition on that integral needs an actual endpoint/source law or a
closed-loop Wilson condition.

## 2. Solve the fixed-holonomy problem exactly

Suppose that law fixes the lifted effective phase integral

    integral_0^L b dx=beta.

In the same endpoint frames define

    Delta=beta-integral_0^L a dx,
    R_gamma=integral_0^L dx/N(x).                       (2)

The symbol R_gamma denotes this positive integral, with no additional
coefficient. For the present nonzero smooth path on a compact interval
it is finite. A simultaneous endpoint-frame change shifts beta and
the connection integral by the same amount, so Delta is invariant.
An untransformed open-path beta alone would not be a physical datum.

Writing c=b-a, Cauchy-Schwarz gives

    Delta^2=(integral c dx)^2
                  <=(integral N c^2 dx) R_gamma.

Equality occurs precisely at

    b_*(x)=a(x)+Delta/[R_gamma N(x)].                   (3)

Consequently the reduced response at fixed gamma and lifted beta is

    Gamma[gamma,beta]=E_horizontal[gamma]
                                      +Delta^2/R_gamma.             (4)

This also follows by a Lagrange multiplier in (1). The conjugate
phase momentum, in the orientation of increasing beta, is

    d Gamma/d beta=2Delta/R_gamma.

The corresponding variational current 2N(b_*-a) is constant along
the interval and has this same value. Its coefficient comes from
the existing charged-mode norm. No independent boundary stiffness
was inserted.

If only the effective U1 phase is fixed, allow its integer lifts and
minimize (4) over Delta+2pi n when the source permits those branches.
A registered lift can instead retain n. Colour-charged E8 probes
distinguish the centre data hidden by the effective U1 quotient.
Their full-group transition and branch cannot be dropped by this
Abelian minimization. The sign of the Wilson phase is set by the
chosen covariant-derivative convention; (1)-(4) use b=e_Q B_x and
the positive-charge transformation b->b+d phi.

## 3. A same-action sewing law

Split a fixed path into two intervals with connection integrals
I_1,I_2 and positive integrals R_1,R_2 of dx/N. For a fixed total
lifted beta, vary the intermediate phase allocation beta_1+beta_2=beta.
The extra energy is

    (beta_1-I_1)^2/R_1+(beta_2-I_2)^2/R_2.

Its minimum has

    (beta_1-I_1)/R_1=(beta_2-I_2)/R_2,
    extra Gamma=(beta-I_1-I_2)^2/(R_1+R_2).             (5)

The currents match at the seam, with the corresponding opposite
outward-normal signs. The source coefficient composes by adding
the two integrals of dx/N. This derives the scalar phase part of a
boundary response from a common kinetic action. It leaves the source's
choice of total phase and its physical origin explicit.

If beta is free, minimizing over it removes the extra term and
recovers the unconstrained result. If gamma is also varied, both its
horizontal energy and the two integrals in (2) vary. Replacing those
by a fitted constant would discard part of its actual equations.

## 4. Limits and the full physical earning condition

At a path approaching the vertex, R_gamma can diverge. The lower
bound in (4) can then approach zero without an attained smooth
phase response. N=0 restores the gauge symmetry and invalidates
the division in (3). Such a path must retain the unreduced fields,
the operator domain and its actual source law.

A common positive action scale rescales (1) and its response
together. It leaves the stationary connection unchanged and remains
a separate normalization duty. An endpoint law, a phase branch and
the physical path have not been derived by solving their conditional
response. The normal field equations, matter backreaction, non-Abelian
transport, full centre and complete fermionic operator remain.

The advance is an explicit current and sewing law with its coefficient
fixed by the same action once its physical path is fixed. It is not a
fundamental selection of that path or its boundary condition. No
foundational input is counted removed by this calculation.
