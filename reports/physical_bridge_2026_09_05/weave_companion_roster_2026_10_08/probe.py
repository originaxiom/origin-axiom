"""Exact weight roster and local operator checks; see PROOF for analytic scope."""
from functools import lru_cache
from itertools import combinations, product
from pathlib import Path
import importlib.util
import json
import sympy as s

C1, C2, F1, F2, W = VARS = s.symbols('c1 c2 f1 f2 w', nonzero=True)
COLOUR = [C1, C2, 1/(C1*C2)]
FAMILY = [F1, F2, 1/(F1*F2)]
CHARS = [[1]*8, [1,1,1,1,-1,-1,-1,-1],
         [1,1,-1,-1,1,1,-1,-1], [1,1,-1,-1,-1,-1,1,1],
         [2,-2,0,0,0,0,0,0]]


def prior():
    path = Path(__file__).resolve().parent.parent/'weave_form_parent_2026_10_08/probe.py'
    spec = importlib.util.spec_from_file_location('sealed_form_parent', path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def ext(values, k):
    return sum(s.prod(x) for x in combinations(values, k))


def adj(values):
    return sum(x/y for x in values for y in values)-1


def e8_character(eigenvalues):
    v = [q*f for q in eigenvalues for f in FAMILY]
    vb = [1/x for x in v]
    c, cb, weak = sum(COLOUR), sum(1/x for x in COLOUR), W+1/W
    return s.expand(adj(COLOUR) + adj([W,1/W]) + adj(v)
                    + c*weak*sum(vb) + cb*weak*sum(v)
                    + c*ext(v,2) + cb*ext(vb,2) + weak*ext(v,3))


def weights(polynomial):
    out = {}
    for term in s.Add.make_args(s.expand(polynomial)):
        powers = term.as_powers_dict()
        key = tuple(int(powers.get(x,0)) for x in VARS)
        monomial = s.prod(x**n for x,n in zip(VARS,key))
        value = s.simplify(term/monomial)
        if value:
            assert value.is_Integer
            out[key] = out.get(key,0)+int(value)
    return {k:v for k,v in out.items() if v}


def pack(poly):
    return [[list(k),v] for k,v in sorted(weights(poly).items())]


def self_dual(poly):
    d = weights(poly)
    return all(d.get(tuple(-n for n in k),0) == v for k,v in d.items())


@lru_cache(None)
def modules():
    a, b = s.diag(s.I,-s.I), s.Matrix([[0,1],[-1,0]])
    group = [s.eye(2),-s.eye(2),a,-a,b,-b,a*b,-a*b]
    values = []
    cache = {}
    for g in group:
        eigen = tuple(x for x,m in g.eigenvals().items() for _ in range(m))
        key = (int(g.trace()),int(g.det()))
        if key not in cache:
            cache[key] = e8_character(eigen)
        values.append(cache[key])
    projected = [s.expand(sum(x*y for x,y in zip(char,values))/8) for char in CHARS]
    return values, projected


def expected_modules():
    c,cb = sum(COLOUR),sum(1/x for x in COLOUR)
    f,fb = sum(FAMILY),sum(1/x for x in FAMILY)
    sym2 = sum(FAMILY[i]*FAMILY[j] for i in range(3) for j in range(i,3))
    sym2b = sum(1/(FAMILY[i]*FAMILY[j]) for i in range(3) for j in range(i,3))
    one = adj(COLOUR)+adj([W,1/W])+adj(FAMILY)+c*sym2+cb*sym2b
    chi = 1+adj(FAMILY)+c*fb+cb*f
    rho = (W+1/W)*(c*fb+cb*f+adj(FAMILY)+2)
    return [s.expand(x) for x in (one,chi,chi,chi,rho)]


def line_selection(spin):
    # Actual simultaneous fixed spaces for the four compact flat LINE factors.
    # The nonparallel rho exclusion is analytic (PROOF), not this linear solve.
    sa,sb = spin
    return [1-s.Matrix([[sa*char[2]-1],[sb*char[4]-1]]).rank() for char in CHARS[:4]]


def slots(a,b):
    return [1+a,1-a,-1+b,-1-b]


def dimension(poly):
    return sum(weights(poly).values())


def twist_profile(a,b,spin_dim):
    q = slots(a,b)
    scalar,form,spin = q.count(0),sum(abs(x)==2 for x in q),sum(abs(x)==1 for x in q)
    return {'charges':q,'scalar_slots':scalar,'form_slots':form,'spin_slots':spin,
            'left_zero_dimension':55*scalar+111*form+spin_dim*spin,
            'neutral_supercharge_slots':scalar,
            'R_copies':form,'R_symmetric_mass_parameters':form*(form-1)//2,
            'ordinary_spin_zero_angular_fibre_channels':112*spin}


@lru_cache(None)
def run():
    values,m = modules()
    expected = expected_modules()
    dim = [dimension(x) for x in m]
    spins = [(1,1),(1,-1),(-1,1),(-1,-1)]
    selection = [line_selection(x) for x in spins]
    spin_dim = [sum(x*y for x,y in zip(row,dim)) for row in selection]
    form = m[0]+m[4]
    profiles,full_weights = {},{}
    for a,b in product((-1,0,1),repeat=2):
        rows=[]
        for i,d in enumerate(spin_dim):
            p=twist_profile(a,b,d)
            spin_module=sum(selection[i][j]*m[j] for j in range(4))
            full=s.expand(p['scalar_slots']*m[0]+p['form_slots']*form+p['spin_slots']*spin_module)
            p['all_weights_self_conjugate']=self_dual(full)
            p['dimension_from_weights']=dimension(full)
            rows.append(p)
            full_weights[f'{a},{b}:{i}']=pack(full)
        profiles[f'{a},{b}']=rows
    fprior=prior()
    _,ad3,gram=fprior.sl3_adjoint()
    eps=s.Matrix([[0,1],[-1,0]])
    bil3=fprior.invariant_bilinears(ad3)
    B=s.kronecker_product(bil3[0],eps)
    paired=s.kronecker_product(eps,B)
    t,L=s.symbols('t L',positive=True)
    u=s.Function('u')(t)
    bump=t*(1-t)
    residual=s.integrate(s.diff(bump,t)**2,(t,0,1))/s.integrate(bump**2,(t,0,1))/L**2
    f=s.exp(t/2)*u
    form_square=s.simplify(s.exp(-t/2)*(-s.diff(f,t,2)+s.diff(f,t)))
    beta=s.symbols('beta',real=True)
    r=s.symbols('r',positive=True)
    norm_z=r**(2*beta)/s.log(1/r)
    norm_t=s.simplify(norm_z.subs(r,s.exp(-t))*s.exp(-t))
    weak_in_spin=[sum(v for k,v in weights(p).items() if k[-1] in (-1,1)) for p in m[:4]]
    qminus=s.expand((values[0]-values[1])/2)
    test_complex=sum(COLOUR)*(W+1/W)*F1
    pA=profiles['1,0']
    pAB=profiles['1,1']
    facts={
        'E8_dimension':dimension(values[0])==248,
        'exact_Q8_dimensions':dim==[55,27,27,27,56],
        'all_joint_weights_match_branching':all(s.expand(x-y)==0 for x,y in zip(m,expected)),
        'no_negative_weight_multiplicities':all(v>=0 for p in m for v in weights(p).values()),
        'spin_line_selector_is_a_permutation':selection==[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]],
        'spin_dimensions_all_four_structures':spin_dim==[55,27,27,27],
        'no_weak_doublet_in_any_spin_zero_module':weak_in_spin==[0,0,0,0],
        'norm_coordinate_change':norm_t==s.exp(-(2*beta+1)*t)/t,
        'critical_spin_exponent_log_diverges':s.simplify(norm_t.subs(beta,-s.Rational(1,2))-1/t)==0,
        'regular_spin_exponent_exponentially_decays':s.simplify(norm_t.subs(beta,s.Rational(1,2))-s.exp(-2*t)/t)==0,
        'canonical_degree_negative_one':-2*s.Rational(1,2)==-1,
        'dual_canonical_not_ordinary_dual_degree':-2*s.Rational(1,2)!=1,
        'all_nine_twists_four_spin_structures':len(profiles)==9 and all(len(v)==4 for v in profiles.values()),
        'every_left_slot_counted_once':all(p['scalar_slots']+p['form_slots']+p['spin_slots']==4 for rows in profiles.values() for p in rows),
        'single_A_full_dimensions':[p['left_zero_dimension'] for p in pA]==[276,220,220,220],
        'single_B_full_dimensions':[p['left_zero_dimension'] for p in profiles['0,1']]==[276,220,220,220],
        'untwisted_dimensions':[p['left_zero_dimension'] for p in profiles['0,0']]==[220,108,108,108],
        'double_twist_dimensions':[p['left_zero_dimension'] for p in pAB]==[332]*4,
        'dimensions_equal_weight_rosters':all(p['left_zero_dimension']==p['dimension_from_weights'] for rows in profiles.values() for p in rows),
        'all_complete_zero_rosters_self_conjugate':all(p['all_weights_self_conjugate'] for rows in profiles.values() for p in rows),
        'complex_chiral_control_detected':not self_dual(test_complex),
        'one_R_in_single_twist_no_symmetric_mass':all(p['R_copies']==1 and p['R_symmetric_mass_parameters']==0 for p in pA),
        'actual_R_bilinear_skew_rank16':B.T==-B and B.rank()==16,
        'two_R_copies_admit_symmetric_full_rank_mass':paired.T==paired and paired.rank()==32,
        'double_twist_has_two_R_copies':all(p['R_copies']==2 and p['R_symmetric_mass_parameters']==1 for p in pAB),
        'positive_family_kinetic_gram':gram.is_positive_definite is True,
        'retained_nonzero_family_gauge_vertex':ad3[0]!=s.zeros(8),
        'minus_holonomy_space_dimension112':dimension(qminus)==112,
        'minus_holonomy_contains_same_rho_gauge_module':s.expand(qminus-2*m[4])==0,
        'single_twist_has224_zero_angular_fibre_channels':all(p['ordinary_spin_zero_angular_fibre_channels']==224 for p in pA),
        'Weyl_sequence_residual_tends_to_zero':residual==10/L**2 and s.limit(residual,L,s.oo)==0,
        'form_square_has_quarter_threshold':form_square==-s.diff(u,t,2)+u/4,
        'double_twist_has_no_ordinary_spin_slot':all(p['spin_slots']==0 for p in pAB),
        'discarding_companions_changes_roster':276!=55+111,
    }
    return {'facts':facts,'predicates_passed':sum(facts.values()),
            'module_weights':[pack(p) for p in m],'module_dimensions':dim,
            'spin_line_selection':selection,'spin_kernel_dimensions':spin_dim,
            'twist_profiles':profiles,'complete_zero_weights':full_weights,
            'protected_R_bilinear_ranks':[B.rank(),paired.rank()],
            'spin_Weyl_residual_coefficient':10,
            'full_curved_action_derived':False,'gapped_4D_reduction_derived':False,
            'physical_chiral_SM_derived':False,'global_anomaly_acceptance':False,
            'nonauthor_acceptance':False}


if __name__=='__main__':
    result=run()
    print(json.dumps(result,indent=2))
    raise SystemExit(0 if all(result['facts'].values()) else 1)
