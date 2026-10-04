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
