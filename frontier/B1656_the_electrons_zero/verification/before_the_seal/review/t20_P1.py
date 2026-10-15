import numpy as np, sys
sys.path.insert(0, ".")
from load_inst import load
ns = load()
for k in ("pairs","residues","sector_twists","line_w","OM","GEN","SECTORS","SIXY","UNITS","np"): globals()[k] = ns[k]
z = np.array([0.21+0.17j, -0.33+0.05j, 0.1-0.4j])
for t in (OM, GEN):
    w = line_w(4/9, 7/9, t); x, y = sector_twists(w, t, SIXY["L"], SIXY["e"]); P = pairs(x, y, z, t)
    print("tau", np.round(t,3), " lep |P_1|/max|P_s| at regular points:", [float(abs(P["1"][k])/max(abs(P[s][k]) for s in UNITS)) for k in range(3)])
