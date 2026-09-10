import snappy, warnings, json; warnings.filterwarnings("ignore")
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

def expsum(word, gens):
    v=[0]*len(gens)
    for ch in word:
        if ch.islower(): v[gens.index(ch)]+=1
        else: v[gens.index(ch.lower())]-=1
    return v

def cusp_trivial_group(M):
    """A = H_1(M) / <mu, lambda>  -- exactly the group of cusp-trivial characters."""
    G=M.fundamental_group()
    gens=list(G.generators()); g=len(gens)
    if g==0: return None
    rows=[expsum(r,gens) for r in G.relators()]
    mu,lam=G.peripheral_curves()[0]
    rows.append(expsum(mu,gens)); rows.append(expsum(lam,gens))
    A=sp.Matrix(rows)
    S=smith_normal_form(A)
    inv=[]
    for i in range(min(S.rows,S.cols)):
        d=abs(int(S[i,i]))
        if d==0: return 'INFINITE'
        if d>1: inv.append(d)
    # any generator columns beyond rank -> free part
    if S.cols>S.rank(): return 'INFINITE'
    return inv

hits=[]; n=0; infinite=0
for M in snappy.OrientableCuspedCensus(cusps=1):
    n+=1
    try: A=cusp_trivial_group(M)
    except Exception: continue
    if A=='INFINITE': infinite+=1; continue
    if A is None: continue
    order=1
    for d in A: order*=d
    if order%3==0:
        hits.append((M.name(), A, order, M.num_tetrahedra(), str(M.homology())))
print("one-cusped census manifolds scanned:", n)
print("with INFINITE cusp-trivial character group:", infinite)
print("with 3 | |A| (order-3 cusp-trivial characters EXIST):", len(hits))
print()
for h in hits[:25]: print("   ", h)
json.dump(hits, open("hits.json","w"))
