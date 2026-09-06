"""R8: all-light-field leading EFT and actual broken-phase spectra of R7."""
import argparse
from collections import defaultdict
from functools import lru_cache
import hashlib
import itertools
import json
from pathlib import Path
import time

import numpy as np
import sympy as sp

from . import higgs_sector as h
from . import quantum_vacuum as q
from . import vacuum as v

HERE = Path(__file__).resolve().parent
PINS = {
    "vacuum.py": "4be56d6b20eeeb4826590c4b5b38f82eaf7603ab1c2688d8fdc06a83540000f0",
    "quantum_vacuum.py": "aabef052bb69613a51ee768d53b7dc07062dc005011379f6c1b96b1a68309457",
    "quantum_shift.py": "94c4399491dfa5bcb702b7b2b75eba00cce6ca9f94be5fe96c487e46053bd5bc",
    "higgs_sector.py": "29a85c5ed38ba34bd6c9e2901595f1e844f5c45dfa46e6aefbe2b3100c6f0556",
    "higgs_rerun_1.json": "5a507a4cfb5898ac049ed418e7837a164d45501ec572093520a31da8af11a3bd",
}
EPSILONS = (.01, .0025)
SPIN = np.array([1., -2., 3.])/(64*np.pi**2)


def maxabs(array):
    return float(np.max(np.abs(array)))


