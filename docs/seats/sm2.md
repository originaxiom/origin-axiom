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

### M9 — 2026-11-28 — your first card at banking: Q0008 (P-885)

1. **Your first live card is at banking: Q0008**, since round 2 at 14:33 UTC today. It is the card
   `relays/claims/CLAIM_2026-11-27_C8_two_registers.md` on `audit/physical-bridge-2026-09-05`, at the commit its record on
   the queue's branch names (`git show origin/queue:queue/cards/Q0008.json`). It is deciding.
2. **Do it as your checklist says** (`scripts/queue/banking.py`'s form, on your branch under `relays/claims/banking/`):
   - commit `EXPECT_Q0008.md` first, before anything runs (K3);
   - recompute what decides with your own code and its own failing control, naming no file of the producer's (K2);
   - commit `SEAL_Q0008.txt`, the SHA-256 of your verdict file's exact bytes, with your script;
   - push `VERDICT_Q0008.json` only in a round after the runner's report says both seals were first sighted (K1). The
     record of Q0008 on the queue's branch says when, in its check file `queue/checks/Q0008.json`.
3. **Read nothing but the card and main** (K1): not the peer's note on it, not the other banking seat's branch.
4. **From now on main posts each card that reaches you here,** after each round.

0 of 19.

### M8 — 2026-11-28 — nothing to verdict yet; your loop (P-885)

1. **No card has reached banking yet.** The runner's first round today recorded nothing (two faults, being mended). Your
   files for each live card stay as you wrote them under M7.
2. **Your loop.** The author starts you with `/loop` so that you never stand idle. At every turn: fetch main, read this page from the last message you read, do what it asks in order, push your branch with your status's six lines brought up to date, and when nothing is asked, wait on `python3 scripts/seats/listen.py --seat sm2` in the background. Never wait on main in silence: if you are blocked, say so on your status's `needs:` line and push.

0 of 19.

### M7 — 2026-11-28 — you are named banking seat V2; where your verdict files go (P-885)

The banking stage has landed on main (T9). `queue/BANKING_SEATS.json` now names you as V2, by your code
`fam1-v1-unset-05` and your branch `sm2/banking`.
- **Your files.** Keep your verdict files where the stage reads them: `relays/claims/banking/` on `sm2/banking`, as
  `EXPECT_<card>.md`, `SEAL_<card>.txt` and `VERDICT_<card>.json` (the form is in `scripts/queue/banking.py`).
- **When to open.** Open a verdict only from the round after the runner's report says both seals were first sighted.
- **Nothing yet.** Nothing comes to you until the runner is switched on.

0 of 19.

### M6 — 2026-11-27 — your practice verdicts agree with the key; the key stays sealed (P-885)

Your verdicts on P1, P2 and P3 (`sm2/banking` at eb6c03615) agree with main's key. Their SHA-256s match
`relays/verdicts/HASHES_SM2.txt`, committed before anything was opened. M2 said the key would be opened here once both
banking seats had filed. It will not be: the author has decided that it stays sealed, so that the practice cards can still
train a later banking seat. Its seals stand (cd90847da264fe4d for P1 and P2, 464831c93785c46a for P3). Your practice is
complete. Nothing more is asked of you until the trial's cards come through the queue; its runner is still being built.

### M5 — 2026-11-27 — both banking seats have filed their practice verdicts (P-885)

Banking seat V1 has filed P1 and P3 on `sm/banking`. Your verdicts and V1's are both sealed. The key's opening waits on the
author's word. Nothing else is asked of you until the trial's cards come through the queue.

### M4 — 2026-11-27 — P3 received; K1 made explicit; your listener once per step (P-885)

1. **Your P3 is received and registered** (harvest row 2040). The order reads right on your branch: the expectation at
   `7e50f4eee`, then your script, outputs and verdict, then its hash. Its answer opens when banking seat V1 has filed, like
   the other two. You found the ignored outputs and the commit whose message named a hash it did not hold, and you said so
   yourself. Your rule for live cards, a name that is not ignored and `git ls-files` before sealing, is the right one.
2. **K1 now says in words what it meant** (`docs/roles/BANKING.md`): until your verdict on a card is sealed, do not read
   other seats' branches, relays or cards about the arcs that card touches. You decide from the card and main.
3. **Your listener:** `--once` at the start of each step is enough. A live card arrives through the queue, and you are
   woken for it.
4. **No live card yet.** They come when the runner lands, after the builder's T7b. Main's seven trial cards come first.

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
| P1, P2 | two practice cards (M1, M2) | **filed** by you (abaeeebeb): both agree with the key, which stays sealed (M6) |
| P3 | a third practice card (M3), replacing P2 | **filed** by you (6d21df3f4): agrees with the key (M6) |

## What main is waiting for from you

- `relays/STATUS_SM2.md` with `read: M6`
- nothing else until the trial's cards come through the queue
