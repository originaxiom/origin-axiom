import sys, pathlib as _p; sys.path.insert(0, str(_p.Path(__file__).resolve().parent))
from chk1 import *
def hd(t):
    c0,_=warm(t); h=1e-3
    cx=[solve(t+s*h,c0) for s in (-1,1)]; cy=[solve(t+1j*s*h,c0) for s in (-1,1)]
    return (0.5*(2*(cx[1]-cx[0])/(2*h)+1j*2*(cy[1]-cy[0])/(2*h))).imag
w=complex(-0.5,math.sqrt(3)/2)
for t in (0.02+1j,0.04+1j,0.1+math.sqrt(1-0.01)*1j,0.2+math.sqrt(1-.04)*1j,0.3+math.sqrt(1-.09)*1j,0.4+math.sqrt(1-.16)*1j,0.49+math.sqrt(1-.2401)*1j,0.49+0.9*1j, 0.5+1.2j,0.5+2j,0.5+3j,0.0+1.5j,0.02+2j,0.02+3j):
    if t.imag<1e-9: continue
    h=hd(t); print(t,"h",h,"rho=h*y^2",h*t.imag**2,flush=True)
