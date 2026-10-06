#!/usr/bin/env python3
"""B1547 -- controls K1-K8, before the seal.  No count is read here except at the trivial character, whose count is banked
(sm:B1541's generic interior class of N45, (4, -10), reproduced by sm:B1546's control K3).  Everything else is structure.

  K1  the population, in each route on its own (run.setup): the 46 common loops (the same words in both routes), the n of the
      fifteen order-2 characters of the free part (ten 1s, five 3s), the five room-3 characters' keys, chi0, and the 1024
      members' keys in order (sha-256 of the list); 256 Galois classes of size 4.  The routes must agree.
  K2  every member, in both routes: trivial on every cusp (its values on each cusp's two peripheral loops are 0 mod 8); of
      order 8 with nu^4 = chi0 (its key mod 2 is chi0's key).
  K3  the deck group tau: of order 5 on the free lattice, and the five room-3 characters are one tau-orbit (both routes); at the
      eight sample members (route R), tau*nu is a member over a room-3 character other than chi0, with nu's structure and
      strata.
  K4  Galois invariance (PREREGISTRATION section 2, Lemma Γ): the holonomy's entries lie in Q(zeta_6) (only zeta_24^0 and
      zeta_24^4 appear) and |det| is rational for a, b and t, so the four is defined over Q(sqrt 3); for each odd k mod 8 some
      j in (Z/24)^* has j = k mod 8 and j = +-1 mod 12 (it fixes sqrt 3 and sends zeta_8 to zeta_8^k).
  K5  the trivial character (banked), in both routes: the structure (23, 18, 9, 4, 5, 0) and a generic interior class's count
      (4, -10).
  K6  the strata at the eight sample members (the first four, in key order, with a distinct stratum off the interior, and the
      first four whose only distinct stratum is the interior), in both routes: the structure, every X_U's dimension and the
      distinct strata agree; X_{} has the dimension of K0's interior part (k0_interior); at each distinct stratum a generic
      class has support exactly U.
  K7  the read-out on synthetic rows (read_out.selftest).
  K8  route F's class_basis (one reduction) picks the columns that adding them one at a time while the rank grows picks, on
      four inputs (the trivial character's classes of the four and of the line, a vanishing space, a member's classes).

    python3 controls.py [--record]   ->  controls.json"""
import hashlib
import importlib.util
import json
import random
import sys
import time
import zlib
from collections import Counter
from fractions import Fraction
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SAMPLE_OFF, SAMPLE_INT = 4, 4


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


def f_walk(cov, e, x, w, m):
    """route F: the value (mod m) of the character with edge exponents e on the path w from sheet x, and its end"""
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


def k1(RUN):
    out = {}
    for route in ("R", "F"):
        C = RUN.setup(route)
        ML, cv, CH = C["ML"], C["cover"], C["chars"]
        loops = ML.common_loops({g: list(cv.cov.P[g]) for g in ("a", "t")})
        r3, ns = ML.room3(CH, loops)
        keys = [k for k, _ in C["members"]]
        gal = Counter(ML.galois_rep(k) for k in keys)
        out[route] = {"loops": len(loops), "loops (sha-256)": sha("\n".join(loops)), "n of the fifteen": ns,
                      "room-3 keys": [RUN.key_str(k) for k, _ in r3], "chi0": RUN.key_str(C["chi0"]), "members": len(keys),
                      "member keys in order (sha-256)": sha("\n".join(RUN.key_str(k) for k in keys)),
                      "Galois classes by size": {str(s): c for s, c in sorted(Counter(gal.values()).items())}}
    a = out["R"]
    out["holds"] = (out["R"] == out["F"] and a["loops"] == 46 and a["n of the fifteen"] == [1] * 10 + [3] * 5
                    and len(a["room-3 keys"]) == 5 and a["chi0"] == a["room-3 keys"][0] and a["members"] == 1024
                    and a["Galois classes by size"] == {"4": 256})
    return out


