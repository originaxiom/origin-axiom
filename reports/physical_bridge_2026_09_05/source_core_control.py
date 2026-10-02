"""R77 independent exact control; no native or third-party imports.

Row reduction builds an inverse of the current map, not its native
entrywise formula. Five rational samples interpolate the action's
quadratic coefficient, including the positive-gradient countercontrol.
This is an ADDED relaxed model, not physical source/profile admission.
"""
from fractions import Fraction as F
from functools import lru_cache
import json


class C(tuple):
    """Gaussian rationals: no floating-point complex arithmetic."""
    def __new__(cls, real=0, imag=0):
        return tuple.__new__(cls, (F(real), F(imag)))

    @staticmethod
    def of(x):
        return x if isinstance(x, C) else C(x)

    def __add__(self, other):
        q = C.of(other)
        return C(self[0]+q[0], self[1]+q[1])

    __radd__ = __add__

    def __neg__(self):
        return C(-self[0], -self[1])

    def __sub__(self, other):
        return self + -C.of(other)

    def __mul__(self, other):
        q = C.of(other)
        return C(self[0]*q[0]-self[1]*q[1], self[0]*q[1]+self[1]*q[0])

    __rmul__ = __mul__

    def conj(self):
        return C(self[0], -self[1])


def zero(n):
    return [[C() for _ in range(n)] for _ in range(n)]


def scale(q, a):
    return [[q*x for x in row] for row in a]


