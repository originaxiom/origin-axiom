# The seats: how main and the seats work together

*In force from 2026-11-11, by the owner's ruling to main (register row P-795). Main keeps this page. A seat that finds
a rule here wrong, or in its way, says so to main in a note; main amends the page with a date.*

## 1. In one minute

- **Each seat has one page on main,** in this folder. Main writes to a seat there and nowhere else.
- **Each seat runs a listener** that fetches the repository every ten minutes and wakes the seat only when its page
  has changed.
- **Each seat answers on its own branch:** one status file at a fixed place, and its work.
- **Main runs the same listener on the seats' branches,** so it wakes when a seat pushes.
- **Nobody relays by hand.** The owner supervises from these pages.

## 2. The seats

| seat | its page | what it does | how main reads it |
|---|---|---|---|
| the SM seat | `docs/seats/sm.md` | verifies the physical lane's results; later builds the parameter inventory | directly |
| the web seat (chat1) | `docs/seats/chat1.md` | re-audits main's corrections; verifies the SM seat's results that touch data and the agy lane's theorems; reads headline results cold | directly |
| agy-002 (the session of the branch stage4-sync) | `docs/seats/agy-002.md` | second derivations of main's results that use no data, from the statement alone | through the mask; its code is never run by main |
| the agy lane | `docs/seats/agy.md` | frontier work, at the owner's word; verified later | through the mask; its code is never run by main |
| agy-exp (the session of the loop's branch) | `docs/seats/agy-exp.md` | verifies the pure mathematics of the SM seat and of the web seat | through the mask; its code is never run by main |
| the advisor seat (cld-advisor) | `docs/seats/cld-advisor.md` | builds five packages of the clean-up; is not asked to verify | directly |
| the physical lane | `docs/seats/physical.md` | builds the packages on the action and the dynamics; its results are verified by the SM seat | its mathematical files, through the second mask |
| main (cc) | — | directs; recomputes what decides; lands; keeps the map, the programme and the register | — |

No seat verifies its own work. No seat gives a verdict on what it built.

**A seat's name is an address and nothing more.** It says where a piece of work is sent. It is not an author and not an
authority: what is written about a result is how it was checked (computed once; recomputed with separate code;
recomputed on another family of model; expectations committed first; tested against planted errors), not who checked
it. The owner has ruled this (register row P-797); the words for how a check is named are in `TERMINOLOGY.md`, and § 12
below lists them.

## 3. The loop

1. **Main writes.** It adds a numbered message at the top of your page: M1, M2, and so on. It also keeps two lists on
   the page up to date: your cards, and what it is waiting for from you.
2. **You hear.** Your listener sees that the page changed and shows you the messages you have not read.
3. **You act,** on your own branch, in your own way.
4. **You push.** Your status file says where you are. Your work is in your branch.
5. **Main hears,** reads what you pushed, recomputes what decides, lands it or sends it back, and writes to you.

## 4. The listener

Run it from the root of your clone, in the background:

```
python3 scripts/seats/listen.py --seat NAME
```

NAME is your page's name without `.md`: `sm`, `chat1`, `agy-002`, `agy-exp`, `agy`, `cld-advisor` or `physical`.

- **It fetches main every ten minutes** and looks at your page only.
- **It is silent while nothing is new.**
- **When your page has changed it prints the messages you have not read and stops.** Read them, act, and start it
  again.
- **It never changes your files, your branch or your HEAD.** It only fetches. Its memory is in your git directory.
- **If your session cannot keep a command running in the background,** run it with `--once` at the start of each step
  of work and at least every ten minutes: status 0 means there is something new, 3 that there is not.
- **If it says it could not look,** say so in your status file. Do not treat it as nothing new.

Start it once, when the owner asks you to fetch. After that he asks you nothing.

## 5. Your status file

One file at the root of your branch's relays folder, named for you: relays/STATUS_SM.md, relays/STATUS_CHAT1.md,
relays/STATUS_AGY-002.md, relays/STATUS_AGY-EXP.md, relays/STATUS_AGY.md, relays/STATUS_CLD-ADVISOR.md, relays/STATUS_PHYSICAL.md. Rewrite it at
every push. Its first lines, exactly these six:

```
seat: chat1
read: M3
state: working
on: C2
needs: nothing
next push: when C2's outputs are committed
```

- **read** is the last message of main you have read and taken in.
- **state** is one of: working, waiting on main, blocked, idle.
- **on** is the card you are on.
- **needs** names what you need and from whom, or says nothing.

Below those lines write what you like. A seat that already keeps a status page keeps it and names its path there.

## 6. The card: one page before a piece of work

Before you start a piece of work, commit one page on your branch, relays/cards/NAME_Cn_a-few-words.md, with six
things:

1. the package and the question, in a sentence;
2. what you will deliver, and what done means;
3. how it could come out wrong, written before any run;
4. what it rests on, and what it must not touch;
5. one control that must fail if the work is broken;
6. what you need from main or from another seat.

- **A card main proposed on your page is approved the moment you commit it** with the scope main gave. You do not
  wait.
- **A card of your own** waits for main's word, which comes at main's next landing: approved, or amended with the
  reason.
- **You may decline a card,** split it, or propose a better one. Say so in your status file.
- **After that you work your own way.** Main checks no step.

## 7. Delivering

- **Outputs are committed before the page that reads them.** A count or a value that could be chosen after the fact is
  sealed first: its rule and what you expect are committed before the run.
- **Say what was not done.** A delivery names what it leaves out.
- **Write one note** in your relays folder saying which card it closes and where each thing is.
- **Main recomputes what decides** by its own route, and lands the result with a grade that says how far it was
  checked. Where main cannot reproduce it, the note comes back with the reason.

## 8. Verifying another seat's work

- **Your card says, before any run, what would count as not reproducing.**
- **You use your own code** for the number that decides. You may read the builder's files; you do not run its script
  and call that a check.
- **One verdict for each item:** REPRODUCED, DIFFERS, or CANNOT CHECK, with the commit you read and one line of why.
- **A question for the builder** goes in your status file under needs. Main passes it on through the builder's page.

## 9. What is fixed for every seat

1. **The firewall.** No held-out target is computed, and nothing is compared with a measured value, outside a sealed
   card that main has approved under the owner's hold. If a check can be made only by such a comparison, the verdict
   is CANNOT CHECK, with the comparison named.
2. **No verdict on your own build.**
3. **Nothing changes on main before main has recomputed it.** You write to your own branch only.
4. **No question of fact is put to the owner.** A question for him goes to main.
5. **The owner's messages are private** (his ruling of 2026-11-11, register row P-796). What he rules is entered in
   plain words, dated. Quote nothing he says to you: not in a page, a status file or a commit message. What you
   recorded before that date stays as it is.
6. **Commits carry the repository's author.** No vendor's or model's name stands in a tracked file.
7. **Main's arc numbers are main's.** A seat numbers its own work in its own way.

## 10. What a seat is free to do

- Choose its method.
- Propose a card for anything, in the plan or not.
- Run several cards.
- Say that main is wrong, with the computation that shows it. The record has many cases where a seat was right
  against main.

Its name stands on its results in the record.

## 11. Where things are

- The plan and its packages: `frontier/B1861_the_closure_programme/PROGRAMME.md`.
- Where the work stands: `frontier/B1883_where_we_stand/WHERE_WE_STAND.md`.
- What each seat has sent and what became of it: `frontier/B1889_the_seats_digested/SEATS.md`.
- Every item a seat has sent, with its path and commit: `docs/HARVEST_LEDGER.md`. A harvest row is cited on these
  pages by its number.
- The binding rules: `WORKING_RULES.md`.

## 12. How a check is named

By the owner's ruling of 2026-11-11 (register row P-797), what is written about a result is how it was checked. Use
these words and no others, in a delivery, a verdict or a page:

| the label | what it says | its evidence |
|---|---|---|
| computed once | one computation, by whoever built it | the script and its output |
| reproduced | the same code run again, on a clean checkout | the second output |
| recomputed independently | a second computation, with code that shares none with the first | both scripts and both outputs |
| recomputed on another family of model | the same, by a session of another family | both scripts and both outputs |
| expectations committed first | what was expected, and what would count as failure, was committed before the run | the commit of the expectations and the commit of the output |
| tested against planted errors | faults were planted and the count that was caught is given | the planted cases and the count |
| checked by a person | read or recomputed by a human being | none yet |
| checked outside the project | by someone who is not part of it | none yet |
| not independently checked | nothing of the above | — |

- **A label names its evidence,** so that it can be held to the files.
- **A check has a result, not a verdict.** No session accepts, approves or rules. Where main's builder still reads the
  words "verdict" and "accepted" in a seat's file, they stay until main changes what it reads.
- **No session is credited in a statement of the mathematics.**

