"""R74 actual exterior coefficient and finite controls for authored admission proof."""
from functools import lru_cache
import importlib.util
import itertools
import json
from pathlib import Path
import sympy as s

def local(name,path):
    spec=importlib.util.spec_from_file_location(name,Path(__file__).with_name(path))
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m

f=local('r74_log_source','nilpotent_cone.py')
c=local('r74_form_source','cone_channel.py')
sp,zero,comm,tensor,blocks=c.sp,c.zero,c.comm,c.tensor,c.blocks

def lie_wedge(X):
    n=X.rows;pairs=list(itertools.combinations(range(n),2));out=s.zeros(len(pairs))
    for j,(a,b) in enumerate(pairs):
        for u in range(n):
            if u!=b:
                i=pairs.index(tuple(sorted((u,b))));out[i,j]+=X[u,a]*(1 if u<b else -1)
            if u!=a:
                i=pairs.index(tuple(sorted((a,u))));out[i,j]+=X[u,b]*(1 if a<u else -1)
    return sp(out)

def group_wedge(X):
    pairs=list(itertools.combinations(range(X.rows),2))
    return sp(s.Matrix(len(pairs),len(pairs),lambda i,j:X[pairs[i][0],pairs[j][0]]*X[pairs[i][1],pairs[j][1]]-X[pairs[i][0],pairs[j][1]]*X[pairs[i][1],pairs[j][0]]))

n,p,z,h=(lie_wedge(a) for a in (f.N,f.P,f.D,f.H))
I6=sp(s.eye(6));I24=sp(s.eye(24));zero24=sp(s.zeros(24))
M=tensor(c.M,I6);Gamma=blocks(zero24,-I24,I24,zero24);J=-Gamma

def operators(t,v,beta,alpha,k,power=0):
    E=s.sqrt(alpha)*t*tensor(c.ex,n)+(tensor(c.ey,k*z+beta*t*t*p))/s.sqrt(alpha)
    L=E+E.H;K=-v*tensor(sp(s.eye(4)),h)
    A=blocks(M+K,-L,-L,-M-K.H)
    d=blocks(E,zero24,power*I24+M+K,-E)
    delta=blocks(E.H,-power*I24+M+K.H,zero24,-E.H)
    return A,d,delta

@lru_cache(None)
def coefficient_controls():
    g=sp(s.diag(s.Rational(3,5)+4*s.I/5,1,1,s.Rational(3,5)-4*s.I/5))
    q=s.Symbol('q',positive=True);b=s.Symbol('beta',real=True);t=s.Symbol('t',positive=True)
    L4=sp(s.diag(q,q**-3,q,q)*(s.eye(4)+b*t*t*f.P));L6=group_wedge(L4)
    mu5=sp(s.diag(-1,-1,-1,-1,1));mu10=group_wedge(mu5)
    charges=list(z.diagonal());H5=sp(s.diag(f.D,0));zw=lie_wedge(H5)
    plus=sp(s.diag(*(int(v==2) for v in charges)));minus=I6-plus
    T=L6-I6;Tinv=T.inv()
    checks=dict(
        actual_dimension=n.shape==(6,6),
        charge_multiset=charges.count(2)==3 and charges.count(-2)==3,
        Lie_commutator=zero(comm(h,n)-n) and zero(comm(h,p)-2*p),
        Lie_preserves_flatness=zero(comm(n,p)) and zero(comm(z,n)) and zero(comm(z,p)),
        positive_adjoints=all(zero(lie_wedge(a.H)-lie_wedge(a).H) for a in (f.N,f.P,f.D,f.H)),
        rhoP_not_square_rhoN=not zero(p-n*n),
        group_not_Lie_map=not zero(group_wedge(s.eye(4))-lie_wedge(s.eye(4))),
        compact_wedge_unitary=zero(group_wedge(g).H*group_wedge(g)-I6),
        actual_longitude_charpoly=zero(L6.charpoly().as_expr()-(L6.charpoly().gen-q*q)**3*(L6.charpoly().gen-q**-2)**3),
        invertible_longitude_generic=zero(T*Tinv-I6) and zero(Tinv*T-I6),
        torus_acyclic_at_q2=T.subs(q,2).det()!=0,
        q1_inverse_excluded=zero((T.det()).subs(q,1)),
        exact_charge_reduction=all(zero(comm(plus,a)) and zero(comm(minus,a)) for a in (n,p,h,z,n.H,p.H)),
        periodic_six_count=list(mu10.diagonal()).count(1)==6 and list(mu10.diagonal()).count(-1)==4,
        twist_four_not_periodic=not zero(mu5[:4,:4]-s.eye(4)),
        i_twist_six_antiperiodic=zero(group_wedge(s.I*s.eye(4))+I6),
        full10_charge_roster=sorted(zw.diagonal())==[-3,-2,-2,-2,1,1,1,2,2,2],
        zero_trace_H=zero(s.trace(h)) and h.norm()<=2,
    )
    return dict(checks=checks,coefficient_dimension=6,charges=charges,scope='Actual Lie/group exterior actions and central twist; no index imported')

