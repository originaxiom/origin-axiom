"""The multi-cusp index, EXACTLY over Q(zeta_12), on m004's own chiral multi-cusped covers.

A prediction of the derivation, TESTED here rather than assumed:
peripheral holonomy is unipotent, so Sym^m of it has every eigenvalue 1; multiplying by a
primitive cube root leaves no eigenvalue 1.  Hence at a cusp where psi is NON-trivial,
t_0^(i) = t_0*^(i) = 0, so t_1^(i) = 0 and that cusp contributes NOTHING to t_0, t_1 or r_1.

If that holds, the index sees only its LIVE cusps (psi trivial there), B1332's mechanism applies
at each, and the genuinely new multi-cusp phenomenon -- cancellation BETWEEN cusps -- needs at
least TWO live cusps.  That is the sector to aim at, and it is reported per row.
"""
import sys, warnings, itertools; sys.path.insert(0,'/tmp/sweep'); warnings.filterwarnings("ignore")
from fractions import Fraction as Fr
from collections import Counter
from q12 import *
from q12 import _dot
from fi_lib import wev, sym, blockdiag, fox, invariants
from cup import invariant_forms, cocycles, cup, gram, reduce_mod

def expsum(word,gens):
    v=[0]*len(gens)
    for ch in word:
        if ch.islower(): v[gens.index(ch)]+=1
        else: v[gens.index(ch.lower())]-=1
    return v

def all_order3_chars(gens,rels):
    """every hom pi_1 -> Z/3 (as exponent vectors mod 3), trivial one included"""
    g=len(gens)
    M=[[x%3 for x in expsum(r,gens)] for r in rels]
    piv=[]; r=0
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
        out.add(tuple(v))
    return sorted(out)

def chi_on(word,gens,psi):
    return sum(e*p for e,p in zip(expsum(word,gens),psi))%3

def analyse_exact(gens,rels,per,rho,d):
    """a_0, Z^1, per-cusp t_0/t_1, r_1 -- exact over Q(zeta_12)"""
    g=len(gens)
    a0=invariants([rho[x] for x in gens],d)
    J=[]
    for r in rels:
        bl=[fox(r,x,rho,d) for x in gens]
        for a in range(d): J.append([bl[j][a][b] for j in range(g) for b in range(d)])
    Zs=nullspace(J,g*d)
    a1=len(Zs)-(d-a0)
    cusps=[]
    for (mu,lam) in per:
        A=wev(mu,rho,d); B=wev(lam,rho,d)
        t0=invariants([A,B],d)
        Zt,Bt_=cocycles(A,B,d)
        cusps.append(dict(mu=mu,lam=lam,A=A,B=B,t0=t0,t1=len(Zt)-(d-t0)))
    c=len(cusps)
    FX={}
    for x in cusps:
        FX[x['mu']]=[fox(x['mu'],gg,rho,d) for gg in gens]
        FX[x['lam']]=[fox(x['lam'],gg,rho,d) for gg in gens]
    R=[]
    for v in Zs:
        z=[v[j*d:(j+1)*d] for j in range(g)]
        row=[]
        for x in cusps:
            for w in (x['mu'],x['lam']):
                out=[Z]*d
                for j in range(g):
                    Fx=FX[w][j]
                    for a in range(d):
                        s=out[a]
                        for b in range(d):
                            if not is_zero(Fx[a][b]): s=add(s,mul(Fx[a][b],z[j][b]))
                        out[a]=s
                row+=out
        R.append(row)
    Bt=[]
    for i,x in enumerate(cusps):
        Am=msub(x['A'],eye(d)); Bm=msub(x['B'],eye(d))
        for k in range(d):
            row=[Z]*(2*c*d)
            for r_ in range(d):
                row[2*i*d+r_]=Am[r_][k]; row[2*i*d+d+r_]=Bm[r_][k]
            Bt.append(row)
    rB=rank(Bt); r1=rank(R+Bt)-rB
    return dict(c=c,a0=a0,a1=a1,t0=sum(x['t0'] for x in cusps),t1=sum(x['t1'] for x in cusps),
                t0s=[x['t0'] for x in cusps],t1s=[x['t1'] for x in cusps],r1=r1,n=a1-r1,
                live=sum(1 for x in cusps if x['t0']>0))
