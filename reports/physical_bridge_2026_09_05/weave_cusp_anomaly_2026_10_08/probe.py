"""Physical cusp end signature, gauge admission and scoped anomaly persistence."""
from collections import Counter, defaultdict
from functools import lru_cache
import importlib.util
import json
from pathlib import Path
import sympy as s

path=Path(__file__).resolve().parent.parent/'weave_physical_mass_2026_10_08/probe.py'
spec=importlib.util.spec_from_file_location('cusp_anomaly_mass',path)
physical=importlib.util.module_from_spec(spec);spec.loader.exec_module(physical)
old=physical.old
Q=s.Rational
zero=lambda a:all(s.simplify(v)==0 for v in a)

def end_blocks(j,k,h,tau=1,adjoint=True):
    out=[];J=s.diag(1,-1)
    for row in old.blocks(j,k,h):
        if row['kind']=='pair':
            b=tau*s.sqrt(row['b2']);d=row['d']
            C=s.Matrix([[d,b],[b,-d]])
            if h==1 and adjoint:C=-J*C*J
        else:
            mu=(-1 if row['kind']=='top' else 1)*row['d']
            if h==1 and adjoint:mu=-mu
            C=s.Matrix([[mu]])
        out.append(C)
    return out

def module_signature(j,k,adjoint=True):
    value=0
    for h in (0,1):
        for C in end_blocks(j,k,h,adjoint=adjoint):
            if C.rows==1:value+=s.sign(C[0,0])
            else:
                assert C.trace()==0 and C.det()<0
    return int(value)

def module_closed(j,k):
    a=Q(j+1,2) if j%2==0 else Q(j,2)
    return (-1 if j%2==0 else 1)*(s.sign(k+a)+s.sign(k-a))/2

@lru_cache(None)
def modules():
    weights=defaultdict(Counter)
    for (a,b,w,q,m),mult in physical.full_weights().items():
        weights[a,b,w,q][m]+=mult
    out={}
    for key,pop in weights.items():
        assert all(pop[m]==pop[-m] for m in pop)
        for j in range(max(pop)+1):
            mult=pop[j]-pop[j+1]
            assert mult>=0
            if mult:out[key+(j,)]=mult
    return out

@lru_cache(None)
def gauge_indices(n):
    out=Counter()
    for (a,b,w,q,j),mult in modules().items():
        out[a,b,w,q]+=Q(mult*module_signature(j,n*q),2)
    return dict(out)

def profile(n):
    ww=gauge_indices(n);out={}
    for q,rr in physical.REP.items():
        vals={ww[a,b,w,q] for a,b,w in rr}
        assert len(vals)==1
        out[str(q)]=int(vals.pop())
    return out

def anomaly(n):
    out=[s.Integer(0)]*5
    for (a,b,w,q),idx in gauge_indices(n).items():
        terms=[Q((a+2*b)**3,-6),Q(a*a*q,4),Q(w*w*q,4),q**3,q]
        out=[x+Q(1,2)*idx*y for x,y in zip(out,terms)]
    return [str(x) for x in out]

def line_end(a):
    return Q(s.sign(1-a),2) if a%2==0 else s.Integer(0)

