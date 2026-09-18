#!/usr/bin/env python3
"""EXACT (characteristic zero) re-derivation of the index on Y_4 generation backgrounds, over Q(zeta_60),
with my own cyclotomic arithmetic -- no prime fields anywhere.  Same definitions as myindex.py."""
import sys, os, json, math, warnings, time, random
from fractions import Fraction
from collections import Counter
warnings.filterwarnings("ignore")
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
import numpy as np, snappy
from cyclo import Cyc
from v2_loci import abvec

def rref_cyc(F, rows, ncols, want_null=False):
    R=[list(r) for r in rows]; piv=[]; rk=0
    for c in range(ncols):
        k=None
        for i in range(rk,len(R)):
            if not F.is_zero(R[i][c]): k=i; break
        if k is None: continue
        R[rk],R[k]=R[k],R[rk]
        iv=F.inv(R[rk][c]); R[rk]=[F.mul(iv,x) for x in R[rk]]
        for i in range(len(R)):
            if i!=rk and not F.is_zero(R[i][c]):
                f=R[i][c]; R[i]=[F.sub(x,F.mul(f,y)) for x,y in zip(R[i],R[rk])]
        piv.append(c); rk+=1
    if not want_null: return rk,None
    free=[c for c in range(ncols) if c not in piv]; NS=[]
    for fc in free:
        v=[F.zero()]*ncols; v[fc]=F.one()
        for i,pc in enumerate(piv): v[pc]=F.neg(R[i][fc])
        NS.append(v)
    return rk,NS

class M2:
    """2x2 (or dxd) matrices over F"""
    def __init__(s,F): s.F=F
    def eye(s,n): return [[s.F.one() if i==j else s.F.zero() for j in range(n)] for i in range(n)]
    def mul(s,A,B):
        F=s.F; n,k,m=len(A),len(B),len(B[0])
        return [[ (lambda acc: acc)(_sum(F,[F.mul(A[i][l],B[l][j]) for l in range(k)])) for j in range(m)] for i in range(n)]
    def sub(s,A,B): return [[s.F.sub(x,y) for x,y in zip(r,t)] for r,t in zip(A,B)]
    def add(s,A,B): return [[s.F.add(x,y) for x,y in zip(r,t)] for r,t in zip(A,B)]
    def inv(s,A):
        F=s.F; n=len(A)
        aug=[list(A[i])+[F.one() if i==j else F.zero() for j in range(n)] for i in range(n)]
        R=[list(r) for r in aug]; rk=0
        for c in range(n):
            k=None
            for i in range(rk,n):
                if not F.is_zero(R[i][c]): k=i; break
            assert k is not None,"singular"
            R[rk],R[k]=R[k],R[rk]
            iv=F.inv(R[rk][c]); R[rk]=[F.mul(iv,x) for x in R[rk]]
            for i in range(n):
                if i!=rk and not F.is_zero(R[i][c]):
                    f=R[i][c]; R[i]=[F.sub(x,F.mul(f,y)) for x,y in zip(R[i],R[rk])]
            rk+=1
        return [r[n:] for r in R]
    def T(s,A): return [list(r) for r in zip(*A)]
def _sum(F,l):
    a=F.zero()
    for x in l: a=F.add(a,x)
    return a

class ModX:
    def __init__(s,F,gens,mats):
        s.F=F; s.A=M2(F); s.gens=list(gens); s.d=len(mats[gens[0]]); s.M=dict(mats)
        for g in gens: s.M[g.upper()]=s.A.inv(mats[g])
    def word(s,w):
        R=s.A.eye(s.d)
        for ch in w: R=s.A.mul(R,s.M[ch])
        return R
    def fox(s,w):
        F=s.F; d=s.d; D={g:[[F.zero()]*d for _ in range(d)] for g in s.gens}; pre=s.A.eye(d)
        for ch in w:
            g=ch.lower()
            if ch.islower(): D[g]=s.A.add(D[g],pre); pre=s.A.mul(pre,s.M[ch])
            else: pre=s.A.mul(pre,s.M[ch]); D[g]=s.A.sub(D[g],pre)
        return D
    def dual(s): return ModX(s.F,s.gens,{g:s.A.T(s.A.inv(s.M[g])) for g in s.gens})

