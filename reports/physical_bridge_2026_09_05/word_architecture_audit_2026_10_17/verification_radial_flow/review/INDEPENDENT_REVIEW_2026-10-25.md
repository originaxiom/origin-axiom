# Independent source review of radial flow and real Cartan matching

Date: 2026-10-25. Kind: `source_review_only`.

Reviewed snapshot: `332120cac170fadfc3d28280c9227eccbb438c66`, on
`audit/physical-bridge-2026-09-05`. This reviewer did not author the
scientific documents or controls. This review creates only this new note;
it does not change scientific sources, designs, the index or inherited
staged work, and does not commit or push.

Verdict: **CHANGES_REQUIRED for the finite verification coverage as
described**, with **no blocking algebra error found in the analytical
arguments within the reviewed scope**. The two findings below concern
what the proposed controls can actually discriminate. They are not
counterexamples to the radial or scalar global proofs. No scientific
execution is approved. No global physical SM, SM3, gravity, selected
vacuum or completed input payment is certified.

## Method and actual source-reading coverage

I personally read the complete WORKING_RULES.md, GOAL_CONTRACT.md,
SAME_ACTION_RADIAL_VACUUM_FLOW_AND_RESPONSE.md,
GLOBAL_CARTAN_AMPLITUDE_MATCHING.md, verification_radial_flow/DESIGN.md,
checks.py, SOURCE_REVIEW_INVENTORY.json and REVIEW_STATUS.md. I also read
the complete PROOF.md bodies for weave_curved_action, weave_cusp_condensate,
weave_global_condensate, weave_graded_condensate, weave_sm_parallel and
weave_neutral_stability (all dated 2026_10_08), and the complete
ACTUAL_GRADED_CUSP_RESPONSE_AND_STATE_SCOPE.md.

Producer reading was selective, not a claim to have reviewed every old
producer: graded probe.py radial_blocks, spectrum, normalized_coefficients
and their normalization/dual-R assertions; graded reference.py polynomial,
blocks_from_polynomials and their weighted-adjoint/dual-pairing usage;
SM probe.py triple and embedding/grade helpers; SM reference.py use of the
polynomial modules and bilinear isometry; neutral probe.py fourier_block
and canonical_reduction. The source search located those actual functions
before their bodies were read. Old recorded output was not treated as a
fresh reproduction. This is a local source review, not a repository-wide
absence/priority sweep or external specialist review of the old parent.

Only text, Git metadata and file hashes were read. There were no science
imports, collection, tests, numerical experiments, new probes or execution
of old producers. The first hash command failed because the inherited
locale was unavailable; repeating the metadata-only command with LC_ALL=C
produced the hashes below. That failure was unrelated to scientific code.

## Findings requiring changes to the verification claim or a successor

### R1 — test 6 does not independently check the physical Yukawa or dual-R identification

In checks.py lines 161–179, the coordinate calculation reconstructs the
unequal gauge/spin derivative coefficients correctly. But k0 is then an
arbitrary real symbol. The subsequent D2D1 calculation accepts every
constant k0, including a wrongly normalized physical raising map. No R
field, its weight -m-1, trace pairing or cubic-Hessian reconstruction
appears in this method. The generic adjoint calculation in test 7 starts
from an already supplied K and cannot close that physical identification.

Consequently the proposed tests can pass while a claimed physical k
normalization or dual-R dictionary is wrong. The old producer's two
routes give sqrt(2)*sqrt(y)/(2sqrt(y)) =
y/(2sqrt(y))*sqrt(2/y) = 1/sqrt(2), but that is source reasoning retained
by this review, not an independent check performed by this new method.
The design/status language must not imply that a new control establishes
the full physical dual-slot/Hessian normalization. Either narrow the
coverage claim explicitly or supply a separately sealed successor that
reconstructs the actual ladder map, both normalization routes and
trace-dual weight, with wrong-normalization and wrong-dual controls.
This reviewer has not edited or run such a successor.

### R2 — test 8 cannot discriminate the scalar derivative orientations

