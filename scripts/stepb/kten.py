"""STEP B's generator, K over the ten and the CKM leg's statistic on continuous tau, through the cell index (cells.py; main's
rulings after the interpolant's diagnosis, 2026-10-30, replacing continuous_k's 4 x 4 rule; data-free).

THE MIXTURE.  For a choice j (line, direction, radius, reading) and a target, the six's tau mixture is
    Q_j = sum over the cells of j's rows of the integral of 2^-M(six(tau)) dmu(tau),    M = compression.misfit_bits,
dmu = dx dy / y^2 normalised over the band (each half 3/8; a row appears in its own line's half and, mirrored, in its
partner's), and L_six = A + min_j (-log2 Q_j).  The four's code: the posterior over the six's window (weights the six's
integrand) predicts the CKM by Gaussian kernels; the reference is the frame's unconditional marginal (every row's cell under
the prior dmu); bits_CKM = log2 p_post(y4) - log2 p_marg(y4); C_ten = C_six + bits_CKM (the fourth review's F3).

THE QUADRATURE (measured on the mini patch, sigma = ALLOW: a choice's total at n x n Gauss per cell against n = 96 errs up to
6.5 bits at n = 4, 0.57 at n = 8, 0.004 at n = 16, ~1e-9 at n = 32).  Tier 1: every window row at 4 x 4.  Tier 2: every
row whose RIGOROUS upper bound (its cell measure x the integrand's bound at its enclosure's least chi2) exceeds 2^-34 of the
tier-1 total, at 16 x 16 (a choice whose rows all stay below can carry at most 2^-23 of the total, so it is never the
best).  The check: the rows carrying the top 1 - 2^-20 of the mass at 32 x 32; if the total moves by more than 0.01 bits,
the 32 x 32 values are used and a 64 x 64 check is reported.

THE WINDOWS (rigorous).  The six: rows whose enclosure's least chi2_six is below ub + D, ub the best node's chi2_six (an
attained value); the dropped mass is at most n_rows x the largest cell measure x 2^-M(ub + D), and D doubles until that is
below 2^-30 of the computed total.  The CKM marginal: rows whose enclosure's least chi2_4 is below X (first 12^2), with the
same bound against its total.  The posterior's numerator: the six's window, with its dropped part bounded likewise."""
from __future__ import annotations

import math

import numpy as np

import compression as K
import stepb_core as C
from cells import CellIndex

LOG2E = math.log2(math.e)
SIX, FOUR = tuple(range(6)), (6, 7, 8, 9)
TIER2_BITS = 34.0
CHECK_MASS_BITS = 20.0
CHECK_TOL_BITS = 0.01
DROP_BITS = 30.0
D0 = 2 * math.log(2) * 40.0
CHUNK_POINTS = 1 << 21          # 2M points x 10 features x 8 bytes = 168 MB a chunk


def lse2(a) -> float:
    a = np.asarray(a, float).ravel()
    if not len(a):
        return -math.inf
    top = np.max(a)
    return -math.inf if not np.isfinite(top) else float(top + math.log2(np.exp2(a - top).sum()))


def lse2_rows(a):
    top = np.max(a, axis=1, keepdims=True)
    fin = np.isfinite(top[:, 0])
    out = np.full(a.shape[0], -np.inf)
    out[fin] = (top[fin, 0] + np.log2(np.exp2(a[fin] - top[fin]).sum(axis=1)))
    return out


def kernel_log2(f4, y4, s4):
    z = (f4 - y4) / s4
    return -0.5 * np.einsum("...k,...k->...", z, z) * LOG2E - float(np.log2(np.sqrt(2 * np.pi) * s4).sum())


