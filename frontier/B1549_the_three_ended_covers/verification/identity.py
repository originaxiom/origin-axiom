#!/usr/bin/env python3
"""sm:B1549 -- the banked identity, checked before run.py reads anything:
  - every sealed file's sha-256 as ARTIFACT_HASHES.txt records it;
  - the controls re-run: K2 (main's banked counts), K3 (sm:B1545's m136 reading), K4 (the read-out on synthetic rows),
    K5 (n(1) = 0 on every cover). K1, the SVD re-read of every member orbit, is not repeated; its record is sealed.
A single difference stops the run.

    python3 identity.py   ->  identity.json beside this file"""
import hashlib
import json
import time

import controls as K
import three_lib as T

HERE = T.HERE


def hashes():
    bad = []
    for line in (HERE.parent / "ARTIFACT_HASHES.txt").read_text().splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        h, path = line.split(None, 1)
        p = HERE.parent / path.strip()
        if not p.exists() or hashlib.sha256(p.read_bytes()).hexdigest() != h:
            bad.append(path.strip())
    return bad


def main():
    t0 = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    bad = hashes()
    k23 = K.run_K2_K3()
    k4 = K.K4()
    k5 = K.K5()
    holds = (not bad and all(x["holds"] for x in k23["K2"]) and all(x["holds"] for x in k23["K3"]) and k4["holds"]
             and k5["holds"])
    out = {"started": t0, "ended": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "hash mismatches": bad,
           "K2": [(x["character"], x["route"], x["got"], x["holds"]) for x in k23["K2"]],
           "K3": [(x["route"], x["got"], x["holds"]) for x in k23["K3"]], "K4": k4, "K5": k5, "holds": holds}
    (HERE / "identity.json").write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps({"hash mismatches": bad, "holds": holds}))
    if not holds:
        raise SystemExit("the banked identity does not hold: the run must not start")


if __name__ == "__main__":
    main()
