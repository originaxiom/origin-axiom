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
