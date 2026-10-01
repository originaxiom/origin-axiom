#!/usr/bin/env python3
"""The boundary-parabolic points of the periodic curves on the root's three-fold cover (s961), and what sits there.

A curve of B1444 has finitely many points where the peripheral holonomy is parabolic or trivial in PSL(2): its
reducible end, and the points with kappa = -2.  For a character of order four the curve is a rational quartic and
kappa = -2 at two complex-conjugate points (reached here by continuation round the branch point e = 1/4 on either
side); for a character of order two the curve is a line and kappa = -2 at the quaternion point (0, 0, 0).

  sectors   : the torsion of every doublet sector at the complete-cusp points of every curve of order four
  bidoublet : for every coupling of every background (B1445's cases): the class index and the torsion of the
              bidoublet at the parabolic points of the product of the extension's curve and the Higgs character's

usage: parabolic.py sectors | bidoublet <first> <last>
"""
import sys, json, itertools, collections, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "B1444_the_backgrounds_are_ends_of_periodic_curves" / "verification"))
sys.path.insert(0, str(HERE.parents[1] / "B1445_the_mass_term_on_the_product_of_two_curves" / "verification"))
sys.path.insert(0, str(HERE))
import curve_engine as ce
import mass_term as mt
import index_num as ix
from mpmath import mp, mpf, mpc, nstr, inverse, sqrt, exp, pi, pslq
from fractions import Fraction as Fr
mp.dps = 60
L = mt.Level("+LR", 3); z = exp(2j * pi / L.N)
_pts = {}

def walk(B, path):
    """continuation of the curve along a polyline in the complex e-plane, from the torsion point"""
    cur = mpc(mpf("1e-6")) * mpc(path[0]) / abs(mpc(path[0])); p = ce.newton(B.Phi, B.p0, B.sig, cur)
    for target in path:
        target = mpc(target); step = (target - cur) / 40
        while abs(cur - target) > mpf(10) ** (-40):
            s = step if abs(target - cur) > abs(step) else target - cur
            while True:
                try: q = ce.newton(B.Phi, p, B.sig, cur + s); break
                except (AssertionError, ZeroDivisionError):
                    s = s / 4
                    if abs(s) < mpf(10) ** (-10): raise AssertionError("stalled at e = %s" % nstr(cur, 8))
            p = q; cur = cur + s
    return p
def point(ell, which):
    """(B, p, g, T) at 'end' (e = 1e-14), 'cusp+', 'cusp-' (kappa = -2)"""
    if (ell, which) in _pts: return _pts[(ell, which)]
    B = L.curve(ell).B
    if which == "end": p = ce.newton(B.Phi, B.p0, B.sig, mpc(mpf("1e-14")))
    elif L.order2(ell):
        p1 = ce.newton(B.Phi, B.p0, B.sig, mpc(mpf("1e-3"))); mov = max(range(3), key=lambda i: abs(p1[i] - B.p0[i]))
        p = [mpc(c) for c in B.p0]; p[mov] = mpc(0)                      # the line: one coordinate moves; kappa = -2 where it vanishes
    else:
        side = 1 if which == "cusp+" else -1
        p = walk(B, [mpc("0.1", 0), mpc("0.1", side * 0.7), mpc(4, side * 0.7), mpc(4, 0)])
    q = ce.tracemap(B.Phi, p); assert all(abs(q[i] - B.sig[i] * p[i]) < mpf(10) ** (-35) for i in range(3)), "not on the curve"
    if which != "end": assert abs(ce.kappa(p) + 2) < mpf(10) ** (-35), "kappa is not -2"
    g = ce.rep(p); T = ce.intertwiner(B.Phi, g, B.sig)
    _pts[(ell, which)] = (B, p, g, T); return _pts[(ell, which)]
def in_K(t):
    """t as r1 + r2 sqrt5 + (r3 sqrt3 + r4 sqrt15) i, r rational, or None"""
    re = pslq([t.real, mpf(1), sqrt(mpf(5))], tol=mpf(10) ** (-45), maxcoeff=10 ** 4, maxsteps=10 ** 5)
    im = pslq([t.imag, sqrt(mpf(3)), sqrt(mpf(15))], tol=mpf(10) ** (-45), maxcoeff=10 ** 4, maxsteps=10 ** 5) if abs(t.imag) > mpf(10) ** (-40) else [1, 0, 0]
    if re and im and re[0] and im[0]:
        r = [Fr(-re[1], re[0]), Fr(-re[2], re[0]), Fr(-im[1], im[0]), Fr(-im[2], im[0])]
        return "%s + %s*sqrt(5) + %s*sqrt(-3) + %s*sqrt(-15)" % tuple(r)
    return None

