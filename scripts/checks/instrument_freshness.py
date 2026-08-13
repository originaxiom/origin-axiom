"""Re-run every arc instrument and report the ones whose committed `results.json` is a LIE.

WHY THIS EXISTS (B1054, Review 1). At `5b26e51` the branch tip carried **six red instruments and a
green suite**. Proven on a pristine worktree: `pytest` returned 46 passed / 0 failed over those six
arcs' locks, while re-running the six `verify.py` scripts turned every one of them red.

The mechanism is structural, not sloppiness:

  * an arc's lock (`tests/test_bNNNN_*.py`) asserts over `frontier/BNNNN_*/results.json`;
  * `results.json` is a CACHE, written once at banking time and committed;
  * later arcs edit the files the instrument measures -- that is what a consolidation window IS --
    and nothing re-runs the instrument;
  * so the lock validates the cache against itself and cannot see the drift. **By construction.**

That is Review 42's governing finding -- *"two locks were red at HEAD, and nobody knew"* -- in its
third and worst form. B1041 found it recurring within two days of Review 42. This is the recurrence
after that, and the reason it kept recurring is that every previous repair fixed the RED LOCKS
rather than the fact that a lock cannot see its own instrument.

WHAT IT COSTS, measured, because a check nobody runs is not a check: **~5m20s for 26 instruments**
on this container. That is too slow for a per-push gate (gates run at every bank) and proportionate
inside the full suite, which already runs ~48 minutes and is the surface the failure hid behind.
So it is wired as a test, not a gate. The per-push version is registered, not pretended.

NON-MUTATING, DELIBERATELY. Running an instrument rewrites its `results.json`, so this module
snapshots every file first and puts it back unconditionally -- findings are REPORTED, never
written. The first version did leave the regenerations in place, and that was wrong twice over:
it DESTROYED B946's four cached values (only git still had them), and because this runs inside
the suite alongside locks that read the same files, a mutating sweep would make their results
depend on TEST ORDER -- the E39 shape wearing a different hat. A diagnostic must not edit its
subject.
"""
import glob
import json
import os
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
TIMEOUT = 900


def instruments(lo=0, hi=10 ** 9):
    """(arc_id, verify_path, results_path) for every arc carrying BOTH, deduped by number."""
    seen = set()
    for d in sorted(glob.glob(str(ROOT / "frontier" / "B*"))):
        m = re.match(r"B(\d+)_", os.path.basename(d))
        if not m:
            continue
        n = int(m.group(1))
        if n in seen or not (lo <= n <= hi):
            continue
        v, r = os.path.join(d, "verify.py"), os.path.join(d, "results.json")
        if os.path.isfile(v) and os.path.isfile(r):
            seen.add(n)
            yield n, v, r


def _all_pass(results_path):
    """True / False / None -- None when the instrument records no verdict field at all.

    THREE spellings are live in this corpus and all three are read here: `all_pass` (the window's
    convention), `all_ok` (B1026), and a bare `checks` map with per-check `pass` flags. A results
    file with none of them is not a defect -- B943 and B946 record computed VALUES and their locks
    assert over those values rather than over a self-reported flag -- so the caller falls back to
    the instrument's exit code rather than guessing.
    """
    try:
        R = json.loads(pathlib.Path(results_path).read_text(encoding="utf-8"))
    except Exception:
        return None
    for key in ("all_pass", "all_ok"):
        if key in R:
            return bool(R[key])
    if isinstance(R.get("checks"), dict) and R["checks"]:
        return all(v.get("pass") for v in R["checks"].values())
    return None


def sweep(lo=0, hi=10 ** 9):
    """[(arc, kind, detail)] -- empty when every instrument re-runs green.

    kind is one of:
      STALE-GREEN  the committed cache said green and the live run is red -- the failure this
                   module exists to catch;
      RED          the instrument was already recording red;
      KEY-LOSS     re-running DROPS keys the committed file had -- the lock asserts over data
                   the instrument cannot produce. The original is restored, never destroyed;
      CRASH        the instrument could not run at all;
      NO-VERDICT   the results file records no pass/fail state, so no lock over it can mean
                   anything (reported, never guessed).
    """
    bad = []
    for n, v, r in instruments(lo, hi):
        before = _all_pass(r)
        # SNAPSHOT FIRST. Re-running an instrument OVERWRITES its results file, and B946 proved
        # that is not always safe: its `results.json` carried four keys the script has not
        # produced since B963, so the first regeneration silently DESTROYED them and only git
        # still had the values. A tool built to expose stale caches must not eat the evidence --
        # so the original is restored whenever a re-run loses keys, and the loss is REPORTED.
        snapshot = pathlib.Path(r).read_text(encoding="utf-8")
        try:
            keys_before = set(json.loads(snapshot))
        except Exception:
            keys_before = set()
        try:
            p = subprocess.run([sys.executable, v], cwd=ROOT, capture_output=True, text=True,
                               timeout=TIMEOUT)
        except subprocess.TimeoutExpired:
            bad.append((f"B{n}", "CRASH", f"timed out after {TIMEOUT}s"))
            continue
        regenerated = pathlib.Path(r).read_text(encoding="utf-8")
        try:
            lost = keys_before - set(json.loads(regenerated))
        except Exception:
            lost = set()
        after = _all_pass(r)
        # ALWAYS RESTORE. This sweep is a DIAGNOSTIC, and a diagnostic that edits the thing it
        # inspects is a worse defect than the one it reports:
        #   * it destroyed B946's four values on its first run (only git still had them);
        #   * and it runs inside the suite, where OTHER locks read these same files -- so a
        #     mutating sweep makes their results depend on TEST ORDER, which is the E39 shape
        #     wearing a different hat (a lock whose answer depends on something invisible to it).
        # Reading the verdict needs the regenerated file, so the read happens above and the
        # original goes back here, unconditionally. The findings are REPORTED, never written.
        pathlib.Path(r).write_text(snapshot, encoding="utf-8")
        if lost:
            bad.append((f"B{n}", "KEY-LOSS",
                        "re-running drops " + ", ".join(sorted(lost))
                        + " -- the lock asserts over data the instrument cannot produce"))
            continue
        if after is None:
            # No self-reported verdict: the results file holds computed VALUES and the arc's lock
            # asserts over those. The instrument's own exit code is then the only honest signal.
            if p.returncode != 0:
                bad.append((f"B{n}", "CRASH",
                            f"exit {p.returncode}; " + (p.stderr.strip()[-200:] or "no stderr")))
        elif after is False:
            kind = "STALE-GREEN" if before is True else "RED"
            # Read the failing check names out of the REGENERATED text held in memory. The file on
            # disk is the restored original by now, and reading it here would report the cache's
            # OLD verdict -- reintroducing the exact confusion this module exists to end.
            try:
                fails = [k for k, x in json.loads(regenerated).get("checks", {}).items()
                         if not x.get("pass")]
            except Exception:
                fails = []
            bad.append((f"B{n}", kind, ", ".join(fails[:4]) or (p.stderr.strip()[-200:])))
    return bad


if __name__ == "__main__":
    lo = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    hi = int(sys.argv[2]) if len(sys.argv) > 2 else 10 ** 9
    out = sweep(lo, hi)
    n = len(list(instruments(lo, hi)))
    if not out:
        print(f"instrument-freshness: ok ({n} instruments re-run, all green)")
    else:
        print(f"instrument-freshness: {len(out)} of {n} instruments do NOT re-run green --")
        for arc, kind, detail in out:
            print(f"    {arc:8} {kind:12} {detail}")
    raise SystemExit(1 if out else 0)
