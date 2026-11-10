# Pre-banking review of AGY P-753 at da5c71251

2026-11-10. Exact source
`da5c71251194ad9866264338d4bd1f99f082ba4c`, against main
`30dd1fea7086ce5faad1a4c5ac9829baab27b4dd`. Decision
`REVISE_BEFORE_BANKING_WP_2_2_AND_WP_3_2_AS_COMPLETE`.

This review personally read the entire new producer, referee script,
tests, relay and tracked receipts. The associated physical-source
passages and main's actual work-package definitions were checked.
Metadata and hash checks ran. Scientific code, imports, collection and
tests remain unrun by this reviewer. HAND_COUNTERCHECKS.md supplies
exact hand derivations and rejecting examples.

The physical reviewer authored some upstream dependencies and the new
repair arguments. Keep that shared authorship visible for acceptance.
The new hand proofs require their own nonauthoring scrutiny before
adoption. No main content or AGY assignment is changed by this review.

## Supported mathematical content

1. The weave cocycle representation splits into two conjugate triplets.
   An explicit cocycle basis in the hand supplement yields the packet's
   monomial TL,TR exactly. Their image has order96, center4 and
   projective order24 by an exact diagonal-kernel argument.
2. An explicit orthogonal intertwiner proves
   T=chi3 tensor Sym2(conjugate Weil2). The untwisted square has
   order48. An exact central-sheet argument excludes every even twist
   and, more generally, the symmetric square of every honest
   two-dimensional Mp2Z representation. This corrects main's current
   unqualified untwisted-square statement in WP-3.2.
3. The order-two E8 central identity relating a change of h4 sign
   to simultaneous core spinor-sign changes survives on all roots and
   the Cartan. It identifies duplicate descriptions of holonomies.
   The singlet/triplet relative sign also survives. Changing h4 sign
   cannot make both those channels trivial simultaneously.
4. The binary-octahedral axis stabilizer and parity-character stabilizer
   have a natural common order16 preimage and index3. This is compatible
   with the supplied balanced carrier's three-branch orbit. The new
   code exhibits candidate compensators for its generators on the
   five E8 summands. A full physical action still needs its complete
   geometric, spin, metric and operator transport.
5. The meromorphic section spaces and their pole subspaces have the
   stated invariant-line structure under the specified theta subgroup.
   The existing conditional pure-slot kernel theorem can retain its
   2+1 invariant decomposition when its physical transport hypotheses
   hold. These are scoped positives to preserve.

The independently calculated order96 and explicit odd-twist relation
are substantial mathematical clarification. No observed SM parameter
has been derived by this packet. Its field/family identification remains
subject to the following findings.

## F1. The active one-form induced matrices contradict their character

Severity HIGH for the asserted exact physical induced module.
Producer lines989-1001 and relay section4 assign L^2 -> -1 and
S_theta -> +1 to the active one-form line. But the supplied matrices
give S_theta b=-b for the branch b=(0,1,0), which S_theta fixes.
The calculation is shown in HAND_COUNTERCHECKS section3.

The tests check the group order and braid relation, omitting this
stabilizer character. Multiplying both generators by-1 repairs the
printed character while preserving the order24 comparison. Reconstruct
the induced action from actual coset representatives and transported
line data, then add tests of its stabilizer character and central sheet.

There is also an exact constructive relation with the weave triplet.
For the displayed matrices T=chi21 tensor A. For the character-repaired
pair T=chi9 tensor A'. Thus their projective actions coincide. Derive
the scalar line from the actual field/spin transport before using the
finite image orders to close the physical join. Arbitrarily inserting
that line would leave an input. Declaring it unavailable from the bare
slot name would leave an unproved exclusion.

## F2. The physical-kernel and induced-action joins remain unproved here

Severity BLOCKING for closing physical WP-3.2.

Producer lines869-889 fill the off-slot blocks with zero and test those
same blocks. They do not construct or transport actual kernel modes.
The earlier physical pure-slot theorem gives a conditional reason for
the decomposition. Its hypotheses and complete-domain equivariance
must accompany the physical conclusion.

Lines891-955 calculate finite Koszul holonomies and then set mode counts
to2 plus a trivial-character rank. This retains the earlier analytic
kernel theorem as a dependency. The new referee's elliptic contours
test local Laurent coefficients and one swap. They never implement
the physical Hodge map, normalize global modes or check the domain.

In particular the source identifies the2 modes with H1(S^-3 L)
through its trace-dual degree-two Hodge partner. The relay substitutes
H0(O(2p)) or H0(chi11(2p)) with a dz factor. For a representation
comparison one must transport the dualization, spin line, geometry,
norm and modular scalar factors too. Fibre dimensions alone cannot
specify that equivariant identification.

Lines989-1012 insert the two induced3x3 matrix pairs. They do not derive
their stabilizer characters from a restriction to an actual normalized
kernel or compute the full E_theta relation and compensation cocycle.
On a family over tau, specify whether the comparison concerns an
equivariant bundle, a chosen flat transport or a Berry connection.
Changing tau-dependent trivializations is more general than the
constant unitary conjugations used by the tests.

There is also a dimension-accounting duty. Inducing a full3-dimensional
per-branch coefficient space across an index3 orbit gives dimension9.
The source's displayed3x3 examples require their embeddings into that
whole space, including both one-form flag lines. The pure-permutation
comparison is not accompanied by an actual full-kernel map identifying
each missing channel. Any physical quotient or selected subspace needs
its own action and observable map.

The relay's proposal to remove WP-3.1 from WP-3.2 is justified for an
abstract finite-module comparison. The same removal does not establish
the physical kernel representation. Keep separate algebraic and physical
nodes, with the latter retaining the operator/domain dependency. A new
physical realization could change the proposed field join, so this
packet cannot close all generation routes by exclusion.

