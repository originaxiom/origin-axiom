"""Reviewer, v2 review: the controls' margins on the instrument's own seeded draws (default_rng(16531), consumed in the
instrument's order: PAIRS, SS, then U4's five random lines and its S indices).  Reviewer's own series-based thetas."""
import sys
sys.path.insert(0, ".")
import numpy as np
from rv_core import *

rng = np.random.default_rng(16531)
def rnd_twist(): return (mp.mpf(rng.uniform(-0.5, 0.5)), mp.mpf(rng.uniform(-1, 1)))
def rnd_S():
    z = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
    return mp.matrix([[mp.mpc(z[0, 0]), mp.mpc(z[0, 1])], [mp.mpc(z[1, 0]), mp.mpc(z[1, 1])]])
OMEGA = mp.exp(2 * J * mp.pi / 3)
TAUS = [mp.mpc(0.13, 1.07), mp.mpc(-0.31, 0.88), OMEGA]
PTS = [mp.mpc(0.21, 0.17), mp.mpc(0.33, -0.12), mp.mpc(-0.4, 0.29)]
PAIRS = [(rnd_twist(), rnd_twist()) for _ in range(5)]
SS = [rnd_S() for _ in range(20)]
U4LINES = [wpt(rnd_twist(), TAUS[0]) for _ in range(5)]
print("PAIRS (a,b):", [([round(float(v), 4) for v in x], [round(float(v), 4) for v in y]) for x, y in PAIRS])
print("b_x - b_y:", [round(float(x[1] - y[1]), 4) for x, y in PAIRS])

BLOCKS = [QJ, QI, QK]
def bilf(x, y, z, t, frame="record"):
    ax, bx = x; ay, by = y; T = 2 * t
    g = lambda a, b, zz: thab(a, b, zz, T)
    X0, X1, Y0, Y1 = g(ax, bx, z), g(ax, bx, z + t), g(ay, by, z), g(ay, by, z + t)
    t1, t1t = thr(1, z, t), thr(1, z + t, t); D = J * ex(-t / 2) * ex(-z) * t1
    if frame == "record": p01, p10 = ex(by), ex(bx)
    else: p01 = p10 = ex((bx + by) / 2)
    return mp.matrix([[X0 * Y0 / t1, p01 * X0 * Y1 / D], [p10 * X1 * Y0 / D, ex(bx + by) * X1 * Y1 / t1t]])
def pair_from(M, C):
    K = QJ * C; return mp.fsum(K[m, n] * M[m, n] for m in range(2) for n in range(2))
def res_bil(x, y, t, rad=mp.mpf("0.02"), N=96):
    acc = mp.matrix(2, 2)
    for m in range(N):
        z = rad * mp.exp(2 * J * mp.pi * m / N); acc += bilf(x, y, z, t) * z
    return acc / N
def coupling(S, M):
    Y = mp.matrix(3, 3)
    for a, Ca in enumerate(BLOCKS):
        for b, Cb in enumerate(BLOCKS):
            K = Ca.T * QJ * S * Cb; Y[a, b] = mp.fsum(K[m, n] * M[m, n] for m in range(2) for n in range(2))
    return Y
def ratio(Y): s = sorted([abs(v) for v in mp.svd_c(Y, compute_uv=False)], reverse=True); return s[2] / s[0]
def mx(M): return max(abs(M[m, n]) for m in range(M.rows) for n in range(M.cols))
def det2(M): return M[0, 0] * M[1, 1] - M[0, 1] * M[1, 0]
def left_null(Y):
    U, S, V = mp.svd_c(Y); k = min(range(3), key=lambda i: abs(S[i]))
    v = [U[r, k] for r in range(3)]; n = mp.sqrt(sum(abs(z) ** 2 for z in v)); return [z / n for z in v]
def overlap(a, b): return abs(sum(mp.conj(a[k]) * b[k] for k in range(3)))
def twist_of(w, t): a = mp.im(w) / mp.im(t); return (a, 2 * (mp.re(w) - a * mp.re(t)))

