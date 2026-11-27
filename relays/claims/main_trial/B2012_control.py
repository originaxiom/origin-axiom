"""B2012's failing control (for its claim card; data-free).

It reads the decisive script frontier/B2012_*/verification/blind_checks.py as text and runs it with ONE deliberate
change: in N1's factorisation the second shifted factor R(x + 2) becomes R(x + 3), i.e. it tests a pairing of the
four-move sum's spectrum lambda <-> lambda + 1 instead of the claimed lambda <-> lambda + 2. Both occurrences of the
text "shift(4) * shift(2)" (the exact branch over Z and the branch modulo three primes) are changed; nothing else is.
Degrees are unchanged, so a False can only come from the offset. If the claim were wrong in this way (the spectrum
paired by 1, not 2), the committed decisive lines "... over Z: True" and "modulo three 62-bit primes: [True, True,
True]" would not appear.

Run beside the card, from anywhere inside the repository (or with OA_ROOT set to the repository's root):
    python3 -B control.py
Exit status: 1 = the control FAILS as required (no N1 line states the factorisation; the pointwise identity, which
the change does not touch, still holds on all six orbits); 0 = the control did NOT fail (the decisive lines survive
the change: a control that cannot fail); 2 = the change could not be applied or the run crashed (not a failing
control)."""

import sys as _sys, os as _os, traceback as _tb
def _crash(et, ev, tb):   # main's trial convention (P-885): a crash is never a failing control; it exits 3
    _tb.print_exception(et, ev, tb); print("CONTROL INVALID: the control raised; a crash is not a failing control")
    _sys.stdout.flush(); _os._exit(3)
_sys.excepthook = _crash
import contextlib, glob, io, os, pathlib, re, sys

OLD, NEW = "shift(4) * shift(2)", "shift(4) * shift(3)"


def find_root():
    if os.environ.get("OA_ROOT"):
        return pathlib.Path(os.environ["OA_ROOT"])
    for start in (pathlib.Path(__file__).resolve().parent, pathlib.Path.cwd().resolve()):
        for d in (start, *start.parents):
            if glob.glob(str(d / "frontier" / "B2012_*" / "verification" / "blind_checks.py")):
                return d
    return None


class Tee(io.TextIOBase):
    def __init__(self, *streams): self.streams = streams
    def write(self, s):
        for st in self.streams: st.write(s)
        return len(s)
    def flush(self):
        for st in self.streams: st.flush()


def main():
    root = find_root()
    if root is None:
        print("CONTROL NOT RUN (exit 3): the repository root was not found; set OA_ROOT"); return 3
    path = pathlib.Path(glob.glob(str(root / "frontier" / "B2012_*" / "verification" / "blind_checks.py"))[0])
    src = path.read_text()
    n_old = src.count(OLD)
    if n_old != 2:
        print("CONTROL NOT APPLIED (exit 3): expected the text %r twice in %s, found %d" % (OLD, path.name, n_old)); return 3
    changed = src.replace(OLD, NEW)
    print("control: %s with %r -> %r (%d occurrences); all else unchanged" % (path.name, OLD, NEW, n_old), flush=True)
    # CHANGED 2026-11-27 (P-885): run as a separate process beside the script (control_run.py), not exec'd here: the
    # intake's guard refuses exec
    from control_run import run_changed
    rc, stdout, stderr = run_changed(path, changed)
    print(stdout, end="", flush=True)
    if rc != 0:
        print("CRASH (exit 3): the changed run exited %d: %s -- not a failing control"
              % (rc, (stderr.strip().splitlines() or [""])[-1])); return 3
    out = stdout.splitlines()
    n1 = [l for l in out if l.startswith("N1 ")]
    pointwise = sum("pointwise: True" in l for l in n1)
    exact_true = sum("over Z: True" in l for l in n1)
    exact_false = sum("over Z: False" in l for l in n1)
    mod_true = sum("primes: [True, True, True]" in l for l in n1)
    mod_any_false = sum(bool(re.search(r"primes: \[.*False.*\]", l)) for l in n1)
    print("control summary: %d N1 lines; pointwise identity True on %d; factorisation over Z True on %d, False on %d; "
          "modulo three primes all True on %d, some False on %d" % (len(n1), pointwise, exact_true, exact_false, mod_true, mod_any_false))
    if len(n1) != 6 or pointwise != 6 or exact_true + exact_false != 5 or mod_true + mod_any_false != 1:
        print("CONTROL INCONCLUSIVE (exit 3): the run did not produce six comparable N1 lines"); return 3
    if exact_true == 0 and mod_true == 0:
        print("CONTROL FAILS: as required, with the pairing offset 1 in place of 2, no orbit gives the factorisation")
        return 1
    print("CONTROL DID NOT FAIL (exit 0): the decisive lines survive the change")
    return 0


if __name__ == "__main__":
    sys.exit(main())
