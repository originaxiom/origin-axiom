#!/usr/bin/env python3
"""Failing control for Card AGY-C67 (door rule D3: exits 1 with no traceback; 0 of 19).

Imports the AGY-C67 producer module beside this file and runs the odd-prime Weil
unfolding & 3^k chiral-index scan with ONE deliberate mathematical perturbation:
collapsing the Heisenberg non-commutativity multiplier r = 1 in X Z = zeta_N^r Z X
to the commuting limit r = 0.

Exit codes (per P-885 / rerun.py):
  1  control fails as it must: turning off PF1 non-commutativity (r = 0) completes
     cleanly with no crash and kills both the p == 3 mod 4 chiral split and the
     constant +2 chiral index on the 3^k tower;
  0  control did not fail;
  3  control invalid (unexpected exception or incomplete scan; a crash is not a failure).
"""

import ast
import os
import pathlib
import sys
import traceback


def crash_handler(et, ev, tb):
    traceback.print_exception(et, ev, tb)
    print("CONTROL INVALID: unexpected exception; a crash is not a failing control")
    sys.stdout.flush()
    os._exit(3)


sys.excepthook = crash_handler
sys.dont_write_bytecode = True

import c67_weil_unfolding_markoff_jacobian_and_p775_ptolemy_producer as prod
import mpmath as mp


def main():
    tree = ast.parse(pathlib.Path(__file__).read_text(encoding="utf-8"))
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, (float, complex)):
            print("CONTROL INVALID: float or complex literal in control script")
            return 3

    mp.mp.dps = 55
    pert = prod.run_e1_e2_weil_unfolding(r_mult=0)
    if len(pert["prime_rows"]) != 8 or len(pert["tower_3k_rows"]) != 5:
        print("CONTROL INVALID: perturbed scan did not complete all 8 primes and 5 tower rungs")
        return 3

    print(
        f"CONTROL: commuting r=0 perturbation completed cleanly across 8 primes: "
        f"chiral_split_primes={pert['chiral_split_primes']}, "
        f"all_3k_index_plus2={pert['all_3k_constant_chiral_index_plus2_verified']}"
    )
    if (
        pert["chiral_split_primes"] == [3, 7, 11, 19, 23]
        and pert["all_3k_constant_chiral_index_plus2_verified"] is True
    ):
        print("CONTROL DID NOT FAIL: chiral split and +2 index survived commuting r=0 collapse")
        return 0

    print(
        "CONTROL FAILS: as it must, collapsing PF1 non-commutativity (r = 1 -> r = 0) "
        f"yields chiral_split_primes={pert['chiral_split_primes']} != [3, 7, 11, 19, 23] "
        f"and all_3k_index_plus2={pert['all_3k_constant_chiral_index_plus2_verified']} != True"
    )
    return 1


if __name__ == "__main__":
    sys.exit(main())
