#!/usr/bin/env python3
"""B1538 -- post-run tables (written during Part F', run after the sealed read-out and the scoped read-out; descriptive only:
the verdict and the predictions are read_out.py's and read_out_scoped.py's).  It reads run_L.jsonl and run_F.jsonl (or their
banked .jsonl.gz) and controls.json's K10, and prints the tables FINDINGS quotes:
  - Part L by state: covers, puncture characters and Galois orbits read, hits (n >= 1) by n, candidates (n >= 2), the largest n,
    and by |D|;
  - Proposition H: on each of K10's covers, the hits at zeta_H (s and n) and their sum;
  - Part F (the sealed partial record and Part F'): by state, candidates read, readings, members, the caps (capW, capL2) in each
    route, members with capL2 >= 2, the largest min(capW, capL2), whether the routes agree.
Writes post_run_tables.json beside it.

    python3 post_run_tables.py      (about a minute)"""
import gzip
import json
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent


def lines(name):
    p = HERE / f"{name}.jsonl"
    f = open(p) if p.exists() else gzip.open(HERE / f"{name}.jsonl.gz", "rt")
    with f:
        for line in f:
            if line.strip():
                yield json.loads(line)


def main():
    rep = {}
    L = defaultdict(lambda: {"covers": set(), "orbits": 0, "characters": 0, "hits by n": Counter(), "by |D|": defaultdict(Counter)})
    hits_at = defaultdict(list)
    for r in lines("run_L"):
        st = r["state"]
        L[st]["covers"].add(r["cover"])
        if not r["read"]:
            continue
        L[st]["orbits"] += r.get("puncture orbits", 0)
        L[st]["characters"] += r.get("puncture characters", 0)
        D = int(r["cover"].split(".D")[1].split(".")[0])
        for h in r["hits"]:
            L[st]["hits by n"][h["n"]] += 1
            L[st]["by |D|"][D][h["n"]] += 1
            hits_at[r["cover"]].append(h)
    rep["Part L"] = {}
    for st in ("m004", "m003", "m136", "m135"):
        x = L[st]
        rep["Part L"][st] = {"covers": len(x["covers"]), "puncture orbits": x["orbits"], "puncture characters": x["characters"],
                             "hits (Galois orbits) by n": dict(sorted(x["hits by n"].items())),
                             "candidates (n >= 2)": sum(v for n, v in x["hits by n"].items() if n >= 2),
                             "largest n": max(x["hits by n"], default=0),
                             "by |D| (n: count)": {D: dict(sorted(c.items())) for D, c in sorted(x["by |D|"].items())}}
    ctl = json.loads((HERE / "controls.json").read_text())
    H = {}
    for cid, hc in sorted(ctl["K10"]["covers"].items()):
        at = [h for h in hits_at.get(cid, []) if list(h["zeta"]) == list(hc["ez"]) and h["m"] == hc["m"]]
        H[cid] = {"acts on Q8 as the identity": hc["acts on Q8 as the identity"],
                  "hits at zeta_H (s, n)": sorted([[h["s"], h["n"]] for h in at]), "sum of n": sum(h["n"] for h in at)}
    rep["Proposition H"] = H
    F = defaultdict(lambda: {"candidates": set(), "readings": 0, "members": 0, "caps R": Counter(), "caps P4": Counter(),
                             "capL2 >= 2": 0, "largest min caps": 0, "routes agree": True})
    for f in lines("run_F"):
        st = f["cover"].split(".")[0]
        key = (f["cover"], tuple(f["chi"]["zeta"]), f["chi"]["m"], tuple(f["chi"]["s"]))
        if f.get("kind") == "candidate":
            F[st]["candidates"].add(key)
            continue
        F[st]["readings"] += 1
        if f["h1 R"] != f["h1 P4"]:
            F[st]["routes agree"] = False
        if f.get("member"):
            F[st]["members"] += 1
            cr, cp = (f["R"]["capW"], f["R"]["capL2"]), (f["P4"]["capW"], f["P4"]["capL2"])
            F[st]["caps R"][cr] += 1
            F[st]["caps P4"][cp] += 1
            if f["R"] != f["P4"]:
                F[st]["routes agree"] = False
            if max(cr[1], cp[1]) >= 2:
                F[st]["capL2 >= 2"] += 1
            F[st]["largest min caps"] = max(F[st]["largest min caps"], min(cr), min(cp))
    rep["Part F (the partial record and Part F')"] = {
        st: {"candidates": len(x["candidates"]), "readings": x["readings"], "members": x["members"],
             "caps R": {str(k): v for k, v in sorted(x["caps R"].items())},
             "caps P4": {str(k): v for k, v in sorted(x["caps P4"].items())},
             "members with capL2 >= 2": x["capL2 >= 2"], "largest min(capW, capL2)": x["largest min caps"],
             "routes agree": x["routes agree"]} for st, x in sorted(F.items())}
    print(json.dumps(rep, indent=1, default=str))
    (HERE / "post_run_tables.json").write_text(json.dumps(rep, indent=1, default=str) + "\n")


if __name__ == "__main__":
    main()
