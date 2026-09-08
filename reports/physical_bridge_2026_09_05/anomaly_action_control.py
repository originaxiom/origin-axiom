"""Action-level derivations for R21; original source remains immutable."""
import importlib.util
import json
from pathlib import Path

import sympy as sp

SPEC = importlib.util.spec_from_file_location(
    'r21_action_prior', Path(__file__).with_name('anomaly_completion.py'))
ac = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(ac)


def kinetic():
    f, rho, theta, q, A, dr, dt, g, B, lam = sp.symbols(
        'f rho theta q A dr dt g B lambda', real=True)
    x, y = (f+rho)*sp.cos(theta), (f+rho)*sp.sin(theta)
    dx, dy = dr*sp.cos(theta)-(f+rho)*dt*sp.sin(theta), dr*sp.sin(theta)+(f+rho)*dt*sp.cos(theta)
    norm = sp.trigsimp(((dx+q*A*y)**2+(dy-q*A*x)**2)/2)
    expected = (dr**2+(f+rho)**2*(dt-q*A)**2)/2
    mass2 = sp.simplify(sp.diff(norm.subs({q: 4, A: g*B, rho: 0, dt: 0, dr: 0}), B, 2))
    potential = lam*(((f+rho)**2-f*f)/2)**2
    z = sp.Symbol('z', nonzero=True)
    phi, dphi, de = sp.symbols('Phi dPhi d_epsilon')
    transformed = z**4*(dphi+4*sp.I*de*phi)-4*sp.I*(A+de)*z**4*phi
    derivative = dphi-4*sp.I*A*phi
    return dict(polar_kinetic=sp.expand(norm), polar_identity=sp.simplify(norm-expected) == 0,
                gauge_mass_squared=mass2, gauge_mass_check=sp.simplify(mass2-16*g*g*f*f) == 0,
                potential_radial_first=sp.diff(potential, rho).subs(rho, 0),
                potential_radial_second=sp.diff(potential, rho, 2).subs(rho, 0),
                potential_phase_second=sp.diff(potential, theta, 2),
                finite_gauge_covariance=sp.expand(transformed-z**4*derivative) == 0,
                missing_connection_fails=sp.expand(z**4*(dphi+4*sp.I*de*phi)-z**4*dphi) != 0)


def masses():
    f, M, yv, yn = sp.symbols('f M yV yN', positive=True)
    z = sp.Symbol('phase', nonzero=True)
    phi, phibar = f*z/sp.sqrt(2), f/(z*sp.sqrt(2))
    mV, mN = yv*phi, yn*phibar**2/M
    gauge_phase = sp.Symbol('gauge_phase', nonzero=True)
    D = ac.data()
    projected = [w-sp.Rational(3, 4)*w[0]*D['u'] for w in D['spinor']]
    opposite_pairs = [(i, j) for i, v in enumerate(projected) for j, w in enumerate(projected)
                      if v+w == sp.zeros(6, 1)]
    return dict(vector_mass_at_zero_phase=mV.subs(z, 1),
                singlet_mass_at_zero_phase=mN.subs(z, 1),
                vector_phase_cancellation=sp.cancel(mV.subs(z, z*gauge_phase**4)*gauge_phase**(-4)-mV) == 0,
                singlet_phase_cancellation=sp.cancel(mN.subs(z, z*gauge_phase**4)*gauge_phase**8-mN) == 0,
                wrong_singlet_conjugation_fails=sp.cancel((yn*phi**2/M).subs(z, z*gauge_phase**4)*gauge_phase**8-yn*phi**2/M) != 0,
                spinor_opposite_weight_pairs=opposite_pairs)


def descent():
    r = ac.anomaly_controls()
    theta, epsilon = sp.symbols('theta epsilon')
    c = r['character']/4
    light_variation = sp.cancel(sp.I*epsilon*r['spinor_I6']/c)
    local_term = -sp.I*theta*r['X4']
    variation = sp.expand(local_term.subs(theta, theta+4*epsilon)-local_term)
    wrong = sp.expand(local_term.subs(theta, theta+3*epsilon)-local_term)
    return dict(light_variation=light_variation, counterterm_variation=variation,
                cancellation=sp.expand(light_variation+variation) == 0,
                missing_counterterm_fails=light_variation != 0,
                wrong_charge_fails=sp.expand(light_variation+wrong) != 0)


def residual():
    d = ac.data()
    h = d['u']/3
    phases = [ac.fractional((w.T*d['C']*h)[0]) for w in d['spinor']]
    quotient_phase = ac.fractional((ac.singlet_weight(4).T*d['C']*h)[0])
    order = sp.ilcm(*[(d['C']*h)[i].q for i in range(6)])
    return dict(spinor_phase_exponents=phases, quotient_phase=quotient_phase,
                gauge_element_order=order, cube_in_kernel=3*quotient_phase % 1 == 0,
                generator_outside_spin10=quotient_phase != 0)


def run():
    return ac.serial(dict(kinetic=kinetic(), masses=masses(), descent=descent(), residual=residual()))


if __name__ == '__main__':
    print(json.dumps(run(), indent=2, sort_keys=True))
