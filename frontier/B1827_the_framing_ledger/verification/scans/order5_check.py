"""The blind reader's claim (FL-08), checked with main's code: on order-5 lines Y_u is symmetric (R_1(up) = 0) and
Y_e = Y_d^T; an order-7 line as a control.  Data-free."""
import math, sys, pathlib
import numpy as np
from fractions import Fraction as F
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from mirror_rule_probe import Z
B = Z.mods()["B"]
def Y_of(tau, line, d, L, r, sector):
    sn, ql, qr = [s for s in Z.SECTORS if s[0] == sector][0]
    w = B.line_w(line[0], line[1], tau); x, yy = B.sector_twists(w, tau, ql, qr)
    R = B.residues(x, yy, tau); c = B.cA(x, yy, tau, R); a = Z.direction(d, tau)
    Sm = a[0] * B.QI + a[1] * B.QJ + a[2] * B.QK
    if r: Sm = B.EPS @ Sm.conj() @ B.EPS.T
    u = {k: (math.sqrt(2 * math.pi * L + c[k]) * R[k] if c[k] is not None and 2 * math.pi * L + c[k] > 0 else 0) for k in B.UNITS}
    return B.coupling(Sm, B.weighted_M(u)), R
for line in ((F(2, 5), F(1, 10)), (F(2, 5), F(0)), (F(1, 5), F(3, 5)), (F(2, 7), F(1, 7))):
    for tau in (complex(0.3, 2.6), complex(0.12, 1.9)):
        L = Z.radii(tau)[1]
        Yu, Ru = Y_of(tau, line, "DR", L, 0, "up"); Yd, Rd = Y_of(tau, line, "DR", L, 0, "down"); Ye, Re = Y_of(tau, line, "DR", L, 0, "lepton")
        sym_u = np.linalg.norm(Yu - Yu.T) / np.linalg.norm(Yu)
        e_dT = np.linalg.norm(Ye - Yd.T) / np.linalg.norm(Yd)
        sd, se = np.linalg.svd(Yd, compute_uv=False), np.linalg.svd(Ye, compute_uv=False)
        print("line (%s,%s) tau %s: |R1(up)| %.1e  sym(Yu) %.1e  ||Ye-Yd^T||/||Yd|| %.1e  sv(e)/sv(d) %s" % (
            line[0], line[1], tau, abs(Ru["1"]), sym_u, e_dT, np.round(se / sd, 4)), flush=True)
