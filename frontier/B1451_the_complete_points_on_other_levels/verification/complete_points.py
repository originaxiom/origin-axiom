#!/usr/bin/env python3
"""The complete-cusp points of the periodic curves on a level, and what the frame's sectors and couplings carry there.

  sectors   : for each generation-shaped background, the torsion of its six sectors at the kappa = -2 point of the
              extension character's curve (B1446 did this on the root's three-fold cover).
  couplings : for each coupling (l, eta, A1) of B1445's selection, with the extension at its reducible end and the
              Higgs character at its kappa = -2 point: the bidoublet is the sum of two doublets on the Higgs
              character's curve, (alpha, beta) = (A1, A1/eta) and (A1/l, A1/(l eta)), and its torsion is the product
              of theirs (checked against the rank-four computation); and, with both at their kappa = -2 points, the
              class index and the torsion of the rank-four module.

A kappa = -2 point is 'parabolic' when the meridian has trace +-2 there, 'elliptic' otherwise (then the cusp is not
complete and the point is reported but not counted).

usage: complete_points.py <state> <k> [cap on extension characters] [cap on couplings]
"""
import sys, json, itertools, collections, pathlib
HERE = pathlib.Path(__file__).resolve().parent
for d in ("B1444_the_backgrounds_are_ends_of_periodic_curves", "B1445_the_mass_term_on_the_product_of_two_curves", "B1446_the_parabolic_points_and_the_branch_points"):
    sys.path.insert(0, str(HERE.parents[1] / d / "verification"))
import curve_engine as ce
import mass_term as mt
import index_num as ix
from mpmath import mp, mpf, mpc, nstr, exp, pi, inverse
mp.dps = 60
SECT = mt.SECT
PATHS = [("+a", [mpc("0.05", 0), mpc("0.05", "0.9"), mpc(4, "0.9"), mpc(4, 0)]), ("+b", [mpc("0.02", 0), mpc("0.02", "2.5"), mpc(4, "2.5"), mpc(4, 0)]),
         ("+c", [mpc("0.01", 0), mpc("0.01", "6"), mpc(4, "6"), mpc(4, 0)]), ("+d", [mpc("-0.05", 0), mpc("-0.05", "1.3"), mpc(4, "1.3"), mpc(4, 0)])]

def walk(B, path, nsteps=60):
    cur = mpc(mpf("1e-6")) * mpc(path[0]) / abs(mpc(path[0])); p = ce.newton(B.Phi, B.p0, B.sig, cur)
    for target in path:
        target = mpc(target); step = (target - cur) / nsteps
        while abs(cur - target) > mpf(10) ** (-40):
            s = step if abs(target - cur) > abs(step) else target - cur
            while True:
                try: q = ce.newton(B.Phi, p, B.sig, cur + s); break
                except (AssertionError, ZeroDivisionError):
                    s = s / 4
                    if abs(s) < mpf(10) ** (-9): raise AssertionError("stalled at e = %s" % nstr(cur, 8))
            p = q; cur = cur + s
    return p

