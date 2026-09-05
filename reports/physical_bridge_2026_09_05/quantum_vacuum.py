"""R5: complete one-loop angular potential for the explicitly chosen R4 action."""
import argparse
from functools import lru_cache
import hashlib
import json
from pathlib import Path
import subprocess
import time

import numpy as np
from scipy import linalg, optimize
import sympy as sp

from . import vacuum as v


def invsqrt_positive(matrix):
    a = np.asarray(matrix, float)
    if a.ndim != 2 or a.shape[0] != a.shape[1] or not np.isfinite(a).all():
        raise ValueError("finite square kinetic metric required")
    if not np.allclose(a, a.T, atol=1e-12, rtol=1e-12):
        raise ValueError("kinetic metric must be symmetric")
    ev, u = np.linalg.eigh(a)
    if ev.min() <= 0:
        raise ValueError("kinetic metric is not positive definite")
    return (u/np.sqrt(ev))@u.T


def psd_eigenvalues(matrix):
    a = np.asarray(matrix, float)
    if not np.isfinite(a).all() or not np.allclose(a, a.T, atol=1e-10, rtol=1e-10):
        raise ValueError("finite symmetric mass-squared matrix required")
    ev = np.linalg.eigvalsh((a+a.T)/2)
    tol = 2e-10*max(1, np.max(np.abs(ev)))
    if ev.min() < -tol:
        raise ValueError(f"negative tree mass squared: {ev.min()}")
    # Only floating-point negatives are clipped. Small positive eigenvalues
    # are retained; light emerging vector masses must not disappear by threshold.
    return np.maximum(ev, 0)


def log_sum(m2, constant, mu=1):
    x = np.asarray(m2, float)
    if mu <= 0 or not np.isfinite(mu) or not np.isfinite(x).all() or np.any(x < 0):
        raise ValueError("nonnegative finite masses and positive scale required")
    positive = x > 0
    return float(np.sum(x[positive]**2*(np.log(x[positive]/mu**2)-constant)))


def real_action(a):
    return np.block([[a.real, -a.imag], [a.imag, a.real]])


@lru_cache(maxsize=1)
def geometry():
    s, n, y, h, _, _ = v.embedding()
    tensors = np.array([np.array(t, complex) for t in v.representation()[4]])
    gram_complex = np.einsum("aij,bji->ab", tensors, tensors, optimize=True)
    assert np.max(np.abs(gram_complex.imag)) < 1e-12
    gram = gram_complex.real
    # Tr27((H_i/2)^2)=3 is checked, not inferred from the word E6.
    assert np.allclose(np.diag(gram)[:6]/4, 3)
    assert np.allclose(gram[:6, :6], 6*np.array(v.CARTAN, float))
    ks = linalg.block_diag(2*np.eye(108), gram)
    kg = gram/3
    js, gs = v.fluctuation_matrices()
    j, g = np.array(js, float), np.array(gs, float)
    assert np.linalg.matrix_rank(j, tol=1e-9) == 109
    assert np.linalg.matrix_rank(g, tol=1e-9) == 66
    return {"s": np.array(s, complex).ravel(), "n": np.array(n, complex).ravel(),
            "y": np.array(y, complex), "yh": np.array(h, float).ravel(),
            "T": tensors, "gram": gram, "gram_inv": np.linalg.inv(gram),
            "ks": ks, "kg": kg, "si": invsqrt_positive(ks), "gi": invsqrt_positive(kg),
            "cartan_si": invsqrt_positive(gram[2:6, 2:6]), "j": j, "g": g}


def normalize_adjoint(a):
    a = np.asarray(a, complex)
    if a.shape != (27, 27) or not np.isfinite(a).all() or not np.allclose(a, a.conj().T):
        raise ValueError("finite Hermitian adjoint required")
    norm2 = np.trace(a@a).real
    if norm2 <= 0:
        raise ValueError("zero adjoint cannot be normalized")
    return a*np.sqrt(5/norm2)


def cartan_background(x):
    x = np.asarray(x, float)
    if x.shape != (4,) or not np.isfinite(x).all() or np.linalg.norm(x) == 0:
        raise ValueError("nonzero finite four-dimensional Cartan direction required")
    geo = geometry()
    h = geo["cartan_si"]@x*np.sqrt(5)/np.linalg.norm(x)
    return np.einsum("a,aij->ij", h, geo["T"][2:6])


