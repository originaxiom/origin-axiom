# R17: a uniform charged cusp-tail bound, including approach to source lines

2026-09-07. Path-local continuation of R14--R16, sealed at db6b5af3.
No B number, physical chirality verdict or complete TOE is asserted.

## Result and physical relevance

For the prescribed separated source potential on an exact hyperbolic
cusp, and a fixed graded tangential Hilbert-complex realization, the
charged deformed-form operator has an energy barrier growing without
bound at large height. The estimate is uniform in distance to the source
punctures. It therefore controls the joint line/cusp escape which the
finite-height normal calculation alone did not address.

The result does not choose the physical defect domain or count the
complete H1 kernel. It rules out normalized bounded-energy states whose
support escapes to arbitrarily large height in this realization, not
decaying tails of global zero modes attached to the finite-height core.
The separate neutral one-form control has Rayleigh quotient tending to
zero, so a scalar spectral gap has not been substituted for a form gap.

## Declared geometry, potential and domains

Let s=log(z), with metric ds^2+exp(-2s)(dx^2+dy^2) and orientation
dx wedge dy wedge ds. R14 supplies

```text
H=qF=V(x,y)+h(s),
V=q sum_i beta_i U(w-p_i),
h(s)=q exp(2s)(b s+c),   b=pi Q/A>0,   q real and nonzero.
```

The origin z0=1 is conventional; changing it shifts c. Neither q beta_i
nor the through-flux c is selected by this calculation.

On the punctured flat torus choose a densely defined graph-closed,
graded differential d_V=d+dV wedge with d_V^2=0. Its Hilbert adjoint is
delta_V; set D_T=d_V+delta_V and N=diag(0,1,1,2). The realization is
independent of s. Fixed minimal/maximal complexes are examples, not a
selection of the physical one. A general s-dependent defect law is not
covered by this hypothesis.