def sectors():
    out = []; classes = collections.Counter()
    ells = [c for c in L.chars if c != (0, 0) and not L.order2(c)]
    for ell in ells:
        Ba, sl, rows = ce.analyse(1, "LR", 3, ell); info = {r["beta"]: r for r in rows}
        for which in ("cusp+", "cusp-"):
            B, p, g, T = point(ell, which); lam = g[1] * g[2] * inverse(g[1]) * inverse(g[2])
            rec = dict(ell=list(ell), point=which, X=nstr(p[0], 30), X_minpoly_residual=nstr(abs(p[0] ** 4 + 3 * p[0] ** 3 + 5 * p[0] ** 2 + 6 * p[0] + 4), 3),
                       tr_longitude=nstr(ce.tr(lam), 20), tr_meridian=nstr(ce.tr(T), 20), sectors=[])
            for be, r in sorted(info.items()):
                ax, ay = B.v[0] * z ** be[0], B.v[1] * z ** be[1]; tau, E, dP = ce.sector_torsion(B.Phi, g, T, ax, ay)
                kind = "%d matches, order %s, coefficient %s" % (r["matches"], r["order"], nstr(r["coeff"].real, 6))
                ex = in_K(tau); rec["sectors"].append(dict(beta=list(be), index=r["index"], kind=kind, torsion=nstr(tau, 25), abs=nstr(abs(tau), 25), exact=ex))
                classes[(kind, nstr(tau.real, 10), nstr(abs(tau.imag), 10), "|t| = " + nstr(abs(tau), 12), str(ex))] += 1
            out.append(rec); print("l = %s %s done" % (ell, which), flush=True)
    tab = [dict(count=v, kind=k[0], re=k[1], abs_im=k[2], modulus=k[3], exact=k[4]) for k, v in sorted(classes.items())]
    for t in tab: print(t)
    json.dump(dict(level="+LR 3", curves=len(ells), table=tab, points=out), open(HERE / "parabolic_sectors.json", "w"), indent=1)

def bidoublet(first, last):
    nb, cases, skipped, reach = L.frame_cases(); keys = list(cases)[first:last]; out = []
    for (l, eta, A1) in keys:
        types = sorted(set(u[0] for u in cases[(l, eta, A1)])); sign = cases[(l, eta, A1)][0][1]
        rec = dict(l=list(l), eta=list(eta), A1=list(A1), types=types, sign=sign, eta_order=2 if L.order2(eta) else 4, points=[])
        he = ("cusp+",) if L.order2(eta) else ("cusp+", "cusp-")
        combos = [(wl, we) for wl in ("cusp+", "cusp-") for we in he] + [("end", we) for we in he] + [("cusp+", "end"), ("cusp-", "end")]
        for wl, we in combos:
            Bl, pl, gl, Tl = point(l, wl); Be, pe, ge, Te = point(eta, we)
            ax = z ** A1[0] / (Bl.v[0] * Be.v[0]); ay = z ** A1[1] / (Bl.v[1] * Be.v[1])
            h = {1: ax * mt.kron(gl[1], ge[1]), 2: ay * mt.kron(gl[2], ge[2])}; T = mt.kron(Tl, Te)
            I, a, b = ix.index(L.Phi, h, T); t = mt.torsion_n(L.Phi, h, T)
            rec["points"].append(dict(extension=wl, higgs=we, index=I, V=dict(h0=a["h0"], t0=a["t0"], h1=a["h1"], interior=a["interior"]), Vdual=dict(h0=b["h0"], t0=b["t0"], h1=b["h1"], interior=b["interior"]),
                                      smallest_kept=nstr(a["gaps"][1][0], 5), largest_dropped=nstr(a["gaps"][1][1], 5), torsion=nstr(t, 25), abs=nstr(abs(t), 25), exact=in_K(t) if abs(t) > mpf(10) ** (-30) else "0"))
        out.append(rec); print("l=%s eta=%s A1=%s %s done" % (l, eta, A1, types), flush=True)
    json.dump(dict(level="+LR 3", backgrounds=nb, cases=len(cases), first=first, last=last, records=out), open(HERE / ("parabolic_bidoublet_%02d.json" % first), "w"), indent=1)

if __name__ == "__main__":
    if sys.argv[1] == "sectors": sectors()
    else: bidoublet(int(sys.argv[2]), int(sys.argv[3]))
