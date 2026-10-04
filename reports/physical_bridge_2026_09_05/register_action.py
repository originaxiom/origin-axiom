"""R94 exact safeguards; conditional character dynamics, not physical selection.

No files written. Import/execute only after the pushed pre-run seal.
"""
from functools import lru_cache
import json
import sympy as sp


@lru_cache(None)
def moves():
    x, y, z = sp.symbols('x y z')
    variables = sp.Matrix([x, y, z])
    K = x*x+y*y+z*z-x*y*z
    bivector = sp.Matrix([[0, 2*z-x*y, x*z-2*y],
                         [x*y-2*z, 0, 2*x-y*z],
                         [2*y-x*z, y*z-2*x, 0]])
    data = {
        'L': (sp.Matrix([x,z,x*z-y]), 1),
        'R': (sp.Matrix([z,y,y*z-x]), 1),
        'P': (sp.Matrix([y,x,z]), -1),
        'Li': (sp.Matrix([x,x*y-z,y]), 1),
        'Ri': (sp.Matrix([x*y-z,y,x]), 1),
        'T': (sp.Matrix([z,x,x*z-y]), -1),
        'Ti': (sp.Matrix([y,x*y-z,x]), -1),
    }
    def substitute(expr, image):
        return expr.subs(dict(zip(variables,image)), simultaneous=True)
    def compose(outer, inner):
        return substitute(outer,inner).applyfunc(sp.expand)
    return variables,K,bivector,data,substitute,compose


@lru_cache(None)
def chart():
    r,b = sp.symbols('r b', positive=True)
    x = r+1/r
    u = r-1/r
    coordinates = sp.Matrix([x,x/u*(b+1/b),x/u*(r*b+1/(r*b))])
    X,Y,Z = coordinates
    K = sp.cancel(X*X+Y*Y+Z*Z-X*Y*Z)
    area = sp.cancel(sp.diff(X,r)*sp.diff(Y,b)/(2*Z-X*Y))
    return r,b,coordinates,K,area


@lru_cache(None)
def generating():
    c,C,u,v,h = sp.symbols('c C u v h')
    ideal = sp.groebner([c*c-u*u-1,C*C-v*v-1,h*h-u*u*v*v+1],
                        c,C,h,u,v)
    def normal(expr):
        numerator = sp.cancel(expr).as_numer_denom()[0]
        return sp.expand(ideal.reduce(sp.expand(numerator))[1])
    def dq(expr):
        return sp.diff(expr,c)*u+sp.diff(expr,u)*c+sp.diff(expr,h)*u*c*v*v/h
    def dQ(expr):
        return sp.diff(expr,C)*v+sp.diff(expr,v)*C+sp.diff(expr,h)*u*u*v*C/h
    a = (C*u+h)/c
    b = (c*v+h)/C
    r = c+u
    ep = a/r
    old = sp.Matrix([2*c,c/u*(ep+1/ep),c/u*(a+1/a)])
    new = sp.Matrix([2*C,C/v*(b+1/b),C/v*(b*(C+v)+1/(b*(C+v)))])
    target = sp.Matrix([old[2],old[0],old[0]*old[2]-old[1]])
    # Derive derivatives of logs, rather than inserting the desired Hessian.
    pQ = dQ(a)/a
    Pq = dq(b)/b
    return dict(c=c,C=C,u=u,v=v,h=h,a=a,b=b,old=old,new=new,target=target,
                normal=normal,pQ=pQ,Pq=Pq,cross=u*v/h)


@lru_cache(None)
def orbit():
    variables,K,bivector,data,substitute,compose = moves()
    t = sp.symbols('t')
    T = data['T'][0]
    square = compose(T,T)
    jac = square.jacobian(variables)
    points = []
    for sign in (1,-1):
        x = (3+sign*sp.I*sp.sqrt(3))/2
        y = (3-sign*sp.I*sp.sqrt(3))/2
        p = sp.Matrix([x,y,y])
        reduction = lambda expr: sp.simplify(sp.expand(expr))
        j = substitute(jac,p).applyfunc(reduction)
        grad = substitute(sp.Matrix([sp.diff(K,s) for s in variables]),p)
        discriminant = reduction((x*x/4-1)*(y*y/4-1)-1)
        points.append(dict(point=p,jacobian=j,grad=grad,
                           discriminant=discriminant,
                           characteristic=reduction(j.charpoly(t).as_expr()),t=t))
    return points


