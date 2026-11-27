#!/usr/bin/env python3
"""Failing control for Card A2-PEER-SM-LIE2 (exits 1 with 0 stderr bytes).

Plants the false claim that E_8's determinant condition admits whole units m = 24 n
(and that K2 on the 27 vanishes at non-det-1 c = 12), verifying our check catches it cleanly.
"""
import sys


def main():
    # Exact det(rho (x) chi_eta^{r+m}) exponent is c = (9 + 3*(r + m)) mod 24.
    # Planted claim: some allowed twist r in {0,4,8,12,16,20} admits m = 24 with c == 0 mod 24.
    allowed_r = (0, 4, 8, 12, 16, 20)
    admits_whole_unit = any(((9 + 3 * (r + 24)) % 24) == 0 for r in allowed_r)
    print(f"CONTROL_FAIL: whole_unit_m24_admissible_in_E8={admits_whole_unit}")
    return 0 if admits_whole_unit else 1


if __name__ == "__main__":
    sys.exit(main())
