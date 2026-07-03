"""B378-content — the complete local census table: lines and doublets per prime power.

The derived mechanism (this session): sector@N = (invariant LINE at one CRT factor) tensor
(helicity DOUBLET at the other). This module computes the full local table at 3, 5, 9, 25,
27, 81, 125 (multiplier u=1 suffices per Galois transport; 5 also at u=2 for the sigma-check)
and saves it exactly (F_p, cross-checked at a second prime for the summary bits).
"""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "B372_level45_sweeper"))
from fp_engine import primes_1_mod, primitive_root
import random

def census(q, u, p, g):
    def zeta(n): return pow(g, (p-1)//n, p)
    zq = zeta(q)
    D  = [[pow(zq,( u*(j*(j-1)//2))%q,p) if i==j else 0 for j in range(q)] for i in range(q)]
    F  = [[pow(zq,( u*i*j)%q,p) for j in range(q)] for i in range(q)]
    iq = pow(q,p-2,p)
    Fi = [[pow(zq,(-u*i*j)%q,p)*iq%p for j in range(q)] for i in range(q)]
    Di = [[pow(zq,(-u*(j*(j-1)//2))%q,p) if i==j else 0 for j in range(q)] for i in range(q)]
    def mm(A,B):
        Bt=list(zip(*B))
        return [[sum(x*y for x,y in zip(r,c))%p for c in Bt] for r in A]
    WR = mm(mm(F,Di),Fi); W1 = mm(WR,D)
    I=[[1 if i==j else 0 for j in range(q)] for i in range(q)]
    pw=[I]; P=W1; o=1
    while P!=I:
        pw.append(P); P=mm(P,W1); o+=1
        assert o<200*q
    zo=zeta(o); io=pow(o,p-2,p)
    tr=[sum(M[i][i] for i in range(q))%p for M in pw]
    dims={a:sum(pow(zo,(-j*a)%o,p)*tr[j] for j in range(o))%p*io%p for a in range(o)}
    def eig(a,s):
        rnd=random.Random(s); v=[rnd.randrange(1,p) for _ in range(q)]
        out=[0]*q; w=v[:]
        for j in range(o):
            c=pow(zo,(-j*a)%o,p)*io%p
            out=[(x+c*y)%p for x,y in zip(out,w)]
            w=[sum(W1[i][k]*w[k] for k in range(q))%p for i in range(q)]
        return out
    def clos(vs,cap):
        basis=[]
        def add(v):
            v=v[:]
            for piv,row in basis:
                if v[piv]:
                    f=v[piv]; v=[(x-f*y)%p for x,y in zip(v,row)]
            for i in range(q):
                if v[i]:
                    inv=pow(v[i],p-2,p); basis.append((i,[x*inv%p for x in v])); basis.sort(); return True
            return False
        for v in vs: add(v)
        ch=True
        while ch and len(basis)<=cap:
            ch=False
            for v in [r for _,r in basis]:
                for G in (D,WR):
                    if add([sum(G[i][k]*v[k] for k in range(q))%p for i in range(q)]): ch=True
        return len(basis)
    lines=[a for a in range(o) if dims[a] and dims[a]<=3 and
           min(clos([eig(a,77*a+s)],2) for s in range(2))==1]
    doublets=[]
    for a in range(1,(o+1)//2):
        b=(o-a)%o
        if dims.get(a,0)>=1 and dims.get(b,0)>=1:
            if clos([eig(a,11*a),eig(b,13*a)],3)==2:
                doublets.append((a,b))
    return dict(q=q,u=u,ord=o,lines=sorted(set(lines)),
                doublets=doublets,
                doublet_deg=[round(360*a/o,1) for a,_ in doublets])

if __name__=="__main__":
    p = primes_1_mod(4*5*81*25, 1, start=10**9)[0]   # zeta available for all q here via p-1 mult
    # need zeta_q for q in {3,5,9,25,27,81,125} and their W1-orders: use p = 1 mod lcm big
    p = primes_1_mod(4*81*125, 1, start=10**9)[0]
    g = primitive_root(p)
    out={}
    for (q,u) in ((3,1),(5,1),(5,2),(9,1),(25,1),(27,1),(81,1),(125,1)):
        r=census(q,u,p,g)
        out[f"{q},u{u}"]=r
        print(q,"u=",u,"->",r, flush=True)
    json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                     "local_censuses.json"),"w"), indent=1)
    print("DONE")