def k2(RUN):
    out = {}
    for route in ("R", "F"):
        C = RUN.setup(route)
        cv = C["cover"]
        chi0 = tuple(C["chi0"])
        bad_cusp, bad_chi, bad_order = 0, 0, 0
        for key, e in C["members"]:
            if route == "R":
                vals = [sum(s * int(e[i]) for i, s in w) % 8 for ws in cv.cov.cusps for w in ws]
            else:
                vals = []
                for cu in cv.cov.cusps:
                    for w in cu["loops"]:
                        v, end = f_walk(cv.cov, e, cu["x"], w, 8)
                        assert end == cu["x"]
                        vals.append(v)
            bad_cusp += any(vals)
            bad_chi += tuple(x % 2 for x in key) != chi0
            bad_order += not any(x % 2 for x in key)
        out[route] = {"members": len(C["members"]), "cusps": len(cv.cov.cusps), "not trivial on a cusp": bad_cusp,
                      "nu^4 not chi0": bad_chi, "not of order 8": bad_order}
    out["holds"] = all(out[r] == {"members": 1024, "cusps": 5, "not trivial on a cusp": 0, "nu^4 not chi0": 0,
                                  "not of order 8": 0} for r in ("R", "F"))
    return out


def sample(RUN):
    """the eight sample members (route R, structure only): the first four in key order with a distinct stratum off the
    interior, and the first four whose only distinct stratum is the interior"""
    C = RUN.setup("R")
    ML, cv, CH = C["ML"], C["cover"], C["chars"]
    off, inner = [], []
    for i, (key, e) in enumerate(C["members"]):
        if len(off) == SAMPLE_OFF and len(inner) == SAMPLE_INT:
            break
        M = ML.RMember(cv, CH.nu(e))
        dims = {U: d for U, (d, _) in ML.strata(M).items()}
        dist = ML.distinct_strata(dims)
        if any(U for U in dist) and len(off) < SAMPLE_OFF:
            off.append(i)
        elif dist == [""] and len(inner) < SAMPLE_INT:
            inner.append(i)
    return off + inner


