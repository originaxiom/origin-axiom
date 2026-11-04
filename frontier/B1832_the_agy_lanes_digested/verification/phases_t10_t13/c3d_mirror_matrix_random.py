"""agy digest, T11e on random points (two seeds): main's FR-FIB (a0 = 0) satisfies the MATRIX mirror
    Y_s(line (alpha, -b), -conj tau) = P conj(Y_s(line (alpha, b), tau)) P,   P = diag(1, 1, -1) on [QJ, QI, QK],
for the census's theta-power directions F_a (main's cm_zero_line.direction formula), both readings, three sectors.
Control: the same line (alpha, b) at -conj tau.  Also P2c: Phase 2's LL singular values at the pre-naming fitted point
tau* = 0.44643117 + 2.60792242i (B1826 section 2), to locate the relay's numbers.  Data-free."""
import json, math, pathlib
from fractions import Fraction as F
import numpy as np
import mpmath as mp
from frame_common import B, norms, matter, yukawa, P, higgs

OUT = {}
def rec(k, v): OUT[k] = v; print(k, ":", v, flush=True)

def Fa(a, tau):
    q = mp.exp(1j * mp.pi * mp.mpc(tau.real, tau.imag)); eps = 1j ** ((a + 2) // 2)
    t2, t3, t4 = mp.jtheta(2, 0, q), mp.jtheta(3, 0, q), mp.jtheta(4, 0, q)
    return np.array([complex(eps * t2 ** a), complex(eps * t4 ** a), complex(1j * t3 ** a)])

def Y(line, tau, s, a, reading, L=2.36):
    R, c = norms(line, tau, s); v = Fa(a, tau)
    h = np.conj(v) if reading == "S~" else v
    S = h[0] * B.QI + h[1] * B.QJ + h[2] * B.QK
    return yukawa(S, matter(R, c, L))

for seed in (1790, 1821):
    rng = np.random.default_rng(seed); worst = 0.0; ctrl = []; rows = []
    for _ in range(4):
        q = int(rng.integers(3, 13)); p1 = F(int(rng.integers(1, q)), q); p2 = F(int(rng.integers(1, q)), q)
        tau = complex(round(float(rng.uniform(0.02, 0.48)), 3), round(float(rng.uniform(1.6, 3.6)), 3))
        a = int(rng.choice([-2, 6, 10, 14])); reading = str(rng.choice(["S", "S~"]))
        for s in ("up", "down", "lepton"):
            Y0 = Y((float(p1), float(p2)), tau, s, a, reading)
            Ym = Y((float(p1), -float(p2)), -tau.conjugate(), s, a, reading)
            Yc = Y((float(p1), float(p2)), -tau.conjugate(), s, a, reading)
            e = float(np.max(np.abs(Ym - P @ np.conj(Y0) @ P)) / np.max(np.abs(Y0)))
            worst = max(worst, e); ctrl.append(float(np.max(np.abs(Yc - P @ np.conj(Y0) @ P)) / np.max(np.abs(Y0))))
        rows.append({"line": (str(p1), str(p2)), "tau": str(tau), "F_a": a, "reading": reading,
                     "control (same line at -conj tau), least over sectors": min(ctrl[-3:]),
                     "line self-mirror (b == -b mod 1)?": (2 * p2).denominator == 1})
    rec("seed %d configurations" % seed, rows)
    rec("seed %d worst relative |Y((a,-b), -conj tau) - P conj(Y) P| over 12 sector-rows" % seed, worst)
    rec("seed %d control (same line at -conj tau): least relative deviation" % seed, min(ctrl))

tstar = complex(0.44643117, 2.60792242)
R_ll, _ = norms((0.4, 0.0), tstar, "LL"); _, c3 = norms((0.4, 0.0), tstar, "down")
S, _, _ = higgs(tstar, -1.0)
sv_relay = [0.04970, 0.17539, 3.42198]   # the ToE relay's section 2 (printed only to compare normalisations)
for L in (2.369205660785321, float(np.interp(tstar.imag, [2.0, 2.25, 2.5, 2.75, 3.0], [2.4404154646430865, 2.406639297403933, 2.3796454106029277, 2.3577376878276057, 2.3397188997332714]))):
    rec("P2c LL singular values at tau* (twist-3 norms, a0 = -b, L = %.6f)" % L, [round(float(v), 5) for v in np.sort(np.linalg.svd(yukawa(S, matter(R_ll, c3, L)), compute_uv=False))])
R_g, _ = norms((0.4, 0.0), complex(1 / 5 ** 0.5, ((1 + 5 ** 0.5) / 2) ** 2), "LL")
_, c3g = norms((0.4, 0.0), complex(1 / 5 ** 0.5, ((1 + 5 ** 0.5) / 2) ** 2), "down")
Sg, _, _ = higgs(complex(1 / 5 ** 0.5, ((1 + 5 ** 0.5) / 2) ** 2), -1.0)
svg = np.sort(np.linalg.svd(yukawa(Sg, matter(R_g, c3g, 2.369205660785321)), compute_uv=False))
rec("P2c tau_G: main's (s1/s3, s2/s3) vs the relay's", [[float(svg[0] / svg[2]), float(svg[1] / svg[2])], [sv_relay[0] / sv_relay[2], sv_relay[1] / sv_relay[2]]])
rec("P2c tau_G: relay / main per singular value (a common normalisation?)", [sv_relay[i] / float(svg[i]) for i in range(3)])
pathlib.Path(__file__).with_suffix(".json").write_text(json.dumps(OUT, indent=1, default=str))
