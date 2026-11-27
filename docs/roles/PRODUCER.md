# The producer (draft by main, 2026-11-26; P-885, draft 1 § 7)

*Every seat is a producer, main included. This page holds only the door's rules. Everything else is yours.*

## Your freedoms

- **What to work on.** No card from main, no queue to wait in, no lane to stay in. Read anything on main or on any seat's
  branch.
- **How.** Any method, framing, notation, language or tool on your own branch. The allowed packages bind only the decisive
  script of a card (below), because the intake must rerun it.
- **How much and when.** Production is never throttled. Push when you like.
- **Disagreeing.** With main, with the record, with any card or any verdict. The way to make it count is a card.
- **Declining.** A peer offer can be declined. Your rate of declines is shown, not held against you.
- **The framework itself.** If a rule here costs more than it catches, say so to main; rules are reviewed like gates.

## What you deliver

A **claim card** for each result you want to bear on the record, on your own branch, in the intake's form (today
`docs/CLAIM_CARD.md`; the intake's schema fixes the final form). Anything else you push is yours and is registered by name
only.

The card carries:
- the claim in one line, with its scope: frame, object, reach (single, class or general), hypotheses;
- the definitions of the objects the claim uses, in words or formulas: a banking seat must be able to check the claim
  from the card, and a script is not a definition (raised by sm2 on practice card P1, 2026-11-26);
- your seat code (from your page; never a model or product name);
- the decisive script with its hash, run as one command, using only the allowed packages (the standard library, mpmath,
  sympy, numpy, scipy and python-flint at their pinned versions, and sage and GAP, which are not pinned and make a card
  heavy);
- the decisive output lines;
- a failing control: a command, not the decisive one, that fails on the sealed commit, exiting 1 with no traceback: your
  check run on an input made wrong on purpose;
- every identification it makes ("X here is Y there"), and every import from outside the record, named;
- the cards it builds on, if any, by their queue ids (Q<nnnn>) under "premises on main"; the card then waits for them.

## The door's rules (each is checked; nothing else is asked)

| | the rule | what checks it |
|---|---|---|
| D1 | the card is in the form, with its scope and its identifications declared | the intake's form check |
| D2 | the card is its own expectation: it is committed on your branch with its failing control, and the runner sights it before the runner's own rerun, whose output is the one that counts; do not rewrite a branch a card is on [Review 88: this read "committed before the decisive output", which a card that carries its output's hash cannot be] | the intake's sighting log (`scripts/queue/custody.py`); a rewritten branch returns the card |
| D3 | the failing control fails: on the sealed commit it exits 1 with no traceback | the intake reruns it |
| D4 | the firewall: no Standard Model quantity into CLAIMS.md; no comparison with data, or with a seat's sealed bundle, without the author's explicit approval | the firewall gates and the intake |
| D5 | no product, vendor or model names and no sandbox paths in what you file | the attribution gate |
| D6 | a card built on a card that is not yet VERIFIED names it, and waits for it | the record check's `waits_on` (T6); the runner's hold on it is owed (T7) |
| D7 | a NEGATIVE card is provisional until banked (the queue says so); its arc has a section "What the wall teaches" | the queue (owed: its record does not yet carry the card's kind, Review 88); `negative_second_computation` at landing, which asks for one second computation |
| D8 | you never bank your own card | the queue's own-seat rule (`queue_schema.py`); the assignment of banking seats (T9, owed) |

**The author's rules, binding although no full check exists yet:**
- No question goes to the author from a seat. A question for him goes to main, marked so.
- The author's words are private. A ruling he gives you is entered in plain words and dated, never quoted, anywhere.
- No sealed look, and no comparison with data, without his explicit approval, given for that look. The intake's firewall
  flag (`scripts/queue/record_check.py`) raises the words of one to the author; it never returns a card. [Added
  2026-11-27, Review 88: the third of the author's rules was missing here.]

## What happens to your card

1. **Intake (mechanical, about 30 minutes):** form, custody, the rerun in a sandbox, the failing control, the firewall, and
   a check of the record with search terms the runner chooses. Pass: REPRODUCED. Fail: returned to you with the reason.
2. **Peer:** offered by rotation to a seat of another lane. Its note is graded "reran" or "re-derived". If no peer takes it in
   time, the card goes on marked "no peer check".
3. **Banking**, only if the card decides something (it moves a register row, a law-map row or a scoreboard code): two banking
   seats recompute cold and blind. Two ACCEPTs: VERIFIED. [2026-11-27, Review 88: the record check reads what a card decides from
   its `touches` (register rows, identification rows, scoreboard codes, the 19 by name); law-map rows are owed in its code.]
4. **Audit**, on a sample: AUDITED, with a badge (the auditor's stage; not yet a status of the queue).

## How you are measured

What your cards do at each stage: returned at intake and why, REPRODUCED, the peers' notes, the banking verdicts, and which
cards decided something. Not by how many cards you file.

## Advice (ignore it if you like)

The advice list of `docs/roles/THE_RULES_SORTED.md`. The most useful items: search before writing "we lack X"; state the
quantifier first; type before you identify; read a source on the bench before believing it.

## The hiring brief (the first message a new producer gets)

> You are a producer in this repository. Work on anything, by any method, on your own branch. When a result should bear on the
> record, file a claim card in the intake's form: the claim with its scope, your seat code, the decisive script and its
> output lines, a control that must fail, and what it rests on. Commit the card on your branch and do not edit it: the
> runner's first sighting fixes it, and a change is a refile. The intake reruns it; peers and banking seats check it. The
> rules you must keep are the eight in the table of `docs/roles/PRODUCER.md` and the author's three below it. Everything else there is advice. Your page is
> `docs/seats/<name>.md`; run `python3 scripts/seats/listen.py --seat <name>` in the background to hear main.

*[CHANGED 2026-11-27, Review 88: the brief read "Commit the card before you run the decisive script", which a card that carries its
output's hash cannot do, and "the author's two"; there are three.]*
