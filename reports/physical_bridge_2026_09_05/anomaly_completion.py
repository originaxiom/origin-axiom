"""R21: exact subgroup anomaly completion and unchanged-holonomy controls.

This tests the specified added-field model, not a geometric derivation,
UV completion, universal chirality obstruction or physical TOE.
"""
from __future__ import annotations

from collections import Counter
from functools import lru_cache
import importlib.util
import itertools
import json
import math
from pathlib import Path
import time

import sympy as sp

SPEC = importlib.util.spec_from_file_location(
    'r21_prior_holonomy', Path(__file__).with_name('holonomy_spectrum.py'))
hs = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(hs)
Z = sp.Matrix(sp.symbols('z0:6'))
P1 = sp.Symbol('p1_T')


def integral(M):
    return all(v.is_Integer for v in M)


def tuples(weights):
    return {tuple(w) for w in weights}


@lru_cache(maxsize=2)
def data(arm_swap=True):
    C = hs.e6_cartan()
    Ci = C.inv()
    u = Ci[:, 0]
    c_row = sp.Rational(3, 4)*sp.eye(6)[0, :]
    projection = sp.eye(6)-u*c_row
    O = sp.eye(6)
    if arm_swap:
        O.row_swap(1, 2)
    F = O*projection+3*u*c_row
    roots = [sp.Matrix(r) for r in hs.weyl_orbit(C, sp.eye(6)[:, 0])]
    old27 = [sp.Matrix(w) for w in hs.weyl_orbit(C, u)]
    pullback = [Ci*F.T*C*w for w in old27]
    spinor = [w for w in roots if w[0] == 1]
    return dict(C=C, Ci=Ci, u=u, c_row=c_row, F=F,
                cocharacter_map=F*Ci, roots=roots, old27=old27,
                pullback=pullback, spinor=spinor,
                vector=[w for w in pullback if w[0] == -2],
                singlet=[w for w in pullback if w[0] == 4])


def anomaly(weights, copies=1):
    if not isinstance(copies, int):
        raise ValueError('integral signed multiplicity required')
    ell = [(w.T*Z)[0] for w in weights]
    return sp.expand(copies*(sum(a**3 for a in ell)/6-P1*sum(ell)/24))


def singlet_weight(q):
    q = sp.sympify(q)
    if q.has(sp.Float):
        raise ValueError('exact charge required')
    return sp.Rational(3, 4)*q*data()['u']


def lattice_controls():
    d = data()
    C, Ci, u, F = (d[k] for k in ('C', 'Ci', 'u', 'F'))
    cols = C[:, 1:]
    minors = [cols.extract(rows, range(5)).det()
              for rows in itertools.combinations(range(6), 5)]
    trow = 3*Ci[0, :]
    d5roots = [r for r in d['roots'] if r[0] == 0]
    mapped_d5 = [F*r for r in d5roots]
    pulled_spinor = [w for w in d['pullback'] if w[0] == 1]
    old_plus = [w for w in d['old27'] if w[0] == sp.Rational(1, 3)]
    return dict(cartan=C, direction=u, singlet_character_row=trow,
                character_gcd=sp.igcd(*list(trow)),
                d5_coroot_maximal_minors=minors,
                d5_coroot_saturation_index=sp.igcd(*minors),
                F=F, cocharacter_map=d['cocharacter_map'],
                map_integral=integral(d['cocharacter_map']),
                map_determinant=d['cocharacter_map'].det(),
                inverse_integral=integral(d['cocharacter_map'].inv()),
                direction_tripled=F*u == 3*u,
                d5_root_count=len(d5roots), d5_roots_preserved=tuples(mapped_d5) == tuples(d5roots),
                d5_metric_preserved=(F.T*C*F-C)[1:, 1:] == sp.zeros(5),
                pullback_integral=all(integral(w) for w in d['pullback']),
                pullback_charge_dimensions=dict(sorted(Counter(w[0] for w in d['pullback']).items())),
                actual_positive_spinor=tuples(pulled_spinor) == tuples(d['spinor']),
                original_27_spinor_not_same=tuples(old_plus) != tuples(d['spinor']),
                no_swap_integral=integral(data(False)['cocharacter_map']),
                no_swap_same_spinor=tuples(w for w in data(False)['pullback'] if w[0] == 1) == tuples(d['spinor']),
                singlet_charges={str(q): integral(singlet_weight(q)) for q in range(-4, 13)},
                scalar_weight_4=singlet_weight(4),
                scalar_from_cube=singlet_weight(4) == 3*u)


