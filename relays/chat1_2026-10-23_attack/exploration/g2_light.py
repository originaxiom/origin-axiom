"""Data-free: the light left state's rotation for h = f3 + d f2 + e f1 (f3 = h0, f2 = e1, f1 = conj h0), reading S."""
import numpy as np, math
rng = np.random.default_rng(1)
f1 = np.array([0, 1, -1j]) / math.sqrt(2); f2 = np.array([1, 0, 0], dtype=complex); f3 = np.array([0, 1, 1j]) / math.sqrt(2)
F = np.stack([f1, f2, f3], axis=1)
def cross(v): return np.array([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]])
def Y_of(u, w, h): return np.outer(u, h) + np.outer(h, u) - (u @ h) * np.eye(3) + w * cross(h)
# the cross products in the f basis
print("f3 x f1 =", np.round(F.conj().T @ np.cross(f3, f1), 6), " f3 x f2 =", np.round(F.conj().T @ np.cross(f3, f2), 6), " f2 x f1 =", np.round(F.conj().T @ np.cross(f2, f1), 6))
worst = []
for trial in range(2000):
    u = rng.normal(size=3) + 1j * rng.normal(size=3); w = complex(rng.normal(), rng.normal())
    sc = 10 ** rng.uniform(-4, -2)
    d = sc * complex(rng.normal(), rng.normal()); e = sc * complex(rng.normal(), rng.normal()) * 0.3
    h = f3 + d * f2 + e * f1
    Y = Y_of(u, w, h)
    a1, a2, a3 = np.vdot(f1, u), np.vdot(f2, u), np.vdot(f3, u)
    Dl = a2 ** 2 + w ** 2 + 2 * a1 * a3
    beta = np.conj(d + 2 * e * a3 * (a2 - 1j * w) / Dl); gam = -np.conj(e * (a2 - 1j * w) ** 2 / Dl)
    Ul, s, Vh = np.linalg.svd(Y)
    x = Ul[:, 2]; x = x / (np.vdot(f1, x))            # normalise the f1 component to 1
    b_num, g_num = np.vdot(f2, x), np.vdot(f3, x)
    # first-order validity: compare relative to the size of the correction
    worst.append((abs(b_num - beta) / max(abs(beta), 1e-30), abs(g_num - gam) / max(abs(gam), 1e-30), sc, abs(Dl)))
    # det law
    if trial < 5:
        print("det law:", abs(np.linalg.det(Y) - (h @ h) * (u @ h) * (u @ u + w ** 2)) / abs(np.linalg.det(Y)))
W = np.array(worst)
for lo, hi in ((1e-4, 1e-3), (1e-3, 3e-3), (3e-3, 1e-2)):
    m = (W[:, 2] >= lo) & (W[:, 2] < hi) & (W[:, 3] > 0.3)
    print(f"departure scale {lo:.0e}-{hi:.0e}, |Delta| > 0.3: median rel. error beta {np.median(W[m,0]):.2e}, gamma {np.median(W[m,1]):.2e}  (n = {m.sum()})")
