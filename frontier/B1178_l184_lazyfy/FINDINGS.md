# B1178 — L184 EXECUTED

**Verdict**: `OPEN` · **instrument**: true · **creates_law**: false
**Banked**: 2026-08-27 (`65928f29`) · **This document authored**: 2026-08-29 (R52-4 discharge, B1207)

> **Provenance of this document.** The arc banked its verdict, its results file and its
> verification artifacts, but no findings document -- the gap B817's writer-safety gate caught in
> the first full OA_SLOW run (R52-4, 2026-08-29). What follows is authored **from this arc's own
> banked record**: `arc_verdict.json` is primary, with `b1178_results.json` and `verification/` beside it.
> Nothing is supplied from memory and no computation is re-narrated that the record does not
> carry -- the exact mirror of B1176's thirteen retro `arc_verdict.json` files, where FINDINGS was
> the primary and the verdict the missing half. Section 1 is the banked claim, segmented at its
> own enumeration; section 2 lists the artifacts that certify it.


## 1. The finding, as banked

L184 EXECUTED (the collection lazy-fy; the E50 cost class's root fix, promised as 'the named next sitting' and delivered same-day). THE DIAGNOSIS WAS SURGICAL, NOT STRUCTURAL: the per-file sweep (1063 files) found TWO files carrying the whole cost -- test_b371_two_state_sector.py at 156.95 s (a module-level REPORT=run() executing ~157 s of exact computation AT COLLECTION -- 88% of the suite's entire 178.41 s collect) and test_cc2_r5_adopted.py at 36.05 s (a 300-line module-level lock script); everything else <= 7.7 s (~4.3 s interpreter+conftest baseline). THE FIX (the E50 remedy pattern, now named THE CACHED-RUNNER MOVE): each body moved into a functools.lru_cache'd _report()/_run() with the frontier-engine import DEFERRED inside it -- the compute runs once at first TEST EXECUTION (total cost unchanged when the tests actually run; ZERO at collection). OUTCOMES PRESERVED: both files 5/5 pass post-fix (277.88 s execution = the same compute, now paid where it belongs). THE CERTIFIED WIN: full-suite collection 178.41 s -> 15.14 s (12x; 5587 tests) -- the fast lane's collection tax is gone and the full certificate-of-record suite is routinely collectable. The B1177 measurements addendum landed in the same sitting (the per-file table committed; the OA_SLOW first-ever run continues -- launched, not yet complete, no phantom green). Instrument arc; test-outcome-preserving by construction and by the 5/5 re-run; Gate 5 clean.

## 2. The certifying record

- `arc_verdict.json`
- `b1178_results.json`
- `verification/reproduce.sh`

## 3. Status at authoring

The verdict field is authoritative and unchanged: `OPEN`. This document does not re-adjudicate it; it makes the arc readable without opening its JSON, which is the whole function the missing file was performing badly.
