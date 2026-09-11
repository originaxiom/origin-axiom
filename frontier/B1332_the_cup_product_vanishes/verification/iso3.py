"""HOW special is the form?  Isotropy of L_V is LINEAR in F, so
   {F pi_1(T)-invariant : L_V isotropic for F}
is a subspace.  Measure its dimension and compare with the SL2-invariant forms.

If it were all of the pi_1(T)-invariant forms, the mechanism would be pure cusp-locality.
If it is exactly the SL2-invariant ones, the mechanism needs the GLOBAL self-duality of Sym^m too.
"""
import sys, warnings; sys.path.insert(0,'/tmp/sweep'); warnings.filterwarnings("ignore")
from iso import restrict, sl2form
from cup import *
from q12 import *
from fi_lib import get_rho, sym, blockdiag, order3_chars

NM=sys.argv[1]; MS=tuple(int(c) for c in sys.argv[2])
M,G,gens,rels,mu,lam,rho=get_rho(NM)
base={g:blockdiag([sym(rho[g],m) for m in MS]) for g in gens}
d=sum(m+1 for m in MS)
g1=[[ONE,ONE],[Z,ONE]]; g2=[[ONE,Z],[ONE,ONE]]
SL2F=invariant_forms([blockdiag([sym(g1,m) for m in MS]),
                      blockdiag([sym(g2,m) for m in MS])], d)
print(f"{NM} germ Sym^{MS} d={d}   SL2-invariant forms on W: {len(SL2F)}", flush=True)
for psi in [tuple([0]*len(gens))]+list(order3_chars(gens,rels,mu,lam)):
    V={g:scal(powe(OMEGA,psi[i]),base[g]) for i,g in enumerate(gens)}
    R,Bt,A,B,t0=restrict(gens,rels,mu,lam,V,d)
    LV=reduce_mod(R,Bt,2*d); r1=len(LV)
    Fs=invariant_forms([A,B],d)                 # pi_1(T)-invariant forms
    # isotropy is linear in F: build rows (p,q) x (form basis)
    rows=[]
    for p in range(r1):
        for q in range(r1):
            rows.append([cup(LV[p],LV[q],A,B,Fx,d) for Fx in Fs])
    ker = nullspace(rows,len(Fs)) if rows else [[ONE if i==j else Z for i in range(len(Fs))] for j in range(len(Fs))]
    # is every SL2-invariant form in that kernel?
    sl2_iso = all(all(is_zero(cup(LV[p],LV[q],A,B,Fx,d)) for p in range(r1) for q in range(r1))
                  for Fx in SL2F)
    print(f"  psi={psi}: t0={t0} dim L_V={r1}"
          f" | pi_1(T)-inv forms: {len(Fs)}"
          f" | of these, L_V isotropic for a subspace of dim {len(ker)}"
          f" | SL2-inv forms ({len(SL2F)}) all give isotropy: {sl2_iso}", flush=True)
