"""R9: exact light invariant basis and leading infrared alignment logarithm."""
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

from . import broken_vacuum as b
from . import higgs_sector as h
from . import quantum_vacuum as q
from . import vacuum as v

HERE = Path(__file__).resolve().parent
PINS = {
    "broken_vacuum.py": "3f0c33f492b58b571e61de020c8fc292982e61db70eee57bc621ab554c59be0c",
    "broken_vacuum_first_run.json": "015c08ebd4165c57ec9bb9a41d8bdd6a67d59d4228577115e2a55efe73f87c7a",
    **b.PINS,
}
EPSILONS = (.01, .0025, 1e-4, 1e-8)
ETAS = (0., .1, .25, .5, .75, .9, 1.)
GW, GY, YUKAWA = .5, np.sqrt(.15), .25


@lru_cache(maxsize=1)
def inputs():
    for name, digest in PINS.items():
        assert hashlib.sha256((HERE/name).read_bytes()).hexdigest() == digest, name
    return json.loads((HERE/"broken_vacuum_first_run.json").read_text())


def strings(matrix):
    return [[str(item) for item in row] for row in matrix.tolist()]


@lru_cache(maxsize=1)
def representation():
    inputs()
    _, ids = h.light_basis()
    ts = v.representation()[4]
    raising = v.representation()[2][tuple(v.CARTAN[:, 5])]
    weak = [(raising+raising.T)/2, sp.I*(raising-raising.T)/2, ts[5]/2]
    hypercharge = v.embedding()[2]
    ew = weak+[hypercharge]
    metric = sp.Matrix(4, 4, lambda i, j: sp.trace(ew[i]*ew[j])/3)
    assert metric == sp.diag(1, 1, 1, sp.Rational(5, 3))
    blocks = [[t.extract(block, block) for t in ew] for block in ids]
    symbols = sp.symbols("j0:4")
    trial = sp.Matrix(2, 2, symbols)
    equations = sp.Matrix([term for left, right in zip(*blocks)
                           for term in left.T*trial+trial*right])
    null = equations.jacobian(symbols).nullspace()
    assert len(null) == 1
    intertwiner = sp.Matrix(2, 2, null[0])
    norm = sp.trace(intertwiner.H*intertwiner)/2
    intertwiner /= sp.sqrt(norm)
    assert intertwiner.H*intertwiner == sp.eye(2)
    for root in [2, 3]:
        e = v.representation()[2][tuple(v.CARTAN[:, root])]
        for index in sum(ids, []):
            assert e[:, index] == e.T[:, index] == sp.zeros(27, 1)
            assert ts[root][:, index] == sp.zeros(27, 1)
    old = v.contract(sum(v.embedding()[:2], sp.zeros(27, 1)))
    raw = sp.Matrix.hstack(*old.nullspace())
    gram = raw.H*raw
    assert gram.is_diagonal() and gram.shape == (17, 17)
    kernel = raw*sp.diag(*(1/sp.sqrt(gram[i, i]) for i in range(17)))
    assert kernel.H*kernel == sp.eye(17) and old*kernel == sp.zeros(27, 17)
    return {"ids": ids, "ew": ew, "blocks": blocks, "J": intertwiner,
            "K": kernel, "metric": metric, "raising": raising}


