#!/usr/bin/env python3
"""A1 + B1: THE JORDAN CUBIC MEETS THE BEAT — and the no-bilinear census.

A1 (opens C-S2): build the E6-invariant cubic form C on the 27 EXACTLY —
  unknowns = symmetric triples of crystal-basis indices with total weight zero
  (Cartan invariance forces the rest to vanish); constraints = the derivation
  condition dC = 0 for the 12 Chevalley generators e_i, f_i (they generate e6).
  Assert the solution space is EXACTLY 1-dimensional; normalize; then
  CROSS-CHECK invariance under ALL 72 root generators (not just the 12).
  Record whether C is RATIONAL in the crystal basis.
  Then the beat: Omega = exp(rho27(q e)) o gal (sigma27/sp2_seat's Omega, the
  chi=+1 machinery).  Verify exactly over Q(q):
      C(Omega u, Omega v, Omega w) = gal( C(u,v,w) )   for all basis triples,
  i.e. the transported cubic C' with C'_{ijk} = sum C_{abc} U_ai U_bj U_ck
  equals gal(C) entrywise; plus the A27 = Omega^2 invariance cross-check.

B1 (the no-mass-term theorem): the same machinery in degree 2 — the space of
  e6-invariant symmetric bilinears on the 27 alone is EXACTLY 0 (weight-zero
  pairs pruned, derivation conditions imposed, nullspace computed).  So no
  invariant mass-like bilinear exists on the matter module by itself: the
  record's 'no mass term' fence becomes a theorem.  (The pairing that does
  exist is 27 x 27bar — different module, not touched here.)

Two-outcome (preregistered in CAMPAIGN_CELLS.json): GREEN = dim=1, covariance
exact, bilinear space 0.  RED on any leg = a bankable anomaly to hunt.
"""
from fractions import Fraction as F
from collections import defaultdict
SCR=__import__('os').path.dirname(__import__('os').path.abspath(__file__))+""
src=open(SCR+"/twisted_double.py").read()
cut=src.index("# ---------------- stage 4")
exec(src[:cut])   # e6 + the 27 (rho27_Q verified on all 3003 brackets in-run)

# ---- the 27's weights as vectors: diagonal of rho27_Q(h_i) for the 6 simple coroots
H=[rho27_Q(hv) for hv in ( [F(1) if k==i else F(0) for k in range(DIM)] for i in range(N) )]
wt=[tuple(H[i][a][a] for i in range(N)) for a in range(27)]
def addw(*ws): return tuple(sum(x) for x in zip(*ws))
ZERO6=tuple(F(0) for _ in range(N))

# ---- generators: e_i, f_i for the 6 simple roots (they generate e6)
gens=[]
for i in range(N):
    r=SIMPLE_R[i] if 'SIMPLE_R' in dir() else tuple(1 if k==i else 0 for k in range(N))
    gens.append(('e%d'%i, rho27_Q(evec(r)), r))
    gens.append(('f%d'%i, rho27_Q(evec(tuple(-x for x in r))), tuple(-x for x in r)))

# ---------- degree 3: unknowns = weight-zero symmetric triples
from itertools import combinations_with_replacement
triples=[t for t in combinations_with_replacement(range(27),3) if addw(wt[t[0]],wt[t[1]],wt[t[2]])==ZERO6]
tid={t:n for n,t in enumerate(triples)}
NT=len(triples)
print(f"weight-zero symmetric triples on the 27: {NT}")

def key(a,b,c): return tuple(sorted((a,b,c)))

def deriv_rows(M, rootw=None):
    """rows of dC=0 for generator with matrix M: (dC)(i,j,k) = sum_l M_li C(l,j,k)
       + M_lj C(i,l,k) + M_lk C(i,j,l) = 0.  The generator's weight shift (in the
       PAIRING coordinates the wt[] vectors use) is read off M itself: for any
       nonzero entry M[l][i], shift = wt[l] - wt[i].  Equations live at triples
       of total weight = -shift (C is supported on weight zero)."""
    nz0=next(((l,i) for l in range(27) for i in range(27) if M[l][i]!=0), None)
    if nz0 is None: return []
    shift=tuple(a-b for a,b in zip(wt[nz0[0]],wt[nz0[1]]))
    assert all(tuple(a-b for a,b in zip(wt[l],wt[i]))==shift for l in range(27) for i in range(27) if M[l][i]!=0)
    target=tuple(-x for x in shift)
    rows={}
    nz=[(l,i) for l in range(27) for i in range(27) if M[l][i]!=0]
    col_of=defaultdict(list)
    for l,i in nz: col_of[i].append(l)
    for (i,j,k) in combinations_with_replacement(range(27),3):
        if addw(wt[i],wt[j],wt[k])!=target: continue
        row=defaultdict(F)
        for (slot,(x,y,z)) in enumerate(((i,j,k),(j,i,k),(k,i,j))):
            # act on position holding x, partners y,z
            for l in col_of.get(x,[]):
                t=key(l,y,z)
                if t in tid: row[tid[t]]+=M[l][x]
        if row: rows[(i,j,k)]=row
    return list(rows.values())

allrows=[]
for name,M,r in gens:
    allrows.extend(deriv_rows(M))
print(f"derivation equations (12 generators): {len(allrows)}")
assert len(allrows)>0

# nullspace of the sparse system over Q
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

