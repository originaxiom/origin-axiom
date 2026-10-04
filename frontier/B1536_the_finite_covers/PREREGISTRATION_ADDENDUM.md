# B1536 — addendum beside the seal: one control's import, changed before run.py read anything (2026-10-04)

The PREREGISTRATION (sha-256 `eb1a17947bfab6c7ade94fda5046246fdc0e657bcd42e3cd6ba220a349f96d0d`, SEAL_LEDGER) is unchanged,
byte for byte. This addendum records the one change made to a sealed file after the seal. It was made before any outcome was
read.

- **What happened.** The banked identity (§8) ran at 06:28Z on the sealed files. K2 and K4 reproduced their records. Then K1
  stopped with an error before reading anything:
  - `control_k1.py` takes sm:B1532's banked census through a bare `import read_out`, after putting sm:B1532's directory first
    on the path.
  - `identity.py` had already imported this arc's own `read_out.py`, through `read_out_selftest.py` (K6). Python returned
    that cached module, which has no `Route`.
  - So the identity failed and the launcher stopped. `run.py` did not start.
- **Why the records stand.** Run alone, as it was for `k1.json` and `k1_m6.json`, `control_k1.py` imports `read_out` for the
  first time with sm:B1532's directory first, so the old import found the right file.
- **The change.** `control_k1.py` loads sm:B1532's `read_out.py` by its path, under its own module name (`b1532_read_out`).
  The same file is read, and the same function computes the same histogram. Nothing else changes.
- **The check.**
  - In one process that first imports this arc's `read_out.py` (as `identity.py` does), the cached module has no `Route`,
    and the new loader returns sm:B1532's reader.
  - `identity.py` then runs again on the amended files. The launcher starts `run.py` only if the identity holds.
- **The hashes.** `ARTIFACT_HASHES.txt` gives `control_k1.py`'s new sha-256 and this addendum's. It keeps the sealed hash of
  `control_k1.py` as a comment.
- **Nothing else** was run on the population between the seal and this addendum.
- **BANKED IDENTITY:** as sealed (PREREGISTRATION §8). `identity.py` reproduces K1 (M₂, M₃), K2, K4, K5 and K6 and checks
  every hash in `ARTIFACT_HASHES.txt` before `run.py` reads anything.
- **PRIOR ART:** as sealed (PREREGISTRATION §0). This addendum changes no mathematics.
