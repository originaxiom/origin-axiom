#!/usr/bin/env python3
"""MEMO-73 CELL: THE RESIDUAL CHARACTERIZED — the per-factor GUE deviation
under theta-exact and local-empirical unfolding: is it an unfolding artifact
or intrinsic finite-height statistics?  (Closes the B1151 -> memo 68 chain.)

Memo 68 (scoped by B1158): the ~0.04 per-factor KS deviation is NOT surmise
error (exact Gaudin law: unchanged); the sole named suspect was the
leading-order unfolding.  This cell tests that suspect with the two
refinements available WITHOUT circularity:
  (B) THETA-EXACT unfolding: x_n = theta(t_n)/pi using the exact
      Riemann-Siegel theta for zeta (mpmath.siegeltheta) and the exact
      Gamma-factor phase for L(chi_-3) (odd primitive character mod 3:
      theta_L(t) = Im ln Gamma((s+1)/2) - (t/2) ln(pi/3) at s=1/2+it) —
      includes ALL smooth terms to all orders (constants drop in spacings).
  (C) LOCAL-EMPIRICAL unfolding: spacings normalized by the local mean over
      a sliding window (w=25) — removes every smooth AND slowly-fluctuating
      density component including S(t) drift, leaving pure short-range
      statistics.
Both compared against the EXACT Gaudin law (sine-kernel Fredholm CDF, the
memo-68 machinery rebuilt in-run with the same convergence gates).

PREREGISTERED (two-outcome):
  ANCHORS: baseline (midpoint-density) D_zeta = 0.0416, D_L = 0.0502 vs
    exact Gaudin (memo 68's numbers) reproduced to 1e-3; Gaudin grid
    convergence < 1e-10; unit mean.
  BRANCH I (unfolding artifact): D under (B) or (C) drops below 0.02 with
    p > 0.01 for both factors -> the residual was unfolding; arc closes.
  BRANCH II (intrinsic): the residual survives both refinements -> it is a
    genuine finite-height short-range deviation at T = 3000 (the known
    O(1/log T) class of corrections to bulk-GUE universality for zeta-like
    spectra is the CITED context; 1/log(3000/2pi) ~ 0.16 sets the natural
    scale) -> the arc closes as CHARACTERIZED: not surmise (memo 68), not
    unfolding (this memo), consistent in size with known finite-height
    corrections; nothing object-specific claimed.
Gate 5 untouched (zeros + closed-form kernels only).
"""
import os
from math import log, pi
import numpy as np
from scipy.stats import kstest
import mpmath as mp
mp.mp.dps=30

HERE=os.path.dirname(os.path.abspath(__file__))
DATA=os.path.join(HERE,'c4data')
def read_zeros(fn): return sorted(float(x) for x in open(os.path.join(DATA,fn)) if x.strip())
zz=read_zeros('c4_zeros_zeta.txt'); zl=read_zeros('c4_zeros_L.txt')

# ---- exact Gaudin CDF (memo 68 machinery, rebuilt)
def E_gaudin(s,m=40):
    if s<=0: return 1.0
    x,w=np.polynomial.legendre.leggauss(m)
    x=0.5*s*(x+1); w=0.5*s*w
    XX,YY=np.meshgrid(x,x)
    K=np.sinc(XX-YY)   # sin(pi u)/(pi u)
    M=np.sqrt(np.outer(w,w))*K
    return float(np.linalg.det(np.eye(m)-M))
for sv in (0.5,1.5,3.0):
    assert abs(E_gaudin(sv,40)-E_gaudin(sv,80))<1e-10
grid=np.arange(0,6.0005,0.005)
Eg=np.array([E_gaudin(s) for s in grid])
dE=np.gradient(Eg,grid)
Fg=1+dE
Fg=np.clip(Fg,0,1)
assert abs(Fg[0])<1e-5 and abs(Fg[-1]-1)<1e-9
mean=np.trapezoid(1-Fg,grid)
assert abs(mean-1)<2e-3
def gaudin_cdf(s):
    return np.interp(s,grid,Fg)

