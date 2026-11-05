"""Proof by bilinearity of the flip lemma Y(h; u^flip) = D Y(Ph; u)^T D (D = diag(1, -1, 1) in BLOCKS order (QJ, QI, QK), P = diag(-1, 1, 1)
on the Higgs (QI, QJ, QK)): coupling(S, M) is bilinear, S(h) = sum h_c Q_c and M(u) = sum u_s EDUAL_s are linear, so the identity holds for
all (h, u) iff it holds on the 12 basis pairs (c, s).  The basis couplings are exact small rationals (times 1, i): check exactly."""
import sys, pathlib, json
from fractions import Fraction as Fr
import numpy as np
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _main_frame import B
Bf = B(); QS = [Bf.QI, Bf.QJ, Bf.QK]; KEYS = list(Bf.UNITS); D = np.diag([1.0, -1.0, 1.0])
def exact(z):  # map a float complex entry to an exact pair of fractions (limit denominators 8) and report the rounding residual
    fr, fi = Fr(z.real).limit_denominator(8), Fr(z.imag).limit_denominator(8); return (fr, fi), max(abs(z.real - float(fr)), abs(z.imag - float(fi)))
worst_round, fails = 0.0, []
for c in range(3):
    for s in KEYS:
        lhs = Bf.coupling(QS[c], (-1 if s == "i" else 1) * Bf.EDUAL[s])
        rhs = D @ Bf.coupling((-1 if c == 0 else 1) * QS[c], Bf.EDUAL[s]).T @ D
        L = [[exact(z) for z in row] for row in lhs]; R = [[exact(z) for z in row] for row in rhs]
        worst_round = max(worst_round, max(e[1] for row in L + R for e in row))
        if [[e[0] for e in row] for row in L] != [[e[0] for e in row] for row in R]: fails.append((c, s))
print("12 basis pairs; entries rational with denominators <= 8 (max rounding residual %.1e); exact mismatches: %s" % (worst_round, fails))
# control: the same without the transpose, and without the D's, must fail
ctrl = sum(int(not np.allclose(Bf.coupling(QS[c], (-1 if s == "i" else 1) * Bf.EDUAL[s]), Bf.coupling((-1 if c == 0 else 1) * QS[c], Bf.EDUAL[s]))) for c in range(3) for s in KEYS)
print("control (no transpose, no D): %d of 12 basis pairs differ" % ctrl)
json.dump({"mismatches": fails, "max_rounding": worst_round, "control_differ": ctrl}, open(pathlib.Path(__file__).with_suffix(".json"), "w")); print("exit 0")
