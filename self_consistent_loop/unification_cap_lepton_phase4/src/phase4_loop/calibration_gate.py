"""Step 2: Textbook Calibration Gate for Phase 4.

Verifies to < 1e-12 prior to evaluating candidate histories:
  1. Positive-weight S_4-symmetric 14-point degree-5 tetrahedral quadrature on all
     monomials of degree <= 5 (covering degree-3 Dirac Yukawa and degree-4 Weinberg
     integrands) and Epstein-Penner 24-cone volumes on m004 (`b++LR`) and m003 (`b+-LR`).
  2. Exact Fox free-differential calculus and Wada-Reidemeister 1-loop torsion against
     the analytical Alexander polynomial |3 - 2 cos(theta)| = (7 -+ sqrt(5))/2 on m004
     (`b++LR`) and |3 + 2 cos(theta)| = (5 +- sqrt(5))/2 on m003 (`b+-LR`) at theta = 2*pi*q/5.
  3. PMNS Seesaw & Weinberg Haar U(3)^3 basis-scrambling invariance (< 1e-12, Guardrail 3)
     on both a complex CP-violating benchmark and a real CP-conserving control.
"""

from __future__ import annotations

import itertools
import math
from typing import Any, Dict

import numpy as np
import snappy

from .phase4_core import (
    TET_QUAD14_BARY,
    TET_QUAD14_WTS,
    _integer_snf_with_inverses,
    compute_penner_tet_volume,
    compute_wada_reidemeister_torsion,
    extract_epstein_penner_data,
    extract_lepton_pmns_observables,
    verify_lepton_seesaw_haar_invariance,
    verify_lepton_weinberg_haar_invariance,
)


def run_quadrature_and_epstein_penner_calibration() -> Dict[str, Any]:
    """Verify 14-point degree-5 simplex quadrature (deg 3 Yukawa + deg 4 Weinberg) and Penner volume."""
    min_wt = float(np.min(TET_QUAD14_WTS))
    wt_sum_err = abs(float(np.sum(TET_QUAD14_WTS)) - (1.0 / 6.0))

    max_deg3_err = 0.0
    max_deg4_err = 0.0
    max_deg5_err = 0.0
    n_monomials = 0
    for a in range(6):
        for b in range(6 - a):
            for c in range(6 - a - b):
                for d in range(6 - a - b - c):
                    deg = a + b + c + d
                    exact = (
                        math.factorial(a) * math.factorial(b) * math.factorial(c) * math.factorial(d)
                    ) / math.factorial(deg + 3)
                    vals = (
                        (TET_QUAD14_BARY[:, 0] ** a)
                        * (TET_QUAD14_BARY[:, 1] ** b)
                        * (TET_QUAD14_BARY[:, 2] ** c)
                        * (TET_QUAD14_BARY[:, 3] ** d)
                    )
                    err = abs(float(np.dot(TET_QUAD14_WTS, vals)) - exact)
                    if deg <= 3:
                        max_deg3_err = max(max_deg3_err, err)
                    if deg == 4:
                        max_deg4_err = max(max_deg4_err, err)
                    max_deg5_err = max(max_deg5_err, err)
                    n_monomials += 1

    vol_checks = {}
    max_vol_err = 0.0
    for spec in ("b++LR", "b+-LR"):
        ep = extract_epstein_penner_data(spec)
        penner_vol = sum(compute_penner_tet_volume(G, nq=20) for G in ep["grams"])
        err = abs(penner_vol - ep["snappy_volume"])
        max_vol_err = max(max_vol_err, err)
        vol_checks[spec] = {
            "snappy_volume": ep["snappy_volume"],
            "penner_24cone_volume": penner_vol,
            "abs_err": err,
            "max_inter_gluing_err": ep["max_inter_gluing_err"],
        }

    passed = (
        min_wt > 0.0
        and wt_sum_err < 1e-15
        and max_deg3_err < 1e-15
        and max_deg4_err < 1e-15
        and max_deg5_err < 1e-15
        and max_vol_err < 1e-12
    )
    return {
        "min_quad_weight": min_wt,
        "weight_sum_err": wt_sum_err,
        "num_monomials_checked": n_monomials,
        "max_deg3_yukawa_monomial_err": max_deg3_err,
        "max_deg4_weinberg_monomial_err": max_deg4_err,
        "max_deg5_monomial_err": max_deg5_err,
        "epstein_penner_volumes": vol_checks,
        "max_penner_volume_err": max_vol_err,
        "passed": passed,
    }


