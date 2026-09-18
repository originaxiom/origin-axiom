"""Firing + generation census on any level, using the PROVED cusp filter:
t_0(V) != 0 requires rho_V(mu) and rho_V(lam) to have eigenvalue 1, and rho_V(x) = psi(x) rho_chi(x) has
eigenvalues psi(x) chi(x)^{+-1}; so psi = chi^{-1} or chi on both peripheral curves.  (On Y_2, Y_3, Y_4 this
filter was checked against the unrestricted scan of every psi and gave the identical firing count.)"""
import sys,json,math,warnings,time
warnings.filterwarnings("ignore")
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
import numpy as np, snappy
from myindex import Mod, index, rank_and_null
from v5_census import primroot, primes_1mod, abvec, fox1, SECT
from collections import Counter

def run(n,N,dump=None):
    t0=time.time(); P=primes_1mod(N,3,1000)
    Y=snappy.Manifold('m004').covers(n,cover_type='cyclic')[0]
    G=Y.fundamental_group(); gens=list(G.generators()); rels=list(G.relators()); mu,lam=G.peripheral_curves()[0]
    A=[abvec(r,gens) for r in rels]; g=len(gens)
    fg=[j for j in range(g) if all(a[j]==0 for a in A)]
    base=[]
    for ka in range(N):
        for kc in range(N):
            k=[0]*g; oth=[j for j in range(g) if j!=fg[0]]; k[oth[0]]=ka; k[oth[1]]=kc
            if all(sum(a[j]*k[j] for j in range(g))%N==0 for a in A): base.append(tuple(k))
    chars=[tuple(b[j]+(kb if j==fg[0] else 0) for j in range(g)) for b in base for kb in range(N)]
    am=abvec(mu,gens); al=abvec(lam,gens)
    def ev(c,v): return sum(x*y for x,y in zip(v,c))%N
    def mulc(a,b): return tuple((x+y)%N for x,y in zip(a,b))
    def powc(a,k): return tuple((k*x)%N for x in a)
    fifth={}
    for y in chars: fifth.setdefault(powc(y,5),[]).append(y)
    out={}
    for pi,p in enumerate(P):
        z=pow(primroot(p),(p-1)//N,p); loci=[]
        for c in chars:
            if all(x==0 for x in c): continue
            val={gg:pow(z,2*c[i]%N,p) for i,gg in enumerate(gens)}
            rows=[[fox1(r,gens,val,p)[gg]%p for gg in gens] for r in rels]
            rk,NS=rank_and_null(rows,g,p,want_null=True)
            b=[(val[gg]-1)%p for gg in gens]; rb=1 if any(b) else 0
            if len(NS)-rb<=0: continue
            ct=None
            for zz in NS:
                if rb==0: ct=zz; break
                r2,_=rank_and_null([b,zz],g,p)
                if r2==2: ct=zz; break
            if ct: loci.append((c,dict(zip(gens,ct)),len(NS)-rb))
        out[p]=loci
        if pi==0:
            bylam={}
            for ps in chars: bylam.setdefault((ev(ps,am),ev(ps,al)),[]).append(ps)
    common=set(c for c,_,_ in out[P[0]])
    for p in P[1:]: common &= set(c for c,_,_ in out[p])
    h1mult=dict(Counter(h for c,_,h in out[P[0]] if c in common))
    p=P[0]; z=pow(primroot(p),(p-1)//N,p)
    firing={}; ncand=0; sigs=Counter(); allbg=[]
    for (c,ct,h) in out[p]:
        if c not in common: continue
        cv={gg:pow(z,c[i]%N,p) for i,gg in enumerate(gens)}
        rho={gg:[[cv[gg],ct[gg]*pow(cv[gg],p-2,p)%p],[0,pow(cv[gg],p-2,p)]] for gg in gens}
        km,kl=ev(c,am),ev(c,al)
        cand=set(bylam.get(((-km)%N,(-kl)%N),[]))|set(bylam.get((km,kl),[])); ncand+=len(cand)
        S={}
        for ps in cand:
            pv={gg:pow(z,ps[i]%N,p) for i,gg in enumerate(gens)}
            mats={gg:[[pv[gg]*rho[gg][0][0]%p,pv[gg]*rho[gg][0][1]%p],[0,pv[gg]*rho[gg][1][1]%p]] for gg in gens}
            I,dV,dVs=index(Mod(gens,mats,p),rels,mu,lam)
            if I!=0: S[ps]=I; sigs[(dV,dVs)]+=1
        firing[c]=S
        for u,Iu in S.items():
            for v,Iv in S.items():
                if Iu!=Iv: continue
                w=mulc(u,powc(v,-1))
                for pY in fifth.get(w,[]):
                    pG=mulc(u,powc(pY,-2))
                    cnt=[S.get(mulc(powc(pY,sy),powc(pG,sg)),0) for (lab,sy,sg) in SECT]
                    if cnt[0]==cnt[1]==cnt[2]==cnt[3]==cnt[4]!=0: allbg.append((list(c),list(pY),list(pG),cnt))
    uniq={(tuple(b[0]),tuple(b[1]),tuple(b[2])):b for b in allbg}
    # recheck every firing module over the other two primes
    diff=0;rech=0
    for q in P[1:]:
        zq=pow(primroot(q),(q-1)//N,q); lq={c:ct for c,ct,_ in out[q]}
        for c,S in firing.items():
            ct=lq[c]; cv={gg:pow(zq,c[i]%N,q) for i,gg in enumerate(gens)}
            rho={gg:[[cv[gg],ct[gg]*pow(cv[gg],q-2,q)%q],[0,pow(cv[gg],q-2,q)]] for gg in gens}
            for ps,I in S.items():
                pv={gg:pow(zq,ps[i]%N,q) for i,gg in enumerate(gens)}
                mats={gg:[[pv[gg]*rho[gg][0][0]%q,pv[gg]*rho[gg][0][1]%q],[0,pv[gg]*rho[gg][1][1]%q]] for gg in gens}
                I2,_,_=index(Mod(gens,mats,q),rels,mu,lam); rech+=1
                if I2!=I: diff+=1
    r=dict(n=n,N=N,H1=str(Y.homology()),primes=P,n_chars=len(chars),loci=len(common),h1_multiset=h1mult,
           T5_candidates=ncand,firing=sum(len(s) for s in firing.values()),rechecked=rech,differing=diff,
           firing_signatures={str(k):v for k,v in sigs.items()},
           generation_backgrounds=len(uniq),loci_carrying=len(set(tuple(b[0]) for b in allbg)),
           signs=dict(Counter(b[3][0] for b in uniq.values())),
           abs_counts=dict(Counter(abs(b[3][0]) for b in uniq.values())),
           nuc=dict(Counter(b[3][5] for b in uniq.values())),seconds=round(time.time()-t0,1))
    if dump: json.dump(list(uniq.values()),open(dump,'w'))
    return r
if __name__=='__main__':
    res={}
    for a in sys.argv[1:]:
        n,N=[int(x) for x in a.split(',')]
        r=run(n,N); res[n]=r; print(json.dumps(r),flush=True)
    json.dump(res,open('<here>/v5c_levels.json','w'),indent=1)
