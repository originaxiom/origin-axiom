#!/usr/bin/env python3
"""B1536 -- post-run summary, written after the sealed read-out (disclosed in FINDINGS section 4).  Descriptive only: the
verdict and the predictions are read_out.py's.  It reads the four run records (run_<route>_<state>.jsonl if present, else
the banked run_<route>_<state>.jsonl.gz) and prints the tables FINDINGS quotes:
  - the members by caps (capW, capL2), per state, and whether the two routes give the same caps at every member;
  - every member with min(capW, capL2) >= 2 or capL2 >= 3 (where room is largest), with its cover's degree and cusps;
  - the supplies at the trivial character (u = 0, kappa = 0) on every cover where n(1) or n(rho) is positive, by degree;
  - the counts read: Part P at the pulled-back class, and Part O's readings at the cover's own classes, by count.
Writes post_run_rooms.json beside it.

    python3 post_run_rooms.py      (a few seconds)"""
import gzip
import json
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent


def rows(route, state):
    p = HERE / f"run_{route}_{state}.jsonl"
    text = p.read_text() if p.exists() else gzip.open(HERE / f"run_{route}_{state}.jsonl.gz", "rt").read()
    out = {}
    for line in text.splitlines():
        r = json.loads(line)
        if not r.get("done"):
            out[(r["cover"], tuple(r["u"]), r["kappa"])] = r
    return out


def main():
    report = {}
    for st in ("m004", "m003"):
        N, R = rows("N", st), rows("R", st)
        assert set(N) == set(R)
        caps = Counter()
        same_caps = True
        big = []
        k1 = []
        part_p, part_o = Counter(), Counter()
        for key, r in sorted(N.items()):
            rr = R[key]
            if r["member"] != rr["member"]:
                same_caps = False
            if not r["member"]:
                continue
            c = (r["S"]["capW"], r["S"]["capL2"])
            if c != (rr["S"]["capW"], rr["S"]["capL2"]):
                same_caps = False
            caps[c] += 1
            if min(c) >= 2 or c[1] >= 3:
                big.append({"cover": r["cover"], "degree": r["degree"], "cusps": r["cusps"], "abelian": r["abelian"],
                            "u": r["u"], "kappa": r["kappa"], "caps": list(c)})
            if r["u"] == ["0", "0"] and r["kappa"] == "0":
                n1, nr = r["S"]["n(L)"], r["S"]["n((VL)*)"]
                if n1 or nr:
                    k1.append({"cover": r["cover"], "degree": r["degree"], "cusps": r["cusps"], "abelian": r["abelian"],
                               "n(1)": n1, "n(rho)": nr, "caps": list(c)})
            if "P" in r:
                part_p[tuple(r["P"]["count"])] += 1
            for o in r.get("O", []):
                for x in o["readings"]:
                    part_o[tuple(x["count"])] += 1
        by_deg = defaultdict(lambda: Counter())
        for x in k1:
            by_deg[x["degree"]][(x["n(1)"], x["n(rho)"])] += 1
        best = max((min(c) for c in caps), default=0)
        print(f"{st}: {len(N)} characters, {sum(caps.values())} members; the routes give the same membership and caps at "
              f"every row: {same_caps}")
        print(f"  members by caps (capW, capL2): {dict(sorted(caps.items()))}; the largest min(capW, capL2) is {best}")
        print(f"  members with min(caps) >= 2 or capL2 >= 3: {len(big)}")
        groups = defaultdict(list)
        for b in big:
            groups[(b["cover"], b["degree"], b["cusps"], b["abelian"], tuple(b["caps"]))].append((b["u"], b["kappa"]))
        for (cv, dg, cu, ab, c), lst in sorted(groups.items()):
            print(f"    {cv} (degree {dg}, {cu} cusps, {'abelian' if ab else 'non-abelian'}): caps {c} at {len(lst)} "
                  f"character(s), e.g. u = ({', '.join(lst[0][0])}), kappa = {lst[0][1]}")
        print(f"  the trivial character, covers with n(1) or n(rho) > 0: {len(k1)}; by degree, (n(1), n(rho)): "
              + "; ".join(f"{d}: {dict(sorted(v.items()))}" for d, v in sorted(by_deg.items())))
        print(f"  Part P counts (pulled-back class): {dict(sorted(part_p.items()))}")
        print(f"  Part O readings (the cover's own classes): {dict(sorted(part_o.items()))}")
        report[st] = {"characters": len(N), "members": sum(caps.values()), "routes give the same caps": same_caps,
                      "caps": {str(k): v for k, v in sorted(caps.items())}, "largest min(caps)": best,
                      "members with min(caps) >= 2 or capL2 >= 3": big, "trivial character supplies": k1,
                      "Part P counts": {str(k): v for k, v in sorted(part_p.items())},
                      "Part O readings": {str(k): v for k, v in sorted(part_o.items())}}
    (HERE / "post_run_rooms.json").write_text(json.dumps(report, indent=1) + "\n")


if __name__ == "__main__":
    main()
