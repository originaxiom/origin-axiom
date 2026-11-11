# Review 79: the web seat's reading of B1878, B1880, B1882, B1883, B1886 and B1888

**Reader:** the web seat (chat1), card `relays/cards/CHAT1_W-R79_review_79_seven_arcs.md` (545582095). **Main at:**
323f92327, the commit the listener printed with M4. Every arc was read through the mask; main's code was read
directly. The computations relied on are in `relays/chat1_2026-11-11_r79/` (`r79_checks.py` and its output),
committed before this file. Every quotation below was checked by machine against its file at 323f92327 (that
output's section Q), and the mask shows each one whole.
- **A fault of this seat's, mended before this file:** the first version of `r79_checks.py` (5046fb5be) spelled the
  vendor names in its pattern, in a tracked file. The version committed with this file imports main's own encoded
  pattern instead. An old output of this seat's (`relays/chat1_2026-10-14_the_first_row/run.txt`) carried one in a
  local path. It is cut to a relative path, with the unedited file's sha256 recorded beside it. The history keeps both.

**B1889 is not read.** It digests the seats' deliveries, this seat's among them, so it judges this seat's work.
By § 13 it is left for main to give to another reader. (The card's title and its § 1 still list it among the seven;
its § 2 leaves it.)

## 1. Findings

| arc | file | quoted exactly | what is wrong | how this seat knows |
|---|---|---|---|---|
| B1882 | `frontier/B1882_the_v1_card_run_on_main/FINDINGS.md` | "At the bottom end, at less than a tenth of it." | Kind 3: wider than computed. It holds for the seat's menu (0.06, 0.08, 0.08) and for five of the other six cells, but not for the first null's covariant menu: 12 lost against a share of 0.0667, ratio 0.18. § 5's dated sentence, now in B1726 and B1753, says over all menus that "a lower bottom end would add almost none". The same bullet's top-end range, "1.5 to 2", is exceeded under the other menus (2.08 to 2.36), so the bullet speaks of the seat's menu without saying so | `card/v1_null_run.txt` line 29 |
| B1886 | `ROADMAP.md` | "waits on a computation, at the owner's word (P-769)." | Kind 5: a correction that did not travel. The live root page still says that the relation of the tick to the owner's earlier ruling (2026-10-08) waits on a computation, and that none of these rulings is yet in a governing document. B1879 made the computation. B1886 entered the item in `GENESIS.md` v1.65, re-typed as a condition the weight must deliver | `ROADMAP.md` lines 741 to 743, last changed at 7480c2426 (B1878's landing). The file was edited again at b99bf8a2b, after B1886 landed (9ace774f4), and these lines were left. B1879's opening; B1886 § 2 |
| B1886 | `frontier/B1886_the_foundation_at_version_1_65/FINDINGS.md` | "the lock compares them all with the committed v1.64." | Kind 3: the lock's reach is narrower than the sentence. It reads only the 29 rows that open with one of its identifiers (its pattern at line 20; line 43 asserts 29). It does not read the foundation's other tables with a Status column, among them the table of claims about the generations. The result stands: this seat's own route finds none of those rows changed | `r79_checks.py` K2b: 19 such rows at v1.64, none with a changed status cell |
| B1886 | `frontier/B1886_the_foundation_at_version_1_65/verification/test_b1886_the_foundation_at_version_1_65.py` | "this checkout does not hold the commit of version 1.64" | Kind 4. On a checkout without 8f0b03814 (a shallow clone, or an export with no repository), the test of the arc's central claim skips and the suite stays green. Main's own gates refuse such a checkout ("a shallow clone must not pass with nothing checked", `scripts/gates/gates.py` line 244); this lock does not | the test's line 41 |
| B1888 | `frontier/B1888_the_public_form_scrutinised/verification/candidate_chain.py` | "so the chain here can be longer than the true one and not shorter." | Kind 3. Files are found from string constants (the patterns `ARC` and `FILE`, lines 29 to 30 and 76 to 82; literal paths, 83 to 84) and from import statements (86 to 90). A file whose name is built at run time is missed, as the arc's own Disclosed says. So the chain can be shorter than the true one, and "an upper bound" holds only for files named literally. The lock asserts the sentence "It is an upper bound" (test line 63) | the script's lines named; FINDINGS, Disclosed |
| B1888 | `frontier/B1888_the_public_form_scrutinised/FINDINGS.md` | "The derivation half never touches the measured values." | Kind 3, the same cause. What was measured is that the static chain from the census does not reach the measured file. "Never touches" needs the run-time case that the Disclosed section leaves open | `verification/candidate_chain_run.txt` line 22 |

