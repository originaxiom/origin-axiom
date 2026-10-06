# B1538 — run notes (operational; no outcome)

cc (the SM-derivation seat), 2026-10-04. Kept from the run as it happened, for FINDINGS. No Part L or Part F reading is
recorded here beyond the aggregates the addendum states.

- **The seal and the identity.** Sealed at 3b8562a2 (pushed 11:46Z). `identity.py` ran 11:46:57Z–12:08:24Z, chained to Part L:
  K0–K12 reproduce `controls.json` (K1 1,138 s, K12 100 s), all eleven hashes match (`identity.json`).
- **A docstring slip in a sealed file.** `identity.py`'s docstring says "controls.py (K0-K10 ...)"; the code compares every
  field of `controls.json` but the timings, that is K0–K12. No effect on what is checked.
- **Records.** `*.jsonl` is gitignored (the chronicle firewall). `run_L.jsonl` and `run_F.jsonl` are banked as `.jsonl.gz`
  with a sha-256 file of the raw records, as sm:B1532 and sm:B1536 did.
- **Machine.** Shared during Part L's first minutes with sm:B1536's two m003 runs and the e41609cf fast lane (`pytest -n 2`).
- **Part L.**
  - Launched 12:08:25Z on one worker.
  - Stopped at a chunk boundary at 12:27:50Z, right after `m135.D8.4-2-2.w5` chunk 7/8 was written, once the fast lane had
    finished. By exact PID: the launcher first, so that no exit code was written, then the run and its worker. `run_L.jsonl`
    had 7 rows, the last line parsed.
  - Relaunched 12:28:00Z on two workers: "101 chunks to read (7 done)". `run.py` resumes by cover and chunk; the read-out's
    coverage check confirms that no chunk was lost or read twice.
  - Finished 13:45:11Z, exit code 0, 108 rows.
- **Part F, as sealed.** Started 13:45:16Z. Its first line, "B1538 run, Part F: 64422 candidates", was seen when the launch was
  checked. The first candidate planned 65,536 readings, at about 24 a second on one worker.
  - `partF_cost.py` (aggregate only; no candidate, character or n printed): 948,832,288 planned readings, about 458 days on
    one worker; by state and by planned size as the addendum's §0 lists.
  - Stopped 13:54:06Z by exact PID (the launcher, then the run). The partial record, the first candidate's header and 12,825
    readings, every line whole, sha-256 `1e9c6e55…`, is kept unread.
- **The addendum** (87f7b788, 14:20Z): Part F′. Before it: `run_f_scoped.py --dry` (the hash check and the aggregates), the
  timing of ten planned-0 candidates (headers only, discarded), and control K13 (84 s, identical).
- **Part F′.** Launched 14:20:34Z on four workers, after the addendum was pushed; `TMPDIR` pointed at the scratchpad for the
  tasks' temporary directories.
  - 14:31–14:33Z: a structure-only cover count (low_index, degree ≤ 15) ran beside it and took about 45% of the CPU (its
    threads, in another session, are not held back by `nice`). Stopped by exact PID after 82 s. No reading was affected; the
    run only slowed.
  - The worker process of the session restarted at about 14:48Z. Part F′, detached with `setsid nohup`, kept running (6,412
    candidates done at 14:48:36Z); only the session's watcher was restarted.
  - The zero-reading headers finished at about 15:14Z (11,420 of 12,152 candidates); the readings followed at about 77 a
    second on four workers (5,920 of 501,792 at 15:14:43Z).
- **The post-run scripts, committed before the read-out.** `post_partFp_append.py` (the structure check and the append, with
  the sha-256 of `run_F.jsonl` before and after) and `post_run_tables.py` (descriptive tables for FINDINGS, run after both
  read-outs) were written during Part F′ and committed while it ran, before any Part F′ reading was read. The order after
  Part F′ exits 0: the append, the sealed `read_out.py --record` once, `read_out_scoped.py --record` once, then the tables.

## The records regenerated (2026-10-06)

The seat's container was replaced before Part F′ finished. The records were gitignored and unbanked, so `run_L.jsonl`, the
sealed partial `run_F.jsonl` and `run_F_scoped.jsonl` were lost unread. No reading of Part L, Part F or Part F′ had been read.
They are regenerated with the sealed code, unchanged, in this order.
- **The banked identity, first** (`dedd2a9b`): K0–K12 reproduce `controls.json` and all fifteen sealed hashes match.
- **Part L, regenerated.** Launched 18:44:59Z on three workers with `TMPDIR` in the scratchpad. Finished 19:43:24Z with exit
  code 0 and 108 rows, one per (cover, chunk), none repeated. Banked as `run_L.jsonl.gz` with the raw record's sha-256
  (`run_L_sha256.txt`). Its row order differs from the original's (three workers, not one then two), and no part of the
  read-out depends on row order.
- **The sealed partial Part F record, regenerated** by `regen_partial_f.py`, committed before it runs. The original was the
  first candidate's header and 12,825 readings (sha-256 `1e9c6e55…`, the addendum). The original Part L wrote its first 7 rows
  on one worker in the sealed task order, and Part F took its candidates in row order. So the first candidate is the first hit
  with n ≥ 2 among the first 7 tasks in that order (the script stops if there is none). The script reads it by the sealed
  `read_part_F` through the driver path of the addendum (as control K13 does), keeps the first 12,826 lines and writes
  `run_F.jsonl` only if their sha-256 equals the sealed one.
- **Then Part F′**, by `run_f_scoped.py` unchanged; then the append, the two read-outs once each, and the tables, as above.