def add(a, b):
    return [[x+y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def trans(a):
    return [list(row) for row in zip(*a)]


def dagger(a):
    return [[x.conj() for x in row] for row in trans(a)]


def product(a, b):
    return [[sum((x*y for x, y in zip(row, col)), C())
             for col in zip(*b)] for row in a]


def comm(a, b):
    return add(product(a, b), scale(-1, product(b, a)))


def trace(a):
    return sum((a[i][i] for i in range(len(a))), C())


def norm(a):
    q = sum((x.conj()*x for row in a for x in row), C())
    if q[1] != 0:
        raise ArithmeticError('non-real norm')
    return q[0]


def moment(fields):
    answer = zero(len(fields[0]))
    for z in fields:
        answer = add(answer, comm(z, dagger(z)))
    return answer


def hermitian_basis(n=5):
    answer = []
    for i in range(n-1):
        a = zero(n)
        a[i][i], a[-1][-1] = C(1), C(-1)
        answer.append(a)
    for i in range(n):
        for j in range(i+1, n):
            for q in (C(1), C(0, 1)):
                a = zero(n)
                a[i][j], a[j][i] = q, q.conj()
                answer.append(a)
    return answer


def coords(a):
    n = len(a)
    if dagger(a) != a or trace(a) != C():
        raise ValueError('coordinate input must be trace-free Hermitian')
    return [a[i][i][0] for i in range(n-1)] + [
        a[i][j][part] for i in range(n) for j in range(i+1, n)
        for part in (0, 1)]


def fixed_matrices():
    # Different diagonal from the native construction; all entries distinct.
    a = zero(5)
    for i, q in enumerate((0, 1, 4, 9, -14)):
        a[i][i] = C(q)
    answer = [a]
    for j in range(4):
        b = zero(5)
        b[j][4] = b[4][j] = C(1)
        answer.append(b)
    return answer


@lru_cache(None)
def inverse_data():
    aa, basis = fixed_matrices(), hermitian_basis()
    columns = [coords(scale(C(0, -2), comm(a, b)))
               for a in aa for b in basis]
    left = [list(row) for row in zip(*columns)]
    width = len(columns)
    table = [row + [F(i == j) for j in range(24)]
             for i, row in enumerate(left)]
    pivots, row = [], 0
    for col in range(width):
        pivot = next((i for i in range(row, 24) if table[i][col]), None)
        if pivot is None:
            continue
        table[row], table[pivot] = table[pivot], table[row]
        q = table[row][col]
        table[row] = [x/q for x in table[row]]
        for i in range(24):
            if i != row and table[i][col]:
                q = table[i][col]
                table[i] = [x-q*y for x, y in zip(table[i], table[row])]
        pivots.append(col)
        row += 1
        if row == 24:
            break
    return aa, basis, left, table, pivots


def fields_for(target):
    aa, basis, left, table, pivots = inverse_data()
    if len(pivots) != 24:
        raise ArithmeticError('current map is not surjective')
    yy = coords(target)
    xx = [F(0) for _ in range(len(left[0]))]
    for row, col in enumerate(pivots):
        xx[col] = sum(x*y for x, y in zip(table[row][120:], yy))
    fields = []
    for j, a in enumerate(aa):
        b = zero(5)
        for coefficient, h in zip(xx[24*j:24*(j+1)], basis):
            b = add(b, scale(coefficient, h))
        fields.append(add(a, scale(C(0, 1), b)))
    return fields


def example():
    a = zero(5)
    for i, q in enumerate((1, -2, 3, -4, 2)):
        a[i][i] = C(q)
    for i in range(5):
        for j in range(i+1, 5):
            a[i][j] = C(i+1, -j-1)
            a[j][i] = a[i][j].conj()
    return a


def coefficients(value):
    """Exact degree<=4 interpolation; no numerical derivative/tolerance."""
    m2, m1, c0, p1, p2 = (value(F(i)) for i in (-2, -1, 0, 1, 2))
    c1 = (8*(p1-m1)-(p2-m2))/12
    c2 = (16*(p1+m1)-(p2+m2)-30*c0)/24
    c3 = ((p2-m2)-2*(p1-m1))/12
    c4 = ((p2+m2)-4*(p1+m1)+6*c0)/24
    return (c0, c1, c2, c3, c4)


def integrate(poly):
    return sum((x/F(i+1) for i, x in enumerate(poly)), F(0))


def square(poly):
    out = [F(0)]*(2*len(poly)-1)
    for i, a in enumerate(poly):
        for j, b in enumerate(poly):
            out[i+j] += a*b
    return out


@lru_cache(None)
def run():
    aa, basis, left, table, pivots = inverse_data()
    cur = example()
    fields = fields_for(scale(F(-1, 6), cur))
    matched = add(cur, scale(6, moment(fields)))
    h = zero(5)
    h[0][4] = C(0, 1)

    def residual(t):
        varied = list(fields)
        varied[0] = add(varied[0], scale(t, h))
        return add(cur, scale(6, moment(varied)))

    source_coeff = coefficients(lambda t: norm(residual(t))/4)
    bulk_coeff = coefficients(lambda t: norm(scale(t, basis[0]))/4)
    d = scale(-1, matched)

    def offshell(aux):
        q = trace(product(aux, aux))*F(1, 4) + trace(product(aux, matched))*F(1, 2)
        if q[1]:
            raise ArithmeticError('non-real auxiliary action')
        return q[0]

    u = [[C(1, 1), C(2, -1)], [C(3, 1), C(-1, -1)]]
    tail = coefficients(lambda t: norm(moment([scale(t, u)]))/2)
    kinetic = 2*integrate(square([F(0), F(1), F(-1)]))
    gradient = 2*integrate(square([F(1), F(-2)]))
    lifted = coefficients(lambda t: norm(moment([scale(t, u)]))/2 + gradient*t*t)
    ht = [[C(1), C()], [C(), C(-1)]]
    tau = lambda a: scale(-1, trans(a))
    dual_fields = [tau(z) for z in fields]
    partial = add(cur, scale(6, moment(dual_fields)))
    rotated = zero(5)
    for i in range(5):
        rotated[i][i] = C(1)
    rotated[0][0] = rotated[1][1] = C(F(3, 5))
    rotated[0][1], rotated[1][0] = C(F(-4, 5)), C(F(4, 5))
    rot = lambda a: product(product(rotated, a), dagger(rotated))
    checks = {
        'full_current_rank_24': len(pivots) == 24,
        'all_24_targets_recovered': all(moment(fields_for(b)) == b for b in basis),
        'opposite_current_recovered': moment(fields_for(scale(-1, cur))) == scale(-1, cur),
        'zero_current_recovered': moment(fields_for(zero(5))) == zero(5),
        'all_fields_tracefree': all(trace(z) == C() for z in fields),
        'matched_full_current': matched == zero(5),
        'wrong_sign_live': norm(add(cur, scale(6, moment(fields_for(scale(F(1, 6), cur)))))) > 0,
        'source_first_coefficient_zero': source_coeff[1] == 0,
        'source_second_coefficient_positive': source_coeff[2] > 0,
        'bulk_first_coefficient_zero': bulk_coeff[1] == 0,
        'bulk_second_coefficient_positive': bulk_coeff[2] > 0,
        'auxiliary_first_variation_all_24': all(offshell(add(d, b)) == offshell(add(d, scale(-1, b))) for b in basis),
        'auxiliary_elimination_five_amplitudes': all(
            trace(product(scale(-1, residual(t)), scale(-1, residual(t))))[0]/4
            + trace(product(scale(-1, residual(t)), residual(t)))[0]/2
            == -norm(residual(t))/4 for t in map(F, (-2, -1, 0, 1, 2))),
        'quartic_tail_quadratic_zero': tail[2] == 0,
        'quartic_tail_live_positive': tail[4] > 0,
        'hermitian_tail_exact_flat': all(moment([scale(t, ht)]) == zero(2) for t in map(F, (-2, -1, 0, 1, 2))),
        'positive_profile_kinetic': kinetic == F(1, 15),
        'positive_internal_gradient': gradient == F(2, 3),
        'same_coefficient_extraction_detects_gradient': lifted[2] == gradient,
        'unitary_control': product(dagger(rotated), rotated) == [[C(i == j) for j in range(5)] for i in range(5)],
        'moment_unitary_covariance': moment([rot(z) for z in fields]) == rot(moment(fields)),
        'duality_current_covariance': moment(dual_fields) == tau(moment(fields)),
        'duality_complete_balance': add(tau(cur), scale(6, moment(dual_fields))) == zero(5),
        'duality_kinetic_norm': sum(map(norm, dual_fields)) == sum(map(norm, fields)),
        'duality_potential_five_amplitudes': all(norm(tau(residual(t))) == norm(residual(t)) for t in map(F, (-2, -1, 0, 1, 2))),
        'untransported_current_detected': norm(partial) > 0,
        'two_patch_square_partition': moment([scale(F(3, 5), z) for z in fields] + [scale(F(4, 5), z) for z in fields]) == moment(fields),
        'omitted_patch_detected': moment([scale(F(3, 5), z) for z in fields]) != moment(fields),
        'interpolation_live_quadratic': coefficients(lambda t: F(2)+3*t+5*t*t+7*t**3+11*t**4) == tuple(map(F, (2, 3, 5, 7, 11))),
    }
    return {'checks': checks, 'rank': len(pivots), 'image_dimension': 24,
            'source_coefficients': list(map(str, source_coeff)),
            'tail_coefficients': list(map(str, tail)),
            'gradient_coefficients': list(map(str, lifted)),
            'all_checks_pass': all(checks.values()),
            'scope': 'exact relaxed-model controls, not physical mirror, source admission or TOE'}


if __name__ == '__main__':
    result = run()
    print(json.dumps(result, sort_keys=True, indent=2))
    raise SystemExit(0 if result['all_checks_pass'] else 1)
