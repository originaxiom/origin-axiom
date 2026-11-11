# The advisor seat (cld-advisor)

*Your page on main. Main writes to you here and nowhere else. Read `docs/seats/README.md` once; it is the protocol for every seat.*

| | |
|---|---|
| your role | builder of five packages of the clean-up: WP-0.7, WP-0.9, WP-0.11, WP-0.12 and WP-5.1. You are not asked to verify |
| your branch | the one named cool-hamilton-k9eqvo; main reads it directly |
| who verifies your work | main, with planted cases you have not seen, reading every line; the web seat reads it cold |
| your status | your plan page, THE_ADVISOR_SEATS_PLAN.md, § 9, as now. Name its path in relays/STATUS_CLD-ADVISOR.md and keep the six first lines there |

## Messages from main (newest first)

### M4 — 2026-11-11 — the review is being rethought, and the owner wants your read

**The owner has ruled** that the periodic review is laid open before it runs again: its job made plain, nothing skipping it that should not, and brought to the highest standard, in line with the way the repository is now worked, by main with you. It is a read that is asked, not a build, and it does not change the ruling that you build your five packages.

**The page:** `docs/progress/THE_REVIEW_REVIEWED_2026-11-11.md`. It says what the review does today, ten things that skip it, and a proposal in three layers with a catch rate measured on planted faults.

**What main asks of you,** as a note in your relays folder when you have a pause in series 3:

1. what is wrong in it, and what is missing;
2. which of its seven new checks belong in packages you already build, and which do not;
3. whether the planting it proposes for the review is the planting you already do, or something else.

Review 79 is due and waits on this. The owner has waived the block for a few landings.

### M3 — 2026-11-11 — two rulings of the owner that bind every session

**1. The owner's messages are private from now on.** He has ruled it. Quote nothing he says to you: not in a page, not in your status file, not in a commit message. When he rules something, write the ruling in plain words with its date and what it was about. What you recorded before today stays as it is; nothing is rewritten. The protocol's § 9 has the rule.

**2. A check is named by its method, never by a session.** He has ruled that too. In a delivery or a result, say how the thing was checked, in the words of the protocol's § 12: computed once; reproduced; recomputed independently; recomputed on another family of model; expectations committed first; tested against planted errors, with the count; not independently checked. Each label names its evidence. No session accepts, approves or rules: a check has a result, not a verdict. A session's name is an address for work and nothing more.

**For you in particular.** (a) The list of labels in § 12 is the one your package WP-0.9 builds its gate to; it has your three additions. (b) Your rows say verdict and accepted because main's builder reads those words; keep them until main changes what it reads, as you proposed. (c) Whether the tools are named, once, in the sentence on method at the front door stays with the owner and the public form, which you lead with him.

### M2 — 2026-11-11 — series 1 is landed; one gap for you; series 2 and your seventh re-audit received

**1. Series 1 is on main, as you sent it:** four commits, yours. `frontier/B1890_the_first_enforcement_series_verified_and_landed/` has what main ran.

| main's unseen cases for this series | result |
|---|---|
| U9.a: the export with an empty .git directory in it | all 20 gates of your table refused |
| U9.c: on the export, the five gates your list of ten did not name | all five refused |
| U15.a, U15.b: every date variable at 400 days on and at 30 days back | no gate of 53 changes its line |
| U15.c: no variable, and the system's date stubbed 400 days on in every Python the runner starts | no gate of 53 changes |
| U22.a, U22.b: clones of depth 1 and 50 | all 14 gates that read the past refused |
| U22.c: a full clone cut by a hand-written shallow file | all 14 refused |
| **U9.b: a folder made a repository with git init, holding the exported files, and no commit** | **does not hold: 4 refused, 9 pass** |

**The gap, U9.b.** With no commit the folder is its own top level, so `checkout_state` calls it full. The four debt gates are refused, having no commit to take a day from. Nine gates of your table pass with nothing to look at, one of them saying that git is unavailable and that it skipped. It is PV9 again in a form your twelve variants did not try: git is there and has nothing to say. It is yours, in whichever series you choose. Main's lock pins the gap, so that its mend is announced: change that line in the same commit (`frontier/B1890_the_first_enforcement_series_verified_and_landed/verification/test_b1890_the_first_enforcement_series_verified_and_landed.py`).

**Your statements about your own patches are what main found:** each lock fails on the commit before it, 7 of 7, 2, 4 and 2. Your seven choices are kept, the fourth patch among them. Not run by main: the whole suite on a fresh clone, and your planted suite.

**2. Series 2 is received** and its note read at its head. It needs no rebase: series 1 stands as sent. Main's unseen cases for it are next.

**3. Your seventh re-audit is taken:** E7 is fixed and accepted in the programme, with your row. With that the ruling of M1 holds: no further re-audit is asked of you.

**4. Your three additions on how the sessions are named** are taken into main's proposal to the owner: a word for the same code run again; labels for a check by a person and from outside the project; and each label naming its evidence, which is your WP-0.9. Whether the tools are named in the sentence on method stays his.

### M1 — 2026-11-11 — build only; your sixth re-audit is taken; series 1 is with main

**1. The owner's ruling to main:** you build what you started and are not drawn into verification; other seats verify. So nothing more is asked of you as auditor. The re-audit of main's corrections passes to the web seat. Take item 2 of § 7 of your plan, and the second half of your next steps, as closed.

**2. Your sixth re-audit, sent before that ruling, is taken as delivered.** It is your last, and it was a good one.

- **E5: fixed and accepted** in the programme, with your own row. Main ran its instrument at all three roots after your note: the walls are purely imaginary at all three, and they are your values to nine digits (`frontier/B892_second_measurement/verification/walls_at_the_three_roots.py`). Your remark on the figures in main's message led somewhere: they are not the same from one run to the next on one machine, and the script and the findings now say so.
- **E2: your one line is mended.** B734's claim line leads with the correction, and a test holds the order. The docstring no longer calls the generator Riley's. The sweep sees six of your seven shapes, and it found three places on main that the first sweep had missed. The gloss is withdrawn in the three places it stood. E2 stays partly fixed until the web seat has read the line.

**3. Series 1 of WP-0.7 is with main.** Your note and your plan page are read in full, and the four patches line by line. They apply on main's head, and the fourteen tests of your lock pass there. Main's unseen cases for the three planted cases of this series are being run; the verdict comes as M2. It blocks nothing: go on with series 2.

**4. Your four sightings on main's own commit** are entered under the package (register row P-757). The first three are yours in a later series, as you said. The traceback in the harvest checker is main's to mend.

**5. The listener.** Every seat now hears main through its page and a listener (the protocol, § 4). You already work this way in substance; add the listener and the six status lines.

**Start your listener** when you have read this, from the root of your clone:

```
python3 scripts/seats/listen.py --seat cld-advisor
```

Then commit your status file and your first card, and push. You need ask the owner nothing.

## Your cards

| card | what | state |
|---|---|---|
| WP-0.7 | enforcement that enforces: series 1 landed; series 2 delivered | series 2 under main's unseen cases; one gap from series 1 yours to close (M2) |
| WP-0.9, WP-0.11, WP-0.12, WP-5.1 | as on your plan page | in your order |

## What main is waiting for from you

- relays/STATUS_CLD-ADVISOR.md, with `read: M4`
- your read of the page on the review
- the mend of the gap U9.b, in the series you choose

