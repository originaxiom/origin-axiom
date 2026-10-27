import json, math, sys
from fractions import Fraction as Fr
import numpy as np
SIXY = {"Q": 1, "u": -4, "d": 2, "L": -3, "e": 6}; SECT = {"up": ("Q", "u"), "down": ("Q", "d"), "lep": ("L", "e")}
def nd(x): x = x % 1; return min(x, 1 - x)
def E(ax, ay): return [nd(ax)**2 + nd(ay)**2 - Fr(1,8), nd(ax)**2 + nd(ay+Fr(1,2))**2 - Fr(1,8), nd(ax+Fr(1,2))**2 + nd(ay)**2 - Fr(1,8), nd(ax+Fr(1,2))**2 + nd(ay+Fr(1,2))**2 - Fr(1,8)]
rows = [json.loads(l) for f in sys.argv[1:] for l in open(f)]
keys = []
for r in rows:
    k = (r["a"], r["b"], r["sec"], r["nth"])
    if k not in keys: keys.append(k)
for k in keys:
    rs = sorted([r for r in rows if (r["a"], r["b"], r["sec"], r["nth"]) == k], key=lambda r: r["y"])
    a = Fr(k[0]); ql, qr = (SIXY[f] for f in SECT[k[2]]); mu = E(ql * a, qr * a)
    closed = Fr(1, 2) - (nd(2 * ql * a) + nd(2 * qr * a)) / 2
    ys = np.array([r["y"] for r in rs])
    print("=== line (%s, %s) %s  nth=%s  closed m2/m3 = %s = %.4f;  E_ij = %s" % (k[0], k[1], k[2], k[3], closed, float(closed), [round(float(e), 4) for e in mu]))
    # block exponents from |r_ij| (local slopes)
    lr = np.array([[math.log(float(r["absr"][i][j])) for r in rs] for i in range(2) for j in range(2)])
    loc = lambda v: [float(-(v[n+1] - v[n]) / (2 * math.pi * (ys[n+1] - ys[n]))) if ys[n+1] != ys[n] else float("nan") for n in range(len(ys) - 1)]
    print("  r_ij local exps:", {("r%d%d" % (q // 2, q % 2)): [round(x, 4) for x in loc(lr[q])] for q in range(4)})
    for rd in ("S", "St"):
        for idx, nm in ((0, "m2/m3"), (1, "m1/m3")):
            v = np.array([math.log(float(r[rd][idx])) for r in rs])
            l = loc(v)
            # fit ln rho = -2 pi e y + k ln y + c over all heights >= 8
            sel = ys >= 8
            A = np.vstack([-2 * math.pi * ys[sel], np.log(ys[sel]), np.ones(sel.sum())]).T
            (e, kk, c), *_ = np.linalg.lstsq(A, v[sel], rcond=None)
            A2 = np.vstack([-2 * math.pi * ys[sel], np.ones(sel.sum())]).T; (e2, c2), *_ = np.linalg.lstsq(A2, v[sel], rcond=None)
            print("  %-2s %s  ys %s  local %s | fit(no log) %.4f | fit(+k ln y) e=%.4f k=%.2f" % (rd, nm, [float(x) for x in ys], [round(float(x), 4) for x in l], e2, e, kk))
    # c-differences
    cs = {s: [None if r["c"][s] is None else float(r["c"][s]) for r in rs] for s in ("1", "i", "j", "k")}
    print("  c_s:", {s: [None if v is None else round(v, 4) for v in cs[s]] for s in cs})
    dm = [math.log(float(r["absdetM"])) for r in rs]; mm = [math.log(float(r["maxM"])) for r in rs]
    print("  detM local exps:", [round(x, 4) for x in loc(dm)], " vs E00+E11 = %.4f;  detM/maxM^2 local:" % float(mu[0] + mu[3]), [round(x, 4) for x in loc([d - 2 * m for d, m in zip(dm, mm)])])
