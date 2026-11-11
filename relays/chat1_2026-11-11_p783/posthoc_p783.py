"""
P-783, POST HOC (written after reading the sealed output c13cbc521; committed before its own run).  It uses the sealed
script's functions unchanged (imported, not edited).

WHY.  The sealed run found 25 confirmed states in 15 values to R = 11.  Two values, each confirmed in one mirror-even
class, were also found in the other W-class of the same parity by the first truncation, passing its next-coefficient
and automorphy tests, and then failed rule (iii): the second truncation's refinement found no sign change in its
bracket of +-0.004.  They are 7.4946304901 in (+1, +1) (confirmed in (+1, -1)) and 9.2608655254 in (+1, -1)
(confirmed in (+1, +1)).  If both are states, the count is 27 in 15 values, which is the count the seat's earlier
referee reported for the agy lane.  Separately, at the lane's 6.6632356489 the class (+1, +1) has the smallest scaled
singular value of any class at either lane value, 0.0035, with no eigenvalue within 0.13.

QUESTIONS, AND WHAT EACH ANSWER WOULD MEAN (written before the run)
  P1  At each of the two values, in the class where it was not confirmed, with both truncations:
      (a) H on a grid of step 0.0002 over +-0.01, both normalisations; every sign change refined and tested as in the
          sealed rule (next coefficient and automorphy below 1e-6);
      (b) the smallest scaled singular value over the median at the value;
      (c) the automorphy error of each truncation's solution at the value, at the sealed test points and at 20 more
          points (on |z - (2+i)/5| = 0.03 and near i/sqrt 5).
      A state: both truncations give a root within 1e-6 of the value, each passing the tests, and a scaled singular
      value below 1e-6.  Then the value is a doublet and the count is 27 in 15.  Otherwise it stays unconfirmed.
  P2  At the lane's 6.6632356489, class (+1, +1): the smallest scaled singular value at both truncations on R from
      6.60 to 6.72 in steps of 0.001, and every sign change of H there at step 0.0005.  A state would show a dip of
      the singular value to below 1e-6 at both truncations with a confirmed root; a value that stays above 1e-4 is no
      state at this resolution.
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np                                        # noqa: E402
from scipy.optimize import brentq                         # noqa: E402
import p783_spectrum as S                                 # noqa: E402

TRUNCS = {'first': (45, 60, 0.17, 0.15), 'second': (52, 70, 0.165, 0.14)}


def extra_points():
    ze = (2 + 1j) / 5
    pe = np.array([ze + 0.03 * np.exp(1j * (0.2 + 0.6 * k)) for k in range(10)])
    pw = np.array([complex(0.02 + 0.03 * k, 0.46 + 0.01 * (k % 4)) for k in range(10)])
    return pe, pw


def automorphy_more(a, R, sigma, eps):
    pe, pw = extra_points()
    E1 = lambda z: (2 * z - 1) / (5 * z - 2)
    W = lambda z: -1 / (5 * z)
    f0 = S.evalf(a, R, sigma, pe)
    f1 = S.evalf(a, R, sigma, E1(pe))
    g0 = S.evalf(a, R, sigma, pw)
    g1 = S.evalf(a, R, sigma, W(pw))
    return max(np.abs(f1 + f0).max() / np.abs(f0).max(), np.abs(g1 - eps * g0).max() / np.abs(g0).max())


def p1(value, sigma, eps):
    out = {}
    for name, (M, Q, Y1, Y2) in TRUNCS.items():
        sc = S.Scanner(M, Q, Y1, Y2)
        grid = np.round(np.arange(value - 0.01, value + 0.01 + 1e-12, 0.0002), 12)
        roots = []
        for fix in (0, 1):
            vals = np.array([sc.H(R, sigma, eps, fix)[0] for R in grid])
            for i in range(len(grid) - 1):
                if vals[i] * vals[i + 1] > 0:
                    continue
                try:
                    r = brentq(lambda R: sc.H(R, sigma, eps, fix)[0], grid[i], grid[i + 1], xtol=1e-13)
                except Exception:
                    continue
                h, a1, a2, k, k2 = sc.H(r, sigma, eps, fix)
                agree = abs(a1[k2] - a2[k2]) / max(1.0, abs(a1[k2]))
                aut = S.automorphy(a1, r, sigma, eps)
                aut2 = automorphy_more(a1, r, sigma, eps)
                roots.append(dict(R=r, fix='a_%d = 1' % (fix + 1), next_agree=agree, automorphy=aut,
                                  automorphy_more=aut2, distance=abs(r - value)))
        V, diag = sc.S1.matrix(value, sigma, eps)
        s = np.linalg.svd(V / diag[None, :], compute_uv=False)[::-1]
        out[name] = dict(roots=roots, scaled_sv=[float(s[0] / np.median(s)), float(s[1] / np.median(s))])
    return out


def p2(value=6.6632356489):
    out = {}
    for name, (M, Q, Y1, Y2) in TRUNCS.items():
        sc = S.Scanner(M, Q, Y1, Y2)
        Rs = np.round(np.arange(6.60, 6.72 + 1e-12, 0.001), 12)
        svs = []
        for R in Rs:
            V, diag = sc.S1.matrix(R, 1, 1)
            s = np.linalg.svd(V / diag[None, :], compute_uv=False)[::-1]
            svs.append(s[0] / np.median(s))
        svs = np.array(svs)
        i = int(np.argmin(svs))
        grid = np.round(np.arange(6.60, 6.72 + 1e-12, 0.0005), 12)
        changes = []
        for fix in (0, 1):
            vals = np.array([sc.H(R, 1, 1, fix)[0] for R in grid])
            for j in range(len(grid) - 1):
                if vals[j] * vals[j + 1] <= 0:
                    changes.append(dict(fix='a_%d = 1' % (fix + 1), between=[float(grid[j]), float(grid[j + 1])],
                                        H=[float(vals[j]), float(vals[j + 1])]))
        out[name] = dict(min_scaled_sv=float(svs[i]), at=float(Rs[i]), at_lane_value=float(
            np.interp(value, Rs, svs)), sign_changes=changes)
    return out


def main():
    res = {}
    for value, cls in ((7.4946304901, (1, 1)), (9.2608655254, (1, -1))):
        r = p1(value, *cls)
        res['P1 %.10f in %s' % (value, cls)] = r
        print('P1  %.10f in class %s:' % (value, cls))
        for name, v in r.items():
            print('    %s truncation: scaled singular values %.2e, %.2e' % (name, v['scaled_sv'][0], v['scaled_sv'][1]))
            for x in v['roots']:
                print('      root %.10f (%s): distance %.1e, next coefficient %.1e, automorphy %.1e and %.1e'
                      % (x['R'], x['fix'], x['distance'], x['next_agree'], x['automorphy'], x['automorphy_more']))
    r = p2()
    res['P2'] = r
    for name, v in r.items():
        print('P2  %s truncation, class (+1, +1), R in [6.60, 6.72]: least scaled singular value %.2e at R = %.3f; '
              'at the lane value %.2e; sign changes of H: %s' % (name, v['min_scaled_sv'], v['at'], v['at_lane_value'],
                                                                  v['sign_changes']))
    import json
    json.dump(res, open(sys.argv[1], 'w'), indent=1, default=str)
    return 0


if __name__ == '__main__':
    sys.exit(main())
