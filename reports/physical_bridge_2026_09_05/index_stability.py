"""R26 controls of a fixed-domain Fredholm argument, not a PDE eigensolver.

The infinite-dimensional proof and physical restrictions are separate from
these algebraic controls. No stationary source or numerical gap is assumed.
"""
from __future__ import annotations

from functools import lru_cache
import importlib.util
import json
from pathlib import Path
import time

import sympy as sp


def local(name, filename):
    spec = importlib.util.spec_from_file_location(name, Path(__file__).with_name(filename))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


cd = local('r26_forms', 'charged_domain.py')
hs = local('r26_flat', 'holonomy_spectrum.py')
PARITY = sp.diag(*[(-1)**len(b) for b in cd.BASIS])


def matrix_of(operation):
    out = sp.zeros(8)
    for j, basis in enumerate(cd.BASIS):
        for target, coefficient in operation({basis: sp.Integer(1)}).items():
            out[cd.BASIS.index(target), j] = coefficient
    return out


def simplify_matrix(matrix):
    return matrix.applyfunc(sp.simplify)


@lru_cache(maxsize=1)
def perturbation_symbol():
    q = sp.Symbol('q', real=True)
    av = sp.symbols('a0:3', real=True)
    vv = sp.symbols('v0:3', real=True)
    a = {(i,): av[i] for i in range(3)}
    v = {(i,): vv[i] for i in range(3)}
    metric = cd.MetricForms((1, 1, 1))
    h = cd.exterior({(): cd.r**2 + cd.theta*cd.t})

    def covariant(form):
        return cd.add(cd.exterior(form), cd.wedge(cd.add(h, v, cd.scale(a, -sp.I*q)), form))

    def adjoint(form):
        # In dimension 3: delta_(A,H) on degree j = (-1)^j * (d_A-dH wedge) *.
        return cd.add(*(cd.scale(metric.star(cd.add(
            cd.exterior(metric.star({b: coefficient})),
            cd.wedge(cd.add(cd.scale(h, -1), cd.scale(v, -1), cd.scale(a, -sp.I*q)),
                     metric.star({b: coefficient})))), (-1)**len(b))
                        for b, coefficient in form.items()))

    original = matrix_of(lambda f: cd.add(covariant(f), adjoint(f), cd.scale(metric.D(f, h), -1))).applyfunc(sp.expand)
    ea = matrix_of(lambda f: cd.wedge(a, f))
    ia = matrix_of(lambda f: metric.contract_gradient(f, a))
    ev = matrix_of(lambda f: cd.wedge(v, f))
    iv = matrix_of(lambda f: metric.contract_gradient(f, v))
    expected = -sp.I*q*(ea-ia)+ev+iv
    norm_square = q*q*sum(x*x for x in av)+sum(x*x for x in vv)
    wrong_adjoint = -sp.I*q*(ea+ia)+ev+iv
    return dict(operator=original, expected=expected,
                actual_map=simplify_matrix(original-expected) == sp.zeros(8),
                hermitian=original.H == original,
                odd=original*PARITY+PARITY*original == sp.zeros(8),
                square=simplify_matrix(original*original), norm_square=norm_square,
                scalar_norm=simplify_matrix(original*original-norm_square*sp.eye(8)) == sp.zeros(8),
                wrong_adjoint_rejected=original != wrong_adjoint,
                wrong_adjoint_not_hermitian=wrong_adjoint.H != wrong_adjoint,
                even_scalar_not_odd=sp.eye(8)*PARITY+PARITY*sp.eye(8) != sp.zeros(8))


@lru_cache(maxsize=1)
def curvature_witness():
    x, y, z = cd.COORDS
    epsilon, q = sp.symbols('epsilon q', real=True)
    radius_square = x*x+y*y+z*z
    bump = sp.exp(-1/(1-radius_square))  # smooth zero extension outside the open unit ball
    a = {(1,): epsilon*bump*x}
    h = cd.exterior({(): x*x+y*z})
    eta = cd.add(h, cd.scale(a, -sp.I*q))
    curvature = cd.exterior(a)

    def differential(f):
        return cd.add(cd.exterior(f), cd.wedge(eta, f))

    rows = []
    profile = 1+x+y+z
    for basis in cd.BASIS:
        form = {basis: profile}
        square = differential(differential(form))
        target = cd.scale(cd.wedge(curvature, form), -sp.I*q)
        rows.append(dict(basis=basis, identity=cd.add(square, cd.scale(target, -1)) == {}))
    centre = {x: 0, y: 0, z: 0}
    f0 = {b: sp.simplify(c.subs(centre)) for b, c in curvature.items()}
    zero_square = differential(differential({(): sp.Integer(1)}))
    return dict(bump=bump, connection=a, curvature=curvature,
                centre_curvature=f0, nonflat=f0.get((0, 1), 0) == epsilon/sp.E,
                square_rows=rows, zero_form_square_nonzero=zero_square != {},
                centre_square=sp.simplify(zero_square[(0, 1)].subs(centre)),
                zero_amplitude_flat=all(sp.simplify(c.subs(epsilon, 0)) == 0 for c in curvature.values()),
                centre_mass=h, sphere_support_radius=1)


