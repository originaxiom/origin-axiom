#!/usr/bin/env python3
"""B1542 -- THE CONTROLS (PREREGISTRATION.md section 6), on structure or on values already banked.  No class of a degree-60
cover is read.

  K1  each cover (ncyc.build): degree 60, connected, its cusps; it is the cover sm:B1540 read (its canonical form equals that of
      sm:B1540's room_lib.cyclic_cover along the banked own character in pulled_back_rooms.json); and at the trivial character
      route N and route R give room_60.json's primes, (n(1), n(rho)) and caps.
  K2  each cover's class space: h^1(N; rho) in route N (p_N), route R (p_N) and route R (p_R); tau's eigenspaces on H^1 and their
      interior parts (classes that restrict to coboundaries at every cusp), in route N (deck_N) and in route R (deck_R, at p_R),
      equal EXPECT, and their support equals run.STRUCTURE (the sealed subspaces).
  K3  each cover's transport (ncyc.transport): route N's cocycles go to route R's cocycles, the map has rank h^1 on H^1, and it
      carries deck_N to deck_R (tau to tau, not tau^-1) up to coboundaries.
  K4  the generalized library on sm:B1541's N_45 (order 5): ncyc.build("m003", "d9.2", (1/5, 3/5), 0, 5) is the canonical cover
      of sm:B1541's n45.build; h^1 = 23 and tau's eigenspaces (3, 5, 5, 5, 5) in both routes (sm:B1541's banked K2); the class
      pulled back from m003 reads (0, 0) in route N, route R and route R at p_N transported (sm:B1541's banked K4).
  K5  sm:B1536's Part O code path, unchanged: its banked Part O readings at m003's d10.4, trivial character, reproduced in both
      routes (same seeds).
  K6  the read-out on synthetic rows (read_out.evaluate): every prediction's True, False and None cases.
  K7  the state's group is the census manifold m003's (WORKING_RULES 2026-10-06: the name is load-bearing for the headline):
      for every index n <= 7, the number of conjugacy classes of subgroups of index n of the group the run uses (sm:B1536's
      cover_lib.state) equals that of SnapPy's m003 fundamental group, counted by low_index (an enumerator the cover code does
      not use); the same check run on m004 gives m004's numbers, and they differ from m003's (the check can fail); and SnapPy's
      bundle b+-LR is isometric to m003 and not to m004 (the bundle convention).

    python3 controls.py [--record]     ->  controls.json (a few minutes)"""
import gzip
import importlib.util
import json
import random
import sys
import time
import zlib
from fractions import Fraction as Fr
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
B1540V = ROOT / "frontier" / "B1540_the_room_for_three" / "verification"
B1541V = ROOT / "frontier" / "B1541_the_count_on_the_room" / "verification"
# the class spaces' dimensions (h^1; tau's eigenspaces on H^1 for zeta^0..zeta^5; their interior parts), fixed before the seal
EXPECT = {
    "d10.13": {"h1": 9, "eigen": [5, 0, 0, 4, 0, 0], "interior": [2, 0, 0, 1, 0, 0]},
    "d10.16": {"h1": 11, "eigen": [5, 0, 2, 2, 2, 0], "interior": [2, 0, 2, 1, 2, 0]},
    "d10.36": {"h1": 9, "eigen": [5, 0, 0, 4, 0, 0], "interior": [2, 0, 0, 1, 0, 0]},
    "d10.40": {"h1": 11, "eigen": [5, 0, 2, 2, 2, 0], "interior": [2, 0, 2, 1, 2, 0]},
}


def _sib(alias, path):
    if alias not in sys.modules:
        spec = importlib.util.spec_from_file_location(alias, path)
        mod = importlib.util.module_from_spec(spec)
        sys.modules[alias] = mod
        spec.loader.exec_module(mod)
    return sys.modules[alias]


L = _sib("b1542_ncyc", HERE / "ncyc.py")
RUN = _sib("b1542_run", HERE / "run.py")
RO = _sib("b1542_read_out", HERE / "read_out.py")


