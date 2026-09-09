#!/usr/bin/env python3
"""MEMO-52 CELL: THE YUKAWA READS THE CLOCK — the unique coupling's exact
selection rule over the meridian's depth grading.

Memo 50: the meridian grades the carrier into chains of length 3, 2, 1
(6/15/6), with odd chains = matter.  Memo 48: the unique coupling is
Y = eps (x) C.  This cell decomposes Y over the chain structure exactly.

The meridian's log is E_diag = e_2 (x) 1 + 1 (x) E27, part of a diagonal
sl2-triple (E,H,F) (the tautological triple tensor the bridge triple); the
Jordan chains ARE the sl2-strings (chain length = 2j+1).  Y is invariant
under this whole triple (eps under sl2, C under all of e6) — VERIFIED
DIRECTLY IN-RUN, not cited.  The string content:
    Psi:  6 chains of length 3 (locked), 15 of length 2 (unlocked),
          6 of length 1 (locked)          [memo 50]
    27 :  6 chains of length 2 (doublets), 15 of length 1 (singlets)

PREREGISTERED (two-outcome; every claim an assert):
  FACT A: Y's invariance under E, F, H verified directly on the sparse
    tensor (540 support entries; derivation identity = 0 for all three).
  FACT B: explicit chain-adapted string bases constructed and verified
    (E annihilates tops, steps up bottoms; counts 6/15/6 and 6/15; the
    change of basis is triangular w.r.t. weights, hence invertible).
  FACT C (the selection rule): writing s = chain length, Y's block
    (s1, s2, s3) on string-triples is IDENTICALLY ZERO for every triple
    forbidden by the sl2 triangle rule for (j = (s-1)/2), i.e. all of
      (3,1,*), (1,3,*), (3,3,2), (2,2,2), (1,1,2), (3,2,1), (2,3,1),
      (2,1,1), (1,2,1)   [11 blocks incl. both * values]
    — computed EXHAUSTIVELY on the string basis (weight-filtered), zero
    entry by entry, not cited from Clebsch.
  FACT D (the hit pattern, expected branch: ALL allowed blocks are hit):
    each of the 7 Clebsch-allowed blocks
      (3,3,1), (3,2,2), (2,3,2), (2,2,1), (2,1,2), (1,2,2), (1,1,1)
    contains a nonzero entry (exact witness each).  If some allowed block
    were empty that would be a STRONGER-than-representation-theory
    selection rule — the other preregistered branch.
  FACT E (the parity reading): every nonzero block has s1+s2+s3 ODD —
    the depth-level refinement of memo 47's {2-odd:30, 0-odd:15} rule.

Reading (interpretive, if D lands on the expected branch): depth-3 matter
chains couple to each other ONLY through internal singlets and to the
unlocked depth-2 chains ONLY through internal doublets; total chain length
is conserved mod 2 at every vertex.
"""
import itertools
from fractions import Fraction as F
from collections import Counter, defaultdict
SCR=__import__('os').path.dirname(__import__('os').path.abspath(__file__))+""
src=open(SCR+"/twisted_double.py").read()
cut=src.index("# ---------------- stage 4")
exec(src[:cut])

# ---- weights and bridge triple on the 27 (rational)
r0=ROOTS[0]
E27=rho27_Q(evec(r0))
F27=rho27_Q([-x for x in evec(tuple(-t for t in r0))])
hA=[F(0)]*DIM
for k in range(N): hA[k]=F(r0[k])
Hint=rho27_Q(hA)
wt=[int(Hint[a][a]) for a in range(27)]
assert dict(Counter(wt))=={1:6,0:15,-1:6}
# triple check: [E27,F27] = Hint
def mmQ(X,Y):
    n=len(X); m=len(Y[0])
    out=[[F(0)]*m for _ in range(n)]
    for i in range(n):
        for k in range(len(Y)):
            if X[i][k]==0: continue
            x=X[i][k]
            for j in range(m):
                if Y[k][j]!=0: out[i][j]+=x*Y[k][j]
    return out
