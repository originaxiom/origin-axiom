# Harmonic transfer and the conditional interaction test

Authored before execution, 2026-10-04. This argument retains the supplied
hyperbolic metric, twisted gauge action, spacetime and positive coupling.
Finite tests discharge algebraic prerequisites, not global analytic proof.
R54/F15 supplied prior art for the derivative-to-vertex method, on different
data. No canonical-metric estimate from that seat is used here.

## 1 The actual new stationary background

Fix either new component at t0=-1. Its literal holonomy is

    A0(g)=diag((-1)^v_g zeta3^(j a_g)) P_g.

All factors are unitary in the standard complex metric, determinant one
and contained in a finite monomial group. The relators and fixed marked
peripherals have already been checked and are checked again by the jets.
The diagonal phases commute with every trace-free real diagonal matrix.
Consequently the associated real diagonal adjoint bundle on M6 is EXACTLY
the old permutation bundle, not only a bundle with equal fiber dimension.
The tests verify this by actual conjugation of every diagonal basis matrix.

The old logarithmic cocycle v therefore remains a nonzero interior real
diagonal class, with H0=0 and zero meridian/longitude periods. The authored
construction in monomial_harmonic_background_2026_09_27/PROOF.md applies
on M6 itself: the scalar Hardy inequality and Rellich argument give the
zero-form inverse; a compact representative gives a unique harmonic beta;
the finite torus cover and complete Fourier/Bessel argument give bounded
primitives, all-jet rapid cusp decay and all finite Lp norms for beta.
Nothing in those steps requires A0 to descend as a rank-five bundle to M2.
Its diagonal bundle and exponent cocycle do descend, as already checked.

The commuting nonlinear construction is unchanged:

    A_z=A0+i Im(z) beta,  Psi_z=Re(z) beta,
    C_z=A0+z beta,         t=-exp(z).

All curvature and moment residuals vanish. On the universal cover the
primitive F of beta transforms by v_g and Ad(P_g); since the new diagonal
phase commutes with F, exp(zF) intertwines the literal new E(t) holonomy
and C_z by the same identity as in the original proof. This is not a
globally allowed complex gauge that removes the nonzero class.

The full E8 Cartan projection used earlier commutes with structure Weyl
transport. Diagonal structure torus factors fix the Cartan pointwise and
preserve each root space, so they also commute with this projection.
Thus beta remains nongauge in the full parent. Its kinetic coefficient is
finite and positive, (60/g7^2)||beta||^2 in the raw adjoint trace convention;
its numerical value is not computed. The same invariant torus one-form
channel leaves zero in the neutral essential spectrum. No isolated EFT
or preferred value of z follows.

## 2 Harmonic charged profiles at the unitary center

At z=0 the induced E and E* connections are finite unitary. The complete
charged comparison in charged_l2_bridge_2026_09_27/PROOF.md applies with
the new A0: its proof uses a unitary end, zero-form gap modulo H0, bounded
frame change and the anchored Hardy primitive estimate, not the old
permutation matrices. It supplies H1_L2=ordinary interior H1 without a
degree-one gap. The previous exact calculation gives dimension one on
both charged sides, with H0=0, and dimension zero in Lambda2 E and its dual.

Their harmonic one-forms have compact closed representatives. Subtracting
the reduced zero-form Green correction yields the harmonic form, exactly
as for beta. On the finite torus cover its L2 harmonic primitive has constant
zero Fourier mode and decaying nonzero modes. Its derivative has no zero
mode. Therefore the charged profiles and all derivatives decay rapidly;
the primitive is bounded on each cusp. All triple products below are
absolutely integrable, and complete cutoffs justify integration by parts.
This is an authored transfer, not a global numerical PDE solution.

## 3 Ordinary obstruction with boundary artifacts removed

Differentiate the flat coefficient at t=t0 exp(z) over the dual numbers.
If J(z) is the Fox degree-one differential, a cocycle x continues to first
order only if J x1=-dot J x. The connecting homomorphism of
0 -> E -> E_epsilon -> E -> 0 therefore sends [x] to [dot J x] in
ordinary H2. Differentiating J B=0 shows it kills ordinary coboundaries.
The base figure-eight one-relator complex and its verified covering
presentation compute this ordinary group cohomology; equivalently the
connecting map is defined without a choice of presentation resolution.

