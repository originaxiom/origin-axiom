"""R28 exact controls. Standard fixed-metric action; no derived physical source.

No files are written by this producer. Run only after its design/source/test seal.
The analytic quantifiers and exclusions live in SOURCE_ACTION_PROOF.md.
"""
from functools import lru_cache
import json
import sympy as sp


def clean(expr):
    return sp.simplify(sp.trigsimp(sp.expand_trig(expr)))


def zero(expr):
    return clean(expr) == 0


def metric_data(metric, coordinates):
    """Coordinate Christoffel and Ricci tensors, independent of a Hessian guess."""
    n = len(coordinates)
    inverse = metric.inv()
    gamma = [[[clean(sum(inverse[k, l] * (
        sp.diff(metric[l, j], coordinates[i])
        + sp.diff(metric[l, i], coordinates[j])
        - sp.diff(metric[i, j], coordinates[l]))
        for l in range(n)) / 2) for j in range(n)]
        for i in range(n)] for k in range(n)]
    ricci = sp.Matrix(n, n, lambda i, j: clean(sum(
        sp.diff(gamma[k][i][j], coordinates[k])
        - sp.diff(gamma[k][i][k], coordinates[j])
        + sum(gamma[k][i][j] * gamma[l][k][l]
              - gamma[l][i][k] * gamma[k][l][j] for l in range(n))
        for k in range(n))))
    return inverse, gamma, ricci


@lru_cache(None)
def tube():
    r, eps, R, length = sp.symbols('r eps R L', positive=True)
    theta, ell, beta = sp.symbols('theta ell beta', real=True)
    w = sp.sinh(r) * sp.cosh(r)
    potential = beta * sp.log(sp.tanh(r))
    radial = clean(sp.diff(potential, r))
    divergence = clean(sp.diff(w * radial, r) / w)
    metric = sp.diag(1, sp.sinh(r)**2, sp.cosh(r)**2)
    coordinates = (r, theta, ell)
    inverse, gamma, ricci = metric_data(metric, coordinates)
    hessian = sp.Matrix(3, 3, lambda i, j: clean(
        sp.diff(potential, coordinates[i], coordinates[j])
        - sum(gamma[k][i][j] * sp.diff(potential, coordinates[k])
              for k in range(3))))
    hnorm = clean(sum(inverse[i, i] * inverse[j, j] * hessian[i, j]**2
                      for i in range(3) for j in range(3)))
    boundary = clean(w * radial * sp.diff(radial, r))
    primitive = 2 * sp.pi * length * beta**2 * sp.log(sp.tanh(r))
    norm = primitive.subs(r, R) - primitive.subs(r, eps)
    leading = sp.limit(norm / sp.log(1 / eps), eps, 0, dir='+')
    wrong_radial = beta / sp.sinh(r)
    wrong_div = clean(sp.diff(w * wrong_radial, r) / w)
    return dict(r=r, eps=eps, R=R, length=length, beta=beta, w=w,
                radial=radial, divergence=divergence, metric=metric,
                ricci=ricci, hessian=hessian, hnorm=hnorm,
                boundary=boundary, primitive=primitive, norm=norm,
                leading=leading, wrong_div=wrong_div,
                bochner_residual=clean(w * (hnorm - 2 * radial**2)
                                      - sp.diff(boundary, r)))


