"""B1513 sealed run (PREREGISTRATION.md section 7).  Not to be run before the seal.

0  The banked identity first: B1510's exact kappa_l_hat at its six points through this arc's `triple` (controls K4). The run stops if
   it fails.
A  The Higgs sector's fibre polynomial on the whole family: P_L(q, s) = det(s - S) on H^1(F; Lambda^2 rho_q), degree 6 in s, over Q(q).
   It is computed from exact charpolys at integer points (flint) and interpolation, and verified at fresh points. Read at every root of
   unity of order <= 6 (the levels M_1..M_6): identically zero or not; the exceptional polynomial in q; its gcd with each population's
   polynomial. Also the identities D7.
B  Exact counts at each population, over Q[q]/(g) (all conjugate points at once):
   I   the triplet: s961 = G_3, g = q^6 - 34 q^3 + 1, the three members nu_k = (0,2), (2,2), (2,0) with lam3 = -1;
   II  B1509's join: m004 = G_1, g = q^2 - 34 q + 1, the twist mu = -1 (one member).
   For each population:
   - h^1(Lambda^2 rho_q) on the level (and, for I, on G_1 and on B1511's Reidemeister-Schreier presentation of M_3), with the boundary
     data, and H^0 of the fibre;
   - for every member k: h^1(Lambda^2 W_k), h^1(Lambda^2 W_k*) and their (a0, a1, t0, t1, r1);
   - the own 5'_H test: the rank of H^1(Lambda^2 W_k) -> H^1(V_k);
   - the own 5bar'_H test: c_k* is nonzero in H^1(Lambda^2 W_k*);
   - the interior 10' classes of H^1(W_k*).
C  The couplings, exactly: Y_k = Y(h, a_k, a_k) for every basis class h of H^1(Lambda^2 W_k), through the form (f ^ g)(omega), with a_k
   the interior 10'. The instrument's checks at each population:
   - Y(a, a, h) = Y and Y(a, h, a) = -Y;
   - coboundaries added in each slot;
   - lift independence: a_k + e f_0 gives the same Y (Lemma 6);
   - the cross term <c_k u e u c_k*> = 0 (Lemma 6's input).
D  Over GF(p), at three primes and every root of each population's polynomial: B's dimensions and C's non-vanishing.
E  Invariant forms on Lambda^2 W_k (x) W_i* (x) W_j* for all 27 (i, j, k) of the triplet, over GF(p) (an upper bound for the exact
   dimension; P5).
Record: higgs_census_run.txt (JSON), with the log in higgs_census_log.txt."""
import json
import sys
import time
from pathlib import Path

import flint
import sympy as sp
from sympy.polys.matrices import DomainMatrix

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import controls as K  # noqa: E402
import higgs_lib as H  # noqa: E402

T = H.T
q, s = H.q, H.s
CYCLO = {1: s - 1, 2: s + 1, 3: s ** 2 + s + 1, 4: s ** 2 + 1, 5: s ** 4 + s ** 3 + s ** 2 + s + 1, 6: s ** 2 - s + 1}
G_JOIN = q ** 2 - 34 * q + 1
POPULATIONS = {
    "I (the triplet, s961)": {"level": 3, "g": H.G0, "members": [(ab, -1) for ab in H.TRIPLET]},
    "II (B1509's join, m004)": {"level": 1, "g": G_JOIN, "members": [((0, 0), -1)]},
}


# ============================================================================================ 0
def banked_identity():
    TL = H.form_line_pairing()
    rows, signs = [], set()
    for label, qq, mu, ml, kap in K.banked_kappas():
        G, V, Vd, c, cs, e = K.b1510_setup(qq, mu)
        C, z, _ = G.fundamental()
        Y = H.triple(G, C, z, c, e, cs, TL)
        ok = (Y == K.EI.K.zero) if kap == K.EI.K.zero else (Y == kap or Y == -kap)
        if kap != K.EI.K.zero:
            signs.add(1 if Y == kap else -1)
        rows.append({"point": f"{label}, mu = {ml}", "Y": str(K.EI.K.to_sympy(Y)), "kappa": str(K.EI.K.to_sympy(kap)), "ok": ok})
    return {"rows": rows, "passed": all(r["ok"] for r in rows) and len(signs) == 1}


# ============================================================================================ A
def resultant_in_q(P, phi):
    if sp.Poly(phi, s).degree() == 1:
        R = P.subs(s, sp.solve(phi, s)[0])
    else:
        R = sp.resultant(P, phi, s)
    return sp.numer(sp.together(sp.cancel(R)))


