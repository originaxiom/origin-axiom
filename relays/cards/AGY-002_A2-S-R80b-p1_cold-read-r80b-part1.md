# Card `A2-S-R80b-p1`: Cold-Read of Builder Series `R80b` Part One (`112e73d67`, Three Patches on `B1861`)

- **Seat:** `agy-002` (`origin/agy-002/verify`)
- **Card ID:** `A2-S-R80b-p1` (assigned in `M15` of `docs/seats/agy-002.md` at `778ce8d47`)
- **Builder target:** `R80b` Part One on `origin/cld/cool-hamilton-k9eqvo` at `112e73d67` (three patches on `frontier/B1861_the_closure_programme/`, built on `main`'s `10fbbc1c2` plus `R80a`, answering `SM-28`, `SM-29`, and `F10(b)`, together with the full-suite addition to `R80a`)
- **Files of `origin/cld/cool-hamilton-k9eqvo`'s `r80b/` opened prior to this card commit:** **NONE** (`expectations committed first`, `docs/seats/README.md` § seven and § twelve).
- **Conflict-of-interest and firewall (`M15`, `docs/seats/README.md` § nine item one and § thirteen, `P-796`):** None of `SM-28`, `SM-29`, or `F10(b)` belongs to `agy-002`'s thirty-six Review 80 rows, and none touches `B1895` or `B1897`; quote zero words of the owner (`P-796`); `0 of 19`.

---

## 1. The Question, in One Sentence

When `R80b` Part One's three patches on `B1861` are applied in order onto `main`'s `10fbbc1c2` plus `R80a`, does each patch do strictly what `SM-28`, `SM-29`, and `F10(b)` in `STATUS_OF_THE_57.md` ask and nothing else — removing every owner quotation from `B1861`'s source, generated page, builder refusal, and patch text itself (`P-796`), making every planted quotation shape and punctuation-leading input pass before its mend and fail after it (including fresh unseen plants of `agy-002`'s own), and never writing `F10(b)` as checked by `main` where `STATUS_OF_THE_57.md` gives `F10(b)` as `"not checked"`?

---

## 2. What Will Be Delivered, and What Done Means

Done means three commits inside `relays/` on `origin/agy-002/verify`:

1. **Commit one (this card + `relays/STATUS_AGY-002.md`):** Committed and pushed strictly before opening any file of `r80b/` on `origin/cld/cool-hamilton-k9eqvo`.
2. **Commit two (`relays/r80b_p1_cold/verify_r80b_p1.py` and `relays/r80b_p1_cold/verify_r80b_p1_out.txt`):** Independent Python verification script and raw output applying `R80a` and `R80b` Part One step by step in an isolated temporary detached worktree at `10fbbc1c2`, auditing:
   - **Patch one (`SM-28`):** how the script applies cleanly without carrying the removed owner quotation in diff text (`P-796`), whether `B1861`'s source, builder refusal, and generated `PROGRAMME.md` match after rebuilding from source, and whether any quoted owner words remain anywhere in `B1861` or in the relay artifact itself;
   - **Patch two (`SM-29`):** whether `B1861`'s lock now detects quotations on `PROGRAMME.md` by structural shape rather than a single literal phrase, whether each of the builder's planted cases passes on Patch one and fails on Patch two while clean twins pass, and whether fresh unseen adversarial quotation shapes planted by `agy-002` (multi-line Markdown blockquotes `>`, indented blockquotes, smart curly quotes `“...”` / `‘...’`, guillemets, attribution dashes, inline quoted clauses) are caught or evade;
   - **Patch three (`F10(b)`):** whether `B1861`'s shortening helper on punctuation-leading strings fails before Patch three (returning only the ellipsis/mark) and succeeds after Patch three (including multi-character leading punctuation, brackets, mathematical symbols, empty/whitespace strings, and boundary-length inputs), whether a planted regression test is in the patch's own test (`passes before, fails after`), and whether `F10(b)` is kept strictly distinct from `main`-checked rows (`STATUS_OF_THE_57.md` marks `F10(b)` as `"not checked"`);
   - **Process-state leak check and full gate sweep:** independent reproduction of the builder's disclosed interaction between `B1861`'s lock and closure-gate tests in a single `pytest` process, plus clean-checkout gate checks on each patch.
3. **Commit three (`relays/AGY002_TO_CC_2026-11-12_M15_R80B_PART1_COLD_READ.md` and `relays/STATUS_AGY-002.md`):** Concise plain-word cold-read report to `main`.

---

## 3. Expectations and How `R80b` Part One Could Fail (Written Before Opening `r80b/`)

1. **`P-796` residue in Patch one (`SM-28`):**
   - A script-form patch avoids removed diff lines (`- ...`), yet could still embed a substring, hash-reversible literal, or partial phrase of the owner's words in its replacement locator, test fixture, or `README`, or leave `PROGRAMME.md` out of sync with `B1861`'s generator script when `build` is re-run.
2. **Shape-evasion gaps in Patch two (`SM-29`):**
   - A shape-based quotation detector on `PROGRAMME.md` may catch `>` blockquotes and ASCII double quotes `"..."` over a word-count threshold while missing Unicode curly quotes (`\u201c...\u201d`), single-quoted sentences, blockquote lines preceded by list indentation (`  > ...`), or multi-paragraph `>` continuations, or conversely hard-coding an allowlist for the `2026-10-08` three-word ruling name so broad that an adjacent quoted sentence on the same line or section is excused.
3. **Edge-case truncation in Patch three (`F10(b)`):**
   - Fixing leading punctuation in a word-boundary shortener by skipping the first token split can still return a bare mark when a string begins with two punctuation tokens separated by spaces (such as `"— (see ...)"`), an opening parenthesis/bracket before a long token exceeding `limit`, or all-punctuation input, or may keep no before/after planted test in `B1861`'s lock.
4. **Attribution slip on `F10(b)`:**
   - Calling `F10(b)` checked by `main` in a patch header, note, or `README` when `STATUS_OF_THE_57.md` gives `(a) held; (b) not checked`.

---

## 4. Controls

1. **`CTL-R80B-P1-CLEAN`:** Applying `R80a` and all three steps of `R80b` Part One onto a clean detached worktree at `10fbbc1c2` succeeds cleanly, regenerating `B1861/PROGRAMME.md` produces zero diff, and `B1861`'s lock exits zero (`rc == zero`).
2. **`CTL-R80B-P1-BEFORE-AFTER`:** Running Patch two's and Patch three's new test assertions against the tree immediately before each respective mend fails (`rc != zero`), and running them on the mended tree passes (`rc == zero`).

0 of 19.
