"""Referee's independent weighted channel norm: Duffy-transformed Gauss-Legendre over the lattice square (origin at a vertex of
8 triangles), integrand W|K_s|^2 - W0/|z|^2 (O(1/|z|), bounded after the Duffy Jacobian), restored by W0 * I_log with
I_log = int_0^{2pi} log rmax(theta) dtheta.  Kernels K_s = P_s/R_s are the frame's (b1656_funcs.pairs)."""
import sys, io, math, contextlib, importlib.util, pathlib, numpy as np
from numpy.polynomial.legendre import leggauss
ROOT = next(q for q in __import__("pathlib").Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
spec = importlib.util.spec_from_file_location("c26", ROOT / "frontier/B1726_the_two_ingredients_replicated/verification/census.py")
C = importlib.util.module_from_spec(spec); spec.loader.exec_module(C)
MM = C._modules(); B, te, col = MM["B"], MM["te"], MM["col"]

def I_log(t, n=400):
    br = B.vangles(t); xg, wg = leggauss(n); tot = 0.0
    for a, b in zip(br[:-1], br[1:]):
        th = 0.5*(b-a)*xg + 0.5*(b+a); tot += np.sum(0.5*(b-a)*wg*np.log(B.rmax_np(th, t)))
    return float(tot)

def duffy_nodes(t, n):
    g, w = leggauss(n); u = 0.25*(g + 1); wu = 0.25*w; v = 0.5*(g + 1); wv = 0.5*w        # u in [0,1/2], v in [0,1]
    U, V = np.meshgrid(u, v, indexing="ij"); WW = np.outer(wu, wv) * U                       # Jacobian u
    Z, Wt = [], []
    for sx in (1, -1):
        for sy in (1, -1):
            for swap in (0, 1):
                x1, y1 = (U, U*V) if not swap else (U*V, U)
                Z.append(sx*x1 + sy*y1*t); Wt.append(WW*t.imag)
    return np.concatenate([z.ravel() for z in Z]), np.concatenate([w.ravel() for w in Wt])

def lattice(z, t):
    y1 = z.imag/t.imag; return z.real - y1*t.real, y1

def c_weighted(x, y, t, R, Wfun=None, n=96):
    """regularised int |K_s|^2 W  =  int_P (W|K|^2 - W0/|z|^2) + W0 I_log   (the eps -> 0 limit of B1656's cA, weighted).
    Returns (c dict, W0).  The cut norm at the horocycle is then 2 pi W0 L + c."""
    z, wt = duffy_nodes(t, n); P = B.pairs(x, y, z, t)
    Wz = np.ones(z.shape) if Wfun is None else Wfun(z); W0 = 1.0 if Wfun is None else float(Wfun(np.array([0j]))[0])
    Il = I_log(t); out = {}
    for s in B.UNITS:
        if abs(R[s]) < 1e-12: out[s] = None; continue
        out[s] = float(np.sum(wt*(Wz*np.abs(P[s]/R[s])**2 - W0/np.abs(z)**2)) + W0*Il)
    return out, W0

def higgs_S(t):
    import mpmath as mp
    av = [complex(te.ev(cc, mp.mpc(t.real, t.imag))) for cc in te.B[1]]
    return av[0]*B.QI + av[1]*B.QJ + av[2]*B.QK

def L_of(im_t): return float(np.interp(im_t, [q[0] for q in col], [q[1] for q in col]))

def ratios_from_lam2(lam2, Rd, Rl, S):
    """lam2[s] = the channel's cut norm (common to both sectors); returns R2, R1 and the sectors' (m2/m3, m1/m3)"""
    out = {}
    for sec, R in (("down", Rd), ("lep", Rl)):
        u = {s: (math.sqrt(lam2[s])*R[s] if lam2[s] is not None and lam2[s] > 0 else 0) for s in B.UNITS}
        sv = np.linalg.svd(B.coupling(S, B.weighted_M(u)), compute_uv=False); out[sec] = (sv[1]/sv[0], sv[2]/sv[0])
    return out["lep"][0]/out["down"][0], out["down"][1]/out["lep"][1], out

def sector_data(a, b, t):
    w = float(a)*t + float(b); d = {}
    for sec, (lf, rf) in (("down", ("Q", "d")), ("lep", ("L", "e"))):
        x, y = B.sector_twists(w, t, B.SIXY[lf], B.SIXY[rf]); d[sec] = (x, y, B.residues(x, y, t))
    return d
