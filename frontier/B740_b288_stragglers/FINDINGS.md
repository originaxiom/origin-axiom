# FINDINGS — B740: the B288 grid COMPLETED — the kill is reconfirmed, now fully earned (OUTCOME B, 78/78)

cc banking seat, 2026-07-21. Prereg sealed `14847ec1`. Hunt-cell #3 (cc2 register crack #1). Pure
math; Gate 5; nothing to CLAIMS.

## THE CRACK, CONFIRMED IN SUBSTANCE — then CLOSED BY COMPUTATION
cc2's register: B288's banked headline "NO closed hyperbolic filling re-sees ℚ(√−3)" was computed
on **54 of 78** hyperbolic fillings (the FINDINGS' own "54 closed hyperbolic fillings resolved" vs
the grid's 87 coprime − 9 exceptional = 78) — **24 hyperbolic fillings were never analyzed** (the
line-40 `continue` + `'>20'` unknowns; environment-dependent which). cc-verified at the code and at
the banked text. [Nuance: in TODAY'S environment only the 9 genuinely exceptional slopes fail the
default positivity check — the 24 were an artifact of the original run's environment — but the
banked RECORD covered 54, so the gap was real regardless.]

## THE COMPLETION (fresh, the whole grid)
All **78** hyperbolic fillings (|p|≤8, 1≤q≤8, gcd=1, minus the 9 exceptional (p,1), |p|≤4)
recomputed from scratch (`b740_full.py`, sage): retriangulation recovery (0 unresolved), invariant
trace field via Sage `find_field`, √−3-containment test:
- **60 fillings**: field identified at degree ≤ 24 (prec ≤ 1000) — degrees 3–13+ — **none contains √−3**.
- **11 more** (`b740_deep.py`): identified at degree ≤ 32 (prec 2000) — degrees 19–31 — **none contains √−3**.
- **The last 7** ((−p,q) for (p,q) ∈ {(7,8),(5,7),(5,8),(3,7),(3,8),(1,7),(1,8)}): closed by the
  **amphichirality shortcut** — `4₁(p,q) ≅ 4₁(−p,q)` (the mirror isometry; **verified 7/7 by
  snappy `is_isometric_to`, volumes matching to 1e-10**) ⇒ conjugate = the same abstract invariant
  trace field ⇒ √−3-containment inherited from the RESOLVED clean sibling. **All clean.**

**VERDICT: OUTCOME B on the COMPLETED grid — no closed hyperbolic filling of m004 has √−3 in its
invariant trace field. The E₆/being atom is an open-object property, destroyed by closing — now
computed on 78/78, upgraded from asserted-on-54 to EARNED.** (Dual-protocol rule 7 satisfied: the
negative is no longer unearned.)

## Methodological yields
1. **The amphichirality shortcut**: for any mirror-symmetric census over m004, the (−p,q) half is
   determined by the (p,q) half (field-conjugation invariance of containment) — halves all future
   filling censuses.
2. **The E22-family lesson extended**: a banked "full-grid" claim must state its grid arithmetic
   (87 coprime = 9 exceptional + 78 hyperbolic); B288's own text said 54 without flagging the gap.
3. Hunt-ledger: cell #3 CLOSED (width 3). The register's crack produced not a revival but a genuine
   UPGRADE of the kill — exactly what "compute both directions" is for.

Artifacts: `b740_full_out.txt` (78 rows), `b740_deep_out.txt` (11 deep IDs), `b740_mirror.py`
output (7/7 isometries). Credit cc2 (the crack); the amphichiral closure (this seat).
