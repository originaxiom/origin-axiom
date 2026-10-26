# Independent source review of the radial R1/R2 successor

Date: 2026-10-26. Kind: `source_review_only`.

Verdict: **NO_BLOCKING_SOURCE_ERROR_FOUND_WITHIN_REVIEWED_SCOPE**.
The successor addresses the two finite-coverage findings R1 and R2 of
the preserved October 25 review. This is a source/proof/code judgment,
not a scientific pass, runtime discovery certificate or execution approval.
The predecessor's **CHANGES_REQUIRED** verdict remains correct for its
unchanged source and is not retroactively upgraded.

Reviewed candidate: `72a0b9a24dd8fe788167a268f9e5e79f64a9c5f6`, branch
`audit/physical-bridge-2026-09-05`. Every hashed source below matched that
commit as well as the working-tree bytes personally read. The successor
design is present in the earlier commit
`90989a0df18b8ed3ca0aa8dceb75f7f546377098`; implementation is the candidate
commit. I did not author the reviewed science or controls. This review
creates only this new note; it edits no science, design, inventory, old
review or inherited staged file, and performs no commit or push.

## Method and actual reading coverage

I personally read WORKING_RULES.md and the complete applicable
GOAL_CONTRACT.md; the entire preserved October 25 independent review;
both radial verification DESIGN.md and checks.py files; both inventories
and status notes; and the October 26 author reply. I read the complete
SAME_ACTION_RADIAL_VACUUM_FLOW_AND_RESPONSE.md,
GLOBAL_CARTAN_AMPLITUDE_MATCHING.md and
ACTUAL_GRADED_CUSP_RESPONSE_AND_STATE_SCOPE.md.

I also personally read the full PROOF.md bodies for the October 8
weave_curved_action, weave_graded_condensate, weave_cusp_condensate,
weave_sm_parallel, weave_neutral_stability and weave_global_condensate
packages. I read the entire graded reference.py, including polynomial,
blocks_from_polynomials and its dual-isometry/R-weight comparisons.
Reading of graded probe.py was selective: radial_blocks, spectrum,
normalized_coefficients and the associated kinetic, Hessian, dual-R and
population predicates. I do not claim a full review of that producer's
root enumeration, all old producers, or all scientific claims in the old
parent. Hashing an entire selectively read file does not enlarge coverage.

Only text, stdlib AST/JSON/hash processing and Git metadata were used.
Neither scientific module was imported or evaluated; no SymPy import,
symbolic evaluation, collection, tests, numerical experiments or old
producer execution occurred. AST parsing is inspection of source text,
not execution of its definitions. No literature was newly consulted or
certified by this review. This is not an absence/priority sweep.

## R1: the physical map is now discriminated

The old method's arbitrary k0 and D2D1 identity were insufficient to fix
physical normalization. V2 first calls that unchanged method, then adds
an independent polynomial reconstruction. On monomials x^(n-k)y^k,
E=x partial_y has entry k in row k-1, F=y partial_x has entry n-k
in row k+1, and H has diagonal n-2k. With g_k=1/binomial(n,k),
G^-1 E^T G=F. Conjugation by diag(sqrt(g_k)) gives squared raising
amplitude k(n-k+1), hence (j-m)(j+m+1) at k=j-m. This is the actual
graded reference producer's metric, rather than its output histogram
or a substituted normalized ladder formula. The wrong identity Gram
differs on nontrivial included blocks; the flag is required true.

The source curved metric has chiral weights (1/2,Omega,Omega) and
gauge weight Omega^2. In the stated cusp frame its normalized fields are
lambda=sqrt(y)u_lambda, delta A=sqrt(2/y)u_A and delta q,r=u_Q,R.
Using q_bg=f/(2sqrt(y)), the gauge Killing route is
sqrt(2) q_bg sqrt(y)=f/sqrt(2). The cubic W-Hessian route is
y q_bg sqrt(2/y)=f/sqrt(2). V2 reconstructs both factors before
multiplying the polynomial ladder amplitude. Removing the gauge
sqrt(2) is rejected at nonzero f. The common sign/phase conventions are
those of the declared rephased source block; this is not a test of an
independent physical phase selection.

For integral j, the anti-diagonal bilinear J_(k,n-k)=(-1)^k g_k
satisfies J T+T^T J=0 for E,F,H and J^T G^-1 J=G. Thus pairing a
Q weight m+1 requires R weight -m-1. In the included even-m paired
blocks, Q weight is odd and nonzero, so its same-weight bilinear
entry is zero. This makes the same-weight control discriminating.
At r_index=j+m+1 the R raising norm is
(j+m+1)(j-m), equal to the Q-target coefficient's square. The ranges
ensure r_index>=1 and <=2j, so no spurious negative matrix index
enters this R calculation. For j=1,2,3,4 the code visits respectively
1,2,3,4 pairs; paired_count=10 is the correct finite total.

