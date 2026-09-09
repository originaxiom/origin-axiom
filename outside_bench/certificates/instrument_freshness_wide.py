#!/usr/bin/env python3
"""THE WIDENED FRESHNESS SWEEP -- memo 189's repair, built and RUN, on this lane.

scripts/checks/instrument_freshness.py (B1054 / Review 42) catches the failure it names in
its own docstring: a lock asserts over a committed `results.json` CACHE, later arcs edit
what the instrument measures, nothing re-runs it, "so the lock validates the cache against
itself and cannot see the drift.  BY CONSTRUCTION."  Review 42's governing finding was
"two locks were red at HEAD, and nobody knew".

Memo 189 measured that the check now selects on the literal pair (verify.py, results.json)
while the corpus moved to probe.py / verdict.py / compute.py / per-arc scripts and
per-arc result files -- so it sees 2 arcs out of the 152 carrying that structure.

THIS IS THE WIDENED SELECTOR, run here rather than on main.  Everything that makes the
original safe is preserved and, where possible, strengthened:

  * NON-MUTATING, and more conservatively than the original: the original snapshots the
    single results file; this snapshots EVERY regular file in the arc directory and
    restores all of them unconditionally, because a widened selector runs scripts whose
    write-set is not known in advance.  Its own docstring records why this matters -- the
    first version of the original destroyed B946's four cached values and "only git still
    had them".
  * A DIAGNOSTIC, never a gate.  Per-instrument timeout, and a cap, so a sweep can be
    sampled or sharded rather than run whole.
  * REPORTS, never guesses.  The verdict-reading helper is imported from the original
    rather than re-implemented, so the three live spellings (all_pass / all_ok / a checks
    map) are read exactly as the corpus reads them.

VERDICT KINDS (same vocabulary as the original)
  STALE-GREEN  the committed cache said green and the live run is red   <- the target
  RED          the instrument was already recording red
  KEY-LOSS     re-running DROPS keys the committed file had
  CRASH        the instrument could not run at all (includes timeout)
  NO-VERDICT   the result file records no pass/fail state, so no lock over it can mean
               anything.  NOT A DEFECT on its own -- the upstream docstring says so: B943
               and B946 record computed VALUES and their locks assert over those values.
               It is reported, never counted as a failure.
  HARNESS      the run failed from the repository root and succeeded from the arc's own
               directory -- the finding belongs to the sweep, not to the arc

Usage:  python3 instrument_freshness_wide.py [--limit N] [--timeout S] [--offset K]
Gate 5: no measured physical value; this only re-runs the corpus's own scripts.
"""
import sys, os, re, json, glob, pathlib, subprocess, argparse

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts" / "checks"))
from instrument_freshness import _all_pass as _all_pass_upstream   # the corpus's own reader

# FIRST FINDING OF THE WIDENING, recorded here because it is upstream's, not ours:
# _all_pass assumes the results file's top-level JSON is a DICT (it calls R.get). Some
# arcs in the widened set store a top-level LIST, and upstream raises AttributeError on
# them. The narrow selector never reached those files, so the bug has never fired. It is
# guarded here -- a diagnostic must not crash on its subject -- and counted, so the fix
# can be made where it belongs.
READER_CRASH = []
def _all_pass(path):
    try:
        return _all_pass_upstream(path)
    except Exception as e:
        READER_CRASH.append((path, type(e).__name__))
        return None

RUNNER = re.compile(r"^(verify|probe|verdict|compute|run|check)\.py$|^b\d+[_a-z0-9]*\.py$")
RESULT = re.compile(r"^(results|.*_results|.*_out|output)\.(json|txt)$")

def instruments():
    """(arc, runner_path, result_path) for every arc carrying both, deduped by number."""
    seen = set()
    for d in sorted(glob.glob(str(ROOT / "frontier" / "B*"))):
        m = re.match(r"B(\d+)_", os.path.basename(d))
        if not m or not os.path.isdir(d): continue
        n = int(m.group(1))
        if n in seen: continue
        fs = sorted(os.listdir(d))
        runs = [f for f in fs if RUNNER.match(f)]
        outs = [f for f in fs if RESULT.match(f)]
        if not runs or not outs: continue
        # prefer a runner/result pair sharing a stem, else the first of each
        pick = None
        for r_ in runs:
            st = r_[:-3]
            for o in outs:
                if o.startswith(st): pick = (r_, o); break
            if pick: break
        if not pick: pick = (runs[0], outs[0])
        seen.add(n)
        yield n, os.path.join(d, pick[0]), os.path.join(d, pick[1])

