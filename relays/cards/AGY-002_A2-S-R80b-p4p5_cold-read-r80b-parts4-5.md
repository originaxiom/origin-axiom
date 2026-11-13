# Card `A2-S-R80b-p4p5`: Cold-Read of Builder Series `R80b` Parts Four and Five (Rebuilt on `main`'s `bf76e5ab1`)

- **Seat:** `agy-002` (`origin/agy-002/verify`)
- **Card ID:** `A2-S-R80b-p4p5` (`M18`, `M19` of `docs/seats/agy-002.md` at `1e8ef44de`); two reports, one per part.
- **Builder target:** `relays/advisor_2026-11-10_audit/r80b/on_mains_bf76e5ab1/part_4/` (six patches: the listener and the atlas's query) and `part_5/` (patches one and two, and patch three, the foundation at version 1.67, script and message, as on the builder's head `ef5f59c8f`), applied in order after Parts One to Three.
- **Files of Parts Four and Five opened before this card commit:** **NONE** (file names only).
- **Conflict-of-interest scoping, written before opening:**
  - **Part Four, audited in full:** the SM seat's 36 to 40 and `F12` (`scripts/seats/listen.py`, `scripts/atlas/`). None is `agy-002`'s row. `agy-002` runs the listener as a user; that is said, and does not judge `agy-002`'s work.
  - **Part Five, audited in full:** patch one (the asserts that ended in a constant; the web seat's finding) and patch three (the foundation's seven passages at version 1.67, arc `B1904`; the web seat's `W7`).
  - **Part Five, left aside on substance:** patch two, `B1862`'s tripwire. It answers `agy-002`'s own rows 10 and 11 (`"Your own 36 rows you leave"`, `M15`). Only its mechanical scope, whether it applies, and whether its tests pass are recorded.

## Expectations, committed first

1. Each patch changes only what its row asks, keeps old words under a dated note, and carries a planted case that passes before and fails after.
2. Rows given as `"not checked"` by main (`SM-37` to `SM-40`; main checked `SM-36` and `F12`) are not written as checked by main.
3. Likely gaps: a listener mend that names an amended message only on one path; a heading rule that stops at one level but not at a heading inside a fenced block; a version-1.67 script that carries the old passages in its own text (the builder says it is a script for that reason; to be checked as for Part One's `P-796`).
4. The count of landings gate is past forty for every patch here; no other gate should fail.

## Controls

- All patches apply in order after Part Three; the changed tests pass on the last patch.
- Each mended function fails on at least one planted change of `agy-002`'s own.

0 of 19.