def _other_arc(prefix, alias, path):
    """another arc's banked module, by path under a unique name; its own aliases for sm:B1536's modules are pointed at the modules
    this arc already loaded from the same files (route_r allocates PARI's stack on import: it is executed once)"""
    for name, mod in (("route_r", L.R), ("route_n", L.N), ("cover_lib", L.CL), ("gf", L.GF), ("population", L.POP)):
        sys.modules.setdefault(f"{prefix}_b1536_{name}", mod)
    return _sib(alias, path)


def eigen_dims(Z, B, deck, p, k, rank):
    """dimensions of tau's eigenspaces on the span of the cocycle columns Z modulo the coboundary columns B: rank([P_j Z, B]) -
    rank B, with the route's own rank (route N: route_n.rank; route R: route_r.prank)"""
    rB = rank(B, p)
    out = []
    for j in range(k):
        PZ = np.stack([L.project(Z[:, i] % p, deck, j, p, k) for i in range(Z.shape[1])], axis=1)
        out.append(int(rank(np.hstack([PZ, B]), p) - rB))
    return out


def per_cover(cid, rep):
    c = RUN.setup(cid)
    st, perms, tau, G, gens = c["st"], c["perms"], c["tau"], c["G"], c["gens"]
    B, p, K = c["B"], c["B"].p, RUN.K
    # K1
    RL = _other_arc("b1540", "b1542_b1540_room_lib", B1540V / "room_lib.py")
    pb = json.loads((B1540V / "pulled_back_rooms.json").read_text())["by member"][f"m003:{cid}"]
    r60 = json.loads((B1540V / "room_60.json").read_text())["covers"][f"m003:{cid}"]
    S40, perms40, cov40 = RL.cover("m003", cid)
    pe40, k40 = RL.cyclic_cover(cov40, RL.Ab(cov40), tuple(pb["room >= 3"][0]["c"]), pb["M"])
    same_cover = L.CL.canonical(perms, gens) == RL.canonical(S40, pe40)
    sN = L.N.supplies(B, c["pa"], c["chi"])
    sR = L.R.supplies(c["cov"], c["BR"].rho, c["chiR"], c["pR"])
    k1 = {"degree": len(perms["a"]), "cusps": len(L.CL.cusps(G, perms)), "the cover sm:B1540 read": bool(same_cover),
          "route N (prime, n(1), n(rho), capW, capL2)": [p, sN["n(L)"], sN["n((VL)*)"], sN["capW"], sN["capL2"]],
          "route R (prime, n(1), n(rho), capW, capL2)": [c["pR"], sR["n(L)"], sR["n((VL)*)"], sR["capW"], sR["capL2"]]}
    k1["holds"] = bool(k1["degree"] == 60 and k1["cusps"] == RUN.STRUCTURE[cid]["cusps"] == r60["cusps"] and same_cover
                       and k1["route N (prime, n(1), n(rho), capW, capL2)"] == r60["route N (prime, n(1), n(rho), capW, capL2)"]
                       and k1["route R (prime, n(1), n(rho), capW, capL2)"] == r60["route R (prime, n(1), n(rho), capW, capL2)"])
    # K2
    mod = L.N.tensor(B, L.N.small_four(B, c["chi"], 5), c["pa"])
    Zb = c["Zb"] % p
    Bcols = np.vstack([mod.M[g].dense(p) - np.eye(mod.D, dtype=np.int64) for g in mod.gens]) % p
    h1N = Zb.shape[1] - L.N.rank(Bcols, p)
    dk = lambda z: L.deck_N(z, tau, len(gens))  # noqa: E731
    nc = len(c["cusps"])
    Bint = L.N.stratum_basis(c["Zb"], c["Rm"], c["BP"], c["cusps"], list(range(nc)), 4, p)
    eigN = eigen_dims(Zb, Bcols, dk, p, K, L.N.rank)
    intN = eigen_dims((Zb @ Bint) % p, Bcols, dk, p, K, L.N.rank)
    cov = c["cov"]
    modRN = L.R.lift(cov, c["rhoN"], p)
    CRN = L.R.Coh(cov, modRN, keep=True)
    pR, CR, TR = c["pR"], c["CR"], c["TR"]
    modRR = L.R.lift(cov, c["rhoR"], pR)
    BRR = np.vstack([(m - np.eye(4, dtype=np.int64)) % pR for m in modRR.M])
    ZR = (CR.Zrows % pR).T
    dR = lambda v: L.R.mm(TR, v.reshape(-1, 1), pR).ravel()  # noqa: E731
    e = 4
    RZ = L.R.mm(CR.R, ZR, pR)
    A = np.zeros((2 * e * nc, ZR.shape[1] + e * nc), dtype=np.int64)
    for i in range(nc):
        A[2 * e * i:2 * e * (i + 1), :ZR.shape[1]] = RZ[2 * e * i:2 * e * (i + 1)]
        A[2 * e * i:2 * e * (i + 1), ZR.shape[1] + e * i:ZR.shape[1] + e * (i + 1)] = \
            (-CR.BP[2 * e * i:2 * e * (i + 1), e * i:e * (i + 1)]) % pR
    Kn = L.R.pnull(A, pR, ZR.shape[1] + e * nc)
    W = np.stack([k[:ZR.shape[1]] % pR for k in Kn], axis=1) if len(Kn) else np.zeros((ZR.shape[1], 0), dtype=np.int64)
    eigR = eigen_dims(ZR, BRR, dR, pR, K, L.R.prank)
    intR = eigen_dims(L.R.mm(ZR, W, pR), BRR, dR, pR, K, L.R.prank) if W.shape[1] else [0] * K
    want = EXPECT[cid]
    s = RUN.STRUCTURE[cid]
    k2 = {"h1 (route N p_N, route R p_N, route R p_R)": [int(h1N), CRN.h1, CR.h1],
          "eigenspaces (route N; route R, p_R)": [eigN, eigR], "interior parts (route N; route R, p_R)": [intN, intR]}
    k2["holds"] = bool([int(h1N), CRN.h1, CR.h1] == [want["h1"]] * 3 and eigN == eigR == want["eigen"]
                       and intN == intR == want["interior"]
                       and tuple(j for j in range(K) if want["eigen"][j]) == s["eigen"]
                       and tuple(j for j in range(K) if want["interior"][j]) == s["interior"]
                       and sum(want["interior"]) == sN["n((VL)*)"])
    # K3
    BRN = np.vstack([(m - np.eye(4, dtype=np.int64)) % p for m in modRN.M])
    rBRN = L.R.prank(BRN, p)
    FR = np.vstack([L.R.fox(modRN, r, len(cov.sgens)) for r in cov.rels]) % p
    TZ = np.stack([np.concatenate(L.transport(Zb[:, i] % p, st, perms, cov, B)) for i in range(Zb.shape[1])], axis=1) % p
    cocycles = not np.any(L.R.mm(FR, TZ, p) % p)
    rank_h1 = L.R.prank(np.hstack([BRN, TZ]), p) - rBRN
    TRN = L.deck_R_matrix(cov, c["rhoN"], tau, p)
    rng = random.Random(zlib.crc32(f"B1542|K3|{cid}".encode()))
    inter = True
    for _ in range(3):
        z = (Zb @ np.array([rng.randrange(p) for _ in range(Zb.shape[1])], dtype=np.int64)) % p
        a = np.concatenate(L.transport(dk(z), st, perms, cov, B)) % p
        b = L.R.mm(TRN, (np.concatenate(L.transport(z, st, perms, cov, B)) % p).reshape(-1, 1), p).ravel()
        inter &= L.R.prank(np.hstack([BRN, ((a - b) % p).reshape(-1, 1)]), p) == rBRN
    k3 = {"transported cocycles are cocycles": bool(cocycles), "rank on H^1": int(rank_h1),
          "carries deck_N to deck_R": bool(inter)}
    k3["holds"] = bool(cocycles and rank_h1 == want["h1"] and inter)
    rep["K1"][cid], rep["K2"][cid], rep["K3"][cid] = k1, k2, k3


