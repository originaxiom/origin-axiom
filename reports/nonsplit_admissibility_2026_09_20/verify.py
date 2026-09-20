"""Exact checks supporting F01's written analytic argument; not a PDE solver.

Independent SymPy implementation of small matrix and differential identities.
No SnapPy rank algorithm or upstream cohomology producer is called here.
The nonzero cohomological index is prior evidence, not recomputed by this file.
"""
import hashlib
import json
from pathlib import Path
import platform
import sys

import sympy as s


def simp(x):
    return s.simplify(s.expand_complex(x))


def clean(m):
    return m.applyfunc(simp)


def word(w, a, b):
    letters = {'a': a, 'b': b, 'A': a.inv(), 'B': b.inv()}
    result = s.eye(a.rows)
    for ch in w:
        result = clean(result * letters[ch])
    return result


def sym_power(m, degree):
    x, y = s.symbols('x y')
    a, b, c, d = list(m)
    cols = []
    for j in range(degree + 1):
        p = s.Poly(s.expand((a*x+c*y)**(degree-j)*(b*x+d*y)**j), x, y)
        cols.append([simp(p.coeff_monomial(x**(degree-i)*y**i))
                     for i in range(degree + 1)])
    return s.Matrix.hstack(*(s.Matrix(col) for col in cols))


def projection_ranks(mats):
    """P onto span(e1): P=e1*(1,p1,...), so P^2=P automatically."""
    n = mats[0].rows
    unknowns = s.symbols(f'p1:{n}')
    p = s.zeros(n)
    p[0, :] = s.Matrix([[1, *unknowns]])
    equations = []
    for m in mats:
        equations.extend(list(clean(p*m-m*p)))
    lhs, rhs = s.linear_eq_to_matrix(equations, unknowns)
    return lhs.rank(), lhs.row_join(rhs).rank()


def algebra():
    u = (1+s.I*s.sqrt(3))/2
    a = s.Matrix([[0, 1], [-1, 1]])
    b = s.Matrix([[0, u**2], [u, -2]])
    p = s.Matrix([[1, 0], [u, 1]])
    ap, bp = clean(p.inv()*a*p), clean(p.inv()*b*p)
    assert simp(u**2-u+1) == 0
    assert simp(u*s.conjugate(u)) == 1
    assert simp(u**6) == 1 and simp(u**3) == -1
    assert clean(ap-s.Matrix([[u, 1], [0, 1-u]])) == s.zeros(2)
    assert clean(bp-s.Matrix([[-1, u**2], [0, -1]])) == s.zeros(2)
    assert word('aabaBaaBab', ap, bp) == s.eye(2)
    assert simp(ap.det()) == simp(bp.det()) == 1
    mu, longitude = word('AbAA', ap, bp), word('babA', ap, bp)
    assert mu == s.Matrix([[1, -1], [0, 1]])
    assert longitude == s.Matrix([[1, 1], [0, 1]])
    assert mu*longitude == s.eye(2)
    va, vb = clean(u*sym_power(ap, 3)), clean(-sym_power(bp, 3))
    assert word('aabaBaaBab', va, vb) == s.eye(4)
    assert va.is_upper and vb.is_upper
    ranks = [clean((vb-s.eye(4))**j).rank() for j in range(1, 5)]
    assert ranks == [3, 2, 1, 0]
    base_projection = projection_ranks([ap, bp])
    v_projection = projection_ranks([va, vb])
    # P(e1)=e1 is eliminated before solving, so ranks need not match a
    # producer which keeps that condition as an extra affine equation.
    assert base_projection[1] == base_projection[0] + 1
    assert v_projection[1] == v_projection[0] + 1
    diagonal = [s.diag(*m.diagonal()) for m in [va, vb]]
    split_projection = projection_ranks(diagonal)
    assert split_projection[0] == split_projection[1]

    h11, h22, hr, hi = s.symbols('h11 h22 hr hi', real=True)
    h = s.Matrix([[h11, hr+s.I*hi], [hr-s.I*hi, h22]])
    equations = []
    for m in [ap, bp]:
        for entry in clean(m.conjugate().T*h*m-h):
            equations.extend([s.re(entry), s.im(entry)])
    invariant_h = s.linsolve(equations, (h11, hr, hi, h22))
    assert invariant_h == s.FiniteSet((0, 0, 0, h22))
    # This is an unitarizability control, not a substitute for harmonicity.
    return {'field': 'Q(sqrt(-3))', 'peripheral_mu': str(mu),
            'peripheral_longitude': str(longitude),
            'V_b_unipotent_power_ranks': ranks,
            'base_projection_ranks': base_projection,
            'V_projection_ranks': v_projection,
            'split_projection_ranks': split_projection,
            'base_invariant_Hermitian_forms': str(invariant_h)}


