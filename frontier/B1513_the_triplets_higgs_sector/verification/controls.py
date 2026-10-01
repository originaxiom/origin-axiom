"""B1513 controls, run before the seal.  None computes a sealed quantity: nothing here touches Lambda^2 rho_q, Lambda^2 W_k or a
coupling at the triplet's points, and nothing touches Lambda^2 rho_q at any q other than q = 1.

K1  the chains: ELL is the longitude (matrices), with eigenvalues q, q, q, q^-3 (B1510's Lemmas C and R); phi fixes ELL;
    d sigma = -[ell], dK(w) = w, dC = z, dz = 0 on levels 1-6; the prism identity dh + hd = 1 - c_t on test chains.
K2  G_n is pi_n: rho_q satisfies G_n's relators (symbolically, n = 1..4); B1511's banked triplet rows reproduced on G_3 exactly over
    Q[q]/(q^6 - 34 q^3 + 1): h^1(V_k) = h^1(V_k*) = 1, W_k's (a0, a1, t0, r1) = (0, 1, 1, 1), dual (1, 2, 1, 1), I(W_k) = -1, for all three.
K3  Shapiro at the hyperbolic point q = 1 (a theorem: h^1(M; Ad) = #cusps for each sl(2) factor of Lambda^2 rho_1 = so(3,1) (x) C):
    h^1(G_1; Lambda^2 rho_1) = 2, h^1(G_3; Lambda^2 rho_1) = 2, and the same on B1511's Reidemeister-Schreier presentation of M_3.
K4  the banked identity: B1510's exact kappa_l_hat at its six points equals the relative triple product <c u e u c*> of B1509's
    cocycles (generator_cocycle) with the fibration class, up to one global sign; zero at the two mu = -1 points.
K5  the instrument's invariances at B1510's +-i points: coboundaries added in each slot; the cyclic identity Y(c, e, c*) = Y(c*, c, e);
    the transposition Y(c, c*, e) = -Y(c, e, c*).
K6  the levels: B1510's classes pulled back to G_2 and G_3 (t = m^n) give the same number (the transfer: pi^* e = n e_n).
K7  the wedge form is invariant: T(L2(g) om, g.f, g.f') = T(om, f, f') for random integer g in GL(5).
K8  the fibre polynomial machinery: at q = 1, dim ker(S - 1) on H^1(F; Lambda^2 rho_1) = 2 (K3's value); for rho_q at B1509's points,
    ker (S - mu)^j on H^1(F; rho_q) is [1, 2] at mu = -1 (B1509 T3's Jordan block) and [1, 1] at +-i (B1510 Theorem B).
K9  the census's code paths on B1509's level-one W_1 (banked): interior_classes(W_1*) finds one class at mu = -1 and none at +-i
    (B1509's table: W_1* (b0, b1, s0, q1) = (1, 2, 1, 1) and (1, 2, 1, 2)), with a valid relative lift; Lambda^2 W_1 and Lambda^2 W_1*
    satisfy the relators; the projection Lambda^2 W -> V and the inclusion V* -> Lambda^2 W* commute with coboundaries; c* includes
    to a cocycle; a relative coboundary (delta u, u) in the first slot of the wedge triple product gives 0.  No Lambda^2 cohomology.
K10 the interpolated fibre polynomial of rho_q itself on m004 is B1509's banked monic Q (T3, tower_lib.Q_MONIC)."""
import json
import random
import sys
import time
from pathlib import Path

import sympy as sp
from sympy.polys.matrices import DomainMatrix

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import higgs_lib as H  # noqa: E402

T = H.T
q = H.q
EI = H.load(H.ROOT / "frontier/B1509_the_join_on_the_projective_vacuum/verification/extension_index.py", "b1509_extension_index")
B1510_RUN = H.ROOT / "frontier/B1510_the_two_sided_deformation/verification/two_sided_run.txt"