## 2. Notes that are not findings

- **B1883's milestone rows overlap.** WP-0.6 is counted in M1 and again in M2, and WP-6.1 (C6) is in none. The rows
  also add to 43, but they read 19 started and 23 not started, against line 47's 18 and 24. They are B1861's
  definitions (`r79_checks.py` K3); the page does not say they overlap.
- **Quotations of the owner in pages dated 2026-11-11.** All six arcs landed before 7b89eda8a, the landing that
  applied his ruling that his messages are private (P-796). Only B1883's generated page changed after it. Where:
  - B1878's Disclosed: the sentence of a ruling confirmed on 2026-11-10;
  - B1880's § 8: the answer this seat's relay recorded;
  - B1883's opening paragraph and its verdict file's claim line: his question;
  - B1888's FINDINGS line 5: his question, relayed through the advisor seat;
  - B1861's `PROGRAMME.md`, lines 998 to 1001 and 1008 to 1011, which B1886's landing feeds: his answers to main's
    questions.

  § 13's kind 8 reads "after 2026-11-11", so none is a finding on its face. Whether the ruling reaches them is main's
  to say.
- **B1880 keeps r4,** a sentence of arrival in other words, as a test that asserts the gate lets it pass. That pins
  a known limit. It is disclosed, and it will fail the day the gate improves.

## 3. Arc by arc: what was done, and what could not be checked

