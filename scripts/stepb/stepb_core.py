"""STEP B's generator, the core (GENERATOR_IMPLEMENTATION_PLAN.md; data-free).  Pure functions of a census and a target.

Conventions, each taken from the record's sealed instruments:
- the six, in this order: (c/t, u/t, s/b, d/b, mu/tau, e/tau) = per sector (m2/m3, m1/m3) (B1741 compare.py).  The census
  stores per sector (m1/m3, m2/m3) (B1821's evaluator, cm_zero_line.py line 75); `features` swaps them.
- the nine add (|V_us|, |V_cb|, |V_ub|) (B1741); the ten add |J| (the second review's item 5: J enters S; its sign is
  never scored, B1821).  `features` returns the ten.
- the misfit: chi2 in NATURAL log, sigma per quantity the relative error in quadrature with ALLOW = 0.10 (B1741's sigmas()).
- the lepton factor c multiplies mu/tau and divides e/tau (B1726, B1741): in log space +log c and -log c.
- the nine values of c the data's scan used: {1/3, 1/2, 2/3, 1, 3/2, 2, 3, 4, 5} (B1798 section 4).
- the support threshold: chi2_ten below 23.21, the 0.99 quantile of chi2_10, which keeps B1747's tail (21.67 is chi2_9's);
  chi2_nine below 21.67 is a read-out (main's ruling on the third review's B2).  Only rows with the mixing defined.
- c: our world is scored at c = 3 only; every null world scans the nine values and keeps its best (the third review's B1;
  the second review's item 6).  Every function takes the c values as an argument.
Nothing here reads a file of measured values: sigma and the target are arguments."""
from __future__ import annotations

import math
from dataclasses import dataclass, field

import numpy as np

ALLOW = 0.10
C_SCAN = (1 / 3, 1 / 2, 2 / 3, 1.0, 3 / 2, 2.0, 3.0, 4.0, 5.0)
SUPPORT_THRESHOLD = 23.209251158954356        # chi2.ppf(0.99, 10)
THRESHOLD_NINE = 21.665994333461924           # chi2.ppf(0.99, 9), B1747's 21.67 (a read-out)
CKM_LEG_THRESHOLD = 13.276704135987622        # chi2.ppf(0.99, 4): the CKM leg's own support clause
C_OURS = (3.0,)                               # our world (P-495, the bar's C5)
C_ARM1 = (1.0,)                               # the clean read-out arm
N_DIRS = 13                       # B1810's thirteen; two of them (a0, F_-2) are one direction (B1824)
N_RADII = 2
READINGS = ("SSS", "SSSt", "SStS", "SStSt", "StSS", "StSSt", "StStS", "StStSt")


@dataclass
class Census:
    """rows as arrays.  cfg: index of the (line, tau) configuration; d, r, k: direction, radius, reading indices.
    m: (n, 3, 2) the census's per-sector (m1/m3, m2/m3); v: (n, 3) |V|; J: (n,); vdef: (n,) bool.
    lines: per cfg the line key; tau: (n_cfg, 2) (Re, Im)."""
    cfg: np.ndarray
    d: np.ndarray
    r: np.ndarray
    k: np.ndarray
    m: np.ndarray
    v: np.ndarray
    J: np.ndarray
    vdef: np.ndarray
    lines: list = field(default_factory=list)
    tau: np.ndarray = None

    def __post_init__(self):
        n = len(self.cfg)
        for name in ("d", "r", "k", "J", "vdef"):
            assert len(getattr(self, name)) == n, name
        assert self.m.shape == (n, 3, 2) and self.v.shape == (n, 3)


def features(c: Census) -> np.ndarray:
    """(n, 10) natural-log features: per sector (m2/m3, m1/m3), then |V_us|, |V_cb|, |V_ub|, then |J|.
    Rows with a non-positive output get -inf in that slot, so they can never fall inside a finite ball."""
    m = np.asarray(c.m, dtype=float)
    six = np.stack([m[:, 0, 1], m[:, 0, 0], m[:, 1, 1], m[:, 1, 0], m[:, 2, 1], m[:, 2, 0]], axis=1)
    four = np.concatenate([np.asarray(c.v, float), np.abs(np.asarray(c.J, float))[:, None]], axis=1)
    with np.errstate(divide="ignore", invalid="ignore"):
        F6 = np.where(six > 0, np.log(six), -np.inf)
        F4 = np.where(four > 0, np.log(four), -np.inf)
    return np.concatenate([F6, F4], axis=1)


