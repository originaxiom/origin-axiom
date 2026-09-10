import sys, json, warnings, snappy; sys.path.insert(0,'/tmp/sweep'); warnings.filterwarnings("ignore")
from driver import *
from index_lib import a0_dim, is_irreducible_2d
from collections import Counter

hits=json.load(open('hits.json'))                 # manifolds with order-3 cusp-trivial characters
names=[h[0] for h in hits]
PRIMES=[7,13,19]
inD=Counter(); outD=Counter(); nonzero_in_D=[]; nsec=0; nman=0
for nm in names[:120]:
    try:
        M=snappy.Manifold(nm); G=M.fundamental_group()
        gens=list(G.generators()); rels=list(G.relators()); mu,lam=G.peripheral_curves()[0]
        if len(gens)!=2: continue
        chars=order3_chars(gens,rels,mu,lam)
        if not chars: continue
        nman+=1
        for p in PRIMES:
            om=[x for x in range(2,p) if pow(x,3,p)==1][0]
            for rho in sl2p_reps(gens,rels,mu,p,limit=25):
                if not is_irreducible_2d(gens,rho,p): continue   # reductive + parabolic cusp => irreducible
                for m in (1,2):                       # Sym^1 and Sym^2 (their family)
                    base={g:sym_power(rho[g],m,p) for g in gens}; d=m+1
                    for psi in chars:
                        V ={g:scal(pow(om,psi[i],p),base[g],p) for i,g in enumerate(gens)}
                        Vd={g:scal(pow(om,(-psi[i])%3,p),base[g],p) for i,g in enumerate(gens)}
                        A=analyse(gens,rels,mu,lam,V,p,d); B=analyse(gens,rels,mu,lam,Vd,p,d)
                        if a0_dim(gens,V,p,d)==a0_dim(gens,Vd,p,d) and A['t0']==B['t0']:
                            inD[A['I']]+=1; nsec+=1
                            if A['I']!=0: nonzero_in_D.append((nm,p,m,psi,A,B))
                        else:
                            outD[A['I']]+=1
    except Exception:
        continue
    if nman%20==0: print(f"  ...{nman} manifolds, {nsec} in-D sectors, nonzero-in-D={len(nonzero_in_D)}", flush=True)
print()
print("manifolds scanned          :", nman)
print("sectors INSIDE domain D    :", nsec, " distribution of I:", dict(inD))
print("sectors OUTSIDE domain D   :", sum(outD.values()), " distribution of I:", dict(outD))
print("NON-ZERO index inside D    :", len(nonzero_in_D))
for x in nonzero_in_D[:5]: print("   ",x)
json.dump({'inD':dict(inD),'outD':dict(outD),'nonzero':[str(x) for x in nonzero_in_D],'nman':nman},open('bigscan.json','w'))
