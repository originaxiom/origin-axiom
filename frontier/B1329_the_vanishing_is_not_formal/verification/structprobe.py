import sys, json, warnings, snappy; sys.path.insert(0,'/tmp/sweep'); warnings.filterwarnings("ignore")
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
hits=json.load(open('hits.json')); names=[h[0] for h in hits]
trip=Counter()
for nm in names[:25]:
    try:
        M=snappy.Manifold(nm); G=M.fundamental_group()
        gens=list(G.generators()); rels=list(G.relators()); mu,lam=G.peripheral_curves()[0]
        if len(gens)!=2: continue
        chars=order3_chars(gens,rels,mu,lam)
        if not chars: continue
        for p in [7,13]:
            om=[x for x in range(2,p) if pow(x,3,p)==1][0]
            for rho in sl2p_reps(gens,rels,mu,p,limit=6):
                if not is_irreducible_2d(gens,rho,p): continue
                for ms in [(1,),(1,1),(1,2),(1,1,1),(1,2,3)]:
                    base={g:blockdiag([sym_power(rho[g],m,p) for m in ms],p) for g in gens}
                    d=sum(m+1 for m in ms)
                    for psi in chars:
                        V={g:scal(pow(om,psi[i],p),base[g],p) for i,g in enumerate(gens)}
                        Vd={g:scal(pow(om,(-psi[i])%3,p),base[g],p) for i,g in enumerate(gens)}
                        A=analyse(gens,rels,mu,lam,V,p,d); B=analyse(gens,rels,mu,lam,Vd,p,d)
                        if a0_dim(gens,V,p,d)!=a0_dim(gens,Vd,p,d) or A['t0']!=B['t0']: continue
                        a0=a0_dim(gens,V,p,d); a1=A['dimZ1']-(d-a0)
                        trip[(A['t0'],a1,A['r1'])]+=1
    except Exception: continue
print("(t0, a1=h^1(M;V), r1) -> count      [I = t0 - r1]")
for k,v in sorted(trip.items()):
    t0,a1,r1=k
    tag = 'a1 == t0' if a1==t0 else ('a1 > t0' if a1>t0 else 'a1 < t0')
    print(f"   t0={t0}  a1={a1:2d}  r1={r1}   I={t0-r1:+d}   x{v:5d}   {tag}")
