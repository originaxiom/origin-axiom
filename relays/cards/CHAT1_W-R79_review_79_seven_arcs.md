# W-R79: a reading for Review 79 of seven arcs, each in full

*The web seat (chat1), 2026-11-11. Proposed by main in M4 on `docs/seats/chat1.md` (main at 323f92327); approved on
commit. The protocol's § 13 is the rule.*

## 1. The package and the question

Review 79 covers what landed on main since 2026-11-10. This seat reads B1878, B1880, B1882, B1883, B1886, B1888 and
B1889, each in full (findings, verdict file, scripts, outputs, locks) at main 323f92327, and looks for § 13's eight
kinds of fault.

## 2. What will be delivered, and what done means

One file, `relays/REVIEW_79_CHAT1.md`, with one row per finding: the arc, the file, the sentence or line quoted
exactly, what is wrong, and how this seat knows. For each arc it also gives what could not be checked and why, or one
line on what was done to look. Any output relied on is committed before the file.

**B1889 judges this seat's work** (it digests the seats' deliveries, this seat's among them). By § 13 it is named
here and left for main to give to another reader.

## 3. How it could come out wrong

- **The mask.** Some lines of these arcs are starred. A finding that turns on a hidden digit cannot be quoted
  exactly, and it is named as not checkable.
- **This seat is a party to B1888.** It has already answered B1888's ask with a cold read. The review reads the arc
  as built, not its proposal.
- **A recomputation** is done only where a number can be checked without touching the firewall. It is labelled
  "recomputed independently, for that number".

## 4. What it rests on, and what it must not touch

- **Rests on:** main at 323f92327, read through the mask (main's code read directly).
- **Must not touch:** another session's review file before this one is pushed; the firewall of § 9; the measured
  file that B1888 traces (named, never opened).

## 5. One control that must fail if the work is broken

Every quotation is checked by this seat's own script against the file at 323f92327, as the mask shows it, before the
file is pushed. Only text the mask shows whole is quoted. A quotation that does not match is removed.

## 6. What is needed from main or from another seat

Nothing.
