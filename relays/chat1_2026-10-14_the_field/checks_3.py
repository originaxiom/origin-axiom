"""C5b: for null R and null a (a.R != 0), B1645's Y(a) = (R x a)(R x a)^T / (a.R) exactly, so the one non-zero mass is
||R x a||^2 / |a.R|; and B1646's D3 product law s1 s2 = |R|^2 |a.a| read near the cone. Not a sealed prediction."""
import json, pathlib, numpy as np
rng = np.random.default_rng(1014)
def R_np(t, K=60):
    n = np.arange(-K, K + 1); q = lambda x: np.exp(1j * np.pi * t * x)
    th2, th3, th4 = np.sum(q((n + 0.5) ** 2)), np.sum(q(n * n)), np.sum((-1.0) ** n * q(n * n))
    den = np.pi * th2 * th3 * th4
    return np.array([-th2 ** 2 / den, -th4 ** 2 / den, 1j * th3 ** 2 / den])
def Yf(a, R): return np.outer(a, R) + np.outer(R, a) - np.dot(a, R) * np.eye(3)
def anull(xi): return np.array([1 - xi * xi, 1j * (1 + xi * xi), -2 * xi])
worst_form, worst_mass, worst_prod = 0.0, 0.0, 0.0
for t in [0.13 + 1.07j, 1j, -0.31 + 0.82j, 0.5 + 0.866j]:
    R = R_np(t)
    for _ in range(50):
        a = anull(complex(rng.normal(), rng.normal())) * complex(rng.normal(), rng.normal())
        Y = Yf(a, R); w = np.cross(R, a); form = np.outer(w, w) / np.dot(a, R)
        worst_form = max(worst_form, np.abs(Y - form).max() / np.abs(Y).max())
        s = np.linalg.svd(Y, compute_uv=False)
        worst_mass = max(worst_mass, abs(s[0] - np.linalg.norm(w) ** 2 / abs(np.dot(a, R))) / s[0])
        b = a + 1e-3 * (rng.normal(size=3) + 1j * rng.normal(size=3)); s = np.linalg.svd(Yf(b, R), compute_uv=False)
        worst_prod = max(worst_prod, abs(s[0] * s[1] - np.linalg.norm(R) ** 2 * abs(np.dot(b, b))) / (s[0] * s[1]))
out = {"Y_equals_(Rxa)(Rxa)^T/(a.R)_max_rel": worst_form, "heavy_mass_formula_max_rel": worst_mass,
       "s1s2_equals_|R|^2|a.a|_near_cone_max_rel": worst_prod}
print(json.dumps(out, indent=1)); json.dump(out, open(pathlib.Path(__file__).parent / "checks_3.json", "w"), indent=1)
