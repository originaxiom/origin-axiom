import numpy as np, math, sys
sys.path.insert(0, ".")
from load_inst import load
ns = load()
for k in ("pairs","residues","sector_twists","line_w","OM","GEN","SECTORS","SIXY","UNITS","coupling","weighted_M","cA","D_of","nR2","np"): globals()[k] = ns[k]
rng = np.random.default_rng(31337)
w = line_w(5/9, 8/9, OM)
for sec in ("up", "down"):
    fl, fr = SECTORS[sec]; x, y = sector_twists(w, OM, SIXY[fl], SIXY[fr]); R = residues(x, y, OM); c = cA(x, y, OM, R, nth=64, ns=48)
    D = D_of(c, R)
    for _ in range(2):
        S = rng.normal(size=(2,2)) + 1j*rng.normal(size=(2,2))
        MR = weighted_M(R); Y0 = coupling(S, MR); s0 = np.linalg.svd(Y0, compute_uv=False)
        # ell_S(M) = det Y(M)/det M evaluated at M = M_R + small generic perturbation -> use linearity: ell(M_R) = lim; use exact: ell is linear, so ell(M_R) = ell(M_R + P) - ell(P)
        P = rng.normal(size=(2,2)) + 1j*rng.normal(size=(2,2))
        ell = lambda M: np.linalg.det(coupling(S, M))/np.linalg.det(M)
        ellR = ell(MR + P) - ell(P)
        pred = abs(D)*abs(ellR)/(8*np.pi*s0[0]**2*s0[1])
        out = []
        for L in (40.0, 640.0, 2560.0, 40960.0):
            u = {s: math.sqrt(2*np.pi*L + c[s])*R[s] for s in UNITS}
            sv = np.linalg.svd(coupling(S, weighted_M(u)), compute_uv=False)
            det_chk = abs(np.linalg.det(coupling(S, weighted_M(u)))) / (abs(D)/4*abs(ell(weighted_M(u))))
            out.append((L, L*sv[2]/sv[0]/pred, det_chk))
        print(sec, "pred (L sigma3/sigma1 limit) = %.4f" % pred, " ; ratio measured/pred and det-identity check:", [(L, round(r, 5), round(d, 12)) for L, r, d in out])
