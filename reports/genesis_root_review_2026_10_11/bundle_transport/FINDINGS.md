# The parity constructions survive a coherent change of word convention

2026-10-11. Source sealed at `f472645960fb284f354af2ddbb5dfa066f17363b`; first execution PASS, 371 exact assertions. Source and imported-helper hashes unchanged after execution. This is a local mathematical derivation and replay, pending independent review and normal publication gates. No physical parameter, Λ clause or global analytic domain is declared derived.

The preceding word-level equivalence extends to the existing parity cohomology and local puncture construction. The two spaces require different transport maps. Both preserve parity grading; the cohomology's two algebraic triplets transport, and the graded puncture conditions remain the two extreme subspaces. Thus choosing among the four coherent positive elementary pairs introduces no further convention dependence into these specified mathematical structures.

## Seen first

The exact source pins and reading scope are in PREREGISTRATION.md. The preceding all-retained-ref topic sweep returned 33 of 1408 main arcs on `Sturmian|Nielsen|inner automorphism|braid|word.*lift|positive.*lift` (PROVED 28, NEGATIVE 4, OPEN 1), with matches on 18 retained lanes. The additional current-main full-FINDINGS search included `base.point.*transport|inner automorphism|parity grading|puncture condition`, using quoted Git pathspecs rather than shell-expanded paths from this older checkout. No absence or novelty claim follows from these searches.

B1606's local matrix formula and its dependency addendum were read in full. The SM cohomology pullback, W21 pairing construction and W46 end rule were read as specified in the seal. The producer uses exact matrices and a different quotient chart, not their saved numerical answers. Sharifi's chapter 1 cochain definitions were read for background; the degree-one identities and transport arguments used here are derived in PROOF.md.

## The verified maps

For the base-point change h=J_q, write U=rho(q). The original move f and its chosen lift g transport to h f h^-1 and U g U^-1.

| Mathematical object | Transport | What the proof and exact run establish |
|---|---|---|
| Parity cohomology H1(F2; chi_p rho) | D_q=diag(chi_p(q) I2) | Direct cocycle calculation agrees with the conjugated move matrices. The cohomology chart is checked against a second chart. |
| Its two algebraic triplets | The corresponding D_q conjugacy of projectors | Both projectors have rank three, are invariant under the reconstructed moves, and retain those properties after transport. |
| Local puncture solutions of B1606 | E_q=diag(u_p^-1 U u_p), u_p=(j,i,k) | Direct reconstruction agrees with E_q M E_q^-1. E_q is unitary and commutes with the parity projectors. |
| Graded local condition | B maps to E_q B E_q^-1 | The exact commutant has dimension 2 without grading and 1 with grading. With grading, the zero and full subspaces are the only invariant subspaces and transport to themselves. |
| Uniform cusp pole order | Constant invertible coefficient change | Every integer order is preserved. No particular integer is selected. The all-order statement has an elementary leading-coefficient proof. |

For the four positive pairs, the signs on the three parity blocks are respectively (+,+,+), (+,-,-), (-,+,-), (-,-,+). They do not change a parity sector's dimension or a block-diagonal Hermitian pairing. Consequently any previously established Hodge-sign assignment with the direct-sum pairing is preserved. The run does not independently prove W21's Hodge-theoretic interpretation, and neither triplet is assigned a physical Lorentz hand here.

## The central sign control

The same inner automorphism J_c, c=aBAb, has two allowed intertwiners. With rho(c)=-I, its induced cohomology map is +I. With the opposite intertwiner +I, its induced cohomology map is -I. The Delta^4 control reproduces the latter sign: its product lift is +I, while its action on cohomology is -I.

Thus the word automorphism does not specify its lift. Coherent transport preserves this distinction rather than erasing it. This explicitly protects the central information involved in B1634's correction of the helper-sign error. The local six-space and cohomology six-space also differ on the same natural inner lift, providing a control against identifying them just because both have dimension six.

## What this removes and what it does not

The positive elementary word-pair convention is now removed as an additional choice within these fixed, coherently transported constructions. A different convention need not be treated as a new vacuum or a new physical branch. Conversely, independently adjoining alternative generators still changes the allowed action, as the preceding packet proved.

What has not been removed is the choice of the construction itself. The faithful free group, common-point representation, parity-twisted coefficient system and physical interpretation remain antecedents. The map supplies no gauge 27, no identification of holomorphic modes with four-dimensional matter, and no preferred cusp unit.

In a Fredholm realization whose differential operator and domain are both transported by these unitary maps, kernels and cokernels correspond and the index is unchanged. This is a conditional operator statement, not a verification that the intended noncompact physical realization or its domain has been constructed. The algebraic puncture-subspace result must not be relabelled as that analytic completion.

## Next upstream question

The fixed-pair convention issue is sufficiently resolved for the named constructions; more enumerations of equivalent pairs are not the next priority. The next dependency is why the record grammar should be realized faithfully in the chosen carrier and why that carrier should carry the matter coefficient system. Follow GENESIS GM4/FK5 into GAP1/FK11, keeping record counts, update histories, based loops and field bundles distinct. Recover existing proofs before proposing an additional principle, and do not infer a physical selection from the losses caused by removing an assumption.

The updated `UPSTREAM_DEPENDENCIES.md` records the exact boundary between the implications strengthened here and the conditions still carried by the physical chain.

## Verification and publication scope

First command: `LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 python3.12 reports/genesis_root_review_2026_10_11/bundle_transport/verify.py`, exit 0. Its transcript is `NATIVE_FIRST.txt`, sealed outputs are in `RESULT_HASHES.txt`. All 371 assertions passed; there was no failed scientific first run or source repair. The second quotient chart, cocycle-law controls, reversed-composition control and opposite-lift control are included in that producer. They are not an independent non-author review or a full-repository suite.

Proposed law entry for normal review: **coherent inner transport preserves the specified parity cohomology, local graded puncture conditions and uniform pole order**, under exactly the assumptions above, with PROOF.md and the direct reconstructed matrices as its lock. No shared law ID or B-number is allocated; canonical GENESIS and main's registries remain unchanged pending adoption.
