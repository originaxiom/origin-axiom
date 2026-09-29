#!/usr/bin/env python3
"""VACUITY GUARD for the index: does MY index code ever return |I| >= 2?
Scan t12835 (a sibling where the record/B1418 reports I = +-2) over Sym^m(rho_chi) (x) psi, m = 0,1,2,
every non-split locus at N = 12, every psi in Hom(H_1, mu_12)."""
import sys, json, math, warnings
from collections import Counter
warnings.filterwarnings("ignore")
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
import numpy as np, snappy
from myindex import Mod, index, rank_and_null
from v5_census import primroot, primes_1mod, abvec, fox1

def sym(A,m,p):
    """Sym^m of a 2x2 A on the basis x^{m-j} y^j; A x = a x + c y, A y = b x + d y (columns of A)"""
    a,b=A[0]; c,d=A[1]
    def lin(al,be,k): return [math.comb(k,i)*pow(al,k-i,p)*pow(be,i,p)%p for i in range(k+1)]
    def pm(u,v):
        o=[0]*(len(u)+len(v)-1)
        for i,x in enumerate(u):
            for j,y in enumerate(v): o[i+j]=(o[i+j]+x*y)%p
        return o
    cols=[pm(lin(a,c,m-j),lin(b,d,j)) for j in range(m+1)]
    return [[cols[j][i] for j in range(m+1)] for i in range(m+1)]

name=sys.argv[1] if len(sys.argv)>1 else 't12835'
N=int(sys.argv[2]) if len(sys.argv)>2 else 12
M=snappy.Manifold(name); G=M.fundamental_group()
gens=list(G.generators()); rels=list(G.relators()); mu,lam=G.peripheral_curves()[0]
A=[abvec(r,gens) for r in rels]; g=len(gens)
P=primes_1mod(N,3,1000); p=P[0]; z=pow(primroot(p),(p-1)//N,p)
grids=np.meshgrid(*[np.arange(N,dtype=np.int64)]*g,indexing='ij')
K=np.stack([x.ravel() for x in grids],axis=1); ok=np.ones(len(K),bool)
for a in A: ok &= (K@np.array(a,dtype=np.int64))%N==0
chars=[tuple(int(x) for x in r) for r in K[ok]]
loci=[]
for c in chars:
    if all(x==0 for x in c): continue
    val={gg:pow(z,2*c[i]%N,p) for i,gg in enumerate(gens)}
    rows=[[fox1(r,gens,val,p)[gg]%p for gg in gens] for r in rels]
    rk,NS=rank_and_null(rows,g,p,want_null=True)
    b=[(val[gg]-1)%p for gg in gens]; rb=1 if any(b) else 0
    h1=len(NS)-rb
    if h1<=0: continue
    ct=None
    for zz in NS:
        if rb==0: ct=zz; break
        r2,_=rank_and_null([b,zz],g,p)
        if r2==2: ct=zz; break
    if ct: loci.append((c,dict(zip(gens,ct)),h1))
res={}
for m in (3,4,5,6):
    dist=Counter(); ex=[]
    for (c,ct,h1) in loci:
        cv={gg:pow(z,c[i]%N,p) for i,gg in enumerate(gens)}
        rho={gg:[[cv[gg],ct[gg]*pow(cv[gg],p-2,p)%p],[0,pow(cv[gg],p-2,p)]] for gg in gens}
        S={gg:sym(rho[gg],m,p) for gg in gens}
        for ps in chars:
            pv={gg:pow(z,ps[i]%N,p) for i,gg in enumerate(gens)}
            mats={gg:[[pv[gg]*x%p for x in row] for row in S[gg]] for gg in gens}
            V=Mod(gens,mats,p)
            if not V.ok(rels): raise SystemExit("bad rep")
            I,dV,dVs=index(V,rels,mu,lam); dist[I]+=1
            if abs(I)>=2 and len(ex)<4: ex.append(dict(chi=list(c),psi=list(ps),I=I,V=list(dV),Vstar=list(dVs)))
    res[m]=dict(I_distribution={str(k):v for k,v in sorted(dist.items())}, examples_absI_ge_2=ex)
    print(name,"m=",m,json.dumps(res[m])[:600],flush=True)
print("loci",len(loci),"h1 multiset",dict(Counter(h for _,_,h in loci)))
json.dump(dict(manifold=name,N=N,loci=len(loci),h1_multiset=dict(Counter(h for _,_,h in loci)),per_m=res),
          open('<here>/v10_index_vacuity_%s.json'%name,'w'),indent=1)
