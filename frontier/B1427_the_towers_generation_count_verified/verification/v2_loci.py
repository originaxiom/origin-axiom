#!/usr/bin/env python3
"""(2) OWN enumeration of the non-split character loci on the cyclic covers Y_n of m004, and h^1(pi; chi^2)
at every one of them, computed BOTH over prime fields GF(p) (p = 1 mod N) AND exactly over Q(zeta_m),
m = order of chi^2.  Conventions derived here: a 1-cocycle f obeys f(gh) = f(g) + rho(g) f(h), so
f(w) = sum_g D_g(w) f(g) with D_g accumulated over the letters of w (prefix convention);
Z^1 = ker of the Fox-Jacobian of the relators, B^1 = {(rho(g)-1)v}, h^1 = dim Z^1 - dim B^1.
For a 1-dimensional module chi^2: dim B^1 = 0 if chi^2 trivial else 1.
NOTE on primes: rank over GF(p) can only DROP, so h^1 over GF(p) >= h^1 in characteristic 0.
Hence loci(char 0) is contained in loci(GF(p)) for every p, and an exact run on the union settles it."""
import sys, os, math, json, warnings, time
from collections import Counter
from fractions import Fraction
warnings.filterwarnings("ignore")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import snappy
from cyclo import Cyc, rank_cyc

# ---------------- GF(p) minimal linear algebra (own) ----------------
def gf_rank(rows, ncols, p):
    R = [list(r) for r in rows]; rk = 0
    for c in range(ncols):
        piv = None
        for i in range(rk, len(R)):
            if R[i][c] % p: piv = i; break
        if piv is None: continue
        R[rk], R[piv] = R[piv], R[rk]
        iv = pow(R[rk][c], p - 2, p); R[rk] = [x * iv % p for x in R[rk]]
        for i in range(len(R)):
            if i != rk and R[i][c] % p:
                f = R[i][c]; R[i] = [(x - f * y) % p for x, y in zip(R[i], R[rk])]
        rk += 1
        if rk == len(R): break
    return rk

