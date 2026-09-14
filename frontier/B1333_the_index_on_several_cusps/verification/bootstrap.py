"""BOOTSTRAP -- make this directory runnable from a clean checkout.  (R57-4, E80)

THE PROBLEM.  Fifteen scripts here open with `sys.path.insert(0,'/tmp/sweep')` and read
`/tmp/sweep/covcache.json` by absolute path.  /tmp does not survive a container, so the
directory that certifies B1333's 38 070 sectors could not re-run itself: everything is
committed, correct, and points outward.  That is ERROR_LEDGER class **E80**.

WHY THIS IS A NEW FILE AND NOT AN EDIT.  The scripts beside it are the record of what was
actually run.  Rewriting their paths would make the directory reproducible by changing the
artifact that says what happened -- so the repair is ADDITIVE: this script recreates the
environment those scripts expect, and not one banked line moves.

USAGE
    python bootstrap.py            # modules + the degree-10 cache (minutes)
    python bootstrap.py 2 13       # the full range B1333 actually used (much longer)

It is idempotent: re-running skips covers already cached.

VERIFIED FROM AN EMPTY /tmp/sweep (2026-09-14): 22 modules copied, degree-10 cache rebuilt,
**30 of 32** chiral multi-cusped covers recognised by `recogmc.exact_rho`. The two that do not
recognise are the known case B1333's own addendum documents (`d9_5`, `d10_6`, `d10_8` there),
for which the fallback normalisation `recogmc2.exact_rho2` exists; this bootstrap does not
invoke it, so a full reproduction of B1333's 54 covers needs that second pass. Said here
rather than left for the next seat to discover.

The first run of this test was CONTAMINATED -- /tmp/sweep already existed, populated earlier in
the same session -- and reported 54 of 54. That is E78's shape (a test served by the state it
was meant to create), caught by deleting the directory and running again. The numbers above are
from the clean run.
"""
import os, shutil, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SWEEP = "/tmp/sweep"                      # the path the banked scripts hardcode
lo, hi = (int(sys.argv[1]), int(sys.argv[2])) if len(sys.argv) > 2 else (10, 11)

os.makedirs(SWEEP, exist_ok=True)
copied = 0
for f in sorted(os.listdir(HERE)):
    if f.endswith(".py") and f != os.path.basename(__file__):
        shutil.copy2(os.path.join(HERE, f), os.path.join(SWEEP, f)); copied += 1
print(f"bootstrap: copied {copied} modules -> {SWEEP}")

cache = os.path.join(SWEEP, "covcache.json")
print(f"bootstrap: regenerating the cover cache for degrees {lo}..{hi-1}")
print("           (PSLQ recognition per cover; this is the slow step, and it is the")
print("            reason the cache existed in the first place)")
r = subprocess.run([sys.executable, os.path.join(SWEEP, "cache_covers.py"), str(lo), str(hi)],
                   cwd=SWEEP)
if r.returncode != 0:
    sys.exit(f"bootstrap FAILED: cache_covers.py returned {r.returncode}")
if not os.path.exists(cache):
    sys.exit("bootstrap FAILED: no covcache.json was written")
size = os.path.getsize(cache)
print(f"bootstrap: {cache} present, {size} bytes")
print("bootstrap: OK -- the banked scripts in this directory can now be run from here.")
