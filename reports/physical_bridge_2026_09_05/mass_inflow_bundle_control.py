"""R23 follow-on: characteristic-class control, not a singular determinant."""
from functools import lru_cache
import importlib.util
import json
from pathlib import Path
import time

import sympy as sp

SPEC = importlib.util.spec_from_file_location('r23_bundle_prior', Path(__file__).with_name('mass_inflow.py'))
m = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(m)
K = sp.Symbol('K')


@lru_cache(maxsize=1)
def characteristic_forms():
    weights = m.ac.data()['spinor']
    ell = [(w.T*m.ac.Z)[0] for w in weights]
    n = len(ell)
    p1, p2 = m.ac.P1, sp.Symbol('p2_T')
    ahat8 = (7*p1*p1-4*p2)/5760
    forms = {0: sp.Integer(n), 2: sum(ell),
             4: sum(x*x for x in ell)/2-n*p1/24,
             6: m.ac.anomaly(weights), 8: m.anomaly_forms()['I8']}
    series = sp.expand(-sum((-K)**j*forms[8-2*j]/sp.factorial(j) for j in range(5)))
    shifted = sp.expand(-sum((x-K)**4/24-p1*(x-K)**2/48 for x in ell)-n*ahat8)
    omitted = sp.expand(series-(-forms[8]+K*forms[6]))
    conjugate_mass = sp.expand(-sum((-x+K)**4/24-p1*(-x+K)**2/48 for x in ell)-n*ahat8)
    return dict(forms={j: sp.expand(v) for j, v in forms.items()}, B8=series,
                independent_weight_expression=shifted,
                polynomial_identity=sp.expand(series-shifted) == 0,
                omitted_terms=omitted, CPT_pair_invariant=sp.expand(conjugate_mass-series) == 0,
                inverse_line=sp.expand(series.subs(K, -K)),
                flat_sphere_reduction=sp.Poly(series, K).nth(0)+K*sp.Poly(series, K).nth(1))


def eigenbundle_response(splus, sminus, reference=1):
    if any(s not in (-1, 1) for s in (splus, sminus, reference)):
        raise ValueError('invertible signed eigenvalues required')
    plus = sum(K**j/sp.factorial(j) for j in range(5))
    minus = plus.subs(K, -K)
    answer = sp.expand(((splus-reference)*plus+(sminus-reference)*minus)/2)
    return dict(plus=plus, minus=minus, response=answer)


def four_spheres(gauge_flux=(2, 3, 4, 5), eigenline_flux=(1, 1, 1, 1)):
    if len(gauge_flux) != 4 or len(eigenline_flux) != 4 or any(
            not isinstance(x, int) for x in tuple(gauge_flux)+tuple(eigenline_flux)):
        raise ValueError('four integral gauge and eigenline fluxes required')
    x = sp.symbols('s0:4')
    f = sum(a*b for a, b in zip(gauge_flux, x))
    k = sum(a*b for a, b in zip(eigenline_flux, x))
    # The actual allowed cocharacter is C^-1 e0; its R-weight charges are w0.
    charges = [w[0] for w in m.ac.data()['spinor']]
    full = sp.expand(-sum((q*f-k)**4 for q in charges)/24)
    truncated = sp.expand(-sum((q*f)**4 for q in charges)/24+k*sum((q*f)**3 for q in charges)/6)
    monomial = sp.prod(x)
    integral = sp.Poly(full, *x).coeff_monomial(monomial)
    linear_integral = sp.Poly(truncated, *x).coeff_monomial(monomial)
    independent = -sum(sp.prod(q*a-b for a, b in zip(gauge_flux, eigenline_flux)) for q in charges)
    return dict(gauge_flux=gauge_flux, eigenline_flux=eigenline_flux,
                actual_charges=charges, integral=integral, product_formula=independent,
                truncated_integral=linear_integral, integral_class=integral.is_Integer)


def main():
    start = time.monotonic()
    out = dict(scope='conditional compact spin extension class; not full open-end determinant or anomaly completion',
               characteristic=characteristic_forms(),
               eigenbundles=[eigenbundle_response(a, b) for a, b in ((1, 1), (1, -1), (-1, 1), (-1, -1))],
               products=[four_spheres(), four_spheres(eigenline_flux=(1, 0, 0, 0)),
                         four_spheres(eigenline_flux=(0, 0, 0, 0)),
                         four_spheres(gauge_flux=(1, -2, 3, -4), eigenline_flux=(-1, 1, 2, 0))])
    out['seconds'] = time.monotonic()-start
    print(json.dumps(m.serial(out), indent=2))


if __name__ == '__main__':
    main()
