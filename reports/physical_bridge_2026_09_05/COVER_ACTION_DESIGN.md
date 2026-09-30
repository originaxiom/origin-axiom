# Finite cover transport of an action and its limits

September 30, 2026. Path-local R58 pre-execution design and authored proof.
This is the first bounded test under the approved physics mission.

## Question and quantifier

Given a finite smooth covering p:Y->X and a rank-r complex bundle E on Y,
which products, norms and operator domains survive on F=p_*E? Does
replacing p_*End(E) by all End(F) merely change notation? The quantifier
is finite covers with the explicitly transported data below, not all
generated relations or all physical theories. No M6 index is recomputed.

Prior: direct image should preserve sheetwise local dynamics with its
transported metric and domain. It should not identify the induced
endomorphism algebra with the entire enlarged matrix algebra, select
a boundary condition, or preserve a quartic after replacing its sum by
the square of a sum. These distinctions could fail in the finite controls;
an implementation failure must be retained and separately diagnosed.

## Prior work and scope

This serves the registered PB-HANDOFF-M6 and PB-TRANSITIONS duties, with
PB-BOUNDARY retained. The owner-approved September 30 priority supersedes
automatic continuation of the canonical tensor calculation.

The full B1384 findings and handoff_checks.py producer were read at
93c7b428. Its induce function is block monomial on the three cosets.
Its Shapiro/Mackey and T^3 identities are prior results, not discoveries
of this test. Its cohomology and root computations are not imported.
Our FINITE_TWIST_PROOF already requires boundary-map compatibility.
The parallel checkout at 490d77c4 already distinguishes geometric deck
descent from fibre holonomy and gives pulled-back L2 norm scaling.
Its coupled-boundary DECK_PROOF also warns that exterior square must
precede regular-representation expansion. These are retained, not rerun.

Prior searches: LAW_MAP, OPEN_LEADS, arc-verdict bodies and selected
producer/report bodies for Shapiro, Mackey, direct image/direct-image,
induction with action/kinetic/bracket, plus the corresponding atlas card
and already_banked query. The local atlas is old; its null is not an
absence finding. The local kill graph has no incoming B1384 entry;
its older induction-related rows do not certify a new closure. All-head
fetch returned no new incoming commits. No all-history absence or
mathematical novelty claim is made.

