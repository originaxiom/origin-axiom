"""R39: full candidate-parent residuals and positive-operator controls.

No empirical input, selected parent, chiral vacuum, localized source,
quantum phase or gravitational completion is asserted. See the sealed
design/proof for the global arguments beyond these finite exact checks.
"""
from __future__ import annotations

from collections import Counter
from functools import lru_cache
import importlib.util
import itertools
import json
from pathlib import Path
import time

import sympy as sp

SPEC = importlib.util.spec_from_file_location(
    'r39_parent_prior', Path(__file__).with_name('parent_vertex.py'))
pv = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(pv)
x, y = sp.symbols('x y', real=True)
z = sp.Symbol('z', positive=True)
COORDS = (x, y, z)
U = sp.diag(3, -1, -1, -1)


def clean(M):
    return M.applyfunc(sp.simplify) if isinstance(M, sp.MatrixBase) else sp.simplify(M)


def zero(M):
    return all(sp.simplify(a) == 0 for a in M)


def comm(A, B):
    return A*B-B*A


def block(h, alpha, beta, B):
    if alpha.shape != (1, 3) or beta.shape != (3, 1) or B.shape != (3, 3):
        raise ValueError('one row, one column and a three-by-three block required')
    if sp.simplify(sp.trace(B)) != 0:
        raise ValueError('the neutral block must be traceless')
    return sp.Matrix.vstack(sp.Matrix.hstack(sp.Matrix([[3*h]]), alpha),
                            sp.Matrix.hstack(beta, B-h*sp.eye(3)))


def symbols_block(label):
    h = sp.Symbol(label+'h')
    a = sp.Matrix(1, 3, sp.symbols(label+'a0:3'))
    b = sp.Matrix(3, 1, sp.symbols(label+'b0:3'))
    v = sp.symbols(label+'v0:8')
    B = sp.Matrix([[v[0], v[1], v[2]], [v[3], v[4], v[5]],
                   [v[6], v[7], -v[0]-v[4]]])
    return h, a, b, B


@lru_cache(maxsize=1)
def branching():
    d = pv.root_data()
    v = tuple(sp.Matrix(a)/2 for a in
              ((-1, 1, 1), (-1, -1, -1), (1, -1, 1), (1, 1, -1)))
    roots = d['roots']
    d5 = {r[:5] for r in roots if r[5:] == (0, 0, 0)}
    d3 = {r[5:] for r in roots if r[:5] == (0,)*5}
    vec = set()
    for i, sign in itertools.product(range(5), (-1, 1)):
        w = [0]*5
        w[i] = sign
        vec.add(tuple(w))
    spin = {r[:5] for r in roots if sp.Matrix(r).dot(d['U']) == 1}
    actual = Counter(roots)
    actual[(0,)*8] += 8
    expected = Counter(w+(0,)*3 for w in d5)
    expected[(0,)*8] += 5
    expected.update((0,)*5+w for w in d3)
    expected[(0,)*8] += 3
    expected.update(w+tuple(v[i]+v[j]) for w in vec
                    for i, j in itertools.combinations(range(4), 2))
    expected.update(w+tuple(-a) for w in spin for a in v)
    expected.update(tuple(-t for t in w)+tuple(a) for w in spin for a in v)
    wrong = Counter(w+(0,)*3 for w in d5)
    wrong[(0,)*8] += 8
    wrong.update((0,)*5+w for w in d3)
    wrong.update(w+tuple(v[i]+v[j]) for w in vec
                 for i, j in itertools.combinations(range(4), 2))
    wrong.update(w+tuple(a) for w in spin for a in v)
    wrong.update(tuple(-t for t in w)+tuple(-a) for w in spin for a in v)
    t0, t1, t2 = sp.symbols('t0 t1 t2', real=True)
    eigenvalues = (t0, t1, t2, -t0-t1-t2)
    embedded = sum((a*t for a, t in zip(v, eigenvalues)), sp.zeros(3, 1))
    defining_trace = sum(t*t for t in eigenvalues)
    adjoint_trace = sp.expand(sum(sp.Matrix(r[5:]).dot(embedded)**2 for r in roots))
    trace_ratio = sp.cancel(adjoint_trace/defining_trace)
    return dict(weights=v, d5=d5, vector=vec, spin=spin, actual=actual,
                expected=expected, wrong=wrong,
                charges=[a.dot(d['U'][5:, :]) for a in v],
                weight_gram=sp.Matrix(4, 4, lambda i, j: v[i].dot(v[j])),
                all_a3_roots={tuple(a-b) for a in v for b in v if a != b} == d3,
                actual_spinor=spin == {tuple(d['B'].inv()*(d['C']*w)[1:, :])
                                      for w in pv.ac.data()['spinor']},
                adjoint_trace=adjoint_trace, defining_trace=defining_trace,
                trace_ratio=trace_ratio,
                center_phases=[sp.I**j for j in range(4)])