def native(value):
    if isinstance(value, np.generic):
        return native(value.item())
    if isinstance(value, np.ndarray):
        return native(value.tolist())
    if isinstance(value, dict):
        return {native(key): native(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [native(item) for item in value]
    if value is None or isinstance(value, (str, bool, int, float)):
        return value
    raise TypeError(f"Unsupported result type: {type(value).__name__}")


@lru_cache(maxsize=1)
def inputs():
    for name, digest in PINS.items():
        assert hashlib.sha256((HERE/name).read_bytes()).hexdigest() == digest, name
    return json.loads((HERE/"higgs_rerun_1.json").read_text())


@lru_cache(maxsize=1)
def light_geometry():
    inputs()
    geo, base = h.geometry(), h.base()
    higgs, ids = h.light_basis()
    blocks = []
    index_blocks = []
    for cartans, support in [([2, 3], {2, 3}), ([5], {5})]:
        indices = list(cartans)
        for k, (coefficients, _, _) in enumerate(v.representation()[3]):
            active = {i for i, coefficient in enumerate(coefficients) if coefficient}
            if active and active <= support:
                indices += [6+2*k, 7+2*k]
        raw = np.eye(78)[:, indices]
        raw = raw@q.invsqrt_positive(raw.T@geo["gram"]@raw)
        light = np.zeros((294, len(indices)))
        light[108:186] = raw
        blocks.append(light)
        index_blocks.append(indices)
    assert [block.shape[1] for block in blocks] == [8, 3]
    light = np.column_stack((*blocks, higgs))
    sm = np.array(v.sm_generator_coordinates(), float)
    sm_c = sm@q.invsqrt_positive(sm.T@geo["kg"]@sm)
    errors = {"orthonormality": maxabs(light.T@geo["ks"]@light-np.eye(19)),
              "tree_kernel": maxabs(base["j"]@light),
              "gauge_orthogonality": maxabs(base["go"].T@geo["ks"]@light)}
    orbits = [h.orbit(direction)@sm for direction in light.T]
    generators = []
    for k in range(12):
        action = np.column_stack([orbit[:, k] for orbit in orbits])
        generator = light.T@geo["ks"]@action
        errors[f"SM_closure_{k}"] = maxabs(action-light@generator)
        assert maxabs(generator+generator.T) < 1e-10
        generators.append(generator)
    assert max(errors.values()) < 1e-9
    eigenvalues, modes = np.linalg.eigh(base["masses"][0])
    positive = eigenvalues > 1e-9
    assert np.count_nonzero(positive) == 209
    assert np.linalg.matrix_rank(base["go"], tol=1e-9) == 66
    assert 294-209-66 == light.shape[1]
    return {"L": light, "sm": sm, "sm_c": sm_c, "generators": generators,
            "positive_ev": eigenvalues[positive], "positive_modes": modes[:, positive],
            "ids": ids, "generator_indices_O_T": index_blocks, "errors": errors}


def exact_weak_identity():
    t = v.representation()[4]
    raising = v.representation()[2][tuple(v.CARTAN[:, 5])]
    weak = [(raising+raising.T)/2, sp.I*(raising-raising.T)/2, t[5]/2]
    variables = sp.symbols("T1:4", real=True)
    matrix = sum((a*b for a, b in zip(variables, weak)), sp.zeros(27))/sp.sqrt(3)
    for index_set in light_geometry()["ids"]:
        block = matrix.extract(index_set, index_set)
        assert sp.simplify(block*block-sum(x*x for x in variables)*sp.eye(2)/12) == sp.zeros(2)
    traces = [sp.trace(g*g) for g in weak]
    assert traces == [3, 3, 3]
    return {"Tr27_t_squared": list(map(str, traces)), "both_doublet_square_remainders": ["0", "0"],
            "canonical_square_coefficient": "1/12"}


@lru_cache(maxsize=1)
def quartic():
    lg, geo, base = light_geometry(), h.geometry(), h.base()
    light, j, weights = lg["L"], base["j"], base["w"]
    pairs = list(itertools.combinations_with_replacement(range(19), 2))
    changes = [h.jacobian(geo["z"]+r)-j for r in light.T]
    c2 = np.column_stack([changes[i]@light[:, k]/(2 if i == k else 1) for i, k in pairs])
    rhs = 2*geo["si"]@j.T@(weights[:, None]*c2)
    modes, ev = lg["positive_modes"], lg["positive_ev"]
    response = -geo["si"]@modes@((modes.T@rhs)/ev[:, None])
    analytic_response = np.zeros_like(response)
    for p, (i, k) in enumerate(pairs):
        if i == k and i < 11:
            analytic_response[108:114, p] = -geo["yh"]/10
    residual = c2+j@response
    gram = residual.T@(weights[:, None]*residual)
    error_response = maxabs(response-analytic_response)
    error_stationarity = maxabs(base["h0"]@response+2*j.T@(weights[:, None]*c2))
    assert max(error_response, error_stationarity) < 1e-9
    polynomial = defaultdict(float)
    for a, pair_a in enumerate(pairs):
        for b, pair_b in enumerate(pairs):
            polynomial[tuple(sorted(pair_a+pair_b))] += gram[a, b]
    expected = defaultdict(float)
    for block in [range(11, 15), range(15, 19)]:
        for i in block:
            for k in block:
                expected[tuple(sorted((i, i, k, k)))] += .2/4
    for i in range(8, 11):
        for k in range(11, 19):
            expected[(i, i, k, k)] += .02/24
    coefficient_error = max(abs(polynomial[key]-expected[key]) for key in set(polynomial)|set(expected))
    assert coefficient_error < 1e-9
    omitted = c2[:, pairs.index((0, 0))]
    bare_octet = float(omitted@(weights*omitted))
    effective_octet = float(gram[pairs.index((0, 0)), pairs.index((0, 0))])
    assert abs(bare_octet-.2) < 1e-10 and abs(effective_octet) < 1e-16
    rng = np.random.default_rng(202609068)
    direction = rng.normal(size=19)
    direction /= np.linalg.norm(direction)
    p = np.array([direction[i]*direction[k] for i, k in pairs])
    predicted = float(p@gram@p)
    path = []
    for step in [.04, .02, .01, .005]:
        constraints = h.constraints(geo["z"]+step*light@direction+step**2*response@p)
        value = float(constraints@(weights*constraints)/step**4)
        path.append({"step": step, "V_over_step4": value, "error": abs(value-predicted)})
    assert path[-1]["error"] < path[0]["error"]/4
    assert path[-1]["error"] < .01*predicted
    report = {"quadratic_monomial_count": len(pairs), "quartic_monomial_count_checked": len(polynomial),
              "maximum_coefficient_error": coefficient_error,
              "nonzero_quartic_coefficients": [{"indices": list(key), "coefficient": float(value)}
                                                for key, value in sorted(polynomial.items()) if abs(value) > 1e-12],
              "normal_response_error": error_response, "normal_stationarity_error": error_stationarity,
              "bare_vs_integrated_octet_quartic": [bare_octet, effective_octet],
              "finite_path_predicted_quartic": predicted, "finite_path": path,
              "exact_weak_identity": exact_weak_identity()}
    return {"pairs": pairs, "G": gram, "N": response, "report": report}


def quartic_derivatives(x):
    data = quartic()
    pairs = np.array(data["pairs"], int)
    i, j = pairs.T
    p = x[i]*x[j]
    dp = np.zeros((len(p), len(x)))
    np.add.at(dp, (np.arange(len(p)), i), x[j])
    np.add.at(dp, (np.arange(len(p)), j), x[i])
    gp = data["G"]@p
    gradient = 2*dp.T@gp
    hessian = 2*dp.T@data["G"]@dp
    for a, (i, j) in enumerate(pairs):
        hessian[i, j] += 2*gp[a]
        hessian[j, i] += 2*gp[a]
    return float(p@gp), gradient, hessian, p


@lru_cache(maxsize=1)
def quantum_data():
    lg, geo, base = light_geometry(), h.geometry(), h.base()
    row = next(r for r in h.quantum()["runs"] if r["mu"] == 1.)
    reference = next(r for r in inputs()["quantum"]["runs"] if r["mu"] == 1.)
    for key in ["gradient_parts_scalar_Weyl_vector", "normal_displacement", "Higgs_leading_curvature_matrix"]:
        assert maxabs(np.array(row[key])-np.array(reference[key])) < 1e-9
    m_o, m_t = [row["angular_curvatures"][key]["total"] for key in ["color_octet", "weak_triplet"]]
    higgs = np.array(row["Higgs_leading_curvature_matrix"])
    m_u, m_d = [float(np.trace(higgs[start:start+4, start:start+4])/4) for start in [0, 4]]
    expected = np.diag([m_o]*8+[m_t]*3+[m_u]*4+[m_d]*4)
    light = lg["L"]
    instruments = h.spectral(1.)
    def second(r):
        derivatives = h.derivatives(r)
        return sum(SPIN[a]*spec.second(*derivatives[a]) for a, spec in enumerate(instruments))
    diagonals = [second(r) for r in light.T]
    matrix = np.diag(diagonals)
    for i in range(19):
        for j in range(i):
            matrix[i, j] = matrix[j, i] = (second(light[:, i]+light[:, j])-diagonals[i]-diagonals[j])/2
    delta = np.array(row["normal_displacement"])
    canonical = np.linalg.solve(geo["si"], light)
    normal = canonical.T@h.derivatives(delta)[0][0]@canonical
    matrix += normal
    assert maxabs(matrix-expected) < 1e-9
    for generator in lg["generators"]:
        assert maxabs(matrix@generator-generator@matrix) < 1e-9
    scaled = []
    for epsilon in EPSILONS:
        scaled_instruments = [h.SpectralTrace(epsilon*mass, constant, np.sqrt(epsilon))
                              for mass, constant in zip(base["masses"], [1.5, 1.5, 5/6])]
        forces = np.zeros((3, 294))
        for k, direction in enumerate(np.eye(294)):
            derivatives = h.derivatives(direction)
            for a, spec in enumerate(scaled_instruments):
                forces[a, k] = SPIN[a]*spec.first(epsilon*derivatives[a][0])
        error = maxabs(forces/epsilon**2-np.array(row["gradient_parts_scalar_Weyl_vector"]))
        assert error < 1e-9
        scaled.append({"epsilon": epsilon, "gradient_parts": forces, "normalized_scaling_error": error})
    return {"matrix": matrix, "masses_O_T_U_D": [m_o, m_t, m_u, m_d], "delta": delta,
            "report": {"reference_mu": 1., "masses_O_T_U_D": [m_o, m_t, m_u, m_d],
                       "entire_19_curvature_matrix": matrix, "normal_contribution": normal,
                       "block_form_error": maxabs(matrix-expected), "fresh_scaled_forces": scaled}}


@lru_cache(maxsize=1)
def phase_data():
    weights, _, _, _, ts = v.representation()
    sv, nv = v.embedding()[:2]
    si = next(i for i in range(27) if sv[i])
    ni = next(i for i in range(27) if nv[i])
    equations = sp.Matrix.vstack(v.CARTAN[2:6, :], weights[si].T, weights[ni].T)
    coefficients = equations.inv()*sp.Matrix([0, 0, 0, 0, 2, 2])
    gc = sum((coefficients[i]*ts[i] for i in range(6)), sp.zeros(27))
    assert gc*sv == 2*sv and gc*nv == 2*nv
    charges = []
    for block in light_geometry()["ids"]:
        assert len({gc[i, i]-2 for i in block}) == 1
        charges.append(gc[block[0], block[0]]-2)
    anomaly = sp.simplify(sp.trace((sp.eye(27)+gc)*(ts[2]/2)**2))
    assert charges == [-sp.Rational(18, 5), -sp.Rational(12, 5)]
    assert anomaly == 3
    gauge = np.zeros(78)
    gauge[:6] = np.array(coefficients, float).ravel()
    assert maxabs(phase_tangent(h.geometry()["z"])+h.orbit(h.geometry()["z"])@gauge) < 1e-10
    rng = np.random.default_rng(202609069)
    z = h.geometry()["z"]+.03*rng.normal(size=294)
    changed = phase_rotate(z, .37)
    before, after = h.constraints(z), h.constraints(changed)
    potential_error = abs(float(before@(h.weights()*before)-after@(h.weights()*after)))
    yukawa_error = maxabs(h.fermion_mass(changed)-np.exp(-2j*.37)*h.fermion_mass(z))
    assert potential_error < 1e-10 and yukawa_error < 1e-12
    return {"gauge": gauge, "report": {"compensating_Cartan_coefficients": list(map(str, coefficients)),
            "residual_U_D_charges": list(map(str, charges)), "mixed_color_anomaly_trace": str(anomaly),
            "classical_potential_phase_error": potential_error, "Yukawa_phase_error": yukawa_error,
            "quantum_exact_Goldstone_claimed": False}}


def phase_rotate(z, angle):
    out = z.copy()
    for pos in [0, 54, 186, 240]:
        field = (z[pos:pos+27]+1j*z[pos+27:pos+54])*np.exp(-2j*angle)
        out[pos:pos+27], out[pos+27:pos+54] = field.real, field.imag
    return out


def phase_tangent(z):
    out = np.zeros(294)
    for pos in [0, 54, 186, 240]:
        field = -2j*(z[pos:pos+27]+1j*z[pos+27:pos+54])
        out[pos:pos+27], out[pos+27:pos+54] = field.real, field.imag
    return out


@lru_cache(maxsize=1)
def fermion_data():
    sv, nv, ym = v.embedding()[:3]
    old = v.contract(sv+nv)
    raw = sp.Matrix.hstack(*old.nullspace())
    gram = raw.H*raw
    assert gram.is_diagonal() and gram.shape == (17, 17)
    kernel = raw*sp.diag(*(1/sp.sqrt(gram[i, i]) for i in range(17)))
    assert kernel.H*kernel == sp.eye(17) and old*kernel == sp.zeros(27, 17)
    charge = ym+v.representation()[4][5]/2
    ids = light_geometry()["ids"]
    neutral = [next(i for i in block if charge[i, i] == 0) for block in ids]
    charged_d = next(i for i in ids[1] if i != neutral[1])
    controls = []
    for name, down in [("neutral", neutral[1]), ("charge_breaking", charged_d)]:
        hu, hd = sp.eye(27)[:, neutral[0]], sp.eye(27)[:, down]
        u, d = sp.symbols("u d")
        symbolic = sv+nv+u*hu+d*hd
        invariant = sp.expand(sum(c*symbolic[a]*symbolic[b]*symbolic[cidx]
                                  for (a, b, cidx), c in zip(v.cubic()[0], v.cubic()[1])))
        mass = v.contract(sv+nv+hu/10+hd/9)
        projected = kernel.T*v.contract(hu/10+hd/9)*kernel
        controls.append({"orientation": name, "U_D_weight_indices": [neutral[0], down],
                         "rational_control_full_rank": mass.rank(), "leading_projected_rank": projected.rank(),
                         "cubic_polynomial": str(invariant)})
    return {"K": np.array(kernel, float), "charge": np.array(charge, complex),
            "neutral": neutral, "charged_d": charged_d, "controls": controls}


def broken_state(epsilon, orientation):
    lg, geo, quantum = light_geometry(), h.geometry(), quantum_data()
    m_o, m_t, m_u, m_d = quantum["masses_O_T_U_D"]
    assert m_o > 0 and m_t > 0 and m_u < 0 and m_d < 0
    fermions = fermion_data()
    u_index = lg["ids"][0].index(fermions["neutral"][0])
    d_weight = fermions["neutral"][1] if orientation == "neutral" else fermions["charged_d"]
    d_index = lg["ids"][1].index(d_weight)
    x = np.zeros(19)
    x[11+2*u_index] = np.sqrt(-epsilon*m_u/.2)
    x[15+2*d_index] = np.sqrt(-epsilon*m_d/.2)
    fourth, grad4, hess4, p = quartic_derivatives(x)
    potential = epsilon**2*float(x@quantum["matrix"]@x)/2+epsilon*fourth
    gradient = epsilon**2*quantum["matrix"]@x+epsilon*grad4
    hessian = epsilon**2*quantum["matrix"]+epsilon*hess4
    gradient_error = maxabs(gradient)/epsilon**2.5
    assert gradient_error < 1e-9
    eigenvalues = np.linalg.eigvalsh(hessian)/epsilon**2
    assert np.count_nonzero(eigenvalues > 1e-9) == 13
    assert np.count_nonzero(np.abs(eigenvalues) < 1e-9) == 6
    z = geo["z"]+lg["L"]@x+epsilon*quantum["delta"]+quartic()["N"]@p
    orbit = h.orbit(z)
    canonical_orbit = np.linalg.solve(geo["si"], orbit)
    vectors, singular, _ = np.linalg.svd(canonical_orbit@geo["gi"], full_matrices=False)
    rank = int(np.count_nonzero(singular > 1e-10))
    full_m2 = np.sort(.25*epsilon*singular**2)
    projected_singular = np.linalg.svd(canonical_orbit@lg["sm_c"], compute_uv=False)
    projected_rank = int(np.count_nonzero(projected_singular > 1e-10))
    projected_m2 = np.sort(.25*epsilon*projected_singular**2)
    assert rank-66 == projected_rank
    color_error = maxabs(orbit@lg["L"][108:186, :8])
    qcoeff = np.zeros(78)
    qcoeff[:6] = geo["yh"]
    qcoeff[5] += .5
    electromagnetic_action = float(np.linalg.norm(orbit@qcoeff))
    assert color_error < 1e-9
    if orientation == "neutral":
        assert rank == 69 and electromagnetic_action < 1e-9
    else:
        assert rank == 70 and electromagnetic_action > 1e-6
    light_gauge_actions = lg["L"].T@geo["ks"]@orbit@lg["sm"]
    gauge_hessian_error = maxabs(hessian@light_gauge_actions)/epsilon**2.5
    assert gauge_hessian_error < 1e-9
    low_full = full_m2[78-rank:78-rank+projected_rank]
    low_projected = projected_m2[12-projected_rank:]
    vector_error = maxabs(low_full-low_projected)/float(max(low_projected))
    radii_squared = [float(np.dot(x[11:15], x[11:15])/2), float(np.dot(x[15:19], x[15:19])/2)]
    weak_predictions = None
    if orientation == "neutral":
        total = sum(radii_squared)
        weak_predictions = [.25*epsilon*total/2]*2+[.4*epsilon*total/2]
        assert maxabs(low_projected-np.array(weak_predictions))/epsilon**2 < 1e-9
    mass = np.sqrt(epsilon)*h.fermion_mass(z)
    projected_mass = fermions["K"].T@(np.sqrt(epsilon)*h.fermion_mass(lg["L"]@x))@fermions["K"]
    fermion_masses = np.linalg.svd(mass, compute_uv=False)
    projected_masses = np.linalg.svd(projected_mass, compute_uv=False)
    fermion_error = maxabs(fermion_masses[-17:]-projected_masses)/float(max(projected_masses))
    charge_error = maxabs(fermions["charge"].T@mass+mass@fermions["charge"])
    if orientation == "neutral":
        assert charge_error < 1e-9
    tangent = phase_tangent(z)+orbit@phase_data()["gauge"]
    canonical_tangent = np.linalg.solve(geo["si"], tangent)
    physical = canonical_tangent-vectors[:, :rank]@(vectors[:, :rank].T@canonical_tangent)
    phase_norm = float(np.linalg.norm(physical))
    light_tangent = lg["L"].T@geo["ks"]@tangent
    assert maxabs(hessian@light_tangent)/epsilon**2.5 < 1e-9
    if orientation == "neutral":
        assert phase_norm > 1e-6
    return {"epsilon": epsilon, "orientation": orientation, "light_coordinates": x,
            "complex_doublet_norms_squared": radii_squared, "leading_potential": potential,
            "normalized_gradient_error": gradient_error,
            "light_Hessian_over_epsilon_squared": hessian/epsilon**2,
            "light_mass_squared_over_epsilon_squared": eigenvalues,
            "positive_light_modes": 13, "angular_zero_modes": 6,
            "broken_EW_generators": projected_rank, "remaining_physical_leading_zero_modes": 6-projected_rank,
            "gauge_Hessian_error": gauge_hessian_error,
            "unbroken_gauge_dimension": 78-rank, "color_action_error": color_error,
            "electromagnetic_action_norm": electromagnetic_action,
            "vector_mass_squared_all_78": full_m2, "projected_SM_vector_mass_squared": projected_m2,
            "neutral_W_W_Z_leading_prediction": weak_predictions, "vector_projection_relative_error": vector_error,
            "fermion_singular_masses_all_27": fermion_masses,
            "fermion_leading_projection_all_17": projected_masses,
            "fermion_full_numerical_rank": int(np.count_nonzero(fermion_masses > 1e-11*max(fermion_masses))),
            "fermion_leading_projected_rank": int(np.count_nonzero(projected_masses > 1e-11*max(projected_masses))),
            "fermion_projection_relative_error": fermion_error, "Q_Yukawa_invariance_error": charge_error,
            "global_phase_physical_norm": phase_norm,
            "global_phase_physical_norm_over_sqrt_epsilon": phase_norm/np.sqrt(epsilon)}


@lru_cache(maxsize=1)
def analyze():
    lg = light_geometry()
    classical = quartic()["report"]
    quantum = quantum_data()["report"]
    phases = phase_data()["report"]
    fermions = fermion_data()["controls"]
    states = [broken_state(epsilon, orientation) for epsilon in EPSILONS
              for orientation in ["neutral", "charge_breaking"]]
    for epsilon in EPSILONS:
        pair = [row for row in states if row["epsilon"] == epsilon]
        assert abs(pair[0]["leading_potential"]-pair[1]["leading_potential"])/epsilon**3 < 1e-9
    for orientation in ["neutral", "charge_breaking"]:
        sequence = [row for row in states if row["orientation"] == orientation]
        for key in ["vector_projection_relative_error", "fermion_projection_relative_error"]:
            assert sequence[1][key] < sequence[0][key]+1e-12
    return native({"inputs_sha256": PINS,
                   "geometry": {"light_dimension": 19, "positive_tree_modes": 209, "gauge_directions": 66,
                                "Higgs_weight_indices": lg["ids"], "O_T_generator_indices": lg["generator_indices_O_T"],
                                "errors": lg["errors"]},
                   "quartic": classical, "quantum": quantum, "phase_symmetry": phases,
                   "exact_fermion_controls": fermions, "broken_states": states,
                   "scope": "leading EFT of the specified action and weak-coupling family; no EM selection, pole matching, physical families or TOE claimed"})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    start = time.monotonic()
    result = {**analyze(), "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "elapsed_seconds": time.monotonic()-start}
    payload = json.dumps(result, indent=2, allow_nan=False)+"\n"
    with args.output.open("x", encoding="utf-8") as handle:
        handle.write(payload)
    print(json.dumps({"quartic_max_error": result["quartic"]["maximum_coefficient_error"],
                      "masses_O_T_U_D": result["quantum"]["masses_O_T_U_D"],
                      "phase_symmetry": result["phase_symmetry"], "exact_fermion_controls": result["exact_fermion_controls"],
                      "states": [{key: row[key] for key in ["epsilon", "orientation", "unbroken_gauge_dimension",
                          "remaining_physical_leading_zero_modes", "fermion_full_numerical_rank", "fermion_leading_projected_rank",
                          "vector_projection_relative_error", "fermion_projection_relative_error", "global_phase_physical_norm"]}
                                 for row in result["broken_states"]], "elapsed_seconds": result["elapsed_seconds"]}, indent=2))


if __name__ == "__main__":
    main()
