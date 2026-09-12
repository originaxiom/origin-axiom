"""What are the FIBRES of  psi |-> L_psi ?

On s958/t12833/t12835 the cusp-trivial character group is Z/3 -- only ONE inverse pair, so
"L_psi = L_{psi^-1}" is a single equation and cannot be told apart from other explanations.
d8_4 and d8_6 carry (Z/3)^2: NINE cusp-trivial characters, FOUR inverse pairs. There the
structure is visible:

  * if L_psi = L_{psi^-1} on all four pairs, the theorem holds in a genuinely richer setting;
  * if the four pairs give FOUR DISTINCT subspaces, the map factors through inversion and
    NOTHING MORE -- L_psi knows psi exactly up to inversion. That is the sharpest possible
    form of the statement, and it says the only collapse is precisely the one I = 0 needs.

Cusp-trivial means trivial on every peripheral curve of every cusp, so the cusp matrices are
identical across the whole family and the subspaces are directly comparable (asserted, not assumed).
"""
import sys, warnings, json, os; sys.path.insert(0,'/tmp/sweep'); warnings.filterwarnings("ignore")
from fractions import Fraction as Fr
from q12 import *
from q12 import _dot
from fi_lib import sym, blockdiag, fox, invariants, wev
from cup import reduce_mod
from mcexact import all_order3_chars, chi_on

def restrict_mc(gens,rels,per,rho,d):
    """restricted cocycles R and the boundary coboundaries Bt, on several cusps"""
    g=len(gens); J=[]
    for r in rels:
        bl=[fox(r,x,rho,d) for x in gens]
        for a in range(d): J.append([bl[j][a][b] for j in range(g) for b in range(d)])
    Zs=nullspace(J,g*d)
    cusps=[]
    for (mu,lam) in per:
        cusps.append((mu,lam,wev(mu,rho,d),wev(lam,rho,d)))
    FX={}
    for mu,lam,A,B in cusps:
        for w in (mu,lam):
            if w not in FX: FX[w]=[fox(w,gg,rho,d) for gg in gens]
    c=len(cusps); R=[]
    for v in Zs:
        z=[v[j*d:(j+1)*d] for j in range(g)]; row=[]
        for mu,lam,A,B in cusps:
            for w in (mu,lam):
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
    for i,(mu,lam,A,B) in enumerate(cusps):
        Am=msub(A,eye(d)); Bm=msub(B,eye(d))
        for k in range(d):
            row=[Z]*(2*c*d)
            for r_ in range(d):
                row[2*i*d+r_]=Am[r_][k]; row[2*i*d+d+r_]=Bm[r_][k]
            Bt.append(row)
    A0=[(x[2],x[3]) for x in cusps]
    return R,Bt,A0,invariants([m for x in cusps for m in (x[2],x[3])],d)

db=json.load(open('/tmp/sweep/covcache.json'))
GERMS=[tuple(int(c) for c in s) for s in os.environ.get('G','2,22').split(',')]
for tag in sys.argv[1:]:
    v=db[tag]; gens=v['gens']; rels=v['rels']; per=[tuple(x) for x in v['per']]
    rho={g:[[tuple(Fr(e) for e in v['rho'][g][i][j]) for j in range(2)] for i in range(2)] for g in gens}
    chars=[p for p in all_order3_chars(gens,rels)
           if all(chi_on(mu,gens,p)==0 and chi_on(lam,gens,p)==0 for mu,lam in per)]
    print(f"\n=== {tag} === cusps={v['cusps']} lift={'-I' if v['proj'] else '+I'} "
          f"cusp-trivial characters: {len(chars)}", flush=True)
    for ms in GERMS:
        if v['proj'] and any(m%2 for m in ms): print(f"  germ {ms}: odd under -I lift, skipped"); continue
        base={g:blockdiag([sym(rho[g],m) for m in ms]) for g in gens}; d=sum(m+1 for m in ms)
        Ls=[]; cusp0=None
        for psi in chars:
            V={g:scal(powe(OMEGA,psi[i]),base[g]) for i,g in enumerate(gens)}
            R,Bt,A0,t0=restrict_mc(gens,rels,per,V,d)
            if cusp0 is None: cusp0=A0
            assert A0==cusp0, "cusp matrices differ across cusp-trivial characters"
            Ls.append((psi,reduce_mod(R,Bt,len(Bt[0])),t0))
        Bt0=Bt; rB=rank(Bt0)
        def same(i,j):
            ri=rank(Ls[i][1]+Bt0)-rB; rj=rank(Ls[j][1]+Bt0)-rB
            return ri==rj==rank(Ls[i][1]+Ls[j][1]+Bt0)-rB
        n=len(Ls)
        # partition the characters by which give the same subspace
        parts=[]
        for i in range(n):
            for p_ in parts:
                if same(i,p_[0]): p_.append(i); break
            else: parts.append([i])
        print(f"  Sym^{ms}: t0={Ls[0][2]} dim L = {[len(L) for _,L,_ in Ls]}")
        print(f"     FIBRES of psi -> L_psi : {len(parts)} classes")
        for p_ in parts:
            ps=[Ls[i][0] for i in p_]
            inv_closed = all(any(all((a+b)%3==0 for a,b in zip(x,y)) for y in ps) for x in ps)
            print(f"       {{{', '.join(str(x) for x in ps)}}}"
                  f"   size {len(ps)}  inverse-closed: {inv_closed}")