To restrict its INPUT to interior classes, choose strict zero-period
cocycles N=ker(J stacked with R). Subtracting a coboundary can make any
interior cocycle strict, since its boundary restriction is boundary-exact.
The kernel of N -> interior H1 is precisely B ker(boundary d0), with
dimension t0-a0. The boundary matrices are constant in z, so these classes
continue as B(z)k and their ordinary and fixed-peripheral obstructions
vanish. The code checks this directly, including the derivative identities.

The rank increment rank[J, dot J N]-rank J is consequently the rank of
the ordinary obstruction on the actual interior space. Its field degree
is two, so every reported rational rank increment is divided by two.
The stacked (J,R) rank increment additionally requires zero peripheral
periods of x1. A relative-only answer is explicitly insufficient here.
Any positive ordinary answer has a literal cycle/cokernel pairing witness.

In differential forms the same connecting homomorphism is, up to one
global convention sign, [beta acting wedge alpha], where alpha is the
charged closed one-form. Naturality of the local-coefficient de Rham
comparison identifies this with the Fox calculation. Replacing beta or
alpha by its harmonic representative changes the ordinary class by an
exact term; it cannot change a positive ordinary answer.

## 4 A nonzero ordinary answer gives a nonzero overlap

This implication is CONDITIONAL on a nonzero ordinary answer; no outcome
is assumed before execution. Both beta and alpha are interior classes and
have compact representatives. Their product lies in the image of H2_c(E)
in H2(E). Poincare-Lefschetz duality gives a nondegenerate pairing of that
image with the image of H1_c(E*) in H1(E*). One way to see the descent is
to pair a compact two-form with a compact dual one-form: if the latter is
ordinary-exact, the integral is zero by Stokes on compact support. The
long exact sequence and its dual then identify the two interior images
as dual spaces. This uses the oriented compact core and its boundary.
It does not assert an ordinary H3 fundamental class on the open manifold.

Thus a nonzero ordinary obstruction in the one-dimensional interior
charged space has nonzero pairing with its one-dimensional interior dual.
Replace compact representatives by the actual harmonic profiles. Their
bounded primitives and rapid form decay make every Stokes boundary term
vanish on an exhaustion of the cusp. The same pairing becomes

    Y = integral_M6 gamma wedge (beta acting wedge alpha) != 0,

for nonzero harmonic charged profiles alpha and gamma in the actual dual.
No closed range or inverse for the degree-one Laplacian was assumed in
this reasoning. This avoids importing R54's acyclic charged end into the
present invariant-channel, zero-threshold geometry. Positive finite kinetic
normalization is an invertible rescaling and cannot turn nonzero Y into zero.
Its numerical normalized value is not obtained from the Fox pairing.

## 5 The parent vertex and its interpretation

The verified regular A4+A4 E8 branching contains the structure adjoint,
E paired with its dual and the corresponding gauge representation paired
with its dual. Invariance of the nondegenerate parent trace identifies the
adjoint-charge-dual contraction with evaluation lambda(Hv), up to a fixed
nonzero factor. This is the defining action of sl5, not an independently
supplied Yukawa coefficient. The unitary full gauge algebra is checked
separately through all charged H0 and the complex-linear commutant of E.

Expansion of the general fermion term in the supplied action gives
Tr(psi wedge [delta C wedge psi]). Inserting beta, alpha and gamma yields
the overlap above. The action was personally checked at Braun et al.
(2.13) and (6.2)-(6.5) on October 4:
https://arxiv.org/html/1812.06072v2 . The examples' Morse sources, compact
G2 setting and associative instanton geometry are not hypotheses of this
local action application. This packet establishes at most a conditional
finite nonzero classical fermion vertex, not a cubic scalar potential.

If both charged sides have nonzero obstruction, the neutral deformation
acts on a PAIR. It is not selective mirror removal or chirality. A nearby
pole mass, a separated reduction in the presence of the continuum, quantum
selection, anomalies, gravity and empirical predictions remain unpaid.
If the ordinary obstruction is zero, retain the paired modes and report
that answer: isolation alone cannot rule out a higher-order interaction.
