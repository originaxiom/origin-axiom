"""The web seat, 2026-11-05: POST HOC to closure_review_check.py (ea295738c -> 66ff92883), written after reading its output.
Data-free; same guards (no held-out quantity; no line of the family's classes).

Why: two of that run's metrics cannot carry a conclusion.
  - (C2) compared ratios of singular values, sv2/sv0 included; where a Yukawa is (numerically) rank 2, that ratio is
    rounding noise, and a ratio of two noises is meaningless. Its entrywise moduli agreed to 5.6e-16 and 4.9e-15.
  - (D) compared Y2 with P conj(Y1) P entrywise with no phase freedom; a global phase between two computations (a
    convention of the residues' phases) reads as a failure, and the wrong relation scored about the same.
Expected before this run, from B1656's thc() and bil(): w -> w + tau leaves every component of the bilinear unchanged
(the characteristic a moves by an integer q, and thc() sums over n in Z + a), and w -> w + 1 multiplies every component by
the one phase exp(4 pi i (q_L a_x + q_R a_y)), so each sector's Yukawa changes by at most a global phase.

Measured here, at (C2)'s and (D)'s own points (delta 0.3), every sector and reading:
  (C2') Y(w + 1) and Y(w + tau) against e^{i phi} Y(w), phi fitted (phi = arg <Y(w), Y(w')>): the residual
        max|Y' - e^{i phi} Y| / max|Y|; the singular values scaled by the largest, as absolute differences; and the
        smallest scaled singular value of Y(w) (rank 2 if it is at rounding level);
  (D')  C-MIR's relation with a fitted global phase: Y2 against e^{i phi} P conj(Y1) P, and two wrong relations under the
        same freedom, P Y1 P (no conjugation) and conj(Y1) (no P); and the smallest scaled singular value of Y1.

    python3 closure_review_posthoc.py <main checkout>      (main at a494173bc)
"""
import contextlib
import importlib.util
import io
import math
import pathlib
import sys
from fractions import Fraction as F

import numpy as np

ROOT = pathlib.Path(sys.argv[1]).resolve()
CHK = ROOT / "frontier" / "B1842_the_closure_instruments" / "verification"
FAMILY_3A = {F(1, 5), F(4, 5)}
UNITS = ("1", "i", "j", "k")


def load(name, path):
    sp = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(sp); sys.modules[name] = m
    with contextlib.redirect_stdout(io.StringIO()):
        sp.loader.exec_module(m)
    return m


X = load("p688_exact_card_instrument", CHK / "exact_card_instrument.py")
with contextlib.redirect_stdout(io.StringIO()):
    MX = X.mods()
ee, B = MX["ee"], MX["B"]


def guard(a):
    assert (3 * F(a)) % 1 not in FAMILY_3A, ("a line of the family's classes", a)


def yuk_at(tau, w, sec, G, rd, Lh):
    ql, qr = X.CHARGES[sec]
    x, yy = B.sector_twists(w, tau, ql, qr); R = B.residues(x, yy, tau)
    N, _ = ee.twisted_norms(tau, G["al"], G["be"], Lh, x, yy, R, nth=X.NTH, ns=X.NS)
    u = {s: (math.sqrt(N[s]) * R[s] if N.get(s) is not None and N[s] > 0 else 0) for s in UNITS}
    Mw = B.weighted_M(u)
    return {rn: B.coupling(H, Mw) for rn, H in rd.items()}


def phase_fit(A, Bm):
    """max|A - e^{i phi} Bm| / max|A| with phi = arg <Bm, A>"""
    ip = np.vdot(Bm.ravel(), A.ravel()); ph = ip / abs(ip) if abs(ip) > 0 else 1.0
    return float(np.max(np.abs(A - ph * Bm)) / np.max(np.abs(A)))


def svs(Y):
    sv = np.linalg.svd(Y, compute_uv=False); return sv / sv[0]


if __name__ == "__main__":
    print("(C2') lattice translations of the twist point, with a fitted global phase (delta 0.3)")
    worst = {"w+1 residual": 0.0, "w+1 sv": 0.0, "w+tau residual": 0.0, "w+tau sv": 0.0}; smin = []
    for tau in (complex(0.31, 2.9), complex(-0.12, 3.2)):
        with contextlib.redirect_stdout(io.StringIO()):
            c, _ = X.accessory(tau); G = ee.geometry(tau, c); rd = ee.higgs(tau)
        Lh = G["L_max"] + 0.3
        for (a, b) in ((F(1, 3), F(1, 4)), (F(1, 10), F(3, 10))):
            guard(a); w = float(a) * tau + float(b)
            for sec in X.CHARGES:
                Y0 = yuk_at(tau, w, sec, G, rd, Lh)
                for rn in Y0:
                    smin.append(("%+.2f%+.2fi" % (tau.real, tau.imag), "(%s, %s)" % (a, b), sec, rn, float(svs(Y0[rn])[2])))
                for tag, sh in (("w+1", 1.0), ("w+tau", tau)):
                    Y1 = yuk_at(tau, w + sh, sec, G, rd, Lh)
                    for rn in Y0:
                        worst[tag + " residual"] = max(worst[tag + " residual"], phase_fit(Y1[rn], Y0[rn]))
                        worst[tag + " sv"] = max(worst[tag + " sv"], float(np.max(np.abs(svs(Y1[rn]) - svs(Y0[rn])))))
    print("  largest: %s" % {k: "%.1e" % v for k, v in worst.items()})
    low = [s for s in smin if s[4] < 1e-10]
    print("  smallest scaled singular value of Y(w): %.1e-%.1e; below 1e-10 (rank 2) at %d of %d (tau, line, sector, reading): %s" % (
        min(s[4] for s in smin), max(s[4] for s in smin), len(low), len(smin), [s[:4] for s in low]))
    print("(D') C-MIR with a fitted global phase (delta 0.3)")
    Pm = np.diag([1, 1, -1]); res = {"P conj(Y1) P": 0.0, "wrong: P Y1 P": [], "wrong: conj(Y1)": []}; sm = []
    for (re_t, im_t, a, b) in ((0.27, 2.95, F(1, 3), F(1, 7)), (0.13, 3.05, F(1, 4), F(2, 9))):
        guard(a)
        with contextlib.redirect_stdout(io.StringIO()):
            Y1, _ = X.yukawas_exact(re_t, im_t, a, b, 0.3); Y2, _ = X.yukawas_exact(-re_t, im_t, a, (-b) % 1, 0.3)
        for sec in X.CHARGES:
            for rn in ("S", "St"):
                A = Y2[sec][rn]
                res["P conj(Y1) P"] = max(res["P conj(Y1) P"], phase_fit(A, Pm @ np.conj(Y1[sec][rn]) @ Pm))
                res["wrong: P Y1 P"].append(phase_fit(A, Pm @ Y1[sec][rn] @ Pm))
                res["wrong: conj(Y1)"].append(phase_fit(A, np.conj(Y1[sec][rn])))
                sm.append(float(svs(Y1[sec][rn])[2]))
    print("  P conj(Y1) P, largest residual %.1e | P Y1 P, residual %.1e-%.1e | conj(Y1), residual %.1e-%.1e | smallest scaled "
          "singular value of Y1 %.1e-%.1e" % (res["P conj(Y1) P"], min(res["wrong: P Y1 P"]), max(res["wrong: P Y1 P"]),
                                             min(res["wrong: conj(Y1)"]), max(res["wrong: conj(Y1)"]), min(sm), max(sm)))
    print("closure_review_posthoc exit 0")