@lru_cache(maxsize=1)
def symbolic():
    data = representation()
    x = sp.symbols("x0:8", real=True)
    gw, gy, y = sp.symbols("gW gY y", real=True)
    up = sp.Matrix([(x[0]+sp.I*x[1])/sp.sqrt(2), (x[2]+sp.I*x[3])/sp.sqrt(2)])
    down = sp.Matrix([(x[4]+sp.I*x[5])/sp.sqrt(2), (x[6]+sp.I*x[7])/sp.sqrt(2)])
    rho_u, rho_d = [sp.expand((field.H*field)[0]) for field in [up, down]]
    invariant = sp.expand((up.T*data["J"]*down)[0])
    norm_b = sp.expand(invariant*sp.conjugate(invariant))
    p = sp.Matrix(4, 4, lambda i, j: sp.expand(sum(
        (field.H*(block[i]*block[j]+block[j]*block[i])*field)[0]
        for field, block in zip([up, down], data["blocks"]))))
    couplings = sp.diag(gw, gw, gw, gy)
    vm = couplings*p*couplings
    full = sp.zeros(27, 1)
    for field, block in zip([up, down], data["ids"]):
        for i, index in enumerate(block):
            full[index] += field[i]
    fm = y*data["K"].T*v.contract(full)*data["K"]
    fsq = (fm.H*fm).applyfunc(sp.expand)
    vf = sp.expand(sp.trace(vm*vm))
    ff = sp.expand(sp.trace(fsq*fsq))
    expected_v = ((3*gw**4+gy**4)*(rho_u+rho_d)**2/4
                  +gw**2*gy**2*((rho_u-rho_d)**2+4*norm_b)/2)
    expected_f = y**4*(8*rho_u**2+2*rho_d**2+8*rho_u*rho_d-8*norm_b)
    assert sp.expand(vf-expected_v) == 0
    assert sp.expand(ff-expected_f) == 0
    au, ad = sp.symbols("aU aD", real=True, nonzero=True)
    neutral = dict.fromkeys(x, 0)
    neutral.update({x[0]: sp.sqrt(2)*au, x[6]: sp.sqrt(2)*ad})
    charged = dict.fromkeys(x, 0)
    charged.update({x[0]: sp.sqrt(2)*au, x[4]: sp.sqrt(2)*ad})
    def orientation_coefficient(expression):
        return sp.cancel((expression.subs(neutral)-expression.subs(charged))/(au**2*ad**2))
    coefficient = orientation_coefficient(3*vf-2*ff)
    wrong_sign = orientation_coefficient(3*vf+2*ff)
    assert sp.expand(coefficient-(6*gw**2*gy**2+16*y**4)) == 0
    actual = sp.expand(3*vf-2*ff-coefficient*norm_b)
    radial = sp.expand(3*expected_v-2*expected_f-coefficient*norm_b)
    assert actual == radial
    fixed = sp.simplify(coefficient.subs({gw: sp.Rational(1, 2),
                                        gy: sp.sqrt(sp.Rational(3, 20)), y: sp.Rational(1, 4)}))
    assert fixed == sp.Rational(23, 80)
    penalty = sp.expand(rho_u*rho_d-norm_b)
    return {"x": x, "couplings": (gw, gy, y), "up": up, "down": down,
            "rho": (rho_u, rho_d), "B": invariant, "B2": norm_b, "penalty": penalty,
            "vector_matrix": vm, "fermion_matrix": fm, "coefficient": coefficient,
            "wrong_sign_coefficient": wrong_sign,
            "fixed_coefficient": fixed,
            "report": {"vector_fourth_trace_remainder": "0", "fermion_fourth_trace_remainder": "0",
                       "all_real_Higgs_variables": 8, "quartic_monomials_covered": 330,
                       "J": strings(data["J"]), "EW_kinetic_metric": strings(data["metric"]),
                       "B": str(invariant), "vector_fourth_trace": str(expected_v),
                       "fermion_fourth_trace": str(expected_f),
                       "supertrace_B2_coefficient": str(coefficient), "fixed_coefficient": str(fixed),
                       "vector_matrix": strings(vm), "projected_fermion_matrix": strings(fm)}}


