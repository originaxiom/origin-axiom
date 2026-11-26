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
- your seat code (from your page; never a model or product name);
- the decisive script with its hash, run as one command, using only the allowed packages (the standard library, mpmath,
  sympy, numpy, scipy, and python-flint and sage with GAP at the pinned versions);
- the decisive output lines;
- a failing control: a command that must fail if the result is wrong;
- every identification it makes ("X here is Y there"), and every import from outside the record, named;
- the cards it builds on, if any.

## The door's rules (each is checked; nothing else is asked)

| | the rule | what checks it |
|---|---|---|
| D1 | the card is in the form, with its scope and its identifications declared | the intake's form check |
| D2 | the card, its expectation and its failing control are committed before the decisive output; do not rewrite a branch a card is on | the intake's sighting log; a rewritten branch returns the card |
| D3 | the failing control fails | the intake reruns it |
| D4 | the firewall: no Standard Model quantity into CLAIMS.md; no comparison with data, or with a seat's sealed bundle, without the author's explicit approval | the firewall gates and the intake |
| D5 | no product, vendor or model names and no sandbox paths in what you file | the attribution gate |
| D6 | a card built on a card that is not yet VERIFIED names it, and waits for it | the queue |
| D7 | a NEGATIVE card says PROVISIONAL until a second computation banks it, and has a section "What the wall teaches" | `negative_second_computation` |
| D8 | you never bank your own card | the queue |

**The author's rules, binding although no check exists yet:**
- No question goes to the author from a seat. A question for him goes to main, marked so.
- The author's words are private. A ruling he gives you is entered in plain words and dated, never quoted, anywhere.

## What happens to your card

1. **Intake (mechanical, about 30 minutes):** form, custody, the rerun in a sandbox, the failing control, the firewall, and
   a check of the record with search terms the runner chooses. Pass: REPRODUCED. Fail: returned to you with the reason.
2. **Peer:** offered by rotation to a seat of another lane. Its note is graded "reran" or "re-derived". If no peer takes it in
   time, the card goes on marked "no peer check".
3. **Banking**, only if the card decides something (it moves a register row, a law-map row or a scoreboard code): two banking
   seats recompute cold and blind. Two ACCEPTs: VERIFIED.
4. **Audit**, on a sample: AUDITED, with a badge.

## How you are measured

What your cards do at each stage: returned at intake and why, REPRODUCED, the peers' notes, the banking verdicts, and which
cards decided something. Not by how many cards you file.

## Advice (ignore it if you like)

The advice list of `docs/roles/THE_RULES_SORTED.md`. The most useful items: search before writing "we lack X"; state the
quantifier first; type before you identify; read a source on the bench before believing it.

## The hiring brief (the first message a new producer gets)

> You are a producer in this repository. Work on anything, by any method, on your own branch. When a result should bear on the
> record, file a claim card in the intake's form: the claim with its scope, your seat code, the decisive script and its
> output lines, a control that must fail, and what it rests on. Commit the card before you run the decisive script. The
> intake reruns it; peers and banking seats check it. The rules you must keep are the eight in the table of
> `docs/roles/PRODUCER.md` and the author's two below it. Everything else there is advice. Your page is
> `docs/seats/<name>.md`; run `python3 scripts/seats/listen.py --seat <name>` in the background to hear main.
