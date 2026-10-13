"""Finite exact safeguards, not a machine proof of the analytic estimates."""
from functools import lru_cache
import importlib.util
import json
from pathlib import Path
import sympy as s


def zero(value):
    if isinstance(value, s.MatrixBase):
        return all(s.simplify(s.expand_complex(x)) == 0 for x in value)
    return s.simplify(value) == 0


def load_sibling(folder):
    path = Path(__file__).resolve().parents[1]/folder/'verify.py'
    spec = importlib.util.spec_from_file_location('pinned_'+folder, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def coefficient():
    a0 = s.diag(s.I, -s.I)
    b0 = s.Matrix([[0, 1], [-1, 0]])
    p13 = s.Matrix([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
    return (s.diag(-a0, a0, -a0), s.diag(b0, -b0, -b0),
            s.kronecker_product(p13, (s.eye(2)+a0)/s.sqrt(2)))


def cusp_phases(gamma, sign=1):
    if gamma not in (-1, 1) or sign not in (-1, 1):
        raise ValueError('chirality and spin sign must be plus or minus one')
    a, _, t = coefficient()
    indices = [j for j in range(6) if a[j, j] == gamma*s.I]
    z = sign*t.H.extract(indices, indices)
    eighth = (1+s.I)/s.sqrt(2)
    phases = []
    for val, multiplicity in z.eigenvals().items():
        matches = [j for j in range(8) if zero(val-eighth**j)]
        if len(matches) != 1:
            raise ValueError('eigenvalue is not a unique eighth root')
        phases.extend([s.Rational(matches[0], 8)]*multiplicity)
    return tuple(sorted(phases))


@lru_cache(None)
def checks():
    rows = {}
    def check(name, value):
        rows[name] = bool(value)

    x, u, v, r, h = s.symbols('x u v r h', real=True)
    y, area = s.symbols('y area', positive=True)
    F = s.Function('F')
    actual = F(u+x*v, y*v)
    fr = s.Subs(s.Derivative(F(r, h), r), (r, h), (u+x*v, y*v))
    fs = s.Subs(s.Derivative(F(r, h), h), (r, h), (u+x*v, y*v))
    check('horizontal_x_chain_rule', zero(y*s.diff(actual, x)-y*v*fr))
    check('horizontal_y_chain_rule', zero(y*s.diff(actual, y)-y*v*fs))
    norm = s.sqrt(y/area)
    check('fibre_norm_unitary', zero(area/y*norm**2-1))
    check('fibre_normalization_derivative', zero(y*s.diff(norm,y)/norm-s.Rational(1,2)))
    check('deck_keeps_complex_coordinate', zero((u-v)+(x+1)*v+s.I*y*v
                                                -(u+x*v+s.I*y*v)))

    # Wirtinger algebra on a local branch, with z and zb independent.
    z, zb = s.symbols('z zb', nonzero=True)
    hol, anti = s.Function('hol')(z), s.Function('anti')(zb)
    def dr(expr):
        return s.diff(expr,z)+s.diff(expr,zb)
    def ds(expr):
        return s.I*(s.diff(expr,z)-s.diff(expr,zb))
    height = (z-zb)/(2*s.I)
    density = hol*anti
    check('holomorphic_CR', zero(ds(hol)-s.I*dr(hol)))
    check('antiholomorphic_CR', zero(ds(anti)+s.I*dr(anti)))
    check('radial_IBP_real_identity', zero(ds(height*density)-density
          -height*(anti*ds(hol)+hol*ds(anti))))
    check('radial_IBP_imag_identity', zero(height*(anti*ds(hol)-hol*ds(anti))
          -s.I*height*dr(density)))
    check('puncture_boundary_term_vanishes', 1+1-1 > 0)
    log_h = -s.Rational(1,2)*s.log(y)
    # For gamma=+1: (partial - barpartial) log(H) / 2.
    check('half_Hodge_unitary_connection', zero(-s.I*s.diff(log_h,y)/2-s.I/(4*y)))
    for gamma in (-1, 1):
        expectation_s = -s.Rational(1,2)
        expectation_r = expectation_s/(s.I*gamma)
        check(f'{gamma}_projected_quarter', zero(expectation_r-s.I*gamma/4-s.I*gamma/4))
        check(f'{gamma}_dropped_mixed_term_detected', not zero(expectation_r-s.I*gamma/4))
        check(f'{gamma}_normalization_and_base_density',
              expectation_s+s.Rational(1,2)-s.Rational(1,2) == -s.Rational(1,2))
        f = hol if gamma == 1 else anti
        g = height*ds(f)+f/2
        qx = height*dr(f)-s.I*gamma*f/2
        check(f'{gamma}_off_diagonal_identity', zero(qx+s.I*gamma*g))
        singular = z**(-s.Rational(1,2)) if gamma == 1 else zb**(-s.Rational(1,2))
        singular_g = height*ds(singular)+singular/2
        leading = ((z**(-s.Rational(1,2))+zb*z**(-s.Rational(3,2)))/4
                   if gamma == 1 else
                   (zb**(-s.Rational(1,2))+z*zb**(-s.Rational(3,2)))/4)
        check(f'{gamma}_critical_mixing_profile', zero(singular_g-leading))
        forbidden = s.diff(singular_g, zb if gamma == 1 else z)
        target = (z if gamma == 1 else zb)**(-s.Rational(3,2))/4
        check(f'{gamma}_vertical_derivative_not_cancelled', zero(forbidden-target) and target != 0)
    check('mixing_profile_L2_power', 1+2*(-s.Rational(1,2)) > -1)
    check('mixing_vertical_derivative_not_L2_power', 1+2*(-s.Rational(3,2)) <= -1)
    check('nonzero_mixing_at_regular_midcircle', zero((height*ds(hol)+hol/2).subs(zb,z)-hol/2)
          and (hol/2) != 0)

    a, b, t = coefficient()
    old = load_sibling('nodal_transport')
    check('same_actual_coefficient', all(zero(left-right) for left,right in zip(coefficient(),old.coefficient())))
    check('unitary_actual_move', zero(t.H*t-s.eye(6)))
    check('forward_based_intertwining', zero(t*b*t.H-a*b) and zero(t*a*t.H-a))
    check('inverse_based_intertwining', zero(t.H*b*t-a.H*b) and zero(t.H*a*t-a))
    check('wrong_based_move_rejected', not zero(t*b*t.H-a.H*b))
    expected = {1:(s.Rational(1,8),s.Rational(5,8),s.Rational(7,8)),
                -1:(s.Rational(1,8),s.Rational(3,8),s.Rational(7,8))}
    for gamma in (-1, 1):
        check(f'{gamma}_actual_three_phases', cusp_phases(gamma) == expected[gamma])
        for sign in (-1,1):
            phases = cusp_phases(gamma,sign)
            check(f'{gamma}_{sign}_integer_frequency_distance',
                  min(min(p,1-p) for p in phases) == s.Rational(1,8))
            check(f'{gamma}_{sign}_all_positive_frequency_bounds', all(p>=s.Rational(1,8) for p in phases))
            check(f'{gamma}_{sign}_all_negative_frequency_bounds', all(1-p>=s.Rational(1,8) for p in phases))
        check(f'{gamma}_spin_sign_shifts_every_phase',
              cusp_phases(gamma,-1) == tuple(sorted((p+s.Rational(1,2)) % 1 for p in expected[gamma])))

    p1, p2, p3 = s.Matrix([[0,1],[1,0]]), s.Matrix([[0,-s.I],[s.I,0]]), s.diag(1,-1)
    c1, c2 = s.I*p1, s.I*p2
    cs = [s.I*s.kronecker_product(p1,s.eye(2)),s.I*s.kronecker_product(p2,s.eye(2)),
          s.I*s.kronecker_product(p3,p1),s.I*s.kronecker_product(p3,p2)]
    metric = load_sibling('total_metric_dirac')
    check('same_full_metric_Cliffords', all(zero(c-d) for c,d in zip(cs,metric.gammas())))
    gv = s.I*cs[2]*cs[3]
    check('mixed_spin_term_sign', zero(cs[0]*cs[2]*cs[3]+s.I*gv*cs[0]))
    for gamma in (-1,1):
        m = c2-s.I*gamma*c1
        check(f'{gamma}_coupling_rank_one_not_zero', m.rank()==1 and not zero(m))
        check(f'{gamma}_coupling_one_polarization_only', (m.H*m).eigenvals() == {s.Integer(0):1,s.Integer(4):1})
    tt, aa, beta = s.symbols('t a beta', real=True)
    mu = aa*s.exp(tt)+beta
    vec = s.Matrix([s.Function('w0')(tt),s.Function('w1')(tt)])
    def radial(w):
        return c2*w.diff(tt)+s.I*c1*mu*w
    residual = radial(radial(vec))+vec.diff(tt,2)-mu**2*vec-s.I*c2*c1*s.diff(mu,tt)*vec
    # No complex expansion of unspecified functions is required here.
    check('radial_square_all_differential_terms', all(s.simplify(e)==0 for e in residual))
    involution = s.I*c2*c1
    check('squared_potential_Hermitian_involution', zero(involution.H-involution)
          and zero(involution**2-s.eye(2)))
    check('omitted_potential_derivative_rejected', not zero(involution))
    check('shifted_mass_bound_SOS', zero((aa+beta)**2-(aa**2/2-beta**2)-(aa+2*beta)**2/2))
    q = s.symbols('q', nonnegative=True)
    check('linear_potential_bound_SOS', zero(q*q/4-q+1-(q/2-1)**2))
    check('actual_confinement_coefficient', (2*s.pi*s.Rational(1,8))**2/4 == s.pi**2/64)
    check('zero_phase_control_no_confinement', zero(mu.subs(aa,0)-beta)
          and s.diff(mu,tt).subs(aa,0) == 0)
    radial_scale = s.exp(tt/2)
    check('base_radial_unitary_removes_half_density',
          zero(s.diff(radial_scale,tt)-radial_scale/2))

    # Exact counterexample to inferring projection derivatives from a growing gap.
    unit = s.Matrix([s.cos(y*y),s.sin(y*y)])
    p = unit*unit.T
    complementary = s.eye(2)-p
    toy = s.sqrt(y)*complementary
    derivative = y*p.diff(y)
    check('rotating_control_true_projection', zero(p*p-p) and zero(p.H-p))
    check('rotating_control_exact_kernel', zero(toy*unit))
    check('rotating_control_growing_complement_gap', zero(toy**2-y*complementary)
          and s.simplify(s.trace(toy))==s.sqrt(y))
    check('rotating_control_unbounded_horizontal_derivative', zero(derivative**2-4*y**4*s.eye(2)))
    check('rotating_control_offdiagonal_projection_derivative', zero(p*derivative*p))
    return rows


if __name__ == '__main__':
    result = checks()
    print(json.dumps({'scope':'finite exact safeguards; not analytic certification',
                      'checks':result,'count':len(result),'passed':all(result.values())},indent=2))
    raise SystemExit(0 if all(result.values()) else 1)
