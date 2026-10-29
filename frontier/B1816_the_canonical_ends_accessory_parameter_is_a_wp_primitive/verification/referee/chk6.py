import sys, pathlib as _p; sys.path.insert(0, str(_p.Path(__file__).resolve().parent))
from chk1 import *
gx,gw=np.polynomial.legendre.leggauss(8)
s=0
for xi,wi in zip(0.25*gx+0.25,0.25*gw):
    c,_=warm(complex(xi,1.0)); s+=2*wi*c.real; print(xi,c,flush=True)
print("<Re c>_x(1) =",s)
import math
