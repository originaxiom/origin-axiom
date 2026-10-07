# B1550 -- the run, as it happened

- **The identity.** `identity.py` ran 11:34:47Z to 11:36:50Z on 2026-10-07, chained to the run in one background command
  with a two-hour limit. There were no hash mismatches, K2-K5 reproduced, and it held (`identity.json`).
- **The run.** `run.py 3` started at 11:36:50Z with 120 tasks to read and none done, and ended at 12:26:53Z with rc 0.
  There was one start and no stop.
- **The record.**
  - Before it was read, it was checked by key: 120 rows, every sealed task once, none twice, three draws in every row.
  - It was compressed (`gzip -n`) to `run.jsonl.gz`. `run_sha256.txt` holds the raw file's sha-256.
  - It was committed unread.
- **Alongside the run** the seat worked in its scratch on the next arc's structure. That work read structure only: the
  line's room on the tetrahedral covers, the four over the spin line, and the spin cover's presentation. It touched none
  of this arc's files and read no row of this record.
