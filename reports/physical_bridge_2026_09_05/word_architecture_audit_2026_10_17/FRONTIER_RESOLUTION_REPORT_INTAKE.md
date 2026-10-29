# Intake: the proposed triplet, index and gauge frontier resolution

October 19, 2026. Read-only analytical audit of the owner's attachment
and its actual linked producer/output. Not an independent numerical
reproduction, experiment admission, accepted correction or input payment.
The report contains useful candidates, but its claimed seven discharges
are not supported as stated. Failures below are scoped to the inferences
and checks identified; they do not exclude the broader programme.

## Evidence read and fixed

The complete 206-line attachment, complete 591-line Python producer and
complete JSON output were read directly. No imports or producer were run.
Their paths and SHA256 values are:

- Owner attachment: `/Users/dri/.codex/attachments/0ba20679-57c0-4c0c-b780-89d88625e9ed/Pasted text.txt`;
  `afd4e77aa90c5dfff0e8c75fbe330d2eb219dcabf06e1e90cc8caa304b565cc7`.
- Producer under `/Users/dri/.gemini/antigravity/brain/4105bba8-c6de-44ce-82a5-c678bd0cc545/scratch/verify_triplet_index_gauge_frontier.py`;
  `8ae04bc2c8849a287638223172a6ca4d1e4f1942b625941d1e1959576cb2f8a4`.
- Output beside it, `verify_triplet_index_gauge_frontier.json`;
  `97793021d9a2387d409c38525c000f9c3bfd66392c731ee67fdca7bc9caa0c8d`.

These are intake byte identifiers, not a preregistration or verified
execution seal. The producer imports a mutable absolute FRONTIER at
`/Users/dri/origin-axiom/frontier`; its dependency closure and runtime
are not pinned by those three hashes. Its import helper suppresses stdout
and executes imported modules. It is not a self-contained proof package.
The current B1606 local-boundary producer was also read in full there;
B1617's lift and composition definitions were inspected directly.
The existing branch analytical proofs were compared at `a57847e5e`.

## 1. Preserve the tensor/theta candidate; do not claim the sheaf recovered

The numerical intertwiner search offers a candidate factorization of
the restricted six-dimensional local action into a triplet and doublet.
The supplied output reports small residuals and appropriate character
twists. That is worth retaining and comparing with the existing
[common-register factorization](MATTER_AND_BOUNDARY_COMMON_REGISTER.md).
It is not evidence for identifying the local module with cohomology.

The proposed theta-dependent maps have a legitimate pointwise algebraic
idea: for any nonzero doublet v, the maps I3 tensor v and
I3 tensor (v^T epsilon) have ranks three, compose to zero and give
an exact sequence of vector spaces. No special theta identity is needed
for v^T epsilon v=0. To obtain the claimed sheaf sequence, however,
one must establish automorphy in the actual source/target frames,
all lifts and cusp extension data, and identify these maps with the
actual puncture evaluation and connecting maps.

The producer tests pointwise ranks at ten sampled tau values and
names the resulting Boolean `exact_everywhere_on_H`. That label
overstates its numerical check. It does not test the theta maps'
automorphy or establish their identity with the withdrawn geometric maps.
The analytic nonvanishing argument is a separate proof duty, not supplied
by the ten samples. Correct Euler arithmetic is not sufficient to
construct or identify a short exact sequence.

## 2. A differential expression is not a verified four-dimensional index

Writing sqrt(2)(dbar+dbar*) is a useful candidate differential expression.
The report has not specified and proved the required metric/end behavior,
closed operator domain, Fredholmness and comparison with its coherent
sheaf Euler characteristic on the noncompact punctured/cusped surface.
The square root of the canonical bundle and its descent require proof;
writing lambda^(3/2) does not alone provide a canonical spin structure.

Degeneration of the displayed Leray spectral sequence, when its
cohomological-dimension hypotheses apply, does not determine the higher
direct-image sheaves. In particular the two asserted direct-image
identifications are load-bearing additional claims, not consequences
of the vanishing of d2. The report mixes the open surface and a
compactification without completing that comparison.

The script assigns
`Leray_E2_degeneration_d2_vanishes_identically: True` literally.
It then subtracts the existing one-dimensional modular Euler values and
calls them `ind_4D_Dirac`. It neither constructs nor checks a
four-dimensional boundary-value problem. Its agreement with
n(dim Lambda-3) therefore does not verify the missing bridge.
Even that conditional formula retains n; nothing here derives n=1.

## 3. The parity exclusion transfers between inequivalent actions

This is the central error. The script obtains B_V2 and B_V4 from
the commutant of the LOCAL matrices S_L6,T_L6. But its positive-word
matrices come from W.ML,W.MR on COHOMOLOGY. It then applies the
cohomology parity matrix Pa to the local B_V2 projector. Equal
dimensions and coordinates do not make these the same representation.

