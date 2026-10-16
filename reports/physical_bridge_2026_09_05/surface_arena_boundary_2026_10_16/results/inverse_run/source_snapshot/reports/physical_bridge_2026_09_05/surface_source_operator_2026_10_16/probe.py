"""Actual pinned metric/Fock frame, no prior science producer executed."""
import importlib.util
import sympy as s
from analysis import ROOT,emit,zero,clean
prior=ROOT/'reports/physical_bridge_2026_09_05/surface_real_boundary_2026_10_15'
sp=importlib.util.spec_from_file_location('source_operator_prior',prior/'analysis.py')
old=importlib.util.module_from_spec(sp);sp.loader.exec_module(old)
native=old.load(prior/'probe.py','source_operator_actual',analysis=old)
def main():
    raw=native.geo.gammas();vac=s.eye(4)[:,0]
    c0=(raw[0]-s.I*raw[1])/2;c1=(raw[2]-s.I*raw[3])/2
    F=s.Matrix.hstack(vac,c0*vac,c1*vac,c0*c1*vac)
    return emit([clean(F.H*c*F) for c in raw],zero(F.H*F-s.eye(4)))
if __name__=='__main__':raise SystemExit(main())
