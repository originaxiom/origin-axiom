# CARD `X-R80`: FULL READING OF FOUR REVIEW-80 ARCS, FIFTEEN ARC DIFFERENCES, AND SEVEN INSTRUMENT DIFFERENCES (`c40446392` AND `0dda7b472`)

- **Address:** `agy-exp` (branch `origin/agy/self-consistent-loop-2026-11-11`)
- **Card:** `X-R80` (proposed by `main` in `M10`, prioritized ahead of `X-C1b` in `M11`, and expanded by four differences in `M12` on docs/seats/agy-exp.md at `origin/main` `5c7abd72a`; active upon commit)
- **Date:** `2026-11-12`
- **Pinned `main` commits read:**
  - `c40446392` for the four full Review-80 arcs (`B1891`, `B1894`, `B1895`, `B1897`), the eleven post-second-round arc differences (`git diff 896cae025 c40446392 -- frontier/<ARC>`), and the seven instrument/test differences (`git diff 0dda7b472 c40446392 -- <PATH>`), per `M10`;
  - `0dda7b472` (base `38d2a36dc`) for the four Review-79 window differences added in `M12` (`git diff 38d2a36dc 0dda7b472 -- frontier/<ARC>` on `B734`, `B1028`, `B1222`, `B1643`).
- **Mask and firewall discipline:** pure mathematics and governance/audit checks only; zero floating-point or scientific-notation literals in prose, zero measured values or held-out targets (`0 of 19`), zero authority verbs or vendor names, and strict recusal from any row or section judging `agy-exp` or its model family (`B1894` own-finding rows, `B1889` own-family session part, and any other self-judging clause).

---

## 1. The Package and the Question, in One Sentence

At `origin/main` commit `c40446392` (with diff bases `896cae025` and `0dda7b472`) and at `0dda7b472` (with diff base `38d2a36dc` for the four `M12` arcs), do any of the four full Review-80 arcs (`B1891`, `B1894`, `B1895`, `B1897`), the eleven post-second-round arc differences (`B862`, `B874`, `B1632`, `B1641`, `B1861`, `B1862`, `B1881`, `B1882`, `B1885`, `B1886`, `B1889`), the seven instrument/test differences (`scripts/seats/listen.py`, `scripts/atlas/query.py`, `scripts/checks/point_debt.py`, `tests/test_seat_listener.py`, `tests/test_b1641_w46_on_main_and_the_two_objects.py`, `tests/test_b874_ladder.py`, `tests/test_b1221_the_adjoint_control.py`), or the four `M12` Review-79 window differences (`B734`, `B1028`, `B1222`, `B1643`) contain any of the eight defects of section `13` of docs/seats/README.md — unsupported statements, mismatched numbers, claims wider than computed, non-failing locks, untravelled corrections, unindexed debts, over-strong check labels under section `12`, or post-ruling owner quotations / authority verbs / vendor names — and in particular do `B1895`'s identity on all `120` matrices of `SL(2, F_5)` and bound on the least reading hold from the statements alone, and does `B1881`'s rebuilt lock (`B1897`) resist adversarial planted mutations?

---

## 2. Deliverables and What Done Means

1. **Independent check script and raw output committed first** (`relays/x_r80_verify/`): before writing `relays/REVIEW_80_AGY-EXP.md`, commit a standalone check script and then its raw output (committed unread before the review prose) that:
   - independently derives and checks `B1895`'s identity across all `120` matrices of determinant `1` modulo `5` (`SL(2, F_5)`) and its bound on the least reading directly from the mathematical statements, without importing `B1895`'s producer code;
   - probes `B1881`'s rebuilt lock (`B1897`) and the locks of `B1891`, `B1894`, `B1895`, `B1897`, plus the touched tests (`test_seat_listener.py`, `test_b1641_w46_on_main_and_the_two_objects.py`, `test_b874_ladder.py`, `test_b1221_the_adjoint_control.py`), against planted adversarial mutations in temporary sandboxes / memory to check whether any way through remains;
   - checks every pure-mathematical calculation and machine-verifies every exact quotation against `c40446392` (or `0dda7b472` for the four `M12` diffs).
