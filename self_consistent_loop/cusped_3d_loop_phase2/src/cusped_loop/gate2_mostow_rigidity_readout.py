"""Gate 2: Mostow-Prasad Topological Rigidity Readout (Zero Continuous Dials).

Extracts exact, parameter-free 3D hyperbolic topological invariants in quad
precision (`SnapPyHP`) across the golden background `LR` and all 18 bundle-extending
histories in the bounded family `A6` under both `b++` and `b+-` conventions:
  1. Hyperbolic volume Vol(M_H) and 3D Chern-Simons invariant CS(M_H) mod 1/2
     (plus parity indicator sin(4*pi*CS(M_H)) and amphicheirality check).
  2. Shortest-meridian cusp conformal modulus tau_cusp(M_H) and its PSL(2, Z)
     fundamental-domain representative tau_cusp_F(M_H).
  3. Shortest closed geodesic (Margulis throat) complex length l_1 + i*theta_1
     and associated geometric tube moduli tau_tube = (theta_1 + i*l_1)/(2*pi)
     and dual_tau_tube = 2*pi*i / (l_1 - i*theta_1) reduced to F.
  4. Selection (`A-one`: minimal hyperbolic volume and minimal word length) vs.
     Aggregation (`A-all`: Boltzmann e^{-Vol(M_H)} and Chern-Simons complex-volume
     partition weights), with zero embedded empirical or target coordinates (Guardrail 1).
"""

from __future__ import annotations

import cmath
import math
from typing import Any, Dict, List

import numpy as np
import snappy

from .gate1_3d_twisted_throat import enumerate_bounded_extending_family_A6
from .hyperbolic_fem_core import gauss_reduce_tau


def extract_mostow_invariants_for_spec(spec: str) -> Dict[str, Any]:
    """Extract quad-precision Mostow-Prasad invariants for a single cusped 3-manifold."""
    M_std = snappy.Manifold(spec)
    M = M_std.high_precision() if hasattr(M_std, "high_precision") else M_std

    vol = float(M.volume())
    cvol = complex(M.complex_volume())
    try:
        cs = float(M.chern_simons())
    except Exception:
        cs = float("nan")
    parity_sin4pi_cs = math.sin(4.0 * math.pi * cs) if not math.isnan(cs) else 0.0

    try:
        is_amph = bool(M_std.symmetry_group().is_amphicheiral())
    except Exception:
        is_amph = abs(parity_sin4pi_cs) < 1e-10

    M.set_peripheral_curves("shortest")
    cusp_mod = complex(M.cusp_info(0)["modulus"])
    if cusp_mod.imag < 0:
        cusp_mod = -cusp_mod
    tau_cusp_F = gauss_reduce_tau(cusp_mod)

    # Shortest closed geodesic (Margulis throat)
    l1_real = float("nan")
    theta1 = float("nan")
    l1_mult = 0
    tau_tube_F = None
    dual_tau_tube_F = None
    for cutoff in (1.5, 2.5, 3.5):
        try:
            ls = M.length_spectrum(cutoff)
            if len(ls) > 0:
                g0 = ls[0]
                z_len = complex(g0["length"])
                l1_real = float(z_len.real)
                theta1 = float(z_len.imag)
                l1_mult = int(g0["multiplicity"])
                # Tube holonomy modulus: (theta1 / (2*pi)) + i * (l1 / (2*pi)) in H
                tau_raw = complex(theta1 / (2.0 * math.pi), l1_real / (2.0 * math.pi))
                tau_tube_F = gauss_reduce_tau(tau_raw)
                # Dual conformal annulus/torus modulus: 2*pi*i / (l1 - i*theta1) = 2*pi*(theta1 + i*l1)/(l1^2 + theta1^2)
                dual_raw = (2.0 * math.pi * 1j) / complex(l1_real, -theta1)
                if dual_raw.imag < 0:
                    dual_raw = -dual_raw
                dual_tau_tube_F = gauss_reduce_tau(dual_raw)
                break
        except Exception:
            continue

    return {
        "spec": spec,
        "homology": str(M.homology()),
        "volume": vol,
        "chern_simons": cs,
        "complex_volume": [float(cvol.real), float(cvol.imag)],
        "parity_sin_4pi_cs": parity_sin4pi_cs,
        "is_amphicheiral": is_amph,
        "cusp_modulus_shortest": [float(cusp_mod.real), float(cusp_mod.imag)],
        "tau_cusp_F": [float(tau_cusp_F.real), float(tau_cusp_F.imag)],
        "shortest_geodesic_length": l1_real,
        "shortest_geodesic_torsion": theta1,
        "shortest_geodesic_mult": l1_mult,
        "tau_tube_F": (
            [float(tau_tube_F.real), float(tau_tube_F.imag)] if tau_tube_F is not None else None
        ),
        "dual_tau_tube_F": (
            [float(dual_tau_tube_F.real), float(dual_tau_tube_F.imag)]
            if dual_tau_tube_F is not None
            else None
        ),
    }


