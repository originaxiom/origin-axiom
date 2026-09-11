"""Is L_V = L_{V*} as SUBSPACES of H^1(T;W), or merely equal in dimension?
r1 = r1* is a dimension statement. L_V = L_{V*} is the structural one, and it is
exactly 'L_V is Lagrangian', which is exactly I = 0 with a mechanism."""
import sys, warnings, itertools; sys.path.insert(0,'/tmp/sweep'); warnings.filterwarnings("ignore")
from fractions import Fraction as F
from q12 import *
from q12 import _dot
from final_index import (get_rho, wev, sym, blockdiag, fox, invariants, order3_chars)
from collections import Counter

def images(gens,rels,mu,lam,rho,d):
    """return (t0, basis of B^1(T), basis of the restriction image L, all in H^1(T))"""
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
    return t0, Bt, R

def same_span(A,B,Bt):
    """do A and B span the same subspace MODULO Bt?"""
    rA=rank(Bt+A); rB=rank(Bt+B); rAB=rank(Bt+A+B)
    return rA==rB==rAB, rA-rank(Bt), rB-rank(Bt), rAB-rank(Bt)

GERMS=[(2,),(2,2),(2,4),(2,2,2)]
for NM in sys.argv[1:] or ['s958']:
    got=get_rho(NM)
    if got is None: print(NM,'not recognised'); continue
    M,G,gens,rels,mu,lam,rho=got
    chars=order3_chars(gens,rels,mu,lam)
    print(f"=== {NM} ===  chiral={not M.symmetry_group().is_amphicheiral()}")
    same=0; diff=0
    for ms in GERMS:
        base={g:blockdiag([sym(rho[g],m) for m in ms]) for g in gens}
        d=sum(m+1 for m in ms)
        for psi in chars:
            V ={g:scal(powe(OMEGA,psi[i]),base[g]) for i,g in enumerate(gens)}
            Vd={g:scal(powe(OMEGA,(-psi[i])%3),base[g]) for i,g in enumerate(gens)}
            t0,Bt,LV = images(gens,rels,mu,lam,V,d)
            t0d,Btd,LVd= images(gens,rels,mu,lam,Vd,d)
            eq,rv,rvd,rboth = same_span(LV,LVd,Bt)
            tag = "L_V == L_V*" if eq else "L_V != L_V*"
            print(f"  Sym{ms} psi{psi}: t0={t0}  dim L_V={rv}  dim L_V*={rvd}  dim(L_V+L_V*)={rboth}   {tag}")
            if eq: same+=1
            else: diff+=1
    print(f"  --> identical subspaces: {same}   distinct: {diff}")
