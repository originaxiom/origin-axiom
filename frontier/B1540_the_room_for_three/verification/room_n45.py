#!/usr/bin/env python3
"""B1540 -- THE ROOM FOR THREE: N_45's supplies and its one fixed count, from the banked rows and read directly.

  1. sm:B1536's banked rows (m003's d9.2; routes R and N): at the pulled-back character nu = (u, kappa), n(L) is the line at
     nu^-4 and n((VL)*) the four at nu^3 (rho is self-dual).  At chi^j = (j u0, 0), u0 = (1/5, 3/5): the line is n(L) at
     nu = (j u0, 0) (nu^-4 = nu on the 5-torsion) and the four is n((VL)*) at nu = (2 j u0, 0) (nu^3 = chi^j).
  2. Lemma A (Shapiro, Mackey at the cusps): N_45, the 5-fold cyclic cover of d9.2 along chi, has n(1) = sum_j n(chi^j) and
     n(rho) = sum_j n(rho chi^j).
  3. Read directly on N_45 (B1541's sealed n45.build, loaded by path): route N (Shapiro on m003 with the degree-45 permutation
     module, sm:B1536's route_n), route R (N_45's own presentation, sm:B1536's route_r, another prime), and the integer
     homology of N_45's presentation (PARI's Smith form): b1 - cusps = n(1).
  4. The count at the class pulled back from m003: the sum of sm:B1536's banked Part P counts at d9.2's five members (u, 0)
     (Shapiro, and W at nu = chi^k equal to chi^k (x) W at the trivial character), and read directly in both routes by
     sm:B1536's own Part P code path.

    python3 room_n45.py [--record]      ->  room_n45.json (about two minutes)"""
import gzip
import importlib.util
import json
import sys
from fractions import Fraction as Fr
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
B1541V = ROOT / "frontier" / "B1541_the_count_on_the_room" / "verification"


def _n45():
    if "b1540_n45" not in sys.modules:
        spec = importlib.util.spec_from_file_location("b1540_n45", B1541V / "n45.py")
        mod = importlib.util.module_from_spec(spec)
        sys.modules["b1540_n45"] = mod
        spec.loader.exec_module(mod)
    return sys.modules["b1540_n45"]


def banked(L):
    rows = {}
    for route in ("R", "N"):
        for line in gzip.open(L.B1536V / f"run_{route}_m003.jsonl.gz", "rt"):
            r = json.loads(line)
            if not r.get("done") and r["cover"] == "d9.2":
                rows[(route, tuple(r["u"]), r["kappa"])] = r
    return rows


