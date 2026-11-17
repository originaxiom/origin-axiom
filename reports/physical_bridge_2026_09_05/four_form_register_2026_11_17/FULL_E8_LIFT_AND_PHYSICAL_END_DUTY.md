# Carrying the curvature unit into the full physical register

2026-11-17. PHYSICAL-C7 author hand derivation, pending independent
review. This applies the existing E8 root/centre calculation to the
four-form family. No scientific producer or test ran.

## 1. The four singlets see an effective circle

The actual source generator is

    Q=(2/3)(e_1+e_2+e_3).

It has charges +1 and -1 on the colour-singlet E6 spinor grades.
The full E8 coefficient roster also contains charges +/-1/3 and +/-2/3.
The existing source therefore has

    exp(6pi i Q)=1,
    z_3=exp(2pi i Q)!=1, z_3^3=1.                    (1)

On the four form coefficients, z_3 acts as identity. Thus their
effective phase circle is the quotient of the faithful Q circle
by this Z3. This is the same centre retained by P-C3c's explicit
colour-preserving E6 inclusion. It remains visible to colour-charged
probes of the full parent.

Normalize the full Q-circle angle as theta=phi/3, so theta has period
2pi. Its map to the effective circle is exp(i theta)->exp(3i theta).
For principal circle bundles on a sphere this implies

    c_1(effective)=3 c_1(full Q-circle).               (2)

The primitive c_1=1 orbit bundle derived in C7 therefore has no lift
through the pure Q circle over that same sphere. Equivalently, the
would-be colour line of charge -1/3 would have degree -1/3. An
ordinary complex line bundle has integral degree. A transition
exp(i varphi Q) also ends at z_3 when varphi goes from zero to 2pi,
so it fails to be a loop in the full Q circle.

This is an obstruction to that particular lift. It does not obstruct
the coefficient family or a lift that retains the actual colour group.

## 2. The existing U3 subgroup supplies compatible full-group lifts

Use the source's complementary SU4 and its colour-preserving subgroup

    V in U3 -> diag[(det V)^-1,V] in SU4 subset E8.    (3)

The four of SU4 has one colour singlet and one colour triplet. Taking
V=exp(-i phi/3) I_3 gives charges +1 on the singlet and -1/3 on
the triplet, exactly as in the source. The effective character is
therefore chi(V)=(det V)^-1. Its kernel is SU3.

Let L be the effective line with c_1(L)=1 on the parameter sphere.
A compatible colour rank-three bundle E satisfies

    det E=L^-1.                                      (4)

For example E=L^-1 direct-sum 1 direct-sum 1 realizes (4), and
L direct-sum E has trivial determinant. The associated SU4 bundle
and its E8 embedding are well-defined. The equatorial transition

    diag[exp(i varphi),exp(-i varphi),1,1]             (5)

is a closed loop implementing this example. It includes a colour
Cartan contribution alongside the Q phase. A compensating projective
colour transition carries the centre information that (2) exposed.

Thus full-group lifts exist with colour transported. Their connection
and their physical realization require the full source theory. The
four singlets alone fix chi and its primitive period, while leaving
the SU3 connection data unmeasured. A pure central Q connection with
a globally fixed trivial colour frame would impose the stronger
divisibility condition (2).

Formula (4) is a constraint on the parameter-family bundle. It does
not select a colour flux on the original physical surface. A family
of gauge-equivalence classes and a globally framed universal family
have different lifting requirements.

## 3. What a physical end map would have to establish

The C7 unit is integrated on a sphere of stationary-field directions.
The source end/index unit belongs to its physical carrier and its
fermion realization. To connect them one needs an actual map f from
that carrier's relevant cycle to the field-direction family, together
with the admissible full-group lift and source transformation law.

For a closed oriented two-cycle C on which such a map and lift exist,
the effective phase curvature would obey

    (1/(2pi)) integral_C f^* F = <f^* c_1(L),[C]> in Z.              (6)

The family supplies a primitive class. The map f supplies the integer
in (6). Its degree, boundary behavior, stationarity and backreaction
are further duties. A requirement that this integer equal one would
still be an added condition until that map or an internal law forced it.
For an open surface the actual relative boundary trivialization and
the end contribution must also be included before using a relative
Chern number or a fermion index.

The coefficient cone includes its vertex at finite metric distance.
The circle action degenerates there and Q becomes unbroken. The
primitive sphere contracts through that vertex in the full cone.
An argument using the nonzero-amplitude region must therefore justify
any condition preventing an actual physical field from reaching the
vertex, or retain the unreduced gauge fields through it. Parameter-
space topology by itself does not supply that physical restriction.

## 4. The mechanical connection is one part of fermion transport

On a chosen parameter path, the full real Gauss inverse determines
the gauge compensator. Its scalar leading component is C7's A_0.
The fermionic field transports in the full E8 representation, with
the spin, core, Hilbert metric and complete operator domain carried
at the same time. Its colour-charge sectors need the lift above.

If an isolated finite spectral subspace is independently established,
its projected connection comes from its actual spectral projection
and this complete field transport. An embedded zero mode beside a
continuum at zero cannot acquire a finite effective connection simply
by assigning a basis to it. The full source operator remains available
on the common domains proved conditionally in the companion note.

An effective Q phase acts as a scalar on a fixed Q eigenline. A link
containing only that phase cannot turn two equal kernel lines into
transverse ones. It cannot reproduce the chosen cross-module Spin10
rotation of the two-cell lifting example by itself. The non-Abelian
field response, source equation and actual operator must provide any
such additional relative transport.

## 5. Normalization, state and history freedom remain discriminators

Multiplying the common classical action by a positive constant rescales
its kinetic and residual forms together. The mechanical connection
is unchanged because its real Gauss numerator and denominator scale
together. Its curvature class is unchanged as well. With a quantum
reference held fixed, canonically normalized interaction strengths
can still change under this rescaling, as in reduction card 01.
The C7 topological unit therefore leaves that normalization duty open.

The same distinction can be checked with differential forms. In the
canonical four-mode coordinates the source symplectic form is

    omega=i sum_j(dP_j wedge dbar P_j+dR_j wedge dbar R_j)
         =d Theta,
    Theta=Im(P^dagger dP+R^dagger dR).

On the zero-moment locus, Theta annihilates the phase generator and
is invariant, so it descends to a globally defined one-form on the
smooth quotient. In the unit-vector coordinates it is

    Theta=t^2(a_u+a_v),
    omega_red=d[t^2(a_u+a_v)].                        (7)

On the primitive sphere v=bar u, Theta and the pulled-back omega_red
are zero. Their integral vanishes, while the difference connection
A_0=(a_u-a_v)/2 has the nonzero period established above. Thus its
curvature unit does not quantize the scale of this exact reduced
symplectic form. Requiring prequantization of omega_red on this
region would allow every positive common scale because its de Rham
class is zero. A different nonzero moment level or boundary source
would change this argument and must have its own derivation.

Likewise, deriving the connection for a specified path does not select
the path, amplitude or measure on paths. Its nonzero curvature permits
different links for different paths with the same endpoints. The
scalar phase alone also forgets closed-word commutators. The full
registering relation must retain the based path, non-Abelian transport
and physical source instead of reducing the entire history to this
one phase.

The concrete advance is a derived family geometry, a same-action
connection, a primitive class, and its exact centre/lift constraint.
The consequential next question is whether the foundational based
register supplies the map f, its colour lift and its source dynamics.
That is an explicit mathematical target for earning the physical
end unit. It remains open, with no three-generation or gravitational
identification claimed by the class alone.
