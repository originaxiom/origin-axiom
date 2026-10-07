#!/usr/bin/env python3
"""sm:B1552 -- the sealed read-out, run once on the complete record (run_1.jsonl and run_2.jsonl).

    python3 read_out.py   ->  read_out.json beside this file

The predictions (PREREGISTRATION.md section 7):
  P1  two routes: for every (state, module, lift index) the multiset of counts over parities, kappa and draws is the same
      in route 1 and route 2;
  P2  draws: the two draws give the same count at every reading, in each route;
  P3  the deck: in route 2 (the deck-compatible marking), at each (state, module, lift, kappa) the three parities read
      the same count;
  P4  gaps: every route-2 rank decision has a gap of at least 1e6 (the smallest kept over the largest dropped);
  P5  the question: on each of the six chiral twins (-LR, +LLLR, -LLLLLR, +LLLRLR, -LLLRRR, -LLRLRR), in a module, at
      one of its two values of kappa the three parities read (-1, -1); held per module and per state;
  P6  the six vector-like twins: recorded, no prediction.
The verdict rule: with P1-P4, PROVED as sealed if P5 holds on all six chiral twins in module (a) or in module (b);
NEGATIVE if P5 holds on no chiral twin in either module; OPEN otherwise. Without P1-P4, the run is void."""
import json
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
CHIRAL = ["-LR", "+LLLR", "-LLLLLR", "+LLLRLR", "-LLLRRR", "-LLRLRR"]
VECTOR = ["+LR", "-LLLR", "+LLLLLR", "-LLLRLR", "+LLLRRR", "+LLRLRR"]


def load(route):
    rows, done = [], set()
    for line in open(HERE / f"run_{route}.jsonl"):
        r = json.loads(line)
        if r.get("done"):
            done.add(r["state"])
        else:
            rows.append(r)
    return rows, done


def evaluate(r1, r2, done1, done2):
    out = {"complete": sorted(done1) == sorted(CHIRAL + VECTOR) == sorted(done2)}
    # P2: draws
    def draws_ok(rows):
        by = defaultdict(set)
        for r in rows:
            by[(r["state"], r["module"], r["lift"], r["parity"], r["kappa (eighths)"])].add(tuple(r["count"]))
        return all(len(v) == 1 for v in by.values()), by
    p2_1, by1 = draws_ok(r1)
    p2_2, by2 = draws_ok(r2)
    out["P2"] = bool(p2_1 and p2_2)
    # P1: multisets per (state, module, lift)
    def ms(rows):
        m = defaultdict(Counter)
        for r in rows:
            m[(r["state"], r["module"], r["lift"])][tuple(r["count"])] += 1
        return m
    m1, m2 = ms(r1), ms(r2)
    out["P1"] = bool(set(m1) == set(m2) and all(m1[k] == m2[k] for k in m1))
    # P3: the three parities alike in route 2
    by_k = defaultdict(set)
    for (s, mod, li, par, kap), v in by2.items():
        by_k[(s, mod, li, kap)].add(next(iter(v)))
    out["P3"] = bool(all(len(v) == 1 for v in by_k.values()))
    # P4: route-2 gaps
    out["P4"] = bool(all(r["worst gap"] >= 1e6 for r in r2))
    # P5: per module, per chiral twin, in route 2
    p5 = {}
    for mod in ("a", "b"):
        per = {}
        for s in CHIRAL:
            kaps = sorted({kap for (ss, mm, li, kap) in by_k if ss == s and mm == mod})
            hit = False
            for li in (0, 1):
                for kap in kaps:
                    vals = by_k.get((s, mod, li, kap))
                    if vals and vals == {(-1, -1)}:
                        hit = True
            per[s] = hit
        p5[mod] = per
    out["P5"] = p5
    # the tables
    table = {}
    for s in CHIRAL + VECTOR:
        table[s] = {mod: {f"lift {li}, kappa {kap}/8": sorted(by_k[(s, mod, li, kap)])[0]
                          for (ss, mm, li, kap) in sorted(by_k) if ss == s and mm == mod}
                    for mod in ("a", "b")}
    out["P6 and the tables (route 2, per state, module, lift, kappa: the parities' common count)"] = table
    ok = out["complete"] and out["P1"] and out["P2"] and out["P3"] and out["P4"]
    if not ok:
        out["verdict"] = "void (P1-P4 or completeness failed)"
    elif any(all(p5[m].values()) for m in p5):
        out["verdict"] = "PROVED as sealed"
    elif not any(any(p5[m].values()) for m in p5):
        out["verdict"] = "NEGATIVE as sealed"
    else:
        out["verdict"] = "OPEN as sealed"
    return out


if __name__ == "__main__":
    r1, d1 = load("1")
    r2, d2 = load("2")
    res = evaluate(r1, r2, d1, d2)
    res["readings"] = {"route 1": len(r1), "route 2": len(r2)}
    with open(HERE / "read_out.json", "w") as f:
        json.dump(res, f, indent=1)
    print(json.dumps({k: v for k, v in res.items() if not k.startswith("P6")}, indent=1))
