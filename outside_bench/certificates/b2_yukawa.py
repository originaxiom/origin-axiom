#!/usr/bin/env python3
"""B2: THE YUKAWA COUNT — how many independent Yukawa-shaped couplings does the
trinification closing admit on the 27?  Structure only; no values.

Under full e6 the symmetric-trilinear invariant space on the 27 is 1-dim (memo
32: the Jordan cubic C).  Under the CLOSING's subalgebra — the orthogonal A2
triple sl3+sl3+sl3 (trinification; maximal rank, same Cartan) — the space is
classically expected to be 4-dim: det(a) + det(b) + det(c) + tr(abc)-type, one
per slot plus the mixed trace, of which only one combination survives to e6.
PREREGISTERED two-outcome: dim = 4 (the classical count realized exactly on the
bench's crystal basis) or dim != 4 (a finding either way).

Method: same exact derivation machinery as jordan_beat.py, but constraint rows
only from the 18 root generators (+/-) of an orthogonal A2-triple found from
scratch in this frame; unknowns = the same 45 weight-zero triples (the
subalgebra has full rank).  Then: C (memo 32's cubic, re-derived in-run) lies
in the 4-space; and the 4-space decomposes as 3 slot-dets + 1 mixed piece,
identified by support on the 27's three 9-dim slot blocks.
"""
import itertools
from fractions import Fraction as F
from collections import defaultdict
SCR=__import__('os').path.dirname(__import__('os').path.abspath(__file__))+""
src=open(SCR+"/twisted_double.py").read()
cut=src.index("# ---------------- stage 4")
exec(src[:cut])

# weights of the 27
H=[rho27_Q(hv) for hv in ( [F(1) if k==i else F(0) for k in range(DIM)] for i in range(N) )]
wt=[tuple(H[i][a][a] for i in range(N)) for a in range(27)]
def addw(*ws): return tuple(sum(x) for x in zip(*ws))
ZERO6=tuple(F(0) for _ in range(N))

# ---- find an orthogonal A2 triple (18 roots) from scratch in THIS frame
def iprod(r,s):
    # exact root inner product via the Cartan pairing: <r,s> = sum r_i * (A s)_i /?
    # use: <r,s> = r . (A @ s) with A recovered from brackets — but simpler:
    # roots stored as simple-root coefficient vectors; use the E6 Cartan matrix
    return sum(r[i]*As[i] for i,As in [(i,sum(CART[i][j]*s[j] for j in range(N))) for i in range(N)])
CART=[[2,0,-1,0,0,0],[0,2,0,-1,0,0],[-1,0,2,-1,0,0],[0,-1,-1,2,-1,0],[0,0,0,-1,2,-1],[0,0,0,0,-1,2]]
# verify CART against brackets (as cp1_strata did)
for j in range(N):
    hj=[F(0)]*DIM; hj[j]=F(1)
    for i in range(N):
        r=tuple(1 if k==i else 0 for k in range(N))
        ei=evec(r); brr=br(hj,ei)
        val=next(brr[k]/ei[k] for k in range(DIM) if ei[k]!=0)
        assert val==CART[i][j], "Cartan mismatch"
def ip2(r,s): return sum(r[i]*sum(CART[i][j]*s[j] for j in range(N)) for i in range(N))//1
POS=[r for r in ROOTS if r>tuple([0]*N) or (sum(x for x in r)>0)]
# A2 subsystems: pairs (r,s), ip=-1; the subsystem = {±r,±s,±(r+s)}
def a2sys(r,s): return {r,s,tuple(a+b for a,b in zip(r,s)),tuple(-x for x in r),tuple(-x for x in s),tuple(-(a+b) for a,b in zip(r,s))}
Rset=set(ROOTS)
found=None
pairs=[(r,s) for r,s in itertools.combinations(ROOTS,2) if ip2(r,s)==-1 and tuple(a+b for a,b in zip(r,s)) in Rset]
import random
random.seed(1)
for (r1,s1) in pairs:
    S1_=a2sys(r1,s1)
    rest1=[p for p in pairs if all(ip2(p[0],t)==0 and ip2(p[1],t)==0 for t in (r1,s1))]
    for (r2,s2) in rest1:
        S2_=a2sys(r2,s2)
        if S2_&S1_: continue
        rest2=[p for p in rest1 if all(ip2(p[0],t)==0 and ip2(p[1],t)==0 for t in (r2,s2))]
        for (r3,s3) in rest2:
            S3_=a2sys(r3,s3)
            if (S3_&S1_) or (S3_&S2_): continue
            found=(S1_,S2_,S3_); break
        if found: break
    if found: break
