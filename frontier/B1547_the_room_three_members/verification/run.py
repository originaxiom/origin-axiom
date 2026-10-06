#!/usr/bin/env python3
"""B1547 -- THE RUN (PREREGISTRATION.md section 5): the counts at the room-three members' classes where three can live, in two
routes.

A room-three member is a character nu of pi_1(N45) of order 8, trivial on every cusp, with nu^4 = chi0: chi0 is the room-3
order-2 character (n(chi0) = 3) with the least key among the five, and the five are one tau-orbit (control K3).  There are 1024
members.  Each route finds its own characters and members, and names each member by its key, its values (mod 8) on the 46
common loops; the members are taken in the order of their keys, so the i-th member is the same character in both routes
(control K1).

At a member, by Theorem C (ii) and Lemma F' (PREREGISTRATION section 3.2), a class reading I(W1) = -3 lies in K0^nu
(the cup map's kernel) and vanishes on at least three of the five cusps: it lies in a stratum
X_U = K0^nu ∩ {c : c vanishes off U}, |U| <= 2, and its support is U.  On the classes of support U the least I(W1) is the
generic class's (Lemma G).  So the run reads, at each member, the generic class of each distinct stratum (X_U with
dim X_U > 0 and larger than every X_U' with U' strictly inside U), three draws each.

A task is (route, member); it writes one row: the member's key and Galois class, its structure, the dimension of every X_U
(16 sets U), the distinct strata, and at each distinct stratum the three readings (the count, rk delta1_W, the class's support,
and in route R every connecting rank and identity).  In route R the row also carries the load-bearing checks (P9): one reading
at a generic class of K0^nu (when it is not zero) and one at a generic class of H^1(N; nu^5 rho), where Theorem C's cap
I(W1) >= rk delta1_W - 3 and Lemma F' (I(W1) >= k - 5) exclude three; the design relies on both for every class it does not
read.  Seeds are crc32 of "B1547|route|key|U|draw" (and "B1547|R|key|K0|0", "B1547|R|key|H1|0").  No count is printed.

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
MEMBERS = 1024
ROUTES = ("R", "F")
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


def setup(route):
    if route not in _CACHE:
        ML = load("b1547_member_lib", HERE / "member_lib.py")
        FL = ML.FL
        if route == "R":
            cv = FL.RCover("N45")
            CH = ML.RChars(cv)
        else:
            cv = FL.FCover("N45", FL.F().primes(1)[0])
            CH = ML.FChars(cv)
        loops = ML.common_loops({g: list(cv.cov.P[g]) for g in ("a", "t")})
        k0, mem = ML.population(CH, loops)
        assert len(mem) == MEMBERS and len({k for k, _ in mem}) == MEMBERS
        _CACHE[route] = {"ML": ML, "cover": cv, "chars": CH, "chi0": k0, "members": mem}
    return _CACHE[route]


def key_str(key):
    return "".join(str(int(x)) for x in key)


def task(t):
    route, i = t
    t0 = time.time()
    C = setup(route)
    ML, cv, CH = C["ML"], C["cover"], C["chars"]
    key, e = C["members"][i]
    ks = key_str(key)
    M = ML.RMember(cv, CH.nu(e)) if route == "R" else ML.FMember(cv, CH.nu(e))
    st = ML.strata(M)
    dims = {U: d for U, (d, _) in st.items()}
    dist = ML.distinct_strata(dims)
    readings = {}
    for U in dist:
        rs = []
        for d in range(DRAWS):
            rng = random.Random(zlib.crc32(f"B1547|{route}|{ks}|{U}|{d}".encode()))
            rs.append(M.reading(M.draw(st[U][1], rng)))
        readings[U] = rs
    checks = {}
    if route == "R":
        K = M.K0()
        if M.dim_mod(K) > 0:
            checks["K0"] = M.reading(M.draw(K, random.Random(zlib.crc32(f"B1547|R|{ks}|K0|0".encode()))))
        checks["H1"] = M.reading(M.draw(M.Cs, random.Random(zlib.crc32(f"B1547|R|{ks}|H1|0".encode()))))
    row = {"route": route, "index": i, "key": ks, "galois rep": key_str(ML.galois_rep(key)), "chi0": key_str(C["chi0"]),
           "prime": int(cv.p), "structure": M.structure(), "strata": dims, "distinct": dist, "readings": readings,
           "checks": checks}
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
    print(f"B1547 run: {len(todo)} tasks to read ({len(done)} done)", flush=True)
    n = len(done)
    with get_context("spawn").Pool(workers) as pool:
        for row, secs in pool.imap_unordered(task, todo):
            if rec:
                with open(out, "a") as f:
                    f.write(json.dumps(row) + "\n")
            n += 1
            nr = sum(len(v) for v in row["readings"].values())
            print(f"{n}/{2 * MEMBERS}: route {row['route']} member {row['index']}: {len(row['distinct'])} strata, "
                  f"{nr} readings, {secs} s", flush=True)


if __name__ == "__main__":
    main()
