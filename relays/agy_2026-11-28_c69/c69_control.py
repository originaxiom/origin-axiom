#!/usr/bin/env python3
"""Standalone failing control for Card AGY-C69 (P-885 / T1b / T7b gate):
Plants two deliberate mathematical corruptions with zero sibling imports:
  (1) Replaces the Legendre divided-power wake-up formula 2*d + 1 - v_3(d!) with the naive
      un-divided formula 2*d + 1 (ignoring v_3(3!) = 1) and asserts that k = 6 wakes up;
  (2) Sets the Heisenberg symplectic orientation r = 0 on O_27 (x) Weil(3, r) (commuting
      fiber collapse g_{3,w} = I_3) and asserts that the bundle chiral index d_1 - d_2 equals +6.
Exits with code 1 and zero traceback on stderr when either false assertion is refuted.
"""

import sys


def main():
    # Corruption 1: Naive un-divided valuation 2*d + 1 for d = 1..6 misses k = 6 (mod 729)
    naive_wake = [2 * d + 1 for d in range(1, 7)]
    k6_present_naive = (6 in naive_wake)

    # Corruption 2: Commuting fiber r = 0 on O_27 (x) Weil(3, 0) sets fiber dims (3, 0, 0)
    orb = [(3, 3, 3)]
    seen = {(3, 3, 3)}
    qi = 0
    while qi < len(orb):
        x, y, z = orb[qi]
        qi += 1
        for nu in ((x, z, (x * z - y) % 27), (z, y, (y * z - x) % 27), (x, (x * y - z) % 27, y), ((y * x - z) % 27, y, x)):
            if nu not in seen:
                seen.add(nu)
                orb.append(nu)
    fix_c = sum(1 for (x, y, z) in orb if (y, z, x) == (x, y, z))
    b0 = (len(orb) + 2 * fix_c) // 3  # 26
    b1 = (len(orb) - fix_c) // 3      # 23
    # Tensor with r = 0 trivial fiber (F_0, F_1, F_2) = (3, 0, 0):
    d1_r0 = b1 * 3
    d2_r0 = b1 * 3
    chiral_idx_r0 = d1_r0 - d2_r0

    if (not k6_present_naive) or chiral_idx_r0 != 6:
        print(
            "CONTROL_REFUTED: undivided valuation misses k=6 "
            f"(naive_wake={naive_wake}) and r=0 collapses O_27 (x) Weil(3) chiral index to "
            f"{chiral_idx_r0} != 6."
        )
        sys.exit(1)

    print("UNEXPECTED: planted corruptions were not refuted.")
    sys.exit(0)


if __name__ == "__main__":
    main()
