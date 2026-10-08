"""Separate polynomial Green identity and Laurent boundary calculations."""
from functools import lru_cache
from itertools import combinations, product
import json
import sympy as s
I=s.I
zero=lambda A:all(s.simplify(a)==0 for a in A)
@lru_cache(None)
def run():
    facts={};x,y=s.symbols('x y',real=True);om=2+x+y
    a=s.Matrix([1+x*y, x+I*y,1+y*y,x*x+I])
    b=s.Matrix([x*x-y,1+I*x,y+x*y,1-y+I*x*x])
    dz=lambda z:s.diff(z,x)-I*s.diff(z,y)
    db=lambda z:s.diff(z,x)+I*s.diff(z,y)
    def mass(z):
        return s.Matrix([-dz(z[1])/(s.sqrt(2)*om**2),s.sqrt(2)*dz(z[0]),db(z[3])/om,-db(z[2])/om])
    H=s.diag(om**2,s.Rational(1,2),om,om)
    residual=(a.T*H*mass(b)-mass(a).T*H*b)[0]
    current_x=(-a[0]*b[1]+a[1]*b[0])/s.sqrt(2)+a[2]*b[3]-a[3]*b[2]
    current_y=I*(a[0]*b[1]-a[1]*b[0])/s.sqrt(2)+I*(a[2]*b[3]-a[3]*b[2])
    volume=s.integrate(s.expand(residual),(x,0,1),(y,0,1))
    surface=s.integrate(current_x.subs(x,1)-current_x.subs(x,0),(y,0,1))+s.integrate(current_y.subs(y,1)-current_y.subs(y,0),(x,0,1))
    facts['variable_metric_green_identity_including_surface']=s.simplify(volume-surface)==0
    facts['dropping_surface_term_is_detected']=s.simplify(volume)!=0
    t=s.symbols('t',real=True)
    vec=s.Matrix([1+x*t, x*x+I*t, t*t+I*x,x+t])
    V=s.Matrix([[0,I,0,0],[-I,0,0,0],[0,0,0,I],[0,0,-I,0]])
    R=s.diag(1,1,-1,-1);drift=s.diag(s.Rational(1,2),-s.Rational(1,2),0,0)
    apply=lambda z:s.diff(z,t)+I*s.exp(t)*R*s.diff(z,x)+drift*z
    adj=lambda z:-s.diff(z,t)+I*s.exp(t)*R*s.diff(z,x)+drift*z
    facts['differential_antilinear_kernel_pairing_sign']=zero(V*apply(vec).conjugate()+adj(V*vec.conjugate()))
    facts['opposite_sign_control_fails']=not zero(V*apply(vec).conjugate()-adj(V*vec.conjugate()))
    z=s.symbols('z',nonzero=True)
    star=lambda A:A.conjugate().subs(s.conjugate(z),1/z)
    def S(B):
        return s.BlockMatrix([[s.zeros(2),B],[star(B).T,s.zeros(2)]]).as_explicit()
    windings=[];passing=[]
    for n in (-3,-1,0,1,3):
        B=I*s.diag(z**(1+2*n),z**-1)
        C=I*s.diag(z,z**(-1-2*n));base=I*s.diag(z,z**-1)
        U=S(B);W=S(C);P=(s.eye(4)+U)/2;Pc=(s.eye(4)+W)/2
        dets=[s.cancel(A.det()/base.det()) for A in (B,C)]
        windings.append([int(s.cancel(z*s.diff(d,z)/(2*d))) for d in dets])
        passing.append(all([zero(star(U).T-U),zero(U*U-s.eye(4)),
          zero(R*U+U*R),zero(U.subs(z,-z)-R*U*R),
          zero(V*star(W)*V+U),zero(Pc.T*V*P)]))
    facts['laurent_seam_adjoint_and_cross_sector_pairing']=all(passing)
    facts['laurent_relative_winding_controls']=windings==[[n,-n] for n in (-3,-1,0,1,3)]
    K=s.Matrix([[1,2,0,0,0],[0,1,1,0,0]])
    rect=[[len(K.nullspace()),len(K.T.nullspace()),len(K.nullspace())-len(K.T.nullspace())],
          [len(K.T.nullspace()),len(K.nullspace()),len(K.T.nullspace())-len(K.nullspace())]]
    facts['independent_rectangular_kernel_cokernel_count']=rect==[[3,0,3],[0,3,-3]]
    # SU5_g x SU5_b tensor branching, independent of E8 root producer.
    charges=[-2,-2,-2,3,3]
    fund=charges;anti=[-q for q in fund]
    ten=[sum(charges[i] for i in ij) for ij in combinations(range(5),2)]
    roster=[a-b for a,b in product(charges,repeat=2) if a!=b]
    # Include all diagonal and equal-charge roots of gauge24 separately.
    roster=[charges[i]-charges[j] for i in range(5) for j in range(5) if i!=j]+[0]*4
    roster += [0]*24
    roster += [q for q in ten for _ in range(5)]+[-q for q in ten for _ in range(5)]
    roster += [q for q in anti for _ in range(10)]+[q for q in fund for _ in range(10)]
    ranks=[roster.count(q)//d for q,d in zip(range(1,7),(6,3,2,3,6,1))]
    cn=[sum(q!=0 for q in roster),roster.count(0)]
    facts['separate_tensor_roster_keeps_all_charges']=len(roster)==248 and cn==[212,36] and ranks==[5,10,10,5,1,5] and all(roster.count(q)==roster.count(-q) for q in range(1,7))
    return {'predicates':{k:bool(v) for k,v in facts.items()},'predicates_passed':sum(bool(v) for v in facts.values()),
        'multiplicity_ranks':ranks,'charged_neutral_dimensions':cn,
        'rectangular_control':rect,'winding_samples':windings,
        'nonauthor_acceptance':False,'physical_goal_achieved':False}
if __name__=='__main__':
    d=run();print(json.dumps(d,indent=2,sort_keys=True))
    raise SystemExit(0 if all(d['predicates'].values()) else 1)
