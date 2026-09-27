# Exact gauge centralizer and the role of the undeformed point

Authored before execution, 2026-09-27. Algebraic conclusions below are
conditional on the specified exact controls. The physical use additionally
depends on the prior authored harmonic construction and charged L2 proof,
the supplied metric/action, and the complete domain. No independent review
or machine-certified global PDE proof is claimed.

## 1. What the global H0 calculation establishes

The representation is the actual M6 restriction of E_t from either literal
monomial M2 seed, t!=0. The two permutation images and integer exponent
cocycles are fixed upstream. In sl5 the diagonal trace-free four and the
off-diagonal twenty are invariant submodules for every t. The diagonal
module has zero H0, checked on the actual M6 words.

For any coefficient V, H0 is the kernel of the stacked matrices rho(g)-I.
If this rectangular Laurent matrix has a full-column-rank minor, H0=0
wherever its determinant is nonzero. Clearing denominators by powers of
t adds only the excluded point zero. Factoring the minor over Q and
recomputing the whole matrix over each Q[t]/f covers all its complex roots,
including all embeddings. Spurious roots of a chosen minor cause no
false enhancement because full ranks are recomputed there. An omitted
factor would leave the classification incomplete.

Apply this independently to E, E*, W=Lambda2(E), W* and off. Add the
t-independent diagonal calculation. The full branching then gives

    h0(ad E8) = 24 + h0(off)
                    + 10(h0(E)+h0(E*)) + 5(h0(W)+h0(W*)).       (1)

The declared gauge sl5 is an included subalgebra of dimension 24. If the
other H0 spaces vanish, it is the WHOLE unbroken complex algebra, not just
a candidate contained in something larger. On the prior positive harmonic
background, the zero-form moment identity identifies D-flat sections with
simultaneously A-parallel and Higgs-annihilated sections. Thus the actual
compact stabilizer Lie algebra complexifies to (1). This uses the previous
complete-domain proof; it is not assumed for arbitrary nonsplit systems.

The producer reports possible extra exceptional factors without suppressing
them. Identification of every larger algebra must be made before a complete
all-t Lie-algebra conclusion is promoted.

## 2. The finite subgroup and the continuous SU4 at t=1

At t=1 every holonomy is an even real permutation on five letters. The
fixed vector is (1,1,1,1,1); its orthogonal complement U has complex
dimension four and determinant one, since the whole permutation has
determinant one. A compact change of basis identifies the image with a
subgroup of SU4 acting on 1+U.

The actual M6 image is generated and checked to have order 60. For each
permutation g, char_U(g)=number_of_fixed_letters(g)-1. Exact character
averages test that U has no invariants and is irreducible; Lambda2(U) has
no invariants; and End(U) has only its scalar invariant. Therefore the
finite subgroup fixes nothing in U, U*, Lambda2(U) or ad(U). These are
the only nontrivial SU4 coefficient slots in the branching below. Its
centralizer in the FULL E8 consequently equals the continuous SU4
centralizer. This is not the unjustified assertion that every finite
subgroup has the same centralizer as its containing continuous group.

## 3. Identify the entire root system and the spinors

Use the already-verified E8 roots in R8 and the structure A4 simple roots.
Take A3 to be the last three adjacent structure simple roots: in the
standard defining five this leaves the first line fixed. A root orthogonal
to all three commutes with all SU4 generators: in the simply laced system
adding/subtracting an orthogonal root has squared length four, not two,
and cannot be an E8 root. The commuting Cartan has dimension 8-3=5.

Enumerate every orthogonal root. Choose positives by a regular fixed
grading, extract indecomposable positive roots, and compare their Cartan
matrix with the standard D5 simple roots

    e1-e2, e2-e3, e3-e4, e4-e5, e4+e5.

Then compare the labels of ALL commuting roots with ALL signed-pair
vectors +/-ei +/-ej. This checks the full D5 root system rather than
inferring so(10) from 45 dimensions. The given gauge A4 roots must belong
to it. The compact real form inherited from compact E8 is so(10).

Restrict ALL 240 roots and all eight Cartan weights to D5 x A3. The
claimed product character is checked exactly as

    248 = (45,1) + (1,15) + (16,4) + (16*,4*) + (10,6).       (2)

The D5 vector weights are +/-ei. Its two spinor sets are the sixteen
half-integer vectors (+/-1/2,...,+/-1/2) of the two sign parities. The
producer checks these ENTIRE distinct sets against the coefficients in
(2), together with the vector and adjoint weight sets. Exchanging which
spinor is called 16 changes only convention. Replacing the conjugate
spinor by the same one in both terms must fail. No physical spinor or
chirality was inferred merely from a number 16.

