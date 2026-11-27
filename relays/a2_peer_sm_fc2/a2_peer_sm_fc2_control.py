#!/usr/bin/env python3
"""Failing control for Card A2-PEER-SM-FC2 (exits 1 with 0 stderr bytes).

Plants the unshifted-end fault in Frame C under S: (tau, v, L) -> (-1/tau, v S^{-1}, L)
without shifting L -> L + ln|tau|, verifying our Frame C evaluator catches the failure cleanly.
"""
import sys
from fractions import Fraction as Fr

import mpmath as mp

import a2_peer_sm_fc2_decisive as V


def main():
    mp.mp.dps = 30
    ctx = V._setup_mats()
    t0 = mp.mpc(V._f2m(Fr(13, 100)), V._f2m(Fr(6, 5)))
    L0 = V._f2m(Fr(266, 100))
    v0 = (Fr(4, 15), Fr(1, 30))
    S_g = ((0, -1), (1, 0))
    tS = V._apply_sl2z_tau(S_g, t0)
    vS = V._apply_sl2z_pt_ginv(S_g, v0)
    r0, V0 = V._invariants_from_Ys(V._frame_c_eval(t0, v0[0], v0[1], L0, ctx))
    # Planted fault: keep L0 unshifted instead of L0 + ln|t0|
    r_bad, V_bad = V._invariants_from_Ys(V._frame_c_eval(tS, vS[0], vS[1], L0, ctx))
    diff = V._inv_diff(r0, V0, r_bad, V_bad)
    ok = diff < mp.mpf(10) ** (-15)
    print(f"CONTROL_FAIL: unshifted_L_breaks_S_covariance diff={mp.nstr(diff, 6)} ok={ok}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
