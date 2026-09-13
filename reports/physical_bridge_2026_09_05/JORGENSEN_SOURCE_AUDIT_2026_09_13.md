# Jorgensen source audit: retain the stronger geometric selector

2026-09-13. Owner-requested literature/reception audit after R29, not a new
physical-spectrum calculation, a new B arc or independent main banking.

## The positive and the definitions

Write j(A,B)=|tr(A)^2-4|+|tr[A,B]-2|. The ordinary group J infimizes
over generating pairs; the generalized J-tilde infimizes over
non-elementary discrete two-element subgroups, without requiring them
to generate the ambient group.

Callahan's Theorem 2.3 characterizes the figure-eight complement by
J-tilde=1 among orientable hyperbolic three-manifolds. Corollary 2.4
gives the ordinary-J version. B1345's corollary wording is actually
present in the primary paper; it is not merely an inaccurate paraphrase.
[Callahan, definitions and section 2](https://arxiv.org/pdf/0905.1318).

For the attained case needed here, the proof uses a parabolic A,
j(A,B)=|c|^2=1, and the maximal-cusp waist bound to obtain waist one.
Adams' cusp characterization then identifies the manifold, without
assuming the ambient group has two generators.
[Adams, introduction](https://arxiv.org/pdf/1703.01324).

The published generalized-infimum statement is cited, not re-proved.
Its proof passes from the infimum to attainment; this audit does not
supply a separate attainment theorem. The explicitly attained case
above does not need that extra step.

## The record's exact witness is useful, not a new numerical discovery

For B1345's positive, the outside memo gives A=[[1,1],[0,1]],
B=[[1,0],[u,1]], u=exp(i*pi/3). Direct symbolic multiplication gives
tr[A,B]=2+u^2. Since A is parabolic and |u^2|=1, j(A,B)=1.
The geometric figure-eight representation and its generating property
are literature inputs here, not consequences of merely checking one
relator. No new numerical reproduction is claimed in this checkpoint.

This connects the banked MERIDIAN unit obstruction |kappa-2|=1 to
saturation. The fibre kappa=-2 belongs to a different marked pair/group
problem; substituting it into the meridian calculation is not licensed.
B1345's positive is retained, with its own later corrections read to EOF.

## The later axiom correction also needs correcting

The received memo 226 equates a two-generator group with A1, then says
the theorem assumes A1. That inference is not valid as written:

| Item | Actual object in the axiom ledger | What must not be identified with it |
|---|---|---|
| A1 | integer record state space Z^2 | two generators of a generally nonabelian fundamental group |
| A2 | invertible integer-linear updates in GL(2,Z) | arbitrary discrete Mobius transformations in PSL(2,C) |
| A3 | determinant +1 for those integer updates | ambient orientation preservation without a map to the update lattice |
| A5 | absence of torsion in the specified first homology | absence of finite-order elements in a Kleinian group |

These are different types, not interchangeable wordings. Moreover the
stronger attained-pair route does not assume that the ambient group is
two-generated. Thus the claim that two-generator input is unavoidable
in this geometric selection route is too narrow. Conversely this does
NOT establish the earlier memo's count of five discharged axioms.
Neither count is accepted by vocabulary matching.

Selecting the manifold offers a route to its punctured-torus fibre,
the fibre's rank-two integral homology and its monodromy. It still needs
an explicit reconstruction and a declared identification with the
programme's record dynamics, including basis/order and positivity.
The geometric theorem is an alternative CONDITIONAL entrance, not a
derivation of integer record physics from no assumptions.

The two meanings of torsion-free are particularly important: a
torsion-free fundamental group can have torsion in its abelianization.
The repo's A5 is explicitly about the latter. This is not an objection
to Callahan's theorem; it is a correction to a cross-structure reading.

## Consequence for the mission

This is a genuine geometric uniqueness criterion. It narrows selection
much more sharply than a small census or a matching dimension does.
It does not yet explain why the physical construction should saturate
the bound. If the unit obstruction was first evaluated after selecting
m004, the implication back to m004 is a characterization, not an
independent derivation from weaker starting premises.

The stated class still supplies hyperbolic three-geometry and
orientability. A normalized geometric minimum is not a spacetime action,
a dimensional derivation, an E6 identification or a chiral Dirac index.
Complex conjugating both matrices preserves j; this trace-modulus
functional by itself cannot distinguish a geometry from its mirror.

Nor should every later cover, filling or sourced sector be required to
saturate: that would confuse a selector for the base object with a
restriction on all its relations. R19's conditional sourced kernel and
R29's finite-width construction are not refuted by this theorem.

Two parallel duties now remain explicitly linked:

1. Audit the non-circular entrance: starting class, discreteness,
   extremality, and the map from selected geometry to record dynamics.
2. Continue the existing physical path: derive the finite-width/end
   fermion action and domain, then its spectrum, anomaly and currents.
   The geometric selector does not replace that calculation.

## What was actually checked

All heads/tags were fetched. The paper-review pin is 44ca6c35 and the
outside pin is 6388c69b. B1345/B1401 are present on that paper-review pin;
B1345's path is not present at origin-main b94ed03a. This says where the
artifact is, not that the main corpus contains no related mathematics.
No other branch was edited or merged.

Read completely: B1345 FINDINGS including the withdrawn refutation;
its short-word and unit-obstruction producers; B1401 FINDINGS through
addendum 2 and its bidirectional producer; outside memos 225 and 226
including addenda; the precise uniqueness-axiom document. Read primary
Callahan pages 1-4 and Adams pages 1-2, not both complete papers.
[Pins, file digests and read boundaries](JORGENSEN_SOURCE_AUDIT_RECEIPTS_2026_09_13.json).
Direct records: [B1345 with addendum](https://github.com/originaxiom/origin-axiom/blob/44ca6c357f102e911c90e6f379a0dc971735250c/frontier/B1345_the_jorgensen_number/FINDINGS.md),
[memo 226](https://github.com/originaxiom/origin-axiom/blob/6388c69bea95c68dd9041c2a699f2055ffdb4971/outside_bench/memos/JORGENSEN_IS_IT_RIGHT.md),
[the precise axioms](https://github.com/originaxiom/origin-axiom/blob/44ca6c357f102e911c90e6f379a0dc971735250c/docs/UNIQUENESS_THEOREM.md).

The short-word producer does not test generation of every pair.
B1401 correctly separates several upper-bound witnesses from the
remaining all-generating-pair lower-bound problem in its addenda.
Numerically rounded/capped Nielsen searches are not accepted here as
exact equality certificates or exhaustive word-distance exclusions.
No incoming census or other-manifold J value is newly certified.

The existing bank query returned no local frontier hit for its ASCII
term, while the twelve-head synonym sweep returned PRESENT. The
latter searches deleted filenames, not all historical file content;
neither output licenses a universal absence statement.

Read-only lookup errors (guessed paths, Ruby source/locale/brace errors,
one unavailable publisher URL and truncated tool displays) were not
treated as mathematical negatives. The relevant source bodies were
subsequently read in bounded chunks. No scientific producer or test
was modified, executed or silently repeated. Reporting gates and
post-receipt hashes are recorded in the
[final checks](JORGENSEN_SOURCE_AUDIT_FINAL_CHECKS_2026_09_14.txt): 26 PASS /
4 FAIL, the same failed identities as R29, with only the old relay's age
incremented. All 403 then-latest artifact hashes and 63 design seals match;
131 relative links resolve. The final receipt is added after the run.
