"""Independent existence check: take backgrounds found by the fast instrument (short presentation, orbit cache), translate
their characters to the LONG presentation (x = x_0, y = y_0, T = T), rebuild every sector module there with B1432's own
module/cocycle/index (no cache), at primes from 40000 up, and check that the counts are a background's."""
import sys, json, os, random
os.environ['SHORT'] = '1'
import fast_census as FC
import first_background as F
import short_cover
CC = F.CC
long_cover = F.__dict__['_long'] if '_long' in F.__dict__ else None
name, n = sys.argv[1], int(sys.argv[2])
F.ROOTS[name] = name; phi = F.mono(name)
FC.install(phi, n); CC.cover = short_cover.short_cover(phi)
tors, _ = F.torsion(phi, n); N = F.exponent(tors)
out, bgs, I, chars, cov = CC.census(n, N, 5000, verbose=False)
print(name, n, 'fast run: backgrounds', len(bgs), flush=True)
random.seed(1); sample = random.sample(sorted(bgs), min(6, len(bgs)))
# restore the plain instrument and the long presentation
CC.index = FC._index; CC.module = FC._module
import importlib; importlib.reload(F); CC = F.CC
ng, rels, mu, lam, tau = F.bundle_cover(phi)(n)
L_rels = [CC.letters(r) for r in rels]; L_mu = CC.letters(mu); L_lam = CC.letters(lam)
def to_long(c): return (c[0], c[1], c[1 + n])          # T, x_0, y_0
P = CC.primes_1mod(N, 2, 40000)
ok = 0
for key in sample:
    lc = to_long(key[0]); res = []
    for p in P:
        zeta = pow(CC.primroot(p), (p - 1) // N, p)
        h1, ct = CC.cocycle(lc, rels, ng, N, zeta, p)
        cnt = []
        for a in key[1:]:
            V = CC.module(lc, to_long(a), ct, ng, N, zeta, p); assert V.ok(L_rels)
            cnt.append(CC.index(V, L_rels, L_mu, L_lam)[0])
        res.append((p, h1, tuple(cnt)))
    fast = bgs[key]
    good = all(r[2] == tuple(fast) for r in res) and len(set(fast[:5])) == 1 and fast[0] != 0
    ok += good
    print('  bg', 'counts fast', fast, '| long, no cache:', [(r[0], r[1], r[2]) for r in res], 'OK' if good else 'MISMATCH', flush=True)
print(name, n, f'confirmed {ok}/{len(sample)}')
