# Card `A2-S-R80b-p2`: Cold-Read of Builder Series `R80b` Part Two (Rebuilt on `main`'s `bf76e5ab1` at `bc71f9373`)

- **Seat:** `agy-002` (`origin/agy-002/verify`)
- **Card ID:** `A2-S-R80b-p2` (assigned in `M15`, `M17`, and `M18` of `docs/seats/agy-002.md` at `5cc9fe2a1`)
- **Builder target:** `R80b` Part Two as rebuilt on `main`'s `bf76e5ab1` at `bc71f9373` under `relays/advisor_2026-11-10_audit/r80b/on_mains_bf76e5ab1/` (twelve patches on `B1881`, `B1895`, and `B1897` applied after Part One, answering sixteen rows of `STATUS_OF_THE_57.md` — `SM-19` through `SM-25`, `SM-30`, `SM-31`, `F1` through `F5`, `F8`, `F9` — and the note on the two derivations). *(Note per `M18`: zero files of the first sending `part_2/` at `122967212` were opened before `M18` arrived, so `agy-002` reads directly the rebuilt Part Two on `bf76e5ab1`.)*
- **Files of `r80b/part_2/` or `r80b/on_mains_bf76e5ab1/` opened prior to this card commit:** **NONE** (`expectations committed first`, `docs/seats/README.md` § seven and § twelve).
- **Conflict-of-interest scoping (`M17` — `"Leave aside what is about your own rows, and say which"` — and `docs/seats/README.md` § thirteen):**
  - **Audited in full:** Every patch and hunk on `B1881` (`SM-30`, `SM-31`, `F1` through `F5`, and `B1881`'s lock docstring in `SM-19`), `F9` (`B1895`'s generic lock sweep of structured JSON fields), `SM-22`, `SM-24`, and the note/test on `agy-exp`'s two derivations (`b1895_probes` fidelity to `main`'s numbers), plus mechanical scope, clean-checkout gates, and `STATUS_OF_THE_57.md` attribution on all four `"not checked"` rows (`SM-22`, `SM-25`, `SM-30`, `F9`).
  - **Explicitly left aside on substance (declared and listed by patch/hunk in the report):** Lines and rows that judge or record `agy-002`'s own earlier Review 79 rows/deliveries — `SM-20` (updating `B1895` and `harvest row 1730` for `agy-002`'s plant run), `SM-21` (sentence attributed on `docs/seats/agy-002.md`, `B1897`, and `harvest row 1733`), `SM-23` where `B1895 § three row A1` answers `agy-002`'s `A2-R79b` row `A1` (auditing only whether the lock's integer-word comparison matches `main`'s `b1895_probes`), `SM-25` (`B1897 § four` and `P-822` owed from `agy-002`'s `A2-R79c`), `F8` (replacing `agy-002`'s session name on `B1895`/`B1897` ledger lines), and the `B1895`/`B1897`/`harvest row 1733` occurrences of `SM-19`.

---

## 1. The Question, in One Sentence

When `R80b` Part Two's twelve rebuilt patches are applied by `git am` onto `main`'s `bf76e5ab1` plus Part One, does each non-COI patch do strictly what its `STATUS_OF_THE_57.md` row and `main`'s `b1895_probes` / `plants_b1881_third` files ask and nothing else — keeping old words under dated notes, writing none of the four `"not checked"` rows (`SM-22`, `SM-25`, `SM-30`, `F9`) as checked by `main`, making both the builder's plants and `main`'s five `plants_b1881_third` plants pass before the mend and fail after it, and defeating fresh unseen adversarial plants of `agy-002`'s own against `B1881`'s and `B1895`'s mended locks?

---

## 2. What Will Be Delivered, and What Done Means

Done means three commits inside `relays/` on `origin/agy-002/verify`:

1. **Commit one (this card + `relays/STATUS_AGY-002.md`):** Committed and pushed strictly before opening any file of Part Two (`122967212` or `bc71f9373`).
2. **Commit two (`relays/r80b_p2_cold/verify_r80b_p2.py` and `relays/r80b_p2_cold/verify_r80b_p2_out.txt`):** Independent Python verification script and raw output in an isolated temporary detached worktree (`bf76e5ab1` + Part One + Part Two), checking:
   - patch-by-patch scope, COI classification, and dated-note retention of old words;
   - `STATUS_OF_THE_57.md` attribution on all twelve commit messages and changed pages/register rows (specifically verifying `SM-22`, `SM-25`, `SM-30`, and `F9` are never attributed to `main`);
   - `main`'s five plants in `plants_b1881_third` (`F1` through `F5`) passing before Part Two and all five failing after Part Two, plus each patch's own before/after planted case;
   - fresh unseen adversarial plants by `agy-002` against `B1881`'s mended lock (digest/monkeypatch bypasses, degenerate inputs to `check`, `made_with` tampering, partial-field corruption in the weaker comparison) and against `B1895`'s mended JSON field-by-field sweep (`F9` nested-list/dict field hiding, cross-sentence excuse within a single string field) and `b1895_probes` assertions;
   - exact numerical agreement of every number in `B1895`'s new notes/tests with `main`'s `b1895_probes` (no builder-invented number or mathematical statement, including the disclosed omission of the reader's case-by-case argument);
   - clean-checkout `53`-gate run (`scripts/gates/gates.py`) and `pytest` execution of the changed locks.
3. **Commit three (`relays/AGY002_TO_CC_2026-11-12_M18_R80B_PART2_COLD_READ.md` and `relays/STATUS_AGY-002.md`):** Concise plain-word report pushed immediately upon completion per `M18`.

---

## 3. Expectations and How `R80b` Part Two Could Fail (Written Before Opening Part Two)

1. **`B1881` lock digest / monkeypatch gaps (`F1`–`F5`):**
   - Holding `B1881`'s producer script by byte digest blocks editing the `.py` file on disk, yet if the lock still trusts a cached JSON output file without checking that running or calling the digested script reproduces the JSON fields, mutating the committed JSON output file in part A or behind a prefix pin (`F4`/`F5`) could still slip past an unheld field.
2. **Intra-field excuse in `F9` (`B1895`'s lock sweeping JSON text by text):**
   - Splitting a JSON file field-by-field instead of sweeping `json.dumps` as one block stops a correction tag in `disclosed` from excusing a retracted claim in `claim_one_line`, yet if a multi-sentence string field (or a list of strings joined before scanning) still allows a cue word in sentence two to excuse a retracted claim in sentence one of the *same* field, an intra-field plant passes.
3. **Attribution drift on the four `"not checked"` rows (`SM-22`, `SM-25`, `SM-30`, `F9`):**
   - Summarizing `"sixteen rows checked"` or omitting `"not checked by main"` in any of the four rows' commit messages, notes, or new register rows (`P-835`, `P-836`).
4. **Incomplete mend disclosed by builder (`the reader's argument by cases`):**
   - `STATUS_OF_THE_57.md` line eighty-four says `"The argument by cases was read and is right. To build: a note in B1895 § 7 and a test."` Checking whether `main`'s handoff folder gave prose for the case argument or only `b1895_probes`, and whether the builder properly stopped and disclosed rather than inventing mathematics.

---

## 4. Controls

1. **`CTL-R80B-P2-CLEAN`:** Applying Part One and all twelve rebuilt patches of Part Two onto `bf76e5ab1` succeeds cleanly, all `53` gates pass (`rc == zero`), and `B1881`, `B1895`, and `B1897` locks pass (`rc == zero`).
2. **`CTL-R80B-P2-PLANTS-FLIP`:** `main`'s `plants_b1881_third` passes `5/5` on `bf76e5ab1` + Part One and catches `5/5` (`0` passing) after Part Two.

0 of 19.
