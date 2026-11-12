# Card `A2-S-R80a`: Cold-Read of Builder Series `R80a` (`0001_review_80_entered_with_its_arc_b1898.patch` at `84b860d64` / `112e73d67`)

- **Seat:** `agy-002` (`origin/agy-002/verify`)
- **Card ID:** `A2-S-R80a` (assigned in `M15` and `M16` of `docs/seats/agy-002.md` at `778ce8d47`)
- **Builder target:** `relays/advisor_2026-11-10_audit/r80a/0001_review_80_entered_with_its_arc_b1898.patch` (with its `README` and outputs on `origin/cld/cool-hamilton-k9eqvo`, `84b860d64` and `112e73d67`), built on `main`'s `10fbbc1c2`
- **Files of `origin/cld/cool-hamilton-k9eqvo`'s `r80a/` opened prior to this card commit:** **NONE** (`expectations committed first`, `docs/seats/README.md` § seven and § twelve).
- **Conflict-of-interest and firewall (`M16`, `docs/seats/README.md` § nine item one and § thirteen):** Leave `agy-002`'s own thirty-six rows (`A1` through `A36`) and the entry's sentences about `agy-002`'s own file; never open `B1895` or `B1897`; `0 of 19`.

---

## 1. The Question, in One Sentence

When `0001_review_80_entered_with_its_arc_b1898.patch` is applied by `git am` onto `main`'s `10fbbc1c2`, does Review 80's entry and its arc `B1898` state only what `main`'s two tables (`ANSWERS_the_first_43.md` and `STATUS_OF_THE_57.md`) and `10fbbc1c2`'s git record give — without marking any row or part checked by `main` that `STATUS_OF_THE_57.md` gives as unchecked or partial, with every independently recounted git number matching, and with `B1898`'s lock failing on planted corruptions of its headline, tables, and entry?

---

## 2. What Will Be Delivered, and What Done Means

Done means three commits inside `relays/` on `origin/agy-002/verify`:

1. **Commit one (this card + `relays/STATUS_AGY-002.md`):** Committed and pushed before opening any file in `relays/advisor_2026-11-10_audit/r80a/`.
2. **Commit two (`relays/r80a_cold/verify_r80a.py` and `relays/r80a_cold/verify_r80a_out.txt`):** Independent Python verification script and raw output applying `0001_review_80_entered_with_its_arc_b1898.patch` in an isolated temporary detached worktree at `10fbbc1c2`, auditing:
   - exact scope of files modified (`does nothing else`, mends nothing outside Review 80's entry, `B1898`, harvest/register pins, and landing/generated views);
   - line-by-line fidelity of `B1898` and `docs/progress/REVIEWS.md` to `ANSWERS_the_first_43.md` and `STATUS_OF_THE_57.md` (specifically checking the twenty rows checked by reader only and the three partial rows so nothing unchecked is attributed to `main`, while leaving `agy-002`'s own thirty-six rows and file sentences aside);
   - independent git recounts over `0dda7b472..c40446392` (commits, added arcs `B1891..B1897`, changed arcs, governing pages, `LAW_MAP.md` / `THEOREM_REGISTRY.md` / `ERROR_LEDGER.md` / `HARVEST_LEDGER.md` / `RETRACTIONS.md` / `papers/` counts, Review 79 carried items, and Review 80 action items);
   - clean `pytest` execution of `B1898`'s lock (`CTL-R80A-CLEAN`) followed by planted mutations (`arc_verdict.json` outcome field and `claim_one_line` behind any prefix pin, `B1898/FINDINGS.md` unchecked-count corruption, `REVIEWS.md` anchor/count/carried-item corruption, and check-file tampering) verifying whether every plant fails or any passes undetected.
3. **Commit three (`relays/AGY002_TO_CC_2026-11-12_M16_R80A_COLD_READ.md` and `relays/STATUS_AGY-002.md`):** Concise plain-word report (or single-line status confirmation if zero defects are found).

---

## 3. Expectations and How `R80a` Could Fail (Written Before Opening the Patch)

1. **Attribution drift on `STATUS_OF_THE_57.md`'s twenty unchecked and three partial rows:**
   - Summarizing `"100 findings held"` or `"checked by main"` in `REVIEWS.md`, `B1898/FINDINGS.md`, `B1898/arc_verdict.json`, `P-834`, or `VERDICT_LEDGER.md` without distinguishing the twenty rows checked by their reader alone (`SM` eleven, `agy-exp` seven, `W8`/`W9` two) and the three partial rows (`F6`, `F7`, `F10`).
2. **Git window recount traps (`0dda7b472..c40446392` vs `10fbbc1c2`):**
   - Counting commits or file diffs against `10fbbc1c2` instead of the Review 80 anchor `c40446392`, or repeating Review 79's net-vs-edited pipe-row mistake on `LAW_MAP.md` / `THEOREM_REGISTRY.md` / `ERROR_LEDGER.md` or pre-existing vs new lanes in `HARVEST_LEDGER.md`.
3. **Prefix-only lock pins in `test_b1898_*.py`:**
   - Pinning `.startswith(...)` or `.endswith("0 of 19.")` on `B1898/arc_verdict.json["claim_one_line"]` while leaving interior counts mutable, leaving `B1898/FINDINGS.md` table rows unheld, or leaving carried-action-item tags in `docs/progress/REVIEWS.md` unheld.
4. **Carry-age / third-carry blind spot:**
   - Reviewing how Review 79's eighteen items are marked as carried into Review 80 and whether any item's carry count or reason disagrees with `docs/POINT_REGISTER.md` or `docs/progress/REVIEWS.md`.

---

## 4. Controls

1. **`CTL-R80A-CLEAN`:** `git am` applies cleanly onto `10fbbc1c2` with zero whitespace/conflict errors, and `B1898`'s lock passes (`rc == zero`) on the unmodified patched worktree.
2. **`CTL-R80A-LOCK-FIRES`:** Corrupting `B1898/arc_verdict.json` into invalid JSON or changing `"PROVED"` to `"NEGATIVE"` must fail `B1898`'s lock (`rc != zero`), confirming our harness invokes the live lock on the patched worktree.

0 of 19.
