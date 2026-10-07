# B1547 — run notes (operational; no outcome)

cc (the SM-derivation seat), 2026-10-06 and 2026-10-07. Kept as the run happens, for FINDINGS. No count is recorded here.

- **The seal** at 32cc4ff6 (pushed 23:35Z on 2026-10-06).
- **The banked identity**: `identity.py` ran 23:35:31–23:46:27Z. K1–K8 reproduced `controls.json` in every field but the
  timings, and the seven sealed files hash as sealed (`identity.json`, 732fea09).
- **The run, first launch.** Chained to the identity, `run.py --workers 3 --record` started at 23:46:27Z. sm:B1538's bank tests
  ran beside it for about 13 minutes on two workers.
- **Stopped and relaunched on four workers.** The fourth core was idle once those tests ended. The run was stopped at
  00:03:44Z on 2026-10-07 by exact PID: the launcher first, so that no exit code was written, then the run, then its workers
  and their resource tracker. `run.jsonl` then had 148 rows, every line whole, no task twice. The same command with
  `--workers 4` was launched at 00:03:49Z. The sealed `run.py` resumes by task ("1900 tasks to read (148 done)"), and the
  read-out's coverage check confirms that no task is lost or read twice. Tasks in flight at the stop were read again from the
  start, with the same seeds.
- **Three workers killed by the kernel's memory limit; the run stopped and resumed on two workers.**
  - The kernel's out-of-memory killer (memory cgroup) killed three of the four pool workers on 2026-10-07, at about
    01:45:42Z, 02:14:28Z and 02:40:58Z (`dmesg`). Their resident sizes were 3.6 to 5.1 GB.
  - Other jobs of the seat shared the machine's memory at those times: two affected-test runs and a re-run of the web
    seat's listening log.
  - The pool replaced each worker. The three tasks in flight, route R at members 611, 743 and 910, never returned, and
    the pool waited on them. `run.jsonl` stood at 2045 rows from 03:42Z, every line whole, no task twice.
  - The run was stopped at 04:24:14Z by exact PID: the launcher first, so that no exit code was written, then the run, its
    four workers and the resource tracker.
  - The same sealed command with `--workers 2` was launched at 04:24:25Z and reported "3 tasks to read (2045 done)". The
    three tasks are read from the start with their sealed seeds, and nothing else of the seat runs beside them.
- **The end of the run.**
  - The three tasks read from 04:24:25Z, and the run ended with rc 0 at 04:25:41Z on 2026-10-07: 2048 rows, every task
    once, every line whole.
  - The record was gzipped (`run.jsonl.gz`, `gzip -9 -n`), with both sha-256s in `run_sha256.txt`, and committed before
    `read_out.py` was run.
  - A slip of the seat's shell while writing these notes is disclosed. Backquotes inside an unquoted here-document were
    taken as commands, and a stray `gzip -9 -n` waited on its input until killed by exact PID. It touched no file:
    `run.jsonl.gz` decompresses to the raw record's sha-256, the notes were unchanged, and no read-out file existed.
