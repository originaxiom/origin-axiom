#!/usr/bin/env python3
"""Where a second member's Higgs can be switched on along the first's curve (root, three-fold cover).

The three Higgs characters eta_0, eta_1, eta_2 of a deck orbit have trivial product and equal slopes.  On the curve
of eta_0 the doublet sector with characters (alpha, beta) = (eta_0 eta_1, eta_1) is doubly matched; a class of it at
a point of the curve is a first-order direction in which eta_1's Higgs is switched on there.  B1444's exact record
gives the product N of that sector's torsions for the two signs of the meridian on the quartic
X = u - 1, Y = -Z, Z^2 = 1 + 1/u^2:

      N = 8 sqrt2 Z P5(u) / u^2 + R6(u) / u^3 ,

and N = 0 forces R6^2 = 128 (u^2 + 1) P5^2.
"""
import sys, json, itertools, pathlib
HERE = pathlib.Path(__file__).resolve().parent
B1444 = HERE.parents[1] / "B1444_the_backgrounds_are_ends_of_periodic_curves" / "verification"
sys.path.insert(0, str(B1444))
import curve_engine as ce
from mpmath import mp, mpf, mpc, sqrt, polyroots, nstr, exp, pi, inverse
mp.dps = 60

def exact():
    import sympy as sp
    rec = open(B1444 / "torsion_exact_run.txt").read()
    assert "((-8*z^3 + 8*z)*uu^5 + (32*z^3 - 32*z)*uu^4 + (-48*z^3 + 48*z)*uu^3 + (24*z^3 - 24*z)*uu^2 + (16*z^3 - 16*z)*uu - 16*z^3 + 16*z)/uu^2)*ZZ_ + (12*uu^6 - 44*uu^5 + 68*uu^4 - 60*uu^3 + 24*uu^2 + 24*uu - 24)/uu^3" in rec, "the exact record has changed"
    u = sp.symbols("u")
    P5 = u**5 - 4*u**4 + 6*u**3 - 3*u**2 - 2*u + 2                 # -8 z^3 + 8 z = 8 sqrt2 for z = exp(2 pi i / 8)
    R6 = 12*u**6 - 44*u**5 + 68*u**4 - 60*u**3 + 24*u**2 + 24*u - 24
    F = sp.factor(sp.expand(R6**2 - 128*(u**2 + 1)*P5**2)); w = sp.symbols("w")
    six = u**6 - 8*u**4 + 12*u**3 + 4
    assert sp.expand(F - 16*(u - 1)**4*(u + 1)**2*six) == 0
    assert sp.Poly(six, u).is_irreducible
    resw = sp.factor(sp.resultant(six, u*w - u**2 + 1, u))
    return dict(factorisation=str(F), P5=str(sp.factor(P5)), R6=str(sp.factor(R6)), w_polynomial=str(resw), discriminant=str(sp.factorint(sp.discriminant(six, u))))

def numeric():
    Phi = ce.monodromy(1, "LR", 3); Phi1 = ce.monodromy(1, "LR", 1); sig = (1, -1, -1); z8 = exp(2j * pi / 8); N = 4
    roots = polyroots([1, 0, -8, 12, 0, 0, 4], maxsteps=300, extraprec=300); out = []
    # the deck orbit of the extension character at u = 1 and the doubly matched sectors there
    (a, b), (c, d) = ce.ab(Phi1[1]), ce.ab(Phi1[2]); deck = lambda ch: ((a * ch[0] + b * ch[1]) % N, (c * ch[0] + d * ch[1]) % N)
    for u in roots:
        w = u - 1 / u
        for zs in (1, -1):
            Z = zs * sqrt(1 + 1 / u ** 2); p = (u - 1, -Z, Z); q = ce.tracemap(Phi, p)
            assert all(abs(q[i] - sig[i] * p[i]) < mpf(10) ** (-40) for i in range(3)), "not on the curve"
            g = ce.rep(p); T = ce.intertwiner(Phi, g, sig); zero = []
            for (i, j) in itertools.product((0, 2, 4, 6), (1, 3, 5, 7)):
                for ts in (1, -1):
                    try: tau, E, dP = ce.sector_torsion(Phi, g, ts * T, z8 ** i, z8 ** j)
                    except AssertionError: continue
                    if abs(tau) < mpf(10) ** (-30): zero.append(dict(a=[i, j], meridian_sign=ts))
            out.append(dict(u=nstr(u, 25), w=nstr(w, 25), kappa=nstr(ce.kappa(p), 25), tr_meridian=nstr(ce.tr(T), 25), Z_sign=zs, real=bool(abs(u.imag) < mpf(10) ** (-40)), zero_sectors=zero))
    # the orbit statement, on the level's own characters
    B, sl, rows = ce.analyse(1, "LR", 3, (2, 1)); S = B.slopes()
    orbit = [(2, 1)];
    while deck(orbit[-1]) != orbit[0]: orbit.append(deck(orbit[-1]))
    prod = tuple(sum(o[i] for o in orbit) % N for i in range(2))
    double = sorted(tuple(r["beta"]) for r in rows if r["matches"] == 2)
    inv = lambda ch: ((-ch[0]) % N, (-ch[1]) % N)
    partners = sorted(set(o for o in orbit[1:]) | set(inv(o) for o in orbit[1:]))
    return dict(points=out, orbit_of_the_character=[list(o) for o in orbit], product_trivial=prod == (0, 0), slopes_equal=len(set(nstr(S[o], 20) for o in orbit)) == 1,
                doubly_matched_beta=[list(x) for x in double], orbit_partners_and_inverses=[list(x) for x in partners])

if __name__ == "__main__":
    res = dict(exact=exact(), numeric=numeric())
    json.dump(res, open(HERE / "branch_points.json", "w"), indent=1)
    print(json.dumps(res["exact"], indent=1))
    for p in res["numeric"]["points"]: print(p["u"][:22], "w", p["w"][:22], "kappa", p["kappa"][:22], "tr T", p["tr_meridian"][:22], "Z%+d" % p["Z_sign"], p["zero_sectors"])
    print({k: v for k, v in res["numeric"].items() if k != "points"})
