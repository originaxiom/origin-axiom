"""Recognise the normalised geometric holonomy in Q(sqrt3, i) = Q(zeta_12) via PSLQ."""
import snappy, warnings; warnings.filterwarnings("ignore")
from mpmath import mp, mpf, mpc, pslq, sqrt as msqrt, nstr
from fractions import Fraction as F
mp.dps=50
S3=msqrt(mpf(3))
def clean(t): return str(t).replace(" E","E").replace(" e","e")
def tompc(x): return mpc(mpf(clean(x.real())), mpf(clean(x.imag())))
def mm(A,B): return [[A[i][0]*B[0][j]+A[i][1]*B[1][j] for j in range(2)] for i in range(2)]
def minv(A):
    d=A[0][0]*A[1][1]-A[0][1]*A[1][0]
    return [[A[1][1]/d,-A[0][1]/d],[-A[1][0]/d,A[0][0]/d]]

def in_Qs3(x, maxcoeff=10**6, tol=mpf(10)**-30):
    """x = p + q*sqrt3 with p,q rational -> (p,q) or None"""
    if abs(x) < tol: return (F(0),F(0))
    r = pslq([x, mpf(1), S3], maxcoeff=maxcoeff, maxsteps=2000, tol=mpf(10)**-35)
    if r is None or r[0]==0: return None
    p = F(-r[1], r[0]); q = F(-r[2], r[0])
    chk = mpf(p.numerator)/p.denominator + (mpf(q.numerator)/q.denominator)*S3
    return (p,q) if abs(chk-x)<tol else None

def normalised(nm):
    M=snappy.ManifoldHP(nm); G=M.fundamental_group()
    mu,lam=G.peripheral_curves()[0]
    rho={g:[[tompc(G.SL2C(g)[i,j]) for j in range(2)] for i in range(2)] for g in G.generators()}
    Mu=[[tompc(G.SL2C(mu)[i,j]) for j in range(2)] for i in range(2)]
    tr=Mu[0][0]+Mu[1][1]; sgn=1 if tr.real>0 else -1
    N=[[Mu[0][0]-sgn,Mu[0][1]],[Mu[1][0],Mu[1][1]-sgn]]
    fp=-N[1][1]/N[1][0] if abs(N[1][0])>mpf(10)**-30 else (-N[0][1]/N[0][0] if abs(N[0][0])>mpf(10)**-30 else None)
    C=[[mpc(1),mpc(0)],[mpc(0),mpc(1)]] if fp is None else [[mpc(0),mpc(1)],[mpc(1),-fp]]
    Ci=minv(C); Mn=mm(mm(C,Mu),Ci)
    t=Mn[0][1] if abs(Mn[0][1])>mpf(10)**-30 else mpc(1)
    D=[[mpc(1),mpc(0)],[mpc(0),t]]; Di=minv(D)
    return M,G,list(G.generators()),list(G.relators()),mu,lam,{g:mm(mm(Di,mm(mm(C,rho[g]),Ci)),D) for g in G.generators()}

if __name__=="__main__":
    import sys
    for nm in sys.argv[1:] or ['m004','s958','t12833','t12835','v2873']:
        M,G,gens,rels,mu,lam,rec=normalised(nm)
        ok=True; bad=None; out={}
        for g in gens:
            E=[[None]*2,[None]*2]
            for i in range(2):
                for j in range(2):
                    z=rec[g][i][j]
                    a=in_Qs3(z.real); b=in_Qs3(z.imag)
                    if a is None or b is None:
                        ok=False; bad=(g,i,j,nstr(z,24)); break
                    E[i][j]=(a,b)      # (p+q sqrt3) + i(r+s sqrt3)
                if not ok: break
            if not ok: break
            out[g]=E
        print(f"{nm:9s} in Q(sqrt3, i): {ok}" + ("" if ok else f"   failed at {bad}"))
        if ok:
            g0=gens[0]; print(f"          rho({g0})[0][0] = ({out[g0][0][0][0][0]} + {out[g0][0][0][0][1]}*sqrt3) + i*({out[g0][0][0][1][0]} + {out[g0][0][0][1][1]}*sqrt3)")