def k4(rep):
    """the generalized library at order 5 against sm:B1541's banked N_45"""
    n45 = _other_arc("b1541", "b1542_b1541_n45", B1541V / "n45.py")
    st, perms, pts, tau = L.build("m003", "d9.2", (Fr(1, 5), Fr(3, 5)), Fr(0), 5)
    st1, perms1, pts1, tau1 = n45.build()
    gens = list(st["G"].gens)
    same = L.CL.canonical(perms, gens) == L.CL.canonical(perms1, gens)
    B, pa, chi, (mod, Zb, Rm, BP), cusps = L.route_n_setup(st, perms)
    p = B.p
    Zb = Zb % p
    tmod = L.N.tensor(B, L.N.small_four(B, chi, 5), pa)
    Bcols = np.vstack([tmod.M[g].dense(p) - np.eye(tmod.D, dtype=np.int64) for g in tmod.gens]) % p
    h1N = Zb.shape[1] - L.N.rank(Bcols, p)
    eigN = eigen_dims(Zb, Bcols, lambda z: L.deck_N(z, tau, len(gens)), p, 5, L.N.rank)
    G = st["G"]
    cov = L.R.PCover(G, perms)
    cus, Lc, Nroot, _ = L.POP.characters(st, perms)
    pR = L.GF.primes_1_mod(Nroot, 1 << 31, 1)[0]
    BR = L.N.Base(st, L.GF.GF(pR, Nroot))
    chiR = BR.character((Fr(0), Fr(0)), Fr(0))
    rhoR = {g: np.asarray(BR.rho[g], dtype=np.int64) % pR for g in gens}
    CR = L.R.Coh(cov, L.R.lift(cov, rhoR, pR), keep=True)
    TR = L.deck_R_matrix(cov, rhoR, tau, pR)
    BRR = np.vstack([(m - np.eye(4, dtype=np.int64)) % pR for m in L.R.lift(cov, rhoR, pR).M])
    eigR = eigen_dims((CR.Zrows % pR).T, BRR, lambda v: L.R.mm(TR, v.reshape(-1, 1), pR).ravel(), pR, 5, L.R.prank)
    c = dict(L=L, G=G, gens=gens, B=B, pa=pa, chi=chi, perms=perms, cov=cov, pR=pR, BR=BR, chiR=chiR, rhoR=rhoR)
    pN = RUN.pulled_back(c, "N")
    pRr = RUN.pulled_back(c, "R")
    d = len(perms["a"])
    pa1 = L.N.perm_arrays(G, {"a": [0], "b": [0], "t": [0]})
    z1 = L.N.base_classes(B, L.N.tensor(B, L.N.small_four(B, chi, 5), pa1))["c1"]
    cz = {g: z1[gi * 4:(gi + 1) * 4] for gi, g in enumerate(B.gens)}
    zfull = np.concatenate([np.concatenate([cz[g]] * d) for g in B.gens]) % p
    pT = RUN.rd(L.R.reading(cov, B.rho, chi, L.transport(zfull, st, perms, cov, B), p))
    rep["K4"] = {"the canonical cover of sm:B1541's n45.build": bool(same), "h1 (route N p_N, route R p_R)": [int(h1N), CR.h1],
                 "eigenspaces (route N; route R, p_R)": [eigN, eigR],
                 "pulled back (route N, route R, route R at p_N transported)": [pN["count"], pRr["count"], pT["count"]],
                 "identities": [pN["all"], pRr["all"], pT["all"]]}
    rep["K4"]["holds"] = bool(same and [int(h1N), CR.h1] == [23, 23] and eigN == eigR == [3, 5, 5, 5, 5]
                              and pN["count"] == pRr["count"] == pT["count"] == [0, 0] and all(rep["K4"]["identities"]))