def part_a(log):
    m, n = T.ballas(q)
    E = {"m": H.wedge2_sym(m).applyfunc(sp.cancel), "n": H.wedge2_sym(n).applyfunc(sp.cancel)}
    t0 = time.time()
    res = H.fibre_polynomial(E)
    P = res["P"]
    log(f"A: P_L(q, s) computed, degree {res['deg_s']} in s, {time.time() - t0:.1f}s")
    out = {"P_L(q,s) factored": str(sp.factor(P)), "degree in s": res["deg_s"], "B^1 part": str(sp.factor(res["Pb"])),
           "H^0(F) = 0 (rank of the coboundary matrix at q = 7/3)": res["rank_B_at_q=7/3"],
           "interpolation points": res["points"], "Laurent range of S": list(res["laurent_range_S"])}
    P0 = sp.factor(P.subs(s, 0))
    out["P_L(q, 0)"] = str(P0)
    out["D7a: P_L(1/q, s) = P_L(q, s)"] = sp.simplify(P.subs(q, 1 / q) - P) == 0
    out["D7b: s^6 P_L(q, 1/s) = P_L(q, 0) P_L(q, s)"] = sp.simplify(sp.expand(s ** 6 * P.subs(s, 1 / s)) - P0 * P) == 0
    loci = {}
    for k, phi in CYCLO.items():
        num = resultant_in_q(P, phi)
        row = {"identically zero": sp.expand(num) == 0}
        if not row["identically zero"]:
            facs = []
            for f, mlt in sp.factor_list(sp.expand(num))[1]:
                if sp.Poly(f, q).degree() == 0:
                    continue
                roots = [r for r in sp.real_roots(sp.Poly(f, q)) if r > 0 and r != 1]
                facs.append({"factor": str(f), "mult": mlt, "degree": sp.Poly(f, q).degree(),
                             "positive_roots_not_1": [str(sp.N(r, 12)) for r in roots]})
            row["factors"] = facs
            for name, pop in POPULATIONS.items():
                row[f"gcd with {pop['g']}"] = str(sp.gcd(sp.Poly(num, q), sp.Poly(pop["g"], q)).as_expr())
        loci[f"order {k}"] = row
        log(f"A: locus at order-{k} roots of unity: {json.dumps(row)[:400]}")
    out["loci"] = loci
    gI, gII = f"gcd with {H.G0}", f"gcd with {G_JOIN}"
    out["P1: generic h1 = 0 at every root of unity of order <= 6"] = all(not r["identically zero"] for r in loci.values())
    out["P2: triplet (orders 1, 3) on no locus"] = all(loci[f"order {k}"].get(gI) == "1" for k in (1, 3))
    out["P2': triplet on M_6 (orders 1, 2, 3, 6) on no locus"] = all(loci[f"order {k}"].get(gI) == "1" for k in (1, 2, 3, 6))
    out["P2: join (order 1) on no locus"] = loci["order 1"].get(gII) == "1"
    return out


# ============================================================================================ B and C
def field_show(field, x):
    if field.kind == "gf":
        return int(x) % field.p
    return str(field.dom.to_sympy(x))


def fibre_h0_rank(G, field):
    """the rank of the fibre's coboundary matrix for Lambda^2 rho_q (6 means H^0(F) = 0)"""
    L2 = H.Module(G, H.rho_mats(G, field)).wedge2()
    I6 = DomainMatrix.eye(6, field.dom)
    return T.dm_rank((L2.rep.M["x"] - I6).vstack(L2.rep.M["y"] - I6))


