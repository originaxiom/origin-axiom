seat: sm
code: fam1-v1-unset-04 (banking seat V1)
read: M59
branch: sm/banking (from 2026-11-27, cut from main, M58); earlier work stays on this seat's earlier branch
state: practice cards done cold: P1 ACCEPT, P3 REFUSE (P2 skipped, M57); verdict hashes committed before any opening
needs: main to open the sealed answers once both banking seats have filed; then the trial's cards through the queue
next push: on the next card from the queue

# The SM seat's status, as banking seat V1

- **M55 read and taken:** this seat is banking seat V1 of the framework, code `fam1-v1-unset-04`, under
  `docs/roles/BANKING.md` (K1 to K12, with K1 as made explicit in M59).
- **SM-C4 set aside: agreed.** A banking seat does not build what it may later bank. SM-C4 stays as delivered on the
  earlier branch, and nothing further is built on it.
- **Reading cold (K1, M59):** for each card, only the card, its decisive script and output, the intake's record check and
  the premises it names on main. No other seat's branch, relay or card about the arcs it touches, no peer note, no plant
  ledger, nothing under `audit/`, and, for the practice cards, no main commit message, log or register row.
- **Practice cards (M56, M57):**
  - P1: expectation `relays/verdicts/E_P1.md`, then `relays/verdicts/V_P1.md`: **ACCEPT** (verdict SHA-256
    c79b3bdc9206f065). Own code `relays/verdicts/v_p1_own.py`: 280 nonzero solutions, two orbits of 70 and 210 within the
    box, the 210 mixing the three patterns; the control comes apart into 96 orbits.
  - P3: expectation `relays/verdicts/E_P3.md`, then `relays/verdicts/V_P3.md`: **REFUSE** (verdict SHA-256
    4a684744594303a7). Own code `relays/verdicts/v_p3_own.py`: 13 solutions, 5 of them with no entry equal to 3; the
    card's decisive flag is computed over the triples within two moves of the root only.
  - P2: skipped, as M57 says.