def quadratic_level(B):
    """Least integer k with k*z^t B*z/2 integral for every integral z.

    Coefficients on z_i^2 and z_i*z_j prove the all-lattice statement;
    no finite-grid inference. B must be exact symmetric rational.
    """
    if B != B.T or any(not v.is_Rational for v in B):
        raise ValueError('exact symmetric rational bilinear form required')
    coefficients = [B[i, i]/2 for i in range(B.rows)]
    coefficients += [B[i, j] for i in range(B.rows) for j in range(i+1, B.cols)]
    return int(sp.ilcm(*[v.q for v in coefficients]))


@lru_cache(maxsize=1)
def anomaly_controls():
    d = data()
    C, Ci, F = (d[k] for k in ('C', 'Ci', 'F'))
    lam = Ci*Z
    t = (3*Ci[0, :]*Z)[0]
    Q = sp.expand((lam.T*C*lam)[0]/2)
    Qprime = sp.expand(((F*lam).T*C*(F*lam))[0]/2)
    X4 = 3*Q-P1/2
    actual = anomaly(d['spinor'], 3)
    completed = d['spinor']+d['vector']+d['singlet']
    c = sp.Symbol('c')
    v = sp.symbols('v1:6')
    spin_ell = [c+sum(s*x for s, x in zip(signs, v))/2
                for signs in itertools.product((-1, 1), repeat=5)
                if signs.count(-1) % 2 == 0]
    ortho = sp.expand(sum(a**3 for a in spin_ell)/6-P1*sum(spin_ell)/24)
    expected_ortho = sp.Rational(8, 3)*c**3+2*c*sum(x*x for x in v)-sp.Rational(2, 3)*c*P1
    levels = {str(k): quadratic_level(k*Ci) == 1 for k in (1, 2, 3, 6)}
    # S2 x S2 is spin and p1=0. Equal cocharacter fluxes on both factors
    # pair to Ci[i,i]; this witnesses nonintegrality of a proposed level.
    flux_pair = Ci[0, 0]
    return dict(character=t, Q=Q, pullback_Q=Qprime, X4=sp.expand(X4),
                spinor_I6=actual, factorization=sp.expand(actual-t*X4) == 0,
                integral_class_pullback_identity=sp.expand(3*Q-3*Qprime+t*t) == 0,
                orthonormal_spinor_count=len(spin_ell), independent_D5_identity=sp.expand(ortho-expected_ortho) == 0,
                direct_pulled_27_anomaly=anomaly(d['pullback']),
                completed_anomalies={str(n): anomaly(completed, n) for n in (1, 2, 3, 9)},
                spectator_anomaly=anomaly(d['vector']+d['singlet'], 3),
                vectorlike_anomaly=anomaly(d['spinor']+[-w for w in d['spinor']]),
                missing_singlet_nonzero=anomaly(d['spinor']+d['vector']) != 0,
                wrong_counterterm_nonzero=sp.expand(actual-t*(Q-P1/2)) != 0,
                general_copy_identity=all(sp.expand(anomaly(d['spinor'], n)-sp.Rational(n, 3)*t*X4) == 0 for n in (1, 2, 3, 9)),
                minimum_quadratic_level=quadratic_level(Ci), levels=levels,
                spin_S2xS2_Q=flux_pair, spin_S2xS2_X4=3*flux_pair,
                one_copy_formal_X4=flux_pair,
                two_copy_formal_X4=2*flux_pair)


