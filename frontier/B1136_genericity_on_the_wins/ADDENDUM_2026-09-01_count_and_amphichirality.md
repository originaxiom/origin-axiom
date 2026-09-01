# ADDENDUM (2026-09-01, fresh physics seat) — the ≤6-tetrahedra count is 21, not 14 (census truncation), and the amphichirality column was not a computation

**Scope.** Two corrections to the banked census table of this arc; the separator verdict is
unchanged. Original FINDINGS.md left unedited.

**1. "Exactly 14" is a truncation artifact.** `verify_genericity.py:29–30` breaks the census
walk at index 1200 (`if i > 1200: break`). Seven further members satisfying the same
all-shapes-in-ℚ(√−3) criterion sit at census indices 1256–1262 (s955–s961). The true count at
≤6 tetrahedra is **21**. All seven extras are already inside B1186's 112-member family, so the
family-level statements downstream are not changed; the *number* 14, wherever it is quoted as
"exactly", is wrong. (B1186 suspected a criterion conflation as the cause of its own 14→112
growth; the cause of the 14-vs-21 gap is truncation, not the criterion.) Recomputed in Ring R2
cell R20 (`reports/fresh_physics_seat_2026-09-01/recompute/R20_family_separator/`,
R2_REPORT D6).

**2. "All 14 amphichiral" (line 93 of the script; FINDINGS table row "amphichirality ✓ / ALL
thirteen others") was produced by `reverse_orientation()` + `is_isometric_to()`, which SnapPy
evaluates orientation-blind — it returns `True` on every manifold and could not have failed.
Orientation-aware (`symmetry_group().is_amphicheiral()`, cross-checked by CS mod ½):

| amphichiral (6) | chiral (8) |
|---|---|
| m003 (CS ¼), m004 (0), m203 (0), m206 (0), m207 (¼), s596 (0) | m202 (1/12), m208 (0), m410 (3/8), m412 (3/8), s118 (1/12), s119 (5/12), s594 (1/8), s595 (0) |

So amphichirality **is** a separating-type property inside the 14 (6/14), contrary to the
banked row — it just does not single out m004. The banked headline (H₁ = ℤ is the unique
separator among the seven properties) **stands**: H₁ = ℤ remains the only property true of
m004 alone in the 14, and also in the 21. Note that within B1186's 112 it does not (see
B1186's own finding and `seat_spotcheck_d5.txt`: o10_150700 also has H₁ = ℤ).

Ledger: R2_REPORT D5 (CONFIRMED-HERE), D6, V9. B1226 (2026-08-31) first caught the instrument
on m208; this note propagates it to the source table.
