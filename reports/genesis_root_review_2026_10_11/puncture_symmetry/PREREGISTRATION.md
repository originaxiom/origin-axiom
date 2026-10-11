# Minimal symmetry for the puncture condition

Pre-execution preregistration, 2026-10-11. Prepared outside the research tree during the now-completed certification run; no new verifier has been executed. Path-local packet: `reports/genesis_root_review_2026_10_11/puncture_symmetry/`. No shared bank number is allocated.

## Question and scope

For W24 and W28's specified local puncture coefficient representation, does one non-scalar unitary flat coefficient symmetry, together with the two moves, suffice to exclude the intermediate invariant subspaces? Does the concrete parity sign extend to the supplied compact E8 interacting action at its flat quaternion background?

This is a joint-move statement about the specified six-dimensional local representation, not a census of one thread. It retains move invariance as a premise. It does not infer invariance of an individual modulus-dependent boundary condition from covariance of a family of conditions. The fixed-modulus scope correction in W50 remains in force.

The intended gain is to weaken a sufficient symmetry assumption and show that the available interactions need not destroy the concrete surviving sign. The supplied parent, gauge embedding and physical identification are not derived here. In particular, neither a physical generation count nor the modular cusp unit is selected.

## Prior work and known outcomes

SM pin: `6877cc87d31941a85f139e2f25e5e13694e22ce6`. W24 D0 and W28 E2 already state the two irreducible pieces of dimensions 2 and 4. W28 E4 already states that their flat endomorphism stabilizers are scalar. Its corrected NOTE retains the naturality requirement as stated rather than derived. The proof draft gives exact elementary derivations; it does not claim these older results were absent.

Physical pin: `9e434bfaa63cff9450959d54384e1a6ad969546a`. The form-parent and curved-action packets supply the embedding, complete field roster, interacting functional and domains. The puncture-operator packet separates sheaf Euler characteristic, finite-distance Green data and complete-cusp kinetic domains. The physical-mass packet supplies a separate full four-Weyl operator/domain map. These constructions must not be identified by their dimensions, labels or integer flux notation.

All expected algebraic outcomes below have hand arguments before execution. The prior is high confidence in those conditional algebraic statements, with instrument/convention errors still possible. No expectation of a newly selected physical vacuum or a discharged Standard-Model parameter accompanies a passing run. The new verifier has not been executed; existing sealed physical-mass and end-Gaussian reference programs were separately rerun and are not results of this packet.

## Fixed conventions

- Parity characters in order (2,0), (0,2), (2,2), interpreted as exponents of i on a,b.
- Pauli Z=diag(1,-1), Y=[[0,-i],[i,0]]; quaternion units qi=iZ, qj=iY, qk=qi qj.
- Move words L:a maps to a, b maps to ab; R:a maps to ab, b maps to b. The code reconstructs the parity permutation from these words rather than loading the desired projector.
- Local lifts G_L=(I+qi)/sqrt(2), G_R=(I-qj)/sqrt(2), tensored with the resulting unsigned parity permutations. These are local puncture pushforward matrices, not silently substituted cohomology pullbacks.
- W(a) and W(b) are the parity-twisted doublet direct sums. Phi=diag(qj,qi,qk) identifies this coefficient with three copies of the untwisted quaternion doublet.
- P2=(J3/3) tensor I2, P4=I6-P2. D=diag(1,-1,-1) tensor I2.
- All coefficient inner products are positive standard Hermitian products in these bases. Exact symbolic zero is checked by simplification, not a floating tolerance or unsimplified syntactic identity.
- The illustrative doubled coefficient model uses E plus E, diagonal action U plus U, Green matrix J=[[0,I],[I,0]] and grading Gamma=diag(I,-I). It is a separately supplied local model, not the full physical boundary problem.

## Predictions and rejecting controls