class Integrand:
    """log2 of the integrand at features f (..., 10): the six's 2^-M (with the c shift folded into tt), optionally times the
    CKM kernel at y4; and its rigorous per-row upper bound from the enclosure"""

    def __init__(self, ci: CellIndex, tt, six=True, ckm=False):
        self.ci, self.tt, self.six, self.ckm = ci, np.asarray(tt, float), six, ckm
        self.s = ci.sig

    def __call__(self, f):
        out = np.zeros(f.shape[:-1])
        if self.six:
            z = (f[..., :6] - self.tt[:6]) / self.s[:6]
            out = out - K.misfit_bits(np.einsum("...k,...k->...", z, z))
        if self.ckm:
            out = out + kernel_log2(f[..., 6:10], self.tt[6:10], self.s[6:10])
        return np.where(np.isfinite(out), out, -np.inf)

    def upper(self, rows):
        out = self.ci.log2_cell_measure(rows)
        if self.six:
            out = out - K.misfit_bits(self.ci.chi2_lower(rows, self.tt, SIX))
        if self.ckm:
            out = out - 0.5 * self.ci.chi2_lower(rows, self.tt, FOUR) * LOG2E - float(np.log2(np.sqrt(2 * np.pi) * self.s[6:10]).sum())
        return out


def integrals(ci, rows, g: Integrand, n: int):
    """per-row log2 integrals at n x n Gauss points (chunked)"""
    rows = np.asarray(rows, np.int64); out = np.empty(len(rows))
    step = max(16, CHUNK_POINTS // (n * n))                        # bounded transients: about CHUNK_POINTS points a chunk
    for a in range(0, len(rows), step):
        r = rows[a:a + step]
        V, LW = ci.gauss(r, n)
        out[a:a + step] = lse2_rows(LW + g(V))
    return out


def tiered(ci, rows, g: Integrand) -> tuple:
    """(per-row log2 integrals, report): tier 1 at 4 x 4, tier 2 at 16 x 16 above 2^-34 of the total by the rigorous bound,
    the 32 x 32 check on the rows carrying 1 - 2^-20 of the mass"""
    rows = np.asarray(rows, np.int64)
    if not len(rows):
        return np.zeros(0), {"rows": 0}
    I = integrals(ci, rows, g, 4); tot4 = lse2(I)
    U = g.upper(rows)
    sel = np.nonzero(U > tot4 - TIER2_BITS)[0] if np.isfinite(tot4) else np.arange(len(rows))
    if len(sel):
        I[sel] = integrals(ci, rows[sel], g, 16)
    tot = lse2(I)
    rep = {"rows": int(len(rows)), "tier2": int(len(sel)), "total_bits": tot}
    if not np.isfinite(tot):
        return I, rep
    order = np.argsort(-I); frac = np.cumsum(np.exp2(I[order] - tot))
    top = order[:int(np.searchsorted(frac, 1 - 2.0 ** -CHECK_MASS_BITS) + 1)]
    I32 = integrals(ci, rows[top], g, 32)
    J = I.copy(); J[top] = I32; d32 = abs(lse2(J) - tot)
    rep.update(check_rows=int(len(top)), delta32=d32)
    if d32 > CHECK_TOL_BITS:
        I = J; I64 = integrals(ci, rows[top], g, 64); J2 = I.copy(); J2[top] = I64
        rep.update(used32=True, delta64=abs(lse2(J2) - lse2(I)))
    return I, rep


def best_node_chi2(ci: CellIndex, tt, space, comps) -> float:
    """the least chi2 over comps at a node (an attained value of the interpolant): candidates in the space's ball bound
    (a node with chi2 below x2 is always among them), x2 raised to the least found until it is the least over all nodes"""
    x2 = 4.0
    while True:
        cand = ci.candidates(space, tt, x2)
        m = float(ci._x2(ci.feat(ci.coords(cand)), tt, comps).min()) if len(cand) else math.inf
        if m <= x2:
            return m
        if not math.isfinite(m):
            if x2 > 1e12:
                return math.inf
            x2 *= 16.0
        else:
            x2 = m


def window(ci, tt, space, comps, x2max, physical=False):
    cand = ci.candidates(space, tt, x2max)
    if physical and len(cand):
        cand = cand[ci.phys[cand]]
    if not len(cand):
        return cand
    return cand[ci.chi2_lower(cand, tt, comps) < x2max]


def windowed(ci: CellIndex, tt, g: "Integrand", space, comps, const_bits: float, physical=False) -> tuple:
    """(rows, per-row log2 integrals, report) over the window {rows: the enclosure's least chi2 over comps < ub + D}, ub the
    least node chi2; the integrand is at most 2^-(chi2/2 log2 e + const_bits); D doubles until the rows outside (at most
    n_rows x the largest cell measure x that bound at ub + D) carry less than 2^-30 of the window's total"""
    ub = best_node_chi2(ci, tt, space, comps)
    if not math.isfinite(ub):
        return np.zeros(0, np.int64), np.zeros(0), {"rows": 0, "total_bits": -math.inf}
    lm = ci.measure_totals()[0]; ln = math.log2(max(1, len(ci.rows))); D = D0
    while True:
        rows = window(ci, tt, space, comps, ub + D, physical)
        I, rep = tiered(ci, rows, g); tot = lse2(I)
        drop = ln + lm - (ub + D) / 2 * LOG2E - const_bits
        if drop <= tot - DROP_BITS or len(rows) == len(ci.rows):
            rep.update(ub=ub, D=D, drop_bits_rel=drop - tot)
            return rows, I, rep
        D *= 2.0


def six_mixture(ci: CellIndex, tt) -> dict:
    """the six's window (rigorous), its per-row integrals (tiered), and per choice -log2 Q_j"""
    rows, I, rep = windowed(ci, tt, Integrand(ci, tt, six=True), "six", SIX, K.MISFIT_CONST6)
    if not len(rows):
        return {"L_tau": math.inf}
    per = {}
    for a, i in enumerate(rows):
        for j in (ci.choice[i], ci.partner[i]):
            if j >= 0:
                per.setdefault(int(j), []).append(I[a])
    Lt = {j: -lse2(v) for j, v in per.items()}
    jbest = min(Lt, key=Lt.get)
    return {"L_tau": Lt[jbest], "choice": jbest, "rows": rows, "I": I, "report": rep}


def K_ten(ci: CellIndex, t10, c_values) -> dict:
    t10 = np.asarray(t10, float); s = ci.sig
    L_raw6 = K.L_raw(t10[:6], s[:6])
    if not math.isfinite(L_raw6):
        return {"grade": "UNJUDGED", "reason": "the six lie outside the primary null's box"}
    best = None
    for cv in c_values:
        tt = t10 - C.c_shift(cv)
        m = six_mixture(ci, tt)
        if math.isfinite(m["L_tau"]) and (best is None or K.A_DISCRETE + m["L_tau"] < best[0]):
            best = (K.A_DISCRETE + m["L_tau"], cv, tt, m)
    if best is None:
        return {"grade": "UNJUDGED", "reason": "no row reached"}
    L6, cbest, tt, m = best
    k4 = float(np.log2(np.sqrt(2 * np.pi) * s[6:10]).sum())
    # the posterior predictive at the four: numerator int 2^-M kernel (its own window on the ten), denominator int 2^-M
    # (the six's window, every choice); the marginal: int kernel over every row's cell / the prior mass (exact)
    rn, In, repn = windowed(ci, tt, Integrand(ci, tt, six=True, ckm=True), "nine", tuple(range(10)), K.MISFIT_CONST6 + k4)
    num, den = lse2(In), lse2(m["I"])
    # the marginal is the null's own (BL1): the physical choices only, normalised over their prior mass (so the Markov
    # bound P(bits >= b) <= 2^-b is exact under the null that draws from it)
    rm, Im, repm = windowed(ci, tt, Integrand(ci, tt, six=False, ckm=True), "ckm3", FOUR, k4, physical=True)
    lp_marg = lse2(Im) - ci.measure_totals()[1]
    lp_post = num - den
    bits = lp_post - lp_marg
    C_six = L_raw6 - L6
    drop = max(m["report"].get("drop_bits_rel", -math.inf), repn.get("drop_bits_rel", -math.inf), repm.get("drop_bits_rel", -math.inf))
    return {"grade": "JUDGED", "L_six": L6, "C_six": C_six, "bits_CKM": bits, "C_ten": C_six + bits, "c": cbest,
            "choice": m["choice"], "six_report": m["report"], "num_report": repn, "marg_report": repm,
            "drop_bits_rel": drop, "converged": converged(m["report"], repn, repm) and drop <= -DROP_BITS}


def converged(*reports) -> bool:
    """the quadrature's checks (the fifth review's N2): each tiered integral's 32 x 32 check within CHECK_TOL_BITS, or, where
    it was not and the 32 x 32 values were used, the 64 x 64 check within it"""
    for r in reports:
        if not r.get("rows"):
            continue
        d32 = r.get("delta32")
        if d32 is None:
            return False
        if d32 > CHECK_TOL_BITS and not (r.get("used32") and r.get("delta64", math.inf) <= CHECK_TOL_BITS):
            return False
    return True


def K_ten_brute(ci: CellIndex, t10, c_values, n: int = 32) -> dict:
    """every row at n x n Gauss points (the reference the tiered windows must equal)"""
    t10 = np.asarray(t10, float); s = ci.sig; best = None
    for cv in c_values:
        tt = t10 - C.c_shift(cv)
        I = integrals(ci, ci.rows, Integrand(ci, tt, six=True), n)
        per = {}
        for a, i in enumerate(ci.rows):
            for j in (ci.choice[i], ci.partner[i]):
                if j >= 0:
                    per.setdefault(int(j), []).append(I[a])
        L = K.A_DISCRETE + min(-lse2(v) for v in per.values())
        if best is None or L < best[0]:
            best = (L, cv, tt, I)
    L6, cv, tt, I = best
    In = integrals(ci, ci.rows, Integrand(ci, tt, six=True, ckm=True), n)
    lp_post = lse2(In) - lse2(I)
    pr = ci.rows[ci.phys[ci.rows]]
    Im = integrals(ci, pr, Integrand(ci, tt, six=False, ckm=True), n)
    lp_marg = lse2(Im) - lse2(ci.log2_cell_measure(pr))
    C_six = K.L_raw(t10[:6], s[:6]) - L6
    return {"L_six": L6, "bits_CKM": lp_post - lp_marg, "C_ten": C_six + lp_post - lp_marg, "c": cv}


CLAUSE_DCHI2 = 20.0 / LOG2E          # within 2^-10 of the posterior's top: the six's chi2 within 13.86 of its least


def ckm_clause(ci: CellIndex, tt, T4=C.CKM_LEG_THRESHOLD) -> dict:
    """the CKM leg's own support clause on continuous tau: an address the six support -- its chi2_six within 13.86 of the
    least over every cell (posterior density within 2^-10 of the top) -- reaching the four with chi2_4 < 13.28.  The least
    chi2_six by branch-and-bound (relative 1e-3, and the bound widened by that tolerance, so no address is lost); then every
    row whose enclosures allow both, until one cell holds such a point"""
    g = ci.global_min(tt, (1.0,), comps=SIX, space="six")          # tt already c-shifted: c = 1 adds no shift
    if not math.isfinite(g["min_chi2"]):
        return {"clause": False, "min_chi2_six": math.inf, "best_chi2_4": math.inf, "undecided": 0}
    bound = g["min_chi2"] * (1 + 1e-3) + 1e-3 + CLAUSE_DCHI2
    cand = window(ci, tt, "six", SIX, bound)
    if len(cand):
        cand = cand[ci.chi2_lower(cand, tt, FOUR) < T4]
    best4, und = math.inf, 0
    for i in cand[np.argsort(ci.chi2_lower(cand, tt, FOUR))] if len(cand) else []:
        st, b4, _ = ci.cell_find2(int(i), tt, SIX, bound, FOUR, T4)
        best4 = min(best4, b4); und += st == "undecided"
        if st == "found":
            return {"clause": True, "min_chi2_six": g["min_chi2"], "best_chi2_4": b4, "undecided": und}
    return {"clause": False, "min_chi2_six": g["min_chi2"], "best_chi2_4": best4, "undecided": und}
