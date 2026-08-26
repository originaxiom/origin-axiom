#!/usr/bin/env python3
"""MEMO-82 CELL (WAVE-3 MB2): THE FAMILY RANK THEOREM — in the record's
only three-family channel, EVERY family-Yukawa matrix has rank exactly 2,
and its massless direction is the Higgs's own family.  (cc's B1162
meditation SS-B: another forced DIMENSIONLESS structure — a rank, not a
value.)

Channel and fence: the E8 family triplet (3,27) — the record's only true
three-copy structure (memo 74) — with its forced coupling (memo 53:
eps_family (x) C_Jordan, factorization proven from the full tensor).  E8
is possibility-space, not object-paid (banked fence, memos 53/62/74).

CONSTRUCTION (memo 53's machinery rebuilt verbatim; then the new theorem
checked on the FULL tensor T, not on the factorization): for each of the
45 internal weight-zero triples (ia, ib, ic), each choice of the Higgs leg
(the internal weight carried by the scalar), and each Higgs family f3, the
FAMILY MATRIX is
    M[f1][f2] = T( root(f1,ia), root(f2,ib), root(f3,ic) )
(zero when the root triple is not in the support).

PREREGISTERED (asserts, per matrix — 45 triples x 6 leg assignments x 3 Higgs families = 810 matrices):
  (i)   M has EXACTLY 2 nonzero entries, at TRANSPOSED off-diagonal
        positions spanning the two non-Higgs families;
  (ii)  det M = 0 and rank M = 2 EXACTLY;
  (iii) ker M = the line spanned by e_{f3} — the Higgs's own family.
[ERROR FILED AT POINT OF OCCURRENCE: the first draft also preregistered
VALUE-antisymmetry M[i][j] = -M[j][i] on the raw entries.  The machine
refused — the SAME sigma-gauge trap the bench fell into (and filed) in
memo 62/53: raw Chevalley entries carry per-root signs, and antisymmetry
is a statement in the sigma-degauged basis (banked, memo 53), not the raw
one.  Hit twice, caught twice by the machine; the gauge-INVARIANT facts
(i)-(iii) are what this cell asserts, and they alone carry the theorem.]
THE THEOREM (if all 810 pass): every Yukawa matrix in the three-family
channel annihilates exactly one family direction — the family the Higgs
itself occupies.  AT LEAST ONE EXACTLY-MASSLESS FAMILY PER COUPLING is a
rank statement forced by the coupling's antisymmetry; no value, no
hierarchy, no scale (Gate 5 untouched).  Distinct from BOTH walls on
record: cc's SEAM-Y (mu_u = 0, their bundle) and the object channel's
existing up-shape (memo 80) — channels differ; the rhyme-fence of memo 75
is maintained, mechanisms now three and all named.
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
def neg(r): return tuple(-x for x in r)

S0,S1,S2,T1,T2,color=slots_and_triples(alg)
perp3=[r for r in allr if all(ipr(r,s)==0 for s in S0|S1|S2)]
S3=set(perp3)
assert len(S3)==6
def find_a2(pool):
    for r1 in pool:
        for r2 in pool:
            if r2!=r1 and ipr(r1,r2)==-1 and tuple(x+y for x,y in zip(r1,r2)) in pool:
                return r1,r2
f1,f2=find_a2(perp3)
crossing=[r for r in allr if r not in S3 and any(ipr(r,s)!=0 for s in S3)]
proj=lambda r:(ipr(r,f1),ipr(r,f2))
TRIPLET=[(1,0),(-1,1),(0,-1)]
FAM=[r for r in crossing if proj(r) in TRIPLET]
assert len(FAM)==81
FAMset=set(FAM)
famidx={t:i for i,t in enumerate(sorted(TRIPLET))}
comp=[r for r in allr if all(ipr(r,s)==0 for s in S3)]
base6=[]
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
ilab={r:tuple(ipr(r,c) for c in base6) for r in FAM}
state={(famidx[proj(r)], ilab[r]): r for r in FAM}
assert len(state)==81
print("frame re-anchored: 81 family roots = 3 families x 27 internal weights")

FAMs=sorted(FAM)
triples=[]
for i,r in enumerate(FAMs):
    for j in range(i+1,len(FAMs)):
        s_=FAMs[j]
        t_=neg(tuple(a+b for a,b in zip(r,s_)))
        if t_ in FAMset and t_>s_: triples.append((r,s_,t_))
assert len(triples)==270
kapset=set()
DIM=alg['DIM']
r0f=FAMs[0]
er=evec(r0f); enr=evec(neg(r0f)); tot=F(0)
for p in range(DIM):
    z=[F(0)]*DIM; z[p]=F(1)
    w=br(enr,z)
    if all(x==0 for x in w): continue
    w2=br(er,w)
    tot+=w2[p]
kap=tot
T={}
for (r,s_,t_) in triples:
    for (x,y,z) in itertools.permutations((r,s_,t_)):
        w=br(evec(y),evec(z))
        coef=w[n+IDX[neg(x)]]
        assert coef!=0
        T[(x,y,z)]=kap*coef
assert len(T)==1620
print(f"vertex rebuilt: 1620 ordered entries (kappa = {kap}; memo 53 reproduced)")

# the 45 internal weight-zero triples
itri=sorted(set(tuple(sorted((ilab[r],ilab[s_],ilab[t_]))) for (r,s_,t_) in triples))
assert len(itri)==45

def Tval(x,y,z):
    return T.get((x,y,z), F(0))

checked=0; kernel_ok=0
for (ia,ib,ic) in itri:
    # all assignments of the three internal weights to (leg1, leg2, Higgs)
    for (wa,wb,wc) in set(itertools.permutations((ia,ib,ic))):
        for f3 in range(3):
            rc=state[(f3,wc)]
            M=[[F(0)]*3 for _ in range(3)]
            for fa in range(3):
                for fb in range(3):
                    ra=state.get((fa,wa)); rb=state.get((fb,wb))
                    M[fa][fb]=Tval(ra,rb,rc)
            nz=[(i,j) for i in range(3) for j in range(3) if M[i][j]!=0]
            assert len(nz)==2, f"expected 2 nonzero entries, got {nz}"
            (i1,j1),(i2,j2)=nz
            # positions transposed; VALUE antisymmetry is sigma-gauge only (error filed)
            assert (i2,j2)==(j1,i1) and i1!=j1, "transposed off-diagonal pair"
            assert {i1,j1}=={0,1,2}-{f3}, "support must be the two non-Higgs families"
            det=(M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
                -M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
                +M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))
            assert det==0
            minor=M[i1][j1]*M[j1][i1]-M[i1][i1]*M[j1][j1]
            assert minor!=0, "rank must be exactly 2"
            # kernel = e_{f3}
            ev=[F(0)]*3; ev[f3]=F(1)
            img=[sum(M[i][j]*ev[j] for j in range(3)) for i in range(3)]
            assert all(x==0 for x in img)
            checked+=1; kernel_ok+=1
print(f"THE THEOREM: {checked} family matrices checked (45 internal triples x leg")
print(f"   assignments x 3 Higgs families): ALL with exactly 2 nonzero")
print(f"   transposed entries, det = 0, rank EXACTLY 2, kernel = the Higgs's own family: {kernel_ok}/{checked}")

print("""
THE FAMILY RANK THEOREM: in the record's three-family channel, every
Yukawa matrix annihilates EXACTLY ONE family direction — the family the
Higgs itself occupies.  One exactly-massless family per coupling is
FORCED, dimensionless, by the sigma-gauge antisymmetry of the unique vertex (memo 53); which
family is massless is set by where the Higgs sits (an observer/vacuum
question, priced, not answered).  No value, no hierarchy, no scale.
FENCES: E8 possibility-space (memos 53/62/74); distinct from cc's SEAM-Y
wall and from the object channel's existing up-shape (memo 80) — three
Yukawa mechanisms on record, all named, none identified with another.
Gate 5 untouched.""")
