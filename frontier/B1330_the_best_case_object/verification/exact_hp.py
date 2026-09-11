"""High-precision recognition of the geometric holonomy in Q(omega), via ManifoldHP."""
import snappy, warnings, sys; warnings.filterwarnings("ignore")
from mpmath import mp, mpf, mpc, sqrt as msqrt, nstr
from fractions import Fraction as F
mp.dps = 55
OM = mpc(mpf(-1)/2, msqrt(mpf(3))/2)

def _clean(t):
    # SnapPyHP prints exponents as " E-64" / " e-64" -- mpmath cannot parse the space
    return str(t).replace(" E", "E").replace(" e", "e").replace("E ", "E").replace("e ", "e")

def tompc(x):
    return mpc(mpf(_clean(x.real())), mpf(_clean(x.imag())))

def rat(x, maxden):
    """best rational approx of an mpf, via continued fractions"""
    from fractions import Fraction
    return Fraction(str(nstr(x, mp.dps-5))).limit_denominator(maxden)

def recognise(z, maxden, tol):
    b = z.imag / OM.imag
    a = z.real - b*OM.real
    fa, fb = rat(a, maxden), rat(b, maxden)
    chk = mpc(mpf(fa.numerator)/fa.denominator, 0) + mpc(mpf(fb.numerator)/fb.denominator,0)*OM
    return (fa, fb) if abs(chk - z) < tol else None

def mats(nm):
    M = snappy.ManifoldHP(nm); G = M.fundamental_group()
    mu, lam = G.peripheral_curves()[0]
    out = {g: [[tompc(G.SL2C(g)[i,j]) for j in range(2)] for i in range(2)] for g in G.generators()}
    Mu = [[tompc(G.SL2C(mu)[i,j]) for j in range(2)] for i in range(2)]
    return M, G, list(G.generators()), list(G.relators()), mu, lam, out, Mu

def mm(A,B): return [[A[i][0]*B[0][j]+A[i][1]*B[1][j] for j in range(2)] for i in range(2)]
def minv(A):
    d=A[0][0]*A[1][1]-A[0][1]*A[1][0]
    return [[A[1][1]/d, -A[0][1]/d], [-A[1][0]/d, A[0][0]/d]]

def normalise(nm, maxden, tol):
    M,G,gens,rels,mu,lam,rho,Mu = mats(nm)
    tr = Mu[0][0]+Mu[1][1]
    sgn = 1 if tr.real > 0 else -1
    N = [[Mu[0][0]-sgn, Mu[0][1]],[Mu[1][0], Mu[1][1]-sgn]]
    if abs(N[1][0]) > mpf(10)**(-30): fp = -N[1][1]/N[1][0]
    elif abs(N[0][0]) > mpf(10)**(-30): fp = -N[0][1]/N[0][0]
    else: fp = None
    C = [[mpc(1),mpc(0)],[mpc(0),mpc(1)]] if fp is None else [[mpc(0),mpc(1)],[mpc(1),-fp]]
    Ci = minv(C)
    Mn = mm(mm(C,Mu),Ci)
    t = Mn[0][1] if abs(Mn[0][1])>mpf(10)**(-30) else mpc(1)
    D=[[mpc(1),mpc(0)],[mpc(0),t]]; Di=minv(D)
    rec={}
    for g in gens:
        B = mm(mm(Di,mm(mm(C,rho[g]),Ci)),D)
        r=[[recognise(B[i][j],maxden,tol) for j in range(2)] for i in range(2)]
        if any(x is None for row in r for x in row):
            return None, [[nstr(B[i][j],20) for j in range(2)] for i in range(2)]
        rec[g]=r
    return (M,G,gens,rels,mu,lam,rec), None

for nm in sys.argv[1:] or ['t12833','t12835','v2873']:
    for maxden in [400, 5000, 50000]:
        res, bad = normalise(nm, maxden, mpf(10)**(-25))
        if res: 
            print(f"{nm:9s} RECOGNISED over Q(omega) at maxden={maxden}")
            g0=res[2][0]; print(f"          rho({g0}) = {res[6][g0]}")
            break
    else:
        print(f"{nm:9s} not recognised (last residue sample: {bad[0][0]})")
