"""Derive tube geometry in actual coordinates before closed-frame comparison."""
import sympy as s
from analysis import HERE,load,a,b,ell,simp,zero,emit
def main():
    geo=load(HERE.parent/'surface_parent_dictionary_2026_10_13/upstream_total_metric.py','actual_tube_metric')
    g,co,E,gi,G,C=geo.geometry()[:6]
    aa=s.sqrt(geo.A/geo.y)*(geo.u+geo.x*geo.v);bb=s.sqrt(geo.A*geo.y)*geo.v
    sub={geo.u:a*s.sqrt(geo.y/geo.A)-geo.x*b/s.sqrt(geo.A*geo.y),geo.v:b/s.sqrt(geo.A*geo.y),geo.l:ell}
    cl=lambda z:simp(s.simplify(z.subs(sub,simultaneous=True)))
    grad=lambda f:s.Matrix([s.simplify(sum(E[i,j]*s.diff(f,geo.coords[j]) for j in range(4))) for i in range(4)])
    f=s.expand(aa*aa+bb*bb);N=grad(f).applyfunc(cl);D=s.Matrix.hstack(grad(aa),grad(bb)).applyfunc(cl)
    cc=[[[cl(z) for z in row] for row in plane] for plane in C]
    transT={geo.x:geo.x+1,geo.u:geo.u-geo.v}
    transS={geo.x:-geo.x/(geo.x**2+geo.y**2),geo.y:geo.y/(geo.x**2+geo.y**2),geo.u:geo.v,geo.v:-geo.u}
    charts=s.simplify(f.subs(transT,simultaneous=True)-f)==0 and s.simplify(f.subs(transS,simultaneous=True)-f)==0
    valid=zero(co.T*co-g) and s.simplify(f-geo.A*((geo.u+geo.x*geo.v)**2/geo.y+geo.y*geo.v**2))==0
    return emit(N,D,cc,valid,charts)
if __name__=='__main__':raise SystemExit(main())
