#!/usr/bin/env python3
"""Failing control for Card A2-PEER-SM-R581 (exits 1 with 0 stderr bytes).

Plants a non-primitive hypercharge normalization (doubled charges -> Z_12 kernel instead of Z_6)
and verifies the exact kernel check rejects it cleanly.
"""
import sys
from fractions import Fraction as Fr


def main():
    # Primitive normalization gives 6 elements (Z_6); doubled normalization gives 12 (Z_12).
    ker_size = sum(
        1 for a in range(3) for b in range(2) for num in range(12)
        if (Fr(a, 3) + 4 * Fr(num, 12)).denominator == 1
        and (Fr(b, 2) - 6 * Fr(num, 12)).denominator == 1
    )
    ok = (ker_size == 6)
    print(f"CONTROL_FAIL: nonprimitive_Y_kernel_order={ker_size} expected=6 ok={ok}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
