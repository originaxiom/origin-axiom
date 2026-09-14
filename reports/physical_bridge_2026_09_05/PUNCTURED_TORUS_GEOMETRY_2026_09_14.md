# Punctured-torus geometry and the physical bridge

The geometric literature supplies a useful reconstruction framework, but
it does not yet supply the missing fermion/source action. The strongest
immediate improvement is a precise separation of the surface, its fibre
cover, the finite-volume quotient, and the physical operator on that
quotient. This preserves the Jorgensen selection positive and the existing
conditional chiral sector without combining incompatible boundary problems.

## The literature and its domain

Minsky's Theorem A determines a marked discrete faithful punctured-torus
surface representation in PSL(2,C) from its ordered end invariants.
Its source group is free of rank two, with parabolic commutator. These
are not arbitrary two-generator three-manifold groups. Section 3 removes
the main cusp before describing the two ends. Section 7 gives commutator
trace -2. Theorem B's inverse parameterization is continuous, but the
end-invariant map itself need not be. The Pivot Theorem and model
manifold construction provide coarse geometric control, not numerical
fermion masses or boundary conditions. Its section 9.5 figure-eight is
a curve used in a general argument, not a uniqueness theorem for the
figure-eight knot.[^1]

Thurston's mapping-torus construction provides the relevant connection:
use the stable/unstable laminations of a pseudo-Anosov monodromy, obtain
the limiting surface representation, then quotient by the isometry
implementing the monodromy. His introduction explicitly credits
Jorgensen's pioneering examples.[^2] The quoted historical attribution
is therefore supported, independently of this repository.

The bibliography needs a correction: *On pairs of once-punctured tori*
was printed in **2003**, following a circa-1975 manuscript; 2001 is the
workshop year. Cambridge lists pages 183-208 and online publication in
2009. The 1977 Annals article is correctly identified as volume 106,
pages 61-72.[^3][^4] The complete 1977 article is available in twelve
supplied page images. The 2003 chapter remains a bibliography/summary
source only: publisher downloads returned HTML and an indexed book
mirror returned 404. That access failure is not a mathematical negative.

## Jorgensen's compact construction and the peripheral relation

The 1977 paper proves existence of compact hyperbolic three-manifolds
fibering over the circle. Its initial examples are orbifolds: the fibre
is a torus with one cone point of order n, for integer n >= 2. Sections
6-8 give matrices, face pairings and the presentations

    G_n = <X,Y | [X,Y]^n = 1>,
    T X T^-1 = X Y^-1,    T (Y X) T^-1 = Y.

The commutator has trace -2 cos(pi/n), and G_n is the fibre subgroup
of the infinite cyclic extension. Section 9 uses a torsion-free finite
index subgroup and Stallings' fibration theorem to obtain smooth compact
examples. This is an explicit orbifold-to-manifold construction, not
an assertion that these finite-n examples are the cusped m004.[^4]

Here is the elementary algebraic consequence relevant to the record.
The second conjugation equation implies

    theta(X) = X Y^-1,    theta(Y) = Y^2 X^-1.

On column exponent vectors in the ordered basis ([X],[Y]), its matrix
is A0=[[1,-1],[-1,2]]. With B=[[0,1],[-1,0]], direct multiplication
gives B A0 B^-1=[[2,1],[1,1]]. Thus the familiar characteristic polynomial
t^2-3t+1 appears in this family as well. This comparison is an
abelianized return-map calculation; it does not identify the full groups.
In particular the finite-order commutator relation is invisible in
abelianization, since every commutator already has exponent vector zero.
The same integer return data therefore do not by themselves choose the
peripheral relation. This is not a refutation of additional axioms or
of the separately established Jorgensen extremum for a complete cusp.

One must also resist substituting n=infinity into a trace and calling
the result a verified cusp. In the paper's diagonal normalization,
K=diag(-lambda^2,-lambda^-2), with lambda=exp(pi*i/(2n)), tends to -I.
Trace -2 alone does not distinguish that central matrix from a nontrivial
parabolic matrix. A claimed cusp limit requires a suitable normalization
and convergence of the representation and geometry, not just the trace.
No such limit or identification with a particular filling is certified here.

Two reception safeguards are especially important. Section 11's suggestion
that essentially one solution is discrete is a tentative remark, not a
proved uniqueness theorem. Its contrast with “Kleinian” normal subgroups
also must not be transplanted into the modern broad meaning of that term:
the paper's own construction supplies a finitely generated infinite-index
normal fibre subgroup. The internal context rules out reading that
historical sentence as a general obstruction to hyperbolic fibre groups.[^4]

The constructive benefit is a concrete place to investigate a return map,
a cone/core relation and a smooth finite cover together. The cost must
stay visible: passing to a smooth finite cover changes the fibre, and
removing a branch locus changes the completeness problem. Neither operation
already specifies a fermion action, its domain, or the fate of partner modes.
These are comparison geometries for the physical programme, not a new
chiral mechanism or a reason to abandon the existing source calculation.

