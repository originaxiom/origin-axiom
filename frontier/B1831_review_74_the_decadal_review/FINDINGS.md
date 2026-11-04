# B1831 — REVIEW 74, THE DECADAL REVIEW (a process arc; 2026-11-04, S299): THE BACKLOG READ FOR LEADS, THE CANDIDATE'S CONFIRMATION ONE TARGET SHORT, THE CARRY RULE MADE TO FIRE

**Verdict: PROVED,** as a process arc: the review's checks ran, and every correction it applied was verified by main at its
source first. The entry is `docs/progress/REVIEWS.md`, Review 74. Nothing here is compared with data. cc (main).

## What it did

- **At the owner's word ("do the decadal"), and their mid-review ask** that relays and old rows handed to the review be taken
  seriously because "they could contain game changing leads": every open relay (84), every SCHEDULED harvest row (276),
  every [LEAD] row of the register (142) and every other open lead of OPEN_LEADS (77) was read in full, for load on main and
  for leads nobody followed — by readers who report only; main verified what it applied.
- **The loop:** the carry rule could not fire (E84); fixed in `scripts/review/review_tools.py` with a planted control;
  R73-1–R73-3 declined at their true third carry; the rest resolved or carried.
- **The tools:** the fresh-clone suite became a tool step (R73-7); the seal check reads staged tables, an arc root and a
  rename; the provenance scan has the gate's negation window (E52); the harvest gate checks the pin against its rows (P-541).
- **The seats** moved after S298 and were harvested under P-585's firewall (rows 1544–1547). Main re-ran the web seat's
  strong-angle check on its own tree and ruled θ̄ off P-585's held-out list; the candidate's confirmation is one held-out
  target short (P-597).
- **Corrections verified and applied:** the seeded sample's (B1821, B1822, B1823, B1824, B1828); B1809:129; main's own
  S298 claims without an instrument (σ_b, the LL pair; instruments now in B1826 `verification/review74/`); the H = I scope
  on thirteen FR-FIB arcs and eleven law-map rows (P-594); the exact-end failure attributed to the web seat's sealed look
  (P-595); P-535's seal-order cases; B1425's retraction count (S298's, unseen by its partial suite).
- **Decided:** P-592 (six packages declined for admission); P-563 and P-565 adopted as practices; 79 relays closed with
  evidence; 27 register rows (P-594–P-620).

## Verification (this folder)

- `readers/` — the readers' reports, local paths scrubbed: the relay halves, the three SCHEDULED readings, the two lead
  readings, the seeded sample, the firewalled harvest (its sealed part is not here and was not opened by main), P-535, P-592,
  P-086.
- `apply/` — the scripts that made every edit, kept as the record (not to be re-run) and `relay_table.json`.
- `theta_rule_check_rerun_on_main_out.txt` — the web seat's script on main's tree, one worker (its Pool(2) set to Pool(1)).
- `b1809_null_m2.py` and its output — main's check of B1809:129 with B1821's evaluator.
- `fresh_clone_suite_summary.txt`, `fresh_clone_suite_failures.txt` — the full suite in a fresh clone of eb130f01f.
- `test_b1831_review_74.py` — the lock.

## Seen first

- `VERDICT topic-sweep /decadal review|carry.age|carried (item|items) age|SCHEDULED (rows|backlog|sweep)|backlog read|leads? read at/
  (full text): 24 of 1577 arcs on main match (NEGATIVE 4, PROVED 20); 15 register rows match (DONE 9, QUEUED 6)` — the reviews'
  own arcs (B1448 the instruments, B1461 the review fires and carried items age, B1464 the rule binding first, B1488, B1608
  and the later reviews), and **B1337, the SCHEDULED sweep**: 156 of the 277 rows readable on main at the time, the other
  121 on branches then absent; this review read all 276 in full, the retired seats' through their archive tags. The
  carry-age rule (B1461) was built to count keys before the colon; the re-keying convention that defeated it is recorded
  from Review 62 on (the review's mechanics) and was never set against the counter. P-086 is the owner's standing checklist
  this review ran in part ((b)–(d)).
- **Literature (pointers):** none bears on the mathematics; the loop's practices (carried items that age by lineage, a
  backlog triaged by load and by unfollowed idea) follow ordinary issue-tracker and audit practice — an analogy for the
  shape, not a source.

## Disclosed

- The SCHEDULED rows and the leads were read by readers; their proposed closures are listed for main to confirm one by one
  (P-616, P-617) and none was applied on a reader's word, except where main checked the pointer (L251, P-020).
- The relay closures rest on the readers' evidence; main checked that every cited harvest row exists and names the seat
  item, every cited register row's state, and read the load-bearing ones at source.
- W183's cells were verified by a reader against the seat's committed JSON, not re-run on main.
- The fresh-clone suite ran at the window's last landing; four of its seven failures are date-driven and closed here.
