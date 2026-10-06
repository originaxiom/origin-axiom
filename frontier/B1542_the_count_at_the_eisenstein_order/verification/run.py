#!/usr/bin/env python3
"""B1542 -- THE RUN (PREREGISTRATION.md section 5): the counts (I(W), I(L2W)) at the sealed classes of H^1(N; rho), at the
trivial character of each of the four degree-60 covers N (ncyc.py), in two routes.

    python3 -u run.py [--workers k] --record      ->  run.jsonl (one row per reading; resumable by task)

The tasks, per cover (every one outcome-blind; the classes are drawn with seeds fixed by crc32):
  Part A  the cusp strata (sm:B1536's Part O on N): every subset S of N's cusps, DRAWS classes whose restriction to every cusp
          outside S is a coboundary.  Route N draws at its prime p_N and reads; route R reads each of those classes again at p_N
          through ncyc.transport; route R draws its own classes at its own prime p_R and reads them.
  Part B  the deck group's eigenspaces: for every j with a non-zero eigenspace (STRUCTURE, checked by control K2), DRAWS classes
          in tau's eigenspace for zeta^j and, where it is non-zero, DRAWS in its interior part (route N by ncyc.deck_N, then
          transported to route R at p_N; route R's own at p_R by ncyc.deck_R_matrix).
  Part C  the class pulled back from m003, in both routes at their own primes.
Every reading records the count, sm:B1536's identities and Theorem C's checks; nothing is asserted on outcomes."""
import json
import os
import random
import sys
import time
import zlib
from fractions import Fraction as Fr
from itertools import combinations
from multiprocessing import get_context
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
DRAWS = 3
K = 6
PSI = ((Fr(0), Fr(0)), Fr(1, 6))
COVERS = ("d10.13", "d10.16", "d10.36", "d10.40")
# the class spaces' structure at the trivial character (control K2 checks it in both routes before the seal):
#   d10.13, d10.36: h^1 9 = 5 + 4 on tau's eigenvalues zeta^0, zeta^3; interior 2 + 1 = n(rho) = 3
#   d10.16, d10.40: h^1 11 = 5 + 2 + 2 + 2 on zeta^0, zeta^2, zeta^3, zeta^4; interior 2 + 2 + 1 + 2 = n(rho) = 7
STRUCTURE = {
    "d10.13": {"cusps": 6, "eigen": (0, 3), "interior": (0, 3)},
    "d10.16": {"cusps": 4, "eigen": (0, 2, 3, 4), "interior": (0, 2, 3, 4)},
    "d10.36": {"cusps": 6, "eigen": (0, 3), "interior": (0, 3)},
    "d10.40": {"cusps": 4, "eigen": (0, 2, 3, 4), "interior": (0, 2, 3, 4)},
}
_CACHE = {}


def lib():
    import importlib.util
    if "b1542_ncyc" not in sys.modules:
        spec = importlib.util.spec_from_file_location("b1542_ncyc", HERE / "ncyc.py")
        mod = importlib.util.module_from_spec(spec)
        sys.modules["b1542_ncyc"] = mod
        spec.loader.exec_module(mod)
    return sys.modules["b1542_ncyc"]


def rd(r):
    """a reading, compacted (sm:B1536's run.rd)"""
    return {"count": [r["I(W)"], r["I(L2W)"]], "k": r["k"], "b0": r["b0"], "n(L)": r["n(L)"], "n((VL)*)": r["n((VL)*)"],
            "n(V)": r["n(V)"], "rk d1": r["rk d1"], "bound W": r["rk d1(E*) bound"],
            "bound L2": r["rk d1"]["L2*"] - r["k"], "all": r["all"], "failed": [k for k, v in r["checks"].items() if not v]}


