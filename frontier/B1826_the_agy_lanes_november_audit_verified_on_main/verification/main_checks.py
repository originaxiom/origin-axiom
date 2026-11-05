"""Main's own checks of the agy lane's surviving claims (2026-11-03): (1) the CKM corner inversion at B1825's address (the full
V from main's evaluator); (2) c_s identical across the three sectors (main's cA); (3) c_j + c_k - c_1 - c_i -> 0 on slopes
1/12 and 5/12 (and 1/4), not on 2/5, as Im tau grows."""
import math, pathlib, sys
from fractions import Fraction as F
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "frontier" / "B1821_the_frames_mirror_symmetry_in_re_tau" / "verification"))
import cm_zero_line as Z
B = Z.mods()["B"]

# (1) the full V at B1825's least-chi2 address: (3/8, 3/8), DR, L_2, reading S~S~S
tau = complex(0.093359375, 2.742578125); line = (F(3, 8), F(3, 8)); L = Z.radii(tau)[1]
U = {}
for (sn, ql, qr), r in zip(Z.SECTORS, (1, 1, 0)):
    w = B.line_w(line[0], line[1], tau); x, yy = B.sector_twists(w, tau, ql, qr)
    R = B.residues(x, yy, tau); c = B.cA(x, yy, tau, R); a = Z.direction("DR", tau)
    Sm = a[0] * B.QI + a[1] * B.QJ + a[2] * B.QK
    if r: Sm = B.EPS @ Sm.conj() @ B.EPS.T
    u = {k: (math.sqrt(2 * math.pi * L + c[k]) * R[k] if c[k] is not None and 2 * math.pi * L + c[k] > 0 else 0) for k in B.UNITS}
    Y = B.coupling(Sm, B.weighted_M(u)); u_, s, _ = np.linalg.svd(Y); o = np.argsort(s); U[sn] = u_[:, o]
V = U["up"].conj().T @ U["down"]; A = np.abs(V)
J = float(np.imag(V[0, 1] * V[1, 2] * np.conj(V[0, 2]) * np.conj(V[1, 1])))
s12, s23, s13 = A[0, 1], A[1, 2], A[0, 2]
Jmax = s12 * s23 * s13 * math.sqrt(max(1 - s12 ** 2 - s13 ** 2, 0)) * math.sqrt(max(1 - s23 ** 2 - s13 ** 2, 0)) / (1 - s13 ** 2) if s13 < 1 else float("nan")
print("(1) |V| at B1825's address:\n", np.round(A, 5))
print("    |V_ub|/(|V_us||V_cb|) = %.4f   |V_td|/(|V_us||V_cb|) = %.4f   |V_ub|/|V_td| = %.3f   J = %.3e  sin(delta)~|J|/Jmax = %.4f" % (
    A[0, 2] / (A[0, 1] * A[1, 2]), A[2, 0] / (A[0, 1] * A[1, 2]), A[0, 2] / A[2, 0], J, abs(J) / Jmax))

# (2) c_s across sectors, (3) the cusp combination
def cs(line, tau, ql, qr):
    w = B.line_w(line[0], line[1], tau); x, yy = B.sector_twists(w, tau, ql, qr)
    R = B.residues(x, yy, tau); return B.cA(x, yy, tau, R)
print("(2) c_s by sector (keys %s):" % list(B.UNITS))
worst = 0.0
for line, tau in (((F(2, 5), F(1, 10)), complex(0.3, 2.1)), ((F(1, 7), F(3, 7)), complex(0.1, 1.6)), ((F(4, 9), F(2, 9)), complex(0.45, 2.9))):
    cc = [cs(line, tau, ql, qr) for _, ql, qr in Z.SECTORS]
    for k in B.UNITS:
        vals = [c_[k] for c_ in cc]
        if None not in vals: worst = max(worst, max(vals) - min(vals))
    print("   ", line, tau, {k: [None if c_[k] is None else round(c_[k], 9) for c_ in cc] for k in B.UNITS})
print("    largest spread across sectors: %.3e" % worst)
print("(3) c_j + c_k - c_1 - c_i on the down sector (keys in UNITS order assumed 1, i, j, k):")
keys = list(B.UNITS)
for al in (F(1, 12), F(1, 4), F(5, 12), F(2, 5), F(1, 7)):
    row = []
    for y in (2.0, 3.0, 4.0):
        c = cs((al, F(0)), complex(0.0, y), 1, 2)
        if None in (c[keys[0]], c[keys[1]], c[keys[2]], c[keys[3]]): row.append(None); continue
        row.append(c[keys[2]] + c[keys[3]] - c[keys[0]] - c[keys[1]])
    print("    alpha = %-5s Im tau 2, 3, 4: %s" % (al, ["%.2e" % v if v is not None else None for v in row]))