def member_rows(G, field, members, C, z, tag, log, with_checks=True):
    rho = H.rho_mats(G, field)
    out = {}
    dom = field.dom
    F = H.form_wedge(5)
    for ab, lam in members:
        t0 = time.time()
        row = {}
        V = H.Module(G, H.member_mats(G, field, ab, lam, rho))
        Vd = V.dual()
        cb, h1V = H.h1_basis(V)
        cbd, h1Vd = H.h1_basis(Vd)
        row["h1(V), h1(V*)"] = [h1V, h1Vd]
        c, cs = cb[0], cbd[0]
        W = V.extension(c.column())
        Wd, L2W = W.dual(), W.wedge2()
        L2Wd = Wd.wedge2()
        assert W.check() and L2W.check() and L2Wd.check()
        hb, h1L = H.h1_basis(L2W)
        hbd, h1Ld = H.h1_basis(L2Wd)
        row["h1(L2 W)"], row["h1(L2 W*)"] = h1L, h1Ld
        row["L2 W (a0,a1,t0,t1,r1)"] = list(H.cohomology_data(L2W))
        row["L2 W* (a0,a1,t0,t1,r1)"] = list(H.cohomology_data(L2Wd))
        imgs = [H.Cocycle(V, H.quotient_to_V(L2W, h, 5)) for h in hb]
        assert all(x.is_cocycle() for x in imgs)
        row["rank of H1(L2 W) -> H1(V)"] = H.rank_mod_coboundaries(V, imgs)
        inc = H.include_Vstar(L2Wd, cs, 5)
        assert inc.is_cocycle()
        row["c* nonzero in H1(L2 W*)"] = H.rank_mod_coboundaries(L2Wd, [inc]) == 1
        ints = H.interior_classes(Wd)
        row["interior classes of H1(W*)"] = len(ints)
        ys = []
        if ints:
            a, ea = ints[0]
            for j, h in enumerate(hb):
                Y = H.triple(G, C, z, h, a, a, F)
                ys.append({"class": j, "maps onto c": H.rank_mod_coboundaries(V, [imgs[j]]) == 1, "Y": field_show(field, Y),
                           "Y nonzero": Y != dom.zero})
            own = [h for h, x in zip(hb, imgs) if H.rank_mod_coboundaries(V, [x]) == 1]
            if with_checks and own:
                h = own[0]
                Y0 = H.triple(G, C, z, h, a, a, F)
                chk = {"Y(a, a, h) = Y": H.triple(G, C, z, a, a, h, H.form_permuted(F, (2, 0, 1)), e=ea) == Y0,
                       "Y(a, h, a) = -Y": H.triple(G, C, z, a, h, a, H.form_permuted(F, (1, 0, 2)), e=ea) == -Y0}
                u10 = DomainMatrix([[dom.convert(k + 1)] for k in range(10)], (10, 1), dom)
                u5 = DomainMatrix([[dom.convert(2 * k - 3)] for k in range(5)], (5, 1), dom)
                chk["coboundary in h"] = H.triple(G, C, z, h.plus_coboundary(u10), a, a, F) == Y0
                chk["coboundary in a (both slots)"] = H.triple(G, C, z, h, a.plus_coboundary(u5), a.plus_coboundary(u5), F) == Y0
                f0 = DomainMatrix([[dom.zero]] * 4 + [[dom.one]], (5, 1), dom)
                zero5 = DomainMatrix.zeros((5, 1), dom)
                ef0 = H.Cocycle(Wd, {"x": zero5, "y": zero5, "t": f0})
                assert ef0.is_cocycle()
                a2 = H.Cocycle(Wd, {g: a.v[g] + ef0.v[g] for g in G.gens})
                chk["lift independence: Y(h, a + e f0, a + e f0) = Y"] = H.triple(G, C, z, h, a2, a2, F) == Y0
                X = H.triple(G, C, z, c, H.fibration_class(G, dom), cs, H.form_line_pairing())
                chk["cross term <c u e u c*>"] = field_show(field, X)
                chk["cross term zero (Lemma 6 input)"] = X == dom.zero
                row["checks"] = chk
        row["couplings"] = ys
        row["seconds"] = round(time.time() - t0, 1)
        out[str(ab)] = row
        log(f"{tag} member {ab}: {json.dumps(row, default=str)[:700]}")
    return out


def part_b_c_exact(log):
    out = {}
    for name, pop in POPULATIONS.items():
        field = T.Field("ext", g=pop["g"], gaussian=False)
        n = pop["level"]
        G = H.FibredGroup(n)
        row = {"fibre: rank of the coboundary matrix (6 = no H^0(F))": fibre_h0_rank(G, field)}
        for lv in sorted({1, n}):
            Gl = H.FibredGroup(lv)
            L2 = H.Module(Gl, H.rho_mats(Gl, field)).wedge2()
            assert L2.check()
            row[f"h1(G_{lv}; L2 rho_q)"] = H.h1_basis(L2)[1]
            row[f"G_{lv} L2 rho_q (a0,a1,t0,t1,r1)"] = list(H.cohomology_data(L2))
        if n == 3:
            cov = T.rs_cover(3)
            rs = T.DMRep(cov["gens"], T.rs_rho(cov, field))
            row["h1(RS_3; L2 rho_q)"] = T.h1_classes(T.wedge2_rep(rs), cov["rels"])[1]
        log(f"B exact {name}: {row}")
        C, z, _ = G.fundamental()
        row["members"] = member_rows(G, field, pop["members"], C, z, f"B/C exact {name}", log)
        out[name] = row
    return out


def primes_with_roots(g, count=3, start=1009):
    out, p = [], start
    while len(out) < count:
        p = int(sp.nextprime(p))
        roots = T.gf_roots(g, p)
        if roots:
            out.append((p, roots))
    return out


