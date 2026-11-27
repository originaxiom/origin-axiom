#!/usr/bin/env python3
"""Failing control for Card A2-PEER-SM-R612 (exits 1 with 0 stderr bytes).

Plants a deliberate unshifted T-law violation (tau -> tau + 1 without b -> b - a)
and verifies that the independent Frame A verifier catches the violation cleanly.
"""
import sys
from fractions import Fraction as Fr

import a2_peer_sm_r612_decisive as V


def main():
    tau = complex(21 / 100, 297 / 100)
    a, b = Fr(2, 5), Fr(1, 10)
    cd_src = V.sector_channel_data(tau, a, b, "delta_inf", reduce_flag=False)
    # Planted fault: omit the b -> b - a shift under T: tau -> tau + 1
    cd_bad = V.sector_channel_data(tau + 1, a, b, "delta_inf", reduce_flag=False)
    s_src, _ = V.extract_six_and_D(cd_src, V.eval_higgs_vec("DR", tau), 3)
    s_bad, _ = V.extract_six_and_D(cd_bad, V.eval_higgs_vec("DR", tau + 1), 3)
    diff = V._vec_dist(s_src, s_bad)
    ok = diff < 10 ** (-10)
    print(f"CONTROL_FAIL: planted_unshifted_T_violates_PL5 diff={diff:.6g} ok={ok}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
