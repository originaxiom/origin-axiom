"""Recognise a MULTI-CUSPED manifold's normalised geometric holonomy over Q(zeta_12).

Same normalisation as recog12 (conjugate so the first cusp's meridian is upper-triangular with
1 in the corner), but returns EVERY cusp's (meridian, longitude) rather than only the first.
Accepts a Manifold object as well as a name, so covers -- which have no census name -- work.
"""
import snappy, warnings; warnings.filterwarnings("ignore")
from mpmath import mp, mpf, mpc
from fractions import Fraction as F
from recog12 import clean, tompc, mm, minv, in_Qs3
mp.dps=60

def normalised_mc(M):
    if isinstance(M,str): M=snappy.ManifoldHP(M)
    elif not isinstance(M,snappy.ManifoldHP): M=snappy.ManifoldHP(M)
    G=M.fundamental_group()
    per=list(G.peripheral_curves())
    rho={g:[[tompc(G.SL2C(g)[i,j]) for j in range(2)] for i in range(2)] for g in G.generators()}
    mu0=per[0][0]
    Mu=[[tompc(G.SL2C(mu0)[i,j]) for j in range(2)] for i in range(2)]
    tr=Mu[0][0]+Mu[1][1]; sgn=1 if tr.real>0 else -1
    N=[[Mu[0][0]-sgn,Mu[0][1]],[Mu[1][0],Mu[1][1]-sgn]]
    fp=-N[1][1]/N[1][0] if abs(N[1][0])>mpf(10)**-30 else (-N[0][1]/N[0][0] if abs(N[0][0])>mpf(10)**-30 else None)
    C=[[mpc(1),mpc(0)],[mpc(0),mpc(1)]] if fp is None else [[mpc(0),mpc(1)],[mpc(1),-fp]]
    Ci=minv(C); Mn=mm(mm(C,Mu),Ci)
    t=Mn[0][1] if abs(Mn[0][1])>mpf(10)**-30 else mpc(1)
    D=[[mpc(1),mpc(0)],[mpc(0),t]]; Di=minv(D)
    rec={g:mm(mm(Di,mm(mm(C,rho[g]),Ci)),D) for g in G.generators()}
    return M,G,list(G.generators()),list(G.relators()),per,rec

def entry(z):
    a=in_Qs3(z.real); b=in_Qs3(z.imag)
    return None if (a is None or b is None) else (a[0],a[1],b[0],b[1])

def exact_rho(M):
    """the recognised rep over Q(zeta_12), or None if PSLQ does not recognise every entry"""
    M,G,gens,rels,per,rec=normalised_mc(M)
    rho={}
    for g in gens:
        E=[[entry(rec[g][i][j]) for j in range(2)] for i in range(2)]
        if any(x is None for r in E for x in r): return None
        rho[g]=E
    return M,G,gens,rels,per,rho
