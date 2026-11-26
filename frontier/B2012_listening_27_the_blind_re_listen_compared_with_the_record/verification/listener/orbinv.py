# orbinv.py -- invariants of a finite orbit seen as a permutation representation of <L,R>:
#   S = L r L (order 2: (x,y,z)->(y,x,xy-z)), C = r L (order 3: (x,y,z)->(y,z,x)), L = S C^-1.
#   e2 = #fixed points of S, e3 = #fixed points of C, cusps = #cycles of L, widths = cycle lengths of L,
#   genus g = 1 + n/12 - e2/4 - e3/3 - cusps/2  (Riemann-Hurwitz for the cover of the (2,3,infinity) orbifold)
#   group order via GAP; congruence test: D = <(L,l),(R,r)> in G x SL(2,Z/N) with N = order of L;
#   the action is congruence of level N iff |D| = |SL(2,Z/N)|.
from fractions import Fraction as Fr
from collections import Counter
from math import gcd

def inv(pm):
    q = [0]*len(pm)
    for i, j in enumerate(pm): q[j] = i
    return q
def comp(a, b):  # a after b : i -> a[b[i]]
    return [a[j] for j in b]
def cycles(pm):
    n = len(pm); seen = [False]*n; out = []
    for i in range(n):
        if not seen[i]:
            l = 0; j = i
            while not seen[j]: seen[j] = True; j = pm[j]; l += 1
            out.append(l)
    return out
def lcm(a, b): return a*b//gcd(a, b)

def invariants(pL, pR):
    n = len(pL)
    pr = inv(pR)
    S = comp(pL, comp(pr, pL)); C = comp(pr, pL)
    e2 = sum(1 for i in range(n) if S[i] == i); e3 = sum(1 for i in range(n) if C[i] == i)
    w = cycles(pL); c = len(w)
    g = 1 + Fr(n, 12) - Fr(e2, 4) - Fr(e3, 3) - Fr(c, 2)
    N = 1
    for t in w: N = lcm(N, t)
    assert all(S[S[i]] == i for i in range(n)) and all(C[C[C[i]]] == i for i in range(n))
    return dict(n=n, e2=e2, e3=e3, cusps=c, widths=dict(sorted(Counter(w).items())), genus=g, level=N)

def gap_info(pL, pR, congruence=True, maxN=400):
    from sage.all import libgap
    n = len(pL)
    L = libgap.PermList([i+1 for i in pL]); R = libgap.PermList([i+1 for i in pR])
    G = libgap.Group([L, R])
    order = int(G.Size())
    res = dict(order=order)
    if n > 1:
        res['primitive'] = bool(G.IsPrimitive(libgap.eval("[1..%d]" % n)))
        an = bool(libgap.IsNaturalAlternatingGroup(G)); sy = bool(libgap.IsNaturalSymmetricGroup(G))
        res['natural'] = "Alt(%d)" % n if an else ("Sym(%d)" % n if sy else "")
        res['sign_L'] = int(libgap.SignPerm(L)); res['sign_R'] = int(libgap.SignPerm(R))
    if congruence:
        w = cycles(pL); N = 1
        for t in w: N = lcm(N, t)
        if N <= maxN:
            # SL(2,Z/N) acting on (Z/N)^2 as permutations, l = [[1,1],[0,1]], r = [[1,0],[1,1]] acting on column vectors;
            # the composition convention is fixed by matching: our word rL is C (order 3); we try both l,r and l,r transposed.
            vecs = [(a, b) for a in range(N) for b in range(N)]
            vi = {v: i for i, v in enumerate(vecs)}
            def mperm(M):
                return [vi[((M[0][0]*a + M[0][1]*b) % N, (M[1][0]*a + M[1][1]*b) % N)] for (a, b) in vecs]
            best = None
            for (ml, mr) in ((((1, 1), (0, 1)), ((1, 0), (1, 1))), (((1, 0), (1, 1)), ((1, 1), (0, 1)))):
                pl = mperm(ml); pr = mperm(mr)
                shift = n
                gl = libgap.PermList([i+1 for i in pL] + [shift + j + 1 for j in pl])
                gr = libgap.PermList([i+1 for i in pR] + [shift + j + 1 for j in pr])
                D = libgap.Group([gl, gr])
                H = libgap.Group([libgap.PermList([j+1 for j in pl]), libgap.PermList([j+1 for j in pr])])
                dsz = int(D.Size()); hsz = int(H.Size())
                ok = (dsz == hsz)
                if best is None or ok: best = (ok, dsz, hsz)
                if ok: break
            res['congruence'] = best[0]; res['|D|'] = best[1]; res['|SL(2,Z/N)| (as perms)'] = best[2]; res['N'] = N
        else:
            res['congruence'] = 'not tested (N=%d)' % N
    return res