def cohom(V,rels,mu,lam):
    F=V.F; d=V.d; gens=V.gens; I=V.A.eye(d)
    D0=[row for g in gens for row in V.A.sub(V.M[g],I)]
    rk0,_=rref_cyc(F,D0,d); a0=d-rk0
    J=[]
    for r in rels:
        Fx=V.fox(r)
        for i in range(d): J.append([Fx[g][i][j] for g in gens for j in range(d)])
    rkJ,Z1=rref_cyc(F,J,len(gens)*d,want_null=True)
    a1=(len(gens)*d-rkJ)-rk0
    Am=V.A.sub(V.word(mu),I); Al=V.A.sub(V.word(lam),I)
    BT=[list(Am[i]) for i in range(d)]+[list(Al[i]) for i in range(d)]
    rkBT,_=rref_cyc(F,BT,d); t0=d-rkBT
    ZT=[[F.neg(Al[i][j]) for j in range(d)]+[Am[i][j] for j in range(d)] for i in range(d)]
    rkZT,_=rref_cyc(F,ZT,2*d); t1=(2*d-rkZT)-rkBT
    Dm=V.fox(mu); Dl=V.fox(lam)
    Res=[[Dm[g][i][j] for g in gens for j in range(d)] for i in range(d)]+[[Dl[g][i][j] for g in gens for j in range(d)] for i in range(d)]
    cols=[[_sum(F,[F.mul(Res[i][k],z[k]) for k in range(len(z))]) for i in range(2*d)] for z in Z1]
    BTc=[[BT[i][j] for i in range(2*d)] for j in range(d)]
    rk_all,_=rref_cyc(F,cols+BTc,2*d); rkB,_=rref_cyc(F,BTc,2*d)
    return a0,a1,t0,t1,rk_all-rkB

def index(V,rels,mu,lam):
    a0,a1,t0,t1,r1=cohom(V,rels,mu,lam)
    b0,b1,s0,s1,q1=cohom(V.dual(),rels,mu,lam)
    I=(a1-r1)-(b1-q1)
    assert r1+q1==t1==s1,("annihilator",r1,q1,t1,s1)
    assert I==(a0-b0)+s0-r1,("identity",I,a0,b0,s0,r1)
    return I,(a0,a1,t0,r1),(b0,b1,s0,q1)

SECT=[("Q",1,3),("uc",-4,3),("ec",6,3),("dc",2,1),("L",-3,1),("nuc",0,-5)]
if __name__=='__main__':
    N=60; F=Cyc(N)
    Y=snappy.Manifold('m004').covers(4,cover_type='cyclic')[0]
    G=Y.fundamental_group(); gens=list(G.generators()); rels=list(G.relators()); mu,lam=G.peripheral_curves()[0]
    bgs=json.load(open('<here>/Y4_backgrounds.json'))
    random.seed(7); pick=random.sample(bgs,min(3,len(bgs)))
    res=[]
    for (chi,pY,pG,cnt) in pick:
        t=time.time()
        chi=tuple(chi); pY=tuple(pY); pG=tuple(pG)
        # exact h^1(chi^2) and a non-coboundary cocycle
        val={g:F.zeta(2*chi[i]) for i,g in enumerate(gens)}
        rows=[]
        for r in rels:
            D={g:F.zero() for g in gens}; pre=F.one()
            for ch in r:
                g=ch.lower()
                if ch.islower(): D[g]=F.add(D[g],pre); pre=F.mul(pre,val[g])
                else: pre=F.mul(pre,F.inv(val[g])); D[g]=F.sub(D[g],pre)
            rows.append([D[g] for g in gens])
        rk,NS=rref_cyc(F,rows,len(gens),want_null=True)
        b=[F.sub(val[g],F.one()) for g in gens]; rb=0 if all(F.is_zero(x) for x in b) else 1
        h1=len(NS)-rb
        ct=None
        for z in NS:
            if rb==0: ct=z; break
            r2,_=rref_cyc(F,[b,z],len(gens))
            if r2==2: ct=z; break
        ctd=dict(zip(gens,ct))
        cv={g:F.zeta(chi[i]) for i,g in enumerate(gens)}
        rho={g:[[cv[g],F.mul(ctd[g],F.inv(cv[g]))],[F.zero(),F.inv(cv[g])]] for g in gens}
        counts={}
        for (lab,sy,sg) in SECT:
            sec=tuple((sy*pY[i]+sg*pG[i])%N for i in range(len(gens)))
            pv={g:F.zeta(sec[i]) for i,g in enumerate(gens)}
            mats={g:[[F.mul(pv[g],rho[g][0][0]),F.mul(pv[g],rho[g][0][1])],[F.zero(),F.mul(pv[g],rho[g][1][1])]] for g in gens}
            V=ModX(F,gens,mats)
            E=V.A.eye(2)
            assert all(V.word(r)==E for r in rels), "not a representation"
            I,dV,dVs=index(V,rels,mu,lam)
            counts[lab]=(I,dV,dVs)
        res.append(dict(chi=list(chi),psi_Y=list(pY),psi_gamma=list(pG),h1_chi2_exact=h1,
                        counts={k:v[0] for k,v in counts.items()},
                        dims={k:[list(v[1]),list(v[2])] for k,v in counts.items()},
                        prime_field_counts=list(cnt), seconds=round(time.time()-t,1)))
        print(json.dumps(res[-1]),flush=True)
    json.dump(res,open('<here>/v9_exact_index.json','w'),indent=1)
