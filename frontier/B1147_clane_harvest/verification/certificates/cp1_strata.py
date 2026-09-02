#!/usr/bin/env python3
"""C-P1: THE FOUR DISTINGUISHED PARITIES — the 20-row stratum/parity dictionary
completed, from scratch.

Memo 2 (PROJECTIVE_HATCH) classified the 16 Levi-regular strata of e6 by the
parity of their 27-spectrum (projective = all even = lift-independent) and left
the 4 distinguished-non-regular strata UNCLASSIFIED (projective count bounded
6..10).  This certificate closes C-P1 with NO literature input:

  1. enumerate ALL nilpotent characteristics of e6 from first principles:
     for every dominant labeling c in {0,1,2}^6, H_c = sum c_j omega_j^vee is a
     characteristic iff a generic e in g(2) admits f in g(-2) with [e,f] = H_c
     (then (e,H_c,f) is an sl2 triple by the grading, and H_c — dominant — is
     the weighted Dynkin diagram of O_e).  Exact linear algebra over Q.
     CONTROL: exactly 20 nonzero characteristics must appear (E6 has 20 nonzero
     nilpotent orbits — Bala-Carter; the count is REPRODUCED, not assumed).
  2. rebuild the 16 Levi-principal characteristics independently (2rho^vee of
     each simple-root subset, conjugated to dominance) — CONTROL vs memo 2.
  3. the 4 leftovers = the distinguished-non-regular strata.  For each: verify
     the JM triple exactly, compute the exact 27-spectrum of H, type its parity
     (projective / lift-sensitive) and its fermion-capability (odd weights =>
     the two lifts give different matter reps, memo 29's criterion).
  4. for every lift-sensitive stratum among the 4: verify the beat closes on
     its matter rep over the selected chi=+1 lift (Omega^2 = A27 and both
     intertwinings), exactly — memo 29's functorial argument, checked on the
     nose (e has rational coefficients, so gal fixes them and
     Omega^2 = exp((q+qbar) rho(e)) = A27).
"""
import itertools, random
from fractions import Fraction as F
from collections import Counter
SCR=__import__('os').path.dirname(__import__('os').path.abspath(__file__))+""
src=open(SCR+"/twisted_double.py").read()
cut=src.index("# ---------------- stage 4")
exec(src[:cut])   # exact e6 (ROOTS, br, evec, smul_, DIM, N) + the 27 (rho27_Q, verified on 3003 brackets)

random.seed(4)  # deterministic

# Cartan matrix from the roots' pairing: A[i][j] = alpha_i(h_j) — for the simply-laced
# basis here, alpha_i(h_j) = the bracket [h_j, e_{alpha_i}] eigenvalue; read it off br().
SIMPLE=[tuple(1 if k==i else 0 for k in range(N)) for i in range(N)]
def hvec(coeffs):
    h=[F(0)]*DIM
    for k in range(N): h[k]=F(coeffs[k])
    return h
A=[[None]*N for _ in range(N)]
for j in range(N):
    hj=hvec(SIMPLE[j])
    for i in range(N):
        ei=evec(SIMPLE[i]); brr=br(hj,ei)
        # brr = A[i][j] * ei exactly (ei is a root vector)
        val=None
        for k in range(DIM):
            if ei[k]!=0: val=brr[k]/ei[k]; break
        assert all(brr[k]==val*ei[k] for k in range(DIM))
        A[i][j]=val
print("Cartan matrix recovered from brackets:", A)

# H_c in the h-basis: t = A^{-1} c  (then alpha_k(H_c) = c_k); root grading is combinatorial:
def grade(root, c): return sum(F(root[k])*c[k] for k in range(N))

def solve_lin(Mrows, rhs):
    """Solve M y = rhs exactly over Q (M given as list of rows). Return y or None."""
    m=len(Mrows); n=len(Mrows[0]) if m else 0
    aug=[row[:]+[rhs[i]] for i,row in enumerate(Mrows)]
    piv=[]; r=0
    for col in range(n):
        p=None
        for i in range(r,m):
            if aug[i][col]!=0: p=i; break
        if p is None: continue
        aug[r],aug[p]=aug[p],aug[r]
        pv=aug[r][col]
        aug[r]=[x/pv for x in aug[r]]
        for i in range(m):
            if i!=r and aug[i][col]!=0:
                f=aug[i][col]; aug[i]=[x-f*y for x,y in zip(aug[i],aug[r])]
        piv.append(col); r+=1
        if r==m: break
    for i in range(r,m):
        if aug[i][n]!=0: return None
    y=[F(0)]*n
    for i,col in enumerate(piv): y[col]=aug[i][n]
    return y