@lru_cache(maxsize=1)
def invariant_basis():
    data = representation()
    z = sp.symbols("z0:8")  # U,D and their independent conjugates.
    ru, rd = z[0]*z[4]+z[1]*z[5], z[2]*z[6]+z[3]*z[7]
    ub, db = sp.Matrix(z[:2]), sp.Matrix(z[2:4])
    cb = sp.Matrix(z[4:6]).T*sp.conjugate(data["J"])*sp.Matrix(z[6:])
    bb = sp.expand((ub.T*data["J"]*db)[0]*cb[0])
    expected = {1: [], 2: [ru, rd], 3: [], 4: [ru**2, rd**2, ru*rd, bb]}
    generators = []
    for k in [2, 3]:
        left, right = data["blocks"][0][k], data["blocks"][1][k]
        generators.append(sp.diag(left, right, -left.T, -right.T))
    charges = [-sp.Rational(18, 5)]*2+[-sp.Rational(12, 5)]*2
    generators.append(sp.diag(*(charges+[-charge for charge in charges])))
    root = data["raising"]
    for matrix in [root, root.T]:
        left, right = [matrix.extract(ids, ids) for ids in data["ids"]]
        generators.append(sp.diag(left, right, -left.T, -right.T))
    rows = []
    for degree in range(1, 5):
        monomials = list(itertools.combinations_with_replacement(range(8), degree))
        candidates = [indices for indices in monomials if all(
            sum(generator[i, i] for i in indices) == 0 for generator in generators[:3])]
        equations = defaultdict(lambda: [sp.S.Zero]*len(candidates))
        for col, indices in enumerate(candidates):
            for gi, generator in enumerate(generators[3:]):
                for slot, i in enumerate(indices):
                    for j in range(8):
                        if generator[i, j]:
                            key = (gi, tuple(sorted(indices[:slot]+(j,)+indices[slot+1:])))
                            equations[key][col] += generator[i, j]
        matrix = sp.Matrix(list(equations.values())) if equations else sp.zeros(0, len(candidates))
        nullity = len(candidates)-matrix.rank()
        polynomial_basis = [sp.Poly(sp.expand(item), z) for item in expected[degree]]
        coefficients = sp.Matrix(len(candidates), len(polynomial_basis), lambda i, j:
                                 polynomial_basis[j].coeff_monomial(sp.prod(z[k] for k in candidates[i])))
        assert coefficients.rank() == nullity == len(expected[degree])
        assert matrix*coefficients == sp.zeros(matrix.rows, coefficients.cols)
        rows.append({"degree": degree, "all_monomials": len(monomials),
                     "weight_zero_candidates": len(candidates), "invariant_dimension": nullity,
                     "basis": list(map(str, expected[degree]))})
    return rows


@lru_cache(maxsize=1)
def instruments():
    data = symbolic()
    variables = (*data["x"], *data["couplings"])
    return {"vector": sp.lambdify(variables, data["vector_matrix"], "numpy"),
            "fermion": sp.lambdify(variables, data["fermion_matrix"], "numpy"),
            "penalty_hessian": sp.lambdify(data["x"], sp.hessian(data["penalty"], data["x"]), "numpy")}


def embed(x):
    return h.light_basis()[0]@np.asarray(x, float)


def soft_masses(x):
    inst = instruments()
    vector = np.asarray(inst["vector"](*x, GW, GY, YUKAWA), complex)
    fermion = np.asarray(inst["fermion"](*x, GW, GY, YUKAWA), complex)
    ve = np.linalg.eigvalsh(vector)
    if ve.min() < -1e-12:
        raise ValueError("negative soft vector squared mass")
    # Retain all positive values, discard only diagnosed negative roundoff.
    ve = np.maximum(ve, 0.)
    fe = np.linalg.svd(fermion, compute_uv=False)**2
    kappas = inputs()["quantum"]["masses_O_T_U_D"]
    light = np.concatenate((np.zeros(11), x))
    matrix = np.diag([kappas[0]]*8+[kappas[1]]*3+[kappas[2]]*4+[kappas[3]]*4)
    scalar_hessian = matrix+b.quartic_derivatives(light)[2]
    se = np.linalg.eigvalsh(scalar_hessian)
    if se.min() < -1e-10:
        raise ValueError("negative resummed scalar squared mass")
    se = np.maximum(se, 0.)
    return se, fe, np.concatenate((np.zeros(8), ve))


def representative(eta):
    if not 0 <= eta <= 1:
        raise ValueError("eta must be in [0,1]")
    ku, kd = inputs()["quantum"]["masses_O_T_U_D"][2:]
    x = np.zeros(8)
    x[0] = np.sqrt(-ku/.2)
    x[4] = np.sqrt(-kd/.2)*np.sqrt(1-eta)
    x[6] = np.sqrt(-kd/.2)*np.sqrt(eta)
    return x