The R-only potential in the old cusp proof is
Omega^-1|Dbar delta r|^2+2|[q,delta r]|^2. In measure dt the quartic
coefficient becomes 2y q_bg^2 e_R^2=f^2 e_R^2/2, precisely k^2.
The actual R derivative is partial_t+h(-m-1)/2=partial_t-b.
Its formal adjoint is -partial_t-b, giving
-partial_t^2+b^2+bdot+k^2. V2 reconstructs the coordinate derivative,
rejects the wrong dual sign, independently composes this R operator,
and compares it to the lower diagonal of the paired Bdag B.
The other component is ((a-b)k-kdot)u, canceled by
fdot=(1-h)f/2. This checks the physical complex, rather than merely
the generic arbitrary-k0 identity. None of these finite identities
computes a charged global index or certifies the full parent theory.

## R2: scalar first-order signs and varying squares are now retained

The source has one scalar extreme in each integral spin module:
upper A_j for even j and lower Q_-j for odd j. V2 retains j=0,...,4
and calls the old constant-square/channel-population method first.
The upper kinetic coordinate map gives
sqrt(y)[partial_y(sqrt(y)u)+hj sqrt(y)u/(2y)], hence
B=partial_t+1/2+hj/2. At the lower extreme the source spin map is
partial_t-hj/2. Its formal adjoint in the fixed dt measure is
B=-partial_t-hj/2. Thus epsilon is +1 or -1 respectively,
B=epsilon(partial_t+K), and K is 1/2+hj/2 or hj/2.
The lower minus sign is justified by that formal adjoint, not by
positivity of a constant square.

Writing c=epsilon K, the code actually composes
B=epsilon partial_t+c and Bdag=-epsilon partial_t+c on arbitrary
u(t). The products give K^2-Kdot and K^2+Kdot respectively. At h=1
they recover (j+1)/2 or j/2 before squaring. For each nonzero j,
omitting Kdot leaves a nonzero symbolic multiple of hdot*u; j=0
correctly has K=1/2 and no derivative term. First-order epsilon is
still checked for j=0, so that legitimate constant case cannot mask
the orientation defect that caused R2.

For the doubled operator [[0,Bdag],[B,0]], the constant unitary
diag(1,i epsilon) gives -i sigma1 partial_t-sigma2 K. V2 applies the
operators to arbitrary two-component profiles, rather than comparing
constant matrices only. Removing i fails in that declared convention.
Flipping epsilon while retaining c changes the derivative term, also
detected on arbitrary u. A consistently transported alternative
Clifford/frame convention is not excluded. The intended signs,
phases and square formulas agree with the old graded physical blocks
and the actual-response source. I found no blocking sign error here.

## Preservation, loading and intended population

The complete predecessor source still declares ten unique test methods.
The successor declares exactly one TestCase subclass and two overrides,
whose first operations call the corresponding super methods. Its other
eight methods are inherited unchanged. Taking the union of names gives
exactly the inventory's ten intended names, with no removed control or
new test-name duplication. The eight retained bodies still cover the
coordinate residual/orientation, Jacobi/reality/parity, trace differential,
fixed points, scalar reduction/linearization, paired formal squares,
transported projector and two-slot Green/integrated-norm controls.

The import path resolves from the successor file to its sibling
verification_radial_flow/checks.py. Literal SHA256 comparison occurs
before exec_module. The compared digest agrees with the original bytes
reviewed here. The base source imports only unittest and SymPy, defines
helpers and its class, and has no direct-run block or import-time test
invocation. The dynamic module is retained as _base, rather than exposing
its TestCase as a module-level class alias; the public class is the
successor. Thus ordinary unittest module loading has one candidate
TestCase class and inherited method names, not twenty direct methods.
This is static reasoning about intended discovery, not runtime collection.

The digest check is an integrity guard for the predecessor source only.
It neither admits execution nor checks runtime, dependency or wrapper
closure. exec_module would import SymPy and create science definitions
if someone imported the successor directly; no internal admission gate
precedes that operation. This is consistent with the present design's
explicit prohibition of direct import and dependence on a future admitted
entrypoint, not a certificate that the source can safely be collected now.
Any eventual runner must bind both science files and verify the actual
ten-test population, no skips/xfails, result propagation and custody.
The seventeen author pins matched, but their agreement proves bytes,
not source-complete executable closure.

