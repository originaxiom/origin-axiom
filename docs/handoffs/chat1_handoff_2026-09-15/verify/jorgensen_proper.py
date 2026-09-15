#!/usr/bin/env python3
"""PROPER Jorgensen upper bounds. Replaces the mislabelled 'slack table'.

J(Gamma) = inf over GENERATING pairs of  |tr^2 X - 4| + |tr[X,Y] - 2|.
Method: BFS over NIELSEN MOVES from SnapPy's generating pair. Nielsen moves preserve
generation, so every pair visited genuinely generates => every value is a true UPPER
BOUND on J(Gamma). Depth is declared. Nothing here is an infimum.
"""
import snappy, sys, itertools
def mul(A,B): return [[A[0][0]*B[0][0]+A[0][1]*B[1][0], A[0][0]*B[0][1]+A[0][1]*B[1][1]],
                      [A[1][0]*B[0][0]+A[1][1]*B[1][0], A[1][0]*B[0][1]+A[1][1]*B[1][1]]]
def inv(A):
    d=A[0][0]*A[1][1]-A[0][1]*A[1][0]
    return [[A[1][1]/d,-A[0][1]/d],[-A[1][0]/d,A[0][0]/d]]
def tr(A): return A[0][0]+A[1][1]
def Jval(X,Y):
    C=mul(mul(X,Y),mul(inv(X),inv(Y)))
    return abs(tr(X)**2-4)+abs(tr(C)-2)
def nielsen(p):
    X,Y=p
    return [(Y,X),(inv(X),Y),(X,inv(Y)),(mul(X,Y),Y),(X,mul(X,Y)),
            (mul(X,inv(Y)),Y),(X,mul(inv(X),Y))]
def key(p):
    return tuple(round(z.real,7)+1j*round(z.imag,7) for M in p for r in M for z in r)
def Jbound(M, depth):
    G=M.fundamental_group(); g=G.generators()
    if len(g)!=2: return None,None
    P=(G.SL2C(g[0]), G.SL2C(g[1]))
    P=([[complex(v) for v in r] for r in P[0]],[[complex(v) for v in r] for r in P[1]])
    seen={key(P)}; frontier=[P]; best=Jval(*P); arg=P
    for d in range(depth):
        nxt=[]
        for p in frontier:
            for q in nielsen(p):
                k=key(q)
                if k in seen: continue
                seen.add(k)
                v=Jval(*q)
                if v<best: best, arg = v, q
                if len(seen)<40000: nxt.append(q)
        frontier=nxt
        if not frontier: break
    return best, len(seen)
DEPTH=int(sys.argv[2]) if len(sys.argv)>2 else 6
names=sys.argv[1].split(',')
print(f"Nielsen BFS depth={DEPTH}. Values are UPPER BOUNDS on J(Gamma), not infima.\n")
print(f"{'mfld':9s} {'J upper bound':>15s} {'pairs seen':>11s}   (theorem: m004 = 1)")
for nm in names:
    try:
        b,n=Jbound(snappy.Manifold(nm), DEPTH)
        print(f"{nm:9s} {b:15.9f} {n:11d}" if b is not None else f"{nm:9s}  (not 2-generator)")
    except Exception as e: print(f"{nm:9s} err {str(e)[:40]}")
