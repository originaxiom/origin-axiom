# E0-like plumbing at lines/taus other than the sealed ones: numpy bilinear vs mp bilinear; null quaternion; residue formula
import numpy as np, math, sys
sys.path.insert(0, ".")
from load_inst import load
ns = load()
for k in ("bil","bil_mp","residues","sector_twists","line_w","OM","GEN","SECTORS","SIXY","UNITS","nR2","np","mp","NK","twist_of"): globals()[k] = ns[k]
mp.mp.dps = 30
dd = 0.0
for (p1, p2) in [(5/9, 8/9), (7/9, 4/9), (8/9, 8/9)]:
    for t in (OM, -0.17+0.95j):
        w = line_w(p1, p2, t)
        for sec, (fl, fr) in SECTORS.items():
            x, y = sector_twists(w, t, SIXY[fl], SIXY[fr])
            for z in (0.17+0.11j, -0.22+0.31j):
                Mn = bil(x, y, np.array(z), t); Mm = bil_mp((mp.mpf(x[0]), mp.mpf(x[1])), (mp.mpf(y[0]), mp.mpf(y[1])), mp.mpc(z), mp.mpc(t))
                dd = max(dd, max(abs(complex(Mn[m][n]) - complex(Mm[m][n]))/abs(complex(Mm[m][n])) for m in range(2) for n in range(2)))
print("numpy vs mp bilinear max rel diff %.2e (thr 1e-11)" % dd)
CPRED = {"1": -1j, "i": -1, "j": -1, "k": 1j}; THOF = {"1": 1, "i": 2, "j": 4, "k": 3}
def th_any(n, z, t):
    q = np.exp(1j*np.pi*t); m = np.arange(-NK, NK + 1); z = complex(z)
    if n == 1: return complex(-1j*np.sum((-1.0)**m*np.exp(1j*np.pi*t*(m+.5)**2 + 1j*np.pi*(2*m+1)*z)))
    if n == 2: return complex(np.sum(np.exp(1j*np.pi*t*(m+.5)**2 + 1j*np.pi*(2*m+1)*z)))
    if n == 3: return complex(np.sum(np.exp(1j*np.pi*t*m*m + 2j*np.pi*m*z)))
    return complex(np.sum((-1.0)**m*np.exp(1j*np.pi*t*m*m + 2j*np.pi*m*z)))
nullmax = 0.0; formmax = 0.0; worst = None
for (p1, p2) in [(5/9, 8/9), (7/9, 4/9), (8/9, 8/9), (0.613, 0.287), (1/9, 2/9)]:
    for t in (OM, -0.17+0.95j):
        w = line_w(p1, p2, t)
        for sec, (fl, fr) in SECTORS.items():
            x, y = sector_twists(w, t, SIXY[fl], SIXY[fr]); R = residues(x, y, t)
            nullmax = max(nullmax, abs(sum(R[s]**2 for s in UNITS))/nR2(R))
            ub = SIXY[fl]*w + SIXY[fr]*w; de = SIXY[fl]*w - SIXY[fr]*w
            pred = {s: CPRED[s]*th_any(THOF[s], ub, t)*th_any(THOF[s], de, t) for s in UNITS}
            ref = R["i"]/pred["i"]
            e = max(abs(R[s] - ref*pred[s]) for s in UNITS)/math.sqrt(nR2(R))
            if e > formmax: formmax = e; worst = (p1, p2, str(np.round(t,3)), sec)
print("null quaternion max %.2e (thr 1e-12)" % nullmax, "residue formula max %.2e (thr 1e-10)" % formmax, worst)
# the twist_of / line-point identity: wpt(twist_of(q w)) == q w
def wpt(x, t): return x[0]*t + x[1]/2
w = line_w(8/9, 7/9, OM)
print("wpt(twist_of(6w)) - 6w =", abs(wpt(twist_of(6*w, OM), OM) - 6*w), " ; delta check: ", abs((wpt(twist_of(-3*w, OM), OM) - wpt(twist_of(6*w, OM), OM)) - (-9*w)))