class Points:
    def __init__(self, L): self.L = L; self.cache = {}; self.z = exp(2j * pi / L.N)
    def end(self, ell):
        B = self.L.curve(ell).B; p = ce.newton(B.Phi, B.p0, B.sig, mpc(mpf("1e-14"))); g = ce.rep(p)
        return B, p, g, ce.intertwiner(B.Phi, g, B.sig)
    def cusp(self, ell):
        """(B, p, g, T, info) at a kappa = -2 point of the curve of ell, or (None, ..., info)"""
        if ell in self.cache: return self.cache[ell]
        L = self.L; out = (None, None, None, None, dict(reached=False)); B = None
        try:
            B = L.curve(ell).B; cands = []
            if L.order2(ell):
                p1 = ce.newton(B.Phi, B.p0, B.sig, mpc(mpf("1e-3"))); mov = max(range(3), key=lambda i: abs(p1[i] - B.p0[i]))
                p = [mpc(c) for c in B.p0]; p[mov] = mpc(0); cands.append(("line", p))
        except (AssertionError, ZeroDivisionError) as ex: out[4]["error"] = str(ex)[:80]; B = None
        if B is not None:
            for tag, path in ([] if L.order2(ell) else PATHS):
                try: cands.append((tag, walk(B, path))); break
                except (AssertionError, ZeroDivisionError): continue
            for tag, p in cands:
                q = ce.tracemap(B.Phi, p)
                if not all(abs(q[i] - B.sig[i] * p[i]) < mpf(10) ** (-30) for i in range(3)) or abs(ce.kappa(p) + 2) > mpf(10) ** (-30): continue
                try: g = ce.rep(p); T = ce.intertwiner(B.Phi, g, B.sig)
                except (AssertionError, ZeroDivisionError) as ex: out[4]["error"] = str(ex)[:80]; continue
                lam = g[1] * g[2] * inverse(g[1]) * inverse(g[2]); trT = ce.tr(T)
                kind = "parabolic" if abs(abs(trT) - 2) < mpf(10) ** (-25) else "elliptic"
                out = (B, p, g, T, dict(reached=True, path=tag, kind=kind, X=nstr(p[0], 30), Y=nstr(p[1], 30), Z=nstr(p[2], 30), tr_meridian=nstr(trT, 20), tr_longitude=nstr(ce.tr(lam), 20)))
                break
        self.cache[ell] = out; return out
    def sector(self, pt, beta):
        """torsion of the doublet with characters (eta beta, beta) on the curve, at the point"""
        B, p, g, T = pt[:4]; z = self.z
        return ce.sector_torsion(B.Phi, g, T, B.v[0] * z ** beta[0], B.v[1] * z ** beta[1])[0]

