"""The realistic case: V = (+) Sym^{n_i} (x) chi, so t0 = #summands > 1.
A single Sym^m gives t0 = 1, t1 = 2, where a line in a 2-dim symplectic space
is isotropic for free -- structurally biased toward I = 0."""
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
SUMS=[(1,1),(1,2),(2,2),(1,1,1),(1,2,3)]     # t0 = 2,2,2,3,3
res=Counter(); nonzero=[]; tot=0
for nm in names[:30]:
    try:
        M=snappy.Manifold(nm); G=M.fundamental_group()
        gens=list(G.generators()); rels=list(G.relators()); mu,lam=G.peripheral_curves()[0]
        if len(gens)!=2: continue
        chars=order3_chars(gens,rels,mu,lam)
        if not chars: continue
        for p in [7,13]:
            om=[x for x in range(2,p) if pow(x,3,p)==1][0]
            for rho in sl2p_reps(gens,rels,mu,p,limit=8):
                if not is_irreducible_2d(gens,rho,p): continue
                for ms in SUMS:
                    base={g:blockdiag([sym_power(rho[g],m,p) for m in ms],p) for g in gens}
                    d=sum(m+1 for m in ms)
                    for psi in chars:
                        V ={g:scal(pow(om,psi[i],p),base[g],p) for i,g in enumerate(gens)}
                        Vd={g:scal(pow(om,(-psi[i])%3,p),base[g],p) for i,g in enumerate(gens)}
                        A=analyse(gens,rels,mu,lam,V,p,d); B=analyse(gens,rels,mu,lam,Vd,p,d)
                        if a0_dim(gens,V,p,d)!=a0_dim(gens,Vd,p,d) or A['t0']!=B['t0']: continue
                        tot+=1; res[(A['t0'],A['I'])]+=1
                        if A['I']!=0: nonzero.append((nm,p,ms,psi,A,B))
    except Exception: continue
print("in-domain sectors with SUMMED germs:",tot)
print("(t0, I) distribution:",dict(sorted(res.items())))
print("t0 > 1 sectors:",sum(v for (t,i),v in res.items() if t>1))
print("NON-ZERO index:",len(nonzero))
for x in nonzero[:6]: print("   ",x[0],"p=",x[1],"Sym",x[2],"t0=",x[4]['t0'],"r1=",x[4]['r1'],"I=",x[4]['I'])
