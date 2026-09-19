"""R34: Gaussian matching and exact Grassmann, gauge and Lorentz controls.

The four-dimensional fields/action are ADDED inputs. No quantum phase,
localization hierarchy or physical chiral spectrum is calculated here.
"""
from __future__ import annotations

from functools import lru_cache
import importlib.util
import itertools
import json
from pathlib import Path
import time

import sympy as sp


def prior(name, filename):
    spec = importlib.util.spec_from_file_location(name, Path(__file__).with_name(filename))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


mi = prior('r34_mirror_interaction', 'mirror_interaction.py')
cd = prior('r34_charged_domain', 'charged_domain.py')


def clean(form):
    return {key: value for key, coeff in form.items() if (value := sp.expand(coeff)) != 0}


def add(*forms):
    result = {}
    for form in forms:
        for key, coeff in form.items():
            result[key] = result.get(key, 0)+coeff
    return clean(result)


def parity(sequence):
    return (-1)**sum(sequence[i] > sequence[j]
                     for i in range(len(sequence)) for j in range(i+1, len(sequence)))


@lru_cache(maxsize=2)
def bilinears(sign):
    if sign not in (-1, 1):
        raise ValueError('Spin(10) chirality must be +1 or -1')
    # u_A = theta_A, d_A = theta_(16+A); epsilon_ud = +1.
    # Full epsilon contraction = 2 sum Y_AB u_A d_B, since Y is symmetric.
    return tuple({(a, 16+b): 2*Y[a, b] for a in range(16) for b in range(16) if Y[a, b] != 0}
                 for Y in mi.clifford_data()['sectors'][sign]['yukawa'])


@lru_cache(maxsize=2)
def quartic(sign):
    # Reuse the frozen exterior product, not commuting fermion symbols.
    return add(*(cd.wedge(B, B) for B in bilinears(sign)))


def variation(form, generator):
    """Even infinitesimal derivation: delta theta_i = sum_j T_ij theta_j."""
    if generator.shape != (32, 32):
        raise ValueError('32-generator action required')
    rows = {i: [(j, generator[i, j]) for j in range(32) if generator[i, j] != 0]
            for i in range(32)}
    out = {}
    for key, coeff in form.items():
        for position, i in enumerate(key):
            for j, entry in rows[i]:
                sequence = key[:position]+(j,)+key[position+1:]
                if len(set(sequence)) != len(sequence):
                    continue
                target = tuple(sorted(sequence))
                out[target] = out.get(target, 0)+parity(sequence)*coeff*entry
    return clean(out)


def permutation_coefficient(sign, key):
    """Independent full 24-term antisymmetrization of (theta^t A theta)^2."""
    if len(key) != 4 or len(set(key)) != 4:
        raise ValueError('four distinct generator indices required')
    epsilon = sp.Matrix([[0, 1], [-1, 0]])
    total = 0
    for Y in mi.clifford_data()['sectors'][sign]['yukawa']:
        A = sp.kronecker_product(epsilon, Y)
        for order in itertools.permutations(range(4)):
            i, j, k, l = [key[n] for n in order]
            total += parity(order)*A[i, j]*A[k, l]
    return sp.expand(total)


@lru_cache(maxsize=2)
def minor_quartic(sign):
    """Independent full coefficient formula, -8 sum_a det(Y_a[rows,cols])."""
    yy = mi.clifford_data()['sectors'][sign]['yukawa']
    out = {}
    for i, k in itertools.combinations(range(16), 2):
        for j, l in itertools.combinations(range(16), 2):
            coeff = sp.expand(-8*sum(Y[i, j]*Y[k, l]-Y[i, l]*Y[k, j] for Y in yy))
            if coeff != 0:
                out[(i, k, 16+j, 16+l)] = coeff
    return out


@lru_cache(maxsize=2)
def commuting_quartic(sign):
    """Comparator: ONE commuting 16-component spinor, not a Weyl fermion."""
    out = {}
    for Y in mi.clifford_data()['sectors'][sign]['yukawa']:
        B = {}
        for i in range(16):
            for j in range(16):
                if Y[i, j] != 0:
                    key = tuple(sorted((i, j)))
                    B[key] = B.get(key, 0)+Y[i, j]
        for j, c in B.items():
            for k, d in B.items():
                key = tuple(sorted(j+k))
                out[key] = out.get(key, 0)+c*d
    return clean(out)