comm=[[a-b for a,b in zip(r1,r2)] for r1,r2 in zip(mmQ(E27,F27),mmQ(F27,E27))]
assert comm==Hint
print("bridge sl2 triple on the 27: [E,F] = H verified")

# ---- rebuild C in-run: full-tensor e6-invariant on 27x27x27 (memo 48's rung 3)
Hs=[rho27_Q([F(1) if k==i else F(0) for k in range(DIM)]) for i in range(N)]
wt6=[tuple(Hs[i][a][a] for i in range(N)) for a in range(27)]
def addw(*ws): return tuple(sum(x) for x in zip(*ws))
ZERO6=tuple(F(0) for _ in range(N))
ordered=[t for t in itertools.product(range(27),repeat=3) if addw(wt6[t[0]],wt6[t[1]],wt6[t[2]])==ZERO6]
tid={t:n for n,t in enumerate(ordered)}
gens=[]
for i in range(N):
    r=tuple(1 if k==i else 0 for k in range(N))
    gens.append(rho27_Q(evec(r)))
    gens.append(rho27_Q(evec(tuple(-x for x in r))))
rows=[]
for M in gens:
    col_of=defaultdict(list)
    for l in range(27):
        for i in range(27):
            if M[l][i]!=0: col_of[i].append(l)
    nz0=next(((l,i) for l in range(27) for i in range(27) if M[l][i]!=0))
    shift=tuple(a-b for a,b in zip(wt6[nz0[0]],wt6[nz0[1]]))
    target=tuple(-x for x in shift)
    for (i,j,k) in itertools.product(range(27),repeat=3):
        if addw(wt6[i],wt6[j],wt6[k])!=target: continue
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
assert len(NS)==1
Cvec=NS[0]
C={t:Cvec[tid[t]] for t in ordered if Cvec[tid[t]]!=0}
print(f"C rebuilt in-run: unique e6 invariant, {len(C)} nonzero ordered triples")

# ---- Y = eps (x) C as a sparse dict on (2x27)^2 x 27; index (i,a) -> 27*i+a
eps={(0,1):F(1),(1,0):F(-1)}
Y={}
for (i,j),ev in eps.items():
    for (a,b,c),cv in C.items():
        Y[(27*i+a,27*j+b,c)]=ev*cv
print(f"Y = eps (x) C: {len(Y)} nonzero entries")

# ---- diagonal sl2 on Psi (54-dim): E_diag = e2 (x) 1 + 1 (x) E27, etc.
def sparse_of(M):
    d=defaultdict(list)
    for l in range(len(M)):
        for i in range(len(M[0])):
            if M[l][i]!=0: d[i].append((l,M[l][i]))
    return d   # column -> [(row, val)]
E27s=sparse_of(E27); F27s=sparse_of(F27)
def Ediag_col(x):
    i,a=divmod(x,27)
    out=[(27*l_+ (a),v) for (l_,v) in ([(0,F(1))] if i==1 else [])]  # e2: down->up
    out+=[(27*i+l_,v) for (l_,v) in E27s.get(a,[])]
    return out
def Fdiag_col(x):
    i,a=divmod(x,27)
    out=[(27*1+a,F(1))] if i==0 else []                              # f2: up->down
    out+=[(27*i+l_,v) for (l_,v) in F27s.get(a,[])]
    return out
wtPsi=[(1 if i==0 else -1)+wt[a] for i in range(2) for a in range(27)]

# FACT A: derivation identities for E, F, H on Y, computed sparsely.
# (D_M Y)(x,y,z) = Y(M e_x, e_y, e_z) + Y(e_x, M e_y, e_z) + Y(e_x, e_y, M27 e_z):
# scatter FROM Y's support — for each support (u,v,w) and each x whose column
# of M contains u, add val * Y[u,v,w] into Z[(x,v,w)], etc.
colE={x:Ediag_col(x) for x in range(54)}
colF={x:Fdiag_col(x) for x in range(54)}
colE27={x:[(l_,v) for (l_,v) in E27s.get(x,[])] for x in range(27)}
colF27={x:[(l_,v) for (l_,v) in F27s.get(x,[])] for x in range(27)}
def deriv_zero(col54,col27):
    inv54=defaultdict(list)
    for x,lst in col54.items():
        for (l_,val) in lst: inv54[l_].append((x,val))
    inv27=defaultdict(list)
    for x,lst in col27.items():
        for (l_,val) in lst: inv27[l_].append((x,val))
    Z=defaultdict(F)
    for (u,v,w),yv in Y.items():
        for (x,val) in inv54.get(u,[]): Z[(x,v,w)]+=val*yv
        for (x,val) in inv54.get(v,[]): Z[(u,x,w)]+=val*yv
        for (x,val) in inv27.get(w,[]): Z[(u,v,x)]+=val*yv
    return all(z==0 for z in Z.values())
