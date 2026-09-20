# F07: regular local changes cannot replace missing global matter data

2026-09-20. Local fork `audit/fork-2026-09-20`. This is a report-guided
compatibility check connecting F05's complete-space gap, F06's local core
and the already-existing bounded-conjugacy arguments. It is not a new
general theorem of Hilbert complexes or a universal chirality exclusion.

## Result and immediate consequence

**A regular core replacement preserving the geometric flat bundle and its
ordinary-L2 end class cannot generate exact charged zero modes.** This is
true for arbitrarily large fixed smooth compact changes, not just small
perturbations of the Dirac operator.

The important qualifier is WHAT is preserved. Keep a closed flat complex
`d`, its consistent graph realization, and positive norms satisfying

    m ||u||old^2 <= ||u||new^2 <= M ||u||old^2,
    0 < m <= M < infinity,

in every degree. If its original Dirac operator has gap delta0>0, the new
Laplacian obeys

    Delta_new >= delta0^2 m/M.

For each of F05's charged coefficient four and its dual this gives
`Delta_new >= (9/4)m/M > 0` in the reference curvature normalization.
The adjoint, Dirac domain and nonzero eigenvalues are allowed to change;
the proof does not confuse a nonunitary chain map with unitary spectral
conjugacy. See the full [argument](PROOF.md), including closed domains and
the quantitative estimate. Finite tests below support its algebraic
controls, not independent acceptance of its infinite-dimensional proof.

The standard orthogonal-decomposition and closed-range ingredients are
also recorded in [Holt--Piovani, section 4, Theorem 4.2 and Lemma 4.3](https://arxiv.org/html/2310.08993v2#S4).
Only those ingredients are used; unrelated complex-geometric conclusions
and general unbounded-operator sum claims are not imported.

## Why it applies to one concrete proposed gluing

Remove finitely many disjoint embedded closed balls in the regular interior
of the SAME three-manifold. Its exterior still carries the whole fundamental
group: each ball and each spherical overlap in van Kampen is simply connected.
If the new smooth flat connection agrees with the old one on this exterior
and its collars, the based holonomy representations agree. Parallel transport
then identifies the flat bundles by an isomorphism equal to the prescribed
one outside. The isomorphism and inverse are bounded over the compact balls.

Smooth positive base and fiber metrics agreeing outside those balls likewise
give equivalent L2 norms, including volume and all form degrees. Thus the
comparison applies even if a transition changes local curvature, currents
and mixed terms drastically. F06's loss of a pointwise positive Higgs bound
does not undo this global contraction.

This is conditional on successfully constructing that smooth flat gluing.
It neither proves nor disproves the classical matching itself. Instead, it
shows that such matching would not accomplish the hoped-for production of
massless matter. F06 remains a valid LOCAL full-parent solution and a useful
geometry comparator. Its algebraic tensor kernel is not retracted and is
not promoted to particles.

## What the result explicitly does not exclude

| Change | Status under this test |
|---|---|
| Arbitrarily large fixed regular metric change at fixed flat complex | Still acyclic; quantitative positive bound with its own m,M. |
| A family whose equivalence constants degenerate | Very light positive modes remain possible; no uniform bound is supplied. |
| A different global holonomy representation | Not the same complex; must be checked independently. |
| Non-equivalent cusp weights or unbounded chain transport | Outside this theorem, even if ordinary monodromy is unchanged. |
| Proper source arcs, drilled boundaries, new singular domains | Not regular interior ball replacement; retain their actual domain/interface data. |
| Nonflat operators, additional physical fields, quantum phases | Not covered by flat-complex equivalence; equations and consistency still required. |

Two explicit controls protect these qualifications. The metric family with
two-term differential d=1 has positive eigenvalue t^-2 at every finite t,
but it tends to zero as equivalence degenerates. Separately, on the real
line an unbounded chain multiplier converts a gapped constant Witten
operator into one with a Gaussian L2 zero mode. Ordinary bundle isomorphism
alone does not determine L2 cohomology without the boundedness hypothesis.
A circle holonomy control also changes kernels, in paired degrees; it is
not a chiral three-dimensional physical vacuum.

## What was already in the repository, and what the second look adds

- R18 uses bounded homotopies and closed-range estimates.
- R30 already proves that bounded finite-width source conjugacy preserves
  the compact regulated kernels, not its whole spectrum; R30/R31 preserve
  the distinction between exact zeros and light pairs.
- R26's wider perturbation class preserves an index but can add pairs.
  That does not contradict the stronger fixed-complex assumption here.
- R27 and F05 supply the reference geometric vanishing/gap mechanism.

The useful addition is the JOIN and its effect on F06's next-action list:
**do not treat unchanged-holonomy regular compact gluing as a mechanism for
creating massless matter.** The ingredients are credited rather than
rebadged as a new general theorem. No fresh all-head absence claim follows
from the targeted searches, and no remote snapshot was refreshed here.

## Revised next-action gate

Before solving another local core or a difficult global matching problem,
state which global data its candidate changes, and exhibit the map:

1. Does it change global flat holonomy, the complete end norm/domain, the
   field content, or flatness of the physical fermion operator?
2. Is that change licensed by the same parent action and its boundary
   variation, rather than chosen to force a desired count?
3. Does the COMPLETE normalizable spectrum have the intended light fields
   and partners, with a consistent quantum anomaly and interaction sector?

If all of item 1 are unchanged in the class above, exact matter production
is already ruled out there; do not spend a new numerical search on it.
If one changes, this result gives no success certificate. Reuse the actual
source/end and nongeometric constructions in the corpus to pose that next
test, while keeping their different assumptions explicit. The nonsplit
index positives and singular-source results are not withdrawn by F07.

This refines entries 1--3 and 6 of the whole-picture audit. It leaves the
separate boundary-index, one-loop and experimental deliverables in place.
A full physical TOE, or even a complete chiral four-dimensional vacuum,
has not been achieved.

## Verification and custody

- Original scientific seal `e4bd5190`: **16 passed, 1 failed**. The failure
  was structural equality on unsimplified exact complex arithmetic.
- [First failure and post-failure diagnostic](FIRST_RUN.md) retained; the
  original scientific sources, expectations and failure were not overwritten.
- Correction seal `7fe4e822`: **18 passed**, including all sixteen unaffected
  original cases, all previously unreached assertions and a wrong-adjoint
  negative control. No floating tolerance or changed producer.
- **105 unchanged antecedent checks passed**, with one optional GUI warning.
- All six F07 scientific hashes match their respective seals. F01--F06
  directories were byte-unchanged against `81980ab2` before living-report
  follow-through additions.

[Execution receipt](RECHECKS.md). No full-suite certificate, independent
review, shared B allocation, other-seat edit, push or external publication.