@lru_cache(None)
def core():
    t = tube()
    r, eps, length, beta, w = (t[k] for k in ('r', 'eps', 'length', 'beta', 'w'))
    phi = beta * sp.tanh(r) / sp.sinh(eps)**2
    div = clean(sp.diff(w * phi, r) / w)
    volume = sp.integrate(2 * sp.pi * length * w, (r, 0, eps))
    flux = clean((2 * sp.pi * length * w * phi).subs(r, eps))
    cost = clean(sp.integrate(2 * sp.pi * length * w * div**2, (r, 0, eps)))
    bound = clean(flux**2 / volume)
    v, k = sp.symbols('v k', real=True)
    shape = 1 + k * (1 - 2 * v)
    nonuniform_cost = sp.integrate(shape**2, (v, 0, 1))
    # A concrete regular radial profile with the same boundary flux.
    vr = sp.sinh(r)**2 / sp.sinh(eps)**2
    phi_k = beta * (vr + k * vr * (1 - vr)) / w
    div_k = clean(sp.diff(w * phi_k, r) / w)
    rho = 2 * beta / sp.sinh(eps)**2
    return dict(phi=phi, div=div, volume=clean(volume), flux=flux, cost=cost,
                bound=bound, core_limit=sp.limit(eps**2 * bound, eps, 0, dir='+'),
                axis_slope=sp.limit(phi / r, r, 0, dir='+'),
                matching=clean(phi.subs(r, eps) - t['radial'].subs(r, eps)),
                v=v, k=k, vr=vr, shape=shape, nonuniform_cost=nonuniform_cost,
                phi_k=phi_k, div_k=div_k,
                shape_residual=clean(div_k - rho * shape.subs(v, vr)),
                shifted_residual=clean(-div + rho),
                wrong_shift=clean(-div - rho))


@lru_cache(None)
def cusp():
    s, b, c, db, dc = sp.symbols('s b c db dc', real=True)
    area = sp.symbols('A', positive=True)
    H = sp.exp(2 * s) * (b * s + c)
    laplace = clean(sp.diff(H, s, 2) - 2 * sp.diff(H, s)
                    - 2 * b * sp.exp(2 * s))
    Hdot = sp.exp(2 * s) * (db * s + dc)
    radial_velocity = sp.diff(Hdot, s)
    density = clean(area * sp.exp(-2 * s) * radial_velocity**2)
    primitive = area * sp.exp(2 * s) * (4 * (db * s + dc)**2 + db**2) / 2
    through = clean(density.subs(db, 0))
    # The torus-constant harmonic scalar zero mode, including both solutions.
    c0, c2 = sp.symbols('c0 c2', real=True)
    zero_mode = c0 + c2 * sp.exp(2 * s)
    mode_equation = clean(sp.diff(zero_mode, s, 2) - 2 * sp.diff(zero_mode, s))
    growing_norm_density = area * sp.exp(-2 * s) * (c2 * sp.exp(2 * s))**2
    # Finite, nonharmonic radial one-form control on a cusp; extend by cutoff.
    f = sp.exp(-s)
    finite_norm_density = area * sp.exp(-2 * s) * f**2
    finite_residual_density = area * sp.exp(-2 * s) * (sp.diff(f, s) - 2 * f)**2
    return dict(s=s, b=b, c=c, db=db, dc=dc, area=area, H=H,
                laplace=laplace, density=density, primitive=primitive,
                antiderivative_residual=clean(sp.diff(primitive, s) - density),
                through=through, mode_equation=mode_equation,
                growing_norm_density=clean(growing_norm_density),
                finite_norm_density=finite_norm_density,
                finite_residual_density=finite_residual_density,
                tangent_norm_density=clean(area * sp.exp(-2 * s) * sp.exp(2 * s)))


@lru_cache(None)
def action_controls():
    x, t, a, b, lam = sp.symbols('x t a b lam', real=True)
    residual = t * a + t**2 * b
    energy = residual**2
    # The form convention: each antisymmetric pair appears twice in sum_ij.
    f01, f02, f12, div = sp.symbols('f01 f02 f12 div', real=True)
    components = sp.Matrix([[0, f01, f02], [-f01, 0, f12], [-f02, -f12, 0]])
    norm2 = f01**2 + f02**2 + f12**2
    component_potential = sum(e**2 for e in components) + (2 * div)**2 / 2
    torus_factor = (2 * sp.pi)**2
    sin_norm = torus_factor * sp.integrate(sp.sin(x)**2, (x, 0, 2 * sp.pi))
    sin_residual = torus_factor * sp.integrate(sp.diff(sp.sin(x), x)**2,
                                             (x, 0, 2 * sp.pi))
    const_norm = (2 * sp.pi)**3
    u = sp.diag(1, -1)
    epsilon = sp.Matrix([[0, 1], [1, 0]])
    gauge_velocity = sp.I * (epsilon * u - u * epsilon)
    compensated = u + lam * gauge_velocity
    return dict(first=sp.diff(energy, t).subs(t, 0),
                second=sp.diff(energy, t, 2).subs(t, 0), a=a,
                nonzero_first=sp.diff((1 + t)**2, t).subs(t, 0),
                convention_residual=clean(component_potential - 2 * (norm2 + div**2)),
                sin_norm=sin_norm, sin_residual=sin_residual, const_norm=const_norm,
                gauge_projection=clean(sp.trace(u * gauge_velocity)),
                gauge_norm=clean(sp.trace(compensated * compensated) / 2), lam=lam)


