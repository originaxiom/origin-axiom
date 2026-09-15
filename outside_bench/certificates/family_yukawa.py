#!/usr/bin/env python3
"""MEMO-53 CELL: THE THREE-FAMILY YUKAWA IS INTER-FAMILY — inside E8, the
bracket-induced coupling on the family triplet of 27's factorizes exactly as
eps_family (x) (the Jordan cubic), so same-family Yukawa couplings VANISH
IDENTICALLY in the E8 channel.

Named follow-up of golden_gate G-3 (the 27 enters E8 exactly THREE times,
indexed by the triplet of the fourth orthogonal A2) and of memo 52 (probe the
family structure against the coupling).  POSSIBILITY-SPACE CELL: E8 is not
object-paid; this computes what the ambient possibility space forces IF the
three families are the G-3 triplet.  The object connection: the internal
factor is forced onto the object's own unique coupling (memos 32/47/48).

Construction: T(x,y,z) = K(x, [y,z]) on the (3,27) block, with K the exact
ad-trace Killing form and [,] the Frenkel-Kac bracket — every number computed,
every property VERIFIED rather than cited.

PREREGISTERED (two-outcome; every claim an assert):
  FACT 1 (G-3 re-anchored): all four orthogonal A2 slots have 72-root e6
    complement and 162 crossing roots in 6 projection classes x 27; the
    family block FAM = the 81 roots over the three triplet weights.
  FACT 2 (support): the zero-sum triples inside FAM number EXACTLY 270 =
    45 internal weight-zero triples x 6 family assignments; every one has
    THREE DISTINCT family weights (no same-family triple exists at all);
    each of the 45 internal triples occurs with all 6 assignments.
  FACT 3 (the form): kappa(r) = tr(ad e_r ad e_{-r}) is the SAME constant
    for all 81 roots (exact ad-trace, 248-dim); T built from kappa * eps.
  FACT 4 (invariance, verified not cited): the derivation identity
    T([g,x],y,z) + T(x,[g,y],z) + T(x,y,[g,z]) = 0 holds for ALL 72
    complement-e6 root vectors AND all 6 family-A2 root vectors.
  FACT 5 (total antisymmetry): T(perm) = sgn(perm) T for all 270 support
    triples and all 6 permutations.
  FACT 6 (exact factorization, gauge-corrected): C'(a,b,c) :=
    T((mu1,a),(mu2,b),(mu3,c)) (lexicographic family order) has values one
    constant times +-1 and satisfies T(family-permuted) = sgn C' — but the
    RAW C' is NOT symmetric, and the machine refused the first draft's
    symmetric-C' assert.  [ERROR FILED at point of occurrence, lane error
    #4: the Chevalley root vector e_(mu_i, w_a) differs from the factorized
    basis f_i (x) v_a by a per-root sign c_{i,a}; raw C' picks up
    c_{1,a}c_{2,b}c_{3,c} and need not be symmetric.  The correct claim is
    gauge existence.]  CORRECTED CLAIM: there exist signs sigma_{i,a} and a
    SYMMETRIC sign function S on the 45 unordered internal triples with
      T((mu_i,a),(mu_j,b),(mu_k,c)) =
        kappa * sgn(ijk) * sigma_{i,a} sigma_{j,b} sigma_{k,c} * S({a,b,c})
    for ALL 1620 ordered entries — solved CONSTRUCTIVELY as a linear system
    over GF(2) (126 unknowns, 270 equations), then verified forward on
    every entry.  In the sigma-rescaled basis T = eps_family (x) C_sym
    exactly; C_sym is e6-invariant (FACT 4), symmetric, nonzero => by the
    banked dimension-1 count (memo 48 rung 3) it IS the Jordan cubic up to
    scale.
  FACT 7 (sl3 side, in-run): the sl3-invariant trilinears on 3 x 3 x 3
    have dimension EXACTLY 1 and the survivor is totally antisymmetric
    (eps unique) — the family factor could not have been anything else.

=> THE RESULT: in the E8 channel the three-family Yukawa is
   eps_family (x) C_Jordan — nonzero ONLY with one leg from each family.
   Same-family (diagonal) Yukawa couplings are identically zero.
"""
import itertools
from fractions import Fraction as F
from collections import Counter, defaultdict
SCR=__import__('os').path.dirname(__import__('os').path.abspath(__file__))+""
exec(open(SCR+'/e7_ladder.py').read().split("CART={")[0])

