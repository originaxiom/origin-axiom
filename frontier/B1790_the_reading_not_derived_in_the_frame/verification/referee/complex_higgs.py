"""Scope check: the mirror preserves the S reading because DR's I, J coefficients are real and K's imaginary.  For a covariant
weight-7/2 Higgs H_c = E4 R + c D^2R (B1691's module), c complex, conj(H_c(tau)) = Lambda H_cbar(-conj tau): the mirror then maps
H_c to H_cbar, not to itself."""
import sys; sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))
import common as C, numpy as np, mpmath as mp
from fractions import Fraction as Fr
te = C.te
def H(tau, c):
    t = mp.mpc(tau.real, tau.imag); e4 = te.ev(te.e4, t)
    return C.quat(np.array([complex(e4 * te.ev(r, t) + c * te.ev(d2, t)) for r, d2 in zip(te.R, te.B[2])]))
for c in (1.0, 1j, 0.6 + 0.8j):
    for (t, a, b) in ((complex(0.3, 3.0), Fr(2, 5), Fr(1, 10)), (complex(0.6, 2.5), Fr(1, 7), Fr(2, 7))):
        tm = 1 - t.conjugate(); bm = (-a - b) % 1
        p = C.spectra(t, a, b, "L_max", Shiggs=H(t, c))
        q_same = C.spectra(tm, a, bm, "L_max", Shiggs=H(tm, c)); q_bar = C.spectra(tm, a, bm, "L_max", Shiggs=H(tm, np.conj(c)))
        d_same = max(C.dln(p[(s, rd)], q_same[(s, rd)]) for s in C.SECT for rd in ("S", "St"))
        d_bar = max(C.dln(p[(s, rd)], q_bar[(s, rd)]) for s in C.SECT for rd in ("S", "St"))
        print("c = %s, point %s: mirror with the same Higgs %.1e; mirror with c -> conj c %.1e" % (c, t, d_same, d_bar))
