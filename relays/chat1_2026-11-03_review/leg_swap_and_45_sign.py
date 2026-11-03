"""The web seat's check for its review of main's S290 (data-free; no measured value read).

(1) The adjugate reading is a swap of the coupling's two legs. In main's frame module (b1656_funcs, via B1821's
    cm_zero_line), coupling(S, M)[a, b] = sum((C_a^T eps S C_b) * M). With adj(S) = eps S^T eps^T:
        coupling(adj S, M) = -coupling(S, M^T)^T
    (exact for any 2 x 2 S and M; shown symbolically for the bilinear x^T eps S y, and numerically in main's code).
    And adj(a0 I + a.Q) = a0 I - a.Q for main's quaternion units.
(2) The 45's sign. On order-5 lines the lepton matrix is the down matrix with its legs swapped, up to a global phase
    (M_e = e^(i phi) M_d^T; phi = 0 on (2/5, 0)), so by (1)
        coupling(k a0 I + v, M_d^T) = [coupling(v, M_d) - k a0 coupling(I, M_d)]^T :
    a singlet entering the leptons with factor k enters with Clebsch -k relative to the down quarks (the triplet with +1).
    Main's gj45_probe uses k = -3 for "the 45" and k = +1 for "a 5-like control": Clebsch +3 and -1. The lepton spectrum
    at k a0 equals the down spectrum at -k a0, and the 5-like value (Clebsch +1) is k = -1.
(3) On main's own probe grid (gj45_probe: two order-5 lines, three tau, DR / F_6 / F_22, both readings, the three nonzero
    c of its four),
    the second generation's lepton/down ratio for k = -3 (main's "45") and k = +3 (the 45 with the correct sign).

Usage: python3 leg_swap_and_45_sign.py <main checkout>   (main at e1e3c6c2f)
"""
import cmath
import contextlib
import io
import math
import pathlib
import sys
from fractions import Fraction as F

import numpy as np
import sympy as sp

sys.dont_write_bytecode = True
ROOT = pathlib.Path(sys.argv[1]).resolve()
sys.path.insert(0, str(ROOT / "frontier" / "B1821_the_frames_mirror_symmetry_in_re_tau" / "verification"))
with contextlib.redirect_stdout(io.StringIO()):
    import cm_zero_line as Z
    B = Z.mods()["B"]

# (1a) symbolic: x^T eps adj(S) y = -(y^T eps S x) for the bilinear form, any S
s11, s12, s21, s22, x1, x2, y1, y2 = sp.symbols("s11 s12 s21 s22 x1 x2 y1 y2")
S = sp.Matrix([[s11, s12], [s21, s22]]); eps = sp.Matrix([[0, 1], [-1, 0]])
x = sp.Matrix([x1, x2]); y = sp.Matrix([y1, y2]); adjS = eps * S.T * eps.T
lhs = (x.T * eps * adjS * y)[0]; rhs = -(y.T * eps * S * x)[0]
print("(1a) x^T eps adj(S) y + y^T eps S x simplifies to:", sp.simplify(lhs - rhs))
print("     adj(S) - det(S) S^-1 simplifies to:", sp.simplify(adjS - S.det() * S.inv()))
print("     main's EPS equals eps:", bool(np.allclose(B.EPS, np.array([[0, 1], [-1, 0]]))))

# (1b) numeric, in main's coupling
rng = np.random.default_rng(1103)
worst = 0.0
for _ in range(200):
    Sm = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2)); M = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
    adj = B.EPS @ Sm.T @ B.EPS.T
    worst = max(worst, float(np.max(np.abs(B.coupling(adj, M) + B.coupling(Sm, M.T).T))))
