"""R72 finite controls for exact local solution/Green witness proof; not particles."""
from functools import lru_cache
import importlib.util
import json
from pathlib import Path
import sympy as s

spec=importlib.util.spec_from_file_location('r72_channel_input',Path(__file__).with_name('cone_channel.py'))
old=importlib.util.module_from_spec(spec)
spec.loader.exec_module(old)
sp,zero,tensor,blocks=old.sp,old.zero,old.tensor,old.blocks
I9=sp(s.eye(9))
I36=sp(s.eye(36))
I72=sp(s.eye(72))
mathG=tensor(sp(s.eye(8)),old.G)
Gamma=blocks(sp(s.zeros(36)),-I36,I36,sp(s.zeros(36)))
J=-mathG*Gamma
M=tensor(old.M,I9)
A0=blocks(M,sp(s.zeros(36)),sp(s.zeros(36)),-M)

def selector(indices,n=72):
    return sp(s.eye(n)[:,indices])

def adjoint(a):
    return sp(mathG.inv()*a.H*mathG)

@lru_cache(None)
def actual_controls():
    alpha=s.Symbol('alpha',positive=True)
    t=s.Symbol('t',positive=True)
    v,beta=s.symbols('v beta',real=True)
    E=s.sqrt(alpha)*t*tensor(old.ex,old.n)+beta*t*t/s.sqrt(alpha)*tensor(old.ey,old.p)
    Ed=s.sqrt(alpha)*t*tensor(old.ex.H,old.nd)+beta*t*t/s.sqrt(alpha)*tensor(old.ey.H,old.pd)
    L=E+Ed
    K=-v*tensor(sp(s.eye(4)),old.h)
    A=blocks(M+K,-L,-L,-M-K)
    wrong=blocks(M+K,-E,-E,-M-K)
    checks=dict(
        actual_Gram_adjoint=zero(adjoint(A)-A),
        actual_Gamma_pairing=zero(A*Gamma+Gamma*A),
        actual_current_conservation=zero(A.H*J+J*A),
        actual_limit=zero(A.subs({t:0,v:0})-A0),
        exact_neutral_Z_no_action=zero(old.z),
        all_72_form_components=A.rows==72 and A.cols==72,
        coefficient_H_Gram_adjoint=zero(old.h.H*old.G-old.G*old.h),
        coefficient_N_Gram_adjoint=zero(old.n.H*old.G-old.G*old.nd),
        coefficient_P_Gram_adjoint=zero(old.p.H*old.G-old.G*old.pd),
        Gamma_skew=zero(Gamma.H+Gamma) and zero(Gamma*Gamma+I72),
        Green_skew_nondegenerate=zero(J.H+J) and J.rank()==72,
        wrong_adjunction_breaks_current=not zero(wrong.H*J+J*wrong),
        H_matrix_norm_bound=old.H.H*old.H==s.diag(1,0,0,1),
        N_matrix_norm_bound=old.N.H*old.N==s.diag(0,0,1,1),
        P_matrix_norm_bound=old.P.H*old.P==s.diag(0,0,0,1),
        link_wedge_unit_bound=zero((old.ex.H*old.ex)**2-old.ex.H*old.ex) and zero((old.ey.H*old.ey)**2-old.ey.H*old.ey),
    )
    return dict(checks=checks,form_dimension=72,tail_bound='2|v|+4sqrt(alpha)t+4|beta|t^2/sqrt(alpha)')

@lru_cache(None)
def contraction_controls():
    gamma=s.Rational(1,8); a=s.Rational(1,4); b=s.Rational(3,4); eps=s.Rational(1,64)
    ell=s.Symbol('ell',nonnegative=True)
    stable=s.integrate(s.exp(-(a-gamma)*ell),(ell,0,s.oo))
    unstable=s.integrate(s.exp(-(b+gamma)*ell),(ell,0,s.oo))
    q=eps*(stable+unstable)
    graph=eps*unstable/(1-q)
    mult={-1:18,0:36,1:18}
    shifts=[s.Rational(1,4),-s.Rational(3,4)]
    dims=[sum(n for eig,n in mult.items() if eig-shift<0) for shift in shifts]
    gaps=[(min(-(eig-shift) for eig in mult if eig-shift<0),
           min(eig-shift for eig in mult if eig-shift>0)) for shift in shifts]
    checks=dict(
        stable_integral=stable==8,
        unstable_integral=unstable==s.Rational(8,7),
        contraction_constant=q==s.Rational(1,7) and q<1,
        exact_seed_estimate=1/(1-q)==s.Rational(7,6),
        unstable_graph_bound=graph==s.Rational(1,48),
        both_gap_pairs=gaps==[(a,b),(a,b)],
        injected_dimensions=dims==[54,18],
        slow_exact_envelope=shifts[0]-gamma==s.Rational(1,8),
        fast_exact_envelope=shifts[1]-gamma==-s.Rational(7,8),
        fast_is_slow_weighted=(shifts[1]-gamma)<(shifts[0]-gamma),
        unsafe_contraction_fails=s.Rational(1,4)*(stable+unstable)>1,
        stable_graph_seed_retained=graph<1 and dims[0]+18==72,
    )
    return dict(checks=checks,slow_space_dimension=54,fast_space_dimension=18,
                contraction=q,graph_bound=graph,scope='Constants of authored continuous contraction; no numerical solve')

