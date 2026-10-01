#!/usr/bin/env python3
"""Couplings between sectors of DIFFERENT backgrounds (Theorem E of B1438).

For sector modules V_A, V_B of two backgrounds and a character eta, the invariant functionals
T: V_A (x) V_B (x) eta -> k are computed by linear algebra (no assumption on their shape), and for each the relative
triple product on the firing classes is computed with B1435's sealed instrument.
Claim: if the extension characters differ, the space is at most one-dimensional, spanned by T(a, b) = a_q b_q (the two
quotient components), and its triple product is zero; if they agree (the same background), eps appears and gives the
coupling of B1435."""
import sys, json, itertools, pathlib, collections
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "B1435_the_interaction_census" / "verification"))
import interaction_census as ic
from relcup import Bundle, relative_lift, mmul, mvec, X, Y
from myindex import rank_and_null
import slope_census as sc
cc = ic.cc

def functionals(VA, VB, eta_vals, p):
    """basis of {T in k^4 : T (rho_A(g) (x) rho_B(g)) eta(g) = T for g = x, y, t}; T indexed by (i, j) -> 2 i + j"""
    rows = []
    for g, MA, MB in ((0, VA.M[X], VB.M[X]), (1, VA.M[Y], VB.M[Y]), (2, VA.Mt, VB.Mt)):
        K = [[MA[i][k] * MB[j][l] % p for k in range(2) for l in range(2)] for i in range(2) for j in range(2)]   # (i j),(k l)
        for col in range(4):                                  # (T K eta - T)_col = 0
            rows.append([(K[r][col] * eta_vals[g] - (1 if r == col else 0)) % p for r in range(4)])
    rk, NS = rank_and_null(rows, 4, p, want_null=True)
    return NS

def triple_T(plan, B, Ea, Eb, Eh, e, T, p):
    import numpy as np
    a = Ea.VAL[plan.i1]; Rb = Eb.RHO[plan.i1]; bv = Eb.VAL[plan.i2]
    b0 = (Rb[:, 0, 0] * bv[:, 0] + Rb[:, 0, 1] * bv[:, 1]) % p; b1 = (Rb[:, 1, 0] * bv[:, 0] + Rb[:, 1, 1] * bv[:, 1]) % p
    w = Eh.RHO[plan.i12, 0, 0] * Eh.VAL[plan.i3, 0] % p
    f = (T[0] * a[:, 0] % p * b0 + T[1] * a[:, 0] % p * b1 + T[2] * a[:, 1] % p * b0 + T[3] * a[:, 1] % p * b1) % p
    tot = int((f * w % p * plan.kC).sum() % p)
    bz = Eb.VAL[plan.j1]; wz = Eh.RHO[plan.j1, 0, 0] * Eh.VAL[plan.j2, 0] % p
    fz = (T[0] * e[0] * bz[:, 0] + T[1] * e[0] * bz[:, 1] + T[2] * e[1] * bz[:, 0] + T[3] * e[1] * bz[:, 1]) % p
    return (tot - int((fz * wz % p * plan.kz).sum() % p)) % p

def run(eps, word, k, max_pairs=None, pstart=3000):
    r, bgs2, cls = sc.slope_census(eps, word, k); N = r["N"]
    ng, rels, mu, lam_w, tau, A, tors = ic.ac.level(eps, word, k)
    p = cc.primes_1mod(N, 1, pstart)[0]; zeta = pow(cc.primroot(p), (p - 1) // N, p)
    B = Bundle(ic.Phi_of(eps, word, k)); C, z, _ = B.fundamental(); plan = ic.Plan(B, C, z)
    chars = cc.characters(rels, [3], 3, N)
    add = lambda x, y: tuple((a + b) % N for a, b in zip(x, y)); neg = lambda x: tuple((-a) % N for a in x)
    mods = {}
    def sector(lc, al, sg):
        key = (lc, al, sg)
        if key not in mods:
            h1, ct = cc.cocycle(lc, rels, 3, N, zeta, p)
            V = ic.my_module(B, lc, al, ct, N, zeta, p, dual=(sg < 0)); a = ic.classes(V)[0]; e = relative_lift(a); assert e is not None
            mods[key] = (V, ic.Evaluator(V, a, plan), e)
        return mods[key]
    H = {}
    def hig(c):
        if c not in H:
            Vh = ic.char_module(B, c, N, zeta, p); hs = ic.classes(Vh); H[c] = (Vh, ic.Evaluator(Vh, hs[0], plan))
        return H[c]
    keys = sorted(bgs2.items()); stat = collections.Counter(); n = 0
    for (k1, c1), (k2, c2) in itertools.product(keys, repeat=2):
        if c1[0] != c2[0]: continue                           # same sign, so both families are zero modes of one kind
        same = (k1[0] == k2[0])
        if max_pairs and n >= max_pairs and not same: continue
        n += 1; sg = c1[0]; lc1, lc2 = k1[0] + (0,), k2[0] + (0,)
        for sA, sB in (("Q", "uc"), ("Q", "dc"), ("ec", "L")):
            aA = k1[1 + ic.SECT.index(sA)] + (0,); aB = k2[1 + ic.SECT.index(sB)] + (0,)
            VA, EA, eA = sector(lc1, aA, sg); VB, EB, eB = sector(lc2, aB, sg)
            for eta in chars:
                ev = [pow(zeta, e_ % N, p) for e_ in eta]
                Ts = functionals(VA, VB, ev, p)
                if not Ts: stat[("same l" if same else "different l", "no functional")] += 1; continue
                Vh, Eh = hig(eta)
                for T in Ts:
                    q = (3 if sg > 0 else 0)                  # the quotient-quotient component: a_2 b_2 for V, a_1 b_1 for V*
                    kind = "quotient.quotient" if [i for i, v in enumerate(T) if v % p] == [q] else "other"
                    y = triple_T(plan, B, EA, EB, Eh, eA, T, p)
                    stat[("same l" if same else "different l", "dim %d" % len(Ts), kind, "Y != 0" if y else "Y = 0")] += 1
    return dict(state=r["state"], k=k, N=N, prime=p, backgrounds=len(bgs2), ordered_pairs_of_backgrounds=n,
                table={" | ".join(kk): v for kk, v in sorted(stat.items())})

if __name__ == "__main__":
    out = []
    for st, k, mp in (("+LR", 3, None), ("-LLRLR", 1, None), ("-LR", 3, 1500), ("+LR", 4, 1500)):
        res = run(1 if st[0] == "+" else -1, st[1:], k, mp); out.append(res); print(json.dumps(res, indent=1), flush=True)
    json.dump(out, open(HERE / "cross_couplings.json", "w"), indent=1)
