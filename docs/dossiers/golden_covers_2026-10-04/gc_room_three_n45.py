#!/usr/bin/env python3
"""The golden covers dossier, section 7: room for three on a degree-45 cover of m003, fixed by sm:B1536's banked rows and
Lemma A, and read directly in two routes.  Nothing here is a sealed arc's reading.

  1. The banked rows (sm:B1536, m003's d9.2, routes R and N identical): at the pulled-back character nu = (u, kappa), n(L) is the
     line at nu^-4 and n((VL)*) the four at nu^3 (rho self-dual).  With u = (1/5, 3/5) times j (j = 1..4) and kappa = 0:
     nu^-4 = nu and nu^3 = (3u, 0), so the line is 1 and the four is 4 at every order-5 character chi^j.
  2. Lemma A (the cyclic cover's supplies, Shapiro and Mackey): the 5-fold cyclic cover N_45 of d9.2 along chi has
     n(1) = 0 + 4 x 1 = 4 and n(rho) = 2 + 4 x 4 = 18, so min(capW, capL2) = min(1 + 4, 18) = 5 at its trivial character.
  3. Read directly: route N (sm:B1536's route_n, Shapiro on m003 with the degree-45 permutation module), route R' (route_r on
     N_45's own Reidemeister-Schreier presentation, another prime), and N_45's integer homology (b1 - cusps = n(1)).

    python3 gc_room_three_n45.py      (about 30 s)"""
import gzip
import importlib.util
import json
from fractions import Fraction as Fr
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[3]
V = ROOT / "frontier" / "B1539_the_room_above_the_room" / "verification"
spec = importlib.util.spec_from_file_location("gc_b1539_controls", V / "controls.py")
K = importlib.util.module_from_spec(spec)
spec.loader.exec_module(K)
O, PO = K.O, K.PO


def banked_d92():
    out = {}
    for route in ("R", "N"):
        for line in gzip.open(O.B1536V / f"run_{route}_m003.jsonl.gz", "rt"):
            r = json.loads(line)
            if not r.get("done") and r["cover"] == "d9.2":
                out[(route, tuple(r["u"]), r["kappa"])] = r["S"]
    return out


def main():
    rep = {}
    bk = banked_d92()
    u0 = (Fr(1, 5), Fr(3, 5))
    us = [tuple((j * x) % 1 for x in u0) for j in range(5)]
    line, four = {}, {}
    for route in ("R", "N"):
        for j, u in enumerate(us):
            key = lambda uu: (route, (str(uu[0]), str(uu[1])), "0")  # noqa: E731
            # the line at chi^j = (u, 0) is n(L) at nu = (u, 0) (nu^-4 = nu on the 5-torsion);
            # the four at chi^j is n((VL)*) at nu = (2u, 0) (nu^3 = (6u, 0) = (u, 0))
            line[(route, j)] = bk[key(u)]["n(L)"] if j else 0
            u2 = tuple((2 * x) % 1 for x in u)
            four[(route, j)] = bk[key(u2)]["n((VL)*)"]
    rep["banked: the line at chi^j, j = 0..4 (routes R, N)"] = [[line[("R", j)] for j in range(5)],
                                                               [line[("N", j)] for j in range(5)]]
    rep["banked: the four at chi^j, j = 0..4 (routes R, N)"] = [[four[("R", j)] for j in range(5)],
                                                               [four[("N", j)] for j in range(5)]]
    n1 = sum(line[("R", j)] for j in range(5))
    nr = sum(four[("R", j)] for j in range(5))
    rep["Lemma A on N_45: (n(1), n(rho))"] = [n1, nr]
    rep["Lemma A: room at the trivial character"] = min(1 + n1, nr)
    st = O.CL.state("m003")
    G = st["G"]
    covs = dict(PO.POP.covers(st))
    chars, Nroot, p, B, cov, rho_np = K.pulled_setup(st, covs["d9.2"])
    ab = O.Ab(cov)
    exps = K.along_words(cov, B.character(u0, Fr(0)), p, Nroot)
    c = ab.coordinates(exps, Nroot)
    rep["chi as an own character of d9.2 (mod %d)" % Nroot] = list(c)
    rep["order of chi"] = O.order_of(c, Nroot)
    rep["route R' on d9.2 at chi^j (n(chi^j), n(rho chi^j)), j = 1..4"] = [
        [O.frame_own(cov, rho_np, [(j * e) % Nroot for e in exps], Nroot, p)[k] for k in ("n(nu)", "n(rho nu)")]
        for j in range(1, 5)]
    pe, nA = O.abelian_cover(cov, ab, [c], Nroot)
    rep["N_45: degree, connected, cusps"] = [len(pe["a"]), bool(O.CL.check_cover(G, pe)), len(O.CL.cusps(G, pe))]
    rep["route N on N_45 at the trivial character: (n(1), n(rho))"] = list(K.route_n(st, pe))
    m = 6
    pR = O.route_primes(m)["R"]
    BR = O.RN.Base(st, O.GF.GF(pR, O.root_order(m)))
    rhoR = {g: np.asarray(BR.rho[g], dtype=np.int64) % pR for g in BR.gens}
    cov45 = O.R.PCover(G, pe)
    r45 = O.frame_own(cov45, rhoR, [0] * len(cov45.sgens), m, pR)
    rep["route R' on N_45 at the trivial character"] = {k: r45[k] for k in ("n(nu)", "n(rho nu)", "capW", "capL2",
                                                                            "h1(V_eta)", "n(V_eta)")}
    rep["route R' prime"] = pR
    ab45 = O.Ab(cov45)
    rep["N_45: H_1 (free rank, torsion); b1 - cusps"] = [len(ab45.free), [d for _, d in ab45.torsion],
                                                         len(ab45.free) - len(O.CL.cusps(G, pe))]
    agree = (rep["Lemma A on N_45: (n(1), n(rho))"] == rep["route N on N_45 at the trivial character: (n(1), n(rho))"]
             == [r45["n(nu)"], r45["n(rho nu)"]] and rep["N_45: H_1 (free rank, torsion); b1 - cusps"][2] == n1)
    rep["all agree"] = bool(agree)
    rep["room at the trivial character of N_45 (min(capW, capL2))"] = min(r45["capW"], r45["capL2"])
    print(json.dumps(rep, indent=1))
    return rep


if __name__ == "__main__":
    main()
