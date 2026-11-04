"""c9: arithmetic of Theorem 27 (toe_closure.py:5142-5254) and of the gauge ansatz it builds on (sm_19_gate.py:877-891,
Theorem 9 Part B) -- the stated formulas evaluated as written; nothing is compared with measured data here."""
import math, pathlib
import mpmath as mp
mp.mp.dps = 30
out = []
def say(*a):
    s = " ".join(str(x) for x in a); print(s); out.append(s)
# Vol(m004) = 2 Cl_2(pi/3) = 6 Lambda(pi/3)
vol = 2 * mp.clsin(2, mp.pi / 3)
say("Vol(m004) = 2 Cl_2(pi/3) = %s (lane literal 2.0298832128193072)" % mp.nstr(vol, 20))
v = float(vol)
say("4/(pi^2 Vol) = %.10f (lane 0.19965914); |1/5 - it| = %.3e (lane: 0.170%%)" % (4 / (math.pi ** 2 * v), abs(0.2 - 4 / (math.pi ** 2 * v))))
say("S_B1782 = 28 pi sqrt84/3 = %.4f (lane 268.7363);  32 pi phi^2 = %.4f (lane 263.1936)" % (28 * math.pi * math.sqrt(84) / 3, 32 * math.pi * ((1 + math.sqrt(5)) / 2) ** 2))
# the gauge ansatz (Theorem 9 Part B), one loop as written
b1, b2, b3 = 41 / 10, -19 / 6, -7.0
a12 = 21 * v; t12 = 2 * v; d3 = b3 * math.log(4 / math.sqrt(3))
a1, a2, a3 = a12 + b1 * t12, a12 + b2 * t12, a12 + d3 + b3 * t12
aem = 5 / 3 * a1 + a2
say("ansatz: alpha_12^-1 = 21 Vol = %.5f, t_12 = 2 Vol = %.5f, M_12/M_Z = e^(4 pi Vol) = %.4e, Delta_3 = -7 ln(4/sqrt3) = %.6f" % (a12, t12, math.exp(2 * math.pi * t12), d3))
say("        alpha_em^-1(M_Z) = %.3f, sin^2 theta_W(M_Z) = %.5f, alpha_s(M_Z) = %.5f  (the relay's 128.559, 0.23158, 0.11976)" % (aem, a2 / aem, 1 / a3))
g2sq, gysq = 4 * math.pi / a2, 0.6 * 4 * math.pi / a1
mzv1 = 0.5 * math.sqrt(g2sq + gysq)
say("        tree-level M_Z/v = sqrt(g2^2 + gY^2)/2 from this one-loop ansatz = %.7f (Theorem 27 imports 0.3712747 from Theorem 12, not checked here)" % mzv1)
for mzv in (0.3712747, mzv1):
    r = (v / math.pi) * mzv * math.exp(6 * math.pi * v)
    say("  M_Pl/v = (Vol/pi) (M_Z/v) exp(6 pi Vol) with M_Z/v = %.7f: %.6e ; G_N v^2 = 1/(8 pi (M_Pl/v)^2) = %.5e" % (mzv, r, 1 / (8 * math.pi * r * r)))
say("  note: exp(6 pi Vol) = exp(2 pi Vol(M_3)) = %.4e" % math.exp(6 * math.pi * v))
pathlib.Path(__file__).with_name("c9_t27_and_gauge_arithmetic_out.txt").write_text("\n".join(out) + "\n")
