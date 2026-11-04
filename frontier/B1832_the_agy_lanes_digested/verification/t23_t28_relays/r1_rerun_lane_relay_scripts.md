# r1 -- the lane's relay scripts re-run from a scratch copy (REPRODUCED grade, not VERIFIED)

Source: `origin/agy/audit-2026-11-02` @ 18c607040, `relays/agy_audit_2026_11_02/`. Scratch tree: the branch's `src/` and
`relays/agy_audit_2026_11_02/` (git archive) beside symlinks to main's `frontier/`, `scripts/`, `docs/` (the branch changed none
of the files these scripts read). Runs single-threaded, `PYTHONDONTWRITEBYTECODE=1`, `python3 -I`, 2026-11-04.

| script | runtime | stdout vs committed `*_out.txt` | JSON vs committed `*_results.json` |
|---|---|---|---|
| `independent_core_recompute.py` | 0.2 s | identical | identical |
| `verify_ckm_inversion.py` | 3 s | identical | identical |
| `hostile_referee_audit.py` | 46 s | (no committed stdout; the run's stdout was written to scratch and not read: it prints firewalled lines) | 521 leaves identical, 0 differing (only `audit_metadata/runtime_seconds`) |

The referee script imports `origin_axiom.toe_closure` and `sm_19_gate` (areas 8, 9), whose outputs include firewalled
quantities; the comparison above was made leaf-by-leaf by a script that prints paths only, never values.
