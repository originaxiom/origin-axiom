# calibration C13: the kernel's own multipliers K(z+1) = e(alpha) K(z), K(z+tau) = e(beta) K(z), read from B1656's code,
# and c_s against -2 pi log|g_a(tau)| (the Kronecker function) at a characteristic a built from (alpha, beta)
import sys, pathlib, math, cmath, random, itertools
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import numpy as np, b1656_kernel as B, sm_c7_lib as L
def mult(x, y, t, R, s):
    z = np.array([0.11 + 0.07j]); K = lambda zz: B.pairs(x, y, zz, t)[s] / R[s]
    a = cmath.phase(complex(K(z + 1)[0] / K(z)[0])) / (2 * math.pi); b = cmath.phase(complex(K(z + t)[0] / K(z)[0])) / (2 * math.pi)
    return a % 1.0, b % 1.0
def kronA(a, t):            # -2 pi log|g_a(t)|
    return L.kron((a[1], -a[0]), t)
random.seed(13)
CANDS = {"(al,-be)": lambda al, be: (al, -be), "(be,al)": lambda al, be: (be, al), "(-be,al)": lambda al, be: (-be, al),
         "(be,-al)": lambda al, be: (be, -al), "(al,be)": lambda al, be: (al, be), "(-al,be)": lambda al, be: (-al, be)}
for t in [0.21 + 1.13j, -0.37 + 0.92j]:
    data = []
    for _ in range(5):
        p1, p2 = random.uniform(0.05, 0.45), random.uniform(0.05, 0.95)
        w = B.line_w(p1, p2, t); x, y = B.sector_twists(w, t, 1, 0); R = B.residues(x, y, t); c = B.cA(x, y, t, R)
        data.append({s: (c[s], mult(x, y, t, R, s)) for s in c if c[s] is not None})
    print("tau", t, " multipliers (ch 1):", [tuple(round(v, 4) for v in d["1"][1]) for d in data])
    for s in "1ijk":
        best = None
        for (cn, cf), k in itertools.product(CANDS.items(), (1.0, 2.0, -1.0, -2.0)):
            v = [d[s][0] - k * kronA(cf(*d[s][1]), t) for d in data if s in d]
            sp = max(v) - min(v)
            if best is None or sp < best[0]: best = (sp, cn, k, v[0])
        print("   channel %s: spread %.2e  a=%s  c_s - %.0f*(-2pi log|g_a|)  const %.9f" % (s, *best))