def backgrounds(L):
    N, S = L.N, L.S; triv = (0, 0); eq = lambda a, b: abs(a - b) < mpf(10) ** (-20); mul = lambda a, m: ((m * a[0]) % N, (m * a[1]) % N)
    def index(l, al):
        be = L.add(al, L.neg(l))
        if al == triv or be == triv: return 0
        return int(eq(S[al], S[l])) - int(eq(S[be], S[l]))
    bgs = {}
    for th, ps, W in itertools.product(L.chars, repeat=3):
        l = L.add(mul(th, 2), L.neg(W))
        if l == triv: continue
        al = [L.add(L.add(th, mul(ps, sy)), mul(W, (sg - 1) // 2)) for _, sy, sg in SECT]; I = [index(l, a) for a in al]
        if all(i == 1 for i in I[:5]) or all(i == -1 for i in I[:5]): bgs[(l,) + tuple(al)] = (I[0], I[5])
    return bgs

def run(name, k, cap_l=8, cap_c=12):
    L = mt.Level(name, k); P = Points(L); N = L.N
    rec = dict(state=name, k=k, exponent=N, characters=len(L.chars), sectors=[], couplings=[], points={})
    bgs = backgrounds(L); ells = sorted(set(key[0] for key in bgs)); rec["backgrounds"] = len(bgs); rec["extension_characters"] = len(ells)
    step = max(1, len(ells) // cap_l); pick = ells[::step][:cap_l]
    print("%s level %d: exponent %d, %d backgrounds on %d extension characters, %d taken" % (name, k, N, len(bgs), len(ells), len(pick)), flush=True)
    for l in pick:
        pt = P.cusp(l); rec["points"][str(l)] = pt[4]
        print("   l=%s slope %s: %s" % (l, nstr(L.S[l], 8), pt[4]), flush=True)
        if pt[0] is None: continue
        for key, (sign, inu) in sorted(bgs.items()):
            if key[0] != l: continue
            row = dict(l=list(l), slope=nstr(L.S[l], 12), sign=sign, nu_index=inu, kind=pt[4]["kind"], torsion={}, alpha={})
            for (nm, _, _), al in zip(SECT, key[1:]):
                row["alpha"][nm] = list(al)
                try: row["torsion"][nm] = nstr(P.sector(pt, L.add(al, L.neg(l))), 25)
                except (AssertionError, ZeroDivisionError) as ex: row["torsion"][nm] = None
            rec["sectors"].append(row)
    nb, cases, skipped, reach = L.frame_cases(); keys = list(cases); step = max(1, len(keys) // cap_c); keys = keys[::step][:cap_c]
    rec["distinct_cases"] = len(cases); checked = False
    print("   couplings: %d cases, %d taken" % (len(cases), len(keys)), flush=True)
    for (l, eta, A1) in keys:
        c = dict(l=list(l), eta=list(eta), A1=list(A1), types=sorted(set(u[0] for u in cases[(l, eta, A1)])), sign=cases[(l, eta, A1)][0][1],
                 s_l=nstr(L.S[l], 12), s_eta=nstr(L.S[eta], 12), eta_order2=L.order2(eta))
        pe = P.cusp(eta); rec["points"][str(eta)] = pe[4]; c["higgs_point"] = pe[4].get("kind", "not reached")
        if pe[0] is not None:
            try:
                b1 = L.add(A1, L.neg(eta)); b2 = L.add(b1, L.neg(l)); t1, t2 = P.sector(pe, b1), P.sector(pe, b2)
                c["doublets"] = [nstr(t1, 25), nstr(t2, 25)]; c["torsion_end_cusp"] = nstr(t1 * t2, 25); c["abs_end_cusp"] = nstr(abs(t1 * t2), 15)
                if not checked:
                    Bl, pl, gl, Tl = P.end(l); Be, p_, ge, Te = pe[:4]; z = P.z
                    ax = z ** A1[0] / (Bl.v[0] * Be.v[0]); ay = z ** A1[1] / (Bl.v[1] * Be.v[1])
                    t4 = mt.torsion_n(L.Phi, {1: ax * mt.kron(gl[1], ge[1]), 2: ay * mt.kron(gl[2], ge[2])}, mt.kron(Tl, Te))
                    c["rank_four_check"] = nstr(abs(t4 - t1 * t2) / max(1, abs(t4)), 3); checked = True
            except (AssertionError, ZeroDivisionError) as ex: c["error_end_cusp"] = str(ex)[:80]
            pl = P.cusp(l); rec["points"][str(l)] = pl[4]; c["extension_point"] = pl[4].get("kind", "not reached")
            if pl[0] is not None:
                try:
                    Bl, p1, gl, Tl = pl[:4]; Be, p2, ge, Te = pe[:4]; z = P.z
                    ax = z ** A1[0] / (Bl.v[0] * Be.v[0]); ay = z ** A1[1] / (Bl.v[1] * Be.v[1])
                    h = {1: ax * mt.kron(gl[1], ge[1]), 2: ay * mt.kron(gl[2], ge[2])}; T = mt.kron(Tl, Te)
                    I, a, b = ix.index(L.Phi, h, T); t = mt.torsion_n(L.Phi, h, T)
                    c["cusp_cusp"] = dict(index=I, interior=[a["interior"], b["interior"]], h1=[a["h1"], b["h1"]], torsion=nstr(t, 25), abs=nstr(abs(t), 15),
                                          smallest_kept=nstr(a["gaps"][1][0], 5), largest_dropped=nstr(a["gaps"][1][1], 5))
                except (AssertionError, ZeroDivisionError, KeyError, IndexError) as ex: c["error_cusp_cusp"] = str(ex)[:80]
        rec["couplings"].append(c)
        print("   l=%s eta=%s A1=%s %s: Higgs point %s, |torsion| %s, cusp-cusp %s" % (l, eta, A1, c["types"], c["higgs_point"], c.get("abs_end_cusp"), c.get("cusp_cusp", c.get("error_cusp_cusp"))), flush=True)
    return rec

if __name__ == "__main__":
    name, k = sys.argv[1], int(sys.argv[2])
    rec = run(name, k, int(sys.argv[3]) if len(sys.argv) > 3 else 8, int(sys.argv[4]) if len(sys.argv) > 4 else 12)
    out = pathlib.Path(sys.argv[5]) if len(sys.argv) > 5 else HERE
    json.dump(rec, open(out / ("complete_%s_%d.json" % (name, k)), "w"), indent=1)