def sphere_coordinates(a):
    geo = geometry()
    h = np.linalg.solve(geo["gram"][2:6, 2:6],
                        np.einsum("aij,ji->a", geo["T"][2:6], a).real)
    return np.linalg.solve(geo["cartan_si"], h)/np.sqrt(5)


def matrices(a):
    """Unscaled full Hessian and gauge Gram at a zero of the tree constraints."""
    geo = geometry()
    a = np.asarray(a, complex)
    if not np.allclose(a, a.conj().T, atol=1e-12):
        raise ValueError("Hermitian adjoint required")
    coeffs = geo["gram_inv"]@np.einsum("bij,ji->b", geo["T"], a).real
    rebuilt = np.einsum("b,bij->ij", coeffs, geo["T"])
    if not np.allclose(rebuilt, a, atol=1e-10):
        raise ValueError("matrix is not in the specified adjoint representation")
    if (np.linalg.norm(a@geo["s"])+np.linalg.norm(a@geo["n"]) > 1e-9
            or abs(np.trace(a@a).real-5) > 1e-8):
        raise ValueError("background is outside the sealed tree-level vacuum family")
    j = geo["j"].copy()
    j[166, 108:] = 2*np.einsum("aij,ji->a", geo["T"], a).real
    j[167:221, :54] = real_action(a)
    j[221:275, 54:108] = real_action(a)
    tangent = 1j*(geo["T"]@a-a@geo["T"])
    projection = np.einsum("bij,aji->ba", geo["T"], tangent, optimize=True).real
    orbit = geo["g"].copy()
    orbit[108:, :] = geo["gram_inv"]@projection
    assert np.max(np.abs(j@orbit)) < 1e-9
    scalar = 2*j.T@j
    vector = orbit.T@geo["ks"]@orbit
    return scalar, vector, j, orbit


def spectra(a):
    hs, hv, _, _ = matrices(a)
    geo = geometry()
    ms = psd_eigenvalues(geo["si"]@hs@geo["si"])
    mv = psd_eigenvalues(geo["gi"]@hv@geo["gi"])
    return ms, mv


@lru_cache(maxsize=1)
def fermion_squared():
    s, n = v.embedding()[:2]
    mass = np.array((v.contract(s)+v.contract(n))/4, complex)
    result = np.linalg.svd(mass, compute_uv=False)**2
    np.testing.assert_allclose(result[:10], 1/8, atol=1e-12)
    np.testing.assert_allclose(result[10:], 0, atol=1e-12)
    return result


def potential_parts(ms, mv, lam=1, g=1, mu=1):
    if lam <= 0 or g < 0 or not np.isfinite([lam, g]).all():
        raise ValueError("positive quartic coefficient and nonnegative gauge coupling required")
    return np.array([log_sum(lam*ms, 1.5, mu),
                     -2*log_sum(fermion_squared(), 1.5, mu),
                     3*log_sum(g*g*mv, 5/6, mu)])/(64*np.pi**2)


def curvature_components(a, direction, eps):
    a, direction = np.asarray(a, complex), np.asarray(direction, complex)
    assert abs(np.trace(a@direction)) < 1e-10
    direction /= np.sqrt(np.trace(direction@direction).real)
    center = potential_parts(*spectra(a))
    plus = potential_parts(*spectra(normalize_adjoint(a+eps*direction)))
    minus = potential_parts(*spectra(normalize_adjoint(a-eps*direction)))
    return (plus+minus-2*center)/eps**2


