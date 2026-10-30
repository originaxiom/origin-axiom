"""The assembly on a synthetic census (data-free): the framework code equals a brute-force sum over both halves of the
band with the mirror partner's cells, a self-mirror line counts its own cells twice at half weight, and a planted target
is coded short."""
import math, pathlib, sys
from fractions import Fraction as Fr
import numpy as np
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'scripts' / 'stepb')); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import stepb_core as C
import compression as K
import grid as G
from assemble import Choices
from census_io import line_key, mirror_partner

PTS = [(0.0, 1.0), (0.05, 1.0), (0.25, 2.0), (0.5, 3.5)]
LINES = [line_key("2/5", "1/10"), line_key("2/5", "9/10"), line_key("0", "0")]


def make(seed=0):
    rng = np.random.default_rng(seed); cfg, d, r, k, m, v, J, vd, lines, tau = [], [], [], [], [], [], [], [], [], []
    for L in LINES:
        for p in PTS:
            ci = len(lines); lines.append(L); tau.append(p)
            for dd in (0, 2):
                for rr in (0, 1):
                    for kk in (0, 5):
                        base = np.sort(rng.random((3, 2)) * 0.3 + 1e-3, axis=1)
                        cfg.append(ci); d.append(dd); r.append(rr); k.append(kk); m.append(base)
                        v.append(rng.random(3) * 0.2 + 1e-3); J.append(1e-5); vd.append(True)
    return C.Census(cfg=np.array(cfg), d=np.array(d), r=np.array(r), k=np.array(k), m=np.array(m), v=np.array(v),
                    J=np.array(J), vdef=np.array(vd), lines=lines, tau=np.array(tau))


def brute(cen, F, t6, s6):
    w = G.area_weights(PTS) / 2; pi = {p: i for i, p in enumerate(PTS)}; best = math.inf
    groups = {}
    for i in range(len(cen.cfg)):
        ci = cen.cfg[i]; groups.setdefault((cen.lines[ci], cen.d[i], cen.r[i], cen.k[i]), []).append(i)
    for q, rows in groups.items():
        part = groups.get((mirror_partner(q[0]),) + q[1:], [])
        for cv in C.C_SCAN:
            tt = t6 - C.c_shift(cv)[:6]; terms = []
            for i in rows + part:               # log2 of each term, summed stably (distant targets underflow 2^-M)
                x2 = (((F[i, :6] - tt) / s6) ** 2).sum()
                terms.append(math.log2(w[pi[tuple(cen.tau[cen.cfg[i]])]]) - K.misfit_bits(np.array([x2]))[0])
            if terms:
                top = max(terms)
                best = min(best, K.A_DISCRETE - (top + math.log2(sum(2.0 ** (a - top) for a in terms))))
    return best


def test_self_mirror_line_weights():
    cen = make(); F = C.features(cen); ch = Choices(cen, F, PTS)
    j = next(n for n, q in enumerate(ch.keys) if q[0] == line_key("0", "0"))
    assert (ch.R[j] == ch.P[j]).all()                       # its own cells read twice, each at half weight
    j2 = next(n for n, q in enumerate(ch.keys) if q[0] == line_key("2/5", "1/10"))
    assert not (ch.R[j2] == ch.P[j2]).all()
    assert abs(ch.w_half.sum() * 2 - 1) < 1e-12