@lru_cache(None)
def discrete_controls():
    x, y, z = sp.symbols('x y z', real=True)
    xyz = sp.Matrix([x, y, z])
    T = sp.Matrix([z, x, 2 * x * z - y])
    inv = x**2 + y**2 + z**2 - 2 * x * y * z - 1
    sub = dict(zip(xyz, T))
    J = T.jacobian(xyz)
    grad = sp.Matrix([sp.diff(inv, q) for q in xyz])
    bracket = lambda f, g: sp.expand(grad.dot(
        sp.Matrix([sp.diff(f, q) for q in xyz]).cross(
            sp.Matrix([sp.diff(g, q) for q in xyz]))))
    a, b, c, u, v = sp.symbols('a b c u v', real=True)
    L = sp.exp(u) * v
    first = lambda U, V: sp.diff(L, u).subs({u: U, v: V}, simultaneous=True)
    second = lambda U, V: sp.diff(L, v).subs({u: U, v: V}, simultaneous=True)
    del_expr = second(a, b) + first(b, c)
    csol = sp.solve(del_expr, c)[0]
    DEL_map = sp.Matrix([b, csol])
    jac = clean(DEL_map.jacobian([a, b]).det())
    area_residual = clean(sp.exp(b) * jac - sp.exp(a))
    base = u * v - u**2 / 2
    prev = -sp.diff(base, v).subs({u: a, v: b}, simultaneous=True)
    current = sp.diff(base, u).subs({u: b, v: c}, simultaneous=True)
    alternating_del = sp.expand(prev + current)
    autonomous_del = sp.expand(-prev + current)
    X, Y, Z = sp.symbols('X Y Z', real=True)
    pn = sp.Matrix(sp.symbols('p0:3', real=True))
    pnext = sp.Matrix(sp.symbols('q0:3', real=True))
    nxt = sp.Matrix([X, Y, Z])
    local_action = pn.dot(xyz) + pnext.dot(nxt - T)
    x_gradient = sp.Matrix([sp.diff(local_action, q) for q in xyz])
    p_gradient = sp.Matrix([sp.diff(local_action, q) for q in pnext])
    P = sp.Matrix([[0, 1], [1, 0]])
    shear = sp.Matrix([[1, 1], [0, 1]])
    half = sp.Matrix([[0, 1], [1, 1]])
    return dict(a=a, b=b, c=c, xyz=xyz, T=T, J=J, inv=inv,
                invariant_residual=clean(inv.subs(sub, simultaneous=True) - inv),
                bracket_residual=clean(bracket(T[0], T[1])
                    + bracket(x, y).subs(sub, simultaneous=True)),
                determinant=J.det(), jacobian=jac, area_residual=area_residual,
                nonlinear_del=del_expr, nonlinear_map=DEL_map,
                alternating_del=alternating_del, autonomous_del=autonomous_del,
                mixed_alternating=sp.diff(base, u, v),
                multiplier_x=x_gradient, multiplier_p=p_gradient,
                multiplier_x_residual=x_gradient - (pn - J.T * pnext),
                multiplier_p_residual=p_gradient - (nxt - T),
                conjugacy_residual=P * (shear * P) * P - half,
                half=half, square=half**2)