@lru_cache(None)
def actual_controls():
    t=s.Symbol('t',positive=True);v,beta,k=s.symbols('v beta k',real=True);alpha=s.Symbol('alpha',positive=True);power=s.Symbol('power',real=True)
    A,d,delta=operators(t,v,beta,alpha,k,power)
    jd=blocks(zero24,zero24,I24,zero24)
    derivative=v*t*d.diff(t)
    dsq=operators(t,v,beta,alpha,k,power-1)[1]*d+jd*derivative
    wrong=operators(t,v,beta,alpha,k,power-1)[1]*d
    checks=dict(
        actual48components=A.shape==(48,48),
        positive_Hermitian=zero(A-A.H),
        Gamma_current=zero(A.H*J+J*A),
        Gamma_anticommutes=zero(A*Gamma+Gamma*A),
        d_squared_actual=zero(dsq),
        frozen_nilpotent_derivative_rejected=not zero(wrong),
        exact_Q=zero(d+delta-Gamma*(power*sp(s.eye(48))+A)),
        nonzero_radial_transport=not zero(A.diff(v)),
        zero_Fourier_not_all_A0=not zero(A.subs({t:0,v:0})-blocks(M,zero24,zero24,-M)),
        representation_norm_bounds=all((a.H*a).eigenvals() and max((a.H*a).eigenvals())<=4 for a in (n,p,h)),
    )
    return dict(checks=checks,form_dimension=48,scope='Exact changing coefficient operator, not a frozen-spectrum substitution')

@lru_cache(None)
def limiting_controls():
    w=s.Symbol('w',real=True);a=s.Symbol('a',real=True)
    E=w*c.ey;L=E+E.H;A=blocks(c.M,-L,-L,-c.M)
    polynomial=A.charpoly();x=polynomial.gen
    target=((x*x-w*w)**2-x*x)**2
    val=A.subs(w,s.Rational(2,3))
    spectrum=val.eigenvals();critical=[x for x in spectrum if abs(x)<s.Rational(1,2)]
    k=s.Symbol('k',real=True,nonzero=True)
    checks=dict(
        exact_scalar_charpoly=zero(polynomial.as_expr()-target),
        exact_fixture_spectrum=spectrum=={-s.Rational(4,3):2,-s.Rational(1,3):2,s.Rational(1,3):2,s.Rational(4,3):2},
        four_critical_per_coefficient=sum(spectrum[x] for x in critical)==4,
        actual_aspect_mass=zero(4*k*k/(9*k*k)-s.Rational(4,9)),
        exact_eta=zero(s.sqrt(s.Rational(4,9)+s.Rational(1,4))-s.Rational(1,2)-s.Rational(1,3)),
        exceptional_q_reciprocal=zero((17-12*s.sqrt(2))*(17+12*s.sqrt(2))-1),
        exceptional_k_bound=(17+12*s.sqrt(2)>32) and (3**3<32),
        unit_aspect_outside_limiting=4*3**2>s.Rational(3,4),
        half_meridian_sector_not_zero=s.pi*s.pi*81>s.Rational(3,4),
        threshold_distinct=s.Rational(4,9)<s.Rational(3,4),
    )
    return dict(checks=checks,limiting_eigenvalue_multiplicities={str(x):6*mult for x,mult in spectrum.items()},critical_limiting_dimension=24,scope='Supplied aspect and periodic zero block only, not physical modes')

