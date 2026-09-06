"""R10: finite hard determinant and normal-induced triplet relaxation."""
import argparse
from functools import lru_cache
import hashlib
import json
from pathlib import Path
import time

import numpy as np
import sympy as sp

from . import infrared_alignment as a
from . import broken_vacuum as b
from . import higgs_sector as h
from . import quantum_vacuum as q

HERE = Path(__file__).resolve().parent
PINS = {
    **a.PINS,
    "infrared_alignment.py": "b0625500c6c7194175a30c0f1887a3ad0c5dadadff8cc905713ea1211b0c0fd6",
    "infrared_alignment_first_run.json": "6ddab8d1a67dc11aa86e02205b93d09b5118755a2f181447898ec43659447f97",
}
STEPS = np.array([.08, .064, .05, .04, .032, .0256])
COUNTS = (209, 10, 66)
CONSTANTS = (1.5, 1.5, 5/6)
SPIN = np.array([1., -2., 3.])/(64*np.pi**2)
QUARTIC_TOL = 2e-5
SOURCE_TOL = 2e-6


@lru_cache(maxsize=1)
def inputs():
    for name, digest in PINS.items():
        assert hashlib.sha256((HERE/name).read_bytes()).hexdigest() == digest, name
    row = next(r for r in b.inputs()["quantum"]["runs"] if r["mu"] == 1.)
    return np.array(row["normal_displacement"]), a.inputs()["quantum"]["masses_O_T_U_D"]


def hard_trace(matrix, count, constant, directions=()):
    matrix = np.asarray(matrix)
    if (matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]
            or not np.isfinite(matrix).all()
            or not np.allclose(matrix, matrix.conj().T, atol=1e-11, rtol=0)):
        raise ValueError("finite Hermitian matrix required")
    if not isinstance(count, int) or not 0 < count < len(matrix):
        raise ValueError("a proper positive hard count is required")
    ev, vectors = np.linalg.eigh(matrix)
    low, high = ev[:-count], ev[-count:]
    if high.min() <= 0 or low.max() >= .85*high.min():
        raise ValueError("hard/soft spectral separation failed")
    uh = vectors[:, -count:]
    fp = high*(2*np.log(high)-2*constant+1)
    density = (uh*fp)@uh.conj().T
    gradients = []
    for direction in directions:
        direction = np.asarray(direction)
        if direction.shape != matrix.shape or not np.isfinite(direction).all():
            raise ValueError("finite matching mass derivative required")
        gradients.append(float(np.einsum("ij,ji->", density, direction).real))
    return {"value": q.log_sum(high, constant), "gradient": np.array(gradients),
            "low_min": float(low.min()), "low_max": float(low.max()),
            "hard_min": float(high.min()), "hard_max": float(high.max()),
            "hard_count": count, "soft_count": len(low)}


def extrapolate(values, tolerance):
    values = np.asarray(values, float)
    if values.shape[0] != len(STEPS) or not np.isfinite(values).all():
        raise ValueError("six finite samples required")
    x = STEPS**2
    primary = np.polynomial.polynomial.polyfit(x[:-1], values[:-1], 2)
    cubic = np.polynomial.polynomial.polyfit(x[:-1], values[:-1], 3)
    shortened = np.polynomial.polynomial.polyfit(x[1:-1], values[1:-1], 2)
    holdout = np.polynomial.polynomial.polyval(x[-1], primary)
    resolution = max(b.maxabs(primary[0]-cubic[0]), b.maxabs(primary[0]-shortened[0]),
                     b.maxabs(holdout-values[-1]))
    if resolution > tolerance:
        raise ArithmeticError(f"extrapolation resolution {resolution} exceeds {tolerance}")
    return {"value": primary[0], "cubic_value": cubic[0], "shortened_value": shortened[0],
            "holdout_prediction": holdout, "holdout_actual": values[-1],
            "resolution": resolution, "samples": values}