def k3(RUN, idx):
    out = {}
    for route in ("R", "F"):
        C = RUN.setup(route)
        ML, CH = C["ML"], C["chars"]
        Mt = CH.tau()
        order = next((k for k in range(1, 13) if np.array_equal(np.linalg.matrix_power(Mt, k), np.eye(Mt.shape[0],
                                                                                                         dtype=np.int64))),
                     None)
        import itertools
        r3 = []
        for coeffs in itertools.product([0, 1], repeat=CH.F.shape[0]):
            if any(coeffs) and CH.n_of(sum(a * CH.F[i] for i, a in enumerate(coeffs))) == 3:
                r3.append(tuple(coeffs))
        img = {c: tuple(int(x) % 2 for x in Mt @ np.array(c)) for c in r3}
        orbit, cur = [], r3[0]
        while cur not in orbit:
            orbit.append(cur)
            cur = img[cur]
        out[route] = {"tau's order on the free lattice": order, "room-3 characters": len(r3),
                      "tau maps them to themselves": set(img.values()) == set(r3), "one orbit": len(orbit) == 5}
    # tau*nu at the sample members, route R
    C = RUN.setup("R")
    ML, rc, CH = C["ML"], C["cover"], C["chars"]
    p = rc.p
    one = {g: np.eye(1, dtype=np.int64) for g in rc.rho}
    TL = ML.FL.N45L().deck_R_matrix(rc.cov, one, rc.tau, p, e=1)
    TL = np.where(TL > p // 2, TL - p, TL).astype(np.int64)
    loops = ML.common_loops({g: list(rc.cov.P[g]) for g in ("a", "t")})
    r3keys = {k for k, _ in ML.room3(CH, loops)[0]}
    rows = []
    for i in idx:
        key, e = C["members"][i]
        et = (TL @ np.asarray(e, dtype=np.int64)) % 8
        char = not np.any((CH.Rm @ et) % 8) and not np.any((CH.P @ et) % 8)
        kt = CH.values(et, loops, 8)
        over = tuple(x % 2 for x in kt)
        M, Mtau = ML.RMember(rc, CH.nu(e)), ML.RMember(rc, CH.nu(et))
        d1 = {U: d for U, (d, _) in ML.strata(M).items()}
        d2 = {U: d for U, (d, _) in ML.strata(Mtau).items()}
        rows.append({"member": i, "tau*nu a cusp-trivial character": bool(char), "over a room-3 character": over in r3keys,
                     "over chi0": over == tuple(C["chi0"]), "the same structure": M.structure() == Mtau.structure(),
                     "the same stratum dimensions (as multisets)": sorted(d1.values()) == sorted(d2.values())})
    out["tau*nu at the sample members (route R)"] = rows
    out["holds"] = (all(out[r] == {"tau's order on the free lattice": 5, "room-3 characters": 5,
                                   "tau maps them to themselves": True, "one orbit": True} for r in ("R", "F"))
                    and all(x["tau*nu a cusp-trivial character"] and x["over a room-3 character"] and not x["over chi0"]
                            and x["the same structure"] and x["the same stratum dimensions (as multisets)"] for x in rows))
    return out


def k4():
    RF = load("b1547_route_f_k4", ROOT / "frontier" / "B1541_the_count_on_the_room" / "verification" / "route_f.py")
    d = json.loads((ROOT / "frontier" / "B1541_the_count_on_the_room" / "verification" / "route_f_input_n45.json").read_text())
    S = RF.State(d)
    powers = set()
    for g in "abt":
        for row in S.hol[g]:
            for x in row:
                powers |= {i for i, c in enumerate(x) if c}
    absdet = {g: [str(c) for c in RF.abs_det(S.hol[g])] for g in "abt"}
    rational = all(all(Fraction(c) == 0 for c in v[1:]) for v in absdet.values())
    js = {k: [j for j in range(1, 24, 2) if j % 3 and j % 8 == k and j % 12 in (1, 11)] for k in (1, 3, 5, 7)}
    out = {"powers of zeta_24 in the holonomy": sorted(powers), "|det| (coefficients of zeta_24^i)": absdet,
           "|det| rational": rational, "j with j = k mod 8, j = +-1 mod 12": {str(k): v for k, v in js.items()}}
    out["holds"] = powers <= {0, 4} and rational and all(len(v) >= 1 for v in js.values())
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
        rng = random.Random(zlib.crc32(f"B1547|K5|{route}".encode()))
        out[route] = {"structure": M.structure(), "a generic interior class's count": M.reading(M.draw(M.Cint, rng))["count"]}
    want = {"structure": {"h1(nu^5 rho)": 23, "n(nu^5 rho)": 18, "h1(L)": 9, "n(L)": 4, "dim K0": 5, "dim K0 interior": 0},
            "a generic interior class's count": [4, -10]}
    out["holds"] = out["R"] == out["F"] == want
    return out


def k6(RUN, idx):
    rows = []
    for i in idx:
        r = {"member": i}
        for route in ("R", "F"):
            C = RUN.setup(route)
            ML, cv, CH = C["ML"], C["cover"], C["chars"]
            key, e = C["members"][i]
            M = ML.RMember(cv, CH.nu(e)) if route == "R" else ML.FMember(cv, CH.nu(e))
            st = ML.strata(M)
            dims = {U: d for U, (d, _) in st.items()}
            dist = ML.distinct_strata(dims)
            supp = {}
            for U in dist:
                rng = random.Random(zlib.crc32(f"B1547|K6|{route}|{RUN.key_str(key)}|{U}".encode()))
                supp[U] = M.support(M.draw(st[U][1], rng))
            s = M.structure()
            r[route] = {"key": RUN.key_str(key), "structure": s, "strata": dims, "distinct": dist,
                        "X_{} is K0's interior part": dims[""] == s["dim K0 interior"],
                        "generic supports are U": all(tuple(supp[U]) == (tuple(int(x) for x in U.split(",")) if U else ())
                                                      for U in dist)}
        r["routes agree"] = r["R"] == r["F"]
        rows.append(r)
    return {"members": rows, "holds": all(r["routes agree"] and r["R"]["X_{} is K0's interior part"]
                                          and r["R"]["generic supports are U"] for r in rows)}


def k7():
    RO = load("b1547_read_out_k7", HERE / "read_out.py")
    return RO.selftest()


def k8(RUN, i):
    C = RUN.setup("F")
    ML, fc, CH = C["ML"], C["cover"], C["chars"]
    Fm, p = ML.FL.F(), fc.p

    def one_at_a_time(Z, D0):
        cols, cur = [], D0 % p
        r = Fm.rank(cur, p)
        for j in range(Z.shape[1]):
            cand = np.hstack([cur, Z[:, j:j + 1]])
            rc = Fm.rank(cand, p)
            if rc > r:
                cur, r = cand, rc
                cols.append(j)
        return Z[:, cols]
    M1 = ML.FMember(fc, {(x, g): 1 for x in range(fc.cov.d) for g in fc.cov.gens})
    Mi = ML.FMember(fc, CH.nu(C["members"][i][1]))
    cases = {"the four's classes at nu = 1": (M1.CC.Z, M1.CC.D0), "the line's classes at nu = 1": (M1.CL.Z, M1.CL.D0),
             "classes vanishing on cusps 0 and 2 at nu = 1": (M1.vanishing([0, 2]), M1.CC.D0),
             f"member {i}'s classes": (Mi.CC.Z, Mi.CC.D0)}
    out = {}
    for name, (Z, D0) in cases.items():
        a, b = one_at_a_time(Z, D0), Mi.class_basis(Z, D0)
        out[name] = {"columns": int(b.shape[1]), "the same": bool(a.shape == b.shape and np.array_equal(a % p, b % p))}
    out["holds"] = all(v["the same"] for v in out.values() if isinstance(v, dict))
    return out


def main():
    t0 = time.time()
    RUN = load("b1547_run_controls", HERE / "run.py")
    rep = {}
    for name, fn in (("K1", lambda: k1(RUN)), ("K2", lambda: k2(RUN)), ("K4", k4), ("K5", lambda: k5(RUN)), ("K7", k7)):
        t1 = time.time()
        rep[name] = fn()
        rep[name]["seconds"] = round(time.time() - t1, 1)
        print(name, rep[name]["holds"], rep[name]["seconds"], flush=True)
    t1 = time.time()
    idx = sample(RUN)
    rep["the sample members"] = {"members": idx, "seconds": round(time.time() - t1, 1)}
    for name, fn in (("K3", lambda: k3(RUN, idx)), ("K6", lambda: k6(RUN, idx)), ("K8", lambda: k8(RUN, idx[0]))):
        t1 = time.time()
        rep[name] = fn()
        rep[name]["seconds"] = round(time.time() - t1, 1)
        print(name, rep[name]["holds"], rep[name]["seconds"], flush=True)
    rep["all hold"] = all(rep[k]["holds"] for k in ("K1", "K2", "K3", "K4", "K5", "K6", "K7", "K8"))
    rep["seconds"] = round(time.time() - t0, 1)
    print(json.dumps({k: (v["holds"] if isinstance(v, dict) and "holds" in v else v) for k, v in rep.items()}), flush=True)
    if "--record" in sys.argv:
        (HERE / "controls.json").write_text(json.dumps(rep, indent=1, default=str) + "\n")
    return rep


if __name__ == "__main__":
    main()
