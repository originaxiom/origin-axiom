# R30: what happens to the chiral sector when its cores are resolved?

**Subsequent R31 result:** [the global compact Poisson argument](GLOBAL_POISSON.md)
now supplies the uniform-source sub-duty under its fixed-truncation and
proper-arc hypotheses. The original R30 science, runs, correction and
historical open-duty wording below are retained. Complete cusp limits
and physical source/end completion remain open.

2026-09-15. Local research on the same physical-bridge mission, not a
main arc, an independently accepted theorem, or a completed physical theory.

## Result and significance

The added R29 source model now has an explicit quadratic fermion extension
with positive bulk kinetic norm, a self-adjoint compact operator domain,
and full transmission through artificial core interfaces. In this
specified smooth, flat/exact, absolute-boundary class, its finite-width
zero modes are ordinary twisted cohomology. The two nontrivial
source-C3-compatible m202 characters have **no zero modes at finite width**.
This is a result about that extension, not a retraction of R19's singular
three/zero result on a different Hilbert domain.

There is also a conditional low-energy result: sufficiently strong
shrinking logarithmic wells produce light opposite-chirality pairs,
not a proof that unwanted partners become heavy. The quantitative well
bounds have not yet been established for R29's actual global Poisson
solution. Neither the local radial formula nor the finite tests fills
that gap. The [complete argument](RESOLVED_FERMION_PROOF.md) distinguishes
the finite-width theorem from this additional implication.

The physical bottleneck is therefore more specific: a successful singular
index does not yet specify a source completion with the same spectrum,
anomaly and interactions. This round supplies one explicit test of that
join and explains its failure to give an unpaired chiral compact kernel.
It does not exclude finite physical widths with different dynamics,
interacting defect sectors, other bundle topology, or derived end data.

## 1. What model was actually tested?

Fix a compact smooth connected three-dimensional truncation Q. Retain
R29's finite-width charged tube source and flat/exact stationary point
h=dF_epsilon, with a unitary coefficient line L extending through the
cores. Add R23's single charged representative 16_(1): odd internal
forms are four-dimensional left profiles, even forms right profiles.
Its parent conjugate is not counted as a second determinant.

The internal mass operator is

    d_q = d_A + q dF_epsilon wedge,
    D = d_q,max + d_q,max*,

with the usual positive bulk L2 norm. The four-dimensional quadratic
action contains both chiral kinetic terms and the mutually adjoint
off-diagonal D mass terms. Its variations in A and h have bilinear
fermion currents, which vanish at zero fermion background. Thus this
extension retains R29's classical stationary bosonic point. It does not
establish supersymmetry, radiative stability, a full-parent lift or the
absence of other allowed couplings.

At the actual compact boundary the absolute condition is iota_n psi=0.
The Green form and its half-dimensional annihilator are checked; D^2
also requires iota_n d_q psi=0. Scalars obey the deformed Robin condition
(nabla_n^A+q partial_n F)psi=0, not old Neumann data. The scalar quadratic
form domain is H1, with no essential scalar trace restriction.[^1]
Across an artificial tube cut the whole form must transmit, with opposite
outward normals. Tangential matching alone fails the Green-form test.[^2]

The outer absolute condition is an **input compact regulator**, not the
object's selected physical cusp condition. The metric, source positions,
widths, amplitudes and minimal fermion couplings are also inputs.

## 2. Exact kernel and the missing core contribution

For each fixed positive width, bounded invertible multiplication gives

    d_q = exp(-qF_epsilon) d_A exp(qF_epsilon).

This preserves the maximal complex and its cohomology. It is not unitary
in the unchanged bulk norm and does not identify the entire spectrum
with the undeformed spectrum. Absolute Hodge theory gives the following
complete graded kernel from the actual frozen m202 Fox complex.[^3]

| Extending unitary character (x,y) | H0,H1,H2,H3 | Left/right zero modes per 16_(1) |
|---|---|---|
| Nontrivial, P(x,y) != 0 | 0,0,0,0 | 0/0 |
| Nontrivial, P(x,y) = 0 | 0,1,1,0 | 1/1 |
| Trivial | 1,2,1,0 | 2/2 |

