# calibration C11: the closed form of c_s at fixed tau. Candidates: c_s + k log|th_s(ubar)| - g (Im ubar)^2/Im tau,
# which must not depend on ubar
import sys, pathlib, math, random, itertools
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import numpy as np, b1656_kernel as B
THOF = {"1": 1, "i": 2, "j": 4, "k": 3}
NK = 30; m = np.arange(-NK, NK + 1)
def th(n, z, t):
    if n == 1: return -1j*np.sum((-1.0)**m*np.exp(1j*np.pi*t*(m+.5)**2 + 1j*np.pi*(2*m+1)*z))
    if n == 2: return np.sum(np.exp(1j*np.pi*t*(m+.5)**2 + 1j*np.pi*(2*m+1)*z))
    if n == 3: return np.sum(np.exp(1j*np.pi*t*m*m + 2j*np.pi*m*z))
    return np.sum((-1.0)**m*np.exp(1j*np.pi*t*m*m + 2j*np.pi*m*z))
random.seed(11)
for t in [0.21 + 1.13j, -0.37 + 0.92j]:
    data = []
    for _ in range(5):
        p1, p2 = random.uniform(0.05, 0.45), random.uniform(0.05, 0.95)
        w = B.line_w(p1, p2, t); x, y = B.sector_twists(w, t, 1, 0); R = B.residues(x, y, t); c = B.cA(x, y, t, R)
        data.append((w, c))
    print("tau", t)
    for s in "1ijk":
        best = None
        for k, g in itertools.product([2*math.pi, 4*math.pi, -2*math.pi, -4*math.pi], [0, 2*math.pi**2, 4*math.pi**2, -2*math.pi**2, -4*math.pi**2]):
            v = [c[s] + k*math.log(abs(th(THOF[s], w, t))) - g*(w.imag)**2/t.imag for (w, c) in data if c[s] is not None]
            sp = max(v) - min(v)
            if best is None or sp < best[0]: best = (sp, k/math.pi, g/math.pi**2, v[0])
        print("   channel %s: best spread %.2e with k = %+.0f pi, g = %+.0f pi^2, constant %.9f" % (s, *best))
