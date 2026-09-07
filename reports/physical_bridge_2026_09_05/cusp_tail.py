"""R17: exact warped-cusp charged operator and uniform tail form bound.

No complete H1 count, global domain selection or physical TOE is asserted.
All science is printed; this module does not write files.
"""
from __future__ import annotations

from functools import lru_cache
from itertools import combinations
import importlib.util
import json
import math
from pathlib import Path
import sys
import time

import mpmath as mp
import numpy as np
import sympy as sp
from numpy.polynomial.legendre import leggauss

x, y, s = sp.symbols("x y s", real=True)
kx, ky, ks, ux, uy, g = sp.symbols("kx ky ks ux uy g", real=True)
TANGENT = ((), (0,), (1,), (0, 1))
N = sp.diag(0, 1, 1, 2)
ZERO = (0, 0, 0)
EYE = sp.eye(4)


def load_local(name, filename):
    spec = importlib.util.spec_from_file_location(name, Path(__file__).with_name(filename))
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def simplified(matrix):
    return matrix.applyfunc(lambda v: sp.factor(sp.simplify(sp.expand(v))))


def wedge_matrix(i, n=2):
    basis = tuple(j for degree in range(n+1) for j in combinations(range(n), degree))
    out = sp.zeros(len(basis))
    for col, j in enumerate(basis):
        if i not in j:
            target = tuple(sorted((i,)+j))
            out[basis.index(target), col] = (-1)**sum(k < i for k in j)
    return out


EPS = (wedge_matrix(0), wedge_matrix(1))
IOTA = tuple(e.T for e in EPS)


def transverse_symbol():
    d = EPS[0]*(kx+ux)+EPS[1]*(ky+uy)
    delta = IOTA[0]*(-kx+ux)+IOTA[1]*(-ky+uy)
    return d, delta


@lru_cache(maxsize=1)
def metric_derivation():
    # An isolated module instance reuses the banked exterior/Hodge algorithm;
    # only its coordinate tuple is rebound in memory, not its source.
    forms = load_local("r17_private_metric", "charged_domain.py")
    forms.COORDS = (x, y, s)
    metric = forms.MetricForms((sp.exp(-s), sp.exp(-s), 1))
    ordered = TANGENT + tuple(j+(2,) for j in TANGENT)
    signs = (1,)*4 + tuple((-1)**len(j) for j in TANGENT)
    weights = tuple(sp.exp((1-len(j))*s) for j in TANGENT)*2
    phase = sp.exp(kx*x+ky*y+ks*s)
    dH = {(0,): ux, (1,): uy, (2,): g}
    matrix = sp.zeros(8)
    unitary = []
    for col, j in enumerate(ordered):
        coeff = signs[col]*weights[col]
        unitary.append(sp.simplify(coeff**2*metric.volume/metric.basis_length(j)**2))
        out = metric.D({j: coeff*phase}, dH)
        for row, k in enumerate(ordered):
            matrix[row, col] = sp.simplify(out.get(k, 0)/(signs[row]*weights[row]*phase))
    d, delta = transverse_symbol()
    DT = d+delta
    B = (g+1)*EYE-N
    expected = sp.BlockMatrix([[sp.exp(s)*DT, B-ks*EYE],
                               [B+ks*EYE, -sp.exp(s)*DT]]).as_explicit()
    no_shift = sp.BlockMatrix([[sp.exp(s)*DT, (g-ks)*EYE],
                               [(g+ks)*EYE, -sp.exp(s)*DT]]).as_explicit()
    return dict(matrix=simplified(matrix), expected=simplified(expected),
                residual=simplified(matrix-expected), unitary=unitary,
                no_degree_shift_residual=simplified(matrix-no_shift),
                omitted_weight_norms=[sp.exp((2*len(j)-2)*s) for j in TANGENT])


def add_coefficient(out, key, value):
    out[key] = out.get(key, sp.zeros(8))+value


