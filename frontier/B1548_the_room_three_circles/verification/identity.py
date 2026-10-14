#!/usr/bin/env python3
"""B1548 -- the banked identity (PREREGISTRATION.md section 8), checked before run.py reads anything:
  - controls.py (K1-K9, loaded by its path under a unique name, E12) reproduces controls.json in every field but the
    timings;
  - every sealed file's sha-256 equals ARTIFACT_HASHES.txt.
A single difference stops the run, and nothing is read.

    python3 identity.py   ->  identity.json (exit status 1 if the identity fails)"""
import hashlib
import importlib.util
import json
import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")
HERE = Path(__file__).resolve().parent
ARC = HERE.parent
TIMINGS = ("seconds",)


def strip(x):
    if isinstance(x, dict):
        return {k: strip(v) for k, v in x.items() if k not in TIMINGS}
    if isinstance(x, list):
        return [strip(v) for v in x]
    return x


def main():
    spec = importlib.util.spec_from_file_location("b1548_controls", HERE / "controls.py")
    K = importlib.util.module_from_spec(spec)
    sys.modules["b1548_controls"] = K
    spec.loader.exec_module(K)
    saved = sys.argv
    sys.argv = ["controls.py"]
    try:
        now = json.loads(json.dumps(K.main(), default=str))
    finally:
        sys.argv = saved
    rec = json.loads((HERE / "controls.json").read_text())
    out = {"controls reproduced": strip(now) == strip(rec), "controls hold": bool(now.get("all hold"))}
    if not out["controls reproduced"]:
        out["differing controls"] = sorted(k for k in set(now) | set(rec) if strip(now.get(k)) != strip(rec.get(k)))
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
    out["identity holds"] = out["controls reproduced"] and out["controls hold"] and not bad and n > 0
    (HERE / "identity.json").write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps(out, indent=1))
    sys.exit(0 if out["identity holds"] else 1)


if __name__ == "__main__":
    main()
