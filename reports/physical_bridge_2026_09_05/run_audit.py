"""Reproduce the sealed audit without importing a script that overwrites its bank.

Run from the repository root:
  python3.12 -m reports.physical_bridge_2026_09_05.run_audit --output <new-path>
Output creation refuses to overwrite an existing file.
"""
import argparse
import ast
import copy
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path

import numpy as np
from scipy.optimize import minimize_scalar

from .gauge_running import (SM_B, boundary_down, boundary_up, evolve,
                            inverse_couplings, InvalidTrajectory, legacy_box,
                            piecewise_one_loop)
from .spectrum import (ONE_FAMILY, HIGGS, D_PAIR, L_PAIR, SINGLET, anomalies,
                       beta, matter_beta, threshold_requirement)

ROOT = Path(__file__).resolve().parents[2]
BANK = ROOT / "frontier/B915_the_crossing"
SOURCE_HASH = "00c55a31b1e00ffb278331526d81f7403ac558c943adf7566e7150ac5b90d01d"
RESULT_HASH = "893fb73f5e8524150a989e940ee747540a43c8b7806256fcbb1bc7bb3c4b9eed"


def legacy_functions():
    """Load precisely the original setup/definitions, stopping before its scan.

The AST prefix boundary is the assignment to MUs; no original output-writing
statement executes. The exact source hash protects this extraction contract.
"""
    source = (BANK / "crossing.py").read_bytes()
    if hashlib.sha256(source).hexdigest() != SOURCE_HASH:
        raise RuntimeError("legacy source changed; audit design must be revisited")
    tree = ast.parse(source)
    prefix = []
    found = False
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
                isinstance(target, ast.Name) and target.id == "MUs" for target in node.targets):
            found = True
            break
        prefix.append(node)
    if not found:
        raise RuntimeError("legacy prefix boundary was not found")
    namespace = {}
    exec(compile(ast.Module(body=prefix, type_ignores=[]), str(BANK / "crossing.py"), "exec"),
         namespace)
    return namespace, prefix


def vary_legacy_guess(namespace, prefix, strong):
    """Change only the literal 0.118 in the legacy curve's first equation."""
    node = copy.deepcopy(next(n for n in prefix
                              if isinstance(n, ast.FunctionDef) and n.name == "curve_point"))
    replacements = 0

    class Replace(ast.NodeTransformer):
        def visit_Constant(self, item):
            nonlocal replacements
            if isinstance(item.value, float) and item.value == .118:
                replacements += 1
                return ast.copy_location(ast.Constant(value=strong), item)
            return item

    node = Replace().visit(node)
    if replacements != 1:
        raise RuntimeError("expected exactly one legacy strong-coupling literal")
    scope = dict(namespace)
    exec(compile(ast.fix_missing_locations(ast.Module(body=[node], type_ignores=[])),
                 "<legacy-guess-sensitivity>", "exec"), scope)
    return scope["curve_point"]


def audit_boundary(fixture, old, prefix):
    inv = fixture["input"]["inv_alpha_em_MZ"]
    mz = old["MZ"]
    rows = []
    for mu, obs in zip(fixture["curve_samples"]["MU"], fixture["curve_samples"]["two_loop"]):
        if not np.isfinite(obs).all():
            continue
        t = math.log(mu / mz)
        original = old["curve_point"](mu, True)
        x = inverse_couplings(inv, *original)
        endpoint = evolve(x, 0, t)
        tight = evolve(x, 0, t, rtol=2e-13, atol=2e-14)
        corrected = boundary_down(t, inv)
        simultaneous = boundary_up(t, inv, guess=tuple(original))
        rows.append({"MU_GeV": mu, "legacy_observables": list(original),
                     "archive_difference": float(max(abs(np.array(obs) - original))),
                     "legacy_UV_residuals": list(np.diff(endpoint)),
                     "tighter_integrator_endpoint_difference": float(max(abs(tight-endpoint))),
                     "corrected_observables": list(corrected.observables),
                     "up_down_difference": float(max(abs(simultaneous-corrected.observables))),
                     "corrected_UV_residuals": list(np.diff(evolve(corrected.inverse_ir, 0, t)))})
    mu = fixture["curve_2loop_at_dmin"]["MU_GeV"]
    sensitivity = []
    for strong in (.09, .118, .15):
        fn = vary_legacy_guess(old, prefix, strong)
        obs = fn(mu)
        sensitivity.append({"legacy_fixed_strong_coupling": strong, "observables": list(obs),
                            "UV_residuals": list(np.diff(evolve(
                                inverse_couplings(inv, *obs), 0, math.log(mu/mz))))})
    control = []
    for t in (5., 15., 25., 30.):
        p = boundary_down(t, inv, 1)
        up = boundary_up(t, inv, loops=1, guess=(p.sin2theta, p.alpha_s))
        control.append(float(max(abs(up - p.observables))))
    return {"historical_valid_points": len(rows), "rows": rows,
            "legacy_fixed_input_sensitivity": sensitivity,
            "one_loop_up_down_control_errors": control}


