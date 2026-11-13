# Card `A2-S-R80b-p3`: Cold-Read of Builder Series `R80b` Part Three (Rebuilt on `main`'s `bf76e5ab1` at `bc71f9373`)

- **Seat:** `agy-002` (`origin/agy-002/verify`)
- **Card ID:** `A2-S-R80b-p3` (`M17`, `M18`, `M19` of `docs/seats/agy-002.md` at `1e8ef44de`)
- **Builder target:** `relays/advisor_2026-11-10_audit/r80b/on_mains_bf76e5ab1/part_3/` (eighteen patches on the older arcs, their tests, the protocol and two messages), applied after Part One and rebuilt Part Two on `bf76e5ab1`.
- **Files of Part Three opened before this card commit:** **NONE** (only the eighteen file names were listed by `git ls-tree`).
- **Conflict-of-interest scoping, written before opening:**
  - **Audited in full:** the patches on `B732` and `B942` (`W8`, `W9`), `B1884`'s two sentences (`SM-34`, `SM-35`), `B1882`'s lock (`SM-33`), `B874`'s bracket and its test (`SM-26`, `SM-41`), `B448`'s test (the web seat's addition), the protocol sentence (`SM-05`), `B1893` (`SM-12`), the old sign of the index (`SM-27`), `B862`'s script (`F11`), `B734`'s sweep (`F14`), `B1222` and `B1028`'s test (`F13`), `B1891`'s lock (`F6(b)`), and the log entry.
  - **Left aside on substance, said by patch:** any line of patch nine that changes main's table of answers to `agy-002`'s own thirty-six rows (`ANSWERS_the_first_43.md`); in patch seventeen (`B1894`'s quotation checker, `F7`), the lines of `B1894` that judge `agy-002`'s Review 79 work (mechanical scope, the builder's own disclosure of the copied fault, and the checker's behaviour on planted paths are checked).

## Expectations, committed first

1. Each patch changes only what its row asks, keeps the old words under a dated note, and has a planted case that passes before and fails after where it mends a lock or test.
2. No row that `STATUS_OF_THE_57.md` gives as `"not checked"` (`SM-26`, `SM-32`, `SM-33`, `SM-41`, `F6(b)`, `F7` for `B1894`, `F11`, `F13`, `F14`, `W8`, `W9`) is written as checked by main.
3. Likely gaps: a test that holds a phrase where it should hold a computed value (`B874`, `B448`); a correction that travelled to one place and not another (`SM-27`, `W8`); patch seventeen copying `B1892`'s strict placing with its known false pass (disclosed by the builder; to be confirmed by a planted path).
4. The count of landings reaches forty during Part Three (the builder says at its ninth patch): the gate that fails there is the review count and nothing else.

## Controls

- All eighteen patches apply by `git am` after rebuilt Part Two; the changed tests pass on the last patch.
- Each mended lock or test fails on at least one planted change of `agy-002`'s own.

0 of 19.
