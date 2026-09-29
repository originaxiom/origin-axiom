#!/usr/bin/env python3
"""VACUITY GUARD: show that the quantity h^1(pi;psi) computed by this code CAN take values other than 1,
and search the tower (higher cyclic covers, and the non-cyclic covers of m004) for a locus with h^1(chi^2) >= 2."""
import sys, os, json, math, warnings
from collections import Counter
warnings.filterwarnings("ignore")
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
import numpy as np, snappy
from v2_loci import h1_gf, h1_exact, primes_1_mod, primitive_root, abvec

def scan(M, N, label, nprimes=3, pstart=1000, cap=4_000_000):
    G=M.fundamental_group(); gens=list(G.generators()); rels=list(G.relators())
    A=[abvec(r,gens) for r in rels]; g=len(gens)
    if N**g > cap: return dict(label=label, skipped="N^g too big", N=N, gens=g)
    P=primes_1_mod(N,nprimes,pstart); zet={p:pow(primitive_root(p),(p-1)//N,p) for p in P}
    grids=np.meshgrid(*[np.arange(N,dtype=np.int64)]*g, indexing='ij')
    K=np.stack([x.ravel() for x in grids],axis=1); ok=np.ones(len(K),bool)
    for a in A: ok &= (K@np.array(a,dtype=np.int64))%N==0
    chars=[tuple(int(x) for x in r) for r in K[ok]]
    cache={}; vals=Counter(); best=[]
    for k in chars:
        tw=[2*x%N for x in k]; d=N
        for x in tw: d=math.gcd(d,x)
        m=N//d; ee=tuple((x//d)%m for x in tw) if m>1 else tuple(0 for _ in tw)
        key=(m,ee)
        if key not in cache:
            e=dict(zip(gens,ee))
            hs=[h1_gf(gens,rels,e,max(m,1),p,pow(zet[p],N//m,p) if m>1 else 1) for p in P]
            h=min(hs)                     # GF(p) can only overestimate; the min over primes is the tightest bound
            if h>=1:
                h=h1_exact(gens,rels,e,max(m,1))
            cache[key]=h
        h=cache[key]
        if all(x==0 for x in k): continue      # chi trivial excluded
        vals[h]+=1
        if h>=2: best.append((k,h))
    return dict(label=label, H1=str(M.homology()), gens=g, rels=len(rels), N=N, primes=P,
                n_chars=len(chars), h1_multiset_over_nontrivial_chi=dict(vals),
                loci=sum(v for h,v in vals.items() if h>=1), examples_h1_ge_2=best[:8])

if __name__=='__main__':
    out=[]
    # A. controls where the value is NOT 1: b_1 = 2 and b_1 = 3 manifolds at the trivial module
    for nm in ['m129','m125','t12067','m003']:
        M=snappy.Manifold(nm); G=M.fundamental_group()
        from v2_loci import h1_exact as HE
        gens=list(G.generators()); rels=list(G.relators())
        h=HE(gens,rels,{g:0 for g in gens},1)
        out.append(dict(control=nm,H1=str(M.homology()),num_cusps=M.num_cusps(),
                        h1_trivial_module=h, note="equals b_1; shows the routine returns values != 1"))
        print(out[-1],flush=True)
    # B. the Whitehead link's full character scan (2 cusps): does h^1 = 2 occur at a NONTRIVIAL character?
    r=scan(snappy.Manifold('m129'),12,'m129 (Whitehead link, 2 cusps), N=12'); out.append(r); print(json.dumps(r),flush=True)
    r=scan(snappy.Manifold('m125'),12,'m125 (2 cusps), N=12'); out.append(r); print(json.dumps(r),flush=True)
    # C. the tower higher up, and non-cyclic covers of m004
    for n,N in [(6,120),(8,420)]:
        try:
            Y=snappy.Manifold('m004').covers(n,cover_type='cyclic')[0]
            r=scan(Y,N,'Y_%d cyclic cover of m004, N=%d'%(n,N)); out.append(r); print(json.dumps(r),flush=True)
        except Exception as e:
            print('Y_%d failed: %s'%(n,e),flush=True)
    json.dump(out,open('<here>/v6_vacuity.json','w'),indent=1,default=str)