def run_alexander_reidemeister_calibration() -> Dict[str, Any]:
    """Verify Fox-Wada Reidemeister torsion against exact Alexander polynomials on m004 and m003."""
    sqrt5 = math.sqrt(5.0)
    exact_m004 = {1: 0.5 * (7.0 - sqrt5), 2: 0.5 * (7.0 + sqrt5)}
    exact_m003 = {1: 0.5 * (5.0 + sqrt5), 2: 0.5 * (5.0 - sqrt5)}

    results = {}
    max_alex_err = 0.0
    max_reid_err = 0.0
    max_wada_spread = 0.0

    for spec, label, exact_map in (
        ("b++LR", "m004_figure_eight", exact_m004),
        ("b+-LR", "m003_sister", exact_m003),
    ):
        M = snappy.Manifold(spec)
        G = M.fundamental_group()
        gens = list(G.generators())
        rels = list(G.relators())

        A = np.zeros((len(rels), len(gens)), dtype=int)
        for ri, r in enumerate(rels):
            for ch in r:
                A[ri, gens.index(ch.lower())] += -1 if ch.isupper() else 1

        _, _, _, V_snf, _ = _integer_snf_with_inverses(A)
        free_cols = [
            np.array([int(x) for x in V_snf[:, j]], dtype=int)
            for j in range(V_snf.shape[1])
            if np.all(A @ np.array([int(x) for x in V_snf[:, j]], dtype=object) == 0)
        ]
        assert len(free_cols) == 1
        v_free = free_cols[0]

        q_records = {}
        for q in (1, 2):
            theta = 2.0 * math.pi * q / 5.0
            rho = {gens[i]: np.exp(1j * theta * int(v_free[i])) for i in range(len(gens))}
            res = compute_wada_reidemeister_torsion(gens, rels, rho)

            # Free generator has |v_free[i]| == 1:
            free_gen = next(gens[i] for i in range(len(gens)) if abs(int(v_free[i])) == 1)
            alex_num = res["col_numerators"][free_gen]
            alex_exact = exact_map[q]
            reid_exact = alex_exact / (2.0 * math.sin(0.5 * theta))

            a_err = abs(alex_num - alex_exact)
            r_err = abs(res["torsion_abs"] - reid_exact)
            max_alex_err = max(max_alex_err, a_err)
            max_reid_err = max(max_reid_err, r_err)
            max_wada_spread = max(max_wada_spread, res["wada_column_spread"])

            q_records[f"q_{q}"] = {
                "theta": theta,
                "fox_alexander_abs": alex_num,
                "analytical_alexander_abs": alex_exact,
                "alexander_abs_err": a_err,
                "wada_reidemeister_torsion": res["torsion_abs"],
                "analytical_reidemeister_torsion": reid_exact,
                "reidemeister_abs_err": r_err,
                "wada_column_spread": res["wada_column_spread"],
            }
        results[label] = q_records

    passed = max_alex_err < 1e-13 and max_reid_err < 1e-13 and max_wada_spread < 1e-13
    return {
        "benchmarks": results,
        "max_alexander_err": max_alex_err,
        "max_reidemeister_err": max_reid_err,
        "max_wada_column_spread": max_wada_spread,
        "passed": passed,
    }


