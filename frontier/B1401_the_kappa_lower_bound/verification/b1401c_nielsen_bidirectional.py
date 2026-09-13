#!/usr/bin/env python3
"""L206, BIDIRECTIONAL. Nielsen moves are invertible, so reachability is symmetric: BFS from
(a,b) and from the target, then intersect. Half-depth d covers Nielsen distance ~2d, so the
cost that reached distance 7 one-way reaches ~14 here.

Decisive in the POSITIVE direction, which is what L206 needs: a meeting point PROVES the target
is a generating pair, because the holonomy is discrete and faithful, so matrix equality IS word
equality.
"""
import sys
import mpmath as mp
import snappy
mp.mp.dps = 80

def M2(S):
    return mp.matrix([[mp.mpmathify(complex(S[0,0])), mp.mpmathify(complex(S[0,1]))],
                      [mp.mpmathify(complex(S[1,0])), mp.mpmathify(complex(S[1,1]))]])
def mul(A, B):
    return mp.matrix([[A[0,0]*B[0,0]+A[0,1]*B[1,0], A[0,0]*B[0,1]+A[0,1]*B[1,1]],
                      [A[1,0]*B[0,0]+A[1,1]*B[1,0], A[1,0]*B[0,1]+A[1,1]*B[1,1]]])
def inv(A):
    d = A[0,0]*A[1,1]-A[0,1]*A[1,0]
    return mp.matrix([[A[1,1]/d, -A[0,1]/d], [-A[1,0]/d, A[0,0]/d]])
def key(A, q=14):
    e = [A[0,0], A[0,1], A[1,0], A[1,1]]
    i = max(range(4), key=lambda k: abs(e[k]))
    s = e[i]/abs(e[i])
    # ABSOLUTE rounding, not significant digits: nstr prints the full noise mantissa of a
    # near-zero entry, so two copies of the SAME matrix got different keys and the m004
    # control failed. E75 again, in a new disguise -- and raising precision made it worse.
    return tuple((mp.nstr(mp.mpf(round(float(mp.re(x/s)), 10)), 12),
                  mp.nstr(mp.mpf(round(float(mp.im(x/s)), 10)), 12)) for x in e)
def pk(U, V): return (key(U), key(V))
MOVES = [lambda u,v:(v,u), lambda u,v:(inv(u),v), lambda u,v:(u,inv(v)),
         lambda u,v:(mul(u,v),v), lambda u,v:(u,mul(u,v)),
         lambda u,v:(mul(v,u),v), lambda u,v:(u,mul(v,u)),
         lambda u,v:(mul(u,inv(v)),v), lambda u,v:(u,mul(inv(u),v)),
         lambda u,v:(mul(inv(v),u),v), lambda u,v:(u,mul(v,inv(u)))]
CAP = mp.mpf(10)**14

def ball(start, depth, cap_pairs):
    seen = {pk(*start): 0}
    frontier = [start]
    for d in range(1, depth+1):
        nxt = []
        for (u, v) in frontier:
            for mv in MOVES:
                try: nu, nv = mv(u, v)
                except Exception: continue
                if max(abs(nu[0,0]),abs(nu[0,1]),abs(nu[1,0]),abs(nu[1,1]),
                       abs(nv[0,0]),abs(nv[0,1]),abs(nv[1,0]),abs(nv[1,1])) > CAP: continue
                k = pk(nu, nv)
                if k in seen: continue
                seen[k] = d; nxt.append((nu, nv))
                if len(seen) > cap_pairs: return seen, d, "CAP"
        frontier = nxt
        if not frontier: return seen, d, "closed"
    return seen, depth, "depth"

name = sys.argv[1] if len(sys.argv) > 1 else "m003"
D = int(sys.argv[2]) if len(sys.argv) > 2 else 5
G = snappy.Manifold(name).fundamental_group()
a, b = M2(G.SL2C('a')), M2(G.SL2C('b'))
mer, lon = G.meridian(0), G.longitude(0)
print(f"  {name}: mer={mer!r} lon={lon!r}   half-depth {D} (Nielsen distance ~{2*D})", flush=True)
F, df, wf = ball((a, b), D, 300000)
print(f"  forward ball: {len(F)} pairs, depth {df} [{wf}]", flush=True)
for lab, w in (("(mer,a)", (mer,'a')), ("(mer,b)", (mer,'b')),
               ("(lon,a)", (lon,'a')), ("(lon,b)", (lon,'b'))):
    T = (M2(G.SL2C(w[0])), M2(G.SL2C(w[1])))
    if pk(*T) in F:
        print(f"  {lab}: in the forward ball at depth {F[pk(*T)]} -> GENERATES (PROVED)", flush=True)
        continue
    B, db, wb = ball(T, D, 300000)
    meet = set(F) & set(B)
    if meet:
        m0 = min(meet, key=lambda k: F[k]+B[k])
        print(f"  {lab}: MEET at fwd {F[m0]} + bwd {B[m0]} = distance {F[m0]+B[m0]}"
              f" -> GENERATES (PROVED)", flush=True)
    else:
        print(f"  {lab}: no meeting point ({len(B)} bwd pairs [{wb}]) -- NOT SETTLED", flush=True)
