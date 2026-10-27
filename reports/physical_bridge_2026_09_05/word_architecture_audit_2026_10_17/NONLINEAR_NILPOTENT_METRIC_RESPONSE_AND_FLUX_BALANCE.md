# Nonlinear nilpotent metric response: the Higgs norm is not constant along the extension family

October 27, 2026. UNREVIEWED author hand derivation. No scientific
producer/import/CAS/test execution. This continues the SAME specified
ordinary compact rank-two Hitchin model. It is not a nonlinear physical
surface solution, an SM vacuum or a foundational reduction of that parent.

## 1. Use the actual orthogonal splitting, not a frozen root metric

Retain the fixed smooth genus-three Q8 cover, nonzero zero-free nilpotent
pair and extension coordinate e from the preceding compact proofs.
The existence theorem gives a harmonic metric for each fixed stable
holomorphic pair. In its smooth orthogonal splitting along the intrinsic
holomorphic kernel L, write the line metric on L as sqrt(n), so the
root L^2=K^-1 has metric n>0. The orthogonal quotient has the reciprocal
metric because det E is fixed. This smooth splitting need not be a
holomorphic split extension.

In local holomorphic line frames for L and the quotient L^-1, and their
orthogonal smooth lift, the matrices are

  A_barz=[[0,b],[0,0]],
  A_z=[[partial_z log(n)/2,0],[-n conjugate(b),-partial_z log(n)/2]],
  Phi=[[0,1],[0,0]] dz,
  Phi^dagger=[[0,0],[n,0]] dbar z.                        (1)

Here b dbar z is the ACTUAL second fundamental extension form. The
ordinary lower matrix in (1) is -E_- in our earlier compact-root
convention; the curvature/Higgs sign has not been changed. The line
frames, their transitions and the fixed map L^2 K=O travel with (1).

Direct multiplication gives the upper diagonal curvature coefficient

  (F_zbarz)_11=-(1/2) partial_z partial_barz log(n)+n|b|^2,

and upper off-diagonal coefficient partial_z b+(partial_z log n)b.
The commutator [Phi,Phi^dagger] has coefficient n diag(1,-1).
Thus the FULL compact equations reduce to

  partial_z(n b)=0,
  partial_z partial_barz log n=2n+2n|b|^2.                 (2)

Holomorphy of Phi holds since A_barz and Phi have the same upper
nilpotent direction. The remaining off-diagonal curvature equation is
the conjugate of the first equation in (2). No component has been
omitted; the determinant trace is fixed to zero.

Assume the harmonic representative retains the canonical combined Q8
action. Its invariant harmonic extension space is dual to the single
invariant quadratic q0. For the fixed Serre-coordinate e, (2) then gives

  N_n=integral_Y |q0|^2/n d^2z,
  b=e conjugate(q0)/(n N_n),
  partial_z partial_barz log n
       =2n+2|e|^2 |q0|^2/(n N_n^2).                     (3)

This is a scalar NONLOCAL equation through N_n, not a freely prescribed
metric or an assertion that the earlier tangent beta0 remains the exact
finite-amplitude form. In an equivariant unitary representative the
harmonic-Serre pairing fixes the normalization in (3).

## 2. Exact integrated balance, including the second fundamental term

Let h be the split uniformizing root metric. It solves
partial partialbar log h=2h and has area
A_h=integral_Y h d^2z=pi(g-1)=2pi for curvature -4.
Since u=log(n/h) is a globally defined smooth function, integration of
its exact Laplacian on the closed curve gives

  integral_Y n d^2z + |e|^2/N_n = A_h.                    (4)

The second term is the norm squared of the extension form in the
line-metric convention of the preceding tangent note. It is NOT an
extra tunable constant. The old split flux/Higgs-size identity is
recovered when e=0. Away from that point the induced line connection's
curvature and the diagonal block of the full connection differ by the
second fundamental term n|b|^2. Dropping it would incorrectly keep the
Higgs norm fixed throughout the nonsplit family.

Equation (4) gives

  0<integral_Y n<A_h for e!=0,
  N_n>|e|^2/A_h for e!=0.                                (5)

It does not bound e itself. A growth of the harmonic metric's dual norm
N_n can compensate a large extension coordinate. Finite norm at each
fixed compact fibre is not the full modular-end norm.

