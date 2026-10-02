"""B1514 -- controls, run BEFORE the seal on banked data and on structure only (no Higgs-sector dimension, twisted-bulk cohomology or
coupling at a case-(b) member is computed here).

K1  the populations: 18 (level, class, lam) groups and 184 members per prime-root, read from B1511's and B1512's records.
K2  route T's relative fundamental class: dC = z on levels 4, 5 and 6.
K3  the banked identity, both routes: at every member of every population (one prime-root each; M4 also exactly) h^1(L) = 1,
    h^1(V) and h^1(V_eta) as banked (2 at M5's w = 7, else 1), h^1(W1) = h^1(V) (B1511/B1512's a1), and on M4 h^1(W1*) = 2
    (B1511's b1).
K4  the positive control at every member, both routes: x u c != 0 (B1511 Theorem A: I(W1) = +1 iff x u c != 0; banked +1 at all).
K5  the generalised code at B1513's banked points, both routes: with an order-2 character L = nu^-4 is trivial and the member is
    B1513's W; the 10' coupling form is zero on s961's triplet and non-zero at B1510's +-i point, as banked.
K6  the cross-coupling lemma's hypotheses at random q (not a case-(b) point): rho_q is absolutely irreducible, and
    Hom(rho (x) rho, rho) = Hom(Lambda^2 rho, rho) = 0.
Record: controls_run.txt."""
import json
import random
import sys
import time
from pathlib import Path

import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import law_lib as LT  # noqa: E402
import lift_route as LR  # noqa: E402

H, T = LT.H, LT.T
IA = LR.IA
RECORD = HERE / "controls_run.txt"


def k1():
    pt, pl = LT.populations(), LR.populations()
    n_members = sum(sum(len(v) for v in p["orbits"].values()) for p in pl)
    same = [(a["label"], a["orbits"], a["lam"], a["factor"]) for a in pt] == [(b["label"], b["orbits"], b["lam"], b["factor"]) for b in pl]
    return {"populations": len(pl), "members per prime-root": n_members, "routes read the same populations": same,
            "pass": len(pl) == 18 and n_members == 184 and same}


def k2():
    out = {}
    for n in (4, 5, 6):
        G = H.FibredGroup(n)
        C, z, ok = G.fundamental()
        out[f"level {n}"] = {"cells": len(C), "checks": ok}
    out["pass"] = all(all(v["checks"].values()) for k, v in out.items() if k.startswith("level"))
    return out


def banked_h1(pop):
    if pop["level"] == 4:
        return {"L": 1, "V": 1, "V_eta": 1}
    h = pop["banked_h1"][0]
    return {"L": h[0], "V": h[1], "V_eta": h[2]}


def route_T_member_checks(G, C, z, field, rho, ab, N, lam_v, bank, level4):
    m = LT.Member(G, field, rho, ab, N, lam_v)
    hL, hV, hE = m.h1_L, H.h1_basis(m.V)[1], m.h1_Veta
    hW = H.h1_basis(m.W1)[1]
    hWd = H.h1_basis(m.W1d)[1] if level4 else None                    # banked only on M4 (B1511's b1 = 2)
    ctl = LT.control_triple(G, C, z, m)
    ok = (hL, hV, hE) == (bank["L"], bank["V"], bank["V_eta"]) and hW == hV and (not level4 or hWd == 2) and m.W1.check()
    return ok, any(v != field.dom.zero for v in ctl)


def route_L_member_checks(F, mn, n, ab, N, lam_v, zeta, bank, level4):
    m = LR.Member(F, mn, n, ab, N, lam_v, zeta)
    hL, hV, hE = (LR.h_data(r)["h1"] for r in (m.L, m.V, m.Veta))
    hW = LR.h_data(m.W1)["h1"]
    hWd = LR.h_data(m.W1d)["h1"] if level4 else None                  # banked only on M4 (B1511's b1 = 2)
    ok = (hL, hV, hE) == (bank["L"], bank["V"], bank["V_eta"]) and hW == hV and (not level4 or hWd == 2) and m.W1.relators_hold()
    return ok, LR.x_cup_c(m)["non-zero"]


