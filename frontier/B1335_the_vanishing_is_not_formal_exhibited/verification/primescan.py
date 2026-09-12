"""Is the m010 non-zero index a characteristic-13 accident, or robust across primes?

For each prime p: enumerate honest reps pi_1(m010) -> SL2(F_p), keep those with UNIPOTENT
commuting peripheral holonomy (the domain's cusp condition) and IRREDUCIBLE image (reductive),
twist by cusp-trivial characters, and report every in-domain sector with I != 0.

A pattern across many primes is evidence of a characteristic-0 phenomenon.
A hit only at p = 13 is a mod-p artifact.
"""
import sys, warnings, itertools, os; sys.path.insert(0,'/tmp/sweep'); warnings.filterwarnings("ignore")
import snappy
from collections import Counter
import index_lib as L
from mc_lib import check, dual_rho
from broad import chars_of_order, sym_p

def irreducible(rho,gens,p):
    """no common eigenvector: the algebra generated acts irreducibly on F_p^2"""
    mats=[rho[g] for g in gens]
    for lam in range(p):
        # common eigenvectors for eigenvalue lam?
        rows=[]
        for A in mats:
            rows.append([(A[0][0]-lam)%p,A[0][1]%p]); rows.append([A[1][0]%p,(A[1][1]-lam)%p])
        if L.rank(rows,p)<2: return False
    return True

NAME=os.environ.get('MF','m010')
M=snappy.Manifold(NAME); G=M.fundamental_group()
gens=list(G.generators()); rels=list(G.relators()); per=list(G.peripheral_curves())
mu,lam=per[0]
print(f"{NAME}: gens={gens} rels={rels} chiral={not M.symmetry_group().is_amphicheiral()}",flush=True)
for p in [int(x) for x in os.environ.get('PS','5,7,11,13,17,19').split(',')]:
    S=[[[a,b],[c,d]] for a in range(p) for b in range(p) for c in range(p) for d in range(p) if (a*d-b*c)%p==1]
    ch=chars_of_order(gens,rels,per,p)
    reps=[]
    for tup in itertools.product(S,repeat=len(gens)):
        rho=dict(zip(gens,tup))
        if all(L.word_eval(r,rho,p,2)==L.eye(2) for r in rels): reps.append(rho)
    ok=[]
    for rho in reps:
        Mu=L.word_eval(mu,rho,p,2); La=L.word_eval(lam,rho,p,2)
        trm=(Mu[0][0]+Mu[1][1])%p; trl=(La[0][0]+La[1][1])%p
        if trm!=2 or trl!=2: continue                # unipotent peripherals
        if Mu==L.eye(2) and La==L.eye(2): continue   # trivial peripheral: degenerate
        if not irreducible(rho,gens,p): continue     # reductive
        ok.append(rho)
    hits=[]; tested=0
    for rho in ok:
        for m in (1,2,3,4):
            base={g:sym_p(rho[g],m,p) for g in gens}; d=m+1
            for c in ch:
                V={g:[[(c[i]*base[g][x][y])%p for y in range(d)] for x in range(d)] for i,g in enumerate(gens)}
                if any(L.word_eval(r,V,p,d)!=L.eye(d) for r in rels): continue
                A,B,ids=check(gens,rels,per,V,p,d)
                if not all(ids.values()): continue
                inD=(A['a0']==B['a0']) and (A['t0']==B['t0'])
                if not inD: continue
                tested+=1
                if A['I_exact']!=0: hits.append((m,c,A['t0'],A['r1'],A['I_exact']))
    print(f"  p={p:3d}: reps {len(reps):5d} | unipotent+irreducible {len(ok):4d} | cusp-trivial chars {len(ch):3d}"
          f" | IN-DOMAIN sectors {tested:5d} | NON-ZERO {len(hits)}",flush=True)
    for h in hits[:3]: print(f"        Sym^{h[0]} chi={h[1]} t0={h[2]} r1={h[3]} I={h[4]}")
