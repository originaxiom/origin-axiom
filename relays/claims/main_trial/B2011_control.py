"""Failing control for the B2011 claim card (decisive script: c60_levels.py, check A1 at mod 135).

It reads the decisive script's text from the repository and execs it with ONE deliberate change: the level of check A1
is shifted from 135 to 81 (the four places A1 names its level: pairing(135), leaf(135) and the labels "mod-135"
and "G_135").
At mod 81 the halving identity is known to hold exactly (B2002), so if the mod-135 result were an artefact of the code
(a pairing routine that leaves roots unpaired at any level, a factor list printed regardless of input), the A1 lines
would come out again. They must not: the gcd must cover the whole charged polynomial, nothing may be left unpaired,
and the A1 equality must print False. Everything else in the script (A2, A6, A7) runs unchanged and must complete, so
a crash cannot pass for a failure.

Run beside the card, single-threaded:
    OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 python3 -B control.py
The repository root is found by walking up from this file and from the working directory to the first folder holding
frontier/B2011_*/verification/c60_levels.py; set B2011_REPO to name it instead.

Exit status (the intake's rule D3: the failing control fails):
    1  the control FAILS AS IT MUST: the perturbed run completed and the decisive A1 lines did not come out;
    0  anything else: the decisive lines came out (the control did not fail), or the control is INVALID (the decisive
       script was not found, the edit did not apply, or the perturbed run crashed or stopped early). A crash therefore
       never counts as the control failing.
"""

import sys as _sys, os as _os, traceback as _tb
def _crash(et, ev, tb):   # main's trial convention (P-885): a crash is never a failing control; it exits 3
    _tb.print_exception(et, ev, tb); print("CONTROL INVALID: the control raised; a crash is not a failing control")
    _sys.stdout.flush(); _os._exit(3)
_sys.excepthook = _crash
import contextlib, io, os, pathlib, re, sys

sys.dont_write_bytecode = True


def find_script():
    starts = [pathlib.Path(os.environ["B2011_REPO"])] if os.environ.get("B2011_REPO") else []
    starts += [pathlib.Path(__file__).resolve().parent, pathlib.Path.cwd()]
    for s in starts:
        for d in [s, *s.parents]:
            hit = sorted(d.glob("frontier/B2011_*/verification/c60_levels.py"))
            if hit:
                return hit[0]
    print("CONTROL INVALID: the decisive script frontier/B2011_*/verification/c60_levels.py was not found")
    sys.exit(3)


SCRIPT = find_script()
src = SCRIPT.read_text()

# the one deliberate change: A1's level 135 -> 81
edits = [("pairing(135)", "pairing(81)"), ("leaf(135)", "leaf(81)"), ("the mod-135 orbit", "the mod-81 orbit"), ("through G_135, via", "through G_81, via")]
for old, new in edits:
    if src.count(old) != 1:
        print("CONTROL INVALID: the edit did not apply (%r occurs %d times in c60_levels.py)" % (old, src.count(old)))
        sys.exit(3)
    src = src.replace(old, new)

buf = io.StringIO()
ns = {"__file__": str(SCRIPT), "__name__": "__main__"}
try:
    with contextlib.redirect_stdout(buf):
        exec(compile(src, "c60_levels.py [control: A1 level 135 -> 81]", "exec"), ns)
except BaseException as e:   # a crash is not a failing control
    print(buf.getvalue(), end="")
    print("CONTROL INVALID: the perturbed run crashed: %s: %s" % (type(e).__name__, e))
    sys.exit(3)
out = re.sub(r"  \[\d+ s\]$", "", buf.getvalue(), flags=re.M)
print(out, end="")

# the decisive claim's substantive lines (from the committed c60_levels_run.txt, timing brackets removed)
decisive = [
    "    degree of gcd(p_neutral(2x)/2^d, S): 949 of the charged 959",
    "    charged left unpaired: degree 10; factors (constant first, multiplicity): [([-2, -2, 1], 1), ([-2, 2, 1], 1), ([-1, -3, 0, 1], 1), ([1, -3, 0, 1], 1)]",
    "    A1: the charged unpaired part equals (x^2 - 2x - 2)(x^2 + 2x - 2)(x^3 - 3x - 1)(x^3 - 3x + 1): True",
]
lines = out.splitlines()
completed = any(l.startswith("    Phi_18(-2) = 73, Phi_6(-2) = 7") for l in lines)   # the script's last line: no crash
came_out = [d for d in decisive if d in lines]
a1 = [l for l in lines if l.startswith("    A1:")]
gcd1 = next((l for l in lines if "degree of gcd" in l), "")
unp1 = next((l for l in lines if "charged left unpaired" in l), "")
print("CONTROL: run completed: %s; decisive A1 lines that came out: %d of %d" % (completed, len(came_out), len(decisive)))
print("CONTROL: in their place: %s | %s | %s" % (gcd1.strip(), unp1.strip(), a1[0].strip() if a1 else "no A1 line"))
if not completed:
    print("CONTROL INVALID: the perturbed run stopped before the script's last line")
    sys.exit(3)
if not came_out and a1 and a1[0].endswith(": False"):
    print("CONTROL FAILS: as it must, with A1's level shifted to 81, where the halving holds, nothing is left unpaired and A1 prints False")
    sys.exit(1)
print("CONTROL DID NOT FAIL")
sys.exit(0)
