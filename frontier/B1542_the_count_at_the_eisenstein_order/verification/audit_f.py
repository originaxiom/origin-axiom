#!/usr/bin/env python3
"""B1542's audit by route F (sm:B1541's route_f.py, loaded by path), before the bank (the seal's section 9; NO NEGATIVE FROM A
BUG, WORKING_RULES 2026-10-01; the load-bearing rule of 2026-10-06).  Route F is separate code (numpy and the standard library
only) on a second presentation, at three primes p = 1 mod 120 in (2^25, 2^26), none of the run's.

It reads the data export_f.py wrote (route_f_input_degree60.json) and checks it itself: the four is a representation of the
two-generator presentation; b's matrix and permutation are its word's; the cusp words commute and are unipotent; each cover's
deck permutation tau commutes with the action and has order 6.  On each of the four covers it then reads the structure (cusps,
h^1(rho), n(rho), n(1), tau's eigenspaces and their interior parts) and, at two generic draws per prime, the counts in these of
the run's subspaces (the seal's section 9: for NEGATIVE, at least one per cover of each kind read; for PROVED, the subspace that
read (-3, -3), added by --also):
  the cusp strata S = {} (the interior), {0} and all cusps (cusps matched to sm:B1536's order by their point sets);
  tau's eigenspaces for zeta^0 and zeta^3 = -1 (label-free), each with its interior part; on d10.16's and d10.40's covers also
  zeta^2 (the run's zeta^2 and zeta^4 are complex conjugate, so route F's zeta^2 must give a count the run read on one of them).

    python3 audit_f.py [--also "cover part name"] [--record]   ->  audit_f.json (exit 1 if route F disagrees anywhere)"""
import importlib.util
import json
import random
import sys
import time
import zlib
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
ROUTE_F = ROOT / "frontier" / "B1541_the_count_on_the_room" / "verification" / "route_f.py"
DRAWS = 2


def load_route_f():
    spec = importlib.util.spec_from_file_location("b1542_route_f", ROUTE_F)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["b1542_route_f"] = mod
    spec.loader.exec_module(mod)
    return mod


def subspace_basis(F, C, kill, p):
    """cocycles (columns) whose restriction to every cusp in kill is a coboundary of that cusp"""
    Z = C.Z
    if not kill:
        return Z
    e = 4
    RZ = F.mm(C.R, Z, p)
    A = np.zeros((2 * e * len(kill), Z.shape[1] + e * len(kill)), dtype=np.int64)
    for i, T in enumerate(kill):
        A[2 * e * i:2 * e * (i + 1), :Z.shape[1]] = RZ[2 * e * T:2 * e * (T + 1)]
        A[2 * e * i:2 * e * (i + 1), Z.shape[1] + e * i:Z.shape[1] + e * (i + 1)] = \
            (-C.BP[2 * e * T:2 * e * (T + 1), e * T:e * (T + 1)]) % p
    K = F.nullspace(A, p)[:Z.shape[1]]
    return F.mm(Z, K, p)


def eigen_dims(F, Z, D0, tau, d, k, zk, p):
    rB = F.rank(D0, p)
    out = []
    for j in range(k):
        PZ = np.stack([F.project(Z[:, i], tau, d, 4, j, k, zk, p) for i in range(Z.shape[1])], axis=1)
        out.append(F.rank(np.hstack([PZ, D0]), p) - rB)
    return out


