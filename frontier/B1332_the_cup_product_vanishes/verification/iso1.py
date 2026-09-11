"""One germ, printed in full: the Gram matrix of the cup product on L_V."""
import sys, warnings; sys.path.insert(0,'/tmp/sweep'); warnings.filterwarnings("ignore")
from fractions import Fraction as Fr
from iso import restrict, sl2form
from cup import *
from q12 import *
from fi_lib import get_rho, wev, sym, blockdiag, order3_chars, invariants

def show(x):
    a,b,c,dd=x
    if a==b==c==dd==0: return "0"
    return f"({a},{b},{c},{dd})"

NM=sys.argv[1] if len(sys.argv)>1 else 's958'
MS=tuple(int(c) for c in (sys.argv[2] if len(sys.argv)>2 else '2'))
M,G,gens,rels,mu,lam,rho=get_rho(NM)
print(f"{NM}  germ Sym^{MS}  gens={gens} rels={rels}")
print(f"  mu={mu!r}  lam={lam!r}")
base={g:blockdiag([sym(rho[g],m) for m in MS]) for g in gens}
d=sum(m+1 for m in MS); Fm=sl2form(MS)
chars=[tuple([0]*len(gens))]+list(order3_chars(gens,rels,mu,lam))
for psi in chars:
    V ={g:scal(powe(OMEGA,psi[i]),base[g]) for i,g in enumerate(gens)}
    Vd={g:scal(powe(OMEGA,(-psi[i])%3),base[g]) for i,g in enumerate(gens)}
    R,Bt,A,B,t0=restrict(gens,rels,mu,lam,V,d)
    Rd,_,Ad,Bd,t0d=restrict(gens,rels,mu,lam,Vd,d)
    cusp_same = (A==Ad and B==Bd)
    rB=rank(Bt); t1=len(cocycles(A,B,d)[0])-rB
    LV=reduce_mod(R,Bt,2*d); LVd=reduce_mod(Rd,Bt,2*d)
    r1=len(LV); r1d=len(LVd)
    Gm=gram(LV,A,B,Fm,d)
    # the ambient H^1(T;W) Gram, for contrast: it must be nondegenerate
    Zs,Bs=cocycles(A,B,d); H=reduce_mod(Zs,Bs,2*d); GH=gram(H,A,B,Fm,d)
    print(f"\n  psi={psi}  cusp-trivial(V|T == V*|T): {cusp_same}")
    print(f"    t0={t0} t0*={t0d}  t1={t1}   dim L_V={r1}  dim L_V*={r1d}   I=t0-r1={t0-r1}")
    print(f"    ambient H^1(T;W): dim={len(H)}  cup rank={rank(GH)}  (nondegenerate={rank(GH)==len(H)})")
    print(f"    GRAM of cup on L_V ({r1}x{r1}):")
    for row in Gm: print("      [", "  ".join(show(x) for x in row), "]")
    print(f"    ISOTROPIC: {all(is_zero(x) for row in Gm for x in row)}")
