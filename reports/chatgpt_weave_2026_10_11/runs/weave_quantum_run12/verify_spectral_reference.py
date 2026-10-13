#!/usr/bin/env python3
"""Independent spectral construction for the higher-trace domain control.

Uses smooth sine partial sums instead of the first instrument's boundary
layers. This checks a scalar operator channel, not the silver eigenvalues.
"""
from pathlib import Path
import json
import sympy as s

r = s.symbols('r', real=True)
n = s.symbols('n', integer=True, positive=True)
f = r*(1-r)
c = s.simplify(2*s.integrate(f*s.sin(n*s.pi*r),(r,0,1)))
expected = 4*(1-(-1)**n)/(s.pi**3*n**3)
checks = {}
def put(name, value):
    checks[name] = bool(value)
    print(('PASS ' if value else 'FAIL ')+name)
put('exact_sine_coefficient', s.simplify(c-expected)==0)
for N in (1,3,7):
    partial = sum(expected.subs(n,k)*s.sin(k*s.pi*r) for k in range(1,N+1))
    put(f'smooth_spectral_core_N{N}', partial.subs(r,0)==0 and partial.subs(r,1)==0
        and partial.diff(r,2).subs(r,0)==0 and partial.diff(r,2).subs(r,1)==0)
L2sum = s.simplify(32/s.pi**6*(1-s.Rational(1,64))*s.zeta(6))
D2sum = s.simplify(32/s.pi**2*(1-s.Rational(1,4))*s.zeta(2))
put('Parseval_L2_equals_polynomial', L2sum==s.integrate(f*f,(r,0,1)))
put('Parseval_graph_derivative_equals_polynomial', D2sum==s.integrate(f.diff(r,2)**2,(r,0,1)))
put('limit_fails_secondary_trace', f.diff(r,2).subs(r,0)==-2 and f.diff(r,2).subs(r,1)==-2)
result = {'status':'PASS' if all(checks.values()) else 'FAIL','checks':checks,
          'exact_checks_passed':sum(checks.values()),'exact_checks_total':len(checks),
          'coefficient':str(c),'limit_L2_norm_squared':str(L2sum),
          'limit_second_derivative_norm_squared':str(D2sum),
          'graph_convergence_argument':'The nonnegative Parseval tails tend to zero.',
          'same_author_separate_construction':True,'silver_spectrum_computed':False}
Path(__file__).with_name('SPECTRAL_REFERENCE_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
raise SystemExit(0 if all(checks.values()) else 1)
