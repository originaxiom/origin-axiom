# B1962 — Frame D1's cusp mixing: the card sealed before its outputs (P-861)

**Verdict: OPEN.** The card is sealed. The code checks C0a and C0b are disclosed in CARD.md. No output of frame D1's
mixing is computed in this commit. Main, 2026-11-19. Data-free. **0 of 19.**

## Seen first

- **Swept:** `VERDICT topic-sweep /frame D1|shifted charges|cusp mixing|Szego zero|identity E|Higgs.s own twist/: 7 of 1702 arcs on main match (NEGATIVE 2, PROVED 5); 12 register rows match (DONE 1, QUEUED 11)`.
  - **B1946** reads frame C's mixing; **B1947** closed the first form of frame D1; the web seat's W-B2 stage 3 (harvest
    row 1842), with main's hand reduction, gives frame D1 as frame C at shifted charges.
- **The literature:** the Yukawa couplings of magnetized tori, a triple overlap of theta functions with characteristics
  (Cremades, Ibáñez and Marchesano, hep-th/0404229), as B1947 cites it. Nothing in it fixes the sign c.

## What is here

- **`CARD.md`:** the definition (frame C at identity E's shifted charges, both signs of c), the cells, the
  classification and the gate, with expectations and priors, fixed before the run.
- **`verification/d1_mixing.py`:** the instrument. It refuses to run until CARD.md is committed unchanged.

## Not claimed

Any output of frame D1's mixing, the identity E at the norms, and any comparison with a measured number.