## Thurston's limits and the geometry of a proposed core

Thurston's complete paper supplies more than the mapping-torus existence
argument. Theorem 3.3 bounds lengths on an efficiently pleated surface
using an alternation term and a lower bound on its closed pleating leaves.
Pages 15-16 explain why short folds and accidental parabolics defeat an
unqualified version of that estimate. Theorems 4.1 and 6.2 distinguish a
binding-pair double limit from convergence restricted to subsurfaces.[^2]

Section 7 is directly relevant to any proposed surgery/limit comparison.
Under explicit hypotheses on a locally finite collection C of level curves,
Theorem 7.2 constructs geometric limits homeomorphic to S x R minus C.
New rank-two cusps occur; infinite C gives an infinitely generated limit
group. The proof separately establishes convergence, faithfulness, the
absence of an extra covering, and the claimed homeomorphism. None of
those conclusions is obtained merely by inspecting limiting traces.[^2]

The physical inference is methodological and limited. A source-end limit
must track the actual space, coefficient bundle and operator domain,
not just a convenient finite list of holonomies. A change in geometry
may open a route, or invalidate a transferred index; the sign cannot be
decided from the geometric theorem alone. This motivates keeping the
finite-width problem and the complete-cusp limit separate until their
mode matching and kinetic norms have been established.

## The three structures that must stay separate

For a once-punctured torus S and monodromy f, the following is the
appropriate reconstruction, using the mapping-torus construction.[^2]

| Structure | Algebra | Required extra information |
|---|---|---|
| Integral fibre record | H1(S;Z)=Z^2 with f_* | Ordered basis and identification with the programme's record variables |
| Fibre subgroup and its cover | pi1(S)=F2; cover topologically S x R | Geometric representation and marking |
| Mapping-torus quotient | pi1(M_f)=F2 semidirect Z | The actual return automorphism, not just its invariant directions |

The exact sequence 1 -> F2 -> pi1(M_f) -> Z -> 1 follows by pulling
the fibration back to the universal cover of the circle. It splits after
choosing a lift of its generator; changing that lift changes the fibre
automorphism by an inner automorphism. Abelianizing F2 produces the
integer lattice. It does not identify the lattice with the original
nonabelian group. This is a concrete mathematical route between the
types, not an automatic discharge of the programme's axioms.

Likewise the commutator of a fibre basis and the commutator of a
meridian generating pair must not be interchanged. The preceding
[Jorgensen audit](JORGENSEN_SOURCE_AUDIT_2026_09_13.md) already records
the meridian value 2+u^2 and the different fibre value -2. The literature
review confirms the distinction; it does not discover a contradiction
between them or produce a new J-number computation.

## A reconstruction still needs the quotient period

Here is an elementary consequence of the mapping-torus description,
not a new classification theorem. For every positive integer n,
M_(f^n) is an n-sheeted cyclic cover of M_f. Both unwind to the same
fibre cover. The invariant projective directions of f and f^n agree,
although their stretch factors differ by the nth power. The pulled-back
hyperbolic volume of the finite quotient is multiplied by n.

Thus specifying the two limiting directions alone cannot distinguish
the base return from its positive iterates. One must also specify the
quotient subgroup of the deck action. This is a retained ambiguity in
that particular reconstruction, not a refutation of a separate
primitive-period or Jorgensen selection criterion.

For the familiar matrix A=[[2,1],[1,1]], its characteristic polynomial
is t^2-3t+1. With phi=(1+sqrt(5))/2, the eigenvalues are phi^2 and
phi^-2, with eigenlines [phi:1] and [-phi^-1:1]. Every positive power
has those same lines. These statements follow by direct substitution
using phi^2=phi+1. They are an elementary illustration, not a new
computer experiment. To use slopes rather than lines, the convention
and ordering must be written down; a sign change of slope convention
is not a change in the manifold.

This is useful for the programme's journey: golden arithmetic can
describe the invariant directions and return dynamics without those
directions alone fixing which quotient, vacuum or physical spectrum
is being used. A selector for the original object and a later choice
of sourced/filling sector are different obligations.

## Consequences for chirality and normalization

The physical calculation remains on its specified space and Hilbert
domain. There are two simple checks that any proposed transfer through
the fibre cover must pass.

First, let p:N->M be an infinite cyclic Riemannian cover and let a
nonzero field on M have finite positive kinetic norm K on one
fundamental region. For a pulled-back positive kinetic density, or a
field with unitary deck-equivariant transition, every translated region
has the same norm. Consequently

    norm_N^2 = sum over j in Z of K = infinity.