def c_shift(cval: float) -> np.ndarray:
    """the lepton factor as an additive shift on the ten log features: +log c on mu/tau, -log c on e/tau"""
    s = np.zeros(10)
    s[4], s[5] = math.log(cval), -math.log(cval)
    return s


def sigma_from_relative(rel6, rel4, allow: float = ALLOW) -> np.ndarray:
    """B1741's sigmas(): per quantity sqrt(relative error^2 [+ the other member's for a ratio, already combined in rel6] + ALLOW^2);
    rel4 = the three moduli's and |J|'s relative errors"""
    rel = np.concatenate([np.asarray(rel6, float), np.asarray(rel4, float)])
    assert rel.shape == (10,)
    return np.sqrt(rel ** 2 + allow ** 2)


def chi2(F: np.ndarray, target_log: np.ndarray, sigma: np.ndarray, cval: float, q: int = 10) -> np.ndarray:
    """per row chi2 against one target (natural-log), at lepton factor c, over the first q quantities (6, 9 or 10)"""
    assert q in (6, 9, 10)
    X = (F[:, :q] + c_shift(cval)[:q] - target_log[:q]) / sigma[:q]
    out = np.einsum("ij,ij->i", X, X)
    return np.where(np.isfinite(out), out, np.inf)


def support(c: Census, F: np.ndarray, target_log, sigma, c_values=C_SCAN, threshold: float = SUPPORT_THRESHOLD, q: int = 10):
    """bar S1 at the census's nodes: over every row with the mixing defined and every c given, the least chi2_q, the rows
    below the threshold (row index, c value), and the best row.  Brute force; the k-d screen (screen.py) must agree.
    (Continuous tau through the interpolant is interp.py's; this is the node-level reference.)"""
    ok = np.asarray(c.vdef, bool)
    best = (math.inf, None, None); below = []
    for cv in c_values:
        x2 = chi2(F, np.asarray(target_log, float), np.asarray(sigma, float), cv, q=q)
        x2 = np.where(ok, x2, np.inf)
        i = int(np.argmin(x2))
        if x2[i] < best[0]:
            best = (float(x2[i]), i, cv)
        hit = np.nonzero(x2 < threshold)[0]
        below.extend((int(j), cv) for j in hit)
    return {"min_chi2": best[0], "best_row": best[1], "best_c": best[2], "below": below,
            "in_support": best[0] < threshold, "q": q, "c_values": tuple(c_values)}


def clopper_pearson_upper(k: int, n: int, conf: float = 0.975) -> float:
    """the upper end of the exact two-sided 95% interval of a binomial rate (THE_BAR, B1798, the second review's NB13: each p
    decided on its Clopper-Pearson 95% bound = the beta quantile at 0.975)"""
    from scipy.stats import beta
    if k >= n:
        return 1.0
    return float(beta.ppf(conf, k + 1, n - k))


def null_six(rng: np.random.Generator, n: int) -> np.ndarray:
    """B1741's random hierarchies for the six (its draws(), r_masses): per sector r2 = 10^U(-3,-1), r1 = 10^U(-6,-2.5),
    redrawn until r1 < r2; returned as natural logs in the six's order (r2, r1) per sector.  Vectorised by rejection."""
    out = np.empty((n, 6))
    for s in range(3):
        need = np.arange(n)
        r2 = np.empty(n); r1 = np.empty(n)
        while len(need):
            a = 10 ** rng.uniform(-3, -1, len(need)); b = 10 ** rng.uniform(-6, -2.5, len(need))
            good = b < a
            r2[need[good]] = a[good]; r1[need[good]] = b[good]
            need = need[~good]
        out[:, 2 * s], out[:, 2 * s + 1] = np.log(r2), np.log(r1)
    return out
