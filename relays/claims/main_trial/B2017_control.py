"""B2017's failing control (claim card, 2026-11-26; data-free).

It reads the decisive script frontier/B2017_*/verification/census.py as text and executes it with ONE deliberate change:
the constant of the whole's form, p_neutral(2x)/2^d = (x^2 - 9) x S(x), is replaced by 4, i.e. (x^2 - 4) x S(x). The
constant enters census.py in two places, both changed together: the exact factor Q9 = x^2 - 9 (classify_exact) and its
roots +-3 in the double-precision test (classify_num). Nothing else changes: same levels, same moves, same sectors
(B2011's sectors_exact, imported unchanged), same tolerances.

If the census's result were wrong in this way (the neutral sector carrying (x^2 - 4) x instead of (x^2 - 9) x beside the
charged sector), the decisive line would not come out. The control prints the perturbed census and then one verdict:
  exit 1  "CONTROL FAILS, AS IT MUST": the decisive line is absent (the expected outcome);
  exit 0  "CONTROL DID NOT FAIL": the decisive line came out despite the change (the census would be insensitive to it);
  exit 3  "CONTROL INVALID": the change could not be applied or the run raised (a crash is not a failing control).

The repository root is found by walking up from this file and from the working directory to a folder holding
frontier/B2017_*/verification/census.py; the environment variable OA_ROOT overrides it.
    python3 -B control.py"""

import sys as _sys, os as _os, traceback as _tb
def _crash(et, ev, tb):   # main's trial convention (P-885): a crash is never a failing control; it exits 3
    _tb.print_exception(et, ev, tb); print("CONTROL INVALID: the control raised; a crash is not a failing control")
    _sys.stdout.flush(); _os._exit(3)
_sys.excepthook = _crash
import contextlib, io, os, pathlib, sys, traceback

DECISIVE = ("over all levels: the orbits in (a) or (a'), by level: "
            "{27: {'a': 2, \"a'\": 1}, 25: [], 5: [], 7: [], 11: [], 13: [], 49: []}")
CHANGES = [("Q9 = flint.fmpz_poly([-9, 0, 1])", "Q9 = flint.fmpz_poly([-4, 0, 1])"),
           ("for t in (3.0, -3.0, 0.0):", "for t in (2.0, -2.0, 0.0):")]


def find_root():
    if os.environ.get("OA_ROOT"):
        return pathlib.Path(os.environ["OA_ROOT"]).resolve()
    for start in (pathlib.Path(__file__).resolve().parent, pathlib.Path.cwd().resolve()):
        for p in (start, *start.parents):
            if list(p.glob("frontier/B2017_*/verification/census.py")):
                return p
    return None


def main():
    root = find_root()
    if root is None:
        print("CONTROL INVALID: no repository root holding frontier/B2017_*/verification/census.py (set OA_ROOT)")
        return 3
    script = next(root.glob("frontier/B2017_*/verification/census.py"))
    src = script.read_text()
    for old, new in CHANGES:
        if src.count(old) != 1:
            print("CONTROL INVALID: %r occurs %d times in census.py, not once" % (old, src.count(old)))
            return 3
        src = src.replace(old, new)
    print("control: census.py with the whole's form's constant 9 -> 4 (x^2 - 9 -> x^2 - 4; roots +-3 -> +-2)", flush=True)
    # CHANGED 2026-11-27 (P-885): run as a separate process beside the script (control_run.py), not exec'd here: the
    # intake's guard refuses exec
    from control_run import run_changed
    rc, out, stderr = run_changed(script, src)
    print(out, end="", flush=True)
    if rc != 0:
        print("CONTROL INVALID: the perturbed census exited %d (%s); a crash is not a failing control"
              % (rc, (stderr.strip().splitlines() or [""])[-1]))
        return 3
    if "over all levels: the orbits in (a) or (a'), by level:" not in out:
        print("CONTROL INVALID: the perturbed census did not reach its last line")
        return 3
    if DECISIVE in out:
        print("CONTROL DID NOT FAIL: the decisive line came out with the constant changed")
        return 0
    print("CONTROL FAILS: as it must, the decisive line does not come out with x^2 - 4 in place of x^2 - 9")
    return 1


if __name__ == "__main__":
    sys.exit(main())
