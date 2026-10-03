#!/usr/bin/env python3
"""B1532 -- route C after the run (P1): the cover read whole, against route T's sums of twisted terms.

    python3 -u run_route_c.py [--record]   ->  route_c_run.json

The sample (sealed):
  - on each level, the eight members first in the order of sha256("B1532 route C:<n>:<label>") (M2: its five), at every subgroup
    B with |B| <= 5, and on M5 at one subgroup of order 11 (the first in sorted order) for the first two of them;
  - at the one-class class c, or at a two-class member's interior class and generic class;
  - then every |N| = 3 hit of read_out.json with |B| <= 16, at its class (a rational special class included; a conjugate pair is
    not read by route C), and up to 20 further generation-shaped hits with |B| <= 8, the first in read_out.json's order.
Route T's sum: the sum over B of the run's route-T terms at that class (at a special class x: the special term for the chi whose
special set contains x, the generic term for the rest).  Route C: I(W1(c) (x) C[A]) and I(Lambda^2 W1(c) (x) C[A]) at one class:
the generic class is read at the first of the member's generic seeds that is special for no chi in B."""
import hashlib
import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import cover_lib_t as CT  # noqa: E402
import read_out as RO  # noqa: E402
import route_c as RC  # noqa: E402
import run_terms as RUN  # noqa: E402


def sample_members(n, labels):
    return sorted(labels, key=lambda x: hashlib.sha256(f"B1532 route C:{n}:{x}".encode()).hexdigest())[:8]


def tsum(rows, n, nu, B, cname, pt=None):
    w = l = 0
    for chi in B:
        r = rows[(n, nu, chi)]
        if r["kind"] == "one":
            t = r["c"]
        elif cname == "int":
            t = r["int"]
        elif cname == "gen":
            t = r["gen"][1]
        else:
            t = next((tt for p, f, tt in r["special"] if p == pt), r["gen"][1])
        w, l = w + t[0][0], l + t[1][0]
    return [w, l]


def main():
    t0 = time.time()
    rows = RO.load(HERE / "terms_T.jsonl")
    ps = RUN.primes("T")
    jobs = []
    for n in RUN.LEVELS:
        labels = sorted({k[2] for k in rows if k[0] == n})
        subs = RO.subgroups(labels)
        small = sorted((B for B in subs if len(B) <= 5), key=lambda B: (len(B), sorted(B)))
        mem = sample_members(n, labels)
        for i, nu in enumerate(mem):
            kind = rows[(n, nu, "0,0")]["kind"]
            for cname in (("c1",) if kind == "one" else ("int", "gen")):
                for B in small:
                    jobs.append((n, nu, cname, sorted(B), None, "sample"))
                if n == 5 and i < 2:
                    B11 = sorted((B for B in subs if len(B) == 11), key=sorted)[0]
                    jobs.append((n, nu, cname, sorted(B11), None, "sample"))
    ro = HERE / "read_out.json"
    if ro.exists():
        cen = json.loads(ro.read_text())["census"]["T"]
        shaped = cen["generation-shaped"]
        three = [x for x in shaped if abs(x["N"]) == 3 and x["|B|"] <= 16]
        other = [x for x in shaped if abs(x["N"]) != 3 and x["|B|"] <= 8][:20]
        for x in three + other:
            if isinstance(x["class"], str):
                jobs.append((x["n"], x["nu"], x["class"], x["B"], None, "hit"))
            else:
                pt = x["class"][1]
                if pt[0] == "r":
                    jobs.append((x["n"], x["nu"], "special", x["B"], pt, "hit"))
    out, ctx = [], {}
    for n, nu, cname, B, pt, why in jobs:
        if n not in ctx:
            ctx = {n: CT.LevelT(n, ps[n])}
        LT = ctx[n]
        ab = next(x for x in LT.chars if LT.label(x) == nu)
        m = CT.MemberT(LT, ab)
        if cname == "c1":
            c = m.c_one
        elif cname == "int":
            c = m.c_int
        elif cname == "gen":
            spec = {p[1] for chi in B for p, f, t in rows[(n, nu, chi)]["special"] if p[0] == "r"}
            c = m.cls_at(next(s for s in m.s_gen if s not in spec))
        else:
            c = m.cls_at(pt[1])
        got = RC.cover_index(LT, m, c, B)
        want = tsum(rows, n, nu, B, cname, pt)
        agree = [got[0][0], got[1][0]] == want
        out.append({"n": n, "nu": nu, "class": cname, "point": pt, "|B|": len(B), "B": B, "route C": [got[0][0], got[1][0]],
                    "route T sum": want, "agree": agree, "why": why, "route C data": got})
        print(f"[{time.time() - t0:8.1f}s] M{n} {nu} {cname} |B| = {len(B)}: C {got[0][0]},{got[1][0]} T {want} {agree}",
              flush=True)
    rec = {"readings": len(out), "all agree": all(x["agree"] for x in out), "rows": out, "seconds": round(time.time() - t0, 1)}
    print(json.dumps({k: v for k, v in rec.items() if k != "rows"}), flush=True)
    if "--record" in sys.argv:
        (HERE / "route_c_run.json").write_text(json.dumps(rec, indent=1, default=str) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
