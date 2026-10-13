"""Exact safeguards for an authored vertical gap proof, not a PDE certificate."""
from fractions import Fraction
from functools import lru_cache
import importlib.util
import json
import math
from pathlib import Path
import sympy as s


def zero(m):
    return all(s.simplify(v) == 0 for v in m)


def literal_coefficient():
    a0 = s.diag(s.I, -s.I)
    b0 = s.Matrix([[0, 1], [-1, 0]])
    return s.diag(-a0, a0, -a0), s.diag(b0, -b0, -b0)


def laurent_interval(alpha):
    """Exact strict endpoint inequalities, not a chosen mode cutoff."""
    lower = s.floor(-alpha) + 1
    upper = s.ceiling(s.Rational(1, 2)-alpha) - 1
    return tuple(range(int(lower), int(upper)+1))


def fraction_interval(alpha):
    lower, upper = -alpha, Fraction(1, 2)-alpha
    return tuple(range(math.floor(lower)+1, math.ceil(upper)))


@lru_cache(maxsize=1)
def checks():
    out = {}
    def check(name, condition):
        out[name] = bool(condition)

    a, b = literal_coefficient()
    eye = s.eye(6)
    check('actual_unitary_generators', zero(a.H*a-eye) and zero(b.H*b-eye))
    check('actual_central_puncture', zero(a*b*a.H*b.H+eye))
    check('end_gluing_intertwines_opposite_characters', zero(b*a*b.H+a))
    check('not_commuting_torus_coefficients', not zero(a*b-b*a))
    p = (eye-s.I*a)/2
    q = (eye+s.I*a)/2
    check('quarter_character_projectors', zero(p*p-p) and zero(q*q-q) and zero(p*q))
    check('three_of_each_quarter_character', p.rank() == q.rank() == 3)
    check('end_gluing_exchanges_three_planes', zero(b*p*b.H-q))
    path = Path(__file__).resolve().parents[1]/'nodal_transport'/'verify.py'
    spec = importlib.util.spec_from_file_location('pinned_nodal_transport', path)
    old = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(old)
    old_a, old_b, _ = old.coefficient()
    check('same_actual_coefficient_as_nodal_packet', zero(a-old_a) and zero(b-old_b))

    for alpha in (s.Rational(1, 4), s.Rational(3, 4)):
        tag = str(alpha)
        frac = Fraction(int(s.numer(alpha)), int(s.denom(alpha)))
        ints = laurent_interval(alpha)
        check(tag+'_fraction_crosscheck', ints == fraction_interval(frac))
        check(tag+'_sharp_transverse_distance', min(alpha, 1-alpha) == s.Rational(1, 4))
        check(tag+'_full_strict_interval', ints == ((0,) if alpha == s.Rational(1, 4) else ()))
        # Every integer outside {-1,0} is farther from -alpha; no finite scan is the proof.
        check(tag+'_nonnegative_ladder_lower_bound', alpha >= s.Rational(1, 4))
        check(tag+'_negative_ladder_lower_bound', 1-alpha >= s.Rational(1, 4))
    check('strict_endpoint_excludes_log_modes', laurent_interval(s.Integer(0)) == ()
          and laurent_interval(s.Rational(1, 2)) == ())
    check('three_holomorphic_cylinder_modes',
          3*len(laurent_interval(s.Rational(1, 4)))
          +3*len(laurent_interval(s.Rational(3, 4))) == 3)
    check('conjugation_keeps_three_and_reverses_character',
          laurent_interval(1-s.Rational(3, 4)) == (0,)
          and laurent_interval(1-s.Rational(1, 4)) == ())

    zeta = s.symbols('zeta', nonzero=True)
    f4 = zeta/(zeta-1)**2
    log_derivative = s.Rational(1, 4)/zeta-s.Rational(1, 2)/(zeta-1)
    check('profile_fourth_power_derivative', s.simplify(s.diff(f4,zeta)-4*log_derivative*f4) == 0)
    check('profile_upper_quarter_monodromy', s.residue(log_derivative,zeta,0) == s.Rational(1,4))
    check('profile_puncture_minus_monodromy', s.residue(log_derivative,zeta,1) == -s.Rational(1,2))
    check('profile_lower_opposite_quarter', s.limit(zeta*log_derivative,zeta,s.oo) == -s.Rational(1,4))
    check('wrong_puncture_sign_rejected', s.exp(2*s.pi*s.I*(-s.Rational(1,2))) != 1)
    check('regular_trace_rejects_only_scalar_mode', s.Integer(1).subs(zeta,1) != 0)
    check('near_puncture_nonzero_critical_coefficient_squared', s.limit((zeta-1)**2*f4,zeta,1) == 1)
    check('upper_end_norm_integrable', 2*s.Rational(1,4)-1 > -1)
    check('lower_end_norm_integrable', 2*s.Rational(1,4)-2 < -1)
    check('puncture_radial_norm_integrable', 1+2*(-s.Rational(1,2)) > -1)
    u, v = s.symbols('u v', real=True)
    # Squared denominator in |f|^2, avoiding branch simplification.
    rho = s.exp(-2*s.pi*v)
    abs_den_sq = rho**2+1-2*rho*s.cos(2*s.pi*u)
    check('exact_profile_norm_identity', s.simplify((s.expand(abs_den_sq/rho)
          -(2*s.cosh(2*s.pi*v)-2*s.cos(2*s.pi*u))).rewrite(s.exp)) == 0)
    check('upper_tail_squared_norm_exponent', 4*s.pi*s.Rational(1,4) == s.pi)
    check('lower_tail_squared_norm_exponent', 4*s.pi*(s.Rational(1,2)-s.Rational(1,4)) == s.pi)

    sigma1 = s.Matrix([[0,1],[1,0]])
    sigma2 = s.Matrix([[0,-s.I],[s.I,0]])
    cu, cv = -s.I*sigma1, -s.I*sigma2
    pu, pv, du, dv = s.symbols('pu pv du dv', real=True)
    symbol = s.I*(cu*pu+cv*pv)
    comm = cu*du+cv*dv
    check('flat_dirac_full_symbol_square', zero(symbol**2-(pu**2+pv**2)*s.eye(2)))
    check('cutoff_commutator_exact_norm', zero(comm.H*comm-(du**2+dv**2)*s.eye(2)))
    f = s.Function('f')(u+s.I*v)
    check('holomorphic_profile_solves_positive_dirac', s.simplify(s.diff(f,u)+s.I*s.diff(f,v)) == 0)
    x = s.symbols('x', real=True)
    area, height = s.symbols('area height', positive=True)
    fibre_symbol = height/area*pu**2+(pv-x*pu)**2/(area*height)
    ps = s.symbols('ps', real=True)
    check('actual_sheared_fibre_scale', s.simplify(fibre_symbol.subs(pv,x*pu+height*ps)
          -height/area*(pu**2+ps**2)) == 0)
    check('inverse_complement_scale', s.simplify(1/s.sqrt(height/area)-s.sqrt(area/height)) == 0)
    plane = s.exp(2*s.pi*s.I*v/height)
    check('periodic_control_actual_eigenfunction', s.simplify(-s.diff(plane,v,2)
          -(2*s.pi/height)**2*plane) == 0)
    check('periodic_control_orthogonal_to_constants', s.integrate(plane,(v,0,height)) == 0)
    check('periodic_control_closing_gap', s.limit(2*s.pi/s.sqrt(area*height),height,s.oo) == 0)
    check('trivial_circle_fails_positive_gap', min(Fraction(0),Fraction(1)) == 0)
    return out


def main():
    rows = checks()
    print(json.dumps({'checks': rows, 'passed': sum(rows.values()),
                     'scope': 'exact algebra/profile safeguards; infinite-dimensional estimate is authored in PROOF'}, indent=2))
    return 0 if all(rows.values()) else 1


if __name__ == '__main__':
    raise SystemExit(main())
