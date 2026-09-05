"""Post-failure numerical control repair; R7 scientific functions unchanged."""
import argparse
import hashlib
import json
from pathlib import Path
import time

import numpy as np
from scipy.linalg import expm

from . import higgs_sector as h


def primitive_checks():
    geo, b = h.geometry(), h.base()
    z = geo["z"]
    np.testing.assert_allclose(h.constraints(z), 0, atol=1e-12)
    rng = np.random.default_rng(202609057)
    displaced = z+.02*rng.normal(size=294)
    direction = rng.normal(size=294)
    direction /= np.linalg.norm(direction)
    numeric_j = (h.constraints(displaced+1e-4*direction)-h.constraints(displaced-1e-4*direction))/2e-4
    np.testing.assert_allclose(numeric_j, h.jacobian(displaced)@direction, atol=2e-10)
    first, second = h.derivatives(direction)[0]
    errors = {}
    for step in [1e-2, 1e-3, 1e-4, 1.]:
        plus, minus = [h.full_tree_hessian(z+sign*step*direction) for sign in [1, -1]]
        f1 = geo["si"]@((plus-minus)/(2*step))@geo["si"]
        f2 = geo["si"]@((plus+minus-2*b["h0"])/step**2)@geo["si"]
        errors[str(step)] = {"first": float(np.max(np.abs(f1-first))),
                             "second": float(np.max(np.abs(f2-second)))}
        np.testing.assert_allclose(f1, first, atol=2e-9)
        if step in [1e-2, 1e-3]:
            np.testing.assert_allclose(f2, second, atol=3e-7)
        if step == 1:
            np.testing.assert_allclose(f2, second, atol=1e-10)
    unitary = expm(1j*(.19*geo["T"][7]+.13*geo["T"][14]))
    sv, a = unitary@geo["s"], unitary@geo["y"]@unitary.conj().T
    for sign, cubic in [(-1, False), (1, True)]:
        def mass(field, adj):
            operator = adj+sign*.5*np.eye(27)
            result = operator@operator
            if cubic:
                cc = h.cubic_matrix(field)
                result += cc.conj().T@cc
            return result
        np.testing.assert_allclose(mass(sv, a), unitary@mass(geo["s"], geo["y"])@unitary.conj().T, atol=2e-12)
    j = h.jacobian(z, .4)
    changed = geo["si"]@(2*j.T@(h.weights()[:, None]*j))@geo["si"]
    w = h.weights()
    w[384:438] = 0
    omitted = geo["si"]@(2*b["j"].T@(w[:, None]*b["j"]))@geo["si"]
    detuned_count = int(np.count_nonzero(np.linalg.eigvalsh(changed) < 1e-9))
    omitted_count = int(np.count_nonzero(np.linalg.eigvalsh(omitted) < 1e-9))
    assert detuned_count == 77 and omitted_count == 89
    return {"Hessian_derivative_step_errors": errors, "complex_compact_covariance": True,
            "detuned_offset_scalar_kernel": detuned_count, "omitted_cubic_scalar_kernel": omitted_count}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    with args.output.open("x", encoding="utf-8") as handle:
        start = time.monotonic()
        result = {"primitive_checks": primitive_checks(), "classical": h.classical(),
                  "Yukawa_projection": h.exact_yukawa_projection(),
                  "exact_extra_fourth_trace": h.extra_fourth_trace_identity(), "quantum": h.quantum(),
                  "unchanged_scientific_code_sha256": hashlib.sha256(Path(h.__file__).read_bytes()).hexdigest(),
                  "control_wrapper_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  "elapsed_seconds": time.monotonic()-start}
        json.dump(result, handle, indent=2, allow_nan=False)
        handle.write("\n")
    brief = {"primitive_checks": result["primitive_checks"], "Yukawa_projection": result["Yukawa_projection"],
             "exact_extra_fourth_trace": result["exact_extra_fourth_trace"],
             "quantum": [{key: value for key, value in row.items() if key in
                          ["mu", "old_relative_shifts_phi1_phi2_adjoint", "new_U_D_shift_norms_in_S_VEV_units",
                           "kernel_force_and_stationarity_residual", "Higgs_leading_mass_squared", "angular_curvatures"]}
                         for row in result["quantum"]["runs"]], "elapsed_seconds": result["elapsed_seconds"]}
    print(json.dumps(brief, indent=2, allow_nan=False))


if __name__ == "__main__":
    main()
