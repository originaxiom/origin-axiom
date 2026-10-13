"""Exact hypotheses for the authored noncompact admission application.

No finite computation certifies the analytic existence theorem or spectrum.
"""
from pathlib import Path
from itertools import product
import hashlib
import json
import sympy as s
from sympy.polys.matrices import DomainMatrix

HERE = Path(__file__).resolve().parent
checks = {}


def check(name, condition):
    if name in checks:
        raise AssertionError('duplicate check: ' + name)
    checks[name] = bool(condition)
    if not checks[name]:
        raise AssertionError(name)


def clean(matrix):
    return matrix.applyfunc(s.simplify)


def zero(matrix):
    return all(s.simplify(v) == 0 for v in matrix)


def rank(matrix):
    return DomainMatrix.from_Matrix(matrix, extension=True).rank()


def word(rep, letters):
    result = s.eye(next(iter(rep.values())).rows)
    for letter in letters:
        g = rep[letter.lower()]
        result = clean(result * (g if letter.islower() else g.inv()))
    return result


raw = (HERE / 'candidate.json').read_bytes()
check('candidate_git_blob', hashlib.sha1(b'blob ' + str(len(raw)).encode()
      + b'\0' + raw).hexdigest() == 'e1e4b140bc27df46d9bc41bfdfebf8464b17fa2d')
data = json.loads(raw)
T = s.Matrix([[1, 0, 0, 0], [0, 0, 1, s.I],
              [0, 0, 1, -s.I], [0, 1, 0, 0]])
V = {}
for g, rows in data['holonomy'].items():
    M = s.Matrix([[s.Rational(x) + s.I*s.Rational(y)
                   for x, y in row] for row in rows])
    den = s.sqrt(s.simplify(M.det()*s.conjugate(M.det())))
    V[g] = clean(data['nu'][g]*T.inv()*s.kronecker_product(M, M.conjugate())*T/den)
    check('determinant_' + g, s.simplify(V[g].det()) == 1)

c = s.Matrix([s.Rational(x) + s.sqrt(2)*s.Rational(y)
              for x, y in data['cocycle_Qsqrt2_pairs']])
W = {}
for j, g in enumerate('abt'):
    W[g] = V[g].row_join(c[4*j:4*j+4, :]).col_join(s.Matrix([[0, 0, 0, 0, 1]]))
for j, rel in enumerate(data['relators']):
    check('four_relator_' + str(j), zero(word(V, rel) - s.eye(4)))
    check('five_relator_' + str(j), zero(word(W, rel) - s.eye(5)))
B = s.Matrix.vstack(*(V[g] - s.eye(4) for g in 'abt'))
check('actual_extension_nonsplit', rank(B) == 4 and rank(B.row_join(c)) == 5)
check('split_control_retained', rank(B.row_join(s.zeros(12, 1))) == 4)
for j, rel in enumerate(data['cusp_words']):
    check('literal_peripheral_split_' + str(j), zero(word(W, rel)[:4, 4:5]))

words = [''] + [''.join(w) for n in range(1, 5) for w in product('abt', repeat=n)]
matrices = [word(V, w) for w in words]
span = s.Matrix.hstack(*(m.reshape(16, 1) for m in matrices))
dm = DomainMatrix.from_Matrix(span, extension=True)
_, pivots = dm.rref()
check('full_complex_matrix_algebra', len(pivots) == 16)
check('identity_only_control', rank(s.Matrix.hstack(*(s.eye(4).reshape(16, 1) for _ in range(3)))) == 1)

r = s.symbols('r', nonnegative=True)
ell, eps, A0, b0 = s.symbols('ell eps A0 b0', positive=True)
area = A0*s.exp(-2*r/ell)
wall = b0*s.exp(2*r/ell)
lap = lambda f: s.diff(f, r, 2) - 2*s.diff(f, r)/ell
check('volume_log_derivative', s.simplify(s.diff(area, r)/area + 2/ell) == 0)
check('wall_current_conserved', s.diff(s.simplify(area*wall), r) == 0)
check('wrong_wall_exponent_rejected', s.simplify(s.diff(area*b0*s.exp(r/ell), r)) != 0)
Xi = s.diag(1, 1, 1, 1, -4)
radial_flag = -wall*Xi
degree = s.simplify(area*s.trace(radial_flag[:4, :4]))
flux = s.simplify(area*s.trace(Xi*radial_flag))
check('total_flag_trace_zero', s.trace(radial_flag) == 0)
check('actual_subbundle_degree', degree == -4*A0*b0)
check('degree_is_one_fifth_current', s.simplify(degree - flux/5) == 0)
check('strict_positive_amplitude_slope', (degree/4).is_negative is True)
check('zero_amplitude_not_strict', degree.subs(b0, 0) == 0)
check('opposite_amplitude_reverses_degree', degree.subs(b0, -b0).is_positive is True)
phi = s.exp(-eps*r/ell)
barrier = ell**2*(1-phi)/(eps*(eps+2))
check('barrier_correct_laplacian', s.simplify(lap(barrier) + phi) == 0)
check('barrier_zero_seam', barrier.subs(r, 0) == 0)
check('barrier_bounded_limit', s.limit(barrier, r, s.oo) == ell**2/(eps*(eps+2)))
check('weighted_volume_integral', s.simplify(s.integrate(area*phi, (r, 0, s.oo)) - A0*ell/(eps+2)) == 0)
check('growing_comparison_harmonic', s.simplify(lap(s.exp(2*r/ell))) == 0)
R = s.symbols('R', nonnegative=True)
tail = A0*ell*s.exp(-2*R/ell)/2
check('tail_volume_bound', s.simplify(s.diff(tail, R) + area.subs(r, R)) == 0
      and s.limit(tail, R, s.oo) == 0)
check('tail_volume_zero_endpoint', s.simplify(s.integrate(area, (r, 0, s.oo)) - tail.subs(R, 0)) == 0)
check('wrong_tail_coefficient_rejected', s.simplify(s.diff(2*tail/3, R) + area.subs(r, R)) != 0)
norm = s.simplify(area*s.trace(s.diff(radial_flag, b0)**2))
check('amplitude_tangent_not_finite_modulus', norm == 20*A0*s.exp(2*r/ell)
      and s.integrate(norm, (r, 0, s.oo)) == s.oo)

result = {
    'checks': checks,
    'passed': sum(checks.values()),
    'matrix_algebra_rank': len(pivots),
    'spanning_words': [words[i] for i in pivots],
    'extension_coboundary_ranks': [rank(B), rank(B.row_join(c))],
    'degree_V': str(degree),
    'slope_V': str(degree/4),
    'flag_flux': str(flux),
    'scope': 'finite coefficient and radial hypotheses of authored analytic application',
    'analytic_theorem_machine_certified': False,
    'exact_end_profile_transport_proved': False,
    'physical_spectrum_or_genesis_selection': False,
}
print(json.dumps(result, indent=2))
