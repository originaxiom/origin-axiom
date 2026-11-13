# calibration C12: c_s at fixed tau against log|th_n(u~)| e^{-pi (Im u~)^2/Im tau} at a rotated point u~ of ubar
import sys, pathlib, math, random, itertools
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import numpy as np, b1656_kernel as B
exec(open(pathlib.Path(__file__).resolve().parent / "cal11.py").read().split("random.seed(11)")[0].split("THOF = ")[1].join(["THOF = ", ""]) if False else "")
NK = 30; m = np.arange(-NK, NK + 1)
def th(n, z, t):
    if n == 1: return -1j*np.sum((-1.0)**m*np.exp(1j*np.pi*t*(m+.5)**2 + 1j*np.pi*(2*m+1)*z))
    if n == 2: return np.sum(np.exp(1j*np.pi*t*(m+.5)**2 + 1j*np.pi*(2*m+1)*z))
    if n == 3: return np.sum(np.exp(1j*np.pi*t*m*m + 2j*np.pi*m*z))
    return np.sum((-1.0)**m*np.exp(1j*np.pi*t*m*m + 2j*np.pi*m*z))
ROT = {"u=a1 t+a2": lambda a1, a2, t: a1*t + a2, "u=a2 t-a1": lambda a1, a2, t: a2*t - a1,
       "u=-a2 t+a1": lambda a1, a2, t: -a2*t + a1, "u=a2 t+a1": lambda a1, a2, t: a2*t + a1,
       "u=2a1 t+2a2": lambda a1, a2, t: 2*(a1*t + a2), "u=2(a2 t-a1)": lambda a1, a2, t: 2*(a2*t - a1)}
random.seed(11)
for t in [0.21 + 1.13j, -0.37 + 0.92j]:
    data = []
    for _ in range(5):
        p1, p2 = random.uniform(0.05, 0.45), random.uniform(0.05, 0.95)
        w = B.line_w(p1, p2, t); x, y = B.sector_twists(w, t, 1, 0); R = B.residues(x, y, t); c = B.cA(x, y, t, R)
        a1 = w.imag / t.imag; a2 = w.real - a1 * t.real
        data.append((a1, a2, c, x))
    print("tau", t, " twists x:", [tuple(round(v, 3) for v in d[3]) for d in data][:2])
    for s in "1ijk":
        best = None
        for (rn, rf), n, k in itertools.product(ROT.items(), (1, 2, 3, 4), (2*math.pi, 4*math.pi)):
            v = []
            for (a1, a2, c, _) in data:
                if c[s] is None: continue
                u = rf(a1, a2, t)
                v.append(c[s] + k*(math.log(abs(th(n, u, t))) - math.pi*(u.imag)**2/t.imag))
            sp = max(v) - min(v)
            if best is None or sp < best[0]: best = (sp, rn, n, k/math.pi, v[0])
        print("   channel %s: spread %.2e  %s  theta_%d  k=%.0f pi  const %.9f" % (s, *best))