def primitive_checks():
    geo = geometry()
    y = geo["y"]
    hs, hv, _, _ = matrices(y)
    ms, mv = spectra(y)
    np.testing.assert_allclose(ms, np.maximum(linalg.eigh(hs, geo["ks"], eigvals_only=True), 0), atol=1e-10)
    np.testing.assert_allclose(mv, np.maximum(linalg.eigh(hv, geo["kg"], eigvals_only=True), 0), atol=1e-10)
    assert len(ms) == 186 and np.count_nonzero(ms > 1e-8) == 109
    assert len(mv) == 78 and np.count_nonzero(mv > 1e-8) == 66
    action_s = np.einsum("aij,j->ai", geo["T"], geo["s"])
    action_n = np.einsum("aij,j->ai", geo["T"], geo["n"])
    da = 1j*(geo["T"]@y-y@geo["T"])
    direct = 2*(action_s.conj()@action_s.T+action_n.conj()@action_n.T).real
    direct += np.einsum("aij,bji->ab", da, da, optimize=True).real
    np.testing.assert_allclose(hv, direct, atol=1e-10)
    # Pure norm-square terms: complex radial coordinate has K=2, adjoint K=Tr.
    unit_p = np.zeros(186)
    unit_p[np.flatnonzero(geo["s"])[0]] = 1/np.sqrt(2)
    assert abs(unit_p@hs@unit_p-4) < 1e-10
    radial = np.zeros(186)
    radial[108:114] = geo["yh"]/np.sqrt(5)
    assert abs(radial@geo["ks"]@radial-1) < 1e-12
    assert abs(radial@hs@radial-40) < 1e-10
    # One complex charge-q VEV v gives Mv^2=2 g^2 q^2 v^2.
    charge, vev, coupling = 3., 2., .5
    orbit = np.array([[0.], [charge*vev]])
    assert float((coupling**2*orbit.T@(2*np.eye(2))@orbit)[0, 0]) == 2*coupling**2*charge**2*vev**2
    a = cartan_background(np.array([1., 2., 3., 4.]))
    _, _, jac, _ = matrices(a)
    rng = np.random.default_rng(7101)
    direction = rng.normal(size=186)
    direction /= np.linalg.norm(direction)
    eps = 1e-4
    fields_p = list(v.fields_at(eps*direction))
    fields_m = list(v.fields_at(-eps*direction))
    fields_p[2] += a-y
    fields_m[2] += a-y
    deriv = (v.constraints(*fields_p)-v.constraints(*fields_m))/(2*eps)
    np.testing.assert_allclose(deriv, jac@direction, atol=2e-10)
    return {"scalar_modes": len(ms), "scalar_positive": int(np.count_nonzero(ms > 1e-8)),
            "vector_modes": len(mv), "vector_massive": int(np.count_nonzero(mv > 1e-8)),
            "fermion_modes": len(fermion_squared()), "fermion_massive": 10,
            "complex_radial_m2_at_lambda_1": float(unit_p@hs@unit_p),
            "adjoint_radial_m2_at_lambda_1": float(radial@hs@radial),
            "generalized_mass_and_direct_kinetic_checks": True,
            "non_Y_constraint_derivative_max_error": float(np.max(np.abs(deriv-jac@direction)))}


def named_backgrounds():
    geo = geometry()
    # On the defining SU5, H3+2 H4+3 H5+4 H6 has eigenvalues (1,1,1,1,-4).
    su4 = normalize_adjoint(np.einsum("a,aij->ij", [1, 2, 3, 4], geo["T"][2:6]))
    old = normalize_adjoint(np.einsum("a,aij->ij", [1, 4, 16, 64], geo["T"][2:6]))
    return {"SM_Y": geo["y"], "SU4_U1": su4, "old_generic_competitor": old}


