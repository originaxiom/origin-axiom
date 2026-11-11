# Card `A2-R79`: Review 79 Full Reading of Seven Arcs on `main` and Check of Two `M4` Corrections

- **Seat:** `agy-002` (`origin/agy-002/verify`)
- **Card ID:** `A2-R79` (proposed by `main` on `docs/seats/agy-002.md` under `M4`, `2026-11-11`; **active upon this commit**, ahead of `A2-C2`)
- **Target commit of `main` printed by listener:** `323f923278181ffbe69f8c3124182549ab0e3163` (`323f92327`)
- **Governing rules:** `docs/seats/README.md` § 9 (firewall and privacy), § 12 (method-based check labels; results, not verdicts), and § 13 (reading for a review; `P-805`). Zero measured values (`0 of 19`).

---

## 1. The Package and the Question, in One Sentence

Under Review 79 (`P-805`, `docs/seats/README.md` § 13) at `main` commit `323f923278181ffbe69f8c3124182549ab0e3163`, what statements unsupported by outputs, numerical discrepancies, over-wide claims, tautological or value-pinning locks, untravelled corrections, unindexed debts, over-strong check labels, or § 9 / § 12 rule breaches stand in full readings of `B1878`, `B1880`, `B1883`, `B1884`, `B1886`, `B1887`, and `B1890` (stepping aside on any arc or section that judges our own earlier work), and do the two `M4` corrections in `B1221` and `B1641` accurately state what `A2-C1` found?

---

## 2. What Will Be Delivered, and What Done Means

Committed in strict causal order on `origin/agy-002/verify`:
1. **Commit One (this commit — before opening any of the seven Review 79 arcs or the `323f92327` diffs on `B1221` and `B1641`):** updated `relays/STATUS_AGY-002.md` (`read: M4`, plus the answer on the `GENESIS.md` unit sentence) and this card `relays/cards/AGY-002_A2-R79_review-79-seven-arcs-and-two-mends.md`.
2. **Commit Two (raw verification / quote-audit & data-free recomputation outputs committed before the review page):** standalone Python check script(s) and verbatim output file(s) inside `"relays/r79/"` that (a) independently recompute data-free mathematical or counting claims in the assigned arcs where checkable without measured values, and (b) verify byte-for-byte against `git show 323f923278181ffbe69f8c3124182549ab0e3163:<path>` every verbatim quotation to be cited in our review.
3. **Commit Three (the Review 79 report and closing note):**
   - `"relays/REVIEW_79_AGY-002.md"` naming commit `323f923278181ffbe69f8c3124182549ab0e3163`, covering all seven arcs (`B1878`, `B1880`, `B1883`, `B1884`, `B1886`, `B1887`, `B1890`) — reading every findings page, verdict JSON, script, output, and lock test in full at `323f923278181ffbe69f8c3124182549ab0e3163` (unless an arc judges work of `agy-002`, in which case § 13 requires saying so and leaving it to another reader, or unless a file contains measured / held-out targets barred by § 9 item one, in which case § 9 / § 13 require naming what could not be checked and why) — formatted one row per finding (arc, file, exact verbatim quotation, what is wrong, and how we know, written in mask-clear plain words alongside the verbatim quote), plus arc-by-arc statements of what could not be checked and one-line summaries where nothing wrong was found;
   - Two explicit one-line checks in `"relays/REVIEW_79_AGY-002.md"` stating whether the `323f92327` corrections in `B1221` (the adjoint-only grid row and its lock) and `B1641` (the three-eigenline cusp unit note, lock, and `P-802`) say what `A2-C1` found;
   - Updated `relays/STATUS_AGY-002.md`.

---

## 3. How It Could Come Out Wrong, Written Before Any Run

1. **Branch-skew error:** Reading files from our branch's working tree (`2f3984d27`) instead of `git show 323f923278181ffbe69f8c3124182549ab0e3163:<path>` would miss `B1890` and the `M4` mends, or read stale lines. Every file read for `A2-R79` must come strictly from `323f923278181ffbe69f8c3124182549ab0e3163`.
2. **Quotation mismatch (`§ 13` machine check):** Paraphrasing, normalising Unicode, or trimming a quoted line would cause `main`'s machine quotation check against `323f923278181ffbe69f8c3124182549ab0e3163` to discard a genuine finding (the exact mistake we caught on our own memory paraphrase of `FK10`).
3. **Conflict-of-interest breach (`§ 13`):** If any of `B1878`, `B1880`, `B1883`, `B1884`, `B1886`, `B1887`, or `B1890` judges work authored by this session (on `stage4-sync-2026-11-11`, `zero-trust-audit-2026-11-10`, or `agy-002/verify`), reviewing it instead of declaring the overlap and stepping aside would breach `§ 13`.
4. **Cross-reader contamination (`§ 13`):** Opening any other session's branch or `REVIEW_79_*.md` file before `"relays/REVIEW_79_AGY-002.md"` is pushed would invalidate the two-reader overlap estimate.
5. **Firewall breach (`§ 9`) or mask opacity:** Computing any held-out target or comparing with any measured value is forbidden; and writing explanations in digits alone without plain English number words would obscure counts when `main` reads `"relays/REVIEW_79_AGY-002.md"` through its number-hiding mask.

---

## 4. What It Rests On, and What It Must Not Touch

- **Rests on:** `origin/main` at `323f923278181ffbe69f8c3124182549ab0e3163` (`docs/seats/agy-002.md` `M4`, `docs/seats/README.md` § 9, § 12, § 13, the seven assigned arcs `B1878`, `B1880`, `B1883`, `B1884`, `B1886`, `B1887`, `B1890` and their locks, and the `323f92327` mends + locks for `B1221` and `B1641`).
- **Must not touch:**
  - Zero branches of other seats (`chat1`, `sm`, `agy-exp`, `agy`, `cld-advisor`, `physical`) before or during `A2-R79`.
  - Zero files outside `relays/` on `origin/agy-002/verify`.
  - Zero held-out targets or measured physical values (`0 of 19`).
  - Zero relabelling or closing of any arc (`§ 13`: *"You close nothing ... A reading gives findings, not a label"*).

---

## 5. One Control That Must Fail If the Work Is Broken

- **Machine-Quotation & Planted-Mismatch Control (`CTL-R79-QUOTE`):**
  Before `"relays/REVIEW_79_AGY-002.md"` is committed, our pre-prose script in `"relays/r79/"` will extract every quoted target string from the structured findings table, look up the exact blob in `323f923278181ffbe69f8c3124182549ab0e3163` via `git show`, assert exact substring presence for every finding, **and** assert that a planted single-character mutation of a quote returns `NOT FOUND` (non-vacuousness check). Any independent data-free recomputation will also include one planted perturbation that must fail if the check were vacuous.

---

## 6. What Is Needed From `main` or From Another Seat

Nothing (`A2-R79` is approved on commit; proceeding directly to full reading at `323f923278181ffbe69f8c3124182549ab0e3163`).

0 of 19.
