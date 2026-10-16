"""Exterior-Fock and aligned upper signed E8 engine; shared authored questions."""
import importlib.util
from itertools import combinations
import sympy as s
from analysis import ROOT,emit,zero
prior=ROOT/'reports/physical_bridge_2026_09_05/surface_real_boundary_2026_10_15'
sp=importlib.util.spec_from_file_location('interacting_reference_formulation',prior/'analysis.py')
old=importlib.util.module_from_spec(sp);sp.loader.exec_module(old)
ref=old.load(prior/'reference.py','interacting_reference_engine',analysis=old)
def main():
    basis=[v for n in range(3) for v in combinations(range(2),n)];es=[]
    for j in range(2):
        e=s.zeros(4)
        for k,v in enumerate(basis):
            if j not in v:e[basis.index(tuple(sorted((j,)+v))),k]=(-1)**sum(x<j for x in v)
        es.append(e)
    cs=[es[0]-es[0].H,s.I*(es[0]+es[0].H),es[1]-es[1].H,s.I*(es[1]+es[1].H)]
    return emit(cs,ref.Engine(),all(zero(e*e) for e in es) and zero(es[0]*es[1]+es[1]*es[0]))
if __name__=='__main__':raise SystemExit(main())