In checks.py lines 200–232 the extreme branches assert numerical d,
k_lower=-d, squared thresholds and channel counts. They never construct
the scalar B=epsilon*partial_t+c or its unitary transport, and never
differentiate the varying extreme profile. An erroneous first-order
epsilon at either extreme would leave these assertions unchanged, since
constant squared thresholds lose that sign information. Test 7's paired
2x2 J does not instantiate either one-dimensional extreme.

The design's requirement to retain both orientations therefore exceeds
this method's discrimination. It also does not verify the radial note's
varying extremes K_upper=1/2+h*j/2 and K_lower=h*j/2, including their
Kdot terms. Narrow the finite coverage description or add a separately
sealed successor checking the actual scalar first-order maps/transport
and their varying squares, with an opposite-orientation control. This
finding does not reject the formulas: direct source reasoning below
supports them. It rejects treating the current constant-square count as
an orientation check.

## Independently reconstructed analytical reasoning

The parent's moment residual is F+Omega([q,q†]+[r,r†]), with connection
kinetic weight 1/2 and spin kinetic weights Omega. With A_y=0,
F_xy=-partial_y A_x=(Hdot-H)/(4y²). Differentiating E/(2sqrt(y)) gives
i(4Edot-2E+[H,E])/(8y^(3/2)); the same holds for G. These establish
the radial signs and all factors in (2). Hermitian reality, tracelessness
and the peripheral parities are preserved. Product differentiation and
Jacobi give Cdot=C-[H,C]/4 for C=[E,G]. This argument is independent of
the finite 2x2 examples and covers the specified compact Lie algebra.

For the trace polynomial, the E contribution to the real differential
is 2 Re Tr((2E-[H,E])†dE), and analogously for G. Substituting
Edot=(2E-[H,E])/4 gives the coefficient 8 in the speed norm. H contributes
its ordinary positive trace norm. Boundedness is an additional hypothesis:
on a compact trajectory closure P is bounded and the speed derivative is
bounded; finite integrated squared speed plus uniform continuity forces
speed to zero. A subsequence at positive distance from the critical set
would converge to a noncritical point with speed zero, a contradiction.
This proves approach to the critical set, not a single limiting vacuum.
Finite cusp volume alone does not supply boundedness.

The one-triple substitution gives hdot=h-f² and fdot=(1-h)f/2. The
linearization and quadratic remainder in (6) are correct. In the weighted
sup norm with 0<alpha<-lambda_s, the stable convolution and the unstable
future convolution of a quadratic remainder are bounded by constants
times the squared norm. Their difference estimates are small on a small
ball. The fixed point fixes z_s(T)=c and supplies a local decaying tail;
it does not impose any core matching. Bounded profiles and bounded first
derivatives in orthonormal frames have finite end graph/kinetic norms on
this finite-area cusp. That assertion concerns the specified end and
does not invent global solutions.

The real Cartan deformation uses a globally parallel H0 and the actual
spin-valued q0. With *dx=dy and *dy=-dx,
delta A_x=H0*u_y/2 and delta A_y=-H0*u_x/2. Its commutator contribution
to Dbar precisely cancels the derivative of exp(u), while
delta F=-H0*Delta_flat(u)/2. The moment equation therefore is
Delta_g u=(exp(2u)-1)/2, with the maximum convention stated in the note.
On the original finite-type surface, smoothness, no boundary/sources
and uniform zero limit at the end force positive suprema and negative
infima into the compact core, contradicting this equation unless u=0.
For radial u, h=1-2udot and f=exp(u) give exactly the previous ODE.
Thus nonzero local stable tails cannot extend globally in this fixed
real-Cartan orbit and zero-end class. The proof does not eliminate the
old neutral Q0+c*psi*Z modulus, other holomorphic data, two-field
backgrounds, nonzero-moment stationary phases, defects or different ends.
It does not require borrowing a harmonic-map uniqueness theorem.

The parent kinetic rescalings give gauge derivative a=1/2+hm/2 and
spin derivative b=h(m+1)/2. The actual gauge-map and cubic-Hessian
coefficients both give f*e_m/sqrt(2). Since a-b=(1-h)/2, background
fdot establishes kdot=(a-b)k and D2D1=0. The R slot is trace-dual at
r=-m-1: its radial derivative is partial_t-b, not partial_t+b. Its
R-only quadratic operator is -partial_t²+b²+bdot+k², agreeing with
the lower diagonal of K²-Kdot. This is a useful independent sign check.

