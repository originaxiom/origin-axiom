"""Failing control for B2014's decisive script (verification/walks.py, S1 and S2: the six moves as two commuting walks).

It reads walks.py's own text up to its S5 block (S5 does not use the walks; the cut is the arc's own lock's cut) and execs
it twice in a fresh namespace:
  (a) unchanged: the decisive check must PASS (so a failure in (b) is the change's, not the harness's);
  (b) with ONE deliberate change: the walks' definition, in both places it is written (S1 and S2), swaps R^-1 and R:
        W+ = L + X + R^-1 , W- = R + L^-1 + X^-1      (the claim: each walk is the orbit of one move under C)
     -> W+ = L + X + R    , W- = R^-1 + L^-1 + X^-1   (the six moves split by inversion instead)
     The six-move sum and W- = W+^T are unchanged by the swap, so what must fail is exactly the decisive content:
     the commutator [W+, W-] = 0, C W+ C^-1 = W+, and the sector law Pi_q W+ Pi_q = 3 w^-q Pi_q sigma Pi_q.
The decisive check is the arc's own (test_b2014_seats_rungs.py, test_s1_to_s3_rerun): the S1 line with zero commutator
and zero covariance defect on all four orbits, and in S2 one assignment to 1e-12 with the other off by more than 0.5.

Exit status: 1 = the control FAILS as it must (the decisive lines do not come out under the change; (a) passed);
             0 = the control did NOT fail (the decisive lines survive the change: the check could not see this fault);
             2 = harness error or crash (not a failing control).
Run beside the card, or anywhere inside the repository:  python3 -B control.py
(The repository root is found by walking up from this file and from the working directory, or taken from OA_ROOT.)"""

import sys as _sys, os as _os, traceback as _tb
def _crash(et, ev, tb):   # main's trial convention (P-885): a crash is never a failing control; it exits 3
    _tb.print_exception(et, ev, tb); print("CONTROL INVALID: the control raised; a crash is not a failing control")
    _sys.stdout.flush(); _os._exit(3)
_sys.excepthook = _crash
import contextlib, io, os, pathlib, re, sys, traceback

GOOD = 'Wp = P["L"] + P["X"] + P["Ri"]; Wm = P["R"] + P["Li"] + P["Xi"]'
BAD = 'Wp = P["L"] + P["X"] + P["R"]; Wm = P["Ri"] + P["Li"] + P["Xi"]'
S1_DECISIVE = ("[W+, W-] has 0 non-zero entries; C W+ C^-1 - W+ has 0; W+ + W- equals the six-move sum: True; "
               "W- = W+ transposed: True")


def find_root():
    cands = [os.environ.get("OA_ROOT")] if os.environ.get("OA_ROOT") else []
    for start in (pathlib.Path(__file__).resolve().parent, pathlib.Path.cwd().resolve()):
        cands += [str(p) for p in (start, *start.parents)]
    for c in cands:
        hits = sorted(pathlib.Path(c).glob("frontier/B2014_*/verification/walks.py"))
        if hits:
            return hits[0]
    raise SystemExit("harness error: the repository (frontier/B2014_*/verification/walks.py) was not found; set OA_ROOT")


def run(src, walks):
    """CHANGED 2026-11-27 (P-885): the text runs as a separate process beside walks.py (control_run.py), not exec'd
    here, since the intake's guard refuses exec; a run that does not exit 0 raises, and the harness reports a crash"""
    from control_run import run_changed
    rc, stdout, stderr = run_changed(walks, src)
    if rc != 0:
        raise RuntimeError("the run exited %d: %s" % (rc, (stderr.strip().splitlines() or [""])[-1]))
    return stdout


def decisive(out):
    """The arc's own S1/S2 check; returns a list of what fails (empty = the decisive claim comes out)."""
    lines = [re.sub(r"\s+\[\d+ s\]$", "", l) for l in out.splitlines()]
    s1 = [l for l in lines if l.startswith("S1")]
    bad = []
    n1 = sum(S1_DECISIVE in l for l in s1)
    if len(s1) != 4 or n1 != 4:
        bad.append("S1: the decisive line holds on %d of %d orbits" % (n1, len(s1)))
    s2 = [l for l in lines if l.startswith("S2")]
    nfail = 0
    for l in s2:
        a, b = [float(x) for x in re.findall(r"H\| = ([\d.e+-]+)", l)]
        q = int(re.search(r"q = (\d)", l).group(1)); plus = "W+" in l
        ok = (a < 1e-12 and b < 1e-12) if q == 0 else ((b < 1e-12 and a > 0.5) if plus else (a < 1e-12 and b > 0.5))
        nfail += not ok
    if len(s2) != 12 or nfail:
        bad.append("S2: the sector law (W+ = 3 w^-q, W- = 3 w^q times sigma's compression) fails on %d of %d lines" % (nfail, len(s2)))
    return bad, s1, s2


def main():
    walks = find_root()
    full = walks.read_text()
    src = full.split("# S5")[0]
    if src.count(GOOD) != 2:
        print("harness error: the walks' definition occurs %d times, expected 2 (walks.py changed?)" % src.count(GOOD))
        return 3
    print("control on %s (up to its S5 block)" % walks.relative_to(walks.parents[3]))
    base_bad, _, _ = decisive(run(src, walks))
    print("(a) unchanged:  the decisive check %s" % ("PASSES" if not base_bad else "FAILS: " + "; ".join(base_bad)))
    if base_bad:
        print("harness error: the unchanged script does not pass the decisive check, so (b) would prove nothing")
        return 3
    out = run(src.replace(GOOD, BAD), walks)
    bad, s1, s2 = decisive(out)
    print("(b) changed (W+ = L + X + R, W- = R^-1 + L^-1 + X^-1):")
    for l in s1 + s2:
        print("    " + l)
    if bad:
        print("CONTROL FAILS: as it must, " + "; ".join(bad))
        return 1
    print("CONTROL DID NOT FAIL: the decisive lines survive the change")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except SystemExit:
        raise
    except Exception:
        traceback.print_exc()
        print("CRASH (exit 3): not a failing control")
        sys.exit(3)
