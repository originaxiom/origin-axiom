import sys, warnings, snappy; sys.path.insert(0,'/tmp/sweep'); warnings.filterwarnings("ignore")
from driver import *
from index_lib import a0_dim, is_irreducible_2d
from collections import Counter
def blockdiag(mats,p):
    d=sum(len(m) for m in mats); out=[[0]*d for _ in range(d)]; o=0
    for m in mats:
        k=len(m)
        for i in range(k):
            for j in range(k): out[o+i][o+j]=m[i][j]
        o+=k
    return out
NM='v2873'
M=snappy.Manifold(NM); G=M.fundamental_group()
gens=list(G.generators()); rels=list(G.relators()); mu,lam=G.peripheral_curves()[0]
print(f"{NM}: chiral={not M.symmetry_group().is_amphicheiral()}  gens={gens}")
chars=order3_chars(gens,rels,mu,lam)
print("order-3 cusp-trivial characters:",len(chars))
res=Counter(); nonzero=[]; tot=0
for p in [7,13,19]:
    om=[x for x in range(2,p) if pow(x,3,p)==1][0]
    reps=[r for r in sl2p_reps(gens,rels,mu,p,limit=60) if is_irreducible_2d(gens,r,p)]
    print(f"  p={p}: irreducible parabolic reps = {len(reps)}")
    for rho in reps:
        for ms in [(2,),(4,),(2,2),(2,4),(2,2,2),(2,4,6),(2,2,2,2)]:
            base={g:blockdiag([sym_power(rho[g],m,p) for m in ms],p) for g in gens}
            d=sum(m+1 for m in ms)
            for psi in chars:
                V ={g:scal(pow(om,psi[i],p),base[g],p) for i,g in enumerate(gens)}
                Vd={g:scal(pow(om,(-psi[i])%3,p),base[g],p) for i,g in enumerate(gens)}
                A=analyse(gens,rels,mu,lam,V,p,d); B=analyse(gens,rels,mu,lam,Vd,p,d)
                if a0_dim(gens,V,p,d)!=a0_dim(gens,Vd,p,d) or A['t0']!=B['t0']: continue
                tot+=1; res[(A['t0'],A['I'])]+=1
                if A['I']!=0: nonzero.append((p,ms,psi,A,B))
print()
print("in-domain sectors:",tot)
print("(t0,I) distribution:",dict(sorted(res.items())))
print("NON-ZERO INDEX:",len(nonzero))
for x in nonzero[:8]: print("   p=",x[0],"Sym",x[1],"t0=",x[3]['t0'],"r1=",x[3]['r1'],"I=",x[3]['I'])
