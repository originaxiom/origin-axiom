#!/usr/bin/env python3
"""The tower beyond level 6: loci and h^1(chi^2) on Y_7, Y_8, Y_9, Y_10 (the record computed only up to 6).
Character enumeration done component-wise so N^3 is never materialised."""
import sys, os, json, math, warnings, time
from collections import Counter
warnings.filterwarnings("ignore")
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
import snappy
from v2_loci import h1_gf, h1_exact, primes_1_mod, primitive_root, abvec

def run(n):
    t0=time.time()
    Y=snappy.Manifold('m004').covers(n,cover_type='cyclic')[0]
    G=Y.fundamental_group(); gens=list(G.generators()); rels=list(G.relators())
    A=[abvec(r,gens) for r in rels]; g=len(gens)
    H1=str(Y.homology())
    e=1
    for part in H1.replace(' ','').split('+'):
        if part.startswith('Z/'): e=e*int(part[2:])//math.gcd(e,int(part[2:]))
    N=12*e//math.gcd(12,e)
    zero_cols=[j for j in range(g) if all(a[j]==0 for a in A)]
    P=primes_1_mod(N,3,1000); zet={p:pow(primitive_root(p),(p-1)//N,p) for p in P}
    # enumerate solutions of A k = 0 mod N without materialising N^g
    if len(zero_cols)==1 and g==3:
        fg=zero_cols[0]; oth=[j for j in range(g) if j!=fg]
        base=[]
        for ka in range(N):
            for kc in range(N):
                k=[0]*g; k[oth[0]]=ka; k[oth[1]]=kc
                if all(sum(a[j]*k[j] for j in range(g))%N==0 for a in A): base.append(tuple(k))
        chars=[tuple(b[j]+(kb if j==fg else 0) for j in range(g)) for b in base for kb in range(N)]
    else:
        return dict(n=n,H1=H1,note="unexpected presentation shape",gens=gens,rels=rels,zero_cols=zero_cols)
    cache={}; vals=Counter(); ge2=[]
    for k in chars:
        tw=[2*x%N for x in k]; d=N
        for x in tw: d=math.gcd(d,x)
        m=N//d; ee=tuple((x//d)%m for x in tw) if m>1 else tuple(0 for _ in tw)
        key=(m,ee)
        if key not in cache:
            ed=dict(zip(gens,ee))
            hs=[h1_gf(gens,rels,ed,max(m,1),p,pow(zet[p],N//m,p) if m>1 else 1) for p in P]
            h=min(hs)
            if h>=1: h=h1_exact(gens,rels,ed,max(m,1))
            cache[key]=h
        h=cache[key]
        if all(x==0 for x in k): continue
        vals[h]+=1
        if h>=2: ge2.append((list(k),h))
    return dict(n=n,H1=H1,N=N,primes=P,n_chars=len(chars),
                h1_multiset_over_nontrivial_chi=dict(vals),
                loci=sum(v for hh,v in vals.items() if hh>=1),
                examples_h1_ge_2=ge2[:8], seconds=round(time.time()-t0,1))

if __name__=='__main__':
    out={}
    for n in [int(x) for x in sys.argv[1:]] or [7,8]:
        r=run(n); out[n]=r; print(json.dumps(r),flush=True)
    json.dump(out,open('<here>/v7_high_levels_%s.json'%'_'.join(sys.argv[1:]),'w'),indent=1)
