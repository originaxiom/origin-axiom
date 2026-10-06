#!/usr/bin/env python3
"""B1544 -- THE RUN (PREREGISTRATION.md section 5): the counts at generic classes of K0(S), for every closed support S of the
cup map's kernel K0, on the five covers, in two routes.

K0 = {c in H^1(N; rho) : c u y = 0 in H^2(N; rho) for every y in H^1(N; C)}.  For a set S of cusps (labelled by the least point
of their orbit), K0(S) is the part of K0 whose restriction to every cusp outside S is a cusp coboundary; S is a closed support
when K0(S) is non-zero on every cusp of S.  The closed supports are sealed below (STRUCTURE); control K1 reads them in both
routes.  A generic class of K0(S) is non-zero on exactly the cusps of S (P2 checks it at every reading), and by Lemma G'' its
count attains the least I(W) over the classes of K0 with that support, so the readings decide the least I(W) on all of K0.

Each route computes its own K0(S) and draws its own classes; seeds are crc32 of "B1544|cover|route|subspace|draw".  A task is
(cover, subspace, draw); it writes two rows, one per route: the count (I(W), I(L2W)), rk delta1_W by the cochain formula, the
class's support, Lemma F's ingredients, and in route R every connecting rank and identity.

    python3 -u run.py [--workers k] --record    ->  run.jsonl  (resumable: tasks already in the record are skipped)"""
import importlib.util
import json
import random
import sys
import time
import zlib
from multiprocessing import get_context
from pathlib import Path

HERE = Path(__file__).resolve().parent
DRAWS = 3
# the closed supports of K0 on each cover, with dim K0(S) (both routes, control K1), and the deck group's action on the cusps
STRUCTURE = {
    "N45": {"closed": [[[0, 1, 2], 1], [[0, 1, 4], 1], [[0, 1, 5], 1], [[0, 2, 4], 1], [[0, 2, 5], 1], [[0, 4, 5], 1],
                       [[1, 2, 4], 1], [[1, 2, 5], 1], [[1, 4, 5], 1], [[2, 4, 5], 1], [[0, 1, 2, 4], 3], [[0, 1, 2, 5], 3],
                       [[0, 1, 4, 5], 3], [[0, 2, 4, 5], 3], [[1, 2, 4, 5], 3], [[0, 1, 2, 4, 5], 5]],
            "tau": {0: 1, 1: 4, 2: 5, 4: 2, 5: 0}},
    "d10.13": {"closed": [[[], 3], [[0, 1, 3, 5], 4], [[0, 1, 7, 13], 4], [[3, 5, 7, 13], 5], [[0, 1, 3, 5, 7, 13], 6]],
               "tau": {0: 1, 1: 0, 3: 13, 5: 7, 7: 5, 13: 3}},
    "d10.16": {"closed": [[[], 2], [[0, 1, 2, 4], 3]],
               "tau": {0: 0, 1: 1, 2: 4, 4: 2}},
    "d10.36": {"closed": [[[], 3], [[0, 1, 2, 7], 4], [[0, 2, 3, 8], 4], [[1, 3, 7, 8], 5], [[0, 1, 2, 3, 7, 8], 6]],
               "tau": {0: 2, 1: 8, 2: 0, 3: 7, 7: 3, 8: 1}},
    "d10.40": {"closed": [[[], 2], [[0, 1, 3, 6], 3]],
               "tau": {0: 0, 1: 3, 3: 1, 6: 6}},
}
COVERS = ("N45", "d10.13", "d10.16", "d10.36", "d10.40")
_CACHE = {}


def s_name(S):
    return "S=" + ",".join(str(x) for x in sorted(S))


def subspaces(cid):
    return [s_name(S) for S, _ in STRUCTURE[cid]["closed"]]


def tasks():
    return [(cid, sub, draw) for cid in COVERS for sub in subspaces(cid) for draw in range(DRAWS)]


def load(name, path):
    """a module of this arc, by path under its own name (E12)"""
    if name not in sys.modules:
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        sys.modules[name] = mod
        spec.loader.exec_module(mod)
    return sys.modules[name]


def setup(cid):
    if cid not in _CACHE:
        _CACHE.clear()                                  # one cover per process at a time (memory)
        FL = load("b1544_floor_lib", HERE / "floor_lib.py")
        pF = FL.F().primes(1)[0]
        _CACHE[cid] = (FL.FCover(cid, pF), FL.RCover(cid))
    return _CACHE[cid]


def task(t):
    cid, sub, draw = t
    t0 = time.time()
    fc, rc = setup(cid)
    rows = []
    for route, Cv in (("F", fc), ("R", rc)):
        rng = random.Random(zlib.crc32(f"B1544|{cid}|{route}|{sub}|{draw}".encode()))
        B = Cv.subspace(sub)
        c = Cv.draw(B, rng)
        rows.append({"cover": cid, "subspace": sub, "draw": draw, "route": route, "prime": Cv.p,
                     "reading": Cv.reading(c)})
    return rows, round(time.time() - t0, 1)


def main():
    args = sys.argv[1:]
    workers = int(args[args.index("--workers") + 1]) if "--workers" in args else 1
    rec = "--record" in args
    out = HERE / "run.jsonl"
    done = set()
    if out.exists():
        for line in out.read_text().splitlines():
            if line.strip():
                r = json.loads(line)
                done.add((r["cover"], r["subspace"], r["draw"]))
    todo = [t for t in tasks() if t not in done]
    print(f"B1544 run: {len(todo)} tasks to read ({len(done)} done)", flush=True)
    with get_context("spawn").Pool(workers) as pool:
        for rows, secs in pool.imap_unordered(task, todo):
            if rec:
                with open(out, "a") as f:
                    for r in rows:
                        f.write(json.dumps(r) + "\n")
            print(f"{rows[0]['cover']} {rows[0]['subspace']} draw {rows[0]['draw']}: 2 readings, {secs} s", flush=True)


if __name__ == "__main__":
    main()
