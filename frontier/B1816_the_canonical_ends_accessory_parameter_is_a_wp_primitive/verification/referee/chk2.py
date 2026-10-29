import sys, pathlib as _p; sys.path.insert(0, str(_p.Path(__file__).resolve().parent))
from chk1 import *
for t in (0.4+1.5j,0.35+2.5j,-0.2+1.1j,0.15+3j,0.3+5j):
    c,s=warm(t)
    lat,z0,Aa,Ab=cc.monodromy(t,c); P0=cc.mobius_of(cc.puncture_loop(lat,c,z0,0.05))
    g,Ra,Rb,RP,lam=cc.normalise(Aa,Ab,P0)
    x,y,z=(abs(v) for v in cc.traces(Aa,Ab))
    print("true",t,"c",c,"Im u min",cc.uniformisation_check(t,c,g,npts=5),"markov",abs(x*x+y*y+z*z-x*y*z)/(x*y*z),"tr P0",np.trace(P0),flush=True)
t=0.15+3j
c=solve(t,0j)
lat,z0,Aa,Ab=cc.monodromy(t,c); P0=cc.mobius_of(cc.puncture_loop(lat,c,z0,0.05))
g,Ra,Rb,RP,lam=cc.normalise(Aa,Ab,P0)
print("control c",c,"Im u min",cc.uniformisation_check(t,c,g,npts=5),"trP0",np.trace(P0),"traces",[abs(v) for v in cc.traces(Aa,Ab)])