def setup(cid):
    """per process and cover: the cover N, route N's class space at p_N, route R at p_N (for the transported classes) and at its
    own p_R"""
    if cid in _CACHE:
        return _CACHE[cid]
    L = lib()
    st, perms, pts, tau = L.build("m003", cid, PSI[0], PSI[1], K)
    G = st["G"]
    gens = list(G.gens)
    B, pa, chi, (mod, Zb, Rm, BP), cusps = L.route_n_setup(st, perms)
    cov = L.R.PCover(G, perms)
    rhoN = {g: np.asarray(B.rho[g], dtype=np.int64) % B.p for g in gens}
    cus, Lc, Nroot, _ = L.POP.characters(st, perms)
    pR = L.GF.primes_1_mod(Nroot, 1 << 31, 1)[0]
    BR = L.N.Base(st, L.GF.GF(pR, Nroot))
    chiR = BR.character((Fr(0), Fr(0)), Fr(0))
    rhoR = {g: np.asarray(BR.rho[g], dtype=np.int64) % pR for g in gens}
    CR = L.R.Coh(cov, L.R.lift(cov, rhoR, pR), keep=True)
    TR = L.deck_R_matrix(cov, rhoR, tau, pR)
    _CACHE[cid] = dict(L=L, cid=cid, st=st, perms=perms, tau=tau, G=G, gens=gens, B=B, pa=pa, chi=chi, Zb=Zb, Rm=Rm, BP=BP,
                       cusps=cusps, cov=cov, rhoN=rhoN, pR=pR, BR=BR, chiR=chiR, rhoR=rhoR, CR=CR, TR=TR)
    return _CACHE[cid]


def subspaces(cid):
    """the sealed list of (part, name) on one cover: the cusp strata, then the eigenspace pieces, then the pulled-back class"""
    s = STRUCTURE[cid]
    nc = s["cusps"]
    out = [("A", "S=" + ",".join(map(str, S))) for k in range(nc + 1) for S in combinations(range(nc), k)]
    out += [("B", f"j={j}") for j in s["eigen"]] + [("B", f"j={j} interior") for j in s["interior"]]
    return out + [("C", "pulled back")]


def rng_for(cid, route, name, draw):
    return random.Random(zlib.crc32(f"B1542|{cid}|{route}|{name}|{draw}".encode()))


def class_N(c, name, draw):
    """route N's class for (name, draw): a cocycle vector at p_N"""
    L = c["L"]
    p, Zb = c["B"].p, c["Zb"]
    nc = len(c["cusps"])
    rng = rng_for(c["cid"], "N", name, draw)
    if name.startswith("S="):
        S = [int(x) for x in name[2:].split(",") if x != ""]
        kill = [O for O in range(nc) if O not in S]
        Bs = L.N.stratum_basis(Zb, c["Rm"], c["BP"], c["cusps"], kill, 4, p)
        coeff = np.array([rng.randrange(1, p) for _ in range(Bs.shape[1])], dtype=np.int64)
        return (Zb @ ((Bs @ coeff) % p)) % p
    j = int(name.split()[0][2:])
    if name.endswith("interior"):
        Bs = L.N.stratum_basis(Zb, c["Rm"], c["BP"], c["cusps"], list(range(nc)), 4, p)
        coeff = np.array([rng.randrange(1, p) for _ in range(Bs.shape[1])], dtype=np.int64)
        z = (Zb @ ((Bs @ coeff) % p)) % p
    else:
        coeff = np.array([rng.randrange(1, p) for _ in range(Zb.shape[1])], dtype=np.int64)
        z = (Zb @ coeff) % p
    return L.project(z, lambda v: L.deck_N(v, c["tau"], len(c["gens"])), j, p, K)


def class_R(c, name, draw):
    """route R's own class for (name, draw): values on the Schreier generators at p_R"""
    L = c["L"]
    p, C = c["pR"], c["CR"]
    Z = C.Zrows % p
    e, ng = 4, len(c["cov"].sgens)
    nc = len(c["cusps"])
    rng = rng_for(c["cid"], "R", name, draw)

    def stratum_rows(kill):
        if not kill:
            return [np.eye(Z.shape[0], dtype=np.int64)[i] for i in range(Z.shape[0])]
        RZ = L.R.mm(C.R, Z.T, p)
        A = np.zeros((2 * e * len(kill), Z.shape[0] + e * len(kill)), dtype=np.int64)
        for i, O in enumerate(kill):
            A[2 * e * i:2 * e * (i + 1), :Z.shape[0]] = RZ[2 * e * O:2 * e * (O + 1)]
            A[2 * e * i:2 * e * (i + 1), Z.shape[0] + e * i:Z.shape[0] + e * (i + 1)] = \
                (-C.BP[2 * e * O:2 * e * (O + 1), e * O:e * (O + 1)]) % p
        Kn = L.R.pnull(A, p, Z.shape[0] + e * len(kill))
        return [k[:Z.shape[0]] for k in Kn if np.any(k[:Z.shape[0]] % p)]

    def draw_from(rows):
        w = np.zeros(Z.shape[0], dtype=np.int64)
        for r in rows:
            w = (w + (rng.randrange(1, p) * (r % p)) % p) % p
        return L.R.mm(w.reshape(1, -1), Z, p).ravel()
    if name.startswith("S="):
        S = [int(x) for x in name[2:].split(",") if x != ""]
        z = draw_from(stratum_rows([O for O in range(nc) if O not in S]))
    else:
        j = int(name.split()[0][2:])
        z = draw_from(stratum_rows(list(range(nc)) if name.endswith("interior") else []))
        # route_r's modular product: p_R is near 2**31, so a raw int64 product TR @ v would overflow (sm:B1541's K2 caught it)
        z = L.project(z, lambda v: L.R.mm(c["TR"], v.reshape(-1, 1), p).ravel(), j, p, K)
    return [z[k * e:(k + 1) * e] for k in range(ng)]


