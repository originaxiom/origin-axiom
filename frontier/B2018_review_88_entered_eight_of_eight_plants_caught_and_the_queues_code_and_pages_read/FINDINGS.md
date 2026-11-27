# B2018 — Review 88 entered: three cold readers of the window's process work caught all eight plants and found real faults in the queue's code and the role pages; each checked by main on the live tree; the pages mended, the code sent to the builder; the trial's arcs left to the trial

**Verdict: PROVED (a process arc).** Main, 2026-11-27. Register rows P-881 and P-885. **0 of 19.**

## Seen first

- **Swept:** `VERDICT topic-sweep /Review 88|claim card queue|intake runner|sandbox(ed)? rerun|symlink|export-subst/: 0 of 1758 arcs on main match (none); 25 register rows match (QUEUED 25)`.
  The rows are P-885's backlog behind the framework. This arc follows Review 87's method (B2013).
- **The literature:** none applies; this is a review of the record's own window.

## Why now, and what was read

- **When it opened: in time.** The gates printed "review-due: 27" at the fresh-clone landing and "28" at the next; the
  review opened at the 28th landing since Review 87's anchor 36f9cc5c2, before the 34th that R84-4, R85-1 and R87-1 ask.
  R87-1 is met.
- **The window:** 36f9cc5c2 to 64cc951b3, the anchor of this entry. It holds 28 commits and 5 arcs with a verdict, B2013 to
  B2017 (`scripts/review/review_tools.py`).
- **The sample, and why it is not the five arcs.**
  - The tool, seeded by the anchor, drew all five: B2013 to B2017.
  - All five are among main's seven trial cards, B2011 to B2017, which the framework's trial gives to two blind banking
    seats, with natural plants held sealed (sealed, SHA-256 07bca6c8cfeaa75c173153f47813b8786327250ef7b0500a857aba393ba59ad9,
    on main since 2026-11-26). A review's reading now would mend those arcs before the trial and spoil it.
  - So their reading is the trial itself, two blind banking seats with plants, which is what a review does. If the trial
    has not run by Review 89, these arcs go to Review 89's readers (R88-2).
  - **Read instead: the window's process work,** which no reader had read and which the trial depends on: the queue's code,
    the builder's thin path T1 to T6 and T1b as landed (`scripts/queue/`, 1,254 lines, and its six test files), the card's
    template (`docs/CLAIM_CARD.md`), the three role pages (`docs/roles/`), the seats' protocol page
    (`docs/seats/README.md`), and the day's change to the harvest gate.
