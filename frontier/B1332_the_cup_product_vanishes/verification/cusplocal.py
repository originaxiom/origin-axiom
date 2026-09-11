"""IS L_V DETERMINED BY THE CUSP DATA ALONE?

B1331 named cusp-locality as the surviving candidate mechanism. Here is a sharp, decidable form.

Because psi is CUSP-TRIVIAL, the cusp matrices (A,B) are IDENTICAL for every cusp-trivial psi --
V and V* and the untwisted W all restrict to the same pair. So L_V for different psi are subspaces
of ONE space H^1(T;W), directly comparable with no identification needed.

If L_V were determined by (A,B) alone, then L_V = L_{V*} would be immediate -- and that IS the
theorem (B1332 section 1). So:

    TEST: on a fixed manifold and germ, is L_V the SAME SUBSPACE for every cusp-trivial psi?

A yes is strong evidence for the mechanism. A NO kills it outright, and that is worth as much.
"""
import sys, warnings; sys.path.insert(0,'/tmp/sweep'); warnings.filterwarnings("ignore")
from collections import Counter
from q12 import *
from fi_lib import get_rho, sym, blockdiag, wev
from iso import restrict
from cup import reduce_mod
from mcexact import all_order3_chars, chi_on

GERMS=[(2,),(4,),(2,2),(2,4)]
for NM in sys.argv[1:] or ['s958','t12833']:
    M,G,gens,rels,mu,lam,rho=get_rho(NM)
    chars=[p for p in all_order3_chars(gens,rels)
           if chi_on(mu,gens,p)==0 and chi_on(lam,gens,p)==0]
    print(f"\n=== {NM} === cusp-trivial order-3 characters: {len(chars)}", flush=True)
    for ms in GERMS:
        base={g:blockdiag([sym(rho[g],m) for m in ms]) for g in gens}
        d=sum(m+1 for m in ms)
        Ls=[]; A0=B0=None
        for psi in chars:
            V={g:scal(powe(OMEGA,psi[i]),base[g]) for i,g in enumerate(gens)}
            R,Bt,A,B,t0=restrict(gens,rels,mu,lam,V,d)
            if A0 is None: A0,B0=A,B
            # the cusp data must be identical across cusp-trivial psi -- checked, not assumed
            assert A==A0 and B==B0, "cusp matrices differ: psi is not cusp-trivial"
            Ls.append((psi,reduce_mod(R,Bt,2*d),Bt,t0))
        rB=rank(Ls[0][2]); Bt=Ls[0][2]
        def same(i,j):
            ri=rank(Ls[i][1]+Bt)-rB; rj=rank(Ls[j][1]+Bt)-rB
            rij=rank(Ls[i][1]+Ls[j][1]+Bt)-rB
            return ri==rj==rij
        print(f"  Sym^{ms}: t0={Ls[0][3]}  dim L_V = {[len(L) for _,L,_,_ in Ls]}")
        for i in range(len(Ls)):
            for j in range(i+1,len(Ls)):
                pi,pj=Ls[i][0],Ls[j][0]
                inv = all((a+b)%3==0 for a,b in zip(pi,pj))   # psi_j = psi_i^{-1} ?
                print(f"     psi{pi} vs psi{pj}: {'SAME' if same(i,j) else 'different'}"
                      f"{'   <- these are psi and psi^-1 (V and V*)' if inv and any(pi) else ''}")
