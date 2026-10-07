#!/usr/bin/env python3
"""B1547 -- tables for the bank, read from the committed record after the read-out ran once (2026-10-07, 04:29:29Z).

They add no verdict. From run.jsonl.gz:
  - in each route, every distinct stratum's generic count (the least I(W1) and the least I(Lambda^2 W1) over its three
    draws, as the read-out takes it), by the member's structure and by |U|;
  - at every route R reading, the two ranks three would need at their ceiling (Corollary 1: s = rk d1(E*) = k + 3
    and t = rk d1(L2*) = k + 3), as the largest s - k and t - k reached (route F records interior dimensions, not
    connecting ranks);
  - route R's load-bearing checks (a generic class of K0 and of H^1 at every member): their counts.

    python3 post_run_tables.py   ->  post_run_tables.json beside this file"""
import collections
import gzip
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def generic(readings):
    return [min(r["count"][0] for r in readings), min(r["count"][1] for r in readings)]


def tables(rows):
    out = {}
    for route in ("R", "F"):
        rr = [r for r in rows if r["route"] == route]
        by_struct = collections.defaultdict(collections.Counter)
        by_size = collections.Counter()
        s_minus_k = collections.Counter()
        t_minus_k = collections.Counter()
        for r in rr:
            st = r["structure"]
            key = (st["h1(nu^5 rho)"], st["n(nu^5 rho)"], st["dim K0"], st["dim K0 interior"])
            for U, rs in r["readings"].items():
                g = tuple(generic(rs))
                size = 0 if U == "" else len(U.split(","))
                by_struct[str(list(key))][str((size, list(g)))] += 1
                by_size[str((size, list(g)))] += 1
                for x in rs:
                    if "rk d1" in x:  # route R records the connecting ranks; route F records interior dimensions
                        s_minus_k[x["rk d1"]["E*"] - x["k"]] += 1
                        t_minus_k[x["rk d1"]["L2*"] - x["k"]] += 1
        out[route] = {
            "members": len(rr),
            "generic counts by (h1, n, dim K0, dim K0 interior)": {k: dict(v) for k, v in sorted(by_struct.items())},
            "generic counts by (|U|, count)": dict(sorted(by_size.items())),
            "s - k over every stratum reading": {str(k): v for k, v in sorted(s_minus_k.items())},
            "t - k over every stratum reading": {str(k): v for k, v in sorted(t_minus_k.items())},
            "largest s - k": max(s_minus_k) if s_minus_k else None,
            "largest t - k": max(t_minus_k) if t_minus_k else None,
        }
    checks = collections.Counter()
    for r in rows:
        if r["route"] == "R":
            for name, x in r["checks"].items():
                checks[str((name, x["count"]))] += 1
    out["R"]["load-bearing check counts (name, count)"] = dict(sorted(checks.items()))
    return out


def main():
    rows = [json.loads(x) for x in gzip.open(HERE / "run.jsonl.gz", "rt") if x.strip()]
    out = tables(rows)
    out["source"] = "run.jsonl.gz (the committed record; read_out.py ran once before these tables)"
    (HERE / "post_run_tables.json").write_text(json.dumps(out, indent=1) + "\n")
    for route in ("R", "F"):
        print(route, json.dumps(out[route]["generic counts by (|U|, count)"]), "largest s-k", out[route]["largest s - k"],
              "largest t-k", out[route]["largest t - k"])
    print(json.dumps(out["R"]["load-bearing check counts (name, count)"]))


if __name__ == "__main__":
    main()
