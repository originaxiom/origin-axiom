#!/usr/bin/env python3
"""Design arithmetic for THE FINAL ACT'S BAR (the web seat, 2026-10-29). Data-free.

It computes how much one world's depth can say about a law for Im tau, so that the bar's typicality
cell is not built to be unpassable or unfailable (WHAT_WOULD_COUNT 4A.0, E2/MB12). Nothing here is set beside
a measured value. The strip's bounds are the record's (P-373: Im tau 2.96-3.11, centre 3.03), and the
six's resolution in Im tau is read from P-373's two post hoc numbers (chi2_six 2.66 at the optimum and 34 at
+-0.1), in a quadratic approximation, for illustration only.

1. The strip's probability under the two clocks of B1813:
   - followed (hyperbolic area): P(Im tau > Y) = 3/(pi Y) for Y >= 1;
   - counted (Minkowski's measure lifted to the geodesic flow): B1813's limit law, "i.i.d. Geometric(1/2)
     runs with their roof", computed here by this seat's own Monte Carlo and checked against B1813's limit
     row (0.3829, 0.1676, 0.03462, 0.00754, 0.00039 at Y = 1.5, 2, 3, 4, 6) and against row 1476's
     asymptotic form C(<2Y>) Y^(-1/2) 4^(-Y) (1 - c/Y), C in [3.914, 3.999], c about 0.090.
2. THE_BAR's gate at the joint look count (LOOK_LEDGER, P-367; m = 52 after B1814, P-445; the next look 53).
3. The width of a window at the strip's centre whose null probability equals the gate, under each clock.
4. The chance that an exactly right law's window of that width contains the six's best height, at the
   six's resolution.
"""
import math
import numpy as np

STRIP = (2.96, 3.11)
CENTRE = 3.03
M_LEDGER = 52          # LOOK_LEDGER after B1814 (P-445's ruling of 2026-10-29)
M_NEXT = M_LEDGER + 1  # the next look
GATE_1 = 0.01


def followed_tail(y):
    return 3.0 / (math.pi * y)


def followed_interval(a, b):
    return followed_tail(a) - followed_tail(b)


# ---- the counted clock: B1813's limit law, this seat's implementation ----
def minkowski_sample(rng, n, depth=48):
    """x in (0,1) with continued-fraction digits i.i.d. P(a = k) = 2^-k (Minkowski's measure)."""
    a = rng.geometric(0.5, size=(n, depth)).astype(np.float64)
    x = np.zeros(n)
    for k in range(depth - 1, -1, -1):
        x = 1.0 / (a[:, k] + x)
    return x