In the raw local frame each true generator acts by a permutation of
three doublet blocks together with the SAME g on every block. Therefore

    W2={(v,v,v)}, W4={(v1,v2,v3):v1+v2+v3=0}

are invariant under each generator and hence every positive word.
This exact proof appears in
[the coherent local-action analysis](COHERENT_WORD_LIFTS_AND_LOCAL_BOUNDARY.md).
Conjugating by the fixed block frames gives precisely B1606's
local modules. A parity sign without the local quaternion factor
is a different action. The report does not derive a replacement.
Thus its computation on V does not eliminate the two middle local
boundary choices or force plus/minus three in that problem.

The exact positive-word local calculation is especially direct:
g_L=(1+i)/sqrt(2), g_R=(1-j)/sqrt(2) give
g_R g_L^2 g_R=i and g_L g_R^2 g_L=-j. Both word permutations
are identity on parity labels. Their raw local actions are therefore
I3 tensor i and I3 tensor (-j), preserving both W2 and W4.
They anticommute rather than becoming the two commuting bare
cohomology parity signs. This supplies a constructive countercheck
to the claimed boundary exclusion, not just a numerical discrepancy.

There is also an explicit arithmetic slip in the reported count matrices.
For its displayed L=[[1,1],[0,1]], R=[[1,0],[1,1]], direct multiplication
gives R L^2 R=[[3,2],[4,3]] and L R^2 L=[[3,4],[2,3]], not
[[1,2],[2,5]] and [[5,2],[2,1]]. All four are identity mod 2,
so this slip does not by itself refute the mod-2 observation. The
inequivalent-action transfer, not that typo alone, defeats the exclusion.

## 4. A character repair is a candidate, not a complete physical spin proof

The section-sign diagnosis and character twist can be useful. Multiplying
an old triplet by an eta character can cancel its central sign and produce
an ordinary octahedral representation. Numerical generator relations
are evidence for that restricted representation claim.

Our existing coherent lift E already distinguishes a word operation,
its SU(2) implementation, the local action and the cohomology action.
The report must place its twist within that SAME full structure and
geometric automorphy, rather than identify a finite character with a
globally descended spin bundle by definition. Its claim of a canonical
physical spin coupling is not proved by the finite relation checks.
This does not reinstate the old arbitrary-section sign as a valid no-go.

## 5. Gauge completion: retain conditional positives and the global check

Changing the embedded module from irreducible local L6 to reducible
T plus Tbar can change the commutant, and an additional central character
can remove invariant exterior-power sectors. The reported dimension-12
centralizer is worth independently certifying for that specified model.
It does not derive the embedding or central twist from the principle.
The report itself correctly recognizes that its J generator lacks
the up-antiquark and charged-antilepton hypercharges.

The Z2 identity (-I6,-I2,I3)=1 can preserve the weak ADJOINT algebra.
But (-I6,+I2,I3), equivalent to (+I6,-I2,I3), is NOT the identity
on all E8 sectors: it acts as minus one on the displayed weak-doublet
sectors. The script confirms Delta^4_M6=-I6 and assigns the claimed
global-center repair Boolean literally. Weak-root survival is not
by itself proof of the required full lifted relation. Any additional
spin/gauge identification must be given, not assumed.

There are further presentation errors to repair: SU(6) times SU(2)
mod Z2 is a SUBGROUP of E6, not E6 itself (dimensions 38 versus 78).
With the report's displayed branching, its proposed Z6 generator
(exp(i pi/3)I6,-I2,exp(-2 pi i/3)I3) acts on (6,2,3) by
exp(2 pi i/3), not one. Reversing that SU(3) phase repairs this
kernel convention; its cube is still the stated valid Z2 element.
Neither presentation error alone disproves the branching construction.

## 6. Hypercharges are present after the split; a chiral spectrum is not

The explicit traceless diagonal Y has the stated charges on the chosen
6 and exterior-square sectors. These additions can be checked directly.
This is a useful conditional embedding, not a derived full SM.
The producer enters that diagonal and the colour/lepton split by hand.
A cusp theta line does not alone derive that split, its physical
normalization or survival of the required generators on the whole domain.

The displayed 27 still contains seven components beyond one 16 and
the four Higgs-doublet components: Lambda^2(bar4) has six components
and Lambda^2(bar2) one. They are not accounted for in the selected list.
Moreover 248 contains BOTH (27,3) and its conjugate. A triplet dimension
does not select three net chiral zero modes from that full field roster.
The same physical operator must determine both, plus all boundary modes.

The unimodular determinant can eliminate a particular determinant-based
mixed modular anomaly contribution. The script hard-codes k_T0=0
and the four resulting zero entries; it does not perform a full anomaly
analysis of a physically derived spectrum and action. The report's
untwisted electromagnetic cancellation is a different restricted check,
not cancellation of all gauge/global anomalies of the completed model.

## 7. Larger words: exact quaternion positive, unearned dynamics

