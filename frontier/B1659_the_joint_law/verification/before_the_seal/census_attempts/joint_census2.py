"""EXPLORATION (main, firewalled; P-168; the data were SEEN -- a scoreboard). The inverse map of the joint law, fast:
B1656's frame at omega on W59's 18 lines, P4 (u_s = sqrt(2 pi L + c_s) R_s), ONE Higgs S (scale-free), log L free.
Targets: up m2/m3, m1/m3; down m2/m3, m1/m3; leptons m2/m3 (the electron is 0 on these lines for every S, L).
Least squares in log space (sigma floored at 5%: the frame is leading order), 64 starts per line, two seeds.
Read-outs at the best fit: the residuals, |d_S|, L, the CKM moduli under both index conventions (I-33's convention open)."""
import json, math, pathlib, pickle, sys
import numpy as np
from scipy.optimize import least_squares
ROOT = pathlib.Path(__file__).resolve().parents[3]
src = (ROOT / "frontier/B1656_the_electrons_zero/verification/the_electrons_zero.py").read_text(encoding="utf-8")
NS = {"__file__": str(ROOT / "frontier/B1656_the_electrons_zero/verification/x.py"), "__name__": "b1656_head"}
exec(compile(src.split("T0 = time.time()")[0], "b1656_head", "exec"), NS)
EDUAL, coupling, UNITS, BLOCKS, EPS = NS["EDUAL"], NS["coupling"], NS["UNITS"], NS["BLOCKS"], NS["EPS"]
DATA = pickle.load(open(pathlib.Path(__file__).with_name("sector_data.pkl"), "rb"))
SEED = int(sys.argv[1]) if len(sys.argv) > 1 else 1
NSTART = int(sys.argv[2]) if len(sys.argv) > 2 else 32
# Y_ab = sum T[a,b,i,j,k,l] S_ij M_kl, T = (C_a^T eps)[k,i] C_b[j,l]
T = np.einsum('aki,bjl->abijkl', np.array([C.T @ EPS for C in BLOCKS]), np.array(BLOCKS))
rng = np.random.default_rng(SEED)
for _ in range(3):
    S = rng.normal(size=(2, 2)) + 1j*rng.normal(size=(2, 2)); M = rng.normal(size=(2, 2)) + 1j*rng.normal(size=(2, 2))
    assert np.allclose(np.einsum('abijkl,ij,kl->ab', T, S, M), coupling(S, M), atol=1e-12)
    assert np.allclose((T.reshape(9, 16) @ np.kron(S.ravel(), M.ravel())).reshape(3, 3), coupling(S, M), atol=1e-12)
hz = json.load(open(ROOT / "frontier/B1637_fits_on_the_ruled_branch/received/HZ2021_running_masses_MZ.json"))["masses_GeV"]
v_, s_ = hz["value"], hz["sigma"]
def rr(a, b): r = v_[a]/v_[b]; return math.log(r), max(math.hypot(s_[a]/v_[a], s_[b]/v_[b]), 0.05)
TGT = [("up", 1, rr("c", "t")), ("up", 2, rr("u", "t")), ("down", 1, rr("s", "b")), ("down", 2, rr("d", "b")), ("lep", 1, rr("mu", "tau"))]
SECS = ("up", "down", "lep")
KM = T.reshape(9, 16)                                                         # vec Y = KM @ kron(vec S, vec M)
def Mparts(ln, sec):
    R, c = DATA[ln][sec]; ks = [s for s in UNITS if c[s] is not None]
    return np.array([c[s] for s in ks], dtype=float), np.array([R[s]*EDUAL[s] for s in ks])
PARTS = {ln: {sec: Mparts(ln, sec) for sec in SECS} for ln in DATA}
def Ms(ln, sec, L):
    cs, E = PARTS[ln][sec]; return np.tensordot(np.sqrt(2*np.pi*L + cs), E, 1)
def Yof(S, M): return (KM @ np.kron(S.ravel(), M.ravel())).reshape(3, 3)
def unpack(p): return (p[0:4] + 1j*p[4:8]).reshape(2, 2), math.exp(p[8])
def svs(S, ln, L): return {sec: np.linalg.svd(Yof(S, Ms(ln, sec, L)), compute_uv=False) for sec in SECS}
def resid(p, ln):
    S, L = unpack(p); sv = svs(S, ln, L)
    return np.array([(math.log(max(sv[sec][k]/sv[sec][0], 1e-300)) - mu)/sg for sec, k, (mu, sg) in TGT])
out = []
for ln in sorted(DATA):
    best = None
    for st in range(NSTART):
        p0 = np.concatenate([rng.normal(size=8), [math.log(10**rng.uniform(0.3, 3.5))]])
        try:
            r = least_squares(resid, p0, args=(ln,), method="trf", max_nfev=400, xtol=1e-12, ftol=1e-12, gtol=1e-12)
        except Exception as e:
            print("start failed:", repr(e)[:120], flush=True); continue
        if best is None or r.cost < best.cost: best = r
    S, L = unpack(best.x); Ys = {sec: Yof(S, Ms(ln, sec, L)) for sec in SECS}
    U = {sec: np.linalg.svd(Ys[sec]) for sec in SECS}
    V = U["up"][0].conj().T @ U["down"][0]; Vc = U["up"][2] @ U["down"][2].conj().T
    ck = lambda X: [abs(X[2, 1]), abs(X[1, 0]), abs(X[2, 0])]
    rec = {"line": list(ln), "chi2": 2*best.cost, "resid": best.fun.round(3).tolist(), "L": L,
           "dS_rel": abs(np.linalg.det(S))/np.linalg.norm(S)**2,
           "ratios": {sec: (U[sec][1][1]/U[sec][1][0], U[sec][1][2]/U[sec][1][0]) for sec in SECS},
           "ckm_rows": ck(V), "ckm_cols": ck(Vc)}
    out.append(rec)
    print(f"{ln[0]:.3f},{ln[1]:.3f} chi2 {rec['chi2']:8.2f} resid {rec['resid']} L {L:8.2f} |dS| {rec['dS_rel']:.3g} "
          f"CKM(us,cb,ub) rows {np.round(rec['ckm_rows'], 4).tolist()} cols {np.round(rec['ckm_cols'], 4).tolist()}", flush=True)
json.dump(out, open(pathlib.Path(__file__).with_name(f"joint_census2_seed{SEED}.json"), "w"), indent=1, default=float)
print("targets:", [(sec, k, round(math.exp(mu), 7)) for sec, k, (mu, sg) in TGT])
