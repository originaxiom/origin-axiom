# External audit intake and the corrected W f1 witness

2026-11-09. The owner supplied an exploration-seat audit summary and
will provide its commit or script/output paths. This intake personally
verifies the reported Clifford sign correction by hand against the exact
AGY source. The numerical residuals remain attributed to the external
summary while its producing artifacts and provenance are pending.

AGY source is CENTRALIZER_COMPONENTS.md at
6e9683ab93f438971a0da5b10107acc3cacafc31,
SHA256a0e86b7164e401498869fce468a5fcfad140ca28529e86d721b3dffab7673075.
The same bytes are present at the current AGY head
be7047fb6d29346d0fce3818c2cae05ec5ca33b9. Lines86 and88 retain
the mistaken witness sign. The physical seat's earlier scoped hand
review at8ff6329c0fc7e8c5a3d0e1772e6f35c16a7198a5 missed this
specific sign. This addendum records that review failure and its repair.

## Direct Clifford derivation

Use the declared positive Euclidean Clifford convention. The products
W and U each contain five disjoint orthonormal vectors, with U^2=1.
Let omega10=W U, omega6=f1 f2 f3 f4 f5 f6 and
omega16=omega10 omega6. Then

    omega6^2=-1, omega6^-1=-omega6,
    W=omega10 U=omega16 U(-omega6).

The even product omega6 commutes with the disjoint odd product U.
Within its own six-space, however, omega6 anticommutes with each f_j.
For f1 there are exactly five distinct vectors to cross. Therefore

    omega6 f1=-f1 omega6,
    (-omega6) f1=+f1 omega6,
    W f1=omega16 U(-omega6)f1=omega16(U f1)omega6.

Write pi for the faithful semispin map into E8, with kernel
{1,omega16}, s=pi(U f1), C=pi(omega6) and Zeta=pi(-1).
The corrected identity in E8 is

    pi(W f1)=s C.

The historical expression pi(U f1(-omega6)) is instead

    s C^-1=Zeta s C.

Thus the two expressions agree on120 and differ by a sign on128.
Keep scalar -1 in Spin16 distinct from a uniform matrix minus sign
on all248 directions. Its E8 image is Zeta, with actions +I120,-I128.
Equivalently pi(-omega6)=C^-1=Zeta C, while pi(omega6)=C.

Both omega6 and -omega6 belong to Spin6. Consequently both displayed
representatives lie in the same outer component s C0. The two-component
classification and the correctly typed phase witnesses retain their
previous hand scope. The corrected W f1 element is the existing s C
outer witness from the phase classification.

CENTRALIZER_COMPONENTS_W_F1_SIGN_2026_11_09.patch supplies the exact
two replacements against the named source bytes. Apply it in AGY's
next substantive checkpoint and publish the new source hash. Preserve
the original proof and earlier review in Git history.

## Numerical report received from the exploration seat

The summary reports a full120_so16 plus128_S+ matrix construction,
residuals below approximately3.4e-14 for the central identities, the
repaired k0=f3 f5 and g1=(f1 f2)s witnesses, the failed k_bad and h3
controls, coherent K_h(N)=I, and the fourth-root character bridge.
It also states that SL2(F5)/SL2(Z) checks concern B1855 through B1857,
but supplies no per-claim source/output record for that part yet.

One reported failure size has an exact hand consistency check. If
(A h3)^2=Zeta K_pi, its difference from K_pi is zero on120 and twice
a unitary matrix on128. Hence the full Frobenius norm is

    2 sqrt(128)=16 sqrt(2).

That matches the reported value approximately22.63. This hand dimension
check does not reproduce the external matrix builder or its residuals.

The report concerns central/group identities and finite representation
controls. Centralizer connectedness, exhaustion of continuous conjugacy
classes, all-word extension and complete physical operator/domain
statements retain their respective analytical proofs and quantifiers.
Representative matrix equalities alone leave those universal duties
to their established arguments.

## Artifact intake still required

Record the external code commit or immutable file hashes, exact target
source commits, commands, environment, raw outputs and first-failure/
repair history. Read the construction of the Clifford generators,
positive-chirality selection and the source A,D,H lifts, including
the image of omega16 and scalar -1. Inspect whether the expected right
sides were independently reconstructed, and retain the deliberate
k_bad/h3 failures and this W f1 sign failure in the evidence.

For the character bridge, bind the actual quotient and normal-generator
conventions and separate the finite checks from the all-word proof.
For B1855-B1857, identify each tested proposition, operator, norm and
control before assigning coverage. Authorship and the relation to the
sealed prospective designs must be recorded for an independent-review
claim or any project admission decision.

No external script was executed or imported by the physical seat in
this intake. Existing prospective controls retain their recorded UNRUN
status. The external reported execution gets its own evidence record
when the artifacts arrive. The immediate mathematical contribution is
the verified witness repair and its preserved provenance.
