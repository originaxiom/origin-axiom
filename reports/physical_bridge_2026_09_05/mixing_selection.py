"""R83 exact comparators, not a computed physical quartic at q0. No writes."""
import json
from functools import lru_cache
import sympy as s


def norm2(m):
    return s.expand(s.trace(m.H*m))


@lru_cache(None)
def scalar():
    x,y,a,c,d,j1,j2=s.symbols('x y a c d J1 J2',real=True)
    v=a*(x*x+y*y)+c*(x**4+y**4)+d*x*x*y*y-j1*x-j2*y
    gy=s.diff(v,y); gx=s.diff(v,x)
    r2=s.symbols('r2',nonnegative=True)
    l,m=s.symbols('lambda kappa',positive=True)
    c1,c2=s.symbols('c1 c2',positive=True)
    ratio2=d*d/(4*c1*c2)
    shifted=ratio2.subs({d:d/(l*l*m*m),c1:c1/l**4,c2:c2/m**4},simultaneous=True)
    checks={
        'x_axis_requires_transverse_source_zero':gy.subs(y,0)==-j2,
        'y_axis_requires_transverse_source_zero':gx.subs(x,0)==-j1,
        'large_d_still_not_exact_axis':gy.subs({y:0,d:10**6,j2:1})==-1,
        'zero_transverse_source_axis_possible':gy.subs({y:0,j2:0})==0,
        'zero_source_radius_comparison':s.expand(c*(x*x+y*y)**2+(d-2*c)*x*x*y*y-c*(x**4+y**4)-d*x*x*y*y)==0,
        'transverse_hessian':s.diff(gy,y).subs(y,0)==2*a+2*d*x*x,
        'finite_response_not_projection':gy.subs({a:1,c:1,d:3,x:1,y:s.Rational(1,8),j2:1})==s.Rational(1,128),
        'coordinate_ratio_invariant':s.cancel(shifted-ratio2)==0,
    }
    return {'checks':checks,'axis_gradient':str(gy.subs(y,0))}


@lru_cache(None)
def projection():
    u,v,w,t=s.symbols('u v w t',real=True)
    L=s.Matrix([[1,1],[1,-1],[0,0]]); ob=s.Matrix([u,v,w])
    beta=-(L.T*L).inv()*L.T*ob
    residual=s.simplify(L*beta+ob)
    P=s.eye(3)-L*(L.T*L).inv()*L.T
    higher=t*t*residual+t**3*s.Matrix([1,0,0])
    checks={
        'full_gram_minimizer':s.simplify(L.T*residual)==s.zeros(2,1),
        'projector_idempotent':P*P==P,
        'projector_self_adjoint':P.T==P,
        'relaxed_coefficient':norm2(residual)==w*w,
        'frozen_coefficient':norm2(ob)==u*u+v*v+w*w,
        'unobstructed_not_frozen_zero':norm2(ob).subs({u:1,v:2,w:0})==5 and norm2(residual).subs(w,0)==0,
        'obstruction_stays_positive':norm2(residual).subs(w,2)==4,
        'wrong_sign_correction_rejected':s.simplify(-L*beta+ob-residual)!=s.zeros(3,1),
        'sixth_order_survives':norm2(higher).subs(w,0)==t**6,
    }
    return {'checks':checks,'beta':[str(z) for z in beta],'relaxed':str(norm2(residual))}


@lru_cache(None)
def profiles():
    x,y=s.symbols('x y',real=True)
    n=s.Matrix([[0,1],[0,0]]); j=s.diag(1,-1)
    comm=lambda a,b:a*b-b*a
    one=x*n+y*n.H
    mu_one=-comm(one,one.H)/2
    cx=x*n;cy=y*n.H; f=comm(cx,cy)
    mu_two=-(comm(cx,cx.H)+comm(cy,cy.H))/2
    eone=norm2(mu_one);etwo=norm2(mu_two)+norm2(f)
    checks={
        'same_direction_full_moment':s.simplify(mu_one+(x*x-y*y)*j/2)==s.zeros(2),
        'same_direction_quartic':s.expand(eone-(x*x-y*y)**2/2)==0,
        'transverse_curvature_live':f==x*y*j,
        'transverse_full_quartic':s.expand(etwo-(x**4+y**4)/2-x*x*y*y)==0,
        'curvature_omission_rejected':s.expand(etwo-eone)==2*x*x*y*y,
        'same_direction_mixed_zero':eone.subs({x:1,y:1})==0,
        'transverse_mixed_not_zero':etwo.subs({x:1,y:1})==2,
        'one_axis_retains_positive_cost':eone.subs({x:1,y:0})==etwo.subs({x:1,y:0})==s.Rational(1,2),
    }
    return {'checks':checks,'same_direction':str(eone),'transverse':str(etwo)}


@lru_cache(None)
def schur():
    m=s.diag(2,3,5,7,s.Rational(1,210)); n=s.eye(5)
    for i in range(4):n[i,i+1]=1
    variables=s.symbols('z0:25'); X=s.Matrix(5,5,variables)
    eq=(X*m-m*X).reshape(25,1).col_join((X*n-n*X).reshape(25,1))
    linear=eq.jacobian(variables)
    e=s.eye(5)[:,0]; p=s.diag(1,0,0,0,0)
    checks={
        'determinants_one':m.det()==n.det()==1,
        'commutant_scalar':linear.rank()==24,
        'proper_line_invariant':m*e==2*e and n*e==e,
        'line_not_trivial_representation':m*e!=e,
        'no_trivial_fixed_vector':(m-s.eye(5)).det()!=0,
        'no_dual_trivial_fixed_vector':(m.inv().T-s.eye(5)).det()!=0,
        'full_proper_flag_invariant':all(m[k:,:k]==s.zeros(5-k,k) and n[k:,:k]==s.zeros(5-k,k) for k in range(1,5)),
        'invariant_line_not_reducing_complement':n*p!=p*n,
    }
    return {'checks':checks,'commutant_dimension':25-linear.rank(),'scope':'SL5 free-group comparator, not figure-eight witness'}


def report():
    groups={k:f() for k,f in [('scalar',scalar),('projection',projection),('profiles',profiles),('schur',schur)]}
    checks=[v for g in groups.values() for v in g['checks'].values()]
    return {'groups':groups,'passed':sum(checks),'total':len(checks),'all_checks_pass':all(checks)}


if __name__=='__main__':
    out=report();print(json.dumps(out,indent=2,sort_keys=True))
    raise SystemExit(0 if out['all_checks_pass'] else 1)
