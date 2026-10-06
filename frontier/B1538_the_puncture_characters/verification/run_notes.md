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
- **The partial record matched.** `regen_partial_f.py` ran 19:48:57–19:57Z (485 s): the first 12,826 lines have sha-256
  `1e9c6e55…`, equal to the sealed one, so `run_F.jsonl` is written. `regen_partial_f.json` records the check. It also names
  the first candidate (its cover and its one hit with n ≥ 2), which is needed to find the record. That is a Part L reading
  of one candidate. It was written to the file and not read. It does not touch any choice still open: the scope of Part F′ is
  fixed by structure. The equality is also a check of the regenerated Part L: the first candidate's hit and every one of its
  12,825 readings came out byte for byte as before.
- **`run_f_scoped.py --dry`** (20:05Z): the hash check passes and the scope's aggregates equal the addendum's (12,152 candidates
  in scope, 501,792 planned readings).
- **Part F′, regenerated.** Launched 20:05:37Z by `run_f_scoped.py --workers 3 --record`, unchanged, with `TMPDIR` in the
  scratchpad.
  - The seat's container restarted at about 21:56Z and the run stopped with it. Its log's last line (21:56:20Z) reads 11,675 of
    12,152 candidates and 68,128 of 501,792 readings.
  - Relaunched 21:57:39Z with the same command. The driver's own resume keeps every whole block of the sealed shape, in the
    scope's order, and cuts an incomplete tail. It found 11,675 candidates done and cut nothing (its log has no "cutting"
    line). Each block is written whole and synced before the next, so a stop can leave at most one incomplete tail.
  - The sealed read-out's coverage check requires every candidate's header and exactly its planned readings, so a lost or
    doubled block would show there.
- **The comparison, committed before the regenerated records are read.** `regen_compare.py` compares the two read-outs'
  outputs, and Part F′'s own rows, with every number this seat's relay of 2026-10-06 (its §3) recorded from the original
  read-out. A single difference withholds the bank and goes to ERROR_LEDGER first. It was tested on synthetic records only.
- **Part F′ finished** at 23:25:54Z with rc 0: 12,152 candidates and 501,792 readings, every block of the sealed shape.
- **The append** (`post_partFp_append.py`, 23:35:35Z): `run_F.jsonl` was the sealed partial record (sha-256 `1e9c6e55…`),
  Part F′'s record had 12,152 headers and 501,792 readings, and after the append `run_F.jsonl` has 526,770 lines, sha-256
  `d9bc774d…` (`run_F_append.json`). It is banked as `run_F.jsonl.gz` with both sha-256s (`run_F_sha256.txt`). Nothing was
  read before this record was committed.
