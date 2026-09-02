# R42 — the m = 12 class-count discrepancy (B8135 → B8148): 3, confirmed

**Question.** B8135 (Paper I, SCOPE) flags: "an independent count reports 2 primitive classes at m = 12 where this
gives 3 — UNRESOLVED". B8148_m12_settled (structure-genesis head) re-implements and returns 3, naming the likely
source of the 2: coding the reduction bound as `b < floor(sqrt(D))` drops `b = floor(sqrt(D))` when D is not a square.

**Recompute (this cell, `r42.py`).** Discriminant D = m² + 4 (the metallic family x² − m x − 1). Four counts:
PARI `quadclassunit(D).no`, PARI `qfbclassno(D)`, and a from-scratch reduced-form enumeration with ρ-cycles
(SL(2,ℤ)) and improper identification (GL(2,ℤ)).

| m | D | PARI .no | qfbclassno | own SL(2,ℤ) | own GL(2,ℤ) |
|---|---|---|---|---|---|
| 1–5 | 5,8,13,20,29 | 1 | 1 | 1 | 1 |
| 6 | 40 | 2 | 2 | 2 | 2 |
| 7,8 | 53,68 | 1 | 1 | 1 | 1 |
| 9,10 | 85,104 | 2 | 2 | 2 | 2 |
| 11 | 125 | 1 | 1 | 1 | 1 |
| **12** | **148** | **3** | **3** | **3** | **3** |

**Verdict.** MATCH with B8148: the banked GL(2,ℤ) table (1,1,1,1,1,2,1,1,2,2,1) for m = 1..11 is reproduced exactly
as a control, and m = 12 gives 3 by all four counts (h(148) = 3; the narrow and wide class numbers coincide at every
m ≤ 12 here because the fundamental unit of the order has norm −1). The "2" is the off-by-one on the reduction bound
B8148 names. Paper I's remark should read "3, settled (B8148)"; the seat's sweep verdict #1489 is corrected from
STANDS to SUPERSEDED.