This does not make the original finite-volume field unphysical. It
means its lift is not an ordinary L2 state on the whole cover. Working
per fundamental region or with an appropriate Bloch decomposition is
different from imposing square-integrability on the entire cover.
A nonperiodic localized field is another legitimate possibility, but
then its source and its descent or failure to descend must be explained.

Second, if a quotient is cut along a fibre, the two new faces are an
artificial interface. For a compatible Dirac-type action the Green
boundary pairing has opposite normal signs there. With the actual
spin/gauge/geometric gluing U and matching traces, the two contributions
cancel. Independent chiral boundary conditions on the two faces do
not follow from the quotient: they define an altered problem. The
needed spin structure and U have not been derived for a new physical
model in this review.

Neither check says that chirality is impossible. Both prevent an index
or a finite norm computed on one domain from being silently transferred
to another. In particular they do not retract the following earlier
results on their own hypotheses:

- [R19](HOLONOMY_SPECTRUM.md): the three/zero charged kernel for the
  strong singular-source maximal domain and generic unitary character;
  its trivial and exceptional-character cases remain recorded.
- [R26](INDEX_STABILITY.md): stability within the stated fixed-domain
  class. Resolving a deleted source core is not automatically such a
  perturbation.
- [R29](DEFECT_GAUGE.md): a declared coupled finite-width bosonic source
  on compact truncations and the separately scoped shrinking-line
  gauge result. It has not yet supplied its complete fermionic sector.

There is a further concrete transfer constraint: the R19 witness uses
the **two-cusped m202**, not the bare m004 fibre cover. A bundle with a
once-punctured-torus fibre has one boundary-circle orbit, hence one
torus cusp. Directly substituting the punctured-torus model for m202
is therefore unjustified. An explicit covering, different fibre or
other geometric construction would be needed; no such transfer is
asserted here.

## What the repository search establishes

The [history receipt](PUNCTURED_TORUS_HISTORY_2026_09_14.json) includes
all unique blobs reachable from the listed fetched/local heads, tags
and two retained historical tips: 4,361 commits and 28,304 blobs. It
includes deleted versions and binary bytes. This is the pinned intake
before paper-review B1404, not a claim about branches after that new
publication. The quantities below count
**distinct matching blob versions**, not papers, occurrences, current
files or completed derivations.

| Search term | Matching blobs |
|---|---:|
| Minsky / Marden / Bromberg / veering / ending lamination | 0 each |
| Maskit | 1 |
| Bers, whole word | 20 |
| quasi-Fuchsian spelling pattern | 324 |
| end-invariant pattern | 8 |
| Thurston-norm pattern | 2 |
| fibered-face pattern | 5 |

These results do not reproduce or endorse the forwarded counts, whose
population was different or unspecified. Nor does a regex zero prove
that equivalent mathematics is absent under another name. The single
Maskit hit is a Gilman--Maskit search lead in a historical theorem
registry, not evidence that Minsky's classification was already used.
Many quasi-Fuchsian hits are successive versions of the same lead.
The fibre-face regex does not cover the British spelling `fibred`;
the displayed count must not be used to assert absence of that wording.

