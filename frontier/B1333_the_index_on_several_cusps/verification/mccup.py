"""Is L_V isotropic when there are SEVERAL cusps?

One cusp (B1332): L_V is Lagrangian, and isotropy IS the mechanism for I = 0.
Several cusps: the pairing on H^1(dM;W) is the SUM of the per-torus pairings. If L_V were
isotropic then L_V <= L_V^perp = L_{V*}, and equal dimensions would force L_V = L_{V*}.

So: if L_psi != L_{psi^-1} while dim L_psi = dim L_{psi^-1}, then L_V is NOT isotropic --
and the index would have to vanish for a reason OTHER than isotropy.

Both halves are computed here directly, and a one-cusped control must still come out isotropic.
"""
import sys, warnings, json, os; sys.path.insert(0,'/tmp/sweep'); warnings.filterwarnings("ignore")
from fractions import Fraction as Fr
from q12 import *
from q12 import _dot
from fi_lib import sym, blockdiag, invariants
from cup import reduce_mod, invariant_forms, cup
from mcexact import analyse_exact, all_order3_chars, chi_on

def sl2form(ms):
    g1=[[ONE,ONE],[Z,ONE]]; g2=[[ONE,Z],[ONE,ONE]]
    return blockdiag([invariant_forms([sym(g1,m),sym(g2,m)],m+1)[0] for m in ms])

def mc_cup(x,y,cusps,Fm,d):
    """sum over cusps of the per-torus cup product"""
    tot=Z
    for i,(A,B) in enumerate(cusps):
        xi=x[2*i*d:2*(i+1)*d]; yi=y[2*i*d:2*(i+1)*d]
        tot=add(tot,cup(xi,yi,A,B,Fm,d))
    return tot

if __name__=="__main__":
    db=json.load(open('/tmp/sweep/covcache.json'))
    GERMS=[tuple(int(c) for c in s) for s in os.environ.get('G','2').split(',')]
    for tag in sys.argv[1:]:
        v=db[tag]; gens=v['gens']; rels=v['rels']; per=[tuple(x) for x in v['per']]
        rho={g:[[tuple(Fr(e) for e in v['rho'][g][i][j]) for j in range(2)] for i in range(2)] for g in gens}
        chars=[p for p in all_order3_chars(gens,rels)
               if all(chi_on(mu,gens,p)==0 and chi_on(lam,gens,p)==0 for mu,lam in per)]
        print(f"\n=== {tag} === cusps={v['cusps']} cusp-trivial chars={len(chars)}", flush=True)
        for ms in GERMS:
            if v['proj'] and any(m%2 for m in ms): continue
            base={g:blockdiag([sym(rho[g],m) for m in ms]) for g in gens}
            d=sum(m+1 for m in ms); Fm=sl2form(ms)
            res={}
            for psi in chars:
                V={g:scal(powe(OMEGA,psi[i]),base[g]) for i,g in enumerate(gens)}
                A=analyse_exact(gens,rels,per,V,d)
                L=reduce_mod(A['R'],A['Bt'],len(A['Bt'][0]))
                cus=[]
                from fi_lib import wev
                for (mu,lam) in per: cus.append((wev(mu,V,d),wev(lam,V,d)))
                G=[[mc_cup(p,q,cus,Fm,d) for q in L] for p in L]
                iso=all(is_zero(x) for row in G for x in row)
                res[psi]=(A,L,G,iso,cus,A['Bt'])
            first=chars[0]
            Bt=res[first][5]; rB=rank(Bt)
            def same(p,q):
                Lp,Lq=res[p][1],res[q][1]
                rp=rank(Lp+Bt)-rB; rq=rank(Lq+Bt)-rB
                return rp==rq==rank(Lp+Lq+Bt)-rB
            print(f"  Sym^{ms}:")
            seen=set()
            for psi in chars:
                if not any(psi): continue
                inv=tuple((-x)%3 for x in psi)
                key=tuple(sorted([psi,inv]))
                if key in seen: continue
                seen.add(key)
                A=res[psi][0]
                print(f"    psi={psi}  t0s={A['t0s']} t1={A['t1']} r1={A['r1']} I={A['t0']-A['r1']}"
                      f" | L_psi==L_psi^-1: {same(psi,inv)} | L_psi ISOTROPIC: {res[psi][3]}")