def instrument_controls():
    x = STEPS**2
    known = 1.25-3*x+7*x**2
    fit = extrapolate(known, 1e-10)
    assert abs(fit["value"]-1.25) < 1e-10
    corrupt = known.copy()
    corrupt[-1] += .01
    try:
        extrapolate(corrupt, 1e-5)
    except ArithmeticError:
        pass
    else:
        raise AssertionError("corrupted extrapolation was accepted")
    mass = np.diag([0., .1, 2., 3.])
    derivative = np.diag([0., 0., 1., -1.])
    result = hard_trace(mass, 2, 1.5, [derivative])
    step = 1e-5
    numerical = (hard_trace(mass+step*derivative, 2, 1.5)["value"]
                 -hard_trace(mass-step*derivative, 2, 1.5)["value"])/(2*step)
    assert abs(numerical-result["gradient"][0]) < 1e-8
    rejected = 0
    for bad, count in [(np.diag([1., 1.01]), 1), (np.diag([-2., -1.]), 1),
                       (np.array([[0., 1.], [0., 2.]]), 1),
                       (np.diag([0., np.nan]), 1), (mass, 4)]:
        try:
            hard_trace(bad, count, 1.5)
        except ValueError:
            rejected += 1
    assert rejected == 5
    return {"known_polynomial_intercept": float(fit["value"]),
            "corrupted_polynomial_rejected": True, "invalid_matrix_controls_rejected": rejected,
            "independent_trace_derivative_error": abs(numerical-result["gradient"][0])}


def matrices(z):
    geo = h.geometry()
    mf, go = h.fermion_mass(z), h.orbit(z)
    return [geo["si"]@h.full_tree_hessian(z)@geo["si"], mf.conj().T@mf,
            .25*geo["gi"]@go.T@geo["ks"]@go@geo["gi"]]


def tree_gradient(z):
    return 2*h.jacobian(z).T@(h.weights()*h.constraints(z))


def mixed_mass_derivative(left, right, dl=None, dr=None):
    dl = h.derivatives(left) if dl is None else dl
    dr = h.derivatives(right) if dr is None else dr
    combined = h.derivatives(left+right)
    return [(combined[i][1]-dl[i][1]-dr[i][1])/2 for i in range(3)]


def normal_cubic(x, directions):
    delta, _ = inputs()
    geo, base = h.geometry(), h.base()
    r = a.embed(x)
    jd = h.jacobian(geo["z"]+delta)-base["j"]
    jr = h.jacobian(geo["z"]+r)-base["j"]
    crr, cdr = jr@r/2, jd@r
    full = 2*(jd.T@(base["w"]*crr)+jr.T@(base["w"]*cdr))
    return directions.T@full


@lru_cache(maxsize=1)
def geometry_controls():
    inputs()
    geo, lg, base = h.geometry(), b.light_geometry(), h.base()
    delta = inputs()[0]
    errors = []
    for eta in [0., .5, 1.]:
        r = a.embed(a.representative(eta))
        dm = h.derivatives(r)
        direct = matrices(geo["z"]+.047*r)
        errors.append(max(b.maxabs(direct[i]-base["masses"][i]-.047*dm[i][0]
                                  -.047**2*dm[i][1]/2) for i in range(3)))
        force = tree_gradient(geo["z"]+.17*r)
        errors.append(b.maxabs(lg["positive_modes"].T@geo["si"]@force))
    assert max(errors) < 1e-10
    x, directions = a.representative(.5), lg["L"][:, 8:11]
    r, da, hb = a.embed(x), .13, .07
    gradients = {}
    for ds, hs in [(1, 1), (1, -1), (-1, 1), (-1, -1), (1, 0), (-1, 0)]:
        gradients[ds, hs] = directions.T@tree_gradient(geo["z"]+ds*da*delta+hs*hb*r)
    numerical = (gradients[1, 1]+gradients[1, -1]-gradients[-1, 1]-gradients[-1, -1]
                 -2*gradients[1, 0]+2*gradients[-1, 0])/(4*da*hb**2)
    analytic = normal_cubic(x, directions)
    normal_error = b.maxabs(numerical-analytic)
    assert normal_error < 2e-8
    return {"mass_polynomial_and_tree_normal_force_errors": errors,
            "normal_mixed_derivative_error": normal_error,
            "normal_source_analytic": analytic, "normal_source_numerical": numerical}


