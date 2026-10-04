#!/usr/bin/env python3
"""B1536 banked identity (PREREGISTRATION section 8), checked before run.py reads anything:
  - control_k2.py (both routes on sm:B1534's 148 banked silver rows) reproduces k2.json in every field but the timings;
  - control_k4.py (the two states themselves) reproduces k4.json in every field but the timings;
  - control_k1.py on M2 and M3 (both routes; sm:B1532's banked census) reproduces k1.json's histograms;
  - control_k5.py (the covers' counts on two presentations, and their cusps against SnapPy's) reproduces k5.json;
  - read_out_selftest.py (K6: the read-out's logic on synthetic rows) reproduces k6.json;
  - every sealed file's sha-256 equals ARTIFACT_HASHES.txt.
A single difference stops the run, and nothing is read.

    python3 identity.py   ->  identity.json (exit status 1 if the identity fails)"""
import hashlib
import json
import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")
HERE = Path(__file__).resolve().parent
ARC = HERE.parent
sys.path.insert(0, str(HERE))
TIMINGS = ("seconds", "started")


def strip(x):
    if isinstance(x, dict):
        return {k: strip(v) for k, v in x.items() if k not in TIMINGS}
    if isinstance(x, list):
        return [strip(v) for v in x]
    return x


def main():
    import control_k1 as K1
    import control_k2 as K2
    import control_k4 as K4
    import control_k5 as K5
    import read_out_selftest as K6
    out = {}
    k2 = json.loads(json.dumps(K2.main(), default=str))
    out["K2 reproduced"] = strip(k2) == strip(json.loads((HERE / "k2.json").read_text()))
    k4 = json.loads(json.dumps(K4.main(), default=str))
    out["K4 reproduced"] = strip(k4) == strip(json.loads((HERE / "k4.json").read_text()))
    saved = sys.argv
    sys.argv = ["control_k1.py", "--levels", "2", "3", "--route-r-levels", "2", "3"]
    try:
        k1 = json.loads(json.dumps(K1.main(), default=str))
    finally:
        sys.argv = saved
    rec = json.loads((HERE / "k1.json").read_text())
    out["K1 reproduced (M2, M3)"] = all(strip(k1["per level"][n]) == strip(rec["per level"][n]) for n in ("2", "3"))
    k5 = json.loads(json.dumps(K5.main(), default=str))
    out["K5 reproduced"] = strip(k5) == strip(json.loads((HERE / "k5.json").read_text()))
    k6 = json.loads(json.dumps(K6.main(), default=str))
    out["K6 reproduced"] = k6 == json.loads((HERE / "k6.json").read_text())
    bad, n = [], 0
    for line in (ARC / "ARTIFACT_HASHES.txt").read_text().splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        h, name = line.split(None, 1)
        n += 1
        if hashlib.sha256((ARC / name).read_bytes()).hexdigest() != h:
            bad.append(name)
    out["sealed files checked"] = n
    out["hash mismatches"] = bad
    out["identity holds"] = (out["K2 reproduced"] and out["K4 reproduced"] and out["K1 reproduced (M2, M3)"] and
                             out["K5 reproduced"] and out["K6 reproduced"] and not bad)
    (HERE / "identity.json").write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps(out, indent=1))
    sys.exit(0 if out["identity holds"] else 1)


if __name__ == "__main__":
    main()
