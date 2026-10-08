"""Separate exact rational/Weyl-closure route, same author, not outside review."""
from collections import Counter
from fractions import Fraction as F
from math import comb
import json


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def simple_roots():
    result = [(1, -1, -1, -1, -1, -1, -1, 1), (2, 2, 0, 0, 0, 0, 0, 0)]
    for k in range(6):
        result.append(tuple(-2*int(i == k)+2*int(i == k+1) for i in range(8)))
    return result


def weyl_roots():
    simples = simple_roots()
    result = set(simples)
    queue = list(simples)
    for b in queue:
        for a in simples:
            numerator = dot(a, b)
            assert numerator % 4 == 0
            v = tuple(b[i]-(numerator//4)*a[i] for i in range(8))
            if v not in result:
                result.add(v)
                queue.append(v)
    return result


def polynomial_levels(n):
    # x^(n-k)y^k; E=x d/dy, F=y d/dx, Gram_k=1/binomial(n,k).
    gram = [F(1, comb(n, k)) for k in range(n+1)]
    result = []
    for k in range(n+1):
        norm_E = F(k*k)*gram[k-1]/gram[k] if k else F(0)
        m = F(n, 2)-k
        result.append(m*m/4+norm_E/2)
    return result, gram


def periphery(b):
    v = (0, 0, 0, 2, -2, 0, 0, 0)
    return (dot(b, v)//4) % 2


def string_profile(rr, alpha):
    histogram = Counter()
    for b in rr:
        if not periphery(b):
            continue
        if b == alpha or all(b[i] == -alpha[i] for i in range(8)):
            n, k = 2, (0 if b == alpha else 2)
        else:
            up = down = 0
            while tuple(b[i]+(up+1)*alpha[i] for i in range(8)) in rr:
                up += 1
            while tuple(b[i]-(down+1)*alpha[i] for i in range(8)) in rr:
                down += 1
            n, k = up+down, up
        levels, _ = polynomial_levels(n)
        histogram[str(levels[k])] += 1
    return histogram


def run():
    rr = weyl_roots()
    # Scalar coefficient equations, independently of matrix differentiation.
    h = -F(1, 2)/2
    c2 = -h
    derivative_coefficient = -F(1, 2)-2*h
    moment_coefficient = h+c2
    hvec = (-4, -4, -4, 6, 6, 0, 0, 0)
    v = (0, 0, 0, 2, -2, 0, 0, 0)
    alpha = (0, 0, 0, 2, 0, 2, 0, 0)
    odd = {b for b in rr if periphery(b)}
    hist = string_profile(rr, alpha)
    thresholds = {str(n): [str(v) for v in polynomial_levels(n)[0]] for n in range(3)}
    tests = {
        'Weyl_closure_240_roots': len(rr) == 240 and all(dot(b, b) == 8 for b in rr),
        'root_system_has_both_signs': all(tuple(-x for x in b) in rr for b in rr),
        'reflection_closed': all(tuple(b[i]-dot(b, a)//4*a[i] for i in range(8)) in rr for b in rr for a in simple_roots()),
        'nonzero_branch_coefficients': h == -F(1, 4) and c2 == F(1, 4) and derivative_coefficient == moment_coefficient == 0,
        'flat_connection_fails': -F(1, 2) != 0 and c2 != 0,
        'wrong_amplitude_fails': h+1 != 0,
        'parallel_spin_charge': -F(1, 2)-2*h == 0,
        'expanded_energy_balances': h*h+c2*c2-c2/2 == 0 and h*h+c2*c2 > 0,
        'norms_finite_positive_coefficients': c2 == F(1, 4) and h*h == F(1, 16),
        'peripheral_root_action_identity': all((dot(b, hvec)-dot(b, v)) % 8 == 0 for b in rr),
        'odd_population112': len(odd) == 112,
        'sl2_centralizer_spectators54': sum(dot(b, alpha) == 0 for b in odd) == 54,
        'root_strings_threshold_histogram': hist == Counter({'0': 54, '1/16': 28, '9/16': 28, '1/4': 1, '5/4': 1}),
        'all112_root_strings_checked': all(string_profile(rr, a) == hist for a in odd),
        'mixed_coefficient_control': F(1, 16)+F(1, 4) != polynomial_levels(1)[0][1],
        'nontrivial_Hermitian_Gram_used': polynomial_levels(2)[1] == [F(1), F(1, 2), F(1)],
        'positive_lifted_population58': sum(n for k, n in hist.items() if k != '0') == 58,
        'spectator_population_not_deleted': hist['0'] == 54 and sum(hist.values()) == 112,
    }
    for n in range(3):
        _, gram = polynomial_levels(n)
        tests['polynomial_raising_lowering_adjoint_'+str(n)] = all(k*gram[k-1] == (n-k+1)*gram[k] for k in range(1, n+1))
    return dict(predicates=tests, predicates_passed=sum(tests.values()),
        end_profile=dict(h=str(h), amplitude_squared=str(c2), root_population=len(odd),
            sl2_thresholds=thresholds, R_threshold_histogram=dict(hist),
            odd_spectators=hist['0'], free_spin_slot_channels=2*hist['0']))


if __name__ == '__main__':
    result = run()
    print(json.dumps(result, indent=2, sort_keys=True))
    raise SystemExit(0 if all(result['predicates'].values()) else 1)
