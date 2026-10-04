# A graded boundary completion with nonzero brackets

This is an authored algebraic argument, not an independent analytic
acceptance or a construction of a physical vacuum.

Let H = H0 + H1 + H2 be a finite cyclic graded Lie algebra with perfect
pairing between H0 and H2 and a nondegenerate skew pairing on H1. The
example in scope is cohomology of an oriented boundary torus with the
adjoint local system and invariant trace form. Let L be maximal isotropic
in H1 and let k be a Lie subalgebra of H0 such that [k,L] is contained in L.
Then set A0 = k, A1 = L, A2 = ann(k).

The pairing vanishes on A: the degree-zero and degree-two spaces annihilate
each other, and L is isotropic. Perfection gives dim ann(k) = dim H2 - dim k;
together with 2 dim L = dim H1 this gives half the total dimension.
Thus A is graded Lagrangian in this finite sense.

Closure in degrees zero and zero/one is the assumption on k. For z,w in k
and a in ann(k), invariance gives <w,[z,a]> = <[w,z],a> = 0 up to a harmless
convention sign. Hence [k,ann(k)] is in ann(k). For u,v in L and z in k,
cyclicity gives <z,[u,v]> = <[z,u],v> = 0. Thus [L,L] is in ann(k). Higher
degrees vanish. Nothing requires [L,L] itself to vanish.

## Application being checked

Use the supplied sl5 gauge times sl5 structure embedding in E8. Its
boundary cohomology is the direct sum of the two adjoints and the two
charged dual pairs. Set k to the constant gauge sl5, not the partial
charged parameter kernel which failed closure in the previous packet.
On gauge H1 use sl5 times one common torus form line. On structure H1
use the global restriction image. On each charged pair use the earlier
paired complements, including all gauge multiplicities. The direct sum
is maximal isotropic if the stated component tests pass. The gauge sl5
preserves it by the tensor-factor action, so the lemma applies to the
full parent cohomology. This does not assert maximality of k.

The neutral computation is needed: End0(E) is self-dual by trace, not
by a choice of unitary holonomy. If S is its trace Gram matrix, its
torus pairing in the current cochain coordinates is
J_trace = J_group diag(S,S). Invariance P^T S P = S and Q^T S Q = S
identifies the literal dual. Test descent, skew symmetry and perfection
on closed cocycles modulo exacts, not on arbitrary cochains.

Charged H0 is excluded and charged H2 retained in this chosen A. The
linear mapping-cone spectrum is therefore the already computed reversed
completion, not the earlier favorable endpoint convention. This is a
cost of this concrete construction, not a theorem excluding other k,
boundary fields, polarizations or analytic laws.

## Limits of the construction

A subalgebra of cohomology need not lift to a smooth differential graded
boundary subalgebra; homotopy transfer may generate higher operations.
Gauge parallel zero modes are not all local gauge transformations.
Hermitian reality, supersymmetry, normal derivatives, ellipticity,
Fredholmness and finite norms have not been supplied by this lemma.
In particular, cochain ghost and antifield endpoints may not be identified
with a physical charged fermion operator without a separate map.

The boundary-field perspective is consistent with the distinction in
[Cattaneo, Mnev and Reshetikhin, section 3.7](https://arxiv.org/html/1201.0290v3#S3.SS7)
between an isotropic choice and a boundary condition compatible with the
cohomological vector field. That section was read directly. It motivates
testing closure; it does not prove that this finite construction is a
boundary condition for the supplied seven-dimensional physical action.
