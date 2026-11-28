#!/usr/bin/env python3
"""Standalone self-contained failing control for Card A2-WEAVE-E8-WEIL-SEAM (Phase 2).
Tests a planted fault: setting Heisenberg Z_3 chiral flux to theta=0 (mirror-symmetric)
and testing whether it breaks P_flip^(3) protection on C^3. Fails cleanly with exit 1 and 0 stderr."""
import sys


def main():
    # Exact 3x3 P_flip^(3) and mirror-symmetric shift S_0 = T_3 + T_3^{-1} on C^3
    p_flip = ((1, 0, 0), (0, 0, 1), (0, 1, 0))
    s_0 = ((0, 1, 1), (1, 0, 1), (1, 1, 0))

    def mat_mul(A, B):
        return tuple(
            tuple(sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3))
            for i in range(3)
        )

    comm_zero = (mat_mul(p_flip, s_0) == mat_mul(s_0, p_flip))
    # Planted false claim: mirror-symmetric theta=0 breaks P_flip^(3)
    if not comm_zero:
        print("CONTROL_UNEXPECTED_PASS: theta=0 broke P_flip^(3)")
        return 0
    print("CONTROL_FAIL_EXPECTED: theta=0 commutes identically with P_flip^(3) (J=0 protected)")
    return 1


if __name__ == "__main__":
    sys.exit(main())
