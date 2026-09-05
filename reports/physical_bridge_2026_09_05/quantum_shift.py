"""R6: full one-loop gradient and leading normal shift of the chosen E6 model."""
import argparse
from functools import lru_cache
import hashlib
import json
from pathlib import Path
import time

import numpy as np
import sympy as sp

from . import vacuum as v
from . import quantum_vacuum as q


@lru_cache(maxsize=1)
def tensor():
    out = np.zeros((27, 27, 27))
    for index, value in v.cubic()[3].items():
        out[index] = float(value)
    return out


def constraint_hessian(coefficients):
    """Exact real quadratic-form recipe for sum coefficients[a]*constraint[a]."""
    w = np.asarray(coefficients, float)
    if w.shape != (275,):
        raise ValueError("275 real constraint coefficients required")
    out = np.zeros((186, 186))
    out[:54, :54] = 2*w[0]*np.eye(54)
    out[54:108, 54:108] = 2*w[1]*np.eye(54)
    unit = np.eye(27)
    cross = np.block([[w[2]*unit, w[3]*unit], [-w[3]*unit, w[2]*unit]])
    out[:54, 54:108] += cross
    out[54:108, :54] += cross.T
    for start, left, right in [(4, 0, 0), (58, 0, 54), (112, 54, 54)]:
        z = w[start:start+27]-1j*w[start+27:start+54]
        d = np.einsum("a,abc->bc", z, tensor())
        block = np.block([[d.real, -d.imag], [-d.imag, -d.real]])
        if left == right:
            out[left:left+54, right:right+54] += 2*block
        else:
            out[left:left+54, right:right+54] += block
            out[right:right+54, left:left+54] += block.T
    geo = q.geometry()
    out[108:, 108:] = 2*w[166]*geo["gram"]
    for start, offset in [(167, 0), (221, 54)]:
        z = w[start:start+27]-1j*w[start+27:start+54]
        block = np.einsum("i,aij->aj", z, geo["T"])
        real = np.hstack((block.real, -block.imag))
        out[108:, offset:offset+54] += real
        out[offset:offset+54, 108:] += real.T
    return out


@lru_cache(maxsize=1)
def all_constraint_hessians():
    # About 76 MB, finite and explicit; no omitted scalar directions.
    return np.array([constraint_hessian(row) for row in np.eye(275)])


def coordinates(p, n, a):
    geo = q.geometry()
    h = geo["gram_inv"]@np.einsum("bij,ji->b", geo["T"], a).real
    return np.concatenate((np.asarray(p).real, np.asarray(p).imag,
                           np.asarray(n).real, np.asarray(n).imag, h))


def fields(z):
    z = np.asarray(z, float)
    if z.shape != (186,):
        raise ValueError("186 scalar coordinates required")
    return (z[:27]+1j*z[27:54], z[54:81]+1j*z[81:108],
            np.einsum("a,aij->ij", z[108:], q.geometry()["T"]))


def vacuum_coordinates():
    geo = q.geometry()
    return coordinates(geo["s"], geo["n"], geo["y"])


def constraint_data(z):
    jac = np.einsum("aij,j->ai", all_constraint_hessians(), z, optimize=True)
    c = jac@z/2
    c[[0, 1, 166]] -= [1, 1, 5]
    return c, jac


def full_tree_hessian(z, lam):
    c, jac = constraint_data(z)
    return 2*lam*(jac.T@jac+constraint_hessian(c))


def tree_hessian_derivative(z, direction, lam):
    _, jac = constraint_data(z)
    dj = np.einsum("aij,j->ai", all_constraint_hessians(), direction, optimize=True)
    return 2*lam*(dj.T@jac+jac.T@dj+constraint_hessian(jac@direction))


def orbit(z):
    p, n, a = fields(z)
    geo = q.geometry()
    out = np.zeros((186, 78))
    for offset, field in [(0, p), (54, n)]:
        action = 1j*np.einsum("aij,j->ai", geo["T"], field)
        out[offset:offset+54, :] = np.hstack((action.real, action.imag)).T
    action = 1j*(geo["T"]@a-a@geo["T"])
    projection = np.einsum("bij,aji->ba", geo["T"], action, optimize=True).real
    out[108:, :] = geo["gram_inv"]@projection
    return out


def fermion_mass(z, yukawa):
    p, n, _ = fields(z)
    return yukawa*np.einsum("abc,c->ab", tensor(), p+n)


def fprime_matrix(mass_squared, constant, mu):
    m = np.asarray(mass_squared)
    if not np.allclose(m, m.conj().T, atol=1e-11):
        raise ValueError("Hermitian mass squared required")
    ev, u = np.linalg.eigh(m)
    tol = 2e-10*max(1, np.max(np.abs(ev)))
    if ev.min() < -tol:
        raise ValueError("negative mass squared at expansion point")
    ev = np.maximum(ev, 0)
    fp = np.zeros_like(ev)
    positive = ev > 0
    fp[positive] = ev[positive]*(2*np.log(ev[positive]/mu**2)-2*constant+1)
    return (u*fp)@u.conj().T