CART_E8=[[2,-1,0,0,0,0,0,0],[-1,2,-1,0,0,0,0,0],[0,-1,2,-1,0,0,0,-1],[0,0,-1,2,-1,0,0,0],[0,0,0,-1,2,-1,0,0],[0,0,0,0,-1,2,-1,0],[0,0,0,0,0,-1,2,0],[0,0,-1,0,0,0,0,2]]
alg=build_algebra(CART_E8)
assert alg['DIM']==248 and len(alg['roots'])==240
n=alg['n']; ipr=alg['ipr']; allr=alg['roots']; br=alg['br']; evec=alg['evec']
eps=alg['eps']; IDX=alg['IDX']
rootset=set(allr)
def neg(r): return tuple(-x for x in r)

# FACT 1: the four slots, the family block
S0,S1,S2,T1,T2,color=slots_and_triples(alg)
perp3=[r for r in allr if all(ipr(r,s)==0 for s in S0|S1|S2)]
def find_a2(pool):
    for r1 in pool:
        for r2 in pool:
            if r2!=r1 and ipr(r1,r2)==-1 and tuple(x+y for x,y in zip(r1,r2)) in pool:
                return r1,r2
f1,f2=find_a2(perp3)
S3=set(perp3)
for name,S in (('S0',S0),('S1',S1),('S2',S2),('S3',S3)):
    comp=[r for r in allr if all(ipr(r,s)==0 for s in S)]
    crossing=[r for r in allr if r not in S and any(ipr(r,s)!=0 for s in S)]
    assert len(comp)==72 and len(crossing)==162
assert len(S3)==6
crossing=[r for r in allr if r not in S3 and any(ipr(r,s)!=0 for s in S3)]
proj=lambda r:(ipr(r,f1),ipr(r,f2))
classes=Counter(proj(r) for r in crossing)
assert len(classes)==6 and all(v==27 for v in classes.values())
TRIPLET=[(1,0),(-1,1),(0,-1)]
assert all(t in classes for t in TRIPLET)
assert tuple(sum(x) for x in zip(*TRIPLET))==(0,0)
FAM=[r for r in crossing if proj(r) in TRIPLET]
assert len(FAM)==81
FAMset=set(FAM)
mu={t:i for i,t in enumerate(sorted(TRIPLET))}   # lexicographic family order 0,1,2
print("FACT 1: four A2 slots re-anchored (72-root e6 complement, 162 crossing,")
print(f"        6 classes x 27); family block = 81 roots over triplet weights {sorted(TRIPLET)}")

# internal labels: pair against 6 independent complement roots
comp=[r for r in allr if all(ipr(r,s)==0 for s in S3)]
base6=[]
import fractions
def indep(cand,rows):
    M=[list(map(F,row)) for row in rows]+[list(map(F,cand))]
    r=0
    for c in range(len(cand)):
        p=next((i for i in range(r,len(M)) if M[i][c]!=0),None)
        if p is None: continue
        M[r],M[p]=M[p],M[r]
        pv=M[r][c]; M[r]=[x/pv for x in M[r]]
        for i in range(len(M)):
            if i!=r and M[i][c]!=0:
                fq=M[i][c]; M[i]=[x-fq*y for x,y in zip(M[i],M[r])]
        r+=1
    return r==len(rows)+1
for r in comp:
    if len(base6)==6: break
    if indep(r,base6): base6.append(r)
assert len(base6)==6
ilab={r:tuple(ipr(r,c) for c in base6) for r in FAM}
for t in TRIPLET:
    blk=[ilab[r] for r in FAM if proj(r)==t]
    assert len(set(blk))==27
print("        internal labels: 27 distinct e6-weights per family block")

# FACT 2: zero-sum support
FAMs=sorted(FAM)
triples=[]
for i,r in enumerate(FAMs):
    for j in range(i+1,len(FAMs)):
        s_=FAMs[j]
        t_=neg(tuple(a+b for a,b in zip(r,s_)))
        if t_ in FAMset and t_>s_: triples.append((r,s_,t_))
assert len(triples)==270
for (r,s_,t_) in triples:
    fams={proj(r),proj(s_),proj(t_)}
    assert len(fams)==3, "same-family triple found!"
itri=Counter(tuple(sorted((ilab[r],ilab[s_],ilab[t_]))) for (r,s_,t_) in triples)
assert len(itri)==45 and all(v==6 for v in itri.values())
print(f"FACT 2: zero-sum triples in the family block: {len(triples)} = 45 internal")
print("        weight-zero triples x 6 family assignments; EVERY triple has three")
print("        DISTINCT families — no same-family triple exists at all")

# FACT 3: kappa by exact ad-trace
DIM=alg['DIM']
def adtrace_pair(r):
    er=evec(r); enr=evec(neg(r)); tot=F(0)
    for p in range(DIM):
        z=[F(0)]*DIM; z[p]=F(1)
        w=br(enr,z)
        if all(x==0 for x in w): continue
        w2=br(er,w)
        tot+=w2[p]
    return tot
