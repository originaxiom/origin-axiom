#!/usr/bin/env python3
"""B1548 -- THE RUN (PREREGISTRATION.md section 5): the counts at the members on N45's room-three circle through chi0, in two
routes.

The circle is the homomorphism phi : pi_1(N45) -> Z whose values on the 46 common loops are W_CIRCLE (found in route R by the
census of the dossier and the controls; sealed here).  Each route solves for phi in its own lattice basis (circle_lib.
solve_direction) and checks it at setup: its order-2 point is the route's own chi0, its order-3 points are room-three
characters in the route's own census, and phi is primitive.  The members are the points nu = exp(2 pi i j phi / m) of exact order
m, for m in ORDERS (orders dividing 600, not dividing 4: b0 = 0, and nu^4 lies on the circle, so the room is exactly three).
They are taken in the order (m, key); the i-th member is the same character in both routes.

At a member, as in sm:B1547 (Corollary 1 and Lemma G, unchanged), a class reading I(W1) = -3 lies in a distinct stratum
X_U = K0^nu ∩ {c vanishes off U}, |U| <= 2, and the generic class of each distinct stratum has the least counts on the classes of
support U.  A task is (route, member); it writes one row: the member's order and key, its structure, n(nu^4), the sixteen
strata's dimensions, the distinct strata and three readings at each, and in route R the load-bearing checks at a generic class
of K0^nu and of H^1.  Seeds are crc32 of "B1548|route|m|key|U|draw" (and "|K0|0", "|H1|0").  No count is printed.

    python3 -u run.py [--workers k] --record    ->  run.jsonl  (resumable: tasks already in the record are skipped)"""
import importlib.util
import json
import random
import sys
import time
import zlib
from math import gcd
from multiprocessing import get_context
from pathlib import Path

HERE = Path(__file__).resolve().parent
DRAWS = 3
ROUTES = ("R", "F")
ORDERS = (3, 5, 6, 8, 10, 12, 15, 20, 24, 30, 40, 60)
MEMBERS = sum(sum(1 for j in range(1, m) if gcd(j, m) == 1) for m in ORDERS)
# sealed: the circle's values on the 46 common loops (route R's census: the circle through chi0; controls.json, K1)
W_CIRCLE = (0, 0, 1, 0, -1, -1, 1, -1, 0, -2, 0, 0, 1, 0, 0, -1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, -2, -3, -2, 0, 0,
             0, 1, 0, 0, 1, 0, -1, -2, 2, 3, 0, 0, 0, 0, 1)
_CACHE = {}


def tasks():
    """(route, member index), the two routes interleaved"""
    return [(route, i) for i in range(MEMBERS) for route in ROUTES]


def load(name, path):
    """a module of this arc, by path under its own name (E12)"""
    if name not in sys.modules:
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        sys.modules[name] = mod
        spec.loader.exec_module(mod)
    return sys.modules[name]


def galois_rep(key, m):
    """the least key in the member's Galois class: nu -> nu^k over the automorphisms that fix sqrt 3 (Lemma Gamma): every unit k
    mod m when 12 does not divide m, else the k = +-1 mod 12"""
    units = [k for k in range(1, m) if gcd(k, m) == 1 and (m % 12 or k % 12 in (1, 11))]
    return min(tuple((k * x) % m for x in key) for k in units)


def setup(route):
    if route not in _CACHE:
        CL = load("b1548_circle_lib", HERE / "circle_lib.py")
        ML, FL = CL.ML, CL.FL
        if route == "R":
            cv = FL.RCover("N45")
            CH = ML.RChars(cv)
        else:
            cv = FL.FCover("N45", FL.F().primes(1)[0])
            CH = ML.FChars(cv)
        loops = ML.common_loops({g: list(cv.cov.P[g]) for g in ("a", "t")})
        v = CL.solve_direction(CH, W_CIRCLE, loops)
        r2, _ = ML.room3(CH, loops)
        chi0 = r2[0][0]
        assert CH.values(CL.exponents(CH, v, 2), loops, 2) == chi0, "the circle's order-2 point is not this route's chi0"
        l3 = CL.room_lines(CH, cv, route, 3)
        assert any(tuple(x % 3 for x in v) in L for L in l3), "the circle's order-3 points are not room-three here"
        g = 0
        for x in v:
            g = gcd(g, abs(x))
        assert g == 1, "the circle's direction is not primitive"
        mem = []
        for m in ORDERS:
            for key, e in CL.circle_points(CH, loops, v, m):
                mem.append((m, key, e))
        assert len(mem) == MEMBERS
        _CACHE[route] = {"CL": CL, "ML": ML, "cover": cv, "chars": CH, "chi0": chi0, "direction": v, "members": mem}
    return _CACHE[route]


def key_str(key):
    return "".join(str(int(x)) + "." for x in key)


def task(t):
    route, i = t
    t0 = time.time()
    C = setup(route)
    CL, ML, cv, CH = C["CL"], C["ML"], C["cover"], C["chars"]
    m, key, e = C["members"][i]
    ks = key_str(key)
    M = CL.member(cv, route, e, m)
    room = CL.line_n(CH, cv, route, (4 * e) % m, m)
    st = ML.strata(M)
    dims = {U: d for U, (d, _) in st.items()}
    dist = ML.distinct_strata(dims)
    readings = {}
    for U in dist:
        rs = []
        for d in range(DRAWS):
            rng = random.Random(zlib.crc32(f"B1548|{route}|{m}|{ks}|{U}|{d}".encode()))
            rs.append(M.reading(M.draw(st[U][1], rng)))
        readings[U] = rs
    checks = {}
    if route == "R":
        K = M.K0()
        if M.dim_mod(K) > 0:
            checks["K0"] = M.reading(M.draw(K, random.Random(zlib.crc32(f"B1548|R|{m}|{ks}|K0|0".encode()))))
        checks["H1"] = M.reading(M.draw(M.Cs, random.Random(zlib.crc32(f"B1548|R|{m}|{ks}|H1|0".encode()))))
    row = {"route": route, "index": i, "order": m, "key": ks, "galois rep": key_str(galois_rep(key, m)),
           "chi0": key_str(C["chi0"]), "prime": int(cv.p), "n(nu^4)": room, "structure": M.structure(), "strata": dims,
           "distinct": dist, "readings": readings, "checks": checks}
    return row, round(time.time() - t0, 1)


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
                done.add((r["route"], r["index"]))
    todo = [t for t in tasks() if t not in done]
    print(f"B1548 run: {len(todo)} tasks to read ({len(done)} done)", flush=True)
    n = len(done)
    with get_context("spawn").Pool(workers) as pool:
        for row, secs in pool.imap_unordered(task, todo):
            if rec:
                with open(out, "a") as f:
                    f.write(json.dumps(row) + "\n")
            n += 1
            nr = sum(len(v) for v in row["readings"].values())
            print(f"{n}/{2 * MEMBERS}: route {row['route']} member {row['index']} (order {row['order']}): "
                  f"{len(row['distinct'])} strata, {nr} readings, {secs} s", flush=True)


if __name__ == "__main__":
    main()
