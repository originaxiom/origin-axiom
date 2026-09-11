"""Exact arithmetic in Q(omega), omega^2 = -1-omega. Elements are pairs (a,b) = a + b*omega."""
from fractions import Fraction as F
Z=(F(0),F(0)); ONE=(F(1),F(0)); OM=(F(0),F(1))
def add(x,y): return (x[0]+y[0], x[1]+y[1])
def sub(x,y): return (x[0]-y[0], x[1]-y[1])
def neg(x): return (-x[0], -x[1])
def mul(x,y):
    a,b=x; c,d=y
    return (a*c - b*d, a*d + b*c - b*d)
def conj(x):                      # omega -> omega^2 = -1-omega
    a,b=x; return (a-b, -b)
def norm(x): return mul(x,conj(x))[0]
def inv(x):
    n=norm(x)
    if n==0: raise ZeroDivisionError
    c=conj(x); return (c[0]/n, c[1]/n)
def is_zero(x): return x[0]==0 and x[1]==0
def powom(k):                     # omega^k
    k%=3
    return ONE if k==0 else (OM if k==1 else mul(OM,OM))

def mm(A,B):
    n=len(A); m=len(B[0]); k=len(B)
    return [[_dot(A[i],[B[t][j] for t in range(k)]) for j in range(m)] for i in range(n)]
def _dot(r,c):
    s=Z
    for x,y in zip(r,c): s=add(s,mul(x,y))
    return s
def eye(n): return [[ONE if i==j else Z for j in range(n)] for i in range(n)]
def msub(A,B): return [[sub(A[i][j],B[i][j]) for j in range(len(A[0]))] for i in range(len(A))]
def scal(c,A): return [[mul(c,A[i][j]) for j in range(len(A[0]))] for i in range(len(A))]
def minv2(A):
    a,b=A[0]; c,d=A[1]
    det=sub(mul(a,d),mul(b,c)); di=inv(det)
    return [[mul(d,di),mul(neg(b),di)],[mul(neg(c),di),mul(a,di)]]
def minv(A):
    n=len(A); M=[list(A[i])+list(eye(n)[i]) for i in range(n)]; r=0
    for c in range(n):
        piv=next((i for i in range(r,n) if not is_zero(M[i][c])),None)
        if piv is None: return None
        M[r],M[piv]=M[piv],M[r]
        iv=inv(M[r][c]); M[r]=[mul(x,iv) for x in M[r]]
        for i in range(n):
            if i!=r and not is_zero(M[i][c]):
                f=M[i][c]; M[i]=[sub(M[i][j],mul(f,M[r][j])) for j in range(2*n)]
        r+=1
    return [row[n:] for row in M]
def rank(M):
    if not M or not M[0]: return 0
    M=[list(r) for r in M]; rows=len(M); cols=len(M[0]); r=0
    for c in range(cols):
        piv=next((i for i in range(r,rows) if not is_zero(M[i][c])),None)
        if piv is None: continue
        M[r],M[piv]=M[piv],M[r]
        iv=inv(M[r][c]); M[r]=[mul(x,iv) for x in M[r]]
        for i in range(rows):
            if i!=r and not is_zero(M[i][c]):
                f=M[i][c]; M[i]=[sub(M[i][j],mul(f,M[r][j])) for j in range(cols)]
        r+=1
        if r==rows: break
    return r
def nullspace(M,ncols):
    if not M: return [[ONE if i==j else Z for i in range(ncols)] for j in range(ncols)]
    M=[list(r) for r in M]; rows=len(M); r=0; piv=[]
    for c in range(ncols):
        p=next((i for i in range(r,rows) if not is_zero(M[i][c])),None)
        if p is None: continue
        M[r],M[p]=M[p],M[r]
        iv=inv(M[r][c]); M[r]=[mul(x,iv) for x in M[r]]
        for i in range(rows):
            if i!=r and not is_zero(M[i][c]):
                f=M[i][c]; M[i]=[sub(M[i][j],mul(f,M[r][j])) for j in range(ncols)]
        piv.append(c); r+=1
        if r==rows: break
    free=[c for c in range(ncols) if c not in piv]
    out=[]
    for fc in free:
        v=[Z]*ncols; v[fc]=ONE
        for i,pc in enumerate(piv): v[pc]=neg(M[i][fc])
        out.append(v)
    return out
