#!/usr/bin/env python3
"""SM-C23's failing control (fam1-v1-unset-04): the card's covariance check run on an input made wrong on purpose. S is
applied to the modulus while the point is left unmoved (the sealed plant P1); the check must reject it. The check runs
in a copy of relays/sm_c23/ through a small driver written beside the copy.
    python3 relays/claims/sm_refile/c23_control.py
Exit 1 with a last line "CONTROL FAILS:" when the check rejects the wrong input; 0 when it does not; 3 if invalid."""
import pathlib, shutil, subprocess, sys, tempfile
DRIVER = '''import sys
import run_c23 as R
mp = R.mp
mp.mp.dps = 50
t0 = mp.mpc("0.13", "1.2")
L0 = mp.mpf(R.TABLE_CANON(complex(0.13, 1.2))["L_2"])
t1, j = R.mob(R.S, t0)
worst = 0.0
for v in R.POINTS[:4]:
    mp.mp.dps = 50
    a = R.frame(t0, v, L0)
    mp.mp.dps = 50
    b = R.frame(t1, v, L0 + mp.log(abs(j)))
    worst = max(worst, *R.dist(a, b))
print("WORST %r" % worst)
'''
try:
    HERE = pathlib.Path(__file__).resolve().parent
    ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
    tmp = pathlib.Path(tempfile.mkdtemp()) / "sm_c23"
    shutil.copytree(ROOT / "relays" / "sm_c23", tmp)
    (tmp / "control_driver.py").write_text(DRIVER)
    r = subprocess.run([sys.executable, "-B", "control_driver.py", str(ROOT)], cwd=tmp, capture_output=True, text=True)
    worst = float([l for l in r.stdout.splitlines() if l.startswith("WORST ")][0].split()[1])
except Exception as e:
    print("CONTROL INVALID: %s" % type(e).__name__); sys.exit(3)
print("S with the point unmoved: worst difference %.2e" % worst)
if worst > 1e-3:
    print("CONTROL FAILS: as it must, the covariance check rejects S with the point unmoved"); sys.exit(1)
print("CONTROL DID NOT FAIL: the check accepted a wrong action"); sys.exit(0)
