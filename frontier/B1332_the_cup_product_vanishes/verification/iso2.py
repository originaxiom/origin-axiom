"""Isotropy where it is NOT vacuous: dim L_V >= 2, so the Gram has off-diagonal entries to kill.

For an alternating pairing every 1-dim subspace is isotropic for free, so Sym^2 alone says nothing.
Germs with t_0 >= 2 give dim L_V >= 2 and C(r,2) genuine equations.
Also: check isotropy against EVERY pi_1(T)-invariant form, not just the canonical SL2 one --
L_{V*} is the canonical annihilator and does not depend on a choice, so a choice-dependent
answer would be a red flag.
"""
import sys, warnings; sys.path.insert(0,'/tmp/sweep'); warnings.filterwarnings("ignore")
from iso import restrict, sl2form
from cup import *
from q12 import *
from fi_lib import get_rho, sym, blockdiag, order3_chars

def show(x):
    a,b,c,d=x
    return "0" if a==b==c==d==0 else f"({a},{b},{c},{d})"

NM=sys.argv[1]; MS=tuple(int(c) for c in sys.argv[2])
M,G,gens,rels,mu,lam,rho=get_rho(NM)
base={g:blockdiag([sym(rho[g],m) for m in MS]) for g in gens}
d=sum(m+1 for m in MS); Fc=sl2form(MS)
print(f"{NM} germ Sym^{MS} d={d}", flush=True)
for psi in [tuple([0]*len(gens))]+list(order3_chars(gens,rels,mu,lam)):
    V ={g:scal(powe(OMEGA,psi[i]),base[g]) for i,g in enumerate(gens)}
    Vd={g:scal(powe(OMEGA,(-psi[i])%3),base[g]) for i,g in enumerate(gens)}
    R,Bt,A,B,t0=restrict(gens,rels,mu,lam,V,d)
    Rd,_,Ad,Bd,t0d=restrict(gens,rels,mu,lam,Vd,d)
    assert A==Ad and B==Bd, "psi not cusp-trivial"
    rB=rank(Bt)
    LV=reduce_mod(R,Bt,2*d); LVd=reduce_mod(Rd,Bt,2*d)
    r1,r1d=len(LV),len(LVd)
    Zs,Bs=cocycles(A,B,d); H=reduce_mod(Zs,Bs,2*d); t1=len(H)
    same = (rank(LV+LVd+Bt)-rB == r1 == r1d)
    G1=gram(LV,A,B,Fc,d)
    iso_c=all(is_zero(x) for row in G1 for x in row)
    # every pi_1(T)-invariant form
    Fs=invariant_forms([A,B],d)
    iso_all=[]
    for Fx in Fs:
        Gx=gram(LV,A,B,Fx,d)
        iso_all.append(all(is_zero(x) for row in Gx for x in row))
    print(f"\n psi={psi}: t0={t0} t1={t1} dim L_V={r1} dim L_V*={r1d} I={t0-r1}  L_V==L_V*: {same}")
    print(f"   equations isotropy imposes: {r1*(r1-1)//2 if r1>1 else 0}"
          f"   {'(VACUOUS: dim 1 and the form is alternating)' if r1<2 else '(NON-VACUOUS)'}")
    print(f"   GRAM (canonical SL2 form), {r1}x{r1}:")
    for row in G1: print("      [", "  ".join(show(x) for x in row), "]")
    print(f"   ISOTROPIC (canonical): {iso_c}")
    print(f"   pi_1(T)-invariant forms on W: {len(Fs)};  isotropic for ALL of them: {all(iso_all)}"
          f"  (for {sum(iso_all)}/{len(Fs)})", flush=True)
