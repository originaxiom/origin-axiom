# Test a condensate that supplies its own peripheral twist

Post-run hand-derived proposal, October8. UNEXECUTED. Not part of the
de1d52db6 certificate, not a new banked result. Seal a separate design and
verifier before any calculation is promoted.

The single-root completion needed an extra flat compensator, while its
odd centralizer retained gapless spin channels. Test whether both features
change when the sl2 grading itself produces the existing involution p.

Candidate in the same Euclidean root frame:

    alpha1=e4+e6, alpha2=e4-e6,
    alpha3=-e5+e7, alpha4=-e5-e7;
    E=E_alpha1+E_alpha2+E_alpha3+E_alpha4,
    H=H_alpha1+H_alpha2+H_alpha3+H_alpha4.

Predicted: the four roots are orthogonal, commute with color, and are
p-odd. Their diagonal sl2 has H=2v for old weak v=e4-e5. If the actual
root brackets and compact adjoint normalization verify this, the global
spin connection A=sH/2 uses the integral cocharacter v directly and
its limiting holonomy exp(i*pi*H/2) equals p without a compensator.
The extra fourth-root line lift may then be unnecessary as well.

Predicted adjoint sl2 decomposition from this H:78 spin0 copies,
55 spin1 copies, one spin2 copy. Do NOT identify a78-dimensional
centralizer with E6 by dimension alone. The expected spin0 directions
are p-even, potentially removing the previous ODD spectator obstruction.
The already derived R-block formula would predict a positive threshold
on all odd zero-angular channels; this still says nothing by itself
about the full coupled gauge-fixed boson/fermion operator.

Required discriminators: actual brackets, faithful embedding/peripheral
map, global spin transition, SAME action and kinetic measure, complete
adjoint decomposition, all coupled blocks and reality, gauge modes removed
correctly, and comparison with the one-root positive/zero-spectator controls.
Keep scale, root choice and genesis forcing priced. No SM mass or family
count from these integers. A full gap, if established, is still not a
proof of chirality; an SL2 self-duality map must be checked rather than
ignored or treated as an architecture-wide kill.

## Full-operator hand calculation to scrutinize, not a certificate

The proposed embedding factors through SO3:exp(i*pi*H)=1 in E8 since
H/2=v is integral. Do not call it a faithful SU2. All predicted adjoint
spins are integral. A dimension78 commutant is only a hypothesis for E6
until its actual brackets/root identification are exhibited.

In t=log(y), candidate canonically normalized radial variables are
delta(Ax+iAy)=sqrt(2)*y^(-1/2)*uA, delta q=uQ, delta r=uR,
and epsilon=y^(1/2)*u_lambda for the gauge scalar. With weight H=2m,
the proposed deformation-complex block uses

    D_m = d/dt + (m+1)/2,
    e_m = sqrt((j-m)*(j+m+1)), c=1/sqrt(2),
    D1 = (D_m,-c*e_m), D2 = (c*e_m,D_m),
    B_m = [[D_m,c*e_m],[-c*e_m,D_m^dagger]].

Crucial checks before using this:derive the maps from the actual chiral
metric, superpotential Hessian and gauge Killing map; retain connection
and spin-density factors; trace pairing puts R at weight -m-1, not m+1.
If the normalization and domains hold, B_m^dagger B_m has scalar
potential (m+1)^2/4+e_m^2/2. This agrees by hand with the previous R
block at the paired negative weight. Unpaired highest/lowest slots must
be retained. This is a proposed calculation, not an executed result.

Predicted zero-angular singular-channel profile for the four-root
candidate:mass squared1/4:133,5/4:110,9/4:3,13/4:2, total248.
Nonzero angular modes should be confining. Gauge fixing, reality,
domains and relative signs are load-bearing; a guessed mass matrix or
the R block alone cannot certify a gap. A positive essential threshold
would still allow isolated global zero modes and would not count them.

Possible remaining obstruction, also UNVERIFIED:if the centralizer is
E6, the structure SU3 representations3 and bar3 restrict to the same
real SO3 representation. A full intertwiner might pair the27/bar27
operators and domains. Construct and check it before asserting a zero
physical index. Conversely, never promote that conditional pairing to
a kill of other sources, domains, condensates or the architecture.
