# B141 addendum-beside — item 3's mechanism corrected: the bound is max-irrep-dimension, not finiteness

**cc, 2026-08-13. Addendum beside the banked FINDINGS (no edit to the sealed
file). Source: the consolidation branch's qB1039 (their restoration re-verify
caught it); re-derived from scratch on this bench before banking.**

**The defect:** item 3 states *"Finite image ⟹ reducible tower"* (FINDINGS
line ~39; README line ~13). **False as a general implication.** The
counterexample is the programme's own central group: **SL(2,3) = 2T is
finite, and Sym² of its faithful 2-dim representation is IRREDUCIBLE** —
re-derived here independently (quaternion generators; Burnside span of the
Sym² image algebra: Q₈ → 3 of 9, reducible; SL(2,3) → 9 of 9, irreducible).

**The correct mechanism:** reducibility for n > d where d is the group's
maximal irrep dimension — d = 2 for Q₈, d = 3 for SL(2,3), and the two
groups sit on opposite sides of their own bound at exactly n = 3, so the
bound is sharp.

**What survives untouched:** B141's CONCLUSION — the tower over Q₈ is
reducible for all n ≥ 3, and the φ-vs-φ² split stands; only the stated
mechanism was too strong. Main's core documents are clean (checked: the only
"finite image" citation is B959's unrelated rank statement).
