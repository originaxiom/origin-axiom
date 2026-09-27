"""R50 exact finite controls; not a global PDE or physical-vacuum solver."""
from fractions import Fraction as F
from functools import lru_cache
import json

import sympy as s


def zero(value):
    entries = list(value) if isinstance(value, s.MatrixBase) else [value]
    return all(s.cancel(x) == 0 for x in entries)


def comm(a, b):
    return a*b-b*a


def add(*polys):
    out = {}
    for poly in polys:
        for word, coefficient in poly.items():
            out[word] = out.get(word, F(0)) + coefficient
    return {w: v for w, v in out.items() if v}


def scale(a, poly):
    return {w: F(a)*v for w, v in poly.items() if a*v}


def mul(a, b):
    out = {}
    for u, x in a.items():
        for v, y in b.items():
            out[u+v] = out.get(u+v, F(0)) + x*y
    return {w: v for w, v in out.items() if v}


def atom(name):
    return {(name,): F(1)}


DEGREE = {'c': 1, 'p': 1, 'sigma': 0, 'c2': 1}


def differential(poly):
    """Free graded derivation: dc=dp=0, d sigma=p, d c2=-c*c."""
    rules = {'c': {}, 'p': {}, 'sigma': atom('p'),
             'c2': {('c', 'c'): F(-1)}}
    out = {}
    for word, coefficient in poly.items():
        degree_before = 0
        for i, letter in enumerate(word):
            for replacement, value in rules[letter].items():
                new_word = word[:i]+replacement+word[i+1:]
                out = add(out, {new_word: coefficient*value*(-1)**degree_before})
            degree_before += DEGREE[letter]
    return out


def formal_flat_residual(commutator_sign=1, half=F(1, 2), include_c2=True):
    c, p, sigma = atom('c'), atom('p'), atom('sigma')
    alpha = add(c, scale(-1, p))
    correction = add(atom('c2') if include_c2 else {},
                     scale(commutator_sign, add(mul(sigma, c), scale(-1, mul(c, sigma)))),
                     scale(half, add(mul(p, sigma), scale(-1, mul(sigma, p)))))
    return add(differential(correction), mul(alpha, alpha))


@lru_cache(None)
def tail_controls():
    q, R = s.symbols('q R', positive=True)
    k = s.symbols('k', real=True)
    N = s.zeros(4)
    N[0, 2] = N[2, 3] = 1
    P, D, J = N**2, s.diag(1, -3, 1, 1), s.diag(5, -3, 1, -3)/8
    b = 6/(q-1/q)
    b1 = s.cancel(q*s.diff(b, q))
    b2 = s.cancel(q*s.diff(b1, q))
    bx, br = N/s.sqrt(R), J/R
    c = D+b1*P/R
    c2 = b2*P/(2*R)
    # k+s is linear; the nonlinear q contribution is differentiated by q*d/dq.
    expected_b2 = 6*q*(q**4+6*q**2+1)/(q**2-1)**3
    return {
        'second_k_derivative': zero(b2-expected_b2),
        'taylor_half': zero(c2-q*s.diff(c, q)/2),
        'meridian_first': zero(comm(bx, c)),
        'radial_first': zero(c.diff(R)+comm(br, c)),
        'meridian_second': zero(comm(bx, c2)),
        'radial_second': zero(c2.diff(R)+comm(br, c2)),
        'second_not_zero': not zero(c2),
        'missing_radial_derivative_rejected': not zero(comm(br, c2)),
        'missing_taylor_half_rejected': not zero(c2-q*s.diff(c, q)),
        'q_one_is_excluded_pole': s.denom(s.factor(b2)).subs(q, 1) == 0,
    }


def adjoint(d, g_from, g_to):
    return g_from.inv()*d.T*g_to


def harmonic_projector(lap, gram):
    basis = lap.nullspace()
    if not basis:
        return s.zeros(lap.rows)
    n = s.Matrix.hstack(*basis)
    return n*(n.T*gram*n).inv()*n.T*gram