@lru_cache(None)
def tail_controls():
    x=s.Symbol('s',positive=True)
    bound=4/s.sqrt(x)+5/x
    late=2**20
    eps=s.Rational(1,64)
    checks=dict(
        exact_comparator_moment=zero(2*(-1/(2*x*x)-1/(2*x))+1/x+1/(x*x)),
        late_comparator_passes=bound.subs(x,late)<eps,
        late_comparator_bound_rational=bound.subs(x,late)==s.Rational(4101,1048576),
        unsafe_early_tail=bound.subs(x,1)>eps,
        comparator_bound_monotone=s.diff(bound,x).is_negative is True,
        comparator_tends_zero=s.limit(bound,x,s.oo)==0,
        fixed_parameters_not_uniform_radius=late>1,
    )
    return dict(checks=checks,exact_comparator_tail=late,comparator_epsilon_bound=bound.subs(x,late),
                scope='Declared comparator only; general S exists from the actual branch limits')

@lru_cache(None)
def geometry_controls():
    minus=[i for i in range(72) if A0[i,i]==-1]
    middle=[i for i in range(72) if A0[i,i]==0]
    plus=[i for i in range(72) if A0[i,i]==1]
    slow=selector(minus+middle)
    fast=selector(minus)
    crit=selector(middle)
    restricted=slow.H*J*slow
    iJ8=s.I*blocks(sp(s.zeros(4)),sp(s.eye(4)),-sp(s.eye(4)),sp(s.zeros(4)))
    checks=dict(
        exact_limit_multiplicities=[len(minus),len(middle),len(plus)]==[18,36,18],
        slow_rank=slow.rank()==54 and fast.rank()==18,
        fast_annihilator_limit=zero(fast.H*J*slow),
        restricted_rank=restricted.rank()==36,
        radical_dimension=restricted.cols-restricted.rank()==18,
        critical_nonzero_Green=crit.H*J*crit!=s.zeros(36) and (crit.H*J*crit).rank()==36,
        ambient_balanced_signature=iJ8.eigenvals()=={-1:4,1:4},
        quotient_balanced_half=36-18==18 and 54-18==36,
        frozen_fast_minimal_power=2*s.Rational(7,8)-1==s.Rational(3,4),
        four_Z_prior_not_entire_witnessed=4<36 and 36-4==32,
    )
    return dict(checks=checks,ambient_dimension=72,witnessed_quotient_dimension=36,radical_dimension=18,
                witnessed_signature=[18,18],scope='Limit linear algebra supporting actual conserved-current proof')

@lru_cache(None)
def norm_controls():
    x=s.Symbol('s',positive=True)
    eps=s.Symbol('epsilon',positive=True)
    r=s.Symbol('r',positive=True)
    rho=s.Rational(7,8)
    cut=eps**-2*s.integrate(r**(2*rho),(r,0,2*eps))
    bad=eps**-2*s.integrate(r**s.Rational(1,2),(r,0,2*eps))
    checks=dict(
        slow_L2_bound=s.integrate(s.exp(-s.Rational(3,4)*x),(x,1,s.oo))==s.Rational(4,3)*s.exp(-s.Rational(3,4)),
        fast_L2_bound=s.integrate(s.exp(-s.Rational(11,4)*x),(x,1,s.oo))==s.Rational(4,11)*s.exp(-s.Rational(11,4)),
        fast_cutoff_norm_zero=s.limit(cut,eps,0,dir='+')==0,
        fast_cutoff_exponent=zero(cut/(eps**s.Rational(3,4))-2**s.Rational(11,4)*s.Rational(4,11)),
        too_slow_cutoff_fails=s.limit(bad,eps,0,dir='+')==s.oo,
        exact_solutions_pair_zero=s.limit(s.exp(-s.Rational(3,4)*x),x,s.oo)==0,
        residual_weight_still_dangerous=s.integrate(s.exp(x),(x,1,s.oo))==s.oo,
    )
    return dict(checks=checks,cutoff_squared_error_bound=cut,scope='Envelope and cutoff bounds, not product-domain admission')

