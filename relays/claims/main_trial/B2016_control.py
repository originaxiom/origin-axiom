"""B2016's failing control (drafted for B2016's claim card, 2026-11-26).

It runs n0_light.py (beside this file) on the arc's own code with ONE deliberate change to cosets_gap.py's text: the
whole's form's constant, Q9 = x^2 - 9, becomes x^2 - 4. If the halving's residual factor on the whole's orbit were not
(x^2 - 9) x, cosets_gap.py's test would not give category (a), and the decisive line "the whole's stabiliser class:
category a, ..." would not come out. Everything else (the orbit, the six moves, the sector polynomials, the CRT) runs
unchanged, so the control fails because of the change and not because of a crash.

Exit 1: the decisive claim did not come out (the control FAILS, as it must). Exit 2: the run crashed or was incomplete (not
a failing control). Exit 0: the decisive claim came out despite the change (the control is broken).
Run from the repository root or from the arc's verification/ folder:
    OMP_NUM_THREADS=1 python3 -B control.py
"""

import sys as _sys, os as _os, traceback as _tb
def _crash(et, ev, tb):   # main's trial convention (P-885): a crash is never a failing control; it exits 3
    _tb.print_exception(et, ev, tb); print("CONTROL INVALID: the control raised; a crash is not a failing control")
    _sys.stdout.flush(); _os._exit(3)
_sys.excepthook = _crash
import importlib.util, pathlib, sys, traceback

HERE = pathlib.Path(__file__).resolve().parent
PATCH = ("Q9 = flint.fmpz_poly([-9, 0, 1])", "Q9 = flint.fmpz_poly([-4, 0, 1])")

spec = importlib.util.spec_from_file_location("n0_light", HERE / "n0_light.py")
n0 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(n0)

print("control: one change to cosets_gap.py's text: %r -> %r" % PATCH)
try:
    got = n0.run(patch=PATCH)
except Exception:
    traceback.print_exc()
    print("CONTROL CRASHED: not a failing control")
    sys.exit(3)
if sorted(got) != [27, 81] or any(got[N][:2] != n0.COMMITTED[N][:2] for N in (27, 81)):
    print("CONTROL INCOMPLETE: the group or rho differ from the committed run, so the change is not what was tested")
    sys.exit(3)
came_out = [N for N in (27, 81) if got[N][2] == n0.COMMITTED[N][2]]
if came_out:
    print("CONTROL BROKEN: the decisive line still came out at mod %s" % came_out)
    sys.exit(0)
print("CONTROL FAILS: as it must, with the constant 4 the whole's stabiliser class is not in category (a) at mod 27 or 81")
sys.exit(1)