# U0(b): the control frame's form spread, min over (tau, pair) of max over units 1, i
def spread(x, y, t, s, frame):
    A = x[0] + y[0]; ub = wpt(x, t) + wpt(y, t)
    vals = [pair_from(bilf(x, y, u, t, frame), UNIT[s]) * thr(1, u, t) * mp.exp(-2 * J * mp.pi * A * u) / thr(RTH[s], u + ub, t) for u in PTS]
    return max(abs(v / vals[0] - 1) for v in vals[1:])
u0b = min(max(spread(x, y, t, s, "control") for s in "1i") for t in TAUS for (x, y) in PAIRS)
print("\nU0(b) control min spread (needs > 1e-3):", mp.nstr(u0b, 4))

# U2(d): triplet non-isotropy, min over (tau, pair), closed form
u2d = min(rel_rr(closed_R(wpt(x, t) + wpt(y, t), wpt(x, t) - wpt(y, t), t)) for t in TAUS for (x, y) in PAIRS)
print("U2(d) min |R.R|/|R|^2 over 3 tau x 5 pairs (needs > 1e-3):", mp.nstr(u2d, 4))

# U3(c): the two-point control
u0p = mp.mpc(0.3, 0.2); u3c = []
for (x, y) in PAIRS[:3]:
    Rb = res_bil(x, y, TAUS[0]); Vb = bilf(x, y, u0p, TAUS[0]); Vb = Vb * (mx(Rb) / mx(Vb))
    for k in range(20):
        u3c.append(ratio(coupling(SS[k], Rb) + coupling(SS[(k + 7) % 20], Vb)))
print("U3(c) two-point min ratio over 60 (needs > 1e-6):", mp.nstr(min(u3c), 4), " median", mp.nstr(sorted(u3c)[30], 4))

# U4(c): different left field (6Y = 2 for the down-type's left field), five random lines, SS[0] and SS[1]
SIXY = {"Q": 1, "u": -4, "d": 2}
u4c = []
for wl in U4LINES:
    t = TAUS[0]
    Yu = coupling(SS[0], res_bil(twist_of(wl, t), twist_of(-4 * wl, t), t))
    Yx = coupling(SS[1], res_bil(twist_of(2 * wl, t), twist_of(2 * wl, t), t))
    u4c.append(1 - overlap(left_null(Yu), left_null(Yx)))
print("U4(c) 1 - overlap at the five random lines (needs > 1e-3):", [mp.nstr(v, 4) for v in u4c])

# U6: the spread control as built (24 nodes, 8 per circle, radial weight)
c0 = mp.mpc(0.3, 0.2)
def spread_M(x, y, t, nodes_per=8, radii=("0.03", "0.06", "0.1")):
    nodes = [c0 + mp.mpf(r) * mp.exp(2 * J * mp.pi * k / nodes_per) for r in radii for k in range(nodes_per)]
    M = mp.matrix(2, 2)
    for z in nodes: M += mp.exp(-abs(z - c0) ** 2 / mp.mpf("0.0025")) * bilf(x, y, z, t)
    return M
u6a = []; u6b = []
for (x, y) in PAIRS[:3]:
    M = spread_M(x, y, TAUS[0])
    u6a.append(abs(det2(M)) / mx(M) ** 2); u6b.append(min(ratio(coupling(S, M)) for S in SS))
    G0 = bilf(x, y, c0, TAUS[0]); W = mx(M) / mx(G0)
    print(f"  pair: |det M|/max^2 = {mp.nstr(u6a[-1],4)}, min ratio over 20 S = {mp.nstr(u6b[-1],4)}; "
          f"|M/(sum w) - G(c0)|/|G(c0)| = {mp.nstr(mx(M / (mp.fsum(mp.exp(-mp.mpf(r)**2/mp.mpf('0.0025')) for r in ('0.03','0.06','0.1')) * 8) - G0) / mx(G0), 4)}")
    M16 = spread_M(x, y, TAUS[0], nodes_per=16)
    print(f"        same radii, 16 nodes per circle: |det M|/max^2 = {mp.nstr(abs(det2(M16))/mx(M16)**2, 4)}")
print("U6 as built: min |det M|/max^2 (needs > 1e-6):", mp.nstr(min(u6a), 4), "; min ratio (needs > 1e-8):", mp.nstr(min(u6b), 4))
