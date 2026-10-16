"""Actual frame -> Fock map; lower-cocycle E8 builder, no legacy verdict run."""
import sympy as s
from analysis import ROOT,load,emit,zero,clean
geo=load(ROOT/'reports/physical_bridge_2026_09_05/surface_parent_dictionary_2026_10_13/upstream_total_metric.py','reality_actual_frame')
legacy=load(ROOT/'frontier/B1138_structural_completion/verification/my_chevalley.py','reality_lower_E8')
class Engine:
    def __init__(self):
        self.alg=legacy.ChevalleyAlgebra(legacy.en_cartan(8),'E8')
        self.roots=self.alg.roots;self.cartan=self.alg.A
    def pair(self,p,q):return {j:x for j,x in enumerate(self.alg._bracket_basis(p,q)) if x}
def main():
    raw=geo.gammas();vac=s.eye(4)[:,0]
    cr=[(raw[0]-s.I*raw[1])/2,(raw[2]-s.I*raw[3])/2]
    F=s.Matrix.hstack(vac,cr[0]*vac,cr[1]*vac,cr[0]*cr[1]*vac)
    cs=[clean(F.H*c*F) for c in raw]
    return emit(cs,zero(F.H*F-s.eye(4)),Engine())
if __name__=='__main__':raise SystemExit(main())
