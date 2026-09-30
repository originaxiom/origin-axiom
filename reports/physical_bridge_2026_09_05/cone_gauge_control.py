"""R64 sign-inference repair; original source and failures stay unchanged."""
from functools import lru_cache
import importlib.util
from pathlib import Path
import json
import sympy as s

spec = importlib.util.spec_from_file_location('r64_original_sign_input', Path(__file__).with_name('cone_gauge.py'))
C = importlib.util.module_from_spec(spec)
spec.loader.exec_module(C)


@lru_cache(None)
def repair():
    eta = C.eta
    original = C.clean((C.r**(2*eta+1)-s.Symbol('v', positive=True)**(2*eta+1)).subs(
        {C.r: 2, s.Symbol('v', positive=True): 1}))
    expression = 2**(2*eta+1)-1
    derivative = s.diff(expression, eta)
    def certificate(expr):
        return bool(expr.subs(eta, 0)>0) and s.diff(expr, eta).is_positive is True
    checks = dict(
        kernel_positive_control=certificate(expression),
        original_expression_preserved=C.zero(original-expression),
        wrong_sign_rejected=not certificate(-expression) and (-derivative).is_negative is True,
        domain_boundary_rejected=expression.subs(eta, -s.Rational(1, 2))==0 and expression.subs(eta, -1)<0,
        diagnostic_unknown_not_false=original.is_positive is None and original.is_positive is not False,
    )
    return dict(checks={k: bool(v) for k, v in checks.items()},
                expression=expression, value_at_zero=expression.subs(eta, 0),
                derivative=derivative, original_sign_inference=original.is_positive,
                sympy_version=s.__version__)


@lru_cache(None)
def run():
    old, control = C.run(), repair()
    effective = dict(old['checks'])
    effective['volterra_kernel_positive_control'] = control['checks']['kernel_positive_control']
    effective.update({'repair_'+k: v for k, v in control['checks'].items() if k!='kernel_positive_control'})
    return dict(scope='Same R64 local mathematics, explicit monotonicity certificate; original failures retained',
                original_checks=old['checks'], original_all_checks_pass=old['all_checks_pass'],
                repair=control, effective_checks=effective,
                all_effective_checks_pass=all(effective.values()))


if __name__ == '__main__':
    result = run()
    print(json.dumps(C.r63.serial(result), indent=2))
    raise SystemExit(0 if result['all_effective_checks_pass'] else 1)
