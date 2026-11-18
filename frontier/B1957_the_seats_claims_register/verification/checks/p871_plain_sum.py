"""B1957, P-871's next computation (agy-exp's X-L5 harness, registered at harvest row 1927): does the plain sum over the 24 points
of order 5 of frame D1's residue-level coupling (unit weights: no channel norms) change under tau -> tau + 5 in the sectors
the level-5 law obstructs?  On main's own construction (checks/web_wb2_d1.py, d1: v_x(-h) v_y(-h)^T / theta_1'(0) contracted
with the frame's Higgs triplet, h = c q_H w).  Nothing of the seat's is run; its harness was read as text: it takes the
LEAST drift over its cases, which shows that some case has none, not that none has any.
 P1  for c = 0, 2, -2 and each sector: E = q_L^2 + q_R^2 + c q_H^2 mod 5, and the plain sum's singular-value ratios
     (s2/s1, s3/s1) at tau = 0.13 + 1.7i and at tau + 5, in both readings: the largest change.
 P2  the row sums: for each row 5a = 1..4 the sum over b of the coupling, against the largest single term of that row
     (if the obstructed rows summed to zero, their phases could not move the plain sum).
 P3  the same plain sum at tau + 25, where the law closes.
 P4  (added 2026-11-18) why c = +-2 shows no change: the five rows' sums differ in size by tens of orders, so the plain sum is
     the largest row's alone, and a phase common to one row cannot move singular-value ratios; the same sum with the law's
     phases put on the rows at tau has the same ratios there, and at c = 0 it does not."""
import sys, pathlib, functools
from fractions import Fraction as Fr
import numpy as np
print = functools.partial(print, flush=True)
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import web_wb2_d1 as D
mp = D.mp
PTS = [(Fr(i, 5), Fr(j, 5)) for i in range(5) for j in range(5) if (i, j) != (0, 0)]
def ratios(M):
    s = np.linalg.svd(M, compute_uv=False); return s[1] / s[0], s[2] / s[0]
for c in (0, 2, -2):
    for sec in ("up", "down", "lepton"):
        ql, qr, qh = D.SEC[sec]; E = (ql * ql + qr * qr + c * qh * qh) % 5; out = []
        for rd in ("S", "St"):
            Y = {}
            for tx in ("0.13", "5.13", "25.13"):
                t = mp.mpc(tx, "1.7"); Y[tx] = {p: D.d1(t, p[0], p[1], sec, c, rd) for p in PTS}
            S0, S5, S25 = (sum(Y[tx].values()) for tx in ("0.13", "5.13", "25.13"))
            r0, r5, r25 = ratios(S0), ratios(S5), ratios(S25)
            d5 = max(abs(x - y) for x, y in zip(r0, r5)); d25 = max(abs(x - y) for x, y in zip(r0, r25))
            rows = []
            for i in range(1, 5):
                terms = [Y["0.13"][p] for p in PTS if p[0] == Fr(i, 5)]
                rows.append(np.abs(sum(terms)).max() / max(np.abs(T).max() for T in terms))
            out.append("%s: ratios at tau (%.4f, %.4f), at tau + 5 (%.4f, %.4f): change %.2e; at tau + 25 change %.1e; row sums over the largest term, rows 5a = 1..4: %s"
                       % (rd, r0[0], r0[1], r5[0], r5[1], d5, d25, ["%.3f" % x for x in rows]))
        print("P c = %+d, %s (E = %d): %s" % (c, sec, E, " | ".join(out)))

import cmath
z = cmath.exp(2j * cmath.pi / 5)
for c, sec in ((0, "up"), (2, "down"), (-2, "up")):
    ql, qr, qh = D.SEC[sec]; E = (ql * ql + qr * qr + c * qh * qh) % 5; t = mp.mpc("0.13", "1.7")
    Y = {p: D.d1(t, p[0], p[1], sec, c, "S") for p in PTS}
    S0 = sum(Y.values()); Sph = sum(z ** ((E * int(5 * p[0]) ** 2) % 5) * Y[p] for p in PTS)
    norms = [float(np.abs(sum(Y[p] for p in PTS if int(5 * p[0]) == i)).max()) for i in range(5)]
    print("P4 c = %+d, %s (E = %d): the rows' sums by size (5a = 0..4): %s; the plain sum's ratios %s, with the law's phases on the rows %s"
          % (c, sec, E, ["%.1e" % x for x in norms], ["%.4f" % x for x in ratios(S0)], ["%.4f" % x for x in ratios(Sph)]))
