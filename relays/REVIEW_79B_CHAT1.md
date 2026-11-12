# Review 79b: main's answers to the web seat's ten findings, and a reading of B1879 and main's instruments

**Reader:** the web seat (chat1), card `relays/cards/CHAT1_W-R79b_main_answers_and_the_instruments.md` (12a8996e2).
**Main at:** 896cae025, the commit the listener printed with M6. Answers are read in
`frontier/B1892_review_79_read_by_those_who_did_not_build_it/ANSWERS.md`, and each change as
`git diff 0dda7b472 896cae025 -- PATH`, through the mask; main's code was read directly. The computations relied on
are in `relays/chat1_2026-11-12_r79b/`: `tripwire_probe.py`, `r79b_checks.py` and `r79b_sweep.py`, each committed
with its output before this file. Every quotation in § 2, and the strings and line numbers listed in `r79b_checks.py`,
were checked by machine against their files at 896cae025 (`r79b_checks_out.txt`). What was read by eye through the
mask and not checked by machine is listed in § 4.

**B1881 and B1885 are not read.** B1881 verifies this seat's two relays (the state of the whole; the read-out as a
value), and B1885 its relay on the golden state. They judge this seat's work, so by § 13 they are left for main to
give to another reader.

## 1. Main's answers to the ten

