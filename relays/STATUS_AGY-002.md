seat: agy-002
read: M1
state: waiting on main
on: A2-C1
needs: nothing
next push: when main writes M2 on docs/seats/agy-002.md

---

## Status Summary (`A2-C1` Delivered)

- **Branch:** `origin/agy-002/verify` (cut from `main` at `2f3984d275d7b2a666afaca0efe2d15b0ec44761`).
- **What `agy-002` is (two lines):** `agy-002` is a dedicated second-family verifying session (distinct from the `agy` frontier session and from `agy-exp`), tasked with independent data-free second derivations from statements and stated premises alone (`0 of 19`, zero measured values, zero self-certification). Before `docs/seats/agy-002.md` landed at `95988c96b` and the owner confirmed in plain words on `2026-11-11` that `agy` is a separate seat from `agy-002`, this session left one pre-protocol note at `d37c773d6` on `origin/agy/stage4-sync-2026-11-11`; all `agy-002` work lives exclusively on `origin/agy-002/verify`.
- **Completed causal commits for `A2-C1`:**
  1. `809f68916` — pre-registered card `relays/cards/AGY-002_A2-C1_three-headline-derivations.md` (before any computation);
  2. `03f291185` — zero-float exact scripts & verbatim outputs (`relays/a2_c1/derive_g_root.py`, `relays/a2_c1/derive_mc_z6.py`, `relays/a2_c1/derive_w_index3.py` and their verbatim output files in `relays/a2_c1/`, before prose and before opening `main`'s arcs);
  3. `d003e482b` — blind theorems & unsaid-inputs ledger `relays/a2_c1/BLIND_DERIVATIONS_AND_UNSAID_INPUTS.md` (before opening `main`'s arcs);
  4. Closing comparison & delivery commit — `relays/a2_c1/COMPARISON_WITH_MAIN_ARCS.md` and `relays/AGY002_TO_CC_2026-11-11_A2_C1_DELIVERED.md`.
- **Listener:** `scripts/seats/listen.py --seat agy-002` running silently in the background.

0 of 19.
