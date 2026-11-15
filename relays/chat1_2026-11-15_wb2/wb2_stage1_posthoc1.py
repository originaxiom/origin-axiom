#!/usr/bin/env python3
"""W-B2, stage 1, post hoc 1 (committed before its run; NOT blind: the sealed run's output has been read).

The sealed run's control failed (V0) because of the harness, not the frame. With unit weights (u_s = R_s) the
residue-level coupling has rank 2: its third singular value is of order 1e-16 of the first, so s3/s1 is rounding noise and
its relative deviation is meaningless. (Frame C's full frame, with its norms, is covariant at the same points: checked
in a debugging run of the transcription's frame() at one point, not part of any sealed output.)
This run repeats the sealed test with the two non-zero singular values only:
  dev = max(|s1(tau + 1) / s1(tau) - 1|, |r2(tau + 1) / r2(tau) - 1|), r2 = s2/s1, and reports s3/s1's largest value.
Same candidates, sectors, points, moduli and expectations (V0 to V3, the plant) as wb2_stage1.py.

    python3 -I -u wb2_stage1_posthoc1.py
"""
import os, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import wb2_stage1 as K  # noqa: E402

S3MAX = [0.0]


def svals(t, a, b, sec, kc, tt, rd):
    w = float(a) * t + float(b)
    lf, rf = K.SECT[sec]
    x, y = K.twist_of(K.SIXY[lf] * w, t), K.twist_of(K.SIXY[rf] * w, t)
    R = K.residues_h(x, y, t, kc * K.QH[sec] * w)
    ta, tb = (K.QH[sec] * float(a), K.QH[sec] * float(b)) if tt else (0.0, 0.0)
    c = K.comps(t, ta, tb)
    S = c[0] * K.QI + c[1] * K.QJ + c[2] * K.QK
    if rd == "St":
        S = K.EPS @ np.conj(S) @ K.EPS.T
    sv = np.linalg.svd(K.NS["coupling"](S, K.NS["weighted_M"](R)), compute_uv=False)
    S3MAX[0] = max(S3MAX[0], sv[2] / sv[0])
    return sv


def worst(kc, tt, rd, move=True, secs=("up", "down", "lep")):
    out = {}
    for sec in secs:
        wv = 0.0
        for a, b in K.POINTS:
            for t in K.TAUS:
                s0 = svals(t, a, b, sec, kc, tt, rd)
                s1 = svals(t + 1, a, (b - a) % 1 if move else b, sec, kc, tt, rd)
                wv = max(wv, abs(s1[0] / s0[0] - 1), abs((s1[1] / s1[0]) / (s0[1] / s0[0]) - 1))
        out[sec] = float(wv)
    return out


def main():
    res = {}
    for rd in ("S", "St"):
        res[("K0", rd)] = worst(0, False, rd)
        res[("K1", rd)] = worst(0, True, rd)
        for c in (1, -1, 2, -2):
            res[("K2(%+d)" % c, rd)] = worst(c, False, rd)
            res[("K3(%+d)" % c, rd)] = worst(c, True, rd)
    for (k, rd), d in res.items():
        K.say("%-7s %-2s  %s" % (k, rd, K.fmt(d)))
    v0 = all(max(res[("K0", rd)].values()) < 1e-8 for rd in ("S", "St"))
    v1 = all(max(res[("K1", rd)].values()) > 1e-3 for rd in ("S", "St"))
    v2 = [(c, rd) for c in (1, -1, 2, -2) for rd in ("S", "St") if max(res[("K2(%+d)" % c, rd)].values()) < 1e-8]
    v3 = [(c, rd) for c in (1, -1, 2, -2) for rd in ("S", "St") if max(res[("K3(%+d)" % c, rd)].values()) < 1e-8]
    plant = max(worst(0, False, "S", move=False, secs=("up",)).values()) > 1e-3
    K.say("V0 holds:", v0, "| V1 holds:", v1, "| V2 covariant K2 (c, reading):", v2, "| V3 covariant K3:", v3,
          "| plant fails:", plant, "| largest s3/s1 seen: %.1e" % S3MAX[0])


if __name__ == "__main__":
    main()
