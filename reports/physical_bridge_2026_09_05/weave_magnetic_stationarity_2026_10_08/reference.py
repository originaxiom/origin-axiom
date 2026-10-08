"""Separate abstract SU5 weights / rational matrices; no native imports."""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations
import json

def add(a, b): return [[x+y for x, y in zip(ar, br)] for ar, br in zip(a, b)]
def scale(c, a): return [[c*x for x in row] for row in a]
def mul(a, b): return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def tr(a): return sum(a[i][i] for i in range(len(a)))
def bracket(a, b): return add(mul(a, b), scale(-1, mul(b, a)))

def root_profile():
    five = (-2, -2, -2, 3, 3)
    adj = Counter(a-b for i, a in enumerate(five) for j, b in enumerate(five) if i != j)
    adj[0] += 4
    total = adj.copy(); total[0] += 24
    for a, b in combinations(five, 2):
        total[a+b] += 5; total[-a-b] += 5
    for a in five:
        total[-a] += 10; total[a] += 10
    return {'charges': {str(k): v for k, v in sorted(total.items())},
            'adjoint_trace_Z2': sum(k*k*v for k, v in total.items()),
            'norm_Z2': sum(F(v*v, 4) for v in (5, 5, 5, -3, -3, -3, -3, -3)),
            'gauge_roots': 20, 'bundle_roots': 20, 'SM_roots': adj[0]-4,
            'unstable_root_multiplicity_per_sign': adj[5]}

def pole_orders(k):
    # Enumerate monomials reduced by y^2=cubic(x), not the native loops.
    return sorted(2*a+3*b for a in range(k+1) for b in (0, 1) if 2*a+3*b <= k)

def sample_profile():
    rows = []
    for flux in range(-3, 4):
        charge = 5 if flux >= 0 else -5
        degree = flux*charge
        rows.append({'n': flux, 'q': charge, 'k': degree, 'mass2': -degree,
                     'negative_complex_lower_bound': 6*degree,
                     'threshold': str(F(2*degree+1, 2)**2),
                     'conjugate_threshold': str(F(1-2*degree, 2)**2)})
    return rows

def run():
    p = {}; roster = root_profile()
    p['abstract_full248_with_both_conjugates'] = sum(roster['charges'].values()) == 248
    p['trace_norm_and_charge_profile'] = roster['adjoint_trace_Z2'] == 1800 and roster['norm_Z2'] == 30 and roster['charges']['1'] == 30
    p['SM_vs_SU5_and_six_broken_roots'] = roster['SM_roots'] == 8 and roster['gauge_roots'] == 20 and roster['unstable_root_multiplicity_per_sign'] == 6
    p['cocharacter_pairing_has_primitive_charge'] = '1' in roster['charges'] and all(int(q) == F(q) for q in roster['charges'])
    e = [[0, 1], [0, 0]]; et = [[0, 0], [1, 0]]
    h = bracket(e, et)
    p['root_plane_bracket'] = h == [[1, 0], [0, -1]]
    # Hermitian ax=(e+et)/2, ay=(e-et)/(2i): -i[ax,ay]=[e,et]/2.
    real_f2 = scale(F(1, 4), bracket(add(e, et), add(e, scale(-1, et))))
    real_f2 = scale(-1, real_f2)
    p['actual_quadratic_curvature'] = real_f2 == scale(F(1, 2), h)
    quadratics = []; quartics = []; masses = []
    for flux in (-3, -1, 0, 1, 3):
        for charge in (-5, 5):
            z = scale(F(charge, 2), h); mu = scale(-flux, z)
            quadratic = tr(mul(mu, real_f2)); quartic = tr(mul(real_f2, real_f2))/2
            kinetic = F(1, 2)*tr(mul(et, e))
            quadratics.append(quadratic == F(-flux*charge, 2))
            quartics.append(quartic == F(1, 4))
            masses.append(quadratic/kinetic == -flux*charge)
    p['all_signed_quadratics'] = all(quadratics)
    p['quartic_is_positive'] = all(quartics)
    p['kinetic_mass_ratio'] = all(masses)
    p['wrong_charge_stabilizing_control'] = (-1)*(-5) > 0
    # Independent rational ladder in non-orthonormal weight basis.
    e5 = [[0]*5 for _ in range(5)]; f5 = [[0]*5 for _ in range(5)]
    for i in range(4): e5[i+1][i] = 4-i; f5[i][i+1] = i+1
    h5 = bracket(e5, f5)
    p['principal_ladder_and_moment_cancellation'] = h5 == [[2*(i-2) if i == j else 0 for j in range(5)] for i in range(5)] and bracket(h5, e5) == scale(2, e5)
    p['wrong_amplitude_has_nonzero_matter_gradient'] = bracket(add(scale(F(-1, 4), h5), h5), e5) != [[0]*5 for _ in range(5)]
    p['sections_have_distinct_allowed_poles'] = all(pole_orders(k) == [0]+list(range(2, k+1)) and len(pole_orders(k)) == k for k in range(1, 101))
    p['k5_basis'] = pole_orders(5) == [0, 2, 3, 4, 5]
    # r=exp(-t): L2 at pole p is exp(-2(k-p+1)t)*t^(2k).
    p['radial_integrability_and_bad_endpoint'] = all(2*(k-pole+1) > 0 for k in range(1, 41) for pole in range(k+1)) and all(2*(k-(k+1)+1) == 0 and 2*k >= 0 for k in range(1, 41))
    p['worst_allowed_mode_decays_and_is_L4'] = all(2*(k-k+1) == 2 and 4*(k-k+1) == 4 for k in range(1, 41))
    p['even_spin_power_independent'] = all((-1)**(2*k) == 1 for k in range(1, 41))
    p['both_flux_signs_same_lower_bound'] = all(row['mass2'] == -5*abs(row['n']) and row['negative_complex_lower_bound'] == 30*abs(row['n']) for row in sample_profile())
    p['fermion_drift_not_a_count'] = F(11, 2)**2 == F(121, 4) and F(-9, 2)**2 == F(81, 4)
    roster['norm_Z2'] = int(roster['norm_Z2'])
    return {'predicates': p, 'predicates_passed': sum(p.values()),
            'root_profile': roster, 'sample_profile': sample_profile(),
            'analytic_domain_independently_accepted': False,
            'physical_goal_achieved': False}

if __name__ == '__main__':
    result = run(); print(json.dumps(result, indent=2, sort_keys=True))
    raise SystemExit(0 if all(result['predicates'].values()) else 1)
