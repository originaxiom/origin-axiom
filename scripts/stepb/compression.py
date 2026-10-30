"""STEP B's generator, the compression cell K (the bar's K1, K2; the second review's K1 ruling; data-free).

Definitions (each to be fixed on the card before Stage B; the second pre-seal review's rulings in brackets):
- precision: each of the six is coded to a cell of width sigma_i in natural-log units (the targets' own sigma, B1741).
- L_raw [ruling 3: "L_raw is the primary null's own code length"]: -log2 of the primary null's probability of the target's
  cell, with B1741's box (per sector ln r2 uniform on [-3, -1] ln 10, ln r1 on [-6, -2.5] ln 10, restricted to r1 < r2):
  L_raw = sum over sectors of log2(area of the sector's region / (sigma_2 sigma_1)) (inside the region; +inf outside).
- the misfit code of a target given a row: M = (chi2_six / 2) log2(e) + 6 log2(sqrt(2 pi)) (a Gaussian at sigma, cell
  width sigma).
- the address, two-part over the discrete choices: log2(266) + log2(12) + 1 + 3 + log2(9) for (line, direction, radius,
  reading, c) [the directions priced as twelve, B1824], with tau MIXED, not chosen: for each discrete choice d,
  L_tau(d) = -log2 sum_tau w(tau) 2^(-M(target | d, tau)), w the hyperbolic-area weights of the census's tau cells,
  normalised over the band [the design section 5: "tau's price: a mixture code under hyperbolic area"].
- L_ours = min over d of [A_d + L_tau(d)]; C = L_raw - L_ours; the framework's own length is reported apart (it cancels
  against the null, whose worlds pay the same).
- p_K = the fraction of null worlds whose L is at most L_ours, with the free check p_K <= 2^-C (no-hypercompression:
  under the primary null, P(L_raw - L >= C) <= 2^-C for any prefix code L)."""
from __future__ import annotations

import math

import numpy as np

import stepb_core as C

LOG2E = math.log2(math.e)
MISFIT_CONST6 = 6 * math.log2(math.sqrt(2 * math.pi))
A_DISCRETE = math.log2(266) + math.log2(12) + 1 + 3 + math.log2(9)
LN10 = math.log(10)
# B1741's box per sector, natural log: x = ln r2 in [X0, X1], y = ln r1 in [Y0, Y1], region y < x
X0, X1, Y0, Y1 = -3 * LN10, -1 * LN10, -6 * LN10, -2.5 * LN10


def region_area() -> float:
    """area of {X0 <= x <= X1, Y0 <= y <= Y1, y < x}: the full box minus the part with y >= x"""
    full = (X1 - X0) * (Y1 - Y0)
    # y >= x inside the box: x in [X0, min(X1, Y1)], y in [max(x, Y0), Y1]; here X0 = -6.9 > Y0 = -13.8, Y1 = -5.76 < X1
    lo, hi = X0, min(X1, Y1)
    cut = 0.0 if hi <= lo else _cut(lo, hi)
    return full - cut


def _cut(lo, hi):
    # integral over x in [lo, hi] of (Y1 - max(x, Y0)) dx; with Y0 < lo every x > Y0, so (Y1 - x)
    return (Y1 - lo) ** 2 / 2.0 - (Y1 - hi) ** 2 / 2.0


def in_box(t6: np.ndarray) -> bool:
    for s in range(3):
        x, y = t6[2 * s], t6[2 * s + 1]
        if not (X0 <= x <= X1 and Y0 <= y <= Y1 and y < x):
            return False
    return True


def L_raw(t6, sigma6) -> float:
    t6 = np.asarray(t6, float); s = np.asarray(sigma6, float)
    if not in_box(t6):
        return math.inf
    A = region_area()
    return float(sum(math.log2(A / (s[2 * k] * s[2 * k + 1])) for k in range(3)))


def misfit_bits(chi2_six: np.ndarray) -> np.ndarray:
    return chi2_six / 2.0 * LOG2E + MISFIT_CONST6


# ---- K over the ten (main's ruling on the third review's B4/B5; generator_review_3/MAIN_RULINGS.md) ----
GATE_ALPHA = 0.01


def gate_bits(m: int) -> float:
    """the bits a compression must carry for a 2^-C bound alone to clear the gate 0.01/m (12.37 at m = 53)"""
    assert m >= 53, "m is the joint look ledger's count plus one, at least 53"
    return math.log2(m / GATE_ALPHA)


def check_markov(k: int, n: int, C_bits: float) -> bool:
    """the free pipeline check (no-hypercompression): under the primary null, P0(C >= c) <= 2^-c for the framework's prefix
    code.  With k of n null worlds at C >= C_bits, the two-sided 95% Clopper-Pearson LOWER end of k/n must not exceed
    2^-C_bits; False means the pipeline is inconsistent (a bug or a code that is not prefix).  Exact for the C-based rarity;
    the bar's p_K is L-based and equals it where the null's density is flat (the six's box)."""
    from scipy.stats import beta
    lower = 0.0 if k == 0 else float(beta.ppf(0.025, k, n - k + 1))
    return lower <= 2.0 ** (-C_bits) + 1e-15