## F3. Two purported irreducibility tests do not test irreducibility

Severity HIGH for the exact zero-mode decomposition claims.

At producer lines1019-1029 the flag/splitting boolean is one numerical
Szego equality, and the vector-doublet irreducibility boolean is only
the S2/S4 swap equality. A swap with an identity second generator has
two invariant eigenlines and passes that swap test. Compute the actual
second generator on the gauge-compensated channels and its joint
commutant or invariant subspaces.

An invariant flag alone does not imply complete reducibility under
an infinite group. The explicit section transformation identities in
the hand supplement can preserve the claimed holomorphic splitting
on those particular spaces. Their transfer to physical harmonic
representatives remains the F2 duty. Preserve the supported conditional
2+1 decomposition while repairing the stronger claims and tests.

## F4. Covariance has not selected the remaining physical data

Severity BLOCKING for the claimed completed input-reduction table.

The unique modular-fixed odd torus spin class and the trivial flat
point are valid fixed-point statements. The ledger's separate demand
to derive the physical spin/lift and state selection persists.
E-equivariance permits sums or families over other orbits as well.
The packet itself uses precisely that procedure for the balanced
background's three branches. The same reasoning must be considered
for the permuted even spin classes and flat-character alternatives.

With only E_theta imposed on one branch, chi11 is itself a nontrivial
fixed2-torsion point. On the U1 character torus before additional
candidate-specific identifications, invariance under L^2 gives2u=0,
and S gives u=v with2u=0, leaving both0 and(1/2,1/2). A selection
argument must account for those points or exhibit their actual gauge
identification with the other sign data. Branch covariance alone
does not establish a unique trivial-character description.

The sign identity supports the simultaneous relabelling
(h4 sign,sa,sb) -> (-h4 sign,-sa,-sb). It removes a duplicated
binary label if the candidate parameterization counted it twice.
It leaves the remaining simultaneous sign/background classes to
classify and select with all measuring/charge conventions retained.
The earlier coherent-phase and outer-conjugacy results must be reused.
Do not count their redundancy again as a new foundational payment.

The full datum E:L06 also contains the supplied D5+A3 split, charge
readout and coherent-phase alternatives. The new builder accepts
only the two h4 signs. It does not select U3 over the previously
supported disconnected so5 phase. State the h4-family restriction in
the closure table and preserve that alternative and its original grade.

## F5. The stated full global quotient has the wrong kernel

Severity MEDIUM for the source statement, binding before adoption.
The relay's literature paragraph writes
(Spin10 times Spin6)/Z2 for the global subgroup. Its full kernel in
E8 is Z4. The tested diagonal(-1,-1) relation is its square.
HAND_COUNTERCHECKS section4 gives the representation calculation
and a primary-source passage. Correct this sentence while preserving
the valid order-two identity and its limited sign reparametrization.

## F6. Verification coverage, independence and execution custody

Severity BLOCKING for promotion of this receipt to full certification.

The producer and its separate referee were authored in the same
checkpoint ff8244a58, with their tracked outputs. A separate
implementation with zero producer imports is valuable evidence.
Nonauthoring review independence still needs its actual reviewer record.
No such review or exact admission binding for P753 was located in the
checked named design/specification/review/acceptance files at this head.
Main's earlier P-753 prediction supplies predeclared questions, while
the prospective source-complete execution duties still need disposition.

The referee checks roots, one scrambled S_theta action, parity counts,
the weave/Weil comparison and local theta contours. It omits the
asserted actual induced3-branch actions, their characters and physical
domains. Its all-pass boolean therefore covers less than the relay's
complete-resolution claim. Test lines124-165 partly reread a saved
receipt and rerun only referee checks1 and4. Record that coverage.

Rounded6-decimal matrix keys and rounded numerical ranks are numerical
calculations. Calling all their orders exact requires an analytic or
exact-arithmetic certificate. The hand supplement supplies such an
argument for the central triplet orders and obstruction, preserving
these results without inferring exactness from a tolerance alone.

The receipt has no source hashes, interpreter/environment identity,
exact command, timestamp or execution-admission reference. Current
bytes can be pinned by this review, but that does not reconstruct
the historical run's custody. Preserve the raw files and the gaps.
CC can arrange a prospectively admitted exact reimplementation or
rerun after review. This reviewer ran metadata checks and hand algebra.

## Disposition for main

| Proposed banking scope | Disposition |
| --- | --- |
| Explicit weave triplet, odd Weil-square twist, untwisted obstruction | Supported by new exact hand proofs, subject to review of these proofs and main's ordinary banking evidence |
| E8 paired-sign identity and h4 singlet/triplet obstruction | Supported at the stated root/parameterization scope, with the Z4 correction |
| Candidate index3 carrier/parity orbit and generator compensators | Retain as scoped algebraic material, with exact full-relation and geometric-transport duties explicit |
| Complete WP-2.2 datum selection and input reduction | Revise F4-F5 and reconcile the full existing input/phase ledger |
| Complete WP-3.2 physical kernel and generation join | Keep open pending F1-F3 and the physical/domain map |
| Complete independent computational certification of all relay claims | Keep open pending F6 and admitted verification of the corrected scope |

The next consequential calculation is the actual E_theta action on
the physical harmonic modes and their scalar/spin transport, with
the stabilizer character and central sheet checked directly. It can
reuse the now explicit exact triplet. It should distinguish the
remaining scalar-line derivation from state selection and the
eventual physical weak-current/family test.

The new AGY03b-r5 packet at5242c938a is separate work. It has been
fetched but has not been reviewed by this P753 report. Its Lorentzian
and source-space claims retain their own review obligations.
