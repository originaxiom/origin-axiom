# B1538 — addendum beside the seal: Part F scoped to what can be read (Part F′), written after Part L and before any Part F reading was read (2026-10-04)

The PREREGISTRATION (sha-256 `dc351bf1a041598608d11122fc468e018f4d3f3f04b7dd138a667f6d50df1b97`, SEAL_LEDGER) is
unchanged, byte for byte, and so are the ten other sealed files. This addendum records why the sealed Part F was stopped, and
seals the Part F′ that reads in its place. It was written after Part L finished and before any Part F reading was read.

## 0. What happened

- **Part L ran as sealed.** It finished at 13:45:11Z with exit code 0: 108 rows, one for every chunk of K11's manifest. Its
  restart at 12:27:50Z (from one worker to two, at a chunk boundary) is disclosed in FINDINGS.
- **Part F started as sealed** at 13:45:16Z. Its first line, "B1538 run, Part F: 64422 candidates", was seen when the launch
  was checked.
- **As sealed, it could not finish.** The first candidate planned 65,536 readings, read at about 24 a second. Part F runs on
  one worker and is not resumable.
  - An aggregate-only count gave 948,832,288 planned readings, about 458 days on one worker. It took each candidate's
    planned readings from Part L's records and the sealed `smith_fourth_roots`, and printed no candidate, character or n.
  - By state: m135 917,526,528; m136 31,302,656; m003 2,688; m004 416.
  - Candidates by planned readings: 0: 11,362; 16: 2; 64: 48; 128: 128; 256: 80; 512: 162; 1,024: 370; 2,048: 1,388;
    4,096: 7,348; 8,192: 33,790; 65,536: 9,744.
  - The design never estimated Part F's cost (ERROR_LEDGER, 2026-10-04).
- **It was stopped** at 13:54:06Z, by exact PID. Its partial record `run_F.jsonl` is kept, unread, as the sealed run's
  record: the first candidate's header and 12,825 of its 65,536 readings, every line whole. Its sha-256 is
  `1e9c6e5550f2bb46453375cce8761e87ad6307a19d0ce25f1bb80f74602bcec7`.

## 1. What does not change

- The PREREGISTRATION, the ten other sealed files, and the reading rules of §9.
- **The sealed read-out runs once, unchanged.** `read_out.py --record` reads `run_L.jsonl` and `run_F.jsonl`, which will be
  the partial record followed by Part F′'s rows (§2).
- On these records P7 and P8 are False on a refuting row, wherever it is. Otherwise they are None, since Part F is
  incomplete. They cannot be True.

## 2. Part F′

- **In scope.** Fixed by structure before any Part F reading was read:
  - every candidate on m004 and m003, the golden pair: 8 and 42 candidates, with 416 and 2,688 planned readings;
  - every candidate on m136 and m135 with at most 1,024 planned readings, zero included: 4,923 and 7,179 candidates, with
    277,504 and 221,184 planned readings. A candidate's planned readings are four times the sealed `smith_fourth_roots`.
  - In all, 12,152 candidates and 501,792 planned readings.
- **Out of scope.** 52,270 candidates of m136 and m135, each with 2,048 or more planned readings, 948,330,496 in all. The
  sealed record's first candidate is one of them.
- **Why this cut.** Cost only.
  - A candidate's planned readings are fixed by its cover's invariant character group and its ζ. No membership, capW or
    capL2 has been read anywhere.
  - The golden pair is read whole, as the owner's "choice might be golden" asks.
  - At 1,024 the run takes about two and a half hours on four workers (§5). The next size, 2,048, would add 2.8 million
    readings, about eight hours more.