@lru_cache(maxsize=8)
def path(eta):
    geo, lg, base = h.geometry(), b.light_geometry(), h.base()
    r = a.embed(a.representative(eta))
    dr = h.derivatives(r)
    triplets = lg["L"][:, 8:11]
    dt = [h.derivatives(t) for t in triplets.T]
    mixed = [mixed_mass_derivative(r, t, dr, td) for t, td in zip(triplets.T, dt)]
    base_source = np.array([hard_trace(base["masses"][i], COUNTS[i], CONSTANTS[i],
                                     [td[i][0] for td in dt])["gradient"] for i in range(3)])
    assert b.maxabs(base_source) < 1e-10
    rows = []
    for step in STEPS:
        endpoints = []
        for sign in [1, -1]:
            t = sign*step
            parts = []
            for i in range(3):
                mass = base["masses"][i]+t*dr[i][0]+t*t*dr[i][1]/2
                derivatives = [dr[i][0]+t*dr[i][1]]
                derivatives += [td[i][0]+t*mx[i] for td, mx in zip(dt, mixed)]
                parts.append(hard_trace(mass, COUNTS[i], CONSTANTS[i], derivatives))
            endpoints.append(parts)
        plus, minus = endpoints
        parity_error = max(abs(plus[i]["value"]-minus[i]["value"]) for i in range(3))
        assert parity_error < 1e-10
        values = np.array([(plus[i]["value"]+minus[i]["value"])/2 for i in range(3)])
        radial = np.array([(plus[i]["gradient"][0]-minus[i]["gradient"][0])/2 for i in range(3)])
        source = np.array([(plus[i]["gradient"][1:]+minus[i]["gradient"][1:])/2-base_source[i]
                           for i in range(3)])/step**2
        rows.append({"step": step, "hard_potential_parts": SPIN*values,
                     "hard_radial_gradient_parts": SPIN*radial,
                     "hard_triplet_source_parts": SPIN[:, None]*source,
                     "spectral_envelopes": [{k: plus[i][k] for k in
                         ["low_min", "low_max", "hard_min", "hard_max", "hard_count", "soft_count"]}
                                            for i in range(3)], "parity_error": parity_error})
    return rows


@lru_cache(maxsize=1)
def matching():
    rows = [path(eta) for eta in a.ETAS]
    reference = rows[0]
    neutral = a.representative(1.)
    ru, rd = np.dot(neutral[:4], neutral[:4])/2, np.dot(neutral[4:], neutral[4:])/2
    fits = []
    for eta, sequence in zip(a.ETAS[1:], rows[1:]):
        potential, gradient = [], []
        for row, ref in zip(sequence, reference):
            t = row["step"]
            potential.append((row["hard_potential_parts"]-ref["hard_potential_parts"])/(t**4*ru*rd*eta))
            gradient.append((row["hard_radial_gradient_parts"]-ref["hard_radial_gradient_parts"])
                            /(4*t**3*ru*rd*eta))
        pf, gf = extrapolate(potential, QUARTIC_TOL), extrapolate(gradient, QUARTIC_TOL)
        comparison = b.maxabs(pf["value"]-gf["value"])
        assert comparison < QUARTIC_TOL
        fits.append({"eta": eta, "potential_fit": pf, "gradient_fit": gf,
                     "method_discrepancy": comparison})
    value = fits[-1]["gradient_fit"]["value"]
    orientation_error = max(b.maxabs(row["gradient_fit"]["value"]-value) for row in fits)
    assert orientation_error < QUARTIC_TOL
    return {"rU_rD": [ru, rd], "hard_cB_parts_scalar_Weyl_vector": value,
            "hard_cB_total": float(sum(value)), "all_orientation_fits": fits,
            "orientation_agreement": orientation_error, "raw_paths": rows}