assert found, "no orthogonal A2 triple found"
T18=set().union(*found)
print(f"orthogonal A2 triple found: 3 x 6 = {len(T18)} roots, pairwise orthogonal")
assert len(T18)==18

# ---- the 27's slot blocks: each basis index by which A2-slots act nontrivially
# (each 27-index belongs to a bi-fundamental of two of the three slots)
def slot_wt(a, S):
    # nonzero if some Cartan of that slot pairs nontrivially: use the two simple coweights of the slot
    tot=0
    for r in S:
        h=[F(0)]*DIM
        for k in range(N): h[k]=F(r[k])
        M=rho27_Q(h)
        if M[a][a]!=0: tot+=1
    return tot
blocks=defaultdict(list)
for a in range(27):
    sig=tuple(1 if slot_wt(a,Si)>0 else 0 for Si in found)
    blocks[sig].append(a)
print("27 slot-signature blocks:", {k:len(v) for k,v in blocks.items()})

# ---- invariant trilinears under the A2-triple subalgebra
triples=[t for t in itertools.combinations_with_replacement(range(27),3) if addw(wt[t[0]],wt[t[1]],wt[t[2]])==ZERO6]
tid={t:n for n,t in enumerate(triples)}
NT=len(triples)
print(f"weight-zero symmetric triples (full-rank Cartan shared): {NT}")
def key(a,b,c): return tuple(sorted((a,b,c)))
def deriv_rows(M):
    nz0=next(((l,i) for l in range(27) for i in range(27) if M[l][i]!=0), None)
    if nz0 is None: return []
    shift=tuple(a-b for a,b in zip(wt[nz0[0]],wt[nz0[1]]))
    target=tuple(-x for x in shift)
    col_of=defaultdict(list)
    for l in range(27):
        for i in range(27):
            if M[l][i]!=0: col_of[i].append(l)
    rows=[]
    for (i,j,k) in itertools.combinations_with_replacement(range(27),3):
        if addw(wt[i],wt[j],wt[k])!=target: continue
        row=defaultdict(F)
        for (x,y,z) in ((i,j,k),(j,i,k),(k,i,j)):
            for l in col_of.get(x,[]):
                t=key(l,y,z)
                if t in tid: row[tid[t]]+=M[l][x]
        if row: rows.append(row)
    return rows
def nullspace(rows, n):
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
    basis=[]
    for fc in free:
        v=[F(0)]*n; v[fc]=F(1)
        for i,col in enumerate(piv): v[col]=-dense[i][fc]
        basis.append(v)
    return basis
rows=[]
for r in sorted(T18):
    rows.extend(deriv_rows(rho27_Q(evec(r))))
NS=nullspace(rows, NT)
print(f"\nYUKAWA COUNT: dim of trinification-invariant symmetric trilinears on the 27 = {len(NS)}")
print("(preregistered: 4 = three slot-determinants + one mixed trace; e6 keeps 1)")

# e6 cubic C lies inside (re-derive quickly: add the remaining 54 generators' rows)
rows_full=list(rows)
for r in ROOTS:
    if r in T18: continue
    rows_full.extend(deriv_rows(rho27_Q(evec(r))))
NSe6=nullspace(rows_full, NT)
print(f"cross-check: adding the other 54 root generators cuts the space to dim = {len(NSe6)} (e6's 1)")
assert len(NSe6)==1

# identify the 4-space structurally: support of each basis vector on slot blocks
def support_blocks(vec):
    sup=set()
    for t,n_ in tid.items():
        if vec[n_]!=0:
            for a in t:
                sig=tuple(1 if slot_wt(a,Si)>0 else 0 for Si in found)
                sup.add(sig)
    return sup
for i,v in enumerate(NS):
    print(f"  basis vector {i}: {sum(1 for x in v if x!=0)} nonzero coeffs; touches blocks {sorted(support_blocks(v))}")

print(f"\nB2 banked: the closing admits EXACTLY {len(NS)} independent Yukawa-shaped")
print("couplings on one 27 (structure only, Gate 5 untouched); e6 selects the")
print("single Jordan combination among them (memo 32's C, the beat-covariant one).")