def main():
    L = _n45()
    N, R, CL, POP, GF = L.N, L.R, L.CL, L.POP, L.GF
    from cypari import pari
    rep = {}
    rows = banked(L)
    us = [tuple((j * x) % 1 for x in L.U0) for j in range(5)]
    key = lambda route, u: (route, (str(u[0]), str(u[1])), "0")  # noqa: E731
    line = {r: [0 if j == 0 else rows[key(r, us[j])]["S"]["n(L)"] for j in range(5)] for r in ("R", "N")}
    four = {r: [rows[key(r, tuple((2 * x) % 1 for x in us[j]))]["S"]["n((VL)*)"] for j in range(5)] for r in ("R", "N")}
    rep["banked: the line at chi^j, j = 0..4 (routes R, N)"] = [line["R"], line["N"]]
    rep["banked: the four at chi^j, j = 0..4 (routes R, N)"] = [four["R"], four["N"]]
    sums = [sum(line["R"]), sum(four["R"])]
    rep["Lemma A: (n(1), n(rho)) of N_45"] = sums
    rep["Lemma A: room at the trivial character"] = min(1 + sums[0], sums[1])
    pcount = {r: [rows[key(r, u)]["P"]["count"] for u in us] for r in ("R", "N")}
    rep["banked Part P counts at d9.2's members (u, 0), u = j u0 (routes R, N)"] = [pcount["R"], pcount["N"]]
    rep["Proposition P: the count at the pulled-back class, by the banked rows"] = [sum(c[i] for c in pcount["R"]) for i in (0, 1)]
    # read directly on N_45
    st, perms, pts, tau = L.build()
    G = st["G"]
    gens = list(G.gens)
    cus = CL.cusps(G, perms)
    rep["N_45: degree, cusps, connected"] = [len(perms["a"]), len(cus), bool(CL.check_cover(G, perms))]
    B, pa, chi, _, _ = L.route_n_setup(st, perms)
    sN = N.supplies(B, pa, chi)
    rep["route N at the trivial character"] = {"prime": B.p, "n(1)": sN["n(L)"], "n(rho)": sN["n((VL)*)"],
                                               "capW": sN["capW"], "capL2": sN["capL2"]}
    _, Lc, Nroot, _ = POP.characters(st, perms)
    pR = GF.primes_1_mod(Nroot, 1 << 31, 1)[0]
    BR = N.Base(st, GF.GF(pR, Nroot))
    chiR = BR.character((Fr(0), Fr(0)), Fr(0))
    cov = R.PCover(G, perms)
    sR = R.supplies(cov, BR.rho, chiR, pR)
    rep["route R at the trivial character"] = {"prime": pR, "n(1)": sR["n(L)"], "n(rho)": sR["n((VL)*)"],
                                               "capW": sR["capW"], "capL2": sR["capL2"], "h1(rho)": sR["h1(V_eta)"]}
    # integer homology of N_45's presentation (the relator rows on the Schreier generators, Smith form)
    n = len(cov.sgens)
    rel = []
    for w in cov.rels:
        v = [0] * n
        for j, e in w:
            v[j] += e
        rel.append(v)
    while len(rel) < n:
        rel.append([0] * n)
    assert len(rel) == n, "more relators than generators"      # 90 relators, 91 Schreier generators on N_45
    D = pari.matsnf(pari.matrix(n, n, [x for r in rel for x in r]))
    d = [abs(int(x)) for x in D]
    free = sum(1 for x in d if x == 0) + max(0, n - len(d))
    rep["N_45: H_1 (free rank, torsion); b1 - cusps"] = [free, sorted(x for x in d if x > 1), free - len(cus)]
    # the pulled-back class, both routes, sm:B1536's Part P code path
    pa1 = N.perm_arrays(G, {"a": [0], "b": [0], "t": [0]})
    z = N.base_classes(B, N.tensor(B, N.small_four(B, chi, 5), pa1))["c1"]
    cz = {g: z[gi * 4:(gi + 1) * 4] for gi, g in enumerate(B.gens)}
    rn = N.reading(B, pa, chi, {g: [cz[g]] * len(perms["a"]) for g in B.gens})
    Veta = {g: np.asarray(BR.rho[g], dtype=np.int64) * pow(int(chiR[g]), 5, pR) % pR for g in gens}
    c0 = R.base_cocycle(G, Veta, pR)
    rr = R.reading(cov, BR.rho, chiR, R.cocycle_on_words(G, Veta, c0, cov.sword, pR), pR)
    rep["the pulled-back class read directly (I(W), I(L2W), identities), routes N and R"] = [
        [rn["I(W)"], rn["I(L2W)"], rn["all"]], [rr["I(W)"], rr["I(L2W)"], rr["all"]]]
    agree = (sums == [rep["route N at the trivial character"]["n(1)"], rep["route N at the trivial character"]["n(rho)"]]
             == [rep["route R at the trivial character"]["n(1)"], rep["route R at the trivial character"]["n(rho)"]]
             and rep["N_45: H_1 (free rank, torsion); b1 - cusps"][2] == sums[0]
             and line["R"] == line["N"] and four["R"] == four["N"] and pcount["R"] == pcount["N"]
             and [rn["I(W)"], rn["I(L2W)"]] == [rr["I(W)"], rr["I(L2W)"]]
             == rep["Proposition P: the count at the pulled-back class, by the banked rows"] and rn["all"] and rr["all"])
    rep["every route agrees"] = bool(agree)
    rep["room at the trivial character of N_45: min(capW, capL2)"] = min(sR["capW"], sR["capL2"])
    print(json.dumps(rep, indent=1))
    if "--record" in sys.argv:
        (HERE / "room_n45.json").write_text(json.dumps(rep, indent=1) + "\n")
    if not agree:      # fail closed (the audit lane's R92): a disagreeing run is kept on record, and exits non-zero
        raise SystemExit("room_n45.py: the routes disagree (see 'every route agrees' above)")
    return rep


if __name__ == "__main__":
    main()
