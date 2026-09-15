#!/usr/bin/env python3
"""MEMO-48 CELL: WHY THE COUPLING IS UNIQUE — the invariance chain counted.
pi1 alone leaves a large coupling space; the gauge principle cuts it to four;
the object's full algebra cuts it to one — the beat-covariant Jordan coupling.

Three rungs, all exact:
  RUNG 1 (pi1 / its Zariski closure): the holonomy is nonelementary, hence
    Zariski-dense in SL(2,C) (CITED-standard), and the internal bridge is an
    algebraic homomorphism, so the closure of the diagonal pi1-image is the
    DIAGONAL SL2.  Invariant trilinears on Psi x Psi x 27 under it are counted
    by exact Clebsch arithmetic from the modules' sl2 content:
      Psi|_diag  = 6*spin1 + 15*spin1/2 + 6*spin0   (derived from the exact
                   joint weight multiset, verified in-run),
      27|_int    = 6*spin1/2 + 15*spin0.
    D1 = sum over component triples of m1*m2*m3*[trivial in j1xj2xj3].
  RUNG 2 (+ trinification gauge): Inv = Inv_sl2(C^2 x C^2) * Inv_sl3^3(27^3)
    = 1 * 4  (memo 35's banked Yukawa count; epsilon unique).
  RUNG 3 (+ full e6): the FULL-TENSOR (non-symmetrized) e6-invariant space on
    27 x 27 x 27 is computed here by exact nullspace on ordered weight-zero
    triples — PREREGISTERED: dim = 1, and the solution is automatically
    SYMMETRIC (so memo 32's Sym^3 count was no restriction).  With epsilon
    unique, the chain ends at exactly Y = eps (x) C.
"""
import itertools
from fractions import Fraction as F
from collections import Counter, defaultdict
SCR=__import__('os').path.dirname(__import__('os').path.abspath(__file__))+""
src=open(SCR+"/twisted_double.py").read()
cut=src.index("# ---------------- stage 4")
exec(src[:cut])

# ---- exact sl2 content of Psi and of the internal 27
r0=ROOTS[0]
hA=[F(0)]*DIM
for k in range(N): hA[k]=F(r0[k])
Hint=rho27_Q(hA)
wts27=Counter(int(Hint[a][a]) for a in range(27))
assert dict(wts27)=={1:6,0:15,-1:6}
# 27|_int: weights {+-1:6, 0:15} -> 6 doublets + 15 singlets
dec27={F(1)/2:6, F(0):15}
# Psi: joint h_diag = h_taut + h_int weight multiset
psi_w=Counter()
for s_ in (1,-1):
    for a in range(27):
        psi_w[s_+int(Hint[a][a])]+=1
print("Psi diagonal-sl2 weight multiset:", dict(psi_w))
# peel highest weights to get the decomposition
decPsi={}
w=dict(psi_w)
while any(v>0 for v in w.values()):
    top=max(k for k,v in w.items() if v>0)
    mult=w[top]
    j=F(top)/2 if False else F(top,2)
    decPsi[j]=decPsi.get(j,0)+mult
    k=top
    while k>=-top:
        w[k]=w.get(k,0)-mult
        k-=2
print("Psi|_diag-sl2 decomposition {spin: mult}:", {str(k):v for k,v in sorted(decPsi.items())})
assert decPsi=={F(1):6, F(1,2):15, F(0):6}

# RUNG 1: D1 by exact Clebsch counting
def has_trivial(j1,j2,j3):
    if (j1+j2+j3) % 1 != 0: return False
    return abs(j1-j2) <= j3 <= j1+j2
D1=0
for j1,m1 in decPsi.items():
    for j2,m2 in decPsi.items():
        for j3,m3 in dec27.items():
            if has_trivial(j1,j2,j3): D1+=m1*m2*m3
print(f"RUNG 1: dim of pi1-invariant trilinears on Psi x Psi x 27  =  {D1}")

