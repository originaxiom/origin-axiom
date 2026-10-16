"""Exterior Clifford and full closed-coframe Koszul method."""
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
    rows={(0,1,0):-s.Integer(1),(1,2,2):s.Rational(1,2),(0,3,2):-s.Integer(1),(1,3,3):-s.Rational(1,2)}
    rows.update({(j,i,k):-v for (i,j,k),v in list(rows.items())})
    C=lambda i,j,k:rows.get((i,j,k),s.Integer(0))
    gk=[[[s.expand((C(i,j,k)-C(j,k,i)+C(k,i,j))/2) for k in range(4)] for j in range(4)] for i in range(4)]
    valid=all(zero(e*e) for e in es) and zero(es[0]*es[1]+es[1]*es[0])
    return emit(cs,gk,valid)
if __name__=='__main__':raise SystemExit(main())