With adjoints in dt, B=J(partial_t+K), B†=(-partial_t+K)J, so B†B is
-partial_t²+K²-Kdot and BB†=J(-partial_t²+K²+Kdot)J. The trace
(1-h)/2 is generally nonzero. The constant U=diag(I,iJ) still transports
the doubled operator because J is constant even though K varies. The
upper extreme B=partial_t+(1/2+hj/2) has K=1/2+hj/2. At the lower
extreme B=-partial_t-hj/2, J=-1, hence K=hj/2. Both are positive in
the old constant background. Their square formulas follow with their
own scalar derivative signs; no original Weyl species is removed.

For Hermitian K, x'=-Kx and v'=Kv conserve x†v. With convergence to an
invertible constant, the stable dimensions sum to the full coefficient
dimension, so the two stable spaces are orthogonal complements. The
orthogonal-projector derivative is -(I-P)KP-PK(I-P). It describes a
moving solution space; an instantaneous spectral projector generally
does not solve it. For the stated rational rotation, in rotating
coordinates the x generator is [[-1,2omega],[0,1]]: its stable solutions
have second coordinate zero. The v generator is [[1,0],[-2omega,-1]],
whose stable solutions have first coordinate zero. This proves that the
two displayed comparator solutions span the actual stable spaces, beyond
merely checking individual decaying solutions. Both norms integrate to
1/2. At t=0 K²=5I, so the instantaneous norm 1/(2sqrt(5)) is wrong.
This comparator has algebraic convergence and is not a radial vacuum;
the actual small vacuum tails have exponential convergence. Neither fact
licenses a universal instantaneous-sign rule.

For an actual smooth global background on the same metric, bundle,
charged blocks and first-order graph domain, a bounded zeroth-order
coefficient difference tending uniformly to zero is graph-compact:
compact-core ellipticity/Rellich plus a uniformly small multiplication
norm on the tail. The original Fredholm charged index consequently
persists. This is conditional on the unchanged operator/domain and
charged decomposition; arbitrary fields breaking that decomposition
cannot silently be assigned its old charged indices. The note states
those restrictions and does not infer a new zero-mode census.

## Limits of the ten controls and execution boundary

Tests 1–5 provide useful coordinate, Jacobi/reality/parity, trace,
fixed-point and scalar-linearization controls. Their generic 2x2 checks
do not replace universal cyclic algebra or enumerate E8. Test 7 checks
formal paired adjoints/derivative terms of the supplied block. Tests
9–10 are useful exact controls against instantaneous projectors/norms.
None proves nonlinear boundedness, contraction on an infinite interval,
global Cartan matching, geometric bundle descent, essential spectrum or
graph compactness. The design expressly leaves those to analytic review.
In particular the global Cartan successor is outside the ten-pin
inventory; that is honest for this source-review list, not executable
closure for the enlarged scientific scope.

The inventory has ten pins that agree with the bytes inspected. Its own
source_complete_execution_specification is false. It supplies no full
runtime/gate closure, fresh-output custody, wrapper binding certificate,
main acceptance or prospective admission. This note is not an
APPROVE_EXECUTION review and must not be converted to that schema or
used to import/collect/run these tests. P210's earlier review is separate.
The old parent remains a supplied conditional classical theory; this
review neither establishes its foundational physical map nor certifies
all inherited global analytic claims by association.

## Exact SHA-256 bindings

Paths below are relative to the repository root. Complete readings are
identified above; hashes on selectively read producers bind source bytes,
not a claim of whole-file substantive coverage.

