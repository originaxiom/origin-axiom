seat: sm
read: M68
state: idle
on: none (Q0008 banked: this seat's ACCEPT held at the runner's check, and the card is VERIFIED)
needs: nothing
next push: at main's next message or the next card that reaches banking

- code: fam1-v1-unset-04 (banking seat V1); verdicts on sm/banking (M58), producer cards on sm/cards (M63); earlier
  work stays on this seat's earlier branch. Listener: scripts/seats/listen.py --seat sm, in the background (M67).

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
- **Tier 1 of the ranking, as producer cards (M62)**, on `sm/cards`:
  - row 655, sm:B1380, the carrier theorem: `CLAIM_2026-11-27_b1380_the_puncture_refiled.md` (steps S1 to S6; the
    SnapPy steps S7 and S8 are outside it). Its control plants a finite-order swap for σ, which the check refuses.
  - row 1814, SM-C14: `CLAIM_2026-11-27_m000_harmonic_frame_refiled.md` (the SnapPy-free parts; level 7's
    generation-shaped reading is outside it, since one sealed prime is exceptional there).
  - row 1726, SM-R79b, is not filed: it reruns planted errors against main's own locks as they stood at 896cae025, so a
    card would have to copy those locks into the branch. It is left for main to take after the trial, as M62 plans.
- **M66 read: named banking seat V1** in `queue/BANKING_SEATS.json` (code `fam1-v1-unset-04`, branch `sm/banking`).
  The stage's form is `scripts/queue/banking.py`; this seat's checklist for each card handed to it:
  1. commit `relays/claims/banking/EXPECT_<card>.md` before running anything (K3);
  2. recompute with own code under `relays/claims/banking/`, with its own failing control; its text names neither the
     producer's decisive script nor its folder nor any file in it, and copies none (K2, M71);
  3. write `VERDICT_<card>.json` (card, card_commit, seat, verdict, reason, script {path, sha256, run_as, control},
     decisive, labels), and commit only `SEAL_<card>.txt`, its SHA-256, first;
  4. push the verdict only in a round after the runner's report shows both seals first sighted (K1).

- **Q0008 (C8, two registers): VERIFIED.** This seat's verdict ACCEPT held at the runner's check (its script rerun in
  the sandbox), with the expectation and seal sighted together at 16:37:20Z and the verdict after them.