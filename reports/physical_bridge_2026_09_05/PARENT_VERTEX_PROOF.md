# R38 authored candidate: subgroup lift and classical field dictionary

September 20, 2026. Written before execution. Root/tensor checks below
are finite and exact. Their application to the quoted classical action
is a source-based mathematical argument, not independent acceptance
of a physical completion. The supplied four-dimensional spacetime,
compact gauge group, twist and parent action are explicit assumptions.

## 1. An explicit candidate, not a new name for a 27

Let C be R21's E6 Cartan matrix, u=C^-1 e0, p=I-(3/4)u e0^t.
For D5 use the simple-root rows

    B = (e4+e5, e4-e5, e3-e4, e2-e3, e1-e2).

Define an 8-by-6 map T by

    T lambda = (B^t (p lambda)[1:], 0,0,0)
               + (3/4)lambda0 U,
    U = (0,0,0,0,0,-2,2,2).

Then T u=U and T maps the five D5 simple coroots to their displayed
roots. A target weight r restricts to w=C^-1 T^t r. Its charge w0
is r dot U. Check every weight, not merely this last component.
The original H cocharacter lattice is C^-1 Z6. In a primitive E8
simple-root basis A the torus map is K=A^-1 T C^-1. Integral K
and gcd of its rank-six minors equal to one establish an injective
map of compact tori, not only an injective Lie-algebra map. Together
with the actual D5 root maps this defines a faithful compact-group
H embedding. Root vectors can be normalized along that D5 subsystem.
This is not an embedding of hyperbolic holonomy in a compact group.

The standard E8 roots are the 112 vectors +/-ei +/-ej and the 128
half-sign vectors with an even number of minus signs. The fixed
simple-root basis used in the code has determinant of absolute value
one and the E8 Gram matrix. Its reflection orbit must agree with the
whole direct enumeration. This controls completeness of the roster.

The orthogonal A2 simple roots are f1=e6+e7 and f2=e8-e7. The three
family weights (r dot f1, r dot f2) are (1,0),(-1,1),(0,-1).
For EACH one, the full H weight set should equal R21's actual
16_1 + 10_-2 + 1_4, including its global lattice. Opposite family
weights give the conjugates. Family-zero roots give an E6 root
subsystem, but NOT the original E6 embedding. The predicted roster is

    248 = 45_0 + 1_0 + 8_0
          + 16_-3 + conjugate(16)_3
          + 3(16_1 + 10_-2 + 1_4)
          + 3(conjugate(16)_-1 + 10_2 + 1_-4).

The compact-H charge dimensions are 54 at zero, 48 each at +/-1,
30 each at +/-2, 16 each at +/-3, and 3 each at +/-4. The zero
weight's multiplicity includes eight Cartan directions; the 54 is
not a 54-dimensional irreducible representation. All extra sectors
must remain in the field ledger. Three algebraic copies do not
derive three chiral low-energy generations.

In the original R19/R21 E6 adjoint, charges are only 0,+/-1.
Its simple root e0 maps under T to squared length EIGHT, not two.
Thus this T does not extend that original E6 root embedding. The
candidate changes the parent, not just its notation. Conversely the
absence of elementary 10_2 and 1_4 in that one adjoint says nothing
against higher representations, localized fields or composites.

## 2. The physical-field map is part of the test