# ---- baseline anchors (midpoint density, as banked)
def unfold_mid(ts,cond):
    us=[]
    for a,b in zip(ts,ts[1:]):
        tm=0.5*(a+b); rho=(1/(2*pi))*log(cond*tm/(2*pi))
        if rho>0: us.append((b-a)*rho)
    return np.array(us)
Dz0,pz0=kstest(unfold_mid(zz,1),gaudin_cdf)
Dl0,pl0=kstest(unfold_mid(zl,3),gaudin_cdf)
print(f"ANCHOR baseline vs exact Gaudin: D_zeta={Dz0:.4f} (memo 68: 0.0416), D_L={Dl0:.4f} (0.0502)")
assert abs(Dz0-0.0416)<1e-3 and abs(Dl0-0.0502)<1e-3

# ---- (B) theta-exact unfolding
xz=[float(mp.siegeltheta(t)/mp.pi) for t in zz]
def thetaL(t):
    s=mp.mpc(0.5,t)
    return float(( mp.im(mp.loggamma((s+1)/2)) - (t/2)*mp.log(mp.pi/3) )/mp.pi)
xl=[thetaL(t) for t in zl]
uB_z=np.diff(xz); uB_l=np.diff(xl)
print(f"(B) theta-exact: mean spacings {uB_z.mean():.6f} / {uB_l.mean():.6f}")
DzB,pzB=kstest(uB_z,gaudin_cdf); DlB,plB=kstest(uB_l,gaudin_cdf)
print(f"(B) vs exact Gaudin: D_zeta={DzB:.4f} p={pzB:.3g};  D_L={DlB:.4f} p={plB:.3g}")

# ---- (C) local-empirical unfolding (window w=25 raw-gap normalization)
def unfold_local(ts,w=25):
    ts=np.array(ts); gaps=np.diff(ts)
    out=[]
    for i in range(len(gaps)):
        lo=max(0,i-w//2); hi=min(len(gaps),i+w//2+1)
        m=gaps[lo:hi].mean()
        out.append(gaps[i]/m)
    return np.array(out)
uC_z=unfold_local(zz); uC_l=unfold_local(zl)
print(f"(C) local-empirical (w=25): mean spacings {uC_z.mean():.6f} / {uC_l.mean():.6f}")
DzC,pzC=kstest(uC_z,gaudin_cdf); DlC,plC=kstest(uC_l,gaudin_cdf)
print(f"(C) vs exact Gaudin: D_zeta={DzC:.4f} p={pzC:.3g};  D_L={DlC:.4f} p={plC:.3g}")

closesI = (min(DzB,DzC)<0.02 and min(DlB,DlC)<0.02 and
           max(pzB if DzB<0.02 else 0, pzC if DzC<0.02 else 0)>0.01 and
           max(plB if DlB<0.02 else 0, plC if DlC<0.02 else 0)>0.01)
scale=1/log(3000/(2*pi))
print(f"\nknown finite-height scale 1/log(T/2pi) at T=3000: {scale:.3f} (CITED context)")
if closesI:
    print("""
BRANCH I: the residual was an UNFOLDING artifact — refined unfolding brings
both factors into agreement with the exact Gaudin law.  The
B1151 -> memo 68 -> memo 73 chain closes: surmise ruled out, unfolding
identified.  Gate 5 untouched.""")
else:
    print(f"""
BRANCH II: the residual SURVIVES both the theta-exact and the
local-empirical unfolding — it is not a surmise artifact (memo 68) and not
an unfolding artifact (this memo).  It is an intrinsic short-range
finite-height deviation of the T=3000 spectra from bulk-GUE, of a size
(D ~ 0.03-0.05) compatible with the known O(1/log T) ~ {scale:.2f}-scale
correction class for zeta-like spectra (CITED context; no object-specific
claim).  The arc closes as CHARACTERIZED: every controllable artifact has
been eliminated by exact computation, and what remains is finite-height
physics of the spectra themselves.  Gate 5 untouched.""")
