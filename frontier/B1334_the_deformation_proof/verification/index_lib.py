"""r1 / t0 for twisted local systems on a one-cusped manifold, over F_p. Exact."""
import itertools

def matmul(A,B,p):
    n=len(A); m=len(B[0]); k=len(B)
    return [[sum(A[i][t]*B[t][j] for t in range(k))%p for j in range(m)] for i in range(n)]
def matadd(A,B,p): return [[(A[i][j]+B[i][j])%p for j in range(len(A[0]))] for i in range(len(A))]
def matsub(A,B,p): return [[(A[i][j]-B[i][j])%p for j in range(len(A[0]))] for i in range(len(A))]
def eye(n): return [[1 if i==j else 0 for j in range(n)] for i in range(n)]
def zeros(n,m): return [[0]*m for _ in range(n)]
def scal(c,A,p): return [[(c*A[i][j])%p for j in range(len(A[0]))] for i in range(len(A))]

def inv2(A,p):
    a,b=A[0]; c,d=A[1]
    det=(a*d-b*c)%p; di=pow(det,p-2,p)
    return [[(d*di)%p,(-b*di)%p],[(-c*di)%p,(a*di)%p]]

def matinv(A,p):
    n=len(A); M=[row[:]+eye(n)[i][:] for i,row in enumerate(A)]
    r=0
    for c in range(n):
        piv=next((i for i in range(r,n) if M[i][c]%p),None)
        if piv is None: return None
        M[r],M[piv]=M[piv],M[r]
        iv=pow(M[r][c],p-2,p)
        M[r]=[(x*iv)%p for x in M[r]]
        for i in range(n):
            if i!=r and M[i][c]%p:
                f=M[i][c]; M[i]=[(M[i][j]-f*M[r][j])%p for j in range(2*n)]
        r+=1
    return [row[n:] for row in M]

def rank(M,p):
    if not M or not M[0]: return 0
    M=[row[:] for row in M]; rows=len(M); cols=len(M[0]); r=0
    for c in range(cols):
        piv=next((i for i in range(r,rows) if M[i][c]%p),None)
        if piv is None: continue
        M[r],M[piv]=M[piv],M[r]
        iv=pow(M[r][c],p-2,p); M[r]=[(x*iv)%p for x in M[r]]
        for i in range(rows):
            if i!=r and M[i][c]%p:
                f=M[i][c]; M[i]=[(M[i][j]-f*M[r][j])%p for j in range(cols)]
        r+=1
        if r==rows: break
    return r

def nullspace(M,p,ncols):
    """basis of ker(M) as list of vectors of length ncols"""
    if not M: return [[1 if i==j else 0 for i in range(ncols)] for j in range(ncols)]
    M=[row[:] for row in M]; rows=len(M); r=0; pivots=[]
    for c in range(ncols):
        piv=next((i for i in range(r,rows) if M[i][c]%p),None)
        if piv is None: continue
        M[r],M[piv]=M[piv],M[r]
        iv=pow(M[r][c],p-2,p); M[r]=[(x*iv)%p for x in M[r]]
        for i in range(rows):
            if i!=r and M[i][c]%p:
                f=M[i][c]; M[i]=[(M[i][j]-f*M[r][j])%p for j in range(ncols)]
        pivots.append(c); r+=1
        if r==rows: break
    free=[c for c in range(ncols) if c not in pivots]
    basis=[]
    for fc in free:
        v=[0]*ncols; v[fc]=1
        for i,pc in enumerate(pivots): v[pc]=(-M[i][fc])%p
        basis.append(v)
    return basis

def fox(word, gen, rho, p, d):
    """rho(d word / d gen) as a d x d matrix"""
    res=zeros(d,d); pre=eye(d)
    for ch in word:
        g=ch.lower()
        if ch.islower():
            if g==gen: res=matadd(res,pre,p)
            pre=matmul(pre,rho[g],p)
        else:
            gi=matinv(rho[g],p)
            pre=matmul(pre,gi,p)
            if g==gen: res=matsub(res,pre,p)
    return res

def word_eval(word,rho,p,d):
    M=eye(d)
    for ch in word:
        g=ch.lower()
        M=matmul(M, rho[g] if ch.islower() else matinv(rho[g],p), p)
    return M

def cocycle_value(word,gens,rho,p,d,z):
    """z(word) = sum_j rho(d word/d x_j) z(x_j);  z given as list of g vectors"""
    out=[0]*d
    for j,g in enumerate(gens):
        F=fox(word,g,rho,p,d)
        for a in range(d):
            out[a]=(out[a]+sum(F[a][b]*z[j][b] for b in range(d)))%p
    return out

def invariants(mats,p,d):
    """dim of common kernel of (A - I) over the given matrices"""
    rows=[]
    for A in mats:
        B=matsub(A,eye(d),p)
        rows.extend(B)
    return d - rank(rows,p) if rows else d

def analyse(gens, rels, mu, lam, rho, p, d):
    g=len(gens)
    # Z^1 = ker of Fox Jacobian
    J=[]
    for r in rels:
        blocks=[fox(r,x,rho,p,d) for x in gens]
        for a in range(d):
            J.append([blocks[j][a][b] for j in range(g) for b in range(d)])
    Z=nullspace(J,p,g*d)
    t0=invariants([word_eval(mu,rho,p,d), word_eval(lam,rho,p,d)],p,d)
    # restriction of each cocycle to the cusp
    R=[]
    for v in Z:
        z=[v[j*d:(j+1)*d] for j in range(g)]
        R.append(cocycle_value(mu,gens,rho,p,d,z)+cocycle_value(lam,gens,rho,p,d,z))
    # B^1 of the torus
    Mu=word_eval(mu,rho,p,d); La=word_eval(lam,rho,p,d)
    Bt=[]
    for i in range(d):
        e=[1 if k==i else 0 for k in range(d)]
        a=[sum((Mu[x][y]-(1 if x==y else 0))*e[y] for y in range(d))%p for x in range(d)]
        b=[sum((La[x][y]-(1 if x==y else 0))*e[y] for y in range(d))%p for x in range(d)]
        Bt.append(a+b)
    rB=rank(Bt,p)
    r1=rank(R+Bt,p)-rB
    # t1 = dim H^1(T^2;V)
    Zt=nullspace([[ (Mu[x][y]-(1 if x==y else 0)) for y in range(d)]+[-(La[x][y]-(1 if x==y else 0))%p for y in range(d)] for x in range(d)],p,2*d)
    t1=len(Zt)-rB
    return dict(t0=t0,t1=t1,r1=r1,I=t0-r1,dimZ1=len(Z))

def a0_dim(gens,rho,p,d):
    """h^0(M;V) = dim V^{pi_1}"""
    rows=[]
    for g in gens:
        rows.extend(matsub(rho[g],eye(d),p))
    return d - rank(rows,p) if rows else d

def is_irreducible_2d(gens,rho,p):
    """2-dim rep: reducible iff the generators share an eigenvector"""
    for v in [[1,0]]+[[x,1] for x in range(p)]:
        ok=True
        for g in gens:
            A=rho[g]
            w=[(A[0][0]*v[0]+A[0][1]*v[1])%p,(A[1][0]*v[0]+A[1][1]*v[1])%p]
            if (w[0]*v[1]-w[1]*v[0])%p!=0: ok=False; break
        if ok: return False
    return True