## Independent analytical scope check and remaining boundary

The radial residuals follow from F_xy=-partial_y A_x and the actual
Dbar conventions. Product/Jacobi differentiation gives
Cdot=C-[H,C]/4. The positive-trace real differential produces the
matter coefficient eight in Pdot. On a bounded trajectory the compact
closure bounds P and the vector-field derivative; finite integrated
squared speed plus uniform continuity gives speed tending to zero,
and accumulation points are critical. Finite cusp volume alone does
not imply the required boundedness or convergence to a single point.

For a compact triple the scalar equations are hdot=h-f^2 and
fdot=(1-h)f/2. Their quadratic remainder and opposite-sign linear
rates agree with the source. The weighted half-line integral map
controls a quadratic remainder on a small ball when
0<alpha<-lambda_s. It supplies local stable tails with initial
stable amplitude, not core matching. Bounded end coefficients and
derivatives give the stated end integrability on this fixed finite-area
cusp; they do not classify every finite-norm end.

In the fixed global real-Cartan class, delta A=-(H0/2)*du cancels
the derivative of exp(u)q0 in Dbar, while delta F=-H0 Delta_flat u/2.
The actual moment map therefore yields
Delta_g u=(exp(2u)-1)/2 with the maximum-negative Laplacian convention.
Smoothness, no physical boundary/source, a compact core and uniform
zero limit at every end force any positive maximum or negative minimum
into the interior, contradicting that equation. Hence u=0 in that
class, consistent with h=1-2udot, f=exp(u) and the radial equations.
This does not remove the old neutral modulus, other holomorphic orbits,
two-field backgrounds, magnetic phases or changed ends.

The paired B=J(partial_t+K) has constant J and varying Hermitian K;
formal squares retain Kdot and tr K=(1-h)/2. The actual-response
unitary transport remains valid because J is constant. For a specified
gapped limiting tail, conservation of xdag v and the stable dimension
count justify complementary stable spaces; evolving a solution
subspace gives Pdot=-(I-P)KP-PK(I-P), not the instantaneous sign rule.
The inherited rational-rotation comparator independently retains both
decaying slots, current nullness and integrated norm 1/2; it is not
a stationary radial vacuum. Finally, compact-core ellipticity/Rellich
and uniformly small tail multiplication prove graph compactness only
for bounded decaying zeroth-order changes on the same metric, bundle,
charged decomposition and graph domain. These assumptions cannot be
replaced by a raw Q8 trace-space analogy or extended to altered ends.

These source arguments support the bounded analytical claims within
their declared hypotheses. The finite controls cannot certify global
PDE existence, every inherited spectral theorem, physical field
identification, vacuum selection, SM3, anomalies, values or gravity.
No physical-input row is paid and historical noncompliance is unchanged.

This package explicitly lacks a complete executable specification,
admission-wrapper binding and its engineering certificate, fresh-output
custody and exact main acceptance. This review grants **no execution
approval** and must not be converted into an APPROVE_EXECUTION artifact.
No science import, collection or run is licensed by its verdict.

## Exact SHA-256 bindings

All paths are repository-relative. All seventeen inventory pins matched
their reviewed bytes and candidate-commit bytes. Additional governance,
status and global-source hashes bind the actual extra readings. The
probe.py hash binds its whole file while its reading scope is selective
as stated above.

