"""Main's check (2026-11-04): the matrix mirror Y((a,-b), -conj tau) = P conj(Y((a,b), tau)) P on FR-FIB, with a PER-SECTOR
control (the same line at -conj tau). The reader's control took the least over sectors, which the lepton sector (charges
multiples of 3) passes trivially on lines whose b and -b agree mod 1/3; per sector the control fails at O(1) for up and down."""
import numpy as np, mpmath as mp
from frame_common import B, norms, matter, yukawa, P
def Fa(a, tau):
    q = mp.exp(1j*mp.pi*mp.mpc(tau.real, tau.imag)); eps = 1j**((a+2)//2)
    t2,t3,t4 = mp.jtheta(2,0,q), mp.jtheta(3,0,q), mp.jtheta(4,0,q)
    return np.array([complex(eps*t2**a), complex(eps*t4**a), complex(1j*t3**a)])
def Y(line, tau, s, a, rd, L=2.36):
    R, c = norms(line, tau, s); v = Fa(a, tau); h = np.conj(v) if rd=="S~" else v
    return yukawa(h[0]*B.QI + h[1]*B.QJ + h[2]*B.QK, matter(R, c, L))
for line, tau, a, rd in (((1/3, 2/3), complex(0.361, 3.3), 6, "S"), ((1/6, 1/3), complex(0.2, 2.4), 6, "S"), ((2/3, 2/3), complex(0.1, 2.9), 14, "S~"),
                         ((1/8, 1/8), complex(0.3, 2.2), -2, "S~"), ((3/10, 1/5), complex(0.4, 1.9), 10, "S")):
    for s in ("up", "down", "lepton"):
        Y0 = Y(line, tau, s, a, rd); n = np.max(np.abs(Y0))
        test = np.max(np.abs(Y((line[0], -line[1]), -tau.conjugate(), s, a, rd) - P@np.conj(Y0)@P))/n
        ctrl = np.max(np.abs(Y(line, -tau.conjugate(), s, a, rd) - P@np.conj(Y0)@P))/n
        print(line, s, "identity %.1e" % test, "control %.1e" % ctrl)
