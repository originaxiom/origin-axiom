#!/usr/bin/env python3
"""Failing control for Card AGY-C65 (door rule D3: exits 1 with no traceback; 0 of 19).

Imports the AGY-C65 producer module beside this file and runs the equal-footing
all-prime systole parabolicity & two-counts quadratic-factor scan with ONE
deliberate mathematical perturbation: replacing the trace-3 systole seed U_1 = L R
(discriminant 3^2 - 4 = 5, polynomial x^2 - 3x + 1) by the trace-4 hyperbolic word
L^2 R = [[3, 1], [1, 1]] (discriminant 4^2 - 4 = 12, polynomial x^2 - 4x + 1).

Exit codes (per P-885 / rerun.py):
  1  control fails as it must: the perturbed scan completes cleanly with no crash and
     neither the p = 5 parabolic systole match nor the p = 5 quadratic kernel holds;
  0  control did not fail;
  3  control invalid (unexpected exception or incomplete scan; a crash is not a failure).
"""

import os as _os
import sys as _sys
import traceback as _tb


def _crash(et, ev, tb):
    _tb.print_exception(et, ev, tb)
    print("CONTROL INVALID: unexpected exception; a crash is not a failing control")
    _sys.stdout.flush()
    _os._exit(3)


_sys.excepthook = _crash

import ast
import pathlib
import sys

sys.dont_write_bytecode = True

import c65_two_counts_prime5_parabolic_systoles_and_diagonal_bundle_producer as prod


def main():
    tree = ast.parse(pathlib.Path(__file__).read_text(encoding="utf-8"))
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, (float, complex)):
            print("CONTROL INVALID: float or complex literal in control script")
            return 3

    trace4_seed = prod.mul2(prod.L_MAT, prod.mul2(prod.L_MAT, prod.R_MAT))
    e1_pert = prod.run_e1_all_prime_systole_scan(seed_word=trace4_seed)
    e2_pert = prod.run_e2_two_counts_spectrum(quad_poly_coeffs=(1, -4, 1))

    if len(e1_pert["prime_rows"]) != 9 or len(e2_pert["golden_kernel_rows"]) != 9:
        print("CONTROL INVALID: perturbed scan did not complete all 9 primes")
        return 3

    print(
        f"CONTROL: trace-4 perturbation (L^2 R, x^2 - 4x + 1) completed cleanly across 9 primes: "
        f"exact_match_primes={e1_pert['exact_complement_match_primes']}, "
        f"pure_cover_primes={e2_pert['primes_with_pure_cover_golden_kernel_in_2_to_23']}"
    )
    if (
        e1_pert["exact_complement_match_primes"] == [5]
        and e2_pert["primes_with_pure_cover_golden_kernel_in_2_to_23"] == [5]
    ):
        print("CONTROL DID NOT FAIL: decisive [5] prime selection still came out under trace-4 perturbation")
        return 0

    print(
        "CONTROL FAILS: as it must, replacing trace-3 L R / (x^2 - 3x + 1) with trace-4 L^2 R / (x^2 - 4x + 1) "
        f"yields exact_match_primes={e1_pert['exact_complement_match_primes']} != [5] and "
        f"pure_cover_primes={e2_pert['primes_with_pure_cover_golden_kernel_in_2_to_23']} != [5]"
    )
    return 1


if __name__ == "__main__":
    sys.exit(main())