@lru_cache(maxsize=1)
def curvature_blocks():
    hi, ai, bi, Bi = symbols_block('i')
    hj, aj, bj, Bj = symbols_block('j')
    dh, da, db, dB = symbols_block('d')
    direct = block(dh, da, db, dB)+comm(block(hi, ai, bi, Bi), block(hj, aj, bj, Bj))
    f00 = sp.Matrix([[3*dh+(ai*bj-aj*bi)[0]]])
    f0b = da+4*(hi*aj-hj*ai)+ai*Bj-aj*Bi
    fb0 = db-4*(hi*bj-hj*bi)+Bi*bj-Bj*bi
    fbb = -dh*sp.eye(3)+dB+comm(Bi, Bj)+bi*aj-bj*ai
    expected = sp.Matrix.vstack(sp.Matrix.hstack(f00, f0b), sp.Matrix.hstack(fb0, fbb))
    residual = (direct-expected).applyfunc(sp.expand)
    return dict(residual=residual, trace=sp.expand(sp.trace(direct)),
                off_row=direct[:1, 1:], expected_row=f0b,
                omitted_neutral_row=(ai*Bj-aj*Bi).applyfunc(sp.expand),
                reversed_charge_column=8*(hi*bj-hj*bi))


@lru_cache(maxsize=1)
def restricted_moment():
    h = sp.symbols('h0:3', real=True)
    alpha = sp.Matrix(3, 3, sp.symbols('a0:9'))
    dh = sp.Symbol('divh', real=True)
    da = sp.Matrix(1, 3, sp.symbols('diva0:3'))
    C = tuple(block(h[i], alpha[i:i+1, :], sp.zeros(3, 1), sp.zeros(3)) for i in range(3))
    dC = block(dh, da, sp.zeros(3, 1), sp.zeros(3))
    moment = dC+dC.H+sum((comm(c, c.H) for c in C), sp.zeros(4))
    G = alpha.H*alpha
    row = da-4*sum((h[i]*alpha[i:i+1, :] for i in range(3)), sp.zeros(1, 3))
    expected = sp.Matrix.vstack(
        sp.Matrix.hstack(sp.Matrix([[6*dh+sp.trace(G)]]), row),
        sp.Matrix.hstack(row.H, -2*dh*sp.eye(3)-G))
    phi = tuple((c+c.H)/2 for c in C)
    A = tuple((c-c.H)/2 for c in C)
    dstar = -(dC+dC.H)/2-sum((comm(a, p) for a, p in zip(A, phi)), sp.zeros(4))
    projector_pairing = sum(sp.trace(p*comm(a, U)) for a, p in zip(A, phi))
    return dict(residual=(moment-expected).applyfunc(sp.expand), gram=G,
                source_conversion=(moment+2*dstar).applyfunc(sp.expand),
                projector_pairing=sp.expand(projector_pairing),
                expected_projector_pairing=-2*sp.trace(G),
                scalar_source_pairing=sp.trace(U), H_source_pairing=sp.trace(U*U))


def gram_residual(alpha):
    if alpha.shape != (3, 3):
        raise ValueError('three internal components and three charged entries required')
    G = alpha.H*alpha
    return clean(G-sp.trace(G)*sp.eye(3)/3)


def generators():
    H = sp.diag(3, 1, -1, -3)
    E = sp.zeros(4)
    for i, value in enumerate((sp.sqrt(3), 2, sp.sqrt(3))):
        E[i, i+1] = value
    return E, E.H, H