def matrix_controls():
    data, inst, geo = representation(), instruments(), h.geometry()
    rng = np.random.default_rng(2026090691)
    ewcoords = np.zeros((78, 4))
    ewcoords[:6, 2] = np.eye(6)[:, 5]/2
    ewcoords[:6, 3] = geo["yh"]
    for i in [0, 1]:
        ewcoords[:, i] = np.linalg.solve(geo["gram"], np.einsum(
            "aij,ji->a", geo["T"], np.array(data["ew"][i], complex)).real)
    scale = np.diag([GW]*3+[GY])
    kernel = np.array(data["K"], complex)
    errors = []
    for _ in range(4):
        x = rng.normal(size=8)/3
        z = embed(x)
        orbit = h.orbit(z)@ewcoords
        actual_v = scale@orbit.T@geo["ks"]@orbit@scale
        actual_f = kernel.T@h.fermion_mass(z)@kernel
        predicted_v = inst["vector"](*x, GW, GY, YUKAWA)
        predicted_f = inst["fermion"](*x, GW, GY, YUKAWA)
        error = [b.maxabs(actual_v-predicted_v), b.maxabs(actual_f-predicted_f)]
        assert max(error) < 1e-10
        errors.append(error)
    # Original full action's Q must annihilate only the neutral representative.
    qcoeff = ewcoords[:, 2]+ewcoords[:, 3]
    action = [float(np.linalg.norm(h.orbit(embed(representative(eta)))@qcoeff)) for eta in [0., 1.]]
    assert action[0] > .1 and action[1] < 1e-10
    return {"generic_complex_vector_fermion_errors": errors, "Q_action_charged_neutral": action}


def scalar_and_angular_controls():
    data = symbolic()
    x = data["x"]
    k, lam = sp.symbols("k lam", real=True)
    u = sp.Matrix(x[:4])
    norm = (u.T*u)[0]
    matrix = (k+lam*norm)*sp.eye(4)+2*lam*u*u.T
    assert sp.expand(sp.trace(matrix*matrix)-(4*k*k+12*k*lam*norm+12*lam*lam*norm**2)) == 0
    reference = soft_masses(representative(1.))[0]
    errors = []
    for eta in ETAS:
        eigenvalues = soft_masses(representative(eta))[0]
        error = b.maxabs(eigenvalues-reference)
        assert error < 1e-9
        errors.append(error)
    neutral = representative(1.)
    penalty_hessian = np.asarray(instruments()["penalty_hessian"](*neutral), float)
    rho_sum = float(neutral@neutral/2)
    expected = np.array([0.]*6+[rho_sum]*2)
    assert b.maxabs(np.linalg.eigvalsh(penalty_hessian)-expected) < 1e-10
    # Penalty and its gradient vanish at neutral, so the constrained Hessian
    # equals this ambient extension; radial multiplier contribution is zero.
    sm = np.array(v.sm_generator_coordinates(), float)
    light = h.light_basis()[0]
    gauge = light.T@h.geometry()["ks"]@h.orbit(embed(neutral))@sm
    assert b.maxabs(penalty_hessian@gauge) < 1e-10
    phase = np.zeros(8)
    for start, charge in [(0, -18/5), (4, -12/5)]:
        phase[start+1:start+4:2] = charge*neutral[start:start+3:2]
    assert b.maxabs(penalty_hessian@phase) < 1e-10
    return {"radial_fourth_trace_identity_remainder": "0", "scalar_orientation_errors": errors,
            "resummed_scalar_squared_masses_all_19": reference,
            "neutral_penalty_Hessian": penalty_hessian,
            "penalty_Hessian_eigenvalues": np.linalg.eigvalsh(penalty_hessian),
            "charged_pair_eigenvalue": rho_sum, "phase_Hessian_residual": b.maxabs(penalty_hessian@phase)}