@lru_cache(maxsize=1)
def fierz():
    data = a.symbolic()
    bilinears = [[sp.expand((field.H*block[k]*field)[0]/sp.sqrt(3)) for k in range(3)]
                 for field, block in zip([data["up"], data["down"]], a.representation()["blocks"])]
    ru, rd = data["rho"]
    actual = [sum(z*z for z in bilinears[0]), sum(z*z for z in bilinears[1]),
              sum(u*d for u, d in zip(*bilinears))]
    expected = [ru**2/12, rd**2/12, (ru*rd-2*data["B2"])/12]
    residuals = [sp.expand(left-right) for left, right in zip(actual, expected)]
    assert residuals == [0, 0, 0]
    return list(map(str, residuals))


def bilinears(x):
    lg = b.light_geometry()
    up, down = h.fields(a.embed(x))[3:]
    matrices_t = [h.fields(t)[2] for t in lg["L"][:, 8:11].T]
    return np.array([[np.vdot(field, mt@field).real for field in [up, down]] for mt in matrices_t])


@lru_cache(maxsize=1)
def triplet():
    lg = b.light_geometry()
    rows, design, targets, normals = [], [], [], []
    for eta in a.ETAS:
        x = a.representative(eta)
        source = [r["hard_triplet_source_parts"] for r in path(eta)]
        fit = extrapolate(np.array(source).reshape(len(STEPS), -1), SOURCE_TOL)
        parts = fit["value"].reshape(3, 3)
        normal = normal_cubic(x, lg["L"][:, 8:11])
        total = parts.sum(axis=0)+normal
        shape = bilinears(x)
        design.append(shape)
        targets.append(total)
        normals.append(normal)
        rows.append({"eta": eta, "hard_source_parts": parts, "normal_source": normal,
                     "total_source": total, "fit": fit, "bilinears": shape})
    # Endpoints determine the two coefficients; five other angles are holdouts.
    training = np.vstack([design[0], design[-1]])
    response = np.concatenate([targets[0], targets[-1]])
    coefficients, _, rank, _ = np.linalg.lstsq(training, response, rcond=None)
    assert rank == 2
    error = max(b.maxabs(m@coefficients-t) for m, t in zip(design, targets))
    assert error < SOURCE_TOL
    nc = np.linalg.lstsq(training, np.concatenate([normals[0], normals[-1]]), rcond=None)[0]
    hc = coefficients-nc
    ru, rd = matching()["rU_rD"]
    stiffness = inputs()[1][1]+.02*(ru+rd)/6
    assert stiffness > 0
    actual_hessian = a.soft_masses(a.representative(1.))[0]
    assert np.min(abs(actual_hessian-stiffness)) < 1e-10
    for row in rows:
        current = row["total_source"]
        row["triplet_over_epsilon"] = -current/stiffness
        row["relaxation_energy_over_epsilon4"] = -float(current@current)/(2*stiffness)
        row["stationarity_residual"] = b.maxabs(stiffness*row["triplet_over_epsilon"]+current)
        assert row["stationarity_residual"] < 1e-12
    cb = float(coefficients[0]*coefficients[1]/(6*stiffness))
    endpoint_cb = (rows[-1]["relaxation_energy_over_epsilon4"]
                   -rows[0]["relaxation_energy_over_epsilon4"])/(ru*rd)
    assert abs(cb-endpoint_cb) < 1e-9
    return {"all_field_Fierz_residuals": fierz(), "fU_fD": coefficients,
            "normal_fU_fD": nc, "hard_fU_fD": hc, "source_shape_error": error,
            "stiffness": stiffness, "relaxation_cB": cb, "endpoint_cB": endpoint_cb,
            "omit_normal_control_cB": float(hc[0]*hc[1]/(6*stiffness)),
            "omit_hard_control_cB": float(nc[0]*nc[1]/(6*stiffness)), "angles": rows}


