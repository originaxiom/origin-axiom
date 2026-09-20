"""Post-failure primitive check; leaves the sealed R16 implementation alone."""
import json
import sympy as s

r, L, eps, R = s.symbols('r L epsilon R', positive=True)
I = (eps**(-2*L)-R**(-2*L))/(2*L)
w = r**(2*L+1)
dchi = 1/(w*I)
energy_primitive = -r**(-2*L)/(2*L*I**2)
normal_primitive = -r**(-2*L)/(2*L*I)
checks = {
    'energy_derivative_residual': s.simplify(s.diff(energy_primitive, r)-w*dchi**2),
    'normalization_derivative_residual': s.simplify(s.diff(normal_primitive, r)-dchi),
    'energy_endpoint_residual': s.simplify(energy_primitive.subs(r, R)-energy_primitive.subs(r, eps)-1/I),
    'normalization_endpoint_residual': s.simplify(normal_primitive.subs(r, R)-normal_primitive.subs(r, eps)-1),
}
assert all(a == 0 for a in checks.values())
mutant = s.simplify(s.diff(energy_primitive/2, r)-w*dchi**2)
assert mutant != 0
control = s.simplify((1/I).subs({L: s.Rational(1, 2), eps: s.Rational(1, 10), R: s.Rational(3, 5)}))
assert control == s.Rational(3, 25)
print(json.dumps({'sympy': s.__version__, 'residuals': {k: str(a) for k, a in checks.items()},
                  'half_primitive_mutant_rejected': True, 'exact_capacity_control': str(control),
                  'original_R16_test_still_failed': True}, indent=2))
