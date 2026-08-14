# B557 — the escalator campaign: two cells reported and locked, the rest never run

cc banking seat, consolidated 2026-08-01 under B840. Prereg in `PREREGISTRATION.md`.
Gate 5; the physics-ladder cell is firewalled hypothesis and is **not** banked as physics.

## Why this file did not exist

**The campaign's results were reported all along — in `CARRIERS_FINDINGS.md` and `E2_FINDINGS.md`,
not in a file named `FINDINGS.md`.** B837's audit therefore counted B557 as a sealed prereg with no
report. **That was a filename artifact, exactly as with B519** (B826). This file consolidates; it
adds no result.

## What ran

**E1 — the explicit 8-letter carrier σ₈** (`CARRIERS_FINDINGS.md`). Adversarially verified and
re-checked in-sandbox, locked by `tests/test_b557_carriers.py`. Closes B557-E1 / FL3. Pure
combinatorics / spectral number theory; **lit-gates UNCLEAR → no novelty claim made.**

**E2 — rule uniqueness: the escalator is FORCED at rung 1, CHOSEN above** (`E2_FINDINGS.md`).
Computed exactly. This is the honesty crux of B556's hypothesis — *is `(C,D) = (M, M²)` forced or a
choice?* By B517 the coupling blocks must intertwine the base (`CM = MC`, `DM = MD`), so `C = p(M)`.
**Forced at the first rung; a choice at every rung above it.**

> **E2 is the load-bearing result, and it is a partial deflation of the escalator hypothesis, not a
> confirmation.** "Canonical" survives only at rung 1.

## What never ran

**E0, the lit-gate that gates the whole campaign's novelty language** — queued behind other searches
and never executed. Also unrun: the saturation cells above rung 1, and the firewalled
physics-ladder cell.

**Consequence, and it is why E0 mattered:** the prereg made E0 gate *all* novelty language. Since E0
never ran, **no novelty claim is available for E1 or E2**, and none is made. `CARRIERS_FINDINGS.md`
already records the lit-gates as UNCLEAR.

## Disposition

**Reported, partially run, honestly bounded.** E1 and E2 stand as computed and locked; the campaign
question — *is the escalator a canonical, novel functor generating the object's interior?* — is
**answered only at rung 1 (forced) and left open above it**, with novelty ungated.
