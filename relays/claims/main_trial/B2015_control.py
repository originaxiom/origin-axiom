"""B2015's failing control (data-free).

It reads the arc's decisive script, frontier/B2015_*/verification/rate_law.py (SHA-256 checked against the card), as text
and executes it with ONE deliberate change: the law's M is shifted to M + 1 wherever the script evaluates the law, i.e.
in the numeric value 2 sqrt(5 + 4 cos(pi/M)) (function val, also used by R2) and in the minimal polynomial of cos(pi/M)
from which the exact factor is built. The orbits, W, the characteristic polynomials, the primes and R2's pull-back are
untouched. If the six-move rate were 2 sqrt(5 + 4 cos(pi/(M + 1))), the decisive lines would come out under this change;
they must not.

It then applies the decisive criteria to the output (stricter than the arc's lock: every multiplicity must be >= 1):
  R1  five double differences < 1e-12; four exact divisions over Z with multiplicity >= 1; mod 625 [True, True, True];
  R2  the new fibre's top 5.672086410291 (to 1e-9) and below 5.9190440049; the law's value's multiplicity 2 on the
      whole orbit and 0 on the new fibre.

Exit 1: the decisive claim does not come out (the control fails, as it must).
Exit 0: it comes out under the change (the control cannot fail).
Exit 2: a crash, a missing file or a hash mismatch (not a failing control).

    python3 -B control.py                    (from the repository root, or with OA_ROOT set to it; about 10 minutes)
    python3 -B control.py --criteria FILE    applies the same criteria to a saved output of the unchanged script
"""

import sys as _sys, os as _os, traceback as _tb
def _crash(et, ev, tb):   # main's trial convention (P-885): a crash is never a failing control; it exits 3
    _tb.print_exception(et, ev, tb); print("CONTROL INVALID: the control raised; a crash is not a failing control")
    _sys.stdout.flush(); _os._exit(3)
_sys.excepthook = _crash
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ.setdefault(_v, "1")
import hashlib, io, pathlib, re, sys, traceback

SHA16 = "c746d6f670f91dee"        # rate_law.py as committed at 6f80ac0e5
EDITS = [("mp.cos(mp.pi / M)", "mp.cos(mp.pi / (M + 1))"),      # val(M): the numeric value (R1 and R2)
         ("sp.cos(sp.pi / M)", "sp.cos(sp.pi / (M + 1))")]      # the minimal polynomial behind the exact factor (R1)


def find_root():
    if os.environ.get("OA_ROOT"):
        return pathlib.Path(os.environ["OA_ROOT"]).resolve()
    for start in (pathlib.Path.cwd(), pathlib.Path(__file__).resolve().parent):
        for d in (start, *start.parents):
            if (d / "frontier").is_dir() and (d / "scripts" / "checks" / "topic_sweep.py").is_file():
                return d
    raise SystemExit("CRASH: repository root not found (run from it, or set OA_ROOT)")


def criteria(t):
    out = []
    diffs = [float(x) for x in re.findall(r"difference ([\d.e+-]+)", t)]
    out.append(("R1 five double differences < 1e-12", len(diffs) == 5 and max(diffs) < 1e-12, diffs))
    mults = [int(x) for x in re.findall(r"divides charpoly\(W\) over Z with multiplicity (\d+)", t)]
    out.append(("R1 four exact divisions over Z, each multiplicity >= 1", len(mults) == 4 and min(mults) >= 1, mults))
    m = re.search(r"modulo three 62-bit primes: (\[[^\]]*\])", t)
    out.append(("R1 mod 625 divides modulo three primes", bool(m) and m.group(1) == "[True, True, True]", m and m.group(1)))
    m = re.search(r"the new fibre's largest eigenvalue ([\d.]+)", t); top = float(m.group(1)) if m else None
    out.append(("R2 new fibre's top 5.672086410291 and below 5.919", top is not None and abs(top - 5.672086410291) < 1e-9 and top < 5.9190440049, top))
    m = re.search(r"its multiplicity on the whole orbit \(to 1e-8\): (\d+), on the new fibre: (\d+)", t)
    out.append(("R2 the law's value: multiplicity 2 on the orbit, 0 on the new fibre", bool(m) and m.groups() == ("2", "0"), m and m.groups()))
    return out


def report(t):
    rows = criteria(t)
    for name, ok, seen in rows:
        print("  %-70s %s   (seen: %s)" % (name, "holds" if ok else "FAILS", seen))
    return all(ok for _, ok, _ in rows)


class Tee(io.StringIO):
    def write(self, s):
        sys.__stdout__.write(s); sys.__stdout__.flush()
        return super().write(s)


def main():
    if len(sys.argv) == 3 and sys.argv[1] == "--criteria":
        print("criteria on %s:" % sys.argv[2])
        ok = report(pathlib.Path(sys.argv[2]).read_text())
        print("DECISIVE CLAIM %s" % ("COMES OUT" if ok else "DOES NOT COME OUT"))
        return 0 if ok else 1
    root = find_root()
    hits = sorted(root.glob("frontier/B2015_*/verification/rate_law.py"))
    if len(hits) != 1:
        print("CRASH: expected one B2015 rate_law.py, found %d" % len(hits)); return 3
    script = hits[0]; raw = script.read_bytes()
    if hashlib.sha256(raw).hexdigest()[:16] != SHA16:
        print("CRASH: rate_law.py's SHA-256 is %s, the card's is %s" % (hashlib.sha256(raw).hexdigest()[:16], SHA16)); return 3
    src = raw.decode()
    for old, new in EDITS:
        if src.count(old) != 1:
            print("CRASH: %r occurs %d times in rate_law.py, expected once" % (old, src.count(old))); return 3
        src = src.replace(old, new)
    print("CONTROL: rate_law.py (SHA-256 %s) run with M -> M + 1 in the law (val and the minimal polynomial of cos(pi/M)); "
          "the labels 'M = ...' and 'cos(pi/M)' below still print the unshifted M" % SHA16, flush=True)
    # CHANGED 2026-11-27 (P-885): run as a separate process beside the script (control_run.py), not exec'd here: the
    # intake's guard refuses exec
    from control_run import run_changed
    rc, stdout, stderr = run_changed(script, src)
    print(stdout, end="", flush=True)
    if rc != 0:
        print("CRASH: the changed script exited %d (%s); this is not a failing control"
              % (rc, (stderr.strip().splitlines() or [""])[-1])); return 3
    print("criteria on the changed run:")
    ok = report(stdout)
    if ok:
        print("CONTROL DOES NOT FAIL: the decisive claim comes out under M -> M + 1 (the check cannot tell the law from its shift)")
        return 0
    print("CONTROL FAILS: as it must, under M -> M + 1 the decisive claim does not come out")
    return 1


if __name__ == "__main__":
    sys.exit(main())
