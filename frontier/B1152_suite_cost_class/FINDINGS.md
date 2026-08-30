# B1152 — THE COST FAILURE CLASS (harvest of cc3's B8139) + the fast lane: a lock never *reached* catches nothing — main audited clean, and the suite given an inner-loop lane

**Status: banked (frontier). Verdict PROVED. A method/tooling bank harvesting cc3's B8139
(`paper/structure-genesis-first` `1f455266`, integrate-don't-merge): the main-band audit + the
suite-runnability remedy. No mathematics; Gate 5 n/a. cc3 credited. Lock
`tests/test_b1152_suite_cost_class.py`.**

## The finding harvested — a new failure class: "cost"

cc3, while banking B8139, named a failure class the usual defences are blind to. Not a missing check,
not a silent pass, not a weakened assertion — **cost**: a lock that *exists, works, and was never
weakened*, but is **never reached** because the suite is too expensive to run. Their suite (1038
files / 4528 tests) takes **421 s just to collect**, and two background runs were killed by timeout.
The concrete drift it let through: cc3 stopped writing `FINDINGS.md` at B8110 and it ran **unbroken
for 16 arcs / 5 days** — every one caught by a lock that never got to run.

> "A killed run is not a run that told you nothing." — cc3 surfaced it only by reading a killed
> run's captured partial output rather than discarding it. (The same discipline saved this seat's C4
> read this session — the finisher's partial output *was* the verdict.)

*[B8140 correction (cc3, adopted 2026-08-26): cc3's first framing gave a specific "killed at 73%,
five failures already emitted" for that run; it is **withdrawn** — the captured log was a truncated
three-line fragment, so the numbers were never sound and the coverage they implied is retracted. The
**principle** (a killed run's partial output is still evidence) stands; the numbers do not.]*

## The main-band audit — main is clean; the difference is main's suite gets *run*

Audited all **1043** `arc_verdict.json` on main for the four drift classes cc3 found in their band:

| drift class | main | note |
|---|---|---|
| missing FINDINGS | **clean** | B519 (RETRACTED) records its result in `VERDICT.md` — a convention already locked (`test_b810_wave1` accepts either; `test_b826/b819/b817/b818`). Not drift. |
| `instrument` not bool | **clean** | 0 arcs carry it as a string |
| verdict off-vocabulary | **clean** | 0 outside {PROVED, NEGATIVE, OPEN, RETRACTED} |
| unrouted NEGATIVE arcs | **clean** | 0 (B1151 routed this cycle) |

cc3's drift was **band-local**. Main held — **because main's suite gets run each bank while cc3's
does not complete.** But main is on the same trajectory: its collection alone is already **>120 s**
(a `--co` run timed out at 120 s this session), a full run is ~22 min, and this seat had to green a
tree by *input-change analysis* rather than a clean re-run this very cycle. Preventive, not just
curative.

## The cost, diagnosed

- Collecting **one** file: **1.17 s** — fixed conftest/plugin overhead is low.
- Collecting the **whole** suite: **>120 s** — so the cost is **import-time work spread across many
  test modules** (module-level computation), not fixed overhead.
- **Mechanism:** pytest imports *every* test module before running any test (documented in
  `tests/conftest.py`, the R22-4 module-level-dps sweep). Module-level compute therefore runs at
  **collection**, and its sum is the collection cost. **`-m "not slow"` cannot help collection** —
  the modules still import.

## The remedy — the inner-loop lane

- **The `slow` marker** registered in `tests/conftest.py` (`pytest_configure`) — kills the
  `UnknownMark` warning and lets `-m "not slow"` skip expensive tests at *execution* time.
- **`scripts/affected_tests.py`** — a **conservative** changed-file selector: it maps the
  working-tree (or a diff range) to only the affected test files, so pytest collects a handful in
  seconds. **Its safety is its fallback** — any change it cannot bound (scripts code, `conftest`,
  unknown paths) runs the **FULL** suite; it is only ever a *superset-or-full* selector, never a
  false green. Validated: a typical bank (a frontier arc + `CHANGELOG`/`PROGRESS`/`RELAY` + views)
  maps to **49** test files — including the corpus-aggregate + gate tests (`test_repo_gates`,
  `test_b833` negative-routing — *the very test that caught B1151's routing this cycle*) — not the
  full ~140.
- **`scripts/run_suite.sh`** gains `--changed` (the selector) and `--fast` (`-m "not slow"`);
  `--serial`/full remain the certificate of record.

## Honest fences

Method/tooling only — no mathematics. **The full suite remains the certificate of record** (the
ARBITER RULE / B1018 stands); the fast lane is the inner loop, not a replacement for the pre-commit
certificate. The **root** collection cost is *not* fixed here — the selector *avoids* it for the
inner loop; a lazy-fy of the slowest module-level importers (moving compute into fixtures) so even
the full suite collects fast is the **named follow-up** (L-registered). cc3 credited (the finding +
the name).

**⚠ Surfaced to the owner, not touched:** cc3's B8139 also flags that `SUBMISSION_METADATA.md`
carries the owner's personal email on a tracked, dual-pushed surface, against a standing lock that
keeps email off tracked surfaces — supplied deliberately for the arXiv submission on 2026-08-15. It
is on cc3's branch and is the owner's decision (removing it could break the submission); recorded
here so the conflict is a decision seen, not one buried in a commit body.
