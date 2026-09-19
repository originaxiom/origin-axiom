"""R33: exact charged Spin(10) Yukawa and phase-locking controls.

This is an ADDED subgroup interaction, not a quantum SMG gap, a local
seven-dimensional fermion completion, or an object-selected vacuum.
No simulation, experimental fit or thermodynamic limit is performed.
"""
from __future__ import annotations

from functools import lru_cache
import importlib.util
import itertools
import json
from pathlib import Path
import time

import sympy as sp

SPEC = importlib.util.spec_from_file_location(
    'r33_anomaly_prior', Path(__file__).with_name('anomaly_completion.py'))
ac = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(ac)
I = sp.I
X = sp.Matrix([[0, 1], [1, 0]])
Y = sp.Matrix([[0, -I], [I, 0]])
Z = sp.diag(1, -1)


def clean(A):
    return A.applyfunc(sp.expand) if isinstance(A, sp.MatrixBase) else sp.expand(A)


def exact_vector(values, dimension=10):
    v = sp.Matrix(values)
    if v.shape != (dimension, 1) or any(x.has(sp.Float) for x in v):
        raise ValueError('exact column of the declared dimension required')
    return v


@lru_cache(maxsize=1)
def clifford_data():
    gamma = []
    for k in range(5):
        for pauli in (X, Y):
            gamma.append(sp.kronecker_product(*([Z]*k+[pauli]+[sp.eye(2)]*(4-k))))
    chirality = sp.kronecker_product(*([Z]*5))
    C = sp.eye(32)
    for k in range(1, 10, 2):
        C = C*gamma[k]
    sectors = {}
    for sign in (1, -1):
        indices = [j for j in range(32) if chirality[j, j] == sign]
        sectors[sign] = dict(
            indices=indices,
            yukawa=[(C*g).extract(indices, indices) for g in gamma],
            generators={(a, b): (gamma[a]*gamma[b]/2).extract(indices, indices)
                        for a, b in itertools.combinations(range(10), 2)},
            weights=[tuple((-I*gamma[2*k]*gamma[2*k+1]/2)[j, j]
                           for k in range(5)) for j in indices])
    return dict(gamma=gamma, chirality=chirality, C=C, sectors=sectors)


def mass_matrix(values, sign=-1):
    if sign not in (1, -1):
        raise ValueError('chiral sign must be +1 or -1')
    v = exact_vector(values)
    yy = clifford_data()['sectors'][sign]['yukawa']
    return clean(sum((v[a]*yy[a] for a in range(10)), sp.zeros(16)))


@lru_cache(maxsize=1)
def algebra_controls():
    d = clifford_data()
    gamma, C, G = d['gamma'], d['C'], d['chirality']
    sector_rows = {}
    for sign, sector in d['sectors'].items():
        yy = sector['yukawa']
        ward = []
        for (a, b), T in sector['generators'].items():
            for c in range(10):
                expected = int(c == a)*yy[b]-int(c == b)*yy[a]
                ward.append(T.T*yy[c]+yy[c]*T == expected)
        sector_rows[sign] = dict(
            dimension=len(sector['indices']),
            symmetric=all(v.T == v for v in yy),
            real_mass_identity=all(yy[a].H*yy[b]+yy[b].H*yy[a] == 2*int(a == b)*sp.eye(16)
                                   for a in range(10) for b in range(a, 10)),
            ward_equations=len(ward), ward_all=all(ward),
            antihermitian_real_direction=yy[0].H == -yy[0] and yy[0] != sp.zeros(16),
            missing_direction_fails=(sp.zeros(16).H*sp.zeros(16) != sp.eye(16)))
    return dict(
        hermitian_gamma=all(g.H == g for g in gamma),
        clifford=all(gamma[a]*gamma[b]+gamma[b]*gamma[a] == 2*int(a == b)*sp.eye(32)
                     for a in range(10) for b in range(a, 10)),
        C_antisymmetric=C.T == -C, C_unitary=C.H*C == sp.eye(32),
        charge_conjugation=all(C*g*C.inv() == -g.T for g in gamma),
        chirality_square=G*G == sp.eye(32),
        chirality_odd=all(G*g == -g*G for g in gamma),
        yukawa_even=all(G*C*g == C*g*G for g in gamma), sectors=sector_rows)