def main():
    F = load_route_f()
    data = json.loads((HERE / "route_f_input_degree60.json").read_text())
    run = json.loads((HERE / "read_out.json").read_text())["the counts by subspace (route N; route R's own)"]
    expect = json.loads((HERE / "controls.json").read_text())["K2"]
    also = []
    args = sys.argv[1:]
    for i, a in enumerate(args):
        if a == "--also":
            cid, part, name = args[i + 1].split(" ", 2)
            also.append((cid, part, name))
    S = F.State({k: data[k] for k in ("gens", "rels", "cusp", "holonomy")})
    k = data["k"]
    rep = {"route F": {"presentation": f"<a, t | {S.R}>, b = {S.b_word}", "cusp words": list(S.cusp)}, "covers": {},
           "readings": [], "disagreements": []}
    t0 = time.time()
    for cid, cd in data["covers"].items():
        cov = F.Cover(S, cd["perms"])
        tau, d = cd["tau"], cov.d
        assert all(cov.P[g][tau[x]] == tau[cov.P[g][x]] for g in ("a", "t") for x in range(d)), "tau does not commute"
        tk = list(range(d))
        for m in range(1, k + 1):
            tk = [tau[x] for x in tk]
            assert (tk == list(range(d))) == (m == k), "tau does not have order k"
        order = {frozenset(o): i for i, o in enumerate(cd["cusps (sm:B1536's order)"])}
        ours = [order[frozenset(T["orbit"])] for T in cov.cusps]
        assert sorted(ours) == list(range(len(ours))), "the cusps do not match"
        nc = len(ours)
        subs = [("A", "S="), ("A", "S=0"), ("A", "S=" + ",".join(map(str, range(nc)))), ("B", "j=0"), ("B", "j=0 interior"),
                ("B", "j=3"), ("B", "j=3 interior")]
        if nc == 4:
            subs += [("B", "j=2"), ("B", "j=2 interior")]
        subs += [(p_, n_) for c_, p_, n_ in also if c_ == cid and (p_, n_) not in subs]
        rep["covers"][cid] = {"cusps": nc, "primes": {}}
        for p in F.primes(3):
            z = F.root_of_order(p, 24)
            zk = F.root_of_order(p, k)
            mats = S.four(p, z)
            chk = S.checks(mats, p)
            assert all(chk.values()), chk
            C = F.Coh(cov, F.base_system(cov, mats), p, keep=True)
            C1 = F.Coh(cov, F.base_system(cov, {g: np.eye(1, dtype=np.int64) for g in "abt"}), p)
            interior = subspace_basis(F, C, list(range(nc)), p)
            st = {"h1(rho)": C.h1, "n(rho)": C.n, "n(1)": C1.n, "eigenspaces": eigen_dims(F, C.Z, C.D0, tau, d, k, zk, p),
                  "interior parts": eigen_dims(F, interior, C.D0, tau, d, k, zk, p)}
            st["as K2"] = (st["h1(rho)"] == expect[cid]["h1 (route N p_N, route R p_N, route R p_R)"][0]
                           and st["eigenspaces"] == expect[cid]["eigenspaces (route N; route R, p_R)"][0]
                           and st["interior parts"] == expect[cid]["interior parts (route N; route R, p_R)"][0])
            rep["covers"][cid]["primes"][str(p)] = st
            print(cid, p, json.dumps(st), round(time.time() - t0, 1), "s", flush=True)
            for part, name in subs:
                for draw in range(DRAWS):
                    rng = random.Random(zlib.crc32(f"B1542|F|{cid}|{name}|{draw}|{p}".encode()))
                    if name.startswith("S="):
                        Sset = {int(x) for x in name[2:].split(",") if x != ""}
                        Bs = subspace_basis(F, C, [i for i, lab in enumerate(ours) if lab not in Sset], p)
                        zc = F.mm(Bs, np.array([[rng.randrange(1, p)] for _ in range(Bs.shape[1])], dtype=np.int64), p).ravel()
                    else:
                        j = int(name.split()[0][2:])
                        Bs = interior if name.endswith("interior") else C.Z
                        zc = F.mm(Bs, np.array([[rng.randrange(1, p)] for _ in range(Bs.shape[1])], dtype=np.int64),
                                  p).ravel()
                        zc = F.project(zc, tau, d, 4, j, k, zk, p)
                    cnt, n = F.count(cov, mats, zc, p)
                    key = f"{cid} {part} {name}"
                    want = run.get(key, [])
                    if part == "B" and name.split()[0] in ("j=2", "j=4"):        # complex conjugate pieces: either label
                        alt = key.replace("j=2", "j=4") if "j=2" in key else key.replace("j=4", "j=2")
                        want = want + run.get(alt, [])
                    ok = len(want) >= 1 and cnt in want
                    rep["readings"].append({"cover": cid, "prime": p, "subspace": f"{part} {name}", "draw": draw,
                                            "count": cnt, "n": n, "the run's count": want, "agrees": ok})
                    if not ok:
                        rep["disagreements"].append([cid, p, f"{part} {name}", draw, cnt, want])
                    print(cid, p, part, name, draw, cnt, "run", want, "ok" if ok else "DISAGREES",
                          round(time.time() - t0, 1), "s", flush=True)
    rep["structure agrees"] = all(st["as K2"] for c in rep["covers"].values() for st in c["primes"].values())
    rep["positive control: non-zero counts returned exactly"] = sum(1 for r in rep["readings"]
                                                                    if r["agrees"] and r["count"] != [0, 0])
    rep["agrees"] = bool(rep["structure agrees"] and not rep["disagreements"])
    rep["seconds"] = round(time.time() - t0, 1)
    print("route F agrees with the run:", rep["agrees"], "| structure", rep["structure agrees"],
          "| non-zero counts reproduced", rep["positive control: non-zero counts returned exactly"], "of", len(rep["readings"]))
    if "--record" in sys.argv:
        (HERE / "audit_f.json").write_text(json.dumps(rep, indent=1) + "\n")
    sys.exit(0 if rep["agrees"] else 1)


if __name__ == "__main__":
    main()