def analyze():
    check = primitive_checks()
    geo = geometry()
    points = [(name, a) for name, a in named_backgrounds().items()]
    rng = np.random.default_rng(20260905)
    points += [(f"random_{i:03d}", cartan_background(rng.normal(size=4))) for i in range(96)]
    records, norms = [], []
    for name, a in points:
        ms, mv = spectra(a)
        norms.append([ms@ms, mv@mv])
        records.append({"name": name, "cartan_sphere_coordinates": sphere_coordinates(a).tolist(),
                        "scalar_m2_at_lambda_1": ms.tolist(), "vector_m2_at_g_1": mv.tolist(),
                        "parts_at_lambda_point2_g_point5": potential_parts(ms, mv, .2, .5).tolist(),
                        "unbroken_dimension": int(np.count_nonzero(mv < 1e-8))})
    norms = np.array(norms)
    variation = np.max(np.abs(norms-norms[0]), axis=0)
    assert np.all(variation < 5e-8*np.maximum(1, norms[0])), (variation, norms[0])
    ms0, mv0 = spectra(geo["y"])
    scale_differences = {}
    for name, a in points[:3]:
        ms, mv = spectra(a)
        delta = [float(np.sum(potential_parts(ms, mv, .2, .5, mu)
                             -potential_parts(ms0, mv0, .2, .5, mu))) for mu in [.5, 1, 2]]
        assert max(delta)-min(delta) < 5e-9
        scale_differences[name] = delta
    curvatures = {}
    for name, d in [("color_octet", geo["T"][2]), ("weak_triplet", geo["T"][5])]:
        curvatures[name] = {str(eps): curvature_components(geo["y"], d.copy(), eps).tolist()
                            for eps in [.02, .01, .005, .0025]}
    offdiagonal = {}
    for name, idx in [("color_octet", 2), ("weak_triplet", 5)]:
        e = v.representation()[2][tuple(v.CARTAN[:, idx])]
        offdiagonal[name] = curvature_components(geo["y"], np.array(e+e.T, complex), .005).tolist()
        np.testing.assert_allclose(offdiagonal[name], curvatures[name]["0.005"], atol=2e-7, rtol=2e-6)
    parameter_grid = []
    for lam in [.05, .2, 1.]:
        for coupling in [0., .25, .5, .75]:
            masses = {}
            for name in curvatures:
                cs, cf, cv = curvatures[name]["0.0025"]
                assert abs(cf) < 1e-8
                masses[name] = lam**2*cs+coupling**4*cv
            delta_su4 = np.sum(potential_parts(*spectra(points[1][1]), lam, coupling)
                              -potential_parts(ms0, mv0, lam, coupling))
            parameter_grid.append({"lambda": lam, "g": coupling,
                                   "leading_angular_m2": masses,
                                   "SU4_minus_SM_energy": float(delta_su4)})
    # Every local search uses the prechosen lambda=.2,g=.5, never a fitted value.
    ref = float(np.sum(potential_parts(ms0, mv0, .2, .5)))
    def objective(x):
        return float(np.sum(potential_parts(*spectra(cartan_background(x)), .2, .5)))-ref
    starts = sorted(records, key=lambda row: sum(row["parts_at_lambda_point2_g_point5"]))[:8]
    local = []
    for row in starts:
        result = optimize.minimize(objective, row["cartan_sphere_coordinates"], method="BFGS",
                                   options={"maxiter": 150, "gtol": 1e-7})
        a = cartan_background(result.x)
        ms, mv = spectra(a)
        local.append({"start": row["name"], "success": bool(result.success),
                      "status": int(result.status), "message": str(result.message),
                      "iterations": int(result.nit), "evaluations": int(result.nfev),
                      "energy_minus_SM": float(result.fun),
                      "cartan_sphere_coordinates": sphere_coordinates(a).tolist(),
                      "scalar_m2_at_lambda_1": ms.tolist(), "vector_m2_at_g_1": mv.tolist(),
                      "unbroken_dimension_at_tolerance_1e-8": int(np.count_nonzero(mv < 1e-8))})
    return {"scope": "R5 chosen one-loop MS-bar Landau-gauge angular calculation; not pole masses or a TOE",
            "checks": check, "mass_fourth_trace_at_SM_scalar_vector": norms[0].tolist(),
            "mass_fourth_trace_max_orientation_variation": variation.tolist(),
            "scale_controls_mu_half_1_2": scale_differences,
            "SM_curvature_components_scalar_fermion_vector": curvatures,
            "SM_offdiagonal_curvature_controls": offdiagonal,
            "parameter_grid": parameter_grid, "all_initial_points": records, "all_local_runs": local,
            "fermion_m2_y_one_quarter": fermion_squared().tolist(),
            "global_minimum_certified": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    # Reserve the unique output before work; a failed empty artifact stays visible.
    with args.output.open("x", encoding="utf-8") as handle:
        start = time.monotonic()
        result = analyze()
        result["code_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
        result["head"] = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=v.ROOT, text=True).strip()
        result["elapsed_seconds"] = time.monotonic()-start
        json.dump(result, handle, indent=2, allow_nan=False)
        handle.write("\n")
    brief = {k: val for k, val in result.items() if k not in ["all_initial_points", "all_local_runs"]}
    brief["local_searches"] = [{k: val for k, val in row.items()
                               if not k.startswith(("scalar_m2", "vector_m2"))}
                              for row in result["all_local_runs"]]
    print(json.dumps(brief, indent=2, allow_nan=False))


if __name__ == "__main__":
    main()