kaps={r:adtrace_pair(r) for r in FAM}
kvals=set(kaps.values())
assert len(kvals)==1
kap=kvals.pop()
print(f"FACT 3: kappa(r) = tr(ad e_r ad e_-r) = {kap} for ALL 81 family roots (exact)")

# T on ordered support: T(r,s,t) = K(e_r,[e_s,e_t]) = kappa * eps(s,t) when r+s+t=0
T={}
for (r,s_,t_) in triples:
    for (x,y,z) in itertools.permutations((r,s_,t_)):
        w=br(evec(y),evec(z))
        coef=w[n+IDX[neg(x)]]
        assert coef!=0
        T[(x,y,z)]=kap*coef
assert len(T)==1620

# FACT 4: invariance under all 72 complement + 6 family-A2 root vectors
gens=list(comp)+sorted(S3)
def deriv_zero(g):
    actinv=defaultdict(list)   # y -> [(x, sign)] with [e_g, e_x] = sign e_y
    for x in FAM:
        y=tuple(a+b for a,b in zip(g,x))
        if y in FAMset: actinv[y].append((x,eps(g,x)))
    Z=defaultdict(F)
    for (r,s_,t_),val in T.items():
        for (x,sg) in actinv.get(r,[]): Z[(x,s_,t_)]+=sg*val
        for (x,sg) in actinv.get(s_,[]): Z[(r,x,t_)]+=sg*val
        for (x,sg) in actinv.get(t_,[]): Z[(r,s_,x)]+=sg*val
    return all(v==0 for v in Z.values())
ok4=all(deriv_zero(g) for g in gens)
print(f"FACT 4: derivation identity = 0 for all {len(gens)} generators (72 e6 + 6 family A2): {ok4}")
assert ok4

# FACT 5: total antisymmetry
sgn={p:s for p,s in zip(itertools.permutations((0,1,2)),(1,-1,-1,1,1,-1))}
sgn={(0,1,2):1,(0,2,1):-1,(1,0,2):-1,(1,2,0):1,(2,0,1):1,(2,1,0):-1}
ok5=True
for (r,s_,t_) in triples:
    base=T[(r,s_,t_)]
    args=(r,s_,t_)
    for p,sg in sgn.items():
        if T[(args[p[0]],args[p[1]],args[p[2]])]!=sg*base: ok5=False
print(f"FACT 5: T totally ANTISYMMETRIC on all 270 x 6 entries: {ok5}")
assert ok5

# FACT 6: exact factorization, gauge-corrected
famof={r:mu[proj(r)] for r in FAM}
Cp={}
for (r,s_,t_) in triples:
    order=sorted((r,s_,t_),key=lambda x:famof[x])
    key=(ilab[order[0]],ilab[order[1]],ilab[order[2]])
    Cp[key]=T[(order[0],order[1],order[2])]
assert len(Cp)==270  # ordered by family: 45 internal triples x 6 internal orders
vals=set(Cp.values())
ok6b=vals=={kap,-kap}
# raw symmetry test (the first draft's refuted assert, kept as a report):
raw_sym=True
for (a,b,c),v in Cp.items():
    for p in sgn:
        key=((a,b,c)[p[0]],(a,b,c)[p[1]],(a,b,c)[p[2]])
        if Cp.get(key)!=v: raw_sym=False
print(f"FACT 6: values one constant x +-1: {ok6b}; RAW C' symmetric: {raw_sym}")
print("        (raw asymmetry = the per-root Chevalley sign gauge; error filed)")
assert ok6b and not raw_sym
# gauge solve over GF(2): unknowns sigma_{i,label} (81) + S_{unordered triple} (45)
labels=sorted({ilab[r] for r in FAM})
sidx={(i,l):(27*i+labels.index(l)) for i in range(3) for l in labels}
utri=sorted(itri)
Sidx={t:81+k for k,t in enumerate(utri)}
NV=81+45
eqs=[]
for (a,b,c),v in Cp.items():
    bit=0 if v==kap else 1
    row=[0]*(NV+1)
    row[sidx[(0,a)]]^=1; row[sidx[(1,b)]]^=1; row[sidx[(2,c)]]^=1
    row[Sidx[tuple(sorted((a,b,c)))]]^=1
    row[NV]=bit
    eqs.append(row)
# GF(2) elimination
r=0
for c in range(NV):
    p=next((i for i in range(r,len(eqs)) if eqs[i][c]),None)
    if p is None: continue
    eqs[r],eqs[p]=eqs[p],eqs[r]
    for i in range(len(eqs)):
        if i!=r and eqs[i][c]:
            eqs[i]=[x^y for x,y in zip(eqs[i],eqs[r])]
    r+=1