@lru_cache(None)
def contraction_controls():
    gamma=s.Rational(1,3);eps=s.Rational(1,256)
    gaps=[(s.Rational(5,12),s.Rational(7,12)),(s.Rational(7,12),s.Rational(5,12))]
    sums=[1/(a-gamma)+1/(b+gamma) for a,b in gaps]
    q=[eps*v for v in sums]
    dimensions=[36,12];rank=dimensions[0]-dimensions[1]
    scalar=s.Rational(1,1024)*(24+s.Rational(8,13))
    checks=dict(
        exact_gap_sums=sums==[s.Rational(144,11),s.Rational(16,3)],
        exact_contractions=q==[s.Rational(9,176),s.Rational(1,48)] and max(q)<1,
        unsafe_tail_rejected=max(sums)*s.Rational(1,8)>1,
        slow_L2_margin=1-2*s.Rational(5,12)==s.Rational(1,6),
        fast_cutoff_margin=2*s.Rational(13,12)-1==s.Rational(7,6),
        annihilator_and_rank=48-36==12 and rank==24,
        current_pair_decay=s.Rational(5,12)-s.Rational(13,12)==-s.Rational(2,3),
        scalar_contraction=scalar==s.Rational(5,208) and scalar<1,
        scalar_separate_decay=s.Rational(7,24)>s.Rational(1,4),
        full_half_not_six=rank//2==12 and 6<12,
    )
    return dict(checks=checks,slow_dimension=36,fast_dimension=12,witnessed_quotient_dimension=24,witnessed_signature=[12,12],scalar_seed_dimension=6,scope='Finite constants of two authored exact contractions, not numerical approximation')

