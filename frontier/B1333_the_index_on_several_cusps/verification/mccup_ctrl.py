"""CONTROL: the same multi-cusp cup code, run on ONE-CUSPED manifolds.
B1332 established L_V is Lagrangian there. If this code does not reproduce ISOTROPIC=True
on s958/t12833/t12835, then the multi-cusp 'not isotropic' finding is a bug, not a result."""
import sys, warnings; sys.path.insert(0,'/tmp/sweep'); warnings.filterwarnings("ignore")
from q12 import *
from fi_lib import get_rho, sym, blockdiag, wev
from cup import reduce_mod
from mcexact import analyse_exact, all_order3_chars, chi_on
from mccup import sl2form, mc_cup

for NM in sys.argv[1:] or ['s958','t12833']:
    M,G,gens,rels,mu,lam,rho=get_rho(NM)
    per=[(mu,lam)]
    chars=[p for p in all_order3_chars(gens,rels)
           if chi_on(mu,gens,p)==0 and chi_on(lam,gens,p)==0]
    print(f"\n=== {NM} (ONE cusp) === cusp-trivial chars={len(chars)}",flush=True)
    for ms in [(2,),(2,2)]:
        base={g:blockdiag([sym(rho[g],m) for m in ms]) for g in gens}
        d=sum(m+1 for m in ms); Fm=sl2form(ms)
        store={}
        for psi in chars:
            V={g:scal(powe(OMEGA,psi[i]),base[g]) for i,g in enumerate(gens)}
            A=analyse_exact(gens,rels,per,V,d)
            L=reduce_mod(A['R'],A['Bt'],len(A['Bt'][0]))
            cus=[(wev(mu,V,d),wev(lam,V,d))]
            Gm=[[mc_cup(p,q,cus,Fm,d) for q in L] for p in L]
            store[psi]=(A,L,all(is_zero(x) for r in Gm for x in r),A['Bt'])
        Bt=store[chars[0]][3]; rB=rank(Bt)
        def same(p,q):
            Lp,Lq=store[p][1],store[q][1]
            rp=rank(Lp+Bt)-rB; rq=rank(Lq+Bt)-rB
            return rp==rq==rank(Lp+Lq+Bt)-rB
        for psi in chars:
            if not any(psi): continue
            inv=tuple((-x)%3 for x in psi)
            A=store[psi][0]
            print(f"  Sym^{ms} psi={psi}: t0s={A['t0s']} t1={A['t1']} r1={A['r1']} "
                  f"I={A['t0']-A['r1']} | L==L*: {same(psi,inv)} | ISOTROPIC: {store[psi][2]}")
            break