The substantive existing question is L71. The outside bench's
[memo 214](https://github.com/originaxiom/origin-axiom/blob/d2d70b692dc473f4dbffd57a62fa400567696ee2/outside_bench/memos/THE_PERIPHERAL_ROUTE_IS_EXHAUSTED.md)
and its cusp-slope preregistration explicitly ask about the geometric
meaning of higher-representation deformations. Their reported
peripheral computations are not independently rerun here. The relevant
restriction is that a deformation into E6 that leaves the principal
SL(2,C) is not thereby a point of the PSL(2,C) surface-character space.
The new literature cannot be substituted for that missing identification.
Thus “the geometry is absent” overstates what the search found.

The [B1400 intake](https://github.com/originaxiom/origin-axiom/blob/d08d1f9834f2e5ceb92ff6e33c2ea1f466446a80/frontier/B1400_the_six_sweeps_intaken/FINDINGS.md)
also records earlier branch-visibility corrections. Its numerical
census results are received, not recertified here. Fetching is necessary
for visibility; reading names or finding a file is not verification of
its theorem, producer or claimed physical consequence.

### The later B1404 intake

At paper-review `31cfd0325d947f797fcd480d2acc32ed526e2913`,
[B1404](https://github.com/originaxiom/origin-axiom/blob/31cfd0325d947f797fcd480d2acc32ed526e2913/frontier/B1404_the_family_has_a_name/FINDINGS.md)
now explicitly introduces Minsky. Its distinction between the fibre
group and finite quotient, and its warning about marking-dependent
coordinates, are useful. The earlier name-search receipt must not be
used to claim this material remains absent. Its [producer](https://github.com/originaxiom/origin-axiom/blob/31cfd0325d947f797fcd480d2acc32ed526e2913/frontier/B1404_the_family_has_a_name/b1404_the_family.py)
was inspected, not rerun; its numerical and census pass counts are not
new certificates of this review.

Three stronger implications need to remain separate from that positive.

1. The Markov/trace equation is a necessary locus, not by itself all
   of Minsky's hypotheses: freeness, discreteness and faithfulness are
   still required. Checking a trace triple does not establish them.
2. The ordered fixed-point orbit is not equivalent to the conjugacy
   class or dilatation of a specified return. The positive-power
   example above is an explicit counterexample to that equivalence:
   A and A^2 share both end directions, while their traces are 3 and
   7 and their dilatations differ. B1404's sentence recovering the
   quotient by a Z-action is correct; its stronger equivalence wording
   must not discard that same action.
3. A nonparabolic commutator of one displayed generating pair does
   not alone exclude all other markings. There is a simpler group-level
   distinction here: the mapping-torus abelianization is
   Z direct-sum coker(A-I)=Z, since det(A-I)=-1, whereas F2 abelianizes
   to Z^2. This checks the distinction without a scan over pairs and
   without mistaking a numerical holonomy test for a universal proof.

These are source-level and elementary logical checks, not a rerun of
B1404 or a rejection of its principal literature connection. The
physical source problem remains the same unfinished task.

## Strategy and completion tests

The priority remains one source/end action whose bosons, fermions,
anomalies and normalized interactions all belong to the same model.
The literature changes the checks imposed on that work; it does not
replace it with another collection of geometric matches.

1. **Finish the typed reconstruction.** Exhibit the actual fibre
   embedding, return word, peripheral identification and orientation
   in the corpus's presentation. Compare positive return powers as a
   control. Use Jorgensen's finite-n family to keep the peripheral
   relation distinct from the return matrix; certify any proposed
   cusp limit or filling identification separately. Distinguish selecting
   a geometric representation from deriving why the physical action selects it.
2. **Resolve the core at the fermionic level.** Specify an admissible
   extension of R29's action, its kinetic inner product, reality/charge
   structure and variational interface conditions. Derive the domain;
   do not choose it because it yields three modes.
3. **Track core gluing and the outer end separately.** A planned
   diagnostic compares the source-relative complex (Q,N_sources) with
   the core-filled complex Q for an extending flat coefficient system.
   Track the connecting maps and possible core partners, then address
   the complete cusp limit. A compact Euler characteristic alone is
   not a physical spectrum. This diagnostic has not been executed as
   a new round, and is not yet the full fermion action.
4. **Calculate the full spectrum and currents together.** Test whether
   any opposite-chirality modes remain, become massive, or fail to be
   normalizable in the actual model. Compute their gauge overlaps and
   the anomaly including every retained sector. The tested free wall's
   non-decoupling in [R25](BOUNDARY_WALL.md) remains a control, not a
   universal no-go for all defects.
5. **Only then claim a physical milestone.** A controlled chiral 4D EFT
   needs a separation from unwanted cusp/core modes and consistent
   interactions. The full [mission roadmap](MISSION_ROADMAP_2026_09_13.md)
   additionally requires quantitative discrimination and same-theory
   gravity/quantum/cosmological completion.

The current verdict is **useful geometric clarification and new
transfer checks, not a completed chirality mechanism or TOE**. The
conditional positive survives; its physical completion remains a
specific calculation, not an absence assertion about the whole corpus.

## Sources

[^1]: Yair N. Minsky, [*The classification of punctured-torus groups*](https://arxiv.org/pdf/math/9807001v3), Annals of Mathematics 149 (1999), 559-626; Theorems A/B, sections 3, 4, 7, 9-12.
[^2]: William P. Thurston, [*Hyperbolic Structures on 3-manifolds, II: Surface groups and 3-manifolds which fiber over the circle*](https://arxiv.org/pdf/math/9801045v1), 1986 preprint/1998 eprint; introduction, Theorems 2.5, 3.3, 4.1, 6.2, 7.2 and section 5. Supplied file: `9801045v1.pdf`, all 32 pages.
[^3]: Troels Jorgensen, [*On pairs of once-punctured tori*, publisher record](https://doi.org/10.1017/CBO9780511542817.010), Cambridge University Press, 2003. Bibliography and publisher summary only; full-text reading remains open.
[^4]: Troels Jorgensen, [*Compact 3-manifolds of constant negative curvature fibering over the circle*, publisher record](https://annals.math.princeton.edu/1977/106-1/p04), Annals of Mathematics 106 (1977), 61-72; sections 1, 6-9, 11. Full text supplied as twelve screenshots dated 2026-09-14, times 07.33.06 through 07.35.01 in chronological order; page/file/hash mapping in [source custody](PUNCTURED_TORUS_SUPPLIED_SOURCES_2026_09_14.json). The linked publisher page provides bibliography, not the inspected full text.
