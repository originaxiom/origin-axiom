# R11 — an explicit source-derived family component, not yet physical families

**The algebraic connection strengthens: the marked founding ratio determines
a pure family-A2 rotation in the specified icosian construction. Its literal
left-multiplication action is NOT that rotation; it factors into this family
component and a commuting E6 Weyl action.** Both statements are verified
exactly, not inferred from equal orders or counts. Neither establishes a
physical compactification, three chiral zero modes or a complete TOE.

## What was actually compared

The incoming sources are main B1275 at `87a2eb3d`, the SM-derivation seat's
renumbered sB1270/sB1271 at `945e091d`, and older B1138. B1138 already exhibited
the E8 family branching; main B1275 rebuilt that branching but left the
founding-element connection unchecked. The source seat constructed a
marked SL(2,F5)-to-icosian isomorphism and showed a three-cycle on classes.
This audit independently implements that construction and checks the
action on the whole root space, not only the six class labels. Full commit
and source-byte SHA256 receipts are inside the result JSON.

Let g be the image of -R L^-1 under the marked isomorphism, A the rational
plane spanned by 1,g, and E its metric orthogonal complement. Here A is A2
and E contains the E6 root system. With B the root-normalized metric, set

    Lg(x) = g*x
    s_a(x) = x - B(x,a)*a
    Wg = s_1 s_g
    Ug = Lg Wg^-1.

All twenty order-three icosian units give the following results:

| action | characteristic polynomial on the 8d root space | fixed root-space dimension | action on the 72 E6 roots |
|---|---|---:|---|
| literal Lg | (x^2+x+1)^4 | 0 | 24 cycles of length 3 |
| pure family Wg | (x-1)^6 (x^2+x+1) | 6 | fixes all 72 individually |
| internal Ug | (x-1)^2 (x^2+x+1)^3 | 2 | 24 cycles of length 3 |

**These dimensions are not invariant dimensions of the 248 or the 78.**
In particular, zero fixed Cartan/root-space directions must NOT be read
as zero invariant Lie-algebra content or a physical gauge no-go.

Lg and Wg induce the SAME permutation of the six 27-root classes: two
three-cycles. Ug preserves each class. But Lg != Wg; their characteristic
polynomials differ, so no change of basis can identify the two full actions.
The original three-cycle is real; the stronger pure-family interpretation
of literal left multiplication would lose its internal E6 rotation.

## The positive recovery is an explicit, unique component

For X with columns 1,g, the metric projector onto A is

    P_A = X (X^T B X)^-1 X^T B,
    Wg = I + (Lg-I) P_A,
    Lg = Ug Wg = Wg Ug.

The independent reflection and projector constructions agree exactly.
Wg is the UNIQUE linear map with Lg's action on A and the identity on E.
This uniqueness is relative to the supplied marked construction and metric;
it does not select a physical background. Ug fixes A pointwise. For each
of the twenty cases, a product of 24 E6-root reflections reconstructs Ug
on the entire eight-dimensional space. The full matrices, simple roots
and reflection words are retained, including the marked founding case

    g = (-1/2, -phi/2, 0, (phi-1)/2).

The marked group isomorphism is checked on ALL 14,400 products. Its coordinate
choice does not privilege a family direction: all twenty g images are
tested; conjugation covariance holds for all 120 units times all twenty
images (2,400 checks). The inverse g^2 gives Wg^-1 in twenty checks. There
are ten unoriented planes in this unit family, not one distinguished plane
without a marking. No physical mirror or chirality bit is thereby chosen.

The A2 root subalgebra commutes with E6: all 432 mixed root sums per case
are absent, and their Cartan pairings vanish by construction. An explicit
order-three SU(3) Weyl representative is exhibited. Thus a group lift
centralizing this E6 exists inside the commuting SU(3). A root permutation
does not fix every possible lift phase, and this audit does not construct
a full E8 adjoint lift of Lg or identify a spacetime holonomy with it.

## Independent construction and controls

The 120 unit quaternions close under every product and have orders
1^1, 2^1, 3^20, 4^30, 5^24, 6^20, 10^24. The 240 roots close under every
root reflection (57,600 pair checks). Their lattice has an exact integral,
even Gram matrix of determinant 1. Every E6 complement has its six-root
Cartan matrix, determinant 3 and integral spans checked, not merely a
72-root count. Six classes of 27 roots are recovered.

Controls reject a corrupted root set, an invalid assignment of the marked
generators, and Lg mislabeled as an E6-fixing family action; Wg passes that
same predicate. The order-four plane instead has 60 perpendicular roots,
so the complement test is discriminating. Rational-coordinate denominators
require four: the scale-two integerization is rejected, not truncated.
These confirm the stated construction, not uniqueness over all possible
originating axioms, transports or physical theories.

