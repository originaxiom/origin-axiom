"""R19: exact flat-character cohomology and actual-parent anomaly controls.

See HOLONOMY_SPECTRUM_DESIGN.md for the independent analytic argument.
No object-selected vacuum, physical mass, inflow or TOE is certified.
"""
from __future__ import annotations

import ast
from collections import Counter
from fractions import Fraction
from functools import lru_cache
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path
import subprocess
import time

import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
SM_PIN = 'd1a91c7a'
SM_SOURCE = 'frontier/B1282_the_siblings_germ/verification/siblings_faces.py'
FOX_SOURCE = 'frontier/B787_interaction_programme/D1_fox_calculus/compute.py'
RELATOR = 'aabbAbAABBaB'
X, Y = sp.symbols('x y', nonzero=True)


def definitions(text, names, namespace=None):
    """Reuse named pure definitions without executing a producer's top level."""
    tree = ast.parse(text)
    nodes = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name in names]
    if {n.name for n in nodes} != set(names):
        raise ValueError('missing banked function')
    env = {} if namespace is None else dict(namespace)
    exec(compile(ast.Module(body=nodes, type_ignores=[]), '<pinned-definitions>', 'exec'), env)
    return env


@lru_cache(maxsize=1)
def banked():
    fox_text = (ROOT / FOX_SOURCE).read_text()
    sm_text = subprocess.run(['git', 'show', f'{SM_PIN}:{SM_SOURCE}'], cwd=ROOT,
                             check=True, text=True, capture_output=True).stdout
    fox = definitions(fox_text, ('reduce_word', 'gr_clean', 'fox_word'))
    sm = definitions(sm_text, ('alexander_m202',), {'sp': sp})
    return fox, sm, {FOX_SOURCE: hashlib.sha256(fox_text.encode()).hexdigest(),
                    f'{SM_PIN}:{SM_SOURCE}': hashlib.sha256(sm_text.encode()).hexdigest()}


def encoded(word):
    letters = {'a': 1, 'A': -1, 'b': 2, 'B': -2}
    return tuple(letters[c] for c in word)


def abelian_image(word, x=X, y=Y):
    return x**sum((c == 1)-(c == -1) for c in word) * y**sum((c == 2)-(c == -2) for c in word)


def fox_row(word=RELATOR):
    fox = banked()[0]['fox_word']
    return sp.Matrix([[sp.cancel(sum(c*abelian_image(w) for w, c in fox(encoded(word), g).items()))
                       for g in (1, 2)]])


def triangular_row(word=RELATOR):
    """Independent cocycle method: upper-right entries of 2 x 2 products."""
    out = []
    for g in ('a', 'b'):
        images = {'a': sp.Matrix([[X, int(g == 'a')], [0, 1]]),
                  'b': sp.Matrix([[Y, int(g == 'b')], [0, 1]])}
        images.update({c.upper(): images[c].inv() for c in ('a', 'b')})
        product = sp.eye(2)
        for c in word:
            product = product*images[c]
        out.append(sp.cancel(product[0, 1]))
    return sp.Matrix([out])