def primitive_root(p):
    n = p - 1; f = []; m = n; d = 2
    while d * d <= m:
        if m % d == 0:
            f.append(d)
            while m % d == 0: m //= d
        d += 1
    if m > 1: f.append(m)
    for g in range(2, p):
        if all(pow(g, n // q, p) != 1 for q in f): return g
    raise ValueError

def primes_1_mod(N, k, start):
    out = []; q = start
    while len(out) < k:
        q += 1
        if q % N != 1: continue
        if all(q % d for d in range(2, int(q ** .5) + 1)): out.append(q)
    return out

# ---------------- Fox derivative of a word for a 1-dim module ----------------
def fox_1dim(word, gens, val, mul, inv, one, zero, add, sub):
    D = {g: zero for g in gens}; pre = one
    for ch in word:
        g = ch.lower()
        if ch.islower():
            D[g] = add(D[g], pre); pre = mul(pre, val[g])
        else:
            pre = mul(pre, inv(val[g])); D[g] = sub(D[g], pre)
    return D

def h1_gf(gens, rels, e, m, p, zeta_m):
    """h^1(pi; chi^2) over GF(p); chi^2(g) = zeta_m^{e[g]}"""
    val = {g: pow(zeta_m, e[g] % m, p) for g in gens}
    ivl = {g: pow(val[g], p - 2, p) for g in gens}
    rows = []
    for r in rels:
        D = fox_1dim(r, gens, val, lambda a, b: a * b % p, lambda a: pow(a, p - 2, p), 1, 0,
                     lambda a, b: (a + b) % p, lambda a, b: (a - b) % p)
        rows.append([D[g] % p for g in gens])
    rk = gf_rank(rows, len(gens), p)
    dimZ = len(gens) - rk
    dimB = 0 if all(x % m == 0 for x in e.values()) else 1
    return dimZ - dimB

def h1_exact(gens, rels, e, m):
    F = Cyc(m)
    val = {g: F.zeta(e[g] % m) for g in gens}
    rows = []
    for r in rels:
        D = fox_1dim(r, gens, val, F.mul, F.inv, F.one(), F.zero(), F.add, F.sub)
        rows.append([D[g] for g in gens])
    rk = rank_cyc(F, rows, len(gens))
    dimZ = len(gens) - rk
    dimB = 0 if m == 1 else 1
    return dimZ - dimB

# ---------------- driver ----------------
def abvec(word, gens):
    v = {g: 0 for g in gens}
    for ch in word: v[ch.lower()] += 1 if ch.islower() else -1
    return [v[g] for g in gens]

def run(n, N, nprimes=3, pstart=1000, exact=True):
    t0 = time.time()
    Y = snappy.Manifold('m004').covers(n, cover_type='cyclic')[0]
    G = Y.fundamental_group()
    gens = list(G.generators()); rels = list(G.relators())
    mu, lam = G.peripheral_curves()[0]
    A = [abvec(r, gens) for r in rels]
    H1 = str(Y.homology())
    P = primes_1_mod(N, nprimes, pstart)
    zet = {p: pow(primitive_root(p), (p - 1) // N, p) for p in P}
    # character group: k in (Z/N)^g with A k = 0 mod N
    import numpy as np
    g = len(gens)
    grids = np.meshgrid(*[np.arange(N, dtype=np.int64)] * g, indexing='ij')
    K = np.stack([x.ravel() for x in grids], axis=1)          # N^g x g
    ok = np.ones(len(K), dtype=bool)
    for a in A:
        ok &= (K @ np.array(a, dtype=np.int64)) % N == 0
    chars = [tuple(int(x) for x in row) for row in K[ok]]
    del K, grids, ok
    # h1 depends only on chi^2; cache on the normalised (m, e)
    def key_of(k):
        tw = [2 * x % N for x in k]
        d = N
        for x in tw: d = math.gcd(d, x)
        m = N // d
        return (m, tuple((x // d) % m for x in tw)) if m > 1 else (1, tuple(0 for _ in tw))
    cache_gf = {}; cache_ex = {}
    res = {}
    for k in chars:
        if all(x == 0 for x in k): continue          # chi trivial excluded, as the record does
        kk = key_of(k)
        if kk not in cache_gf:
            m, ee = kk; e = dict(zip(gens, ee))
            zm = {p: pow(zet[p], N // m, p) for p in P} if m > 1 else {p: 1 for p in P}
            cache_gf[kk] = tuple(h1_gf(gens, rels, e, max(m, 1), p, zm[p]) for p in P)
        res[k] = cache_gf[kk]
    # loci per prime, and the union / intersection
    per_prime = [set(k for k, v in res.items() if v[i] >= 1) for i in range(len(P))]
    union = set().union(*per_prime); inter = set.intersection(*per_prime)
    out = dict(n=n, N=N, H1=H1, gens=gens, rels=rels, mu=mu, lam=lam,
               ab_mu=abvec(mu, gens), ab_lam=abvec(lam, gens), primes=P,
               n_chars=len(chars), loci_per_prime=[len(s) for s in per_prime],
               loci_union=len(union), loci_inter=len(inter))
    # exact pass on the union (a superset of the true loci)
    if exact:
        exval = {}
        for k in sorted(union):
            kk = key_of(k)
            if kk not in cache_ex:
                m, ee = kk; cache_ex[kk] = h1_exact(gens, rels, dict(zip(gens, ee)), max(m, 1))
            exval[k] = cache_ex[kk]
        true_loci = {k: v for k, v in exval.items() if v >= 1}
        out['exact_h1_multiset_on_union'] = dict(Counter(exval.values()))
        out['loci_exact'] = len(true_loci)
        out['exact_h1_multiset_on_loci'] = dict(Counter(true_loci.values()))
        out['max_h1'] = max(exval.values()) if exval else 0
        # cusp data at each true locus: chi(mu), chi(lambda) as exponents of zeta_N
        am = abvec(mu, gens); al = abvec(lam, gens)
        cusp = Counter()
        for k in true_loci:
            cusp[(sum(a * b for a, b in zip(am, k)) % N, sum(a * b for a, b in zip(al, k)) % N)] += 1
        out['cusp_exponents'] = {str(kk): v for kk, v in sorted(cusp.items())}
        out['order_of_chi'] = dict(Counter(N // math.gcd(N, math.gcd(math.gcd(k[0], k[1] if len(k) > 1 else 0),
                                    k[2] if len(k) > 2 else 0)) for k in true_loci))
        out['loci_list'] = sorted(true_loci)
    out['seconds'] = round(time.time() - t0, 1)
    return out

if __name__ == '__main__':
    jobs = eval(sys.argv[1]) if len(sys.argv) > 1 else [(4, 60)]
    allout = {}
    for (n, N) in jobs:
        o = run(n, N)
        allout[f"Y{n}_N{N}"] = o
        print(json.dumps({k: v for k, v in o.items() if k != 'loci_list'}, indent=1), flush=True)
    json.dump(allout, open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
              'v2_loci_%s.json' % '_'.join(f"{n}n{N}" for n, N in jobs)), 'w'), indent=1)
