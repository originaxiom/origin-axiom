# Cohomology products and the boundary prescription

This argument states the finite compatibility test. It is not a derivation
of a nonlinear elliptic domain or a universal physical no-go theorem.

## Tensor lines from the existing parent

Write F=Lambda2(E), with det E canonically trivial in the chosen basis.
The equivariant maps are

    E tensor E -> F,              (u,v) -> u wedge v,
    E tensor F -> F dual,         (u,a)(b) = vol(u wedge a wedge b),
    F tensor F -> E dual,         (a,b)(u) = vol(a wedge b wedge u).

Their dual analogues use the dual volume. These are the maps already
identified in R59's two parent cubic channels. A specific gauge-index
choice can make each bracket channel nonzero; this test concerns the
coefficient maps only and claims no physical relative normalization.
The first coefficient map is alternating, the third symmetric. These
signs do not remove the separate differential-form cup signs.

## Products on the marked torus

For group cohomology with local coefficients the cup on the fundamental
bar cycle [p|q]-[q|p] is the formula in the design. Equivariance of B
ensures it descends to cohomology. Its exact ambiguity is the image of
the target torus differential (1-Q,P-1). The program verifies this
descent on exact and harmonic bases for each channel, instead of relying
on the formula's name. The exchange relation uses the flipped coefficient
map and a minus sign for two degree-one inputs. It is checked modulo
exacts, not as a false equality of raw cochains.

Products of an invariant vector and a closed one-cochain are closed.
Changing that one-cochain by an exact changes the product by a target
exact. Thus testing membership in L modulo target exacts is independent
of the selected harmonic representative, provided L denotes the same
subspace of cohomology. All degree-zero products automatically land in
H0 when the tensor is equivariant, and this is checked directly.

## The condition being tested

In a model where allowed graded boundary cohomology is

    A(E) = H0(T;E) plus L(E),     A2(E)=0,

tensor closure requires both H0 times L products to land in the target
L, and L times L products to vanish in target H2. A nonzero quotient
rank contradicts exactly that requirement. It does not contradict the
existence of the preceding mapping-cone complex: a cochain complex need
not be closed under nonlinear tensor operations.

It also does not prove that every physical realization of the same
linear spectrum fails. A justified boundary action may restrict allowed
degree-zero transformations, supply additional fields, induce nonlinear
trace relations or admit a different analytic extension. Each is a
changed hypothesis requiring its own field equations and spectrum.
Nor does cohomology closure imply pointwise closure or finite action.
The R62 cone calculation illustrates why those stronger steps matter.

The common-line trivial control has L(E)=ell tensor E in all sectors.
Then H0 times L stays on ell and ell wedge ell=0, so every tested
product closes. With independent lines ell,m, the cup contains
det(ell,m) times the coefficient product. Nonzero coefficient and
line determinants give an explicit opposite control. The test can
therefore both pass and fail; it is not designed to force a negative.
