import numpy as np, sys
sys.path.insert(0, ".")
from load_inst import load
ns = load()
for k in ("bil","residues","sector_twists","line_w","OM","GEN","SECTORS","SIXY","weighted_M","np"): globals()[k] = ns[k]
worst = 0; worst1 = 0
for (p1, p2), t in [((2/9, 5/9), OM), ((0.137, 0.291), GEN), ((1/9, 2/9), OM)]:
    w = line_w(p1, p2, t)
    for sec, (fl, fr) in SECTORS.items():
        x, y = sector_twists(w, t, SIXY[fl], SIXY[fr]); R = residues(x, y, t); MR = weighted_M(R)
        uu = 0.01*np.exp(2j*np.pi*np.arange(256)/256); B = bil(x, y, uu, t); Mres = np.mean(B*uu[None, None, :], axis=-1)
        worst = max(worst, np.max(np.abs(Mres - MR))/np.max(np.abs(MR))); worst1 = max(worst1, abs(np.linalg.det(MR))/np.max(np.abs(MR))**2)
print("residue matrix of the bilinear == weighted_M(R): max rel diff %.2e ; rank one: max |det|/max^2 = %.2e" % (worst, worst1))
