#!/usr/bin/env python3
"""THE CHECK BUILT TO CATCH RUSTED INSTRUMENTS HAS ITSELF GONE BLIND: it looks for a
filename the corpus stopped using, so it runs green over 0.2% of the arcs.

Memo 188's pattern -- "the programme's characteristic failure is not error, it is entropy
in its own instruments" -- was not this bench's discovery.  The programme found it first,
in a specific technical form, at B1054 / Review 42, and built a check for it.  From
scripts/checks/instrument_freshness.py's own docstring:

    "an arc's lock asserts over frontier/BNNNN_*/results.json; results.json is a CACHE,
     written once at banking time and committed; later arcs edit the files the instrument
     measures -- that is what a consolidation window IS -- and nothing re-runs the
     instrument; so the lock validates the cache against itself and cannot see the drift.
     BY CONSTRUCTION."

    "two locks were red at HEAD, and nobody knew"  -- Review 42's governing finding.

That check selects its subjects by looking for arcs carrying BOTH `verify.py` AND
`results.json`.  This certificate measures how many arcs that is TODAY, and what the corpus
actually uses instead.

NOTHING IS EDITED HERE.  scripts/checks/ lives on main; this lane does not touch main.  The
finding is measured, the repair is specified exactly, and the decision is the owner's.

Gate 5: pure counting over the repository.  No measured physical value.
"""
import pathlib, collections, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
ARCS = [d for d in (ROOT / "frontier").glob("B*") if d.is_dir()]
print("=" * 78); print("1.  WHAT THE FRESHNESS CHECK CAN SEE"); print("=" * 78)
sys.path.insert(0, str(ROOT / "scripts" / "checks"))
try:
    import instrument_freshness as IF
    seen = list(IF.instruments())
    ok = True
except Exception as e:
    print("   could not import the check: %s" % e); seen = []; ok = False
print("   arcs in frontier/                                : %d" % len(ARCS))
print("   arcs the check selects (verify.py + results.json): %d" % len(seen))
print("   coverage                                         : %.1f%%"
      % (100*len(seen)/max(len(ARCS), 1)))
print("   the arcs it sees                                 : %s" % [s[0] for s in seen])

print(); print("=" * 78); print("2.  WHAT THE CORPUS ACTUALLY USES"); print("=" * 78)
names = collections.Counter()
for d in ARCS:
    for f in d.iterdir(): names[f.name] += 1
for k, v in names.most_common(16):
    print("   %-28s %4d" % (k, v))

print(); print("=" * 78); print("3.  THE COVERAGE GAP, MEASURED"); print("=" * 78)
RUNNER = re.compile(r"^(verify|probe|verdict|compute|run|check|main)\.py$|^b\d+.*\.py$")
RESULT = re.compile(r"^(results|.*_results|.*_out|output)\.(json|txt)$")
has_runner, has_result, has_both, has_dir = set(), set(), set(), set()
for d in ARCS:
    fs = [f.name for f in d.iterdir()]
    r = any(RUNNER.match(f) for f in fs)
    o = any(RESULT.match(f) for f in fs)
    if r: has_runner.add(d.name)
    if o: has_result.add(d.name)
    if r and o: has_both.add(d.name)
    if (d / "verification").is_dir(): has_dir.add(d.name)
print("   arcs with SOME runnable script            : %d" % len(has_runner))
print("   arcs with SOME committed result artefact  : %d" % len(has_result))
print("   arcs with BOTH (a widened selector)       : %d" % len(has_both))
print("   arcs with a verification/ directory       : %d" % len(has_dir))
print("   union of 'has both' and 'has verification/': %d" % len(has_both | has_dir))
print()
print("   the check sees %d of those %d  ->  it is blind to %d arcs that carry exactly the"
      % (len(seen), len(has_both | has_dir), len(has_both | has_dir) - len(seen)))
print("   structure B1054 warned about.")

print(); print("=" * 78); print("4.  THE REPAIR, SPECIFIED (not applied -- this lane does not touch main)")
print("=" * 78)
print("""   scripts/checks/instrument_freshness.py selects on the literal pair
   (verify.py, results.json).  The corpus moved to probe.py (%d), verdict.py (%d),
   compute.py (%d), per-arc bNNNN_*.py, per-arc *_results.json, and a verification/
   directory (%d).  Widening the selector to the patterns used in section 3 takes the
   check from %d arcs to %d.

   TWO THINGS MUST SURVIVE THE WIDENING, both already true of the current file and both
   easy to lose:
     * it is NON-MUTATING -- it snapshots every artefact and restores it unconditionally,
       because running an instrument rewrites its own results and a diagnostic must not
       edit its subject;
     * it is wired as a TEST, not a per-push gate, because it costs minutes.
   A widened sweep will cost proportionally more and should be sampled or sharded rather
   than run whole on every suite pass."""
      % (names.get("probe.py", 0), names.get("verdict.py", 0), names.get("compute.py", 0),
         len(has_dir), len(seen), len(has_both | has_dir)))
print("""
=============================================================================
INTERPRETATION (labelled).

This is memo 188's pattern in its purest available form, and the programme gets the credit
for finding the pattern first: B1054 named it, built a check, and wired it into the suite.
What happened next is the pattern applied to the check itself.  The corpus renamed its
instruments; the check kept looking for the old name; it still runs, still passes, and now
reports on two arcs out of eleven hundred.

A green check with 0.2% coverage is worse than no check, because it answers the question
"is anything stale?" with silence that reads as no.

Nothing here says the hidden arcs ARE stale -- that is the next measurement, and it needs
the widened selector plus the non-mutating snapshot discipline the current file already
has.  What is established is only that nobody can currently see.""")