def relator_hypotheses(word):
    w = encoded(word)
    reduced = banked()[0]['reduce_word'](w)
    cyclic = bool(w) and reduced == w and w[0] != -w[-1]
    periods = [d for d in range(1, len(w)) if len(w) % d == 0 and w == w[:d]*(len(w)//d)]
    return dict(cyclically_reduced=cyclic, proper_periods=periods,
                nonproper_power=cyclic and not periods)


@lru_cache(maxsize=1)
def identities():
    F = fox_row()
    P = sp.cancel(X*F[0]/(1-Y))
    old, a, b = banked()[1]['alexander_m202']()
    old = old.subs({a: X, b: Y})
    sphere = (1+X+Y)*(1+1/X+1/Y)-2
    return dict(polynomial=sp.expand(P), fox=F,
                pinned_match=sp.cancel(P+old) == 0,
                second_method=all(sp.cancel(v) == 0 for v in F-triangular_row()),
                nilpotent=sp.cancel((F*sp.Matrix([X-1, Y-1]))[0]) == 0,
                factorization=sp.cancel(F[1]-(X-1)*P/X) == 0,
                unitary_locus=sp.cancel(P/(X*Y)-sphere) == 0,
                inversion=sp.cancel(P/(X*Y)-(P/(X*Y)).subs({X: 1/X, Y: 1/Y}, simultaneous=True)) == 0,
                missing_term_fails=sp.cancel(((F+sp.Matrix([[1, 0]]))*sp.Matrix([X-1, Y-1]))[0]) != 0)


def exact_matrix(M):
    return M.applyfunc(lambda v: sp.simplify(sp.expand_complex(v)))


def cochains(x, y, k=3, transports=None):
    if not isinstance(k, int) or k < 0:
        raise ValueError('nonnegative integral number of contractible source components required')
    x, y = sp.sympify(x), sp.sympify(y)
    if any(v.has(sp.Float) or sp.simplify(v*sp.conjugate(v)-1) != 0 for v in (x, y)):
        raise ValueError('an exact unitary character is required for this analytic class')
    transports = [sp.Integer(1)]*k if transports is None else list(map(sp.sympify, transports))
    if len(transports) != k or any(sp.simplify(v*sp.conjugate(v)-1) != 0 for v in transports):
        raise ValueError('one unitary fibre identification per component required')
    F = exact_matrix(identities()['fox'].subs({X: x, Y: y}))
    base0 = exact_matrix(sp.Matrix([x-1, y-1]))
    d0 = base0.col_join(sp.Matrix(k, 1, transports))
    d1 = F.row_join(sp.zeros(1, k))
    assert exact_matrix(d1*d0) == sp.zeros(1, 1)
    r0, r1 = int(d0.rank()), int(d1.rank())
    base_r0 = int(base0.rank())
    base = [1-base_r0, 2-base_r0-r1, 1-r1, 0]
    result = [1-r0, 2+k-r0-r1, 1-r1, 0]
    les = [0, k-base[0]+base[1], base[2], base[3]] if k else base
    Pvalue = sp.simplify(identities()['polynomial'].subs({X: x, Y: y}))
    return dict(x=str(x), y=str(y), k=k, polynomial=str(Pvalue),
                trivial=sp.simplify(x-1) == 0 and sp.simplify(y-1) == 0,
                exceptional=sp.simplify(Pvalue) == 0,
                dimensions=[1, 2+k, 1, 0], differential_ranks=[r0, r1, 0],
                base_betti=base, relative_T=result, relative_E_dual=result[::-1],
                exact_sequence=les, exact_sequence_matches=result == les,
                euler=sum((-1)**i*n for i, n in enumerate(result)))


@lru_cache(maxsize=1)
def character_controls():
    rows = []
    for n, z in ((2, sp.Integer(-1)), (3, (-1+sp.I*sp.sqrt(3))/2), (4, sp.I)):
        for i, j in itertools.product(range(n), repeat=2):
            r = cochains(sp.simplify(z**i), sp.simplify(z**j))
            rows.append(dict(grid_n=n, exponents=[i, j], **r))
    for sign in (-1, 1):
        z = (-3+sign*sp.I*sp.sqrt(7))/4
        rows.append(dict(grid_n=None, diagonal_root_sign=sign, **cochains(z, z)))
    return rows


def load_local(name, filename):
    spec = importlib.util.spec_from_file_location(name, Path(__file__).with_name(filename))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@lru_cache(maxsize=1)
def covariant_controls():
    wc = load_local('r19_weighted_controls', 'weighted_cohomology.py')
    cd = wc.cd
    r, x, y = cd.COORDS
    eta = {(1,): sp.I, (2,): 2*sp.I}
    def dA(v):
        return cd.add(cd.exterior(v), cd.wedge(eta, v))
    def K(v):
        return cd.clean({j[1:]: sp.integrate(c, (r, 0, r)) for j, c in v.items() if j and j[0] == 0})
    def P(v):
        return cd.clean({j: c.subs(r, 0) for j, c in v.items() if 0 not in j})
    H = r*r+x*y+r*x
    dH = cd.exterior({(): H})
    rows = []
    for j in cd.BASIS:
        v = {j: 1+r+x+y}
        rows.append(dict(degree=len(j), indices=list(j),
                         flat_square=dA(dA(v)) == {},
                         homotopy=cd.add(dA(K(v)), K(dA(v)), cd.scale(v, -1), P(v)) == {},
                         weighted_conjugacy=cd.add(dA(cd.scale(v, sp.exp(H))),
                            cd.scale(cd.add(dA(v), cd.wedge(dH, v)), -sp.exp(H))) == {}))
    bad_eta = {(1,): sp.I*r}
    def curved(v):
        return cd.add(cd.exterior(v), cd.wedge(bad_eta, v))
    phase = sp.exp(sp.I*(r+x))
    return dict(rows=rows, curved_square_nonzero=curved(curved({(): sp.Integer(1)})) != {},
                unitary_gauge_norm=sp.simplify(phase*sp.conjugate(phase)),
                strong_plus=wc.strong_class(1, (1, 1, 1), (3, 3)),
                strong_minus=wc.strong_class(-1, (1, 1, 1), (3, 3)))


def e6_cartan():
    C = 2*sp.eye(6)
    for i, j in ((0, 2), (2, 3), (3, 4), (4, 5), (1, 3)):
        C[i, j] = C[j, i] = -1
    return C


def weyl_orbit(C, seed):
    seen, queue = set(), [tuple(seed)]
    while queue:
        v = queue.pop()
        if v in seen:
            continue
        seen.add(v)
        for i in range(C.rows):
            new = list(v)
            new[i] -= sum(C[i, j]*v[j] for j in range(C.cols))
            queue.append(tuple(new))
    return sorted(seen)


@lru_cache(maxsize=1)
def parent_controls():
    C = e6_cartan()
    u = C.inv()[:, 0]
    roots = weyl_orbit(C, sp.eye(6)[:, 0])
    weights27 = weyl_orbit(C, u)
    by_q = {q: [sp.Matrix(v) for v in roots if v[0] == q] for q in (-1, 0, 1)}
    w16 = by_q[1]
    w10 = [sp.Matrix(v) for v in weights27 if v[0] == -sp.Rational(2, 3)]
    def labels(v):
        return (C*v)[1:, :]
    def quadratic(vs):
        return sum((labels(v)*labels(v).T for v in vs), sp.zeros(5))
    T16, T10 = quadratic(w16), quadratic(w10)
    h = sp.Matrix(sp.symbols('h1:6'))
    pure_cubic = sp.expand(sum(((labels(v).T*h)[0])**3 for v in w16))
    old = load_local('r19_original_parent', 'global_singular.py').e6_parent()
    adjoint_dims = Counter(v[0] for v in roots)
    adjoint_dims[0] += 6
    actual_dims = {str(q): n for q, n in sorted(adjoint_dims.items())}
    def anomaly(nplus, nminus):
        terms = [(nplus, v) for v in by_q[1]]+[(nminus, v) for v in by_q[-1]]
        mixed = sum((n*v[0]*labels(v)*labels(v).T for n, v in terms), sp.zeros(5))
        value = 2*(nplus-nminus)
        return dict(Tr_u=sum(n*v[0] for n, v in terms),
                    Tr_u3=sum(n*v[0]**3 for n, v in terms),
                    Spin10_squared_u=value, mixed_matrix_matches=mixed == value*T10)
    anomaly27 = dict(Tr_u=sum(v[0] for v in weights27), Tr_u3=sum(v[0]**3 for v in weights27),
                     mixed_matrix=sum((v[0]*labels(sp.Matrix(v))*labels(sp.Matrix(v)).T for v in weights27), sp.zeros(5)))
    b864_text = (ROOT/'frontier/B864_anomaly_ledger/anomaly_ledger.py').read_text()
    b864 = definitions(b864_text, ('parent_level', 'truncated_level'), {'Fr': Fraction})
    b864_full, _ = b864['parent_level']()
    b864_spinor, _ = b864['truncated_level']()
    return dict(root_count=len(roots), fundamental_weight_count=len(weights27),
                adjoint_charge_dimensions=actual_dims, r15_match=actual_dims == old['adjoint_charge_dimensions'],
                u_simple_coroot_coordinates=list(u), cocharacter_denominator=int(sp.ilcm(*[v.q for v in u])),
                pi_u_parent_order=int(sp.ilcm(*[(v/2).q for v in u])),
                pi_u_adjoint_order=int(sp.ilcm(*[sp.Rational(v[0], 2).q for v in roots])),
                fundamental_u_charges={str(q): n for q, n in sorted(Counter(v[0] for v in weights27).items())},
                fundamental_psi_charges={str(q): n for q, n in sorted(Counter(3*v[0] for v in weights27).items())},
                spinor_vector_trace_ratio_two=T16 == 2*T10, pure_spin10_cubic=pure_cubic,
                anomaly_four_one=anomaly(4, 1), anomaly_three_zero=anomaly(3, 0),
                anomaly_vectorlike_pair=anomaly(1, 1), anomaly_full_27=anomaly27,
                b864_parent_psi=b864_full, b864_spinor_charge_one=b864_spinor,
                parent_connection_and_sources_selected=False)


def cusp_norm_controls():
    s, S = sp.symbols('s S', real=True)
    return dict(constant_gauge_zero_form=sp.integrate(sp.exp(-2*s), (s, S, sp.oo)),
                nonzero_period_one_form=sp.integrate(sp.Integer(1), (s, S, sp.oo)))


def run():
    import snappy
    start = time.monotonic()
    Q = snappy.Manifold('m202')
    pi = Q.fundamental_group()
    assert list(pi.generators()) == ['a', 'b'] and list(pi.relators()) == [RELATOR]
    sums = [RELATOR.count(c)-RELATOR.count(c.upper()) for c in ('a', 'b')]
    peripherals = [list(pair) for pair in pi.peripheral_curves()]
    peripheral_exponents = [[w.count(c)-w.count(c.upper()) for c in ('a', 'b')]
                             for pair in peripherals for w in pair]
    algebra = identities()
    assert all(algebra[key] for key in ('pinned_match', 'second_method', 'nilpotent', 'factorization',
                                       'unitary_locus', 'inversion', 'missing_term_fails'))
    arcs = [cochains(x, y, k) for x, y in ((1, 1), (-1, 1)) for k in range(4)]
    phase_control = cochains(-1, 1, 3, [1, sp.I, -1])
    out = dict(scope='declared unitary strong-source maximal complex; not object-selected physics',
               versions=dict(snappy=snappy.version(), sympy=sp.__version__),
               geometry=dict(name='m202', cusps=int(Q.num_cusps()), relator=RELATOR,
                             exponent_sums=sums, homology=str(Q.homology()),
                             peripherals=peripherals, peripheral_exponents=peripheral_exponents,
                             peripheral_rank=int(sp.Matrix(peripheral_exponents).rank()),
                             **relator_hypotheses(RELATOR)),
               algebra=algebra, dependency_sha256=banked()[2], characters=character_controls(),
               arc_controls=arcs, fibre_phase_control=phase_control, covariant=covariant_controls(),
               parent=parent_controls(), cusp_norms=cusp_norm_controls())
    out['runtime_seconds'] = time.monotonic()-start
    return out


if __name__ == '__main__':
    print(json.dumps(run(), default=str, indent=2, sort_keys=True), flush=True)