| arc | what was read and done | not read or not checked, and why |
|---|---|---|
| B1878 | FINDINGS, verdict file and lock in full. K4: 696 first-parent commits after da25c4f49 up to the landing 7480c2426, the landing included. That is the arc's 695 plus its own commit. None of their messages carries a trailer or a vendor's name, by main's own pattern. **Nothing found** | the 2,965 commits and the 693 at or before da25c4f49: the history before 2026-09-10 was not fetched. The two gates' planted tests were not run |
| B1880 | FINDINGS in full; `read_class_a_run.txt` (9 of 9 equal after the substitutions); `measure_all_hash_lists_run.txt` §§ 1 and 2. Every count that can be added up holds: 2,247; 1,826; 354; 417; mismatch 144; no file 210; 11 of 11 with the advisor seat's verdict; 13 of 21 still passing. **Nothing found** | not read, for lack of time: the verdict file, the two scripts, the two JSON files, and the lock beyond its tests' names. The measuring script was not rerun. Classes C, D and E are not read entry by entry, as the arc says |
| B1882 | FINDINGS; the null run's output in full; the preregistered rule. Every 0.1% figure of §§ 2 and 3 matches the output. So do the first null's best-0.1% row of § 4 (line 25's last three bins over 1/15) and the three last-layer all-targets figures (lines 26, 42, 58). K1 recomputes the 13 exact intervals and the thresholds 133.3 and 134.6 with the same quantiles the card's own function uses. The agreement shows the transcription is right, not that a second method agrees | the 1% figures (§ 2's table, § 3's column), and in § 4 the inner-layer all-targets figures and both second-null best-0.1% rows: the run text prints no such layers, and `v1_null.json` was not parsed. Not read, for lack of time: the verdict file beyond its head, the lock beyond its tests' names, `PRE_RUN_NOTE.md`, `the_seats_stage_1/`, `v1_controls_run.txt`, `selftest_out.txt` and `v1_card.py`. The card was not run (hours) |
| B1883 | FINDINGS, the page, its data file, and the builder's counting code. The card's ten packages (8 started, 2 not) and the obligations (43 = 1 + 18 + 24) hold. K3 on the milestones (§ 2) | not read, for lack of time: the verdict file and the lock. The builder was not rerun; the page is gated against it at every push |
| B1886 | FINDINGS in full; the lock, run once (K5: 6 passed); this seat's own routes over `GENESIS.md`, K2 and K2b. K2 matches the 29 rows the lock reads, T-ROOT included. The first status word is unchanged in the 22 where this route finds one. The three new items are FK16, PF5 and SE3. K2b finds 19 rows of tables with a Status column, none changed. Recomputed independently, for those rows. B1886 cites this seat's card on the ground, verified in B1884; it does not judge it | the 7 rows whose status word this route does not know (F-AP, F-CI, F-FC, F-HE, FK1, FK11, GM5b). `GENESIS.md`'s wording beyond the status cells. The map's, the budget's and the falsifier register's entries. Not read: the verdict file |
| B1888 | FINDINGS in full (read first for this seat's cold read); the chain's run output; the lock's assertions; the script's method. The counts hold: 17 files, 3,032 lines, 14 arcs, 6 and 4 direct dependencies, two copies of the helper | the chain script was not rerun. The measured file is named in main's code and was not opened. Not read: the verdict file beyond its head, and `candidate_chain.json`. This seat is a party: its cold read answers B1888's ask |

## 4. M5's additions: the governing pages and fifteen arcs changed and not added

**Read as § 13 asks:** `git diff 38d2a36dc 0dda7b472 -- PATH` for each path main named, through the mask, with
0dda7b472 the commit the listener printed with M5. Every quotation of this section, in the table and in the notes,
was checked by machine against its file at 0dda7b472 (`relays/chat1_2026-11-11_r79/r79_checks_m5_out.txt`).

| arc | file | quoted exactly | what is wrong | how this seat knows |
|---|---|---|---|---|
| B1726 | `frontier/B1726_the_two_ingredients_replicated/FINDINGS.md` | "A lower bottom end would add almost none (0.06)." | Kind 3, the same root as § 1's B1882 row, carried into this window's dated note. The note quotes the covariant and free readings for the top end ("1.5 to 2"). For the bottom end it gives the seat's menu alone (0.06); the first null's covariant menu has 0.18 | B1882's `card/v1_null_run.txt` line 29 |
| B1726 | `frontier/B1726_the_two_ingredients_replicated/FINDINGS.md` | "among the well-fitted the last layer is below its neighbour" | Kind 3. B1882 § 4 says this of the seat's three cells ("in all three cells"); the note drops that limit. Under the first null's covariant menu the last layer is above its neighbour among the best 0.1% (0.130 against 0.123) | B1882's `card/v1_null_run.txt` line 31 |
| B1886 | `GENESIS.md` | "Eleven entries of the record came as suppositions accepted on a seat's recommendation, or relayed by a seat" | Kind 2: a number that differs from its source. The cited sort (the advisor seat's `rulings_sorted/THE_RULINGS_SORTED.md` @ 7726eeed, its § 1 table) counts the suppositions as fourteen entries that are eleven things | that table's row for suppositions, line 22, read through the mask (the file quotes the owner; nothing of it is quoted here) |
| (the governing pages) | `WORKING_RULES.md` | "81 decisions and 16 statements of what he means, which are his to make; 11" | Kind 2, the same source. These three are parts of the 111 rulings the sentence names, and they add to 108. The source's parts are 81, 16 and 14 entries (the fourteen being eleven things) | as above |
| B1886 | `ROADMAP.md` | "waits on a computation, at the owner's word (P-769)." | **A qualification of § 1's row, not a new finding.** The lines sit inside the section headed "VIEW REFRESH — 2026-11-11 (Review 78)". It was written at Review 78 (c626627cd) and corrected as part of it at 7480c2426, before B1879 and B1886. The same commit wrote the goal into `GOVERNANCE.md`, so "none is yet written into a governing document" can only describe the state at the review. If a dated refresh is a record of its review, the row is not a fault. It is still the newest view on the root page, and no later section says otherwise | `ROADMAP.md` at 0dda7b472, the heading at line 727; `git blame` |

**Notes that are not findings.**
- **`WORKING_RULES.md`, the rule of 2026-11-11 on one channel to the owner,** quotes him verbatim three times, his
  answer to main among them, on a governing page.
  - It stands beside the amendment of the same day (P-796), which asks that nothing he says be quoted. The amendment
    keeps what was recorded before its date; whether that covers the same day is main's to say.
  - B1877's lock pins two of his answers of 2026-11-11 as strings, and its new paragraph and claim line quote one.
  - B892's dated note says of the advisor seat's re-audit that it "accepts this mend". B1726 and B1753 say the card
    was "decided by the advisor seat's sealed card". These are words of the same day, before P-797 (7b89eda8a).
- **The protocol names one check two ways, and asks for a verdict where § 12 asks for a result.**
  - § 2 of `docs/seats/README.md` lists "recomputed with separate code"; § 12 ("these words and no others") has
    "recomputed independently" for the same thing.
  - § 8 asks a seat that uses its own code for "REPRODUCED, DIFFERS, or CANNOT CHECK". § 12 defines reproduced as the
    same code run again and says that a check has a result, not a verdict.
- **B1853 and B1872 are left.** Their dated notes verify this seat's card on the read-out as a value and its relay
  on what symmetry allows a state of the whole. They judge this seat's work.
- **B1675's change applies this seat's W-C3 finding.** It was read: the corrected sentence agrees with main's own
  run (718 that keep a line and 40 that keep all three), and the old sentence is kept.

**Read, and nothing found:**
- `GOVERNANCE.md` (the amendment is logged), `TERMINOLOGY.md`, `CLAIMS.md` and `README.md` (1,592 and 810 add up).
- `GENESIS.md`, but for the row above.
- B874: 34 = 2 + 2 + 6 × 5; seven classes, three real.
- B892:
  - every wall, nullity and count in the corrected note matches both new run outputs at all three roots;
  - the verdict file is re-indented, and its claim line gains a dated correction (E5) that agrees with the note.
- B1221: 72 = 3 × 2 × 12; 144 and 360 at 24 and 60 points; 12, 24 and 60 are all multiples of 6.
- B1486, B1494, B1499: dated notes, each disclosing a change made after a seal.
- B1641: corrected the same evening, as is register row P-802; 27/2 − 3/2 = 12.
- B1753: 2.0 to 2.4 under the other menus and a bottom end of 0.08, both match B1882's run.
- B1874: eleven class-A entries, two bearing on a result; the lock asserts both.
- B1877: three disclosures, and its claim line's over-reading corrected.
- B1861, its `FINDINGS.md` and the build run:
  - the last step, the comparison, rests on 42 = 43 − 1 packages (arithmetic and the builder's one-end rule; the
    order itself was not traced);
  - the budget's 47 items and 39 inputs, the exits (28 named, 11 untouched), the packages (1, 18, 24) and the
    audit's 73 all add up.

**Not read in this addition, and why:**
- B1861's generated `PROGRAMME.md` and `PROGRAMME.json`, line by line: 735 changed lines (590 in the JSON, 145 in the
  page), gated against their builder.
- B1861's builder, source and lock changes.
- B892's two new scripts and JSON outputs.
- `docs/seats/README.md` beyond §§ 1 to 8 and the §§ 9, 12 and 13 read earlier.
- Each governing page beyond its diff.

0 of 19.
