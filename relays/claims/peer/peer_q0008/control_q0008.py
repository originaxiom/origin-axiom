#!/usr/bin/env python3
"""Standalone self-contained failing control for peer note PEER_Q0008.
Tests the planted fault of omitting the BD_5 sheet action on the peripheral meridian,
which restores the 8-dimensional periodic spin kernel instead of collapsing it to 0.
Exits 1 with 0 stderr bytes under python3 -I."""
import sys


def main():
    # Exact 64-dim Spin(13) spinor weights for (M=U(1), L=Z U(-2d)) in F_5[t]/(t^2 - 3)
    def f_mul(x, y):
        return ((x[0] * y[0] + 3 * x[1] * y[1]) % 5, (x[0] * y[1] + x[1] * y[0]) % 5)

    def f_tr(x):
        return (2 * x[0]) % 5

    f_one = (1, 0)
    f_two = (2, 0)
    f_m2d = (0, 1)  # -2*(2t) = -4t = t in F_5[t]/(t^2 - 3)
    nz_pairs = []
    seen = set()
    for a in range(5):
        for b in range(5):
            if (a, b) == (0, 0):
                continue
            two_x2 = f_mul(f_two, f_mul((a, b), (a, b)))
            wm = f_tr(f_mul(f_one, two_x2))
            wl = f_tr(f_mul(f_m2d, two_x2))
            key = min((wm, wl), ((-wm) % 5, (-wl) % 5))
            if key not in seen:
                seen.add(key)
                nz_pairs.append(key)

    # Without sheet action (s2_exps = [(0, 0), (0, 0)]), count periodic spin kernel (el == 10, em == 0 mod 20)
    per_ker = 0
    for bits in range(64):
        sm = 0
        sl = 0
        for k, (wm, wl) in enumerate(nz_pairs):
            sgn = 1 if ((bits >> k) & 1) == 0 else -1
            sm = (sm + sgn * wm * 3) % 5
            sl = (sl + sgn * wl * 3) % 5
        if (10 + 4 * sl) % 20 == 10 and (4 * sm) % 20 == 0:
            per_ker += 2

    # Claim tested by control: omitting sheet action still yields 0 periodic spin kernel (FALSE: yields 8!)
    if per_ker == 0:
        print("CONTROL_UNEXPECTED_PASS: periodic spin kernel remained 0 without sheet action")
        return 0
    print(f"CONTROL_FAIL_EXPECTED: omitting sheet action restores periodic spin kernel={per_ker} (not 0)")
    return 1


if __name__ == "__main__":
    sys.exit(main())
