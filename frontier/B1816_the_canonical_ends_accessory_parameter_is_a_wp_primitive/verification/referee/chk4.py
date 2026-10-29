import sys, pathlib as _p; sys.path.insert(0, str(_p.Path(__file__).resolve().parent))
from chk1 import *
import numpy as np
# (a) lower region of F: x in [0,1/2], y in [sqrt(1-x^2),1]; density h = Im dC/dtaubar via 4 solves, h_step 1e-3
def hdens(t):
    c0,_=warm(t); h=1e-3
    cx=[solve(t+s*h,c0) for s in (-1,1)]; cy=[solve(t+1j*s*h,c0) for s in (-1,1)]
    dCx=2*(cx[1]-cx[0])/(2*h); dCy=2*(cy[1]-cy[0])/(2*h)
    return (0.5*(dCx+1j*dCy)).imag, c0
gx,gw=np.polynomial.legendre.leggauss(6)
tot=0
for xi,wi in zip(0.25*gx+0.25,0.25*gw):
    y0=math.sqrt(1-xi*xi); ys,ws=np.polynomial.legendre.leggauss(4)
    sub=0
    for yy,ww in zip(0.5*(1-y0)*ys+0.5*(1+y0),0.5*(1-y0)*ws):
        hv,c=hdens(complex(xi,yy)); sub+=ww*hv
    tot+=wi*sub; print("x",xi,"inner",sub,flush=True)
lower=2*tot  # symmetric x -> -x
print("lower region integral (both halves):",lower,flush=True)
# (b) mean Re c at y=1 over x (symmetry): use points