def run_gate2() -> Dict[str, Any]:
    """Execute Gate 2 Mostow rigidity readout across golden background and A6."""
    bg_pp = extract_mostow_invariants_for_spec("b++LR")
    bg_pm = extract_mostow_invariants_for_spec("b+-LR")

    a6 = enumerate_bounded_extending_family_A6(max_runs=5, max_sum=8)
    records: List[Dict[str, Any]] = []
    for member in a6["extending_members"]:
        w = member["word"]
        dir_pref = member["direct_rank1_prefix"]
        opp_pref = "b+-" if dir_pref == "b++" else "b++"
        inv_dir = extract_mostow_invariants_for_spec(dir_pref + w)
        inv_opp = extract_mostow_invariants_for_spec(opp_pref + w)
        records.append(
            {
                "runs": member["runs"],
                "word": w,
                "letters": len(w),
                "extension_sign_b_pp": member["extension_sign_on_b_pp"],
                "direct_prefix": dir_pref,
                "direct": inv_dir,
                "opposite": inv_opp,
            }
        )

    records.sort(key=lambda r: (r["direct"]["volume"], r["letters"], r["word"]))

    # A-one selection: minimal hyperbolic volume among genuine non-cover departures
    # (excluding pure (LR)^m base covers LRLR, LRLRLR, LRLRLRLR of golden m004)
    non_cover_records = [
        r for r in records if r["word"] != "LR" * (len(r["word"]) // 2)
    ]
    min_vol = non_cover_records[0]["direct"]["volume"]
    a_one_vol_winners = [
        r for r in non_cover_records if abs(r["direct"]["volume"] - min_vol) < 1e-9
    ]

    # A-one by shortest Margulis throat geodesic length l_1
    valid_throat = [
        r for r in non_cover_records if not math.isnan(r["direct"]["shortest_geodesic_length"])
    ]
    valid_throat.sort(key=lambda r: r["direct"]["shortest_geodesic_length"])
    min_l1 = valid_throat[0]["direct"]["shortest_geodesic_length"]
    a_one_throat_winners = [
        r for r in valid_throat if abs(r["direct"]["shortest_geodesic_length"] - min_l1) < 1e-9
    ]

    # A-all aggregation on raw L-initial A6 list vs. intrinsic conjugacy-deduplicated parity closure
    # Exact Fibonacci orientation-reversing involution W_enant = L * swap_LR(W) * L^{-1}:
    # Since W ends with 'R', swap_LR(W) ends with 'L', so cycling its final 'L' to the front gives W_enant!
    def fibonacci_mirror_word(w: str) -> str:
        swapped = w.translate(str.maketrans("LR", "RL"))
        return swapped[-1] + swapped[:-1]

    def canonical_cyclic_word(w: str) -> str:
        return min(w[i:] + w[:i] for i in range(len(w)))

    vols = np.array([r["direct"]["volume"] for r in records], dtype=float)
    boltz = np.exp(-(vols - np.min(vols)))
    boltz /= np.sum(boltz)

    cusp_taus_F = np.array(
        [complex(*r["direct"]["tau_cusp_F"]) for r in records], dtype=np.complex128
    )
    parities = np.array(
        [r["direct"]["parity_sin_4pi_cs"] for r in records], dtype=float
    )

    tau_cusp_boltz_avg = complex(np.sum(boltz * cusp_taus_F))
    net_parity_boltz_raw = float(np.sum(boltz * parities))

    # Build intrinsic cyclic-deduplicated + Fibonacci-mirror-closed ensemble from A6:
    intrinsic_map: Dict[str, Dict[str, Any]] = {}
    for r in non_cover_records:
        for w_cand in (r["word"], fibonacci_mirror_word(r["word"])):
            c_key = canonical_cyclic_word(w_cand)
            if c_key not in intrinsic_map:
                spec_c = r["direct_prefix"] + w_cand
                intrinsic_map[c_key] = extract_mostow_invariants_for_spec(spec_c)

    intr_list = list(intrinsic_map.values())
    vols_intr = np.array([x["volume"] for x in intr_list], dtype=float)
    boltz_intr = np.exp(-(vols_intr - np.min(vols_intr)))
    boltz_intr /= np.sum(boltz_intr)
    taus_intr = np.array([complex(*x["tau_cusp_F"]) for x in intr_list], dtype=np.complex128)
    par_intr = np.array([x["parity_sin_4pi_cs"] for x in intr_list], dtype=float)
    tau_cusp_intr_avg = complex(np.sum(boltz_intr * taus_intr))
    net_parity_boltz_sum = float(np.sum(boltz_intr * par_intr))

    # Complex-volume weight exp(-Vol - i * 2*pi^2 * CS) on intrinsic parity-closed set
    cs_vals = np.array([x["chern_simons"] for x in intr_list], dtype=float)
    complex_wts = np.exp(-(vols_intr - np.min(vols_intr)) - 1j * 2.0 * (math.pi ** 2) * cs_vals)
    Z_complex = complex(np.sum(complex_wts))
    tau_cusp_complex_avg = (
        complex(np.sum(complex_wts * taus_intr) / Z_complex)
        if abs(Z_complex) > 1e-12
        else complex(float("nan"), float("nan"))
    )

    return {
        "gate": "Gate 2: Mostow-Prasad Topological Rigidity Readout",
        "golden_background": {"b++LR": bg_pp, "b+-LR": bg_pm},
        "A_one_minimal_volume": {
            "min_volume": min_vol,
            "winner_count": len(a_one_vol_winners),
            "winners_are_enantiomeric_pair": (
                len(a_one_vol_winners) == 2
                and abs(
                    a_one_vol_winners[0]["direct"]["chern_simons"]
                    + a_one_vol_winners[1]["direct"]["chern_simons"]
                )
                < 1e-12
            ),
            "winners": [
                {
                    "runs": w["runs"],
                    "word": w["word"],
                    "spec": w["direct"]["spec"],
                    "volume": w["direct"]["volume"],
                    "chern_simons": w["direct"]["chern_simons"],
                    "parity_sin_4pi_cs": w["direct"]["parity_sin_4pi_cs"],
                    "tau_cusp_F": w["direct"]["tau_cusp_F"],
                    "shortest_geodesic_length": w["direct"]["shortest_geodesic_length"],
                    "shortest_geodesic_torsion": w["direct"]["shortest_geodesic_torsion"],
                    "tau_tube_F": w["direct"]["tau_tube_F"],
                    "dual_tau_tube_F": w["direct"]["dual_tau_tube_F"],
                }
                for w in a_one_vol_winners
            ],
        },
        "A_one_thinnest_margulis_throat": {
            "min_shortest_geodesic_length": min_l1,
            "winner_words": [w["word"] for w in a_one_throat_winners],
        },
        "A_all_partition_aggregation": {
            "raw_A6_family_size": len(records),
            "intrinsic_parity_closed_size": len(intr_list),
            "raw_L_start_boltzmann_tau_cusp_F": [
                float(tau_cusp_boltz_avg.real),
                float(tau_cusp_boltz_avg.imag),
            ],
            "raw_L_start_truncation_parity_bias": net_parity_boltz_raw,
            "boltzmann_tau_cusp_F": [
                float(tau_cusp_intr_avg.real),
                float(tau_cusp_intr_avg.imag),
            ],
            "boltzmann_net_parity_sum": net_parity_boltz_sum,
            "complex_volume_Z": [float(Z_complex.real), float(Z_complex.imag)],
            "complex_volume_tau_cusp_F": [
                float(tau_cusp_complex_avg.real),
                float(tau_cusp_complex_avg.imag),
            ],
        },
        "all_extending_A6_mostow_table": records,
    }


if __name__ == "__main__":
    import json

    res = run_gate2()
    print(json.dumps(res["A_one_minimal_volume"], indent=2))
    print(json.dumps(res["A_all_partition_aggregation"], indent=2))
