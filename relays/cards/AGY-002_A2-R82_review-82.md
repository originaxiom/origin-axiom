# Card A2-R82: Cold Review 82 Reading of Window `0e637ea9e..73e71e277` at `origin/review-82/read` (`86930f574`) (`M28` & `M30`)

- **Seat:** `agy-002` (`origin/agy-002/verify`)
- **Messages:** `M28` and `M30` (*Review 82 first, then `A2-CANON`*)
- **Target Branch & Commit:** `origin/review-82/read` at commit `86930f574` (window base `0e637ea9e`), read strictly cold without comparing `86930f574` against `73e71e277` or `origin/main`, and without inspecting any other seat's review file (`agy-exp` or `chat1`).
- **Scope (`M28` & Protocol § 13):**
  1. Arcs `B1917` through `B1929` in full: each `FINDINGS.md`, status/metadata JSON, scripts, committed run outputs/JSONs, and lock tests;
  2. Dated corrections and addenda (`B1924`, `B1925`, `B1926`, `B1928`, and any window-modified pages);
  3. The `2026-11-13` rule in `WORKING_RULES.md` and its `negative-second-computation` gate in `scripts/gates/gates.py` (plus gate tests);
  4. Register rows `P-839` through `P-848` in `docs/PROBLEM_REGISTER.md`;
  5. Harvest rows in `docs/HARVEST_LEDGER.md` cited by `B1917`–`B1929` (leaving aside judgements of `agy-002`'s own work per § 13 and stating explicitly every such exclusion).
- **Firewall:** Strictly one hundred percent data-free (`zero` measured values imported or compared).

---

## 1. Pre-Read Expectations & Failure Criteria

1. **Sentence-by-Sentence Evidence Audit:** Every sentence added or amended in `B1917`–`B1929`, `WORKING_RULES.md`, `PROBLEM_REGISTER.md` (`P-839..P-848`), and cited harvest rows will be held directly against the underlying script, raw output JSON/log, and cited seat file at `86930f574`. Any sentence that claims more than the script computed (e.g., all characters/levels/orientations when only a subset was run, exact equality where only a finite tolerance or grid was tested, unconditional proof where a hypothesis remains open, or misquoted numbers/counts/signs) or omits a load-bearing caveat present in the raw output counts as a finding.
2. **Line-by-Line Lock & Gate Audit:** Every lock test in `B1917`–`B1929` and the `negative-second-computation` gate will be inspected line by line and tested conceptually and via standalone checks against adversarial mutations. Any assertion that cannot fail (vacuous loop, `>= 0` on a count/norm, tautological boolean, unanchored substring check that passes when a negation or number flips, or a lock reading a static dictionary literal without testing the rule) counts as a finding.
3. **Travel & Cross-Reference Audit (§ 13 items 5–8):** Every correction or downgrade in `B1917`–`B1929` (`B1924`, `B1925`, `B1926`, `B1928`, `P-839..P-848`) will be checked across governing pages, map nodes, and sibling files at `86930f574` for stale unmended wording, missing register rows, check labels stronger than § 12 permits, or hygiene breaches.
4. **Machine-Verified Verbatim Quotations:** Every finding in `relays/REVIEW_82_AGY-002.md` will carry exact file path, line number(s) at `86930f574`, and a character-for-character verbatim quotation verified by script against `86930f574` prior to commit, with any standalone numerical counterchecks committed first under `relays/r82/`.

0 of 19.