- **The driver,** `verification/run_f_scoped.py`.
  - Each candidate is read by the sealed `run.py`'s own `read_part_F`, loaded by path and unchanged, in a spawned process.
    The sealed Part F likewise ran in its own process.
  - The task writes a one-row `run_L.jsonl` in a temporary directory: the candidate's Part L row, with that one hit and the
    fields `read_part_F` reads. It points the sealed module's `HERE` there and calls `read_part_F(True)`. It returns the
    `run_F.jsonl` written there: the candidate's header and its planned readings.
  - Four workers read golden candidates first, then silver ones by planned readings ascending, in the record's order within
    each.
  - Each block is checked for shape only (header, row count, kind, candidate) and appended to `run_F_scoped.jsonl`. The
    driver resumes by whole candidates.
  - Before reading, it checks every line of `ARTIFACT_HASHES.txt` and the aggregates above. A single difference stops it.
- **Then** `run_F_scoped.jsonl` is appended to `run_F.jsonl`, and both files' sha-256 are recorded before and after.

## 3. The reading

- The sealed read-out runs once (§1). Then `verification/read_out_scoped.py --record` runs once.
- It makes one call of the sealed `evaluate`, loaded by path and unchanged, on:
  - Part L's rows with every out-of-scope candidate's hit removed, and nothing else changed;
  - `run_F.jsonl`'s rows at in-scope candidates.
- **P7′ and P8′** are that call's P7 and P8: P7 and P8 on the in-scope candidates.
  - Each is True only if every in-scope candidate has its header, its two fourth-root counts equal, and exactly its planned
    readings, and no member has capL2 ≥ 2 (P7′), or min(capW, capL2) ≥ 2 (P8′), in either route.
  - The call's other values are discarded, since they are computed on edited rows. The sealed read-out's predictions stand.
- **Priors**, set before Part F′ runs: P7′ 85%, P8′ 85%. P8 implies P8′, so P8′'s prior is at least the sealed 82%.

## 4. The verdict (§9, with P8′)

- **PROVED (room for two)** if P1–P3 and P9 hold and P8 is False: some member read, in scope or in the sealed partial
  record, has min(capW, capL2) ≥ 2.
- **NEGATIVE (scoped)** if P1–P3 and P9 hold, P8 is None and P8′ is True: no member over the in-scope candidates has room
  for two. The out-of-scope candidates stay OPEN, named by count and size.
- **OPEN** otherwise, until the cause is resolved and recorded.
- `read_out_scoped.py` decides this from `read_out.json` and P8′, and records it.

## 5. Control K13 and the timings (before this addendum)

- **K13** (`verification/control_k13.json`). The driver's path, on the sealed record's first candidate (out of scope),
  reproduces the sealed partial record's first 2,000 lines byte for byte. Both digests are
  `2bf113499eb40664ea2d62d978c6972f545f4b9ff9660645d7aa671ded79a72b`. It took 84 s. Only digests were compared.
- **Timing.** The driver's path on ten in-scope candidates with no fourth root, so with no reading: about 1 s each. Their
  header rows were checked for shape and discarded.
- **`--dry`:** the hash check and the aggregates of §2.
- **Nothing else** ran between the stop and this addendum: only the aggregate count (§0), `--dry`, the timing and K13.

## 6. What was seen before the read-out

- The Part F header's count (64,422 candidates) and the aggregates in §0 and §2 are Part L outcomes. They were seen, in
  aggregate, before the sealed read-out runs.
- They decide three predictions in advance:
  - P4 (some n ≥ 1) is True;
  - P5 (no n ≥ 2) is False;
  - P6 (none on m004) is False: m004 has 8 candidates.
- The read-out still computes P4–P6 from the records, but their values are not blind. The priors are unchanged.
- No Part F reading has been read, and nothing of Part L beyond these aggregates.

- **BANKED IDENTITY:** as sealed (§8). `identity.json` (12:08Z) holds for the eleven sealed files. Before it reads, the
  driver re-checks every line of `ARTIFACT_HASHES.txt`: the eleven sealed hashes, `run_f_scoped.py`, `read_out_scoped.py`,
  `control_k13.json` and this addendum.
- **PRIOR ART:** as sealed (§0). This addendum changes no mathematics. It scopes the population Part F reads.
