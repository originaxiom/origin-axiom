"""P-566 exploration (labelled; data-free; the factor 3 is the 45's Clebsch from SU(5) group theory, and that it is what
nature needs is a coarse fact, disclosed): on order-5 lines, where the frame is minimal SU(5) exactly (B1827), a singlet Higgs
component a0 = c sqrt(h.h) entering down with +1 and leptons with Clebsch k (k = -3: the 45; k = +1: a 5-like control).
Reported: (m_mu/m_tau)/(m_s/m_b) and (m_e/m_tau)/(m_d/m_b) -- both 1 without the singlet (identical spectra)."""
import cmath, math, sys, pathlib
import numpy as np
from fractions import Fraction as F
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from mirror_rule_probe import Z
B = Z.mods()["B"]

def M_of(tau, line, L, sector):
    sn, ql, qr = [s for s in Z.SECTORS if s[0] == sector][0]
    w = B.line_w(line[0], line[1], tau); x, yy = B.sector_twists(w, tau, ql, qr)
    R = B.residues(x, yy, tau); c = B.cA(x, yy, tau, R)
    u = {k: (math.sqrt(2 * math.pi * L + c[k]) * R[k] if c[k] is not None and 2 * math.pi * L + c[k] > 0 else 0) for k in B.UNITS}
    return B.weighted_M(u)

def sv(M, a, a0, r):
    Sm = a0 * np.eye(2) + a[0] * B.QI + a[1] * B.QJ + a[2] * B.QK
    if r: Sm = B.EPS @ Sm.conj() @ B.EPS.T
    s = np.sort(np.linalg.svd(B.coupling(Sm, M), compute_uv=False)); return s / s[2]

for line in ((F(2, 5), F(0)), (F(1, 5), F(3, 5))):
    for tau in (complex(0.3, 2.6), complex(0.12, 1.9), complex(0.45, 3.2)):
        L = Z.radii(tau)[1]; Md, Me = M_of(tau, line, L, "down"), M_of(tau, line, L, "lepton")
        for d in ("DR", "F_6", "F_22"):
            a = np.array(Z.direction(d, tau)); hh = complex(a @ a)
            for r in (0, 1):
                row = []
                for c in (0, 1, cmath.exp(2j * math.pi * 2 / 12), 1j * 0.7):
                    for k in ((-3, 1) if c != 0 else (1,)):
                        a0 = c * cmath.sqrt(hh)
                        sd, se = sv(Md, a, a0, r), sv(Me, a, k * a0, r)
                        row.append("c=%s k=%+d: %.3f %.3f" % ("0" if c == 0 else "%.2f%+.2fi" % (c.real, c.imag) if isinstance(c, complex) else str(c), k,
                                                              se[1] / sd[1], se[0] / sd[0]))
                print("(%s,%s) tau %s %-4s r%d | " % (line[0], line[1], tau, d, r) + " | ".join(row), flush=True)
