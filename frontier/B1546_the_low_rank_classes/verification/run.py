#!/usr/bin/env python3
"""B1546 -- THE RUN (PREREGISTRATION.md section 5): the counts at the classes of N45 where three can still live at the trivial
character, in two routes.

By Corollary F' and sm:B1544, a class reading I(W) = -3 has cup rank 1 or 2.  By Proposition L (prop_l.py) the interior classes
of cup rank <= 2 are the classes c of the 10-dimensional Kc0 whose symmetric matrix S(c) has rank <= 2; the rank-1 ones are
the squares S(c) = l l^T.  So the families are:
  Z1       the squares (interior, cup rank 1; irreducible, dimension 4);
  Z2       the classes of rank <= 2 (interior, cup rank 2 at a generic class; irreducible, dimension 7);
  X:S      a square plus a class of K0(S), for each of the ten sets S of three cusps (cup rank 1, support S);
and the run reads three generic classes of each (Lemma G''': a generic class has the least I(W) on its family), in each route,
plus the ten eigen-lines of Kc0 (u_j, w_j, v_a, v_b: special classes of Z1 and Z2), named.

Each route computes its own spaces and draws its own classes; seeds are crc32 of "B1546|route|subspace|draw".  A square is
found by solving delta1_W(c) = v (x) phi for a random vector v of the cup map's 4-dimensional image on Kc0 (lowrank_lib).
A task is (subspace, draw); it writes two rows, one per route: the count, rk delta1_W, the class's support, Lemma F's
ingredients, and in route R every connecting rank and identity.

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
CUSPS = (0, 1, 2, 4, 5)                                    # N45's cusp labels (sm:B1544)
TAU = {0: 1, 1: 4, 2: 5, 4: 2, 5: 0}                       # the deck group on the cusps (sm:B1544)
THREE_SETS = [list(S) for S in __import__("itertools").combinations(CUSPS, 3)]
NAMED = [f"u{j}" for j in range(1, 5)] + [f"w{j}" for j in range(1, 5)] + ["va", "vb"]
# the sealed structure of each subspace: the cup rank of its (generic) class and its support
SUBSPACES = {"Z1": {"rank": 1, "support": []}, "Z2": {"rank": 2, "support": []}}
for _S in THREE_SETS:
    SUBSPACES["X:S=" + ",".join(str(x) for x in _S)] = {"rank": 1, "support": _S}
for _x in NAMED:
    SUBSPACES[_x] = {"rank": 1 if _x[0] == "u" else 2, "support": []}
_CACHE = {}


def tasks():
    return [(sub, draw) for sub in SUBSPACES for draw in range(DRAWS)]


def load(name, path):
    """a module of this arc, by path under its own name (E12)"""
    if name not in sys.modules:
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        sys.modules[name] = mod
        spec.loader.exec_module(mod)
    return sys.modules[name]


def setup():
    if not _CACHE:
        LR = load("b1546_lowrank_lib", HERE / "lowrank_lib.py")
        FL = LR.FL
        pF = FL.F().primes(1)[0]
        _CACHE["G"] = {"F": LR.Graded(FL.FCover("N45", pF)), "R": LR.Graded(FL.RCover("N45"))}
    return _CACHE["G"]


def draw(G, sub, rng):
    """one class of the subspace, in G's route (cocycle vector)"""
    p = G.p
    a = lambda: rng.randrange(1, p)
    one = lambda c: c.reshape(-1, 1) if G.F else c.reshape(1, -1)
    if sub == "Z1":
        return G.combine(one(G.rank1(G.draw_v(rng))), [a()])
    if sub == "Z2":
        c1, c2 = G.rank1(G.draw_v(rng)), G.rank1(G.draw_v(rng))
        return G.combine(G.stack(one(c1), one(c2)), [a(), a()])
    if sub.startswith("X:"):
        S = {int(x) for x in sub.split("S=")[1].split(",")}
        kap = G.reduce(G.Cv.stratum(S, G.K0))
        assert G.n(kap) == 1, ("K0(S)", sub, G.n(kap))
        c1 = G.rank1(G.draw_v(rng))
        return G.combine(G.stack(one(c1), kap), [a(), a()])
    return G.combine(G.named()[sub], [a()])


def task(t):
    sub, d = t
    t0 = time.time()
    Gs = setup()
    rows = []
    for route in ("F", "R"):
        G = Gs[route]
        rng = random.Random(zlib.crc32(f"B1546|{route}|{sub}|{d}".encode()))
        c = draw(G, sub, rng)
        rows.append({"subspace": sub, "draw": d, "route": route, "prime": G.p, "reading": G.Cv.reading(c)})
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
                done.add((r["subspace"], r["draw"]))
    todo = [t for t in tasks() if t not in done]
    print(f"B1546 run: {len(todo)} tasks to read ({len(done)} done)", flush=True)
    with get_context("spawn").Pool(workers) as pool:
        for rows, secs in pool.imap_unordered(task, todo):
            if rec:
                with open(out, "a") as f:
                    for r in rows:
                        f.write(json.dumps(r) + "\n")
            print(f"{rows[0]['subspace']} draw {rows[0]['draw']}: 2 readings, {secs} s", flush=True)


if __name__ == "__main__":
    main()
