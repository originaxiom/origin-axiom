#!/usr/bin/env python3
"""The frame's backgrounds on a level, each sector with the order and leading coefficient of its torsion at the
reducible end of the background's periodic curve.
A background is (theta, psi_Y, W) with l = theta^2 / W and, for the sector of charges (s_Y, s_gamma),
alpha_s = theta psi_Y^{s_Y} W^{(s_gamma - 1)/2}, beta_s = alpha_s / l   (B1432).  It is generation-shaped when the six
charged sectors have index +1, or all -1  (firing law of B1438 from the slopes); nu^c is recorded as it comes."""
import sys, json, itertools, collections, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import curve_engine as ce
from mpmath import mpf, nstr
from mpmath import pslq, sqrt as msqrt, mp
from fractions import Fraction
def recognise(x):
    """x as a rational, or a + b sqrt(d) for d in 5, 2, 3, 13, 21; else 14 digits"""
    for d in (None, 5, 2, 3, 13, 21):
        vec = [x, mpf(1)] + ([msqrt(d)] if d else [])
        rel = pslq(vec, tol=mpf(10) ** (-13), maxcoeff=10 ** 5, maxsteps=10 ** 5)
        if rel and rel[0]:
            a = Fraction(-rel[1], rel[0]); b = Fraction(-rel[2], rel[0]) if d else 0
            if not d: return str(a)
            return "%s%s%s*sqrt(%d)" % (a if a else "", "+" if b > 0 and a else "", b, d)
    return nstr(x, 14)
SECT = [("Q", 1, 3), ("uc", -4, 3), ("ec", 6, 3), ("dc", 2, 1), ("L", -3, 1), ("nuc", 0, -5)]
def run(name, k, max_ell=None):
    eps = 1 if name[0] == "+" else -1; word = name[1:]
    Phi = ce.monodromy(eps, word, k); N = ce.exponent(Phi); chars = ce.level_characters(Phi, N); triv = (0, 0)
    S = {c: ce.slope(Phi, c[0], c[1], N) for c in chars if c != triv}
    add = lambda a, b: ((a[0] + b[0]) % N, (a[1] + b[1]) % N); mul = lambda a, m: ((m * a[0]) % N, (m * a[1]) % N); neg = lambda a: mul(a, -1)
    eq = lambda a, b: abs(a - b) < mpf(10) ** (-20)
    def index(l, al):
        be = add(al, neg(l))
        if al == triv or be == triv or l == triv: return 0
        return int(eq(S[al], S[l])) - int(eq(S[neg(be)], S[l]))
    bgs = {}
    for th, ps, W in itertools.product(chars, repeat=3):
        l = add(mul(th, 2), neg(W))
        if l == triv: continue
        al = [add(add(th, mul(ps, sy)), mul(W, (sg - 1) // 2)) for _, sy, sg in SECT]
        I = [index(l, a) for a in al]
        if all(i == 1 for i in I[:5]) or all(i == -1 for i in I[:5]): bgs[(l,) + tuple(al)] = I[0]      # the five charged sectors; nu^c is recorded, not required (B1432)
    print("%s level %d: %d characters, %d generation-shaped backgrounds (%d of sign +)" % (name, k, len(chars), len(bgs), sum(1 for v in bgs.values() if v > 0)), flush=True)
    ells = sorted(set(key[0] for key in bgs)); tab = {}
    if max_ell: ells = ells[:max_ell]
    for l in ells:
        if not ((2 * l[0]) % N or (2 * l[1]) % N):
            print("   l = %s has order two (a node of kappa = 2): no smooth curve; skipped" % (l,)); continue
        B, sl, rows = ce.analyse(eps, word, k, l)
        tab[l] = {r["beta"]: r for r in rows}
        print("   l = %s slope %s analysed" % (l, nstr(sl, 8)), flush=True)
    pat = collections.Counter(); out = []
    for key, sign in sorted(bgs.items()):
        l = key[0]
        if l not in tab: continue
        rec = dict(l=l, sign=sign, sectors={})
        for (nm, _, _), al in zip(SECT, key[1:]):
            r = tab[l][add(al, neg(l))]
            rec["sectors"][nm] = dict(alpha=al, order=r["order"], coeff=None if r["order"] is None else recognise(r["coeff"].real))
        out.append(rec)
        pat[tuple((nm, rec["sectors"][nm]["order"], rec["sectors"][nm]["coeff"]) for nm, _, _ in SECT)] += 1
    print("   patterns (sector: order, coefficient) x count:")
    for p, c in sorted(pat.items(), key=lambda kv: -kv[1]): print("     %3d x  %s" % (c, "  ".join("%s:%s,%s" % t for t in p)))
    return dict(state=name, k=k, backgrounds=len(bgs), table=[dict(l=list(r["l"]), sign=r["sign"], sectors=r["sectors"]) for r in out],
                patterns=[dict(count=c, pattern=[list(t) for t in p]) for p, c in pat.items()])
if __name__ == "__main__":
    res = run(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]) if len(sys.argv) > 3 else None)
    json.dump(res, open(HERE / ("frame_sectors_%s_%s.json" % (sys.argv[1], sys.argv[2])), "w"), indent=1, default=str)
