"""R23: local mass/Clifford map, normalized transport, retained boundaries.

Not a full singular determinant, boundary completion or physical vacuum.
Analytic scope and prior conventions are in MASS_INFLOW_DESIGN.md.
"""
from __future__ import annotations

from functools import lru_cache
import importlib.util
import itertools
import json
import math
from pathlib import Path
import time

import sympy as sp
from scipy.integrate import quad


def local(name, filename):
    spec = importlib.util.spec_from_file_location(name, Path(__file__).with_name(filename))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


prior = local('r23_prior', 'geometric_completion.py')
cd, ac = prior.cd, prior.ac
I = sp.I
PAULI = (sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -I], [I, 0]]), sp.diag(1, -1))
EVEN = [j for j, b in enumerate(cd.BASIS) if len(b) % 2 == 0]


def simp(matrix):
    return matrix.applyfunc(lambda x: sp.simplify(sp.expand_complex(x)))


@lru_cache(maxsize=1)
def form_matrices():
    creation = []
    for i in range(3):
        e = sp.zeros(8)
        for col, basis in enumerate(cd.BASIS):
            for target, value in cd.wedge({(i,): 1}, {basis: 1}).items():
                e[cd.BASIS.index(target), col] = value
        creation.append(e)
    annihilation = [e.T for e in creation]
    c = [e-a for e, a in zip(creation, annihilation)]
    h = [e+a for e, a in zip(creation, annihilation)]
    return creation, annihilation, c, h


@lru_cache(maxsize=1)
def clifford_map():
    creation, annihilation, c, h = form_matrices()
    J = c[0]*c[1]*c[2]
    parity = sp.diag(*[(-1)**len(b) for b in cd.BASIS])
    G = [(I*J*x).extract(EVEN, EVEN) for x in c]
    T = [(I*J*x).extract(EVEN, EVEN) for x in h]
    projector = (sp.eye(4)-G[2])*(sp.eye(4)+T[2])/4
    seed = next(projector[:, j] for j in range(4) if projector[:, j] != sp.zeros(4, 1))
    seed = seed/sp.sqrt((seed.H*seed)[0])
    U = sp.Matrix.hstack(seed, T[0]*seed, -G[0]*seed, -G[0]*T[0]*seed)
    rotation_matches = []
    rotation_actions = []
    for i, j in itertools.combinations(range(3), 2):
        natural = (-I*(creation[i]*annihilation[j]-creation[j]*annihilation[i])).extract(EVEN, EVEN)
        spin = -I*(G[i]*G[j]+T[i]*T[j])/2
        rotation_matches.append(natural == spin)
        for k in range(3):
            for triple in (G, T):
                expected = I*((int(k == i))*triple[j]-int(k == j)*triple[i])
                rotation_actions.append(spin*triple[k]-triple[k]*spin == expected)
    return dict(J=J, parity=parity, G=G, T=T, U=U,
                J_unitary=J.H*J == sp.eye(8), J_odd=J*parity == -parity*J,
                pair_anticommutators=all(c[i]*h[j]+h[j]*c[i] == sp.zeros(8)
                                         for i in range(3) for j in range(3)),
                G_product=G[0]*G[1]*G[2], T_product=T[0]*T[1]*T[2],
                hermitian=all(x.H == x for x in G+T),
                clifford=all(triple[i]*triple[j]+triple[j]*triple[i] == 2*int(i == j)*sp.eye(4)
                             for triple in (G, T) for i in range(3) for j in range(3)),
                commuting=all(g*t == t*g for g in G for t in T),
                seed_rank=projector.rank(), unitary=U.H*U == sp.eye(4),
                kinetic_map=[simp(U.H*G[i]*U) for i in range(3)],
                mass_map=[simp(U.H*T[i]*U) for i in range(3)],
                rotation_matches=rotation_matches, rotation_actions=rotation_actions)


@lru_cache(maxsize=1)
def actual_symbol():
    p = sp.symbols('p0:3', real=True)
    m = sp.symbols('m0:3', real=True)
    phase = sp.exp(sum(a*x for a, x in zip(p, cd.COORDS)))
    metric = cd.MetricForms((1, 1, 1))
    original = sp.zeros(8)
    for col, b in enumerate(cd.BASIS):
        output = metric.D({b: phase}, {(i,): m[i] for i in range(3)})
        for target, value in output.items():
            original[cd.BASIS.index(target), col] = sp.simplify(value/phase)
    _, _, c, h = form_matrices()
    expected = sum((p[i]*c[i]+m[i]*h[i] for i in range(3)), sp.zeros(8))
    wrong = sum((p[i]*h[i]+m[i]*h[i] for i in range(3)), sp.zeros(8))
    return dict(original=original, symbol_matches=original == expected,
                wrong_codifferential_rejected=original != wrong)


