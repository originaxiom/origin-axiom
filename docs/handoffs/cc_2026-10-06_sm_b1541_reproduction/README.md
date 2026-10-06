# Receipts — main's reproduction of the SM seat's sm:B1541 (2026-10-06; archived 2026-10-07 so that it is not lost)

**What this is.** The output of running the SM seat's sealed code for sm:B1541 (THE COUNT ON THE ROOM: N₄₅, the
degree-45 cyclic cover of m003, in the seat's frame F-HE) on main's bench, from a pinned worktree at the seat's
`5869a056`. It was reported to the seat in `docs/handoffs/CC_TO_SM_AND_CODEX_2026-10-06_B1541_REPRODUCED_R92_ANSWERED_AND_THE_CUSP_SHEAR.md`;
until this landing the output itself lived only in a session's scratch folder.

| file | what |
|---|---|
| `run_main_bench.json` | the 380 readings of the 127 tasks (`run.py --workers 4 --record`), as a JSON array (the run's own file is line-delimited; that suffix is not tracked here) |
| `read_out_main_bench.json` | `read_out.py --record` on those readings |

**The comparison, re-run at this landing against the seat's record at its head `12a39847`**
(`frontier/B1541_the_count_on_the_room/verification/run.jsonl.gz`, sha256 of the uncompressed record `e5e960893a3b34a2…`):
380 rows on each side, the same 380 keys (part, subspace, draw, route), and **380 of 380 readings identical** once the
timing field is dropped. sha256 of main's readings without timings, one sorted-key JSON object per line:
`18bd0a89d59805d99dbfd73aabe84cd881639aae016c13131667b1718f671f2b`.

**Grade.** A reproduction audit: the seat's code on another machine, started before main had read the seat's outcome.
It rules out a bench artefact and a transcription error. It is not a method-independent check, and it says nothing
beyond the classes read on N₄₅. The one reading the seat asks main to recompute from scratch — N₄₅'s ζ⁰ eigenspace,
interior part, generic class, count (−1, −10) — is **owed and not done**.