def projection_variation(r, q):
    """One cotangent component. General all-rank result is the block proof."""
    n = r + q
    er = s.symbols(f'c0:{r*q}', real=True)
    ei = s.symbols(f'd0:{r*q}', real=True)
    eta = s.Matrix(r, q, lambda i, j: er[i*q+j]+s.I*ei[i*q+j])
    a = s.zeros(n)
    a[:r, r:] = eta/2
    a[r:, :r] = -eta.conjugate().T/2
    psi = s.diag(*s.symbols(f'h0:{n}', real=True))
    psi[:r, r:] = eta/2
    psi[r:, :r] = eta.conjugate().T/2
    xi = s.diag(*([q]*r+[-r]*q))
    dxi = a*xi-xi*a
    pairing = simp(s.trace(psi*dxi))
    eta_norm = sum(x*x for x in er+ei)
    assert simp(pairing + s.Rational(n, 2)*eta_norm) == 0
    assert s.trace(xi*xi) == r*q*n
    assert simp(s.trace(psi*(-dxi)) - s.Rational(n, 2)*eta_norm) == 0
    assert pairing.subs(dict.fromkeys(er+ei, 0)) == 0
    assert pairing.subs({x: int(x == er[0]) for x in er+ei}) == -s.Rational(n, 2)
    return {'r': r, 's': q, 'contraction': str(pairing), 'xi_norm_squared': r*q*n}


def christoffel(metric, coords):
    inv = metric.inv()
    n = len(coords)
    return [[[s.simplify(sum(inv[k, l]*(s.diff(metric[l, j], coords[i])
                 + s.diff(metric[l, i], coords[j])-s.diff(metric[i, j], coords[l]))
                 for l in range(n))/2) for j in range(n)] for i in range(n)]
            for k in range(n)]


def busemann():
    x, z = s.symbols('x z', real=True)
    y = s.symbols('y', positive=True)
    coords = [x, z, y]
    metric = s.eye(3)/y**2
    gamma = christoffel(metric, coords)
    b = -s.log(y)
    db = s.Matrix([s.diff(b, c) for c in coords])
    hess = s.Matrix(3, 3, lambda i, j: s.diff(b, coords[i], coords[j])
                    - sum(gamma[k][i][j]*db[k] for k in range(3)))
    assert clean(hess-metric+db*db.T) == s.zeros(3)
    assert (db.T*metric.inv()*db)[0] == 1
    dilation_shift = s.expand_log(-s.log(4*y)+s.log(y), force=True)
    assert s.simplify(dilation_shift+s.log(4)) == 0
    assert dilation_shift != 0
    return {'hessian': str(hess), 'dilation_control_shift': str(dilation_shift)}


