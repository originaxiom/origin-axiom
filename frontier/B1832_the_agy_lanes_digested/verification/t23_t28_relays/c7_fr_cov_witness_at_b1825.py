"""c7: the FR-COV corner-flip witness and the mixed-reading claims at B1825's least-chi2 address, on MAIN's evaluator
(B1826's main_checks.py construction; the scalar component a0 fed to main's coupling as S = a0*I2 + a.Q, see c6).

Claims (ELEVATION s2 clause 3; HOSTILE 4.2, 7.1; SEVEN_PILLARS Thm 6 / Arm 1):
  a0 = 0.20 e^{7 pi i/8} shared: |V_ub|/|V_td| = 0.6778, sin(delta) = 0.6997, |J| = 5.4275e-5
  a0 = (1/2) eta^3 (Theorem 4's natural magnitude): |V_ub|/|V_td| = 5.8205, sin(delta) = 0.1255
  Arm 1: a0_u = +w^2 (1/2)(eta^3)*, a0_d = -w^2 (1/2)(eta^3)*: |V_ub|/|V_td| = 0.1523, sin(delta) = 0.2145
  a0 = 0, quark readings: S~S~ 0.9791/0.2028/0.0633, ratio 11.2797; SS |V_ud| 0.0824, |V_us| 0.9888, ratio 7.4033;
  S~S |V_ud| 0.0992, |V_us| 0.9944, |V_cb| 0.9890, |V_td| 0.9845; SS~ |V_ud| 0.9590, |V_cb| 0.9951, |V_td| 0.2789
Two conventions for a0 under the S~ reading: (A) a0*I added after the reading map; (B) the reading applied to the whole S
(eps S* eps^T conjugates a0).  No chi^2 and no comparison with data is computed here."""
import cmath, math, pathlib, sys
from fractions import Fraction as F
import numpy as np
import mpmath as mp

ROOT = pathlib.Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "frontier" / "B1821_the_frames_mirror_symmetry_in_re_tau" / "verification"))
import cm_zero_line as Z
B = Z.mods()["B"]
out = []
def say(*a):
    s = " ".join(str(x) for x in a); print(s); out.append(s)
I2 = np.eye(2, dtype=complex)
tau = complex(0.093359375, 2.742578125); line = (F(3, 8), F(3, 8)); L = Z.radii(tau)[1]
a = Z.direction("DR", tau)
t = mp.mpc(tau.real, tau.imag); eta = complex(mp.exp(1j * mp.pi * t / 12) * mp.qp(mp.exp(2j * mp.pi * t)))
U_ = {}
for sn, ql, qr in Z.SECTORS:
    w = B.line_w(line[0], line[1], tau); x, yy = B.sector_twists(w, tau, ql, qr)
    R = B.residues(x, yy, tau); c = B.cA(x, yy, tau, R)
    U_[sn] = {k: (math.sqrt(2 * math.pi * L + c[k]) * R[k] if c[k] is not None and 2 * math.pi * L + c[k] > 0 else 0) for k in B.UNITS}

def V_of(readings, a0s, conv):
    U = {}
    for (sn, ql, qr), r, a0 in zip(Z.SECTORS[:2], readings, a0s):
        Sm = a[0] * B.QI + a[1] * B.QJ + a[2] * B.QK
        if conv == "A":
            if r: Sm = B.EPS @ Sm.conj() @ B.EPS.T
            S = a0 * I2 + Sm
        else:
            S = a0 * I2 + Sm
            if r: S = B.EPS @ S.conj() @ B.EPS.T
        Y = B.coupling(S, B.weighted_M(U_[sn])); u_, s, _ = np.linalg.svd(Y); o = np.argsort(s); U[sn] = u_[:, o]
    V = U["up"].conj().T @ U["down"]; A = np.abs(V)
    J = float(np.imag(V[0, 1] * V[1, 2] * np.conj(V[0, 2]) * np.conj(V[1, 1])))
    s12, s23, s13 = A[0, 1], A[1, 2], A[0, 2]
    c13sq = 1 - s13 ** 2
    Jmax = s12 * s23 * s13 * math.sqrt(max(1 - s12 ** 2 - s13 ** 2, 0)) * math.sqrt(max(1 - s23 ** 2 - s13 ** 2, 0)) / c13sq
    return A, J, abs(J) / Jmax if Jmax > 0 else float("nan")

w3 = cmath.exp(2j * math.pi / 3)
cases = [("a0 = 0 (FR-FIB), S~S~", (1, 1), (0, 0)),
         ("a0 = 0.20 e^{7pi i/8} shared, S~S~", (1, 1), (0.2 * cmath.exp(7j * math.pi / 8),) * 2),
         ("a0 = (1/2) eta^3 shared, S~S~", (1, 1), (0.5 * eta ** 3,) * 2),
         ("Arm 1: +w^2 (eta^3)*/2, -w^2 (eta^3)*/2, S~S~", (1, 1), (w3 ** 2 * 0.5 * np.conj(eta ** 3), -w3 ** 2 * 0.5 * np.conj(eta ** 3))),
         ("a0 = 0.20 e^{7pi i/8}, the ledger's S~S", (1, 0), (0.2 * cmath.exp(7j * math.pi / 8),) * 2)]
say("B1825 address (3/8,3/8), DR, L_2 = %.6f, tau = %s; |eta^3|/2 = %.6f" % (L, tau, abs(eta ** 3) / 2))
for conv in ("A", "B"):
    say("convention %s:" % conv)
    for name, rd, a0s in cases:
        A, J, sd = V_of(rd, a0s, conv)
        say("  %-48s |V_ud| %.4f |V_us| %.4f |V_cb| %.4f |V_ub| %.5f |V_td| %.5f  |V_ub|/|V_td| %.4f  |J| %.4e  |J|/Jmax %.4f" % (
            name, A[0, 0], A[0, 1], A[1, 2], A[0, 2], A[2, 0], A[0, 2] / A[2, 0], abs(J), sd))
say("a0 = 0, the four quark readings (up, down):")
for rd in ((1, 1), (0, 0), (1, 0), (0, 1)):
    A, J, sd = V_of(rd, (0, 0), "A")
    say("  %-5s |V_ud| %.4f |V_us| %.4f |V_cb| %.4f |V_td| %.4f |V_ub|/|V_td| %.4f" % (
        "".join("S~" if r else "S" for r in rd), A[0, 0], A[0, 1], A[1, 2], A[2, 0], A[0, 2] / A[2, 0]))
pathlib.Path(__file__).with_name("c7_fr_cov_witness_at_b1825_out.txt").write_text("\n".join(out) + "\n")
