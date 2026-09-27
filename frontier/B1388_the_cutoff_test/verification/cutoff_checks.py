#!/usr/bin/env python3
"""B1388 -- the two checks that decide whether a transition found by cutoff_test.py is the harmonic form's or the truncation's.

(a) Re-solve at a higher mode cut-off (K_n = 20, against the sealed run's 14) and locate cusp 0's transitions again. A real
    transition does not move.
(b) Evaluate the torus function independently, not from cusp 0's truncated expansion. Points of cusp 0's horotorus at heights h and
    h +- delta are pulled back into the fundamental polyhedron and F is read from the chart where each point sits highest (so every
    evaluation is at normalised height >= 0.11, where the expansions are accurate). Then g = dF/dh by central differences, and
    chi({g > 0}) on the grid.
    Both evaluations are compared at tau = 0.12, 0.15, 0.25, on the two sides of the transition cutoff_test.py finds at 0.187 and
    inside the interval where it reports chi = +2.
Usage: python3 cutoff_checks.py"""
import math
import random
import sys
import time
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")
import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import cutoff_test as CT                        # the sealed test's own functions (it loads B1387's instrument as CT.HF)

HF, T = CT.HF, CT.T


def F_global(S, x, y_chart, c):
    """F at the chart-c point y, read from ANOTHER cusp's expansion: the point is pulled back into the polyhedron and F is taken
    from the highest vertex of its tetrahedron that belongs to a cusp other than c, so cusp c's own coefficients are not used"""
    i0 = next(i for i in range(S.P.ntet) for vv in HF.V if S.P.vclass[i][vv] == S.C.base[c])
    i, Ps, acc, _ = S.P.walk(i0, HF.act(S.C.A[c], y_chart), S.v)
    best = None
    for vv in HF.V:
        u = S.P.vclass[i][vv]
        cc = S.C.cusp_of_vertex[u]
        if cc == c:
            continue
        y = S.C.to_chart(cc, u, Ps)
        if best is None or y[1] / S.s[cc] > best[0]:
            best = (y[1] / S.s[cc], cc, u, y)
    if best is None:                                  # every vertex of the tetrahedron belongs to cusp c: step to a neighbour
        raise RuntimeError("no other cusp at this tetrahedron")
    tb, cb, ub, yb = best
    return float(S.row(cb, yb) @ x) - S.C.vgam[ub] + acc, tb


def g_grid_independent(S, x, c, tau, n=90, rel_delta=1e-3):
    b1, b2 = S.C.lat[c]
    h = tau * S.s[c]
    d = rel_delta * h
    G = np.zeros((n, n))
    low = 1e9
    for a in range(n):
        for b in range(n):
            w = (a / n) * b1 + (b / n) * b2
            try:
                fp, t1 = F_global(S, x, (w, h + d), c)
                fm, t2 = F_global(S, x, (w, h - d), c)
            except RuntimeError:
                G[a, b] = np.nan
                continue
            G[a, b] = (fp - fm) / (2 * d)
            low = min(low, t1, t2)
    return G, low


def g_grid_expansion(S, x, c, tau, n=90):
    terms = CT.torus_terms(S, x, c, tau * S.s[c])
    return T.grid_values(terms, n)


if __name__ == "__main__":
    t0 = time.time()
    M = HF.member()
    print("=== (a) the transitions at cusp 0 under a higher mode cut-off ===", flush=True)
    for Kn in (14, 20):                                   # (the K_n = 20 solve is kept for (b))
        S, x, st = HF.solve(M, Kn, 0.10, 1, 1)
        emb = CT.embedded_heights(M, S)
        rows, trans = CT.scan(S, x, 0, emb[0]["tau_emb"], n=40)
        print("K_n %d (unknowns %d, fit residual %.1e, test residual %.1e): chi values %s; transitions %s" % (
            Kn, st["unknowns"], st["fit residual rms"], st["test residual rms"], sorted(set(r[1] for r in rows)),
            [(round(lo, 5), a, b) for lo, hi, a, b in trans]), flush=True)
    print("=== (b) the torus function at cusp 0, independently evaluated (K_n = 20 solve) ===", flush=True)
    for tau in (0.12, 0.15):
        Gi, low = g_grid_independent(S, x, 0, tau)
        Ge = g_grid_expansion(S, x, 0, tau)
        ok = ~np.isnan(Gi)
        scale = np.abs(Ge).max()
        diff = np.abs(Gi[ok] - Ge[ok]).max() / scale
        signs = float(np.mean(np.sign(Gi[ok]) == np.sign(Ge[ok])))
        chi_e = T.chi_grid(Ge > 0)
        chi_i = T.chi_grid(np.where(ok, Gi, Ge) > 0) if ok.all() else None
        print("tau %.2f: points read from another cusp's chart %d/%d; lowest height of those readings %.3f; max |other-chart - cusp-0 "
              "expansion| / max = %.2e; signs agreeing %.4f; chi(d+) other-chart %s, cusp-0 expansion %+d" % (
                  tau, int(ok.sum()), ok.size, low, diff, signs, chi_i, chi_e), flush=True)
    print("=== (c) cusp 2's high transition: the numerical residue of a shell the symmetry kills exactly ===", flush=True)
    # B1386 S4: at cusp 2 the first shell (|k| sqrt(covol) = 1.0746) is killed exactly by R's translation of order 3; the solve returns
    # it at ~1e-5.  It decays like exp(-2 pi 1.0746 tau) against the leading sqrt3-shell's exp(-2 pi 1.8612 tau), so at large tau
    # its residue must win.  If the transition is that residue, it moves up as the residue shrinks (K_n 14 -> 20) and vanishes
    # when the killed shell is set to its exact value, zero.
    for Kn in (14, 20):
        S2, x2, _ = HF.solve(M, Kn, 0.10, 1, 1)
        emb = CT.embedded_heights(M, S2)
        mm, nn, kk = S2.modes[2]
        first = [j for j in range(len(kk)) if abs(kk[j] * S2.s[2] - kk[0] * S2.s[2]) < 1e-6]
        resid = max(abs(S2.coefficient(x2, 2, j)) for j in first) * S2.s[2]
        rows, trans = CT.scan(S2, x2, 2, emb[2]["tau_emb"], n=40)
        xz = x2.copy()
        for j in first:
            xz[S2.first[2] + 2 * j] = 0.0
            xz[S2.first[2] + 2 * j + 1] = 0.0
        rows_z, trans_z = CT.scan(S2, xz, 2, emb[2]["tau_emb"], n=40)
        print("K_n %d: killed first shell's residue |c| sqrt(covol) = %.1e; transitions as solved %s; with the killed shell set to "
              "zero: chi values %s, transitions %s" % (Kn, resid, [(round(lo, 4), a, b) for lo, hi, a, b in trans],
                                                       sorted(set(r[1] for r in rows_z)),
                                                       [(round(lo, 4), a, b) for lo, hi, a, b in trans_z]), flush=True)
    print("(%.0fs)" % (time.time() - t0))
    print("DONE")
