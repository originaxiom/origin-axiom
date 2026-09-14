"""Exact arithmetic in Q(sqrt3, i) = Q(zeta_12). Element = (p,q,r,s) meaning (p+q*sqrt3) + i*(r+s*sqrt3)."""
from fractions import Fraction as F
Z=(F(0),F(0),F(0),F(0)); ONE=(F(1),F(0),F(0),F(0))
# omega = -1/2 + (sqrt3/2) i  -- primitive cube root of unity, lives here
OMEGA=(F(-1,2),F(0),F(0),F(1,2))
def _s3mul(a,b): return (a[0]*b[0]+3*a[1]*b[1], a[0]*b[1]+a[1]*b[0])
def _s3add(a,b): return (a[0]+b[0], a[1]+b[1])
def _s3sub(a,b): return (a[0]-b[0], a[1]-b[1])
def _s3inv(a):
    d=a[0]*a[0]-3*a[1]*a[1]
    if d==0: raise ZeroDivisionError
    return (a[0]/d, -a[1]/d)
def add(x,y): return tuple(map(lambda u,v:u+v, x, y))
def sub(x,y): return tuple(map(lambda u,v:u-v, x, y))
def neg(x): return tuple(-u for u in x)
def mul(x,y):
    a=(x[0],x[1]); b=(x[2],x[3]); c=(y[0],y[1]); d=(y[2],y[3])
    re=_s3sub(_s3mul(a,c),_s3mul(b,d)); im=_s3add(_s3mul(a,d),_s3mul(b,c))
    return (re[0],re[1],im[0],im[1])
def inv(x):
    a=(x[0],x[1]); b=(x[2],x[3])
    N=_s3add(_s3mul(a,a),_s3mul(b,b)); Ni=_s3inv(N)
    re=_s3mul(a,Ni); im=_s3mul((-b[0],-b[1]),Ni)
    return (re[0],re[1],im[0],im[1])
def is_zero(x): return all(u==0 for u in x)
def powe(x,k):
    r=ONE
    for _ in range(k): r=mul(r,x)
    return r
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
def minv(A):
    n=len(A); M=[list(A[i])+list(eye(n)[i]) for i in range(n)]; r=0
    for c in range(n):
        p=next((i for i in range(r,n) if not is_zero(M[i][c])),None)
        if p is None: return None
        M[r],M[p]=M[p],M[r]
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
        p=next((i for i in range(r,rows) if not is_zero(M[i][c])),None)
        if p is None: continue
        M[r],M[p]=M[p],M[r]
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
