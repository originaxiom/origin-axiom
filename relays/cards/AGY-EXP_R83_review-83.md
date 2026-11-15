# Card `R83` — Full Blind Reading of Review `83` (`B1930` through `B1944`, `THE_SWEEP_OF_2026-11-14.md`, `P-849` through `P-858`, Scoreboard `S03` and `C02`, Cited Harvest Rows, and Window Diffs from `73e71e277` at `b35eac607`)

- **Seat:** `agy-exp`
- **Branch:** `agy/self-consistent-loop-2026-11-11`
- **Answering:** `M29` and `M30` on `docs/seats/agy-exp.md`
- **Pinned commit to read:** `b35eac607` (`origin/review-83/read`), with window diff base `73e71e277` where window differences apply
- **Blind-test integrity and isolation rules:**
  1. Never diff or compare `b35eac607` against `c8cece9be` or `origin/main` (`b35eac607` carries six planted faults hashed in `P-858` to test the readers; every finding must come strictly from auditing `b35eac607` on its own files and window base `73e71e277`).
  2. Never open, list, or inspect `agy-002`'s branch or review file before `relays/REVIEW_83_AGY-EXP.md` is committed and pushed.
  3. Pure mathematics and governance/evidence verification only (`0 of 19`): zero measured physical quantities opened or compared (`docs/seats/README.md` section nine), and mask-clean prose (`zero` decimal floats, `zero` scientific-notation literals, `zero` forbidden proper names or empirical-authority words, `zero` vendor/model names). Where an arc (`B1944`, scoreboard entries, etc.) compares with measured values, leave measured values and measured-value comparisons aside under the firewall and state explicitly what was left out, while auditing every pure-mathematical formula, derivation, script, output, amendment, lock assertion, register row, scoreboard typing, and harvest citation.
  4. Strict recusal under sections nine and thirteen on any arc, section, register clause, or harvest row judging `agy-exp`'s own work (`X-CANON`, `X-EXACT-W`, `X-SCAR`, `X-MEASURE`, `X-SURVIVAL`, `X-OWN`, etc.) or its own model family (`agy-002`, `the agy lane`), naming each recused item explicitly while checking `main`'s own scripts, locks, internal consistency, and pure-mathematical identities.

---

## 1. Package and Question (One Sentence)

At `origin/review-83/read` commit `b35eac607` (with window base `73e71e277`), which exact sentences, numbers, amendments, check labels, untravelled corrections, scoreboard typings, sweep entries, register rows, harvest citations, mathematical claims, or lock assertions across `B1930` through `B1944`, `docs/THE_SWEEP_OF_2026-11-14.md`, `P-849` through `P-858`, the scoreboard changes (`SE1` as `S03`; `C02` re-typed), cited `HARVEST_LEDGER.md` rows, and window-modified files violate criteria one through eight of `docs/seats/README.md` section thirteen — including the six faults planted by `main` and any real wording, scope, mathematical, propagation, or non-failing-lock defects?

---

## 2. Deliverables and Definition of Done (Four-Commit Plan)

1. **Commit One (this card + `STATUS_AGY-EXP.md`, committed before reading `b35eac607`):** `relays/cards/AGY-EXP_R83_review-83.md` and `relays/STATUS_AGY-EXP.md`.
2. **Commit Two (`relays/r83_verify/verify_r83.py` + `SCRIPT_SHA256.txt`, sealed before execution):** standalone audit, independent pure-mathematics recomputation, and sandbox lock-mutation script (sharing zero code with `main`) that:
   - runs all non-recused window lock tests at `b35eac607` in an isolated pure-mathematics sandbox (with any measured-value files stripped beforehand) and probes lock assertions with targeted semantic/data mutations to detect any assertion that cannot fail or pins a literal in place of testing the stated rule;
   - independently recomputes `B1940`'s modular translation invariance $\bar{F}(\tau + 1) = \bar{F}(\tau)$ across cusp heights (contrasting IEEE binary64 loss high in the cusp against arbitrary-precision arithmetic) and `B1942`'s mathematical identity on `agy-exp`'s own code, together with deciding pure-mathematical identities in `B1930` through `B1944`;
   - audits `B1937`'s rule and amendments `A1` through `A15`, `B1944`'s pure-mathematical claims and lock, `docs/THE_SWEEP_OF_2026-11-14.md`, `P-849` through `P-858`, scoreboard `S03` and `C02`, cited `HARVEST_LEDGER.md` rows, and all other files changed in `73e71e277..b35eac607`;
   - machine-verifies every quoted finding at `b35eac607` (`exact_match` at its exact one-based line number).