def k5(rep):
    """sm:B1536's Part O at m003's d10.4, trivial character, in both routes, with its own seeds (the first member read there)"""
    st = L.CL.state("m003")
    G = st["G"]
    perms = dict(L.POP.covers(st))["d10.4"]
    rows = {}
    for route in ("N", "R"):
        for line in gzip.open(L.B1536V / f"run_{route}_m003.jsonl.gz", "rt"):
            r = json.loads(line)
            if not r.get("done") and r["cover"] == "d10.4":
                rows.setdefault(route, []).append(r)
    ok, detail = True, {}
    for route in ("N", "R"):
        first = [r for r in rows[route] if r.get("O") is not None][0]
        assert first["u"] == ["0", "0"] and first["kappa"] == "0", "the first Part O member of d10.4 is not the trivial one"
        cus, Lc, Nroot, chars = L.POP.characters(st, perms)
        p = L.GF.primes_1_mod(Nroot, L.N.P_BOUND if route == "N" else 1 << 31, 1)[0]
        B = L.N.Base(st, L.GF.GF(p, Nroot))
        chi = B.character((Fr(0), Fr(0)), Fr(0))
        rng = random.Random(zlib.crc32(f"{route}|m003|d10.4".encode()))
        trivial = [True for _ in cus]
        if route == "N":
            strata = L.N.strata_readings(B, L.N.perm_arrays(G, perms), chi, [dict(cc, trivial=True) for cc in cus], rng)
        else:
            strata = L.R.strata_readings(L.R.PCover(G, perms), B.rho, chi, p, trivial, rng)
        now = [{"S": S, "readings": [RUN.rd(x) for x in reads]} for S, reads in strata]
        same = json.loads(json.dumps(now)) == first["O"]
        ok &= same
        detail[route] = {"strata": len(now), "reproduced": same}
    rep["K5"] = {"routes": detail, "holds": ok}