def cusp():
    r, x1, x2 = s.symbols('r x1 x2', real=True)
    h11, h12, h22, c = s.symbols('h11 h12 h22 c', real=True)
    domain_coords = [r, x1, x2]
    g = s.Matrix([[1, 0, 0], [0, s.exp(-2*r)*h11, s.exp(-2*r)*h12],
                  [0, s.exp(-2*r)*h12, s.exp(-2*r)*h22]])
    gi = g.inv()
    gam = christoffel(g, domain_coords)
    xx, yy, vv = s.symbols('X Y v', real=True)
    target = s.diag(s.exp(-2*vv), s.exp(-2*vv), 1)
    tg = christoffel(target, [xx, yy, vv])
    f = [-x1+x2, s.Integer(0), r+c]
    substitute = dict(zip([xx, yy, vv], f))
    tension = []
    for a in range(3):
        val = 0
        for i in range(3):
            for j in range(3):
                val += gi[i, j]*(s.diff(f[a], domain_coords[i], domain_coords[j])
                    - sum(gam[k][i][j]*s.diff(f[a], domain_coords[k]) for k in range(3))
                    + sum(tg[a][b][d].subs(substitute)*s.diff(f[b], domain_coords[i])
                          * s.diff(f[d], domain_coords[j]) for b in range(3) for d in range(3)))
        tension.append(s.simplify(val))
    k = (h11+2*h12+h22)/(h11*h22-h12**2)
    assert tension[0] == tension[1] == 0
    assert s.simplify(tension[2]+2-k*s.exp(-2*c)) == 0
    # Positive definiteness of h0 makes k positive; impose e^-2c=2/k.
    assert s.simplify(tension[2].subs(s.exp(-2*c), 2/k)) == 0
    wrong = tension[2].subs({h11: 1, h12: 0, h22: 1, c: s.log(2)})
    assert s.simplify(wrong) == -s.Rational(3, 2)
    j = s.Matrix(f).jacobian(domain_coords)
    df2 = s.simplify(s.trace(gi*j.T*target.subs(substitute)*j))
    assert s.simplify(df2-1-k*s.exp(-2*c)) == 0
    assert s.simplify(df2.subs(s.exp(-2*c), 2/k)) == 3
    a0, radius = s.symbols('A0 R', positive=True)
    energy = s.integrate(s.Rational(3, 2)*a0*s.exp(-2*r), (r, 0, s.oo))
    assert energy == 3*a0/4
    bulk = s.integrate(2*a0*s.exp(-2*r), (r, 0, radius))
    inner, outer = a0, -a0*s.exp(-2*radius)
    assert s.simplify(bulk-inner-outer) == 0
    assert s.simplify(bulk-outer) == a0  # dropping inner flux fails
    q0, r0 = s.symbols('Q0 r0', positive=True)
    lower = s.integrate(q0**2*s.exp(2*r)/(2*a0), (r, r0, radius))
    assert s.simplify(lower-q0**2*(s.exp(2*radius)-s.exp(2*r0))/(4*a0)) == 0
    return {'full_tension': [str(v) for v in tension], 'K': str(k),
            'wrong_normalization_radial_tension': str(s.simplify(wrong)),
            'energy': str(energy), 'inner_flux': str(inner), 'outer_flux': str(outer),
            'bulk_q': str(bulk), 'global_energy_lower_bound': str(lower)}


def main(output):
    base = Path(__file__).resolve().parent
    seal = json.loads((base/'SEAL.json').read_text())
    for name, digest in seal['sha256'].items():
        actual = hashlib.sha256((base/name).read_bytes()).hexdigest()
        if actual != digest:
            raise RuntimeError('Pre-execution seal mismatch: '+name)
    result = {'scope': 'exact identities supporting authored finite-volume cutoff proof; not a global PDE solution',
              'python': platform.python_version(), 'sympy': s.__version__,
              'algebra': algebra(), 'projector': [projection_variation(1, 1), projection_variation(1, 3)],
              'busemann': busemann(), 'cusp': cusp(), 'all_assertions_passed': True,
              'not_established': ['global sourced completion', 'physical fermion spectrum',
                                  'full TOE', 'independent proof review', 'full repository certification']}
    Path(output).write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main(sys.argv[1])
