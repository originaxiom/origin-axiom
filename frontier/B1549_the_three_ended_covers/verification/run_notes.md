# B1549 — run notes (operational; no outcome)

cc (the SM-derivation seat), 2026-10-07. Kept as the run happens, for FINDINGS. No count is recorded here.

- **The seal** at `033f8a8e`, pushed 08:43Z. Its companions (FINDINGS stub, arc_verdict, lock test, views) were committed at
  `c7b7d2d0` while the identity ran. They touch none of the sealed files.
- **The banked identity.** `identity.py` ran 08:44:54–08:47:40Z.
  - Every sealed file hashes as sealed.
  - K2–K5 reproduced (`identity.json`).
- **The run, first launch.** Chained to the identity, `run.py 3` started at 08:47:40Z on three workers.
- **Stopped by the session, not by the seat.**
  - The chain ran as one background command of this session, whose limit is 30 minutes unless set otherwise. The seat had
    not set it.
  - At 09:14:54Z, 30 minutes after the command began at 08:44:54Z, the session stopped the command with its processes. The
    record's last write is at 09:14:53Z.
  - No exit code was written. No worker survived (checked at 09:24:05Z).
  - `run.jsonl` then held 226 rows. Every line is whole, no task appears twice, and the file ends with a newline.
- **Resumed.** The same command, `run.py 3`, started at 09:24:18Z with a two-hour limit.
  - It reported "50 tasks to read (226 done)". run.py skips every task with a row.
  - Each task's draws are seeded by its own key (crc32 of "B1549|route|state|lattice|wbar|character|draw"), so a task's
    reading does not depend on when or beside which tasks it runs.
- **The end.** The resumed run ended at 09:30:13Z with rc 0.
  - `run.jsonl` holds 276 rows, every task of `population.json` once, each with three draws.
  - Checked by key, not by content: no count was looked at.
- **The record.** It was committed unread as `run.jsonl.gz` (gzip -n -9), with the sha-256 of the raw record and of the
  archive in `run_sha256.txt`. `read_out.py` runs once after that commit.