- **The reading copy and the readers.**
  - The copy was a git archive of 64cc951b3, cut into three folders, each a small git repository of one commit:
    - A, the door: the queue's schema, the card's form check, discovery, their tests, the template and the producer's page;
    - B, the middle: custody and the sighting log, the sandboxed rerun, the record check, their tests and the template;
    - C, the rules: the role pages, the protocol page and the template against clean copies of all the queue's code, and
      the gate change as a diff.
  - [CORRECTED 2026-11-27, Review 89 (a cold reader's finding, checked by main): in nine files, not seven; A2 sits in two,
    `card_form.py` and the template, as the table below says.] Eight faults were planted in seven files (`verification/plants.txt`, sha256
    440211cdfc9192435a6665c482d4e2ecf74bdd872e6150c1b2d94b68f3d9f54c, fixed in the audit room before any reader started).
    The gate change, the protocol page, the queue's README and, in A, the producer's page were left clean as controls.
  - Three readers of main's own model family that wrote none of this read one folder each, could run the folder's tests and
    small probes of their own, and were told that faults might be planted and to report all the same way.
  - Each reader was told which tests fail in its folder only because the folder lacks the rest of the repository.

## The plants

| plant | file | the fault | caught by |
|---|---|---|---|
| A1 | `queue_schema.py` | the card's path widened to `relays/claims/CLAIM_.+\.md`, which admits a slash and ".." | A (its 5th) |
| A2 | `card_form.py` and the template | `requests`, a network package, added to the allowed packages | A (its 1st) |
| A3 | `test_card_form.py` | the planted-rule loop asserts `not bad or ...`: a lock that cannot fail | A (its 2nd) |
| B1 | `rerun.py` | the normalisation at 8 significant digits, the docstring still saying 12 | B (its 1st) |
| B2 | `custody.py` | the sighting compared with the card's latest move, not its filing | B (its 2nd) |
| B3 | `record_check.py` | "sealed look" dropped from the firewall's words (a test catches it) | B (its 3rd) |
| C1 | `BANKING.md` | VERIFIED on one ACCEPT and no REFUSE | C (its 1st) |
| C2 | `THE_RULES_SORTED.md` | custody "within a day of the decisive output" | C (its 2nd) |

**Eight of eight caught,** seven by reading and one (B3) by a test. No clean control was reported as planted. The lesson of
R86-5 and R87-4 does not arise here: no plant sat in a dated note.

## The readers' own findings, checked by main on the live tree

Readers A and B read the live code except at the planted lines; reader C read clean code. Main reproduced every serious code
finding on the live tree with probes of its own (`verification/probe_live.py`, its run `probe_run.txt`): each one holds.

**In the code (the builder's; sent as one patch to follow T7b, M64):**

| finding (reader) | main's probe on the live code |
|---|---|
| a decisive script committed as a symlink runs a file outside the commit, while custody hashes the link (B5) | REPRODUCED |
| `git archive` applies the commit's `.gitattributes`, so the text run is not the blob custody hashed (B6) | the checkout prints v = 1, the rerun v = 2, REPRODUCED |
| the failing control's imports are never guarded (B8, C5) | a control importing `socket`: REPRODUCED |
| the static guard admits `_socket` and `exec("import socket")`, among others (B7) | both REPRODUCED |
| no filesystem isolation (B9, C5) | already T7b's (M62) |
| a control that runs past the limit turns a failed rerun into HEAVY (B4, C4) | HEAVY with the hash mismatch in its reasons |
| HEAVY returns before the command and control checks (B15, C6) | HEAVY for `run as python3 x.py; rm -rf y` |
| a card's seat code is its own field, never tied to the branch it is on: a seat can file under main's code (A15) | read in `discover.discover` |
| main, signing "main", may move main's own card (A6, B19, C12) | OFFERED to PEERED by main on main's card: no problem |
| REPRODUCED to AT_BANKING skips the peer offer (A7, B19, C19) | a move of the schema |
| the effect's code is never compared with `touches`, so a card can "remove A03" and not decide (B10, A14) | form holds, deciding false |
| the 19 by their common names are not deciding (B11); the firewall misses plurals and forms (B3's own probes) | "the quark Yukawas": false; "the measured values", "compared to data", "1.2 +/- 0.1": no flag |
| `deciding` = 0 is accepted (A11, B20) | no problem |
| a card file deleted along the queue's history is not reported (B12) | no problem |
| one card at a path the schema refuses stops discovery for every seat (A4, C16) | read in `discover.main` |

The rest are in M64, each with its reader: the script path and command checks (A12), discovery without the gate's vendor
rule (A9), the two read paths of the queue (A10), discovery's notes and silent skips (A8, A18, A19, A24, C25), discovery's
last-segment match, which could take an unpushed `origin/sm/banking` for `origin/sm2/banking` (C21), the log's crash on a bad
entry (B22), the record check's loading order and its six title words (B24, B17), and the locks: custody's late-sighting
plant has a one-entry history (B13), the normalisation test passes at any precision from 2 to 16 (B14), the allowed list is
tied to the template but not to `ALLOWED_PACKAGES.json` (A3), and others (A20, B23).

**Answered, not faults:** the lane survey's `short` is defined above the hunk C was shown (C21); the seat-code check against
the scoreboard cannot fire on any valid code (C24, B21), which is true and harmless, kept as a guard on the form; the
references to "the seats' pages, 4/5/6" in the rules' sort are to WORKING_RULES.md, not to the protocol page (C25).

**On the pages (main's; mended in this entry, each with a dated bracket):**
- the failing control: the template and the producer's page said "must fail if the result is wrong"; the rerun requires it to
  fail on the sealed commit, exiting 1 with no traceback (C3);
- custody: the producer's page and its hiring brief asked the card to be committed before the decisive output, which a card
  carrying its output's hash cannot be; now as custody reads it, the card is its own expectation and is sighted before the
  runner's rerun (C2, A16);
- the premise rule: the card names the Q-ids it builds on under "premises on main", and the record check's `waits_on`
  exists; the rules' sort had called it owed (C8, A17);
- the firewall: the author's third rule was missing from the producer's and banking pages; the rules' sort called its check
  owed while the record check flags it; the protocol page worded it differently (C9, C10, C18);
- D7's and D8's checks named as what exists and what is owed (C11, C12, A17); K3's and the banking row's checks named as T9's
  (C15); `selection_family` and `seat_positive_verified` named as partial (C20);
- the banking page: what a banking seat reads (C14); refusing against returning (C13);
- the protocol page: the retired work card, main's recomputing and the tiers marked as replaced; the status file marked as
  advice; RETURN and VERIFIED worded as the banking page has them (C13, C17);
- the template: discovery named; the seat code's form with its version's point and its efforts; sage and GAP not pinned
  (A22, C23, C25);
- D1's fields, D5's naming of seats (by code on cards and in the queue; a page's name is an address) (C22, C25).
- The day's gate change: the lane survey's pin test now takes the full path too (C21).

## What the review shows

- **Eight of eight plants caught,** three per code folder and two on the pages.
- **Main's verification of T1 to T6 missed what the rules let through.** Main verified each patch line by line and with
  mutations of its own (harvest rows 2022 to 2030: "4 of 4", "3 of 3"). The mutations broke what each patch's tests already
  looked at. Nothing tried what a rule admits that it should not: a symlinked script, the archive's attributes, a slow
  control, a control's own imports, a card under another seat's code, an alias. The readers did, with probes built to pass
  each rule wrongly. Two of the plants (B1, B2) sat in exactly the shape the live tests cannot see (B13, B14).
- **The class is E52, the verifier defect** (`docs/ERROR_LEDGER.md`): the intake runner is the framework's verifier, and its
  faults were found before it ran anything. Its standing rule gains a sentence: a gate or a runner is verified by probing
  what it admits, with inputs made to pass it wrongly, not only by mutating its own tests. The page faults are E13, stale
  artifact text, and E11, an overextended record. **No new error class.**
- **What it means for the trial.** The runner does not land until T7b and this patch's items 1 to 13 are built, verified by
  main with these probes and more of the same kind, and landed (R88-1). Main's seven trial cards are filed on main before the
  runner's first round, so that they precede every seat's card in the queue (discovery reads main first).

0 of 19.
