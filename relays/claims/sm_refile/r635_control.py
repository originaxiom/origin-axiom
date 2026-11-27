#!/usr/bin/env python3
"""The failing control of the SM seat's P-635 card.

The sealed script reads the frame's Q8 holonomies (QI, QJ) from main's module
frontier/B1723_the_golden_valley/verification/b1656_funcs.py. This control builds a planted main root in a temporary
directory: a copy of that one module with ONE deliberate change, QJ replaced by the pure unit quaternion
(3/5) QI + (4/5) QJ, so the pair is irreducible but not Q8 (it does not anticommute; its commutator is not -1). The
sealed script runs UNCHANGED on that root, through r635_decisive.run_sealed, and the claim's check is applied.
For such a pair the boundary-held classes are 2 (as the sealed plant P2 shows for a generic pair), so the check must
reject it: "boundary held H1_par = 0" cannot come out.

    python3 relays/claims/sm_refile/r635_control.py
Exit 1 with "CONTROL FAILS:" when the check rejects the planted input (the expected outcome); 0 with
"CONTROL DID NOT FAIL:" when it accepts it; 3 with "CONTROL INVALID:" on any crash or a run that does not complete.
Nothing is written into the repo."""
import pathlib
import shutil
import sys
import tempfile

OLD = 'QJ = np.array([[0, 1], [-1, 0]], dtype=complex)'
NEW = 'QJ = np.array([[0.6j, 0.8], [-0.8, -0.6j]], dtype=complex)'
MOD = pathlib.Path("frontier") / "B1723_the_golden_valley" / "verification" / "b1656_funcs.py"


def main():
    sys.dont_write_bytecode = True
    import r635_decisive as D
    root = D.repo_root()
    if root is None:
        return 3, "CONTROL INVALID: the repo root was not found"
    src = (root / MOD).read_text(encoding="utf-8")
    if src.count(OLD) != 1:
        return 3, "CONTROL INVALID: the planted edit did not apply (%d matches)" % src.count(OLD)
    tmp = tempfile.mkdtemp(prefix="r635_plant_")
    try:
        fake = pathlib.Path(tmp) / "main"
        (fake / MOD).parent.mkdir(parents=True)
        (fake / MOD).write_text(src.replace(OLD, NEW), encoding="utf-8")
        R, msg = D.run_sealed(fake)
        if R is None:
            return 3, "CONTROL INVALID: " + msg
        g0 = R["G0"]
        if g0.get("anticommute") is not False:
            return 3, "CONTROL INVALID: the plant did not reach the script (the pair still anticommutes)"
        lines, holds, bad = D.decisive(R)
        if holds:
            return 0, "CONTROL DID NOT FAIL: the check accepted a non-Q8 pair"
        return 1, "CONTROL FAILS: the check rejects the planted non-Q8 pair (%s)" % "; ".join(bad)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    try:
        code, last = main()
    except BaseException as e:                   # no traceback escapes
        code, last = 3, "CONTROL INVALID: the control raised %s" % type(e).__name__
    print(last)
    sys.stdout.flush()
    sys.exit(code)