# ============================================================================================ K1
def k1():
    out = {}
    mats = T.symbolic_mats()
    L_xy = T.word_matrix(mats, T.fibre_word_in_mn(H.ELL)).applyfunc(sp.cancel)
    L = T.word_matrix(mats, T.WORD_L).applyfunc(sp.cancel)
    out["ELL is the longitude (rho_q(ELL) = rho_q(nMNmmNMn), symbolic)"] = (L_xy - L).applyfunc(sp.cancel) == sp.zeros(4)
    out["phi fixes ELL as a word"] = T.apply(T.PHI, H.ELL) == H.ELL
    cpl = sp.factor(sp.Matrix(L).charpoly(H.s).as_expr())
    out["charpoly of rho_q(ELL)"] = str(cpl)
    out["longitude eigenvalues q, q, q, q^-3 (B1510 Lemmas C, R)"] = sp.simplify(cpl - (H.s - q) ** 3 * (H.s - q ** -3)) == 0
    out["PHI_INV inverts phi"] = all(T.apply(T.PHI, H.PHI_INV[g]) == g and T.apply(H.PHI_INV, T.PHI[g]) == g for g in "xy")
    levels = {}
    for n in range(1, 7):
        G = H.FibredGroup(n)
        t0 = time.time()
        C, z, ok = G.fundamental()
        levels[f"level_{n}"] = {**ok, "cells_in_C": len(C), "seconds": round(time.time() - t0, 2)}
    out["levels"] = levels
    # the prism identity on test chains of the fibre (level 2)
    G = H.FibredGroup(2)
    rnd = random.Random(1513)
    words = ["x", "y", "xY", "yXYx", "XXy", "yyx", "xyXY"]
    ok = True
    for _ in range(12):
        g, k = (T.red(rnd.choice(words)), 0), (T.red(rnd.choice(words)), 0)
        if g == G.ID or k == G.ID:
            continue
        for c in ({(g,): 1}, {(g, k): 1}):
            lhs = G.add(G.boundary(G.prism(c)), G.prism(G.boundary(c)) if len(next(iter(c))) > 1 else {})
            rhs = G.add(c, G.scale(G.push(c), -1))
            ok = ok and lhs == rhs
    out["prism: dh + hd = 1 - c_t on test chains"] = ok
    return out


# ============================================================================================ K2
def k2():
    out = {}
    Fq = T.Field("sym", gaussian=False)
    for n in range(1, 5):
        G = H.FibredGroup(n)
        out[f"rho_q satisfies G_{n}'s relators (over Q(q))"] = H.Module(G, H.rho_mats(G, Fq)).check()
    # B1511's banked triplet rows on G_3, exactly
    G = H.FibredGroup(3)
    K = T.Field("ext", g=H.G0, gaussian=False)
    rho = H.rho_mats(G, K)
    rows = {}
    t0 = time.time()
    for ab in H.TRIPLET:
        V = H.Module(G, H.member_mats(G, K, ab, -1, rho))
        assert V.check()
        basis, h1 = H.h1_basis(V)
        _, h1d = H.h1_basis(V.dual())
        W = V.extension(basis[0].column())
        assert W.check()
        d = H.index(W)
        rows[str(ab)] = {"h1(V)": h1, "h1(V*)": h1d, "W (a0,a1,t0,r1)": [d["a0"], d["a1"], d["t0"], d["r1"]],
                         "W* (b0,b1,s0,q1)": [d["b0"], d["b1"], d["s0"], d["q1"]], "I(W)": d["I"]}
    out["B1511 banked triplet rows on G_3 (exact)"] = rows
    out["B1511 banked triplet rows reproduced"] = all(r == {"h1(V)": 1, "h1(V*)": 1, "W (a0,a1,t0,r1)": [0, 1, 1, 1],
                                                            "W* (b0,b1,s0,q1)": [1, 2, 1, 1], "I(W)": -1} for r in rows.values())
    out["K2 triplet seconds"] = round(time.time() - t0, 1)
    return out


# ============================================================================================ K3
def k3():
    out = {}
    K1 = T.Field("ext", g=q - 1, gaussian=False)
    for n in (1, 3):
        G = H.FibredGroup(n)
        rho = H.Module(G, H.rho_mats(G, K1))
        L2 = rho.wedge2()
        assert L2.check()
        out[f"h1(G_{n}; Lambda^2 rho_1)"] = H.h1_basis(L2)[1]
    cov = T.rs_cover(3)
    rs = T.DMRep(cov["gens"], T.rs_rho(cov, K1))
    out["h1(RS_3; Lambda^2 rho_1)"] = T.h1_classes(T.wedge2_rep(rs), cov["rels"])[1]
    out["Shapiro at q = 1 holds (2, 2, 2)"] = (out["h1(G_1; Lambda^2 rho_1)"], out["h1(G_3; Lambda^2 rho_1)"],
                                                out["h1(RS_3; Lambda^2 rho_1)"]) == (2, 2, 2)
    return out