For independent mathematical context see Wilson's
[E8 construction notes, section 3.6](https://webspace.maths.qmul.ac.uk/r.a.wilson/pubs_files/E8notes2.pdf).
The calculations here use their declared coordinate/norm convention and
are recomputed; they do not rely on that reference for their output.

## What this buys toward the full goal

It buys an actual internal map from the marked ratio to a commuting family
rotation, with an explicitly accounted-for internal action. It is more
specific than saying that three structures have the same omega. It does
not identify the distinct trinification grading INSIDE E6 with the family
SU(3) OUTSIDE E6, and does not discharge I-14 or the physical map I-13.

In the twisted 7d SYM transport, multiplicities of four-dimensional matter
are determined by coefficient-bundle zero modes. They are not simply the
dimension three of a fiber: the relevant differential, background, metric
and boundary conditions must be specified. This distinction is explicit
in [Braun et al., equations (2.40)--(2.49)](https://arxiv.org/pdf/1812.06072).
Couplings further depend on products/overlaps and kinetic normalization;
[Pantev--Wijnholt, section 3.8](https://arxiv.org/pdf/0905.1968) explains
that step in its physical construction. Neither reference constructs the
required physical geometry from this repository's originating object.

The source seat itself corrected its family index in sB1271's addendum.
It also has a newer sB1273 **three-fold closing** claim: three twisted
classes, a nonzero cubic, mirrors and a scoped texture obstruction.
Its FINDINGS was read here; its producer and physical hypotheses are
NOT independently certified by R11. This is a concrete next audit target,
not an absent route. Likewise main B1274's subregular selector and the
physics seat's R63 comparison are read leads, not results of this run.
Do not import the source seat's blanket G2 kill or an uncalibrated B915
significance: the earlier audit already corrected those scopes.

Next carry the actual family action through a specified full fundamental-
group representation and closing/boundary problem, verify the surviving
gauge action and zero modes, then the cubic AND kinetic forms. Separate
the literal Lg from Wg; determine which the physical construction uses.
The three-fold closing must be checked before calling a three-class or
nonzero-Yukawa mechanism missing. Gravity, chirality, input selection and
a distinctive empirical prediction remain uncompleted in this audit.
R4--R10's conditional physics is retained, not replaced by this root result.

## Reproducibility and the new failure, kept visible

Original design/source/eight locks: seal `e066cdee`. The first producer
failed at HNF because an integer-valued matrix retained SymPy's QQ domain;
no JSON was created. The original test fixture produces eight errors.
Raw evidence: [FAMILY_ACTION_FIRST_FAILURE.txt](FAMILY_ACTION_FIRST_FAILURE.txt).
This is NEW R11 software debt, not an earlier failure or a physics negative.

Separate exact-domain adapter and tests: seal `f790acb2`, before rerun.
It converts only already-checked integral entries to domain ZZ and proves
matrix equality. No rounding, scientific assertion, source seal or original
test is changed; the module binding is restored after the run.

The adapted producer succeeds in 21.53 s and its eleven tests pass in
23.00 s: all eight unchanged mathematical lock functions plus three adapter
controls. Combined quiescent regression: **126 passed, 3 failed, 8 errors
in 129.87 s**. The three failures are the preserved earlier G2 exporter
and R7 small-step controls; the eight errors are the unadapted R11 fixture.
Separate repairs pass. This is deliberately not a full-suite green claim.

Use a fresh output path; existing paths are refused:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3.12 -m reports.physical_bridge_2026_09_05.family_action_domain --output /tmp/oa-family-action-new-run.json
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3.12 -m pytest tests/test_physical_bridge_family_domain.py -q -p no:randomly
```

Full exact output: [family_action_rerun_1.json](family_action_rerun_1.json).
Successful and combined-run receipts: [FAMILY_ACTION_CHECKS.txt](FAMILY_ACTION_CHECKS.txt).
All source pins and local artifact hashes are retained. No remote writes,
upstream merge, publication-readiness claim or completed TOE.

## Later receipt: identifiers and new source results

CC's numbering relay and alias table were read at main `2901ae9f` before
this local reporting checkpoint; see [BANKING_RECEIPT.md](BANKING_RECEIPT.md).
R11 is local to this report directory, not an allocation of a main arc or
another seat's Round 11. Earlier sealed files retain their original
branch-qualified IDs and source commits; their bytes are not renamed.

The subsequent fetch also locates physics-seat R64--R68 at `f4d74728`:
factorization, full Lie lifts and a two-sided trinification selector are
now explicit incoming audit targets. They are NOT independently verified
by this R11 run, which predates them; do not turn this audit's scope into
an assertion that these constructions are absent elsewhere. The user's
boundary-index question is pursued separately against main B1290/B1291
and physics-seat R69, preserving their distinct hypotheses.

Dispatch controls sealed at `14f2363a`: **8 passed in 22.37 s**. Every
actual delegated lock accepts the recomputed genuine data and rejects
its specific predeclared corruption with AssertionError. This refutes
the static gate's unconditional-pass classification for those calls;
it is not complete coverage and the unchanged gate remains red. Receipt:
[FAMILY_ACTION_DISPATCH_CHECKS.txt](FAMILY_ACTION_DISPATCH_CHECKS.txt).
