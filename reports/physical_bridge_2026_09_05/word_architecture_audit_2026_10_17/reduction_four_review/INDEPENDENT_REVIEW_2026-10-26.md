# Independent source review of four conditional reduction arguments

Date: October 26, 2026. Kind: source_review_only.

Verdict: **NO_BLOCKING_SOURCE_ERROR_FOUND_WITHIN_REVIEWED_SCOPE**.

Candidate: c4d4ec8b58821f9382d28c678ba408318bca2bf0, on
audit/physical-bridge-2026-09-05. The four reviewed argument files and
the scientific dependencies bound below match the candidate and the
working-tree bytes personally read. This is my non-authoring judgment,
not an author attestation, banking certificate or execution approval.
I wrote no reviewed argument or scientific source.

The authorized population is exactly card 01, the two-spin moment-path
argument, card 02 and the common-Clifford-symbol argument. The later
Hodge geometry, full-mode elimination and interacting dressed-domain
notes are outside this review. No conclusion in those successors is
certified by this verdict. Main acceptance and prospective scientific
admission remain separate duties.

## Method, custody and actual reading coverage

I personally read all four candidate argument files completely. I read
WORKING_RULES.md, the complete review-duties checklist and the relevant
GOAL_CONTRACT sections on scope, input payment, verification, publication
and recent reduction work, with selected historical sections for context.
I do not claim an audit of every historical contract entry. During this
review the parent committed a later out-of-scope note and appended
planning/authorization status. Those mutable files now differ from the
candidate; their changes were inspected and did not change the four
scientific arguments or expand my authorization. Candidate hashes below
bind the version used for the review. HEAD observed later was 1d06025a1.

Complete personally read source proof bodies:

- weave_curved_action, weave_physical_mass, weave_graded_condensate,
  weave_neutral_stability, weave_form_parent and weave_companion_roster,
  all dated 2026_10_08;
- spinor_uniformization_joint_2026_10_14,
  weave_registered_embedding_2026_10_13 and weave_field_map_2026_10_14;
- SAME_ACTION_RADIAL_VACUUM_FLOW_AND_RESPONSE,
  GLOBAL_CARTAN_AMPLITUDE_MATCHING,
  ACTUAL_GRADED_CUSP_RESPONSE_AND_STATE_SCOPE, and
  ACTUAL_CUSP_WEYL_RESPONSE_AND_INDUCED_NORM.

Producer reading was substantive but has these limits. I read the curved
probe's universal_checks, matrix_checks and curvature_checks, their
helpers and the beginning of run through the cutoff predicates, not its
entire final packaging. I read the curved reference.py completely. I
read physical-mass probe.py and reference.py completely as source text;
their imported predecessor dependency tree was not independently read
or executed in full. I read graded reference.py through its polynomial,
weighted-adjoint, block construction and dual-isometry setup, not its
entire final predicate/output assembly. A whole-file hash of a selectively
read file does not enlarge this coverage. Existing kernel, anomaly,
root-population and global spectral claims are not freshly reproduced
merely because their source files were read.

I used text reading, Git metadata and stdlib hashes only. No scientific
module, SymPy engine, symbolic evaluation, test collection, finite matrix
script, numerical experiment or old producer was imported or executed.
The algebra below was reconstructed by hand from the displayed fields,
pairings and derivatives. No new literature source was consulted, and
no whole-repository absence or priority claim is part of this review.
No runtime or exact execution population was reviewed for admission.

## 1. Two-spin Hermitian path: signs, factor two and controlled ends

The compact-reality path is internally consistent. D_a xi is Hermitian
for Hermitian A_a and xi, so A_x'=D_y xi and A_y'=-D_x xi remain in
the actual compact connection. Its complex component is -i Dbar_A xi.
In differentiating Dbar_A q, the -i times -i gives a minus:
the new connection contribution -[Dbar_A xi,q] cancels the derivative
of xi in Dbar_A[xi,q]. The result is [xi,Dbar_A q]. The same holds
for r, while Jacobi gives [xi,[q,r]] for the commuting residual.
This preserves the correct spin line; no S-to-K identification is used.

Direct curvature variation is
F'=D_x A_y'-D_y A_x'=-(D_x^2+D_y^2)xi. For U=[xi,q], compact
adjoint gives U dagger=-[xi,q dagger]. Cyclic trace then gives
Tr(xi[U,q dagger])=Tr(U dagger U) and
Tr(xi[q,U dagger])=Tr(U dagger U). Their SUM is the stated factor
two, positive. Keeping r supplies another positive summand, rather
than an unproved one-field reduction. These agree with the original
metric's real norm 2G on the compact gauge tangent.

