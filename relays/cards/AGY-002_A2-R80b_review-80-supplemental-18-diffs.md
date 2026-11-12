# Card `A2-R80b`: Review 80 Supplemental Cold-Read of Eighteen Arc Differences (`M12`, `M13`, and `M14`)

- **Seat:** `agy-002` (`origin/agy-002/verify`)
- **Card ID:** `A2-R80b` (addition to `A2-R80` assigned under `M12`, `M13`, and `M14` in `docs/seats/agy-002.md` at `bb81d2c56`)
- **Commits of `main` read:**
  - `M12` two differences (`B1884`, `B1889`): base `896cae025`, read at `c40446392`.
  - `M13` ten differences (`B731`, `B732`, `B733`, `B734`, `B942`, `B1028`, `B1030`, `B1067`, `B1222`, `B1643`): base `38d2a36dc`, read at `0dda7b472` (with cross-check against `c40446392` so any post-`0dda7b472` mend or unchanged standing line is explicitly noted).
  - `M14` six differences (`B736`, `B779`, `B1858`, `B1867`, `B1870`, `B1873`): base `38d2a36dc`, read at `0dda7b472` (with cross-check against `c40446392`).
- **Files of `A2-R80b` opened prior to this card commit:** `docs/seats/agy-002.md` (`M12`, `M13`, `M14`) and `git log` subject lines only. **Zero** of the eighteen assigned arc differences have been opened for `A2-R80b` prior to committing and pushing this card (`expectations committed first`, `docs/seats/README.md` § 7, § 12, and § 13).
- **Protocol anchor:** `docs/seats/README.md` §§ 6, 7, 9, 12, and 13; `TERMINOLOGY.md`; `WORKING_RULES.md`

---

## 1. The Package and the Question, in One Sentence

Across the eighteen supplemental arc differences added to `agy-002`'s Review 80 card — two at `896cae025..c40446392` (`B1884`, `B1889`, leaving aside all lines on `agy`-family work) and sixteen over Review 79's window `38d2a36dc..0dda7b472` (`B731`, `B732`, `B733`, `B734`, `B942`, `B1028`, `B1030`, `B1067`, `B1222`, `B1643` from `M13`, plus `B736`, `B779`, `B1858`, `B1867`, `B1870`, `B1873` from `M14`) — do every mathematical correction, scope bracket, builder-to-artifact regeneration, sibling-file update, and verification lock hold, or do any over-claim, miscompute, fail to travel, or pass under planted reversions?

---

## 2. What Will Be Delivered, and What Done Means

Done means committing inside `relays/` on `origin/agy-002/verify`, in strict three-commit order before starting `A2-C3` (`WP-1.2`):

