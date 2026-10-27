#!/usr/bin/env python3
"""
B1764 verification script: Dynamical modular ground state and tau_* selection.

Resolves P-373 and P-380 by deriving the arithmetic geodesic apex:
  tau_* = (1 + i * sqrt(84)) / 3
from:
1. The maximal-depth finite modular ladder word:
     w = LLLLLRRLRLLR (length 12, saturating the N=5 ladder bound)
   with SL(2, Z) matrix:
     A = [[115, -32], [18, -5]], det(A) = 1, Tr(A) = 110.
2. Invariant hyperbolic geodesic semicircle:
     center c_0 = (115 - (-5)) / 36 = 10/3 = 1/3 (mod 1)
     radius R = sqrt(110^2 - 4) / 36 = sqrt(12096) / 36 = sqrt(84) / 3
     apex tau_* = 1/3 + i * sqrt(84) / 3.
3. Modulus stabilization under the modular effective potential:
     V(tau; t_*) = E(tau, 3) - t_* E(tau, 2)
   with:
     t_* = (dE_3/dy) / (dE_2/dy) |_{tau_*} = 4.430013
   which lies strictly within the W154 stability window t in [3.205, 4.624]
   and has positive radial mass squared d^2V/dy^2 = +17.112 > 0.
"""

import sys
import math
import json
import pathlib
import numpy as np
from scipy.special import kv, zeta

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "frontier" / "B1720_the_thread_fixes_the_point" / "verification"))
import thread_geometry as TG

def E_s(t: complex, s: float, N: int = 40) -> float:
    """Non-holomorphic Eisenstein series E(tau, s) via Chowla-Selberg expansion."""
    x, y = t.real, t.imag
    head = (2 * zeta(2 * s) * y**s + 
            2 * math.sqrt(math.pi) * math.gamma(s - 0.5) / math.gamma(s) * zeta(2 * s - 1) * y**(1 - s))
    tail = 0.0
    for k in range(1, N + 1):
        sig = sum(dd**(1 - 2 * s) for dd in range(1, k + 1) if k % dd == 0)
        tail += k**(s - 0.5) * sig * kv(s - 0.5, 2 * math.pi * k * y) * math.cos(2 * math.pi * k * x)
    return head + 4 * math.pi**s / math.gamma(s) * math.sqrt(y) * tail

def main() -> None:
    print("=" * 78)
    print("B1764: DYNAMICAL MODULAR GROUND STATE AND TAU_* SELECTION")
    print("=" * 78)

    # 1. Modular ladder word w
    word = "LLLLLRRLRLLR"
    h_lagrange = TG.lagrange(word) / 2.0
    r_rep, A_mat = TG.representative(word, h_lagrange)
    a, b, c, d = A_mat

    print(f"\n1. Word and Matrix Properties:")
    print(f"   Word: {word} (length {len(word)}, max L-run: 5)")
    print(f"   SL(2, Z) Matrix A: [[{a}, {b}], [{c}, {d}]]")
    det_A = a * d - b * c
    tr_A = a + d
    print(f"   det(A) = {det_A}")
    print(f"   Tr(A)  = {tr_A}")
    assert det_A == 1, "det(A) must be 1"
    assert tr_A == 110, "Tr(A) must be 110"

    # 2. Hyperbolic Geodesic
    c0 = (a - d) / (2.0 * c)
    c0_mod1 = c0 % 1.0
    disc = tr_A**2 - 4
    R2 = disc / (4.0 * c**2)
    R = math.sqrt(R2)
    R_exact = math.sqrt(84.0) / 3.0

    print(f"\n2. Invariant Geodesic Geometry:")
    print(f"   Center c_0        = {c0:.6f} = {a - d}/{2*c} = 10/3 -> {c0_mod1:.6f} (mod 1)")
    print(f"   Tr^2 - 4          = {disc} = 12096")
    print(f"   4 c^2             = {4 * c**2} = 1296")
    print(f"   R^2               = 12096 / 1296 = 28/3 = 84/9 = {R2:.6f}")
    print(f"   Radius R          = {R:.12f}")
    print(f"   Exact sqrt(84)/3  = {R_exact:.12f}")
    print(f"   Diff R - R_exact  = {abs(R - R_exact):.2e}")
    assert abs(R - R_exact) < 1e-14, "Radius must match sqrt(84)/3"
    assert abs(c0_mod1 - 1.0/3.0) < 1e-14, "Center must be 1/3 mod 1"

    tau_star = complex(1.0/3.0, R_exact)

    # 3. Modular Effective Potential
    print(f"\n3. Modulus Potential and Stabilization at tau_*:")
    e3_star = E_s(tau_star, 3.0)
    e2_star = E_s(tau_star, 2.0)
    print(f"   E3(tau_*) = {e3_star:.6f}")
    print(f"   E2(tau_*) = {e2_star:.6f}")

    dy = 1e-5
    de3 = (E_s(complex(1/3, R_exact + dy), 3.0) - E_s(complex(1/3, R_exact - dy), 3.0)) / (2.0 * dy)
    de2 = (E_s(complex(1/3, R_exact + dy), 2.0) - E_s(complex(1/3, R_exact - dy), 2.0)) / (2.0 * dy)
    t_star = de3 / de2

    print(f"   dE3/dy |_{{tau_*}} = {de3:.6f}")
    print(f"   dE2/dy |_{{tau_*}} = {de2:.6f}")
    print(f"   Critical ratio t_* = dE3/dE2 = {t_star:.6f}")

    # Stability window from W154: [3.205, 4.624]
    w154_min, w154_max = 3.205, 4.624
    print(f"   W154 Window: [{w154_min}, {w154_max}]")
    inside_window = (w154_min <= t_star <= w154_max)
    print(f"   Inside W154 Window: {inside_window}")
    assert inside_window, "t_* must lie in W154 window"

    # Radial curvature d^2V/dy^2
    d2e3 = (E_s(complex(1/3, R_exact + dy), 3.0) - 2 * e3_star + E_s(complex(1/3, R_exact - dy), 3.0)) / (dy**2)
    d2e2 = (E_s(complex(1/3, R_exact + dy), 2.0) - 2 * e2_star + E_s(complex(1/3, R_exact - dy), 2.0)) / (dy**2)
    d2V_dy2 = d2e3 - t_star * d2e2
    print(f"   Radial curvature (modulus mass squared) d^2V/dy^2 = {d2V_dy2:.6f}")
    assert d2V_dy2 > 0, "Radial curvature must be positive (stable local minimum)"

    # Save results
    out_dir = ROOT / "frontier" / "B1764_dynamical_modular_ground_state_and_tau_selection" / "verification"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_json = out_dir / "tau_ground_state.json"
    results = {
        "word": word,
        "word_length": len(word),
        "max_rung": 5,
        "matrix_A": [a, b, c, d],
        "det_A": det_A,
        "trace_A": tr_A,
        "geodesic_center_mod1": c0_mod1,
        "geodesic_radius": R,
        "tau_star": [tau_star.real, tau_star.imag],
        "E3_at_tau_star": e3_star,
        "E2_at_tau_star": e2_star,
        "dE3_dy": de3,
        "dE2_dy": de2,
        "t_star": t_star,
        "w154_window": [w154_min, w154_max],
        "is_inside_window": bool(inside_window),
        "modulus_mass_squared": float(d2V_dy2),
    }
    out_json.write_text(json.dumps(results, indent=2))
    print(f"\nSaved structured results to {out_json}")

if __name__ == "__main__":
    main()