The uniform path bounds are adequate under the stated hypotheses.
Bounded xi gives q_s=exp(s xi)q_0 exp(-s xi), and analogously r_s,
with uniform L2 bounds on the finite parameter interval. Differentiating
the covariant gradients gives
(D_x xi)'=i[xi,D_y xi], (D_y xi)'=-i[xi,D_x xi]. A bounded-generator
commutator estimate and Gronwall therefore control their integrated
norms uniformly, starting from the assumed finite gradient norm.

For a compactly supported cutoff the integration by parts leaves
exactly integral dchi.xi.Dxi, with a plus sign. With g=Omega^2 g_flat,
its absolute value is bounded by sup|dchi|_g times the L2(dvol_g)
norm of xi and the conformally invariant L2 norm of Dxi. Finite area
and bounded xi supply the first norm. Integrating in s adds no problem
because the interval is finite and the derivative norm is uniformly
controlled. Both endpoint moments vanish at every finite cutoff.
Increasing-cutoff monotone convergence therefore makes the integrated
nonnegative gauge-tangent norm zero. Smoothness makes each tangent
zero, and the path's displayed field configurations are constant.

I found no missing end term within THESE hypotheses. Importantly, the
proof assumes a globally smooth admitted path, bounded xi, finite source
norms, no physical boundary/source and the stated cutoff control. It
does not deduce those conditions from finite energy, classify general
polar transformations or show existence. A parallel stabilizer may have
xi nonzero and still act trivially on the fields. Equality of these
fields does not erase its possible action on additional measuring or
registered data.

For xi=uH0/2 the integrand reduces to
Tr(H0^2)/4 (|du|^2+Omega^2 u^2 exp(2su)); I recovered its coefficient
using Tr(H0^2)=2Tr(E0 dagger E0). This correctly overlaps the previous
scalar maximum principle without claiming its weaker end hypotheses
automatically imply all new gradient assumptions. The neutral c psi Z
family and nonzero-moment stationary phases are not removed: they have
not been shown to satisfy this fixed-path endpoint comparison.

## 2. Covariant functional classification and the remaining eta

The classification is correct in its EXPLICIT restricted ansatz: constant
C_ij multiplying kappa(Phi_i,Dbar_A Phi_j), two commuting bosonic
spin coefficients and the fixed invariant pairing. Symmetry of C_s,
the product rule and trace invariance give one half Dbar of the symmetric
quadratic. Since d(f dz)=i Dbar(f) dxdy, Stokes gives integral Dbar f
dxdy=-i integral f dz. Thus the primitive -(i/2) integral C_s,ij
kappa(Phi_i,Phi_j) dz has the stated sign and factor.

The antisymmetric coefficient has C_a,12=(C12-C21)/2, giving exactly
eta W0. Expanding the covariant derivative, the two connection terms
combine to -i eta Tr(q[A,r]); neither a second coefficient nor a
discarded mixed vertex is needed. A local gauge parameter's derivative
in the bare Dbar term is canceled by the affine connection compensator
with this same coefficient. The old curved probe checks this derivative
compensator and the full six cubic Hessian terms. Its source does not
merely check constant gauge rotations.

This is NOT a classification of every allowed action. It assumes the
field roster, pairing, one-derivative/bilinear class, locality and constant
coefficients. The note correctly retains these prices. The three symmetric
coefficients are boundary primitives, not universally nonexistent physical
data: a physical finite cut, variable datum or source must retain their
variation unless the actual domain estimate removes it. The note explicitly
does so and does not use a desired boundary count to delete them.

With the old kinetic and gauge maps fixed, multiplying W by positive
eta multiplies its Hessian/F-source by eta and its eliminated F-energy
by eta^2; the D moment sector stays unchanged. For eta>0 the zero-residual
equations are the same. This assertion is about zero-residual vacua,
not equality of all stationary configurations or fluctuations. At eta=0
it would fail, and the note excludes that value.

The E12/E23 control checks by ordinary matrix-unit multiplication:
[q,r]=E13, its norm square is one, and the two self-commutators sum
to diag(1,0,-1), with norm square two. Therefore the density is
1+2eta^2. This is a valid off-shell local discriminator of polynomial
functionals, not a claimed global solution. The old all-four-real-scalar
Yang--Mills identity fixes eta^2=1 in this family because its difference
is 2(eta^2-1)||[q,r]||^2. Positivity/covariance/one successful vacuum
alone do not supply that stronger parent condition.

## 3. The full principal symbol and conditional relative normalization

I compared the new argument with the ACTUAL physical-mass rows, their
bilinear density, trace-dual output conventions and metric isometries.
The derivative rows of M_eta are precisely
(-Dz a/(sqrt2 Omega^2), sqrt2 Dz lambda,
 eta Dbar v/Omega, -eta Dbar u/Omega). Only the last two are W-derived.