def pulled_back(c, route):
    L = c["L"]
    G = c["G"]
    if route == "N":
        B, d = c["B"], len(c["perms"]["a"])
        pa1 = L.N.perm_arrays(G, {"a": [0], "b": [0], "t": [0]})
        z = L.N.base_classes(B, L.N.tensor(B, L.N.small_four(B, c["chi"], 5), pa1))["c1"]
        cz = {g: z[gi * 4:(gi + 1) * 4] for gi, g in enumerate(B.gens)}
        return rd(L.N.reading(B, c["pa"], c["chi"], {g: [cz[g]] * d for g in B.gens}))
    p = c["pR"]
    Veta = {g: c["rhoR"][g] * pow(int(c["chiR"][g]), 5, p) % p for g in c["gens"]}
    c0 = L.R.base_cocycle(G, Veta, p)
    return rd(L.R.reading(c["cov"], c["BR"].rho, c["chiR"], L.R.cocycle_on_words(G, Veta, c0, c["cov"].sword, p), p))


def task(t):
    cid, part, name, draw = t
    c = setup(cid)
    L = c["L"]
    t0 = time.time()
    rows = []
    base = {"cover": cid, "part": part, "subspace": name, "draw": draw}
    if part == "C":
        for route in ("N", "R"):
            rows.append(dict(base, route=route, prime=c["B"].p if route == "N" else c["pR"], reading=pulled_back(c, route)))
    else:
        z = class_N(c, name, draw)
        d = len(c["perms"]["a"])
        rN = rd(L.N.reading(c["B"], c["pa"], c["chi"], L.N.local_from(z, c["B"].gens, d)))
        rows.append(dict(base, route="N", prime=c["B"].p, reading=rN))
        cv = L.transport(z, c["st"], c["perms"], c["cov"], c["B"])
        rT = rd(L.R.reading(c["cov"], c["B"].rho, c["chi"], cv, c["B"].p))
        rows.append(dict(base, route="R at p_N (the same class)", prime=c["B"].p, reading=rT))
        cvR = class_R(c, name, draw)
        rR = rd(L.R.reading(c["cov"], c["BR"].rho, c["chiR"], cvR, c["pR"]))
        rows.append(dict(base, route="R", prime=c["pR"], reading=rR))
    for r in rows:
        r["seconds"] = round(time.time() - t0, 1)
    return rows


def tasks():
    out = []
    for cid in COVERS:
        for part, name in subspaces(cid):
            for draw in (range(1) if part == "C" else range(DRAWS)):
                out.append((cid, part, name, draw))
    return out


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
                done.add((r["cover"], r["part"], r["subspace"], r["draw"]))
    todo = [t for t in tasks() if t not in done]
    print(f"B1542 run: {len(todo)} tasks to read ({len(done)} done)", flush=True)
    with get_context("spawn").Pool(workers) as pool:
        for rows in pool.imap_unordered(task, todo):
            if rec:
                with open(out, "a") as f:
                    for r in rows:
                        f.write(json.dumps(r) + "\n")
                    f.flush()
                    os.fsync(f.fileno())
            print(f"{rows[0]['cover']} {rows[0]['part']} {rows[0]['subspace']} draw {rows[0]['draw']}: {len(rows)} readings, "
                  f"{rows[-1]['seconds']} s", flush=True)


if __name__ == "__main__":
    main()
