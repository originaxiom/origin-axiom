# E0's void gates exactly as sealed (a copy of the block), reporting each margin
import numpy as np, math, sys
sys.path.insert(0, ".")
from load_inst import load
ns = load()
for k in ("bil","bil_mp","residues","sector_twists","line_w","OM","GEN","SECTORS","SIXY","UNITS","nR2","np","mp","NK"): globals()[k] = ns[k]
mp.mp.dps = 30
dd = 0.0; per = []
for (p1, p2) in [(1/9, 1/9), (2/9, 5/9)]:
    w = line_w(p1, p2, OM)
    for sec, (fl, fr) in SECTORS.items():
        x, y = sector_twists(w, OM, SIXY[fl], SIXY[fr])
        for z in (0.17+0.11j, -0.22+0.31j):
            Mn = bil(x, y, np.array(z), OM); Mm = bil_mp((mp.mpf(x[0]), mp.mpf(x[1])), (mp.mpf(y[0]), mp.mpf(y[1])), mp.mpc(z), mp.mpc(OM))
            ents = [abs(complex(Mn[m][n]) - complex(Mm[m][n]))/abs(complex(Mm[m][n])) for m in range(2) for n in range(2)]
            per.append((float(max(ents)), min(abs(complex(Mm[m][n])) for m in range(2) for n in range(2))))
            dd = max(dd, max(ents))
print("numpy_vs_B1653_bilinear = %.2e (void if >= 1e-11); smallest |entry| over the cases = %.2e" % (dd, min(p[1] for p in per)))
mp.mp.dps = 20
CPRED = {"1": -1j, "i": -1, "j": -1, "k": 1j}; THOF = {"1": 1, "i": 2, "j": 4, "k": 3}
def th_any(n, z, t):
    m = np.arange(-NK, NK + 1); z = complex(z)
    if n == 1: return complex(-1j*np.sum((-1.0)**m*np.exp(1j*np.pi*t*(m+.5)**2 + 1j*np.pi*(2*m+1)*z)))
    if n == 2: return complex(np.sum(np.exp(1j*np.pi*t*(m+.5)**2 + 1j*np.pi*(2*m+1)*z)))
    if n == 3: return complex(np.sum(np.exp(1j*np.pi*t*m*m + 2j*np.pi*m*z)))
    return complex(np.sum((-1.0)**m*np.exp(1j*np.pi*t*m*m + 2j*np.pi*m*z)))
LINES18 = [(b + i/3, b + j/3) for b in (1/9, 2/9) for i in range(3) for j in range(3)]
nullmax = 0.0; formmax = 0.0
for (p1, p2) in LINES18[:4] + [(0.137, 0.291)]:
    for t in (OM, GEN):
        w = line_w(p1, p2, t)
        for sec, (fl, fr) in SECTORS.items():
            x, y = sector_twists(w, t, SIXY[fl], SIXY[fr]); R = residues(x, y, t)
            nullmax = max(nullmax, abs(sum(R[s]**2 for s in UNITS))/nR2(R))
            ub = SIXY[fl]*w + SIXY[fr]*w; de = SIXY[fl]*w - SIXY[fr]*w
            pred = {s: CPRED[s]*th_any(THOF[s], ub, t)*th_any(THOF[s], de, t) for s in UNITS}
            ref = R["i"]/pred["i"]
            formmax = max(formmax, max(abs(R[s] - ref*pred[s]) for s in UNITS)/math.sqrt(nR2(R)))
print("null quaternion %.2e (void if >= 1e-12); B1653 residue formula %.2e (void if >= 1e-10)" % (nullmax, formmax))