def channel(k, n, strength, gap=1):
    """Finite block of the infinite rank-one comparison, not the physical manifold."""
    if not isinstance(k, int) or k < 0 or not isinstance(n, int) or n < 1:
        raise ValueError('nonnegative k and positive matched-channel count required')
    strength, gap = sp.sympify(strength), sp.sympify(gap)
    if any(x.has(sp.Float) or x.is_real is not True for x in (strength, gap)) or gap.is_positive is not True:
        raise ValueError('exact real strength and positive exact gap required')
    t0 = sp.zeros(n, k).row_join(gap*sp.eye(n))
    perturbation = sp.zeros(n, n+k)
    perturbation[0, k] = -strength
    block = t0+perturbation
    rank = block.rank()
    d0 = sp.BlockMatrix([[sp.zeros(n+k), t0.H], [t0, sp.zeros(n)]]).as_explicit()
    d1 = sp.BlockMatrix([[sp.zeros(n+k), block.H], [block, sp.zeros(n)]]).as_explicit()
    grading = sp.diag(*([1]*(n+k)+[-1]*n))  # + labels odd/left in this comparison
    return dict(k=k, n=n, strength=strength, gap=gap, block=block,
                odd_kernel=n+k-rank, even_kernel=n-rank, index=k,
                computed_index=(n+k-rank)-(n-rank),
                delta_operator=d1-d0, base_operator=d0, operator=d1,
                hermitian=d1.H == d1, odd=d1*grading+grading*d1 == sp.zeros(2*n+k),
                small_norm=abs(strength) < gap,
                perturbation_rank=perturbation.rank())


@lru_cache(maxsize=1)
def channel_controls():
    rows = []
    for k in (0, 1, 3, 5):
        for n in (1, 2, 4):
            for t in (-2, 0, sp.Rational(1, 2), 1, sp.Rational(3, 2)):
                r = channel(k, n, t)
                rows.append({name: r[name] for name in (
                    'k', 'n', 'strength', 'gap', 'odd_kernel', 'even_kernel',
                    'computed_index', 'small_norm', 'perturbation_rank', 'hermitian', 'odd')})
    return rows


def resolvent_controls():
    row = channel(1, 1, 0)
    d0 = row['base_operator']
    # Couple the original zero mode to the matched channel. A proportional
    # change of the sole matched channel COMMUTES and cannot test order.
    b = sp.zeros(3)
    b[0, 2] = b[2, 0] = sp.Rational(1, 2)
    d1 = d0+b
    spectral_parameter = 2*sp.I
    identity = sp.eye(d0.rows)
    r0 = (d0-spectral_parameter*identity).inv()
    factor = (identity+b*r0)*(d0-spectral_parameter*identity)
    r1 = (d1-spectral_parameter*identity).inv()
    return dict(factorization=simplify_matrix(factor-(d1-spectral_parameter*identity)) == sp.zeros(d0.rows),
                inverse_difference=simplify_matrix(r1-r0+r1*b*r0) == sp.zeros(d0.rows),
                wrong_order_rejected=simplify_matrix((d0-spectral_parameter*identity)*(identity+b*r0)
                                                     -(d1-spectral_parameter*identity)) != sp.zeros(d0.rows))


def tail_controls(gap=1):
    gap = sp.sympify(gap)
    if gap.is_positive is not True or gap.has(sp.Float):
        raise ValueError('positive exact gap required')
    # Independent positive eigenvectors of the infinite matched-channel tail.
    w0 = sp.Matrix([1, 0, 1, 0])/sp.sqrt(2)
    w1 = sp.Matrix([0, 1, 0, 1])/sp.sqrt(2)
    d = sp.BlockMatrix([[sp.zeros(2), gap*sp.eye(2)], [gap*sp.eye(2), sp.zeros(2)]]).as_explicit()
    r = (d-sp.I*sp.eye(4)).inv()
    difference = r*(w0-w1)
    distance = sp.simplify((difference.H*difference)[0])
    # -D0 on the WHOLE infinite tail is bounded but not relatively compact.
    killed = []
    for n in (1, 2, 4, 8):
        row = channel(3, n, 0, gap)
        zero = row['base_operator']-row['base_operator']
        killed.append(dict(matched=n, full_kernel=zero.cols-zero.rank()))
    return dict(orthonormal=(w0.H*w1)[0] == 0,
                both_eigenvectors=d*w0 == gap*w0 and d*w1 == gap*w1,
                resolvent_distance_squared=distance,
                distance_formula=sp.simplify(distance-2/(gap*gap+1)) == 0,
                tail_kill=killed)


def initial_kernel_controls():
    zeta = (-1+sp.I*sp.sqrt(3))/2
    exception = (-3+sp.I*sp.sqrt(7))/4
    rows = []
    for label, x, y in [('pair_free', zeta, sp.conjugate(zeta)),
                        ('trivial', 1, 1), ('exceptional', exception, exception)]:
        row = hs.cochains(x, y, 3)
        b = row['relative_T']
        rows.append(dict(label=label, betti=b, odd=b[1]+b[3], even=b[0]+b[2],
                         index=b[1]+b[3]-b[0]-b[2], euler=row['euler']))
    return rows


def serial(value):
    if isinstance(value, sp.MatrixBase):
        return serial(value.tolist())
    if isinstance(value, sp.Basic):
        return str(value)
    if isinstance(value, dict):
        return {str(k): serial(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [serial(v) for v in value]
    return value


def run():
    start = time.monotonic()
    result = dict(symbol=perturbation_symbol(), curvature=curvature_witness(),
                  channel_rows=channel_controls(), resolvent=resolvent_controls(),
                  tails=[tail_controls(d) for d in (1, 2, 3)],
                  original_kernels=initial_kernel_controls(),
                  scope='Controls of the displayed fixed-domain argument; not a stationary coupled source, numerical PDE spectrum or physical completion.')
    result['runtime_seconds'] = time.monotonic()-start
    return serial(result)


if __name__ == '__main__':
    print(json.dumps(run(), indent=2, sort_keys=True))
