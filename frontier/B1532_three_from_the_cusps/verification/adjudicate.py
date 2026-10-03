#!/usr/bin/env python3
"""B1532 -- the adjudication (PREREGISTRATION section 9), after read_out.py --record.

    python3 -u adjudicate.py [--record]   ->  adjudicate.json

Every (n, nu, chi) on D5's list (d5_failures.json: the two routes' rows differ, or one is missing) is read again in both routes at
sm:B1515's SECOND prime of its level (each route's own), with the sealed readers.  The four rows -- route T and route L at their
first and second primes -- are compared through read_out.row_signature (route L's signature; for a two-class member the interior
and generic terms, the pencils and the multiset of special readings).  The signature that three of the four rows share stands; a
row with no such signature is unresolved, and every count containing it is reported as unresolved."""
import json
import sys
import time
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import read_out as RO  # noqa: E402
import run_terms as RUN  # noqa: E402


def second_primes(route):
    rec = RUN.banked(route)
    return {n: rec["primes"][f"M{n}"][1] for n in RUN.LEVELS}


def main():
    t0 = time.time()
    fails = json.loads((HERE / "d5_failures.json").read_text(encoding="utf-8"))
    rows = {r: RO.load(HERE / f"terms_{r}.jsonl") for r in ("T", "L")}
    p2 = {r: second_primes(r) for r in ("T", "L")}
    ctx, out = {}, []
    for key, why in fails:
        n, nu, chi = key
        sigs = {}
        for r in ("T", "L"):
            row1 = rows[r].get((n, nu, chi))
            sigs[f"{r} first"] = RO.row_signature(r, row1) if row1 else None
            if (r, n) not in ctx:
                ctx[(r, n)] = RUN.level(r, n, p2[r][n])
            L, chars, make, one = ctx[(r, n)]
            ab = next(x for x in chars if L.label(x) == nu)
            ab_chi = next(x for x in chars if L.label(x) == chi)
            m = make(ab)
            row2 = {"kind": m.kind}
            row2.update(m.read_one(ab_chi) if m.kind == "one" else m.read_two(ab_chi))
            sigs[f"{r} second"] = RO.row_signature(r, row2)
        tally = Counter(v for v in sigs.values() if v is not None)
        best, cnt = tally.most_common(1)[0] if tally else (None, 0)
        out.append({"key": key, "why": why, "signatures": sigs, "resolved": cnt >= 3, "standing": best if cnt >= 3 else None})
        print(f"[{time.time() - t0:8.1f}s] {key}: resolved = {cnt >= 3} ({cnt} of 4 agree)", flush=True)
    rec = {"adjudicated": len(out), "unresolved": sum(not x["resolved"] for x in out), "rows": out,
           "seconds": round(time.time() - t0, 1)}
    print(json.dumps({k: v for k, v in rec.items() if k != "rows"}), flush=True)
    if "--record" in sys.argv:
        (HERE / "adjudicate.json").write_text(json.dumps(rec, indent=1, default=str) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
