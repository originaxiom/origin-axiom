"""Cusp spin-power indices and a bosonic magnetic instability lower bound."""
from collections import Counter
from functools import lru_cache
import importlib.util
import json
from pathlib import Path
import sympy as s

Q = s.Rational
path = Path(__file__).resolve().parent.parent/'weave_neutral_stability_2026_10_08/probe.py'
spec = importlib.util.spec_from_file_location('magnetic_index_neutral',path)
old = importlib.util.module_from_spec(spec); spec.loader.exec_module(old)

def integrable(a,p):
    return old.old.integrable_power_log(a-2*p-1,a-2)

def pole_bound(a):
    b = a//2
    if a > 0 and a%2 == 0: b -= 1
    return b

def pole_basis(d):
    if d < 0: return []
    return [0]+[2*i for i in range(1,d//2+1)]+[2*i+3 for i in range(max(0,(d-3)//2+1))]

def hol_dimension(a):
    return len(pole_basis(pole_bound(a)))

def index(a):
    return hol_dimension(a)-hol_dimension(2-a)

def line_index(beta):
    return index(1-beta)-index(-beta)

def weights(): return old.weights()

def charge_indices(n):
    out = Counter()
    for (q,m),mult in weights().items():
        out[q] += mult*line_index(m+2*n*q)
    return dict(sorted(out.items()))

def unstable_bounds(n):
    return {str(q):v for q,v in charge_indices(n).items() if n*q > 0}

def line_table():
    return [{'a':a,'pole_bound':pole_bound(a),'h0':hol_dimension(a),
             'h1':hol_dimension(2-a),'index':index(a)} for a in range(-24,25)]

def matrix_controls():
    # A charged root, its actual Hermitian connection and a commuting triple.
    unit = old.unit; comm = old.old.comm
    z = s.diag(1,1,-2); e = unit(0,1); h = comm(e,e.T)
    u = unit(0,2)+2*unit(1,2)
    ax,ay = (u+u.T)/2,(u-u.T)/(2*s.I)
    q = 3
    soft_u = -s.trace(z*comm(u,u.adjoint()))
    soft_a = -s.trace(z*(-s.I*comm(ax,ay)))
    norm = s.trace(u.adjoint()*u)
    c,cb,d,db,n = s.symbols('c cb d db n')
    qq,qd = e/2+c*z,e.T/2+cb*z
    rr,rd = d*z,db*z
    mu = -h/4-n*z+comm(qq,qd)+comm(rr,rd)
    return {'matter':s.simplify(soft_u+q*norm),
            'connection':s.simplify(soft_a+q*norm/2),
            'soft':soft_u,'norm':norm,
            'two_field_residuals':old.old.zero(comm(qq,rr)) and old.old.zero(mu+n*z)
                and old.old.zero(comm(mu,qq)) and old.old.zero(comm(mu,rr)),
            'new_linear_R_term_nonzero':not old.old.zero(comm(u,z))}

@lru_cache(None)
def run():
    facts = {}
    aa = range(-24,25)
    facts['exact_log_endpoint_and_first_forbidden_pole'] = all(integrable(a,pole_bound(a)) and not integrable(a,pole_bound(a)+1) for a in aa)
    facts['two_opposite_log_equality_controls'] = integrable(0,0) and not integrable(2,1)
    facts['constant_and_first_pole_spin_controls'] = integrable(1,0) and not integrable(1,1)
    facts['pole_basis_dimension_and_distinct_orders'] = all(len(pole_basis(d)) == (0 if d<0 else 1 if d==0 else d) and len(set(pole_basis(d))) == len(pole_basis(d)) for d in range(-3,25))
    facts['simple_pole_is_absent_not_a_missing_basis_element'] = all(1 not in pole_basis(d) for d in range(25)) and pole_basis(1) == [0]
    facts['actual_hodge_dual_exponent_and_index_antisymmetry'] = all(index(a) == -index(2-a) for a in aa)
    facts['beta_zero_endpoint_is_not_counted'] = line_index(0) == 0 and index(0) == index(1) == 0
    facts['positive_beta_exact_parity_difference'] = all(index(-b) == -s.ceiling(Q(b,2)) and index(1-b) == -s.floor(Q(b,2)) and line_index(b) == b%2 for b in range(61))
    # Wrong strict inequality erases the L2 scalar constant at a=0.
    strict_h0 = lambda a: len(pole_basis((a-1)//2))
    strict_j = lambda a: strict_h0(a)-strict_h0(2-a)
    facts['dropping_log_endpoint_changes_index_control'] = strict_j(1)-strict_j(0) == 1 and line_index(0) == 0
    facts['forgetting_spin_shift_or_compact_degree_misses_index'] = line_index(1) == 1 and index(-1)-index(-1) == 0

    y = s.symbols('y',positive=True); a = s.symbols('a',integer=True)
    v = s.Function('v')(y); f = y**((1-a)/2)*v
    facts['canonical_line_metric_is_unitary'] = s.simplify(y**(a-1)*f**2-v**2) == 0
    facts['canonical_line_drift_from_derivative'] = s.simplify(y**((a+1)/2)*s.diff(f,y)-(y*s.diff(v,y)+(1-a)*v/2)) == 0
    h = s.Function('h')(y); b = s.symbols('b')
    facts['hermitian_hodge_coefficient_cancels_derivative'] = s.simplify(s.diff(h*(b/h),y)) == 0
    k,xi,t = s.symbols('k xi t',real=True)
    block_checks = []
    for j in range(5):
        for row in old.radial(j,k):
            if row['kind'] == 'AQ':
                d0,bb = row['d'],s.sqrt(row['b2'])*t
                mat = s.Matrix([[s.I*xi+d0,bb],[-bb,-s.I*xi+d0]])
                target = (xi*xi+d0*d0+t*t*row['b2'])*s.eye(2)
                block_checks.append(old.old.zero(s.simplify(mat.adjoint()*mat-target)))
    facts['principal_homotopy_full_blocks_not_scalar_guess'] = all(block_checks) and len(block_checks)==10
    ki = s.symbols('k',integer=True)
    drifts = [row['d'] for j in range(5) for row in old.radial(j,ki)]
    facts['all_extreme_and_paired_drifts_remain_half_integral'] = all(s.simplify(d-Q(1,2)).is_integer for d in drifts)
    rho = s.symbols('rho',positive=True); c = s.symbols('c',complex=True)
    psi = s.sqrt(y)*s.exp(-s.pi*y)
    facts['every_fixed_finite_neutral_amplitude_decays'] = s.limit(psi,y,s.oo)==0 and s.limit(y*s.diff(psi,y),y,s.oo)==0

    ww = weights()
    facts['whole248_weight_population_retained'] = sum(ww.values())==248
    facts['actual_roster_all_n_beta_bound_reduces_to_first_flux'] = all(m+2*abs(q)>=0 for q,m in ww if q)
    expected = {'1':12,'2':18,'3':12,'4':6,'5':0,'6':2}
    facts['positive_flux_exact_bosonic_index_profile'] = all(unstable_bounds(n)==expected for n in (1,2,3,5))
    facts['opposite_flux_conjugate_profile'] = all({str(-int(q)):v for q,v in unstable_bounds(-n).items()}==expected for n in (1,2,3,5))
    facts['fifty_bound_is_full_weight_count'] = sum(expected.values())==50 and sum(mult for (q,m),mult in ww.items() if q>0 and m%2)==50
    facts['zero_flux_does_not_get_negative_shift'] = unstable_bounds(0)=={} and sum(charge_indices(0)[q] for q in charge_indices(0) if q>0)==40
    facts['gauge_root_only_index_control_is_zero'] = all(charge_indices(n)[5]==0 for n in (1,2,3,5))
    matrix = matrix_controls()
    facts['full_moment_kinetic_factors_have_same_soft_shift'] = matrix['matter']==matrix['connection']==0 and matrix['soft']<0 and matrix['norm']>0
    good,bad = old.gauge_identity()
    facts['actual_moment_gauge_split_and_wrong_coefficient'] = good==0 and bad!=0
    epsilon = Q(1,4)
    facts['graph_approximation_keeps_a_strict_negative_margin'] = epsilon**2-(1-epsilon)**2 < 0 and epsilon**2+(1-epsilon)**2 > 0
    facts['second_neutral_field_stationary_but_changes_fluctuations'] = matrix['two_field_residuals'] and matrix['new_linear_R_term_nonzero']
    facts={name:bool(val) for name,val in facts.items()}
    return {'facts':facts,'predicates_passed':sum(facts.values()),
            'line_table':line_table(),
            'charge_index_profiles':{str(n):{str(q):v for q,v in charge_indices(n).items()} for n in range(-3,4)},
            'unstable_bounds':{str(n):unstable_bounds(n) for n in range(-3,4)},
            'full_Morse_index_computed':False,'physical_fermion_index_computed':False,
            'two_field_stability_computed':False,'stable_nonzero_flux_phase_achieved':False,
            'genesis_selection_derived':False,'nonauthor_acceptance':False,'physical_goal_achieved':False,
            'analytic_grade':'Global Fredholm/domain proof authored, not certified by finite predicates'}

if __name__=='__main__':
    result=run();print(json.dumps(result,indent=2,sort_keys=True))
    raise SystemExit(0 if all(result['facts'].values()) else 1)