def checks():
    t, c, h, a, d = tube(), core(), cusp(), action_controls(), discrete_controls()
    r, beta, length, eps = (t[k] for k in ('r', 'beta', 'length', 'eps'))
    return {
        'tube_residual_zero': zero(t['divergence']),
        'metric_ricci_minus_two': (t['ricci'] + 2 * t['metric']).applyfunc(clean) == sp.zeros(3),
        'tube_norm_primitive': zero(sp.diff(t['primitive'], r) - 2 * sp.pi * length * t['w'] * t['radial']**2),
        'residue_log_coefficient': zero(t['leading'] - 2 * sp.pi * length * beta**2),
        'bochner_boundary_exact': zero(t['bochner_residual']),
        'wrong_tube_rejected': not zero(t['wrong_div']),
        'core_saturates_cauchy_schwarz': zero(c['cost'] - c['bound']),
        'core_continuous_match': zero(c['matching']),
        'core_inverse_square_cost': zero(c['core_limit'] - 4 * sp.pi * length * beta**2),
        'nonuniform_core_cost': zero(c['nonuniform_cost'] - 1 - c['k']**2 / 3),
        'nonuniform_core_is_actual_profile': zero(c['shape_residual']),
        'declared_source_shift_works': zero(c['shifted_residual']),
        'wrong_source_shift_rejected': not zero(c['wrong_shift']),
        'cusp_laplace_zero': zero(h['laplace']),
        'cusp_norm_primitive': zero(h['antiderivative_residual']),
        'through_flux_nonzero': not zero(h['through']),
        'positive_compact_norm_and_potential': a['sin_norm'] == a['sin_residual'] == 4 * sp.pi**3,
        'stationarity_at_zero_residual': a['first'] == 0 and a['nonzero_first'] != 0,
        'action_form_convention': zero(a['convention_residual']),
        'gauge_cannot_cancel_cartan_velocity': a['gauge_projection'] == 0 and zero(a['gauge_norm'] - 1 - 4 * a['lam']**2),
        'trace_map_invariant': zero(d['invariant_residual']),
        'trace_map_anti_poisson_retained': d['determinant'] == -1 and zero(d['bracket_residual']),
        'actual_halfstep_conjugacy': d['conjugacy_residual'] == sp.zeros(2),
        'variable_density_not_unit_jacobian': zero(d['area_residual']) and not zero(d['jacobian'] - 1),
        'alternating_regular_action': d['alternating_del'] == d['c'] - d['b'] - d['a'] and d['mixed_alternating'] != 0,
        'dropping_alternation_fails': not zero(d['autonomous_del'].subs(d['c'], d['a'] + d['b'])),
        'full_map_multiplier_action': d['multiplier_x_residual'] == d['multiplier_p_residual'] == sp.zeros(3, 1),
    }


def report():
    t, c, h, a, d = tube(), core(), cusp(), action_controls(), discrete_controls()
    return {
        'scope': 'Fixed-metric commuting source class; static bulk compatibility, not selected defect or TOE. Discrete controls use different declared action classes.',
        'tube': {k: str(t[k]) for k in ('radial', 'divergence', 'ricci', 'hnorm', 'boundary', 'norm', 'leading')},
        'core': {k: str(c[k]) for k in ('phi', 'div', 'volume', 'flux', 'bound', 'cost', 'axis_slope', 'core_limit', 'nonuniform_cost', 'shifted_residual')},
        'cusp': {k: str(h[k]) for k in ('laplace', 'density', 'primitive', 'through', 'growing_norm_density', 'finite_norm_density', 'finite_residual_density', 'tangent_norm_density')},
        'action': {k: str(a[k]) for k in ('first', 'second', 'sin_norm', 'sin_residual', 'const_norm', 'gauge_projection', 'gauge_norm')},
        'discrete': {k: str(d[k]) for k in ('determinant', 'jacobian', 'nonlinear_map', 'alternating_del', 'autonomous_del', 'multiplier_x', 'multiplier_p', 'half', 'square')},
        'checks': checks(),
    }


if __name__ == '__main__':
    data = report()
    print(json.dumps(data, indent=2, sort_keys=True))
    raise SystemExit(0 if all(data['checks'].values()) else 1)