1. **Commit 1 (this card + `relays/STATUS_AGY-002.md`):** Locks the scope, conflict-of-interest exclusions, pre-read failure hypotheses, and controls **before** opening any of the eighteen arc differences.
2. **Commit 2 (`relays/r80b/verify_r80b_quotes_and_calcs.py` and `relays/r80b/verify_r80b_quotes_and_calcs_out.txt`):** Committed and pushed **before** updating `relays/REVIEW_80_AGY-002.md`, mechanically verifying:
   - exact single-line presence (with zero `|` characters) of every supplemental `exact quotation` cell at its assigned read commit (`c40446392` for `M12`; `0dda7b472` — and checking whether unchanged at `c40446392` — for `M13` and `M14`), plus negative control `CTL-R80B-QUOTE`;
   - independent mathematical/structural recomputation for each of the ten `M13` corrections, the non-COI changes in `B1884` and `B1889` (`M12`), and the six `M14` differences (including comparing `B1858`'s generated node files against `map_source.py` and its builder at `0dda7b472`, and auditing the changed scripts, data, hash lists, and locks in `B736`, `B779`, `B1867`, `B1870`, `B1873`);
   - isolated temporary-directory planted-reversion tests (`CTL-R80B-LOCK`) against the lock of any arc whose mend or `arc_verdict.json` is not held by a test.
3. **Commit 3 (`relays/REVIEW_80_AGY-002.md` and `relays/STATUS_AGY-002.md`):** Appends the supplemental section to `relays/REVIEW_80_AGY-002.md` (keeping rows `R01` through `R36` byte-for-byte untouched), with:
   - any supplemental findings in a four-column § 13 table (`pipe count == 5`, exact single-line quotes, plain-word numbers in Column 4);
   - explicit conflict-of-interest exclusions for `B1889` (`agy`-family lines) and any `B1884` hunk answering `agy-002`'s own findings;
   - a numbered item-by-item account for **every one** of the eighteen arcs stating either what defect was found or that nothing was found and exactly what was checked (`M13` requirement).

---

## 3. How It Could Come Out Wrong, Written Before Reading or Computing

1. **Incomplete travel of Review-79-window corrections (`M13` ten arcs):**
   - A correction to `FINDINGS.md` in an older arc (`B731..B734`, `B942`, `B1028`, `B1030`, `B1067`, `B1222`, `B1643`) may leave `arc_verdict.json`, `docs/VERDICT_LEDGER.md`, `docs/THEOREM_REGISTRY.md`, `docs/LAW_MAP.md`, `docs/RETRACTIONS.md`, or the arc's own verification script/test un-updated, or may have no lock holding the amended sentence or `arc_verdict.json` against reversion.
   - A mathematical correction (sign, subgroup index, congruence level, rank, or bound) may introduce a secondary slip in an adjacent sentence or table cell.
2. **Non-page / non-verdict changes in `M14`'s six arcs (`B736`, `B779`, `B1858`, `B1867`, `B1870`, `B1873`):**
   - In `B1858`, `map_source.py` may misstate a node's scope, premise, or citation relative to its pinned arc, or the committed `NODES.json` / `CLOSURE_MAP.md` at `0dda7b472` may diverge from running the builder.
   - In `B736`, `B779`, `B1867`, `B1870`, and `B1873`, changes exclusively in scripts, tests, JSON artifacts, or hash files may alter what a lock checks (weakening an assertion, hard-coding an exception, or leaving a hash/artifact mismatch) without updating `FINDINGS.md` or `arc_verdict.json`.
3. **Non-COI `B1884` and `B1889` diffs at `896cae025..c40446392` (`M12`):**
   - `B1889`'s builder, `SEATS.md`, `FINDINGS.md`, `arc_verdict.json`, or `test_b1889` on non-`agy` seats may miscount rows, misclassify a seat's ledger state, or leave a lock gap; `B1884`'s non-COI changes (`B1895` transpose propagation is excluded where it answers `agy-002`'s `R79b` Row 14 — we will verify provenance of each hunk in `B1884` and leave aside any hunk answering `agy-002`'s `A5`, `2A14`, or `R79b` Row 14!) may contain non-COI mathematical, citation, or lock defects.

---

## 4. What It Rests On, and What It Must Not Touch

- **Rests on:** `origin/main` at `c40446392` (for `M12` diffs from `896cae025`) and at `0dda7b472` (for `M13` and `M14` diffs from `38d2a36dc`, cross-checked against `c40446392`).
- **Must not touch:** Any file outside `relays/`; `B1895` or `B1897`; lines on `agy`-family work in `B1889` or hunks answering `agy-002`'s own findings in `B1884`; any other session's branch or review file; any measured physical value or held-out target (`0 of 19`).

---

## 5. Controls That Must Fail If the Work Is Broken

1. **`CTL-R80B-QUOTE`:** A single-word mutation of a real line from `0dda7b472` or `c40446392` must be rejected by `verify_r80b_quotes_and_calcs.py`.
2. **`CTL-R80B-LOCK`:** Every lock or builder finding must pass on unmodified target state and fail/reproduce cleanly in an isolated `tempfile` run before entering `REVIEW_80_AGY-002.md`.

---

## 6. What Is Needed From `main` or From Another Seat

- Nothing (`M12`, `M13`, and `M14` assign `A2-R80b` directly ahead of `WP-1.2`).

0 of 19.
