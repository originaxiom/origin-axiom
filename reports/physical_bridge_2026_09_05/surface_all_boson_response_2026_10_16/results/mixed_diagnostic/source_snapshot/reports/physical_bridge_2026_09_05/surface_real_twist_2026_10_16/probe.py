"""Full coordinate metric/Koszul method, credited geometric primitives."""
import sympy as s
from analysis import HERE,load,cm,zero,emit
def main():
    geo=load(HERE.parent/'surface_parent_dictionary_2026_10_13/upstream_total_metric.py','real_twist_metric')
    vals=geo.geometry();raw=vals[8];gk=vals[6]
    vac=s.eye(4)[:,0];a=(raw[0]-s.I*raw[1])/2;b=(raw[2]-s.I*raw[3])/2
    F=s.Matrix.hstack(vac,a*vac,b*vac,a*b*vac)
    tensor=[[[s.simplify(geo.l*x) for x in row] for row in plane] for plane in gk]
    valid=zero(F.H*F-s.eye(4)) and all(s.simplify(vals[6][i][j][k]-vals[7][i][j][k])==0 for i in range(4) for j in range(4) for k in range(4))
    return emit([cm(F.H*c*F) for c in raw],tensor,valid)
if __name__=='__main__':raise SystemExit(main())
