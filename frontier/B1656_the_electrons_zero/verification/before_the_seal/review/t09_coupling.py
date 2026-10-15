# check 3: dual basis, weighted_M, coupling; and the E6 logic on OTHER lines with ANOTHER seed (not the sealed draws)
import numpy as np, math, sys
sys.path.insert(0, ".")
from load_inst import load
ns = load()
for k in ("pairs","bil","residues","sector_twists","line_w","OM","GEN","SECTORS","SIXY","UNITS","EC","EDUAL","weighted_M","coupling","BLOCKS","EPS","cA","nR2","np"): globals()[k] = ns[k]
# (a) pair(M', C_t) == u_t ; M_R from residue of the bilinear equals sum R_s E_s
rng = np.random.default_rng(99)
u = {s: complex(*rng.normal(size=2)) for s in UNITS}
M = weighted_M(u)
print("pair(M',C_t)-u_t max:", max(abs(np.sum(EC[t]*M) - u[t]) for t in UNITS))
w = line_w(5/9, 8/9, OM); x, y = sector_twists(w, OM, SIXY["Q"], SIXY["u"]); R = residues(x, y, OM)
rho = 0.01; N = 256; uu = rho*np.exp(2j*np.pi*np.arange(N)/N); B = bil(x, y, uu, OM)       # shape (2,2,N)
Mres = np.mean(B*uu[None, None, :], axis=-1)
MR = weighted_M(R)
print("residue matrix vs sum R_s E_s:", np.max(np.abs(Mres - MR)), " det/|.|^2 (rank one):", abs(np.linalg.det(MR))/np.max(np.abs(MR))**2)
# the dual basis explicitly
for s in UNITS: print(s, np.round(EDUAL[s], 3).tolist())
# (b) the E6 logic at other lines and another seed
rng = np.random.default_rng(424242)
def rndS(): return rng.normal(size=(2, 2)) + 1j*rng.normal(size=(2, 2))
SS = [rndS() for _ in range(5)]
lep_max = 0.0; qerr = []; q40 = []
for (p1, p2) in [(5/9, 8/9), (7/9, 4/9), (8/9, 8/9)]:
    w = line_w(p1, p2, OM)
    for sec, (fl, fr) in SECTORS.items():
        x, y = sector_twists(w, OM, SIXY[fl], SIXY[fr]); R = residues(x, y, OM); c = cA(x, y, OM, R, nth=64, ns=48)
        for S in SS:
            vals = {}
            for L in (40.0, 640.0, 2560.0):
                uvec = {s: (math.sqrt(2*np.pi*L + c[s])*R[s] if c[s] is not None else 0j) for s in UNITS}
                sv = np.linalg.svd(coupling(S, weighted_M(uvec)), compute_uv=False); vals[L] = sv[2]/sv[0]
            if sec == "lep": lep_max = max(lep_max, max(vals.values()))
            else: qerr.append(abs(2560*vals[2560]/(640*vals[640]) - 1)); q40.append(vals[40.0])
print("lepton sigma3/sigma1 max over L,S,lines: %.2e (thr 1e-12)" % lep_max)
print("quark L-ratio rel err max %.2e (thr 0.02); sigma3/sigma1 at L=40 min %.2e (thr 1e-6), max %.2e" % (max(qerr), min(q40), max(q40)))
