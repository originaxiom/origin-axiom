#!/usr/bin/env python3
"""Design arithmetic for THE FINAL ACT'S BAR, the third clock (the web seat, 2026-10-29). Data-free.

Main's B1816 (S260, 066e3bda9) made Weil-Petersson volume a frame-native clock beside hyperbolic area. Its depth tail
is P_WP(Im tau > Y) = 1 - (6/pi^2)<C>_x(Y), exact on Y >= 1, which B1816 approximates by 3/(Y + delta)^2 with
delta = 4 ln 2 / pi (0.1990 against the stored grid's 0.2016 at Y = 3, about 1.3%). This script uses that
approximation only, so its numbers are approximate to about that size. It computes, for the strip of P-373
(Im tau 2.96-3.11), the same quantities bar_arithmetic.py computed for the other two clocks.
"""
import math

STRIP = (2.96, 3.11)
CENTRE = 3.03
M_NEXT = 53  # LOOK_LEDGER's joint count after B1814 (52, P-445) plus the next look
DELTA = 4.0 * math.log(2.0) / math.pi
SIGMA = 0.1 / math.sqrt(34.0 - 2.66)  # the six's resolution, as in bar_arithmetic.py (illustrative)


def wp_tail(y):
    return 3.0 / (y + DELTA) ** 2


def wp_interval(a, b):
    return wp_tail(a) - wp_tail(b)


def main():
    p = wp_interval(*STRIP)
    gate = 0.01 / M_NEXT
    print("THE FINAL ACT'S BAR -- design arithmetic, the Weil-Petersson clock (B1816's approximate tail; data-free)")
    print(f"delta = 4 ln2/pi = {DELTA:.6f}; tail at Y = 3: {wp_tail(3.0):.4f} (B1816: 0.1990 by the formula, 0.2016 on its grid)")
    print(f"P_WP(Im tau in [{STRIP[0]}, {STRIP[1]}]) ~ {p:.6f}; largest ratio any law can reach ~ {1.0 / p:.1f}; bits {math.log2(1.0 / p):.2f}")
    print(f"P_WP(Im tau >= {CENTRE}) ~ {wp_tail(CENTRE):.6f}")
    lo, hi = 0.0, 1.0
    for _ in range(200):
        w = 0.5 * (lo + hi)
        if wp_interval(CENTRE - w / 2, CENTRE + w / 2) > gate:
            hi = w
        else:
            lo = w
    w = 0.5 * (lo + hi)
    print(f"window at {CENTRE} with null probability {gate:.3e}: width {w:.5f}")
    print(f"an exactly right law's window holds the six's best height with probability {math.erf(w / (2 * math.sqrt(2) * SIGMA)):.3f} (sigma {SIGMA:.4f})")


if __name__ == "__main__":
    main()
