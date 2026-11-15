"""B1947's diagnosis (main, 2026-11-15; data-free, no mixing computed): frame C's Higgs triplet transforms under tau -> tau + 1
by W-B1's matrix T_R (with the point moved as w -> (a, b - a)); with the Higgs twisted (D1', q_H = 3) it picks up further
component-dependent phases of modulus 1, which frame C's quaternion contraction does not absorb."""
import sys, pathlib
sys.argv = [sys.argv[0], "--v2"]
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import d1_coupling as D
from fractions import Fraction as Fr
mp = D.mp; mp.mp.dps = 40
w = mp.exp(1j * mp.pi / 4)
TR = mp.matrix([[w, 0, 0], [0, 0, w], [0, w ** -3, 0]])
for q in (0, 3):
    for a, b in ((Fr(1, 5), Fr(2, 5)), (Fr(2, 5), Fr(4, 5))):
        t = mp.mpc("0.13", "1.7")
        c0 = mp.matrix(D.S_comps(t, q, a, b)); c1 = mp.matrix(D.S_comps(t + 1, q, a, (b - a) % 1)); pred = TR * c0
        r = [complex(c1[k] / pred[k]) for k in range(3)]
        print("q_H = %d, w = (%s, %s): component ratios %s, moduli %s" % (q, a, b, ["%.4f%+.4fi" % (z.real, z.imag) for z in r], ["%.6f" % abs(z) for z in r]))