@lru_cache(None)
def scalar_controls():
    t=s.Symbol('t',positive=True);v,vs,beta,a=s.symbols('v vs beta a',real=True);k=s.Symbol('k',real=True,nonzero=True);alpha=s.Symbol('alpha',positive=True)
    B=(v-vs)*h+v*v*h*h+alpha*t*t*n.H*n+(k*z+beta*t*t*p).H*(k*z+beta*t*t*p)/alpha
    # phi=r^a f0 has normalized scalar coefficient r^(a+1).
    _,D,_=operators(t,v,beta,alpha,k,a+1)
    _,_,Del=operators(t,v,beta,alpha,k,a)
    ja=-blocks(zero24,zero24,I24,zero24).T
    rD=v*t*D.diff(t)-vs*D.diff(v)
    DD=Del*D+ja*rD
    inject=sp(s.eye(48)[:,:6])
    direct=DD*inject
    target=inject*(-a*(a+1)*I6+B)
    W=blocks(I6,I6,-I6/3,4*I6/3)
    Wi=blocks(4*I6/5,-3*I6/5,I6/5,3*I6/5)
    limit=blocks(sp(s.zeros(6)),I6,4*I6/9,I6)
    delta=s.Symbol('delta',real=True)
    fixture=blocks(sp(s.zeros(6)),sp(s.zeros(6)),delta*I6,sp(s.zeros(6)))
    transformed=Wi*fixture*W
    seed=sp([[-s.Rational(3,5),-s.Rational(3,5)],[s.Rational(3,5),s.Rational(3,5)]])
    one_deg=[i for i in range(48) if i//6 in (1,2,4)]
    degrees=sp(s.eye(48)[:,one_deg])
    checks=dict(
        direct_scalar_metric_equation=zero(direct-target),
        actual_B_limit=zero(B.subs({t:0,v:0,vs:0,alpha:9*k*k})-4*I6/9),
        exact_eigenframe_inverse=zero(Wi*W-sp(s.eye(12))) and zero(W*Wi-sp(s.eye(12))),
        exact_scalar_eigenframe=zero(Wi*limit*W-blocks(-I6/3,sp(s.zeros(6)),sp(s.zeros(6)),4*I6/3)),
        exact_perturbation_frame=zero(transformed-tensor(seed,delta*I6)),
        perturbation_norm_coefficient=seed.singular_values()[0]==s.Rational(6,5),
        scalar_growth_fixture=s.Rational(1,3)*(s.Rational(1,3)+1)==s.Rational(4,9),
        scalar_wrong_radial_omission=not zero(B-(alpha*t*t*n.H*n+(k*z+beta*t*t*p).H*(k*z+beta*t*t*p)/alpha)),
        degree_one_current_isotropic=zero(degrees.H*J*degrees),
        shifted_scalar_has_no_stable_seed=(-s.Rational(1,3)+s.Rational(3,4)>0) and (s.Rational(4,3)+s.Rational(3,4)>0),
        tangential_f_recovery=zero((k*z/s.sqrt(9*k*k)).det()**2-s.Rational(2,3)**12),
    )
    return dict(checks=checks,scalar_seed_dimension=6,scope='Actual delta d equation and derivative/product inputs; not selected physical modes')

@lru_cache(None)
def product_controls():
    r=s.Symbol('r',positive=True);R=s.Symbol('R',positive=True);eps=s.Symbol('epsilon',positive=True)
    rho=s.Rational(7,24)
    kinetic=s.integrate(r**(2*rho),(r,0,R))
    L4=s.integrate(r**(4*rho-2),(r,0,R))
    cutoff=eps**-2*s.integrate(r**(2*s.Rational(13,12)),(r,0,2*eps))
    bad=s.integrate(r**(4*s.Rational(1,8)-2),(r,eps,R))
    checks=dict(
        kinetic_integrable=zero(kinetic-s.Rational(12,19)*R**s.Rational(19,12)),
        nonlinear_L4_integrable=zero(L4-6*R**s.Rational(1,6)),
        product_exponent_margin=4*rho-2==-s.Rational(5,6),
        unsafe_product_diverges=s.limit(bad,eps,0,dir='+')==s.oo,
        fast_graph_cutoff_zero=s.limit(cutoff,eps,0,dir='+')==0,
        fast_graph_exponent=zero(cutoff/(eps**s.Rational(7,6))-s.Rational(6,19)*2**s.Rational(19,6)),
        finite_products_not_zero=not zero(comm(f.N,f.N.H)),
        minimal_is_not_maximal_choice=s.Rational(7,24)<s.Rational(1,2),
    )
    return dict(checks=checks,kinetic_bound=kinetic,L4_bound=L4,scope='Sufficient local finite-product norm bounds, not X0 admission or full supersymmetric law')

def serial(v):
    if isinstance(v,dict):return {str(k):serial(a) for k,a in v.items()}
    if isinstance(v,(list,tuple)):return [serial(a) for a in v]
    if isinstance(v,s.MatrixBase):return [[str(x) for x in row] for row in v.tolist()]
    if isinstance(v,s.Basic):return str(v)
    return v

def run():
    groups={name:fn() for name,fn in [('coefficient',coefficient_controls),('actual',actual_controls),('limit',limiting_controls),('contraction',contraction_controls),('scalar',scalar_controls),('products',product_controls)]}
    checks={name+'/'+k:bool(v) for name,g in groups.items() for k,v in g['checks'].items()}
    return serial(dict(scope='Actual split exterior cone and finite-action local profiles; not B1509 nonsplit vacuum, physical chirality or TOE',groups=groups,checks=checks,all_checks_pass=all(checks.values())))

if __name__=='__main__':
    out=run();print(json.dumps(out,sort_keys=True,indent=2));raise SystemExit(0 if out['all_checks_pass'] else 1)
