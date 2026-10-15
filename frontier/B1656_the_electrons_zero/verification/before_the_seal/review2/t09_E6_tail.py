# Review 2, check 4c: the tail risk of E6's quark criteria under the sealed design (5 S x MIX3 lines x {up,down} = 30 draws), using MANY random S (seed 8128, NOT 1655) on the MIX3 lines.
import numpy as np, math, sys, time, pathlib
sys.path.insert(0, ".")
from load_inst import load
ns = load()
for k in ("residues","sector_twists","line_w","OM","GEN","SECTORS","SIXY","UNITS","nR2","np","coupling","weighted_M","cA","D_of","BLOCKS","EPS"): globals()[k] = ns[k]
SRC = pathlib.Path(__file__).resolve().parents[2].joinpath("the_electrons_zero.py").read_text()
exec(SRC[SRC.index("def l_S(S, M):"): SRC.index("e6 = {")], globals())
# vectorised coupling for a stack of S:  Y[n,a,b] = sum_mn (Ca^T EPS S_n Cb)_mn M_mn
CT = np.array([[Ca.T @ EPS for Ca in BLOCKS]], dtype=complex)[0]          # (3,2,2): Ca^T EPS
def coupling_stack(Ss, M):
    # (Ca^T EPS) S Cb : einsum
    T = np.einsum('aik,nkl,blj->nabij', CT, Ss, np.array(BLOCKS))
    return np.einsum('nabij,ij->nab', T, M)
def lS_stack(Ss, M):
    c0 = float(np.abs(M).max()); E = c0*np.eye(2, dtype=complex)
    f = lambda N: np.linalg.det(coupling_stack(Ss, N))/np.linalg.det(N)
    return f(M + E) - f(E)
# sanity: vectorised == instrument
rng = np.random.default_rng(1); S0 = rng.normal(size=(2,2)) + 1j*rng.normal(size=(2,2)); M0 = rng.normal(size=(2,2)) + 1j*rng.normal(size=(2,2))
assert np.allclose(coupling_stack(S0[None], M0)[0], coupling(S0, M0))
LINES18 = [(b_ + i/3, b_ + j/3) for b_ in (1/9, 2/9) for i in range(3) for j in range(3)]
MIX3 = [LINES18[0], LINES18[4], LINES18[13]]
rng = np.random.default_rng(8128); NS = 20000
Ss = rng.normal(size=(NS, 2, 2)) + 1j*rng.normal(size=(NS, 2, 2))
tot = {"L": 0, "q40": 0, "law": 0, "any": 0}; n_tot = 0
for (p1, p2) in MIX3:
    w = line_w(p1, p2, OM)
    for sec in ("up", "down"):
        fl, fr = SECTORS[sec]; x, y = sector_twists(w, OM, SIXY[fl], SIXY[fr]); R = residues(x, y, OM); c = cA(x, y, OM, R, nth=64, ns=48)
        vals = {}
        for L in (40.0, 640.0, 2560.0):
            u = {s: math.sqrt(2*np.pi*L + c[s])*R[s] for s in UNITS}
            sv = np.linalg.svd(coupling_stack(Ss, weighted_M(u)), compute_uv=False); vals[L] = sv[:, 2]/sv[:, 0]
        MR = weighted_M(R); s0 = np.linalg.svd(coupling_stack(Ss, MR), compute_uv=False)
        pred = abs(D_of(c, R))*np.abs(lS_stack(Ss, MR))/(8*np.pi*s0[:, 0]**2*s0[:, 1])
        eL = np.abs(2560*vals[2560.0]/(640*vals[640.0]) - 1); e40 = vals[40.0]; elaw = np.abs(2560*vals[2560.0]/pred - 1)
        fL, f40, fl_ = eL >= 0.02, e40 <= 1e-6, elaw >= 0.02
        print((round(9*p1), round(9*p2)), sec, "P(L-ratio>=2%%) %.4f | P(sigma3/sigma1(40)<=1e-6) %.5f | P(law>=2%%) %.5f | median L-err %.1e, 99pct %.1e, max %.1e | law med %.1e 99pct %.1e max %.1e" % (
              fL.mean(), f40.mean(), fl_.mean(), np.median(eL), np.percentile(eL, 99), eL.max(), np.median(elaw), np.percentile(elaw, 99), elaw.max()))
        tot["L"] += fL.sum(); tot["q40"] += f40.sum(); tot["law"] += fl_.sum(); tot["any"] += (fL | f40 | fl_).sum(); n_tot += NS
p = tot["any"]/n_tot
print("per-draw failure prob (any of the three quark criteria): %.5f  -> P(at least one of the 30 sealed draws fails) = %.3f" % (p, 1 - (1 - p)**30))
print("components: L-ratio %.5f, q40 %.6f, law %.6f" % (tot["L"]/n_tot, tot["q40"]/n_tot, tot["law"]/n_tot))
