"""R81 exact nonsplit boundary comparator. No global W PDE or particles."""
import json
from functools import lru_cache
import sympy as sp


def clean(x):
    return sp.simplify(sp.trigsimp(x))


def comm(a, b):
    return a*b-b*a


@lru_cache(None)
def data():
    s = sp.symbols('s', real=True)
    J = sp.diag(1, -1)
    N = sp.Matrix([[0, 1], [0, 0]])
    sec = 1/sp.cos(s)
    H = sp.diag(sec, sp.cos(s))
    G = sp.diag(sp.cos(s)**sp.Rational(-1, 2),
                sp.cos(s)**sp.Rational(1, 2))
    Cs = -sp.tan(s)*J/2
    Cx = -sec*N
    A = [(c-c.T)/2 for c in (Cs, Cx)]
    psi = [(c+c.T)/2 for c in (Cs, Cx)]
    curvature = (Cx.diff(s)+comm(Cs, Cx)).applyfunc(clean)
    moment = (2*psi[0].diff(s)+sum(
        (2*comm(A[i], psi[i]) for i in range(2)), sp.zeros(2))).applyfunc(clean)
    wrong_cs = -Cs
    wrong_curvature = (Cx.diff(s)+comm(wrong_cs, Cx)).applyfunc(clean)
    wrong_moment = (2*wrong_cs.diff(s)+comm(Cx, Cx.T)).applyfunc(clean)
    L = sp.eye(2)+N
    a = sp.pi/4
    eta_norm = clean(Cx[0, 1]**2)
    primitive = sp.tan(s)
    bulk = primitive.subs(s, a)-primitive.subs(s, -a)
    flux_density = clean(sp.trace(J*psi[0]))
    flux = flux_density.subs(s, a)-flux_density.subs(s, -a)
    return dict(s=s, J=J, N=N, H=H, G=G, Cs=Cs, Cx=Cx,
                curvature=curvature, moment=moment, L=L, a=a,
                wrong_curvature=wrong_curvature, wrong_moment=wrong_moment,
                eta_norm=eta_norm, primitive=primitive, bulk=bulk,
                flux_density=flux_density, flux=flux)


def checks():
    d = data()
    s, N, J, G = (d[k] for k in ('s', 'N', 'J', 'G'))
    zero_matrix = sp.zeros(2)
    rows = {}
    def eq(name, lhs, rhs=0):
        if isinstance(lhs, sp.MatrixBase):
            rows[name] = (lhs-rhs).applyfunc(clean) == zero_matrix
        else:
            rows[name] = clean(lhs-rhs) == 0
    eq('nilpotent', N*N, zero_matrix)
    eq('primitive_holonomy', N.exp(), d['L'])
    eq('det_metric', d['H'].det(), 1)
    eq('metric_at_zero', d['H'].subs(s, 0), sp.eye(2))
    eq('metric_boundary', d['H'].subs(s, d['a']), sp.diag(sp.sqrt(2), 1/sp.sqrt(2)))
    eq('frame_metric', G.T*G, d['H'])
    eq('frame_radial', -G.diff(s)*G.inv(), d['Cs'])
    eq('frame_torus', G*(-N)*G.inv(), d['Cx'])
    eq('flat_full', d['curvature'], zero_matrix)
    eq('moment_full', d['moment'], zero_matrix)
    eq('holonomy_transport', G*d['L']*G.inv(), sp.eye(2)-d['Cx'])
    # Rectangular zero is checked separately; the matrix helper is 2x2 only.
    rows['invariant_line'] = (d['L']-sp.eye(2))*sp.Matrix([1, 0]) == sp.zeros(2, 1)
    rows['unique_eigenline'] = (d['L']-sp.eye(2)).nullspace() == [sp.Matrix([1, 0])]
    rows['nonsplit_minpoly'] = d['L'] != sp.eye(2) and (d['L']-sp.eye(2))**2 == zero_matrix
    eq('extension_norm', d['eta_norm'], 1/sp.cos(s)**2)
    eq('norm_primitive', sp.diff(d['primitive'], s), d['eta_norm'])
    eq('bulk_exact', d['bulk'], 2)
    eq('outward_density', d['flux_density'], -sp.tan(s))
    eq('outward_flux', d['flux'], -2)
    eq('full_projector_balance', 2*d['bulk']+2*d['flux'])
    rows['drop_flux_fails'] = 2*d['bulk'] != 0
    rows['wrong_radial_flat_fails'] = d['wrong_curvature'] != zero_matrix
    rows['wrong_radial_moment_fails'] = d['wrong_moment'] != zero_matrix
    eq('split_control_moment', comm(zero_matrix, zero_matrix), zero_matrix)
    rows['pole_bulk_diverges'] = sp.limit(2*sp.tan(s), s, sp.pi/2, dir='-') == sp.oo
    rows['pole_metric_diverges'] = sp.limit(d['H'][0, 0], s, sp.pi/2, dir='-') == sp.oo
    rows['pole_inverse_diverges'] = sp.limit(d['H'].inv()[1, 1], s, sp.pi/2, dir='-') == sp.oo
    eq('harmonic_trace', sp.diff(sp.log(d['H'].det()), s, 2))
    return rows


if __name__ == '__main__':
    rows = checks()
    print(json.dumps({'audit': 'R81', 'checks': rows, 'passed': sum(rows.values()),
                      'total': len(rows), 'scope': 'exact comparator; no numerical W metric'}, indent=2))
    raise SystemExit(0 if all(rows.values()) else 1)
