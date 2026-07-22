"""
r6_gate.py -- R6 (deep-V localized-regime rerun), GATE STEP.

Preregistered gate: rerun ONE V6 calibration check -- the V=0 bulk ln-variance slope
vs the analytic target 1/pi^2 -- to confirm the calibrated pipeline (lib_chain,
lib_observables, lib_fit from veins/v6_tension) imports cleanly and reproduces its
banked number before any deep-V sweep is trusted.

This is a REUSE, not a rewrite: the physics/statistics engine (flat_occupied_orbitals,
number_variance, linfit_r2) is imported verbatim from the v6_tension libs. Only the
thin driver lines below (which N to probe, which ell window, printing) are new.

Reference (v6_tension/step1_calibrate.py check_bulk_variance, banked PASS):
  bulk Var(Q_A) = a*ln(ell)+b fit: a=... (expect 1/pi^2=0.10132), tol 5%.
"""
import sys
import json
import numpy as np

sys.path.insert(0, "<cc2-seat>/seat-work/veins/v6_tension")
from lib_chain import flat_occupied_orbitals          # noqa: E402
from lib_observables import number_variance            # noqa: E402
from lib_fit import linfit_r2                           # noqa: E402


def gate_bulk_variance(N=4181, tol=0.05):
    occ, evals, npart = flat_occupied_orbitals(N)
    x0 = N // 2 - 100
    ells = np.arange(20, 300, 10)
    varQ = np.array([number_variance(occ, np.arange(x0, x0 + e)) for e in ells])
    slope, intercept, r2, rss = linfit_r2(np.log(ells.astype(float)), varQ)
    target = 1.0 / np.pi ** 2
    rel_err = abs(slope - target) / target
    ok = rel_err < tol
    return {
        'N': N, 'npart': int(npart), 'slope': float(slope), 'target': float(target),
        'rel_err': float(rel_err), 'r2': float(r2), 'tol': tol, 'pass': bool(ok),
    }


if __name__ == "__main__":
    print("=" * 78)
    print("R6 GATE: rerun of V6 calibration check -- V=0 bulk ln-variance slope vs 1/pi^2")
    print("Purpose: confirm lib_chain / lib_observables / lib_fit import cleanly and")
    print("reproduce the banked V6 analytic result before trusting the deep-V sweep.")
    print("=" * 78)
    res = gate_bulk_variance(N=4181, tol=0.05)
    print(f"[GATE] N={res['N']} npart={res['npart']}  bulk Var(Q_A)=a*ln(ell)+b fit:")
    print(f"       a={res['slope']:.6f}  target=1/pi^2={res['target']:.6f}  "
          f"rel_err={res['rel_err']*100:.3f}%  R^2={res['r2']:.6f}  tol={res['tol']*100:.0f}%")
    print(f"GATE PASS = {res['pass']}")
    print("=" * 78)
    with open("outputs/gate.json", "w") as f:
        json.dump(res, f, indent=2)
    print("wrote outputs/gate.json")
    if not res['pass']:
        print("GATE FAILED -- pipeline import / physics engine did not reproduce the banked "
              "calibration number. Aborting is recommended before trusting the sweep.")
        sys.exit(1)
