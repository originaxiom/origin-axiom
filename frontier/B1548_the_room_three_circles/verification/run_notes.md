# B1548 — run notes (operational; no outcome)

cc (the SM-derivation seat), 2026-10-14. Kept as the run happens, for FINDINGS. No count is recorded here.

- **The seal** at aa3506514, pushed at 17:15Z on 2026-10-14.
- **The machine.** The seal's §6 says the run starts when the seat's W80 ends. W80 ended at 18:19:19Z (rc 0), and
  nothing else of the seat was computing then.
- **The banked identity and the run, chained.** At 18:19:44Z the seat launched, detached, `identity.py` (K1–K9
  re-run against `controls.json`, and every sealed file's sha-256 against `ARTIFACT_HASHES.txt`). It was chained by
  `&&` to the sealed command `run.py --workers 3 --record`, so the run starts only if the identity holds.
  - Three workers, not four, because the kernel's memory limit killed three of sm:B1547's workers when other jobs
    shared the memory (sm:B1547's run notes).
  - The seat's pre-push test suite (one process) runs beside it. A watch on available memory is armed, and the suite,
    not the run, yields if memory runs short.
- **A slip of the seat's shell at the launch, disclosed.** The launch line set the log path in a backgrounded
  subshell, so the seat's own `cat` of the log in the foreground read an empty path and failed. The launch itself was
  not affected: the log was written where intended, and the identity's process was running.
- **The banked identity held, 18:19:44–18:23:13Z.** Controls K1–K9 reproduced `controls.json` in every field but the
  timings, and the nine sealed files hash as sealed (`identity.json`). The sealed run started at 18:23:13Z: "168 tasks to
  read (0 done)".
- **The seat's own session restarted at about 18:53Z; the run did not.** The restart stopped the seat's background
  waiters and its pre-push suite, but not the detached run. At 18:53Z the run's process (started 18:23Z) and its three
  workers were alive (about 84% CPU and 1.5–1.7 GB each), and the progress line read 133 of 168. The waiter and the
  suite were started again; nothing of the run was touched.
- **The end of the run.** The run ended with rc 0 at 19:00:56Z on 2026-10-14, after 37 min 43 s: one start, no stop.
  `run.jsonl` has 168 rows, every line whole and every sealed task exactly once. That was checked by parsing each
  line's route and index only; no count was read.
- **The record** was gzipped (`run.jsonl.gz`, `gzip -9 -n`), with both sha-256s in `run_sha256.txt`. The archive
  decompresses to the raw record's sha-256. It was committed before `read_out.py` was run.

