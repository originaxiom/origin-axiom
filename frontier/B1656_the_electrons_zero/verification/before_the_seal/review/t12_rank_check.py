import numpy as np, math, sys
sys.path.insert(0, ".")
from load_inst import load
ns = load()
for k in ("pairs","bil","residues","sector_twists","line_w","OM","GEN","SECTORS","SIXY","UNITS","EC","EDUAL","weighted_M","coupling","BLOCKS","EPS","cA","nR2","np"): globals()[k] = ns[k]
rng = np.random.default_rng(5)
S = rng.normal(size=(2,2)) + 1j*rng.normal(size=(2,2))
w = line_w(4/9, 7/9, OM)
for sec, (fl, fr) in SECTORS.items():
    x, y = sector_twists(w, OM, SIXY[fl], SIXY[fr]); R = residues(x, y, OM)
    MR = weighted_M(R)
    sv = np.linalg.svd(coupling(S, MR), compute_uv=False)
    # rank-3 control: reweight the channels
    u = {s: R[s]*(1.0 + 0.3*k) for k, s in enumerate(UNITS)}
    sv2 = np.linalg.svd(coupling(S, weighted_M(u)), compute_uv=False)
    print(sec, "residue coupling sigma3/sigma1 = %.1e" % (sv[2]/sv[0]), " | channel-reweighted (u_s = R_s (1+0.3k)): %.3e" % (sv2[2]/sv2[0]))
# the claim that M' = sum u_s E_s has det proportional to sum u_s^2 : det M' vs (1/4) sum u_s^2 ?
u = {s: complex(*rng.normal(size=2)) for s in UNITS}
M = weighted_M(u); print("det M' =", np.linalg.det(M), " ; sum u_s^2 =", sum(v*v for v in u.values()), " ratio:", np.linalg.det(M)/sum(v*v for v in u.values()))