# RUNG 3: full-tensor e6 invariants on 27 x 27 x 27 (ordered), exact nullspace
Hs=[rho27_Q([F(1) if k==i else F(0) for k in range(DIM)]) for i in range(N)]
wt=[tuple(Hs[i][a][a] for i in range(N)) for a in range(27)]
def addw(*ws): return tuple(sum(x) for x in zip(*ws))
ZERO6=tuple(F(0) for _ in range(N))
ordered=[t for t in itertools.product(range(27),repeat=3) if addw(wt[t[0]],wt[t[1]],wt[t[2]])==ZERO6]
tid={t:n for n,t in enumerate(ordered)}
print(f"ordered weight-zero triples: {len(ordered)}")
gens=[]
for i in range(N):
    r=tuple(1 if k==i else 0 for k in range(N))
    gens.append(rho27_Q(evec(r)))
    gens.append(rho27_Q(evec(tuple(-x for x in r))))
rows=[]
for M in gens:
    nz0=next(((l,i) for l in range(27) for i in range(27) if M[l][i]!=0))
    shift=tuple(a-b for a,b in zip(wt[nz0[0]],wt[nz0[1]]))
    target=tuple(-x for x in shift)
    col_of=defaultdict(list)
    for l in range(27):
        for i in range(27):
            if M[l][i]!=0: col_of[i].append(l)
    for (i,j,k) in itertools.product(range(27),repeat=3):
        if addw(wt[i],wt[j],wt[k])!=target: continue
        row=defaultdict(F)
        for l in col_of.get(i,[]):
            t=(l,j,k)
            if t in tid: row[tid[t]]+=M[l][i]
        for l in col_of.get(j,[]):
            t=(i,l,k)
            if t in tid: row[tid[t]]+=M[l][j]
        for l in col_of.get(k,[]):
            t=(i,j,l)
            if t in tid: row[tid[t]]+=M[l][k]
        if row: rows.append(row)
def nullspace(rows,n):
    dense=[[F(0)]*n for _ in range(len(rows))]
    for ri,row in enumerate(rows):
        for c,v in row.items(): dense[ri][c]=v
    m=len(dense); r=0; piv=[]
    for col in range(n):
        p=next((i for i in range(r,m) if dense[i][col]!=0),None)
        if p is None: continue
        dense[r],dense[p]=dense[p],dense[r]
        pv=dense[r][col]; dense[r]=[x/pv for x in dense[r]]
        for i in range(m):
            if i!=r and dense[i][col]!=0:
                fq=dense[i][col]; dense[i]=[x-fq*y for x,y in zip(dense[i],dense[r])]
        piv.append(col); r+=1
    free=[c for c in range(n) if c not in piv]
    out=[]
    for fc in free:
        v=[F(0)]*n; v[fc]=F(1)
        for i,col in enumerate(piv): v[col]=-dense[i][fc]
        out.append(v)
    return out
NS=nullspace(rows,len(ordered))
print(f"RUNG 3: dim of FULL-TENSOR e6-invariants on 27 x 27 x 27  =  {len(NS)}")
assert len(NS)==1
Cfull=NS[0]
sym=all(Cfull[tid[(a,b,c)]]==Cfull[tid[(p,q,s_)]]
        for (a,b,c) in ordered for (p,q,s_) in [tuple(sorted((a,b,c)))]
        if tuple(sorted((a,b,c))) in tid) if False else True
# symmetry check: compare each ordered triple's coefficient with a fixed permutation
symok=True
for (a,b,c) in ordered:
    for perm in ((b,a,c),(a,c,b)):
        if perm in tid and Cfull[tid[perm]]!=Cfull[tid[(a,b,c)]]: symok=False
print("the unique full-tensor invariant is automatically SYMMETRIC:", symok)
assert symok

print(f"""
THE UNIQUENESS CHAIN, EXACT:
    pi1 alone (diagonal SL2 closure)      : {D1} independent couplings
    + trinification gauge (memo 35 x eps) : 4
    + the object's full e6 (computed here): 1  — and that one is symmetric,
      so it IS the Jordan coupling Y = eps (x) C of memo 47.
The gauge principle is not decoration: without internal covariance the
carrier admits {D1} couplings; the closing's own symmetry does all the
cutting, and what survives is the single beat-covariant Jordan coupling.
(Zariski-density of the nonelementary holonomy and algebraicity of the
bridge are the CITED-standard steps; every dimension above is computed.)""")
