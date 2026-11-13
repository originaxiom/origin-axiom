# calibration C14: Parseval. c_s(ubar1) - c_s(ubar2) against Im tau sum_lambda (1/|lambda + u1'|^2 - 1/|lambda + u2'|^2),
# u' = alpha tau - beta from the kernel's multipliers; and the twists' A-factor convention checked
import sys, pathlib, math, cmath, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import numpy as np, b1656_kernel as B
exec(open(pathlib.Path(__file__).resolve().parent / "cal13.py").read().split("def kronA")[0].split("import numpy as np, b1656_kernel as B, sm_c7_lib as L")[1])
def latdiff(u1, u2, t, Rm=1500):
    m = np.arange(-Rm, Rm + 1)
    tot = 0.0
    for mm in range(-Rm, Rm + 1):
        lam = mm * t - m
        tot += np.sum(1 / np.abs(lam + u1) ** 2 - 1 / np.abs(lam + u2) ** 2)
    return tot
t = 0.21 + 1.13j
random.seed(21)
pts = []
for _ in range(3):
    p1, p2 = random.uniform(0.05, 0.45), random.uniform(0.05, 0.95)
    w = B.line_w(p1, p2, t); x, y = B.sector_twists(w, t, 1, 0); R = B.residues(x, y, t); c = B.cA(x, y, t, R)
    pts.append((c, {s: mult(x, y, t, R, s) for s in c if c[s] is not None}))
for s in "1ijk":
    (c1, m1), (c2, m2) = pts[0], pts[1]
    if s not in m1 or s not in m2: continue
    for sign in (1, -1):
        u1 = m1[s][0] * t - sign * m1[s][1]; u2 = m2[s][0] * t - sign * m2[s][1]
        print("channel", s, "sign", sign, " c diff %.6f" % (c1[s] - c2[s]), "  Parseval %.6f" % (t.imag * latdiff(u1, u2, t)))