The gauge rows do not acquire eta. All background commutators and
derivatives of metric frame factors are lower order, not dropped fields.

Canonical INPUT coordinates (Omega lambda,a/sqrt2,sqrt(Omega)u,
sqrt(Omega)v), with the corresponding output isometries, give two blocks
Omega^-1[[0,-Dz],[Dz,0]] in the declared ordering,
and eta Omega^-1 times the Dbar skew block. More explicitly in the note's
ordering the first block sends (L,A_c) to (-Dz A_c,Dz L).
For real xi, p_z=i xi_x+xi_y and p_bar=i xi_x-xi_y have the same
absolute square. Thus the canonical M-symbol adjoint product really is
|xi|_g^2 diag(1,1,eta^2,eta^2). The doubled Hermitian operator has the
same squared symbol on its other block as well. Polarization then gives
the common Clifford relation exactly when eta^2=1. No conjugate Weyl
species or scalar extreme is silently removed by this principal test.

The eigenvalue ratio is invariant under unitary slot changes. A general
frame change must transport the metric and dual target too; the generalized
symbol retains the same ratio. A common metric rescaling changes one
common factor, not the relative ratio. Conversely every positive eta
still gives an elliptic operator and positive kinetic form, so neither
condition forces a common Clifford symbol. For a complex coefficient
this test constrains only its magnitude. The note correctly leaves phases
and the complete reference/measuring convention unclassified.

I found no blocking normalization error. This earns eta only GIVEN
the existing kinetic/operator map AND the common internal Dirac-type
requirement. It does not derive those physical premises from the
registered architecture, and does not make the full Yang--Mills parent
or a physical SM an automatic conclusion. The common overall action
coefficient is a distinct duty and is not fixed by this symbol ratio.

## 4. Common action factor and response normalization

For S_alpha=alpha S0, alpha>0, with actual fields/domain fixed, its
first variation, kinetic form, Hessian form and boundary work all scale
by alpha. Homogeneous stationarity and the kinetic-dual linearized
endomorphism are unchanged. Canonical fields Phi=sqrt(alpha)phi then
give alpha^(1-n/2)V_n for an n-field vertex, so equality of vacuum
equations cannot establish equality of normalized interacting theories
in fixed hbar/measuring units. The note appropriately avoids claiming
that alpha is universally physical or universally a convention.

I checked the relevant old constant-tail response formulas directly:
M=lambda(H+sqrt(H^2-lambda^2))^-1 and the reconstructed pair
exp(-Qs)(a,-iMa) have norm (I+M^2)/(2Q)=M' in the stated trace.
At zero this is (2H)^-1. Scaling the bulk pairing while fixing the
source coordinate and trace metric multiplies the Green form by alpha.
Taking Gamma1_alpha=alpha i b therefore gives M_alpha=alpha M and
M_alpha'=alpha gamma dagger gamma with the old bulk dagger. The same
scaled norm follows by direct reconstruction. A simultaneous rescaling
of both trace coordinates can instead retain the old M matrix, but
its source identification must also travel. This is consistent, not
an independently predicted normalization.

These checks support card 01's dependence/scaling claims. They do not
independently certify the whole compact-core response, all angular
domains, quantum unitarity or the full physical energy/mass dictionary.
In particular the card does not promote a locally available c_tail
to an established global parameter merely to claim its removal.

## Verdict and limits

The four notes make internally consistent CONDITIONAL reductions or
dependency clarifications within the supplied models. The narrow
functional and path classes are stated, old neutral/other-orbit positives
remain, and no negative is generalized to every generated word or parent.
Their before/after accounts do not compare a raw input count with measured
SM constants. No foundational input or physical SM3/gravity result has
been paid by this review.

No blocking source correction was identified in the reviewed scope.
This verdict is NOT APPROVE_EXECUTION. No new executable controls were
provided for these four arguments; no finite test could certify the
global cutoff hypotheses by itself. Scientific execution, main acceptance,
global domain/physical identification, quantum/anomaly completion and
banking remain separate. Earlier adverse reviews and historical failures
remain unchanged. This note creates only a new review record and grants
no permission to import, collect or run any scientific source.

## Exact candidate SHA-256 bindings

Let W denote reports/physical_bridge_2026_09_05/word_architecture_audit_2026_10_17/
and P denote reports/physical_bridge_2026_09_05/. The following paths
are relative to those exact prefixes. These bind candidate bytes; whole-
file hashes do not upgrade the selective reading coverage stated above.

