"""The decisive test: is the index non-zero in CHARACTERISTIC ZERO, on the GEOMETRIC holonomy?

The mod-p hits use arbitrary SL2(F_p) reps. In char 0 the parabolic SL2(C) character variety of a
one-cusped manifold is FINITE, so most mod-p reps have no char-0 counterpart. The one that matters
is rho_geo. So: compute the index for Sym^m(rho_geo) (x) psi at high precision, with psi a
cusp-trivial character of H_1(M)/<peripheral> valued in roots of unity.

Ranks are numerical, so every one is reported with its SINGULAR-VALUE GAP -- the ratio of the
smallest kept to the largest dropped. A verdict with a narrow gap is not a verdict.
"""
import sys, warnings, itertools, os; sys.path.insert(0,'/tmp/sweep'); warnings.filterwarnings("ignore")
import snappy
from mpmath import mp, mpc, mpf, svd_r, matrix, exp, pi, mpmathify
mp.dps=60
from recog12 import clean

def tompc(x): return mpc(mpf(clean(x.real())), mpf(clean(x.imag())))
def mm(A,B):
    n=len(A);k=len(B);m=len(B[0])
    return [[sum(A[i][t]*B[t][j] for t in range(k)) for j in range(m)] for i in range(n)]
def eye(n): return [[mpc(1) if i==j else mpc(0) for j in range(n)] for i in range(n)]
def minv2(A):
    d=A[0][0]*A[1][1]-A[0][1]*A[1][0]
    return [[A[1][1]/d,-A[0][1]/d],[-A[1][0]/d,A[0][0]/d]]
def minv(A):
    n=len(A); M=[list(r)+list(e) for r,e in zip(A,eye(n))]
    r=0
    for c in range(n):
        p=max(range(r,n),key=lambda i:abs(M[i][c]))
        if abs(M[p][c])<mpf(10)**-40: return None
        M[r],M[p]=M[p],M[r]; pv=M[r][c]; M[r]=[x/pv for x in M[r]]
        for i in range(n):
            if i!=r:
                f=M[i][c]; M[i]=[M[i][j]-f*M[r][j] for j in range(2*n)]
        r+=1
    return [row[n:] for row in M]
def numrank(M):
    """rank by singular values, with the gap reported"""
    if not M or not M[0]: return 0,None
    rows=len(M); cols=len(M[0])
    A=matrix(rows*2,cols*2)
    for i in range(rows):
        for j in range(cols):
            re=M[i][j].real; im=M[i][j].imag
            A[2*i,2*j]=re;   A[2*i,2*j+1]=-im
            A[2*i+1,2*j]=im; A[2*i+1,2*j+1]=re
    s=svd_r(A,compute_uv=False)
    sv=sorted([abs(x) for x in s],reverse=True)
    if not sv: return 0,None
    tol=sv[0]*mpf(10)**-25
    k=sum(1 for x in sv if x>tol)
    gap=(sv[k-1]/sv[k]) if 0<k<len(sv) else None
    return k//2,gap
def wev(w,rho,d):
    R=eye(d)
    for ch in w: R=mm(R, rho[ch.lower()] if ch.islower() else minv(rho[ch.lower()]))
    return R
def fox(w,gen,rho,d):
    res=[[mpc(0)]*d for _ in range(d)]; pre=eye(d)
    for ch in w:
        g=ch.lower()
        if ch.islower():
            if g==gen: res=[[res[i][j]+pre[i][j] for j in range(d)] for i in range(d)]
            pre=mm(pre,rho[g])
        else:
            pre=mm(pre,minv(rho[g]))
            if g==gen: res=[[res[i][j]-pre[i][j] for j in range(d)] for i in range(d)]
    return res
def sym(A,m):
    from math import comb
    d=m+1;out=[[mpc(0)]*d for _ in range(d)];a,b=A[0];c,dd=A[1]
    for j in range(d):
        coef=[mpc(0)]*d
        for u in range(m-j+1):
            for v in range(j+1):
                coef[u+v]+=comb(m-j,u)*a**(m-j-u)*c**u*comb(j,v)*b**(j-v)*dd**v
        for i in range(d): out[i][j]=coef[i]
    return out
def nullsp_num(M,n):
    """numerical nullspace basis via row reduction with pivoting"""
    if not M: return [[mpc(1) if i==j else mpc(0) for i in range(n)] for j in range(n)]
    A=[list(r) for r in M]; rows=len(A); r=0; piv=[]
    for c in range(n):
        p=max(range(r,rows),key=lambda i:abs(A[i][c])) if r<rows else None
        if p is None or abs(A[p][c])<mpf(10)**-30: continue
        A[r],A[p]=A[p],A[r]; pv=A[r][c]; A[r]=[x/pv for x in A[r]]
        for i in range(rows):
            if i!=r and abs(A[i][c])>0:
                f=A[i][c]; A[i]=[A[i][j]-f*A[r][j] for j in range(n)]
        piv.append(c); r+=1
        if r==rows: break
    free=[c for c in range(n) if c not in piv]; out=[]
    for fc in free:
        v=[mpc(0)]*n; v[fc]=mpc(1)
        for i,pc in enumerate(piv): v[pc]=-A[i][fc]
        out.append(v)
    return out

