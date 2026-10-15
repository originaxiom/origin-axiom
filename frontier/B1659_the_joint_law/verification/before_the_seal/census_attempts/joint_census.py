"""EXPLORATION (main, firewalled; P-168; the data were SEEN -- a scoreboard, not a test).
B1656's frame at tau = omega on W59's 18 lines, the canonical end condition P4 (u_s = sqrt(2 pi L + c_s) R_s), ONE Higgs S.
Per line: fit S (scale-free) and log L to the five non-electron ratios (up m2/m3, m1/m3; down m2/m3, m1/m3; lep m2/m3)
in log space; report the best misfit, the lepton m1 (structurally 0 on W59's lines), and the CKM moduli at the best fit
(rows = the first index of Y read as left-handed; a read-out). Also checks the closed forms on the actual sector matter."""
import json, math, pathlib, sys, time
import numpy as np
from scipy.optimize import minimize
ROOT = pathlib.Path(__file__).resolve().parents[3]
src = (ROOT / "frontier/B1656_the_electrons_zero/verification/the_electrons_zero.py").read_text(encoding="utf-8")
NS = {"__file__": str(ROOT / "frontier/B1656_the_electrons_zero/verification/x.py"), "__name__": "b1656_head"}
exec(compile(src.split("T0 = time.time()")[0], "b1656_head", "exec"), NS)
g = NS.get
OM, line_w, sector_twists, residues, weighted_M, coupling, SIXY, SECTORS, cA, UNITS = (g(k) for k in (
    "OM", "line_w", "sector_twists", "residues", "weighted_M", "coupling", "SIXY", "SECTORS", "cA", "UNITS"))
EPS = np.array([[0, 1], [-1, 0]], dtype=complex)
hz = json.load(open(ROOT / "frontier/B1637_fits_on_the_ruled_branch/received/HZ2021_running_masses_MZ.json"))["masses_GeV"]
v_, s_ = hz["value"], hz["sigma"]
def rr(a, b): r = v_[a]/v_[b]; return math.log(r), math.hypot(s_[a]/v_[a], s_[b]/v_[b])
TGT = {("up", 2): rr("c", "t"), ("up", 1): rr("u", "t"), ("down", 2): rr("s", "b"), ("down", 1): rr("d", "b"), ("lep", 2): rr("mu", "tau")}
LINES18 = [(b + i/3, b + j/3) for b in (1/9, 2/9) for i in range(3) for j in range(3)]
T0 = time.time()
import pickle
CACHE = pathlib.Path(__file__).with_name("sector_data.pkl")
DATA = pickle.load(open(CACHE, "rb")) if CACHE.exists() else {}
for ln in ([] if DATA else LINES18):
    w = line_w(*ln, OM); DATA[ln] = {}
    for sec, (fl, fr) in SECTORS.items():
        x, y = sector_twists(w, OM, SIXY[fl], SIXY[fr]); R = residues(x, y, OM); c = cA(x, y, OM, R, nth=64, ns=48)
        DATA[ln][sec] = (R, c)
pickle.dump(DATA, open(CACHE, "wb")); print(f"sector data on 18 lines: {time.time()-T0:.0f}s", flush=True)
def Ms(ln, sec, L):
    R, c = DATA[ln][sec]
    return weighted_M({s: (math.sqrt(2*np.pi*L + c[s])*R[s] if c[s] is not None else 0j) for s in UNITS})
# closed-form check on the actual matter
rng = np.random.default_rng(7); worst = 0
for ln in LINES18[:3]:
    for sec in SECTORS:
        M = Ms(ln, sec, 50.0); S = rng.normal(size=(2, 2)) + 1j*rng.normal(size=(2, 2)); Y = coupling(S, M)
        worst = max(worst, abs(np.linalg.det(Y) - 4*np.linalg.det(S)*np.linalg.det(M)*np.trace(EPS @ S @ M.T))/abs(np.linalg.det(Y)))
print(f"det Y = 4 det S det M tr(eps S M^T) on the sector matter: worst {worst:.1e}")
def spec(S, ln, L):
    out = {}
    for sec in SECTORS:
        U, sv, Vh = np.linalg.svd(coupling(S, Ms(ln, sec, L))); out[sec] = (sv, U, Vh.conj().T)
    return out
def unpack(p): return (p[0:4] + 1j*p[4:8]).reshape(2, 2), math.exp(p[8])
def loss(p, ln):
    S, L = unpack(p); sp_ = spec(S, ln, L); tot = 0.0
    for (sec, k), (mu, sg) in TGT.items():
        sv = sp_[sec][0]; val = sv[2]/sv[0] if k == 1 else sv[1]/sv[0]
        tot += ((math.log(max(val, 1e-300)) - mu)/max(sg, 0.05))**2      # a 5% floor: the frame is leading order
    return tot
res = []
for ln in LINES18:
    best = None
    for st in range(24):
        p0 = np.concatenate([rng.normal(size=8), [math.log(10**rng.uniform(0.5, 4))]])
        r = minimize(loss, p0, args=(ln,), method="Nelder-Mead", options={"maxiter": 6000, "xatol": 1e-9, "fatol": 1e-10})
        if best is None or r.fun < best.fun: best = r
    S, L = unpack(best.x); sp_ = spec(S, ln, L)
    V = sp_["up"][1].conj().T @ sp_["down"][1]; Vr = sp_["up"][2].conj().T @ sp_["down"][2]   # rows-as-left; columns-as-left
    rat = {sec: (sp_[sec][0][1]/sp_[sec][0][0], sp_[sec][0][2]/sp_[sec][0][0]) for sec in SECTORS}
    dS = np.linalg.det(S)/np.linalg.norm(S)**2
    res.append({"line": ln, "chi2": best.fun, "L": L, "dS_rel": abs(dS), "ratios": rat,
                "Vus": abs(V[2, 1]), "Vcb": abs(V[1, 0]), "Vub": abs(V[2, 0]), "Vus_r": abs(Vr[2, 1]), "Vcb_r": abs(Vr[1, 0]), "Vub_r": abs(Vr[2, 0])})
    print(f"{ln[0]:.3f},{ln[1]:.3f}  chi2 {best.fun:9.2f}  L {L:9.2f}  |dS| {abs(dS):.3g}  "
          + "  ".join(f"{s}:{rat[s][0]:.2e}/{rat[s][1]:.1e}" for s in SECTORS)
          + f"  CKM rows {abs(V[2,1]):.3f} {abs(V[1,0]):.3f} {abs(V[2,0]):.4f}  cols {abs(Vr[2,1]):.3f} {abs(Vr[1,0]):.3f} {abs(Vr[2,0]):.4f}", flush=True)
print("targets (exp):", {f"{k[0]}{k[1]}": f"{math.exp(v[0]):.2e}" for k, v in TGT.items()})
json.dump([{**r, "line": list(r["line"]), "ratios": {k: list(v) for k, v in r["ratios"].items()}} for r in res],
          open(pathlib.Path(__file__).with_suffix(".json"), "w"), indent=1, default=float)
print(f"done {time.time()-T0:.0f}s")
