#!/usr/bin/env python3
"""Standalone failing control for Card AGY-C71 (P-885 format, 0 of 19).

Represents the falsified minus-sign divided-power hypothesis d_8 > 7 at mod 6561 = 3^8
against the true Kempner three-rung plateau d_6 = d_7 = d_8 = 7.
Exits with non-zero status 1 and zero stderr bytes.
"""
import sys


def main() -> int:
    kempner_d6_d7_d8 = (7, 7, 7)
    falsified_jump_at_k8 = (7, 7, 9)
    if kempner_d6_d7_d8 != falsified_jump_at_k8:
        sys.stdout.write(
            "FAILING_CONTROL_C71: Kempner three-rung plateau (d_6, d_7, d_8) = (7, 7, 7) "
            "refutes naive minus-sign jump hypothesis at k = 8 (expected exit 1).\n"
        )
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
