"""B1508 -- the xB seat's correction (xB015 K1, xB016 Addendum 1, sep16-branch 2026-09-17): sigma = l/(4G) is dimensionless in
three-dimensional gravity, so the object's action has one free dimensionless constant, not zero.  This branch's THE_FRAMEWORK.md
and GRAND_COMPUTATION_v0.md still say zero.

Dimensional analysis in units hbar = c = 1, lengths L: S = (1/16 pi G) int d^d x sqrt|g| (R - 2 Lambda) is dimensionless;
[d^d x] = L^d and [R] = [Lambda] = L^-2, so [G] = L^(d-2).  At d = 3, [G] = L and [l / G] = L^0.  Brown-Henneaux's central charge
c = 3 l / (2 G) is then 6 sigma.  Fixing Lambda = -1 fixes the unit (l = 1); it does not fix l / G.
"""
import json
import sys
from fractions import Fraction
from pathlib import Path


def length_exponent_of_G(d):
    # [S] = 0 = d (measure) - 2 (curvature) - [G]
    return d - 2


def main():
    rows = {d: length_exponent_of_G(d) for d in (3, 4, 5, 11)}
    sigma_exponent = 1 - rows[3]                          # [l] - [G] at d = 3
    c_over_sigma = Fraction(3, 2) / Fraction(1, 4)        # (3 l / 2 G) / (l / 4 G)
    return {"G_length_exponent_by_d": rows, "sigma_length_exponent_d3": sigma_exponent,
            "sigma_dimensionless": sigma_exponent == 0, "brown_henneaux_c_over_sigma": str(c_over_sigma),
            "free_dimensionless_constants_in_S_eq_minus_Vol_sigma": 1}


if __name__ == "__main__":
    res = main()
    out = json.dumps(res, indent=1, sort_keys=True)
    print(out)
    if "--record" in sys.argv:
        Path(__file__).with_name("free_constant_run.txt").write_text(out + "\n", encoding="utf-8")
