"""R53 finite identities: not a global differentiability or PDE solver."""
from functools import lru_cache
from pathlib import Path
import importlib.util
import json
import sympy as s


def zero(value):
    entries = list(value) if isinstance(value, s.MatrixBase) else [value]
    return all(s.simplify(x) == 0 for x in entries)


def comm(a, b):
    return a*b-b*a


def load(name, file):
    spec = importlib.util.spec_from_file_location(name, Path(__file__).with_name(file))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@lru_cache(None)
def jacobi_controls():
    H = s.Matrix([[1, 2+s.I], [2-s.I, -1]])
    psi = (s.diag(1, -1), s.Matrix([[0, 1], [1, 0]]))
    hp = (s.Matrix([[2, s.I], [-s.I, -2]]), s.Matrix([[0, 3], [3, 0]]))
    hpp = (s.diag(2, -2), s.Matrix([[0, s.I], [-s.I, 0]]))
    T = s.Matrix([[1, 1], [1, -1]])
    ppsi = (T, -T)  # sum derivative zero, hence moment zero at this point
    def direct(derivatives, tangent=H):
        return sum((-hpp[i]-comm(derivatives[i], tangent)-comm(psi[i], hp[i])
                    +comm(psi[i], hp[i]+comm(psi[i], tangent)) for i in range(2)), s.zeros(2))
    J = -sum(hpp, s.zeros(2))+sum((comm(p, comm(p, H)) for p in psi), s.zeros(2))
    gauge_of_hermitian = sum((-comm(ppsi[i], H)-comm(psi[i], hp[i])+comm(psi[i], hp[i])
                              for i in range(2)), s.zeros(2))
    wrong = sum((-hpp[i]-comm(ppsi[i], H)-comm(psi[i], hp[i])
                 -comm(psi[i], hp[i]+comm(psi[i], H)) for i in range(2)), s.zeros(2))
    energy = sum((s.trace(comm(p, H).conjugate().T*comm(p, H)) for p in psi), s.S.Zero)
    quad = s.trace(H.conjugate().T*sum((comm(p, comm(p, H)) for p in psi), s.zeros(2)))
    mu = -2*T
    return {
        'actual_noncommuting_matrices': not zero(comm(psi[0], H)) and not zero(comm(psi[0], hp[0])),
        'first_derivative_cross_terms_cancel': zero(direct(ppsi)-J),
        'hermitian_J_preserved': J == J.conjugate().T,
        'compact_J_preserved': (s.I*J).conjugate().T == -s.I*J,
        'compact_gauge_of_hermitian_gradient_zero': zero(gauge_of_hermitian),
        'nonharmonic_moment_remainder': zero(direct((T, T))-J-comm(mu, H)),
        'dropping_background_moment_rejected': not zero(direct((T, T))-J),
        'wrong_adjoint_sign_rejected': not zero(wrong-J),
        'positive_commutator_energy': zero(quad-energy) and s.simplify(energy).is_positive is True,
    }


@lru_cache(None)
def projection_controls():
    D = s.Matrix([[1, 0], [2, 0], [0, 1], [0, 3], [0, 0]])
    d1 = s.Matrix([[2, -1, 0, 0, 0]])
    c = s.Matrix([1, 2, 4, -1, 7])
    J = D.T*D
    primitive = J.inv()*D.T*c
    herm = s.Matrix([0, primitive[1]])
    compact = s.Matrix([primitive[0], 0])
    v = c-D*herm
    alpha = v-D*compact
    x, y = s.symbols('x y', real=True)
    shift = s.Matrix([x, y])
    pythagoras = ((alpha+D*shift).T*(alpha+D*shift))[0]-(alpha.T*alpha)[0]-(shift.T*J*shift)[0]
    exact = D*s.Matrix([3, -2])
    not_closed = s.Matrix([1, 0, 0, 0, 0])
    bad = not_closed-D*J.inv()*D.T*not_closed
    return {
        'chain_and_closed_tangent': zero(d1*D) and zero(d1*c),
        'positive_zero_form_operator': J == s.diag(5, 10),
        'metric_relaxation_only': (D.T*v)[1] == 0 and (D.T*v)[0] != 0,
        'combined_projection_harmonic': zero(D.T*alpha) and zero(d1*alpha),
        'nonzero_harmonic_velocity': (alpha.T*alpha)[0] > 0,
        'combined_green_formula': alpha == c-D*J.inv()*D.T*c,
        'kinetic_minimizing_projection': zero(pythagoras),
        'exact_tangent_zero_norm_control': zero(exact-D*J.inv()*D.T*exact),
        'nonclosed_tangent_not_harmonic': not zero(d1*bad),
        'singular_J_has_unforced_direction': s.diag(1, 0)*s.Matrix([0, 1]) == s.zeros(2, 1),
    }