@lru_cache(maxsize=1)
def square_derivation():
    M = metric_derivation()["matrix"]
    U, h = sp.Function("U")(x, y), sp.Function("h")(s)
    coordinates = (x, y, s)
    substitutions = {ux: sp.diff(U, x), uy: sp.diff(U, y), g: sp.diff(h, s)}
    first = {ZERO: M.subs({kx: 0, ky: 0, ks: 0}).subs(substitutions)}
    for i, frequency in enumerate((kx, ky, ks)):
        key = tuple(int(k == i) for k in range(3))
        first[key] = M.diff(frequency)
    actual = {}
    for left_index, A in first.items():
        for right_index, B in first.items():
            key = tuple(i+j for i, j in zip(left_index, right_index))
            add_coefficient(actual, key, A*B)
            if left_index != ZERO:
                variable = coordinates[left_index.index(1)]
                add_coefficient(actual, right_index, A*B.diff(variable))
    actual = {key: simplified(value) for key, value in actual.items()}
    Ut = (sp.diff(U, x), sp.diff(U, y))
    VT = (Ut[0]**2+Ut[1]**2)*EYE
    for i in range(2):
        for j in range(2):
            VT += (EPS[i]-IOTA[i])*(EPS[j]+IOTA[j])*sp.diff(U, coordinates[i], coordinates[j])
    d0 = sum((EPS[i]*Ut[i] for i in range(2)), sp.zeros(4))
    delta0 = sum((IOTA[i]*Ut[i] for i in range(2)), sp.zeros(4))
    B = (sp.diff(h, s)+1)*EYE-N
    Bprime = sp.diff(h, s, 2)*EYE
    expected = {
        (2, 0, 0): -sp.exp(2*s)*sp.eye(8),
        (0, 2, 0): -sp.exp(2*s)*sp.eye(8),
        (0, 0, 2): -sp.eye(8),
        ZERO: sp.BlockMatrix([
            [sp.exp(2*s)*VT+B*B-Bprime, 2*sp.exp(s)*d0],
            [2*sp.exp(s)*delta0, sp.exp(2*s)*VT+B*B+Bprime]]).as_explicit()}
    for i in range(2):
        key = tuple(int(k == i) for k in range(3))
        expected[key] = sp.BlockMatrix([
            [sp.zeros(4), 2*sp.exp(s)*EPS[i]],
            [-2*sp.exp(s)*IOTA[i], sp.zeros(4)]]).as_explicit()
    residual = {key: simplified(actual.get(key, sp.zeros(8))-expected.get(key, sp.zeros(8)))
                for key in actual.keys() | expected.keys()}
    return dict(actual=actual, expected=expected, residual=residual,
                missing_cross_witness=actual[(1, 0, 0)])


@lru_cache(maxsize=1)
def algebra_controls():
    d, delta = transverse_symbol()
    # In this formal symbol delta is the adjoint after k -> i*real frequency.
    DT = d+delta
    S = sp.BlockMatrix([[sp.zeros(4), d], [delta, sp.zeros(4)]]).as_explicit()
    difference = sp.diag(DT*DT, DT*DT)-S*S
    complement = sp.diag(delta*d, d*delta)
    t = sp.Symbol("t", nonnegative=True)
    a, b = sp.symbols("a b", real=True)
    eps3 = tuple(wedge_matrix(i, 3) for i in range(3))
    v = sp.symbols("v0:3", real=True)
    clifford = sum(((eps3[i]+eps3[i].T)*v[i] for i in range(3)), sp.zeros(8))
    return dict(d_squared=simplified(d*d), delta_squared=simplified(delta*delta),
                degree_d=simplified(N*d-d*N-d),
                degree_delta=simplified(N*delta-delta*N+delta),
                cross_complement=simplified(difference-complement),
                high_tail_polynomial=sp.expand(((t+8)-1)**2-3*(t+8)-2-(t+8)**2/4),
                perturbation_square=sp.expand((a-b)**2-(a*a/2-b*b)),
                clifford_square=simplified(clifford*clifford-sum(z*z for z in v)*sp.eye(8)))


def radial(s_value, q, b, c):
    s_value = np.asarray(s_value, dtype=float)
    factor = q*np.exp(2*s_value)
    return factor*(b*(2*s_value+1)+2*c), factor*(b*(4*s_value+4)+4*c)


def sufficient_height(q, b, c):
    if b <= 0 or q == 0 or not all(math.isfinite(v) for v in (q, b, c)):
        raise ValueError("This sufficient bound requires finite b>0 and nonzero q")
    return max(0., .5-c/b, .5*math.log(4/(abs(q)*b)))


