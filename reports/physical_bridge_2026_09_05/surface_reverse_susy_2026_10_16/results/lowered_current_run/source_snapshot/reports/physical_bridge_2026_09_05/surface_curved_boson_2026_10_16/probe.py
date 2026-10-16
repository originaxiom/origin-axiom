"""Actual coordinate metric, canonical norm and complete frame geometry."""
import sympy as s
from analysis import HERE,load,emit
def main():
    geo=load(HERE.parent/'surface_parent_dictionary_2026_10_13/upstream_total_metric.py','boson_actual_metric')
    vals=geo.geometry();g,co,E,gi,G,C=vals[:6]
    hol=s.Matrix([[1,s.I,0,0],[geo.v,s.I*geo.v,1,geo.x+s.I*geo.y]])
    h=s.simplify((hol*gi*hol.H).det())
    qcoord=s.Matrix([s.diff(s.log(h),geo.y)/2,0,0,0])
    fc=s.Matrix(4,4,lambda i,j:s.diff(qcoord[j],geo.coords[i])-s.diff(qcoord[i],geo.coords[j]))
    ff=(E*fc*E.T*geo.l**2).applyfunc(s.simplify)
    rho=s.sqrt(g.det())
    div=[s.simplify(geo.l*sum(s.diff(rho*E[i,j],geo.coords[j]) for j in range(4))/rho) for i in range(4)]
    curv=s.simplify(geo.l**2*geo.scalar_curvature(gi,G))
    cc=[[[s.simplify(geo.l*x) for x in row] for row in plane] for plane in C]
    ef=E.subs({geo.l:1,geo.A:1}).applyfunc(s.simplify)
    valid=s.simplify(h-4*geo.y**3/(geo.l**2*geo.A))==0 and (co.T*co-g).applyfunc(s.simplify)==s.zeros(4)
    return emit(cc,div,ff.tolist(),curv,ef,geo.coords,valid)
if __name__=='__main__':raise SystemExit(main())
