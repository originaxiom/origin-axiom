# B1850 — THE OPEN LEADS AND THE BACKLOG CONFIRMED ONE BY ONE (Review 76's R76-1, the rest of P-617, and P-616)

**Verdict: PROVED (a process arc; data-free).** cc (main), 2026-11-06/07, S306j, at the owner's word on Review 76's items
("lets do them"). Review 74's readers had proposed closing 73 of `docs/OPEN_LEADS.md`'s 77 open leads and 240 of the
harvest ledger's SCHEDULED rows. The register's rule is that no closure is applied on a reader's word. This arc checks
every one of those proposals at its pointer. B1849 did the register's lead rows. 0 of 19.

## 1. How the proposals were checked

- **Six read-only checkers.** Six fresh-context agents each took a slice: two for the answered leads, one for the
  carried leads, and one per backlog report.
  - Each read the lead or row, the reader's reasoning and the pointer, and returned a verdict.
  - Each verdict came with a verbatim quote from the file that decides it. The instruction was to default to "not
    confirmed".
  - They edited nothing and ran no code.
- **Main's checks.**
  - Every quote was found verbatim at its path (`quote_check.py`: 313 of 313; `quote_check_run.txt`).
  - Main read every decision and its reason, and applied only confirmed closures.
  - One closure rested on a reader's hand derivation, so main ran its own computation (L206, § 3).
  - Each checker's skipped rows were matched against the reader's own totals (the lead and debt rows).
- **The records:** `checks_open_leads.json` and `checks_backlog_{cloud,physics,retired}.json` hold each verdict, path
  and quote. `apply_open_leads.py` and `apply_backlog.py` make the edits.

## 2. The results

- **The open leads: 24 of the reader's 73 proposals confirmed, and closed** (`docs/OPEN_LEADS.md`'s headings).
  - **16 answered:** L149, L158, L166, L174, L175, L177, L184, L188, L196, L202, L204, L206, L217, L220, L222 and L234.
    Several already said CLOSED in their own bodies; the heading was never marked.
  - **8 carried in full by register rows:** L151, L154, L165, L176, L191, L232, L248 and L249.
  - **L178** was already WITHDRAWN.
  - **48 kept open.** Each gains a dated note saying what is answered or carried, and what is not.
  - **The reader's "carried in full by register rows" held for 9 of 32 leads.** For the other 23, some live part
    (or all) is in no row.
  - **The lead index:** 79 → 55 open, 42 → 26 stale. The ratchet baselines are lowered.
- **The backlog (P-616): 220 of 240 proposals confirmed.**
  - **216 rows closed** as CLOSED-HANDLED or CLOSED-NO-LOAD-NO-LEAD, each with main's reason and its evidence path, and
    the old disposition kept in [was: …]. Four confirmed rows were already off SCHEDULED: 13, 15, 44 and 623.
  - **10 re-pointed to the open rows that carry them:** P-613 (rows 248, 250, 254, 256, 309, 322), P-615 (350),
    P-528 (195), P-492 (419) and P-606 (200).
  - **10 kept SCHEDULED** with a dated reason: rows 125, 162, 171, 189, 207, 208, 266, 374, 414 and 448.
  - **The 36 rows the readers typed LEAD or DEBT are untouched.** P-616 now carries them.
- **The counter's substring bug is fixed.** Rows whose history kept the word were counted as open: "was: SCHEDULED",
  "Was: RECEIVED, SCHEDULED", "row 261's SCHEDULED".
  - The fix: `harvest_debt.is_scheduled` reads the current disposition only, with a planted test in
    `tests/test_harvest_scheduled_counter.py`.
  - The ledger-wide count is now 46, and SCHEDULED_BASELINE is lowered from 282 to 46.
- **A new point, P-730.** GENESIS points to harvest row 189 at five sites as "the audit lane's R57". Row 189 is the
  physics seat's R57; the audit lane's R57 was harvested in B1457 and has no row. The correction waits for GENESIS's next
  amendment (the foundation lock).

## 3. Main's own check (L206)

- **The claim:** the parabolic pair (the meridian ABABB, a) generates π₁(m003).
  - With SnapPy's presentation ⟨a, b ∣ abAAbabbb⟩, w = mer⁻¹a⁻¹mer⁻¹a⁻³ equals b in the holonomy to 8.5 × 10⁻¹⁵.
  - The control, w against a, is off by 2.00.
- **Why that settles it:** the holonomy is faithful into PSL(2, ℂ), so w = b in the group, and b lies in ⟨ABABB, a⟩
  (`l206_generating_pair.py`).
- P-334's dated note on B1401 stays owed.

## Seen first

- **Swept:** `VERDICT topic-sweep /P-616|SCHEDULED backlog|OPEN_LEADS read/: 1 of 1596 arcs on main match (PROVED 1);
  4 register rows match (DONE 1, QUEUED 3)`. The arc is B1849, this work's first half; the rows are P-616, P-617 and
  their neighbours.
- Read before acting:
  - Review 74's four reader reports (`frontier/B1831_review_74_the_decadal_review/verification/readers/`).
  - The lead-debt and harvest-debt gates' rules.
  - The register's earlier dispositions of every host row.
- **The literature:** none needed. This is a process arc over the record's own leads and rows. The one computation is
  a word identity, checked in SnapPy's faithful holonomy.

## 4. Disclosed

- **The checkers are agents of main's seat, not independent opinions.** Their verdicts are not counted as third
  opinions. What main verified is that each quote exists, and what each decision says. Where a checker said "not
  confirmed", main kept the row open: keeping a lead or a row open loses nothing.
- **Three checkers' reports were extracted from their own hand-back records by a script**, then checked quote by
  quote. The other three were transcribed.
- **A parser slip of main's own** labelled rows 214, 219, 224 and 237 as handled. The checker rightly skipped them as
  lead and debt rows. Main's count was corrected before applying anything.
