# B1620 — ADDENDUM (2026-10-09, B1625): the SM seat's corrections taken — TM1 under T̄ ⊗ T only (TM2 under T ⊗ T), the frame named, the fit predicate made strict

The SM seat verified B1620 exactly from a closed form of the group (W42: 68 subgroups in 26 classes, 57 abelian;
57 / 24 / 16 viable; no order-3 residual under Sym² T; every residual containing K gives permutations). It then found
three things wrong in how B1620 stated its lepton result (relay §43–§46, W43, W44). Each is checked here on B1620's
own stored data (`post_seal_tensors.json`), and each is taken.

## 1. TM1 is allowed under T̄ ⊗ T only; under T ⊗ T the family is TM2

FINDINGS §2–§3, the relay's title, P10's scope note, GENESIS v1.35 and the write-up said "TM1 allowed under T̄ ⊗ T and
T ⊗ T". **That is wrong for T ⊗ T.** Under T ⊗ T both PMNS families of dimension 2 have block sums ⅓ and ⅔ in every
row. Their fixed column is (⅓, ⅓, ⅓), which is **TM2**'s second column. Under T̄ ⊗ T both kinds occur: the (3, 2)
pairs fix (⅓, ⅓, ⅓) (TM2), and the (3, 8) and (6, 8) pairs fix (⅔, ⅙, ⅙) (TM1). The seat's mechanism (W43): every
edge half-turn carries c with c² = ±i in this frame, so no residual containing one survives T ⊗ T, and TM1's column is
an edge half-turn's axis against a 3-cycle's eigenbasis. W43 counts 0 of 576 pairs with a TM1 column under T ⊗ T.
**The label was assumed from P10, which is TM1, and never computed for T ⊗ T** (ERROR_LEDGER, an E65 instance).

**Corrected statement:** in B1620's frame the PMNS reduces to two parameters as follows:
- under T̄ ⊗ T: TM1 or TM2;
- under T ⊗ T: TM2 only, where sin²θ₁₂ = 1/(3 cos²θ₁₃) ≈ 0.341;
- under Sym² T: not at all.

P10 (TM1) therefore applies under T̄ ⊗ T.

## 2. The frame is "all of G is flavour", not W24's

§4 named B1620's frame as "the record's lifts, where c is physical (W24's E₈ embedding)". B1620 treats all of G as
flavour. In W24's frame only c is flavour and every S(g) is gauge, so the flavour group acts by scalars and constrains
no mixing. The seat's W44 computed the second frame on record, where c is gauge:
- **The CKM needs a four-dimensional family in every frame on record.** "The weave's symmetry reduces none of the 13"
  needs no frame.
- Where c is gauge, TM1 and TM2 are each allowed under T̄ ⊗ T and T ⊗ T.
- Under Sym² T there is one lepton relation: a fixed entry 1/√2 or ½, for example sin²θ₂₃ ≈ 0.511.

## 3. The fit predicate made strict

`fit()` counted a family as reaching the PMNS when its largest excursion was at most one half-width OUTSIDE NuFIT's 3σ
ranges, a lenient predicate looser than the stated test ("inside the ranges"). Under the strict predicate:
- the four (8, 8) two-dimensional families (score 0.0707) are outside, by 0.0012;
- the (2, 8) three-dimensional families (score 0.3627) are inside: the seat found strict witnesses this search did not.

The minimum of two is unchanged, and the CKM result is untouched: its predicate was the 3σ pull, and its lower bound
rests on the block test alone, which needs no sampling (the seat's W44).

## 4. The rank estimator

The family dimension took the maximum over three random points, and a point near a degeneracy can add a spurious rank
(the seat found two such counts in its own W43 tally). The CKM conclusion does not use the rank above the block test.
The PMNS minimum (2) is the seat's modal rank too.

**Credit:** the SM seat (W42–W44, relay §43–§46), with the audit lane's point on fit acceptance.