def part_d(log):
    out = {}
    for name, pop in POPULATIONS.items():
        n = pop["level"]
        G = H.FibredGroup(n)
        C, z, _ = G.fundamental()
        rows = []
        for p, roots in primes_with_roots(pop["g"]):
            for r in roots:
                Fp = T.Field("gf", p=p, r=r, gaussian=False)
                row = {"p": p, "q mod p": r}
                for lv in sorted({1, n}):
                    Gl = H.FibredGroup(lv)
                    row[f"h1(G_{lv}; L2 rho_q)"] = H.h1_basis(H.Module(Gl, H.rho_mats(Gl, Fp)).wedge2())[1]
                row["members"] = member_rows(G, Fp, pop["members"], C, z, f"D {name} p={p} r={r}", log, with_checks=False)
                rows.append(row)
        out[name] = rows
    return out


# ============================================================================================ E: invariant forms (P5)
def nmod_of(M, p):
    return flint.nmod_mat(M.shape[0], M.shape[1], [int(M[i, j].element) % p for i in range(M.shape[0]) for j in range(M.shape[1])], p)


def kron(A, B, p):
    a, b = A.nrows(), B.nrows()
    return flint.nmod_mat(a * b, a * b, [int(A[i1, j1]) * int(B[i2, j2]) % p for i1 in range(a) for i2 in range(b)
                                         for j1 in range(a) for j2 in range(b)], p)


def invariant_forms(log):
    """the dimension of invariant trilinear forms on Lambda^2 W_k (x) W_i* (x) W_j* over GF(p). Forms transform by the inverse
    transposes of the three factors, that is by Lambda^2 W_k^-T (x) W_i (x) W_j."""
    p, roots = primes_with_roots(H.G0, 1)[0]
    r = roots[0]
    Fp = T.Field("gf", p=p, r=r, gaussian=False)
    G = H.FibredGroup(3)
    rho = H.rho_mats(G, Fp)
    Ws = []
    for ab in H.TRIPLET:
        V = H.Module(G, H.member_mats(G, Fp, ab, -1, rho))
        Ws.append(V.extension(H.h1_basis(V)[0][0].column()))
    out = {}
    for k, Wk in enumerate(Ws):
        L2 = Wk.wedge2()
        for i, Wi in enumerate(Ws):
            for j, Wj in enumerate(Ws):
                blocks = []
                for g in G.gens:
                    A = nmod_of(T.dm_inv(L2.rep.M[g]).transpose(), p)
                    Kr = kron(kron(A, nmod_of(Wi.rep.M[g], p), p), nmod_of(Wj.rep.M[g], p), p)
                    nn = Kr.nrows()
                    blocks.append([[(int(Kr[a, b]) - (1 if a == b else 0)) % p for b in range(nn)] for a in range(nn)])
                nn = len(blocks[0])
                stacked = flint.nmod_mat(3 * nn, nn, [x for B in blocks for row in B for x in row], p)
                out[f"(k={k}, i={i}, j={j})"] = nn - stacked.rank()
        log(f"E: Higgs member {k} done")
    out["p"], out["q mod p"] = p, r
    vals = {key: v for key, v in out.items() if key.startswith("(k=")}
    out["P5: one form iff i = j = k"] = all(v == (1 if key[3] == key[8] == key[13] else 0) for key, v in vals.items())
    return out


def main():
    logs = []
    logf = open(HERE / "higgs_census_log.txt", "w", encoding="utf-8") if "--record" in sys.argv else None

    def log(msg):
        line = f"[{time.strftime('%H:%M:%S')}] {msg}"
        logs.append(line)
        print(line, flush=True)
        if logf:
            logf.write(line + "\n")
            logf.flush()
    rec = {}
    t0 = time.time()
    rec["0_banked_identity"] = banked_identity()
    log(f"0: banked identity passed = {rec['0_banked_identity']['passed']}")
    assert rec["0_banked_identity"]["passed"], "the banked identity failed: stop"
    rec["A"] = part_a(log)
    rec["B_C_exact"] = part_b_c_exact(log)
    rec["D_modp"] = part_d(log)
    rec["E_invariant_forms"] = invariant_forms(log)
    rec["seconds"] = round(time.time() - t0, 1)
    if logf:
        logf.close()
    return rec


if __name__ == "__main__":
    rec = main()
    txt = json.dumps(rec, indent=1, sort_keys=True, default=str)
    print(txt[:6000])
    if "--record" in sys.argv:
        (HERE / "higgs_census_run.txt").write_text(txt + "\n", encoding="utf-8")