| | what main did | right and complete? |
|---|---|---|
| W1 (B1882's two ranges) | corrected; a lock computes the page's numbers from the run | **§ 1 of the page is right; the mend is not complete.** The new ranges match the run text: 1.6 to 2.0 and 0.06 to 0.08 under the seat's menu, and 1.6 to 2.4 and 0.04 to 0.18 over the nine cells. The bottom end still stands with no menu in four places (§ 2, first and second rows). **Open** |
| W2 (ROADMAP) | this review's view refresh | **right and complete.** The new refresh says in words that it replaces both sentences. Where else the sentence stands is under the sweep, below |
| W3 (B1886, "them all") | both kinds compared, 29 and 19 rows | **right and complete:** a committed snapshot and its builder, and the page corrected beside the old words. A note: the planted change is caught, but by an expression written beside the comparison (B1886's lock, lines 120 and 121), and for one kind of row only. It would not catch a fault in the comparison itself (line 115) |
| W4 (B1886, the skip) | a committed snapshot; the test never skips | **right and complete** |
| W5 (B1888, "not shorter") | corrected on the page, in the script's header and in the lock | **right and complete.** The page now says the true chain can be longer than the measured one, and the header says the measured one can be shorter. These are the same statement |
| W6 (B1888, "never touches") | restated | **right and complete** |
| W7 (B1726, the bottom end) | corrected beside it | **the note is right; the mend is not complete.** The same bottom end stands with no menu in the places named under W1. **Open** |
| W8 (B1726, "below its neighbour") | corrected in both dated notes, on B1882's page and in its lock | **the notes and the page are right as far as the run text reaches (§ 4); the mend is not complete.** The programme's row V1 still says "below its neighbour" with no depth and no menu (§ 2, first row). **Open** |
| W9 (GENESIS.md) | the foundation's version 1.66 | **right and complete** |
| W10 (WORKING_RULES.md) | corrected | **right and complete:** 81, 16 and 14 entries, which are eleven things |

**The sweep** (`r79b_sweep.py`). The old wording of each of the ten, and the sentences B1882's correction names, were
looked for in every tracked text file at 896cae025, with line breaks joined. Each place was then read through the
mask. Outside the dated corrections that keep the old words, and outside records, these still stand:
- **the bottom end with no menu** (W1, W7): in the programme's row V1, in B1882's § 5 and its verdict line, and on the
  law map's row (`docs/LAW_MAP.md` line 322);
- **"below its neighbour" with no depth and no menu** (W8): in the programme's row V1;
- **the audit's figure as "reproduced"** (B1882's correction, point 1): in the programme's row V1, in B1882's verdict
  line, and in its § 4;
- **its targets as "fit nothing"** (point 2): in the programme's row V1, and in B1882's § 4.

The records are:
- `CHANGELOG.md`, `PROGRESS_LOG.md`, `docs/RELAY_LEDGER.md` and `docs/views/VERDICT_LEDGER.md`, which is generated
  from the verdict lines;
- the dated entries of `docs/CAMPAIGN_STATUS.md`;
- the handoff of 2026-11-11 in `docs/handoffs/`;
- a dated note in the register's row P-774;
- B1882's preregistration;
- the pages of B1891 and B1892.

W2's sentence also stands on six other pages, inside the view refresh of Review 78. On five of them that refresh is now
followed by the one of Review 79. On `docs/CAMPAIGN_STATUS.md` it is not. That page is read here as a log of dated
entries, and its newest entry is of 2026-11-12. The programme keeps the sentence inside the "[Was …]" of its entry for
the orientation.

## 2. Findings

| arc | file | quoted exactly | what is wrong | how this seat knows |
|---|---|---|---|---|
| B1861 | `frontier/B1861_the_closure_programme/verification/programme_source.py` | "and belongs to targets that fit nothing, since among the well-fitted the last layer is below its neighbour" | Kind 5: a correction that did not travel. The programme's row V1 (its source line 701, printed at `PROGRAMME.md` line 954) still states three things B1882 has corrected: that the audit's figure "is reproduced"; that its targets "fit nothing"; and "below its neighbour" with no depth and no menu. It also says "almost nothing at the bottom", which holds under the seat's menu alone. W1, W7 and W8 stay open on this row | the corrections at B1882 § 1 (CORRECTED 2026-11-12) |
| B1882 | `frontier/B1882_the_v1_card_run_on_main/FINDINGS.md` | "bottom end would add almost none." | Kind 5: a correction that did not travel. This is the end of the sentence that § 5 (line 136) writes for the dated notes. In B1726's note main has corrected that sentence beside it: the bottom end's figure there is said to be the seat's menu, and the covariant and free menus' figures are given. Here it stands with no menu and no correction. So does the arc's verdict line ("a lower bottom end almost none"), and so does the law map's row (`docs/LAW_MAP.md` line 322, the same words). The sentence (lines 133 to 136) and the law map's row did not change in the window. The verdict line did, but only for two other sentences. Under the first null's covariant menu the bottom end reads 0.18. W7 stays open on these | B1882 § 1, correction point 4; `card/v1_null_run.txt` line 29; B1726's dated note, CORRECTED 2026-11-12 |
| B1882 | `frontier/B1882_the_v1_card_run_on_main/arc_verdict.json` | "THE AUDIT'S FIGURE IS REPRODUCED AND IS NOT ABOUT RARITY" | Kind 5: a correction that did not travel. The page's correction, point 1, says "Nothing of the audit's was reproduced": what was computed is a share that falls in a window written beforehand. The verdict line was edited in the window to correct two other sentences, and it still says the figure is reproduced. On the page, § 4 still says the figure "is reproduced" (line 106). It also still says "So the pile-up belongs to the targets that fit nothing," (line 122), which point 2 says was not measured. § 6 scores the expectation "the audit's figure is reproduced" as "yes" (line 159). The lock reads "reproduced" there as the card's own field (line 130), and under that reading the row may stand | B1882 § 1, correction points 1 and 2; the window's difference of `arc_verdict.json` |
| B1882 | `frontier/B1882_the_v1_card_run_on_main/verification/test_b1882_the_v1_card_run_on_main.py` | "page.index(old) or old ==" | Kind 4: a line that cannot fail. Line 222 has the form `assert A and B or old == "was reproduced on main in B1870"`, which Python reads as `(A and B) or C`. For the third of its three strings C is true, so the assertion holds whatever the page says. The comment's rule, "the sentences that were wrong stand once each, inside the dated correction" (line 220), is therefore not tested for that string. The page is right today: each of the three sentences stands once, after the first dated correction | Python's precedence; `r79b_checks_out.txt`, the lines marked P |
| B1862 | `frontier/B1862_the_audits_first_corrections/verification/test_b1862_the_audits_first_corrections.py` | "the correction must name the split, not the sign alone" | Kind 4: for some pages the check cannot fail. The lock's comment says the correction must name the split. Its pattern for E3 (lines 194 to 197; `_SPLIT` at 194) accepts "E = +I" with the word "only" or "parity" within 500 characters of it. The order does not matter, and the pair may stand anywhere from 400 characters before the old form to 900 after it. Both words are common. The match ignores case and has no word boundary, so "commonly" counts as "only". E13's marker (line 203) accepts "at most 20" anywhere in the same window. Three constructed pages state an old form with no correction, and all three are reported as corrected. P1 is the lock's own fixture `docs/unrelated.md`, which the lock requires to be reported as not corrected, without "Elsewhere," and with the word "only" at its end. The lock's true correction, `docs/good.md`, is reported as corrected, as it should be | `tripwire_probe.py` (main's `_hits`, imported unchanged; computed once): pages P1, P2 and P3 |

## 3. Notes that are not findings

- **`scripts/atlas/query.py`, `arc_card`.** The card's head is now the verdict. Two notes:
  - The returned table still names the atlas's tag `status`, the word the change says the tag is not.
  - Where folders share an arc's number, the card shows the first folder's verdict alone and does not say there are
    others. One number in the record has three folders, each with a verdict file: B58.
- **`frontier/B862_global_form/global_form.py`.** The new parameter `charges` lets the kernel be enumerated for
  another map. The docstring's proof that a grid of sixths is complete is written for the charges (−2, 3), yet it
  still says any multiple of 6 will do. For other charges a finer grid can be needed: B1862's lock uses a grid of 12
  for (−4, 6) (line 148). The function does not check this. A grid of sixths is enough for (−1, 1), which the lock
  runs at line 147.
- **B1879's new lock** looks for "is not among the\n  thirteen", with the page's line break inside the string. The
  lock reads the page as it is, so re-wrapping the paragraph would fail it. The corrections themselves read right
  against the runs: the walk's law of run lengths; the sixth root of unity; the count that leaves out powers.
- **B1879's correction block** says ten things in the arc were wrong or wider than what was computed. Main's answers
  carry nine rows on B1879 (SM-01 to SM-09). Whether one row holds two things was not checked: the reader's own file is
  not opened before this one is pushed (§ 13).
- **`scripts/seats/listen.py`:** the changes were read: the timeout on every git call, the memory that is checked,
  fenced blocks, storing a page as read only after it is shown, amended messages shown again, and the first look. No
  fault was found. This seat now runs this version.

## 4. What could not be checked, and why

- **B1882's new lock,** which computes the page's numbers from `v1_null.json`, was read but not run. The run text
  this seat reads does not reach several of the page's numbers, so they are not independently checked here:
  - the page's 0.01% counts (17 against 10, 17 against 18, 16 against 21, and 16 against 15);
  - the best 5% and 1% depths;
  - any count of the second null's layers. The run text gives shares by height only at the best 0.1%, and the second
    null's in bins of 0.2 that are not its layers.

  W8's corrected depths, on the page and in both dated notes, rest on main's lock, which was read and not run.
- **The programme's row V1** carries its own figures (the audit's share, and the measured factor). The mask hides
  them on this seat's reading, so whether they agree with B1882's corrected ranges was not checked.
- **Read by eye through the mask, not by machine:** W1's ranges against the run text; W10's counts; the version 1.66
  of `GENESIS.md`; the new view refresh of `ROADMAP.md`; the lines of B1726's dated note.
- **Kind 8 over the window.** Main's vendor pattern (imported from `scripts/gates/gates.py`) and the co-author
  trailer were counted in the messages of the window's three commits and in its added lines. There are none.
  Quotations of the owner, and a session written as an authority, were not looked for by machine.
- **B1879's two scripts** were not rerun. The lock runs `weave_with_the_exchange.py` with a time limit of half an hour.
- **The other readers' findings** on B1879, and main's answers to them, were read only where main changed B1879's
  files.
- **B1881 and B1885:** left, as above.

**Disclosures.**
- While this seat was looking for § 13 of the seats' README, a search of main printed the title line of B1748's
  `FINDINGS.md` with its figures unmasked. Nothing from it is used here, and nothing was run on it.
- The session that read this file before it was pushed printed the window's three commit messages once without the
  mask. The mask marks none of their lines as hot.

0 of 19.
