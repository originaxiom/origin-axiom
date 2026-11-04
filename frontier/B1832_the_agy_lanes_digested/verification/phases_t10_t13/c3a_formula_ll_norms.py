"""agy digest, Theorem 13 (and Phase 2's LL channel): main's code only (frame_common).  Data-free.
  F0   the lane's closed form of Y_4D equals main's coupling(a0 I + h.Q, weighted_M(u)) (random complex inputs)
  T13a the identity-channel residue of the LL pair (-3, -3) vanishes: the pairing EPS.1 = EPS reads M01 - M10, and for
       equal twists x = y the bilinear's off-diagonal entries are equal POINTWISE (so R_1 = 0 exactly, every line, every tau)
  T13c the LL norms at (2/5, 0), tau_G by main's cA, against the lane's (-2.29703, 33.91779, 10.00722) for (i, j, k)
  DBL  the doubling law suggested by the lane's 'closed_form_cA(tau, "4/5", "0")': c^{LL}(w) = c^{charged}(2w)?
       tested on tau_G's line and Review 74's four (line, tau) points (B1826 verification/review74/ll_pair_norms.py)
"""
import json, pathlib
from fractions import Fraction as F
import numpy as np
from frame_common import B, norms, lane_formula, TAU_G

OUT = {}
def rec(k, v): OUT[k] = v; print(k, ":", v, flush=True)

rng = np.random.default_rng(20261104)
err = 0.0
for _ in range(20):
    a0, m1 = rng.normal(size=2) + 1j * rng.normal(size=2)
    h = rng.normal(size=3) + 1j * rng.normal(size=3)          # on (QI, QJ, QK)
    u = {k: complex(z) for k, z in zip(B.UNITS, rng.normal(size=4) + 1j * rng.normal(size=4))}
    S = a0 * np.eye(2) + h[0] * B.QI + h[1] * B.QJ + h[2] * B.QK
    Ymain = B.coupling(S, B.weighted_M(u))
    Ylane = lane_formula(a0, [h[1], h[0], h[2]], u["1"], [u["j"], u["i"], u["k"]])
    err = max(err, float(np.max(np.abs(Ymain - Ylane))))
rec("F0 max |main coupling - lane closed form| over 20 random inputs", err)

# T13a pointwise
x = B.twist_of(-3 * B.line_w(0.4, 0.0, TAU_G), TAU_G)
z = 0.03 * np.exp(1j * rng.uniform(0, 2 * np.pi, 7)) + 0.1 * (rng.normal(size=7) + 1j * rng.normal(size=7))
M = B.bil(x, x, z, TAU_G)
rec("T13a max |M01 - M10| at 7 random points, LL at (2/5,0), tau_G", float(np.max(np.abs(M[0, 1] - M[1, 0]))))
rec("T13a EPS.1 pairing equals M01 - M10 (EC['1'])", np.allclose(B.EC["1"], np.array([[0, 1], [-1, 0]])))
R_ll, c_ll = norms((0.4, 0.0), TAU_G, "LL")
rec("T13a |R_1|, |R_i|, |R_j|, |R_k| for LL at (2/5,0), tau_G", [abs(R_ll[k]) for k in B.UNITS])
rec("T13c LL norms at (2/5,0), tau_G (main cA), channels 1,i,j,k", c_ll)
lane = {"i": -2.29703, "j": 33.91779, "k": 10.00722}
rec("T13c max |main - lane quoted| over i,j,k", max(abs(c_ll[k] - lane[k]) for k in lane))

def dbl(line, tau):
    ll = norms(line, tau, "LL")[1]
    two = (2 * line[0], 2 * line[1]); mtwo = (-two[0], -two[1])
    ch2 = norms(two, tau, "down")[1]; ch2u = norms(two, tau, "up")[1]; chm2 = norms(mtwo, tau, "down")[1]
    ch1 = norms(line, tau, "down")[1]
    def dev(a, b): return max((abs(a[k] - b[k]) for k in B.UNITS if a[k] is not None and b[k] is not None), default=None)
    pattern = lambda c: "".join(k if c[k] is not None else "-" for k in B.UNITS)
    return {"LL(w)": {k: (None if ll[k] is None else round(ll[k], 6)) for k in B.UNITS},
            "down(2w)": {k: (None if ch2[k] is None else round(ch2[k], 6)) for k in B.UNITS},
            "max|LL(w) - down(2w)|": dev(ll, ch2), "max|LL(w) - up(2w)|": dev(ll, ch2u), "max|LL(w) - down(-2w)|": dev(ll, chm2),
            "max|LL(w) - down(w)|": dev(ll, ch1), "defined channels LL(w), down(2w)": (pattern(ll), pattern(ch2))}
pts = [((0.4, 0.0), TAU_G), ((1 / 3, 1 / 6), complex(0.2, 2.3)), ((0.3, 0.2), complex(0.4, 1.9)),
       ((5 / 11, 2 / 11), complex(0.05, 2.7)), ((0.4, 0.1), complex(0.3, 2.1))]
for line, tau in pts:
    rec("DBL line %s tau %s" % (tuple(round(v, 6) for v in line), tau), dbl(line, tau))
pathlib.Path(__file__).with_suffix(".json").write_text(json.dumps(OUT, indent=1, default=str))
