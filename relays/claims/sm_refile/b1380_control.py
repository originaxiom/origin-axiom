#!/usr/bin/env python3
"""B1380's failing control (fam1-v1-unset-04): the realizability check S5 run on an input made wrong on purpose. The
golden substitution sigma is replaced by the swap a <-> b, an automorphism of finite order whose abelianization has
root-of-unity eigenvalues; the check must refuse to single out the once-punctured torus for it.
    python3 relays/claims/sm_refile/b1380_control.py
Exit 1 with a last line "CONTROL FAILS:" when the check rejects the planted input; 0 when it does not; 3 if invalid."""
import pathlib, shutil, subprocess, sys, tempfile
DRIVER = '''import puncture as P
P.SIGMA = {P.A: [P.B], P.B: [P.A]}
P.SIGMA2 = P.compose(P.SIGMA, P.SIGMA)
try:
    no_root, verdict, ctrl = P.s5_realizability()
    print("ACCEPTED %s" % sorted(k for k, v in verdict.items() if v.startswith("sigma realizable")))
except AssertionError:
    print("REJECTED")
'''
try:
    HERE = pathlib.Path(__file__).resolve().parent
    ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
    tmp = pathlib.Path(tempfile.mkdtemp())
    shutil.copy(ROOT / "relays" / "sm_b1380" / "verification" / "puncture.py", tmp / "puncture.py")
    (tmp / "driver.py").write_text(DRIVER)
    r = subprocess.run([sys.executable, "-B", "driver.py"], cwd=tmp, capture_output=True, text=True)
    out = r.stdout.strip().splitlines()[-1]
except Exception as e:
    print("CONTROL INVALID: %s" % type(e).__name__); sys.exit(3)
print("with sigma replaced by the swap: %s" % out)
if out == "REJECTED":
    print("CONTROL FAILS: as it must, the realizability check refuses the finite-order swap"); sys.exit(1)
print("CONTROL DID NOT FAIL: the check accepted the planted swap"); sys.exit(0)
