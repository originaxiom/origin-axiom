#!/usr/bin/env python3
"""(2b)+(3) OWN reproduction of the Standard-Model-frame index census on Y_4 = t12839 and on Y_2, Y_3, Y_5.
No T5 shortcut: the index of EVERY doublet module rho_chi (x) psi is computed, psi over the whole character
group Hom(H_1, mu_N).  Then the generation search.  Sector charges (6Y, 3gamma) as in the record's frame:
Q(1,3) u^c(-4,3) e^c(6,3) d^c(2,1) L(-3,1) nu^c(0,-5); sector character = psi_Y^{6Y} psi_gamma^{3gamma}."""
import sys, os, json, math, time, warnings
from collections import Counter, defaultdict
warnings.filterwarnings("ignore")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import numpy as np, snappy
from myindex import Mod, index, rank_and_null, eye

SECT = [("Q",1,3),("uc",-4,3),("ec",6,3),("dc",2,1),("L",-3,1),("nuc",0,-5)]

def primroot(p):
    n=p-1; f=[]; m=n; d=2
    while d*d<=m:
        if m%d==0:
            f.append(d)
            while m%d==0: m//=d
        d+=1
    if m>1: f.append(m)
    for g in range(2,p):
        if all(pow(g,n//q,p)!=1 for q in f): return g
def primes_1mod(N,k,start):
    out=[];q=start
    while len(out)<k:
        q+=1
        if q%N!=1: continue
        if all(q%d for d in range(2,int(q**.5)+1)): out.append(q)
    return out
def abvec(w,gens):
    v={g:0 for g in gens}
    for ch in w: v[ch.lower()] += 1 if ch.islower() else -1
    return [v[g] for g in gens]

def fox1(word, gens, val, p):
    D={g:0 for g in gens}; pre=1
    for ch in word:
        g=ch.lower()
        if ch.islower(): D[g]=(D[g]+pre)%p; pre=pre*val[g]%p
        else: pre=pre*pow(val[g],p-2,p)%p; D[g]=(D[g]-pre)%p
    return D

def build(n, N, p, prime_idx=0):
    Y = snappy.Manifold('m004').covers(n, cover_type='cyclic')[0]
    G = Y.fundamental_group(); gens=list(G.generators()); rels=list(G.relators())
    mu,lam = G.peripheral_curves()[0]
    A=[abvec(r,gens) for r in rels]
    g=len(gens)
    grids=np.meshgrid(*[np.arange(N,dtype=np.int64)]*g, indexing='ij')
    K=np.stack([x.ravel() for x in grids],axis=1); ok=np.ones(len(K),bool)
    for a in A: ok &= (K@np.array(a,dtype=np.int64))%N==0
    chars=[tuple(int(x) for x in r) for r in K[ok]]
    return Y,gens,rels,mu,lam,chars,A

def census(n, N, nprimes=3, pstart=1000, full=True):
    t0=time.time()
    P = primes_1mod(N,nprimes,pstart)
    Y,gens,rels,mu,lam,chars,A = build(n,N,P[0])
    H1=str(Y.homology()); ng=len(gens)
    zeta={p:pow(primroot(p),(p-1)//N,p) for p in P}
    cindex={c:i for i,c in enumerate(chars)}
    def mulc(a,b): return tuple((x+y)%N for x,y in zip(a,b))
    def powc(a,k): return tuple((k*x)%N for x in a)
    # loci: chi nontrivial with a non-coboundary cocycle for chi^2, per prime
    def loci_for(p):
        z=zeta[p]; out={}
        for c in chars:
            if all(x==0 for x in c): continue
            val={g:pow(z,2*c[i]%N,p) for i,g in enumerate(gens)}
            rows=[]
            for r in rels:
                D=fox1(r,gens,val,p); rows.append([D[g]%p for g in gens])
            rk,NS=rank_and_null(rows,ng,p,want_null=True)
            b=[(val[g]-1)%p for g in gens]; rb=1 if any(b) else 0
            h1=len(NS)-rb
            if h1<=0: continue
            ct=None
            for zz in NS:
                if rb==0: ct=zz; break
                rk2,_=rank_and_null([b,zz],ng,p)
                if rk2==2: ct=zz; break
            if ct is None: continue
            out[c]=(h1,dict(zip(gens,ct)))
        return out
    L={p:loci_for(p) for p in P}
    loci=sorted(set.intersection(*[set(L[p]) for p in P]))
    h1mult=dict(Counter(L[P[0]][c][0] for c in loci))
    # index table per locus over the FIRST prime, all psi
    fire={}; sig=Counter(); nmod=0
    for j,c in enumerate(loci):
        p=P[0]; z=zeta[p]; h1,ct=L[p][c]
        cv={g:pow(z,c[i]%N,p) for i,g in enumerate(gens)}
        rho={g:[[cv[g], ct[g]*pow(cv[g],p-2,p)%p],[0,pow(cv[g],p-2,p)]] for g in gens}
        S={}
        for psi in chars:
            pv={g:pow(z,psi[i]%N,p) for i,g in enumerate(gens)}
            mats={g:[[pv[g]*rho[g][0][0]%p, pv[g]*rho[g][0][1]%p],[0, pv[g]*rho[g][1][1]%p]] for g in gens}
            V=Mod(gens,mats,p)
            if not V.ok(rels): raise SystemExit("not a representation at locus %s" % (c,))
            I,dV,dVs = index(V,rels,mu,lam)
            nmod+=1
            if I!=0: S[psi]=(I,dV,dVs); sig[(dV,dVs)]+=1
        fire[j]=S
    nfire=sum(len(s) for s in fire.values())
    # recheck every non-zero over the other primes
    diff=0; rech=0
    for q in P[1:]:
        if q not in L or not all(c in L[q] for c in loci): 
            pass
        z=zeta[q]
        for j,c in enumerate(loci):
            if c not in L[q]: diff+=len(fire[j]); continue
            h1,ct=L[q][c]
            cv={g:pow(z,c[i]%N,q) for i,g in enumerate(gens)}
            rho={g:[[cv[g], ct[g]*pow(cv[g],q-2,q)%q],[0,pow(cv[g],q-2,q)]] for g in gens}
            for psi,(I,dV,dVs) in fire[j].items():
                pv={g:pow(z,psi[i]%N,q) for i,g in enumerate(gens)}
                mats={g:[[pv[g]*rho[g][0][0]%q, pv[g]*rho[g][0][1]%q],[0, pv[g]*rho[g][1][1]%q]] for g in gens}
                I2,d2,d2s=index(Mod(gens,mats,q),rels,mu,lam); rech+=1
                if I2!=I: diff+=1
    # generation search
    def fifth_roots(w):
        return [y for y in chars if powc(y,5)==w]
    fifth_cache={}
    backgrounds=[]; signs=Counter(); nuc=Counter(); loci_used=set(); absI=Counter()
    for j,S in fire.items():
        if not S: continue
        for u,(Iu,_,_) in S.items():
            for v,(Iv,_,_) in S.items():
                if Iu!=Iv: continue
                w=mulc(u,powc(v,-1))
                if w not in fifth_cache: fifth_cache[w]=fifth_roots(w)
                for pY in fifth_cache[w]:
                    pG=mulc(u,powc(pY,-2))
                    cnt=[]
                    for (lab,sy,sg) in SECT:
                        sec=mulc(powc(pY,sy),powc(pG,sg))
                        cnt.append(S[sec][0] if sec in S else 0)
                    if cnt[0]==cnt[1]==cnt[2]==cnt[3]==cnt[4]!=0:
                        backgrounds.append((j,pY,pG,tuple(cnt)))
                        signs[cnt[0]]+=1; absI[abs(cnt[0])]+=1; nuc[cnt[5]]+=1; loci_used.add(j)
    uniq=sorted(set((j,a,b) for (j,a,b,c) in backgrounds))
    am=abvec(mu,gens); al=abvec(lam,gens)
    cuspexp=Counter((sum(x*y for x,y in zip(am,c))%N, sum(x*y for x,y in zip(al,c))%N) for c in loci)
    out=dict(n=n,N=N,H1=H1,gens=gens,rels=rels,mu=mu,lam=lam,primes=P,n_chars=len(chars),
             loci=len(loci),h1_multiset=h1mult,modules_computed=nmod,firing=nfire,
             rechecked=rech,differing=diff,
             firing_signatures={str(k):v for k,v in sig.items()},
             generation_backgrounds=len(uniq), loci_carrying=len(loci_used),
             signs=dict(signs), abs_counts=dict(absI), nuc=dict(nuc),
             cusp_exponents={str(k):v for k,v in sorted(cuspexp.items())},
             seconds=round(time.time()-t0,1))
    return out, backgrounds, loci, fire

if __name__=='__main__':
    jobs=eval(sys.argv[1])
    allout={}
    for (n,N) in jobs:
        o,bg,loci,fire=census(n,N)
        allout[f"Y{n}"]=o
        print(json.dumps(o,indent=1),flush=True)
    json.dump(allout,open('<here>/v5_census_%s.json'%'_'.join(str(n) for n,_ in jobs),'w'),indent=1)
