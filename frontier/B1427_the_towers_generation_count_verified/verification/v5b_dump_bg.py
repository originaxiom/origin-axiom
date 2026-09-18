"""Re-derive Y_4's firing set and generation backgrounds using the PROVED cusp filter
(t_0(V) != 0 requires rho_V(mu) and rho_V(lam) to have eigenvalue 1, i.e. psi(mu) = chi(mu)^{-+1} on both
curves), and dump the backgrounds.  Cross-check: the firing count must equal the 976 of the full scan."""
import sys,json,math,warnings
warnings.filterwarnings("ignore")
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
import numpy as np, snappy
from myindex import Mod, index, rank_and_null
from v5_census import primroot, primes_1mod, abvec, fox1, SECT
N=60; P=primes_1mod(N,3,1000); p=P[0]
Y=snappy.Manifold('m004').covers(4,cover_type='cyclic')[0]
G=Y.fundamental_group(); gens=list(G.generators()); rels=list(G.relators()); mu,lam=G.peripheral_curves()[0]
A=[abvec(r,gens) for r in rels]; g=len(gens)
grids=np.meshgrid(*[np.arange(N,dtype=np.int64)]*g,indexing='ij')
K=np.stack([x.ravel() for x in grids],axis=1); ok=np.ones(len(K),bool)
for a in A: ok &= (K@np.array(a,dtype=np.int64))%N==0
chars=[tuple(int(x) for x in r) for r in K[ok]]
z=pow(primroot(p),(p-1)//N,p)
am=abvec(mu,gens); al=abvec(lam,gens)
def ev(c,v): return sum(x*y for x,y in zip(v,c))%N
loci=[]
for c in chars:
    if all(x==0 for x in c): continue
    val={gg:pow(z,2*c[i]%N,p) for i,gg in enumerate(gens)}
    rows=[]
    for r in rels:
        D=fox1(r,gens,val,p); rows.append([D[gg]%p for gg in gens])
    rk,NS=rank_and_null(rows,g,p,want_null=True)
    b=[(val[gg]-1)%p for gg in gens]; rb=1 if any(b) else 0
    if len(NS)-rb<=0: continue
    ct=None
    for zz in NS:
        if rb==0: ct=zz; break
        r2,_=rank_and_null([b,zz],g,p)
        if r2==2: ct=zz; break
    if ct: loci.append((c,dict(zip(gens,ct))))
print("loci",len(loci))
def mulc(a,b): return tuple((x+y)%N for x,y in zip(a,b))
def powc(a,k): return tuple((k*x)%N for x in a)
bylam={}
for i,ps in enumerate(chars): bylam.setdefault((ev(ps,am),ev(ps,al)),[]).append(ps)
allbg=[]; nf=0; ncand=0; sigs={}
for (c,ct) in loci:
    cv={gg:pow(z,c[i]%N,p) for i,gg in enumerate(gens)}
    rho={gg:[[cv[gg],ct[gg]*pow(cv[gg],p-2,p)%p],[0,pow(cv[gg],p-2,p)]] for gg in gens}
    km,kl=ev(c,am),ev(c,al)
    cand=set(bylam.get(((-km)%N,(-kl)%N),[]))|set(bylam.get((km,kl),[]))
    ncand+=len(cand); S={}
    for ps in cand:
        pv={gg:pow(z,ps[i]%N,p) for i,gg in enumerate(gens)}
        mats={gg:[[pv[gg]*rho[gg][0][0]%p,pv[gg]*rho[gg][0][1]%p],[0,pv[gg]*rho[gg][1][1]%p]] for gg in gens}
        I,dV,dVs=index(Mod(gens,mats,p),rels,mu,lam)
        if I!=0: S[ps]=I; sigs[(dV,dVs)]=sigs.get((dV,dVs),0)+1
    nf+=len(S)
    for u,Iu in S.items():
        for v,Iv in S.items():
            if Iu!=Iv: continue
            w=mulc(u,powc(v,-1))
            for pY in [y for y in chars if powc(y,5)==w]:
                pG=mulc(u,powc(pY,-2)); cnt=[]
                for (lab,sy,sg) in SECT:
                    sec=mulc(powc(pY,sy),powc(pG,sg)); cnt.append(S.get(sec,0))
                if cnt[0]==cnt[1]==cnt[2]==cnt[3]==cnt[4]!=0:
                    allbg.append((list(c),list(pY),list(pG),cnt))
uniq={}
for b in allbg: uniq[(tuple(b[0]),tuple(b[1]),tuple(b[2]))]=b
print("T5 candidates",ncand,"firing",nf,"backgrounds",len(uniq),"signatures",{str(k):v for k,v in sigs.items()})
json.dump(list(uniq.values()),open('<here>/Y4_backgrounds.json','w'))