def lorentz_generators():
    return (sp.BlockMatrix([[sp.zeros(16), sp.eye(16)], [sp.zeros(16), sp.zeros(16)]]).as_explicit(),
            sp.BlockMatrix([[sp.zeros(16), sp.zeros(16)], [sp.eye(16), sp.zeros(16)]]).as_explicit(),
            sp.diag(*([1]*16+[-1]*16)))


@lru_cache(maxsize=2)
def exterior_controls(sign):
    Q = quartic(sign)
    sector = mi.clifford_data()['sectors'][sign]
    wards = [not variation(Q, sp.diag(T, T)) for T in sector['generators'].values()]
    lorentz = [not variation(Q, L) for L in lorentz_generators()]
    # Both a missing vector component and an incorrect fermion sign must be detectable.
    one_component = cd.wedge(bilinears(sign)[0], bilinears(sign)[0])
    mutant_rejected = bool(variation(one_component, sp.diag(sector['generators'][(0, 2)],
                                                         sector['generators'][(0, 2)])))
    witness = min(Q) if Q else None
    return dict(nonzero=bool(Q), monomials=len(Q), all_coefficients_match_minors=Q == minor_quartic(sign),
                witness=dict(indices=witness, coefficient=Q[witness],
                             permutation_coefficient=permutation_coefficient(sign, witness)) if Q else None,
                ward_count=len(wards), ward_all=all(wards), lorentz_all=all(lorentz),
                two_up_two_down=all(sum(i < 16 for i in key) == 2 and len(key) == 4 for key in Q),
                commuting_single_spinor_zero=not commuting_quartic(sign),
                omitted_components_rejected=mutant_rejected)


@lru_cache(maxsize=1)
def gaussian_controls():
    r, k = sp.symbols('r kappa', real=True)
    f = sp.Symbol('f', positive=True)
    P, Pb, J, Jb, S, Sb = sp.symbols('Phi Phi_bar J J_bar S S_bar')
    D = r*r-4*k*k*P*Pb
    potential = r*Sb*S-k*(Pb*S*S+P*Sb*Sb)+S*J+Sb*Jb
    stationary = {S: -(r*Jb+2*k*P*J)/D, Sb: -(r*J+2*k*Pb*Jb)/D}
    effective = -(r*J*Jb+k*P*J*J+k*Pb*Jb*Jb)/D
    residuals = [sp.cancel(sp.diff(potential, v).subs(stationary)) for v in (S, Sb)]
    matched = sp.cancel(potential.subs(stationary)-effective) == 0
    N = sp.Matrix([[r, -2*k*P], [-2*k*Pb, r]])
    real_hessian = sp.diag(*([r-2*k*f]*10+[r+2*k*f]*10))
    a, b, c, d = sp.symbols('B_m B_m_bar B_p B_p_bar')
    ym, ymb, yp, ypb = sp.symbols('y_m y_m_bar y_p y_p_bar')
    numerator = sp.expand(-D*effective.subs({J: ym*a+ypb*d, Jb: ymb*b+yp*c}))
    coeffs = sp.Poly(numerator, a, b, c, d).terms()
    charges = {a: -2, b: 2, c: 2, d: -2, P: 4, Pb: -4}
    weighted = sp.expand(sum(q*v*sp.diff(effective.subs({J: ym*a+ypb*d, Jb: ymb*b+yp*c}), v)
                             for v, q in charges.items()))
    # Test both a generic complex background and the null/stability controls.
    wrong = -(r*J*Jb+k*Pb*J*J+k*P*Jb*Jb)/D
    return dict(symbols=dict(r=r, kappa=k, Phi=P, Phi_bar=Pb, J=J, J_bar=Jb, f=f,
                             B_m=a, B_m_bar=b, B_p=c, B_p_bar=d, y_m=ym, y_m_bar=ymb,
                             y_p=yp, y_p_bar=ypb),
                determinant=D, effective=effective, numerator=numerator,
                stationary_residuals=residuals, stationary_value_matches=matched,
                inverse_matches=(N*N.adjugate()-D*sp.eye(2)) == sp.zeros(2),
                hessian_determinant_matches=sp.expand(real_hessian.det()-(r*r-4*k*k*f*f)**10) == 0,
                gaussian_log_coefficient=sp.Rational(10, 2),
                monomials=[dict(powers=powers, coefficient=sp.factor(coeff)) for powers, coeff in coeffs],
                full_H_charge_residual=sp.cancel(weighted),
                wrong_Phi_conjugation_rejected=sp.cancel(wrong-effective) != 0,
                stable_control_eigenvalues=[(r-2*k*f).subs({r: 3, k: 1, f: 1}),
                                            (r+2*k*f).subs({r: 3, k: 1, f: 1})],
                unstable_control_eigenvalues=[(r-2*k*f).subs({r: 1, k: 1, f: 1}),
                                              (r+2*k*f).subs({r: 1, k: 1, f: 1})],
                singular_control=D.subs({r: 2, k: 1, P: 1, Pb: 1}))


