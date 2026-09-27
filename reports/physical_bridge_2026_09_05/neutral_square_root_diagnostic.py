"""R52 post-result fixture diagnosis; separately sealed before execution."""
from functools import lru_cache
import importlib.util
import json
from pathlib import Path
import sympy as s

spec = importlib.util.spec_from_file_location('r52_square_original', Path(__file__).with_name('neutral_continuity.py'))
original = importlib.util.module_from_spec(spec)
spec.loader.exec_module(original)


@lru_cache(None)
def controls():
    S = s.Matrix([[2, 1], [1, 1]])
    bad = s.Matrix([[1, 2], [2, -1]])
    X, Y = s.diag(1, -1), s.Matrix([[0, 3], [3, 2]])
    t = s.symbols('t', real=True)
    curve = S+t*X+t*t*Y/2
    K = curve*curve
    kp, kpp = K.diff(t).subs(t, 0), K.diff(t, 2).subs(t, 0)
    xp = original.sylvester(S, kp)
    ypp = original.sylvester(S, kpp-2*xp*xp)
    u, v, w = s.symbols('u v w', real=True)
    generic = s.Matrix([[u, v], [v, w]])
    rot = s.Matrix([[s.Rational(3, 5), -s.Rational(4, 5)], [s.Rational(4, 5), s.Rational(3, 5)]])
    pos = rot*s.diag(1, 4)*rot.T
    op = s.kronecker_product(pos, s.eye(2))+s.kronecker_product(s.eye(2), pos)
    expected_old_failures = {'noncommuting_example', 'commuting_shortcut_rejected'}
    return {
        'original_fixture_is_polynomial_in_S': bad == 2*S-3*s.eye(2),
        'original_fixture_commutes': S*bad == bad*S,
        'original_failures_preserved': {k for k,v in original.matrix_controls().items() if not v} == expected_old_failures,
        'replacement_commutator_explicit': S*X-X*S == s.Matrix([[0, -2], [2, 0]]),
        'positive_S': S.det() == 1 and S[0, 0] > 0,
        'direct_first_derivative': kp == S*X+X*S,
        'first_solution_noncommuting': xp == X,
        'direct_second_derivative': kpp == S*Y+Y*S+2*X*X,
        'second_solution_noncommuting': ypp == Y,
        'commuting_shortcut_rejected': not original.zero(S.inv()*kp/2-X),
        'second_product_omission_rejected': original.sylvester(S, kpp) != Y,
        'fully_symbolic_symmetric_tangent': original.zero(original.sylvester(S, S*generic+generic*S)-generic),
        'positive_sylvester_spectrum': rot.T*rot == s.eye(2) and op.eigenvals() == {s.S(2):1,s.S(5):2,s.S(8):1},
    }


if __name__ == '__main__':
    checks = {k:bool(v) for k,v in controls().items()}
    print(json.dumps(dict(checks=checks, passed=sum(checks.values()), total=len(checks),
        all_checks_pass=all(checks.values()), original_fixture_repaired_in_place=False,
        global_analytic_proof_machine_verified=False), indent=2))
    raise SystemExit(0 if all(checks.values()) else 1)
