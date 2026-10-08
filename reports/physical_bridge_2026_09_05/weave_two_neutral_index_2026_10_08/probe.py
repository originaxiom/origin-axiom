"""Full two-spin-field Hessian, exact complex and scoped bosonic index."""
from collections import Counter
from functools import lru_cache
import importlib.util
import json
from pathlib import Path
import sympy as s

Q=s.Rational
path=Path(__file__).resolve().parent.parent/'weave_magnetic_index_2026_10_08/probe.py'
spec=importlib.util.spec_from_file_location('two_neutral_old_index',path)
old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)
neutral=old.old
magnetic=neutral.old
comm=magnetic.comm
zero=magnetic.zero
norm=neutral.norm

def line_index(beta):
    return 2*old.index(1-beta)-old.index(-beta)-old.index(2-beta)

def charge_indices(n):
    out=Counter()
    for (q,m),mult in old.weights().items():
        out[q]+=mult*line_index(m+2*n*q)
    return dict(sorted(out.items()))

def positive_bounds(n):
    return {str(q):i for q,i in charge_indices(n).items() if n*q>0 and i>0}

def blocks(j,k,h):
    out=[]
    for m in range(-j,j+1):
        if (m-h)%2==0:
            out.append({'kind':'pair' if m<j else 'top','m':m,
                'd':k+Q(m+1-h,2),'b2':Q((j-m)*(j+m+1),2),
                'count':2 if m<j else 1})
    if (j+h)%2:
        out.append({'kind':'bottom','m':-j,'d':k-Q(j+h,2),
                    'b2':s.Integer(0),'count':1})
    return out

def populations():
    ww=old.weights()
    even=sum(mult for (q,m),mult in ww.items() if m%2==0)
    odd=sum(mult for (q,m),mult in ww.items() if m%2)
    return {'physical_C1':even+2*odd,'auxiliary_C3':even,
            'h0':sum(mult*sum(row['count'] for row in blocks(j,0,0))
                     for (q,j),mult in neutral.modules().items()),
            'h1':sum(mult*sum(row['count'] for row in blocks(j,0,1))
                     for (q,j),mult in neutral.modules().items()),
            'total':2*(even+odd)}

@lru_cache(None)
def quadratic():
    t,n,h=s.symbols('t n h',real=True)
    om=s.Integer(4);unit=neutral.unit
    e=unit(0,1);hh=comm(e,e.T);z=s.diag(1,1,-2)
    q=e+(2+s.I)*z
    r=h*(3-2*s.I)*z
    ax=unit(0,2)+unit(2,0);ay=-s.I*unit(0,2)+s.I*unit(2,0)
    a=ax+s.I*ay
    u=unit(1,2)+s.I*unit(2,1);v=unit(2,0)+2*s.I*unit(0,1)
    du=unit(0,0)+2*s.I*unit(1,2);dv=unit(0,1)-s.I*unit(2,1)
    f1=s.diag(1,0,-1)+e+e.T
    f2=-s.I*comm(ax,ay);f0=-om**2*hh/4-n*om**2*z
    moment=f0+t*f1+t*t*f2+om*(comm(q+t*u,(q+t*u).adjoint())
                            +comm(r+t*v,(r+t*v).adjoint()))
    fq=t*(du+s.I*comm(q,a))-s.I*t*t*comm(a,u)
    fr=t*(dv+s.I*comm(r,a))-s.I*t*t*comm(a,v)
    fc=comm(q+t*u,r+t*v)
    exact=s.expand((norm(fq)+norm(fr))/om+2*norm(fc)+s.trace(moment*moment)/(2*om**2))
    m0=-n*om**2*z
    m1=f1+om*(comm(u,q.adjoint())+comm(q,u.adjoint())
                 +comm(v,r.adjoint())+comm(r,v.adjoint()))
    m2=f2+om*(comm(u,u.adjoint())+comm(v,v.adjoint()))
    squares=(norm(du+s.I*comm(q,a))+norm(dv+s.I*comm(r,a)))/om+2*norm(comm(q,v)-comm(r,u))+s.trace(m1*m1)/(2*om**2)
    expected=s.expand(squares+s.trace(m0*m2)/om**2)
    wrong=(norm(du+s.I*comm(q,a))+norm(dv))/om+2*norm(comm(q,v))+s.trace(m1*m1)/(2*om**2)+s.trace(m0*m2)/om**2
    return {'n':n,'h':h,'actual':exact.coeff(t,2),'expected':expected,
            'squares':s.expand(squares),'wrong':s.expand(wrong),
            'moment0':moment.subs(t,0),'m0':m0}

def complex_matrices(q,r,p):
    size=q.rows;ident=s.eye(size);zz=s.zeros(size)
    d0=s.sqrt(2)*s.Matrix.vstack(p*ident,-s.I*q,-s.I*r)
    d1=s.Matrix.vstack(s.Matrix.hstack(s.I*q,p*ident,zz),
        s.Matrix.hstack(s.I*r,zz,p*ident),s.Matrix.hstack(zz,-r,q))
    d2=s.Matrix.hstack(r,-q,p*ident)
    return d0,d1,d2

