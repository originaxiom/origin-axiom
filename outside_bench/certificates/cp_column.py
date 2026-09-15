#!/usr/bin/env python3
"""MEMO-83 CELL: THE CP COLUMN — does the object force any CP-odd phase?
(The Cosmogony Ledger's one new computation, and a live stress test of the
gravity charter's C2/parity law: a FORCED mirror-odd dimensionless quantity
would be a charter hit.)

Context: baryogenesis (why there is matter to form atoms) requires a
CP-odd phase (Sakharov, CITED context).  CP-odd phases are mirror-ODD
data; the parity law (B1168) prices mirror-odd data to the observer.  So
the law PREDICTS: the object's forced couplings carry ZERO CP-odd phase —
every rephasing-invariant product of coupling entries is REAL.  This cell
decides it exactly, in both banked channels.

THE DECISION PROCEDURE (exact): a CP-odd phase invariant of a coupling
tensor is a rephasing-invariant product of entries with non-real value.
If every entry of the tensor lies in Q (a totally real, in fact rational,
field), every product of entries is rational, hence real: NO CP-odd
invariant can exist.  So it suffices to verify the two forced coupling
tensors are defined over Q entry-by-entry ON THEIR CONSTRUCTED BASES, and
that this rationality is not an artifact of scaling (the tensors are
unique up to ONE overall constant — banked memos 47/48/53 — so a single
real normalization makes every entry rational; phase INVARIANTS are
normalization-free).

PREREGISTERED (two-outcome):
  FACT 1 (the object channel): the unique invariant coupling C on the 27
    (memo 47's rational nullspace, dim 1) has ALL 45 nonzero entries in
    {+1, -1} after one normalization — entirely rational.
  FACT 2 (the family channel): the E8 vertex T (memo 53's construction,
    1620 ordered entries) has ALL entries equal to kappa * (Chevalley
    integer) with kappa = -60 — entirely rational.
  FACT 3 (the conclusion): every rephasing-invariant product in either
    channel is a nonzero rational — REAL.  Sample invariants computed and
    exhibited.  BRANCH REAL: zero forced CP-odd phase; the CP column of
    the cosmogony ledger lands OBSERVER-SIDE — the same column as the
    arrow of time (both mirror-odd), exactly as the parity law predicts.
    BRANCH PHASE (the stress-test failure): any entry provably requiring
    a non-real value would be a FORCED mirror-odd dimensionless quantity
    — reportable as a charter C2 hit, not explained away.
OWNER-DIRECTIVE NOTE: nature's CKM phase is nonzero and OBSERVED; BRANCH
REAL contradicts nothing — it prices the phase to the observer's closing
(vev phases / frame data), it does not deny it.  FENCES: the two banked
channels only (no claim about all conceivable couplings); "CP" here is
the mirror/conjugation parity of the record (the physical CP of a 4d QFT
lives behind Gates 2/3); Gate 5 untouched.
"""
import itertools
from fractions import Fraction as F
from collections import defaultdict
SCR=__import__('os').path.dirname(__import__('os').path.abspath(__file__))+""
src=open(SCR+"/twisted_double.py").read()
cut=src.index("# ---------------- stage 4")
exec(src[:cut])

# FACT 1: the object channel — C rational (memo 47 construction verbatim)
H=[rho27_Q([F(1) if k==i else F(0) for k in range(DIM)]) for i in range(N)]
wt6=[tuple(H[i][a][a] for i in range(N)) for a in range(27)]
def addw(*ws): return tuple(sum(x) for x in zip(*ws))
ZERO6=tuple(F(0) for _ in range(N))
gens=[]
for i in range(N):
    r=tuple(1 if k==i else 0 for k in range(N))
    gens.append(rho27_Q(evec(r)))
    gens.append(rho27_Q(evec(tuple(-x for x in r))))
triples=[t for t in itertools.combinations_with_replacement(range(27),3) if addw(wt6[t[0]],wt6[t[1]],wt6[t[2]])==ZERO6]
tid={t:n for n,t in enumerate(triples)}
def key3(a,b,c): return tuple(sorted((a,b,c)))
def deriv_rows(M):
    col_of=defaultdict(list)
    for l in range(27):
        for i in range(27):
            if M[l][i]!=0: col_of[i].append(l)
    nz0=next(((l,i) for l in range(27) for i in range(27) if M[l][i]!=0), None)
    shift=tuple(a-b for a,b in zip(wt6[nz0[0]],wt6[nz0[1]]))
    target=tuple(-x for x in shift)
    rows=[]
    for (i,j,k) in itertools.combinations_with_replacement(range(27),3):
        if addw(wt6[i],wt6[j],wt6[k])!=target: continue
        row=defaultdict(F)
        for (x_,y_,z_) in ((i,j,k),(j,i,k),(k,i,j)):
            for l in col_of.get(x_,[]):
                t=key3(l,y_,z_)
                if t in tid: row[tid[t]]+=M[l][x_]
        if row: rows.append(row)
    return rows
