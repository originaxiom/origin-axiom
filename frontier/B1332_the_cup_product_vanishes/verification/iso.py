"""IS L_V ISOTROPIC?  The whole vanishing theorem, reduced to one Gram matrix.

Why the question is even well-posed:  psi is CUSP-TRIVIAL, so on the cusp torus
V|_T = Sym^m = V*|_T -- the same pi_1(T)-module.  Hence H^1(T;V) and H^1(T;V*)
are the same space, t_0 = t_0* for free, and the canonical perfect pairing
H^1(T;V) x H^1(T;V*) -> C becomes a pairing of H^1(T;W) with itself.
L_V and L_{V*} are mutual annihilators (Poincare-Lefschetz), so
     L_V isotropic  ==>  dim L_V <= t_1/2,  same for V*,  and they sum to t_1
     ==> r_1 = t_1/2 = t_0  ==>  I = 0.
"""
import sys, warnings; sys.path.insert(0,'/tmp/sweep'); warnings.filterwarnings("ignore")
from fractions import Fraction as Fr
from collections import Counter
from cup import *
from q12 import *
from q12 import _dot
from fi_lib import get_rho, wev, sym, blockdiag, fox, invariants, order3_chars

def restrict(gens,rels,mu,lam,rho,d):
    """R = restriction of H^1(M;V) cocycles to the torus, as (z(mu),z(lam)); Bt = B^1(T)"""
    g=len(gens); J=[]
    for r in rels:
        bl=[fox(r,x,rho,d) for x in gens]
        for a in range(d): J.append([bl[j][a][b] for j in range(g) for b in range(d)])
    Zs=nullspace(J,g*d)
    Mu=wev(mu,rho,d); La=wev(lam,rho,d)
    # Fox derivatives of mu and lam do not depend on the cocycle -- compute once
    FXmu=[fox(mu,gg,rho,d) for gg in gens]
    FXla=[fox(lam,gg,rho,d) for gg in gens]
    R=[]
    for v in Zs:
        z=[v[j*d:(j+1)*d] for j in range(g)]
        def cv(FX):
            out=[Z]*d
            for j in range(g):
                Fx=FX[j]
                for a in range(d):
                    s=out[a]
                    for b in range(d):
                        if not is_zero(Fx[a][b]): s=add(s,mul(Fx[a][b],z[j][b]))
                    out[a]=s
            return out
        R.append(cv(FXmu)+cv(FXla))
    Bt=[]
    for i in range(d):
        e=[ONE if k==i else Z for k in range(d)]
        Bt.append([_dot(msub(Mu,eye(d))[x],e) for x in range(d)]+[_dot(msub(La,eye(d))[x],e) for x in range(d)])
    t0=invariants([Mu,La],d)
    return R,Bt,Mu,La,t0

def sl2form(ms):
    """the canonical SL2-invariant form on W = (+) Sym^{m_i}, block by block"""
    g1=[[ONE,ONE],[Z,ONE]]; g2=[[ONE,Z],[ONE,ONE]]
    blocks=[invariant_forms([sym(g1,m),sym(g2,m)],m+1)[0] for m in ms]
    return blockdiag(blocks)

if __name__=="__main__":
    GERMS=[(2,),(4,),(2,2),(2,4),(4,4),(2,2,2)]
    for NM in sys.argv[1:] or ['s958']:
        got=get_rho(NM)
        if got is None: print(f"{NM}: not recognised"); continue
        M,G,gens,rels,mu,lam,rho=got
        print(f"\n=== {NM} ===  chiral={not M.symmetry_group().is_amphicheiral()}", flush=True)
        mI=scal((Fr(-1),Fr(0),Fr(0),Fr(0)),eye(2)); proj=False
        for r in rels:
            R2=wev(r,rho,2)
            assert R2==eye(2) or R2==mI, f"relator {r} -> neither +I nor -I"
            if R2==mI: proj=True
        assert all(m%2==0 for ms in GERMS for m in ms), "odd germ present: invalid under a -I lift"
        print(f"  relators -> {'-I present: PROJECTIVE lift' if proj else '+I: genuine SL2 lift'}"
              f"; all germs even, so Sym^even(-I)=+I -- safe")
        chars=order3_chars(gens,rels,mu,lam)
        print(f"  cusp-trivial order-3 characters: {len(chars)}")
        tally=Counter(); bad=[]
        for ms in GERMS:
            base={g:blockdiag([sym(rho[g],m) for m in ms]) for g in gens}
            d=sum(m+1 for m in ms)
            Fm=sl2form(ms)
            for psi in [tuple([0]*len(gens))]+list(chars):
                V ={g:scal(powe(OMEGA,psi[i]),base[g]) for i,g in enumerate(gens)}
                Vd={g:scal(powe(OMEGA,(-psi[i])%3),base[g]) for i,g in enumerate(gens)}
                R,Bt,A,B,t0 = restrict(gens,rels,mu,lam,V,d)
                Rd,_,Ad,Bd,t0d= restrict(gens,rels,mu,lam,Vd,d)
                # CUSP-TRIVIALITY, verified not assumed: the cusp matrices agree for V and V*
                assert A==Ad and B==Bd, "psi is NOT cusp-trivial -- the pairing is not defined"
                rB=rank(Bt); t1=len(cocycles(A,B,d)[0])-rB
                r1=rank(R+Bt)-rB; r1d=rank(Rd+Bt)-rB
                LV =reduce_mod(R, Bt,2*d)
                LVd=reduce_mod(Rd,Bt,2*d)
                Gm=gram(LV,A,B,Fm,d)
                iso=all(is_zero(x) for row in Gm for x in row)
                same=(rank(LV+LVd+Bt)-rB==r1==r1d)     # L_V = L_{V*} as subspaces of H^1(T;W)
                tally[(t0,t1,r1,iso,same,t0-r1)]+=1
                if not iso: bad.append((ms,psi,t0,t1,r1,Gm))
        print(f"  sectors: {sum(tally.values())}")
        for k in sorted(tally): 
            t0,t1,r1,iso,same,I=k
            print(f"    t0={t0} t1={t1} r1={r1} I={I}  ISOTROPIC={iso}  L_V==L_V*={same}   x{tally[k]}")
        print(f"  NON-ISOTROPIC SECTORS: {len(bad)}", flush=True)
