# Card A2-R83: Cold Review 83 Reading of Window `73e71e277..c8cece9be` at `origin/review-83/read` (`b35eac607`) (`M38`)

- **Seat:** `agy-002` (`origin/agy-002/verify`)
- **Message:** `M38` (*Review 83 is opened: your reading card*)
- **Target Branch & Commit:** `origin/review-83/read` at commit `b35eac607` (window `73e71e277..c8cece9be`, with six planted faults whose hash is recorded in `P-858`), read strictly cold without inspecting `B1930`–`B1944`, `docs/THE_SWEEP_OF_2026-11-14.md`, or `P-849`–`P-858` on `origin/main` (`3a55f7360`), without diffing `b35eac607` against `c8cece9be` or `3a55f7360`, and without opening any other seat's `REVIEW_83` file before `relays/REVIEW_83_AGY-002.md` is pushed.
- **Scope (`M38` & Protocol § 13):**
  1. Arcs `B1930` through `B1944` in full at `b35eac607`: every `FINDINGS.md`, status/metadata JSON, script, committed run log/JSON, and lock test — above all `B1937` (the big run's rule and amendments `A1`–`A15`), `B1940` (corrected values and extended-precision frame), `B1944` (the look and its reading), and `B1938`, `B1939`, `B1941`, `B1942`, `B1943`;
  2. `docs/THE_SWEEP_OF_2026-11-14.md` and register rows `P-849` through `P-858` in `docs/PROBLEM_REGISTER.md` at `b35eac607`;
  3. The scoreboard's changes (`SE1` as `S03`; `C02` re-typed) across governing scoreboard/claim pages at `b35eac607`;
  4. Harvest rows in `docs/HARVEST_LEDGER.md` cited by `B1930`–`B1944` (explicitly excluding judgements of `agy-002`'s own work per § 13 and listing every excluded row).

---

## 1. Pre-Read Expectations & Failure Criteria

1. **Sentence-by-Sentence Evidence Audit:** Every sentence added or modified in `B1930`–`B1944`, `docs/THE_SWEEP_OF_2026-11-14.md`, `P-849`–`P-858`, scoreboard updates, and cited non-self harvest rows will be held directly against the underlying script, raw output JSON/log, and cited seat file at `b35eac607`. Any sentence claiming more or less than the underlying output shows (misquoted counts, signs, tolerances, `sha256` hashes, levels, amendments, scoreboard tallies, or scope overstatements) counts as a finding.
2. **Line-by-Line Lock Audit:** Every new or modified lock test in `B1930`–`B1944` and window gate scripts at `b35eac607` will be read line by line and tested conceptually and via standalone counterchecks against adversarial mutations. Any assertion that cannot fail when the stated claim is false (tautology, vacuous iteration, `>= 0` on a norm/count, unanchored string match, or reading a static dictionary flag without testing the rule) counts as a finding.
3. **Independent Recomputations (`M38`):** Recompute on standalone `agy-002` scripts (committed under `relays/r83/` before `relays/REVIEW_83_AGY-002.md`) `B1940`'s $\bar{F}(\tau + 1) = \bar{F}(\tau)$ check across height regimes, `B1942`'s order-15 identity, `B1943`'s fixed-line Smith normal form, and any algebraic/numerical identity in `B1934`–`B1944` whose text or lock could hide a planted sign, factor, or precision fault.
4. **Machine-Verified Verbatim Quotations & Hygiene:** Every finding in `relays/REVIEW_83_AGY-002.md` will carry exact file path, line range at `b35eac607`, and character-exact verbatim quotation verified by script against `b35eac607` prior to commit, keeping physical read-out 7-values strictly out of `.md` files.

0 of 19.
