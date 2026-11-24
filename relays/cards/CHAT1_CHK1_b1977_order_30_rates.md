# Check card CHK-1: an independent recomputation of B1977's order-30 rates, and whether they are limits. Data-free

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `card:` data-free. It was written at the author's word of
2026-11-24: fetch all the seats and check their load-bearing results. B1977 is the newest load-bearing result on main.
It is the first configuration on record that passes every structural test at once. The card is committed before its
script, and the script before its run. Nothing is compared with data.

## 1. What B1977 claims, and what is checked

- **The claim.** Frame C, with every sector reading S, is computed at the 96 points of order 30 whose 5-part is on the
  act's line. From the rates between heights 20 and 30 at the column 0.13 (B1977, as sealed):
  - G1 to G5 hold;
  - the five slow-mixing points share one set of rates, with V₂₃ at 1/30;
  - every rate lies on a grid of 1/60 (860 of 864);
  - 30 points are aligned and hierarchical, with a mixing rate below 1/10.
- **This seat's code.** W-D2's per-sector steps transcribe frame_mp's fbar. The coupling, the SVD, the ordering and the
  CKM are this seat's own. B1977 uses B1945's `determinant_law.parts`. The two share main's theta, norm and table
  routines, so this is an independent assembly, not a computation that shares nothing.
- **What is new beyond reproduction.**
  - B1977 reads each rate from one interval, 20 to 30. Is it a limit? The rates between 30 and 40 are checked.
  - B1977 uses one column. Are the rates the same at another? The column 0.31 is checked, between 20 and 30.

## 2. Expectations (committed now)

| cell | prediction | prior |
|---|---|---|
| R1 | At all 96 points, every rate between 20 and 30 at x = 0.13 agrees with B1977's json within 1e-6. The least diagonal at height 30 agrees within 1e-6 | 85 % |
| R2 | At the five slow points, V₂₃'s rate between 30 and 40 is within 2e-3 of 1/30 | 60 % |
| R3 | At all 96 points, every rate between 20 and 30 at x = 0.31 is within 1e-3 of its value at x = 0.13 | 75 % |
| R4 | B1977's G5 points are still aligned (least diagonal ≥ 0.9) at height 40 | 85 % |
| R5 | At least 95 % of the rates between 30 and 40 lie within 3e-3 of a multiple of 1/60 | 70 % |
| R6 | B1977's G1 to G5, re-evaluated on this seat's numbers with B1977's own criteria, hold as B1977 reports them | 85 % |

## 3. What this card does not do

- It does not compare anything with data, and it reads no target.
- It does not judge B1977's interpretation. That goes in the relay, typed.

0 of 19.
