"""c6: the agy lane's quaternionic identities checked on MAIN's FR-FIB coupling (b1656_funcs.coupling via cm_zero_line.mods()['B']),
which is linear in the Higgs S in M2(C) -- so a scalar component a0 is S = a0*I2 + h.Q fed to main's own function.

  (a) ELEVATION s3: Y(a0 I + h.Q, M) - Y(h.Q, M) = a0 (m1 I - [m_perp]_x), m_perp = (u_j, u_i, u_k) (BLOCKS order)
      and Y(h.Q, M) = h m^T + m h^T - (h.m) I - m1 [h]_x, h = (s_J, s_I, s_K)
  (b) Theorem 3 (= B1659's det Y = 4 det S det M tr(eps S M^T), main): det Y = (a0^2 + h.h)(m1^2 + m.m)(a0 m1 + h.m)
  (c) Theorem 5 (SEVEN_PILLARS): Y = (a0 I - [h]_x)(m1 I - [m]_x) + h m^T; det A = a0 (a0^2 + h.h); the stated A^-1
  (d) Theorem 4 (= B1739's h.h = eta^6/4, main): DR.DR = eta^6/4; R.R = 0; HOSTILE 2.3: the 't=-5/288' direction is null
  (e) SEVEN_PILLARS: |h.h| = |eta(tau*)|^6/4 = 0.00336507 at B1825's tau* = 0.093359375 + 2.742578125i
  (f) FOUR_STEPS 3.1: the (-3,-3) Weinberg pair on (2/5, 0) at the lane's tau = 0.44643117 + 2.60792242i: R_1 = 0 (B1799), the
      triplet moduli (0.2712, 0.2935, 0.3952) in (j, i, k)
  (g) Theorem 26 (toe_closure.py:5034-5037, 5059-5062): its (-3,-3) operator uses the charged sectors' channel norms
      closed_form_cA(tau_g, '2/5', '1/10') (twist 3); main's channel norms of the (-3,-3) sector at tau_Golden on (2/5, 1/10)
"""
import cmath, math, pathlib, sys
from fractions import Fraction as F
import numpy as np
import mpmath as mp

ROOT = pathlib.Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "frontier" / "B1821_the_frames_mirror_symmetry_in_re_tau" / "verification"))
import cm_zero_line as Z
B = Z.mods()["B"]; keys = list(B.UNITS)
out = []
def say(*a):
    s = " ".join(str(x) for x in a); print(s); out.append(s)
rng = np.random.default_rng(20261104)
I2, I3 = np.eye(2, dtype=complex), np.eye(3, dtype=complex)
def cross(v): return np.array([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]], dtype=complex)
def rc(*s): return rng.normal(size=s) + 1j * rng.normal(size=s)

ea = eb = ec = ed = 0.0
for _ in range(50):
    a0 = complex(rc(1)[0]); sI, sJ, sK = rc(3); u = dict(zip(keys, rc(4)))
    S3 = sI * B.QI + sJ * B.QJ + sK * B.QK; S4 = a0 * I2 + S3; M = B.weighted_M(u)
    h = np.array([sJ, sI, sK]); m1 = u["1"]; m = np.array([u["j"], u["i"], u["k"]])
    Y3, Y4 = B.coupling(S3, M), B.coupling(S4, M)
    ea = max(ea, np.abs(Y4 - Y3 - a0 * (m1 * I3 - cross(m))).max())
    eb = max(eb, np.abs(Y3 - (np.outer(h, m) + np.outer(m, h) - (h @ m) * I3 - m1 * cross(h))).max())
    d = np.linalg.det(Y4); pred = (a0 ** 2 + h @ h) * (m1 ** 2 + m @ m) * (a0 * m1 + h @ m)
    b1659 = 4 * np.linalg.det(S4) * np.linalg.det(M) * np.trace(B.EPS @ S4 @ M.T)
    ec = max(ec, abs(d - pred) / abs(d), abs(d - b1659) / abs(d))
    A = a0 * I3 - cross(h); Bm = m1 * I3 - cross(m)
    Ainv = (a0 ** 2 * I3 + a0 * cross(h) + np.outer(h, h)) / (a0 * (a0 ** 2 + h @ h))
    ed = max(ed, np.abs(Y4 - (A @ Bm + np.outer(h, m))).max(), abs(np.linalg.det(A) - a0 * (a0 ** 2 + h @ h)) / abs(np.linalg.det(A)),
             np.abs(Ainv @ A - I3).max())
