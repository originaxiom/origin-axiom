#!/usr/bin/env python3
"""B1388 -- THE CUTOFF TEST, run exactly as sealed in ../PREREGISTRATION.md (sha256 in docs/SEAL_LEDGER.md).

Is cube~3.24's chiral index N(v+) = +-2 (B1387) independent of where the cusps are cut off inside their embedded cusp regions?

For cusp c and chart height T the torus function is
    g_{c,T}(x) = dF_c/dh at h = T = sum_k c_k (-2 pi |k| T K_0(2 pi |k| T)) e^{2 pi i k.x},
using every mode of B1387's solve (K_n = 14, tau = 0.10, seeds 1/1), and the partition is d+_{c,T} = {g_{c,T} > 0}.
- chi(d+_{c,T}) comes from B1386's Morse count, completed, with the triangulated grid as cross-check where the partition is resolved.
- The heights are 40 geometric steps over [tau_emb(c), 20 tau_emb(c)], where tau = T / sqrt(covol) and tau_emb = 1/sqrt(A_max).
- A_max(c) is twice the volume of cusp c's maximal individually-embedded neighbourhood (SnapPy's CuspNeighborhood, the other
  cusps shrunk).
- Every change of chi between neighbouring heights is bisected to 1e-6 relative.

Outcome STABLE iff every cusp's chi is constant on its range and equal to the leading-shell value; else UNSTABLE.
Usage: python3 cutoff_test.py"""
import math
import sys
import time
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")
import numpy as np
from scipy.special import k0

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "frontier" / "B1387_the_index_computed" / "verification"))
import harmonic_cusp_form as HF                  # B1387's instrument, unchanged (it loads B1386's the_open_cusp as HF.T)

T = HF.T
LEADING = {0: -1, 1: 0, 2: 0, 3: -1}             # B1387's asymptotic pattern (the banked identity)


def banked_identity(M, S, x):
    rows, N = HF.analyse(S, x)
    ok = True
    for c in (0, 3):
        ok &= all(abs(m - 1.00695) < 0.01 * 1.00695 for m in rows[c]["|c| sqrt(covol)"])
        ok &= abs(rows[c]["cos of the triple phase"] - 0.370) < 0.01 * 0.370
    ok &= abs(rows[1]["|c| sqrt(covol)"][0] - 1.789) < 0.01 * 1.789
    m2 = sorted(rows[2]["|c| sqrt(covol)"])
    ok &= abs(m2[0] - 0.335) < 0.01 * 0.335 and abs(m2[1] - 0.335) < 0.01 * 0.335 and abs(m2[2] - 2.209) < 0.01 * 2.209
    ok &= {c: rows[c]["chi(d+)"] for c in range(4)} == LEADING
    shapes = []
    for c in range(4):
        b1, b2 = S.C.lat[c]
        tau = complex(b2 / b1)
        snap = complex(M.cusp_info("shape")[c])
        shapes.append(abs(_reduce(tau) - _reduce(snap)) < 1e-6)
    ok &= all(shapes)
    return ok, rows, N


def _reduce(t):
    t = complex(t)
    if t.imag < 0:
        t = -t
    for _ in range(100):
        t = complex(t.real - round(t.real), t.imag)
        if abs(t) < 1 - 1e-12:
            t = -1 / t
        else:
            break
    if abs(abs(t) - 1) < 1e-9 and t.real < 0:        # the boundary identification of the fundamental domain
        t = complex(-t.real, t.imag)
    if abs(t.real + 0.5) < 1e-9:
        t = complex(0.5, t.imag)
    return t


_EMBEDDED = {}


def embedded_heights(M, S=None):
    """tau_emb(c) = 1/sqrt(A_max(c)), A_max = 2 x the volume of cusp c's maximal neighbourhood with the other cusps shrunk.
    Computed once per triangulation (SnapPea's cusp-neighbourhood kernel is not re-entrant on a manifold object)."""
    key = M.triangulation_isosig(decorated=True)
    if key in _EMBEDDED:
        return _EMBEDDED[key]
    out = {}
    for c in range(M.num_cusps()):
        CN = M.copy().cusp_neighborhood()
        for d in range(M.num_cusps()):
            if d != c:
                CN.set_displacement(-2.0, d)
        CN.set_displacement(CN.reach(c), c)
        V = CN.volume(c)
        out[c] = {"reach": CN.reach(c), "volume": V, "tau_emb": 1 / math.sqrt(2 * V)}
    _EMBEDDED[key] = out
    return out


