"""R46 canonical meridian controls, not a numerical global PDE certificate."""
from functools import lru_cache
import importlib.util
import json
from pathlib import Path

import sympy as s

spec = importlib.util.spec_from_file_location(
    'r46_parent_cusp', Path(__file__).with_name('parent_cusp.py'))
pc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pc)
cc = pc.cc
R, W = cc.R, cc.W
KINDS = ('4', 'dual4', '6')


def frequency_gap(exponent):
    """Minimum absolute frequency for phase exp(2*pi*i*exponent/4)."""
    residue = exponent % 4
    return s.pi*min(residue, 4-residue)/2


@lru_cache(None)
def meridian_inverse(kind, omega=W):
    if omega == 0:
        raise ValueError('nilpotent meridian has no zero-frequency inverse')
    _, n, _, _ = pc.operators(kind)
    if n**3 != s.zeros(n.rows):
        raise ValueError('this formula requires N cubed to vanish')
    a = s.I*omega
    inv = s.eye(n.rows)/a - n/(a*a*s.sqrt(R)) + n*n/(a**3*R)
    return a*s.eye(n.rows)+n/s.sqrt(R), cc.clean(inv)


def covariance(kind):
    d, n, p, j = pc.operators(kind)
    _, inv = meridian_inverse(kind)
    return (cc.clean(inv.diff(R)+cc.comm(j/R, inv)),
            cc.clean(cc.comm(cc.K*d+cc.BETA*p/R, inv)))


@lru_cache(None)
def full_cartan(kind='4', omit_derivative=False):
    d, n, p, j = pc.operators(kind)
    tx, inv = meridian_inverse(kind)
    wedge, interior = cc.exterior_operators()
    nu = s.symbols('nu', real=True)
    tt = s.I*nu*s.eye(n.rows)+cc.K*d+cc.BETA*p/R
    zero = (s.kronecker_product(wedge[0],j/R)
            +s.kronecker_product(wedge[1],tx)
            +s.kronecker_product(wedge[2],tt))
    homotopy = s.kronecker_product(interior[1],inv)
    result = zero*homotopy+homotopy*zero-s.eye(8*n.rows)
    if not omit_derivative:
        result += s.kronecker_product(wedge[0],s.eye(n.rows))*homotopy.diff(R)
    return cc.clean(result)


def comparison_metric():
    return s.diag(R**-2,R**-1,1)


def bound(kind, exponent):
    gap = frequency_gap(exponent)
    if gap == 0:
        raise ValueError('the trivial-character bound is unavailable')
    n = pc.operators(kind)[1]
    f1 = s.sqrt(s.trace(n.T*n))
    f2 = s.sqrt(s.trace((n*n).T*(n*n)))
    return (1/gap+f1/(gap**2*s.sqrt(R))+f2/(gap**3*R))/s.sqrt(R)


def rank_one_sources():
    profile = s.Matrix([1,s.I,2,0])*s.Matrix([[1,2,3]])
    return profile, [profile[:,i]*profile[:,j].T-profile[:,j]*profile[:,i].T
                     for i in range(3) for j in range(i+1,3)]


def run():
    inverses, radial, wrong_radial = {}, {}, {}
    for kind in KINDS:
        t, ti = meridian_inverse(kind)
        ident = s.eye(t.rows)
        inverses[kind] = all(cc.clean(a)==s.zeros(t.rows)
                             for a in (t*ti-ident,ti*t-ident))
        radial[kind] = all(a==s.zeros(t.rows) for a in covariance(kind))
        j = pc.operators(kind)[3]
        wrong_radial[kind] = cc.clean(cc.comm(j/R,ti)) != s.zeros(t.rows)
    metric = comparison_metric()
    eps = s.symbols('epsilon',positive=True)
    f = s.exp(eps*s.sqrt(R))
    profile,sources = rank_one_sources()
    checks = {
        'two_sided_inverses':all(inverses.values()),
        'radial_and_longitude_covariance':all(radial.values()),
        'missing_radial_derivative_detected':all(wrong_radial.values()),
        'full_exterior_Cartan':full_cartan()==s.zeros(32),
        'wrong_full_Cartan_fails':full_cartan(omit_derivative=True)!=s.zeros(32),
        'shifted_gap':tuple(frequency_gap(a) for a in range(4))==(0,s.pi/2,s.pi,s.pi/2),
        'zero_frequency_singular':all(pc.operators(kind)[1].det()==0 for kind in KINDS),
        'decaying_meridian_bound':all(s.limit(bound(kind,a),R,s.oo)==0
                                     for kind in KINDS for a in (1,2,3)),
        'nondecaying_longitude_comparison':metric[2,2]==1,
        'canonical_density':s.sqrt(metric.det())==R**(-s.Rational(3,2)),
        'Agmon_gradient':s.simplify(metric.inv()[0,0]*s.diff(f,R)**2/f**2)==eps**2*R/4,
        'L2_not_L4':s.integrate(R**(-s.Rational(9,8)),(R,1,s.oo))==8
                     and s.integrate(R**(-s.Rational(3,4)),(R,1,s.oo))==s.oo,
        'nonzero_mode_zero_source':profile!=s.zeros(4,3) and all(a==s.zeros(4) for a in sources)}
    return {'checks':checks,'all_checks_pass':all(checks.values()),
            'grade':'Finite canonical-end controls; analytic proof separately authored.',
            'received_six_ranks_recomputed_here':False,
            'nonzero_vertex_computed':False,'physical_chirality_derived':False}


if __name__=='__main__':
    data = run()
    print(json.dumps(data,sort_keys=True))
    raise SystemExit(0 if data['all_checks_pass'] else 1)