def connection():
    E, F, H = generators()
    return E/z, sp.I*E/z, H/(2*z)


def curvature(C):
    return tuple(clean(C[j].diff(COORDS[i])-C[i].diff(COORDS[j])+comm(C[i], C[j]))
                 for i, j in itertools.combinations(range(3), 2))


def divergence(forms, hyperbolic=True):
    if hyperbolic:
        return clean(z**3*sum(((a/z).diff(t) for a, t in zip(forms, COORDS)), sp.zeros(forms[0].rows, forms[0].cols)))
    return clean(sum((a.diff(t) for a, t in zip(forms, COORDS)), sp.zeros(forms[0].rows, forms[0].cols)))


def moment_parts(C, hyperbolic=True):
    div = divergence(tuple(c+c.H for c in C), hyperbolic)
    bracket = clean((z**2 if hyperbolic else 1)*sum((comm(c, c.H) for c in C), sp.zeros(C[0].rows)))
    return div, bracket, clean(div+bracket)


def laplacian_zero(C, section):
    differential = tuple(section.diff(t)+c*section for t, c in zip(COORDS, C))
    return clean(-divergence(differential)+z**2*sum((c.H*w for c, w in zip(C, differential)), sp.zeros(section.rows, 1)))


@lru_cache(maxsize=1)
def geometric_controls():
    E, F, H = generators()
    q = sp.Matrix([[sp.sqrt(z), (x+sp.I*y)/sp.sqrt(z)], [0, 1/sp.sqrt(z)]])
    fundamental = tuple(clean(q.inv()*q.diff(t)) for t in COORDS)
    e = sp.Matrix([[0, 1], [0, 0]])
    precursor = (e/z, sp.I*e/z, sp.diag(1, -1)/(2*z))
    C = connection()
    phi = tuple(clean((c+c.H)/2) for c in C)
    A = tuple(clean((c-c.H)/2) for c in C)
    W = tuple(clean(a/sp.I) for a in A)
    pure = tuple(clean(a+b) for a, b in zip(curvature(A),
                 (comm(phi[i], phi[j]) for i, j in itertools.combinations(range(3), 2))))
    higgs_derivative = tuple(clean(phi[j].diff(COORDS[i])-phi[i].diff(COORDS[j])
                                  +comm(A[i], phi[j])-comm(A[j], phi[i]))
                             for i, j in itertools.combinations(range(3), 2))
    dropped = tuple(block(c[0, 0]/3, c[:1, 1:], sp.zeros(3, 1), sp.zeros(3)) for c in C)
    dropped_I = moment_parts(dropped)[2]
    P = sp.diag(1, 0, 0, 0)
    trial = x*sp.eye(4)[:, 0]
    return dict(sl2_residuals=(comm(H, E)-2*E, comm(H, F)+2*F, comm(E, F)-H),
                precursor=fundamental, precursor_expected=precursor,
                curvature=curvature(C), divergence=moment_parts(C)[0],
                commutator=moment_parts(C)[1], moment=moment_parts(C)[2],
                hermitian_phi=all(zero(p-p.H) for p in phi),
                hermitian_W=all(zero(w-w.H) for w in W),
                real_flatness=pure, higgs_derivative=higgs_derivative,
                gauge_curvature=curvature(A),
                phi_norm=clean(z**2*sum(sp.trace(p*p) for p in phi)),
                flat_metric_moment=moment_parts(C, False)[2],
                dropped_moment=dropped_I, dropped_central=clean(sp.trace(U*dropped_I)/12),
                dropped_curvature=curvature(dropped),
                flag_preserved=all(zero((sp.eye(4)-P)*c*P) for c in C),
                adjoint_flag_preserved=all(zero((sp.eye(4)-P)*c.H*P) for c in C),
                laplacian_mixing=clean((sp.eye(4)-P)*laplacian_zero(C, trial)))


def exterior_action(X):
    pairs = list(itertools.combinations(range(X.rows), 2))
    result = sp.zeros(len(pairs))
    for col, (i, j) in enumerate(pairs):
        for k in range(X.rows):
            for a, b, value in ((k, j, X[k, i]), (i, k, X[k, j])):
                if a == b:
                    continue
                row = pairs.index(tuple(sorted((a, b))))
                result[row, col] += value if a < b else -value
    return result


