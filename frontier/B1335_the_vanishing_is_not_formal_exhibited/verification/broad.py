"""Is the vanishing about THIS arithmetic, or about cusped 3-manifolds in general?

The paper's own caveat: "whether it is ever non-zero on a one-cusped hyperbolic manifold in its
domain is not established". The Galois protection it does have runs on Q(sqrt-3) and twists of
order prime to 3. So scan WIDELY and OFF that field: one-cusped census manifolds of any trace
field, cusp-trivial characters of ANY order n (not just 3), Sym^m germs, mod p.

If the index is non-zero anywhere, that is falsifier 6 fired.
If it never is, the vanishing is a general fact about cusped 3-manifolds, not about the object's
arithmetic -- which would mean the index could never have detected chirality, whatever the field.

Cusp-trivial characters = characters of  H_1(M)/<mu,lam>, computed by Smith form.
"""
import sys, warnings, os; sys.path.insert(0,'/tmp/sweep'); warnings.filterwarnings("ignore")
import snappy, itertools
from collections import Counter
from index_lib import *
from mc_lib import check

def expsum(word,gens):
    v=[0]*len(gens)
    for ch in word:
        if ch.islower(): v[gens.index(ch)]+=1
        else: v[gens.index(ch.lower())]-=1
    return v

def smith_quotient(gens,rels,per):
    """invariant factors of H_1(M)/<peripheral>, via integer Smith normal form"""
    rows=[expsum(r,gens) for r in rels]+[expsum(w,gens) for (mu,lam) in per for w in (mu,lam)]
    n=len(gens); A=[r[:] for r in rows]
    if not A: return [],n
    m=len(A); res=[]; r=0; c=0
    while r<m and c<n:
        piv=None
        for i in range(r,m):
            if A[i][c]!=0 and (piv is None or abs(A[i][c])<abs(A[piv][c])): piv=i
        if piv is None: c+=1; continue
        A[r],A[piv]=A[piv],A[r]
        done=True
        for i in range(r+1,m):
            if A[i][c]!=0:
                q=A[i][c]//A[r][c]
                A[i]=[A[i][j]-q*A[r][j] for j in range(n)]
                if A[i][c]!=0: done=False
        if not done: continue
        for j in range(c+1,n):
            if A[r][j]%A[r][c]==0:
                q=A[r][j]//A[r][c]
                for i in range(m): A[i][j]-=q*A[i][c]
        res.append(abs(A[r][c])); r+=1; c+=1
    free=n-len(res)
    return [x for x in res if x!=1], free

def chars_of_order(gens,rels,per,p):
    """characters pi_1 -> F_p^* trivial on all peripheral curves"""
    out=[]
    for tup in itertools.product(range(1,p),repeat=len(gens)):
        ok=True
        for w in [r for r in rels]+[x for (mu,lam) in per for x in (mu,lam)]:
            v=expsum(w,gens); val=1
            for x,e in zip(tup,v): val=(val*pow(x,e%(p-1),p))%p
            if val!=1: ok=False; break
        if ok and any(x!=1 for x in tup): out.append(tup)
    return out

def sym_p(A,m,p):
    from math import comb
    d=m+1; out=[[0]*d for _ in range(d)]
    a,b=A[0]; c,dd=A[1]
    for j in range(d):
        coef=[0]*d
        for u in range(m-j+1):
            for v in range(j+1):
                coef[u+v]=(coef[u+v]+comb(m-j,u)*pow(a,m-j-u,p)*pow(c,u,p)*comb(j,v)*pow(b,j-v,p)*pow(dd,v,p))%p
        for i in range(d): out[i][j]=coef[i]
    return out

def sl2(q):
    return [[[a,b],[c,d]] for a in range(q) for b in range(q) for c in range(q) for d in range(q)
            if (a*d-b*c)%q==1]

P=int(os.environ.get('P','13')); NM=int(os.environ.get('N','120'))
S=sl2(P)
tally=Counter(); hits=[]; tested=0; broken=0; scanned=0; withchars=0
cen=snappy.OrientableCuspedCensus(num_cusps=1)
for M in cen[:NM]:
    G=M.fundamental_group()
    gens=list(G.generators()); rels=list(G.relators()); per=list(G.peripheral_curves())
    if len(gens)>2: continue
    scanned+=1
    tors,free=smith_quotient(gens,rels,per)
    ch=chars_of_order(gens,rels,per,P)
    if not ch: continue
    withchars+=1
    # honest SL2(F_P) representations
    reps=[]
    for tup in itertools.product(S,repeat=len(gens)):
        rho=dict(zip(gens,tup))
        if all(word_eval(r,rho,P,2)==eye(2) for r in rels):
            reps.append(rho)
            if len(reps)>=4: break
    for rho2 in reps:
        for m in (1,2,3,4):
            base={g:sym_p(rho2[g],m,P) for g in gens}; d=m+1
            for c in ch[:8]:
                V={g:[[(c[i]*base[g][x][y])%P for y in range(d)] for x in range(d)]
                   for i,g in enumerate(gens)}
                if any(word_eval(r,V,P,d)!=eye(d) for r in rels): continue
                A,B,ids=check(gens,rels,per,V,P,d); tested+=1
                if not all(ids.values()): broken+=1; continue
                tally[(A['t0'],A['I_exact'])]+=1
                if A['I_exact']!=0: hits.append((M.name(),m,c,A,B))
    if scanned%20==0: print(f"  scanned {scanned}, with cusp-trivial chars {withchars}, "
                           f"sectors {tested}, nonzero {len(hits)}", flush=True)
print(f"\nSCANNED {scanned} one-cusped census manifolds | {withchars} carry cusp-trivial characters mod {P}")
print(f"SECTORS {tested} | identity-broken {broken}")
if tested==0: print("** NOTHING TESTED -- failure **"); sys.exit(1)
live=sum(v for (t0,I),v in tally.items() if t0>=1)
print(f"LIVE sectors (t0>=1): {live}")
print("(t0, I) -> count"); 
for k in sorted(tally): print("   ",k,"->",tally[k])
print(f"\nNON-ZERO INDEX: {len(hits)}")
for h in hits[:10]: print("   ",h[0],"Sym",h[1],"chi",h[2],"t0",h[3]['t0'],"r1",h[3]['r1'],"I",h[3]['I_exact'])