# inverse Cartan (exact) for t = A^{-1} c
def inv_matrix(M):
    n=len(M); aug=[[F(M[i][j]) for j in range(n)]+[F(1) if k==i else F(0) for k in range(n)] for i in range(n)]
    for col in range(n):
        p=next(i for i in range(col,n) if aug[i][col]!=0)
        aug[col],aug[p]=aug[p],aug[col]
        pv=aug[col][col]; aug[col]=[x/pv for x in aug[col]]
        for i in range(n):
            if i!=col and aug[i][col]!=0:
                f=aug[i][col]; aug[i]=[x-f*y for x,y in zip(aug[i],aug[col])]
    return [row[n:] for row in aug]
Ainv=inv_matrix(A)

def Hc(c):
    t=[sum(Ainv[i][j]*F(c[j]) for j in range(N)) for i in range(N)]
    return hvec(t)

def is_characteristic(c, tries=4):
    """Generic e in g(2): does [e,f]=H_c have a solution f in g(-2)?  Also return a witness."""
    H=Hc(c)
    P2=[r for r in ROOTS if grade(r,c)==2]
    if not P2: return None
    M2=[r for r in ROOTS if grade(r,c)==-2]
    basneg=[evec(r) for r in M2]
    for t in range(tries):
        xs=[F(random.randint(1,9)) for _ in P2]
        e=[F(0)]*DIM
        for x,r in zip(xs,P2):
            e=[a+x*b for a,b in zip(e,evec(r))]
        # columns: [e, e_{-beta}] as DIM-vectors
        cols=[br(e,bn) for bn in basneg]
        Mrows=[[cols[j][i] for j in range(len(cols))] for i in range(DIM)]
        y=solve_lin(Mrows,H)
        if y is not None:
            f=[F(0)]*DIM
            for yy,bn in zip(y,basneg):
                f=[a+yy*b for a,b in zip(f,bn)]
            # exact sl2 verification
            assert br(e,f)==H
            assert br(H,e)==smul_(2,e) and br(H,f)==smul_(-2,f)
            return (e,H,f)
    return None

# ---- 1. full enumeration
chars={}
for c in itertools.product((0,1,2),repeat=N):
    if all(x==0 for x in c): continue
    w=is_characteristic(c)
    if w is not None: chars[c]=w
print(f"\nnonzero nilpotent characteristics found: {len(chars)}  (CONTROL: expect 20 = E6's nonzero orbit count)")
assert len(chars)==20

# ---- 2. the 16 Levi-principal ones, independently
def dominantize(vals):
    v=list(vals)
    while True:
        k=next((i for i in range(N) if v[i]<0), None)
        if k is None: return tuple(v)
        vk=v[k]
        v=[v[j]-vk*A[j][k] for j in range(N)]
def root_in_span(r, S): return all(r[k]==0 for k in range(N) if k not in S)
levi=set()
for size in range(1,N+1):
    for S in itertools.combinations(range(N),size):
        two_rho=[0]*N
        for r in ROOTS:
            if grade(r,[1]*N)>0 and root_in_span(r,S):   # positive root of the Levi
                two_rho=[a+b for a,b in zip(two_rho,r)]
        h=hvec([F(x) for x in two_rho])                   # 2 rho^vee_L in h-basis
        vals=[sum(F(A[i][j])*F(two_rho[j]) for j in range(N)) for i in range(N)]
        levi.add(dominantize(vals))
print(f"distinct Levi-principal characteristics: {len(levi)}  (CONTROL: memo 2's 16)")
assert len(levi)==16
assert levi <= set(chars.keys())