def run_pmns_haar_scrambling_calibration() -> Dict[str, Any]:
    """Verify seesaw and Weinberg PMNS observables under random Haar U(3)^3 rotations (< 1e-12)."""
    # Rational + i complex benchmark (zero empirical floats):
    Y_e_cpx = np.array(
        [
            [0.25 + 0.0j, 0.05 + 0.02j, -0.02 + 0.01j],
            [0.04 - 0.01j, 1.0 + 0.1j, 0.25 - 0.15j],
            [0.01 + 0.03j, 0.20 + 0.10j, 3.0 + 0.0j],
        ],
        dtype=np.complex128,
    )
    Y_nu_cpx = np.array(
        [
            [0.5 + 0.1j, 0.4 - 0.2j, 0.1 + 0.05j],
            [0.4 + 0.15j, 0.9 + 0.0j, 0.7 - 0.25j],
            [0.2 - 0.1j, 0.6 + 0.2j, 1.2 + 0.1j],
        ],
        dtype=np.complex128,
    )
    M_R_cpx = np.array(
        [
            [2.0 + 0.0j, 0.25 + 0.1j, 0.0 + 0.0j],
            [0.25 + 0.1j, 5.0 - 0.2j, 0.5 + 0.0j],
            [0.0 + 0.0j, 0.5 + 0.0j, 11.0 + 0.3j],
        ],
        dtype=np.complex128,
    )

    M_nu_seesaw = -(Y_nu_cpx @ np.linalg.solve(M_R_cpx, Y_nu_cpx.T))
    obs_cpx = extract_lepton_pmns_observables(Y_e_cpx, M_nu_seesaw)
    seesaw_haar = verify_lepton_seesaw_haar_invariance(Y_e_cpx, Y_nu_cpx, M_R_cpx, n_trials=20, seed=4001)

    # Weinberg benchmark:
    M_nu_w = 0.5 * (Y_nu_cpx @ Y_nu_cpx.T)
    weinberg_haar = verify_lepton_weinberg_haar_invariance(Y_e_cpx, M_nu_w, n_trials=20, seed=4002)

    # Real CP-conserving negative control:
    obs_real = extract_lepton_pmns_observables(Y_e_cpx.real.astype(np.complex128), M_nu_seesaw.real.astype(np.complex128))
    real_haar = verify_lepton_weinberg_haar_invariance(
        Y_e_cpx.real.astype(np.complex128),
        M_nu_seesaw.real.astype(np.complex128),
        n_trials=20,
        seed=4003,
    )

    passed = (
        abs(obs_cpx["jarlskog_pmns_norm"]) > 1e-6
        and abs(obs_real["jarlskog_pmns_norm"]) < 1e-15
        and seesaw_haar["passed"]
        and weinberg_haar["passed"]
        and real_haar["passed"]
    )
    return {
        "complex_seesaw_jarlskog": obs_cpx["jarlskog_pmns_norm"],
        "complex_seesaw_angles": obs_cpx["angles"],
        "real_control_jarlskog": obs_real["jarlskog_pmns_norm"],
        "seesaw_haar_audit": seesaw_haar,
        "weinberg_haar_audit": weinberg_haar,
        "real_control_haar_audit": real_haar,
        "passed": passed,
    }


def run_all_phase4_calibrations() -> Dict[str, Any]:
    """Run all Step 2 textbook calibrations."""
    c1 = run_quadrature_and_epstein_penner_calibration()
    c2 = run_alexander_reidemeister_calibration()
    c3 = run_pmns_haar_scrambling_calibration()
    return {
        "quadrature_and_epstein_penner": c1,
        "alexander_reidemeister_torsion": c2,
        "pmns_haar_scrambling": c3,
        "all_calibrations_passed": bool(c1["passed"] and c2["passed"] and c3["passed"]),
    }


if __name__ == "__main__":
    out = run_all_phase4_calibrations()
    print("Phase 4 Calibration Gate passed:", out["all_calibrations_passed"])
    print("  1. Deg-5 quad & Penner err:", out["quadrature_and_epstein_penner"]["max_deg5_monomial_err"], out["quadrature_and_epstein_penner"]["max_penner_volume_err"])
    print("  2. Alexander / Reidemeister err:", out["alexander_reidemeister_torsion"]["max_alexander_err"], out["alexander_reidemeister_torsion"]["max_reidemeister_err"])
    print("  3. PMNS Seesaw Haar err:", out["pmns_haar_scrambling"]["seesaw_haar_audit"])
