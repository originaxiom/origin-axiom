"""The index on the GEOMETRIC holonomy, exactly over Q(omega). No prime, no reduction."""
import sys, snappy, warnings; sys.path.insert(0,'/tmp/sweep'); warnings.filterwarnings("ignore")
import numpy as np
from fractions import Fraction as F
from qw import *
from qw import _dot
from math import comb
W = complex(-0.5,(3**0.5)/2)

def recognise(z, maxden=400, tol=1e-6):
    b=z.imag/W.imag; a=z.real-b*W.real
    fa,fb=F(a).limit_denominator(maxden),F(b).limit_denominator(maxden)
    return (fa,fb) if abs(complex(float(fa)+float(fb)*W)-z)<tol else None

def exact_holonomy(nm):
    M=snappy.Manifold(nm); G=M.fundamental_group()
    mu,lam=G.peripheral_curves()[0]
    Mu=np.array([[complex(x) for x in r] for r in G.SL2C(mu)])
    tr=Mu[0,0]+Mu[1,1]
    N=Mu-np.sign(tr.real)*np.eye(2)
    fp = -N[1,1]/N[1,0] if abs(N[1,0])>1e-12 else (-N[0,1]/N[0,0] if abs(N[0,0])>1e-12 else None)
    C = np.eye(2,dtype=complex) if fp is None else np.array([[0,1],[1,-fp]],dtype=complex)
    Ci=np.linalg.inv(C)
    Mn=C@Mu@Ci; t=Mn[0,1] if abs(Mn[0,1])>1e-12 else 1.0
    D=np.array([[1,0],[0,t]],dtype=complex); Di=np.linalg.inv(D)
    rho={}
    for g in G.generators():
        A=np.array([[complex(x) for x in r] for r in G.SL2C(g)])
        B=Di@C@A@Ci@D
        r=[[recognise(B[i,j]) for j in range(2)] for i in range(2)]
        if any(x is None for row in r for x in row): return None
        rho[g]=r
    return M,G,list(G.generators()),list(G.relators()),mu,lam,rho

def wev(word,rho):
    R=eye(2)
    for ch in word:
        g=ch.lower()
        R=mm(R, rho[g] if ch.islower() else minv2(rho[g]))
    return R

def sym(A,m):
    d=m+1; out=[[Z]*d for _ in range(d)]
    a,b=A[0]; c,dd=A[1]
    for j in range(d):
        coef=[Z]*d
        for s in range(m-j+1):
            for t in range(j+1):
                cf=mul(mul((F(comb(m-j,s)),F(0)), _pw(a,m-j-s)), _pw(c,s))
                cf=mul(cf, mul(mul((F(comb(j,t)),F(0)), _pw(b,j-t)), _pw(dd,t)))
                coef[s+t]=add(coef[s+t],cf)
        for i in range(d): out[i][j]=coef[i]
    return out
def _pw(x,k):
    r=ONE
    for _ in range(k): r=mul(r,x)
    return r
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
def wev_d(word,rho,d):
    R=eye(d)
    for ch in word:
        g=ch.lower()
        R=mm(R, rho[g] if ch.islower() else minv(rho[g]))
    return R
def invariants(mats,d):
    rows=[]
    for A in mats: rows.extend(msub(A,eye(d)))
    return d-rank(rows) if rows else d