@lru_cache(maxsize=1)
def global_controls():
    d = ac.data()
    # Rows are the simple D5 roots in the repository order 1,2,3,4,5.
    B = sp.Matrix([[0, 0, 0, 1, 1], [0, 0, 0, 1, -1],
                   [0, 0, 1, -1, 0], [0, 1, -1, 0, 0], [1, -1, 0, 0, 0]])
    def orthogonal_weight(w):
        return B.inv()*(d['C']*w)[1:, :]
    psi = d['spinor']
    chi = [-w for w in psi]
    scalar = [-w for w in d['vector']]
    phi = ac.singlet_weight(4)
    sets = clifford_data()['sectors']
    cartan_variables = sp.Matrix(sp.symbols('h0:5'))
    psi_linear = sum((orthogonal_weight(w).T*cartan_variables)[0] for w in psi)
    psi_cubic = sum((orthogonal_weight(w).T*cartan_variables)[0]**3 for w in psi)
    monomial_charges = dict(mirror_yukawa=2-1-1, ordinary_yukawa=-2+1+1,
                            phase_lock=-4+2+2, dirac_pair=1-1,
                            wrong_yukawa=2+1+1, neutral_vector_mirror=0-1-1)
    return dict(
        D5_map=B, cartan_matched=B*B.T == d['C'][1:, 1:],
        psi_matches_positive=ac.tuples(orthogonal_weight(w) for w in psi) == set(sets[1]['weights']),
        chi_matches_negative=ac.tuples(orthogonal_weight(w) for w in chi) == set(sets[-1]['weights']),
        scalar_vector_weights=ac.tuples(orthogonal_weight(w) for w in scalar) ==
            {tuple(sign*sp.eye(5)[:, a]) for sign in (1, -1) for a in range(5)},
        all_H_weights_integral=all(ac.integral(w) for w in psi+chi+scalar+[phi]),
        charges=dict(psi=sorted({w[0] for w in psi}), chi=sorted({w[0] for w in chi}),
                     S=sorted({w[0] for w in scalar}), Phi=phi[0]),
        locking_weight_pairs=all(any(w+w2-phi == sp.zeros(6, 1) for w2 in scalar) for w in scalar),
        scalar_charge_two_singlet_rejected=not ac.integral(ac.singlet_weight(2)),
        monomial_charges=monomial_charges,
        pure_D5_linear=sp.expand(psi_linear), pure_D5_cubic=sp.expand(psi_cubic),
        full_H_light_anomaly=ac.anomaly(psi, 3),
        full_H_mirror_anomaly=ac.anomaly(chi, 3),
        vectorlike_anomaly=ac.anomaly(psi+chi, 3),
        weight_counts=dict(psi=len(psi), chi=len(chi), S=len(scalar)))


@lru_cache(maxsize=1)
def gap_controls():
    a, b, c = sp.symbols('a b c', real=True)
    rows = {}
    for sign in (1, -1):
        real_v = [sp.Rational(j+1, 7) for j in range(10)]
        real_m = mass_matrix(real_v, sign)
        complex_null = mass_matrix([1, I]+[0]*8, sign)
        m = mass_matrix([a+I*c, I*b]+[0]*8, sign)
        H = clean(m.H*m)
        rho = a*a+b*b+c*c
        rows[sign] = dict(
            real_norm_identity=clean(real_m.H*real_m) == sum(x*x for x in real_v)*sp.eye(16),
            complex_null_rank=complex_null.rank(),
            complex_null_mass_squared=complex_null.H*complex_null,
            complex_polynomial=clean((H-rho*sp.eye(16))**2-4*a*a*b*b*sp.eye(16)) == sp.zeros(16),
            complex_trace=sp.expand(sp.trace(H)-16*rho),
            complex_discriminant=sp.expand(rho**2-((a+I*c)**2-b*b)*((a-I*c)**2-b*b)))
    yy = clifford_data()['sectors'][-1]['yukawa'][0]
    # A fixed symmetry-breaking scalar plus a nonzero Dirac mixing.
    free = sp.BlockMatrix([[sp.zeros(16), 2*sp.eye(16)], [2*sp.eye(16), 3*yy]]).as_explicit()
    free_square = clean(free.H*free)
    mu, M, e = sp.symbols('mu M e', real=True)
    small = sp.Matrix([[0, mu], [mu, M]])
    return dict(sectors=rows, fixed_condensate_control=dict(
        symmetric=free.T == free, rank=free.rank(),
        squared_mass_polynomial=clean(free_square**2-17*free_square+16*sp.eye(32)) == sp.zeros(32),
        squared_mass_trace=sp.trace(free_square),
        two_by_two_charpoly=sp.expand((e*sp.eye(2)-small).det()),
        schur_mass=-mu**2/M))


@lru_cache(maxsize=1)
def locking_controls():
    f, kappa, lam, v = sp.symbols('f kappa lambda v', positive=True)
    r = sp.Symbol('r', real=True)
    x, y = sp.symbols('x0:10', real=True), sp.symbols('y0:10', real=True)
    variables = x+y
    x2, y2 = sum(t*t for t in x), sum(t*t for t in y)
    potential = r*(x2+y2)/2+lam*(x2+y2)**2/4-kappa*f*(x2-y2)
    point = {t: 0 for t in variables}
    point[x[0]] = v
    point[r] = 2*kappa*f-lam*v*v
    gradient = [sp.expand(sp.diff(potential, t).subs(point)) for t in variables]
    hessian = sp.hessian(potential, variables).subs(point).applyfunc(sp.expand)
    expected = sp.diag(2*lam*v*v, *([0]*9), *([4*kappa*f]*10))
    # The stabilizer of an ordered real vector is Spin(9), not Spin(10).
    tangent_columns = []
    n = sp.eye(10)[:, 0]
    for a, b in itertools.combinations(range(10), 2):
        K = sp.zeros(10)
        K[a, b], K[b, a] = 1, -1
        tangent_columns.append(K*n)
    broken = sp.Matrix.hstack(*tangent_columns).rank()
    return dict(potential=potential, gradient=gradient, hessian=hessian,
                hessian_matches=hessian == expected,
                negative_radial_parameter=r-2*kappa*f,
                real_target_dimension=10-1, broken_vector_generators=broken,
                unbroken_vector_generators=45-broken)


