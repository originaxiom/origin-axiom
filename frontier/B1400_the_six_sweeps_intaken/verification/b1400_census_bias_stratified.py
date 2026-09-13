#!/usr/bin/env python3
"""Independent re-run of chat1's SWEEP 6, INSTRUMENTED for the confound their table omits.

Their census_bias.py skips any presentation with >3 generators and reports neither n nor the
skip count. Generator count correlates with complexity, which is the very variable the finding
is about -- so a depth-dependent SKIP RATE, or a shift in the generator mix, could produce the
decline without the underlying property getting rarer. Measured here:
  n, skipped, skip rate, the 2-gen/3-gen mix, and the rate RESTRICTED TO 2-GENERATOR groups.
"""
import itertools, sys, json
import snappy

E = [g for g in itertools.product(range(3), repeat=4) if (g[0]*g[3] - g[1]*g[2]) % 3 == 1]
assert len(E) == 24, len(E)
ID = (1, 0, 0, 1)
def mul(g, h):
    a,b,c,d = g; e,f,x,y = h
    return ((a*e+b*x)%3, (a*f+b*y)%3, (c*e+d*x)%3, (c*f+d*y)%3)
def inv(g):
    a,b,c,d = g; return (d%3, (-b)%3, (-c)%3, a%3)
def ev(w, m):
    r = ID
    for ch in w:
        g = m[ch.lower()]
        r = mul(r, g if ch.islower() else inv(g))
    return r
def gen_size(gs):
    S = {ID}; fr = [ID]
    while fr:
        x = fr.pop()
        for g in gs:
            y = mul(x, g)
            if y not in S:
                S.add(y); fr.append(y)
    return len(S)
def has_surj(G):
    gen = G.generators(); rel = G.relators(); n = len(gen)
    if n > 3: return None, n
    for img in itertools.product(E, repeat=n):
        m = {gen[i]: img[i] for i in range(n)}
        if all(ev(r, m) == ID for r in rel) and gen_size(img) == 24:
            return True, n
    return False, n

if sys.argv[1] == "control":
    # C-ALIVE: m004 must give 48 raw surjections -> 48/24 = 2 (B993's control)
    G = snappy.Manifold('m004').fundamental_group()
    gen, rel = G.generators(), G.relators()
    cnt = 0
    for img in itertools.product(E, repeat=len(gen)):
        m = {gen[i]: img[i] for i in range(len(gen))}
        if all(ev(r, m) == ID for r in rel) and gen_size(img) == 24:
            cnt += 1
    print(f"  m004: generators={len(gen)} relators={len(rel)}  raw surjections={cnt}"
          f"  /24 = {cnt/24}   B993 records 48 -> 2   match={cnt == 48}")
    # C-NULL: a group that must NOT surject (free abelian Z^2 has no SL(2,3) quotient of order 24)
    print(f"  C-NULL |SL(2,3)| = {len(E)} (must be 24); gen_size of the identity alone = {gen_size([ID])} (must be 1)")
    sys.exit(0)

lo, hi = int(sys.argv[1]), int(sys.argv[2])
C = snappy.OrientableCuspedCensus
n = hit = skipped = 0
bygen = {}
vols = []
for i in range(lo, hi):
    try:
        M = C[i]
        r, ng = has_surj(M.fundamental_group())
        if r is None:
            skipped += 1
            bygen.setdefault(ng, [0, 0])[0] += 1
            continue
        n += 1; hit += r
        b = bygen.setdefault(ng, [0, 0]); b[0] += 1; b[1] += r
        vols.append(float(M.volume()))
    except Exception:
        skipped += 1
out = dict(lo=lo, hi=hi, n=n, hit=hit, skipped=skipped,
           rate=100*hit/max(n,1), meanvol=sum(vols)/max(len(vols),1),
           bygen={str(k): v for k, v in sorted(bygen.items())})
print(json.dumps(out))