# ============================================================================================ K4-K6: B1510's banked identity
def mn_cocycle_value(A, vals, w):
    """a cocycle of the (m, n) presentation (values vals on m, n; A an EI.ERep) evaluated on a word in m, n"""
    d = A.d
    v = DomainMatrix.zeros((d, 1), EI.K)
    pre = DomainMatrix.eye(d, EI.K)
    for ch in w:
        if ch.islower():
            v = v + pre * vals[ch]
            pre = pre * A.M[ch]
        else:
            pre = pre * A.M[ch]
            v = v - pre * vals[ch.lower()]
    return v


def b1510_setup(qq, mu, n=1):
    """V = mu rho_q on G_n, B1509's cocycles c (of V) and c* (of V*) pulled back, the fibration class e_n"""
    m, nn = EI.ballas(qq)
    A = EI.ERep({"m": EI.dm(mu * m), "n": EI.dm(mu * nn)})
    Ad = A.dual()
    c, cs = EI.generator_cocycle(A), EI.generator_cocycle(Ad)
    G = H.FibredGroup(n)
    words = {"x": "nM", "y": "mnMM", "t": "m" * n}
    V = H.Module(G, {g: A.word(w) for g, w in words.items()})
    Vd = H.Module(G, {g: Ad.word(w) for g, w in words.items()})
    assert V.check() and Vd.check()
    cc = H.Cocycle(V, {g: mn_cocycle_value(A, c, w) for g, w in words.items()})
    ccs = H.Cocycle(Vd, {g: mn_cocycle_value(Ad, cs, w) for g, w in words.items()})
    assert cc.is_cocycle() and ccs.is_cocycle()
    e = H.fibration_class(G, EI.K)
    return G, V, Vd, cc, ccs, e


def banked_kappas():
    rows = json.loads(B1510_RUN.read_text(encoding="utf-8"))["exact_order2"]
    out = []
    for (label, qq, mu, ml), r in zip(EI.POINTS, rows):
        assert r["point"].startswith(label) and r["mu"] == ml
        out.append((label, qq, mu, ml, EI.K.from_sympy(sp.sympify(r["kappa_l_hat"]))))
    return out


def k4_k6():
    TL = H.form_line_pairing()
    out = {"K4": [], "K5": {}, "K6": []}
    signs = set()
    for label, qq, mu, ml, kap in banked_kappas():
        G, V, Vd, c, cs, e = b1510_setup(qq, mu)
        C, z, _ = G.fundamental()
        Y = H.triple(G, C, z, c, e, cs, TL)
        row = {"point": f"{label}, mu = {ml}", "Y(c, e, c*)": str(EI.K.to_sympy(Y)), "banked kappa_l_hat": str(EI.K.to_sympy(kap))}
        if kap == EI.K.zero:
            row["agrees"] = Y == EI.K.zero
        else:
            sg = +1 if Y == kap else (-1 if Y == -kap else None)
            row["agrees"] = sg is not None
            signs.add(sg)
        out["K4"].append(row)
    out["K4 all agree, one global sign"] = all(r["agrees"] for r in out["K4"]) and len(signs) == 1 and None not in signs
    out["K4 global sign"] = signs.pop() if len(signs) == 1 else None
    # K5 at (7 - 4 sqrt 3, i)
    label, qq, mu, ml, kap = banked_kappas()[2]
    G, V, Vd, c, cs, e = b1510_setup(qq, mu)
    C, z, _ = G.fundamental()
    Y0 = H.triple(G, C, z, c, e, cs, TL)
    rnd = random.Random(7)
    u4 = DomainMatrix([[EI.K.convert(rnd.randint(-5, 5))] for _ in range(4)], (4, 1), EI.K)
    u1 = DomainMatrix([[EI.K.convert(3)]], (1, 1), EI.K)
    out["K5"]["coboundary in slot 1"] = H.triple(G, C, z, c.plus_coboundary(u4), e, cs, TL) == Y0
    out["K5"]["coboundary in slot 2 (trivial module: zero)"] = H.triple(G, C, z, c, e.plus_coboundary(u1), cs, TL) == Y0
    out["K5"]["coboundary in slot 3"] = H.triple(G, C, z, c, e, cs.plus_coboundary(u4), TL) == Y0
    out["K5"]["cyclic: Y(c*, c, e) = Y(c, e, c*)"] = H.triple(G, C, z, cs, c, e, H.form_permuted(TL, (1, 2, 0))) == Y0
    out["K5"]["transposition: Y(c, c*, e) = -Y(c, e, c*)"] = H.triple(G, C, z, c, cs, e, H.form_permuted(TL, (0, 2, 1))) == -Y0
    out["K5"]["Y nonzero here"] = Y0 != EI.K.zero
    # K6: levels 2 and 3, all six points
    for label, qq, mu, ml, kap in banked_kappas():
        G1, V1, Vd1, c1, cs1, e1 = b1510_setup(qq, mu, 1)
        C1, z1, _ = G1.fundamental()
        Y1 = H.triple(G1, C1, z1, c1, e1, cs1, TL)
        row = {"point": f"{label}, mu = {ml}"}
        for n in (2, 3):
            G, V, Vd, c, cs, e = b1510_setup(qq, mu, n)
            Cn, zn, _ = G.fundamental()
            row[f"level {n} equals level 1"] = H.triple(G, Cn, zn, c, e, cs, TL) == Y1
        out["K6"].append(row)
    out["K6 all equal"] = all(all(v for k, v in r.items() if k.startswith("level")) for r in out["K6"])
    return out