def real_structure(phi_unit, S):
    phi_unit = sp.sympify(phi_unit)
    if clean(phi_unit*sp.conjugate(phi_unit)) != 1:
        raise ValueError('unit phase of a NONZERO Phi required')
    return clean(phi_unit*sp.conjugate(exact_vector(S)))


@lru_cache(maxsize=1)
def phase_controls():
    phi = (3+4*I)/5
    S = exact_vector([1+I, 2-I]+[0]*8)
    phases = [1, I, (3+4*I)/5]
    return dict(
        involution=real_structure(phi, real_structure(phi, S)) == S,
        H_covariant=all(real_structure(clean(z**4*phi), clean(z**2*S)) == clean(z**2*real_structure(phi, S))
                        for z in phases),
        omitted_Phi_fails=real_structure(1, clean(phases[-1]**2*S)) != clean(phases[-1]**2*real_structure(1, S)),
        c3_Phi_invariant_arcs=[sum((4*j+h) % 3 == 0 for j in range(3)) for h in range(3)],
        c3_charge12_natural_invariant_arcs=sum((12*j) % 3 == 0 for j in range(3)),
        c3_coupling_phase_identities=all((2*h+2*(-h)) % 3 == 0 and (-4*h+2*(2*h)) % 3 == 0
                                       for h in range(3)))


def serial(v):
    if isinstance(v, dict):
        return {str(k): serial(x) for k, x in v.items()}
    if isinstance(v, sp.MatrixBase):
        return serial(v.tolist())
    if isinstance(v, (tuple, list)):
        return [serial(x) for x in v]
    if isinstance(v, sp.Integer):
        return int(v)
    if isinstance(v, sp.Basic):
        return str(v)
    return v


def run():
    start = time.monotonic()
    a, g, m, l, p = algebra_controls(), global_controls(), gap_controls(), locking_controls(), phase_controls()
    checks = dict(
        clifford_and_C=all(a[k] for k in ('hermitian_gamma', 'clifford', 'C_antisymmetric', 'C_unitary',
                                        'charge_conjugation', 'chirality_square', 'chirality_odd', 'yukawa_even')),
        two_full_intertwiners=all(s['dimension'] == 16 and s['symmetric'] and s['real_mass_identity'] and s['ward_all']
                                  and s['ward_equations'] == 450 for s in a['sectors'].values()),
        actual_global_representations=all(g[k] for k in ('cartan_matched', 'psi_matches_positive', 'chi_matches_negative',
            'scalar_vector_weights', 'all_H_weights_integral', 'locking_weight_pairs', 'scalar_charge_two_singlet_rejected')),
        anomaly_scope=g['vectorlike_anomaly'] == g['pure_D5_linear'] == g['pure_D5_cubic'] == 0 and
                      g['full_H_light_anomaly'] != 0 and sp.expand(g['full_H_light_anomaly']+g['full_H_mirror_anomaly']) == 0,
        complex_scalar_not_automatically_gapped=all(s['real_norm_identity'] and s['complex_null_rank'] == 8 and
            s['complex_polynomial'] and s['complex_trace'] == 0 for s in m['sectors'].values()),
        fixed_condensate_not_chiral=m['fixed_condensate_control']['rank'] == 32 and
                                   m['fixed_condensate_control']['squared_mass_polynomial'],
        locking_classical_only=all(t == 0 for t in l['gradient']) and l['hessian_matches'] and
                               (l['broken_vector_generators'], l['unbroken_vector_generators']) == (9, 36),
        charged_real_structure=p['involution'] and p['H_covariant'] and p['omitted_Phi_fails'],
        inherited_C3_cost=p['c3_Phi_invariant_arcs'] == [1, 1, 1] and p['c3_coupling_phase_identities'])
    return serial(dict(checks=checks, all_checks_pass=all(checks.values()), algebra=a, global_group=g,
                       masses=m, locking=l, phases=p, sympy_version=sp.__version__,
                       runtime_seconds=time.monotonic()-start,
                       scope='Exact ADDED interaction algebra and classical controls; quantum SMG, source localization and TOE unproved.'))


if __name__ == '__main__':
    result = run()
    print(json.dumps(result, indent=2, sort_keys=True))
    raise SystemExit(0 if result['all_checks_pass'] else 1)
