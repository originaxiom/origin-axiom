"""R15: global-parametrix identities and regulated charged-pair topology.

No mesh solution of m202, complete-limit spectrum, or physical parent selection.
The accompanying design contains the analytic extension argument.
"""
from __future__ import annotations

from collections import Counter
from functools import lru_cache
from itertools import product
import json
from math import gcd
from pathlib import Path
import sys
import time

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

sys.path.insert(0, str(Path(__file__).resolve().parent))
from boundary_index import Cubes, det_minus_identity


def parametrix_identities():
    z, s, t, area, length = sp.symbols('z s t A ell', positive=True)
    chi = sp.Function('chi')
    psi = z**2 * chi(sp.log(z))
    delta_psi = sp.expand(z**2*(sp.diff(psi, z, 2)-sp.diff(psi, z)/z))
    target = z**2*(sp.diff(chi(s), s, 2)+2*sp.diff(chi(s), s))
    identity = sp.simplify(delta_psi-target.subs(s, sp.log(z)))
    profiles = [10*t**3-15*t**4+6*t**5, 35*t**4-84*t**5+70*t**6-20*t**7]
    rows = []
    for h in profiles:
        # s varies through an interval of arbitrary length ell.
        delta_integral = sp.integrate(area*(sp.diff(h, t, 2)/length+2*sp.diff(h, t)), (t, 0, 1))
        rows.append(dict(profile=str(h), integral=str(sp.simplify(delta_integral)),
                         endpoint_values=[str(h.subs(t, a)) for a in (0, 1)],
                         endpoint_derivatives=[str(sp.diff(h, t).subs(t, a)) for a in (0, 1)]))
    # A cutoff which becomes constant has zero outgoing flux, unlike z^2.
    h = profiles[0]
    c_s = h.subs(t, s)
    constant_integrand = area*sp.exp(-2*s)*(sp.diff(c_s, s, 2)-2*sp.diff(c_s, s))
    cutoff_constant = sp.simplify(sp.integrate(constant_integrand, (s, 0, 1)))
    w = sp.Function('w')(s)
    f = sp.exp(s)*w
    hardy = sp.simplify(sp.exp(-2*s)*sp.diff(f, s)**2-w**2-sp.diff(w, s)**2-sp.diff(w**2, s))
    r = sp.symbols('r', positive=True)
    line = sp.log(sp.tanh(r))
    local_ode = sp.simplify(sp.trigsimp(sp.diff(line, r, 2)+(sp.coth(r)+sp.tanh(r))*sp.diff(line, r)))
    local_flux = sp.simplify(sp.trigsimp(sp.diff(line, r)*sp.sinh(r)*sp.cosh(r)))
    a0, a1, mu, flow = sp.symbols('A0 A1 mu flow', nonzero=True, real=True)
    coeffs = [-mu/(2*a0)+flow*a1, -flow*a0]
    repaired = sp.simplify(mu+2*(a0*coeffs[0]+a1*coeffs[1]))
    unweighted = sp.simplify(mu+2*(a0*(-mu/2)+a1*0))
    return dict(metric_cutoff_identity=str(identity), transitions=rows,
                cutoff_constant_integral=str(cutoff_constant), hardy_identity=str(hardy),
                line_ode=str(local_ode), line_flux_divided_by_2pi=str(local_flux),
                matching_coefficients=list(map(str, coeffs)), repaired_mean=str(repaired),
                omitted_repair_mean=str(mu), wrong_unweighted_repair=str(unweighted),
                unequal_area_control=str(unweighted.subs({a0: 2, a1: 3, mu: 7})),
                scalar_gap_is_not_a_charged_gap=True)


def excision_prediction(base_b1, intersection):
    """Rational Betti ranks with integral primitiveness checked for the stated Z result.

    Hypotheses: two torus boundary components, H1 free of stated rank,
    H2=Z and the displayed H2(Q)->Z^k intersection map. Not a general
    graph/neighborhood or arbitrary 3-manifold formula.
    """
    v = tuple(int(x) for x in intersection)
    if base_b1 != 2 or not v or gcd(*v) != 1:
        raise ValueError('requires a nonempty primitive, nonzero intersection vector')
    k = len(v)
    b1c = base_b1+k-1
    return dict(core=[1, b1c, 0, 0], tubes=[0, base_b1+k-1, 1, 0],
                exterior=[0, 1, base_b1+k-1, 0],
                intersection_rank=1, meridian_image_rank=k-1)


@lru_cache(maxsize=None)
def cellular_pair(k, n=6, height=1):
    if k not in range(4) or n not in (6, 8) or height not in (1, 2):
        raise ValueError('outside the sealed finite control family')
    grid = Cubes((n, n, 0))
    positions = ((0, 0), (2, 2), (4, 4))[:k]
    tops = set(product(range(n), range(n), range(height)))
    removed = {(x, y, h) for x, y in positions for h in range(height)}
    Q = grid.complex(tops)
    C = grid.complex(tops-removed)
    N = grid.complex(removed)
    T, E = C & N, C & grid.frontier(Q)
    assert C | N == Q
    assert grid.frontier(C) == T | E
    rows = {name: grid.cohomology(cells) for name, cells in
            (('Q', Q), ('C', C), ('T', T), ('E', E), ('boundary_C', T | E))}
    rows['relative_T'] = grid.cohomology(C, T)
    rows['relative_E'] = grid.cohomology(C, E)
    return dict(k=k, n=n, height=height, removed_columns=[list(x) for x in positions],
                interpretation='product-model cellular control, not an m202 triangulation', **rows)