def one_loop_gradient(lam=.2, gauge=.5, yukawa=.25, mu=1.):
    """All 186 derivatives; no off-vacuum logarithms or projected-away forces."""
    geo = q.geometry()
    z = vacuum_coordinates()
    _, jac = constraint_data(z)
    h0 = 2*lam*jac.T@jac
    ms = geo["si"]@h0@geo["si"]
    ps = geo["si"]@fprime_matrix(ms, 1.5, mu)@geo["si"]
    jp = jac@ps
    qs = all_constraint_hessians()
    scalar = 4*lam*np.einsum("ai,air->r", jp, qs, optimize=True)
    scalar += 2*lam*jac.T@np.einsum("ij,aji->a", ps, qs, optimize=True)
    go = orbit(z)
    mv = gauge**2*geo["gi"]@go.T@geo["ks"]@go@geo["gi"]
    pv = geo["gi"]@fprime_matrix(mv, 5/6, mu)@geo["gi"]
    gv = geo["ks"]@go@pv
    mf = fermion_mass(z, yukawa)
    pf = fprime_matrix(mf.conj().T@mf, 1.5, mu)
    vector = np.zeros(186)
    fermion = np.zeros(186)
    for r in range(186):
        direction = np.eye(186)[r]
        derivative_orbit = orbit(direction)
        vector[r] = 6*gauge**2*np.sum(gv*derivative_orbit)
        derivative_mass = fermion_mass(direction, yukawa)
        derivative_squared = derivative_mass.conj().T@mf+mf.conj().T@derivative_mass
        fermion[r] = -2*np.trace(pf@derivative_squared).real
    parts = np.array([scalar, fermion, vector])/(64*np.pi**2)
    return parts, h0


def sm_singlet_basis():
    geo = q.geometry()
    columns = []
    for offset in [0, 27, 54, 81]:
        for sv in [geo["s"].real, geo["n"].real]:
            col = np.zeros(186)
            col[offset:offset+27] = sv
            columns.append(col)
    for ns in v.CARTAN.extract([2, 3, 5], list(range(6))).nullspace():
        col = np.zeros(186)
        col[108:114] = np.array(ns, float).ravel()
        columns.append(col)
    exact_yh = v.embedding()[3]
    for r, (_, label, _) in enumerate(v.representation()[3]):
        if all(label[i] == 0 for i in [2, 3, 5]) and sum(exact_yh[i]*label[i] for i in range(6)) == 0:
            for k in [6+2*r, 7+2*r]:
                columns.append(np.eye(186)[108+k])
    raw = np.array(columns).T
    b = raw@q.invsqrt_positive(raw.T@geo["ks"]@raw)
    assert b.shape == (186, 13)
    sm = np.array(v.sm_generator_coordinates(), float)
    for col in b.T:
        np.testing.assert_allclose(orbit(col)@sm, 0, atol=1e-12)
    return b


