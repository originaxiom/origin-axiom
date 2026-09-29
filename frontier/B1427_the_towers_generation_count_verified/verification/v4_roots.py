#!/usr/bin/env python3
"""Identify the h^1>=1 locus of Y_4 (and Y_2,Y_3,Y_5) on the FULL character torus: for each component of
Hom(H_1, C*) take the gcd of the three 2x2 Fox minors, test squarefreeness, split off the part supported on
roots of unity of order dividing M, and locate the remaining roots numerically."""
import sys, os, json, cmath, warnings
warnings.filterwarnings("ignore")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import numpy as np
from fractions import Fraction
from cyclo import Cyc
from v3_full_character_variety import (LP, const, tvar, to_poly, pdeg, pdivmod, pgcd, strip_t,
                                       fox_LP, abvec, analyse)
import snappy

def deriv(p, F):
    return [ (lambda c, k: tuple(x*k for x in c))(p[i], i) for i in range(1, len(p)) ]

def poly_to_complex(p, F, zval):
    """evaluate the Cyc coefficients at a chosen numeric zeta, giving complex coefficients"""
    out = []
    for c in p:
        s = 0j
        for i, x in enumerate(c): s += complex(x) * zval**i
        out.append(s)
    return out

def run(n, e, M=60):
    Y = snappy.Manifold('m004').covers(n, cover_type='cyclic')[0]
    G = Y.fundamental_group(); gens = list(G.generators()); rels = list(G.relators())
    A = [abvec(r, gens) for r in rels]
    F = Cyc(e)
    zero_cols = [j for j in range(3) if all(a[j] == 0 for a in A)]
    fg = zero_cols[0]; others = [j for j in range(3) if j != fg]
    sols = []
    for ka in range(e):
        for kc in range(e):
            k = [0,0,0]; k[others[0]] = ka; k[others[1]] = kc
            if all(sum(a[j]*k[j] for j in range(3)) % e == 0 for a in A): sols.append(tuple(k))
    tot = 0; sf_ok = True; in_M = 0; out_M = []; orders = {}
    zval = cmath.exp(2j*cmath.pi/e)
    for k in sols:
        val = {}; ival = {}
        for j, g in enumerate(gens):
            if j == fg: val[g] = tvar(F,1); ival[g] = tvar(F,-1)
            else: val[g] = const(F, F.zeta(k[j])); ival[g] = const(F, F.zeta(-k[j]))
        Mx = [[fox_LP(r, gens, val, ival, F)[g] for g in gens] for r in rels]
        minors = [to_poly(Mx[0][a]*Mx[1][b] - Mx[0][b]*Mx[1][a], F) for (a,b) in ((0,1),(0,2),(1,2))]
        g_min = []
        for p in minors:
            p = strip_t(p, F); g_min = p if not g_min else pgcd(g_min, p, F)
        d = pdeg(g_min)
        if d <= 0: continue
        tot += d
        # squarefree?
        dp = deriv(g_min, F)
        gg = pgcd(g_min, dp, F)
        if pdeg(gg) > 0: sf_ok = False
        # part supported on mu_M
        cyc = [F.zero()]*(M+1); cyc[0] = F.neg(F.one()); cyc[M] = F.one()
        gm = pgcd(g_min, cyc, F); dM = pdeg(gm) if gm else 0
        in_M += max(dM, 0)
        if d - max(dM,0) > 0:
            cpx = poly_to_complex(g_min, F, zval)
            rts = np.roots(list(reversed(cpx)))
            out_M.append(dict(k=list(k), deg=d, deg_in_muM=max(dM,0),
                              roots=[[float(abs(r)), float(cmath.phase(r)/(2*cmath.pi))] for r in rts]))
        # order of each root of unity root, via gcd with t^m - 1
        for m in sorted(set(list(range(1, M+1)))):
            cm = [F.zero()]*(m+1); cm[0] = F.neg(F.one()); cm[m] = F.one()
            gmm = pgcd(g_min, cm, F); dm = pdeg(gmm) if gmm else 0
            if dm > 0:
                orders[m] = orders.get(m, 0)
                break
    return dict(n=n, e=e, total_deg=tot, all_squarefree=sf_ok, deg_in_mu_M=in_M, M=M,
                components_with_roots_outside_mu_M=out_M)

if __name__ == '__main__':
    res = {}
    for n, e in [(4,15),(2,5),(3,4),(5,11)]:
        r = run(n, e, M=60 if n != 3 else 12)
        res[n] = r
        print(json.dumps(r, indent=1), flush=True)
    json.dump(res, open('<here>/v4_roots.json','w'), indent=1)