```text
b096a241ffbbe366a619119f0e9e8f2a0f0f2876bdbd2e9a8540fa377e4e10ff WORKING_RULES.md
cc0e036e2926f55b6a1a83399fd31994d7cca98c4d6acfffc5ac03267fdb30ce reports/physical_bridge_2026_09_05/word_architecture_audit_2026_10_17/GOAL_CONTRACT.md
5f6a7b9eb397028741fbbf2c9ab195f5479e544dcfb796df011b037890e4489d reports/physical_bridge_2026_09_05/word_architecture_audit_2026_10_17/SAME_ACTION_RADIAL_VACUUM_FLOW_AND_RESPONSE.md
58d6162fa55638ffa4eddab2b0ed6b2e9081074950922b0af396cdb1996dcb45 reports/physical_bridge_2026_09_05/word_architecture_audit_2026_10_17/GLOBAL_CARTAN_AMPLITUDE_MATCHING.md
ac3dd9f39d34610594e2e77552857533b08932bbeeb3b61a41ee714e2ee9968e reports/physical_bridge_2026_09_05/word_architecture_audit_2026_10_17/ACTUAL_GRADED_CUSP_RESPONSE_AND_STATE_SCOPE.md
a91af2e81589fa6d1537524a0452b3bb9bdc18faa1c8383e3071680b58286497 reports/physical_bridge_2026_09_05/word_architecture_audit_2026_10_17/verification_radial_flow/DESIGN.md
ad60f47e14c9671277e8888202451a2db7b414b58d48ed347cf735b2eff9d7d5 reports/physical_bridge_2026_09_05/word_architecture_audit_2026_10_17/verification_radial_flow/checks.py
e338291fb845b312a8b8fff3c08bee9e4bb35f8da46cf4a90f76b07ecffa64d7 reports/physical_bridge_2026_09_05/word_architecture_audit_2026_10_17/verification_radial_flow/SOURCE_REVIEW_INVENTORY.json
1acc2f85f7a655a7d67af4f029f11197f3f2a3d6c3d54c11e321cbe7b72b3e9d reports/physical_bridge_2026_09_05/word_architecture_audit_2026_10_17/verification_radial_flow/REVIEW_STATUS.md
c505823ce2b934b9737780acf3d6bbbeeb8482613b7ecc76a2ece58b1c2ebc4f reports/physical_bridge_2026_09_05/weave_curved_action_2026_10_08/PROOF.md
fbb0f0d51fcf915a1b3b5203d03a8d1f6df7011b5d8f00aa4be3223a14440977 reports/physical_bridge_2026_09_05/weave_cusp_condensate_2026_10_08/PROOF.md
22a1a213a739348eddc3431f5d022bcd8f604f3bba58febfe48ef044d6f806b9 reports/physical_bridge_2026_09_05/weave_graded_condensate_2026_10_08/PROOF.md
99442d5a50d19ba99abed1d9f733cf085d56cdf80acbbee904bed8061f561f6c reports/physical_bridge_2026_09_05/weave_sm_parallel_2026_10_08/PROOF.md
a9a2e595d6594483a8695da881ce80bf311425eecf72de3da543f3fe4fb5f862 reports/physical_bridge_2026_09_05/weave_neutral_stability_2026_10_08/PROOF.md
05a4f2423a6ba030d8f041c0a3236c32117f1ee78b69feb2cc71ce5050b03e55 reports/physical_bridge_2026_09_05/weave_global_condensate_2026_10_08/PROOF.md
6e7254ff85f2465d077bd90b1f4182e6eb916fc43e244c5b6554fdc9fe136d80 reports/physical_bridge_2026_09_05/weave_graded_condensate_2026_10_08/probe.py
cda1b1e3211c3d01b06e92258f43d285933000194efc1628c2272ac7fd00257f reports/physical_bridge_2026_09_05/weave_graded_condensate_2026_10_08/reference.py
432e8fe1ff674f7d72aec6aa54e86ec1769ffda8f8c2ede04d357d93c8286049 reports/physical_bridge_2026_09_05/weave_sm_parallel_2026_10_08/probe.py
54e011b21ec8a0ffe82a0e28c60c559faa666232dab7a38caf52cbf4a69a0048 reports/physical_bridge_2026_09_05/weave_sm_parallel_2026_10_08/reference.py
57a5b7bbe710e7314baf8e85087b34e9a6d2d007d75b530afd6a8c375bc5d46d reports/physical_bridge_2026_09_05/weave_neutral_stability_2026_10_08/probe.py
```
