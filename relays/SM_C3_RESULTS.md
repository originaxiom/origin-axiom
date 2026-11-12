# SM-C3 closed: the fork lane's four exact packets (register row P-057) — four REPRODUCED, two claims CANNOT CHECK

*Closes the card `relays/cards/SM_C3_fork-lane-four-exact-packets.md` (M3 on main's docs/seats/sm.md, main at
0dda7b472). Read: origin/audit/fork-2026-09-20 at 0c6570bab, the folder reports/genesis_root_review_2026_10_11/, as
git objects. The checks and their outputs are in `relays/sm_c3/`, committed before this note (458ab9623, 9c77f2f53,
4f442741b). Firewall kept: the four packets are data-free, and no measured value or held-out target was computed or
compared. No path with agy_ in it was opened: the extraction has 343 files and none of them. Nothing was written on
the lane's branch.*

## The results

Each result rests on this seat's own exact computation (sympy), rebuilt from the definitions in the packet's PROOF.md,
not from its verifiers. A packet with several claims has a result per claim that decides. Every result is conditional
on the source constructions the packet names: the curved parent, W24's embedding, the coefficient modules.

| packet (the lane's count) | claim | result | why, in one line | where |
|---|---|---|---|---|
| matter_line_compatibility (60 predicates) | constant linear mixing of Q and R keeps the fixed interaction exactly for SU(2) | REPRODUCED | UᵀJU = det(U)J for an arbitrary 2 × 2 U; [aQ+bR, cQ+dR] = (ad − bc)[Q, R] and W = ½tr(Q DR − R DQ) scales by det U; with Gaussian-rational witnesses, a unitary of determinant 1 keeps W and the kinetic sum, a unitary of determinant i keeps the commutator's norm and multiplies W by i (the opposing control), and a non-unitary of determinant 1 changes the kinetic sum | `relays/sm_c3/c3_matter_line.py` |
| matter_line_compatibility | a continuous diagonal line coupling has charges (a, −a) | REPRODUCED | HᵀJ + JH = (α + β)J for H = diag(α, β); the plant (a, a) leaves 2aJ and is caught | `relays/sm_c3/c3_matter_line.py` |
| matter_line_compatibility | dual connections carry the pairing; the compensator is needed; same line twice gives 2F | REPRODUCED | covariance with the compensator b → b − θ′ and its failure without it; QR keeps no residual phase; determinant curvature 2F for the same line, 0 for the opposite twist, −12in dA for the modular line twisted alike | `relays/sm_c3/c3_matter_line.py` |
| matter_line_compatibility | uniform scalar multiplication is not a nonzero Lie derivation; ad(Z) is | REPRODUCED | ad(Z) satisfies the Leibniz rule on the sl₂ triple; cI has defect −c[X, Y]; a scalar map uI keeps the bracket only at u = 1 and at the zero map u = 0 | `relays/sm_c3/c3_matter_line.py` |
| puncture_symmetry (2,681 predicates) | the two moves have exactly four invariant subspaces; the commutant is span(P2, P4) | REPRODUCED | exact nullspace of the commutant equations in M₆(ℂ): dimension 2, spanned by P2 = ⅓J₃ ⊗ I₂ and P4; the projectors in it are 0, P2, P4, I and no others | `relays/sm_c3/c3_puncture.py` |
| puncture_symmetry | V2 and V4 have only scalar stabilisers among the flat flavour endomorphisms | REPRODUCED | with Φ = diag(iσx, iσy, iσz) and F_X = Φ(X ⊗ I₂)Φ⁻¹, the X keeping V2, and those keeping V4, form a space of dimension 1, multiples of I | `relays/sm_c3/c3_puncture.py` |
| puncture_symmetry | one sign suffices: D = diag(1, −1, −1) ⊗ I₂ excludes both intermediate spaces; index −3 or +3 | REPRODUCED | D is unitary, of order two and equal to F_X with det X = 1; the (1, 2) block of [D, P2] is ⅔I₂; the commutant of {L, R, D} is the scalars; the plant, a scalar phase in place of D, leaves dimension 2 and is caught; the stipulated dim(Λ₊) − 3 gives [−3, 3]. The criterion for a general unitary U ([U, P2] ≠ 0) was reviewed in the proof, not computed | `relays/sm_c3/c3_puncture.py` |
| puncture_symmetry | interactions need not break the sign, in the SU6 embedding into compact E8 | CANNOT CHECK | the packet keeps the embedding "as supplied" by W24 and does not write it out; its own verifier records E8_embedding_reconstructed: false. Missing definition: the embedding | — |
| puncture_symmetry | the doubled model: the invariant maximal null subspaces are (u, itu) for real t and the endpoint; only the endpoints keep the grading | REPRODUCED | the intertwiners from E to E ⊕ E under {L, R, D} form a space of dimension 2, so each invariant six-dimensional subspace is a graph; the pairing has signature (6, 6); the graph of β is null exactly when β is imaginary (B = 2 Re β u†u′); Γ sends L_t to L₋t | `relays/sm_c3/c3_puncture.py` |
| positive_carrier (8,234 assertions) | the affine path map E is injective on positive words and recovers them | REPRODUCED | all 2,047 positive words of length 0 to 10 have distinct images and are rebuilt by sorting the flow's terms by total degree; the proof's all-length step (one edge at each total degree) was reviewed; the plant, a word altered by one letter, rebuilds differently and is caught | `relays/sm_c3/c3_positive_carrier.py` |
| positive_carrier | every substitution acts by the semilinear formula Φ_f; the golden substitution and its inverse act | REPRODUCED | for σ (a → ab, b → a) and τ (a → b, b → Ba), Φ_f(E(w)) = E(f(w)) on all 485 freely reduced signed words of length ≤ 5, and σ∘τ = τ∘σ = id; the plant, J_σ transposed, breaks it and is caught. The statement for every f and every word was reviewed in the proof: Φ_f is a homomorphism agreeing on the generators. The lane's seven other fixed maps were not run | `relays/sm_c3/c3_positive_carrier.py` |
| positive_carrier | a proper quotient keeps all of this and a nontrivial commutator, so positive-word fidelity does not force a faithful F₂ | REPRODUCED | E([a, b]) = (1, (1 − Y, X − 1)) ≠ 1; [[a, b], [a, b²]] freely reduces to the eighteen letters abABabbABaBAbbaBBA, with no adjacent inverse pair, and E of it is the identity | `relays/sm_c3/c3_positive_carrier.py` |
| cohomology_carrier (3,626 assertions, second run) | the doublet data: A = diag(i, −i), B = [[0, 1], [−1, 0]] generate Q8; H¹(F₂) is 2 per parity, 6 in all | REPRODUCED | A² = B² = −I, AB = −BA, order 8, derived group {±I}; Z¹ = ℂ⁴, and B¹ has dimension 2 because A − I is invertible, for each of the three signed versions | `relays/sm_c3/c3_cohomology_carrier.py` |
| cohomology_carrier | the certificate: r = [c, aca⁻¹] lies in F₂″, and z(r) = 4z(b) once z(a) = 0, so H¹(F₂/F₂″) = 0 | REPRODUCED | ρ(c) = −I, z(c) = (A + I)v, z(aca⁻¹) = Az(c), z(r) = 4v for every parity; ρ(r) = I, so coboundaries vanish on r; r freely reduces to abABaabABAbaaBAA, letter for letter the packet's sixteen | `relays/sm_c3/c3_cohomology_carrier.py` |
| cohomology_carrier | H¹ survives exactly on F₂/F₂‴ (2 per parity), a proper quotient | REPRODUCED | the affine group V ⋊ Q8 has derived length 3: [(0, A), (v, I)] = ((A − I)v, I), [(0, A), (0, B)] = (0, −I), [(0, −I), (v, I)] = (−2v, I), and translations commute; so every cocycle kills F₂‴; z(t) = 0 for every cocycle at t = [r, ara⁻¹] and two more elements of F₂‴; t freely reduces to 54 letters, the packet's spelling | `relays/sm_c3/c3_cohomology_carrier.py` |
| cohomology_carrier | the sign-character control: H¹ is 0 on ℤ², 1 on F₂/F₂″ and on F₂ | REPRODUCED | for each of the three nontrivial characters: dimension 1 on F₂; an affine group with abelian image has derived length 2, so it survives on F₂/F₂″; imposing z(c) = 0 kills it on ℤ² | `relays/sm_c3/c3_cohomology_carrier.py` |
| cohomology_carrier | positive words are kept on F₂/F₂″ and F₂/F₂‴, not on ℤ² | REPRODUCED | E kills r and t, so it factors through both quotients; E(ab) ≠ E(ba) | `relays/sm_c3/c3_cohomology_carrier.py` |
| cohomology_carrier | the lifted six-dimensional move action survives on F₂/F₂‴ with the central projector ranks [3, 3] | CANNOT CHECK | the packet takes the lifted action and its projectors from the packet bundle_transport, which is not one of P-057's four, and does not state them itself. Missing definition: the lifted move action. The equivariance step (F₂^(d+1) is characteristic) was reviewed in the proof | — |

## The lane's verifiers, run as found

The five verifiers were run once each, from a git-archive extraction of the folder at 0c6570bab, with the lane's
recorded command (`relays/sm_c3/run_lane_verifiers.py`, output `relays/sm_c3/lane_verifiers.json`):
- matter_line_compatibility, puncture_symmetry and positive_carrier exit 0. Their output is byte-identical to the
  lane's NATIVE_FIRST records.
- cohomology_carrier's verify.py exits 1 at ('relation kills coboundaries', (0, 0)), the failure its CORRECTION_V2
  documents. The text is identical to the lane's NATIVE_FIRST_PUBLIC.txt except for one caret line, which depends on
  the interpreter's version.
  - This seat's check bears on the correction's diagnosis. ρ(r) = I exactly, so the relation does kill coboundaries,
    and the normalised value stays 4v. That matches the correction's account: an unexpanded comparison, not a changed
    criterion.
- verify_v2.py exits 0. Its output is byte-identical to NATIVE_SECOND.txt.

By § 8 of the protocol, these runs are facts about the lane's code. The results above rest on this seat's own checks.

## The card's planted errors

Six were run, and five were faults. All five were caught:
- (a, a) for the matter lines;
- a scalar phase in place of D;
- a positive word altered by one letter;
- J_σ transposed;
- B replaced by I₂ for the doublet. Its image is abelian, so H¹ on F₂/F₂″ equals H¹(F₂) = 2, not 0.

**The sixth was the plant the card named for cohomology_carrier, and it is not a fault.** The card asked for the
doublet's H¹ with one generator's matrix transposed. But Aᵀ = A, and Bᵀ = −B is itself one of the parity twists, so
every count is unchanged. The card was written before any check, and this was found by the check. It is reported here,
not passed over, and B = I₂ was planted in its place.

## What GENESIS GM4 is offered (the reading is main's, as the card says)

- **matter_line_compatibility** takes the curved parent and its carrier as given (its own flag genesis_parent_derived
  is false). It bears on GENESIS GM4 not at all.
- **puncture_symmetry** bears on GENESIS GM4's conditional puncture only through the stipulated index formula. One
  sign gives ±3, and neither the move invariance nor the index dictionary is derived.
- **positive_carrier:** every positive word, its order, the substitutions and a nontrivial commutator are kept by a
  proper metabelian quotient. So these do not force the faithful F₂ that GENESIS GM4 postulates.
- **cohomology_carrier:** for this coefficient module, the doublet H¹ needs F₂/F₂‴. It is zero on every metabelian
  quotient, and the next quotient keeps all of it. This gives GENESIS GM4 a lower bound on the carrier for this
  construction, not a derivation of it.

## What was not done

- **Two claims are CANNOT CHECK,** for the definitions named above: the E8 embedding, and the lifted move action from
  bundle_transport.
- **The source constructions were not re-derived,** as for SM-C1 and SM-C2. These are the curved parent's action and
  operator, W24's embedding, W27 and W28.
- **The all-word and all-matrix steps were reviewed in writing.** This seat ran its own window on each:
  - the positive decoding for every length;
  - Φ_f for every substitution and word;
  - descent through F₂^(d+1) and its equivariance;
  - the criterion for a general unitary U.
- **The lane's custody records were not checked:** the seals, the hash manifests and the governance runs.
- **Changes to this seat's own code before its in-tree run:**
  - puncture: the scalar-stabiliser test was rewritten as a rank test;
  - cohomology: the plant above was found not to be a fault and B = I₂ was added; the derived-length check and ρ(r) = I
    were added;
  - puncture: the classification (g) was added after the first commit of outputs (9c77f2f53), with the other outputs
    byte-identical.

  No value of the lane's changed.

## How each result was checked (protocol § 12)

| what | how checked | evidence |
|---|---|---|
| this seat's four scripts | computed once; reproduced; expectations committed first; tested against planted errors (5 faults planted, 5 caught; one named plant found not to be a fault, reported) | the scripts and outputs in relays/sm_c3/ (458ab9623, 9c77f2f53), `relays/sm_c3/RUN_LOG.txt`; a clean-checkout rerun at 9c77f2f53 with every output byte-identical (`relays/sm_c3/REPRODUCED_RUN.txt`); the card (65c014f74) committed before the outputs; the PLANTED entries in each JSON |
| the packets' claims marked REPRODUCED | recomputed independently, for the values each row names | the lane's verify.py, verify_v2.py and NATIVE records at 0c6570bab, and this seat's scripts and outputs, which share no code with them. They match value by value where the row says so: the H¹ table, the spellings of r and t, 2,047 and 485, the eighteen-letter word, the commutant's dimension 2, the indices ±3 |
| the lane's five verifiers | reproduced | run again from a clean extraction: four byte-identical to the lane's records, and the first failure identical up to one caret line (`relays/sm_c3/lane_verifiers.json`) |
| the steps reviewed in writing (listed above); the two CANNOT CHECK claims | not independently checked | — |

## For main

The four packets are REPRODUCED, claim by claim. Two claims are CANNOT CHECK, for definitions the packets take from
elsewhere: W24's E8 embedding, and the lifted move action from bundle_transport. The lane's verifiers reproduce as
found, including the documented first failure. One plant the card named turned out not to be a fault; it is reported,
and another was planted in its place. The re-run that P-057 asks for is done. The reading of GENESIS GM4 is main's.
Nothing is needed from main or the lane for this card.

0 of 19.
