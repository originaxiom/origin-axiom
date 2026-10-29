"""Check: is B1663's walk's exit law in Minkowski's class for every p?

Claim (derived in the T3/T4 report from Forghani-Kaimanovich 2025, Remark 1.22):
in PSL(2,Z) = Z2 * Z3 with a = S, b = ST, one has L = ab, R = ab^2, L^-1 = b^2 a,
R^-1 = ba. The step law of B1663 is then defined by the unlabelled Cayley graph
alone, so every automorphism of that graph fixing e preserves the walk, and the
exit law is one of the R-invariant measures kappa^{1/2,p'}: the b/b^2 letters of
the limit word are i.i.d. uniform, i.e. the continued-fraction digits of the
limit (after the first) are i.i.d. Geometric(1/2).

Test: simulate the walk at several p, read the digits of |xi| exactly, and compare
single and pair frequencies with Geometric(1/2) and its product law.
"""
import random, sys, json
from fractions import Fraction
from math import sqrt

L = (1, 1, 0, 1); R = (1, 0, 1, 1); Li = (1, -1, 0, 1); Ri = (1, 0, -1, 1)

def mul(A, B):
    a, b, c, d = A; e, f, g, h = B
    return (a*e + b*g, a*f + b*h, c*e + d*g, c*f + d*h)

def cf_digits(num, den, n):
    out = []
    num, den = abs(num), abs(den)
    while den and len(out) < n:
        q, r = divmod(num, den)
        out.append(q); num, den = den, r
    return out

def one_walk(p, rng, cap=10**60):
    X = (1, 0, 0, 1)
    while max(abs(x) for x in X) < cap:
        u = rng.random()
        if u < (1 - p) / 2: s = L
        elif u < 1 - p: s = R
        elif u < 1 - p / 2: s = Li
        else: s = Ri
        X = mul(X, s)
    a, b, c, d = X
    # limit xi ~ X(infinity) = a/c ; also X(0) = b/d agree to many digits
    da = cf_digits(a, c, 400); db = cf_digits(b, d, 400)
    k = 0
    while k < min(len(da), len(db)) and da[k] == db[k]: k += 1
    sign = 1 if (a * c) > 0 else -1
    return sign, da[:max(0, k - 20)]   # keep only digits on which both ends agree

def main():
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 7
    res = {}
    for p in (0.0, 0.25, 0.5):
        rng = random.Random(seed + int(1000 * p))
        singles = {}; pairs = {}; n1 = 0; n2 = 0; pos = 0; W = 1500; K = 100; fails = 0
        for _ in range(W):
            sgn, dg = one_walk(p, rng)
            pos += sgn > 0
            if len(dg) < K + 2:
                fails += 1; continue
            tail = dg[2:K + 2]       # a FIXED number of digits per walk (no length bias)
            for x in tail:
                k = min(x, 5); singles[k] = singles.get(k, 0) + 1; n1 += 1
            for x, y in zip(tail[::2], tail[1::2]):   # disjoint pairs
                kk = (min(x, 3), min(y, 3)); pairs[kk] = pairs.get(kk, 0) + 1; n2 += 1
        geo = {1: .5, 2: .25, 3: .125, 4: .0625, 5: .0625}
        g3 = {1: .5, 2: .25, 3: .25}
        chi1 = sum((singles.get(k, 0) - n1 * geo[k]) ** 2 / (n1 * geo[k]) for k in geo)
        chi2 = sum((pairs.get((i, j), 0) - n2 * g3[i] * g3[j]) ** 2 / (n2 * g3[i] * g3[j])
                   for i in g3 for j in g3)
        res[p] = dict(walks=W, fails=fails, P_pos=pos / W, digits=n1,
                      freq={k: round(singles.get(k, 0) / n1, 4) for k in geo},
                      chi2_single_df4=round(chi1, 2), pairs=n2,
                      chi2_pairs_df8=round(chi2, 2))
        print(p, res[p], flush=True)
    json.dump(res, open(sys.argv[2], "w"), indent=1) if len(sys.argv) > 2 else None

if __name__ == "__main__":
    main()
