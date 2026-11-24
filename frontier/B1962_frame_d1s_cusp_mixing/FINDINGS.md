# B1962 — Frame D1's cusp mixing is deranged for every Higgs reading and both signs of c, and its leptons copy the down sector transposed

**Verdict: NEGATIVE as sealed, PROVISIONAL until its second computation** (P-861; the card was committed and pushed at
399670b39 before the run; the second computation is asked of the web seat, M78). Main,
2026-11-19. Data-free: nothing is set beside a measured number. **0 of 19.**

> *2026-11-19, later: the second computation is made. The web seat's W-B3 (harvest row 1979), on its own code, reproduces every number of this arc it could see: at height 30 no pair aligned under either sign, at height 6 (S̃, S̃) 0.12525 and 0.12559, and the leptons a transposed copy. So the verdict is final: NEGATIVE as sealed. W-B3 also shows identity E at the norms exactly, under the flat unitary metric of the Higgs's twist; main checked the step by hand. That metric is the twist bundle's own and is periodic in the Higgs's point, so this arc's one assumption is now a theorem, and P-861 is closed.*

**Review 86 corrections (2026-11-24; cold readers' findings, each checked by main; docs/progress/REVIEWS.md, B1975):**
- **Lines 87 to 90 are stale.** They say identity E at the norms is assumed. It is closed by P-861 through the web seat's W-B3 and main's hand check of the shift law (line 7), not in this arc, and the run still assumes it.
- **"Deranged for every reading" uses the card's gate:** the least diagonal over the 24 points is below 0.1 at some point. Derangement at every point is not shown.
- **E4's "matches at height 6 to two digits"** holds for (S̃, S̃) (0.1252 against 0.1256) and not for the other three pairs.
- **The script's docstring is wrong.** It says "c = −2 gives frame C again". In fact c = −2 gives the charges (−q_R, −q_L), and the run shows it deranges.
- **E0's reproduction of B1946 was read by eye.** The lock does not hold it.

## Seen first

- **Swept:** `VERDICT topic-sweep /frame D1|shifted charges|cusp mixing|Szego zero|identity E|Higgs.s own twist/: 7 of 1702 arcs on main match (NEGATIVE 2, PROVED 5); 12 register rows match (DONE 1, QUEUED 11)`.
  - **B1946** reads frame C's mixing; **B1947** closed the first form of frame D1; the web seat's W-B2 stage 3 (harvest
    row 1842), with main's hand reduction, gives frame D1 as frame C at shifted charges.
- **The literature:** the Yukawa couplings of magnetized tori, a triple overlap of theta functions with characteristics
  (Cremades, Ibáñez and Marchesano, hep-th/0404229), as B1947 cites it. Nothing in it fixes the sign c.

## What was run

- **The card** (`CARD.md`) fixed the cells, the classification, the gate and five expectations with priors before any
  output. The instrument refused to run until the card was committed.
- **Frame D1 is computed as frame C at identity E's shifted charges** q′ = q − c·q_H/2, on frame C's own code (B1945's
  split, B1946's measure), for c = +2, c = −2 and the control c = 0. Each run covers the four Higgs reading pairs, the
  24 points of order 5 and heights 6 and 30. The run takes 44 s.
- **`verification/d1_mixing_run.txt`** is main's run.

## The results

**The control holds (E0).** At c = 0 every number of B1946's table is reproduced to its printed digits, so the run is
valid.

**The mixing.** The figure is the smallest diagonal |V| over the 24 points:

| c | height | (S, S) | (S̃, S̃) | (S̃, S) | (S, S̃) |
|---|---|---|---|---|---|
| 0, frame C (control) | 6 | 0.993 ALIGNED | 0.975 ALIGNED | 1e-7 DERANGED | 3e-7 DERANGED |
| 0, frame C (control) | 30 | 1.000 ALIGNED | 7e-39 DERANGED | 2e-40 DERANGED | 4e-40 DERANGED |
| +2 | 6 | 0.055 DERANGED | 0.126 PARTIAL | 6e-5 DERANGED | 1e-6 DERANGED |
| +2 | 30 | 3e-5 DERANGED | 2e-38 DERANGED | 5e-40 DERANGED | 1e-39 DERANGED |
| −2 | 6 | 0.056 DERANGED | 0.125 PARTIAL | 3e-7 DERANGED | 1e-7 DERANGED |
| −2 | 30 | 3e-5 DERANGED | 8e-39 DERANGED | 5e-40 DERANGED | 8e-41 DERANGED |

- **No reading pair is ALIGNED** at either height under either sign of c. Frame D1 loses the one alignment frame C had,
  (S, S).
- **The outcome does not depend on the reading rule.** Under either rule the record has weighed, every candidate pair
  is deranged at height 30:
  - the charge rule of frame C, mixed readings (P-847);
  - "one object, one reading", same readings (P-847's note of 2026-11-15).

**The leptons (M2).** At every c, height and reading, the lepton coupling's left vectors match those of the transposed
down coupling to 1e-36 or better [corrected 2026-11-24, Review 86: two entries are 9.9e-37 and 1.2e-37]. The normalised spectra agree to 1e-91. So the leptons COPY the down sector, transposed,
as in frame C (B1934's law, Y_e ∝ Y_dᵀ). The plain comparison is not a 0/1 pattern: 0.18 to 0.44 at height 6.

**The gate fails under both signs of c,** on both of its conditions. The result is NEGATIVE as sealed.

## The expectations, read

| | expectation | prior | result |
|---|---|---|---|
| E0 | the control reproduces B1946 | 0.99 | holds |
| E1 | at c = +2 the mixed readings are DERANGED at height 30 | 0.7 | holds |
| E2 | at c = +2, (S, S) ALIGNED at both heights and (S̃, S̃) DERANGED at 30 | 0.5 | fails: (S, S) is DERANGED at both heights |
| E3 | at c = +2 the leptons copy the down sector, transposed | 0.7 | holds, and at every c |
| E4 | at c = −2 the table equals frame C's | 0.5 | fails: c = −2 deranges as c = +2 does, and matches it at height 6 to two digits |
| — | the overall outcome NEGATIVE | 0.8 | holds |

## What it means

- **The Higgs's own twist does not repair the mixing; it removes the alignment frame C had.** The repair route of P-861
  (B1946, B1947, W-B2) is closed in this frame, whichever sign of c is the overlap's own.
- **The mixing fault returns to frame C.** There only the same-reading pair (S, S) aligns, at both heights. That pair
  is the one frame C's charge rule excludes (P-847), so within this family of frames an aligned mixing and a
  charge-consistent reading have not been had together.
- **The leptons do not separate from the down sector in frame D1,** as they do not in frame C.

## What the wall teaches

- **Moving the Higgs's twist to its own Szegő zero is not a neutral change.** It shifts every matter charge by c·q_H/2,
  so the '+' class of each sector is multiplied by 3 at order 5 and the '−' class is kept. That is enough to move the
  sectors' heaviest directions apart, for every reading.
- **So a principle for the reading cannot be looked for inside frame D1.** There is no reading under which D1 aligns.
  The question stays where B1946 left it: frame C aligns only with (S, S), which its own charge rule excludes.
- **The leptons' transposed copy of the down sector survives the shift.** It is a property of the family of frames, not
  of the Higgs's placement.
- **The second computation is asked** of the web seat, on its own stage-3 code (M78). Until it is made, the verdict is
  provisional.

## Not established

- **Identity E at the norms.** It is shown at the residues (row 1842). This run assumes it holds for the norms too.
  If frame D1's own norms differed from frame C's at the shifted charges, its mixing could differ. That is P-861's
  remaining item.
- **Any comparison with data.** "Aligned" is the card's classification of |V|, not a fit.

## Files

`CARD.md` (sealed at 399670b39), `verification/d1_mixing.py`, `verification/d1_mixing_run.txt`; the lock is
`verification/test_b1962_d1_mixing.py`.

0 of 19.
