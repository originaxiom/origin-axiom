"""Is the cusp-trivial character family POSITIVE-DIMENSIONAL?

The idea: on the subgroup S of characters trivial on every peripheral curve, the cusp matrices
are constant, so t_0, t_0* and t_1 are constant on S. Meanwhile r_1(z) + r_1(z^-1) = t_1 holds
identically, and r_1 is the rank of a matrix depending algebraically on z, hence lower
semicontinuous. If S is a POSITIVE-DIMENSIONAL torus, it is irreducible, so:

  * r_1 attains its max rho on a Zariski-open dense U, and inversion is an automorphism of S,
    so U and iota(U) are both dense and meet;
  * at z in U n iota(U):  r_1(z) = rho and r_1(z^-1) = rho, and they sum to t_1, so rho = t_1/2;
  * then for EVERY z: r_1(z) <= t_1/2 and r_1(z^-1) <= t_1/2 summing to t_1, so both equal t_1/2.

That would be a PROOF of I = 0 on S -- needing no isotropy, no Galois, no cusp-locality, which is
exactly the shape the evidence demands.

It all turns on dim S = rank of H_1(M) / <peripheral curves>.  If that is 0, S is finite and the
density argument has nothing to stand on.  So: compute it.
"""
import sys, warnings, json; sys.path.insert(0,'/tmp/sweep'); warnings.filterwarnings("ignore")
import snappy
from fractions import Fraction as Fr

def expsum(word,gens):
    v=[0]*len(gens)
    for ch in word:
        if ch.islower(): v[gens.index(ch)]+=1
        else: v[gens.index(ch.lower())]-=1
    return v

def qrank(rows,n):
    """rank over Q"""
    M=[[Fr(x) for x in r] for r in rows]; r=0
    for c in range(n):
        p=next((i for i in range(r,len(M)) if M[i][c]!=0),None)
        if p is None: continue
        M[r],M[p]=M[p],M[r]
        pv=M[r][c]; M[r]=[x/pv for x in M[r]]
        for i in range(len(M)):
            if i!=r and M[i][c]!=0:
                f=M[i][c]; M[i]=[M[i][j]-f*M[r][j] for j in range(n)]
        r+=1
    return r

def dim_S(gens,rels,per):
    """rank of H_1 / <peripheral>, i.e. dim of the cusp-trivial character torus"""
    n=len(gens)
    rows=[expsum(r,gens) for r in rels]
    rows+=[expsum(w,gens) for (mu,lam) in per for w in (mu,lam)]
    return n-qrank(rows,n)

def b1(gens,rels):
    n=len(gens)
    return n-qrank([expsum(r,gens) for r in rels],n)

print("manifold        cusps  b_1(M)  dim S = rank H_1/<peripheral>")
M0=snappy.Manifold('m004')
for nm in ['m004','s958','t12833','t12835']:
    M=snappy.Manifold(nm); G=M.fundamental_group()
    gens=list(G.generators()); rels=list(G.relators()); per=list(G.peripheral_curves())
    print(f"  {nm:12s} {M.num_cusps():4d}  {b1(gens,rels):5d}   {dim_S(gens,rels,per):5d}")
db=json.load(open('/tmp/sweep/covcache.json'))
pos=[]
for tag,v in sorted(db.items()):
    if not v.get('ok'): continue
    gens=v['gens']; rels=v['rels']; per=[tuple(x) for x in v['per']]
    d=dim_S(gens,rels,per); b=b1(gens,rels)
    if d>0: pos.append((tag,v['cusps'],b,d))
    print(f"  {tag:12s} {v['cusps']:4d}  {b:5d}   {d:5d}")
print(f"\nCOVERS WITH A POSITIVE-DIMENSIONAL cusp-trivial family: {len(pos)}")
for t,c,b,d in pos: print("   ",t,"cusps",c,"b1",b,"dim S",d)
