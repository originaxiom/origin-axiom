#!/usr/bin/env python3
"""Failing control for Q0016 peer note: inflates the three-regime floor by 4x under the conjugate reading."""
import sys
import numpy as np
import verify_q0016 as V


def main():
    rng = np.random.default_rng(271828)
    inflated_violations = 0
    for _ in range(2000):
        h_vec = rng.normal(size=3) + 1j * rng.normal(size=3)
        mu_mat = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
        md_mat = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
        rho_c, f_c, _, _, _ = V.eval_pair(h_vec, mu_mat, md_mat, False)
        if rho_c < 4.0 * f_c - 1e-9:
            inflated_violations += 1
    claim_holds = (inflated_violations == 0)
    print("CONTROL: conjugate reading against 4F had %d violations; holds=%s" % (inflated_violations, claim_holds))
    return 0 if claim_holds else 1


if __name__ == "__main__":
    sys.exit(main())