The standard sheaf terminology was checked against Stacks tags
[0095](https://stacks.math.columbia.edu/tag/0095) and
[0FRT](https://stacks.math.columbia.edu/tag/0FRT), accessed September 30.
They define direct image and differential transport, not the physical
theorem here. The smooth metric/domain proof below is explicit; it is
not imported from algebraic geometry by analogy.

## Transport with the data retained

Assume p has finite degree n, X has a smooth Riemannian metric g, Y has
p^*g, and E has a positive Hermitian metric h and smooth connection.
An internal Riemannian calculation is not a derived Lorentzian spacetime.
On an evenly covered U, write

    F_x = direct sum over y in p^-1(x) of E_y,
    H_x = direct sum of h_y,
    A = p_*End(E) -> End(F),   (a_1,...,a_n) -> diag(a_1,...,a_n).

Sheet transitions permute the blocks and change frames within them.
Therefore A is a well-defined algebra subbundle. The diagonal inclusion
preserves products, graded brackets on forms, metric adjoints and the
sum-of-traces pairing. The induced connection preserves A. These
identities hold in each evenly covered chart and agree on overlaps.

Section transport U:Omega(Y;E)->Omega(X;F) commutes with the differential
of the transported connection. A finite covering is proper, so it also
identifies compactly supported smooth sections. Sheetwise integration
gives ||Uu||_L2(X,F)^2=||u||_L2(Y,E)^2 with no extra factor n. The
factor n applies instead to pulling back a single downstairs section,
as the prior deck-descent proof already records.

By the L2 identity, formal adjoints and the associated first-order
operators intertwine. Closing the compactly supported graph gives
unitary transport of minimal domains. The distributional test-function
definition gives transport of maximal domains. Any other chosen closed
domain transfers by U, but is not thereby selected. With genuine boundary
or source ends, the Green pairing and end terms transfer only with the
same transported data. An independently chosen metric or extension is
outside this assertion. No spectral gap, Fredholm property or harmonic
background existence follows just from this transport.

For an A-valued connection perturbation a, the curvature
F_0+d_0 a+a wedge a stays in A and transports sheetwise. Single-trace
polynomial densities, including curvature norm squared and appropriate
cubic/commutator vertices, integrate to exactly the upstairs sum. The
same holds for a supplied matter action with its transported invariant
tensors. Equality of these functionals with the same admissible fields
and variations gives equality of their classical stationarity problems.
This establishes a conditional action-level connection, not the origin
or quantum consistency of the supplied action.

## Where an enlarged theory enters

At a point, rank(A)=n*r^2 whereas rank(End(F))=n^2*r^2. Off-diagonal
Hom(E_i,E_j), i!=j, are not fields of the original sheetwise algebra.
In the n=3,r=2 comparator these dimensions are 12 and 36. These are
complex algebra-fibre dimensions, not physical particles or generations.
Block-traceless algebras similarly have dimensions 9 versus 35 for
sl2^3 inside sl6; block trace constraints must be specified separately.

Projection from End(F) onto its block diagonal is not a Lie homomorphism:
take E_02 and E_20 in a 6x6 model. Both project to zero, while their
commutator E_00-E_22 has a nonzero block-diagonal projection. Full End(F)
gauge transformations need not preserve A. Enlarging to that parent may
be a legitimate new model or allow a classical truncation, but is not
equivalence to the original field content, especially at quantum level.
No SL5/E8 embedding or all-parent obstruction is inferred.

Even within the original coefficient transport, a quartic needs its
tensor retained. Put x_i=||u_i||^2>=0. Then

    upstairs local quartic = sum_i x_i^2,
    naive downstairs norm quartic = (sum_i x_i)^2.

Their difference is 2 sum_(i<j) x_i*x_j, which is generally nonzero.
The inequalities sum x_i^2 <= (sum x_i)^2 <= n sum x_i^2 show that the
L4 domains coincide as sets with equivalent norms, not equal quartic
actions. A faithful transport keeps the sheet-resolved tensor; the
sheet projectors may be permuted globally, but their summed tensor is
well defined. This is not a claim that physical flavour couplings vanish.

## Boundary choice remains a separate law

The finite boundary comparator uses three identical interval fibres and
the Green form on (value,normal derivative). Dirichlet and Neumann
subspaces are distinct maximal isotropic subspaces, each stable under
cyclic sheet permutation. Thus these supplied data and this symmetry
do not select one. This is a comparator, not a theorem that both domains
are admissible on the actual nonsplit M6 cusp. That actual choice needs
its own end action and analytic admissibility test.

## Sealed finite checks and opposite controls

The producer uses exact SymPy matrices/polynomials, no sampled manifold
census or empirical constants. Check product/bracket/trace transport,
positive Hermitian norms with a nontrivial Gram matrix, a covariant
derivative, integrated kinetic density and its first variation. Check
a block-monomial lift with nontrivial unipotent cube without mistaking
it for a geometric deck operator. Transform the metric with the frame;
leaving it fixed must fail the chosen control.

Opposite controls detect the extra off-diagonal generators, non-Lie
projection and changed quartic. Exact boundary matrices distinguish the
two invariant Lagrangian subspaces. These finite safeguards do not prove
the global functional analysis; that remains authored analysis above.

Commit and push the operational contract, this design, input manifest,
producer and tests; confirm the remote seal before importing or executing
new science. Run the native producer and the fixed selection of the nine
legacy uniqueness tests, seven R57 tests and new R58 tests. Keep HEAD and
tree fixed during runs. Record all first outputs and failures.

Allowed outcomes are verified or failed conditional transport controls,
with individually stated limits. Forbidden promotions: derived physical
action, selected end law, new M6 index, three physical generations,
physical chirality, whole architecture completeness or completed TOE.
