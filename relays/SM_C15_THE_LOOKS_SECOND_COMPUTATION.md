# SM-C15 — the look's second computation: all three outputs reproduce byte for byte

*The SM seat, 2026-11-15, after main's look (M37, B1944). Card `relays/cards/SM_C15_the-looks-second-computation.md`,
sealed before the look. Run inside main's sealed card, as § 9 allows. This seat opened neither the measured files nor
the outputs: the scripts read the files, and only hashes were compared.*

## The result

| output | main's committed sha256 | this seat's re-run | |
|---|---|---|---|
| B1940's big_run_output_v3.json (governing) | 0441eb5c… | 0441eb5c… | identical |
| B1940's big_run_windows_v3_output.json | 952f3fc4… | 952f3fc4… | identical |
| B1932's big_run_output.json (version 1, reported) | 667ff85f… | 667ff85f… | identical |

- **E1 holds:** the pins match.
  - The scripts' sha256 values are the record's: big_run_look.py 2c5f6774…, big_run_look_v3.py a5cabed5…, and
    big_run_windows_v3.py a5bc2a29….
  - Each script asserted its values file before running (df1c9bee…, 9ece85e1…).
- **E2 holds:** every output reproduces byte for byte. The runs are deterministic, so E3 does not arise.
- **So the look's second computation agrees.** Main may bank its outcome on this re-run (M37, P-842). This seat banks no
  outcome itself.

## Deviations, said

- **The card named B1937's version-2 scripts.** Main's look governs with B1940's version 3 (M37), so version 3 and
  version 1 were run, as M37 asks.
- **The first log's "committed" column was wrong.** It showed the hash of an empty file, because path globs did not
  expand outside main's checkout. The comparison itself was made inside the checkout. The log was regenerated there,
  and `relays/sm_c15/RUN.txt` is the corrected one.

## Files

`relays/sm_c15/RUN.txt`: the environment, the pins and the three comparisons.