The partially twisted 7D SYM action of Braun et al.,
[1812.06072v2](https://arxiv.org/pdf/1812.06072v2), sections 2.1, 2.5,
6.1--6.2 and appendix B, uses an adjoint zero-form gaugino lambda
(their chi), an adjoint one-form fermion psi_i, and a complex adjoint
one-form boson varphi_i. Their equations (B.1)--(B.2), (B.12) and
(B.29) fix that dictionary and the relevant contractions.

The local fermionic internal terms, suppressing nonzero conventional
constants, are

    Tr(lambda bar-D^i psi_i) + Tr(epsilon^ijk psi_i D_j psi_k)
    + conjugates,

where D includes bracket with varphi. The resulting cubic types
are lambda--psi--bar-varphi and psi--psi--varphi. Eliminating the
displayed algebraic auxiliaries does not add a lambda--lambda--
varphi cubic. This is a statement about THIS classical pure-SYM
action, not its possible defect, higher-derivative or quantum additions.

The R30 zero-form profile u times a right Weyl field of charge +1
would map, after four-dimensional charge conjugation, to the charge
-1 zero-form gaugino profile conjugate(u). R33's symbol chi means
that left-conjugated partner, not an independent generation. Its
one-form partner v maps kinematically to a one-form fermion. This
specifies the contemplated map on the pure scalar/exact-form branch;
it does NOT prove that R29/R30's source action has the required
supersymmetric partners or that interacting eigenstates stay pure.

Similarly a four-dimensional S or Q descending from the pure-SYM
bosons must multiply an INTERNAL ONE-FORM mode. Its charge alone
does not identify it with R37's internal scalar coefficient s0.
Localized fields need a separate dictionary and source action.

## 3. Two independent tensor tests and positive controls

Under internal SO(3), the spaces of invariant tensors for form
types (0,0,1), (0,1,1), (1,1,1) have dimensions 0,1,1. In the
last two cases the tensors are delta and epsilon. We solve the
complete infinitesimal invariance equations, with no finite sample
of rotations. Supplying an additional internal vector changes this
tensor problem; none is silently used to manufacture the first type.

There is a separate statistics check. For left Weyl Grassmann fields,
epsilon_(alpha beta) theta_A^alpha theta_B^beta is SYMMETRIC in
A,B. The invariant bracket tensor f_ABC of a compact metric Lie
algebra is antisymmetric. Consequently a proposed f_ABC S^C
theta_A theta_B with two identical zero-form field species is zero.
In matrix terms, (f_AB tensor epsilon_spin) is symmetric, whereas
only the antisymmetric part contributes to a Grassmann quadratic.

Adding one-form labels changes this: f_AB epsilon_(ijk) S^k is
symmetric under (A,i)<->(B,j), so its spin-epsilon product is
antisymmetric and need not vanish. We retain a nonzero E8 root
triple with charges (-1,-1,2) and a nonzero component witness.
The root and tensor facts do not assert that its GLOBAL mode integral
is nonzero in the sourced hyperbolic problem.

For the E8 family channel, independently recover the unique A2
trilinear epsilon. The full family block's zero-sum triples should
all use distinct family weights (B1150 prior). Its color/flavour
factor is antisymmetric; the Weyl spin epsilon alone therefore
cannot turn that bracket tensor into a nonzero two-zero-form vertex.
There is no contradiction with B1150's algebraic result: that body
explicitly leaves the field-statistics question open.

Crucially, R33's added H-EFT uses a SYMMETRIC Y_a instead of the
parent bracket tensor. Then Y_a tensor epsilon_spin is antisymmetric
and nonzero. Check all ten blocks, so this parent-vertex restriction
does NOT retract the valid H-invariant Yukawa or R34's nonzero
Grassmann quartic. The putative composites (psi psi)_10_2 and its
charge-four scalar contraction have these same H charges. Their
existence as operators is not a positive kinetic term, a condensate,
a localized source solution or an auxiliary-field UV derivation.

## 4. The overlap operation also has to transfer

For internal one-form profiles v,w,a the pure-SYM cubic integrates
v wedge a wedge w, with the gauge bracket contraction. R36/R37
instead specified scalar-weighted metric contractions of v and w.
They are not interchangeable. On an oriented Euclidean chart take
v=w=dx and a=dz: the wedge vanishes while v dot w=1. Take v=dx,
w=dy and a=dz: the wedge is nonzero while v dot w=0. This tests
both directions, not a universal suppression claim. Complexification
does not change this tensor distinction.

Therefore the conditional E8 representation supply, if it passes,
does not by itself transfer the R33/R37 action into this parent.
A viable next construction must specify localized/composite origin
and matching, or derive a different interacting parent-mode action.
No whole-spectrum/phase/anomaly/end duty is discharged by this test.