def m202_witness():
    import snappy
    rows = {}
    for name in ('m202', 'm004'):
        M = snappy.Manifold(name)
        pi = M.fundamental_group()
        generators = list(pi.generators())
        relators = list(pi.relators())
        ab = sp.Matrix([[word.count(g)-word.count(g.upper()) for g in generators] for word in relators])
        snf = smith_normal_form(ab, domain=sp.ZZ)
        G = M.symmetry_group()
        size = int(G.order())
        table = [[int(G.multiply_elements(i, j)) for j in range(size)] for i in range(size)]
        identity = next(i for i in range(size) if all(table[i][j] == j == table[j][i] for j in range(size)))
        orders = []
        for i in range(size):
            p, count = identity, 0
            while True:
                p, count = table[p][i], count+1
                if p == identity:
                    break
                assert count <= size
            orders.append(count)
        candidates = []
        for i, iso in enumerate(G.isometries()):
            if orders[i] != 3 or list(iso.cusp_images()) != list(range(M.num_cusps())):
                continue
            maps = [[[int(a[r, c]) for c in range(2)] for r in range(2)] for a in iso.cusp_maps()]
            candidates.append(dict(index=i, matrices=maps,
                                   fixed_points_per_cusp=[abs(det_minus_identity(a)) for a in maps],
                                   preserving=all(sp.Matrix(a).det() == 1 for a in maps)))
        rows[name] = dict(generators=generators, relators=relators,
                          abelianized_relators=ab.tolist(), smith=snf.tolist(),
                          homology=str(M.homology()), b1=len(generators)-int(ab.rank()),
                          cusps=int(M.num_cusps()), symmetry_order=size,
                          element_orders=orders, order_three_self_cusp=candidates)
    return dict(snappy_version=snappy.version(), manifolds=rows)


def e6_parent():
    C = 2*sp.eye(6)
    for i, j in ((0, 2), (2, 3), (3, 4), (4, 5), (1, 3)):
        C[i, j] = C[j, i] = -1
    roots, pending = set(), [tuple(int(x) for x in sp.eye(6)[:, i]) for i in range(6)]
    def reflect(v, i):
        out = list(v)
        out[i] -= sum(int(C[i, j])*v[j] for j in range(6))
        return tuple(out)
    while pending:
        v = pending.pop()
        if v in roots:
            continue
        roots.add(v)
        pending.extend(reflect(v, i) for i in range(6))
    zero = [v for v in roots if v[0] == 0]
    u = C.inv()[:, 0]
    u2 = (u.T*C*u)[0]
    charges = Counter(v[0] for v in roots)
    charges[0] += 6
    charged_orbits = {}
    for q in (-1, 1):
        group = {v for v in roots if v[0] == q}
        orbit, pending = set(), [min(group)]
        while pending:
            v = pending.pop()
            if v in orbit:
                continue
            orbit.add(v)
            pending.extend(reflect(v, i) for i in range(1, 6))
        assert orbit == group
        dominant = []
        lengths = set()
        for v in sorted(group):
            vector = sp.Matrix(v)
            projection = vector-u*sp.Rational(q)/u2
            lengths.add((projection.T*C*projection)[0])
            labels = list(C*vector)[1:]
            if all(a >= 0 for a in labels):
                dominant.append(list(map(int, labels)))
        charged_orbits[str(q)] = dict(size=len(orbit), d5_dominant=dominant,
                                      projected_norms=sorted(map(str, lengths)))
    return dict(roots=len(roots), root_lengths=sorted({str((sp.Matrix(v).T*C*sp.Matrix(v))[0]) for v in roots}),
                adjoint_charge_dimensions={str(k): v for k, v in sorted(charges.items())},
                zero_roots=len(zero), zero_root_rank=int(sp.Matrix(zero).rank()),
                u_norm=str(u2), charged_d5_orbits=charged_orbits,
                zero_u_neutral_dimension=6+len(roots),
                physical_parent_is_prescribed=True)


def run():
    started = time.monotonic()
    out = dict(parametrix=parametrix_identities(),
               cells=[cellular_pair(k) for k in range(4)]+[cellular_pair(3, 8, 2)],
               exact_sequence=[dict(intersection=list(v), prediction=excision_prediction(2, v))
                               for v in ((1, 1, 1), (1, 0, 0), (-1, 1, -1))],
               geometry=m202_witness(), parent=e6_parent())
    out['runtime_seconds'] = time.monotonic()-started
    out['scope'] = 'analytic extension identities and regulated cohomology; not a complete physical chiral spectrum'
    return out


if __name__ == '__main__':
    print(json.dumps(run(), indent=2, sort_keys=True, default=str), flush=True)
