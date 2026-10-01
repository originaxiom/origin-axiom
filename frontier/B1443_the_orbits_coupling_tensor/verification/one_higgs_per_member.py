#!/usr/bin/env python3
"""Direct check on a level: for every generation-shaped background and EVERY character eta of the level, all invariant
functionals  V(Q) (x) V(u^c) (x) eta -> k  (and the same for Q.d^c) by linear algebra, and their relative triple
products by B1435's sealed instrument.  Claim: a non-zero coupling occurs for exactly one character, the background's
own Higgs character; so within a deck orbit whose members have distinct Higgs characters, Higgs class k couples to
member k and to no other."""
import sys, json, pathlib, collections
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "B1438_the_slope_law" / "verification"))
import cross_couplings as xc
ic, sc, cc = xc.ic, xc.sc, xc.cc
from relcup import Bundle, relative_lift

def run(eps, word, k, pstart=3000):
    r, bgs2, cls = sc.slope_census(eps, word, k); N = r["N"]
    ng, rels, mu, lam_w, tau, A, tors = ic.ac.level(eps, word, k)
    p = cc.primes_1mod(N, 1, pstart)[0]; zeta = pow(cc.primroot(p), (p - 1) // N, p)
    B = Bundle(ic.Phi_of(eps, word, k)); C, z, _ = B.fundamental(); plan = ic.Plan(B, C, z)
    chars = cc.characters(rels, [3], 3, N)
    add = lambda x, y: tuple((a + b) % N for a, b in zip(x, y)); neg = lambda x: tuple((-a) % N for a in x)
    H = {}; tab = collections.Counter()
    for key2, cnt in sorted(bgs2.items()):
        key = tuple(c + (0,) for c in key2); lc = key[0]; sg = cnt[0]; h1, ct = cc.cocycle(lc, rels, 3, N, zeta, p)
        for sA, sB in (("Q", "uc"), ("Q", "dc")):
            aA = key[1 + ic.SECT.index(sA)]; aB = key[1 + ic.SECT.index(sB)]
            own = add(add(aA, aB), neg(lc)); own = neg(own) if sg > 0 else own
            VA = ic.my_module(B, lc, aA, ct, N, zeta, p, dual=(sg < 0)); VB = ic.my_module(B, lc, aB, ct, N, zeta, p, dual=(sg < 0))
            a = ic.classes(VA)[0]; b = ic.classes(VB)[0]; EA = ic.Evaluator(VA, a, plan); EB = ic.Evaluator(VB, b, plan); eA = relative_lift(a)
            for eta in chars:
                Ts = xc.functionals(VA, VB, [pow(zeta, e_ % N, p) for e_ in eta], p)
                if eta not in H:
                    Vh = ic.char_module(B, eta, N, zeta, p); H[eta] = ic.Evaluator(Vh, ic.classes(Vh)[0], plan)
                couples = any(xc.triple_T(plan, B, EA, EB, H[eta], eA, T, p) for T in Ts)
                tab[("%s.%s" % (sA, sB), "own Higgs character" if eta == own else "another character", "functionals %d" % len(Ts), "couples" if couples else "no coupling")] += 1
    return dict(state=r["state"], k=k, N=N, prime=p, backgrounds=len(bgs2), characters=len(chars), table={" | ".join(kk): v for kk, v in sorted(tab.items())})

if __name__ == "__main__":
    out = [run(1, "LR", 3), run(-1, "LLLR", 3)]
    for o in out: print(json.dumps(o, indent=1))
    json.dump(out, open(HERE / "one_higgs_per_member.json", "w"), indent=1)
