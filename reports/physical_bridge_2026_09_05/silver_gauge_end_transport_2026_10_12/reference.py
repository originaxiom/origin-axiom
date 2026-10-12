"""Coordinate weighted-adjoint and Euler-integral controls; no native import.

Same author/method diversity, not interval or global physical acceptance.
"""
from fractions import Fraction as F
from itertools import combinations
import json
from pathlib import Path
import sympy as s
import mpmath as mp

HERE=Path(__file__).resolve().parent; REPO=HERE.parents[2]

def run():
    exact={}; numeric={}; mp.mp.dps=50
    def ck(name,val):
        exact[name]=bool(val)
        if not val:raise AssertionError(name)
    def nc(name,a,b):
        err=abs(a-b)/(1+abs(a)+abs(b));numeric[name]={'passed':bool(err<mp.mpf('1e-38')),'residual':mp.nstr(err,20)}
        if not numeric[name]['passed']:raise AssertionError(name)
    inp=json.loads((HERE/'INPUTS.json').read_text()); data=json.loads((REPO/inp['candidate_path']).read_text())
    letters=s.symbols('A B T',nonzero=True)
    def char(w):
        result=s.Integer(1)
        for c in w:
            ix=data['generators'].index(c.lower()); result*=letters[ix]**(1 if c.islower() else -1)
        return s.cancel(result)
    rel=[char(w) for w in data['relators']]
    ck('formal_relations_leave_only_T_over_real_periods',rel==[letters[0]**2*letters[1]**2,letters[0]**2*letters[1]**6])
    ck('formal_peripheral_character_matches_actual_free_period',[char(w).subs({letters[0]:1,letters[1]:1}) for w in data['cusp_words']]==[1,letters[2]])
    lx,ly=F(1,2),F(3,2)
    ck('Fraction_dual_lattice_periods',F(-6,5)*lx+F(2,5)*ly==0 and F(-2,5)*lx+F(4,5)*ly==1)
    ck('Fraction_squared_angular_coefficient',lx*lx+ly*ly==F(5,2))
    h=inp['gauge_H']; weights=[sum(h[i] for i in pair) for pair in combinations(range(5),2)]
    ck('complete_10_generic_and_minus_one_fixed_controls',len(weights)==10 and all(w!=0 for w in weights) and sum(w%2==0 for w in weights)==4)
    ck('central_phase_matter_and_gauge_distinguished',all(w%5==4 for w in weights) and all((h[i]-h[j])%5==0 for i in range(5) for j in range(5)))

    # Coordinate basis is degree-ordered tuples, NOT native bit-mask order.
    basis=[tuple(c) for degree in range(4) for c in combinations(range(3),degree)]
    def wedge(j):
        M=s.zeros(8)
        for col,I in enumerate(basis):
            if j in I:continue
            row=basis.index(tuple(sorted((j,)+I)))
            M[row,col]=(-1)**sum(i<j for i in I)
        return M
    eps=[wedge(j) for j in range(3)]
    r,ell,mu,kx,ky=s.symbols('r ell mu kx ky',real=True)
    a=ell*s.exp(-r/ell);W=mu*s.exp(2*r/ell)
    metric=s.diag(*(a**(2-2*sum(j in (1,2) for j in I)) for I in basis))
    U=s.diag(*(a**(1-sum(j in (1,2) for j in I)) for I in basis));Ui=U.inv()
    A=eps[0]; B=W*eps[0]+s.I*kx*eps[1]+s.I*ky*eps[2]
    Ad=-metric.inv()*A.T*metric
    Bd=metric.inv()*B.H*metric-metric.inv()*A.T*metric.diff(r)
    qa=U*(A+Ad)*Ui
    qb=(U*((A+Ad)*Ui.diff(r)+(B+Bd)*Ui)).applyfunc(s.simplify)
    V=(qa*qb.diff(r)+qb*qb).applyfunc(s.simplify)
    ck('coordinate_weighted_adjoint_flat_leading',qa*qa==-s.eye(8))
    ck('coordinate_weighted_adjoint_cancels_first_derivative',all(s.simplify(v)==0 for v in qa*qb+qb*qa))
    ix=[basis.index((j,)) for j in range(3)];L2=(kx*kx+ky*ky)/a**2
    expected=s.Matrix([[(W+1/ell)**2+s.diff(W,r)+L2,-2*s.I*kx/(ell*a),-2*s.I*ky/(ell*a)],
                       [2*s.I*kx/(ell*a),W*W-s.diff(W,r)+L2,0],
                       [2*s.I*ky/(ell*a),0,W*W-s.diff(W,r)+L2]])
    ck('weighted_coordinate_full_one_form_block',all(s.simplify(v)==0 for v in V.extract(ix,ix)-expected))
    ck('weighted_coordinate_scalar_and_top',s.simplify(V[0,0]-W*W-ell**-2-L2)==0 and s.simplify(V[-1,-1]-V[0,0])==0)
    ck('mixed_block_nonzero_cannot_be_truncated',V[ix[0],ix[1]]!=0 and V[ix[0],ix[2]]!=0)
    ck('opposite_wall_keeps_angular_term',s.simplify(V[ix[1],ix[1]].subs(mu,-mu)-W*W-s.diff(W,r)-L2)==0)

    # Actual zero Fourier fixture: h=-1,theta=2/5 -> |xi|2=2/5;
    # choose supplied mu=2/5,ell=1 -> delta=1/4. No physical fit.
    x=mp.mpf(2)/5;elln=mp.mpf(1);delta=mp.mpf(1)/4
    def profile(xx,nu,sg,dd):return mp.whitw(mp.mpf(sg)/2-dd,nu,xx)/mp.sqrt(xx)
    def response(xx,nu,sg,dd):
        f=lambda t:profile(t,nu,sg,dd)
        return -2*xx/elln*mp.diff(f,xx)/f(xx)-sg*xx/elln
    for nu in (mp.mpf(0),mp.mpf(1)/4):
        for sg in (1,-1):
            kap=mp.mpf(sg)/2-delta;aa=nu+mp.mpf('0.5')-kap;bb=1+2*nu
            integrand=lambda y:4*y**(4*aa-1)*(1+y**4)**(bb-aa-1)*mp.exp(-x*y**4)/mp.gamma(aa)
            euler=x**nu*mp.exp(-x/2)*mp.quad(integrand,[0,1,mp.inf])
            f=lambda t:profile(t,nu,sg,delta)
            tag=f'{nu}_{sg}'
            nc('shifted_Euler_'+tag,euler,f(x))
            nc('shifted_radial_equation_'+tag,-4*(x*x*mp.diff(f,x,2)+x*mp.diff(f,x))+(x*x+(-2*sg+4*delta)*x+4*nu*nu)*f(x),0)
            val=response(x,nu,sg,delta)
            ck('shifted_response_positive_'+tag,val>0)
    plus0=response(x,0,1,delta);minus0=response(x,0,-1,delta)
    ck('nonzero_angular_static_product_not_zero',plus0*minus0>mp.mpf('1e-10'))
    nu=mp.mpf(1)/4
    nc('original_zero_angular_partner_recovered',response(x,nu,1,0)*response(x,nu,-1,0),(2*nu/elln)**2)
    nc('original_positive_sign_static_response_recovered',response(x,0,1,0),0)
    # Bounded action identity, keeping angular term and actual canonical flux.
    nu=mp.mpf(1)/4;sig=1;x1=mp.mpf('1.1');base=profile(x,nu,sig,delta)
    f=lambda t:profile(t,nu,sig,delta)/base
    Af=lambda t:(2*t/elln)*mp.diff(f,t)+sig*t/elln*f(t)
    energy=mp.quad(lambda t:elln/(2*t)*(Af(t)**2+(4*delta*t/elln**2+(2*nu/elln)**2)*f(t)**2),[x,x1])
    nc('shifted_actual_finite_interval_action',energy,f(x1)*Af(x1)-f(x)*Af(x))
    canonical=response(x,nu,1,delta)
    ordinary=-2*x/elln*mp.diff(f,x)
    ck('ordinary_normal_flux_mutation_detected',abs(ordinary-canonical)>mp.mpf('1e-10'))
    perm=[basis.index(tuple(j for j in range(3) if mask&(1<<j))) for mask in range(8)]
    canon=V.extract(perm,perm)
    return {'exact_checks':exact,'exact_passed':sum(exact.values()),'numerical_checks':numeric,
            'full_potential_matrix':[[str(v) for v in row] for row in canon.tolist()],
            'numerical_count':len(numeric),'precision':50,
            'static_nonzero_angular_response':{'plus':mp.nstr(plus0,24),'minus':mp.nstr(minus0,24),'product':mp.nstr(plus0*minus0,24)},
            'max_numerical_residual':mp.nstr(max(mp.mpf(v['residual']) for v in numeric.values()),24),
            'global_core_match':False,'new_native_imported':False,'outside_review':False,
            'generated_SM_selection':False,'full_goal_achieved':False}

if __name__=='__main__':print(json.dumps(run(),indent=2,default=str))