def solve_shift(lam=.2, gauge=.5, yukawa=.25, mu=1.):
    geo = q.geometry()
    parts, h0 = one_loop_gradient(lam, gauge, yukawa, mu)
    force = parts.sum(axis=0)
    canonical_force = geo["si"]@force
    hc = geo["si"]@h0@geo["si"]
    ev, u = np.linalg.eigh(hc)
    positive = ev > 1e-9
    assert np.count_nonzero(positive) == 109
    kernel_force = u[:, ~positive].T@canonical_force
    assert np.max(np.abs(kernel_force)) < 1e-9
    displacement_c = -u[:, positive]@((u[:, positive].T@canonical_force)/ev[positive])
    displacement = geo["si"]@displacement_c
    residual = h0@displacement+force
    assert np.max(np.abs(residual)) < 1e-9
    z = vacuum_coordinates()
    sm = np.array(v.sm_generator_coordinates(), float)
    assert np.max(np.abs(orbit(displacement)@sm)) < 1e-9
    np.testing.assert_allclose(orbit(z).T@force, 0, atol=1e-9)
    p, n, a = fields(displacement)
    relative = [float(np.linalg.norm(p)), float(np.linalg.norm(n)),
                float(np.linalg.norm(a)/np.sqrt(5))]
    shifted = z+displacement
    go = orbit(shifted)
    vm = gauge**2*geo["gi"]@go.T@geo["ks"]@go@geo["gi"]
    vv = q.psd_eigenvalues(vm)
    b = sm_singlet_basis()
    singlet_normal_rank = np.linalg.matrix_rank(b.T@h0@b, tol=1e-9)
    singlet_gauge_rank = np.linalg.matrix_rank(b.T@geo["ks"]@orbit(z), tol=1e-9)
    assert (singlet_normal_rank, singlet_gauge_rank) == (9, 4)
    physical_force = np.linalg.solve(geo["ks"], force)
    np.testing.assert_allclose(physical_force, b@(b.T@force), atol=1e-9)
    # The normal shift and the curved tree-vacuum path produce the same
    # leading angular correction; use the full cubic derivative of V0.
    change = tree_hessian_derivative(z, displacement, lam)
    path_second = np.zeros(186)
    path_second[108:114] = -geo["yh"]/5
    relation = {}
    for name, idx in [("color_octet", 2), ("weak_triplet", 5)]:
        tangent = np.zeros(186)
        tangent[108+idx] = 1/np.sqrt(geo["gram"][idx, idx])
        left = float(tangent@change@tangent)
        right = float(force@path_second)
        assert abs(left-right) < 1e-9
        relation[name] = {"normal_shift_tree_mass_correction": left,
                          "curved_path_gradient_term": right}
    return {"lambda": lam, "g": gauge, "y1_y2": yukawa, "mu": mu,
            "one_loop_gradient_parts_scalar_fermion_vector": parts.tolist(),
            "coordinate_displacement": displacement.tolist(),
            "relative_field_shifts_phi1_phi2_adjoint": relative,
            "canonical_shift_norm": float(np.linalg.norm(displacement_c)),
            "relative_canonical_shift_norm": float(np.linalg.norm(displacement_c)/3),
            "passes_declared_ten_percent_shift_diagnostic": bool(max(relative) < .1),
            "minimum_positive_tree_mass_squared": float(ev[positive].min()),
            "kernel_gradient_max_abs": float(np.max(np.abs(kernel_force))),
            "first_order_stationarity_max_abs": float(np.max(np.abs(residual))),
            "SM_singlet_dimensions": {"real": 13, "gauge": int(singlet_gauge_rank),
                                       "physical_normal": int(singlet_normal_rank)},
            "shifted_unbroken_dimension_at_tolerance_1e-8": int(np.count_nonzero(vv < 1e-8)),
            "angular_shift_identity": relation}


def primitive_checks():
    z = vacuum_coordinates()
    np.testing.assert_allclose(constraint_data(z)[1], q.geometry()["j"], atol=1e-12)
    rng = np.random.default_rng(6120926)
    for _ in range(3):
        shifted = z+.1*rng.normal(size=186)
        c, _ = constraint_data(shifted)
        np.testing.assert_allclose(c, v.constraints(*fields(shifted)), atol=2e-12)
    direction = rng.normal(size=186)
    direction /= np.linalg.norm(direction)
    step = 1e-4
    analytic = tree_hessian_derivative(z, direction, .2)
    finite = (full_tree_hessian(z+step*direction, .2)-full_tree_hessian(z-step*direction, .2))/(2*step)
    np.testing.assert_allclose(finite, analytic, atol=5e-9)
    # Deliberately omit the normal-constraint term; this must fail on a radial.
    radial = np.zeros(186)
    radial[np.flatnonzero(q.geometry()["s"])[0]] = 1
    _, jac = constraint_data(z)
    missing = .4*constraint_hessian(jac@radial)
    assert np.max(np.abs(missing)) > 1
    return {"quadratic_constraint_and_J_reconstruction": True,
            "full_tree_H_derivative_max_error": float(np.max(np.abs(finite-analytic))),
            "omitted_normal_term_radial_max_error": float(np.max(np.abs(missing)))}


def analyze():
    checks = primitive_checks()
    runs = []
    for epsilon in [1., .25, .0625]:
        row = solve_shift(.2*epsilon, .5*np.sqrt(epsilon), .25*np.sqrt(epsilon), np.sqrt(epsilon))
        row["weak_coupling_epsilon"] = epsilon
        runs.append(row)
    original = np.array(runs[0]["coordinate_displacement"])
    for row in runs[1:]:
        np.testing.assert_allclose(row["coordinate_displacement"], original*row["weak_coupling_epsilon"], atol=1e-10)
    return {"scope": "leading MS-bar Landau-gauge normal shift; not full loop spectrum or a global vacuum",
            "primitive_checks": checks, "runs": runs,
            "weak_coupling_shift_scaling_verified": True}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    with args.output.open("x", encoding="utf-8") as handle:
        start = time.monotonic()
        result = analyze()
        result["code_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
        result["elapsed_seconds"] = time.monotonic()-start
        json.dump(result, handle, indent=2, allow_nan=False)
        handle.write("\n")
    brief = {**result, "runs": [{k: value for k, value in row.items()
                                if k not in ["one_loop_gradient_parts_scalar_fermion_vector", "coordinate_displacement"]}
                               for row in result["runs"]]}
    print(json.dumps(brief, indent=2, allow_nan=False))


if __name__ == "__main__":
    main()