# ============================================================================================ K7
def k7():
    F = H.form_wedge(5)
    rnd = random.Random(5)
    ok = True
    for _ in range(4):
        while True:
            g = sp.Matrix(5, 5, lambda i, j: rnd.randint(-3, 3))
            if g.det() != 0:
                break
        D = lambda M: DomainMatrix.from_Matrix(M).convert_to(sp.QQ)
        gi = g.inv()
        om = D(sp.Matrix(10, 1, lambda i, j: rnd.randint(-4, 4)))
        f = D(sp.Matrix(5, 1, lambda i, j: rnd.randint(-4, 4)))
        f2 = D(sp.Matrix(5, 1, lambda i, j: rnd.randint(-4, 4)))
        L2 = D(H.wedge2_sym(g))
        gs = D(gi.T)
        ok = ok and F(L2 * om, gs * f, gs * f2) == F(om, f, f2)
        ok = ok and F(om, f, f2) == -F(om, f2, f)
    return {"wedge form GL(5)-invariant and antisymmetric in (f, f')": ok}


# ============================================================================================ K8
def ker_dims_on_H1(S, B, lam, dom, maxpow=2):
    n = S.shape[0]
    N = S - DomainMatrix.eye(n, dom) * lam
    out, P = [], DomainMatrix.eye(n, dom)
    for _ in range(maxpow):
        P = P * N
        out.append(n - T.dm_rank(P.hstack(B)))
    return out


def k8():
    out = {}
    m1, n1 = T.ballas(1)
    E = {"m": H.wedge2_sym(m1), "n": H.wedge2_sym(n1)}
    S, B = H.fibre_monodromy(E)
    dS = DomainMatrix.from_Matrix(S).convert_to(sp.QQ)
    dB = DomainMatrix.from_Matrix(B).convert_to(sp.QQ)
    out["H^0(F; Lambda^2 rho_1) = 0 (rank B = 6)"] = T.dm_rank(dB) == 6
    out["dim ker(S - 1) on H^1(F; Lambda^2 rho_1)"] = ker_dims_on_H1(dS, dB, sp.QQ.one, sp.QQ, 1)[0]
    rows = []
    for label, qq, mu, ml in EI.POINTS:
        m, nn = EI.ballas(qq)
        Sx, Bx = H.fibre_monodromy({"m": m, "n": nn})
        dS = DomainMatrix.from_Matrix(Sx.applyfunc(sp.nsimplify)).convert_to(EI.K)
        dB = DomainMatrix.from_Matrix(Bx.applyfunc(sp.nsimplify)).convert_to(EI.K)
        rows.append({"point": f"{label}, mu = {ml}", "ker (S - mu)^j, j = 1, 2": ker_dims_on_H1(dS, dB, EI.K.from_sympy(sp.sympify(mu)), EI.K)})
    out["rho_q at B1509's points"] = rows
    out["banked Jordan pattern reproduced"] = all(r["ker (S - mu)^j, j = 1, 2"] == ([1, 2] if r["point"].endswith("-1") else [1, 1])
                                                  for r in rows)
    return out


