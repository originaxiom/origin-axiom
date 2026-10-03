"""R82 exact local controls, not a contour, spectrum or quantum certificate."""
import itertools
import json

import sympy as s


def sign(p):
    return (-1) ** sum(p[i] > p[j] for i in range(3) for j in range(i + 1, 3))


def cs_density(A, xyz):
    quadratic = sum(sign(p) * s.trace(A[p[0]] * A[p[2]].diff(xyz[p[1]]))
                    for p in itertools.permutations(range(3)))
    cubic = sum(sign(p) * s.trace(A[p[0]] * A[p[1]] * A[p[2]])
                for p in itertools.permutations(range(3)))
    return s.expand(quadratic + s.Rational(2, 3) * cubic)


def curvature(A, xyz):
    return {(i, j): s.simplify(A[j].diff(xyz[i]) - A[i].diff(xyz[j])
                             + A[i] * A[j] - A[j] * A[i])
            for i in range(3) for j in range(i + 1, 3)}


def contact():
    x, y, z, eps = s.symbols('x y z eps', real=True)
    T = s.diag(s.I, -s.I)
    f = 1 + x*x + y*z
    A = [s.zeros(2), eps*T*x*f, eps*T*f]
    density = cs_density(A, (x, y, z))
    mirror_f = f.subs(z, -z)
    mirror = [s.zeros(2), eps*T*x*mirror_f, -eps*T*mirror_f]
    mirror_density = cs_density(mirror, (x, y, z))
    dA = curvature(A, (x, y, z))
    bare_cubic = sum(sign(p)*s.trace(A[p[0]]*A[p[1]]*A[p[2]])
                     for p in itertools.permutations(range(3)))
    return dict(density=density, expected=-2*eps**2*f**2, f=f, eps=eps,
                xyz=(x, y, z), T=T, curvature=dA, cubic=bare_cubic,
                mirror_density=mirror_density, mirror_f=mirror_f)


def transgression():
    x, y, z, eps = s.symbols('x y z eps', real=True)
    xyz = (x, y, z)
    T = s.diag(1, -1)
    C = [T, s.zeros(2), s.zeros(2)]
    a = [s.Matrix([[x, 1], [0, -x]]),
         s.Matrix([[0, y], [1, 0]]), s.Matrix([[y+z, 0], [1, -y-z]])]
    At = [C[i] + eps*a[i] for i in range(3)]
    difference = s.expand(cs_density(At, xyz) - cs_density(C, xyz))
    quadratic = sum(sign(p)*s.trace(a[p[0]]*(a[p[2]].diff(xyz[p[1]])
                         + C[p[1]]*a[p[2]] - a[p[2]]*C[p[1]]))
                    for p in itertools.permutations(range(3)))
    cubic = sum(sign(p)*s.trace(a[p[0]]*a[p[1]]*a[p[2]])
                for p in itertools.permutations(range(3)))
    boundary = sum(sign(p)*s.diff(s.trace(C[p[1]]*a[p[2]]), xyz[p[0]])
                   for p in itertools.permutations(range(3)))
    target = eps**2*quadratic + s.Rational(2, 3)*eps**3*cubic - eps*boundary
    return dict(difference=difference, target=s.expand(target), cubic=s.expand(cubic),
                boundary=s.expand(boundary), eps=eps,
                curvature_zero=all(v == s.zeros(2) for v in curvature(C, xyz).values()))


def run():
    c = contact()
    x, y, z = c['xyz']
    eps, T = c['eps'], c['T']
    k, sigma, CS, vol = s.symbols('k sigma CS vol', real=True)
    t = k + s.I*sigma
    chat = -CS + s.I*vol
    scalar = s.expand(t*chat/2 + s.conjugate(t)*s.conjugate(chat)/2)
    f = c['f']
    trans = transgression()
    periodic = [s.zeros(2), eps*T*s.cos(x), eps*T*s.sin(x)]
    periodic_density = s.trigsimp(cs_density(periodic, (x, y, z)))
    phi = x*y + z*z
    pure = [T*s.diff(phi, v) for v in (x, y, z)]
    exponents = (1, 4, 5, 7, 8, 11)  # supplied B715 principal sl2 decomposition
    weights = [2*m - 2*j for m in exponents for j in range(2*m + 1)]
    hessian = s.diff(c['density'], eps, 2).subs(eps, 0)
    checks = dict(
        scalar_geometric_identity=s.simplify(scalar + k*CS + sigma*vol) == 0,
        scalar_value_blind_at_CS0=s.diff(scalar, k).subs(CS, 0) == 0,
        contact_density=s.expand(c['density'] - c['expected']) == 0,
        derivative_terms_cancel=s.expand(c['density'] + 2*eps**2*f**2) == 0,
        flat_reference_stationary=s.diff(c['density'], eps).subs(eps, 0) == 0,
        hessian_retained=s.expand(hessian + 4*f**2) == 0,
        hessian_nonzero=hessian != 0,
        k_multiplies_hessian=s.diff(k*c['density'], eps, 2).subs(eps, 0) == k*hessian,
        k_derivative_off_shell=s.diff(k*c['density'], k) == c['density'] and c['density'] != 0,
        contact_not_flat=any(v != s.zeros(2) for v in c['curvature'].values()),
        contact_cubic_zero=s.expand(c['cubic']) == 0,
        compact_T_antihermitian=T.conjugate().T == -T,
        mirror_density=s.expand(c['mirror_density'] - 2*eps**2*c['mirror_f']**2) == 0,
        mirror_pair_not_individually_zero=c['mirror_density'] != 0 and c['density'] != 0,
        periodic_density=periodic_density == 2*eps**2,
        periodic_integral=s.integrate(periodic_density, (x, 0, 2*s.pi),
            (y, 0, 2*s.pi), (z, 0, 2*s.pi)) == 2*eps**2*(2*s.pi)**3,
        periodic_hessian=s.diff(periodic_density, eps, 2) == 4,
        pure_gradient_zero=s.expand(cs_density(pure, (x, y, z))) == 0,
        pure_gradient_flat=all(v == s.zeros(2) for v in curvature(pure, (x, y, z)).values()),
        full_transgression=trans['curvature_zero'] and s.expand(trans['difference']-trans['target']) == 0,
        omitted_cubic_rejected=trans['cubic'] != 0 and s.expand(trans['difference']
            - trans['target'] + s.Rational(2, 3)*trans['eps']**3*trans['cubic']) != 0,
        reversed_boundary_rejected=trans['boundary'] != 0 and s.expand(trans['difference']
            - trans['target'] - 2*trans['eps']*trans['boundary']) != 0,
        principal_E6_trace_nonzero=-sum(w*w for w in weights) == -7488,
        principal_E6_dimension=len(weights) == 78,
    )
    return dict(scope='Full functional versus critical value; no physical contour or SM',
                checks={name: bool(value) for name, value in checks.items()},
                all_checks_pass=all(checks.values()), contact_density=str(c['density']),
                contact_hessian=str(hessian), transgression={name: str(value)
                    for name, value in trans.items()}, principal_trace=-sum(w*w for w in weights))


if __name__ == '__main__':
    result = run()
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result['all_checks_pass'] else 1)
