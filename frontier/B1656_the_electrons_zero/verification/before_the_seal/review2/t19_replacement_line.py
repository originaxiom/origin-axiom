# Review 2: the suggested replacement line (2/9,2/9) = LINES18[9] (class 2): E6-like criteria with a non-1655 seed, tail MC (seed 8128), E5(a)(c)(d) values
import numpy as np, math, sys, pathlib
sys.path.insert(0, ".")
from load_inst import load
ns = load()
for k in ("residues","sector_twists","line_w","OM","GEN","SECTORS","SIXY","UNITS","nR2","np","coupling","weighted_M","cA","D_of","BLOCKS","EPS"): globals()[k] = ns[k]
SRC = pathlib.Path(__file__).resolve().parents[2].joinpath("the_electrons_zero.py").read_text()
exec(SRC[SRC.index("def l_S(S, M):"): SRC.index("e6 = {")], globals())
CT = np.array([[Ca.T @ EPS for Ca in BLOCKS]], dtype=complex)[0]
def coupling_stack(Ss, M):
    T = np.einsum('aik,nkl,blj->nabij', CT, Ss, np.array(BLOCKS)); return np.einsum('nabij,ij->nab', T, M)
def lS_stack(Ss, M):
    c0 = float(np.abs(M).max()); E = c0*np.eye(2, dtype=complex)
    f = lambda N: np.linalg.det(coupling_stack(Ss, N))/np.linalg.det(N); return f(M + E) - f(E)
rng = np.random.default_rng(8128); NS = 20000
Ss = rng.normal(size=(NS, 2, 2)) + 1j*rng.normal(size=(NS, 2, 2))
p1, p2 = 2/9, 2/9; w = line_w(p1, p2, OM); tot = 0; n = 0
for sec in ("up", "down"):
    fl, fr = SECTORS[sec]; x, y = sector_twists(w, OM, SIXY[fl], SIXY[fr]); R = residues(x, y, OM); c = cA(x, y, OM, R, nth=64, ns=48)
    vals = {}
    for L in (40.0, 640.0, 2560.0):
        u = {s: math.sqrt(2*np.pi*L + c[s])*R[s] for s in UNITS}
        sv = np.linalg.svd(coupling_stack(Ss, weighted_M(u)), compute_uv=False); vals[L] = sv[:, 2]/sv[:, 0]
    MR = weighted_M(R); s0 = np.linalg.svd(coupling_stack(Ss, MR), compute_uv=False)
    pred = abs(D_of(c, R))*np.abs(lS_stack(Ss, MR))/(8*np.pi*s0[:, 0]**2*s0[:, 1])
    eL = np.abs(2560*vals[2560.0]/(640*vals[640.0]) - 1); elaw = np.abs(2560*vals[2560.0]/pred - 1); e40 = vals[40.0]
    bad = (eL >= 0.02) | (elaw >= 0.02) | (e40 <= 1e-6); tot += bad.sum(); n += NS
    print("(2/9,2/9)", sec, "|D|/|R|^2 %.4f ; P(L-ratio>=2%%) %.5f P(law>=2%%) %.6f P(q40<=1e-6) %.6f ; law median %.1e max %.1e" % (abs(D_of(c, R))/nR2(R), (eL >= .02).mean(), (elaw >= .02).mean(), (e40 <= 1e-6).mean(), np.median(elaw), elaw.max()))
print("per-draw failure prob %.5f" % (tot/n))
