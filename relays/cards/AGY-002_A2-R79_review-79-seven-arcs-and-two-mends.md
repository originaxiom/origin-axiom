# Card `A2-R79`: Review 79 Full Reading of Seven Arcs on `main` and Check of Two `M4` Corrections

- **Seat:** `agy-002` (`origin/agy-002/verify`)
- **Card ID:** `A2-R79` (proposed by `main` on `docs/seats/agy-002.md` under `M4` at `323f923278181ffbe69f8c3124182549ab0e3163`, committed at `f2625b73b`; **widened under `M5` at `0dda7b4725f613dbef273edafcd3fca73ccb245c` (`0dda7b472`)**, ahead of `A2-C2`)
- **Target commit of `main` printed by listener (`M5`):** `0dda7b4725f613dbef273edafcd3fca73ccb245c` (`0dda7b472`; window base `38d2a36dc`)
- **Governing rules:** `docs/seats/README.md` § 9 (firewall and privacy), § 12 (method-based check labels; results, not verdicts), and § 13 (reading for a review, including non-arc window diffs `git diff 38d2a36dc HEAD -- PATH`; `P-805`). Zero measured values (`0 of 19`).

---

## 1. The Package and the Question, in One Sentence

Under Review 79 (`P-805`, `docs/seats/README.md` § 13) at `main` commit `0dda7b4725f613dbef273edafcd3fca73ccb245c`, what statements unsupported by outputs, numerical discrepancies, over-wide claims, checks that cannot fail or defaults that hide failures, clock/environment reads, untravelled corrections, unindexed debts, over-strong check labels, or § 9 / § 12 rule breaches stand across (a) full readings of `B1878`, `B1880`, `B1883`, `B1884`, `B1886`, `B1887`, `B1890`, and `B1889` (leaving out the part of `B1889` on the `agy` family's sessions), (b) the two `M4`/`M5` mends in `B1221` and `B1641`, (c) the Review 79 window difference `38d2a36dc..0dda7b4725f613dbef273edafcd3fca73ccb245c` for `"GOVERNANCE.md"`, `"WORKING_RULES.md"`, `"TERMINOLOGY.md"`, `"GENESIS.md"`, `"CLAIMS.md"`, `"ROADMAP.md"`, `"README.md"`, and `"docs/seats/README.md"`, and (d) `main`'s own changes to its instruments in `38d2a36dc..0dda7b4725f613dbef273edafcd3fca73ccb245c` across `"scripts/checks"`, `"scripts/seats"`, and `"scripts/gates/gates.py"` (outside the advisor seat's four-patch series)?

---

## 2. What Will Be Delivered, and What Done Means

Committed in strict causal order on `origin/agy-002/verify`:
1. **`M4` Commits One–Three (already pushed at `f2625b73b`, `f43a5fbdc`, `f194f8034`):** pre-work card, raw independent check outputs, and initial `relays/REVIEW_79_AGY-002.md` at `323f923278181ffbe69f8c3124182549ab0e3163`.
2. **`M5` Commit One (this commit — before opening `B1889` or the `38d2a36dc..0dda7b4725f613dbef273edafcd3fca73ccb245c` window diffs):** updated `relays/STATUS_AGY-002.md` (`read: M5`) and this widened `A2-R79` card.
3. **`M5` Commit Two (raw verification & quotation-audit outputs at `0dda7b4725f613dbef273edafcd3fca73ccb245c` committed before updating `REVIEW_79_AGY-002.md`):** updated `relays/r79/verify_r79_quotes_and_calcs.py` and `relays/r79/verify_r79_quotes_and_calcs_out.txt` verifying every quotation (old and new) byte-for-byte against `0dda7b4725f613dbef273edafcd3fca73ccb245c` plus independent checks on `B1889` (outside the `agy` family section), the eight governing-page window diffs, and `main`'s instrument changes (`scripts/checks`, `scripts/seats`, `scripts/gates/gates.py`).
4. **`M5` Commit Three (complete `REVIEW_79_AGY-002.md` at `0dda7b4725f613dbef273edafcd3fca73ccb245c`):** updated `"relays/REVIEW_79_AGY-002.md"` naming commit `0dda7b4725f613dbef273edafcd3fca73ccb245c` and window `38d2a36dc..0dda7b4725f613dbef273edafcd3fca73ccb245c`, covering all eight assigned arcs (`B1878`, `B1880`, `B1883`, `B1884`, `B1886`, `B1887`, `B1889` excluding the `agy` family section, `B1890`), the two `M4`/`M5` mends (`B1221`, `B1641`), the eight governing-page window diffs, and `main`'s instrument changes, plus updated `relays/STATUS_AGY-002.md`.

---

## 3. How It Could Come Out Wrong, Written Before Any Run

1. **Branch-skew or stale-SHA error:** Every quotation and check in the updated review must be verified strictly against `0dda7b4725f613dbef273edafcd3fca73ccb245c` (where `B1641`, `NODES.json`, and `P-802` were just updated by `M5`), and every non-arc window diff must run `git diff 38d2a36dc 0dda7b4725f613dbef273edafcd3fca73ccb245c -- <PATH>` per `docs/seats/README.md` § 13.
2. **Quotation mismatch (`§ 13` machine check):** Paraphrasing, normalising Unicode, or trimming a quoted line would cause `main`'s machine quotation check against `0dda7b4725f613dbef273edafcd3fca73ccb245c` to discard a genuine finding.
3. **Conflict-of-interest breach (`§ 13` and `M5`):** In `B1889`, `M5` explicitly directs leaving out the part on the `agy` family's sessions (`agy`, `agy-002`, `agy-exp`); reviewing our own family's section in `B1889` instead of leaving it to another reader would breach `§ 13` and `M5`. Likewise, in `scripts/gates/gates.py`, `M5` directs focusing on `main`'s own changes outside the advisor seat's four-patch series.
4. **Cross-reader contamination (`§ 13`):** Opening any other session's branch or `REVIEW_79_*.md` file before the `M5` update to `"relays/REVIEW_79_AGY-002.md"` is pushed would invalidate the two-reader overlap estimate.
5. **Firewall breach (`§ 9`) or mask opacity:** Computing any held-out target or comparing with any measured value is forbidden; and writing explanations in digits alone without plain English number words would obscure counts when `main` reads `"relays/REVIEW_79_AGY-002.md"` through its number-hiding mask.

---

## 4. What It Rests On, and What It Must Not Touch

- **Rests on:** `origin/main` at `0dda7b4725f613dbef273edafcd3fca73ccb245c` and window base `38d2a36dc` (`docs/seats/agy-002.md` `M4` and `M5`, `docs/seats/README.md` § 9, § 12, § 13, the eight assigned arcs, the `B1221` and `B1641` mends, the eight governing pages, and `scripts/checks`, `scripts/seats`, `scripts/gates/gates.py`).
- **Must not touch:**
  - Zero branches of other seats (`chat1`, `sm`, `agy-exp`, `agy`, `cld-advisor`, `physical`) before or during `A2-R79`.
  - Zero judgement on the `agy`-family section of `B1889` (`M5`).
  - Zero files outside `relays/` on `origin/agy-002/verify`.
  - Zero held-out targets or measured physical values (`0 of 19`).
  - Zero relabelling or closing of any arc (`§ 13`).

---

## 5. One Control That Must Fail If the Work Is Broken

- **Machine-Quotation & Planted-Mismatch Control (`CTL-R79-QUOTE` and `CTL-R79-CALC`):**
  Before `"relays/REVIEW_79_AGY-002.md"` is committed, our pre-prose script in `"relays/r79/"` extracts every quoted target string from the structured findings table, looks up the exact blob in `0dda7b4725f613dbef273edafcd3fca73ccb245c` via `git show`, asserts exact unique substring presence for every finding, and asserts that both a planted single-word quote mutation (`CTL-R79-QUOTE`) and a planted numerical/instrument perturbation (`CTL-R79-CALC`) are rejected.

---

## 6. What Is Needed From `main` or From Another Seat

Nothing (`A2-R79` as widened by `M5` is approved; proceeding directly to full reading at `0dda7b4725f613dbef273edafcd3fca73ccb245c`).

0 of 19.