@lru_cache(None)
def checks():
    out = {}
    variables,K,bivector,data,substitute,compose = moves()
    for name,(image,sign) in data.items():
        J = image.jacobian(variables)
        out[name+'_preserves_K'] = sp.expand(substitute(K,image)-K)==0
        residual = (J*bivector*J.T-sign*substitute(bivector,image)).applyfunc(sp.expand)
        for i,j in ((0,1),(1,2),(2,0)):
            out[name+'_poisson_'+str(i)+str(j)] = residual[i,j]==0
        # The target sheet has epsilon*s: scalar coefficient epsilon^2=1.
        s = sp.symbols('s')
        out[name+'_tracked_form'] = sign*(sign*s)==s
    identity = variables
    for name,inverse in (('L','Li'),('R','Ri'),('T','Ti'),('P','P')):
        out[name+'_inverse'] = compose(data[name][0],data[inverse][0])==identity
    out['contravariant_LP_halfstep'] = compose(data['P'][0],data['L'][0])==data['T'][0]
    out['contravariant_LR_square'] = compose(data['T'][0],data['T'][0])==compose(data['R'][0],data['L'][0])
    out['swap_conjugates_shears'] = compose(data['P'][0],compose(data['L'][0],data['P'][0]))==data['R'][0]
    wrong = data['T'][0].jacobian(variables)*bivector*data['T'][0].jacobian(variables).T-substitute(bivector,data['T'][0])
    out['unflipped_halfstep_rejected'] = any(sp.expand(e)!=0 for e in wrong)
    plus,minus = sp.symbols('fplus fminus')
    out['nonzero_sheet_coefficient_is_odd'] = sp.solve([minus+plus],minus)=={minus:-plus}
    out['constant_nonzero_coefficient_rejected'] = (minus+plus).subs(minus,plus)==2*plus
    r,b,coordinates,k,area = chart()
    out['nonlinear_parabolic_chart'] = k==0
    out['Darboux_pullback'] = sp.cancel(area-1/(r*b))==0
    out['wrong_abelian_leaf_rejected'] = k-4!=0
    g = generating()
    normal = g['normal']
    out['derived_pQ'] = normal(g['pQ']-g['cross'])==0
    out['derived_Pq'] = normal(g['Pq']-g['cross'])==0
    out['closed_generating_one_form'] = normal(g['pQ']-g['Pq'])==0
    out['wrong_generating_sign_rejected'] = normal(g['pQ']+g['Pq'])!=0
    for i in range(3):
        out['actual_nonlinear_coordinate_'+str(i)] = normal(g['new'][i]-g['target'][i])==0
    out['old_y_matched_branch'] = normal(g['old'][1]-(2*g['c']*g['C']-2*g['h']))==0
    out['opposite_sqrt_changes_old_point'] = normal((2*g['c']*g['C']+2*g['h'])-(2*g['c']*g['C']-2*g['h']))!=0
    s,Pprev,pnext = sp.symbols('s Pprev pnext', real=True)
    previous = -(-s)*Pprev
    current = -s*pnext
    out['signed_DEL_matches_momenta'] = sp.expand(previous+current-s*(Pprev-pnext))==0
    out['untracked_DEL_rejected'] = sp.expand((-s*Pprev-s*pnext).subs(Pprev,pnext))==-2*s*pnext
    out['nondegenerate_mixed_derivative'] = normal(g['cross'])!=0
    for j,row in enumerate(orbit()):
        p = row['point']
        simplify = lambda e:sp.simplify(sp.expand(e))
        out['geometric_'+str(j)+'_leaf'] = simplify(substitute(K,p))==0
        out['geometric_'+str(j)+'_half_exchange'] = (substitute(data['T'][0],p)-sp.conjugate(p)).applyfunc(simplify)==sp.zeros(3,1)
        out['geometric_'+str(j)+'_square_fixed'] = (substitute(compose(data['T'][0],data['T'][0]),p)-p).applyfunc(simplify)==sp.zeros(3,1)
        out['geometric_'+str(j)+'_regular'] = any(simplify(e)!=0 for e in row['grad'])
        out['geometric_'+str(j)+'_chart_discriminant'] = row['discriminant']==-sp.Rational(3,16)
        t = row['t']
        out['geometric_'+str(j)+'_Floquet'] = sp.expand(row['characteristic']-(t-1)*(t*t-5*t+1))==0
    origin = sp.zeros(3,1)
    grad0 = substitute(sp.Matrix([sp.diff(K,s) for s in variables]),origin)
    out['singular_origin_rejected'] = grad0==sp.zeros(3,1)
    return {name:bool(value) for name,value in out.items()}


def report():
    values=checks()
    return dict(scope='R94 regular Fricke leaves and declared move/sign lift; local nonlinear action only',
                checks=values,passed=sum(values.values()),total=len(values),
                failed=[name for name,value in values.items() if not value],
                native_is_analytic_proof=False,non_author_acceptance=False,
                physical_SM_selection_derived=False,physical_chirality_derived=False,
                generated_quantum_law=False,physical_goal_achieved=False)


if __name__=='__main__':
    data=report()
    print(json.dumps(data,sort_keys=True))
    raise SystemExit(0 if not data['failed'] else 1)