okE=deriv_zero(colE,colE27); okF=deriv_zero(colF,colF27)
okH=all(wtPsi[u]+wtPsi[v]+wt[w]==0 for (u,v,w) in Y)
print(f"FACT A: Y invariant under diagonal E: {okE}, F: {okF}, H (weight-zero support): {okH}")
assert okE and okF and okH

# FACT B: chain-adapted string bases (vectors as sparse dicts index->coeff)
tops=[a for a in range(27) if wt[a]==1]; bots=[a for a in range(27) if wt[a]==-1]
sing=[a for a in range(27) if wt[a]==0]
# solve E27 d_t = e_t on the (-1)->(+1) block
Eblk=[[E27[t][b] for b in bots] for t in tops]
def solve6(Ablk,rhs):
    n=len(Ablk); Aug=[row[:]+ [rhs[i]] for i,row in enumerate(Ablk)]
    r=0
    for c in range(n):
        p=next((i for i in range(r,n) if Aug[i][c]!=0),None)
        assert p is not None
        Aug[r],Aug[p]=Aug[p],Aug[r]
        pv=Aug[r][c]; Aug[r]=[x/pv for x in Aug[r]]
        for i in range(n):
            if i!=r and Aug[i][c]!=0:
                fq=Aug[i][c]; Aug[i]=[x-fq*y for x,y in zip(Aug[i],Aug[r])]
        r+=1
    return [Aug[i][n] for i in range(n)]
dvec={}
for ti,t in enumerate(tops):
    rhs=[F(1) if tt==t else F(0) for tt in tops]
    sol=solve6(Eblk,rhs)
    dvec[t]={bots[k]:sol[k] for k in range(6) if sol[k]!=0}
# verify: E27 d_t = e_t and E27 e_t = 0, E27 e_s = 0
def applyM_s(Ms,vd):
    out=defaultdict(F)
    for i,cv in vd.items():
        for (l_,val) in Ms.get(i,[]): out[l_]+=val*cv
    return {k:v for k,v in out.items() if v!=0}
for t in tops:
    assert applyM_s(E27s,dvec[t])=={t:F(1)}
    assert applyM_s(E27s,{t:F(1)})=={}
for s_ in sing: assert applyM_s(E27s,{s_:F(1)})=={}
print("FACT B: 27 string basis verified: 6 doublet chains (bottom solved exactly), 15 singlets")
# 27 strings: label -> (length, list of vectors bottom..top)
str27=[]
for t in tops: str27.append((2,[dvec[t],{t:F(1)}]))
for s_ in sing: str27.append((1,[{s_:F(1)}]))
# Psi strings: up=(i=0), down=(i=1); vector dicts on 0..53
def up(vd): return {27*0+a:c for a,c in vd.items()}
def dn(vd): return {27*1+a:c for a,c in vd.items()}
def vadd(*vs):
    out=defaultdict(F)
    for v in vs:
        for k,c in v.items(): out[k]+=c
    return {k:c for k,c in out.items() if c!=0}
def vscale(v,s):
    return {k:c*s for k,c in v.items()}
strPsi=[]
for t in tops:
    d_=dvec[t]; e_={t:F(1)}
    b3=dn(d_); m3=vadd(up(d_),dn(e_)); t3=vscale(up(e_),F(2))
    s0=vadd(up(d_),vscale(dn(e_),F(-1)))
    strPsi.append((3,[b3,m3,t3]))
    strPsi.append((1,[s0]))