# ---- 3. the four distinguished-non-regular strata
dist=sorted(set(chars.keys())-levi)
print(f"\nTHE FOUR DISTINGUISHED-NON-REGULAR STRATA (labels alpha_1..alpha_6): {dist}")
assert len(dist)==4
def kernel_dim(e):
    cols=[br(e,evec(r)) for r in ROOTS]+[br(e,hvec(SIMPLE[i])) for i in range(N)]
    Mrows=[[cols[j][i] for j in range(len(cols))] for i in range(DIM)]
    # rank via elimination
    m=len(Mrows); n=len(cols); r=0
    aug=[row[:] for row in Mrows]
    for col in range(n):
        p=next((i for i in range(r,m) if aug[i][col]!=0),None)
        if p is None: continue
        aug[r],aug[p]=aug[p],aug[r]
        pv=aug[r][col]; aug[r]=[x/pv for x in aug[r]]
        for i in range(m):
            if i!=r and aug[i][col]!=0:
                fq=aug[i][col]; aug[i]=[x-fq*y for x,y in zip(aug[i],aug[r])]
        r+=1
    return n-r
verdicts={}
for c in dist:
    e,H,f=chars[c]
    H27=rho27_Q(H)
    spec=Counter(H27[i][i] for i in range(27))
    assert all(v.denominator==1 for v in spec)      # sl2 integrality — internal check
    odd=any(int(v)%2!=0 for v in spec)
    dimO=DIM-kernel_dim(e)
    verdicts[c]=(dict(spec),odd,dimO)
    print(f"  c={c}: dim O = {dimO}; 27-spectrum {dict((int(k),v) for k,v in spec.items())}; "
          f"{'ODD (lift-sensitive, fermion-capable)' if odd else 'EVEN (projective, lift-free)'}")

# ---- 4. beat closure on every lift-sensitive distinguished stratum
def fbar(u): return (u[0]+u[1], -u[1])
def galM(M): return [[fbar(x) for x in row] for row in M]
for c in dist:
    spec,odd,dimO=verdicts[c]
    if not odd: continue
    e,H,f=chars[c]
    E27=toF(rho27_Q(e)); F27=toF(rho27_Q(f))
    A27=nilexp(E27,ONE); B27=nilexp(F27,QQ)
    A27i=nilexp(E27,fneg(ONE)); B27i=nilexp(F27,fneg(QQ))
    d27={'a':A27,'A':A27i,'b':B27,'B':B27i}
    Rel=wordmat('a'+'bABa'+'B'+'AbaB',d27)
    U=nilexp(E27,QQ); Ui=nilexp(E27,fneg(QQ))
    Om2=mmul(U,galM(U))
    okA=mmul(U,mmul(galM(A27),Ui))==A27
    okB=mmul(U,mmul(galM(B27),Ui))==wordmat('BabAb',d27)
    print(f"  beat closure on c={c}: relator=+I: {Rel==eye(27)}; Omega^2=A27: {Om2==A27}; "
          f"intertwinings: {okA and okB}")
    assert Rel==eye(27) and Om2==A27 and okA and okB

proj4=sum(1 for c in dist if not verdicts[c][1])

# ---- 5. the FULL 20-row dictionary, every parity recomputed from scratch
print("\nTHE 20-ROW DICTIONARY (label; dim O; 27-parity):")
projN=0
for c in sorted(chars):
    e,H,f=chars[c]
    H27=rho27_Q(H)
    spec=Counter(int(H27[i][i]) for i in range(27))
    odd=any(k%2!=0 for k in spec)
    dimO=DIM-kernel_dim(e)
    tag='LEVI-REGULAR' if c in levi else 'DISTINGUISHED'
    if not odd: projN+=1
    print(f"  {c}  dim {dimO:3d}  {tag:13s}  {'ODD (lift-sensitive)' if odd else 'even (projective)'}")
levi_proj=projN-proj4
print(f"projective totals: Levi-regular {levi_proj}/16 (CONTROL: memo 2's 6) + distinguished {proj4}/4 = {projN}/20")
assert levi_proj==6

print(f"\nC-P1 CLOSED: projective among the 4 distinguished strata: {proj4}")
print(f"=> the FULL 20-row dictionary: projective strata = 6 (re-verified) + {proj4} = {6+proj4}, exact;")
print("   memo 2's bound 6..10 resolved.  Every lift-sensitive stratum in the WHOLE table")
print("   (Levi-regular odd rows, memo 29's A1 seat, and the odd distinguished rows above)")
print("   closes under the beat over the object's selected chi=+1 lift — verified above on")
print("   the distinguished rows, exactly, with the same functorial mechanism (W upstream).")