def common_kernel(matrices):
    return sp.Matrix.vstack(*matrices).nullspace()


def endomorphism_basis(n):
    basis = []
    for i, j in itertools.permutations(range(n), 2):
        B = sp.zeros(n)
        B[i, j] = 1
        basis.append(B)
    for i in range(n-1):
        B = sp.zeros(n)
        B[i, i], B[n-1, n-1] = 1, -1
        basis.append(B)
    return basis


def bilinear_kernel(matrices):
    n = matrices[0].rows
    units = [sp.eye(n)[:, i]*sp.eye(n)[j, :] for i, j in itertools.product(range(n), repeat=2)]
    actions = [sp.Matrix.hstack(*[(X.T*B+B*X).reshape(n*n, 1) for B in units]) for X in matrices]
    return common_kernel(actions)


def root_closure(simple):
    seen = {tuple(a) for a in simple}
    todo = list(seen)
    while todo:
        r = sp.Matrix(todo.pop())
        for a in simple:
            s = tuple(r-2*r.dot(a)*a/a.dot(a))
            if s not in seen:
                seen.add(s)
                todo.append(s)
    return seen


@lru_cache(maxsize=1)
def invariants():
    gen = generators()
    wedge = tuple(exterior_action(X) for X in gen)
    base = endomorphism_basis(4)
    end = tuple(sp.Matrix.hstack(*[comm(X, B).reshape(16, 1) for B in base]) for X in gen)
    kernels = (common_kernel(gen), common_kernel(wedge), common_kernel(end))
    b = branching()
    surviving = Counter(b['d5'])
    surviving[(0,)*5] += 5
    for w in b['vector']:
        surviving[w] += len(kernels[1])
    for w in b['spin']:
        surviving[w] += len(kernels[0])
        surviving[tuple(-a for a in w)] += len(kernels[0])
    surviving[(0,)*5] += len(kernels[2])
    surviving = +surviving
    ee = sp.eye(5)
    simple = [ee[:, i]-ee[:, i+1] for i in range(4)]+[ee[:, 4]]
    cartan = sp.Matrix(5, 5, lambda i, j: 2*simple[i].dot(simple[j])/simple[i].dot(simple[i]))
    J = sp.zeros(4)
    for i, value in enumerate((1, -1, 1, -1)):
        J[i, 3-i] = value
    return dict(kernel_dimensions=[len(k) for k in kernels],
                wedge_kernels=kernels[1], wedge_actions=wedge,
                unbroken_weights=surviving, unbroken_dimension=sum(surviving.values()),
                B5_roots=root_closure(simple), cartan=cartan,
                J=J, invariance=[clean(X.T*J+J*X) for X in gen],
                bilinear_dimension=len(bilinear_kernel(gen)),
                with_U_bilinear_dimension=len(bilinear_kernel(gen+(U,))),
                flat_intertwiner=[clean(J*c+c.T*J) for c in connection()],
                adjoint_intertwiner=[clean(J*c.H+c.conjugate()*J) for c in connection()])


def cusp_norm():
    area, Z = sp.symbols('area Z', positive=True)
    density = geometric_controls()['phi_norm']*area/z**3
    return area, Z, sp.integrate(density, (z, Z, sp.oo))


