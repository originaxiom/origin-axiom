#!/usr/bin/env python3
"""SM-C14's failing control (fam1-v1-unset-04): the card's control C1 (every extension has determinant one) run on an
input made wrong on purpose, the sealed plant P1 (the extension built with no w in its corner). The check must reject it.
    python3 relays/claims/sm_refile/c14_control.py
Exit 1 with a last line "CONTROL FAILS:" when the check rejects the planted input; 0 when it does not; 3 if invalid."""
import json, pathlib, shutil, subprocess, sys, tempfile
try:
    HERE = pathlib.Path(__file__).resolve().parent
    ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
    tmp = pathlib.Path(tempfile.mkdtemp()) / "sm_c14"
    shutil.copytree(ROOT / "relays" / "sm_c14", tmp)
    (tmp / "c14_p1.json").unlink()
    subprocess.run([sys.executable, "-B", "run_c14.py", "p1"], cwd=tmp, capture_output=True, text=True)
    p = json.loads((tmp / "c14_p1.json").read_text())
    passes = all(p[n]["det != 1"] == 0 for n in ("1", "3", "5"))
except Exception as e:
    print("CONTROL INVALID: %s" % type(e).__name__); sys.exit(3)
print("the planted extensions pass the determinant-one check: %s" % passes)
if not passes:
    print("CONTROL FAILS: as it must, the determinant-one check rejects the extensions built with no w in the corner")
    sys.exit(1)
print("CONTROL DID NOT FAIL: the check accepted the planted extensions"); sys.exit(0)