def counted_tails(ys, n_total=8_000_000, chunk=1_000_000, a_max=90, seed=20261029):
    """Fraction of arclength above each height y: E[time above y per run] / E[time per run].

    A run of A equal letters (P(A) = 2^-A) is an excursion whose apex height is (A + s)/2, with s = x' + x''
    the two neighbouring continued fractions (each Minkowski-distributed, independent); the arclength above
    height y on a geodesic semicircle of radius h is 2 arccosh(h / y) when h > y; the arclength of a run is
    2 log(A + x'), averaged with the run's own weight 2^-A.
    """
    rng = np.random.default_rng(seed)
    num_batches = []
    den_batches = []
    for _ in range(n_total // chunk):
        s = minkowski_sample(rng, chunk) + minkowski_sample(rng, chunk)
        # the denominator: E[2 log(A + x')] with A ~ Geometric(1/2)
        A = rng.geometric(0.5, size=chunk).astype(np.float64)
        den_batches.append(np.mean(2.0 * np.log(A + minkowski_sample(rng, chunk))))
        row = []
        for y in ys:
            tot = 0.0
            for a in range(1, a_max):
                arg = (a + s) / (2.0 * y)
                v = np.where(arg > 1.0, 2.0 * np.arccosh(np.maximum(arg, 1.0)), 0.0)
                tot += 2.0 ** (-a) * v.mean()
            row.append(tot)
        num_batches.append(row)
    num = np.array(num_batches)          # batches x ys
    den = np.array(den_batches)          # batches
    ratio_batches = num / den[:, None]
    est = ratio_batches.mean(axis=0)
    se = ratio_batches.std(axis=0, ddof=1) / math.sqrt(len(den))
    # the strip as a difference within each batch (shares the batch's randomness)
    return est, se, ratio_batches


def main():
    print("THE FINAL ACT'S BAR -- design arithmetic (data-free)")
    print()
    p_f = followed_interval(*STRIP)
    print(f"[1a] followed clock: P(Im tau in [{STRIP[0]}, {STRIP[1]}]) = (3/pi)(1/{STRIP[0]} - 1/{STRIP[1]}) = {p_f:.6f}")
    print(f"     followed clock: P(Im tau >= {CENTRE}) = {followed_tail(CENTRE):.6f}")
    print(f"     largest ratio P_D(S)/P_D0(S) any law can reach (P_D(S) <= 1): {1.0 / p_f:.1f}")
    print()

    ys = [1.5, 2.0, 3.0, 4.0, 6.0, STRIP[0], CENTRE, STRIP[1]]
    est, se, batches = counted_tails(ys)
    ref = {1.5: 0.3829, 2.0: 0.1676, 3.0: 0.03462, 4.0: 0.00754, 6.0: 0.00039}
    print("[1b] counted clock, this seat's Monte Carlo of B1813's limit law (8 batches of 10^6 runs):")
    for y, e, s in zip(ys, est, se):
        tag = f"  B1813's limit row: {ref[y]}" if y in ref else ""
        print(f"     P(Im tau > {y:5.2f}) = {e:.6f} +- {s:.6f}{tag}")
    i0, i1 = ys.index(STRIP[0]), ys.index(STRIP[1])
    strip_b = batches[:, i0] - batches[:, i1]
    p_c = strip_b.mean()
    p_c_se = strip_b.std(ddof=1) / math.sqrt(len(strip_b))
    print(f"     counted clock: P(Im tau in the strip) = {p_c:.6f} +- {p_c_se:.6f}")
    print(f"     largest ratio any law can reach: {1.0 / p_c:.1f}")
    # row 1476's asymptotic form, as a cross-check (C at its two ends, c = 0.090)
    def asym(y, C, c=0.090):
        return C * y ** -0.5 * 4.0 ** (-y) * (1.0 - c / y)
    lo = asym(STRIP[0], 3.914) - asym(STRIP[1], 3.999)
    hi = asym(STRIP[0], 3.999) - asym(STRIP[1], 3.914)
    mid = asym(STRIP[0], 3.954) - asym(STRIP[1], 3.954)
    print(f"     row 1476's asymptotic form, C at mean 3.954: {mid:.6f} (C at the ends: {lo:.6f} to {hi:.6f})")
    print()

    g1 = GATE_1
    g53 = GATE_1 / M_NEXT
    print(f"[2] THE_BAR's gate: p < 0.01; at the joint look count m = {M_NEXT}: p < {g53:.3e}")
    print(f"    bits: log2(1/P(S)) = {math.log2(1 / p_f):.2f} (followed), {math.log2(1 / p_c):.2f} (counted);"
          f" the gate at m = {M_NEXT} needs {math.log2(1 / g53):.2f} bits; at m = 1, {math.log2(1 / g1):.2f}")
    print()

    # [3] the window at the centre whose null probability equals the gate
    def width_followed(g):
        lo_, hi_ = 0.0, 1.0
        for _ in range(200):
            w = 0.5 * (lo_ + hi_)
            if followed_interval(CENTRE - w / 2, CENTRE + w / 2) > g:
                hi_ = w
            else:
                lo_ = w
        return 0.5 * (lo_ + hi_)
    # the counted clock's density at the centre, from the strip's mean density (the tail is smooth there)
    dens_c = p_c / (STRIP[1] - STRIP[0])
    w_f = width_followed(g53)
    w_c = g53 / dens_c
    print(f"[3] window at Im tau = {CENTRE} with null probability {g53:.3e}:")
    print(f"    followed: width {w_f:.5f};  counted (strip-mean density {dens_c:.5f} per unit height): width {w_c:.5f}")
    print()

    # [4] the six's resolution and a correct law's chance to land in such a window
    sigma = 0.1 / math.sqrt(34.0 - 2.66)
    def p_in(w):
        return math.erf(w / (2.0 * math.sqrt(2.0) * sigma))
    print(f"[4] the six's resolution in Im tau (quadratic through P-373's chi2 2.66 -> 34 at +-0.1; illustrative): sigma = {sigma:.4f}")
    print(f"    an exactly right law's window contains the six's best height with probability {p_in(w_f):.3f} (followed), {p_in(w_c):.3f} (counted)")
    print(f"    for comparison, the whole strip's width {STRIP[1] - STRIP[0]:.2f} would hold it with probability {p_in(STRIP[1] - STRIP[0]):.3f}")


if __name__ == "__main__":
    main()