def analyse(gens,rels,mu,lam,rho,d):
    g=len(gens); J=[]
    for r in rels:
        blocks=[fox(r,x,rho,d) for x in gens]
        for a in range(d):
            J.append([blocks[j][a][b] for j in range(g) for b in range(d)])
    Zs=nullspace(J,g*d)
    Mu=wev_d(mu,rho,d); La=wev_d(lam,rho,d)
    t0=invariants([Mu,La],d)
    R=[]
    for v in Zs:
        z=[v[j*d:(j+1)*d] for j in range(g)]
        def cval(word):
            out=[Z]*d
            for j,gg in enumerate(gens):
                Fx=fox(word,gg,rho,d)
                for a in range(d):
                    s=out[a]
                    for b in range(d): s=add(s,mul(Fx[a][b],z[j][b]))
                    out[a]=s
            return out
        R.append(cval(mu)+cval(lam))
    Bt=[]
    for i in range(d):
        e=[ONE if k==i else Z for k in range(d)]
        a=[_dot(msub(Mu,eye(d))[x],e) for x in range(d)]
        b=[_dot(msub(La,eye(d))[x],e) for x in range(d)]
        Bt.append(a+b)
    rB=rank(Bt); r1=rank(R+Bt)-rB
    return dict(t0=t0,r1=r1,I=t0-r1,a0=invariants([rho[g] for g in gens],d))

NM=sys.argv[1] if len(sys.argv)>1 else 's958'
res=exact_holonomy(NM)
if res is None: print(NM,"not recognisable over Q(omega)"); sys.exit()
M,G,gens,rels,mu,lam,rho=res
print(f"=== {NM} : geometric holonomy exact over Q(omega) ===")
print("  chiral:",not M.symmetry_group().is_amphicheiral())
ok=True
for r in rels:
    Rm=wev(r,rho)
    isI = Rm==eye(2)
    isMI = Rm==scal((F(-1),F(0)),eye(2))
    print(f"  relator {r!r} -> {'I' if isI else ('-I' if isMI else 'NOT +-I  ** FAIL **')}")
    ok &= (isI or isMI)
print("  RELATORS VALIDATED:",ok)

# ---- order-3 cusp-trivial characters, valued in mu_3 subset Q(omega)* ----
def expsum(word,gens):
    v=[0]*len(gens)
    for ch in word:
        if ch.islower(): v[gens.index(ch)]+=1
        else: v[gens.index(ch.lower())]-=1
    return v
def order3_chars(gens,rels,mu,lam):
    import itertools
    g=len(gens)
    rows=[[x%3 for x in expsum(r,gens)] for r in rels]+[[x%3 for x in expsum(mu,gens)],[x%3 for x in expsum(lam,gens)]]
    # nullspace mod 3
    M=[r[:] for r in rows]; piv=[]; r=0
    for c in range(g):
        p=next((i for i in range(r,len(M)) if M[i][c]%3),None)
        if p is None: continue
        M[r],M[p]=M[p],M[r]
        iv=pow(M[r][c],1,3); iv=1 if M[r][c]%3==1 else 2
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

chars=order3_chars(gens,rels,mu,lam)
print("  order-3 cusp-trivial characters:",len(chars))
GERMS=[(1,),(2,),(1,1),(2,2),(1,2),(2,4),(1,1,1),(2,2,2),(1,2,3),(2,4,6)]
from collections import Counter
res=Counter(); nonzero=[]; tot=0
for ms in GERMS:
    base={g:blockdiag([sym(rho[g],m) for m in ms]) for g in gens}
    d=sum(m+1 for m in ms)
    for psi in chars:
        V ={g:scal(powom(psi[i]),base[g]) for i,g in enumerate(gens)}
        Vd={g:scal(powom((-psi[i])%3),base[g]) for i,g in enumerate(gens)}
        A=analyse(gens,rels,mu,lam,V,d); B=analyse(gens,rels,mu,lam,Vd,d)
        if A['a0']!=B['a0'] or A['t0']!=B['t0']: continue
        tot+=1; res[(A['t0'],A['I'])]+=1
        if A['I']!=0: nonzero.append((ms,psi,A,B))
print()
print(f"  EXACT in-domain sectors over Q(omega): {tot}")
print(f"  (t0, I) distribution: {dict(sorted(res.items()))}")
print(f"  sectors with t0 >= 2: {sum(v for (t,i),v in res.items() if t>=2)}")
print(f"  NON-ZERO INDEX: {len(nonzero)}")
for x in nonzero[:8]: print("     Sym",x[0],"psi",x[1],"t0=",x[2]['t0'],"r1=",x[2]['r1'],"I=",x[2]['I'])