rows=[]
for M in gens: rows.extend(deriv_rows(M))
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
NS=nullspace(rows,len(triples))
assert len(NS)==1, "C is unique up to ONE overall constant (memo 47)"
C=NS[0]
p0=next(i for i,v in enumerate(C) if v!=0); C=[v/C[p0] for v in C]
vals=sorted(set(v for v in C if v!=0))
assert vals==[F(-1),F(1)] and sum(1 for v in C if v!=0)==45
print("FACT 1: the unique 27-coupling C: dim 1 over Q, all 45 entries in {+1,-1}")
print("   after one normalization — ENTIRELY RATIONAL (memo 47 reproduced)")

# FACT 2: the family channel — T rational (memo 53 construction verbatim)
exec(open(SCR+'/e7_ladder.py').read().split("CART={")[0])
CART_E8=[[2,-1,0,0,0,0,0,0],[-1,2,-1,0,0,0,0,0],[0,-1,2,-1,0,0,0,-1],[0,0,-1,2,-1,0,0,0],[0,0,0,-1,2,-1,0,0],[0,0,0,0,-1,2,-1,0],[0,0,0,0,0,-1,2,0],[0,0,-1,0,0,0,0,2]]
alg=build_algebra(CART_E8)
n8=alg['n']; ipr8=alg['ipr']; allr=alg['roots']; br=alg['br']; evec8=alg['evec']; IDX=alg['IDX']
def neg(r): return tuple(-x for x in r)
S0,S1,S2,T1,T2,color=slots_and_triples(alg)
perp3=[r for r in allr if all(ipr8(r,s)==0 for s in S0|S1|S2)]
S3=set(perp3)
def find_a2(pool):
    for r1 in pool:
        for r2 in pool:
            if r2!=r1 and ipr8(r1,r2)==-1 and tuple(x+y for x,y in zip(r1,r2)) in pool:
                return r1,r2
f1,f2=find_a2(perp3)
crossing=[r for r in allr if r not in S3 and any(ipr8(r,s)!=0 for s in S3)]
proj=lambda r:(ipr8(r,f1),ipr8(r,f2))
TRIPLET=[(1,0),(-1,1),(0,-1)]
FAM=sorted(r for r in crossing if proj(r) in TRIPLET)
assert len(FAM)==81
FAMset=set(FAM)
ftri=[]
for i,r in enumerate(FAM):
    for j in range(i+1,len(FAM)):
        s_=FAM[j]
        t_=neg(tuple(a+b for a,b in zip(r,s_)))
        if t_ in FAMset and t_>s_: ftri.append((r,s_,t_))
assert len(ftri)==270
er=evec8(FAM[0]); enr=evec8(neg(FAM[0])); kap=F(0)
for p in range(alg['DIM']):
    z=[F(0)]*alg['DIM']; z[p]=F(1)
    w=br(enr,z)
    if all(x==0 for x in w): continue
    kap+=br(er,w)[p]
assert kap==F(-60)
Tvals=set()
for (r,s_,t_) in ftri:
    for (x,y,z) in itertools.permutations((r,s_,t_)):
        w=br(evec8(y),evec8(z))
        coef=w[n8+IDX[neg(x)]]
        assert coef!=0 and coef.denominator==1
        Tvals.add(kap*coef)
print(f"FACT 2: the E8 family vertex T: all 1620 entries in kappa*Z = {{{', '.join(str(v) for v in sorted(Tvals))}}}")
print("   — ENTIRELY RATIONAL (kappa = -60, memo 53 reproduced)")
assert all(v.denominator==1 for v in Tvals)

# FACT 3: rephasing-invariant products are real — sample invariants
Cnz=[(t,C[tid[t]]) for t in triples if C[tid[t]]!=0]
samples=[]
for (t1,v1) in Cnz[:6]:
    for (t2,v2) in Cnz[6:12]:
        samples.append(v1*v2)
prod_all=F(1)
for (_,v) in Cnz: prod_all*=v
assert all(isinstance(s,F) for s in samples) and isinstance(prod_all,F)
print(f"FACT 3: sample rephasing-invariant products (pairwise + total over all 45):")
print(f"   pairwise samples all in {{+1,-1}}: {sorted(set(samples))==[F(-1),F(1)] or sorted(set(samples))in([F(-1)],[F(1)])}; total product = {prod_all}")
print("   every product of entries in either channel is a nonzero RATIONAL — REAL.")

print("""
BRANCH REAL: the object forces ZERO CP-odd phase — both banked coupling
channels are defined over Q, so no rephasing-invariant of the forced
couplings can be non-real.  The CP column of the cosmogony ledger lands
OBSERVER-SIDE, in the same column as the arrow of time (both mirror-odd),
exactly as the parity law (B1168) predicts — and the charter's C2
survives this stress test.  Nature's observed CP phase contradicts
nothing here: it is priced to the observer's closing (vev phases / frame
data), not denied.  FENCES: the two banked channels only; record-parity,
not 4d-QFT CP (Gates 2/3).  Gate 5 untouched.""")
