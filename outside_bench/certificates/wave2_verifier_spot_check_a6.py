# wave-2 A6 verifier artifact: the independent float64 spot-check of census_distinct.py
# (written by the adversarial verifier agent during the wave-2 loop; relocated from a
#  stray working-tree location into the lane as verification evidence; run from this dir).
# READING NOTE (bench): this scratch's own print labels are SWAPPED — its 'numpy rank(ad e)'
# column IS the orbit dimension (rank of ad e = 78 - centralizer dim), and its 'orbit dim
# (numpy)' column actually prints the CENTRALIZER dimension. The numbers corroborate
# census_distinct.py exactly (orbit dims 22 / 72 / 40 for the three sampled rows); only
# the scratch's labels are off, and no banked claim uses them.
import os, sys
sys.path.insert(0, ".")
from fractions import Fraction as F
SCR = "."
src = open(SCR + "/twisted_double.py").read()
exec(src[:src.index("# ---------------- stage 4")])

# independent rank check using numpy on float64 matrix, for a couple characteristics
import itertools, random
random.seed(4)
SIMPLE = [tuple(1 if k==i else 0 for k in range(N)) for i in range(N)]
def hvec_(coeffs):
    h=[F(0)]*DIM
    for k in range(N): h[k]=F(coeffs[k])
    return h

# reconstruct exactly as census_distinct.py did, to get the same triples
A = [[None]*N for _ in range(N)]
for j in range(N):
    hj = hvec_(SIMPLE[j])
    for i in range(N):
        ei = evec(SIMPLE[i])
        brr = br(hj, ei)
        val=None
        for k in range(DIM):
            if ei[k]!=0:
                val = brr[k]/ei[k]; break
        A[i][j]=val

def inv_matrix(M):
    n=len(M)
    aug=[[F(M[i][j]) for j in range(n)]+[F(1) if k==i else F(0) for k in range(n)] for i in range(n)]
    for col in range(n):
        p=next(i for i in range(col,n) if aug[i][col]!=0)
        aug[col],aug[p]=aug[p],aug[col]
        pv=aug[col][col]
        aug[col]=[x/pv for x in aug[col]]
        for i in range(n):
            if i!=col and aug[i][col]!=0:
                f_=aug[i][col]
                aug[i]=[x-f_*y for x,y in zip(aug[i],aug[col])]
    return [row[n:] for row in aug]
Ainv = inv_matrix(A)
def Hc(c):
    t=[sum(Ainv[i][j]*F(c[j]) for j in range(N)) for i in range(N)]
    return hvec_(t)
def grade(root,c): return sum(F(root[k])*c[k] for k in range(N))
def solve_lin(Mrows, rhs):
    m=len(Mrows); n=len(Mrows[0]) if m else 0
    aug=[row[:]+[rhs[i]] for i,row in enumerate(Mrows)]
    piv=[]; r=0
    for col in range(n):
        p=None
        for i in range(r,m):
            if aug[i][col]!=0: p=i;break
        if p is None: continue
        aug[r],aug[p]=aug[p],aug[r]
        pv=aug[r][col]
        aug[r]=[x/pv for x in aug[r]]
        for i in range(m):
            if i!=r and aug[i][col]!=0:
                f_=aug[i][col]
                aug[i]=[x-f_*y for x,y in zip(aug[i],aug[r])]
        piv.append(col); r+=1
        if r==m: break
    for i in range(r,m):
        if aug[i][n]!=0: return None
    y=[F(0)]*n
    for i,col in enumerate(piv): y[col]=aug[i][n]
    return y
def is_characteristic(c, tries=4):
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
        cols=[br(e,bn) for bn in basneg]
        Mrows=[[cols[j][i] for j in range(len(cols))] for i in range(DIM)]
        y=solve_lin(Mrows,H)
        if y is not None:
            f=[F(0)]*DIM
            for yy,bn in zip(y,basneg): f=[a+yy*b for a,b in zip(f,bn)]
            return (e,H,f)
    return None

import numpy as np
ADJ_BASIS = [evec(r) for r in ROOTS] + [hvec_(SIMPLE[i]) for i in range(N)]

def numpy_rank(e):
    M = np.array([[float(x) for x in br(e,b)] for b in ADJ_BASIS], dtype=np.float64).T
    return np.linalg.matrix_rank(M, tol=1e-8)

targets = [(0,1,0,0,0,0), (2,2,2,2,2,2), (0,0,0,1,0,0)]
for c in targets:
    w = is_characteristic(c)
    e,h,f = w
    r = numpy_rank(e)
    print(c, "numpy rank(ad e)=", r, "orbit dim (numpy)=", DIM-r)