The identity (2) and section 2 prove the t=1 compact centralizer. Global
quotients and disconnected parts of the stabilizer group are not derived.

## 4. Nontrivial fifth roots and the extra abelian direction

The previously sealed entrywise identities give, for zeta^5=1,

    E_j(zeta) = D_j [chi^k_j E_j(1)] D_j^-1,
    k_0=2, k_1=4,  chi_M2=(0,1,-1) mod 5.

Both k_j are nonzero mod 5. At a primitive fifth root these diagonal
conjugators are unitary up to an irrelevant scalar determinant adjustment.
Generate the actual M6 image in permutations x Z5 and verify it is the
full product of order 300. This checks that requiring commutation with
the image is the same as requiring commutation with both the finite
permutation image and the nontrivial fifth center, independently.

For an E8 root with structure A4 Dynkin labels s, that center acts by
zeta^(s1+2s2+3s3+4s4). On the D5 centralizer roots the last three labels
vanish. The remaining invariant roots are checked to be exactly the
twenty roots of the original gauge A4. All five commuting Cartan
directions remain; four belong to that A4 and one commutes with it.
Thus the compact Lie algebra there is su(5)+u(1), if these are the only
nontrivial exceptional roots found in section 1. The additional u(1) is
NOT identified with physical electromagnetism or a newly derived charge
normalization. Its global periodicity/quotient is not settled here.

## 5. Reorganize actual normalizable modes at t=1

The prior complete-domain theorem gives the degree-one L2 harmonic kernel
as ordinary interior H1 for every coefficient in (2). Compute n(1),
n(U), n(U*), n(Lambda2 U), n(End U) and n(End U*) directly from M6.
The canonical trace splitting over characteristic zero gives

    n(ad U) = n(End U)-n(1).

No fiber rank is interpreted as a number of copies. The actual
representation-valued degree-one spectrum at t=1 is therefore

    n(1) copies of 45,
    n(ad U) singlets,
    n(U) copies of 16 and n(U*) copies of 16*,
    n(Lambda2 U) copies of 10.                            (3)

These are complex internal one-form zero modes, with the prescribed
four-dimensional fermionic component from the chosen action. H0/H3
also supply the gauge multiplet and must not be relabeled as generations.
The producer compares (3)'s total dimension against a separate computation
using the original SU5 x SU5 branching and actual structure off/diagonal
coefficients. This is not a claim of an isolated low-energy theory.

## 6. Does the ACTUAL harmonic deformation enter those spinor slots?

At t=1 the flat unitary permutation connection preserves
P=ones(5)/5 and Q=I-P. For a real trace-free diagonal H,

    P H P = 0,
    H = Q H P + P H Q + Q H Q.

The first two blocks belong to U and U*, and QHQ is traceless on U.
They are orthogonal in the Hermitian trace norm. Direct calculation gives

    ||Q H P||^2 = ||P H Q||^2 = (1/5) tr(H^2),
    ||Q H Q||^2 = (3/5) tr(H^2).                          (4)

Check these as identities in FOUR independent diagonal coordinates, not
on one selected numerical vector. Also check equivariance under every
actual generator. Applying these parallel projections to the nonzero
diagonal beta commutes with the unitary flat differential and its adjoint.
Each component is therefore L2 harmonic and has a strictly positive norm
by (4). Its complete-domain harmonic class is nonzero and not gauge.

In (2) the U/U* coefficients occur in the spinor representations; the
structure off-blocks are their gauge-SU5 singlet components. The QHQ block
is in the D5 singlet coefficient ad U. Thus the very same exact nonlinear
family, if section 1 identifies its generic stabilizer as su5, passes
through genuine normalizable spinor-pair symmetry-breaking directions at
the enhanced point. This is more than an arbitrary representation label.

The statement concerns the combined tangent of an already-constructed
exact nonlinear family. It does NOT prove every spinor zero mode is
independently integrable, determine a vacuum expectation value, compute a
numerical kinetic coefficient or show quantum stability. Individual pieces
of beta need not give separate source-free nonlinear families. The two
conjugate directions are not three net chiral generations.

## 7. Scope of the physics

All compact algebras refer to the chosen regular E8 parent, metric and
harmonic family with trivial common line. The complete-domain result is
authored, not independently accepted analysis. The known neutral essential
spectrum at zero is retained. Even a correct GUT-like breaking branch does
not supply gravity, a four-dimensional mass gap, quantum consistency or
empirical predictions. The conditional positive should inform the next
chirality mechanism without being relabeled a completed TOE.