def morse_control(eigenvalues):
    lam = tuple(map(sp.sympify, eigenvalues))
    if len(lam) != 3 or any(not x.is_real or x == 0 or not x.is_number for x in lam):
        raise ValueError('three nonzero real exact eigenvalues required')
    if any(x.has(sp.Float) for x in lam):
        raise ValueError('exact eigenvalues required')
    basis = tuple(i for i, x in enumerate(lam) if x < 0)
    gaussian = sp.exp(-sum(abs(lam[i])*cd.COORDS[i]**2 for i in range(3))/2)
    metric = cd.MetricForms((1, 1, 1))
    residual = metric.D({basis: gaussian}, {(i,): lam[i]*cd.COORDS[i] for i in range(3)})
    energies = [sum(abs(lam[i])+lam[i]*(2*int(i in b)-1) for i in range(3)) for b in cd.BASIS]
    return dict(eigenvalues=lam, degree=len(basis), basis=basis,
                operator_residual=residual, ground_energies=energies,
                zero_basis=[b for b, e in zip(cd.BASIS, energies) if e == 0],
                norm_squared=sp.pi**sp.Rational(3, 2)/sp.sqrt(abs(sp.prod(lam))),
                euler_sign=(-1)**len(basis), left_minus_right=-(-1)**len(basis),
                determinant_sign=sp.sign(sp.prod(lam)))


def pfaffian(A):
    if A.rows != A.cols or A.rows % 2 or A != -A.T:
        raise ValueError('even antisymmetric matrix required')
    if A.rows == 0:
        return sp.Integer(1)
    return sp.expand(sum((-1)**(j+1)*A[0, j]*pfaffian(A.extract(
        [k for k in range(1, A.rows) if k != j], [k for k in range(1, A.rows) if k != j]))
        for j in range(1, A.rows)))