3. **Commit Three (`relays/r83_verify/verify_r83_out.json` + `OUTPUT_SHA256.txt`, committed unread):** raw JSON output of `verify_r83.py` committed in its own commit before inspection.
4. **Commit Four (`relays/REVIEW_83_AGY-EXP.md` + `relays/STATUS_AGY-EXP.md`, pushed to remote):** complete Review `83` report with machine-verified `file:line` quotations, explicit recusals and firewall boundaries, and one concise verification line for every clean item in scope.

---

## 3. How It Could Come Out Wrong (Pre-Read Failure Modes Watched Hard)

- **Wording vs evidence (`Criteria One, Two, Three, Five, Six, Seven, Eight`):**
  - A sentence in `FINDINGS.md`, `arc_verdict.json`, `THE_SWEEP_OF_2026-11-14.md`, scoreboard, or `POINT_REGISTER.md` (`P-849` to `P-858`) claiming more or less than its run file, script, amendment record (`B1937` `A1`–`A15`), or cited seat commit/row.
  - Untravelled amendments or corrections (`B1940` extended-precision correction of `B1932` area values, `B1937` `A1`–`A15`, scoreboard re-typing of `SE1`/`S03` or `C02`, or `HARVEST_LEDGER.md` dispositions lagging behind arc updates).
  - Check labels stronger than section twelve permits (`recomputed independently` or `recomputed on another family of model` without qualifying evidence), session keys credited inside mathematical claims (`claim_one_line` or `FINDINGS.md`), or post-ruling owner quotations.
- **Line-by-line lock audit (`Criterion Four`):**
  - Assertions that cannot fail (`all(...)` on an empty collection, tautological algebra on the same computed variable, hardcoded literal arithmetic, wide ceiling thresholds that pass corrupted data, or pinning literals instead of testing the claimed rule).
- **Pure-mathematical identities (`B1940`, `B1942`, `B1938`–`B1943`, `B1930`–`B1936`):**
  - Any sign, factor, level/conductor, character, weight, cusp-cutoff, or precision defect in `B1940`'s $\tau \to \tau + 1$ invariance check, `B1942`'s identity, or the companion arcs.

---

## 4. What It Rests On, and What It Must Not Touch

- **Rests on:** git objects at `b35eac607` (`origin/review-83/read`) and window diff base `73e71e277`, audited with standalone `python3` / `mpmath` / `numpy` / `ast` checks.
- **Must not touch:** `c8cece9be` or `origin/main` diffs against `b35eac607`; `agy-002`'s branch or review file; any measured physical quantity or comparison table (`0 of 19`); self-judgment on `agy-exp` or own-family work.

---

## 5. Pre-Registered Negative Controls (`verify_r83.py`)

1. **`C-R83-1` (Machine-quotation & line-number rejection control):** perturb one character and shift one line number by plus one on a reference line from `b35eac607`; `check_single_quote` must reject both.
2. **`C-R83-2` (Vacuous-lock mutation survival control):** run the sandbox lock-mutation harness on a synthetic vacuous assertion (`assert all(v > 0 for v in [])`) vs a genuine assertion (`assert v == 1`); the harness must flag the vacuous assertion as `CANNOT_FAIL` and mark the genuine assertion `CAUGHT`.
3. **`C-R83-3` (`B1940` translation & binary64 precision breakdown control):** verify that dropping the `24`-line order-five average to a single non-fixed line breaks $\tau \to \tau + 1$ invariance at moderate height, and that evaluating the frame in IEEE binary64 high in the cusp breaks $\bar{F}(\tau + 1) = \bar{F}(\tau)$ on the lightest singular ratio while arbitrary-precision `mpmath` preserves $\bar{F}(\tau + 1) = \bar{F}(\tau)$.

---

## 6. Needs from `main` or Other Seats

Nothing.

`0 of 19.`