def k6(rep):
    tasks = [("d10.13", "A", "S=", 0), ("d10.13", "A", "S=", 1), ("d10.13", "B", "j=3", 0), ("d10.13", "C", "pulled back", 0),
             ("d10.16", "A", "S=", 0), ("d10.16", "C", "pulled back", 0)]
    A0 = ("d10.13", "A", "S=", 0)

    def rr(count, k=5, rk=None, ok=True):
        return {"count": list(count), "k": k, "rk d1": rk or {"E": 0, "E*": 0, "L2": 0, "L2*": 5}, "all": ok, "failed": []}

    def rows(counts, pb=None, skip=None, dup=False, tamper=None, bad_id=False):
        pb = pb or {}
        out = []
        for t in tasks:
            if t == skip:
                continue
            cid, part, name, draw = t
            if part == "C":
                for route in ("N", "R"):
                    cnt = pb.get((cid, route), (0, 0))
                    out.append(dict(cover=cid, part="C", subspace="pulled back", draw=0, route=route, reading=rr(cnt)))
                continue
            cnt = counts.get((cid, name, draw), counts.get((cid, name)))
            for route in ("N", RO.SAME, "R"):
                c2 = tamper if (tamper is not None and route == RO.SAME and t == A0) else cnt
                out.append(dict(cover=cid, part=part, subspace=name, draw=draw, route=route,
                                reading=rr(c2, ok=not (bad_id and t == A0 and route == "R"))))
        if dup:
            out.append(dict(out[0]))
        return out
    cases, ok = {}, True

    def run(name, rws, want):
        nonlocal ok
        res = RO.evaluate(rws, tasks, say=lambda s: None)
        got = {k: res["predictions"][k] for k in want}
        cases[name] = {"want": want, "got": got, "pass": got == want}
        ok &= got == want
    neg = {("d10.13", "S="): (-1, -4), ("d10.13", "j=3"): (-2, -7), ("d10.16", "S="): (-1, -3)}
    run("negative, complete", rows(neg), {"P1": True, "P2": True, "P3": True, "P4": False, "P5": False, "P6": True})
    run("three at a class", rows({**neg, ("d10.16", "S="): (-3, -3)}), {"P1": True, "P4": True, "P5": True})
    run("generation-shaped, not three", rows({**neg, ("d10.13", "j=3"): (-2, -2)}), {"P4": True, "P5": False})
    run("the transport disagrees", rows(neg, tamper=(-3, -3)), {"P1": False, "P5": False})
    run("a missing task gives None", rows(neg, skip=("d10.13", "B", "j=3", 0)), {"P1": None, "P4": None, "P5": None})
    run("a duplicate row gives None", rows(neg, dup=True), {"P1": None, "P4": None})
    run("a pulled-back class read differently in the two routes", rows(neg, pb={("d10.16", "R"): (1, 0)}), {"P6": False})
    run("a pulled-back class off (0, 0) but one count", rows(neg, pb={("d10.16", "N"): (1, 1), ("d10.16", "R"): (1, 1)}),
        {"P6": True})
    run("a missing pulled-back class gives None", rows(neg, skip=("d10.16", "C", "pulled back", 0)), {"P6": None})
    run("an anomalous (k, -k) count is not generation-shaped", rows({**neg, ("d10.13", "S="): (-3, 3)}), {"P4": False})
    run("two counts in one subspace", rows({**neg, ("d10.13", "S=", 1): (-1, -5)}), {"P1": True, "P2": False, "P4": False})
    run("a failed identity", rows(neg, bad_id=True), {"P3": False})
    cases_v = {"PROVED": {"P1": True, "P2": True, "P3": True, "P4": True, "P5": True, "P6": True},
               "NEGATIVE": {"P1": True, "P2": True, "P3": True, "P4": False, "P5": False, "P6": True},
               "OPEN": {"P1": True, "P2": True, "P3": True, "P4": True, "P5": False, "P6": True}}
    for want_v, pr in cases_v.items():
        got_v = RO.verdict(pr)
        cases[f"verdict {want_v}"] = {"want": want_v, "got": got_v, "pass": got_v == want_v}
        ok &= got_v == want_v
    rep["K6"] = {"cases": len(cases), "holds": ok, "detail": cases}