NS=nullspace(allrows, NT)
print(f"invariant-cubic solution space: dim = {len(NS)}  (GREEN requires exactly 1)")
assert len(NS)==1
C=NS[0]
# normalize: first nonzero coefficient -> 1; record rationality (they are Fractions by construction)
pivn=next(i for i,v in enumerate(C) if v!=0)
C=[v/C[pivn] for v in C]
dens=set(v.denominator for v in C if v!=0); numset=sorted(set(abs(v) for v in C if v!=0))
print(f"C normalized: {sum(1 for v in C if v!=0)} nonzero coefficients on {NT} triples; |coeffs| in {numset}; denominators {sorted(dens)}")
print("C is RATIONAL in the crystal basis:", all(isinstance(v,F) for v in C))

def Cval(a,b,c):
    t=key(a,b,c)
    return C[tid[t]] if t in tid else F(0)

# ---- cross-check: invariance under ALL 72 root generators
ok=0
for r in ROOTS:
    M=rho27_Q(evec(r))
    rows=deriv_rows(M)
    good=all(all((sum(v*C[c] for c,v in row.items())==0) for row in [rw]) for rw in rows) if rows else True
    viol=[rw for rw in rows if sum(v*C[c] for c,v in rw.items())!=0]
    assert not viol, f"invariance FAILS for root {r}"
    ok+=1
print(f"cross-check: dC = 0 verified for ALL {ok} root generators (not just the 12 used)")

# ---------- B1: degree 2 — invariant bilinears on the 27 alone
pairs=[p for p in combinations_with_replacement(range(27),2) if addw(wt[p[0]],wt[p[1]])==ZERO6]
pid={p:n for n,p in enumerate(pairs)}
print(f"\nB1: weight-zero symmetric pairs on the 27: {len(pairs)}")
rows2=[]
def key2(a,b): return tuple(sorted((a,b)))
for name,M,r in gens:
    nz0=next((l,i) for l in range(27) for i in range(27) if M[l][i]!=0)
    shift=tuple(a-b for a,b in zip(wt[nz0[0]],wt[nz0[1]]))
    target=tuple(-x for x in shift)
    col_of=defaultdict(list)
    for l in range(27):
        for i in range(27):
            if M[l][i]!=0: col_of[i].append(l)
    for (i,j) in combinations_with_replacement(range(27),2):
        if addw(wt[i],wt[j])!=target: continue
        row=defaultdict(F)
        for (x,y) in ((i,j),(j,i)):
            for l in col_of.get(x,[]):
                p=key2(l,y)
                if p in pid: row[pid[p]]+=M[l][x]
        if row: rows2.append(row)
NS2=nullspace(rows2, len(pairs))
print(f"invariant-bilinear space on the 27 alone: dim = {len(NS2)}  (GREEN requires exactly 0)")
assert len(NS2)==0
print("=> NO invariant mass-like bilinear exists on the matter module by itself: THEOREM")

# ---------- A1 hinge: the beat vs the cubic
# Omega = U o gal with U = exp(rho27(q e)), e = evec(ROOTS[0]) — sp2_seat/sigma27's beat
r0=ROOTS[0]
E27p=toF(rho27_Q(evec(r0)))
U=nilexp(E27p, QQ)
A27=nilexp(E27p, ONE)
# transported cubic C'(i,j,k) = C(U e_i, U e_j, U e_k) over the pair field
def fmulF(a,b): return fmul(a,b)
def transported(Umat):
    # returns dict triple -> pair-field value, only needs to be compared on ALL triples (i<=j<=k)
    # brute force but pruned: U is unipotent sparse-ish; compute columns
    cols=[[Umat[a][i] for a in range(27)] for i in range(27)]
    out={}
    for (i,j,k) in combinations_with_replacement(range(27),3):
        s=(F(0),F(0))
        for a in range(27):
            ua=cols[i][a]
            if ua==(F(0),F(0)): continue
            for b in range(27):
                ub=cols[j][b]
                if ub==(F(0),F(0)): continue
                uab=fmul(ua,ub)
                for c in range(27):
                    uc=cols[k][c]
                    if uc==(F(0),F(0)): continue
                    cv=Cval(a,b,c)
                    if cv==0: continue
                    # multiplicity handling: C as symmetric tensor evaluated on (a,b,c) ordered = Cval directly
                    s=fadd(s, fmul(uab, fmul(uc,(cv,F(0)))))
        out[(i,j,k)]=s
    return out

print("\ncomputing C(U.,U.,U.) exactly over Q(q) — the beat-transported cubic ...")
TP=transported(U)
gal_ok=all(TP[t]==(Cval(*t),F(0)) for t in TP)   # gal(C)=C since C rational
print("C(Omega u, Omega v, Omega w) = gal(C(u,v,w)) for ALL 3654 basis triples:", gal_ok)
assert gal_ok
TP2=transported(A27)
a_ok=all(TP2[t]==(Cval(*t),F(0)) for t in TP2)
print("cross-check: C invariant under A27 = Omega^2 (the lifted meridian):", a_ok)
assert a_ok

print("\nA1 GREEN + B1 GREEN: the 27 carries a UNIQUE invariant cubic (the Jordan")
print("determinant), RATIONAL in the crystal basis, invariant under all 72 root")
print("generators — and the beat preserves it ON THE NOSE: C(Omega.,Omega.,Omega.) =")
print("gal(C(.,.,.)) exactly, with the meridian cross-check passing.  The matter")
print("module's cubic — the algebraic seat of any Yukawa-shaped coupling — is")
print("beat-covariant: C-S2's bridge has its first exact plank.  And the 27 alone")
print("admits NO invariant bilinear: 'no mass term' is now a theorem of the record.")
