# ADDENDUM (2026-09-18, B1425) — the "timeout under load" was a wrong diagnosis, and raising the timeout was a wrong fix

This arc closed by naming the package's two remaining failures. One of those names is wrong and is corrected here.

**What this arc said.** §What the package now does on this bench: "one subprocess lock that passes alone and failed
once under the load of a 146-file run, whose timeout was tuned to an idle machine and is raised." The lock is
`tests/test_b1411_sm_harvest.py::test_b1355_geometry_is_exact`, and its timeout was raised 600 → 1800 s.

**What is actually true.** The lock is not load-sensitive and never was. Its script asked sympy to solve for the
commutant with `list(X.free_symbols)` as the unknowns — **a set, handed to something for which order changes the
answer's normalisation** — and then compared the result to one written-out dictionary. So it passes or fails with
`PYTHONHASHSEED`, at any load, on any machine. Measured in `frontier/B1425_the_flaky_lock_and_the_hollow_green/`
by pulling this arc's version of the script back out of git and running it beside the fixed one under eight seeds:

| version | passes on seeds | fails on seeds |
|---|---|---|
| as this arc left it | 4, 7 | 0, 1, 2, 3, 5, 6 |
| after B1425 | 0–7 | none |

**Why the wrong diagnosis was reachable.** Every observation fit it. The lock passed when run alone (seed 4 that
day), failed inside the full run, and an outside referee reported it passing on their machine. All three were luck,
and the raised timeout would have preserved a lock failing three runs in four while looking addressed.

**The distinguishing fact, for next time.** Flakiness has a *random* failing set; this has a *reproducible* one.
Running a suspect lock under several `PYTHONHASHSEED` values costs seconds and tells the two apart. Minted as
**E83**, swept over all 3 872 tracked `.py` files: 34 order-sensitive sites, five shipped locks among them, each
run under five seeds and stable.

**What still stands.** Everything else in this arc, including the other named failure (the six unrowed audit-seat
documents), the five referee defects and their fixes. The raised timeout is kept — it costs nothing — but it is no
longer the explanation.