Here P=x^2*y+x^2+x*y^2+x*y+x+y^2+y. More generally, an extending flat
rank-r coefficient on a compact oriented three-manifold with torus
boundary has twisted Euler characteristic r*chi(Q)=0. This constrains
this absolute graded kernel, not every physical defect theory.

The actual attachment explains more than the Euler number. If N has k
contractible proper arc components, the R19 restriction mapping cone
is extended by k degree-zero core cochains. Its attachment parameter t
is algebraic, not a derived physical width or mass. At t=0 the complex
is the relative complex plus those even core states. For t!=0 an explicit
chain homotopy retracts it to the base complex. On an acyclic base with
k=3 the split counts are three odd and three even; full attachment removes
all six zero states. Exceptional and trivial characters retain the paired
base modes in the table. Rank-deficient attachment and unitary transport
phases are separately controlled.

R19's three/zero sector remains a positive in its original strong singular
maximal domain. R26 protects that **fixed** domain against its specified
perturbations. Resolving the cores is not such a bounded-domain transfer:
the inverse/conjugating multipliers need not remain uniformly bounded
as epsilon tends to zero.

### Correcting our own C3 sample

The initial sealed design called (zeta,1),(zeta^-1,1) a C3 pair, and one
test name repeated that description. They have order-three holonomy but
are **not fixed by the source's C3 action**. The original assertions were
valid generic-character checks; their passing result did not verify that
source-compatibility claim. The original code, design, test and runs are
preserved, not retroactively corrected.

The separate [control](RESOLVED_FERMION_C3_CONTROL_DESIGN.md) rebuilds the
action from R20's actual checked word maps. It obtains
A=[[-1,-1],[1,0]] and exhausts the entire fixed torus using
|det(A^t-I)|=3 and the integer adjugate identity. The points are
(0,0),(1/3,2/3),(2/3,1/3): characters (1,1),(zeta,zeta^-1),(zeta^-1,zeta).
At both nontrivial points the actual P=-2, relative H*=(0,3,0,0),
split H*=(3,3,0,0), and resolved H*=0. The original point is explicitly
rejected: (A^t-I)(1/3,0)=(-2/3,-1/3) is not integral. This tests the group
action, not merely the order of a character. No new interval geometry
certificate or source selector is claimed.

## 3. Why a thin core does not automatically hide its partners

The analytic implication requires k disjoint contractible neighborhoods
of entire proper arcs, cutoffs whose derivatives stay away from all cores,
uniformly bounded F on those derivative supports, and an interior bound
|F_epsilon-beta_j log r|<=C with measure comparable to r dr dtheta dz.
For a_j=q beta_j>=1, the scalar trial profile exp(-qF_epsilon)chi_j s_j
has bounded energy but diverging norm. Min-max then gives at least k
small scalar eigenvalues, with upper bounds

    lambda <= C epsilon^(2a_j-2)     (a_j>1),
    lambda <= C/log(1/epsilon)       (a_j=1).

For nontrivial L, H0=0, so each is positive at every finite width. The
closed Hilbert complex supplies an exact normalized odd partner
d_q u/sqrt(lambda). In the declared four-dimensional action these are
Dirac pairs with mass sqrt(lambda). This is not exactly k light levels,
an eigenfunction-convergence result, or an empirical mass prediction.

The actual local hyperbolic comparator integrates R29's h to
F_out=beta log(tanh(r)/tanh(R)), with its regular matched inner profile.
Exact transverse primitives at a=1,2 agree with independent quadrature
at the four sealed parameter points; maximum relative discrepancy is
3.38e-16. Wrong weight, opposite sign and threshold controls distinguish
the hypotheses. These finite controls are not the all-width proof.

A cutoff along only an interior arc segment would be invalid for the
light-mode conclusion: axial energy can grow with the same divergent
transverse norm. The explicit sin(pi*z/L) comparator retains pi^2/L^2.
The proof instead uses the whole proper arc and the absolute scalar
form domain. The global uniform Poisson bound, the complete cusp limit
and the order of those two limits remain separate duties.

