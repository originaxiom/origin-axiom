"""R34 exact rational-normal-form diagnostic; original failed assertion stays."""
import importlib.util
import json
from pathlib import Path

import sympy as sp

SPEC = importlib.util.spec_from_file_location('r34_unchanged_quartic', Path(__file__).with_name('mirror_quartic.py'))
mq = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(mq)


def residual(left, right):
    expression = sp.sympify(left)-sp.sympify(right)
    if expression.has(sp.Float):
        raise ValueError('exact expressions required')
    return sp.cancel(sp.together(expression))


def stable_inverse(r, kappa, phi):
    r, kappa, phi = map(sp.sympify, (r, kappa, phi))
    if any(v.has(sp.Float) or v.free_symbols for v in (r, kappa, phi)):
        raise ValueError('exact numerical input required for this control')
    if r.is_real is not True or kappa.is_real is not True:
        raise ValueError('real r and kappa required')
    if sp.simplify(r-2*sp.Abs(kappa*phi)).is_positive is not True:
        raise ValueError('stable Gaussian requires r > 2 abs(kappa Phi)')
    return sp.simplify(1/(r*r-4*kappa*kappa*phi*sp.conjugate(phi)))


def check():
    g = mq.gaussian_controls()
    s = g['symbols']
    a, b, c, d = (s[x] for x in ('B_m', 'B_m_bar', 'B_p', 'B_p_bar'))
    r, k, P, Pb = (s[x] for x in ('r', 'kappa', 'Phi', 'Phi_bar'))
    ym, ymb, yp, ypb = (s[x] for x in ('y_m', 'y_m_bar', 'y_p', 'y_p_bar'))
    expected = r*(ym*a+ypb*d)*(ymb*b+yp*c)+k*P*(ym*a+ypb*d)**2+k*Pb*(ymb*b+yp*c)**2
    only_raw = sp.expand(g['numerator'].subs({yp: 0, ypb: 0}))
    only_expected = r*ym*ymb*a*b+k*P*ym**2*a**2+k*Pb*ymb**2*b**2
    wrong = expected-k*P*ym**2*a**2
    samples = ((3, 1, 1), (5, 2, (3+4*sp.I)/5), (1, 0, 1))
    invalid = ((2, 1, 1), (1, 1, 1), (-3, 1, 1))
    rejected = []
    for values in invalid:
        try:
            stable_inverse(*values)
        except ValueError:
            rejected.append(True)
        else:
            rejected.append(False)
    return dict(
        original_structural_equality=only_raw == sp.expand(only_expected),
        exact_mirror_residual=residual(only_raw, only_expected),
        full_numerator_residual=residual(g['numerator'], expected),
        zero_kappa_residual=residual(only_raw.subs(k, 0), r*ym*ymb*a*b),
        zero_Phi_residual=residual(only_raw.subs({P: 0, Pb: 0}), r*ym*ymb*a*b),
        changed_coefficient_rejected=residual(g['numerator'], wrong) != 0,
        stable_inverse_values=[stable_inverse(*values) for values in samples],
        singular_and_unstable_rejected=all(rejected),
        normalized_numerator=sp.expand(sp.cancel(g['numerator'])),
        domain='Rational identities at D != 0; convergent scalar elimination only for r > 2 abs(kappa Phi).')


def run():
    row = check()
    ok = (not row['original_structural_equality'] and all(row[k] == 0 for k in
          ('exact_mirror_residual', 'full_numerator_residual', 'zero_kappa_residual', 'zero_Phi_residual')) and
          row['changed_coefficient_rejected'] and row['singular_and_unstable_rejected'] and
          row['stable_inverse_values'] == [sp.Rational(1, 5), sp.Rational(1, 9), 1])
    return mq.mi.serial(dict(all_checks_pass=ok, row=row, sympy_version=sp.__version__,
        scope='Exact rational-expression diagnostic, not a new interaction or quantum result.'))


if __name__ == '__main__':
    result = run()
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result['all_checks_pass'] else 1)