def mass_controls():
    d = data()
    scalar = singlet_weight(4)
    def d5_part(w):
        return w-sp.Rational(3, 4)*w[0]*d['u']
    vector_d5 = tuples(d5_part(w) for w in d['vector'])
    f, rho, g, lam, yv, yn, M = sp.symbols('f rho g lambda yV yN M', positive=True)
    V = lam*(((f+rho)**2-f*f)/2)**2
    return dict(vector_dimension=len(d['vector']), singlet_dimension=len(d['singlet']),
                vector_D5_weights_self_dual=vector_d5 == {tuple(-x for x in w) for w in vector_d5},
                vector_mass_weight_cancellation=all(any(w+w2+scalar == sp.zeros(6, 1) for w2 in d['vector']) for w in d['vector']),
                singlet_mass_weight_cancellation=all(2*w-2*scalar == sp.zeros(6, 1) for w in d['singlet']),
                wrong_mass_charge=4+2*4,
                radial_stationary=sp.diff(V, rho).subs(rho, 0),
                radial_mass_squared=sp.diff(V, rho, 2).subs(rho, 0),
                gauge_mass_squared=16*g*g*f*f,
                vector_mass=yv*f/sp.sqrt(2), singlet_mass=yn*f*f/(2*M),
                spectator_components_for_three=3*(len(d['vector'])+len(d['singlet'])),
                charge12_vector_mass_exponent=sp.Rational(4, 12),
                charge12_singlet_mass_exponent=sp.Rational(-8, 12))


@lru_cache(maxsize=3)
def eta3(q):
    """1808.00009 (4.4), L^3(3), with sqrt(lambda)=lambda^2."""
    zeta = (-1+sp.I*sp.sqrt(3))/2
    total = sum((zeta**(j*(q % 3))-1)*(zeta**(2*j)/(zeta**j-1))**3 for j in (1, 2))/3
    return sp.simplify(sp.expand_complex(total))


def fractional(x):
    return x-sp.floor(x)


def holonomy_controls():
    zeta = (-1+sp.I*sp.sqrt(3))/2
    rows = []
    for q in (0, 1, -2, 4, 8, 12):
        phases = [sp.simplify(sp.expand_complex(zeta**q)),
                  sp.simplify(sp.expand_complex(zeta**(-q)))]
        d0 = sp.Matrix([x-1 for x in phases])
        rows.append(dict(charge=q, phases=phases, parallel_h0=1-int(d0.rank()),
                         singlet_allowed=integral(singlet_weight(q))))
    s = singlet_weight(4)
    u = data()['u']
    C = data()['C']
    return dict(rows=rows, coprime=math.gcd(4, 3),
                smallest_parallel_singlet_charge=sp.ilcm(4, 3),
                residual_Z3_order=3,
                residual_generator_character=sp.simplify((s.T*C*(u/3))[0]),
                eta_single_charge={str(q): eta3(q) for q in (0, 1, 2)},
                eta_spinor_copies={str(n): fractional(16*n*eta3(1)) for n in (1, 2, 3, 9)},
                eta_three_spinors_inverse=fractional(48*eta3(2)),
                independent_net_charge_mod9=48 % 9,
                vectorlike_eta=fractional(eta3(1)+eta3(2)),
                completed_eta={str(n): fractional(n*(16*eta3(1)+10*eta3(-2)+eta3(4))) for n in (1, 2, 3, 9)},
                h0_scalar_nontrivial=rows[3]['parallel_h0'],
                object_derives_added_fields=False, geometric_completion=False,
                three_generations_forced_by_axion=False)


def serial(v):
    if isinstance(v, dict):
        return {str(k): serial(x) for k, x in v.items()}
    if isinstance(v, sp.MatrixBase):
        return [[serial(x) for x in row] for row in v.tolist()]
    if isinstance(v, (tuple, list)):
        return [serial(x) for x in v]
    if isinstance(v, sp.Integer):
        return int(v)
    if isinstance(v, sp.Basic):
        return str(v)
    return v


def run():
    start = time.monotonic()
    result = dict(lattice=lattice_controls(), anomaly=anomaly_controls(),
                  masses=mass_controls(), holonomy=holonomy_controls(),
                  sympy_version=sp.__version__)
    result['runtime_seconds'] = time.monotonic()-start
    return serial(result)


if __name__ == '__main__':
    print(json.dumps(run(), indent=2, sort_keys=True))
