# Keeping the full matrix: a scalar assignment and its global price

October 24, 2026. Authored conditional analytical audit, UNREVIEWED.
No scientific source, test, symbolic engine or numerical experiment was
imported, collected or executed. Frozen verification proposals are unchanged.

Scope: assignments of the full End(C2) matrix into the ALREADY specified
regular SU6 x SU3_colour x SU2_weak frame of E8, retaining its quaternion
embedding. This is not a derivation of that frame, of a physical Higgs,
or of an additional U2 gauge symmetry from the foundational principle.

## 1. Recover the existing result, do not recount doublets

The form-parent and companion-roster proofs of October 8 already give

    Lambda3(C2 tensor C3) = (Sym3 C2,1)+(C2,8),
    rho multiplicity = (3,2,bar3)+(bar3,2,3)+(1,2,8)+2(1,2,1).

The companion producer reconstructs every joint torus weight by Q8
character projection; its reference uses integer weight convolution.
Their test file compares those full records, not just dimensions.
The quartet and the two family-singlet doublet multiplicities are NOT
new findings here.

The registered-embedding proof of October 13 already supplies the
faithful map iota_Q(g)=I3 tensor g in SU6 after its declared fixed
parity-frame conjugation, and its full trace normalization.
The October 14 field-map proof establishes on the complete E8 adjoint

    iota_Q(-I2) = -I6 = iota_w(-I2) = p.                    (1)

These faithful factors commute, although their intersection contains p.
The old bare End(C2) under conjugation is p-even, while the chosen
weak doublets are p-odd. That necessary representation test stands.
It does not prohibit assigning a scalar component to an existing even
adjoint field.

The question here is narrower than another representation census:
what additional requirements are being imposed when someone asks to
embed the WHOLE matrix S rather than its traceless part?

## 2. A full Lie-algebra map already has room in SU6

Write S=S0+s I2, s=tr(S)/2, tr S0=0. For any specified nonzero
T in sl3_family define, in the same conjugated coefficient frame,

    j_T(S)=I3 tensor S0+s T tensor I2 in sl6.               (2)

The two summands commute, and their trace is zero. Therefore

    [j_T(S),j_T(R)]=j_T([S,R]).

They lie in independent tensor summands, so (2) is injective.
It respects quaternion conjugation and commutes with the old colour
and weak factors. Thus no new abstract E8 component has to be added
to write a full scalar-plus-traceless LINEAR LIE-ALGEBRA assignment.

But T is part of the assignment. Under family SU3 it transforms by
conjugation; there is no nonzero fixed T under the full family group.
That follows already from the companion roster: its Q8-invariant,
colour/weak-neutral module is the family adjoint 8, with no further
family singlet. It does not require upgrading a character count to
an independently verified F4 bracket classification.

A choice of T is not automatically a physical parameter: conjugate
T's with all other fields transported can be gauge descriptions of
one configuration. However even at fixed positive norm, distinct
Hermitian eigenvalue spectra remain. For example both

    T1=diag(sqrt(3/2),-sqrt(3/2),0),
    T2=diag(1/sqrt(2),1/sqrt(2),-sqrt(2))

have squared trace norm 3 and trace zero; their determinants differ.
They are not related by unitary family conjugation. A fixed norm
alone does not select the scalar embedding. Allowing T to be a
dynamical family-adjoint field changes the proposed field/state
assignment and requires its same-action equations, not a hand-pick.

The existing quadratic trace law gives, for Hermitian T and arbitrary
complex S,

    Tr248[j_T(S) dagger j_T(S)]
      =180 tr2(S0 dagger S0)+120 |s| squared tr3(T squared). (3)

The mixed term vanishes by tracelessness. If the proposed source metric
is proportional to tr2(S dagger S), matching its scalar and traceless
parts with the same coefficient would require tr3(T squared)=3.
Equation (3) is conditional on that requested metric match; the
actual physical S metric has not been derived by imposing it.

## 3. Lie algebra versus group: a specific incompatibility

Suppose, ADDITIONALLY, that one wants a continuous group homomorphism

    Phi: U2 -> E8

which (i) restricts to the existing faithful iota_Q on SU2,
(ii) commutes with the entire old colour SU3 and weak SU2,
and (iii) represents the full central circle of U2.
These are extra model requirements, not premises proved for the paper's S.

The complete existing E8 branching shows that the Lie algebra
centralizing colour SU3 x weak SU2 is precisely sl6: its only
colour/weak-singlet block is (35,1,1).
Hence the connected image of Phi lies in the existing faithful SU6
factor. Its central circle must also commute with I3 tensor SU2.
Its Hermitian generator is therefore T tensor I2 with traceless
Hermitian T on C3.

Here is the elementary global obstruction. U2 is the quotient of
SU2 x U1 by (-I2,-1): the map (g,z)->z g has exactly that kernel.
The lifted central circle in SU6 has weights t1,t2,t3 on C3.
Periodicity at angle 2pi makes every ti an integer, while determinant
one for every angle requires t1+t2+t3=0. Descending the kernel element
(-I2,-1) would require

    exp(i pi T) tensor I2 = -I6.

