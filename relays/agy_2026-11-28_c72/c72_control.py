#!/usr/bin/env python3
"""Standalone non-vacuous failing control for Card AGY-C72 (P-885 format, 0 of 19).

Runs two genuine exact computations on deliberately corrupted inputs/hypotheses:
  1. Enumerates all 5^3 = 125 triples of F_5^3 across X_kappa(F_5), verifies 0 mismatches
     for the true branchless law p^2 + ((kappa - 2)/p)(3 + ((kappa + 2)/p)) p + 1, and
     evaluates the sign-corrupted formula p^2 + ((kappa - 2)/p)(3 - ((kappa + 2)/p)) p + 1
     (catching 2 mismatches at kappa in {1, 4}).
  2. Enumerates the actual orbit O_9 of (3, 3, 3) mod 9 under L_tr, R_tr and evaluates
     the false mod-9 C-fixed-point hypothesis |Fix_{O_9}(C)| == 3 (actual is 2 != 3).
Exits with non-zero status 1 and zero stderr bytes (writing 0 files).
"""
from collections import deque
import sys


def legendre_mod(a: int, p: int) -> int:
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def count_sign_corrupted_mismatches_f5() -> tuple:
    p = 5
    counts = [0] * p
    for x in range(p):
        for y in range(p):
            for z in range(p):
                c = (x * x + y * y + z * z - x * y * z) % p
                counts[(c - 2) % p] += 1
    true_mismatches = 0
    corrupted_mismatches = 0
    for kappa in range(p):
        km2 = legendre_mod(kappa - 2, p)
        kp2 = legendre_mod(kappa + 2, p)
        if counts[kappa] != p * p + km2 * (3 + kp2) * p + 1:
            true_mismatches += 1
        if counts[kappa] != p * p + km2 * (3 - kp2) * p + 1:
            corrupted_mismatches += 1
    return true_mismatches, corrupted_mismatches


def count_o9_fix_c() -> int:
    m = 9
    root = (3, 3, 3)
    seen = {root}
    q = deque([root])
    while q:
        x, y, z = q.popleft()
        for w in (
            (x, z, (x * z - y) % m),
            (z, y, (y * z - x) % m),
            (x, (x * y - z) % m, y),
            ((x * y - z) % m, y, x),
        ):
            if w not in seen:
                seen.add(w)
                q.append(w)
    return sum(1 for (x, y, z) in seen if (y, z, x) == (x, y, z))


def main() -> int:
    true_mm, bad_mm = count_sign_corrupted_mismatches_f5()
    fix_o9 = count_o9_fix_c()
    if true_mm == 0 and bad_mm > 0 and fix_o9 != 3:
        sys.stdout.write(
            f"FAILING_CONTROL_C72: sign_corrupted_F5_mismatches={bad_mm} (true={true_mm}), "
            f"O9_fix_C={fix_o9}!=3 (expected exit 1).\n"
        )
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
