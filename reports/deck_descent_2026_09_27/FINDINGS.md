# A nontrivial holonomy cube does not exclude geometric deck descent

2026-09-27. Local fork `audit/fork-2026-09-20`. Seal
`5a7ef5467b60f5941a096fa16f6cf9633f259ab4`, committed before either run.
No shared bank number, push or modification of another seat's conclusions.

## Outcome

The scope distinction survives all declared exact controls: **10 tests pass**,
and the native producer exits zero. A general written construction explains
it independently of the finite example:

- The matrix T=(Ind V)(a^2) used in B1384 is a same-fibre holonomy operator;
  T^3=(Ind V)(a^6) can be nontrivial unipotent.
- The geometric deck action D on the full bundle pulled back from M2 to M6
  nevertheless has D^3=Id. It moves the base point and uses the bundle's
  transition identification. This requires no semisimplification.

These are different operators, so there is no contradiction. In the concrete
control, dropping the seam identification gives the wrong cube; restoring it
gives an honest order-three action while keeping the nonsplit monodromy.
Its split opposite control also behaves as prescribed.

This is a qualification of a possible overreading of B1384's phrase
“strict C3 after semisimplification,” NOT a refutation of its displayed
holonomy equation. It supplies a geometric C3 on a particular pullback,
not an already-gaugeable internal symmetry of a physical theory.
No claim is made that this elementary distinction is new to mathematics
or absent everywhere else in the corpus.

## Why it matters to the goal

The new M6 three-shaped positive must not be rejected merely because
the chosen holonomy lift has a nontrivial cube. Equally, its three summands
are not automatically three physical families. One must specify whether
the physical theory retains all cover modes, takes deck invariants, or
uses another earned prescription, with its actual action and domain.

There are three different coefficient-space pairs:

| Pair | Rank | What the recorded comparison says |
|---|---:|---|
| M6 with seed V | 2 | Recorded index -1 |
| M2 with induced p_*V | 6 | Shapiro retains that index -1 |
| M6 with p*p_*V | 6 | Three deck-related summands, recorded total -3 |

Only the first two are the direct Shapiro comparison. Pulling back creates
the third; it is not a passive relabeling of the first. A compatible invariant
projection returns the downstairs complex. These M6/M2 index values are
received from B1378/B1384, not independently recomputed by this cell.

Also distinguish descent along the COVER from extension across a FILLING.
The former exists for this pulled-back bundle; the latter still fails when
the meridian that would be killed has nontrivial holonomy. The nonsplit
extension and its filling obstruction have not been erased.

## Evidence and limitations

[PROOF.md](PROOF.md) gives the total-space and universal-cover constructions,
the invariant-complex statement and its physical-domain qualifications.
This is an authored proof, not independent specialist acceptance.

The exact comparator is a circle, not M6: rank-two Jordan monodromy with
c=1,-2, plus the split c=0 control; rank-six induction; an 18-dimensional
three-fibre action. Its cover/downstairs H0 dimensions are 3/1 in the
nonsplit controls and 6/2 in the split control. H1 matches H0 on the circle:
there is NO chiral index in this example. The geometric averaging projector
has rank six; averaging the same-fibre holonomy fails in the nonsplit case.
Those results verify the distinction, not a physical spectrum.

Native and test transcripts: [native](RUN_NATIVE.txt), [tests](RUN_TESTS.txt).
[Execution custody](EXECUTION.json) records both actual terminal exits and
the unchanged five sealed hashes. Initial locale/interpreter-discovery
issues occurred before any scientific execution and are disclosed there.
No scientific failure, correction or skipped test; no full-suite claim.

The standard term canonical descent datum was cross-checked against
[Stacks, definition 35.2.3](https://stacks.math.columbia.edu/tag/023D).
That source concerns schemes, not this physical model; the smooth-bundle
proof here stands on the explicit pullback construction, not a category
change hidden in the citation.

## Updated next priority

The bounded deck-action distinction in the
[goal reassessment](../goal_reassessment_2026_09_27/ASSESSMENT.md) is now checked.
The next unanswered question is the **physical role and admissibility** of
the M6 orbit-sum in a single parent/action/domain, not another proof that
its formal index equals three. In particular:

1. Identify which proposed SL5 realization actually contains this bundle;
   root-level compatibility alone does not overcome the recorded parabolic
   pairing obstruction. Do not duplicate a full component search already
   assigned elsewhere without first checking its current artifacts.
2. Test that candidate's background equations, norms and end variations.
   Retain F01's finite-energy qualifications and its positive local cusp;
   no universal nonsplit no-go follows from this cell.
3. Only after that join is specified count physical modes, decide the deck
   projection, and normalize the whole interaction and anomaly problem.

F20 remains preserved, unexecuted. F19's paired SL4 family remains a valid
scoped result, not a closure of this different branch. The TOE objective
is neither achieved nor guaranteed by this mathematical clarification.
