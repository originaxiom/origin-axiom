# Positive word lifts and the based genesis

2026-10-11. Scope: the faithful free group F(a,b), its positive elementary substitutions with incidence matrices L and R, and their generated monoids and groups. No manifold, field representation, physical parameter or empirical input is tested. A group completion is not assumed to consist of legal forward updates.

The question is whether choices lost by abelianization introduce independent structure into the ruled weave. This strengthens the root's dependency chain; it is not a new model of matter. Expected identities were derived by hand before this seal. B1323 and B1634 were read; this is not a blind verification or a novelty claim.

## Conventions and finite tests

Words use a,b,A,B, capitals denoting inverses. Composition is f after g. J_w(x)=w x w^-1. Matrices have the exponent sums of images as columns.

- L0=(a,ab), L1=(a,ba); R0=(ab,b), R1=(ba,b). Positivity here means literal words with no inverse letters, a stronger condition than nonnegative exponent sums alone. These are predicted to be the complete possibilities for those incidence matrices.
- C1: all four are automorphisms, with two-sided inverses (a,Ab), (a,bA), (aB,b), (Ba,b), respectively. Their matrices are the expected shears.
- C2: each pair (Li,Rj) is simultaneously conjugate to (L0,R0), through J_q with q=1,b,A,Ab for (i,j)=(0,0),(1,0),(0,1),(1,1). This is a single coordinate change for both generators, not a separate adjustment on each occurrence.
- C3: c=aBAb is fixed exactly by L0 and R0. Delta=L0 R0^-1 L0 satisfies Delta^4=J_c. Its transported version holds for each pair.
- C4: allowing both variants independently in the group completion gives L1 L0^-1=J_A and R1 R0^-1=J_b. These do not fix c. This is the discriminating control against treating the union of the pairs as one coordinate change.
- C5: sigma=(ab,a), P=(b,a). sigma=L0 P, sigma^2=L0 R1=J_ab (L0 R0), but sigma^2 is not L0 R0 as a based automorphism. It is their common homology matrix and their outer class that agree. sigma^2 does not fix c. This rechecks B1607's explicit up-to-inner qualification, not a new refutation of its computation.
- C6: positive matrix products increase the sum of entries at each appended L or R; finite controls through length 8 accompany the all-length proof. The positive monoid does not contain a nontrivial inner automorphism, for either generator set.

## Analytic work and controls

The accompanying proof derives the all-word intersection for a fixed pair from a direct free-group centralizer argument, not a bounded census or the braid-kernel theorem. It does not prove a physical interpretation or the choice of faithful F2. Unit tests use a second, integer-letter reduction/substitution implementation, explicit inverse and composition-order controls, and incorrect equalities that must fail. The theorem's all-word scope comes from the proof, not from those finite tests.

If any identity fails, preserve the first transcript and repair only under a disclosed new seal. A pass permits the stated algebraic conclusions. It does not permit combining results computed with different base points without transporting all additional data, or assuming that such transport is a physical gauge equivalence.

## Seen first and inputs

Pinned main: `6c148ddd495d133213140995976ff08849793d5d`. Read B1323 FINDINGS and the positive-substitution part of its dictionary producer, B1607 FINDINGS and its free-word producer section and full post-seal producer, and B1634 FINDINGS and its full sealed producer. Their definitions are restated above and independently implemented here; no producer is imported.

The current-main topic sweep with `Sturmian|Nielsen|inner automorphism|braid|word.*lift|positive.*lift` finds 33 of 1408 arcs: PROVED 28, NEGATIVE 4, OPEN 1. The same retained-ref sweep was launched before sealing; its completion receipt will be recorded with the findings. The preceding broad sweep and the early-record genesis index were also read. No global absence claim is made.

Literature: Kassel and Reutenauer, *Sturmian morphisms, the braid group B4, Christoffel words and bases of F2*, author publication page and abstract read at https://irma.math.unistra.fr/~kassel/pubKR0904.html (accessed 2026-10-11). The full paper has not been read for this packet and no theorem from it is an input. The elementary identities and centralizer argument below supply the proof used here.

## Execution

Seal this file, PROOF.md, verify.py and test_word_lifts.py with SHA-256 before executing either Python file. Then run the producer and tests with bytecode disabled, preserve their first outputs, and recheck the hashes. The packet is a local derivation/replay pending independent review and normal repository publication gates; it does not amend canonical GENESIS directly.