```text
c3eb303f09f8e693535cb4a867df66b4cf6babf6b506a5eece52f3b11dbce836 W/REDUCTION_CARD_01_PARENT_PROFILE_RESPONSE_AND_SCALE.md
b206f2803136110fe17afa24b32ac40bfc9cb0e54c5e10de8f5536b25815ebf6 W/TWO_SPIN_FIELD_MOMENT_ORBIT_UNIQUENESS.md
5b4307219ec24610ab9f65c2d1dd9a681ed4567522d1b3b02e9ee87444db40be W/REDUCTION_CARD_02_COVARIANT_VERTEX_AND_PARENT_PRICE.md
ff32e832e7ea6bf2cdd7e85cace7469cb8afa2d04596796e815a1aae9e04e478 W/COMMON_CLIFFORD_SYMBOL_AND_RELATIVE_VERTEX.md
5f6a7b9eb397028741fbbf2c9ab195f5479e544dcfb796df011b037890e4489d W/SAME_ACTION_RADIAL_VACUUM_FLOW_AND_RESPONSE.md
58d6162fa55638ffa4eddab2b0ed6b2e9081074950922b0af396cdb1996dcb45 W/GLOBAL_CARTAN_AMPLITUDE_MATCHING.md
ac3dd9f39d34610594e2e77552857533b08932bbeeb3b61a41ee714e2ee9968e W/ACTUAL_GRADED_CUSP_RESPONSE_AND_STATE_SCOPE.md
da4f0b954db49662bf75726bade1503d2e9e1ef7ac07f74793edfdf050eadb12 W/ACTUAL_CUSP_WEYL_RESPONSE_AND_INDUCED_NORM.md
c505823ce2b934b9737780acf3d6bbbeeb8482613b7ecc76a2ece58b1c2ebc4f P/weave_curved_action_2026_10_08/PROOF.md
04fbb6b7ddc23fe2ae56aa24f3df6e9a710f6278363213b8a509b06ace83ef8d P/weave_physical_mass_2026_10_08/PROOF.md
22a1a213a739348eddc3431f5d022bcd8f604f3bba58febfe48ef044d6f806b9 P/weave_graded_condensate_2026_10_08/PROOF.md
a9a2e595d6594483a8695da881ce80bf311425eecf72de3da543f3fe4fb5f862 P/weave_neutral_stability_2026_10_08/PROOF.md
a56dcbb3d4571f466f0a179de0ce843179f90045465a43ba8cea44ec7adab057 P/spinor_uniformization_joint_2026_10_14/PROOF.md
cedd75ade10476f0cf20ff783edd3a4e81caa5196b3b702ede66a066669b360d P/weave_registered_embedding_2026_10_13/PROOF.md
9c496728d230798a4db14841f91fe2ef272720be69950292164b4c697414bbd5 P/weave_form_parent_2026_10_08/PROOF.md
3ac161b2e4418b8826de0926ef853262d2f98ef57a1743a663d0b488f7d153c0 P/weave_companion_roster_2026_10_08/PROOF.md
24cab7e65ddbb8b37c5c8dddb5cde0171e588e7918eb619f54ee8bd53c0332e0 P/weave_field_map_2026_10_14/PROOF.md
dd53ae8840bdaac76e2545296681fcd43314842ac6cd5e302510fc8528786b4e P/weave_curved_action_2026_10_08/probe.py
1b9dc914defe4e38c0d20206c2c40177ca9c72c99073f4a1aa226bc5f481976b P/weave_curved_action_2026_10_08/reference.py
48abceb8f23be7a1097653a49be13bf6126967a2368b6304c2db0b4133bdf124 P/weave_physical_mass_2026_10_08/probe.py
34ac24b07a1463c19d32d36e0bc4208116bdbab6401120333ff39b47d567c285 P/weave_physical_mass_2026_10_08/reference.py
cda1b1e3211c3d01b06e92258f43d285933000194efc1628c2272ac7fd00257f P/weave_graded_condensate_2026_10_08/reference.py
e9856a32165a6fa28312ece8ad3c0789c0dac4df4d6cfa030425dbd948dd8610 W/GOAL_CONTRACT.md
062cb407153e12d30b6201c5e34d1b67d1ba86b0a0aa3b8a78a054e91493b69c W/REDUCTION_ARGUMENTS_REVIEW_DUTIES_2026_10_26.md
b096a241ffbbe366a619119f0e9e8f2a0f0f2876bdbd2e9a8540fa377e4e10ff WORKING_RULES.md
```

The inherited staged binary diff SHA256 before this review's write was
1b1174453bc7f3159582386919a082dc803c0e9d63323a375872d4d346ba3786.
It was unchanged after this note was written. This is preservation,
not review or certification of the staged historical work. No scientific
source, old verdict or index entry was edited; no commit or push was made.