1. Reconstruct L,R and verify unitarity and both holonomy intertwining identities. Check L squared=I3 tensor qi and R squared=I3 tensor (-qj), and the puncture commutator=-I6. A failed word/lift convention stops the interpretation of later checks.
2. Compute the full 36-variable move commutant exactly. Its dimension must be 2, and every returned basis vector must reconstruct from P2 and P4. Verify their ranks, Hermiticity, idempotency and move invariance.
3. Verify Phi's two exact untwisting identities. Solve the symbolic nine-variable conditions P4 F_X P2=0 and P2 F_X P4=0. Each kernel must be one-dimensional and every basis element scalar. The proof, rather than a finite group sample, establishes the universal stabilizer statement.
4. Verify D is unitary, involutive, determinant one and commutes with both holonomies. Its commutator with P2 has (1,2) block 2I2/3. The enlarged commutant must be scalar. Adding a scalar phase instead must leave commutant dimension 2. This distinguishes a useful surviving symmetry from an irrelevant phase.
5. Check common D-conjugation preserves dagger, bracket and trace metric on the complete matrix-unit basis. Retain the nonzero cubic control A=E13, q=E21, r=E32. Its common conjugation must preserve the cubic; transforming only A must fail. These safeguards support the universal conjugation proof, not an independently reconstructed E8 embedding.
6. In the separately declared doubled model, verify the graph (u,it u), for real symbolic t, is null for J, has rank six, and is invariant under the diagonal L,R,D actions. Verify its orthogonal projector exactly. Its grading commutator must have upper-right block -2it I6/(1+t squared), nonzero at t=1. The two endpoint subspaces are graded and null. The real graph (u,t u) must fail nullity at t=1. These checks protect the distinction between symmetry alone and symmetry plus the chosen grading; they neither refute the original graded statement nor certify global selfadjointness or ellipticity.

For unitary U the proof's general criterion is [U,P2] nonzero. The verifier checks the specific D and its scalar-phase control; finite controls are not presented as enumeration of all possible U.

## Analytic and physical scope

The action-extension argument assumes the stated SU6 embedding into compact E8. D commutes with the flat holonomies, so its image gives a parallel gauge transformation. Common adjoint conjugation preserves the invariant metric, bracket and displayed action. At the fixed flat background it preserves compact-support cores and commutes with the kinetic operators, hence preserves graph closures. This is a conditional argument for those specified domains and background, not for arbitrary Higgs phases or end laws.

The finite matrix checks do not certify global PDE regularity, full E8 branching, the complete charged spectrum or a physical index. The independently achieved physical mass map on the other branch remains available; it is not replaced by the doubled coefficient model. The stipulated sheaf index d-3 does not automatically transfer to the complete-cusp kinetic problem.

No empirical comparison or measured constant is used. Passing this packet cannot change the flags for a derived physical index, selected cusp unit, anomaly completion, stable chiral vacuum, genesis-selected parent or achieved TOE.

## Execution and banking discipline

Before execution, finalize the proof and source scope, produce path-local artifact hashes, append the pre-execution seal to docs/SEAL_LEDGER.md, and commit and push this preregistration, proof and verifier on the existing audit branch. Do not execute the new verifier during draft preparation or before that seal. Do not modify the certifying research tree while its suite is live.

The first scientific run must preserve its full output and exit status, including any failure. A correction requires a written diagnosis, unchanged acceptance criteria unless explicitly amended, and a new pre-run seal. Python 3.12 and SymPy are the planned runtime. Syntax-only AST parsing may be used before the seal, without imports or execution of the verifier.

Every declared check must pass; missing output, exceptions, false predicates or duplicate names are failures. A passing finite result supports only its stated algebraic scope. Review the all-input proofs and the operator/domain hypotheses separately. Propose registry links for the exact stabilizer proof, smaller sufficient symmetry criterion and conditional action extension without duplicating W28's existing law or allocating another seat's bank number. The full objective remains to fix genesis and work upstream toward a complete physical theory.
