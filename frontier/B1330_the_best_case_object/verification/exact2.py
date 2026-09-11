import snappy, warnings, cmath; warnings.filterwarnings("ignore")
from fractions import Fraction as F
import numpy as np
W = complex(-0.5, (3**0.5)/2)

def recognise(z, maxden=400, tol=1e-6):
    b = z.imag / W.imag; a = z.real - b*W.real
    fa, fb = F(a).limit_denominator(maxden), F(b).limit_denominator(maxden)
    if abs(complex(float(fa)+float(fb)*W) - z) < tol: return (fa,fb)
    return None

def normalise(nm):
    M=snappy.Manifold(nm); G=M.fundamental_group()
    mu = G.peripheral_curves()[0][0]
    Mu = np.array([[complex(x) for x in row] for row in G.SL2C(mu)])
    # conjugate so the meridian becomes [[1,*],[0,1]]: put its fixed point at infinity
    tr = Mu[0,0]+Mu[1,1]
    if abs(tr-2)>1e-6 and abs(tr+2)>1e-6: return nm,None,f"meridian not parabolic (tr={tr:.4f})"
    N = Mu - np.sign(tr.real)*np.eye(2)
    # fixed point: kernel of N
    if abs(N[1,0])>1e-12: fp = -N[1,1]/N[1,0]
    elif abs(N[0,0])>1e-12: fp = -N[0,1]/N[0,0]
    else: fp = complex('inf')
    C = np.eye(2,dtype=complex) if fp==complex('inf') else np.array([[1,0],[-1/ (fp if abs(fp)>1e-12 else 1e-12),1]],dtype=complex)
    if fp!=complex('inf'):
        C = np.array([[0,1],[1,-fp]],dtype=complex)   # sends fp -> infinity
    Ci = np.linalg.inv(C)
    out={}
    for g in G.generators():
        A = np.array([[complex(x) for x in row] for row in G.SL2C(g)])
        B = C@A@Ci
        # rescale so the meridian's translation is 1
        out[g]=B
    Mn = C@Mu@Ci
    t = Mn[0,1] if abs(Mn[0,1])>1e-12 else 1.0
    D = np.array([[1,0],[0,t]],dtype=complex); Di=np.linalg.inv(D)
    rec={}
    for g,B in out.items():
        B2 = Di@B@D
        r=[[recognise(B2[i,j]) for j in range(2)] for i in range(2)]
        if any(x is None for row in r for x in row): return nm,None,f"entry not in Q(omega): {B2[0,0]:.6f},{B2[0,1]:.6f},{B2[1,0]:.6f},{B2[1,1]:.6f}"
        rec[g]=r
    return nm,rec,"OK"

for nm in ['m004','s958','t12833','t12835','v2873']:
    n,rec,msg = normalise(nm)
    print(f"{n:9s} {msg}")
    if rec:
        for g,r in list(rec.items())[:2]:
            print(f"          rho({g}) = {r}")