for s_ in sing:
    strPsi.append((2,[dn({s_:F(1)}),up({s_:F(1)})]))
# verify chains under E_diag
colE_s=defaultdict(list)
for x in range(54):
    for (l_,v) in colE[x]: colE_s[x].append((l_,v))
def applyE(vd):
    out=defaultdict(F)
    for x,cv in vd.items():
        for (l_,val) in colE_s.get(x,[]): out[l_]+=val*cv
    return {k:v for k,v in out.items() if v!=0}
nch=Counter()
for (L,vecs) in strPsi:
    nch[L]+=1
    assert applyE(vecs[L-1])=={}
assert dict(nch)=={3:6,2:15,1:6}
# verify each E-step lands exactly on the recorded next vector (scaled)
for (L,vecs) in strPsi:
    for k in range(L-1):
        av=applyE(vecs[k])
        nxt=vecs[k+1]
        # av should be proportional to nxt: check cross-ratios
        keys=set(av)|set(nxt)
        ratio=None
        for kk in keys:
            a_=av.get(kk,F(0)); b_=nxt.get(kk,F(0))
            if b_==0: assert a_==0; continue
            rr=a_/b_
            if ratio is None: ratio=rr
            assert rr==ratio
        assert ratio is not None and ratio!=0
print(f"FACT B: Psi string basis verified: chains {dict(nch)} (= memo 50's 6 J3, 15 J2, 6 J1)")

# ---- evaluate Y on string-vector triples, tabulate blocks by (L1,L2,L3)
def wt_of(vd,wts):
    ks=list(vd)
    w0=wts[ks[0]]
    assert all(wts[k]==w0 for k in ks)
    return w0
hit=defaultdict(int); nonzero_blocks=set()
for (L1,vecs1) in strPsi:
    for (L2,vecs2) in strPsi:
        for (L3,vecs3) in str27:
            for v1 in vecs1:
                w1=wt_of(v1,wtPsi)
                for v2 in vecs2:
                    w2=wt_of(v2,wtPsi)
                    for v3 in vecs3:
                        if w1+w2+wt_of(v3,wt)!=0: continue
                        tot=F(0)
                        for u,cu in v1.items():
                            for v,cv in v2.items():
                                for w,cw in v3.items():
                                    yv=Y.get((u,v,w))
                                    if yv is not None: tot+=cu*cv*cw*yv
                        if tot!=0: nonzero_blocks.add((L1,L2,L3)); hit[(L1,L2,L3)]+=1
allowed={(3,3,1),(3,2,2),(2,3,2),(2,2,1),(2,1,2),(1,2,2),(1,1,1)}
forbidden={(a,b,c) for a in (3,2,1) for b in (3,2,1) for c in (2,1)}-allowed
print("\nFACT C/D: Y's block support over chain lengths (s1,s2,s3):")
for blk in sorted(hit): print(f"  block {blk}: {hit[blk]} nonzero string-triple entries")
bad=nonzero_blocks & forbidden
print(f"FACT C: forbidden blocks hit: {sorted(bad)} (expect none)")
assert not bad
missing=allowed-nonzero_blocks
print(f"FACT D: allowed blocks NOT hit: {sorted(missing)} (expected branch: none)")
assert not missing
okpar=all((s1+s2+s3)%2==1 for (s1,s2,s3) in nonzero_blocks)
print(f"FACT E: every nonzero block has s1+s2+s3 ODD: {okpar}")
assert okpar

print("""
THE YUKAWA READS THE CLOCK: over the meridian's chain grading the unique
coupling is supported on EXACTLY the seven sl2-allowed depth blocks — no
extra vanishing, no leakage — and every coupled triple has odd total chain
length.  Depth-3 matter chains talk to each other only through internal
singlets (3,3,1) and to the unlocked depth-2 chains only through internal
doublets (3,2,2); the frozen matter lines (length 1) couple pairwise through
singlets (1,1,1) and to the unlocked sector through doublets (1,2,2).  The
depth grading, the lock parity (memo 47), and the coupling are one
compatible structure.  Structure only; Gate 5 untouched.""")