say("(a) max |Y(a0 I + hQ) - Y(hQ) - a0(m1 I - [m]x)| = %.2e ; max |Y(hQ) - (h m^T + m h^T - (h.m)I - m1[h]x)| = %.2e (50 random)" % (ea, eb))
say("(b) Theorem 3 vs det on main's coupling, and vs B1659's 4 det S det M tr(eps S M^T): max rel err %.2e" % ec)
say("(c) Theorem 5 decomposition, det A, stated A^-1: max err %.2e" % ed)

def eta(tau):
    t = mp.mpc(tau.real, tau.imag); q = mp.exp(2j * mp.pi * t)
    return mp.exp(1j * mp.pi * t / 12) * mp.qp(q)
for tau in (complex(0.3, 1.7), complex(-0.21, 2.6), complex(0.093359375, 2.742578125)):
    dr = np.array(Z.direction("DR", tau)); r = np.array(Z.direction("R", tau)); t5 = np.array(Z.direction("t=-5/288", tau))
    e6 = complex(eta(tau) ** 6) / 4
    say("(d) tau=%s: |DR.DR - eta^6/4|/|eta^6/4| = %.2e ; |R.R|/|R|^2 = %.2e ; |t.t|/|t|^2 ('t=-5/288') = %.2e" % (
        tau, abs(dr @ dr - e6) / abs(e6), abs(r @ r) / np.vdot(r, r).real, abs(t5 @ t5) / np.vdot(t5, t5).real))
ts = complex(0.093359375, 2.742578125)
say("(e) |eta(tau*)|^6/4 = %.8f, sqrt = %.6f (relay: 0.00336507 = 0.058009^2)" % (abs(complex(eta(ts))) ** 6 / 4, math.sqrt(abs(complex(eta(ts))) ** 6 / 4)))

def resid(line, tau, ql, qr):
    w = B.line_w(line[0], line[1], tau); x, yy = B.sector_twists(w, tau, ql, qr)
    R = B.residues(x, yy, tau); return R, B.cA(x, yy, tau, R)
tl = complex(0.44643117, 2.60792242)
R, _ = resid((F(2, 5), F(0)), tl, -3, -3)
say("(f) (-3,-3) on (2/5,0) at %s: |R_1| = %.2e ; (|R_j|, |R_i|, |R_k|) = (%.4f, %.4f, %.4f) (relay: 1.8e-17; 0.2712, 0.2935, 0.3952)" % (
    tl, abs(R["1"]), abs(R["j"]), abs(R["i"]), abs(R["k"])))
phi = (1 + math.sqrt(5)) / 2; tg = complex(1 / math.sqrt(5), phi * phi)
for (ql, qr, nm) in ((1, 2, "down (1,2)"), (-3, 6, "lepton (-3,6)"), (-3, 0, "Dirac nu (-3,0)"), (-3, -3, "Weinberg (-3,-3)")):
    _, c = resid((F(2, 5), F(1, 10)), tg, ql, qr)
    say("(g) tau_Golden, (2/5,1/10), %-17s twist %+d: c_s = %s" % (nm, ql + qr, {k: (None if c[k] is None else round(c[k], 6)) for k in keys}))

pathlib.Path(__file__).with_name("c6_quaternion_identities_on_main_out.txt").write_text("\n".join(out) + "\n")
