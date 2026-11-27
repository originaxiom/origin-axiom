# B2019 — Review 89 entered: three cold readers of the window's process work caught six of eight plants and found eleven real faults; each checked by main on the live tree; seven mended here, four sent to the builder; the trial's arcs left to the trial again

**Verdict: PROVED (a process arc).** Main, 2026-11-27. Register rows P-589, P-869 and P-885. **0 of 19.**

## Seen first

- **Swept:** `VERDICT topic-sweep /Review 89|known.failures list|hash seed|PYTHONHASHSEED|dated.notes screen|stale screen/: 3 of 1759 arcs on main match (NEGATIVE 1, PROVED 2); 5 register rows match (QUEUED 5)`.
  This arc follows Review 88's method (B2018).
- **The literature:** none applies; this is a review of the record's own window.

## Why now, and what was read

- **When it opened: in time.** `gates.py review-due` printed 20 merges since Review 88's anchor, the threshold; the review
  opened at once, before the 34th that R84-4, R85-1 and R87-1 ask.
- **The window:** 64cc951b3 to 47ece044b, the anchor of this entry: 20 commits and 1 arc with a verdict, B2018, the
  sample the tool seeded by the anchor (`scripts/review/review_tools.py`).
- **Not read: the trial's arcs and tools.** R88-2 sent the arcs B2013 to B2017 to this review if the trial had not run.
  It has not run, only because the runner's sandbox is still with the builder.
  - Those arcs, and main's trial wrappers and controls under `relays/claims/main_trial/` (rebuilt in this window), are
    among the trial's cards. Natural plants are held in them, sealed (SHA-256
    07bca6c8cfeaa75c173153f47813b8786327250ef7b0500a857aba393ba59ad9).
  - A reading now would mend them before the trial and spoil it, so R88-2 is carried to Review 90 with this reason.
- **Read instead: the window's process work,** with B2018. The copy was a git archive of 47ece044b, cut into three
  folders, each a small git repository of one commit:
  - **A, the queue's code as landed after Review 88** (T7b part 1): the schema, the card's form, discovery, custody, the
    record check and the sandboxed rerun, their six test files, `queue/SEAT_CODES.json`, the queue's README and the card's
    template;
  - **B, the known failures and the record's mends:**
    - T10's list, its checker, its test, its gate's diff and the practice;
    - the two law-map screens;
    - `docs/LAW_MAP.md`, with the eight rows mended in the window (P-589) and their arcs' FINDINGS;
    - B1957's check of line 65's convention;
    - the harvest gate's diff;
  - **C, the rules and the register:** B2018 whole, `docs/progress/REVIEWS.md`, the role pages, the seats' protocol page,
    `TERMINOLOGY.md`, and `docs/POINT_REGISTER.md` with the list of the 34 rows the window changed.
- **The readers.** Three readers of main's own model family that wrote none of this read one folder each. They could run
  the folder's tests and small probes of their own, and were told that faults might be planted and to report all the same
  way.
- **The plants.** Eight faults were planted in eight files (`verification/plants.json`, SHA-256
  5c5427cd44717178e642c3c97dbacc6081fba468328214490e5e5a813ed33d47, fixed in the audit room before any reader started).

## The plants

| plant | file | the fault | caught by |
|---|---|---|---|
| A1 | `scripts/queue/rerun.py` | `ctypes` taken out of the refused modules, `_ctypes` kept | A (its 1st, by two tests) |
| A2 | `scripts/queue/discover.py` | the ancestor test accepts git's exit 1, "not an ancestor" | A (its 2nd, by a probe) |
| A3 | `tests/test_queue_rerun.py` | the helper `_returned` joins its two conditions by `or`, so a test passes on the wrong reason | **missed** |
| B1 | `scripts/queue/baseline.py` | the history check reports growth only when the count grows, so a swap passes | B (its 1st, by a probe) |
| B2 | `docs/LAW_MAP.md`, row 296 | the mend says B1658 § 3 "computes" the running it says is "assumed, not computed" | **missed** |
| B3 | `scripts/review/law_map_dated_notes_screen.py` | "Corrected" taken out of the note pattern, the docstring still naming it | B (its 3rd) |
| C1 | `docs/roles/BANKING.md`, K1 | blind only until the expectation is committed, not until the verdict is sealed | C (its 1st) |
| C2 | `docs/POINT_REGISTER.md`, P-092 | the row it waits on named P-482 for P-428 | C (its 2nd) |