def reality_control():
    matrices = [sp.Matrix(2, 2, sp.symbols('d0:4')),
                sp.Matrix([[2, 1, -1], [3, 4, 2], [1, -2, 3]])]
    rows = []
    for D in matrices:
        n = D.rows
        skew = sp.BlockMatrix([[sp.zeros(n), D], [-D.T, sp.zeros(n)]]).as_explicit()
        sign = (-1)**(n*(n-1)//2)
        normalized = sign*pfaffian(skew)
        rows.append(dict(n=n, determinant=D.det(), normalized_pfaffian=normalized,
                         identity=sp.expand(normalized-D.det()) == 0,
                         double_count_rejected=sp.expand(normalized-D.det()**2) != 0,
                         extra_square_root_rejected=sp.expand(normalized**2-D.det()) != 0))
    return dict(blocks=rows, real_components_per_real_adjoint_generator=16,
                real_components_per_charged_pair=32, complex_components_in_one_representative=16,
                seven_dimensional_Dirac_size=8, independent_Dirac_flavours=2)


@lru_cache(maxsize=1)
def angular_form():
    theta, phi = sp.symbols('theta phi', real=True)
    n = sp.Matrix([sp.sin(theta)*sp.cos(phi), sp.sin(theta)*sp.sin(phi), sp.cos(theta)])
    P = (sp.eye(2)+sum((n[i]*PAULI[i] for i in range(3)), sp.zeros(2)))/2
    def curvature(projector, connection_theta, connection_phi):
        dp_t = projector.diff(theta)+connection_theta*projector-projector*connection_theta
        dp_p = projector.diff(phi)+connection_phi*projector-projector*connection_phi
        F = connection_phi.diff(theta)-connection_theta.diff(phi)+connection_theta*connection_phi-connection_phi*connection_theta
        value = I*sp.trace(projector*F+projector*(dp_t*dp_p-dp_p*dp_t))/(2*sp.pi)
        return sp.simplify(sp.expand_complex(value))
    zero = sp.zeros(2)
    K = curvature(P, zero, zero)
    U = sp.diag(sp.exp(I*phi), sp.exp(-I*phi))
    rotated = U*P*U.H
    connection = -U.diff(phi)*U.H
    covariant = curvature(rotated, zero, connection)
    omitted = curvature(rotated, zero, zero)
    constant_curved = curvature(sp.diag(1, 0), zero, I*theta*PAULI[2])
    return dict(projector=simp(P), projector_identity=simp(P*P-P) == zero,
                K_theta_phi=K, sphere_flux=sp.integrate(K, (theta, 0, sp.pi), (phi, 0, 2*sp.pi)),
                reversed=curvature(sp.eye(2)-P, zero, zero),
                frame_covariant=covariant, omitted_connection=omitted,
                constant_projector_curved=constant_curved)


def permutation_sign(p):
    return (-1)**sum(p[i] > p[j] for i in range(len(p)) for j in range(i+1, len(p)))


@lru_cache(maxsize=1)
def superconnection_form():
    cubic = sum((permutation_sign(p)*PAULI[p[0]]*PAULI[p[1]]*PAULI[p[2]]
                 for p in itertools.permutations(range(3))), sp.zeros(2))
    # sigma_aux anticommutes with the one-forms: (i*dT*sigma_aux)^3 = i*(dT)^3*sigma_aux.
    coefficient = sp.simplify(sp.sqrt(2)/(2*sp.pi)**sp.Rational(3, 2)*I*sp.trace(cubic)/6)
    r = sp.Symbol('radius', positive=True)
    cutoff = sp.erf(r)-2*r*sp.exp(-r*r)/sp.sqrt(sp.pi)
    radial_density = -4*r*r*sp.exp(-r*r)/sp.sqrt(sp.pi)
    return dict(cubic_trace=sp.trace(cubic), normalized_coefficient=coefficient,
                gaussian_integral=sp.simplify(coefficient*sp.sqrt(sp.pi)**3),
                cutoff=cutoff, primitive_derivative=sp.simplify(-sp.diff(cutoff, r)-radial_density),
                zero_limit=sp.limit(cutoff, r, 0, dir='+'), infinity_limit=sp.limit(cutoff, r, sp.oo),
                radial_integral=sp.integrate(radial_density, (r, 0, sp.oo)),
                wrong_ungraded_sign=-coefficient)


def linear_flux(A):
    A = sp.Matrix(A)
    if A.shape != (3, 3) or not A.det() or any(not x.is_real for x in A):
        raise ValueError('invertible real 3 by 3 linear mass map required')
    entries = [[float(A[i, j]) for j in range(3)] for i in range(3)]
    determinant = float(A.det())
    def theta_integrand(theta):
        def phi_integrand(phi):
            v = (math.sin(theta)*math.cos(phi), math.sin(theta)*math.sin(phi), math.cos(theta))
            length_squared = sum(sum(row[j]*v[j] for j in range(3))**2 for row in entries)
            return -determinant*math.sin(theta)/(4*math.pi*length_squared**1.5)
        return quad(phi_integrand, 0, 2*math.pi, epsabs=1e-10, epsrel=1e-10)[0]
    value, error = quad(theta_integrand, 0, math.pi, epsabs=1e-10, epsrel=1e-10)
    return dict(matrix=A, flux=value, outer_quad_error=error, expected=-int(sp.sign(A.det())),
                numerical_only=True)


def response_eigenvalues(sign1, sign2, reference=1):
    if any(s not in (-1, 1) for s in (sign1, sign2, reference)):
        raise ValueError('nonzero signed mass sectors required')
    return dict(angular=sp.Rational(sign1-sign2, 2),
                regulator=sp.Rational(sign1+sign2-2*reference, 2))


def anomaly_forms():
    spinor = ac.data()['spinor']
    ell = [(w.T*ac.Z)[0] for w in spinor]
    p2 = sp.Symbol('p2_T')
    I8 = sp.expand(sum(x**4 for x in ell)/24-ac.P1*sum(x*x for x in ell)/48
                   +len(ell)*(7*ac.P1**2-4*p2)/5760)
    return dict(one_I6=ac.anomaly(spinor), three_I6=ac.anomaly(spinor, 3), I8=I8,
                one_linear_trace=sum(w[0] for w in spinor), one_cubic_trace=sum(w[0]**3 for w in spinor),
                conjugate_I6=ac.anomaly([-w for w in spinor]))


def exterior(form, coords):
    return cd.add(*(cd.wedge({(i,): sp.diff(value, x)}, {basis: 1})
                    for basis, value in form.items() for i, x in enumerate(coords)))


def descent_sign():
    coords = sp.symbols('r theta phi x0:4', real=True)
    r = coords[0]
    k, ell = sp.Function('k')(r), sp.Function('ell')(r)
    K = {(1, 2): k}
    I4 = {(3, 4, 5, 6): ell}
    product_d = exterior(cd.wedge(K, I4), coords)
    localized = cd.wedge(exterior(K, coords), I4)
    bulk = cd.wedge(K, exterior(I4, coords))
    return dict(product_derivative=product_d, dK_I4=localized, K_dI4=bulk,
                correct=cd.add(product_d, cd.scale(localized, -1), cd.scale(bulk, -1)) == {},
                wrong_sign_rejected=cd.add(product_d, localized, cd.scale(bulk, -1)) != {})


def boundary_balance(charges, local_parameters, end_parameter):
    if len(charges) != len(local_parameters) or any(not isinstance(q, int) for q in charges):
        raise ValueError('integral local charges and one parameter per charge required')
    local_part = sum(q*a for q, a in zip(charges, local_parameters))
    # Explicit Stokes hypothesis: the same K accounts for these local charges and all outer ends.
    flux = sum(charges)
    outer = flux*end_parameter
    bulk = outer-local_part
    return dict(local=local_part, outer=outer, bulk=bulk, total=local_part+bulk,
                end_flux_if_all_charges_are_accounted=flux,
                fake_total_after_dropping_outer=local_part-local_part)


def betti(dimensions, differentials):
    for j, d in enumerate(differentials):
        if d.shape != (dimensions[j+1], dimensions[j]):
            raise ValueError('wrong differential shape')
    if any(differentials[j+1]*differentials[j] != sp.zeros(dimensions[j+2], dimensions[j])
           for j in range(len(differentials)-1)):
        raise ValueError('not a cochain complex')
    ranks = [0]+[d.rank() for d in differentials]+[0]
    return tuple(dimensions[j]-ranks[j]-ranks[j+1] for j in range(len(dimensions)))


def partition_control(z, discs=1):
    z = sp.sympify(z)
    if z == 0 or not isinstance(discs, int) or discs < 1:
        raise ValueError('nonzero character and positive disc count required')
    v = z-1
    torus = betti((1, 2, 1), [sp.Matrix([v, 0]), sp.Matrix([[0, v]])])
    solid = betti((1, 1, 0, 0), [sp.Matrix([[v]]), sp.zeros(0, 1), sp.zeros(0, 0)])
    d0 = sp.Matrix([v]+[1]*discs)
    relative = betti((1, 1+discs, 0, 0), [d0, sp.zeros(0, 1+discs), sp.zeros(0, 0)])
    annulus = betti((1, 2, 1, 0), [sp.Matrix([v, 1]), sp.Matrix([[1, -v]]), sp.zeros(0, 1)])
    return dict(character=z, discs=discs, whole_torus=torus, solid_torus=solid,
                disc_relative=relative, relative_euler=sum((-1)**j*b for j, b in enumerate(relative)),
                essential_annulus_relative=annulus)


def serial(value):
    if isinstance(value, sp.MatrixBase):
        return [[serial(v) for v in row] for row in value.tolist()]
    if isinstance(value, sp.Basic):
        return str(value)
    if isinstance(value, dict):
        return {str(k): serial(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [serial(v) for v in value]
    return value


def main():
    start = time.monotonic()
    c = clifford_map()
    result = dict(scope='local Clifford/normalized mass descent and conditional boundary accounting, not global completion',
                  clifford=c, original_symbol=actual_symbol(),
                  morse=[morse_control(tuple((i+1)*s for i, s in enumerate(signs)))
                         for signs in itertools.product((-1, 1), repeat=3)]
                        +[morse_control((-2, 1, 1)), morse_control((2, -1, -1))],
                  reality=reality_control(), angular=angular_form(), superconnection=superconnection_form(),
                  flux_controls=[linear_flux(A) for A in (sp.diag(1, 2, 3), sp.diag(-2, 1, 1),
                                                          sp.diag(2, -1, -1), sp.Matrix([[1, 1, 0], [0, 2, 1], [0, 0, 3]]))],
                  mass_sign_controls=[response_eigenvalues(a, b) for a, b in itertools.product((-1, 1), repeat=2)],
                  anomaly=anomaly_forms(), descent=descent_sign(),
                  constant_zero_mode=boundary_balance([1, 1, 1], [1, 1, 1], 1),
                  compact_support=boundary_balance([1, 1, 1], [1, 1, 1], 0),
                  zero_total_control=boundary_balance([1, -1], [1, 1], 1),
                  partitions=[partition_control(z, k) for z in (I, prior.ZETA, 1) for k in (1, 2, 3)])
    result['seconds'] = time.monotonic()-start
    print(json.dumps(serial(result), indent=2))


if __name__ == '__main__':
    main()
