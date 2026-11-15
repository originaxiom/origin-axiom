# B1947 — Frame D1's coupling: the card sealed before its outputs (P-861)

**Verdict: OPEN.** The card is sealed. The code is checked: C0 holds, and C1 corrects main's own first expectation, as
CARD.md discloses. No output of frame D1 is computed in this commit. Main, 2026-11-15. Data-free. **0 of 19.**

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

## Not claimed

Any output of frame D1, and any comparison with a measured number.
