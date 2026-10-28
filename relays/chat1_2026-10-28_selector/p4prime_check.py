"""chat1, 2026-10-28: P4' (the next-order holomorphic lift under the framed end condition), checked on the twisted lines.
Post hoc, labelled, data-free; committed before its one run. Under equal framed data the couplings are the residues,
u = R (B1654). If the residues' squares sum to zero, sum_s R_s^2 = 0, the rank-one identity makes det M(u = R) vanish at
every cut, and there is no next order. B1654 showed it for the untwisted kernels; this reads the frame's twisted residues
(B1726's modules) at two of the six's rows, in every sector.
Run:  python3 -B p4prime_check.py <main_checkout>"""
import sys, pathlib
from fractions import Fraction as Fr
import numpy as np
ROOT = pathlib.Path(sys.argv[1]).resolve()
sys.path.insert(0, str(ROOT / "frontier" / "B1726_the_two_ingredients_replicated" / "verification"))
import census as K
M = K._modules(); B = M["B"]
for (re_t, im_t, a, b) in [(0.269, 3.037, Fr(2, 5), Fr(23, 30)), (0.5, 3.03, Fr(2, 5), Fr(1, 10))]:
    t = complex(re_t, im_t); w = float(a) * t + float(b)
    for sec, (lf, rf) in K.SECT.items():
        x, yy = B.sector_twists(w, t, B.SIXY[lf], B.SIXY[rf]); R = B.residues(x, yy, t)
        nr = sum(abs(R[s]) ** 2 for s in B.UNITS); s2 = sum(R[s] ** 2 for s in B.UNITS)
        dM = np.linalg.det(B.weighted_M(R))
        print("tau %s, line (%s, %s), %-4s: |sum R_s^2| / sum |R_s|^2 = %.1e; |det M(u = R)| / (sum |R_s|^2)^(3/2) = %.1e"
              % (t, a, b, sec, abs(s2) / nr, abs(dM) / nr ** 1.5))
print("p4prime_check exit 0")
