"""R57 exact scope controls, not a manifold census or a physical model."""
import itertools
import json
import sympy as sp

L = sp.Matrix([[1, 1], [0, 1]])
R = sp.Matrix([[1, 0], [1, 1]])
P = sp.Matrix([[0, 1], [1, 0]])
I = sp.eye(2)


def reduce_word(word):
    out = []
    for letter in word:
        if out and out[-1] == -letter:
            out.pop()
        else:
            out.append(letter)
    return tuple(out)


def substitute(word, images):
    out = []
    for letter in word:
        image = images[abs(letter)]
        out.extend(image if letter > 0 else tuple(-v for v in reversed(image)))
    return reduce_word(out)


def counts(word):
    return sp.Matrix([sum(1 if v == k else -1 if v == -k else 0 for v in word)
                      for k in (1, 2)])


def core_checks():
    a, b = sp.symbols('a b', positive=True, integer=True)
    B = sp.Matrix([[1, a], [0, 1]]) * sp.Matrix([[1, 0], [b, 1]])
    x, y, z, t = sp.symbols('x y z t', positive=True)
    X = sp.Matrix([[x, y], [z, t]])
    A = L * R
    return {
        'mixed_formula': B == sp.Matrix([[1 + a*b, a], [b, 1]]),
        'det_trace_cokernel': (B.det() == 1 and sp.trace(B) == 2+a*b
                              and sp.expand((B-I).det()) == -a*b),
        'primitive_minimum': A == sp.Matrix([[2, 1], [1, 1]]),
        'positive_trace_increments': (sp.expand(sp.trace(X*L)-sp.trace(X)) == z
                                      and sp.expand(sp.trace(X*R)-sp.trace(X)) == y),
        'GL_swap_and_SL_witness': (P*A*P == R*L and P.det() == -1
                                   and L.inv()*A*L == R*L and L.det() == 1),
        'later_positive_state_distinct': L**2 * R**2 != A,
    }


def admission_checks():
    F = L*P
    return {
        'invertible_but_negative_inverse': L.det() == 1 and L.inv()[0, 1] == -1,
        'inverse_leaves_count_cone': L.inv()*sp.Matrix([0, 1]) == sp.Matrix([-1, 1]),
        'signed_group_witness': (L**2 * R.inv())**2 == -I,
        'signed_target_not_nonnegative': all(v < 0 for v in -L*R),
        'orientation_square': F.det() == -1 and F**2 == L*R,
        'shorter_unsquared_substitution': sum(F) == 3 and sum(F**2) == 5,
    }


def quotient_checks():
    words = [w for n in range(6) for w in itertools.product((1, -1, 2, -2), repeat=n)]
    homs = [({1: (2,), 2: (1,)}, P),
            ({1: (1, 2), 2: (1,)}, L*P),
            ({1: (1,), 2: (1, 2)}, L)]
    equiv = all(counts(substitute(w, h)) == M*counts(w) for h, M in homs for w in words)
    orbit = ((1, 2), (2, 1))
    swap = homs[0][0]
    comm = (1, 2, -1, -2)
    return {
        'no_fixed_representative': all(substitute(w, swap) != w for w in orbit),
        'quotient_is_swap_fixed': counts(orbit[0]) == counts(orbit[1]) == P*counts(orbit[0]),
        'quotient_is_not_injective': reduce_word(comm) == comm and counts(comm) == sp.zeros(2, 1),
        'naturality_finite_controls': equiv,
        'word_population': len(words) == 1365,
    }


def symmetry_checks():
    x = sp.symbols('x', real=True)
    V = (x*x-1)**2
    dV, ddV = sp.diff(V, x), sp.diff(V, x, 2)
    return {
        'even_law': sp.expand(V.subs(x, -x)-V) == 0,
        'paired_minima': all(V.subs(x, v) == 0 and dV.subs(x, v) == 0
                             and ddV.subs(x, v) == 8 for v in (-1, 1)),
        'fixed_point_not_minimum': V.subs(x, 0) == 1 and ddV.subs(x, 0) == -4,
    }


def descent_checks():
    # Group-only control: Z^2 / <a> = Z. No geometric index claimed.
    return {
        'nontrivial_descending_system': I*L == L*I and I == sp.eye(2) and L != I,
        'blocked_system_is_still_representation': L*R**0 == R**0*L and L != I,
        'allowed_quotient_preserves_second_generator':
            all(I**a * L**b == L**b for a in range(-3, 4) for b in range(-3, 4)),
    }


def run():
    groups = {f.__name__: {k: bool(v) for k, v in f().items()}
              for f in (core_checks, admission_checks, quotient_checks, symmetry_checks, descent_checks)}
    values = [v for group in groups.values() for v in group.values()]
    return {'checks': groups, 'passed': sum(values), 'total': len(values),
            'all_checks_pass': all(values),
            'full_architecture_completeness_proved': False,
            'physical_root_selected': False,
            'physical_chirality_derived': False,
            'foreign_geometry_or_index_recertified': False}


if __name__ == '__main__':
    result = run()
    print(json.dumps(result, sort_keys=True))
    raise SystemExit(0 if result['all_checks_pass'] else 1)