@lru_cache(None)
def run():
    facts={}
    z,e,x=s.symbols('z e x')
    virt=s.exp(e*x)*(2*s.exp(z*x)-1-s.exp(2*z*x))*(1-z*x)
    expansion=s.series(virt,x,0,2).removeO().expand()
    facts['virtual_rank_and_two_form_zero']=expansion==0
    wrong=s.exp(e*x)*(s.exp(z*x)-1-s.exp(2*z*x))*(1-z*x)
    facts['missing_spin_field_changes_virtual_density']=s.series(wrong,x,0,2).removeO().expand()!=0
    facts['global_line_equals_bulk_plus_end']=all(
        old.old.index(a)==Q(a-1,2)+line_end(a) for a in range(-41,42))
    facts['angular_parity_and_log_endpoints_retained']=(
        line_end(0)==Q(1,2) and line_end(2)==Q(-1,2)
        and all(line_end(a)==0 for a in range(-41,42,2)))
    facts['bulk_only_misses_actual_index']=old.old.index(0)!=Q(-1,2)
    beta=s.symbols('beta')
    facts['four_slot_bulk_density_cancels']=s.expand(
        2*(-beta)/2-(-beta-1)/2-(1-beta)/2)==0
    facts['line_end_combination_is_physical_index']=all(
        2*line_end(1-b)-line_end(-b)-line_end(2-b)==old.line_index(b)
        for b in range(-41,42))
    d,b,xi,t=s.symbols('d b xi t',real=True);J=s.diag(1,-1)
    B=s.Matrix([[s.I*xi+d,t*b],[-t*b,-s.I*xi+d]])
    C=s.Matrix([[d,t*b],[t*b,-d]])
    facts['radial_factor_is_actual_hermitian_matrix']=zero(J*B-(s.I*xi*s.eye(2)+C)) and C==C.adjoint()
    facts['paired_masses_are_opposite_for_all_amplitudes']=(
        zero(C*C-(d*d+t*t*b*b)*s.eye(2)) and C.trace()==0)
    facts['adjoint_reverses_end_orientation']=zero(-J*B.adjoint()-(s.I*xi*s.eye(2)-J*C*J))
    ki=s.symbols('k',integer=True)
    facts['all_actual_drifts_nonzero_half_integral']=all(
        s.simplify(row['d']-Q(1,2)).is_integer for h in (0,1)
        for j in range(5) for row in old.blocks(j,ki,h))
    facts['two_shifts_keep_every_slot']=all(
        sum(C.rows for h in (0,1) for C in end_blocks(j,2,h))==2*(2*j+1)
        for j in range(5))
    facts['every_module_signature_equals_global_index']=all(
        Q(module_signature(j,k),2)==sum(old.line_index(m+2*k) for m in range(-j,j+1))
        for j in range(5) for k in range(-9,10))
    facts['extreme_closed_formula_has_both_sides']=all(
        Q(module_signature(j,k),2)==module_closed(j,k)
        for j in range(5) for k in range(-9,10))
    facts['wrong_second_orientation_fails']=module_signature(0,1,False)!=module_signature(0,1)
    facts['endpoint_not_uniform_higher_flux']=(module_signature(2,1)==0 and module_signature(2,2)==-2)
    facts['full248_and496_population']=sum(mult*(2*j+1) for (*_,j),mult in modules().items())==248 and sum(
        mult*sum(C.rows for h in (0,1) for C in end_blocks(j,2*q,h))
        for (a,b,w,q,j),mult in modules().items())==496
    facts['full_gauge_weight_index_from_actual_end']=all(
        gauge_indices(n)==physical.gauge_weight_indices(n) for n in (-3,-2,-1,0,1,2,3))
    facts['all_five_end_anomalies_match_physical']=all(
        anomaly(n)==[str(v) for v in physical.anomaly(n)] for n in (-3,-2,-1,0,1,2,3))
    facts['anomaly_is_not_its_own_compensation']=anomaly(2)!=['0']*5
    facts['zero_and_opposite_flux_controls']=profile(0)=={str(q):0 for q in range(1,7)} and all(
        profile(-n)=={q:-v for q,v in profile(n).items()} for n in (1,2,3))
    # Classical scalar gauge graph cutoffs, not a determinant regulator.
    u,T0,ell=s.symbols('u T0 ell',positive=True)
    cut=1-3*u*u+2*u**3
    lost=ell*s.exp(-T0)*(s.integrate(s.exp(-u)*(1-cut)**2,(u,0,1))+s.exp(-1))
    grad=ell*s.exp(-T0)*s.integrate(s.exp(-u)*s.diff(cut,u)**2,(u,0,1))
    facts['gauge_cutoff_graph_errors_vanish']=s.limit(lost,T0,s.oo)==0 and s.limit(grad,T0,s.oo)==0
    facts['gauge_cutoff_not_an_assumed_zero_error']=lost!=0 and grad!=0 and cut.subs(u,0)==1 and cut.subs(u,1)==0
    area,g6=s.symbols('area g6',positive=True)
    norm_factor=1/s.sqrt(area);g4=g6/s.sqrt(area)
    facts['constant_gauge_norm_and_coupling']=s.simplify(area*norm_factor**2)==1 and s.simplify(1/g4**2-area/g6**2)==0
    # Escaping H1 bumps in the quadratic-form domain, with smooth approximants.
    L,v,mu=s.symbols('L v mu',positive=True)
    bump=s.sqrt(2/L)*s.sin(s.pi*v/L)
    bn=s.integrate(bump*bump,(v,0,L));en=s.integrate(s.diff(bump,v)**2+mu**2*bump**2,(v,0,L))
    facts['escaping_bump_norm_and_bounded_energy']=s.simplify(bn-1)==0 and s.simplify(en-mu**2-s.pi**2/L**2)==0
    count,heat=s.symbols('count heat',positive=True)
    facts['positive_heat_trace_bound_diverges']=s.limit(count*s.exp(-heat*(mu**2+s.pi**2/L**2)),count,s.oo)==s.oo
    # Finite illustration only: rank can change, net source-target index cannot.
    pairing=s.Matrix([[1,2,0],[0,0,0]])
    zpair=s.zeros(2,3)
    facts['pairing_control_changes_kernel_not_index']=(pairing.rank()!=zpair.rank() and
        all((A.cols-A.rank())-(A.rows-A.rank())==1 for A in (pairing,zpair)))
    facts['end_sign_change_requires_zero_crossing']=s.sign(-1)==-1 and s.sign(1)==1 and s.sign(0)==0
    facts={k:bool(v) for k,v in facts.items()}
    return {'facts':facts,'predicates_passed':sum(facts.values()),
        'end_index_profiles':{str(n):profile(n) for n in range(-3,4)},
        'end_anomaly_vectors':{str(n):anomaly(n) for n in range(-3,4)},
        'module_end_indices':[[j,k,int(Q(module_signature(j,k),2))] for j in range(5) for k in range(-4,5)],
        'physical_index_located_in_end':True,
        'regulated_parent_determinant_computed':False,'anomaly_compensation_derived':False,
        'stable_chiral_vacuum_derived':False,'genesis_selection_derived':False,
        'nonauthor_acceptance':False,'physical_goal_achieved':False}

if __name__=='__main__':
    result=run();print(json.dumps(result,indent=2,sort_keys=True))
    raise SystemExit(0 if all(result['facts'].values()) else 1)