No closed-RANGE or Poincare hypothesis is assumed. Graph-closed operators
do not imply closed range or finite cohomology. These distinctions and
the adjoint-complex setup are standard; see
[Arnold--Falk--Winther, sections 3.1--3.2](https://www-users.cse.umn.edu/~arnold/papers/bulletin.pdf).
The physical reduction mechanism remains the chosen
[Pantev--Wijnholt parent](https://arxiv.org/pdf/0905.1968), not a newly
derived physical identification of the object.

## Derivation: the degree shift and cross block matter

Write a form as alpha+ds wedge beta. In each tangential degree j,
multiply the new coefficient by exp((1-j)s) to get the physical coordinate
coefficient. The metric Hodge computation verifies all eight L2 weights:
the transformed measure is ds dx dy in every component.

For d_H=d+dH wedge and delta_H=delta+i_grad(H), the transformed
D0=d_H+delta_H is exactly

```text
D0 = [ exp(s) D_T           -partial_s+h'+1-N ]
     [ partial_s+h'+1-N    -exp(s) D_T       ].
```

Independent composition of the differential operators, differentiating
their coefficients, gives the square

```text
diag(-partial_s^2+exp(2s)D_T^2+(h'+1-N)^2-h'',
     -partial_s^2+exp(2s)D_T^2+(h'+1-N)^2+h'')
  + [ 0                    2 exp(s) d_V ]
    [ 2 exp(s) delta_V     0            ].
```

N does not commute with d_V. Removing the degree shift or the off-diagonal
block fails the exact controls and the independent integrated-energy test.

Put S=[0,d_V;delta_V,0]. On the common square-domain core,

```text
diag(D_T^2,D_T^2)-S^2 = diag(delta_V d_V,d_V delta_V) >= 0.
```

Consequently the absolute mixed contribution is at most
epsilon ||exp(s)D_T psi||^2 + epsilon^(-1)||psi||^2. Taking epsilon=1/2,
and minimizing the degree shifts, proves the INTEGRATED estimate

```text
||D0 psi||^2 >= ||partial_s psi||^2 + (1/2)||exp(s)D_T psi||^2
  + integral [max(|h'|-1,0)^2 - |h''| - 2] |psi|^2.
```

This absorbs the possibly unbounded tangential part, rather than assuming
the singular Hessian is small. Prove the identity first on finite sums
of smooth compactly supported s-profiles with tangential square-domain
vectors. Degree-preserving spectral regularization of D_T^2 commutes
with d_V, delta_V and N and approximates the chosen joint core. The
inequality extends to its graph closure by the norm estimate and lower
semicontinuity. Applying it to any other realization requires proving
the corresponding core and adjoint statements; no global-domain theorem
is smuggled into that extension.

## An explicit conservative sufficient height

Set K(s)=b(2s+1)+2c and t=|h'|=|q|exp(2s)K(s) on the following tail:

```text
S0=max(0, 1/2-c/b, (1/2)log(4/(|q|b))).
```

For s>=S0, K>=2b, t>=8 and |h''|=t(2+2b/K)<=3t. Both K and t
increase there. With t=u+8 and u>=0,

```text
(t-1)^2-3t-2-t^2/4 = 3u^2/4+7u+7 >= 0.
```

Thus every high-tail-supported vector in the declared graph closure obeys

```text
||D0 psi||^2 >= integral |h'(s)|^2/4 |psi|^2.
```

This works for either sign of q and any real c. S0 is a sufficient bound,
not a sharp onset or an evaluated m202 physical scale. No exclusion
radius about a source puncture appears, so simultaneous approach to a
line and to infinite height is controlled within the domain hypothesis.

## R15's smooth harmonic correction does not destroy the tail barrier

Adding qv to H adds C_v=q(dv wedge+i_grad(v)). The Clifford calculation
gives C_v^2=q^2|dv|^2 I. If |q dv|<=K_v on a tail, then

```text
||D psi||^2 >= (1/2)||D0 psi||^2-K_v^2||psi||^2
             >= integral (|h'|^2/8-K_v^2)|psi|^2.
```

R15's correction is smooth across the source locations. Above its compact
forcing it has a constant zero mode and decaying modes z K1(kz).
Direct differentiation verifies (z K1(kz))'=-kz K0(kz) and the radial
harmonic equation f''-f'/z-k^2 f=0. The orthonormal gradient of each
unit-amplitude mode is bounded by k z^2 sqrt(K0(kz)^2+K1(kz)^2).
The large-argument Bessel asymptotic is polynomial times exp(-kz).
For a smooth full-torus trace, the Fourier series and differentiated
series are uniformly controlled on a higher slice; the nonconstant
gradient then decays uniformly. The zero mode has zero derivative.
See [DLMF derivatives](https://dlmf.nist.gov/10.29) and
[large-argument asymptotics](https://dlmf.nist.gov/10.40).
No numerical m202 value of K_v or corrected onset height is computed.

## Neutral control and verification receipts

For q=0 on a flat unpunctured torus, a harmonic tangential one-form has
N=1, D_T=0 and no radial degree shift. A sin^2 profile of support length
L has norm 3L/8 and derivative energy pi^2/(2L), hence Rayleigh quotient
4pi^2/(3L^2), tending to zero. Smoothing the endpoints preserves the limit.
The scalar control instead has quotient 1+4pi^2/(3L^2). This matches the
degree-dependent cusp thresholds in
[Golenia--Moroianu, section 5](https://arxiv.org/pdf/0705.3559); it is not
a statement about every punctured neutral realization.

The pre-execution [design](CUSP_TAIL_DESIGN.md), source and nine tests
were committed at db6b5af3 before their first executions. Science
succeeded in 3.887 seconds; [full JSON](cusp_tail_first_run.json) retains
all matrices and controls. Actual R14 radial data give 72 checks over
both charge signs, equal/unequal source densities and c=-20,0,20.
Twelve mixed-degree finite-complex integral controls have maximum
direct/squared relative error 3.10e-16 and quadrature change 1.12e-14.
The smallest lower-bound margin is 701.68; omitting the cross term
produces a nonzero relative error up to 0.00026195. These finite complexes
check the proof's algebra, not a discretized m202 spectrum.

[Focused tests](CUSP_TAIL_CHECKS.txt): 9 passed in 4.72 seconds.
[Quiescent broader regression](CUSP_TAIL_REGRESSION.txt): 212 passed,
7 failed, 8 errors and one optional-GUI warning in 227.51 seconds.
The failures are the preserved original R16 four, G2 export one and R7
finite-difference two; R11's original fixture causes the eight errors.
Their separate controls remain passing; original tests were not changed.
This regression is not the full repository suite or an independent
banking review. See [failure record](FAILURES.md).

[Reporting gates](CUSP_TAIL_GATES.txt): 27 passed / 3 failed, retaining
the already recorded attribution, static-vacuity and provenance debt.
The new sealed design/source hashes are intact; no compliance exemption
or retrospective seal edit is used.

## The next earned join

The high-cusp escape estimate is now supplied for a stated fixed-domain
class. The remaining analytic duties are compactness at finite-height
line singularities, a complete closed-range/Fredholm argument, and an
actual comparison of BOTH charged H1 spaces with the regulated topology.
Weighted de Rham homotopies are a candidate tool, not a proved comparison
here. Unbounded exponential conjugation still cannot substitute for it.

The physical duties remain: derive the gauge/fibre and defect law,
retain the actual amplitudes, identify the Lorentz/gauge quantum numbers,
then test the possible extra vector-like pair's mass and anomalies in
the same action. Neither this estimate nor the separate certified
partial filling automatically performs those identifications.