There is a sound conditional statement here. In the class-two word
quotient, [u,v]=z^(m q-n p). Reading z as -1 in Q8 proves

    [rho(u),rho(v)]=-1 iff det(counts(u),counts(v)) is odd.

This follows exactly from
[the relative-area derivation](RELATIVE_WORD_AREA_AND_PHYSICAL_END_SCOPE.md).
It supports investigating beyond determinant-one substitutions.
It does not show that satisfying one quaternion-point test earns every
foundational admissibility duty, or makes an endomorphism a geometric
automorphism. Larger word maps may be legitimate new candidates.

The rest is limited sampling: positive words of length at most four,
a bounded Sturmian classification, the first eight selected restricted
blocks for the group search, and the first twenty candidate words for
pair interference. The latter loop has at most 20*19=380 ordered
distinct-pair entries. It cannot produce the report's counts 2544,
3354 or 3496; those require other unprovided run evidence.

The actual JSON also says `sturmian_strictly_chiral_preserving: false`,
with residual 2.486212907022135e-10 versus its 1e-12 threshold.
That may be numerical conditioning, not a mathematical counterexample;
it must be explained rather than described as a passing locked test.
The routine sets `discrete_hierarchy_emerges_from_interaction: True`
literally, and does not check the reported cup-product identity.

A sum M1+M2 is a supplied superposition rule. A block between the
two algebraic triplets is not thereby a spacetime chiral Dirac mass.
An action, admissible amplitudes/phases, physical fermion domain and
kinetic normalization are still needed. Split singular values can be
an algebraic positive without being three predicted particle masses.

## What this changes for our work

Keep the tensor/theta candidate, central-character gauge alternatives,
explicit conditional charge embedding and odd-determinant word extension.
Prioritize the theta maps' actual equivariance and their geometric
identification; compare every proposed exclusion using its TRUE local
action, and require one physical operator/action before an index claim.

Do not change the paper or mark its priced-input rows discharged from
this intake. The report is neither wholly worthless nor a verified
resolution: it mixes useful constructions, missing bridges and concrete
checking defects. The latest analytic work here also remains pending
separate review. Frozen v3 and the preserved historical failures are
unchanged; no new scientific execution or publication pass is claimed.

## Follow-up: untracked B1672 and its added locks

The same producer was subsequently located in the other local checkout
at `/Users/dri/origin-axiom/frontier/B1672_discharging_triplet_index_gauge_frontier/`.
Its hash matches the scratch producer above. That checkout's HEAD is
still `2e5716bd9`; Git reports both the B1672 directory and its new test
file as UNTRACKED. Its FINDINGS author/verdict text is received content,
not evidence that main committed or independently accepted this result.

The complete FINDINGS and added test file were read, without execution.
FINDINGS SHA256 is
`0bf9661ec063986f6e15c5b51dc0602aab1544562716489f19c0b300f62d21f5`;
[the historical received test, subsequently archived by main](https://github.com/originaxiom/origin-axiom/blob/5a16562acdce80a7d99a658ffe7c5c307a08781b/frontier/B1672_discharging_triplet_index_gauge_frontier/verification/as_received/lock_as_received.py.txt) SHA256 is
`bd5b4e056588f0d98ef2b1f634545c74aac7b1f5efe063197a88c59bb6ea86af`.

The purported live local-domain check does not construct the actual
B1606 generator action or its invariant doublet. It chooses a coordinate
rank-two projector and manually enters a different `Pa_L6` that mixes
it. That verifies the entered example, not the required representation.
The spin-sign check likewise assigns its desired matrices directly.
Its explanatory comment even equates exp(2 pi i) with -1; the actual
character on Delta^4 needs the correct word exponent, not that equality.
The weak-root test only checks that -I2 commutes with the SU(2) adjoint,
not the full E8 relation. These are insufficient locks for the claims.

FINDINGS adds an assertion that a minimal nontrivial divisor fixes n=1.
No proof of its quoted integral cohomology group or of a physical
minimal-divisor selection is supplied by the inspected producer/test.
Selecting a generator of a mathematical integer group is not in itself
a law forcing the physical background to carry that generator.

The next [theta-sequence derivation](THETA_SEQUENCE_REPAIR_AND_MONODROMY_DUTY.md)
does recover an exact, weight-dependent sequence on the restricted
Omega quotient, with explicit frames and hands. Its full-E extension
fails on the modulus/lattice-only base by the J_c stabilizer sign.
This is a useful positive and a precise next monodromy duty, not a
global rejection of theta-dependent puncture maps.


## Citation provenance correction, October 29

This navigation-only correction replaces a checkout-relative citation
with its verified immutable source. The original text remains at commit
4572f758c4463a0926b102ce65b8be5690a3aa06. Mathematical content and historical read/review
scope are unchanged. No new scientific reproduction or acceptance is
asserted. The dated repair receipt records both document hashes.
The received test was untracked when originally read. Its later archived
copy has the original recorded hash; main's replacement live test is a
different artifact and is not substituted for that historical evidence.
