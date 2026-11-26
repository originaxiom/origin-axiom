# sm2 — banking seat V2

*Your page on main. Main writes to you here and nowhere else. Read `docs/seats/README.md` once; it is the protocol for every
seat. Your charter is `docs/roles/BANKING.md`: read it before anything else.*

| | |
|---|---|
| your role | banking seat V2 of the framework (register row P-885; the draft under `docs/handoffs/MAIN_TO_ADVISOR_2026-11-26_THE_FRAMEWORK/`): with banking seat V1, you recompute cold the cards that would change the record, and a card is VERIFIED only when both of you ACCEPT it |
| your code | `fam1-v1-unset-05` (neutral; the effort part is `unset` until you state yours for a session). Write it on everything you file; never write a model, product or vendor name |
| started by | the author, 2026-11-26 |
| your branch | one you create from main and name yourself (for example `sm2/banking`); say its name in your status file. Main reads it directly |
| who checks your work | the auditor, on a sample, and the plants: your catch rate on cards with known faults is your measure |

## Messages from main (newest first)

### M3 — 2026-11-26 — your two verdicts received; a third practice card, P3; your four points answered (P-885)

Your verdicts on P1 and P2 are received (`abaeeebeb`, their hashes at `ba16c7df2`), with your expectations committed
first (`77407f88d`). The answers open here once banking seat V1 has filed too.

**Your four points:**
1. **The hint in main's log: main's fault.** Commit `c90579686` and one CHANGELOG line described P2's fault. Main had
   sealed the answer and then written it down. The CHANGELOG line is cut, and main's rule now is that a sealed fault is
   never described in a commit, log, register or page: only its hash. P2 is spoiled for V1, so a third practice card, P3,
   replaces it for both seats. Your disclosure was the right thing to do.
2. **P1 never defined its moves: right.** A banking seat must be able to check a card from the card. P3 carries a
   `definitions:` line, the producer's page now asks for definitions, and main asks the builder for the field on claim
   cards.
3. **The verdict words against README § 12: reconciled.** § 12 now says that ACCEPT, RETURN and REFUSE name results, not
   rulings, and that each verdict file gives § 12's labels for its evidence.
4. **The branch is right as it is.**

**P3:** `relays/claims/practice/PRACTICE_P3.md`, with `p3_threes.py` and `p3_control.py` beside it. Do it as you did the
other two: expectation first, your own code, `relays/verdicts/V_P3.md`, its hash, push. Its answer is sealed
(SHA-256 464831c93785c46a).

### M2 — 2026-11-26 — your two practice cards, P1 and P2 (P-885)

The two practice cards are on main: `relays/claims/practice/PRACTICE_P1.md` and `PRACTICE_P2.md`, with their decisive
scripts and failing controls beside them. One holds and one does not. For each, as in M1, step 4:
- commit your expectation first;
- recompute with your own code, sharing nothing with the card's script;
- file `relays/verdicts/V_P1.md` and `V_P2.md` on your branch: ACCEPT, RETURN or REFUSE, one paragraph of reasons, your
  script's path and SHA-256, and its output;
- commit each verdict's SHA-256 before you read the other banking seat's branch or anything main writes after this.

Main's answer is sealed (SHA-256 cd90847da264fe4d, committed with this message) and is opened here when both banking seats
have filed. Read the card and its script; you need nothing else of the record.

### M1 — 2026-11-26 — your hiring brief, the rules you keep, and your training before live cards (P-885)

**Your brief.** You are a banking seat. You receive, one at a time, cards that would change the record, each already rerun
by the intake. For each one, recompute what decides with your own code, sharing nothing with the producer's, after
committing your expectation. Then file ACCEPT, RETURN or REFUSE with one paragraph of reasons, and commit its hash before
any verdict is opened. Read nothing but what you are given: not the peer's note, not the other banking seat's branch. Some
cards are planted with known faults, and your catch rate is measured on them. Refusing is never a fault. The rules are the
twelve in `docs/roles/BANKING.md` (K1 to K12); everything else on that page is advice.

**What to do now, in this order:**
1. Create your branch from main and name it. Write `relays/STATUS_SM2.md` there with the six first lines of the protocol
   (seat, read, state, on, needs, next push), `read: M1`, and your branch's name. Push it.
2. Start your listener in the background: `python3 scripts/seats/listen.py --seat sm2`. Main's messages and your cards reach
   you here.
3. Read `docs/roles/BANKING.md` and `docs/CLAIM_CARD.md` (the card's form). Do not read the queue's plant ledger,
   anything under `audit/`, the other banking seat's branch, or the peers' notes. Those would end your blindness.
4. **Training: two practice cards, before any live card.** Main sends them here shortly. They are built from faults of the
   record whose answers are already known, and they are not the trial's plants. One holds and one does not, and you are
   not told which. For each, commit your expectation, recompute with your own code, and file a verdict under
   `relays/verdicts/` on your branch:
   - `V_<card>.md`: the verdict (ACCEPT, RETURN or REFUSE), one paragraph of reasons, the path and SHA-256 of your own
     script, and its decisive output;
   - its SHA-256, committed before you are told the answer.

   This is the form until the builder's banking-verdict files exist (T9); then you use those. Main then opens the answers
   and writes on this page what you caught and what you missed. Nothing is held against you; it calibrates you before the
   trial.
5. **The trial** follows: the cards of B2011 to B2017 and four plants, through the queue, once the intake runs.

**What you are free to do:** recompute any way you like within the allowed packages; RETURN a card you cannot decide, and
say why; refuse anything you cannot reproduce; produce your own work through the same door (you never bank your own card
or one built on it).

**One channel:** a question for the author goes to main, here or in your status file, marked as a question for the author.
His words are private: if he tells you something, enter it in plain words and dated, and quote nothing.

## Your cards

| card | what | state |
|---|---|---|
| P1, P2 | two practice cards (M1, M2) | **filed** by you (abaeeebeb): the answers open when V1 has filed |
| P3 | a third practice card (M3), replacing P2 | **sent**: your verdict owed |

## What main is waiting for from you

- your branch's name and `relays/STATUS_SM2.md` with `read: M1`
- your listener running
- your verdict on P3 (M3)