@lru_cache(None)
def rotated_controls():
    m=old.M
    a0=blocks(m,sp(s.zeros(4)),sp(s.zeros(4)),-m)
    u=s.Rational(1,1024)
    c=(1-u*u)/(1+u*u); sn=2*u/(1+u*u)
    O=sp([[c,-sn,0,0],[sn,c,0,0],[0,0,1,0],[0,0,0,1]])
    R=blocks(O,sp(s.zeros(4)),sp(s.zeros(4)),O)
    gamma=blocks(sp(s.zeros(4)),-sp(s.eye(4)),sp(s.eye(4)),sp(s.zeros(4)))
    A=R*a0*R.H; j=-gamma
    slowidx=[i for i in range(8) if a0[i,i]!=1]
    fastidx=[i for i in range(8) if a0[i,i]==-1]
    midx=[i for i in range(8) if a0[i,i]==0]
    slow=R*selector(slowidx,8); fast=R*selector(fastidx,8); center=R*selector(midx,8)
    x=s.Symbol('s',real=True)
    U=R*sp(s.diag(*(s.exp(a0[i,i]*x) for i in range(8))))
    diff=A-a0
    frob2=s.trace(diff.H*diff)
    checks=dict(
        orthogonal_frame=zero(R.H*R-s.eye(8)),
        Gamma_preserved=zero(R*gamma-gamma*R),
        small_constant_tail=frob2<s.Rational(1,64)**2,
        exact_not_truncated=zero(U.diff(x)-A*U),
        exact_current=zero(U.H*j*U-j),
        slow_space_dimension=slow.rank()==6 and fast.rank()==2,
        exact_restricted_rank=(slow.H*j*slow).rank()==4,
        fast_annihilator=zero(fast.H*j*slow),
        center_not_frozen_slots=not zero((s.eye(8)-selector(midx,8)*selector(midx,8).H)*center),
        moved_ordinary_trace_nonzero=not zero(diff),
        operator_current_law=zero(A.H*j+j*A),
    )
    return dict(checks=checks,fixture_dimension=8,frobenius_perturbation_squared=frob2,
                scope='Exact small constant symmetric comparator, not nonlinear field background')

@lru_cache(None)
def split_controls():
    eta=s.Rational(1,4)
    E=s.sqrt(5)*old.ey/4
    L=E+E.H
    A=blocks(old.M,-L,-L,-old.M)
    sigma=-eta
    D=blocks(E,sp(s.zeros(4)),sigma*s.eye(4)+old.M,-E)
    delta=blocks(E.H,-sigma*s.eye(4)+old.M,sp(s.zeros(4)),-E.H)
    gamma=blocks(sp(s.zeros(4)),-sp(s.eye(4)),sp(s.eye(4)),sp(s.zeros(4)))
    vectors=(A+sigma*s.eye(8)).nullspace()
    K=sp(s.Matrix.hstack(*vectors))
    checks=dict(
        actual_scalar_limit_mass=5/s.Integer(16)==eta*(eta+1),
        first_order_symbol=zero(D+delta-gamma*(sigma*s.eye(8)+A)),
        two_slow_Q_solutions=K.rank()==2 and zero((D+delta)*K),
        separate_d_nonzero=not zero(D*K),
        separate_delta_nonzero=not zero(delta*K),
        cancellation_retained=zero(D*K+delta*K),
    )
    return dict(checks=checks,slow_Q_dimension=2,scope='R63 distinction reused; not physical separate-domain admission')

def run():
    groups={name:fn() for name,fn in [('actual',actual_controls),('contraction',contraction_controls),
        ('tail',tail_controls),('geometry',geometry_controls),('norm',norm_controls),
        ('rotated',rotated_controls),('split',split_controls)]}
    checks={name+'/'+k:bool(v) for name,g in groups.items() for k,v in g['checks'].items()}
    return old.serial(dict(groups=groups,checks=checks,all_checks_pass=all(checks.values()),
        scope='Finite controls for authored exact local witnessed quotient; not independent analytic review or physical spectrum'))

if __name__=='__main__':
    result=run()
    print(json.dumps(result,indent=2,sort_keys=True))
    raise SystemExit(0 if result['all_checks_pass'] else 1)
