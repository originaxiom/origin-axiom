#!/usr/bin/env python3
"""B1541's audit by route F (route_f.py), before the bank: NO NEGATIVE FROM A BUG (WORKING_RULES 2026-10-01) asks for an
independent re-derivation of the counts a NEGATIVE rests on -- a different method (a second presentation), separate code
(route_f.py imports numpy and the standard library only), a live positive control on the same code path (the run's non-zero
counts must come back exactly), and several primes (three, p = 1 mod 120 in (2^25, 2^26), none of the run's).

Route F reads the data export_f.py wrote (route_f_input_n45.json) and checks it itself: the four is a representation of the
two-generator presentation, b's matrix and permutation are its word's, the cusp words commute and are unipotent, and the deck
permutation tau commutes with the action and has order 5.  It then reads N_45's structure (cusps, h^1(rho), n(rho), n(1), tau's
eigenspaces and their interior parts) and, at two generic draws per prime, the counts in nine of the run's subspaces:
  the cusp strata S = {}, {0}, {0, 1, 2}, {0, 1, 2, 3} and all five (cusps matched to sm:B1536's order by their point sets);
  tau's eigenspace for zeta^0 and for one zeta^j, j != 0, each with its interior part.
The run's labels j = 1..4 depend on the choice of zeta mod p; the run read one count on all four, which route F's j = 1 must give.

    python3 audit_f.py [--record]     ->  audit_f.json (exit status 1 if route F disagrees with the run anywhere)"""
import importlib.util
import json
import random
import sys
import time
import zlib
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
SUBSPACES = [("A", "S="), ("A", "S=0"), ("A", "S=0,1,2"), ("A", "S=0,1,2,3"), ("A", "S=0,1,2,3,4"),
             ("B", "j=0"), ("B", "j=0 interior"), ("B", "j=1"), ("B", "j=1 interior")]
DRAWS = 2


def load_route_f():
    spec = importlib.util.spec_from_file_location("b1541_route_f", HERE / "route_f.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules["b1541_route_f"] = mod
    spec.loader.exec_module(mod)
    return mod


def subspace_basis(F, C, cov, kill, p):
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
    data = json.loads((HERE / "route_f_input_n45.json").read_text())
    run = json.loads((HERE / "read_out.json").read_text())["the counts by subspace (route N; route R's own)"]
    S = F.State(data)
    cov = F.Cover(S, data["perms"])
    tau, k, d = data["tau"], data["k"], cov.d
    P = cov.P
    assert all(P[g][tau[x]] == tau[P[g][x]] for g in ("a", "t") for x in range(d)), "tau does not commute with the action"
    tk = list(range(d))
    for m in range(1, k + 1):
        tk = [tau[x] for x in tk]
        assert (tk == list(range(d))) == (m == k), "tau does not have order k"
    # route F's cusps in sm:B1536's order, matched by their point sets
    order = {frozenset(o): i for i, o in enumerate(data["cusps (sm:B1536's order)"])}
    ours = [order[frozenset(T["orbit"])] for T in cov.cusps]
    assert sorted(ours) == list(range(len(ours))), "the cusps do not match"
    rep = {"route F": {"presentation": f"<a, t | {S.R}>, b = {S.b_word}", "cusp words": list(S.cusp), "cusps": len(cov.cusps)},
           "primes": {}, "readings": [], "disagreements": []}
    t0 = time.time()
    for p in F.primes(3):
        z = F.root_of_order(p, 24)
        zk = F.root_of_order(p, k)
        mats = S.four(p, z)
        chk = S.checks(mats, p)
        assert all(chk.values()), chk
        C = F.Coh(cov, F.base_system(cov, mats), p, keep=True)
        one = {g: np.eye(1, dtype=np.int64) for g in "abt"}
        C1 = F.Coh(cov, F.base_system(cov, one), p)
        interior = subspace_basis(F, C, cov, list(range(len(cov.cusps))), p)
        st = {"checks": chk, "h1(rho)": C.h1, "n(rho)": C.n, "n(1)": C1.n,
              "eigenspaces": eigen_dims(F, C.Z, C.D0, tau, d, k, zk, p),
              "interior parts": eigen_dims(F, interior, C.D0, tau, d, k, zk, p)}
        rep["primes"][str(p)] = st
        print(p, json.dumps({x: y for x, y in st.items() if x != "checks"}), round(time.time() - t0, 1), "s", flush=True)
        for part, name in SUBSPACES:
            for draw in range(DRAWS):
                rng = random.Random(zlib.crc32(f"B1541|F|{name}|{draw}|{p}".encode()))
                if name.startswith("S="):
                    Sset = {int(x) for x in name[2:].split(",") if x != ""}
                    kill = [i for i, lab in enumerate(ours) if lab not in Sset]
                    Bs = subspace_basis(F, C, cov, kill, p)
                    zc = F.mm(Bs, np.array([[rng.randrange(1, p)] for _ in range(Bs.shape[1])], dtype=np.int64), p).ravel()
                else:
                    j = int(name.split()[0][2:])
                    Bs = interior if name.endswith("interior") else C.Z
                    zc = F.mm(Bs, np.array([[rng.randrange(1, p)] for _ in range(Bs.shape[1])], dtype=np.int64), p).ravel()
                    zc = F.project(zc, tau, d, 4, j, k, zk, p)
                cnt, n = F.count(cov, mats, zc, p)
                want = run[f"{part} {name}"]
                ok = len(want) == 1 and cnt == want[0]
                rep["readings"].append({"prime": p, "subspace": f"{part} {name}", "draw": draw, "count": cnt, "n": n,
                                        "the run's count": want, "agrees": ok})
                if not ok:
                    rep["disagreements"].append([p, f"{part} {name}", draw, cnt, want])
                print(p, part, name, draw, cnt, "run", want, "ok" if ok else "DISAGREES", round(time.time() - t0, 1), "s",
                      flush=True)
    want_struct = {"h1(rho)": 23, "n(rho)": 18, "n(1)": 4, "eigenspaces": [3, 5, 5, 5, 5]}
    rep["structure agrees"] = all(all(st[x] == y for x, y in want_struct.items()) for st in rep["primes"].values())
    rep["positive control: non-zero counts returned exactly"] = sum(1 for r in rep["readings"]
                                                                    if r["agrees"] and r["count"] != [0, 0])
    rep["agrees"] = bool(rep["structure agrees"] and not rep["disagreements"]
                         and len(rep["readings"]) == 3 * len(SUBSPACES) * DRAWS)
    rep["seconds"] = round(time.time() - t0, 1)
    print("route F agrees with the run:", rep["agrees"], "| structure", rep["structure agrees"],
          "| non-zero counts reproduced", rep["positive control: non-zero counts returned exactly"])
    if "--record" in sys.argv:
        (HERE / "audit_f.json").write_text(json.dumps(rep, indent=1) + "\n")
    sys.exit(0 if rep["agrees"] else 1)


if __name__ == "__main__":
    main()