@lru_cache(None)
def finite_complex():
    d0 = s.Matrix([[1, 0], [0, 0], [0, 0], [0, 0]])
    d1 = s.Matrix([[0, 2, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
    d2 = s.Matrix([[0, 3, 0]])
    grams = [s.diag(2, 3), s.diag(5, 7, 11, 13), s.diag(17, 19, 23), s.diag(29)]
    a0, a1, a2 = [adjoint(d, grams[i], grams[i+1])
                  for i, d in enumerate((d0, d1, d2))]
    laps = [a0*d0, d0*a0+a1*d1, d1*a1+a2*d2, d2*a2]
    projectors = [harmonic_projector(lap, g) for lap, g in zip(laps, grams)]
    greens = [(lap+pi).inv()-pi for lap, pi in zip(laps, projectors)]
    return (d0, d1, d2), (a0, a1, a2), grams, laps, projectors, greens


def relax(j2, j0):
    ds, ads, grams, laps, pis, greens = finite_complex()
    beta = -ads[1]*greens[2]*j2+ds[0]*greens[0]*j0
    r2, r0 = ds[1]*beta+j2, ads[0]*beta-j0
    return beta, r2, r0, (r2.T*grams[2]*r2+r0.T*grams[0]*r0)[0]


def hilbert_controls():
    ds, ads, grams, laps, pis, greens = finite_complex()
    j2, j0 = s.Matrix([7, 0, 0]), s.Matrix([3, 0])
    beta, r2, r0, norm = relax(j2, j0)
    op = ds[1].col_join(ads[0])
    target = (-j2).col_join(j0)
    target_gram = s.diag(grams[2], grams[0])
    image = s.Matrix.hstack(*op.columnspace())
    projection = image*(image.T*target_gram*image).inv()*image.T*target_gram
    b_ob, r_ob, r0_ob, n_ob = relax(s.Matrix([7, 0, 5]), j0)
    b0_ob, r20_ob, rz_ob, n0_ob = relax(j2, s.Matrix([3, 5]))
    bad = s.Matrix([0, 1, 0])
    _, bad_res, _, bad_norm = relax(bad, s.zeros(2, 1))
    return {
        'chain': zero(ds[1]*ds[0]) and zero(ds[2]*ds[1]),
        'gram_positive': all(g.is_positive_definite for g in grams),
        'green_identities': all(zero(lap*green-(s.eye(lap.rows)-pi))
                                and zero(green*pi)
                                for lap, green, pi in zip(laps, greens, pis)),
        'projectors_metric_self_adjoint': all(zero(pi.T*g-g*pi) and zero(pi*pi-pi)
                                              for pi, g in zip(pis, grams)),
        'exact_curvature_and_moment_cancel': zero(r2) and zero(r0) and norm == 0,
        'correction_is_transverse_to_H1': zero(pis[1]*beta),
        'independent_least_squares_agrees': zero(op*beta-projection*target),
        'curvature_obstruction_retained': r_ob == s.Matrix([0, 0, 5]) and n_ob == 575,
        'degree_zero_obstruction_retained': rz_ob == s.Matrix([0, -5]) and n0_ob == 75,
        'nonclosed_not_certified_by_Pi': zero(pis[2]*bad) and not zero(ds[2]*bad)
                                       and not zero(bad_res) and bad_norm == 19,
        'wrong_gram_changes_correction': beta != s.Matrix([3, -s.Rational(7, 2), 0, 0]),
        'both_channels_required': not zero(ds[1]*(ds[0]*greens[0]*j0)+j2),
    }


def polynomial_controls():
    t, y = s.symbols('t y', real=True)
    # Finite scalar countermodels, not substituted for the global field equations.
    v_flat = (y+t*t)**2
    v_obstructed = v_flat+t**4
    v_higher = v_flat+t**6
    straight = s.expand(v_flat.subs(y, 0))
    relaxed = s.expand(v_flat.subs(y, -t*t))
    higher = s.expand(v_higher.subs(y, -t*t))
    return {
        'positive_straight_quartic': straight == t**4,
        'zero_relaxed_quartic': relaxed == 0,
        'obstructed_control': s.expand(v_obstructed.subs(y, -t*t)) == t**4,
        'sixth_order_not_exact_branch': higher == t**6 and higher != 0,
        'stationary_elimination': s.diff(v_flat, y).subs(y, -t*t) == 0,
    }


def weight_controls():
    # Explicit rational witnesses for the strict inequalities in the proof.
    eps, delta, gamma = s.Rational(3, 8), s.Rational(1, 32), s.Rational(1, 4)
    return {
        'inhomogeneous_absorption': gamma > s.Rational(4, 3)*eps**2,
        'forcing_weight_integrable': 2*(eps+delta) < 1,
        'quartic_from_lifted_estimate': 4*(s.Rational(1, 2)-eps) < 1,
        'endpoint_not_absorbed': not (s.Rational(1, 3) > s.Rational(4, 3)*s.Rational(1, 2)**2),
        'L2_does_not_imply_L4': 2*s.Rational(3, 8) < 1 <= 4*s.Rational(3, 8),
        'product_source_weight_margin': 2*eps+4*delta < 1,
    }


def controls():
    free = {
        'graded_transport': not formal_flat_residual(),
        'wrong_commutator_rejected': bool(formal_flat_residual(commutator_sign=-1)),
        'missing_half_term_rejected': bool(formal_flat_residual(half=0)),
        'missing_flat_twojet_rejected': bool(formal_flat_residual(include_c2=False)),
        'graded_leibniz_sign': differential({('c', 'sigma'): F(1)}) == {('c', 'p'): F(-1)},
        'd_squared_zero': not differential(differential(mul(atom('c2'), atom('sigma')))),
    }
    return {'tail': tail_controls(), 'free_algebra': free,
            'hilbert': hilbert_controls(), 'potential': polynomial_controls(),
            'weights': weight_controls()}


if __name__ == '__main__':
    groups = controls()
    serial = {g: {k: bool(v) for k, v in values.items()} for g, values in groups.items()}
    passed = sum(sum(group.values()) for group in serial.values())
    total = sum(len(group) for group in serial.values())
    print(json.dumps({'checks': serial, 'passed': passed, 'total': total,
                      'all_checks_pass': passed == total,
                      'grade': 'Finite controls support an authored conditional two-jet argument.',
                      'global_PDE_numerically_solved': False,
                      'full_nonlinear_branch_proved': False,
                      'physical_chirality_derived': False}, sort_keys=True))
    raise SystemExit(0 if passed == total else 1)