consistent=all(not row[NV] or any(row[c] for c in range(NV)) for row in eqs)
print(f"        GF(2) gauge system: {len(Cp)} equations, {NV} unknowns, rank {r}, consistent: {consistent}")
assert consistent
# extract one solution (free vars = 0)
sol=[0]*NV
for row in eqs:
    piv=next((c for c in range(NV) if row[c]),None)
    if piv is None: continue
    sol[piv]=row[NV]^0
    for c in range(piv+1,NV):
        if row[c] and sol[c]: sol[piv]^=1
# note: with free vars fixed to 0 the back-substitution above is exact because
# eqs is in reduced row-echelon form (full elimination above and below pivots)
sigma=lambda i,l: -1 if sol[sidx[(i,l)]] else 1
Ssign=lambda t: -1 if sol[Sidx[t]] else 1
# forward verification on ALL 1620 ordered entries
famsgn={(0,1,2):1,(0,2,1):-1,(1,0,2):-1,(1,2,0):1,(2,0,1):1,(2,1,0):-1}
ok6d=True
for (x,y,z),val in T.items():
    fi,fj,fk=famof[x],famof[y],famof[z]
    a,b,c=ilab[x],ilab[y],ilab[z]
    pred=kap*famsgn[(fi,fj,fk)]*sigma(fi,a)*sigma(fj,b)*sigma(fk,c)*Ssign(tuple(sorted((a,b,c))))
    if pred!=val: ok6d=False
print(f"        forward check T = kappa * sgn(fam) * sigma sigma sigma * S on all 1620 entries: {ok6d}")
assert ok6d
print("        => in the sigma-rescaled basis, T = eps_family (x) C_sym EXACTLY;")
print("        C_sym is e6-invariant (FACT 4) + symmetric + support 45 => by the")
print("        banked dim-1 count (memo 48 rung 3) it IS the Jordan cubic up to scale")

# FACT 7: sl3 uniqueness of the family factor, in-run
E12=[[0,1,0],[0,0,0],[0,0,0]]; E23=[[0,0,0],[0,0,1],[0,0,0]]
E21=[[0,0,0],[1,0,0],[0,0,0]]; E32=[[0,0,0],[0,0,0],[0,1,0]]
rows=[]
for M in (E12,E23,E21,E32):
    for (i,j,k) in itertools.product(range(3),repeat=3):
        row=[0]*27
        for l in range(3):
            if M[l][i]: row[9*l+3*j+k]+=M[l][i]
            if M[l][j]: row[9*i+3*l+k]+=M[l][j]
            if M[l][k]: row[9*i+3*j+l]+=M[l][k]
        if any(row): rows.append([F(x) for x in row])
def nullsp(rows,nn):
    M=[r[:] for r in rows]; r=0; piv=[]
    for c in range(nn):
        p=next((i for i in range(r,len(M)) if M[i][c]!=0),None)
        if p is None: continue
        M[r],M[p]=M[p],M[r]
        pv=M[r][c]; M[r]=[x/pv for x in M[r]]
        for i in range(len(M)):
            if i!=r and M[i][c]!=0:
                fq=M[i][c]; M[i]=[x-fq*y for x,y in zip(M[i],M[r])]
        piv.append(c); r+=1
    free=[c for c in range(nn) if c not in piv]
    out=[]
    for fc in free:
        v=[F(0)]*nn; v[fc]=F(1)
        for i,c in enumerate(piv): v[c]=-M[i][fc]
        out.append(v)
    return out
NS=nullsp(rows,27)
assert len(NS)==1
v=NS[0]
anti=all(v[9*i+3*j+k]==-v[9*j+3*i+k] and v[9*i+3*j+k]==-v[9*i+3*k+j] for i in range(3) for j in range(3) for k in range(3))
print(f"FACT 7: sl3-invariant trilinears on 3x3x3: dim = {len(NS)}, survivor totally antisymmetric: {anti} (= eps)")
assert anti

print(f"""
THE THREE-FAMILY YUKAWA IS INTER-FAMILY (E8 channel, possibility space):
the bracket-induced coupling on the G-3 family triplet of 27's is EXACTLY
eps_family (x) C_Jordan — verified entry by entry, invariance and
factorization computed, both factors unique.  Its support has one leg from
each family always: same-family (diagonal) Yukawa couplings are IDENTICALLY
ZERO in this channel — not suppressed, absent.  E8 is not object-paid (G-3
fence stands); what is object-paid is the internal factor, which is forced
to be the object's own unique coupling (memos 32/47/48).  Structure only;
Gate 5 untouched.""")
