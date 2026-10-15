"""Exterior-Fock construction; existing separate upper-cocycle/root engine.

Same analysis and Sympy, not independent authorship or analytic review.
"""
from itertools import combinations
import sympy as s
from analysis import ROOT,load,emit,zero
prior=ROOT/'reports/physical_bridge_2026_09_05/surface_invariant_brackets_2026_10_14'
old_analysis=load(prior/'analysis.py','reality_reference_bracket_formulation')
old=load(prior/'reference.py','reality_upper_E8',analysis=old_analysis)
class Engine:
    def __init__(self):
        self.alg=old.Engine();self.roots=self.alg.roots;self.cartan=self.alg.cartan
        self.sign=[1]*8+[self.alg.sign[r] for r in self.roots]
    def pair(self,p,q):
        return {j:x*self.sign[p]*self.sign[q]*self.sign[j] for j,x in self.alg.pair(p,q).items() if x}
def main():
    basis=[b for n in range(3) for b in combinations(range(2),n)];es=[]
    for j in range(2):
        e=s.zeros(4)
        for k,b in enumerate(basis):
            if j not in b:e[basis.index(tuple(sorted((j,)+b))),k]=(-1)**sum(x<j for x in b)
        es.append(e)
    cs=[es[0]-es[0].H,s.I*(es[0]+es[0].H),es[1]-es[1].H,s.I*(es[1]+es[1].H)]
    valid=all(zero(e*e) for e in es) and zero(es[0]*es[1]+es[1]*es[0])
    return emit(cs,valid,Engine())
if __name__=='__main__':raise SystemExit(main())
