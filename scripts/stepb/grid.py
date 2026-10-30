"""STEP B's generator, the refined census's tau cells and their measures (data-free).

The grid (REFINED_CENSUS_PLAN.md section 6): Re tau = 0, 0.05, ..., 0.5 and Im tau = 1.0, 1.05, ..., 4.0, plus a
0.025 x 0.025 sub-block on Re 0-0.5 x Im 1.0-1.5.  Each point owns the rectangle of half-steps around it, clipped to the
band Re in [0, 1/2], Im in [1, 4]; inside the sub-block the steps are 0.025 in both directions.  With the mirror the band
Re in [-1/2, 1/2] is covered by these cells and their reflections.  Measures: hyperbolic area dx dy / y^2 (primary) and a
Weil-Petersson density supplied as a function of Im tau (a read-out)."""
from __future__ import annotations

import numpy as np

SUB_IM, SUB_RE = (1.0, 1.5), (0.0, 0.5)


def steps(re: float, im: float):
    inside = SUB_IM[0] - 1e-9 <= im <= SUB_IM[1] + 1e-9 and SUB_RE[0] - 1e-9 <= re <= SUB_RE[1] + 1e-9
    return (0.025, 0.025) if inside else (0.05, 0.05)


def cell(re: float, im: float):
    """(x0, x1, y0, y1) of the point's cell, clipped to the band, chosen so that every cell lies inside its interpolation
    stencil's range (the fourth review's F1; no extrapolation): the sub-block's top row (Im = 1.5) owns only its half-step
    below, [1.4875, 1.5]; the main grid's row at Im = 1.55 owns [1.5, 1.575], reaching down to the sub-block's edge."""
    dre, dim = steps(re, im)
    x0, x1 = max(0.0, re - dre / 2), min(0.5, re + dre / 2)
    if abs(im - SUB_IM[1]) < 1e-9:
        y0, y1 = im - 0.0125, im
    elif abs(im - (SUB_IM[1] + 0.05)) < 1e-9:
        y0, y1 = SUB_IM[1], im + 0.025
    else:
        y0, y1 = max(1.0, im - dim / 2), min(4.0, im + dim / 2)
    return x0, x1, y0, y1


def area_weights(points) -> np.ndarray:
    """hyperbolic area of each point's cell (dx dy / y^2), normalised over the band; points as (re, im)"""
    w = []
    for re, im in points:
        x0, x1, y0, y1 = cell(re, im)
        w.append((x1 - x0) * (1.0 / y0 - 1.0 / y1))
    w = np.array(w)
    return w / w.sum()


def band_area() -> float:
    """the band's hyperbolic area for Re in [0, 1/2], Im in [1, 4]: (1/2)(1 - 1/4) = 3/8"""
    return 0.5 * (1.0 - 0.25)
