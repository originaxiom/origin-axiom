import sys, json, warnings, snappy; sys.path.insert(0,'/tmp/sweep'); warnings.filterwarnings("ignore")
from driver import *
from index_lib import a0_dim, is_irreducible_2d
from collections import Counter
hits=json.load(open('hits.json')); names=[h[0] for h in hits]
t0dist=Counter(); nonvac=0; tot=0; byI=Counter()
for nm in names[:40]:
    try:
        M=snappy.Manifold(nm); G=M.fundamental_group()
        gens=list(G.generators()); rels=list(G.relators()); mu,lam=G.peripheral_curves()[0]
        if len(gens)!=2: continue
        chars=order3_chars(gens,rels,mu,lam)
        if not chars: continue
        for p in [7,13]:
            om=[x for x in range(2,p) if pow(x,3,p)==1][0]
            for rho in sl2p_reps(gens,rels,mu,p,limit=15):
                if not is_irreducible_2d(gens,rho,p): continue
                for m in (1,2):
                    base={g:sym_power(rho[g],m,p) for g in gens}; d=m+1
                    for psi in chars:
                        V ={g:scal(pow(om,psi[i],p),base[g],p) for i,g in enumerate(gens)}
                        Vd={g:scal(pow(om,(-psi[i])%3,p),base[g],p) for i,g in enumerate(gens)}
                        A=analyse(gens,rels,mu,lam,V,p,d); B=analyse(gens,rels,mu,lam,Vd,p,d)
                        if a0_dim(gens,V,p,d)!=a0_dim(gens,Vd,p,d) or A['t0']!=B['t0']: continue
                        tot+=1; t0dist[A['t0']]+=1; byI[(A['t0'],A['I'])]+=1
                        if A['t0']>0: nonvac+=1
    except Exception: continue
print("in-domain sectors:",tot)
print("t0 distribution:",dict(sorted(t0dist.items())))
print("NON-VACUOUS (t0 > 0, so T5 does not force I=0):",nonvac, f"= {100*nonvac/max(tot,1):.1f}%")
print("(t0, I) pairs:",dict(sorted(byI.items())))