Thus all three ti would have to be odd integers. Their sum cannot be
zero. This proves that requirements (i)–(iii) cannot all hold together.

This is NOT an obstruction to (2) as a Lie-algebra map, to a map from
a covering group, to a scalar as a geometric variable, or to a nonlinear
state-dependent assignment. Nor does conjugation covariance of S
itself require S to be a U2 connection. The paper does not acquire
this new group hypothesis merely because its matrices are two by two.
It would be a mistake to spend this conditional test as a physical
no-go or a reason to drop tr S.

## 4. A positive global control already inside the same E8

Drop only the requirement that the scalar assignment commute with the
FULL old weak SU2, and use its existing torus. Define

    Phi_w(g,z)=iota_Q(g) iota_w(diag(z,z^-1)).              (4)

By (1), (-I2,-1) maps to p p=1. The two factor images intersect
only at {1,p}: they commute, so their intersection is central in
each faithful SU2 and is therefore contained in {1,-1}.
Consequently (4) has exactly that two-element kernel and descends
to a faithful U2 embedding in E8.

The scalar Lie generator is now the existing weak Cartan H_w,
not a weak-neutral flavon:

    j_w(S)=iota_Q(S0)+s H_w.                               (5)

A nonzero scalar expectation along (5) need not preserve the old
weak SU2; its centralizer there is its torus. This changes the
physical assignment. It is not a construction of the observed Higgs
doublet or of its vacuum.

Within this SPECIFIED weak SU2 and with no extra family circle, a
circle homomorphism has diag(z^n,z^-n) after conjugation. Descent
requires n odd, and faithfulness requires |n|=1; larger |n| leaves
additional central-circle kernel. This gives a primitive control,
not uniqueness among every E8 embedding. Adding family cocharacters
or changing the original embedding is a different family of maps.

The full existing adjoint branching also fixes the induced norm.
Weak adjoint 3 contributes 4 tr2, and its 56 doublet copies contribute
56 tr2, so Tr248 restricts to 60 tr2 on the weak root SU2.
Cross terms with iota_Q(sl2) vanish by invariant-pairing orthogonality
of the commuting semisimple factors. Therefore

    Tr248[j_w(S) dagger j_w(S)]
      =180 tr2(S0 dagger S0)+120 |s| squared.               (6)

This is not 180 tr2(S dagger S): the scalar term would then be 360.
Rescaling H_w by sqrt(3) to force that equality would destroy the
primitive central-circle integrality used in (4). Instead retain
the inherited metric or justify another physical kinetic assignment.
The relative factor is a representation/normalization fact in this
chosen frame, not a measured gauge-coupling prediction.

## 5. What the registering relation changes

A scalar S=s I2 does not mean the whole state is symmetry-fixed.
The preceding matter-trace audit already keeps M as well as S.
For actual nonzero rank-one raw M, M epsilon is not a nonzero scalar,
so its traceless part provides nontrivial transported data.
An assignment depending on these retained fields can break a symmetry
without an externally chosen fixed T. That is a real route to inspect,
but mere existence of many covariant polynomial expressions does not
derive which one occurs in the action.

Thus neither the full-family invariant-vector test nor the U2
central-circle test is an exclusion of state-dependent interactions.
What must be derived is the joint field map and action with its
existing normal/spin factors, not a gauge direction picked after seeing
a desired mass matrix. Distinguish the registering state from a claim
that each of its coordinates is separately an adjoint Higgs.

## 6. Consequence for the physical task

Reuse the already computed doublet and companion roster. Do not repeat
its exterior-power calculation or silently delete its two singlet-family
doublets. Do not discard the trace of S because I6 is not in sl6.
Instead determine which proposed role for that coordinate is actually
demanded by the generated state/action:

- a scalar Lie-algebra assignment with specified T;
- a true compact group/bundle extension, with its central quotient;
- a geometric or coupling variable with its own kinetic law;
- a joint field-dependent assignment retaining matter/register data.

Equations (2) and (4) are compatible-assignment controls, NOT a selection
among these roles. No action, stationary background, chiral spectrum,
generation count or foundational input is newly derived by choosing
one of them. The useful new restriction is on an over-demanding
parent-map specification: Lie, global-group, old-weak-neutral and
metric requirements cannot be conflated.

Separate verification is owed for the tensor centralizers, centre
descent and kernels, trace coefficients, both T examples and a
state-dependent rejecting control. No existing test was run or
retroactively extended. A future source-complete design must precede
execution; the approved P210 review does not cover this note.

Research custody: local starting checkpoint ab5a5c1f6; last successfully
fetched main 8ad6d5cb0, SM f51659605 and chat1 a53347f7f.
Publication is still subject to the previously recorded approval-service
failure; no new fetch or push is asserted. Searches used scalar/trace,
weak/centre/center, End(C2), U(2), GL2 and Unicode F4 variants. Early
unquoted globs failed and a broad U(2) pattern also matched SU(2);
the corrected word-boundary searches were used before drawing scope.
This is not an exhaustive absence or novelty claim.
