"""Data-free (labelled; committed before its run): does the Higgs's scalar part h0 lift Lemma A's obstruction?
B1736's general coupling Y = u h^T + h u^T - (u.h) 1 + w [h]_x + h0 (w 1 + [u]_x), S = h0 + h.(i, j, k), M = w + u.(i, j, k);
every census since B1700 set h0 = 0.  Checks:
  Q1  det Y = N(S) N(M) <S, M> with N(S) = h0^2 + h.h, N(M) = w^2 + u.u, <S, M> = h0 w + h.u  (symbolic);
  Q2  for a null quaternion Higgs (N(S) = 0) the left null vector of Y is conj x with x the null eigenvector of [h]_x of
      eigenvalue h0 (h x x = h0 x, x.x = 0), for every channel: Y^T x = 0 (random draws), and in general
      Y^T x = (lam - h0)(u x x - w x) for h x x = lam x, lam^2 = -h.h, lam != 0 (random draws);
  Q3  so under the Standard Model's reading (up sees (conj h0, conj h), down (h0, h)) the light states are x and conj x,
      orthogonal: |V_ud| = 0 at N(S) = 0 for every h0 - on 2 000 random channels and on the stored channels of THE READING
      TEST's grid (400 rows, a random null quaternion each); with h0 = 0 this is Lemma A's null case."""
import json, pathlib
import numpy as np
import sympy as sp

HERE = pathlib.Path(__file__).resolve().parents[1]
out = {}
u1, u2, u3, h1, h2, h3, w, h0 = sp.symbols("u1 u2 u3 h1 h2 h3 w h0")
u, h = sp.Matrix([u1, u2, u3]), sp.Matrix([h1, h2, h3])
crs = lambda v: sp.Matrix([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]])
Ys = u * h.T + h * u.T - (u.T * h)[0] * sp.eye(3) + w * crs(h) + h0 * (w * sp.eye(3) + crs(u))
q1 = sp.expand(Ys.det() - (h0 ** 2 + (h.T * h)[0]) * (w ** 2 + (u.T * u)[0]) * (h0 * w + (h.T * u)[0]))
out["Q1 det Y = N(S) N(M) <S, M> (symbolic)"] = bool(q1 == 0)


def cr(v):
    return np.array([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]])


def Y(u4, h, h0):
    ww, uu = u4[0], u4[1:]
    return np.outer(uu, h) + np.outer(h, uu) - (uu @ h) * np.eye(3) + ww * cr(h) + h0 * (ww * np.eye(3) + cr(uu))


def eig_x(h, lam):
    """The eigenvector of [h]_x with eigenvalue lam (lam^2 = -h.h, lam != 0)."""
    ev, V = np.linalg.eig(cr(h))
    return V[:, int(np.argmin(np.abs(ev - lam)))]


rng = np.random.default_rng(9)
w2, w3 = 0.0, 0.0
for _ in range(2000):
    hv = rng.normal(size=3) + 1j * rng.normal(size=3); lam = np.sqrt(-(hv @ hv)); x = eig_x(hv, lam)
    u4 = rng.normal(size=4) + 1j * rng.normal(size=4)
    w2 = max(w2, float(np.linalg.norm(Y(u4, hv, lam).T @ x) / np.linalg.norm(Y(u4, hv, lam))))     # h0 = lam: null S
    h0r = complex(*rng.normal(size=2))
    lhs = Y(u4, hv, h0r).T @ x; rhs = (lam - h0r) * (np.cross(u4[1:], x) - u4[0] * x)
    w3 = max(w3, float(np.linalg.norm(lhs - rhs) / max(np.linalg.norm(lhs), 1e-300)))
out["Q2 null S: largest |Y^T x| / |Y| (2 000 draws)"] = w2
out["Q2 general S: largest relative |Y^T x - (lam - h0)(u x x - w x)| (2 000 draws)"] = w3


def vud(uu4, ud4, hv, h0v):
    lu = np.linalg.svd(Y(uu4, np.conj(hv), np.conj(h0v)))[0][:, 2]; ld = np.linalg.svd(Y(ud4, hv, h0v))[0][:, 2]
    return abs(np.vdot(lu, ld))


vr = []
for _ in range(2000):
    hv = rng.normal(size=3) + 1j * rng.normal(size=3); h0v = np.sqrt(-(hv @ hv))
    vr.append(vud(rng.normal(size=4) + 1j * rng.normal(size=4), rng.normal(size=4) + 1j * rng.normal(size=4), hv, h0v))
out["Q3 random channels, null S with h0 != 0: largest |V_ud| (2 000 draws)"] = float(max(vr))
st = np.load(HERE / "reading_test_store.npz")["U"]
vs = []
for p in rng.choice(st.shape[0], 200, replace=False):
    for hr in range(2):
        hv = rng.normal(size=3) + 1j * rng.normal(size=3); h0v = np.sqrt(-(hv @ hv))
        s_u = np.linalg.svd(Y(st[p, 0, hr], np.conj(hv), np.conj(h0v)), compute_uv=False); s_d = np.linalg.svd(Y(st[p, 1, hr], hv, h0v), compute_uv=False)
        if s_u[1] > 1e-9 * s_u[0] and s_d[1] > 1e-9 * s_d[0]:
            vs.append(vud(st[p, 0, hr], st[p, 1, hr], hv, h0v))
out["Q3 the reading test's stored channels (400 rows), null S with h0 != 0: rows, largest |V_ud|"] = [len(vs), float(max(vs))]
print(json.dumps(out, indent=1))
