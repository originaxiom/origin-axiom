"""The index on the geometric holonomy, exactly over Q(zeta_12), for the target manifolds."""
import sys, warnings, itertools; sys.path.insert(0,'/tmp/sweep'); warnings.filterwarnings("ignore")
from fractions import Fraction as F
from math import comb
from q12 import *
from q12 import _dot
from recog12 import normalised, in_Qs3
from collections import Counter

def entry(z):
    a=in_Qs3(z.real); b=in_Qs3(z.imag)
    if a is None or b is None: return None
    return (a[0],a[1],b[0],b[1])
def get_rho(nm):
    M,G,gens,rels,mu,lam,rec = normalised(nm)
    rho={}
    for g in gens:
        E=[[entry(rec[g][i][j]) for j in range(2)] for i in range(2)]
        if any(x is None for r in E for x in r): return None
        rho[g]=E
    return M,G,gens,rels,mu,lam,rho
def wev(word,rho,d):
    R=eye(d)
    for ch in word:
        g=ch.lower()
        R=mm(R, rho[g] if ch.islower() else minv(rho[g]))
    return R
def sym(A,m):
    d=m+1; out=[[Z]*d for _ in range(d)]
    a,b=A[0]; c,dd=A[1]
    for j in range(d):
        coef=[Z]*d
        for s in range(m-j+1):
            for t in range(j+1):
                cf=mul(mul((F(comb(m-j,s)),F(0),F(0),F(0)),powe(a,m-j-s)),powe(c,s))
                cf=mul(cf,mul(mul((F(comb(j,t)),F(0),F(0),F(0)),powe(b,j-t)),powe(dd,t)))
                coef[s+t]=add(coef[s+t],cf)
        for i in range(d): out[i][j]=coef[i]
    return out
def blockdiag(ms):
    d=sum(len(m) for m in ms); out=[[Z]*d for _ in range(d)]; o=0
    for m in ms:
        k=len(m)
        for i in range(k):
            for j in range(k): out[o+i][o+j]=m[i][j]
        o+=k
    return out
def fox(word,gen,rho,d):
    res=[[Z]*d for _ in range(d)]; pre=eye(d)
    for ch in word:
        g=ch.lower()
        if ch.islower():
            if g==gen: res=[[add(res[i][j],pre[i][j]) for j in range(d)] for i in range(d)]
            pre=mm(pre,rho[g])
        else:
            gi=minv(rho[g]); pre=mm(pre,gi)
            if g==gen: res=[[sub(res[i][j],pre[i][j]) for j in range(d)] for i in range(d)]
    return res
def invariants(mats,d):
    rows=[]
    for A in mats: rows.extend(msub(A,eye(d)))
    return d-rank(rows) if rows else d
def analyse(gens,rels,mu,lam,rho,d):
    g=len(gens); J=[]
    for r in rels:
        bl=[fox(r,x,rho,d) for x in gens]
        for a in range(d): J.append([bl[j][a][b] for j in range(g) for b in range(d)])
    Zs=nullspace(J,g*d)
    Mu=wev(mu,rho,d); La=wev(lam,rho,d)
    t0=invariants([Mu,La],d)
    R=[]
    for v in Zs:
        z=[v[j*d:(j+1)*d] for j in range(g)]
        def cv(word):
            out=[Z]*d
            for j,gg in enumerate(gens):
                Fx=fox(word,gg,rho,d)
                for a in range(d):
                    s=out[a]
                    for b in range(d): s=add(s,mul(Fx[a][b],z[j][b]))
                    out[a]=s
            return out
        R.append(cv(mu)+cv(lam))
    Bt=[]
    for i in range(d):
        e=[ONE if k==i else Z for k in range(d)]
        Bt.append([_dot(msub(Mu,eye(d))[x],e) for x in range(d)]+[_dot(msub(La,eye(d))[x],e) for x in range(d)])
    rB=rank(Bt); r1=rank(R+Bt)-rB
    return dict(t0=t0,r1=r1,I=t0-r1,a0=invariants([rho[g] for g in gens],d))
def expsum(word,gens):
    v=[0]*len(gens)
    for ch in word:
        if ch.islower(): v[gens.index(ch)]+=1
        else: v[gens.index(ch.lower())]-=1
    return v
def order3_chars(gens,rels,mu,lam):
    g=len(gens)
    rows=[[x%3 for x in expsum(r,gens)] for r in rels]+[[x%3 for x in expsum(mu,gens)],[x%3 for x in expsum(lam,gens)]]
    M=[r[:] for r in rows]; piv=[]; r=0
    for c in range(g):
        p=next((i for i in range(r,len(M)) if M[i][c]%3),None)
        if p is None: continue
        M[r],M[p]=M[p],M[r]
        iv=1 if M[r][c]%3==1 else 2
        M[r]=[(x*iv)%3 for x in M[r]]
        for i in range(len(M)):
            if i!=r and M[i][c]%3:
                f=M[i][c]; M[i]=[(M[i][j]-f*M[r][j])%3 for j in range(g)]
        piv.append(c); r+=1
    free=[c for c in range(g) if c not in piv]
    basis=[]
    for fc in free:
        v=[0]*g; v[fc]=1
        for i,pc in enumerate(piv): v[pc]=(-M[i][fc])%3
        basis.append(v)
    out=set()
    for co in itertools.product(range(3),repeat=len(basis)):
        v=[0]*g
        for c,b in zip(co,basis):
            for i in range(g): v[i]=(v[i]+c*b[i])%3
        if any(v): out.add(tuple(v))
    return sorted(out)
