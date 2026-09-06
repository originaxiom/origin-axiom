# A true element lemma does not certify an enhancement no-go

Scope: B1259 at fetched **9a79adfd**, not merged into this branch. Its full
findings and producer were read; the producer was replayed verbatim and
passes. Its SO(odd) lemma is correct. The move from that lemma to a universal
claim about enhancement strata is not established by its calculation.
This is a proof-scope correction, **not a derived chiral spectrum** and not
a proof that the opposite physical conclusion is true.

## Exact counterexample to the fixed-subgroup inference

The sealed instrument constructs G=(Z/2)^3 on the seven nontrivial real
characters of F2^3. Each matrix is diagonal with signs (-1)^(a dot v).
Every product, determinant and exterior-cube action is checked exactly.
All eight matrices preserve

    phi = e123+e145+e167+e246-e257-e347-e356.

The metric reconstructed from this three-form is exactly I7. Thus this is
an actual compact-G2 subgroup, not an arbitrary SO7 example labelled G2.
All 16 subgroups are enumerated; stacked exact kernels agree with their
independently computed Reynolds projectors:

| Subgroup order | Number of subgroups | Common fixed dimension |
|---|---|---|
| 1 | 1 | 7 |
| 2 | 7 | 3 |
| 4 | 7 | 1 |
| 8 | 1 | 0 |

Every nonidentity element fixes a three-plane. The whole group fixes only
the origin. Point isotropy orders at a generic plane point, an axis point,
a free point and the origin are respectively 2,4,1,8. Hence the origin is
an isolated **maximal-isotropy stratum**, while the total orbifold singular
set is not isolated there. A wrong SO7 sign matrix is rejected by the G2
form test; retaining only one generator restores a three-dimensional kernel.

## The distinction was already in B1084's own model

An independent exact construction of three of its stated generators
(left -1 on H, g_tau, g_sigma) has stacked rank 7. Checking these against
the original full 96-element float producer gives the same common kernel:
zero. B1084's findings already say the apex has stabilizer 96.

Crucially, the old positive and bounded negative geometry both survive:
the nonidentity element census is {3:53,1:42}; there are 30 A1 planes in
orbits 6,12,12; the three axis stabilizers have order 48; **each of the 30
A1 planes intersects the E6 R3 in a line**. Those lines are computed from
the actual projectors, not inferred just from the element census. Having
a separate apex stratum does not make those pairwise intersections points.

The old exact producer was read fully, but not rerun here. The new three-
generator proof is exact; the complete original-group comparison and
30-plane intersection calculation are numerical with stated 1e-9 rank
tolerance. The separate sign-character G2 example is entirely exact.

## What this does and does not reopen

Three distinct questions were compressed into one word, "isolation":

1. Does an individual group element fix a positive-dimensional space? Yes.
2. Can the common stabilizer stratum nevertheless be a point? Yes, exactly.
3. Does that point carry a localized four-dimensional chiral mode? This
   calculation supplies neither the required operator nor its index.

The SO(odd) lemma does rule out an isolated point of the **total orbifold
singular set** for a nontrivial linear quotient. It does not by itself rule
out an isolated enhancement stratum within that set. Its quantifiers may
not be interchanged.

The standard Acharya--Witten construction requires additional geometry:
an appropriate singularity enhancement/unfolding and an actual localization
or index argument. Witten explicitly distinguishes its relevant conical
points from ordinary orbifold singularities; the group-theoretic example
above is not a realization of that construction. See [Witten, introduction
and section 3](https://arxiv.org/pdf/hep-th/0108165) and [Acharya--Witten,
section 2](https://arxiv.org/pdf/hep-th/0109152). These references support
the physical fence, not the new exact matrix calculation.

Therefore do not use B1259's single-element tests as a mathematical proof
that all flat-G2 enhancement strata have positive dimension, and do not
use this correction to announce that flat orbifolds now supply chiral SM
matter. The named B1084 pairwise-line result remains; its stronger
all-localized-states interpretation needs a physical operator argument.

The source addendum and kill node now say this at point of use. The ladder's
X33 and framework's main geometry paragraph are corrected inline. This also
restores B1105's already-banked distinct-domain correction where the framework
still called the four results one theorem; the positive B1085 edge counts
and rank-reducing hatches are retained, not swept away with that overstatement.

## Provenance, failure, and reproduction

Design/code/tests sealed at **f3696b21**, before execution. The first run
finished all scientific assertions but failed exporting NumPy integer keys.
Its partial JSON and unchanged source remain. The original seven tests give
six passes and one JSON round-trip failure; captured output is
G2_ISOLATION_FIRST_TESTS.txt. A separate native-scalar wrapper, sealed at
**9812f5d5**, changes serialization only. Its fresh successful execution
completed in **1.399 s**. Full original stdout, subgroup matrices, projectors
and all intersection dimensions are in `g2_isolation_rerun_1.json`.

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3.12 -m reports.physical_bridge_2026_09_05.g2_isolation_export --output /tmp/oa-g2-new-result.json
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3.12 -m pytest tests/test_physical_bridge_g2_isolation.py tests/test_physical_bridge_g2_export.py tests/test_b1084_g2_cone.py -q -p no:randomly
```

The original serialization test intentionally still exposes its original
defect; no full-suite-green claim follows from the successful wrapper.
The quiescent combined regression is **91 passed, 3 failed in 61.66 s**:
the original G2 JSON round-trip plus the two unchanged R7 small-step controls
fail. The new export controls, exact subgroup checks, all original B1084
locks and the three B1105 scope checks pass. Captured full output is
`G2_ISOLATION_CHECKS.txt`; this is not a full-repository certificate.

Publication gates are **27 pass, 3 fail**. Attribution and the R6 static
test-vacuity diagnosis remain the earlier declared failures. Seal-provenance
now names **two new deficient files in addition to the two old R4 files**:
UPSTREAM_3_DESIGN and UPSTREAM_3_EXPORT_REPAIR omit its exact required
marker strings. Prior-work content and before-execution commit timing are
visible, but the mechanical provenance requirement was not satisfied.
This new process defect is not disguised as an entirely pre-existing gate
failure. The sealed files and gate are unchanged; a post-result label edit
would not make the original seal compliant. Local evidence is checkpointed,
not certified for publication. Check the literal provenance fields before
sealing the next calculation. All recorded scientific hashes still verify.

After the final inline framework/ladder correction, the three B1105 scope
locks were rerun: **3 passed in 0.32 s**. The staged-tree gates were rerun
and remain **27 pass / 3 fail**, with the same four seal paths listed.
All **80** latest-path artifact digests independently recompute with zero
mismatches. These reporting checks do not turn the earlier 94-test run
into an exact-commit full-suite certificate.

The prior search covered nine fetched heads through 9a79adfd: all report
presence for the intersection/isotropy/G2-isolation regex; no matching deleted
paths. This is not an exhaustive deleted-content search or a novelty proof.
The older 14-to-12 reduction and other recovered positives are preserved in
RECOVERED_PHYSICAL_STEPS.md. R8 remains a visible unsealed draft, not an
executed or abandoned sealed experiment; the next physical task is still
its full leading broken-Higgs potential, masses and orientation test.
