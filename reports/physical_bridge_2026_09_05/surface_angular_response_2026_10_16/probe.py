"""Actual source coefficient and coordinate metric route."""
import sympy as s
from analysis import HERE,load,source,emit,cm,zero
def main():
    geo=load(HERE.parent/'surface_parent_dictionary_2026_10_13/upstream_total_metric.py','angular_coordinate_metric')
    g,co,E=geo.geometry()[:3];f=geo.A*((geo.u+geo.x*geo.v)**2/geo.y+geo.y*geo.v**2)
    point={geo.x:0,geo.y:1,geo.u:s.Rational(9,10),geo.v:s.Rational(6,5),geo.l:1,geo.A:1}
    N=s.Matrix([s.simplify(sum(E[i,j]*s.diff(f,geo.coords[j]) for j in range(4))).subs(point) for i in range(4)])
    n=cm(N/s.sqrt(N.dot(N)));J=s.Matrix([[0,-1,0,0],[1,0,0,0],[0,0,0,-1],[0,0,1,0]])
    c=J*n;ph=s.eye(4)-n*n.T-c*c.T;T=ph[:,0];t=cm(T/s.sqrt(T.dot(T)));frame=s.Matrix.hstack(n,t,J*t,c)
    vv,ext,valid=source('native');valid &= zero(co.T*co-g)
    return emit(vv,ext,frame,valid,'native')
if __name__=='__main__':raise SystemExit(main())