def distance_scan(fixture, mz):
    inv = fixture["input"]["inv_alpha_em_MZ"]
    target = np.array([fixture["test_pair"]["sw2"][0], fixture["test_pair"]["alpha_s"][0]])
    errors = np.array([fixture["test_pair"]["sw2"][1], fixture["test_pair"]["alpha_s"][1]])
    failures = []

    def evaluate(t):
        try:
            one, two = boundary_down(float(t), inv, 1), boundary_down(float(t), inv, 2)
        except InvalidTrajectory as exc:
            return None, str(exc)
        if not (legacy_box(one) and legacy_box(two)):
            return None, "outside B915's actual weak-angle/strong-coupling root brackets"
        width = abs(two.observables - one.observables)
        d = float(np.linalg.norm((target - two.observables) / np.hypot(errors, width)))
        return {"d": d, "MU_GeV": mz*math.exp(t), "t": float(t),
                "two_loop_gauge_only": list(two.observables),
                "one_loop": list(one.observables), "loop_difference": list(width)}, None

    def objective(t):
        row, _ = evaluate(t)
        return float("inf") if row is None else row["d"]

    grids = []
    best = None
    for size in (61, 181):
        ts = np.linspace(math.log(1e3/mz), math.log(1.22e19/mz), size)
        candidates = []
        values = []
        for t in ts:
            row, reason = evaluate(t)
            values.append(float("inf") if row is None else row["d"])
            if row is None:
                if size == 61:
                    failures.append({"MU_GeV": mz*math.exp(t), "reason": reason})
            else:
                candidates.append(row)
        if not candidates:
            raise RuntimeError("no valid comparison points; no verdict is possible")
        grid_best = min(candidates, key=lambda row: row["d"])
        local_best = grid_best
        for i in range(1, size-1):
            if math.isfinite(values[i]) and values[i] <= min(values[i-1], values[i+1]):
                fit = minimize_scalar(objective, bounds=(ts[i-1], ts[i+1]),
                                      method="bounded", options={"xatol": 2e-8})
                row, _ = evaluate(fit.x)
                if fit.success and row is not None and row["d"] < local_best["d"]:
                    local_best = row
        grids.append({"grid_size": size, "valid_points": len(candidates),
                      "grid_best": grid_best, "continuous_refinement": local_best})
        if best is None or local_best["d"] < best["d"]:
            best = local_best
    return {"interpretation": "historical loop-difference metric, not calibrated sigma",
            "scope": "B915 scale interval intersected with BOTH original root brackets",
            "best": best, "criterion_d_le_3": best["d"] <= 3,
            "grid_checks": grids, "uncovered_or_invalid_61_grid_points": failures}


