"""R63 separate polynomial-generator repair; original failures remain visible."""
from functools import lru_cache
import importlib.util
from pathlib import Path
import json
import sympy as s

spec = importlib.util.spec_from_file_location('r63_original', Path(__file__).with_name('cone_spectrum.py'))
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)


@lru_cache(maxsize=1)
def polynomial_controls():
    p1, p2, q1, q2 = s.symbols('p1 p2 q1 q2', real=True)
    z = s.Matrix([p1+s.I*q1, p2+s.I*q2])
    lam = s.expand((z.H*z)[0])
    _, _, A = base.operators(z, 0)
    polynomial = A.charpoly('t')
    t = polynomial.gen
    expected = ((t*t-lam)**2-t*t)**2
    original = base.spectrum_controls()['polynomial']
    L = base.wedge_matrix(z)+base.wedge_matrix(z).H
    wrong = s.BlockMatrix([[base.P, -L], [-L, -base.P]]).as_explicit().charpoly(t)
    requested = s.Symbol('t', real=True)
    toy = s.eye(2).charpoly(requested)
    checks = dict(characteristic_polynomial=s.Poly(polynomial.as_expr()-expected, t).is_zero,
                  wrong_density_shift_rejected=not s.Poly(wrong.as_expr()-expected, t).is_zero,
                  original_polynomial_unchanged=s.Poly(polynomial.as_expr()-original, t).is_zero,
                  wrong_coefficient_rejected=not s.Poly(polynomial.as_expr()-expected-t*t, t).is_zero,
                  diagnostic_mismatch_reproduced=toy.gen!=requested and s.expand(toy.as_expr()-(requested-1)**2)!=0,
                  diagnostic_generator_equality=s.Poly(toy.as_expr()-(toy.gen-1)**2, toy.gen).is_zero)
    return dict(checks={k: bool(v) for k, v in checks.items()}, polynomial=s.factor(polynomial.as_expr()),
                generator_assumptions=t.assumptions0, requested_assumptions=requested.assumptions0,
                sympy_version=s.__version__)


def run():
    original = base.run()
    repair = polynomial_controls()
    effective = dict(original['checks'])
    for name in ('characteristic_polynomial', 'wrong_density_shift_rejected'):
        effective['spectrum_'+name] = repair['checks'][name]
    for name in ('original_polynomial_unchanged', 'wrong_coefficient_rejected',
                 'diagnostic_mismatch_reproduced', 'diagnostic_generator_equality'):
        effective['repair_'+name] = repair['checks'][name]
    return base.serial(dict(scope='Same R63 mathematics with returned-generator comparisons; original failures preserved',
                            original_checks=original['checks'], original_all_checks_pass=original['all_checks_pass'],
                            repair=repair, effective_checks=effective, all_effective_checks_pass=all(effective.values())))


if __name__ == '__main__':
    data = run()
    print(json.dumps(data, indent=2))
    raise SystemExit(0 if data['all_effective_checks_pass'] else 1)