def report():
    b, f, m, g, inv = branching(), curvature_blocks(), restricted_moment(), geometric_controls(), invariants()
    E, F, H = generators()
    area, Z, tail = cusp_norm()
    grams = [gram_residual(a) for a in (sp.diag(1, 0, 0), sp.diag(1, 1, 0), sp.eye(3))]
    checks = dict(
        actual_full_parent_roster=(b['actual'] == b['expected'] and sum(b['expected'].values()) == 248
                                  and b['actual_spinor'] and b['all_a3_roots']),
        charged_map_and_wrong_roster=(b['charges'] == [3, -1, -1, -1] and b['actual'] != b['wrong']
                                      and sum(b['wrong'].values()) == 248 and b['center_phases'][0] == 1
                                      and all(a != 1 for a in b['center_phases'][1:])),
        complete_curvature_blocks=(zero(f['residual']) and f['trace'] == 0
                                   and not zero(f['omitted_neutral_row']) and not zero(f['reversed_charge_column'])),
        complete_moment_blocks=(zero(m['residual']) and zero(m['source_conversion'])),
        gram_and_source_controls=(not zero(grams[0]) and not zero(grams[1]) and zero(grams[2])
                                  and sp.expand(m['projector_pairing']-m['expected_projector_pairing']) == 0
                                  and m['scalar_source_pairing'] == 0 and m['H_source_pairing'] == 12),
        native_geometric_connection=(all(zero(a) for a in g['sl2_residuals'])
                                     and g['precursor'] == g['precursor_expected'] and all(zero(a) for a in g['curvature'])),
        all_real_equations=(zero(g['moment']) and g['divergence'] == -2*H and g['commutator'] == 2*H
                            and all(zero(a) for a in g['real_flatness']+g['higgs_derivative'])
                            and g['hermitian_phi'] and g['hermitian_W']),
        noncommuting_metric_controls=(any(not zero(a) for a in g['gauge_curvature']) and not zero(g['flat_metric_moment'])),
        central_only_false_positive=(g['dropped_central'] == 0 and g['dropped_moment'] == sp.diag(0, -4, 2, 2)
                                     and any(not zero(a) for a in g['dropped_curvature'])),
        positive_norm=(g['phi_norm'] == 15 and tail == 15*area/(2*Z**2) and b['trace_ratio'] == 60),
        complete_invariant_kernels=(inv['kernel_dimensions'] == [0, 1, 0]
                                    and all(zero(a*v) for a in inv['wedge_actions'] for v in inv['wedge_kernels'])),
        unbroken_B5=(inv['unbroken_dimension'] == 55 and inv['unbroken_weights'][(0,)*5] == 5
                     and set(inv['unbroken_weights'])-{(0,)*5} == inv['B5_roots']
                     and len(inv['B5_roots']) == 50 and inv['cartan'].det() == 2),
        unitary_operator_self_duality=(inv['J'].H*inv['J'] == sp.eye(4) and inv['J'].T == -inv['J']
                                       and all(zero(a) for a in inv['invariance']+inv['flat_intertwiner']+inv['adjoint_intertwiner'])
                                       and inv['bilinear_dimension'] == 1 and inv['with_U_bilinear_dimension'] == 0),
        full_operator_mixes_old_lines=(g['flag_preserved'] and not g['adjoint_flag_preserved']
                                       and g['laplacian_mixing'] == sp.Matrix([0, sp.sqrt(3)*z, 0, 0])))
    return dict(checks=checks, all_checks_pass=all(checks.values()),
                branch_dimensions=[45, 15, 60, 64, 64], defining_charges=b['charges'],
                curvature_blocks_residual=f['residual'], moment_blocks_residual=m['residual'],
                source_conversion_residual=m['source_conversion'],
                source_pairings=dict(scalar=m['scalar_source_pairing'], H_center=m['H_source_pairing']),
                gram_residual_controls=grams,
                geometric={k: v for k, v in g.items() if k != 'precursor_expected'},
                cusp_tail=tail, parent_trace_ratio=b['trace_ratio'],
                adjoint_trace_phi_norm=b['trace_ratio']*g['phi_norm'],
                kernel_dimensions=inv['kernel_dimensions'],
                invariant_wedge=inv['wedge_kernels'], unbroken_dimension=inv['unbroken_dimension'],
                invariant_root_count=len(inv['B5_roots']), invariant_cartan=inv['cartan'],
                unitary_duality=inv['J'], bilinear_dimensions=[inv['bilinear_dimension'], inv['with_U_bilinear_dimension']],
                scope='Exact candidate-parent equations and operators; global proof separately authored. No physical chirality, parent selection, source completion, quantum gap or TOE.')


if __name__ == '__main__':
    started = time.monotonic()
    result = report()
    result['elapsed_seconds'] = time.monotonic()-started
    print(json.dumps(pv.ac.serial(result), indent=2))
    raise SystemExit(0 if result['all_checks_pass'] else 1)