def radial_controls():
    cusp = load_local("r17_source_cusp", "singular_cusp.py")
    rows = []
    for beta in ((1., 1., 1.), (1., 2., 3.)):
        for q in (-2., -.25, .25, 2.):
            for c in (-20., 0., 20.):
                field = cusp.CuspField(beta=beta, c=c)
                b = math.pi*field.total/field.tau.imag
                start = sufficient_height(q, b, c)
                for height in (start, start+.5, start+1.):
                    z = math.exp(height)
                    _, rz, rzz = field.radial(z)
                    hp, hpp = radial(height, q, b, c)
                    reference_hp, reference_hpp = q*z*rz, q*(z*z*rzz+z*rz)
                    t = abs(float(hp))
                    W = max(t-1, 0)**2-abs(float(hpp))-2
                    rows.append(dict(beta=beta, q=q, c=c, b=b, s=height, start=start,
                        hprime=float(hp), hsecond=float(hpp),
                        derivative_error=max(abs(float(hp/reference_hp)-1),
                                             abs(float(hpp/reference_hpp)-1)),
                        sufficient=True, bound=W, simplified_bound=t*t/4,
                        slope_margin=b*(2*height+1)+2*c-2*b,
                        hprime_margin=t-8, hsecond_margin=3*t-abs(float(hpp))))
    return rows


def complex_controls():
    rng = np.random.default_rng(170907)
    eps = [np.array(E, dtype=complex) for E in EPS]
    rows = []
    for scale in (.1, 1., 10., 100.):
        v = scale*(rng.normal(size=2)+1j*rng.normal(size=2))
        d = sum((eps[i]*v[i] for i in range(2)), np.zeros((4, 4), complex))
        delta = d.conj().T
        DT = d+delta
        S = np.block([[np.zeros((4, 4)), d], [delta, np.zeros((4, 4))]])
        diagonal = np.kron(np.eye(2), DT@DT)
        complement = diagonal-S@S
        eigen = np.linalg.eigvalsh(complement)
        rows.append(dict(scale=scale, nilpotent_norm=float(np.linalg.norm(d@d)),
                         complement_min=float(eigen.min()), complement_max=float(eigen.max()),
                         cross_nonzero=float(np.linalg.norm(S))))
    return rows


def integrate_complex(q, b, c, order=128):
    rng = np.random.default_rng(170918)
    eps = [np.array(E, dtype=complex) for E in EPS]
    d = eps[0]*(.4+1.2j)+eps[1]*(-.7+.9j)
    delta, Ndiag = d.conj().T, np.array([0., 1., 1., 2.])
    DT = d+delta
    v0 = rng.normal(size=8)+1j*rng.normal(size=8)
    v1 = rng.normal(size=8)+1j*rng.normal(size=8)
    start, width = sufficient_height(q, b, c), .8
    nodes, weights = leggauss(order)
    tt = (nodes+1)/2
    heights = start+width*tt
    angles = math.pi*tt
    envelope = np.sin(angles)**2
    derivative = 2*math.pi/width*np.sin(angles)*np.cos(angles)
    mix = v0[None, :]+tt[:, None]*v1[None, :]
    psi = envelope[:, None]*mix
    ps = derivative[:, None]*mix+envelope[:, None]*v1[None, :]/width
    alpha, beta, ap, bp = psi[:, :4], psi[:, 4:], ps[:, :4], ps[:, 4:]
    Ta, Tb, db = alpha@DT.T, beta@DT.T, beta@d.T
    hp, hpp = radial(heights, q, b, c)
    shift = hp[:, None]+1-Ndiag[None, :]
    exp = np.exp(heights)[:, None]
    output = np.column_stack((exp*Ta-bp+shift*beta, ap+shift*alpha-exp*Tb))
    norm_density = np.sum(abs(psi)**2, axis=1)
    derivative_density = np.sum(abs(ps)**2, axis=1)
    tangent = np.exp(2*heights)*np.sum(abs(Ta)**2+abs(Tb)**2, axis=1)
    shift_density = np.sum(shift**2*(abs(alpha)**2+abs(beta)**2), axis=1)
    second = hpp*np.sum(abs(beta)**2-abs(alpha)**2, axis=1)
    cross = 4*np.exp(heights)*np.real(np.sum(alpha.conj()*db, axis=1))
    W = np.maximum(abs(hp)-1, 0)**2-abs(hpp)-2
    integrator = lambda values: float(width/2*np.dot(weights, values))
    energy = integrator(np.sum(abs(output)**2, axis=1))
    expanded = integrator(derivative_density+tangent+shift_density+second+cross)
    lower = integrator(derivative_density+.5*tangent+W*norm_density)
    simple = integrator(hp*hp/4*norm_density)
    return dict(q=q, b=b, c=c, order=order, start=start, norm=integrator(norm_density),
                direct_energy=energy, expanded_energy=expanded, cross=integrator(cross),
                identity_error=abs(energy-expanded)/energy,
                lower_margin=energy-lower, simple_margin=energy-simple,
                missing_cross_error=abs(energy-(expanded-integrator(cross)))/energy)