@lru_cache(maxsize=1)
def phase_controls():
    # Columns psi, chi, S, Phi; rows ym, yp, mu, kappa.
    matrix = sp.Matrix([[0, 2, 1, 0], [2, 0, -1, 0], [1, 1, 0, 0], [0, 0, 2, -1]])
    gauge = sp.Matrix([1, -1, 2, 4])
    return dict(matrix=matrix, rank=matrix.rank(), kernel=matrix.nullspace(),
                gauge_phase_annihilated=matrix*gauge == sp.zeros(4, 1),
                without_ordinary_yukawa_rank=matrix.extract([0, 2, 3], range(4)).rank(),
                without_locking_rank=matrix.extract([0, 1, 2], range(4)).rank(),
                without_ordinary_and_mixing_rank=matrix.extract([0, 3], range(4)).rank(),
                bare_mirror_quartic_charge=-4, Phi_completed_quartic_charge=-4+4,
                mirror_phase_degree=4, bilinear_dimension=3, quartic_dimension=6,
                Phi_quartic_dimension=7, conserving_coefficient_dimension=2-4,
                breaking_coefficient_dimension=1-4)


def run():
    start = time.monotonic()
    rows = {sign: exterior_controls(sign) for sign in (1, -1)}
    gaussian, phases = gaussian_controls(), phase_controls()
    checks = dict(
        nonzero_Grassmann_both=all(row['nonzero'] for row in rows.values()),
        independent_coefficients=all(row['all_coefficients_match_minors'] and
                                     row['witness']['coefficient'] == row['witness']['permutation_coefficient']
                                     for row in rows.values()),
        gauge_and_Lorentz=all(row['ward_count'] == 45 and row['ward_all'] and row['lorentz_all'] and
                             row['two_up_two_down'] for row in rows.values()),
        fermion_and_omission_controls=all(row['commuting_single_spinor_zero'] and
                                        row['omitted_components_rejected'] for row in rows.values()),
        Gaussian_matching=gaussian['stationary_residuals'] == [0, 0] and
                          gaussian['stationary_value_matches'] and gaussian['inverse_matches'],
        all_allowed_channels=len(gaussian['monomials']) == 10 and gaussian['full_H_charge_residual'] == 0 and
                             gaussian['wrong_Phi_conjugation_rejected'],
        stable_and_unstable=gaussian['stable_control_eigenvalues'] == [1, 5] and
                            gaussian['unstable_control_eigenvalues'] == [-1, 3] and gaussian['singular_control'] == 0,
        measure_retained=gaussian['hessian_determinant_matches'] and gaussian['gaussian_log_coefficient'] == 5,
        continuous_phase_accounting=phases['rank'] == 3 and phases['gauge_phase_annihilated'] and
                                    phases['without_ordinary_yukawa_rank'] == 3 and
                                    phases['without_locking_rank'] == 2 and
                                    phases['without_ordinary_and_mixing_rank'] == 2)
    out = dict(scope='Exact auxiliary Gaussian matching and local algebra; not a quantum mass gap or chirality.',
               checks=checks, all_checks_pass=all(checks.values()), exterior=rows,
               gaussian=gaussian, phases=phases, elapsed_seconds=time.monotonic()-start)
    print(json.dumps(mi.serial(out), indent=2))
    return 0 if out['all_checks_pass'] else 1


if __name__ == '__main__':
    raise SystemExit(run())
