"""STEP B's generator, T1 (the bar's typicality screen; data-free): the two-sided tail of our depth y0 under a clock's law
of Im tau on the declared band, t = 2 min(P(Im <= y0), P(Im >= y0)); NEGATIVE if t < 0.01 (a screen, CONDITIONAL on the
bar's section 0 premise).  Hyperbolic area is exact here; other clocks (WP, followed, counted) enter as their CDFs on the
band, supplied from the record's committed computations (B1813, B1815, B1816) when the card is written."""
from __future__ import annotations

Y_LO, Y_HI = 1.0, 4.0


def area_cdf(y: float) -> float:
    """P(Im tau <= y) under dx dy / y^2 on Re in [-1/2, 1/2], Im in [1, 4] (the declared band; its ends are CHOSEN)"""
    y = min(max(y, Y_LO), Y_HI)
    return (1.0 / Y_LO - 1.0 / y) / (1.0 / Y_LO - 1.0 / Y_HI)


def two_sided_tail(cdf, y0: float) -> float:
    p = cdf(y0)
    return 2.0 * min(p, 1.0 - p)


def T1(cdf, y0: float) -> dict:
    """the fourth review's F5: a non-finite depth or tail raises (it can never be read as CONSISTENT)"""
    import math
    if y0 is None or not math.isfinite(y0):
        raise ValueError("T1 needs a finite depth y0, got %r" % (y0,))
    t = two_sided_tail(cdf, y0)
    if not math.isfinite(t) or t < 0 or t > 1:
        raise ValueError("T1's tail is not a probability: %r" % (t,))
    return {"y0": y0, "t": t, "grade": "NEGATIVE" if t < 0.01 else "CONSISTENT"}
