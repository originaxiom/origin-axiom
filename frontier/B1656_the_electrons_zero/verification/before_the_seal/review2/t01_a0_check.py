# Review 2, check 1a: is a0_of() accurate?  (i) radius/N independence, (ii) independent theory: a0(s) - th_s'(ubar)/th_s(ubar) = const (=2 pi i A) across s
import numpy as np, math, sys
sys.path.insert(0, ".")
from load_inst import load
ns = load()
for k in ("pairs","residues","sector_twists","line_w","OM","GEN","SECTORS","SIXY","UNITS","nR2","np","a0_of","NK"): globals()[k] = ns[k]
THOF = {"1": 1, "i": 2, "j": 4, "k": 3}
def th_and_d(n, z, t):
    m = np.arange(-NK, NK + 1); z = complex(z)
    if n == 1:
        e = np.exp(1j*np.pi*t*(m+.5)**2 + 1j*np.pi*(2*m+1)*z)*(-1.0)**m*(-1j); d = e*1j*np.pi*(2*m+1)
    elif n == 2:
        e = np.exp(1j*np.pi*t*(m+.5)**2 + 1j*np.pi*(2*m+1)*z); d = e*1j*np.pi*(2*m+1)
    elif n == 3:
        e = np.exp(1j*np.pi*t*m*m + 2j*np.pi*m*z); d = e*2j*np.pi*m
    else:
        e = (-1.0)**m*np.exp(1j*np.pi*t*m*m + 2j*np.pi*m*z); d = e*2j*np.pi*m
    return complex(e.sum()), complex(d.sum())
def a0_variants(x, y, t, R):
    out = {}
    for (rad, N) in [(0.05, 128), (0.02, 64), (0.1, 128), (0.01, 64), (0.05, 256), (0.2, 128)]:
        out[(rad, N)] = a0_of(x, y, t, R, rad=rad, N=N)
    return out
cases = [((2/9, 5/9), OM), ((4/9, 7/9), OM), ((0.137, 0.291), GEN), ((0.613, 0.287), -0.17+0.95j), ((1/9, 2/9), OM), ((5/9, 8/9), 0.31+0.7j), ((2/9, 5/9), 0.0+1.9j), ((1/9, 4/9), 0.45+0.6j)]
worst_rad = 0.0; worst_const = 0.0
for (p1, p2), t in cases:
    w = line_w(p1, p2, t)
    for sec, (fl, fr) in SECTORS.items():
        x, y = sector_twists(w, t, SIXY[fl], SIXY[fr]); R = residues(x, y, t)
        V = a0_variants(x, y, t, R); base = V[(0.05, 128)]
        ub = (SIXY[fl] + SIXY[fr])*w
        consts = {}
        for s in UNITS:
            if base[s] is None: continue
            for key, v in V.items():
                worst_rad = max(worst_rad, abs(v[s] - base[s]))
            th, dth = th_and_d(THOF[s], ub, t)
            consts[s] = base[s] - dth/th
        vals = list(consts.values())
        spread = max(abs(a - b) for a in vals for b in vals)
        worst_const = max(worst_const, spread)
        print((round(p1,3), round(p2,3)), np.round(t,3), sec, "|a0|", {s: round(abs(base[s]),4) for s in UNITS if base[s] is not None}, "const spread %.2e" % spread, "2piiA ~", np.round(vals[0],5))
print("max over variants |a0(rad,N) - a0(0.05,128)| = %.3e ; max spread of a0(s) - th_s'/th_s (ubar) across s = %.3e" % (worst_rad, worst_const))