@lru_cache(None)
def complex_checks():
    unit=neutral.unit;ident=s.eye(3)
    q=unit(0,1)+(2+s.I)*ident;r=(3-2*s.I)*ident
    p=s.Integer(2)+3*s.I;om=s.Integer(4)
    d0,d1,d2=complex_matrices(q,r,p)
    h0=om**2*ident
    h1=s.diag(ident/2,om*ident,om*ident)
    h2=s.diag(ident/om,ident/om,2*ident)
    h3=2*ident/om**2
    a0=h0.inv()*d0.adjoint()*h1
    a2=h2.inv()*d2.adjoint()*h3
    # Dz symbol is -conjugate(Dbar); C1 metric is the physical one.
    ga=s.Matrix.hstack(-s.conjugate(p)*ident,-2*s.I*om*q.adjoint(),
                        -2*s.I*om*r.adjoint())
    hodge=s.Matrix.vstack(s.Matrix.hstack(a0,s.zeros(3)),
                         s.Matrix.hstack(d1,a2))
    hs=s.diag(h1,h3);ht=s.diag(h0,h2)
    square=hs.inv()*hodge.adjoint()*ht*hodge
    badq=unit(0,1);badr=unit(1,2)
    b0,b1,b2=complex_matrices(badq,badr,p)
    z0,z1,z2=complex_matrices(s.zeros(3),s.zeros(3),s.Integer(0))
    return {'complex':zero(d1*d0) and zero(d2*d1),
            'noncommuting_fails':not zero(b1*b0) and not zero(b2*b1),
            'gauge_adjoint':zero(a0+ga/(s.sqrt(2)*om**2)),
            'hodge_cross':zero(square[:9,9:]) and zero(square[9:,:9]),
            'physical_block':zero(square[:9,:9]-(d0*a0+h1.inv()*d1.adjoint()*h2*d1)),
            'aux_injective':a2[:3,:].rank()==3 and a2.rank()==3,
            'aux_zero_control':z2.adjoint().rank()==0,
            'wrong_C0_factor_fails':not zero(a0+ga/(2*om**2))}

def shifted_coordinates(j,m,k):
    y=s.symbols('y',positive=True)
    v,alpha=s.Function('v')(y),s.Function('alpha')(y)
    sigma=alpha/(s.sqrt(2)*y**s.Rational(3,2))
    ell=s.sqrt((j-m)*(j+m+1));d=k+Q(m,2);b=ell/s.sqrt(2)
    p2=s.I*(s.diff(v,y)+(m+2*k)*v/(2*y))-ell*alpha/(s.sqrt(2)*y)
    tt=ell*v/(2*s.sqrt(y))+s.I*(y*y*s.diff(sigma,y)+(3-m-2*k)*y*sigma/2)
    return (s.simplify(y*p2-(s.I*(y*s.diff(v,y)+d*v)-b*alpha)),
            s.simplify(s.sqrt(2*y)*tt-(b*v+s.I*(y*s.diff(alpha,y)-d*alpha))),
            s.simplify(2*y**3*sigma*sigma-alpha*alpha))

def flavor():
    unit=neutral.unit;q=unit(0,1)+s.I*unit(2,0)
    r=unit(1,2)+2*unit(2,1)
    qp,rp=Q(3,5)*q+Q(4,5)*r,-Q(4,5)*q+Q(3,5)*r
    c,d=s.symbols('c d')
    return (s.simplify(norm(qp)+norm(rp)-norm(q)-norm(r)),
        zero(comm(qp,qp.adjoint())+comm(rp,rp.adjoint())-comm(q,q.adjoint())-comm(r,r.adjoint())),
        zero(comm(qp,rp)-comm(q,r)),
        s.Matrix([[Q(1,2),c],[0,d]]).det())