def energy_controls():
    rows = []
    b = math.pi*3/(math.sqrt(3)/2)
    for q in (-2., -.25, .25, 2.):
        for c in (-20., 0., 20.):
            low, high = integrate_complex(q, b, c, 64), integrate_complex(q, b, c, 128)
            high["quadrature_change"] = abs(low["direct_energy"]/high["direct_energy"]-1)
            rows.append(high)
    return rows


@lru_cache(maxsize=1)
def neutral_controls():
    tau = sp.Symbol("tau", real=True)
    f = sp.sin(sp.pi*tau)**2
    norm = sp.integrate(sp.expand_trig(f*f), (tau, 0, 1))
    energy = sp.integrate(sp.expand_trig(sp.diff(f, tau)**2), (tau, 0, 1))
    nodes, weights = leggauss(64)
    tt = (nodes+1)/2
    rows = []
    for L in (1., 2., 4., 8., 16.):
        numeric_norm = L/2*np.dot(weights, np.sin(math.pi*tt)**4)
        numeric_energy = L/2*np.dot(weights, (2*math.pi/L*np.sin(math.pi*tt)*np.cos(math.pi*tt))**2)
        rows.append(dict(length=L, one_form=float(numeric_energy/numeric_norm),
                         exact=float(energy/norm)/L**2,
                         scalar=1+float(numeric_energy/numeric_norm)))
    return dict(profile_norm=norm, profile_energy=energy,
                one_form_constant=sp.simplify(energy/norm), rows=rows)


@lru_cache(maxsize=1)
def corrector_controls():
    z, k = sp.symbols("z k", positive=True)
    f = z*sp.besselk(1, k*z)
    derivative = sp.besselsimp(sp.diff(f, z)+k*z*sp.besselk(0, k*z))
    pde = sp.besselsimp(sp.diff(f, z, 2)-sp.diff(f, z)/z-k*k*f)
    rows = []
    with mp.workdps(50):
        for freq in (1, 2, 4):
            for height in (2, 4, 8):
                kv, zv = mp.mpf(freq), mp.mpf(height)
                numerical = mp.diff(lambda v: v*mp.besselk(1, kv*v), zv)
                reference = -kv*zv*mp.besselk(0, kv*zv)
                bound = kv*zv*zv*mp.sqrt(mp.besselk(0, kv*zv)**2+mp.besselk(1, kv*zv)**2)
                rows.append(dict(k=freq, z=height, derivative_error=str(abs(numerical-reference)),
                                 orthonormal_gradient_bound=str(bound)))
    return dict(derivative_residual=derivative, pde_residual=pde, modes=rows)


def serializable(value):
    if isinstance(value, sp.MatrixBase):
        return [[str(v) for v in row] for row in value.tolist()]
    if isinstance(value, sp.Basic):
        return str(value)
    if isinstance(value, dict):
        return {str(k): serializable(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [serializable(v) for v in value]
    return value


def run():
    start = time.monotonic()
    out = dict(scope="Uniform charged cusp-tail estimate in a fixed tangential complex; no global H1 count",
               metric=metric_derivation(), square=square_derivation(), algebra=algebra_controls(),
               radial=radial_controls(), finite_complex=complex_controls(), energy=energy_controls(),
               neutral=neutral_controls(), corrector=corrector_controls())
    out["runtime_seconds"] = time.monotonic()-start
    return out


if __name__ == "__main__":
    print(json.dumps(serializable(run()), indent=2, sort_keys=True), flush=True)
