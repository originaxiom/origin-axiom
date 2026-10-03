#!/usr/bin/env python3
"""B1534 banked identity (PREREGISTRATION section 8), checked before run_terms.py reads anything: the sealed controls,
re-run unchanged after the seal, must reproduce their sealed outputs in every field but the timings ("started",
"seconds").  Compares controls_rerun.json with controls.json and members_every_twist_rerun.json with
members_every_twist.json (the sealed files, unchanged since the seal: ARTIFACT_HASHES.txt), and prints the verdict."""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
TIMING = {"started", "seconds"}


def strip(x):
    if isinstance(x, dict):
        return {k: strip(v) for k, v in x.items() if k not in TIMING}
    if isinstance(x, list):
        return [strip(v) for v in x]
    return x


def diff(a, b, path=""):
    out = []
    if isinstance(a, dict) and isinstance(b, dict):
        for k in sorted(set(a) | set(b)):
            if k not in a or k not in b:
                out.append(f"{path}/{k}: present on one side only")
            else:
                out += diff(a[k], b[k], f"{path}/{k}")
    elif isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            out.append(f"{path}: lengths {len(a)} and {len(b)}")
        for i, (x, y) in enumerate(zip(a, b)):
            out += diff(x, y, f"{path}[{i}]")
    elif a != b:
        out.append(f"{path}: {str(a)[:80]} != {str(b)[:80]}")
    return out


def main():
    ok = True
    for sealed, rerun in (("controls.json", "controls_rerun.json"),
                          ("members_every_twist.json", "members_every_twist_rerun.json")):
        a = strip(json.loads((HERE / sealed).read_text()))
        b = strip(json.loads((HERE / rerun).read_text()))
        d = diff(a, b)
        print(f"{rerun} against the sealed {sealed}: {'identical but the timings' if not d else f'{len(d)} differences'}")
        for line in d[:40]:
            print("   ", line)
        ok &= not d
    print("BANKED IDENTITY HOLDS" if ok else "BANKED IDENTITY FAILS: nothing is read")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