def k3_k4(log):
    out = {"route T": [], "route L": []}
    q = T.Q
    # M4 exactly, both routes
    G4 = H.FibredGroup(4)
    C4, z4, _ = G4.fundamental()
    fT = T.Field("ext", g=q ** 2 - 7 * q + 1, base="Q12")
    rhoT = H.rho_mats(G4, fT)
    K = sp.QQ.algebraic_field(sp.sqrt(5), sp.sqrt(-3))
    FE = IA.Exact(K, "Q(sqrt 5, sqrt -3)")
    mnE = IA.mn_mats(FE, K.from_sympy((7 - 3 * sp.sqrt(5)) / 2))
    zeta3 = K.from_sympy((-1 + sp.sqrt(-3)) / 2)
    for pop in LR.populations():
        if pop["level"] != 4:
            continue
        for orbit in pop["orbits"].values():
            for ab in orbit:
                okT, ctlT = route_T_member_checks(G4, C4, z4, fT, rhoT, ab, 15, fT.dom.one, banked_h1(pop), True)
                okL, ctlL = route_L_member_checks(FE, mnE, 4, ab, 15, FE.c(1), zeta3, banked_h1(pop), True)
                out["route T"].append({"member": f"M4 {ab} exact", "banked": okT, "x u c != 0": ctlT})
                out["route L"].append({"member": f"M4 {ab} exact", "banked": okL, "x u c != 0": ctlL})
    log("K3/K4: M4 exact done")
    # every population mod p, one prime and one root each
    cache = {}
    for pop in LR.populations():
        n, lam = pop["level"], pop["lam"]
        N0 = pop["N"]
        orders = sorted({LR.reduce_char(ab, N0)[1] for orb in pop["orbits"].values() for ab in orb})
        orders = orders + ([4] if lam in ("i", "-i") else [])
        (p, roots), = LR.primes_for(pop["factor"], orders, 1, 2 ** 23 - 7919 * n)
        r = roots[0]
        iota = IA.sqrt_m1(p) if lam in ("i", "-i") else None
        if n not in cache:
            G = H.FibredGroup(n)
            cache[n] = (G,) + G.fundamental()[:2]
        G, C, z = cache[n]
        fT = T.Field("gf", p=p, r=r, iota=iota)
        rhoT = H.rho_mats(G, fT)
        lamT = LT.lam_value(fT, lam)
        FL = IA.ModP(p, f"GF({p})")
        mnL = IA.mn_mats(FL, r)
        lamL = {"1": 1, "-1": p - 1}.get(lam, iota if lam == "i" else (p - iota) % p if iota else None)
        for orbit in pop["orbits"].values():
            for ab in orbit:
                (a_, b_), Nr = LR.reduce_char(ab, N0)
                zeta = LR.root_of_unity(p, Nr)
                okT, ctlT = route_T_member_checks(G, C, z, fT, rhoT, ab, N0, lamT, banked_h1(pop), False)
                okL, ctlL = route_L_member_checks(FL, mnL, n, ab, N0, lamL, zeta, banked_h1(pop), False)
                out["route T"].append({"member": f"{pop['label']} {ab} p={p}", "banked": okT, "x u c != 0": ctlT})
                out["route L"].append({"member": f"{pop['label']} {ab} p={p}", "banked": okL, "x u c != 0": ctlL})
        log(f"K3/K4: {pop['label']} done (p = {p})")
    for route in ("route T", "route L"):
        rows = out[route]
        out[f"{route}: banked identity at every member"] = all(r["banked"] for r in rows)
        out[f"{route}: positive control at every member"] = all(r["x u c != 0"] for r in rows)
        out[f"{route}: members read"] = len(rows)
    out["pass"] = all(out[f"{r}: banked identity at every member"] and out[f"{r}: positive control at every member"]
                      for r in ("route T", "route L"))
    return out


