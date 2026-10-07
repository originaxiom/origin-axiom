#!/usr/bin/env python3
"""B1548 -- controls K1-K9, before the seal.  No count is read here except at the trivial character, whose count is banked
(sm:B1541's generic interior class of N45, (4, -10)).  Everything else is structure.

  K1  the population in each route on its own (run.setup): the circle's direction in the route's basis, solved from W_CIRCLE;
      its order-2 point is the route's own chi0 and its order-3 points are room-three in the route's own census; the members'
      orders and keys in order (equal sha-256 in both routes); phi(m) members of each order.
  K2  every member, in both routes: trivial on every cusp (its values on each cusp's peripheral loops are 0 mod m), of exact
      order m, and on the circle (its key is j W_CIRCLE mod m for a unit j; so nu^4 lies on it too).
  K3  the deck group: tau maps each of the five circles' directions to another's, up to sign (route R), so the five are one
      orbit; at four sample members (route R), tau*nu has nu's structure and stratum dimensions.
  K4  Lemma Gamma's input: only zeta_24^0 and zeta_24^4 in the holonomy, |det| rational; the Galois classes run.galois_rep
      uses (one class per order when 12 does not divide it, two when it does).
  K5  the trivial character (banked), in both routes: the structure (23, 18, 9, 4, 5, 0) and a generic interior class's count
      (4, -10).
  K6  the strata at the first member of each order (twelve members), in both routes: the structure, n(nu^4), every X_U's
      dimension and the distinct strata agree; X_{} is K0's interior part; each distinct stratum's generic class has support
      exactly U.
  K7  the read-out on synthetic rows (read_out.selftest).
  K8  sm:B1547's member_lib, which this arc loads by path, is the sealed one (its sha-256 against sm:B1547's
      ARTIFACT_HASHES.txt).
  K9  the circles (the dossier's census, re-run in route R): at orders 2 to 5 the characters of the free part with n >= 3 are
      exactly the points of the five circles, each with n = 3.

    python3 controls.py [--record]   ->  controls.json"""
import hashlib
import importlib.util
import itertools
import json
import random
import sys
import time
import zlib
from fractions import Fraction
from math import gcd
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
B1547 = ROOT / "frontier" / "B1547_the_room_three_members"


def load(name, path):
    """a module of this arc, by path under its own name (E12)"""
    if name not in sys.modules:
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        sys.modules[name] = mod
        spec.loader.exec_module(mod)
    return sys.modules[name]


def sha(s):
    return hashlib.sha256(s.encode()).hexdigest()


def k1(RUN):
    out = {}
    for route in ("R", "F"):
        C = RUN.setup(route)
        mem = C["members"]
        per = {}
        for m, _, _ in mem:
            per[str(m)] = per.get(str(m), 0) + 1
        out[route] = {"direction": list(C["direction"]), "chi0": RUN.key_str(C["chi0"]), "members": len(mem),
                      "members by order": per,
                      "member orders and keys in order (sha-256)": sha("\n".join(f"{m}:{RUN.key_str(k)}" for m, k, _ in mem))}
    phi = {str(m): sum(1 for j in range(1, m) if gcd(j, m) == 1) for m in RUN.ORDERS}
    a, b = out["R"], out["F"]
    out["holds"] = (a["chi0"] == b["chi0"] and a["members"] == b["members"] == RUN.MEMBERS
                    and a["member orders and keys in order (sha-256)"] == b["member orders and keys in order (sha-256)"]
                    and a["members by order"] == b["members by order"] == phi)
    return out


def f_walk(cov, e, x, w, m):
    tot = 0
    for c in w:
        g = c.lower()
        if c.islower():
            tot += int(e[cov.edge(x, g)])
            x = cov.P[g][x]
        else:
            z = cov.P[c][x]
            tot -= int(e[cov.edge(z, g)])
            x = z
    return tot % m, x


def k2(RUN):
    out = {}
    for route in ("R", "F"):
        C = RUN.setup(route)
        cv = C["cover"]
        W = RUN.W_CIRCLE
        bad_cusp = bad_order = bad_circle = 0
        for m, key, e in C["members"]:
            if route == "R":
                vals = [sum(s * int(e[i]) for i, s in w) % m for ws in cv.cov.cusps for w in ws]
            else:
                vals = []
                for cu in cv.cov.cusps:
                    for w in cu["loops"]:
                        v, end = f_walk(cv.cov, e, cu["x"], w, m)
                        assert end == cu["x"]
                        vals.append(v)
            bad_cusp += any(vals)
            g = m
            for x in key:
                g = gcd(g, x)
            bad_order += g != 1
            # on the circle: the key is j W mod m for a unit j (then nu^4 = 4j W / m lies on it too)
            bad_circle += not any(tuple(key) == tuple((j * x) % m for x in W) for j in range(1, m) if gcd(j, m) == 1)
        out[route] = {"members": len(C["members"]), "not trivial on a cusp": bad_cusp, "not of exact order": bad_order,
                      "off the circle": bad_circle}
    out["holds"] = all(out[r]["not trivial on a cusp"] == 0 and out[r]["not of exact order"] == 0
                       and out[r]["off the circle"] == 0 for r in ("R", "F"))
    return out


