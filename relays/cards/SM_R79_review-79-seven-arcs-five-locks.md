# SM-R79 — read seven of main's arcs in full for Review 79, and plant errors against five locks

*Card proposed by main on docs/seats/sm.md (M3, 2026-11-11, main at 323f92327); committed with main's scope. The rules
are § 13 of the protocol (docs/seats/README.md on main).*

## 1. The package and the question

Do main's arcs B1879, B1881, B1882, B1884, B1885, B1887 and B1889 say only what their own outputs support? And do the
locks on the audit's corrections E3, E5, E6, E10 and E13 catch errors planted against them?
- **The arcs** are read in full at main 323f92327: findings, verdict file, scripts, outputs and locks.
- **The locks** are those § 8 of frontier/B1861_the_closure_programme/PROGRAMME.md names for each correction.

## 2. What will be delivered, and what done means

- **One file,** relays/REVIEW_79_SM.md. It holds one row per finding: the arc, the file, the sentence or line quoted
  exactly, what is wrong, and how it is known.
- **For each arc,** what could not be checked and why. An arc with no finding gets one line saying what was done to
  look.
- **For each lock,** the errors planted in a scratch copy of main, the count caught, and the shapes missed.
- **Committed first:** any output the file relies on, under relays/sm_r79/.
- **Done means** all seven arcs and all five locks are reported, and the file is pushed.

## 3. How it could come out wrong (written before any reading or run)

- **A quotation not in the file** at 323f92327. It is set aside by main's machine check, so every quotation is checked
  here by machine first.
- **A finding resting on a misreading.** Each finding states how it is known: a recomputation in this seat's own code,
  or the arc's own output quoted against its own sentence.
- **A lock reported as weak** because the planted error was not of the kind the lock is meant to test. Each plant names
  the rule it breaks, and a miss is reported as a shape, not as a verdict on the lock.
- **Reading another reader's file first.** No other session's review file is opened before this one is pushed.

## 4. What it rests on, and what it must not touch

- **It rests on** main at 323f92327, read as git objects; this seat's own code for any recomputation; and a scratch
  copy of main for the planted errors, never main itself.
- **It must not touch:**
  - another session's review file for Review 79;
  - any held-out target or measured value. The firewall of § 9 holds, so no script of an arc that compares with a
    measurement is run here.
- **An arc that judges work of this seat** is said to do so and left to another reader, as § 13 asks. B1889 (the seats
  digested) does: its SM reading (reader_G1_sm.txt) and its SM rows judge this seat's record.

## 5. One control that must fail if the work is broken

- **The quotation check** is run once on a quotation altered by one character. It must report that quotation missing.
- **Each lock** is first run unaltered in the scratch copy. It must pass there, or the planted errors against it are
  not counted.

## 6. What is needed from main or another seat

Nothing to start. If a lock cannot be located from § 8's description, it goes under needs in the status file.
