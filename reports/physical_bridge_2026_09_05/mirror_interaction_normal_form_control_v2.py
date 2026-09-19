"""R33 normal-form control v2: mutable negative fixture; failed v1 stays."""
import importlib.util
import json
from pathlib import Path

import sympy as sp

SPEC = importlib.util.spec_from_file_location(
    'r33_unchanged_interaction', Path(__file__).with_name('mirror_interaction.py'))
mi = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(mi)


def check(sign):
    S = sp.Matrix([1+sp.I, 2+2*sp.I]+[0]*8)
    mass = mi.mass_matrix(S, sign)
    raw_norm = (S.H*S)[0]
    norm = sp.expand(raw_norm)
    residual = mi.clean(mass.H*mass-raw_norm*sp.eye(16))
    mutant = sp.MutableDenseMatrix(mass)
    mutant[0, 0] += 1
    a, b = sp.symbols('a b', real=True)
    n = sp.Matrix([sp.Rational(3, 5), sp.Rational(4, 5)]+[0]*8)
    symbolic = mi.mass_matrix((a+sp.I*b)*n, sign)
    null = mi.mass_matrix([1, sp.I]+[0]*8, sign)
    return dict(sign=sign, raw_norm=raw_norm, expanded_norm=norm,
                original_structural_equality=mi.clean(mass.H*mass) == raw_norm*sp.eye(16),
                exact_residual_zero=residual == sp.zeros(16), rank=mass.rank(),
                changed_mass_rejected=mi.clean(mutant.H*mutant-norm*sp.eye(16)) != sp.zeros(16),
                symbolic_collinear=mi.clean(symbolic.H*symbolic-(a*a+b*b)*sp.eye(16)) == sp.zeros(16),
                noncollinear_counterexample=null.rank() == 8 and
                    mi.clean(null.H*null-2*sp.eye(16)) != sp.zeros(16))


def run():
    rows = [check(sign) for sign in (1, -1)]
    ok = all(r['expanded_norm'] == 10 and r['rank'] == 16 and all(r[k] for k in
        ('exact_residual_zero', 'changed_mass_rejected', 'symbolic_collinear', 'noncollinear_counterexample')) for r in rows)
    return mi.serial(dict(rows=rows, all_checks_pass=ok, sympy_version=sp.__version__,
        scope='Exact residual and two-sided controls; original test expression and failed outputs are unchanged.'))


if __name__ == '__main__':
    result = run()
    print(json.dumps(result, indent=2, sort_keys=True))
    raise SystemExit(0 if result['all_checks_pass'] else 1)