def k7(rep):
    import low_index
    import snappy
    from collections import Counter
    tr = str.maketrans({"t": "c", "T": "C"})

    def ours(name):
        G = L.CL.state(name)["G"]
        assert list(G.gens) == ["a", "b", "t"]
        reps = low_index.permutation_reps(3, [r.translate(tr) for r in G.rels], [], 7)
        return dict(sorted(Counter(len(P[0]) for P in reps).items()))

    def census(name):
        F = snappy.Manifold(name).fundamental_group()
        reps = low_index.permutation_reps(F.num_generators(), F.relators(), [], 7)
        return dict(sorted(Counter(len(P[0]) for P in reps).items()))
    o3, c3, o4, c4 = ours("m003"), census("m003"), ours("m004"), census("m004")
    iso = {"b+-LR ~ m003": bool(snappy.Manifold("b+-LR").is_isometric_to(snappy.Manifold("m003"))),
           "b+-LR ~ m004": bool(snappy.Manifold("b+-LR").is_isometric_to(snappy.Manifold("m004")))}
    rep["K7"] = {"subgroup classes by index <= 7 (ours m003, census m003, ours m004, census m004)": [o3, c3, o4, c4],
                 "isometries": iso}
    rep["K7"]["holds"] = bool(o3 == c3 and o4 == c4 and o3 != o4 and iso["b+-LR ~ m003"] and not iso["b+-LR ~ m004"])


def main():
    rep, t = {"K1": {}, "K2": {}, "K3": {}}, {}
    for cid in RUN.COVERS:
        t0 = time.time()
        per_cover(cid, rep)
        t[f"K1-K3 {cid}"] = round(time.time() - t0, 1)
        print(f"K1-K3 {cid} done", t[f"K1-K3 {cid}"], "s", flush=True)
    for k in ("K1", "K2", "K3"):
        rep[k]["holds"] = all(v["holds"] for v in rep[k].values())
    for name, f in (("K4", k4), ("K5", k5), ("K6", k6), ("K7", k7)):
        t0 = time.time()
        f(rep)
        t[name] = round(time.time() - t0, 1)
        print(name, "done", t[name], "s", flush=True)
    rep["seconds"] = t
    rep["all hold"] = all(rep[k]["holds"] for k in ("K1", "K2", "K3", "K4", "K5", "K6", "K7"))
    for k in ("K1", "K2", "K3", "K4", "K5", "K6", "K7"):
        print(k, json.dumps({x: y for x, y in rep[k].items() if x != "detail"}, default=str))
    print("ALL HOLD:", rep["all hold"])
    if "--record" in sys.argv:
        (HERE / "controls.json").write_text(json.dumps(rep, indent=1, default=str) + "\n")
    return rep


if __name__ == "__main__":
    main()