print("(1b) max |coupling(adj S, M) + coupling(S, M^T)^T| over 200 random S, M: %.1e" % worst)
a = rng.normal(size=3) + 1j * rng.normal(size=3); a0 = complex(rng.normal(), rng.normal())
Sq = a0 * np.eye(2) + a[0] * B.QI + a[1] * B.QJ + a[2] * B.QK
print("     |adj(a0 + a.Q) - (a0 - a.Q)| = %.1e" % np.max(np.abs(B.EPS @ Sq.T @ B.EPS.T - (a0 * np.eye(2) - a[0] * B.QI - a[1] * B.QJ - a[2] * B.QK))))


def M_of(tau, line, L, sector):
    """main's gj45_probe.M_of, verbatim in substance"""
    sn, ql, qr = [s for s in Z.SECTORS if s[0] == sector][0]
    w = B.line_w(line[0], line[1], tau); xx, yy = B.sector_twists(w, tau, ql, qr)
    R = B.residues(xx, yy, tau); c = B.cA(xx, yy, tau, R)
    u = {k: (math.sqrt(2 * math.pi * L + c[k]) * R[k] if c[k] is not None and 2 * math.pi * L + c[k] > 0 else 0) for k in B.UNITS}
    return B.weighted_M(u)


def sv(M, av, a0, r):
    """main's gj45_probe.sv"""
    Sm = a0 * np.eye(2) + av[0] * B.QI + av[1] * B.QJ + av[2] * B.QK
    if r: Sm = B.EPS @ Sm.conj() @ B.EPS.T
    s = np.sort(np.linalg.svd(B.coupling(Sm, M), compute_uv=False)); return s / s[2]


# (2) and (3) on main's probe grid
ratios = {-3: [], 3: []}
worst_swap = 0.0; worst_spec = 0.0; five_like = 0.0
for line in ((F(2, 5), F(0)), (F(1, 5), F(3, 5))):
    for tau in (complex(0.3, 2.6), complex(0.12, 1.9), complex(0.45, 3.2)):
        with contextlib.redirect_stdout(io.StringIO()):
            L = Z.radii(tau)[1]
            Md, Me = M_of(tau, line, L, "down"), M_of(tau, line, L, "lepton")
        ph = np.vdot(Md.T.ravel(), Me.ravel()); ph = ph / abs(ph)
        worst_swap = max(worst_swap, float(np.linalg.norm(Me - ph * Md.T) / np.linalg.norm(Md)))
        for d in ("DR", "F_6", "F_22"):
            with contextlib.redirect_stdout(io.StringIO()):
                av = np.array(Z.direction(d, tau))
            hh = complex(av @ av)
            for r in (0, 1):
                for c in (1, cmath.exp(2j * math.pi * 2 / 12), 1j * 0.7):
                    a0 = c * cmath.sqrt(hh)
                    sd = sv(Md, av, a0, r)
                    for k in (-3, -1, 1, 3):
                        se = sv(Me, av, k * a0, r); sdm = sv(Md, av, -k * a0, r)
                        worst_spec = max(worst_spec, float(np.max(np.abs(se - sdm))))
                        if k == -1: five_like = max(five_like, float(np.max(np.abs(se - sd))))
                        if k in ratios: ratios[k].append(se[1] / sd[1])
print("(2) on main's probe grid (2 lines x 3 tau): max over the grid of min over a global phase |M_e - e^(i phi) M_d^T| / |M_d| = %.1e" % worst_swap)
print("    max |lepton spectrum at k a0 - down spectrum at -k a0| over k in (-3, -1, 1, 3): %.1e" % worst_spec)
print("    k = -1 (Clebsch +1, the 5-like value): max |lepton - down spectrum| = %.1e" % five_like)
for k in (-3, 3):
    v = np.array(ratios[k])
    print("(3) k = %+d (Clebsch %+d): second-generation lepton/down ratio over %d probe rows: median %.2f, quartiles %.2f-%.2f, in [2, 4.5]: %d"
          % (k, -k, len(v), np.median(v), np.quantile(v, 0.25), np.quantile(v, 0.75), int(np.sum((v >= 2) & (v <= 4.5)))))