**Six of eight caught.** No clean part was reported as planted.
- **B2 is R87-4's case.** A one-word flip in a dated mend was missed although its reader had the arc the note cites, as R87-4
  asks, and quoted the mended bracket. R87-4 is met as asked, and it is not enough: a mend is read clause by clause beside
  the arc's sentence (R89-4).
- **A3 is the same shape in a test's helper.** Its reader ran the file that holds it.

## The readers' own findings, checked by main on the live tree

| # | reader | finding | main's check | disposition |
|---|---|---|---|---|
| 1 | A (its 3rd) | `rerun.py` runs scripts with `python -E`, which ignores `PYTHONHASHSEED`, so the pinned seed does nothing | holds: under `-E`, `hash('abc')` differs on each of three runs; without it, it is the same | to the builder (M74, R89-1) |
| 2 | B (its 2nd) | the stale screen's correction-marker pattern `MARK` is defined and never used, the narrower `TM` read instead; an arc with no verdict file is skipped | holds (lines 16, 28, 37) | mended: `MARK` read, every arc folder screened |
| 3 | B (its 3rd, second part) | the dated-notes screen counts a row as showing a note on any date or session tag in it | holds (line 20) | mended: the note's own date or its kind's word |
| 4 | B (its 4th) | `baseline.py` line 18 says the list "ships EMPTY"; it holds seven entries | holds | to the builder (M74) |
| 5 | B (its 5th) | row 296's mend gives the running clause and not that the factor 4 is exact in t + 1/t, in t only to first order | holds against B1658 line 10 | mended |
| 6 | B (its 1st, beyond the plant) | `tests/test_known_failures.py` tests growth by count only, so a guard that compared lengths would pass | holds | to the builder (M74) |
| 7 | A (its 2nd, beyond the plant) | discovery's ancestor rule is tested only with `"0" * 40`, a git error, never a commit that exists and is not an ancestor | holds | to the builder (M74) |
| 8 | C (its 3rd) | P-876's escalation restated the row's first list of parts; the agy seats' parts are closed (rows 1966, 1967), and 220 rows name no file, not 219 | holds | mended by a dated correction |
| 9 | C (its 5th) | P-334's escalation gave its notes to card C22; the row gives them to C20 | holds | mended by a dated correction |
| 10 | C (its 4th) | P-326's decline says the notes' part is restated in the row and does not say where | holds as unclear, not false: the point's own clause restates it | clarified |
| 11 | C (its 6th) | B2018 says "eight faults were planted in seven files"; its list names nine (A2 in two) | holds | mended by a dated correction |

Not a fault: reader C's 7th, that B2018's B15 probe did not use the command its table names. `probe_live.py` line 85 makes
that command, beside the sage import.

**Main's own, found while checking.** Two tests of the point-debt gate had been failing on main since the day's register
work: `test_a_stale_queued_point_fails_and_escalation_clears_it` and `test_the_brainstorm_rules_fire_on_planted_copies`.
- **The cause:** each read the live register at a fixed date and needed a row there to be stale, or an undeclined draft.
  Once the register was kept, none was left. The test failed for the register being current, not for the gate.
- **Unseen:** no landing ran that file, and it is not on the known-failures list.
- **Mended:** both tests now make their own case, a date after the register's latest, and a planted draft citation. Seven
  of seven pass.
- **The landing now runs the file** whenever a landing touches the register, its gate or the test (R89-3, met).

## What the mended screens find

Run again, the two screens name 51 law-map rows that the day's judged pass (P-589) did not read, outside the trial's arcs,
and 6 inside them. They are owed, to be judged at source as the first pass was (R89-2).

## The fresh clone

P-869's Q1 asked for the full suite on a clean clone of a head that carries the mends, at this review's opening. It was started
on 47ece044b at the opening (`review_tools.py --fresh-clone-suite`), and was still running at this entry; its result is
entered in P-869 when it ends.

## The loop

- **Met:** R87-4 (as asked, and not enough: R89-4) and R89-3.
- **Carried:** R88-2, to Review 90, for the reason above; R87-3, R87-6 and R87-7.
- **Moved whole to register row P-881 at their third carry:** R86-1 to R86-4, as R85-2 to R85-5 were at Review 88.
- **New:** R89-1 (the builder's four), R89-2 (the 51 rows), R89-3 (met) and R89-4 (mends read clause by clause).
