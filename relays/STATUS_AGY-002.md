seat: agy-002
read: M1
state: working
on: A2-C1
needs: nothing
next push: when A2-C1's blind derivations and unsaid-inputs prose page is committed (after sealing raw script outputs)

---

## Presentation (`M1`)

- **Branch:** `origin/agy-002/verify` (cut cleanly from `main` at `2f3984d275d7b2a666afaca0efe2d15b0ec44761`).
- **What `agy-002` is (two lines):** `agy-002` is a dedicated second-family verifying session (separate from the `agy` frontier session and from `agy-exp`), tasked solely with independent data-free second derivations from statements and stated premises alone (`0 of 19`, zero measured values, zero self-certification). Before `docs/seats/agy-002.md` landed at `95988c96b` and the owner confirmed in plain words on `2026-11-11` that `agy` is a separate seat from `agy-002`, this session left one pre-protocol note at `d37c773d6` on `origin/agy/stage4-sync-2026-11-11`; from `M1` onward all `agy-002` work lives exclusively here on `origin/agy-002/verify`, and `scripts/seats/listen.py --seat agy-002` is used as our listener.

0 of 19.
