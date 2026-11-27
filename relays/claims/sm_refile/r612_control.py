#!/usr/bin/env python3
"""The failing control for P-612's card (SM-R612b). Data-free.

The decisive check is the sealed plant PL5: the T-law at delta = inf, (tau, (a, b)) -> (tau + 1, (a, b - a)), must
keep frame A's defined outputs to 1e-10 (relays/cards/SM_R612b_count-the-image-with-a-zero-floor.md, section 2).
This control makes the input wrong on purpose: in a temporary copy of relays/sm_r612b/run.py, the zero floor is set to
0, which restores the void run's rule (SM-R612: logs of numerical-zero masses are taken as values). On that copy the
same PL5 check, at the first test modulus 0.21 + 2.97i, must reject. It is known to (SM-R612: 0.87 there).

The copy is run as a separate process (a small driver beside it in the temporary folder); nothing is written into the
repository.
    python3 relays/claims/sm_refile/r612_control.py
Exit 1 with "CONTROL FAILS:" when the check rejects the planted input (the expected outcome); 0 with
"CONTROL DID NOT FAIL:" when it accepts it; 3 with "CONTROL INVALID:" when anything crashes."""
import os
import pathlib
import shutil
import subprocess
import sys
import tempfile

PL5_BOUND = 1e-10                     # the card's sealed bound for PL5
OLD, NEW = "\nZERO_FLOOR = 1e-12 ", "\nZERO_FLOOR = 0.0   "

DRIVER = '''import sys, math
sys.path.insert(0, ".")
import run as R
R.load(sys.argv[1])
p = R.plants(R.TAUS[0])
print("PL5_DEV %r" % p["PL5_T_law_dev"])
print("PL5_UNDEFINED %d" % len(p["PL5_undefined_outputs"]))
'''


def root():
    for d in [pathlib.Path(__file__).resolve(), *pathlib.Path(__file__).resolve().parents]:
        if (d / "frontier").is_dir() and (d / "GENESIS.md").is_file():
            return d
    return None


def main():
    rt = root()
    if rt is None:
        print("CONTROL INVALID: no repository root (frontier/ and GENESIS.md) above this file")
        return 3
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="r612c_"))
    try:
        dst = tmp / "sm_r612b"
        shutil.copytree(rt / "relays" / "sm_r612b", dst)
        src = (dst / "run.py").read_text(encoding="utf-8")
        if src.count(OLD) != 1:
            print("CONTROL INVALID: the planted edit did not apply (%d matches)" % src.count(OLD))
            return 3
        (dst / "run.py").write_text(src.replace(OLD, NEW), encoding="utf-8")
        (dst / "control_driver.py").write_text(DRIVER, encoding="utf-8")
        env = dict(os.environ, OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1", MKL_NUM_THREADS="1",
                   VECLIB_MAXIMUM_THREADS="1", PYTHONDONTWRITEBYTECODE="1")
        p = subprocess.run([sys.executable, "-B", "control_driver.py", str(rt)], cwd=dst, env=env,
                           capture_output=True, text=True)
        if p.returncode != 0:
            tail = (p.stderr.strip().splitlines() or [""])[-1]
            print("CONTROL INVALID: the planted run crashed (exit %d): %s" % (p.returncode, tail))
            return 3
        vals = dict(l.split(" ", 1) for l in p.stdout.splitlines() if l.startswith("PL5_"))
        dev = float(vals["PL5_DEV"]); nund = int(vals["PL5_UNDEFINED"])
        accepted = dev < PL5_BOUND and nund < 7
        print("planted input: zero floor 0 (the void run's rule); PL5 at 0.21+2.97i: deviation %s the bound 1e-10, "
              "%d undefined outputs" % ("below" if dev < PL5_BOUND else "above", nund))
        if accepted:
            print("CONTROL DID NOT FAIL: the PL5 check accepted the planted input")
            return 0
        print("CONTROL FAILS: the PL5 check rejects the planted input, as it must")
        return 1
    except BaseException as e:                       # no traceback may escape
        print("CONTROL INVALID: %s: %s" % (type(e).__name__, e))
        return 3
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    try:
        rc = main()
    except BaseException as e:
        print("CONTROL INVALID: %s: %s" % (type(e).__name__, e)); rc = 3
    sys.exit(rc)
