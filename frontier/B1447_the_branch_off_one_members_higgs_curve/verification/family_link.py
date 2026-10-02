import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
for _d in ("B1444_the_backgrounds_are_ends_of_periodic_curves", "B1445_the_mass_term_on_the_product_of_two_curves"):
    sys.path.insert(0, str(HERE.parents[1] / _d / "verification"))
sys.path.insert(0, str(HERE))
import sys, itertools, collections
import curve_engine as ce
import mass_term as mt
from mpmath import mpf
def run(name, k):
    L = mt.Level(name, k); N = L.N; S = L.S; triv = (0, 0); eps = L.eps
    Phi1 = ce.monodromy(eps, L.word, 1); (a, b), (c, d) = ce.ab(Phi1[1]), ce.ab(Phi1[2])
    deck = lambda ch: ((a * ch[0] + b * ch[1]) % N, (c * ch[0] + d * ch[1]) % N)
    add, neg = L.add, L.neg; mul = lambda x, m: ((m * x[0]) % N, (m * x[1]) % N); eq = lambda x, y: abs(x - y) < mpf(10) ** (-20)
    names = [s[0] for s in mt.SECT]
    def index(l, al):
        be = add(al, neg(l))
        if al == triv or be == triv: return 0
        return int(eq(S[al], S[l])) - int(eq(S[be], S[l]))
    bgs = {}
    for th, ps, W in itertools.product(L.chars, repeat=3):
        l = add(mul(th, 2), neg(W))
        if l == triv: continue
        al = [add(add(th, mul(ps, sy)), mul(W, (sg - 1) // 2)) for _, sy, sg in mt.SECT]; I = [index(l, x) for x in al]
        if all(i == 1 for i in I[:5]) or all(i == -1 for i in I[:5]): bgs[(l,) + tuple(al)] = I[0]
    seen = set(); tally = collections.Counter(); sizes = collections.Counter(); nonmember = len(L.chars) - 1
    for key in sorted(bgs):
        if key in seen: continue
        orb = [key]; kk = tuple(deck(x) for x in key)
        while kk != key and len(orb) < 50: orb.append(kk); kk = tuple(deck(x) for x in kk)
        seen.update(orb); sizes[len(orb)] += 1
        if len(orb) != 3 or not all(o in bgs for o in orb): continue
        ls = [o[0] for o in orb]; al = [dict(zip(names, o[1:])) for o in orb]; be = [{n: add(al[i][n], neg(ls[i])) for n in names} for i in range(3)]
        for typ, A, B in (("up", "Q", "uc"), ("down", "Q", "dc")):
            eta = [add(al[i][A], be[i][B]) for i in range(3)]; prod = (sum(e[0] for e in eta) % N, sum(e[1] for e in eta) % N)
            pool = set()
            for i in (1, 2):
                for n in names: pool |= {al[i][n], be[i][n], neg(al[i][n]), neg(be[i][n])}
            thirds = [add(al[0][A], eta[2]), add(be[0][A], eta[2]), add(al[0][A], neg(eta[1])), add(be[0][A], neg(eta[1]))]
            lprod = (sum(l[0] for l in ls) % N, sum(l[1] for l in ls) % N)
            tally[(typ, "distinct eta %d" % len(set(eta)), "eta product trivial %s" % (prod == triv), "l product trivial %s" % (lprod == triv), "thirds that are sector characters of members 1, 2: %d of 4" % sum(t in pool for t in thirds), "pool covers %d of %d characters" % (len(pool - {triv}), nonmember))] += 1
    print("%s level %d: torsion %d, backgrounds %d, orbit sizes %s" % (name, k, len(L.chars), len(bgs), dict(sizes)))
    for kk, v in sorted(tally.items(), key=str): print("   %3d orbits: %s" % (v, " | ".join(kk)))
for name, k in (("+LR", 3), ("-LR", 3), ("+LLR", 3), ("-LLLR", 3)): run(name, k)