def snapshot(dirpath):
    S = {}
    for f in sorted(os.listdir(dirpath)):
        p = os.path.join(dirpath, f)
        if os.path.isfile(p):
            try: S[p] = open(p, "rb").read()
            except Exception: pass
    return S

def restore(S):
    for p, b in S.items():
        try:
            if not os.path.isfile(p) or open(p, "rb").read() != b:
                open(p, "wb").write(b)
        except Exception: pass

def sweep(limit, timeout, offset):
    rows = list(instruments())
    total = len(rows)
    rows = rows[offset:offset+limit]
    out = []
    for n, v, r in rows:
        d = os.path.dirname(v)
        before = _all_pass(r)
        S = snapshot(d)
        try: keys_before = set(json.loads(open(r, encoding="utf-8").read()))
        except Exception: keys_before = set()
        kind, detail = None, ""
        # THE CONTROL THAT HAD TO EXIST FIRST.  The upstream sweep runs with cwd=ROOT.
        # An arc script that expects to run from its OWN directory would then fail for a
        # reason that is the harness's, not the arc's -- and a diagnostic that manufactures
        # its own findings is worthless (memo 164, read the other way round: an instrument
        # FAILING is not the same as the subject being broken).  So every failure is retried
        # from the arc directory, and a recovery is reported as HARNESS, not as a defect.
        def run(cwd):
            try:
                pr = subprocess.run([sys.executable, os.path.abspath(v)], cwd=cwd,
                                    capture_output=True, text=True, timeout=timeout)
                return pr.returncode, pr, None
            except subprocess.TimeoutExpired:
                return None, None, "timed out after %ds" % timeout
            except Exception as e:
                return None, None, str(e)[:80]
        rc, p, err = run(ROOT)
        cwd_used = "ROOT"
        if err or rc != 0:
            rc2, p2, err2 = run(os.path.dirname(os.path.abspath(v)))
            if not err2 and rc2 == 0:
                rc, p, err, cwd_used = rc2, p2, None, "ARCDIR"
        if err:
            restore(S); out.append((n, "CRASH", err)); continue
        try: keys_after = set(json.loads(open(r, encoding="utf-8").read()))
        except Exception: keys_after = set()
        after = _all_pass(r)
        lost = keys_before - keys_after
        restore(S)                                   # ALWAYS, before any reporting
        if cwd_used == "ARCDIR":
            kind, detail = "HARNESS", "fails from repo root, runs clean from its own directory"
        elif rc != 0 and after is None:
            kind, detail = "CRASH", "exit %d: %s" % (rc, (p.stderr or "").strip().splitlines()[-1][:90] if p.stderr.strip() else "")
        elif before is True and after is False:
            kind, detail = "STALE-GREEN", "cache green, live run red"
        elif before is False:
            kind, detail = "RED", "was already red"
        elif lost:
            kind, detail = "KEY-LOSS", "re-run drops %d key(s): %s" % (len(lost), sorted(lost)[:4])
        elif before is None and after is None:
            kind, detail = "NO-VERDICT", "no pass/fail field; exit %d" % rc
        if kind: out.append((n, kind, detail))
    return out, total, len(rows)

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=25)
    ap.add_argument("--timeout", type=int, default=90)
    ap.add_argument("--offset", type=int, default=0)
    a = ap.parse_args()
    bad, total, ran = sweep(a.limit, a.timeout, a.offset)
    print("=" * 78)
    print("WIDENED FRESHNESS SWEEP")
    print("=" * 78)
    print("   arcs the WIDENED selector sees : %d" % total)
    print("   arcs re-run in this pass       : %d  (offset %d, timeout %ds)"
          % (ran, a.offset, a.timeout))
    print("   findings                       : %d" % len(bad))
    if READER_CRASH:
        print("   *** upstream _all_pass raised on %d result file(s) -- top-level JSON is not"
              % len(READER_CRASH))
        print("       a dict.  Guarded here; the fix belongs in scripts/checks/. e.g. %s"
              % os.path.relpath(READER_CRASH[0][0], ROOT))
    print()
    for n, k, d in bad: print("   B%-6d %-12s %s" % (n, k, d))
    if not bad: print("   (every instrument in this shard re-ran consistent with its cache)")
    print()
    print("   NON-MUTATING: every regular file in each arc directory was snapshotted before")
    print("   the run and restored afterwards, unconditionally.")
