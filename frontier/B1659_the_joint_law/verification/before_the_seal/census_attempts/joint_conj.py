"""EXPLORATION (P-168/P-175; the owner's binary rule: 'both can be true if both are allowed'; data SEEN, a scoreboard).
In the SM the up quarks couple to the CONJUGATE Higgs H~ = eps H*, the down quarks and leptons to H. In B1656's frame the
up sector's twist is already the other sign (u-bar = -q_H w; down, leptons +q_H w). Variant: the up sector sees
S~ = eps conj(S) eps^T (= the cofactor of conj S: same |det|, same norm; S~ = S for a real quaternion), the others S.
Also VARIANT=bar: up sees conj(S). Global search as joint_census3 (differential evolution, 2 seeds), every 3rd line."""
import json, math, os, pathlib, sys
import numpy as np
from scipy.optimize import differential_evolution
src = pathlib.Path(__file__).with_name("joint_census2.py").read_text(encoding="utf-8")
sys.argv = ["x", "5", "1"]
NS = {"__file__": str(pathlib.Path(__file__).with_name("joint_census2.py")), "__name__": "jc2"}
exec(compile(src.split("out = []")[0], "jc2", "exec"), NS)
Yof, Ms, DATA, TGT = NS["Yof"], NS["Ms"], NS["DATA"], NS["TGT"]
VAR = os.environ.get("VARIANT", "tilde"); EP = np.array([[0, 1], [-1, 0]], dtype=complex)
def conjS(S): return EP @ S.conj() @ EP.T if VAR == "tilde" else S.conj()
def svs(S, ln, L):
    return {sec: np.linalg.svd(Yof(conjS(S) if sec == "up" else S, Ms(ln, sec, L)), compute_uv=False) for sec in ("up", "down", "lep")}
B = [(-4, 4)]*6 + [(math.log(3), math.log(3e3))]
def toS(x): return np.array([[1, x[0] + 1j*x[1]], [x[2] + 1j*x[3], x[4] + 1j*x[5]]]), math.exp(x[6])
KEYS = [(s, k) for s, k, _ in TGT]; MU = {(s, k): mu for s, k, (mu, sg) in TGT}; SG = {(s, k): sg for s, k, (mu, sg) in TGT}
def chi2(x, ln):
    S, L = toS(x); q = svs(S, ln, L)
    return float(sum(((math.log(max(q[s][k]/q[s][0], 1e-300)) - MU[(s, k)])/SG[(s, k)])**2 for s, k in KEYS))
out = []
for ln in sorted(DATA)[::3]:
    rs = [differential_evolution(chi2, B, args=(ln,), seed=sd, popsize=40, maxiter=600, tol=1e-10, polish=True) for sd in (1, 2)]
    b = min(rs, key=lambda r: r.fun); S, L = toS(b.x); q = svs(S, ln, L)
    out.append({"line": list(ln), "chi2_by_seed": [r.fun for r in rs], "x": b.x.tolist(), "L": L,
                "ratios": {s: [q[s][1]/q[s][0], q[s][2]/q[s][0]] for s in q}})
    print(f"[{VAR}] {ln[0]:.3f},{ln[1]:.3f} chi2 by seed {np.round([r.fun for r in rs], 3).tolist()} L {L:.2f} "
          + "  ".join(f"{s}:{q[s][1]/q[s][0]:.3e}/{q[s][2]/q[s][0]:.2e}" for s in q), flush=True)
json.dump(out, open(pathlib.Path(__file__).with_name(f"joint_conj_{VAR}.json"), "w"), indent=1, default=float)