def inv_dim(ms,d):
    rows=[]
    for A in ms: rows.extend([[A[i][j]-(mpc(1) if i==j else mpc(0)) for j in range(d)] for i in range(d)])
    r,g=numrank(rows); return d-r,g

def expsum(word,gens):
    v=[0]*len(gens)
    for ch in word:
        if ch.islower(): v[gens.index(ch)]+=1
        else: v[gens.index(ch.lower())]-=1
    return v

NAME=os.environ.get('MF','m010')
M=snappy.ManifoldHP(NAME); G=M.fundamental_group()
gens=list(G.generators()); rels=list(G.relators()); mu,lam=G.peripheral_curves()[0]
rho={g:[[tompc(G.SL2C(g)[i,j]) for j in range(2)] for i in range(2)] for g in gens}
print(f"{NAME}: gens={gens} rels={rels}  volume={float(M.volume()):.6f}")
for r in rels:
    R=wev(r,rho,2)
    err=max(abs(R[i][j]-(mpc(1) if i==j else mpc(0))) for i in range(2) for j in range(2))
    err2=max(abs(R[i][j]+(mpc(1) if i==j else mpc(0))) for i in range(2) for j in range(2))
    print(f"  relator {r!r}: |rho(r)-I|={float(min(err,err2)):.2e}  -> {'+I' if err<err2 else '-I'}")
Mu=wev(mu,rho,2); La=wev(lam,rho,2)
print(f"  tr(mu)={complex(Mu[0][0]+Mu[1][1]):.6f}  tr(lam)={complex(La[0][0]+La[1][1]):.6f}  (should be +-2: parabolic)")
# cusp-trivial characters: the dual of H_1/<peripheral>.  Order n characters valued in mu_n.
N=int(os.environ.get('ORD','6'))
z=exp(2*pi*mpc(0,1)/N)
cands=[]
for tup in itertools.product(range(N),repeat=len(gens)):
    ok=True
    for w in list(rels)+[mu,lam]:
        if sum(e*t for e,t in zip(expsum(w,gens),tup))%N!=0: ok=False; break
    if ok and any(tup): cands.append(tup)
print(f"  cusp-trivial characters of order dividing {N}: {cands}")
for psi in cands:
    for m in [int(x) for x in os.environ.get('MS','1,2,3,4').split(',')]:
        d=m+1
        V={g:[[(z**psi[i])*sym(rho[g],m)[x][y] for y in range(d)] for x in range(d)] for i,g in enumerate(gens)}
        bad=max(max(abs(wev(r,V,d)[i][j]-(mpc(1) if i==j else mpc(0))) for i in range(d) for j in range(d)) for r in rels)
        if bad>mpf(10)**-20: print(f"    psi={psi} Sym^{m}: NOT a representation (err {float(bad):.1e}) -- skipped"); continue
        g=len(gens); J=[]
        for r in rels:
            bl=[fox(r,x,V,d) for x in gens]
            for a in range(d): J.append([bl[j][a][b] for j in range(g) for b in range(d)])
        rJ,gJ=numrank(J); dimZ=g*d-rJ
        a0,_=inv_dim([V[x] for x in gens],d)
        a1=dimZ-(d-a0)
        MuV=wev(mu,V,d); LaV=wev(lam,V,d)
        t0,gt=inv_dim([MuV,LaV],d)
        # restriction to the cusp, and r_1
        Zs=nullsp_num(J,g*d)
        FXm=[fox(mu,x,V,d) for x in gens]; FXl=[fox(lam,x,V,d) for x in gens]
        R=[]
        for zv in Zs:
            z2=[zv[j*d:(j+1)*d] for j in range(g)]; row=[]
            for FX in (FXm,FXl):
                o=[mpc(0)]*d
                for j in range(g):
                    for a in range(d): o[a]+=sum(FX[j][a][b]*z2[j][b] for b in range(d))
                row+=o
            R.append(row)
        Bt=[]
        for k in range(d):
            Bt.append([MuV[x][k]-(mpc(1) if x==k else mpc(0)) for x in range(d)]+
                      [LaV[x][k]-(mpc(1) if x==k else mpc(0)) for x in range(d)])
        rB,_=numrank(Bt); rRB,gR=numrank(R+Bt); r1=rRB-rB
        print(f"    psi={psi} Sym^{m}: a0={a0} a1={a1} t0={t0} r1={r1}  I = t0-r1 = {t0-r1}"
              f"   (gaps: J {float(gJ) if gJ else 0:.2e}, t0 {float(gt) if gt else 0:.2e}, R {float(gR) if gR else 0:.2e})")
