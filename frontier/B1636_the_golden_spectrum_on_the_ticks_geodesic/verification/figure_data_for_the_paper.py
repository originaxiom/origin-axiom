"""B1636 -- the data behind the outside-reader write-up's figure (added 2026-10-09, after the arc landed its findings): the lowest
coupling's middle mass over its largest, computed directly from the off-diagonal theta matrix (post-seal M1), along the tick's
axis, three other closed geodesics and the imaginary axis, 25 points each. Writes golden_chart_data.json beside it."""
import mpmath as mp, numpy as np, math, json
mp.mp.dps = 20
def u_eta(t, N=40):
    e = lambda x: mp.exp(1j * mp.pi * t * x)
    th2 = mp.fsum(e((n + mp.mpf(1) / 2) ** 2) for n in range(-N, N)); th3 = mp.fsum(e(n * n) for n in range(-N, N + 1))
    th4 = mp.fsum((-1) ** abs(n) * e(n * n) for n in range(-N, N + 1))
    return [complex(th2 ** 2), complex(th3 ** 2), complex(th4 ** 2)]
def mid(t):
    u2, u3, u4 = u_eta(mp.mpc(t.real, t.imag))
    Y = np.array([[0, u4, u3], [u4, 0, u2], [u3, u2, 0]])
    s = np.linalg.svd(Y, compute_uv=False); return float(s[1] / s[0])
def axis(M, n=25):
    a, b, c, d = M; cen = (a - d) / (2 * c); rad = math.sqrt((a + d) ** 2 - 4) / (2 * abs(c))
    return [complex(cen + rad * math.cos(t), rad * math.sin(t)) for t in np.linspace(0.3, math.pi - 0.3, n)]
curves = {"tick LR (trace 3)": (2, 1, 1, 1), "L²R (trace 4)": (3, 2, 1, 1), "L²R² (trace 6)": (5, 2, 2, 1), "L³R (trace 5)": (4, 3, 1, 1)}
out = {k: [round(mid(t), 6) for t in axis(M)] for k, M in curves.items()}
out["imaginary axis"] = [round(mid(complex(0, y)), 6) for y in np.linspace(0.6, 1.8, 25)]
json.dump(out, open("golden_chart_data.json", "w"), indent=1)
for k, v in out.items(): print(k, min(v), max(v), v[:4])
