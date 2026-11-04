"""S301 verifier B, check T47-T50 (value-free algebra; first principles; no lane code run).

Only the identities Theorems 47-50 label FORCED are re-derived; their bridges to observables are typed in LEDGER.md.
Not computed here (firewall): Theorem 48's trace ratio (it is the lane's tan beta), any y_tau/y_b, any PMNS quantity.
"""
import random
from fractions import Fraction as F
import numpy as np
import mpmath as mp
import sympy as sp

print("T47  Q2(lepton) = (-3)^2 + 6^2 =", (-3) ** 2 + 6 ** 2, "; 1/Q2 =", F(1, 45))
print("     midpoint (1/42 + 1/45)/2 =", (F(1, 42) + F(1, 45)) / 2, " (the lane's unmasked l. 8891: 29/1260)")
k_x, k_12, N, Vol, pi = sp.symbols("k_x k_12 N Vol pi", positive=True)
alpha12 = 1 / (N * Vol)
eps = sp.simplify(alpha12 / (4 * pi) * (2 * k_x * pi * Vol - 2 * k_12 * pi * Vol))
print("     eps_KK = (alpha_12/4pi) ln(M_x^2/M_12^2) with alpha_12^-1 = N Vol, ln(M/M_Z) = k pi Vol:  eps =", eps,
      " -> Vol cancels for ANY integers; eps is a ratio of the chosen integers")

w = np.exp(2j * np.pi / 3)
Pg = np.roll(np.eye(3), 1, axis=0)
Pi = [sum(w ** (-k * m) * np.linalg.matrix_power(Pg, m) for m in range(3)) / 3 for k in range(3)]
err = max(np.abs(Pi[k] @ Pi[k] - Pi[k]).max() for k in range(3))
taut = []
for _ in range(5):
    a, b = random.random(), random.random()
    ev = sorted(np.linalg.eigvalsh(a * Pi[0] + b * Pi[1]))
    taut.append(max(abs(x - y) for x, y in zip(ev, sorted([0.0, a, b]))))
print("\nT48  Z3 projectors idempotent (err %.1e), sum = I (err %.1e);" % (err, np.abs(sum(Pi) - np.eye(3)).max()),
      "rho = a Pi_0 + b Pi_1 has eigenvalues {0, a, b} for random a, b: max err %.1e" % max(taut),
      "-> the 'weighting' returned is the weighting typed in")

lam = [np.array(m, dtype=complex) for m in (
    [[0, 1, 0], [1, 0, 0], [0, 0, 0]], [[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], [[1, 0, 0], [0, -1, 0], [0, 0, 0]],
    [[0, 0, 1], [0, 0, 0], [1, 0, 0]], [[0, 0, -1j], [0, 0, 0], [1j, 0, 0]], [[0, 0, 0], [0, 0, 1], [0, 1, 0]],
    [[0, 0, 0], [0, 0, -1j], [0, 1j, 0]])] + [np.diag([1, 1, -2]).astype(complex) / np.sqrt(3)]
CF = sum((l / 2) @ (l / 2) for l in lam)
print("\nT49  C_F I_3 = sum (lambda/2)^2: C_F =", np.round(CF[0, 0].real, 15), "(4/3);",
      "Gauss-Legendre of a constant integrand is exact for any node count (trivial);",
      "B-L: (Tr(Pi_q T)/3)/Tr(Pi_l T) =", (F(1, 3) * 3 / 3) / F(-1), "(textbook 126 Clebsch -3, inverted)")

mp.mp.dps = 40
v1 = 2 * mp.im(mp.polylog(2, mp.exp(1j * mp.pi / 3)))
v2 = mp.sqrt(3) / 36 * (mp.psi(1, mp.mpf(1) / 6) + mp.psi(1, mp.mpf(1) / 3) - mp.psi(1, mp.mpf(2) / 3) - mp.psi(1, mp.mpf(5) / 6))
v3 = 3 * mp.clsin(2, 2 * mp.pi / 3)                       # 6 Lobachevsky(pi/3), Milnor's form
print("\nT50  Vol(m004): 2 Cl2(pi/3) =", mp.nstr(v1, 25), "; trigamma form - it = %.1e; 3 Cl2(2pi/3) - it = %.1e" % (abs(v2 - v1), abs(v3 - v1)))
print("     C_QCD = 3 (17 + 5) =", 3 * (17 + 5), "; 4 pi C =", 4 * 66, "pi ; 2 pi C =", 2 * 66, "pi")
print("     main's T-THETA-Y-BSTEP: arg det Y_s steps by 12 pi p1 Q2 (Q2 = 17 up, 5 down) -> theta_Y by", 12 * (17 + 5),
      "pi p1 ; P-323's T-step -132 pi a^2 - pi/2: the same numbers (4 pi C = 12 pi (17+5), 2 pi C = 132)")
q = mp.mpc(0.1, 1.3)
eta = lambda t: mp.exp(1j * mp.pi * t / 12) * mp.qp(mp.exp(2j * mp.pi * t))
print("     FORCED-09's eta^3 T-multiplier: eta(t+1)^3 / eta(t)^3 = e^{i pi/4}: err %.1e" % abs(eta(q + 1) ** 3 / eta(q) ** 3 - mp.exp(1j * mp.pi / 4)))