def torus_terms(S, x, c, h, rel=1e-13):
    mm, nn, kk = S.modes[c]
    w = -2 * np.pi * kk * h * k0(2 * np.pi * kk * h)
    coef = np.array([S.coefficient(x, c, j) for j in range(len(kk))]) * w
    keep = np.abs(coef) > rel * np.abs(coef).max()
    terms = []
    for z, m, n in zip(coef[keep], mm[keep], nn[keep]):
        terms += [(complex(z), (int(m), int(n))), (complex(np.conj(z)), (-int(m), -int(n)))]
    return terms


def chi_at(S, x, c, tau):
    """chi(d+_{c,T}) by the Morse count; where the field is so close to one direction that its critical points are not isolated
    (the search finds none, or cannot complete), the grid decides and the row says so (complete = 'grid')"""
    terms = torus_terms(S, x, c, tau * S.s[c])
    grid = T.chi_grid(T.grid_values(terms, 240) > 0)
    try:
        chi, complete, gap, _ = T.morse_chi(terms)
    except (ValueError, MemoryError):                 # no isolated critical points found, or a non-isolated critical set
        return grid, "grid", 0.0, grid, len(terms) // 2
    if not complete:
        return grid, "grid", gap, grid, len(terms) // 2
    return chi, True, gap, (grid if gap > 1e-2 else None), len(terms) // 2


def scan(S, x, c, tau_emb, n=40, top=20.0):
    taus = np.geomspace(tau_emb, top * tau_emb, n)
    rows = [(float(t),) + chi_at(S, x, c, t) for t in taus]
    transitions = []
    for (t1, c1, *_), (t2, c2, *_) in zip(rows, rows[1:]):
        if c1 != c2:
            lo, hi, clo = t1, t2, c1
            while (hi - lo) > 1e-6 * hi:
                mid = math.sqrt(lo * hi)
                cm = chi_at(S, x, c, mid)[0]
                if cm == clo:
                    lo = mid
                else:
                    hi = mid
            transitions.append((lo, hi, c1, c2))
    return rows, transitions


if __name__ == "__main__":
    t0 = time.time()
    M = HF.member()
    S, x, st = HF.solve(M, 14, 0.10, 1, 1)
    ok, rows, N = banked_identity(M, S, x)
    print("B1388 the cutoff test. Solve:", st, flush=True)
    print("BANKED IDENTITY reproduced:", ok, "| asymptotic chi:", {c: rows[c]["chi(d+)"] for c in range(4)}, "| N =", N, flush=True)
    if not ok:
        print("STOP: the banked identity failed; nothing below is read.")
        sys.exit(1)
    emb = embedded_heights(M, S)
    print("embedded ranges:", {c: {k: round(v, 5) for k, v in e.items()} for c, e in emb.items()}, flush=True)
    stable = True
    for c in range(4):
        rows_c, trans = scan(S, x, c, emb[c]["tau_emb"])
        chis = sorted(set(r[1] for r in rows_c))
        incomplete = sum(1 for r in rows_c if r[2] is False)
        gridonly = sum(1 for r in rows_c if r[2] == "grid")
        disagree = sum(1 for r in rows_c if r[4] is not None and r[4] != r[1])
        const = (chis == [LEADING[c]])
        stable &= const and not incomplete and not disagree
        print("cusp %d: tau in [%.4f, %.4f]; chi values %s; leading %+d; constant and equal: %s; incomplete searches %d; grid-only "
              "rows %d; grid disagreements %d; min critical gap %.4f; modes used %d..%d" % (
                  c, rows_c[0][0], rows_c[-1][0], chis, LEADING[c], const, incomplete, gridonly, disagree,
                  min(r[3] for r in rows_c), min(r[5] for r in rows_c), max(r[5] for r in rows_c)), flush=True)
        for r in rows_c[:3] + rows_c[-2:]:
            print("   tau %.4f chi %+d gap %.4f grid %s" % (r[0], r[1], r[3], r[4]), flush=True)
        for lo, hi, a, b in trans:
            print("   TRANSITION at tau in [%.7f, %.7f]: chi %+d -> %+d" % (lo, hi, a, b), flush=True)
    print("OUTCOME:", "STABLE" if stable else "UNSTABLE", "(%.0fs)" % (time.time() - t0), flush=True)
    print("DONE")
