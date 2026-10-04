#!/usr/bin/env python3
"""B1541 -- THE CONTROLS (PREREGISTRATION.md section 6), on structure or on values the banked rows already fix.  No class of
N_45 other than the one pulled back from m003 (count fixed at (0, 0)) is read.

  K1  N_45: degree 45, connected, five cusps; tau commutes with Gamma and has order 5 (n45.build's assertions); and at the
      trivial character (n(1), n(rho)) = (4, 18) in route N and in route R (fixed by sm:B1536's banked rows and Lemma A).
  K2  the class space: h^1(N_45; rho) = 23 in route N (p_N), route R (p_N) and route R (p_R); tau's eigenspaces on H^1 have
      dimensions (3, 5, 5, 5, 5) in route N (deck_N) and in route R (deck_R, at p_R): Lemma A's decomposition.
  K3  the transport (n45.transport): route N's cocycles go to route R's cocycles, the map has rank 23 on H^1, and it carries
      deck_N to deck_R (tau to tau, not tau^-1) up to coboundaries.
  K4  the class pulled back from m003: (0, 0) with every identity, in route N and route R at their own primes, and in route R
      at p_N on route N's class transported.
  K5  sm:B1536's Part O code path, unchanged: its banked Part O readings at m003's d10.4, trivial character, reproduced in both
      routes (same seeds).
  K6  the read-out on synthetic rows (read_out.evaluate): every prediction's True, False and None cases.

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


def _sib(alias, name):
    if alias not in sys.modules:
        spec = importlib.util.spec_from_file_location(alias, HERE / name)
        mod = importlib.util.module_from_spec(spec)
        sys.modules[alias] = mod
        spec.loader.exec_module(mod)
    return sys.modules[alias]


L = _sib("b1541_n45", "n45.py")
RUN = _sib("b1541_run", "run.py")
RO = _sib("b1541_read_out", "read_out.py")


def k1_k4(rep):
    c = RUN.setup()
    st, perms, tau, G, gens = c["st"], c["perms"], c["tau"], c["G"], c["gens"]
    B, p = c["B"], c["B"].p
    sN = L.N.supplies(B, c["pa"], c["chi"])
    sR = L.R.supplies(c["cov"], c["BR"].rho, c["chiR"], c["pR"])
    rep["K1"] = {"degree": len(perms["a"]), "cusps": len(L.CL.cusps(G, perms)),
                 "route N (n(1), n(rho))": [sN["n(L)"], sN["n((VL)*)"]], "route R (n(1), n(rho))": [sR["n(L)"], sR["n((VL)*)"]]}
    rep["K1"]["holds"] = (len(perms["a"]) == 45 and rep["K1"]["cusps"] == 5
                          and rep["K1"]["route N (n(1), n(rho))"] == rep["K1"]["route R (n(1), n(rho))"] == [4, 18])
    # K2
    mod = L.N.tensor(B, L.N.small_four(B, c["chi"], 5), c["pa"])
    Zb = c["Zb"]
    Bcols = np.vstack([mod.M[g].dense(p) - np.eye(mod.D, dtype=np.int64) for g in mod.gens]) % p
    rB = L.N.rank(Bcols, p)
    h1N = Zb.shape[1] - rB
    dk = lambda z: L.deck_N(z, tau, len(gens))  # noqa: E731
    dimsN = []
    for j in range(5):
        PZ = np.stack([L.project(Zb[:, i], dk, j, p) for i in range(Zb.shape[1])], axis=1)
        dimsN.append(L.N.rank(np.hstack([PZ, Bcols]), p) - rB)
    cov = c["cov"]
    modRN = L.R.lift(cov, c["rhoN"], p)
    CRN = L.R.Coh(cov, modRN, keep=True)
    pR, CR, TR = c["pR"], c["CR"], c["TR"]
    modRR = L.R.lift(cov, c["rhoR"], pR)
    BRR = np.vstack([(m - np.eye(4, dtype=np.int64)) % pR for m in modRR.M])
    rBRR = L.R.prank(BRR, pR)
    ZR = CR.Zrows % pR
    dimsR = []
    for j in range(5):
        PZ = np.stack([L.project(ZR[i], lambda v: L.R.mm(TR, v.reshape(-1, 1), pR).ravel(), j, pR)
                       for i in range(ZR.shape[0])], axis=1)
        dimsR.append(L.R.prank(np.hstack([BRR, PZ]), pR) - rBRR)
    rep["K2"] = {"h1 (route N p_N, route R p_N, route R p_R)": [h1N, CRN.h1, CR.h1],
                 "eigenspaces (route N)": dimsN, "eigenspaces (route R, p_R)": dimsR}
    rep["K2"]["holds"] = [h1N, CRN.h1, CR.h1] == [23] * 3 and dimsN == dimsR == [3, 5, 5, 5, 5]
    # K3
    BRN = np.vstack([(m - np.eye(4, dtype=np.int64)) % p for m in modRN.M])
    rBRN = L.R.prank(BRN, p)
    FR = np.vstack([L.R.fox(modRN, r, len(cov.sgens)) for r in cov.rels]) % p
    TZ = np.stack([np.concatenate(L.transport(Zb[:, i] % p, st, perms, cov, B)) for i in range(Zb.shape[1])], axis=1) % p
    cocycles = not np.any((FR @ TZ) % p)
    rank_h1 = L.R.prank(np.hstack([BRN, TZ]), p) - rBRN
    TRN = L.deck_R_matrix(cov, c["rhoN"], tau, p)
    rng = random.Random(11)
    inter = True
    for _ in range(3):
        z = (Zb @ np.array([rng.randrange(p) for _ in range(Zb.shape[1])], dtype=np.int64)) % p
        a = np.concatenate(L.transport(dk(z), st, perms, cov, B)) % p
        b = (TRN @ (np.concatenate(L.transport(z, st, perms, cov, B)) % p)) % p
        inter &= L.R.prank(np.hstack([BRN, ((a - b) % p).reshape(-1, 1)]), p) == rBRN
    rep["K3"] = {"transported cocycles are cocycles": bool(cocycles), "rank on H^1": int(rank_h1),
                 "carries deck_N to deck_R": bool(inter), "holds": bool(cocycles and rank_h1 == 23 and inter)}
    # K4
    pN = RUN.pulled_back(c, "N")
    pRr = RUN.pulled_back(c, "R")
    d = len(perms["a"])
    pa1 = L.N.perm_arrays(G, {"a": [0], "b": [0], "t": [0]})
    z1 = L.N.base_classes(B, L.N.tensor(B, L.N.small_four(B, c["chi"], 5), pa1))["c1"]
    cz = {g: z1[gi * 4:(gi + 1) * 4] for gi, g in enumerate(B.gens)}
    zfull = np.concatenate([np.concatenate([cz[g]] * d) for g in B.gens]) % p
    pT = RUN.rd(L.R.reading(cov, B.rho, c["chi"], L.transport(zfull, st, perms, cov, B), p))
    rep["K4"] = {"route N": pN["count"], "route R": pRr["count"], "route R at p_N (transported)": pT["count"],
                 "identities": [pN["all"], pRr["all"], pT["all"]]}
    rep["K4"]["holds"] = (pN["count"] == pRr["count"] == pT["count"] == [0, 0] and all(rep["K4"]["identities"]))


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
    tasks = [("A", "S=", 0), ("A", "S=", 1), ("B", "j=1", 0), ("C", "pulled back", 0)]

    def rr(count, k=5, rk=None, ok=True):
        return {"count": list(count), "k": k, "rk d1": rk or {"E": 0, "E*": 0, "L2": 0, "L2*": 5}, "all": ok, "failed": []}

    def rows(counts, pb=(0, 0), skip=None, dup=False, tamper=None):
        out = []
        for t in tasks:
            if t == skip:
                continue
            if t[0] == "C":
                out += [dict(part="C", subspace="pulled back", draw=0, route=r, reading=rr(pb)) for r in ("N", "R")]
                continue
            cnt = counts[t[1]]
            for route in ("N", "R at p_N (the same class)", "R"):
                c2 = tamper if (tamper is not None and route == "R at p_N (the same class)" and t == ("A", "S=", 0)) else cnt
                out.append(dict(part=t[0], subspace=t[1], draw=t[2], route=route, reading=rr(c2)))
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
    neg = {"S=": (-1, -4), "j=1": (-2, -7)}
    run("negative, complete", rows(neg), {"P1": True, "P2": True, "P3": True, "P4": False, "P5": False, "P6": True})
    run("three at a class", rows({"S=": (-3, -3), "j=1": (-2, -7)}), {"P1": True, "P4": True, "P5": True})
    run("generation-shaped, not three", rows({"S=": (-2, -2), "j=1": (-2, -7)}), {"P4": True, "P5": False})
    run("the transport disagrees", rows(neg, tamper=(-3, -3)), {"P1": False, "P5": False})
    run("a missing task gives None", rows(neg, skip=("B", "j=1", 0)), {"P1": None, "P4": None, "P5": None})
    run("a duplicate row gives None", rows(neg, dup=True), {"P1": None, "P4": None})
    run("the pulled-back class off (0, 0)", rows(neg, pb=(1, 0)), {"P6": False})
    run("an anomalous (k, -k) count is not generation-shaped", rows({"S=": (-3, 3), "j=1": (-2, -7)}), {"P4": False})
    rep["K6"] = {"cases": len(cases), "holds": ok, "detail": cases}


def main():
    rep, t = {}, {}
    for name, f in (("K1-K4", k1_k4), ("K5", k5), ("K6", k6)):
        t0 = time.time()
        f(rep)
        t[name] = round(time.time() - t0, 1)
        print(name, "done", t[name], "s", flush=True)
    rep["seconds"] = t
    rep["all hold"] = all(rep[k]["holds"] for k in ("K1", "K2", "K3", "K4", "K5", "K6"))
    for k in ("K1", "K2", "K3", "K4", "K5", "K6"):
        print(k, {x: y for x, y in rep[k].items() if x != "detail"})
    print("ALL HOLD:", rep["all hold"])
    if "--record" in sys.argv:
        (HERE / "controls.json").write_text(json.dumps(rep, indent=1, default=str) + "\n")
    return rep


if __name__ == "__main__":
    main()
