"""Attacks 3-4 (large-L / B1646 coupling Y(a, R) only): exponents near tau = i of
   lift = |a.R| / (s1 |R|^2)   (m1/m3 up to |D|/(2 pi L), D(i) != 0)   and   m2/m3 = s2/s1 (exact SVD, never a proxy),
for sections a = f0 R + f1 dR + f2 d2R built with this referee's own coefficients (seed 1807) and own evaluator (refkit).
Slopes from eps = 1e-4, 1e-5, 1e-6 along three directions.  Also edge cases the draft does not state:
  * 7/2 class with f2(i) = 0 AND f0(i) = 0 (f0 = E4 E6^2 at 31/2): does m2/m3 ~ |tau - i|^2 survive?
  * 3/2 class with f2 = 0 identically at n >= 5 (19/2): m1 = 0 (large L)
  * the valence orders nu_i, nu_omega of E4, E6 (numerically).
    python3 ref_near_i.py  -> ref_near_i.json
"""
import json, pathlib, random
import mpmath as mp
from refkit import basis, dot, nrm2

HERE = pathlib.Path(__file__).resolve().parent
I = mp.mpc(0, 1)


def mono(a, b): return lambda e4, e6: e4 ** a * e6 ** b


def Mbasis(w): return [mono(a, (w - 4 * a) // 6) for a in range(w // 4 + 1) if w >= 0 and (w - 4 * a) % 6 == 0]


def make_section(n, seed, f2=None, f0=None):
    rng = random.Random(1807 * 100 + 10 * seed + n)
    cs = [[complex(rng.uniform(-2, 2), rng.uniform(-2, 2)) for _ in range(8)] for _ in range(3)]
    def fs(e4, e6):
        out = []
        for j in range(3):
            if j == 2 and f2 is not None: out.append(f2(e4, e6)); continue
            if j == 0 and f0 is not None: out.append(f0(e4, e6)); continue
            b = Mbasis(2 * n - 2 * j)
            out.append(sum(c * g(e4, e6) for c, g in zip(cs[j], b)) if b else mp.mpc(0))
        return out
    return fs


def evalsec(fs, tau):
    R, dR, d2R, eta6, e2, e4, e6 = basis(tau)
    f = fs(e4, e6)
    a = [f[0] * R[i] + f[1] * dR[i] + f[2] * d2R[i] for i in range(3)]
    return a, R


def masses(a, R):
    aR = dot(a, R)
    Y = mp.matrix(3, 3)
    for r in range(3):
        for c in range(3): Y[r, c] = a[r] * R[c] + R[r] * a[c] - (aR if r == c else 0)
    s = sorted([abs(x) for x in mp.svd_c(Y, compute_uv=False)], reverse=True)
    return abs(aR) / (s[0] * nrm2(R)), s[1] / s[0], s


def slopes(fs):
    rows = []
    for th in (0.3, 1.9, 4.1):
        L, M = [], []
        for e in (4, 5, 6):
            a, R = evalsec(fs, I + mp.mpf(10) ** -e * mp.exp(1j * th))
            lf, m23, _ = masses(a, R); L.append(lf); M.append(m23)
        sl = lambda v: [None if (v[k] < mp.mpf(10) ** -35 or v[k + 1] < mp.mpf(10) ** -35) else round(float(mp.log10(v[k] / v[k + 1])), 4) for k in range(2)]
        rows.append({"lift slopes": sl(L), "m2/m3 slopes": sl(M), "m2/m3 at 1e-6": mp.nstr(M[-1], 6), "lift at 1e-6": mp.nstr(L[-1], 4)})
    return rows


if __name__ == "__main__":
    cases = [("19/2 generic (f2 in M6 = <E6>)", 5, None, None), ("27/2 generic", 7, None, None), ("35/2 generic", 9, None, None),
             ("43/2 generic", 11, None, None), ("43/2 f2 = E6^3", 11, mono(0, 3), None), ("43/2 f2 = E4^3 E6", 11, mono(3, 1), None),
             ("15/2 generic", 4, None, None), ("31/2 generic", 8, None, None), ("31/2 f2 = E6^2", 8, mono(0, 2), None),
             ("39/2 f2 = E4 E6^2", 10, mono(1, 2), None), ("3/2", 1, None, None), ("11/2", 3, None, None),
             ("19/2 f2 = 0", 5, lambda e4, e6: mp.mpc(0), None),
             ("EDGE 31/2 f2 = E6^2 and f0 = E4 E6^2 (f0(i) = 0)", 8, mono(0, 2), mono(1, 2)),
             ("EDGE 31/2 f2 = E6^2 and f0 = E4^4 (f0(i) != 0)", 8, mono(0, 2), mono(4, 0))]
    out = {"cases": {}}
    for name, n, f2, f0 in cases:
        out["cases"][name] = {"seed%d" % s: slopes(make_section(n, s, f2, f0)) for s in (1, 2)}
        print(name, json.dumps(out["cases"][name]["seed1"][0]), flush=True)
    # valence orders at i and omega, numerically (slope of |f| in eps)
    w = mp.exp(2j * mp.pi / 3)
    val = {}
    for nm, g in (("E4", mono(1, 0)), ("E6", mono(0, 1)), ("E4^3 - E6^2 (Delta)", None)):
        for pt, p0 in (("i", I), ("omega", w)):
            v = []
            for e in (5, 6):
                R, dR, d2R, eta6, e2, e4, e6 = basis(p0 + mp.mpf(10) ** -e * mp.exp(0.7j))
                v.append(abs(g(e4, e6)) if g else abs(e4 ** 3 - e6 ** 2))
            val["%s at %s" % (nm, pt)] = round(float(mp.log10(v[0] / v[1])), 4)
    out["valence slopes"] = val
    (HERE / "ref_near_i.json").write_text(json.dumps(out, indent=1))
    print(json.dumps(val))