def log_potential(masses, epsilon):
    if epsilon <= 0:
        raise ValueError("positive epsilon required")
    parts = [weight*q.log_sum(epsilon**2*values, constant, np.sqrt(epsilon))/(64*np.pi**2)
             for weight, values, constant in zip([1., -2., 3.], masses, [1.5, 1.5, 5/6])]
    return np.array(parts)


def alignment():
    ku, kd = inputs()["quantum"]["masses_O_T_U_D"][2:]
    rho = np.array([-ku/.4, -kd/.4])
    c0 = float(symbolic()["fixed_coefficient"])/(64*np.pi**2)
    coefficient = c0*float(np.prod(rho))
    base = soft_masses(representative(0.))
    rows = []
    for eta in ETAS:
        masses = soft_masses(representative(eta))
        runs = []
        for epsilon in EPSILONS:
            parts = log_potential(masses, epsilon)-log_potential(base, epsilon)
            normalized = float(parts.sum()/epsilon**4)
            logarithm = coefficient*eta*np.log(epsilon)
            runs.append({"epsilon": epsilon, "parts_scalar_Weyl_vector": parts,
                         "difference_over_epsilon4": normalized,
                         "logarithmic_part_over_epsilon4": logarithm,
                         "finite_soft_part_over_epsilon4": normalized-logarithm})
        constants = [row["finite_soft_part_over_epsilon4"] for row in runs]
        assert max(constants)-min(constants) < 1e-12
        slope = ((runs[-1]["difference_over_epsilon4"]-runs[0]["difference_over_epsilon4"])
                 /np.log(EPSILONS[-1]/EPSILONS[0]))
        assert abs(slope-coefficient*eta) < 1e-12
        rows.append({"eta": eta, "squared_masses_scalar_Weyl_vector": masses,
                     "runs": runs, "log_slope_error": abs(slope-coefficient*eta)})
    sensitivity = []
    for epsilon in EPSILONS[:2]:
        signs = [c0*np.log(epsilon)+counterterm for counterterm in [-.01, .01]]
        assert signs[0] < 0 < signs[1]
        sensitivity.append({"epsilon": epsilon, "hard_cB_controls": [-.01, .01],
                            "total_B2_coefficients_over_epsilon2": signs})
    gw, gy, y = symbolic()["couplings"]
    proper = symbolic()["coefficient"].subs({gw: 0, gy: 0, y: 1})
    wrong = symbolic()["wrong_sign_coefficient"].subs({gw: 0, gy: 0, y: 1})
    assert proper > 0 and wrong < 0
    return {"rhoU_rhoD_over_epsilon": rho, "B2_log_coefficient": c0,
            "neutral_minus_charged_log_coefficient": coefficient,
            "charged_pair_mass_squared_over_minus_epsilon3_log_epsilon": c0*sum(rho),
            "all_orientation_runs": rows, "finite_hard_counterterm_sensitivity": sensitivity,
            "wrong_Weyl_sign_control": {"correct_pure_Yukawa_coefficient": str(proper),
                                         "wrong_coefficient": str(wrong)},
            "full_finite_matching_computed": False,
            "finite_epsilon_vacuum_selection_claimed": False,
            "scope": "leading soft logarithm; asymptotic neutral preference conditional on fixed hard branch and bounded matching coefficients"}


@lru_cache(maxsize=1)
def analyze():
    result = {"inputs_sha256": PINS, "exact": symbolic()["report"],
              "complete_light_Higgs_invariant_basis": invariant_basis(),
              "independent_matrix_controls": matrix_controls(),
              "scalar_and_angular_controls": scalar_and_angular_controls(),
              "alignment": alignment()}
    return b.native(result)


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
    print(json.dumps({"invariant_dimensions": [r["invariant_dimension"] for r in result["complete_light_Higgs_invariant_basis"]],
                      "exact_coefficient": result["exact"]["fixed_coefficient"],
                      "alignment": {key: value for key, value in result["alignment"].items() if key != "all_orientation_runs"},
                      "elapsed_seconds": result["elapsed_seconds"]}, indent=2))


if __name__ == "__main__":
    main()
