"""Auditor's recomputation of the read-out m = m2/m3 for real unit directions (B1645's Y(a) = aR^T + Ra^T - (a.R)1),
with mpmath theta functions (not chat1's series), and a spot check of B1645's half bound for real a."""
import mpmath as mp, numpy as np, json
mp.mp.dps = 30
def R_of(t):
    q = mp.exp(1j * mp.pi * t); th = lambda n: mp.jtheta(n, 0, q)
    d = mp.pi * th(2) * th(3) * th(4)
    return np.array([complex(-th(2) ** 2 / d), complex(-th(4) ** 2 / d), complex(1j * th(3) ** 2 / d)])
def svals(a, R):
    Y = np.outer(a, R) + np.outer(R, a) - np.dot(a, R) * np.eye(3)
    return np.linalg.svd(Y, compute_uv=False)
out = {"units_(i,j,k)_at_tau=iy": {}, "chat1_FINDINGS_says": {"k": [0.5, 0.5, 0.5], "i or j": [0.610, 0.886, 0.995]}}
for name, a in (("i", [1, 0, 0]), ("j", [0, 1, 0]), ("k", [0, 0, 1])):
    row = {}
    for y in (1, 2, 4):
        s = svals(np.array(a, float), R_of(mp.mpc(0, y)))
        row[str(y)] = {"m2/m3": round(float(s[1] / s[0]), 6), "m1/m3": float(s[2] / s[0])}
    out["units_(i,j,k)_at_tau=iy"][name] = row
# half bound spot check: random real unit a over random tau in the fundamental domain
rng = np.random.default_rng(3); mins = []
for _ in range(12):
    x = rng.uniform(-0.5, 0.5); yy = rng.uniform(np.sqrt(1 - x * x), 3.0); R = R_of(mp.mpc(x, yy))
    ms = []
    for _ in range(400):
        a = rng.normal(size=3); a /= np.linalg.norm(a); s = svals(a, R); ms.append(s[1] / s[0])
    mins.append((round(float(min(ms)), 6), round(float(max(ms)), 6)))
out["random_real_a_(min_m,max_m)_per_tau"] = mins
# isotropic directions orthogonal to e_i (W64's v+-) give m = 0 (B1645), for contrast
for name, a in (("v+ = e_j - i e_k", np.array([0, 1, -1j])), ("v- = e_j + i e_k", np.array([0, 1, 1j]))):
    s = svals(a, R_of(mp.mpc(0.1, 1.3))); out["m_at_" + name] = float(s[1] / s[0])
print(json.dumps(out, indent=1)); json.dump(out, open("readout_m.json", "w"), indent=1)
