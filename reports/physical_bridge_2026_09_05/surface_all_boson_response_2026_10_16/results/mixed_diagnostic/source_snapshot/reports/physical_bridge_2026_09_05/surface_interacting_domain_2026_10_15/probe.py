"""Actual prior metric -> Fock and lower signed E8 engine; no old producer run."""
import importlib.util
import sympy as s
from analysis import ROOT,emit,zero,simp
prior=ROOT/'reports/physical_bridge_2026_09_05/surface_real_boundary_2026_10_15'
sp=importlib.util.spec_from_file_location('interacting_prior_formulation',prior/'analysis.py')
old=importlib.util.module_from_spec(sp);sp.loader.exec_module(old)
native=old.load(prior/'probe.py','interacting_actual_frame',analysis=old)
def main():
    raw=native.geo.gammas();vac=s.eye(4)[:,0]
    c0=(raw[0]-s.I*raw[1])/2;c1=(raw[2]-s.I*raw[3])/2
    F=s.Matrix.hstack(vac,c0*vac,c1*vac,c0*c1*vac)
    cs=[simp(F.H*c*F) for c in raw]
    return emit(cs,native.Engine(),zero(F.H*F-s.eye(4)))
if __name__=='__main__':raise SystemExit(main())