@lru_cache(None)
def scaling_controls():
    B = s.symbols('B', nonnegative=True)
    # alpha=1/2, rho=(1+B)^-4. Scaled coefficients are B/(1+B)^n.
    exponents = (4, 6, 8, 10)
    certificates = []
    for n in exponents:
        poly = s.Poly(s.expand((1+B)**n-B), B)
        certificates.append(all(c >= 0 for c in poly.all_coeffs()) and poly.eval(0) == 1)
    old = load('r53_continuity_input', 'neutral_continuity.py')
    r = s.symbols('r', nonnegative=True)
    s0 = s.Rational(1, 16)
    polynomial = s.Poly((1+r)**8, r)
    integral = sum(coef*old.weighted_moment(power[0], s0, 4) for power,coef in polynomial.terms())
    direct = s.integrate((1+r)**8*s.exp(-(1-4*s0)*r), (r, 0, s.oo))
    h = s.symbols('h', positive=True)
    return {
        'scaled_lower_order_coefficients_bounded': all(certificates),
        'finite_power_rescaling_cost': zero(((1+B)**-4)**-2-(1+B)**8),
        'unrescaled_growth_not_uniform': (B/(1+B)**0).subs(B, 2) > 1,
        'derivative_envelope_improper_integral': zero(integral-direct) and integral > 0,
        'strict_margin_required': old.weighted_moment(8, s.Rational(1, 4), 4) == s.oo,
        'normalized_superlinear_anchor_slope_vanishes': s.limit(h/s.sqrt(h), h, 0, dir='+') == 0,
    }


@lru_cache(None)
def kinetic_controls():
    old = load('r53_parent_character_input', 'neutral_continuity.py')
    q, lam, t4, dual, _, total, weights, _, _, bracket, _ = old.parent_character_data()
    li = lam.inv()
    def variation(V):
        trV, dualV = s.trace(V), -s.trace(li*V*li)
        return s.simplify(trV*dual+t4*dualV+10*(t4*trV-s.trace(lam*V))+16*(trV+dualV))
    K = s.Matrix([[0, 1, 0, 0], [-1, 0, 1, 0], [0, -1, 0, 2], [0, 0, -2, 0]])
    D = s.diag(1, -3, 1, 1)
    rootnorm = sum(mult*weight**2 for weight,mult in weights.items())
    A = s.Matrix([[1, s.I], [-s.I, -1]])
    W = s.Matrix([[0, 2], [2, 0]])
    phi = A+s.I*W
    k0, v, q0 = s.symbols('k0 v q0', positive=True)
    return {
        'literal_q_velocity_detected': zero(variation(q*lam.diff(q))-q*s.diff(total, q)),
        'full_parent_conjugation_velocity_annihilated': zero(variation(comm(K, lam))),
        'actual_gauge_control_not_zero_matrix': not zero(comm(K, lam)),
        'character_velocity_nonzero_off_one': zero(q*s.diff(total, q)-(q-1/q)*bracket) and
            all(c > 0 for c in s.Poly(s.expand(q**3*bracket), q).all_coeffs()),
        'raw_parent_trace_factor': rootnorm == 60*s.trace(D*D) == 720,
        'complex_scalar_positive_kinetic_split': zero(s.trace(phi.conjugate().T*phi)-s.trace(A*A)-s.trace(W*W)),
        'real_scalar_canonical_factor': zero(k0*v*v-s.Rational(1, 2)*(s.sqrt(2*k0)*v)**2),
        'missing_real_factor_two_rejected': not zero(k0*v*v-s.Rational(1, 2)*(s.sqrt(k0)*v)**2),
        'log_parameter_chain_rule': zero(k0*(v/q0)**2-(k0/q0**2)*v*v),
    }


def controls():
    return dict(jacobi=jacobi_controls(), projection=projection_controls(),
                scaling=scaling_controls(), kinetic=kinetic_controls())


if __name__ == '__main__':
    groups = {name:{k:bool(v) for k,v in group.items()} for name,group in controls().items()}
    values = [v for group in groups.values() for v in group.values()]
    print(json.dumps(dict(checks=groups, passed=sum(values), total=len(values),
        all_checks_pass=all(values), global_PDE_numerically_solved=False,
        global_analytic_proof_machine_verified=False, numerical_kinetic_coefficient_computed=False,
        entire_fixed_base_curve_C1_proved=False, physical_chirality_derived=False), indent=2))
    raise SystemExit(0 if all(values) else 1)
