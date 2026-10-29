import sys, pathlib as _p; sys.path.insert(0, str(_p.Path(__file__).resolve().parent))
from chk1 import *
t0=complex(0.25,4.0); c=dict(ST)[t0]
for y in np.arange(4.5,16.01,0.5):
    c=solve(complex(0.25,y),c); print(y,c.real,c.imag,flush=True)