def k5(log):
    """B1513's banked points through the generalised code (order-2 characters, L = 1): the 10' form B on H^1(W*)"""
    out = {}
    q = T.Q
    # s961's triplet, mod p (B1513 Part D's populations), and B1510's +-i point, mod p
    g6 = q ** 6 - 34 * q ** 3 + 1
    (p, roots), = LR.primes_for(g6, [4], 1, 2 ** 23 - 1000)
    r = roots[0]
    G3 = H.FibredGroup(3)
    C3, z3, _ = G3.fundamental()
    fT = T.Field("gf", p=p, r=r, iota=IA.sqrt_m1(p))
    rho = H.rho_mats(G3, fT)
    FL = IA.ModP(p, "k5")
    mnL = IA.mn_mats(FL, r)
    zeros_T, zeros_L = [], []
    for ab in [(0, 2), (2, 2), (2, 0)]:
        m = LT.Member(G3, fT, rho, ab, 4, -fT.dom.one)
        tens, nh, na = LT.coupling_tensor(G3, C3, z3, m.L2W, m.W1d, H.form_wedge(5))
        zeros_T.append(LT.all_zero(tens, fT.dom) and nh == 1 and na == 2)
        mL = LR.Member(FL, mnL, 3, ab, 4, p - 1, LR.root_of_unity(p, 2))
        zeros_L.append(LR.wedge_table(mL.L2Wd, mL.W1d)["zero"])
    out["triplet (banked zero), route T"] = zeros_T
    out["triplet (banked zero), route L"] = zeros_L
    g14 = q ** 2 - 14 * q + 1
    (p, roots), = LR.primes_for(g14, [4], 1, 2 ** 23 - 3000)
    r = roots[0]
    iota = IA.sqrt_m1(p)
    G1 = H.FibredGroup(1)
    C1, z1, _ = G1.fundamental()
    fT = T.Field("gf", p=p, r=r, iota=iota)
    rho = H.rho_mats(G1, fT)
    m = LT.Member(G1, fT, rho, (0, 0), 1, fT.dom(iota))
    tens, nh, na = LT.coupling_tensor(G1, C1, z1, m.L2W, m.W1d, H.form_wedge(5))
    out["+-i point (banked non-zero), route T"] = not LT.all_zero(tens, fT.dom)
    out["+-i point: B symmetric, route T"] = LT.symmetric(tens)
    FL = IA.ModP(p, "k5")
    mL = LR.Member(FL, IA.mn_mats(FL, r), 1, (0, 0), 1, iota, 1)
    out["+-i point (banked non-zero), route L"] = not LR.wedge_table(mL.L2Wd, mL.W1d)["zero"]
    out["pass"] = all(zeros_T) and all(zeros_L) and out["+-i point (banked non-zero), route T"] and out["+-i point (banked non-zero), route L"]
    log("K5 done")
    return out


def k6():
    """rho_q at random q mod p: End = scalars, Hom(rho (x) rho, rho) = 0, Hom(Lambda^2 rho, rho) = 0 (invariant dimensions)"""
    out = []
    rnd = random.Random(1514)
    for _ in range(3):
        p = int(sp.prevprime(rnd.randrange(2 ** 22, 2 ** 23)))
        F = IA.ModP(p, "k6")
        qv = rnd.randrange(2, p - 1)
        mn = IA.mn_mats(F, qv)
        rep = IA.level_rep(F, mn, 1, (1, 1, 1))
        R = {g: rep.g[g][0] for g in IA.GENS}
        Rd = {g: rep.g[g][1].T.copy() for g in IA.GENS}
        L2 = {g: rep.wedge2().g[g][0] for g in IA.GENS}

        def inv_dim(mats):
            size = next(iter(mats.values())).shape[0]
            rows = [(M - np.eye(size, dtype=np.int64)) % p for M in mats.values()]
            return size - F.rank(np.vstack(rows))
        end = inv_dim({g: np.kron(Rd[g], R[g]) % p for g in IA.GENS})                       # rho* (x) rho
        hom_tens = inv_dim({g: np.kron(np.kron(Rd[g], Rd[g]) % p, R[g]) % p for g in IA.GENS})   # (rho (x) rho)* (x) rho
        L2d = {g: rep.wedge2().g[g][1].T.copy() for g in IA.GENS}
        hom_l2 = inv_dim({g: np.kron(L2d[g], R[g]) % p for g in IA.GENS})                    # (Lambda^2 rho)* (x) rho
        out.append({"p": p, "q": qv, "dim End": end, "dim Hom(rho rho, rho)": hom_tens, "dim Hom(L2 rho, rho)": hom_l2})
    return {"rows": out, "pass": all(r["dim End"] == 1 and r["dim Hom(rho rho, rho)"] == 0 and r["dim Hom(L2 rho, rho)"] == 0 for r in out)}


def main():
    t0 = time.time()

    def log(msg):
        print(f"[{time.time() - t0:7.1f}s] {msg}", flush=True)
    rec = {}
    rec["K1"] = k1()
    log(f"K1 {rec['K1']['pass']}")
    rec["K2"] = k2()
    log(f"K2 {rec['K2']['pass']}")
    rec["K3_K4"] = k3_k4(log)
    log(f"K3/K4 {rec['K3_K4']['pass']}")
    rec["K5"] = k5(log)
    log(f"K5 {rec['K5']['pass']}")
    rec["K6"] = k6()
    log(f"K6 {rec['K6']['pass']}")
    rec["all pass"] = all(rec[k]["pass"] for k in ("K1", "K2", "K3_K4", "K5", "K6"))
    rec["seconds"] = round(time.time() - t0, 1)
    if "--record" in sys.argv:
        RECORD.write_text(json.dumps(rec, indent=1, sort_keys=True, default=str) + "\n", encoding="utf-8")
    print("ALL PASS:", rec["all pass"], rec["seconds"], "s")
    return rec


if __name__ == "__main__":
    main()
