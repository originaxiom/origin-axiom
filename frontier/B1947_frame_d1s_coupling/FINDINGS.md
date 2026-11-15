# B1947 — Frame D1's coupling: the card sealed before its outputs (P-861)

**Verdict: NEGATIVE** for the construction, as sealed. Frame C's coupling with a twisted Higgs put in is not
covariant, in either twist convention, so frame D1 cannot be had that way. Main, 2026-11-15. Data-free: no mixing or
mass output was computed. Register row P-861. **0 of 19.**

## Seen first

- **Swept:** `VERDICT topic-sweep /frame D1|frame D|Higgs.s own twist|twisted Higgs|triple overlap|third factor/: 15 of 1688 arcs on main match (NEGATIVE 4, PROVED 11); 17 register rows match (DONE 6, QUEUED 11)`.
  - **The web seat's W-B1** (harvest row 1824) defines frame D1 and leaves one choice open: where the Higgs's twist
    enters. **B1946** shows why D1 is the repair to try.
- **The literature:** the triple overlap of magnetized tori, two fermions and one scalar, with the result a theta
  function with characteristics (Cremades, Ibáñez and Marchesano, hep-th/0404229).

## What is here

- **`CARD.md`:** the definition, its one declared convention, the code checks C0 and C1, and the classification of the
  mixing at height 30 (ALIGNED, DERANGED or PARTIAL), fixed before the run.
- **`verification/d1_coupling.py`:** the construction.
  - `--control` runs C0 and C1.
  - `--run` computes the outputs and refuses until the card is committed.

## The result

- **The sealed run** (card at a64eb0759) stopped at C2, by the card's rule. Under τ → τ + 1 the worst differences were
  8.0 and 1.6 for the two representatives, against 3e-16 for frame C's own harness (`verification/d1_run.txt`).
- **Amendment A1** (9ed3ebdf5) corrected a doubling in main's definition, derived from the transport rule. It too stopped
  at C2, at 9.4 for both representatives (`verification/d1v2_run.txt`).
- **The cause** (`verification/higgs_transport.py`):
  - frame C's Higgs triplet transforms under τ → τ + 1 by W-B1's matrix T_R, the point moving as w → (a, b − a);
  - the twisted triplet picks up further phases, of modulus 1 but different for each component (q_H = 3: for example
    0.43 + 0.90i, 0.19 − 0.98i and −0.88 − 0.48i at w = (1/5, 2/5));
  - frame C's quaternion contraction does not absorb them.
- **What it means.**
  - A covariant frame D1 must be built as a genuine triple overlap: the coupling derived as one integral of three theta
    functions, in which charge conservation makes the three transformation phases cancel.
  - That is a derivation to make, with covariance shown analytically first. It is not a definition to adjust by trial,
    and none is made here.
  - The search was not continued past the amendment, so as not to choose a definition by what passes.

## Not claimed

Any output of frame D1, and any comparison with a measured number.