# ============================================================================================ K9, K10
def k9():
    out = {}
    for label, qq, mu, ml, expect in [("17-12sqrt2", 17 - 12 * sp.sqrt(2), -1, "-1", 1), ("7-4sqrt3", 7 - 4 * sp.sqrt(3), sp.I, "i", 0)]:
        G, V, Vd, c, cs, e = b1510_setup(qq, mu)
        dom = EI.K
        W = V.extension(c.column())
        Wd, L2W = W.dual(), W.wedge2()
        L2Wd = Wd.wedge2()
        row = {"W, W*, L2 W, L2 W* satisfy the relators": all(M.check() for M in (W, Wd, L2W, L2Wd))}
        ints = H.interior_classes(Wd)
        row["interior classes of H1(W*)"] = len(ints)
        row["matches B1509's b1 - q1"] = len(ints) == expect
        ok = True
        I5 = DomainMatrix.eye(5, dom)
        for a, ea in ints:
            ok = ok and a.is_cocycle() and a("t") == (Wd.rho("t") - I5) * ea and a(H.ELL) == (Wd.rho(H.ELL) - I5) * ea
        row["relative lifts valid"] = ok
        rnd = random.Random(9)
        om = DomainMatrix([[dom.convert(rnd.randint(-5, 5))] for _ in range(10)], (10, 1), dom)
        zero10 = DomainMatrix.zeros((10, 1), dom)
        dom_ = H.Cocycle(L2W, {g: zero10 for g in G.gens}).plus_coboundary(om)
        proj = H.quotient_to_V(L2W, dom_, 5)
        P = H.pairs(5)
        qom = DomainMatrix([[om[P.index((i, 4)), 0].element] for i in range(4)], (4, 1), dom)
        I4 = DomainMatrix.eye(4, dom)
        row["projection commutes with coboundaries"] = all(proj[g] == (V.rep.M[g] - I4) * qom for g in G.gens)
        f = DomainMatrix([[dom.convert(rnd.randint(-5, 5))] for _ in range(4)], (4, 1), dom)
        zero4 = DomainMatrix.zeros((4, 1), dom)
        df = H.Cocycle(Vd, {g: zero4 for g in G.gens}).plus_coboundary(f)
        inc = H.include_Vstar(L2Wd, df, 5)
        fw = DomainMatrix([[dom.zero]] * 10, (10, 1), dom)
        fl = fw.to_list()
        for i in range(4):
            fl[P.index((i, 4))][0] = f[i, 0].element
        fw = DomainMatrix(fl, (10, 1), dom)
        I10 = DomainMatrix.eye(10, dom)
        row["inclusion commutes with coboundaries"] = all(inc.v[g] == (L2Wd.rep.M[g] - I10) * fw for g in G.gens)
        row["c* includes to a cocycle of L2 W*"] = H.include_Vstar(L2Wd, cs, 5).is_cocycle()
        if ints:
            C, z, _ = G.fundamental()
            a, ea = ints[0]
            u = DomainMatrix([[dom.convert(rnd.randint(-5, 5))] for _ in range(10)], (10, 1), dom)
            hcob = H.Cocycle(L2W, {g: zero10 for g in G.gens}).plus_coboundary(u)
            row["relative coboundary first: Y = 0"] = H.triple(G, C, z, hcob, a, a, H.form_wedge(5), e=u) == dom.zero
        out[f"{label}, mu = {ml}"] = row
    out["K9 all"] = all(all(v for k, v in r.items() if k != "interior classes of H1(W*)") for r in out.values())
    return out


def k10():
    m, n = T.ballas(q)
    res = H.fibre_polynomial({"m": m, "n": n})
    P = res["P"]
    Qm = T.Q_MONIC
    return {"P_rho(q, s)": str(sp.factor(P)), "equals B1509's monic Q": sp.simplify(sp.expand(P - Qm)) == 0,
            "or Q with s -> 1/s": sp.simplify(sp.expand(s_ ** 4 * Qm.subs(s_, 1 / s_) - P)) == 0,
            "interpolation points": res["points"], "H^0(F; rho_q) = 0 at q = 7/3 (rank B = 4)": res["rank_B_at_q=7/3"] == 4}


s_ = H.s


def main():
    res = {}
    for name, fn in [("K1", k1), ("K2", k2), ("K3", k3), ("K4-K6", k4_k6), ("K7", k7), ("K8", k8), ("K9", k9), ("K10", k10)]:
        t0 = time.time()
        res[name] = fn()
        res[name + " seconds"] = round(time.time() - t0, 1)
        print(name, "done", res[name + " seconds"], "s", flush=True)
    return res


if __name__ == "__main__":
    res = main()
    txt = json.dumps(res, indent=1, sort_keys=True, default=str)
    print(txt[:8000])
    if "--record" in sys.argv:
        (HERE / "controls_run.txt").write_text(txt + "\n", encoding="utf-8")