```text
1b5b2fcbbea3cf90a0e09fe1ea3605b10a170524680b73bebefc57897a061ec6 reports/physical_bridge_2026_09_05/word_architecture_audit_2026_10_17/verification_radial_flow_v2/DESIGN.md
0da1da5d73f777ae65a130db68a89eaf40973b4a2b562ac2f21569eb7243c988 reports/physical_bridge_2026_09_05/word_architecture_audit_2026_10_17/verification_radial_flow_v2/checks.py
a91af2e81589fa6d1537524a0452b3bb9bdc18faa1c8383e3071680b58286497 reports/physical_bridge_2026_09_05/word_architecture_audit_2026_10_17/verification_radial_flow/DESIGN.md
ad60f47e14c9671277e8888202451a2db7b414b58d48ed347cf735b2eff9d7d5 reports/physical_bridge_2026_09_05/word_architecture_audit_2026_10_17/verification_radial_flow/checks.py
e338291fb845b312a8b8fff3c08bee9e4bb35f8da46cf4a90f76b07ecffa64d7 reports/physical_bridge_2026_09_05/word_architecture_audit_2026_10_17/verification_radial_flow/SOURCE_REVIEW_INVENTORY.json
12587b873591b8e44831e320fab0eef579c90c959c0a7fb741d226d68892cdbb reports/physical_bridge_2026_09_05/word_architecture_audit_2026_10_17/verification_radial_flow/review/INDEPENDENT_REVIEW_2026-10-25.md
4aea62c433fe3b4b273d9e0a5480e347b0fe5d5c80b8fe6bbb4d9ad9980796c2 reports/physical_bridge_2026_09_05/word_architecture_audit_2026_10_17/verification_radial_flow/REVIEW_REPLY_2026-10-26.md
5f6a7b9eb397028741fbbf2c9ab195f5479e544dcfb796df011b037890e4489d reports/physical_bridge_2026_09_05/word_architecture_audit_2026_10_17/SAME_ACTION_RADIAL_VACUUM_FLOW_AND_RESPONSE.md
58d6162fa55638ffa4eddab2b0ed6b2e9081074950922b0af396cdb1996dcb45 reports/physical_bridge_2026_09_05/word_architecture_audit_2026_10_17/GLOBAL_CARTAN_AMPLITUDE_MATCHING.md
c505823ce2b934b9737780acf3d6bbbeeb8482613b7ecc76a2ece58b1c2ebc4f reports/physical_bridge_2026_09_05/weave_curved_action_2026_10_08/PROOF.md
22a1a213a739348eddc3431f5d022bcd8f604f3bba58febfe48ef044d6f806b9 reports/physical_bridge_2026_09_05/weave_graded_condensate_2026_10_08/PROOF.md
6e7254ff85f2465d077bd90b1f4182e6eb916fc43e244c5b6554fdc9fe136d80 reports/physical_bridge_2026_09_05/weave_graded_condensate_2026_10_08/probe.py
cda1b1e3211c3d01b06e92258f43d285933000194efc1628c2272ac7fd00257f reports/physical_bridge_2026_09_05/weave_graded_condensate_2026_10_08/reference.py
99442d5a50d19ba99abed1d9f733cf085d56cdf80acbbee904bed8061f561f6c reports/physical_bridge_2026_09_05/weave_sm_parallel_2026_10_08/PROOF.md
fbb0f0d51fcf915a1b3b5203d03a8d1f6df7011b5d8f00aa4be3223a14440977 reports/physical_bridge_2026_09_05/weave_cusp_condensate_2026_10_08/PROOF.md
a9a2e595d6594483a8695da881ce80bf311425eecf72de3da543f3fe4fb5f862 reports/physical_bridge_2026_09_05/weave_neutral_stability_2026_10_08/PROOF.md
ac3dd9f39d34610594e2e77552857533b08932bbeeb3b61a41ee714e2ee9968e reports/physical_bridge_2026_09_05/word_architecture_audit_2026_10_17/ACTUAL_GRADED_CUSP_RESPONSE_AND_STATE_SCOPE.md
b096a241ffbbe366a619119f0e9e8f2a0f0f2876bdbd2e9a8540fa377e4e10ff WORKING_RULES.md
425edf259fb2631428f0842f4be06c18eae0e64d58f1a9952bb26dfabe05dd12 reports/physical_bridge_2026_09_05/word_architecture_audit_2026_10_17/GOAL_CONTRACT.md
d0787ef5d56cd9d4d1d14ba9b4b7bea7e03019b227c735697ce02fc0e4ed9d89 reports/physical_bridge_2026_09_05/word_architecture_audit_2026_10_17/verification_radial_flow_v2/SOURCE_REVIEW_INVENTORY.json
ed80c54dd17f5c6378f4e8bb0b2b698c06b05927b9adedf28427ea3bff6c5698 reports/physical_bridge_2026_09_05/word_architecture_audit_2026_10_17/verification_radial_flow_v2/REVIEW_STATUS.md
1acc2f85f7a655a7d67af4f029f11197f3f2a3d6c3d54c11e321cbe7b72b3e9d reports/physical_bridge_2026_09_05/word_architecture_audit_2026_10_17/verification_radial_flow/REVIEW_STATUS.md
05a4f2423a6ba030d8f041c0a3236c32117f1ee78b69feb2cc71ce5050b03e55 reports/physical_bridge_2026_09_05/weave_global_condensate_2026_10_08/PROOF.md
```

The inherited staged binary diff had SHA256
`1b1174453bc7f3159582386919a082dc803c0e9d63323a375872d4d346ba3786`
before this note was written and was unchanged afterward. This is a
preservation check, not a review or certificate of those staged files.
