#!/usr/bin/env python3
"""Standalone self-contained failing control for Card A2-CHIRAL-E8-SIBLINGS.
Demonstrates under python3 -I that perturbing m004's exact geometric minimal polynomial
X^2 - X + 1 to X^2 - X + 2 fails exact symbolic certification of m004's Thurston gluing
equation z^2 (1 - z)^{-1} * z^{-1} (1 - z)^2 = z (1 - z) == 1 (mod P).
Exits 1 with 0 stderr bytes. Standard library only; zero AST floats.
"""
import sys


def poly_rem_monic_deg2(coeffs_asc, c0, c1):
    """Exact remainder of integer polynomial mod (X^2 + c1*X + c0) -> X^2 = -c1*X - c0."""
    # Represent a + b*X
    a, b = 0, 0
    for coef in reversed(coeffs_asc):
        # Multiply (a + b*X) by X -> -c0*b + (a - c1*b)*X, then add coef
        a, b = coef - c0 * b, a - c1 * b
    return (a, b)


def main():
    # m004 cusp equation z_0 (1 - z_1) = 1 with z_0 = z_1 = X -> X - X^2 - 1 == 0 mod P!
    # True P = X^2 - X + 1 (c0=1, c1=-1) gives remainder (0, 0).
    # Faulted P_bad = X^2 - X + 2 (c0=2, c1=-1) gives remainder (1, 0) != (0, 0)!
    rem_bad = poly_rem_monic_deg2([-1, 1, -1], 2, -1)
    print(f"FAIL_CONTROL: perturbed_m004_gluing_rem={rem_bad} expected=(0, 0)")
    return 0 if rem_bad == (0, 0) else 1


if __name__ == "__main__":
    sys.exit(main())