@lru_cache(None)
def run():
    facts={};qq=quadratic();cc=complex_checks()
    facts['full_two_field_action_expansion']=s.expand(qq['actual']-qq['expected'])==0
    facts['dropping_new_R_terms_changes_the_answer']=s.expand((qq['actual']-qq['wrong']).subs(qq['h'],1))!=0
    facts['R_zero_recovers_pinned_full_quadratic']=s.expand(qq['actual'].subs(qq['h'],0)-neutral.quadratic_expansion()['actual'])==0
    facts['zero_flux_keeps_all_positive_residual_squares']=s.expand(qq['actual'].subs(qq['n'],0)-qq['squares'])==0
    facts['both_field_moment_remains_parallel']=zero(qq['moment0']-qq['m0']) and old.matrix_controls()['two_field_residuals']
    facts['actual_three_maps_form_a_complex']=cc['complex']
    facts['noncommuting_background_breaks_both_compositions']=cc['noncommuting_fails']
    facts['declared_metric_gives_actual_gauge_adjoint']=cc['gauge_adjoint'] and cc['wrong_C0_factor_fails']
    facts['Hodge_norm_has_no_hidden_auxiliary_cross']=cc['hodge_cross'] and cc['physical_block']
    facts['nonzero_R_removes_auxiliary_kernel_pointwise']=cc['aux_injective']
    facts['auxiliary_removal_is_not_assumed_at_R_zero']=cc['aux_zero_control']
    fl=flavor()
    facts['full_flavor_symmetry_not_only_field_norms']=fl[0]==0 and fl[1] and fl[2]
    facts['nonproportional_pair_cannot_be_rotated_away']=fl[3]==s.Symbol('d')/2

    ki=s.symbols('k',integer=True);xi,t=s.symbols('xi t',real=True)
    checks=[];drifts=[];coords=[];counter=0
    for h in (0,1):
        for j in range(5):
            for row in blocks(j,ki,h):
                drifts.append(row['d'])
                if row['kind']=='pair':
                    d=row['d'];b=t*s.sqrt(row['b2'])
                    mat=s.Matrix([[s.I*xi+d,b],[-b,-s.I*xi+d]])
                    checks.append(zero(s.simplify(mat.adjoint()*mat-(xi*xi+d*d+t*t*row['b2'])*s.eye(2))))
                    counter+=1
                    if h==1:coords.append(shifted_coordinates(j,row['m'],ki)==(0,0,0))
    facts['both_shifted_full_homotopy_blocks']=all(checks) and counter==20
    facts['every_extreme_retained_and_half_integral']=all(s.simplify(d-Q(1,2)).is_integer for d in drifts)
    facts['second_block_derived_from_actual_metrics']=all(coords) and len(coords)==10
    facts['both_shift_channel_counts_complete']=all(sum(r['count'] for r in blocks(j,0,h))==2*j+1 for h in (0,1) for j in range(5))
    facts['full496_slots_keep136_auxiliary_separate']=populations()=={'physical_C1':360,'auxiliary_C3':136,'h0':248,'h1':248,'total':496}
    facts['zero_endpoint_and_signed_parity']=line_index(0)==0 and all(line_index(b)==-s.sign(b)*(-1 if b%2 else 1) for b in range(-80,81) if b)
    ww=old.weights()
    facts['full248_population_retained']=sum(ww.values())==248
    facts['all_integer_beta_bound_including_first_endpoint']=all(m+2*abs(q)>=0 and m+4*abs(q)>0 for q,m in ww if q)
    expected={1:-6,2:6,3:4,4:-3,5:-6,6:-1}
    facts['higher_flux_complete_index_profile']=all({q:charge_indices(n)[q] for q in range(1,7)}==expected for n in (2,3,5))
    first=dict(expected);first[1]=0
    facts['first_flux_zero_endpoint_changes_charge_one']=({q:charge_indices(1)[q] for q in range(1,7)}==first)
    facts['opposite_flux_and_zero_flux_controls']=all(charge_indices(-n)=={q:-i for q,i in charge_indices(n).items()} for n in (1,2,3)) and all(i==0 for i in charge_indices(0).values())
    facts['positive_index_bound_is_ten_not_total_signed_index']=all(positive_bounds(n)=={'2':6,'3':4} for n in (1,2,3,5)) and all(sum(positive_bounds(-n).values())==10 for n in (1,2,3,5))
    facts['R_zero_stronger_bound_is_preserved']=sum(old.unstable_bounds(2).values())==50 and magnetic.variation()['mass2']==-magnetic.variation()['n']*magnetic.variation()['q']
    facts['first_flux_essential_instability_control']=neutral.spectrum(1)['scalar_bottom']=='-7/4' and neutral.spectrum(2)['scalar_bottom']=='1/4'
    facts['finite_neutral_terms_decay_on_same_end']=old.run()['facts']['every_fixed_finite_neutral_amplitude_decays']
    facts['physical_negative_path_margin']=Q(1,4)**2-2*(1-Q(1,4))**2<0
    facts={k:bool(v) for k,v in facts.items()}
    return {'facts':facts,'predicates_passed':sum(facts.values()),
        'line_index_table':[{'beta':b,'index':line_index(b)} for b in range(-24,25)],
        'index_profiles':{str(n):{str(q):i for q,i in charge_indices(n).items()} for n in range(-3,4)},
        'positive_bounds':{str(n):positive_bounds(n) for n in range(-3,4)},
        'hodge_populations':populations(),
        'auxiliary_is_physical_field':False,'physical_Weyl_dictionary_derived':False,
        'full_Morse_count_computed':False,'stable_nonzero_flux_phase_achieved':False,
        'all_stationary_phases_excluded':False,'genesis_selection_derived':False,
        'nonauthor_acceptance':False,'physical_goal_achieved':False,
        'analytic_grade':'Authored global complex/domain proof; finite checks are not outside acceptance'}

if __name__=='__main__':
    result=run();print(json.dumps(result,indent=2,sort_keys=True))
    raise SystemExit(0 if all(result['facts'].values()) else 1)
