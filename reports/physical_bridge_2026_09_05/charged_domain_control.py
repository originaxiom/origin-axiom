"""R16 separately sealed normal-form/quadrature controls; old files unchanged."""
from functools import lru_cache
import importlib.util
import json
import math
from pathlib import Path

import sympy as sp
from scipy.integrate import quad

_PATH = Path(__file__).with_name('charged_domain.py')
_SPEC = importlib.util.spec_from_file_location('charged_domain_original', _PATH)
base = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(base)
_ORIGINAL_SIMPLIFY = base.simplify


def simplify(value):
    result = _ORIGINAL_SIMPLIFY(value)
    if result != 0 and result.has(sp.sinh, sp.cosh, sp.tanh, sp.coth):
        exponential = sp.powsimp(result.rewrite(sp.exp), force=True)
        if sp.cancel(sp.together(exponential)) == 0:
            return sp.S.Zero
    return result


@lru_cache(maxsize=1)
def boundary_identities():
    r, a, HYP = base.r, base.a, base.HYP
    rows = {row['basis']: row for row in base.line_modes()}
    scalar, radial = rows[()]['coefficient'], rows[(0,)]['coefficient']
    chi = sp.Function('chi')(r)
    dH = {(0,): a/HYP.volume}
    L, eps, R = sp.symbols('L epsilon R', positive=True)
    weight = r**(2*L+1)
    primitive = -r**(-2*L)/(2*L)
    inverse_integral = primitive.subs(r, R)-primitive.subs(r, eps)
    minimizing_derivative = 1/(weight*inverse_integral)
    energy_primitive = primitive/inverse_integral**2
    energy = energy_primitive.subs(r, R)-energy_primitive.subs(r, eps)
    return dict(green_pair=simplify(HYP.volume*scalar*radial),
                radial_d_cutoff=HYP.dq({(0,): chi*radial}, dH),
                scalar_delta_cutoff=HYP.deltaq({(): chi*scalar}, dH),
                scalar_d_cutoff=HYP.dq({(): chi*scalar}, dH),
                radial_delta_cutoff=HYP.deltaq({(0,): chi*radial}, dH),
                capacity_inverse=1/inverse_integral,
                primitive_derivative=simplify(sp.diff(primitive, r)-1/weight),
                energy_primitive_derivative=simplify(sp.diff(energy_primitive, r)-weight*minimizing_derivative**2),
                capacity_energy_identity=simplify(energy-1/inverse_integral),
                cutoff_normalization=simplify((primitive.subs(r, R)-primitive.subs(r, eps))/inverse_integral))


@lru_cache(maxsize=1)
def numerical_norm_controls():
    rows = []
    outer = 0.01
    for charge in (-2, -1, -0.5, 0, 0.5, 1, 2):
        for mode in base.line_modes():
            j = mode['basis']
            exponent = float(mode['exponent'].subs(base.a, charge))
            for eps in (1e-4, 1e-6, 1e-8):
                lo, hi = math.log(eps), math.log(outer)
                p = 2*exponent+2
                shift = max(p*lo, p*hi)
                amplitude = math.exp(shift)
                exact = base.power_integral(2*exponent+1, eps, outer)
                flat_quad = amplitude*quad(lambda s: math.exp(p*s-shift), lo, hi,
                                          epsabs=0, epsrel=1e-12)[0]
                def hyperbolic(s):
                    radius = math.exp(s)
                    log_A, log_B = math.log(math.sinh(radius)), math.log(math.cosh(radius))
                    log_T = math.log(math.tanh(radius))
                    if 0 in j:
                        log_density = (2*charge*log_T + 2*(1 in j)*log_A
                                       + 2*(2 in j)*log_B-log_A-log_B)
                    else:
                        log_density = (-2*charge*log_T + log_A+log_B
                                       - 2*(1 in j)*log_A-2*(2 in j)*log_B)
                    return math.exp(log_density+s-shift)
                hyper = amplitude*quad(hyperbolic, lo, hi, epsabs=0, epsrel=1e-12)[0]
                rows.append(dict(a=charge, basis=j, epsilon=eps, outer=outer,
                                 exponent=exponent, integrable=base.integrable(exponent),
                                 flat_exact=exact, flat_quad=flat_quad, hyperbolic_quad=hyper,
                                 quadrature_relative_error=abs(flat_quad/exact-1),
                                 hyperbolic_relative_correction=abs(hyper/exact-1)))
    return rows


@lru_cache(maxsize=1)
def cusp_identities():
    F = sp.Function('F')(*base.COORDS)
    q = sp.Symbol('q', real=True)
    dH = base.exterior({(): q*F})
    metric = base.HYP
    scalar = {(): sp.exp(-q*F)}
    top = {(0, 1, 2): metric.volume*sp.exp(q*F)}
    z, C, c, U = sp.symbols('z C c U', positive=True)
    potential = U+C*z**2*sp.log(z)+c*z**2
    density = sp.exp(-2*q*potential)*z**(-3)
    log_density = -2*q*potential-3*sp.log(z)
    separated = sp.exp(-2*q*U)*sp.exp(-2*q*(C*z**2*sp.log(z)+c*z**2))*z**(-3)
    return dict(scalar_equation=metric.D(scalar, dH), top_equation=metric.D(top, dH),
                separated_norm_identity=sp.simplify(density-separated),
                exponential_log_identity=sp.simplify(sp.exp(log_density)/density-1),
                leading_log_density=sp.limit(log_density/(z**2*sp.log(z)), z, sp.oo))


base.simplify = simplify
base.boundary_identities = boundary_identities
base.numerical_norm_controls = numerical_norm_controls
base.cusp_identities = cusp_identities


if __name__ == '__main__':
    out = base.run()
    out['instrument_control'] = 'separate exponential-normal-form, elementary-primitive and scaled-quadrature repair'
    print(json.dumps(out, indent=2, sort_keys=True), flush=True)
