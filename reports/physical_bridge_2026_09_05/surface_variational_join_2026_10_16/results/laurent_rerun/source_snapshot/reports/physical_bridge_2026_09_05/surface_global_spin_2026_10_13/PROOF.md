# Geometric transition maps for the surface fermion operator

This is an authored geometric bundle calculation on the already supplied
metric, not a derivation of the carrier, gauge theory or physical vacuum.
It addresses the geometric part of the previous global-domain duty.

## Coframe and canonical bundle

For gamma=(a b;c d), j=c tau+d, the actual coordinate map is
tau'=(a tau+b)/j, (u',v')=(a u-b v,-c u+d v), w'=w/j.
Thus y'=y/|j|^2, d tau'=d tau/j^2 and

    du'+tau' dv'=(du+tau dv)/j,
    d tau' wedge d w'=j^(-3) d tau wedge d w.

For e_H=e1+i e2 and e_V=e3+i e4, pullback gives
e_H'=exp(-2i theta)e_H and e_V'=exp(-i theta)e_V.
The normalized canonical frame therefore has phase exp(-3i theta).
This derives the transition from the full complex coordinate map;
the real density power2 is not substituted for canonical weight3.

## Ordinary spin and canonical Spin-c

For section COEFFICIENTS (not pulled-back basis vectors), the spin map
is U_spin=exp[-theta G], G=c1c2+c3c4/2. It intertwines the principal
Clifford symbols with the two actual frame rotations. In the Fock
basis used by the previous dictionary, its weights are
3/2,-1/2,1/2,-3/2. The inverse canonical half-line contributes
g_R=exp(-3i theta/2). Hence U_can has weights0,-2,-1,-3,
exactly the coefficient action on0,(0,1)_H,(0,1)_V,(0,2) forms.

At theta increased by2pi, U_spin changes by-I4 and g_R by-1;
U_can is unchanged. The canonical product thus descends through this
geometric metaplectic kernel, although its two factors separately do
not. This does not assert that K^(1/2) exists as a separate line on
the unlifted modular quotient. Spin and R data may instead be carried
on the lift; the canonical Spin-c product is intrinsic to the Kähler
geometry. Further flat lift characters are not selected here.

For S: tau maps to-1/tau, with0<arg(tau)<pi. The successive S angles
sum to pi after S2 and2pi after S4. The section spin map at pi has
square-I4; the canonical map has squareI4. The same continuous lift
gives (ST)^3=S2 geometrically. Together with S4=I in the canonical
product these are the SL2Z defining relations. T has j=1 and zero
angle, so the geometric transition on both products is identity.
This is not identity of the coefficient lift or its cusp phases.

## The connection glues with the full differential operator

Direct differentiation gives

    pullback(dx'/y')-dx/y=2 d theta,
    pullback(a_R')-a_R=3i d theta/2=-d g_R g_R^(-1).

So the earlier a_R=3i dx/(4y) has the required unitary gauge law.
Its nonzero curvature remains; cancellation of a discrete central
sign does not make the connection globally removable.

Use the actual K=-c2/(2ell)+c1c3c4/(4ell). In ell=1 units set
R=diag(Rotation(-2theta),Rotation(-theta)), with entries defined by
the displayed coframe map, and C_j=sum_i R_ij c_i. Then

    K-U_spin K U_spin^*=sum_j C_j G E_j(theta),
    K_can-U_spin K_can U_spin^*
      =sum_j C_j (G+3i/2) E_j(theta),
    K_can=K+3i c1/4.

The base derivatives are E1(theta)=-sin^2(theta),
E2(theta)=sin(theta)cos(theta); fibre derivatives vanish. These
identities give covariance of the FULL first-order expressions,
not just their principal symbols. Dropping the vertical lift or
reversing the R phase fails. The native method checks variable theta;
the second route uses independently reconstructed Fock Cliffords at
exact rational rotations as finite controls.

## The coefficient and physical limitations

Retain the literal rank6 coefficient A0,B0 and the previously embedded
L,R intertwiners. Their supplied S-like product and its fourth power
are computed as a separate factor, with both inverse conventions.
It is not assumed that a geometric SL2 relation is a based relation:
the based Delta4 can be an inner conjugation with puncture transport.
Main B1641 itself restricts its asserted uniqueness to the Delta4
check and leaves full Aut+F2 coherence to Gate12. Our result cannot
discharge that duty by multiplying dimensions or centre characters.

All248 E8 components remain. Their spin/R factors obey the same
geometric covariance; the coefficient/adjoint central actions and
reality law must separately agree with every based relation. No
scalar R character is relabeled as an E8 adjoint gauge generator.

Canonical geometric descent is a positive map, not a selected parent
or physical index. Ordinary spin remains allowed on a suitable lift
or with appropriate additional admitted data; this is no ordinary-spin
or architecture kill. The puncture plane's global compatibility,
complete multiplet/source/end variation, total complementary estimate,
charged kernels, Higgs interactions and anomalies remain owed. In
particular the projected ordinary-spin confinement is not copied
unchanged into the canonical problem. The full SM/TOE goal remains
unachieved, and the earlier common-Hilbert-space correction stands.
