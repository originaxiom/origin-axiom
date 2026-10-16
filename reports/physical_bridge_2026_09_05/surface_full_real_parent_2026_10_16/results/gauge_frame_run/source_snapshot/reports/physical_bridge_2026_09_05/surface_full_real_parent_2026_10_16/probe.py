"""Pinned actual metric frame, no old science execution."""
import sympy as s
from analysis import HERE,load,cm,zero,emit
old=load(HERE.parent/'surface_real_boundary_2026_10_15/analysis.py','weighted_real_prior')
native=old.load(HERE.parent/'surface_real_boundary_2026_10_15/probe.py','weighted_actual_frame',analysis=old)
def main():
    raw=native.geo.gammas();vac=s.eye(4)[:,0]
    a=(raw[0]-s.I*raw[1])/2;b=(raw[2]-s.I*raw[3])/2
    F=s.Matrix.hstack(vac,a*vac,b*vac,a*b*vac)
    return emit([cm(F.H*c*F) for c in raw],zero(F.H*F-s.eye(4)),'superfield')
if __name__=='__main__':raise SystemExit(main())
