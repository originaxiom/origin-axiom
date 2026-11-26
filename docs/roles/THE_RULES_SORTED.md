# WORKING_RULES.md sorted for the framework (draft by main, 2026-11-26; P-885, draft 1 § 7)

Every rule in WORKING_RULES.md, put in one of five places:
- **door rule:** binds every role;
- **the author's rule:** binds every role because the author ruled it, though no check enforces it yet. A check is owed for
  each one;
- **one role's rule:** binds that role only;
- **advice:** nobody checks it, so a seat may ignore it;
- **retired:** replaced by the framework, or out of date.

The test for "rule" (§ 7): the framework checks it, by the intake, a gate or a plant. A rule with no check is advice, except
where the author ruled it; those are listed apart so they are neither dropped nor called checked. The advisor seat reads
this page cold; the charters under `docs/roles/` are built from it.

## Door rules (every role; each with its check)

| id | the rule | where in WORKING_RULES | its check |
|---|---|---|---|
| D1 | A result that is to bear on the record arrives as a claim card in the intake's form. The claim states its scope (frame, object, reach, hypotheses), and the card declares every identification it makes | the claim cards rule (2026-11-24) 1; one statement of the foundations 3; the identification rule 2 | the intake's form check; `verdict_schema`; `identification_register` (completeness only) |
| D2 | Custody: the card, its expectation and its failing control are committed on the seat's own branch and first seen by the intake before the decisive output. A rewritten branch returns the card | numbered 3 (hash first); sender-branch dual-homing | the intake's sighting log |
| D3 | The card names a failing control as a command, and that control must fail | numbered 8 (vacuity); § Enforcement (a two-outcome criterion) | the intake reruns it |
| D4 | The firewall. No Standard Model quantity enters CLAIMS.md. No comparison with data, a seat's sealed bundle included, without the author's explicit approval. Phenomenological vocabulary is bound by Gate 5-Q | numbered 5, 6, 6a | `firewall_oneway`, `claims`, `framing`; the intake's firewall check |
| D5 | Attribution and privacy: no product, vendor or model names and no sandbox paths in tracked files; seats are named by their codes | numbered 11 | `attribution`; the claim-names gate when R82-2 lands |
| D6 | Nothing is built on a card that is not VERIFIED. A card whose premise is an unverified card names it, and waits for it | a count says where it came from 3 | `seat_positive_verified`; the queue's premise check (owed in the thin path) |
| D7 | A NEGATIVE card stays PROVISIONAL until a second computation banks it, and carries "What the wall teaches" | a negative is banked only after a second computation 1, 5 | `negative_second_computation` |
| D8 | No seat verifies or banks its own card | the seats' pages 5 | the queue's assignment by seat code |

## The author's rules (every role; no check yet, a check owed for each)

| id | the rule | where | the check owed |
|---|---|---|---|
| A1 | One channel: no seat puts a question to the author. A seat's question for him goes to main, marked so | one channel to the owner 4, 5 | a plant in the calibration set; a gate on status files for questions addressed to the author |
| A2 | The author's words are private: a ruling he gives a seat is entered in plain words, dated, and never quoted, in no page, status file or commit message | one channel to the owner 6, as amended (P-796) | a gate for quotation of the author in tracked files (none exists) |
| A3 | No sealed look, and no comparison with data, without his explicit approval, given for that look | D4 covers CLAIMS.md only; the rest is the author's ruling of 2026-11-25 | the intake's firewall check extended to cards (thin path) |

## One role's rules

