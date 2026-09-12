"""Recognition that does not give up on the first normalisation.

All traces of these covers -- traces of squares included -- lie in Q(sqrt-3), so the arithmetic
is fine; what fails is the CONJUGATE chosen. The normalisation conjugates by a matrix built from
one cusp's meridian fixed point and then rescales, which can push individual entries out of
Q(zeta_12) even when every trace stays in Q(sqrt-3). So: try each cusp as the anchor, and each
generator's fixed point as a fallback, and keep the first conjugate whose entries are recognised.
"""
import snappy, warnings; warnings.filterwarnings("ignore")
from mpmath import mp, mpf, mpc
from fractions import Fraction as F
from recog12 import clean, tompc, mm, minv, in_Qs3
mp.dps=60

def _conj_from(Mu):
    tr=Mu[0][0]+Mu[1][1]; sgn=1 if tr.real>0 else -1
    N=[[Mu[0][0]-sgn,Mu[0][1]],[Mu[1][0],Mu[1][1]-sgn]]
    if abs(N[1][0])>mpf(10)**-30:  fp=-N[1][1]/N[1][0]
    elif abs(N[0][0])>mpf(10)**-30: fp=-N[0][1]/N[0][0]
    else: fp=None
    C=[[mpc(1),mpc(0)],[mpc(0),mpc(1)]] if fp is None else [[mpc(0),mpc(1)],[mpc(1),-fp]]
    return C

def entry(z):
    a=in_Qs3(z.real); b=in_Qs3(z.imag)
    return None if (a is None or b is None) else (a[0],a[1],b[0],b[1])

def exact_rho2(M):
    """try every anchor; return the first conjugate recognised over Q(zeta_12)"""
    if not isinstance(M,snappy.ManifoldHP): M=snappy.ManifoldHP(M)
    G=M.fundamental_group(); gens=list(G.generators()); rels=list(G.relators())
    per=list(G.peripheral_curves())
    rho={g:[[tompc(G.SL2C(g)[i,j]) for j in range(2)] for i in range(2)] for g in gens}
    anchors=[w for (mu,lam) in per for w in (mu,)] + gens + [w for (mu,lam) in per for w in (lam,)]
    for a_i,w in enumerate(anchors):
        Mu=[[tompc(G.SL2C(w)[i,j]) for j in range(2)] for i in range(2)]
        C=_conj_from(Mu); Ci=minv(C); Mn=mm(mm(C,Mu),Ci)
        for scale in (Mn[0][1], Mn[1][0], mpc(1)):
            if abs(scale)<mpf(10)**-30: continue
            D=[[mpc(1),mpc(0)],[mpc(0),scale]]; Di=minv(D)
            rec={g:mm(mm(Di,mm(mm(C,rho[g]),Ci)),D) for g in gens}
            out={}
            ok=True
            for g in gens:
                E=[[entry(rec[g][i][j]) for j in range(2)] for i in range(2)]
                if any(x is None for r in E for x in r): ok=False; break
                out[g]=E
            if ok: return M,G,gens,rels,per,out,f"anchor#{a_i}:{w}"
    return None
