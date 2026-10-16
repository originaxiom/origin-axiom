"""Exterior Fock construction; same authored action/source formulation."""
from itertools import combinations
import sympy as s
from analysis import emit,zero
def main():
    basis=[v for n in range(3) for v in combinations(range(2),n)];es=[]
    for j in range(2):
        e=s.zeros(4)
        for k,v in enumerate(basis):
            if j not in v:e[basis.index(tuple(sorted((j,)+v))),k]=(-1)**sum(x<j for x in v)
        es.append(e)
    cs=[es[0]-es[0].H,s.I*(es[0]+es[0].H),es[1]-es[1].H,s.I*(es[1]+es[1].H)]
    return emit(cs,all(zero(e*e) for e in es) and zero(es[0]*es[1]+es[1]*es[0]),'component')
if __name__=='__main__':raise SystemExit(main())