def k3(RUN):
    C = RUN.setup("R")
    CL, ML, rc, CH = C["CL"], C["ML"], C["cover"], C["chars"]
    loops = ML.common_loops({g: list(rc.cov.P[g]) for g in ("a", "t")})
    d = CL.directions(CH, rc, "R", loops)
    dirs = [tuple(v) for _, v in d]
    Mt = CH.tau()
    images = []
    for v in dirs:
        im = tuple(int(x) for x in Mt @ np.array(v))
        hit = [u for u in dirs if im == u or im == tuple(-x for x in u)]
        images.append(len(hit) == 1 and hit[0] != v)
    # tau on the sample members' exponent vectors
    p = rc.p
    one = {g: np.eye(1, dtype=np.int64) for g in rc.rho}
    TL = ML.FL.N45L().deck_R_matrix(rc.cov, one, rc.tau, p, e=1)
    TL = np.where(TL > p // 2, TL - p, TL).astype(np.int64)
    rows = []
    for i in (0, 2, 6, 10):
        m, key, e = C["members"][i]
        et = (TL @ np.asarray(e, dtype=np.int64)) % m
        M, Mtau = CL.member(rc, "R", e, m), CL.member(rc, "R", et, m)
        d1 = sorted(d for d, _ in ML.strata(M).values())
        d2 = sorted(d for d, _ in ML.strata(Mtau).values())
        rows.append({"member": i, "order": m, "the same structure": M.structure() == Mtau.structure(),
                     "the same stratum dimensions (as multisets)": d1 == d2})
    out = {"directions (route R)": [list(v) for v in dirs], "tau maps each direction to another (up to sign)": images,
           "tau*nu at sample members (route R)": rows}
    out["holds"] = all(images) and all(r["the same structure"] and r["the same stratum dimensions (as multisets)"] for r in rows)
    return out


def k4(RUN):
    RF = load("b1548_route_f_k4", ROOT / "frontier" / "B1541_the_count_on_the_room" / "verification" / "route_f.py")
    d = json.loads((ROOT / "frontier" / "B1541_the_count_on_the_room" / "verification" / "route_f_input_n45.json").read_text())
    S = RF.State(d)
    powers = set()
    for g in "abt":
        for row in S.hol[g]:
            for x in row:
                powers |= {i for i, c in enumerate(x) if c}
    absdet = {g: [str(c) for c in RF.abs_det(S.hol[g])] for g in "abt"}
    rational = all(all(Fraction(c) == 0 for c in v[1:]) for v in absdet.values())
    C = RUN.setup("R")
    classes = {}
    for m, key, _ in C["members"]:
        classes.setdefault(str(m), set()).add(RUN.galois_rep(key, m))
    ncls = {m: len(v) for m, v in classes.items()}
    want = {str(m): (2 if m % 12 == 0 else 1) for m in RUN.ORDERS}
    out = {"powers of zeta_24 in the holonomy": sorted(powers), "|det| rational": rational, "Galois classes by order": ncls}
    out["holds"] = powers <= {0, 4} and rational and ncls == want
    return out


def k5(RUN):
    out = {}
    for route in ("R", "F"):
        C = RUN.setup(route)
        ML, cv = C["ML"], C["cover"]
        if route == "R":
            M = ML.RMember(cv, [1] * cv.ng)
        else:
            M = ML.FMember(cv, {(x, g): 1 for x in range(cv.cov.d) for g in cv.cov.gens})
        rng = random.Random(zlib.crc32(f"B1548|K5|{route}".encode()))
        out[route] = {"structure": M.structure(), "a generic interior class's count": M.reading(M.draw(M.Cint, rng))["count"]}
    want = {"structure": {"h1(nu^5 rho)": 23, "n(nu^5 rho)": 18, "h1(L)": 9, "n(L)": 4, "dim K0": 5, "dim K0 interior": 0},
            "a generic interior class's count": [4, -10]}
    out["holds"] = out["R"] == out["F"] == want
    return out


def k6(RUN):
    firsts, seen = [], set()
    for i, (m, _, _) in enumerate(RUN.setup("R")["members"]):
        if m not in seen:
            seen.add(m)
            firsts.append(i)
    rows = []
    for i in firsts:
        r = {"member": i}
        for route in ("R", "F"):
            C = RUN.setup(route)
            CL, ML, cv, CH = C["CL"], C["ML"], C["cover"], C["chars"]
            m, key, e = C["members"][i]
            M = CL.member(cv, route, e, m)
            st = ML.strata(M)
            dims = {U: d for U, (d, _) in st.items()}
            dist = ML.distinct_strata(dims)
            supp = {}
            for U in dist:
                rng = random.Random(zlib.crc32(f"B1548|K6|{route}|{m}|{RUN.key_str(key)}|{U}".encode()))
                supp[U] = M.support(M.draw(st[U][1], rng))
            s = M.structure()
            r[route] = {"order": m, "key": RUN.key_str(key), "n(nu^4)": CL.line_n(CH, cv, route, (4 * e) % m, m),
                        "structure": s, "strata": dims, "distinct": dist,
                        "X_{} is K0's interior part": dims[""] == s["dim K0 interior"],
                        "generic supports are U": all(tuple(supp[U]) == (tuple(int(x) for x in U.split(",")) if U else ())
                                                      for U in dist)}
        r["routes agree"] = r["R"] == r["F"]
        rows.append(r)
    return {"members": rows, "holds": all(r["routes agree"] and r["R"]["X_{} is K0's interior part"]
                                          and r["R"]["generic supports are U"] and r["R"]["n(nu^4)"] == 3 for r in rows)}


def k7():
    RO = load("b1548_read_out_k7", HERE / "read_out.py")
    return RO.selftest()


def k8():
    want = None
    for line in (B1547 / "ARTIFACT_HASHES.txt").read_text().splitlines():
        if line.strip().endswith("verification/member_lib.py"):
            want = line.split()[0]
    got = hashlib.sha256((B1547 / "verification" / "member_lib.py").read_bytes()).hexdigest()
    return {"sealed (sm:B1547)": want, "now": got, "holds": want is not None and want == got}


def k9(RUN):
    C = RUN.setup("R")
    CL, ML, rc, CH = C["CL"], C["ML"], C["cover"], C["chars"]
    loops = ML.common_loops({g: list(rc.cov.P[g]) for g in ("a", "t")})
    dirs = [tuple(v) for _, v in CL.directions(CH, rc, "R", loops)]
    out = {}
    ok = True
    for m in (2, 3, 4, 5):
        found = []
        for a in itertools.product(range(m), repeat=CH.F.shape[0]):
            g = m
            for x in a:
                g = gcd(g, x)
            if g != 1:
                continue
            n = CL.line_n(CH, rc, "R", CL.exponents(CH, a, m), m)
            if n >= 3:
                found.append((a, n))
        on = {tuple((j * x) % m for x in v) for v in dirs for j in range(1, m) if gcd(j, m) == 1}
        out[str(m)] = {"characters with n >= 3": len(found), "all with n = 3": all(n == 3 for _, n in found),
                       "exactly the circles' points": {a for a, _ in found} == on}
        ok = ok and out[str(m)]["all with n = 3"] and out[str(m)]["exactly the circles' points"]
    out["holds"] = ok
    return out


def main():
    t0 = time.time()
    RUN = load("b1548_run_controls", HERE / "run.py")
    rep = {}
    for name, fn in (("K1", lambda: k1(RUN)), ("K2", lambda: k2(RUN)), ("K3", lambda: k3(RUN)), ("K4", lambda: k4(RUN)),
                     ("K5", lambda: k5(RUN)), ("K6", lambda: k6(RUN)), ("K7", k7), ("K8", k8), ("K9", lambda: k9(RUN))):
        t1 = time.time()
        rep[name] = fn()
        rep[name]["seconds"] = round(time.time() - t1, 1)
        print(name, rep[name]["holds"], rep[name]["seconds"], flush=True)
    rep["all hold"] = all(rep[k]["holds"] for k in ("K1", "K2", "K3", "K4", "K5", "K6", "K7", "K8", "K9"))
    rep["seconds"] = round(time.time() - t0, 1)
    print(json.dumps({k: (v["holds"] if isinstance(v, dict) and "holds" in v else v) for k, v in rep.items()}), flush=True)
    if "--record" in sys.argv:
        (HERE / "controls.json").write_text(json.dumps(rep, indent=1, default=str) + "\n")
    return rep


if __name__ == "__main__":
    main()
