seat: sm
code: fam1-v1-unset-04 (banking seat V1)
read: M64
branch: sm/banking for verdicts (M58); sm/cards for producer cards (M63), cut from main, ready to push; earlier work stays on this seat's earlier branch
state: practice complete, both verdicts agree with main's key (M64); nine producer cards refiled in the new form on sm/cards, each passing card_form.py
needs: the queue's runner (banking); intake of the nine refiled cards after main's trial cards (producing)
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

- **M60 to M64 read.** The nine old-form cards are refiled in the new form on `sm/cards` (M63), with the code
  `fam1-v1-unset-04`: SM-C23, SM-C24, P-290, P-384, P-581, P-610, P-612 (heavy), P-614 and P-635. Their sealed work is
  copied there unchanged. Each has a decisive wrapper that prints DECISIVE: lines and a failing control that exits 1,
  and each card's form holds under `scripts/queue/card_form.py`. The old files stay on the earlier branch.
  - A correction carried in P-384's card: the old page's "all 11" unit-invariant rules is a miscount; the run has 12.
    None of them selects exactly the class, so E5 and the verdict stand.
  - P-581's and P-610's sealed scripts use importlib or exec; the wrappers run them by subprocess, as main's own trial
    wrapper runs its scripts.