2. **One complete review file** (`relays/REVIEW_80_AGY-EXP.md`), naming `c40446392` (with diff bases `896cae025` and `0dda7b472`) and `0dda7b472` (with diff base `38d2a36dc` for `M12`), and reporting:
   - exact machine-verifiable quotations (arc/path, commit read, exact verbatim sentence or line, what is wrong, and how verified) for every finding across the eight criteria of section `13`;
   - item-by-item coverage across all four full arcs, all eleven `896cae025..c40446392` arc diffs, all seven `0dda7b472..c40446392` instrument/test diffs, and all four `38d2a36dc..0dda7b472` `M12` arc diffs, stating one line of what was checked wherever nothing wrong is found, and explicitly naming every recused or firewalled clause (`B1894` own-finding rows, `B1889` own-family session part, any other self-judging clause, and any `0 of 19` empirical comparison).
3. **Strict isolation:** zero other sessions' Review-80 files opened before `relays/REVIEW_80_AGY-EXP.md` is committed and pushed (`M10` and section `13`).

---

## 3. How It Could Come Out Wrong (Written Before Reading the Arcs)

- **Misquoted source line:** any finding whose quoted text does not match `c40446392` (or `0dda7b472` for `M12` items) character-for-character is set aside by `main`'s machine check, so every quotation must be verified verbatim against `git show <commit>:<path>` before commit.
- **Subtle bypass of a rebuilt lock (`B1881` / `B1897`):** a lock that runs a script or checks hashes/keys can still be bypassed if it leaves an assertion unguarded, checks only summary booleans or subset rows, allows a silent fallback, or leaves a dead/non-failing check standing beside the new check.
- **Scope or recusal breach:** reading another session's Review-80 file before push, touching a measured value (`0 of 19`), or failing to recuse on `agy-exp`'s own rows in `B1894` or own-family session part in `B1889`.

---

## 4. What It Rests On, and What It Must Not Touch

- **Rests on:** `origin/main` commits `c40446392`, `896cae025`, `0dda7b472`, and `38d2a36dc`, plus `M9`–`M12` on docs/seats/agy-exp.md (`5c7abd72a`) and section `13` of docs/seats/README.md.
- **Must not touch:** any other session's Review-80 branch or file prior to push, `B1887`, `agy-exp`'s own rows in `B1892`/`B1894`, `agy-exp`'s own model-family part in `B1889`, any measured quantity (`0 of 19`), or any file outside `relays/` on this branch.

---

## 5. One Control That Must Fail If the Work Is Broken

Before evaluating the real locks and claims in `relays/x_r80_verify/verify_x_r80.py`, the script must run three planted negative controls and abort with non-zero exit code if any control fails to fire:
- **`C-R80-1` (`SL(2, F_5)` swap-conjugation fault):** replace coordinate-swap conjugation `P M P^-1` with matrix transpose `M^T` across the `120` matrices of `SL(2, F_5)` (`M9`'s disclosed error from `M8`), asserting that transpose fails to transform the symmetric row ground into the column convention while swap-conjugation succeeds.
- **`C-R80-2` (Lock-probe harness fault):** run the lock-mutation harness against a deliberately tautological dummy test (`assert True`) and against a genuine invariant test (`assert det == 1`), asserting that the harness classifies the dummy test as non-failing (`SURVIVED`) and the genuine test as failing (`CAUGHT`).
- **`C-R80-3` (Verbatim quotation verifier fault):** perturb a single character in a known line of `c40446392` and assert that the verbatim-quotation checker rejects it immediately.

---

## 6. What Is Needed from `main` or Another Seat

Nothing is needed to execute `X-R80`; commits `38d2a36dc`, `0dda7b472`, `896cae025`, `c40446392`, and `5c7abd72a` are all present in the local git object store.

`0 of 19.`
