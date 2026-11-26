# s22_pair_relation.py -- paired factors of charpoly(T) (s21): are they related by a Moebius or affine map of roots,
# or do they become the same polynomial after the substitution x -> x^2 type maps? (numerical, numpy roots, float64)
import numpy as np, itertools
pairs = {"cubic (p=7,k=5)": ([1, 3, -4, -4], [1, -3, -4, 8]),
         "sextic (p=7,k=1)": ([1, 6, 7, -14, -22, 8, 7], [1, -6, 7, 10, -10, -8, -1])}
for name, (f, g) in pairs.items():
    rf, rg = np.sort(np.roots(f).real), np.sort(np.roots(g).real)
    print(name, "roots f:", np.round(rf, 6), " roots g:", np.round(rg, 6))
    # test lambda*mu = const pairing or lambda+mu = const, lambda^2 - a relation, for some matching
    best = None
    for perm in itertools.permutations(range(len(rg))) if len(rg) <= 6 else []:
        mu = rg[list(perm)]
        for nm, val in (("sum", rf + mu), ("prod", rf * mu), ("mu-lam^2", mu - rf**2), ("mu+lam^2", mu + rf**2), ("(lam-1)(mu-1)", (rf-1)*(mu-1)), ("(lam+1)(mu+1)", (rf+1)*(mu+1)), ("(lam-2)(mu+2)", (rf-2)*(mu+2)), ("(lam+2)(mu-2)", (rf+2)*(mu-2))):
            spread = val.max() - val.min()
            if best is None or spread < best[0]: best = (spread, nm, val.mean(), perm)
    print("    best simple relation:", best)