def octet_control():
    lg, base, geo = b.light_geometry(), h.base(), h.geometry()
    x, t = a.representative(1.), .04
    r = a.embed(x)
    dr = h.derivatives(r)
    source = np.zeros(8)
    for k, octet in enumerate(lg["L"][:, :8].T):
        do = h.derivatives(octet)
        mixed = mixed_mass_derivative(r, octet, dr, do)
        for i in range(3):
            mass = base["masses"][i]+t*dr[i][0]+t*t*dr[i][1]/2
            derivative = do[i][0]+t*mixed[i]
            source[k] += SPIN[i]*hard_trace(mass, COUNTS[i], CONSTANTS[i], [derivative])["gradient"][0]/t**2
    normal = normal_cubic(x, lg["L"][:, :8])
    assert max(b.maxabs(source), b.maxabs(normal)) < 2e-8
    return {"hard_source": source, "normal_source": normal}


def combined():
    match, relax = matching(), triplet()
    ru, rd = match["rU_rD"]
    cb = match["hard_cB_total"]+relax["relaxation_cB"]
    log_coefficient = float(a.symbolic()["fixed_coefficient"])/(64*np.pi**2)
    ref = a.soft_masses(a.representative(0.))
    rows = []
    for eta in a.ETAS:
        masses = a.soft_masses(a.representative(eta))
        finite_soft = sum(SPIN[i]*(q.log_sum(masses[i], CONSTANTS[i])-q.log_sum(ref[i], CONSTANTS[i]))
                          for i in range(3))
        scalar_difference = q.log_sum(masses[0], CONSTANTS[0])-q.log_sum(ref[0], CONSTANTS[0])
        assert abs(scalar_difference) < 1e-12
        for epsilon in a.EPSILONS:
            logarithm = log_coefficient*ru*rd*eta*np.log(epsilon)
            hard = match["hard_cB_total"]*ru*rd*eta
            response = relax["relaxation_cB"]*ru*rd*eta
            rows.append({"epsilon": epsilon, "eta": eta, "logarithm": logarithm,
                         "finite_soft": finite_soft, "finite_hard": hard, "triplet_relaxation": response,
                         "sum_over_epsilon4": logarithm+finite_soft+hard+response})
    return {"hard_plus_relaxation_cB": cb, "angle_samples": rows,
            "scope": "named finite pieces plus R9 soft determinant; a sampled truncated curve, not a full finite-epsilon vacuum certificate"}


@lru_cache(maxsize=1)
def analyze():
    controls = instrument_controls()
    return b.native({"inputs_sha256": PINS, "instrument_controls": controls,
                     "geometry_controls": geometry_controls(), "hard_matching": matching(),
                     "triplet_relaxation": triplet(), "octet_control": octet_control(),
                     "combined": combined(), "renormalization_boundary":
                     "Landau-gauge MS-bar at mu=sqrt(epsilon); renormalized R7 potential, other allowed operators zero at that scale; chosen, not derived"})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    start = time.monotonic()
    result = {**analyze(), "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "elapsed_seconds": time.monotonic()-start}
    payload = json.dumps(result, indent=2, allow_nan=False)+"\n"
    with args.output.open("x", encoding="utf-8") as handle:
        handle.write(payload)
    print(json.dumps({"hard_cB_parts": result["hard_matching"]["hard_cB_parts_scalar_Weyl_vector"],
                      "triplet_fU_fD": result["triplet_relaxation"]["fU_fD"],
                      "triplet_cB": result["triplet_relaxation"]["relaxation_cB"],
                      "neutral_differences": [r for r in result["combined"]["angle_samples"] if r["eta"] == 1.],
                      "elapsed_seconds": result["elapsed_seconds"]}, indent=2, allow_nan=False))


if __name__ == "__main__":
    main()
