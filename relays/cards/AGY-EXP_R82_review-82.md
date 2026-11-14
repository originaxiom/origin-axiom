# Card `R82` — Full Blind Reading of Review `82` (`B1917` through `B1929`, Dated Addenda, `negative-second-computation` Gate, `P-839` through `P-848`, and Cited Harvest Rows at `86930f574`)

- **Seat:** `agy-exp`
- **Branch:** `agy/self-consistent-loop-2026-11-11`
- **Answering:** `M18` on `docs/seats/agy-exp.md` (`aa710437e`)
- **Pinned commit to read:** `86930f574` (`origin/review-82/read`), with window diff base `0e637ea9e` where window differences apply
- **Blind-test integrity and isolation rules:**
  1. Never diff or compare `86930f574` against `73e71e277` or `origin/main` (`86930f574` contains six planted faults hashed in `P-848` to test the readers; every finding must come strictly from auditing `86930f574` on its own files and window base `0e637ea9e`).
  2. Never open, list, or inspect `agy-002`'s branch or review file before `relays/REVIEW_82_AGY-EXP.md` is committed and pushed.
  3. Pure mathematics and governance/evidence verification only (`zero` measured physical quantities, mask-safe prose with `zero` decimal floats, `zero` scientific notation, `zero` vendor/model names, and `zero` authority words).
  4. Strict recusal on any arc, section, register clause, or harvest row judging `agy-exp` or its model family (`X-C1b`, `X-C1c`, `X-NEG`, `X-SM`, `X-C9`, or own-family session evaluations), naming each recused item explicitly.

---

## One-Sentence Question

At `origin/review-82/read` commit `86930f574` (with window base `0e637ea9e`), which exact sentences, numbers, check labels, dated corrections/addenda, gate rules, register rows, harvest citations, or lock assertions across `B1917` through `B1929`, `WORKING_RULES.md`'s rule of `2026-11-13` and its `negative-second-computation` gate, `POINT_REGISTER.md` rows `P-839` through `P-848`, and the harvest rows cited by those arcs violate criteria one through eight of `docs/seats/README.md` section thirteen — including the six faults planted by `main` and any real wording, scope, label, untravelled-correction, or non-failing-lock defects?

---

## Deliverables and Four-Commit Execution Plan

1. **Commit One (this card, committed before reading `86930f574`):** `relays/cards/AGY-EXP_R82_review-82.md`.
2. **Commit Two (`relays/r82_verify/verify_r82.py` + `SCRIPT_SHA256.txt` before output):** standalone audit and sandbox lock-mutation script that:
   - runs all non-recused lock tests at `86930f574` in isolated temporary sandboxes and probes every new lock assertion with targeted semantic/data mutations to verify whether any assertion cannot fail or pins a literal instead of testing the claimed rule;
   - independently recomputes pure-mathematical assertions where needed without importing producer modules;
   - tests the `negative-second-computation` gate script against synthetic compliant and non-compliant negative arcs/files;
   - machine-verifies every quoted finding (exact file path, exact line number, and character-for-character verbatim substring at `86930f574`).
3. **Commit Three (`relays/r82_verify/verify_r82_out.json` + `OUTPUT_SHA256.txt`, committed unread):** raw output of `verify_r82.py`.
4. **Commit Four (`relays/REVIEW_82_AGY-EXP.md` + `relays/STATUS_AGY-EXP.md`, pushed immediately):** complete Review `82` report covering every item in scope, every recusal, every finding with machine-checkable `file:line` verbatim quotation, and one concise verification line on each clean item.

---

## Pre-Read Expectations and Failure Modes Watched Hard (`M18` + Review `81` Lesson)

- **Wording vs evidence (`Criteria One, Three, Five, Seven, Eight`):**
  - Sentences claiming more (universal quantifier, stronger check label from section twelve such as `recomputed independently` or `recomputed on another family of model` where only one family/code ran, or settled status where an item is provisional/open) or less (omitting a disclosed failure mode, restriction, or hypothesis) than the tracked JSON/run output or cited seat file at `86930f574`.
  - Dated corrections and addenda (`B1924, B1925, B1926, B1928`) that mend one place while leaving the old un-mended claim standing in the title, header line, summary table, status file, register row (`P-839` to `P-848`), or harvest ledger.
  - Post-ruling owner quotations after `2026-11-11`, sessions written as authorities, or vendor/model names (`Criterion Eight`).
- **Line-by-line lock and gate audit (`Criterion Four`):**
  - Assertions that always evaluate to `True` (vacuous `all(...)` over an empty filtered list, tautological boolean disjunctions, `isinstance` or key-existence checks where value/sign/equality is claimed, tolerances wider than the effect tested, or helper checks that never exercise the failure branch).
  - Weakness or false-pass bypass in `WORKING_RULES.md`'s `2026-11-13` `negative-second-computation` gate (e.g., accepting self-recomputation on the same seat's code, missing status/disposition spellings, or exempting load-bearing negatives silently).
- **Numerical / cross-file mismatches and unindexed debts (`Criteria Two and Six`):**
  - Discrepancies between `FINDINGS.md`, `arc_verdict.json`, `.json`/`.txt` run files, `POINT_REGISTER.md` (`P-839..P-848`), and cited `HARVEST_LEDGER.md` rows, or owed follow-ups named in prose with no open register row.

---

## Three Negative Controls in `verify_r82.py`

1. **`C-R82-1` (Machine-quote & line-number check):** perturb one character and shift one line number on a reference line from `86930f574`; the verifier must reject both.
2. **`C-R82-2` (Lock-mutation survival check):** run the mutation harness against a planted vacuous test (`assert all(x > 0 for x in [])`) versus a genuine assertion (`assert x == 1`); the harness must classify the vacuous test as `CANNOT_FAIL` and the genuine test as `CAUGHT`.
3. **`C-R82-3` (Gate bypass control):** feed a synthetic negative record lacking a second independent computation into our gate-audit harness; the harness must flag any gate path that lets it pass.

`0 of 19.`
