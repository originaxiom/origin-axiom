#!/usr/bin/env python3
"""Repair, after the sealed run: at some kappa = -2 points kappa has a critical point along the curve, so kappa = -2 is
a double root there and the sealed instrument's Newton leaves the point about 1e-15 off (residual 1e-30).  The
torsions are then good to about fourteen digits, but the ranks behind the class index are not resolved at the
sealed tolerance (singular values near 1e-21 are kept as non-zero).  Here every coupling of a level is recomputed at
110 digits, the points polished by a Newton iteration whose step is doubled along the degenerate direction.

usage: refine_degenerate.py <index of the level's record in run/>"""
import sys, json, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from mpmath import mp, mpf, mpc, nstr, exp, pi, matrix, zeros, svd_c
import complete_points as cp
ce, mt, ix = cp.ce, cp.mt, cp.ix
DPS = 110
def polish(B, p):
    h = mpf(10) ** (-(DPS // 2)); p = [mpc(c) for c in p]; info = dict(degenerate=False)
    def F(p):
        q = ce.tracemap(B.Phi, p); return [q[i] - B.sig[i] * p[i] for i in range(3)] + [ce.kappa(p) + 2]
    p0 = list(p)
    for it in range(200):
        f0 = F(p); J = zeros(4, 3)
        for j in range(3):
            pp = list(p); pp[j] += h; f1 = F(pp)
            for i in range(4): J[i, j] = (f1[i] - f0[i]) / h
        U, S, Vh = svd_c(J); c = U.H * matrix(f0); step = [mpc(0)] * 3
        order = sorted(range(3), key=lambda i: -abs(S[i])); small = order[-1]
        deg = abs(S[small]) < mpf("1e-4") * abs(S[order[0]]); info["degenerate"] = info["degenerate"] or bool(deg)
        for i in range(3):
            m = 2 if (deg and i == small) else 1
            for j in range(3): step[j] -= m * (c[i] / S[i]) * Vh[i, j].conjugate()
        p = [p[j] + step[j] for j in range(3)]
        if max(abs(s) for s in step) < mpf(10) ** (-48): break
    res = max(abs(c) for c in F(p)); assert res < mpf(10) ** (-66), ("polish failed", nstr(res, 3))      # a double root: the point is then within 1e-33
    info.update(iterations=it + 1, residual=nstr(res, 3), moved=nstr(max(abs(p[i] - p0[i]) for i in range(3)), 3))
    return p, info
def main(i):
    mp.dps = DPS
    f = sorted((HERE / "run").glob("complete_*.json"))[i]; d = json.load(open(f)); name, k = d["state"], d["k"]
    L = mt.Level(name, k); P = cp.Points(L); z = exp(2j * pi / L.N); pts = {}
    def point(ell):
        if ell not in pts:
            raw = P.cusp(ell); assert raw[0] is not None and raw[4]["kind"] == "parabolic", (ell, raw[4])
            B = raw[0]; p, info = polish(B, raw[1]); g = ce.rep(p); T = ce.intertwiner(B.Phi, g, B.sig)
            assert abs(abs(ce.tr(T)) - 2) < mpf(10) ** (-40), "the polished point is parabolic"
            pts[ell] = (B, p, g, T, info); print("   point %s: %s" % (ell, info), flush=True)
        return pts[ell]
    out = dict(state=name, k=k, digits=DPS, couplings=[], points={})
    for c in d["couplings"]:
        if not (c.get("higgs_point") == "parabolic" and c.get("extension_point") == "parabolic"): continue
        l, eta, A1 = tuple(c["l"]), tuple(c["eta"]), tuple(c["A1"])
        Bl, p1, gl, Tl, i1 = point(l); Be, p2, ge, Te, i2 = point(eta)
        b1 = L.add(A1, L.neg(eta)); b2 = L.add(b1, L.neg(l))
        t1 = ce.sector_torsion(Be.Phi, ge, Te, Be.v[0] * z ** b1[0], Be.v[1] * z ** b1[1])[0]; t2 = ce.sector_torsion(Be.Phi, ge, Te, Be.v[0] * z ** b2[0], Be.v[1] * z ** b2[1])[0]
        ax = z ** A1[0] / (Bl.v[0] * Be.v[0]); ay = z ** A1[1] / (Bl.v[1] * Be.v[1])
        h = {1: ax * mt.kron(gl[1], ge[1]), 2: ay * mt.kron(gl[2], ge[2])}; T = mt.kron(Tl, Te)
        I, a, b = ix.index(L.Phi, h, T); t = mt.torsion_n(L.Phi, h, T)
        rec = dict(l=list(l), eta=list(eta), A1=list(A1), types=c["types"], doublets=[nstr(t1, 40), nstr(t2, 40)], sealed_h1=c["cusp_cusp"]["h1"], sealed_smallest_kept=c["cusp_cusp"]["smallest_kept"],
                   index=I, h1=[a["h1"], b["h1"]], interior=[a["interior"], b["interior"]], smallest_kept=nstr(a["gaps"][1][0], 5), largest_dropped=nstr(a["gaps"][1][1], 5),
                   degenerate=[i1["degenerate"], i2["degenerate"]], torsion_abs=nstr(abs(t), 10))
        out["couplings"].append(rec)
        print("   l=%s eta=%s %s: index %d, h1 %s (sealed %s), interior %s, kept %s dropped %s" % (l, eta, c["types"], I, rec["h1"], rec["sealed_h1"], rec["interior"], rec["smallest_kept"], rec["largest_dropped"]), flush=True)
    out["points"] = {str(k_): v[4] for k_, v in pts.items()}
    (HERE / "refine").mkdir(exist_ok=True); json.dump(out, open(HERE / "refine" / f.name.replace("complete", "refined"), "w"), indent=1)
if __name__ == "__main__":
    main(int(sys.argv[1]))