There is also a pointwise control. With Delta_h=4 h^-1 partial partialbar,
(3) gives

  Delta_h u=8(exp(u)-1)
             +8|e|^2 |q0|^2/(h^2 exp(u) N_n^2).          (6)

A positive maximum of u contradicts (6), so n<=h. The strong maximum
principle gives n<h everywhere for e!=0: rewrite exp(u)-1=c(u)u with
c(u)>0, and the nonzero nonnegative source prevents u identically zero.
These statements compare line metrics within THIS fixed curve/model.
They are not physical warp-factor bounds or comparisons across the weave.

## 3. The first nonlinear response is fixed by a positive scalar inverse

Near the split pair, smooth local dependence of the stable compact
harmonic solution and the equations give

  u=|e|^2 u2+O(|e|^4),
  (Delta_h-8)u2=8 |q0|^2/(h^2 N_h^2),
  u2=-8(-Delta_h+8)^-1[|q0|^2/(h^2 N_h^2)].              (7)

The phase independence follows from the unitary root rotation combined
with the constant Higgs-phase symmetry of the fibre equations. There
is no linear source for u, and -Delta_h+8 is strictly positive on this
closed compact curve. Thus no freely added homogeneous scalar response
is admitted. Its positive Green operator gives u2<0.
Integration yields the independent check

  integral_Y h u2 d^2z=-1/N_h,
  integral_Y n d^2z=A_h-|e|^2/N_h+O(|e|^4),               (8)

in agreement with (4). The number 8 belongs to the stated auxiliary
curvature/normalization convention; it is not a predicted 4D mass.
The equations derive the second-order fibre metric response instead of
supplying a scalar profile. They do not execute or certify a solver.

## 4. Kinetic and selection consequences with the right inequality direction

At a general finite e, the root-harmonic form dual to q0 has raw norm
1/N_n. In the holomorphic deformation problem, varying the extension
class by this form while keeping Phi fixed is a closed tangent: its
upper direction commutes with Phi. The FULL gauge adjoint now includes
the background lower connection in (1), so its gauge response generally
does not vanish. The orthogonal quotient projection from the preceding
note can only lower the raw norm. Hence, for the same compact kinetic
normalization C_A,

  0<G_(e bar e)(e,Y)<=C_A/N_n<C_A A_h/|e|^2  (e!=0).     (9)

The strict positive left side is for a nonzero tangent of inequivalent
stable pairs; the other inequality is an UPPER bound, not coercivity.
It cannot be used to prove that a pole has infinite energy. Neither
finite nor infinite full-end energy follows without the nonlinear
metric's controlled asymptotics and the actual surface weights.
At e=0 it recovers the earlier exact coefficient C_A/N_h.

There is a useful test of a proposed selector. If one ADDS an independent
positive multiple m^2 of the background Higgs norm, then along this
D-flat nilpotent family (8) makes its quadratic change

  delta V=-m^2 |e|^2/N_h+O(|e|^4)

up to the retained common trace factor. Such an added term destabilizes
the split point in this direction; it does not select it by a positive
quadratic minimum. This is a conditional control for that added
potential, not a claim that the source supplies it. The residual-square
Hitchin action remains zero on the exact family. One must derive the
actual same-parent potential/end contribution before using it to select
a state. Other fields, real conditions and boundary terms remain live.

## 5. Ledger, reuse and verification status

Before: fixed compact nilpotent family, an explicit tangent norm, but
an uncomputed nonlinear root-metric response. After: the complete
orthogonal-splitting equations (2)-(3), integrated balance (4), pointwise
metric bound (6), unique second-order response (7) and correctly directed
kinetic upper bound (9). These are conditional analytical reductions of
profile freedom within the supplied model, not new foundational inputs
paid or SM parameters derived.

The source is the already-read ordinary compact Hitchin equations and
the preceding stable-family/tangent proofs. Their existence theorem is
reused; its uniqueness is not extrapolated to a vacuum selector. The
source physical surface still has K_X, its own horizontal components,
metric, real structure and end law. None is supplied by this curve proof.
No novelty/absence claim, numerical reproduction, independent review
or extension of earlier scientific admission is made.

Next: carry the second fundamental contribution and the actual gauge
projection into the surface equations before estimating the end.
Do not infer a split bundle from covariance, a raw coordinate pole,
or the old constant split Higgs-size formula. The full physical SM,
three-generation and gravity objective remains unfinished.