For a surviving constant normalized D5 gauge mode, normalized charged
profiles couple with g7/sqrt(Vol Q), independently of their concentration.
That is the existing R25 overlap identity, now applied to this model.
It does not apply unchanged to R29's nonconstant massive extra-U1 mode.
Each left/right pair cancels its four-dimensional perturbative anomaly;
the full source/global quantum determinant is not constructed.

## 4. Verification and mission decision

Original native: 18/18 checks, including 105 exact character/attachment
rows. Original new tests: 30 passed. Focused six-file run: 110 passed.
The specified 52-file broad regression: 458 passed, 16 failed, 8 errors;
all 24 failed/error IDs equal R29's, with none added or missing. The
separately sealed C3 native control has 5/5 checks, its three tests pass,
and the combined two-file follow-up has 33 passes. The latter is not
represented as a 53-file broad run. These are authored checks, not
independent proof review or full-repository green.

The [reporting checks](RESOLVED_FERMION_FINAL_CHECKS.txt) retain four
inherited failed gates alongside 26 passes. Scientific source/seal
identity, raw-output custody and the exact failure population are checked
separately; neither result is independent acceptance of the analytic proof.

[Run receipts](RESOLVED_FERMION_RUN_RECEIPTS.json), [original native output](RESOLVED_FERMION_NATIVE_FIRST.json),
[broad first output](RESOLVED_FERMION_REGRESSION.txt), and
[C3 output](RESOLVED_FERMION_C3_NATIVE_FIRST.json) preserve the executed
content. [Prior/history intake](RESOLVED_FERMION_PRIOR.md) records what
was actually read and distinguishes old results from new applications.

The immediate plan remains within the same model, not another census:

1. Prove or disprove the uniform global Poisson well bounds for R29's
   fixed compact source using a local Green-kernel comparison and bounded
   remainder. Endpoint and off-source estimates must be explicit.
2. Analyze the complete end/domain limit without exchanging limits by
   assertion. Recompute the relevant low-energy normalized currents.
3. Use that result to test a specified physical source/end completion
   with its allowed interactions and full anomaly. A different kinetic
   space or end sector must be derived and charged to the input budget,
   not silently used to discard the compensating modes.

PB-BOUNDARY stays open. The programme has a clearer common-model
calculation and a concrete domain/partner obstruction in one extension;
it still lacks a demonstrated realistic chiral four-dimensional sector
with its quantum completion, same-theory gravity and distinctive empirical
predictions. Neither a full TOE nor a universal chirality no-go follows.

## Sources

[^1]: Wen Lu, [A Thom-Smale-Witten theorem on manifolds with boundary](https://intlpress.com/site/pub/files/_fulltext/journals/mrl/2017/0024/0001/MRL-2017-0024-0001-a006.pdf), MRL 24 (2017), section 4, pp. 133--135, equations (53)--(61). Used for the absolute Hilbert-complex realization; the Morse asymptotic theorem is not imported. The flat-coefficient/bounded-conjugacy extension is argued explicitly in the proof.
[^2]: Colette Anne and Junya Takahashi, [Partial collapsing and the spectrum of the Hodge--de Rham operator](https://msp.org/apde/2015/8-5/apde-v8-n5-p01-p.pdf), Analysis & PDE 8 (2015), section 2.1, p. 1028. Used for whole-form transmission, not for a spectral-limit theorem about this different Witten family.
[^3]: Existing path-local [R19 spectrum](HOLONOMY_SPECTRUM.md), [R20 source action](HOLONOMY_EQUIVARIANCE.md), [R23 mass map](MASS_INFLOW.md), [R25 current overlap](BOUNDARY_WALL.md), [R26 fixed-domain stability](INDEX_STABILITY.md), and [R29 bosonic source](DEFECT_GAUGE.md). The frozen producers are used directly; matching dimensions alone is not the verification.
