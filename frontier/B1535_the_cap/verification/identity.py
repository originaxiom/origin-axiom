#!/usr/bin/env python3
"""B1535 banked identity (PREREGISTRATION section 8), checked before Part M or Part W reads anything:
  - controls_rerun.json (controls.py --rerun, unchanged code) equals controls.json in every field but the timings;
  - k1.json still reads all 144 of sm:B1534's banked terms as held;
  - every sealed file's sha-256 equals ARTIFACT_HASHES.txt.
A single difference stops the run, and nothing is read.

    python3 identity.py   ->  identity.json (exit status 1 if the identity fails)"""
import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ARC = HERE.parent
TIMINGS = ("started", "seconds")


def diff(a, b, path="$"):
    """every path at which a and b differ"""
    if isinstance(a, dict) and isinstance(b, dict):
        out = [f"{path}.{k}: only in one" for k in sorted(set(a) ^ set(b), key=str)]
        for k in sorted(set(a) & set(b), key=str):
            out += diff(a[k], b[k], f"{path}.{k}")
        return out
    if isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            return [f"{path}: lengths {len(a)} and {len(b)}"]
        out = []
        for i, (x, y) in enumerate(zip(a, b)):
            out += diff(x, y, f"{path}[{i}]")
        return out
    return [] if a == b else [f"{path}: {a!r} != {b!r}"]


def main():
    a = json.loads((HERE / "controls.json").read_text())
    b = json.loads((HERE / "controls_rerun.json").read_text())
    d = diff({k: v for k, v in a.items() if k not in TIMINGS}, {k: v for k, v in b.items() if k not in TIMINGS})
    k1 = json.loads((HERE / "k1.json").read_text())
    k1_ok = bool(k1["holds"]) and k1["n terms"] == 144 and not k1["failures"]
    bad, n = [], 0
    for line in (ARC / "ARTIFACT_HASHES.txt").read_text().splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        h, name = line.split(None, 1)
        n += 1
        if hashlib.sha256((ARC / name).read_bytes()).hexdigest() != h:
            bad.append(name)
    out = {"controls differences (first 20)": d[:20], "controls differences": len(d), "controls rerun all hold": b.get("all hold"),
           "k1 holds (144 terms)": k1_ok, "sealed files checked": n, "hash mismatches": bad,
           "identity holds": not d and bool(b.get("all hold")) and k1_ok and not bad}
    (HERE / "identity.json").write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps(out, indent=1))
    sys.exit(0 if out["identity holds"] else 1)


if __name__ == "__main__":
    main()
