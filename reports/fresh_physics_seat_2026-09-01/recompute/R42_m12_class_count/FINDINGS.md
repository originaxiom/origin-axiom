# R42 — the m = 12 class-count discrepancy (B8135 → B8148): 3 SL(2,ℤ) classes, 2 GL(2,ℤ) classes — CORRECTED

**Question.** B8135 (Paper I, SCOPE): "an independent count reports 2 primitive classes at m = 12 where this gives 3 —
UNRESOLVED". B8148_m12_settled (structure-genesis head) returns 3 "under both SL(2,ℤ) and GL(2,ℤ)" and blames the 2 on
an off-by-one in the reduction bound.

**Recompute (`r42.py`).** D = m² + 4. PARI `quadclassunit(D).no`, `qfbclassno(D)`, and a from-scratch reduced-form
enumeration with ρ-cycles (SL(2,ℤ) classes) and the improper identification (a,b,c) ~ (c,b,a) (GL(2,ℤ) classes).

| m | D | h (PARI) | own SL(2,ℤ) | own GL(2,ℤ) |
|---|---|---|---|---|
| 1–5 | 5,8,13,20,29 | 1 | 1 | 1 |
| 6 | 40 | 2 | 2 | 2 |
| 7,8 | 53,68 | 1 | 1 | 1 |
| 9,10 | 85,104 | 2 | 2 | 2 |
| 11 | 125 | 1 | 1 | 1 |
| **12** | **148** | **3** | **3** | **2** |

**Verdict.** The banked GL(2,ℤ) table (1,1,1,1,1,2,1,1,2,2,1) for m = 1..11 reproduces — but for m ≤ 11 the SL and GL
counts coincide, so the table cannot discriminate the two conventions. At m = 12 the class group of discriminant 148 is
ℤ/3 (h = h⁺ = 3, a norm −1 unit exists); inversion fixes the identity and pairs the other two classes, so there are
**3 proper (SL(2,ℤ)) classes and 2 full (GL(2,ℤ)) classes.** Both numbers in Paper I's remark are right about different
equivalences. B8148's "3 under both SL(2,ℤ) and GL(2,ℤ)" is wrong for GL(2,ℤ). Codex certificate `r010_gl_class_m12.py`
(origin/codex/seat-r001; rerun here in R46) states exactly this: "3 proper SL classes, 2 full GL classes".

**Seat's own correction (2026-09-02).** The first version of this cell merged ρ-cycles by (a,b,c) ~ (−a,b,−c), which is
not an improper equivalence (it is the negative of the improper conjugate), and so "confirmed" B8148's GL = 3. Caught
by reading codex r010 against my own output. The sweep verdict #1489 is re-noted accordingly; the relay carries the
corrected statement.
