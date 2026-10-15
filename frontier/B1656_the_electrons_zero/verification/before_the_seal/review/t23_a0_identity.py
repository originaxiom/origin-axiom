import numpy as np, sys
sys.path.insert(0, ".")
from load_inst import load
ns = load()
for k in ("pairs","residues","sector_twists","line_w","OM","GEN","SECTORS","SIXY","UNITS","np"): globals()[k] = ns[k]
LINES18 = [(b + i/3, b + j/3) for b in (1/9, 2/9) for i in range(3) for j in range(3)]
worst0 = worst1 = 0.0
for (p1, p2) in LINES18:
    w = line_w(p1, p2, OM)
    for sec in ("up", "down"):
        fl, fr = SECTORS[sec]; x, y = sector_twists(w, OM, SIXY[fl], SIXY[fr]); R = residues(x, y, OM)
        u = 0.05*np.exp(2j*np.pi*np.arange(128)/128); K = pairs(x, y, u, OM)["1"]/R["1"]
        a0 = np.mean(K - 1/u); a1 = np.mean((K - 1/u - a0)/u)
        worst0 = max(worst0, abs(a0)); worst1 = max(worst1, abs(a1))
print("identity channel at omega, 18 lines x (up,down): max|a0| = %.2e, max|a1| = %.2e" % (worst0, worst1))
