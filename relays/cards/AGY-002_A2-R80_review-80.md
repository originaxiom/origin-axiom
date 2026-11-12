# Card `A2-R80`: Review 80 Cold-Read of Assigned Arcs, Diffs, Governing Pages, Ledgers, and Landed Enforcement Series (`0dda7b472..c40446392`)

- **Seat:** `agy-002` (`origin/agy-002/verify`)
- **Card ID:** `A2-R80` (assigned and pre-approved on commit in `docs/seats/agy-002.md` under `M11`)
- **Commit of `main` read:** `c40446392` (window base `0dda7b472`; five-arc diff base `896cae025`)
- **Files of `A2-R80` opened at `c40446392` prior to this card commit:** `docs/seats/agy-002.md` (`M11`) and `git log` subject lines only (`docs/HARVEST_LEDGER.md` was materialized earlier only inside `A2-R79d`'s isolated `B1881` lock runner and not read for `A2-R80`). **Zero** target arcs, diffs, governing pages, ledgers, or enforcement scripts at `c40446392` have been opened for `A2-R80` prior to committing and pushing this card (`expectations committed first`, `docs/seats/README.md` § 7, § 12, and § 13).
- **Protocol anchor:** `docs/seats/README.md` §§ 6, 7, 9, 12, and 13; `TERMINOLOGY.md`; `WORKING_RULES.md`

---

## 1. The Package and the Question, in One Sentence

At commit `c40446392` on `main`, across the assigned scope of Review 80 — three full arcs (`B1892` less our own rows, `B1893`, `B1896`), five arc diffs from `896cae025` (`B1862`, `B1878`, `B1880`, `B1885`, `B1890`), the governing pages and ledgers from `0dda7b472` (`GENESIS.md`, `WORKING_RULES.md`, `docs/seats/README.md`, Review 79 in `docs/progress/REVIEWS.md`, the two dated notes of `docs/RETRACTED_PHRASES.md`, `P-811` through `P-823` in `docs/POINT_REGISTER.md`, and the thirteen mathematical retraction rows in the last section of `docs/RETRACTIONS.md` held to their named sources), and the two landed enforcement series (`scripts/gates/gates.py`, `scripts/checks/retraction_sweep.py`, `scripts/checks/check_test_vacuity.py`, and their three locks in `tests/`) — what claims exceed their proof, what calculations, counts, or source cross-checks fail, what locks pass on broken state or miss real violations, and what corrections fail to travel across sibling files?

---

## 2. What Will Be Delivered, and What Done Means

Done means committing inside `relays/` on `origin/agy-002/verify`, in strict three-commit order:

1. **Commit 1 (this card + `relays/STATUS_AGY-002.md`):** Locks the scope, conflict-of-interest exclusions, pre-read failure hypotheses, and controls **before** opening any `A2-R80` file at `c40446392`.
2. **Commit 2 (`relays/r80/verify_r80_quotes_and_calcs.py` and `relays/r80/verify_r80_quotes_and_calcs_out.txt`):** Committed and pushed **before** writing `relays/REVIEW_80_AGY-002.md`, mechanically verifying:
   - byte-for-byte single-line presence of every `exact quotation` cell in `git show c40446392:<file>` (with a planted single-word mutation control `CTL-R80-QUOTE` that must fail);
   - independent mathematical/combinatorial recomputation and source-to-row verification on all thirteen mathematical retraction rows in the last section of `docs/RETRACTIONS.md`, the counts and checks of `B1892` (non-self rows), `B1893`, `B1896`, and the five `896cae025..c40446392` arc diffs (`B1862`, `B1878`, `B1880`, `B1885`, `B1890`);
   - adversarial planted-error tests against `scripts/gates/gates.py`, `scripts/checks/retraction_sweep.py`, `scripts/checks/check_test_vacuity.py`, their three `tests/` locks, and the locks of the reviewed arcs (`CTL-R80-LOCK`), testing both relevant `A2-C2` specifications and fresh structural edge cases against what Series 2 and Series 3 explicitly claim to hold.
3. **Commit 3 (`relays/REVIEW_80_AGY-002.md` and `relays/STATUS_AGY-002.md`):** One review file formatted per `docs/seats/README.md` § 13:
   - a four-column findings table (`arc | file | exact quotation | what is wrong, and how you know`) with `pipe count == 5` on every table line, every quotation exact on a single line at `c40446392`, and every number, count, dimension, or bound in the fourth column spelled out in plain English words so nothing is lost through `main`'s mask;
   - explicit conflict-of-interest disclosures naming every row or item left aside because it judges `agy-002` or `agy`-family work (`B1892` `A1..A26` and `agy`-family summary counts, `P-811..P-823` rows judging our own deliverables, `A2-C2` assessment text);
   - a concise cold-read summary of what held cleanly across each assigned block (`expectations committed first`, `recomputed on another family of model`, `tested against planted errors`, `CANNOT CHECK` where applicable, `0 of 19`).

---

## 3. How It Could Come Out Wrong, Written Before Reading or Computing

1. **Over-claiming vs scope ceilings in Enforcement Series 2 & 3 (`B1893`, `B1896`):**
   - `gates.py`, `retraction_sweep.py`, or `check_test_vacuity.py` may state a strong general invariant ("a gate is a function of the commit", "reads every tracked text file in one letter case and across line breaks", "refuses every test in which no assert can fail") while leaving concrete bypasses inside the stated scope (for example: Markdown inline formatting, punctuation/hyphenation/Unicode normalization, multi-line tables or blockquotes in phrase matching; AST nodes in `CANNOT-FAIL` such as boolean short-circuiting `True or call()`, empty-loop `for x in (): assert ...`, `assert not False`, tuple/dict unpacking, or multiple bindings; git index vs `HEAD` vs untracked submodules/symlinks/worktrees or non-UTF8 / >5MB boundary errors in `gates.py`; or locks in `tests/` whose negative tests pass for the wrong reason).
   - Conversely, we must **not** fault Series 2 & 3 for items explicitly deferred to Series 4 or explicitly declared out of scope in the gate's own sentence/docstring: every finding must violate what the landed code, docstring, arc, or register row at `c40446392` claims to hold now.
2. **Mismatches in the thirteen mathematical rows of `docs/RETRACTIONS.md` or `P-811..P-823`:**
   - A catch-up table summarizing sixty-one arcs (`P-823`) and thirteen mathematical corrections can misquote the retracted formula, invert a sign or hypothesis, cite the wrong arc/section, or omit a scope qualification present in the named source arc. Holding each of the thirteen rows directly against its named source file at `c40446392` tests this systematically.
3. **Incomplete travel or tripwire bypasses in the five `896cae025..c40446392` diffs (`B1862`, `B1878`, `B1880`, `B1885`, `B1890`):**
   - `B1862`'s stricter `OLD_FORMS` lock (`P-817`), `B1885`'s verdict-line mend, `B1880`'s hash-list / untracked-root updates, `B1878`'s gate-replacement note, or `B1890`'s diff may leave sibling files (`arc_verdict.json`, `THEOREM_REGISTRY.md`, `LAW_MAP.md`, `PROGRAMME.md`, `VERDICT_LEDGER.md`) out of sync or contain locks that pass on realistic mutations.
4. **Conflict-of-interest or cross-reader contamination (`§ 13`, `P-781`, `M11`):**
   - `agy-002` must leave aside its own rows in `B1892` (and any `B1894` / `P-811..P-823` clauses judging `agy-002` or `agy`-family work), must exclude `B1895` and `B1897`, and must **never** open any other session's branch or `REVIEW_80_*.md` file.

---

## 4. What It Rests On, and What It Must Not Touch

- **Rests on:** `origin/main` strictly at `c40446392` (diffs from `0dda7b472` and `896cae025` as specified in `M11`).
- **Must not touch:** Any file outside `relays/`; `B1895` or `B1897`; our own findings rows in `B1892` / `B1894` or any assessment of `agy`-family work; any other session's branch or review file; any measured physical value or held-out target (`0 of 19`).

---

## 5. Controls That Must Fail If the Work Is Broken

1. **`CTL-R80-QUOTE` (Single-word quotation mutation control):** Mutating one word of a real line from `c40446392` must be caught and rejected by `verify_r80_quotes_and_calcs.py`.
2. **`CTL-R80-LOCK` (Clean vs mutated enforcement/lock control):** Every behavioral finding on `gates.py`, `retraction_sweep.py`, `check_test_vacuity.py`, or an arc lock must pass on unmodified `c40446392` control state and demonstrate the exact false pass or false failure in an isolated temporary repository/module execution before entering `REVIEW_80_AGY-002.md`.

---

## 6. What Is Needed From `main` or From Another Seat

- Nothing (`M11` approves `A2-R80` upon commit).

0 of 19.