| role | rules | where | check |
|---|---|---|---|
| banking seat | own code sharing nothing with the producer's; expectations committed before the run | numbered 2; the claim cards rule 3 | custody; plants |
| banking seat | a citation alone supports nothing a verdict rests on: what decides is recomputed or named as a hypothesis | verify load-bearing mathematics 1, 2 | plants (a card resting on a wrong published lemma) |
| banking seat | a failure to fit a family of forms is "not within these forms", never "not Y"; Y is computed from its own definition | a negative … second computation 2 | plants (the B1918 shape) |
| banking seat | an identification needs its map, and the map must act faithfully | the identification rule | plants (the B1223 shape: direct, not semidirect) |
| banking seat | a selection needs a criterion that can fail; the computation is rerun with each declaration changed | before a selection or a hand 2, 3; a count says where it came from 2 | `selection_family`; plants |
| banking seat | controls are two-sided; the instrument is checked before its verdict; a statistic carries its resolution | verify the verifier (E52) | plants (the B8152 shape: a one-sided control) |
| banking seat | labels with their scope and evidence (FORCED, ADMITTED, CHOSEN, FITTED; EXCLUDED is not NOT FOUND); a family is a claim | frame cards 4; a family is a claim | plants (an overreaching scope) |
| supervisor (main) | zero file moves; bank completely (logs, law-map rows, terminology); registration over preservation; the certification envelope; the slow lane quiescent; gates before every landing; the harvest pin | numbered 9, 10; § Enforcement; § CE; the currency notes | `append_only`, `log_changelog_paired`, `law_map_provenance`, `harvest_debt`, `relay_debt`, `views_fresh`; the landing tool |
| supervisor (main) | the brainstorm rules M1 to M7; every document living, record or generated; GENESIS IDs, never the old letters bare | the brainstorm rules; frame cards 5; one statement of the foundations 1, 2 | `point_debt`, `carry_age`, `doc_facts`, `doc_currency`, `genesis_cited` |
| supervisor (main) | a design naming real-world facts gets a factual review between seal and run | numbered 13 | manual: it arises only with a look, which needs the author's approval (A3) |
| builder | a lock asserts the mathematics, not a transcript; every gate has a planted failing case; gates fail closed | numbered 7, 8; § Enforcement | `test_vacuity`, `gate_controls` |

## Advice (any seat may ignore it)

- Read the grounding pages before an important probe (§ 0: COMPUTE_THE_PROGRAM, THE_LADDER, THE_FRAMEWORK, THE_CAMPAIGN).
- "We lack X" is a hypothesis: search before saying it. The intake's record check now does the repository half for every
  card, with search terms of its own; the literature half is the seat's.
- State the quantifier in one sentence before computing (P0).
- Sync before computing.
- When stuck, use the instruments (the atlas, the failure atlas, the views, the error ledger) before the archive.
- Type before you identify.
- Before a frame: its card. Chain backwards from the comparison. Read a source on the bench before believing it.
- A count carries its decomposition; a frame's count says whether it can carry the hand.
- Weave or thread: say which.
- Name the wall from the ledger of walls before attacking a question of a known shape.
- Report faithfully: do not celebrate negatives, and do not soften positives.
- Keep a status file and run the listener (the seats' pages, points 2 and 3).

## Retired or replaced

- **A work card before each piece of work, approved by main** (the seats' pages, 4): replaced. Production is free; the
  claim card at the door is the only card.
- **Four named seats verify** (the seats' pages, 6): replaced by the roles (peer, banking seat, auditor).
- **Tiers A, B, C and one intake a day by `seat_intake.py`** (the claim cards rule, 2, 4): replaced by the intake runner,
  which computes whether a card decides something; only deciding cards go to banking.
- **"Main reproduces; main's own code decides"** (the claim cards rule, 3): replaced by REPRODUCED at intake and VERIFIED by
  two banking seats; main's own cards pass the same door.
- **`git push codeberg main`** (numbered 11): out of date; the mirror is `git push backup main`.
- **The currency banner at the top of WORKING_RULES.md** (2026-08-25): a record of that date, not a rule.

## What this sort asks of the build

- Each banking rule names the plant that tests it, so the plant ledger should hold at least one plant of each shape over the
  rounds. The four plants of the trial are drawn from these shapes; which four is sealed.
- A1 to A3 each need a check. Until one exists, each stays a rule only because the author ruled it, and the auditor's first
  sample should include it.
- WORKING_RULES.md itself becomes a pointer to the role pages once the charters land, keeping its history as a record.
