# ADDENDUM (2026-09-01, fresh physics seat) — the family-wide amphichirality rows in `ADDENDUM_family_wide.md` are false as banked; the instrument was orientation-blind

**Scope.** This note corrects `ADDENDUM_family_wide.md` (rows 13–17, 25, 45) and nothing
else in this arc. The original file is left unedited, per house discipline.

**What is wrong.** The "isometry-signature = mirror's" test used there — and cc3's
`check_family.py` — is `M.reverse_orientation()` followed by `M.is_isometric_to(R)`. SnapPy's
`is_isometric_to` ignores orientation, so that test returns `True` for **every** manifold and
cannot fail. B1226 (2026-08-31, line 35–37) had already caught exactly this on m208; this note
propagates the catch to the rows here, which B1226 did not touch.

**Recomputed (orientation-aware `M.symmetry_group().is_amphicheiral()`, CS via
`M.chern_simons()` mod ½; script
`reports/fresh_physics_seat_2026-09-01/recompute/R20_family_separator/seat_spotcheck_d5.py`,
output `seat_spotcheck_d5.txt` beside it):**

| member | banked here | orientation-aware | CS mod ½ |
|---|---|---|---|
| m004 | amphichiral True | **True** | 0 |
| m003 | amphichiral True | **True** | ¼ |
| m202 | amphichiral True | **False (chiral)** | 1/12 |
| s118 | amphichiral True | **False (chiral)** | 1/12 |

Of B1136's fourteen, six are amphichiral (m003, m004, m203, m206, m207, s596) and eight are
chiral (m202, m208, m410, m412, s118, s119, s594, s595). Over B1186's 112-member family the
count is **38 amphichiral / 74 chiral**, not 112/112. Every amphichiral member has CS ∈ {0, ¼}
(B1224's 2-torsion law holds on all 38; 25 at 0, 13 at ¼); the chiral members take nine
further CS values. m202/s118 at CS = 1/12 are direct witnesses that "amphichiral" was never
computed here.

**What this does and does not touch.** The line "amphichirality is the property of the class,
not m004-specific" is **withdrawn** as a family statement: amphichirality is a property of a
38-member subset, of which m004 is one. The arc's orientation-theorem addendum (m004 is
amphichiral, so no orientation is rescued by the mirror) is **unaffected** — m004 itself is
amphichiral under the correct test. The w0 headline is not touched by this note; Ring R3 cell
R24 audits the downstream chain and its result lands in
`reports/fresh_physics_seat_2026-09-01/recompute/R3_REPORT.md`.

Ledger: R2_REPORT D5 (CONFIRMED-HERE), V9. Error-class: E53 (propagation) on top of an
instrument vacuity (E27/E40).