def audit_spectrum(fixture, mz):
    fields = ONE_FAMILY * 3 + (HIGGS,)
    b, d, l = beta(fields), matter_beta(D_PAIR), matter_beta(L_PAIR)
    x = inverse_couplings(fixture["input"]["inv_alpha_em_MZ"],
                         fixture["test_pair"]["sw2"][0],
                         fixture["test_pair"]["alpha_s"][0])
    t, r = threshold_requirement(x, b, d)
    examples = []
    for n in (1, 2, 3):
        feasible = t > 0 and abs(r) <= n*t
        row = {"copies": n, "feasible_with_all_masses_between_MZ_and_MU": feasible,
               "required_log_M_D_over_M_L_per_equal_copy": -r/n}
        if feasible:
            td, tl = t/2-r/(2*n), t/2+r/(2*n)
            end = piecewise_one_loop(x, t, [(td, np.array(d, float)*n),
                                            (tl, np.array(l, float)*n)])
            direct = x - np.array(b, float)*t/(2*math.pi)
            direct -= (np.array(d, float)*n*(t-td) + np.array(l, float)*n*(t-tl))/(2*math.pi)
            row.update({"illustrative_M_D_GeV": mz*math.exp(td),
                        "illustrative_M_L_GeV": mz*math.exp(tl),
                        "inverse_UV_couplings": list(end),
                        "meeting_residual": float(max(abs(np.diff(end)))),
                        "analytic_piecewise_difference": float(max(abs(end-direct)))})
        examples.append(row)
    degenerate = []
    for tm in (.1*t, .5*t, .9*t):
        end = piecewise_one_loop(x, t, [(tm, np.array(d, float)*3),
                                        (tm, np.array(l, float)*3)])
        base = x-np.array(b, float)*t/(2*math.pi)
        degenerate.append(float(max(abs(np.diff(end)-np.diff(base)))))
    return {"status": "CONDITIONAL INVERSE MATCH; all three archived couplings used",
            "representation_dimension_per_27": sum(f.color_dim*f.weak for f in
                                                    ONE_FAMILY+D_PAIR+L_PAIR+(SINGLET,)),
            "SM_beta_exact": [str(v) for v in b],
            "D_Dbar_delta_beta_exact": [str(v) for v in d],
            "L_Lbar_delta_beta_exact": [str(v) for v in l],
            "degenerate_pair_delta_beta_exact": [str(a+c) for a, c in zip(d, l)],
            "anomalies_SM_plus_three_27_exotic_sectors": {
                key: str(value) for key, value in anomalies(fields+(D_PAIR+L_PAIR)*3).items()},
            "required_t_U": t, "required_M_U_GeV": mz*math.exp(t),
            "required_sum_log_M_L_over_M_D": r, "examples": examples,
            "degenerate_control_errors": degenerate}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        parser.error("output already exists; choose a new filename to preserve the run")
    raw = (BANK / "results.json").read_bytes()
    if hashlib.sha256(raw).hexdigest() != RESULT_HASH:
        raise RuntimeError("archived fixture changed")
    fixture = json.loads(raw)
    old, prefix = legacy_functions()
    print("R1: checking the original curve against both UV equations", flush=True)
    r1 = audit_boundary(fixture, old, prefix)
    print("R1: refining the corrected historical comparison metric", flush=True)
    metric = distance_scan(fixture, old["MZ"])
    print("R2: deriving spectrum indices and threshold requirements", flush=True)
    r2 = audit_spectrum(fixture, old["MZ"])
    result = {"base_sha": "f06d34054899e8c23672b836a7c534af77cbd35d",
              "source_sha256": SOURCE_HASH, "archived_fixture_sha256": RESULT_HASH,
              "R1_boundary": r1, "R1_historical_metric": metric, "R2_spectrum": r2}
    with args.output.open("x") as handle:
        json.dump(result, handle, indent=2, allow_nan=False)
        handle.write("\n")
    print(json.dumps({"legacy_points": r1["historical_valid_points"],
                      "max_legacy_UV_residual": max(max(abs(v) for v in row["legacy_UV_residuals"])
                                                     for row in r1["rows"]),
                      "corrected_metric": metric["best"], "thresholds": r2}, indent=2), flush=True)


if __name__ == "__main__":
    main()
