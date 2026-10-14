"""Main's independent recheck of chat1's O6 and C5b (written on main's bench, not chat1's code)."""
import itertools, json
import mpmath as mp, numpy as np
mp.mp.dps = 30
out = {}
def thetas(t):
    q = mp.exp(1j * mp.pi * t); return q, (lambda n, z: mp.jtheta(n, z, q))
def R_of(t):
    q, th = thetas(t); d = mp.pi * th(2, 0) * th(3, 0) * th(4, 0)
    return [-th(2, 0) ** 2 / d, -th(4, 0) ** 2 / d, 1j * th(3, 0) ** 2 / d]
def g(t, z):   # d^2/dz^2 log theta_1(pi z | tau): equals -wp(z) up to an additive constant
    q, th = thetas(t); return mp.diff(lambda w: mp.log(th(1, mp.pi * w)), z, 2)
# O6: sum_r R_r^2 wp(z_r) = 0 with units (i, j, k) at the zeros of (theta_2, theta_4, theta_3): z = 1/2, tau/2, (1+tau)/2
rows = []
for t in [mp.mpc(0.13, 1.07), mp.mpc(-0.31, 0.92), mp.mpc(0.4, 1.6), mp.mpc(0, 1)]:
    R = R_of(t); Z = [mp.mpf(1) / 2, t / 2, (1 + t) / 2]
    G = [g(t, z) for z in Z]
    scale = sum(abs(R[r] ** 2 * G[r]) for r in range(3))
    rec = abs(sum(R[r] ** 2 * G[r] for r in range(3))) / scale
    ctl = [float(abs(sum(R[r] ** 2 * G[p[r]] for r in range(3))) / scale) for p in itertools.permutations(range(3)) if p != (0, 1, 2)]
    rows.append({"tau": str(t), "record_pairing_rel": float(rec), "other_pairings_rel": ctl, "R.R_rel": float(abs(sum(x * x for x in R)) / sum(abs(x) ** 2 for x in R))})
out["O6_sum_R2_wp"] = rows
# C5b: isotropic a with a.R != 0: Y(a) = (R x a)(R x a)^T / (a.R)
rng = np.random.default_rng(7); worst = 0.0
for t in [complex(0.13, 1.07), complex(-0.31, 0.92)]:
    R = np.array([complex(x) for x in R_of(mp.mpc(t.real, t.imag))])
    for _ in range(20):
        u, v = rng.normal(size=3), rng.normal(size=3); e1 = u / np.linalg.norm(u); v -= v.dot(e1) * e1; e2 = v / np.linalg.norm(v)
        a = (e1 + 1j * e2) * complex(rng.normal(), rng.normal())          # isotropic
        Y = np.outer(a, R) + np.outer(R, a) - np.dot(a, R) * np.eye(3)
        c = np.cross(R, a); F = np.outer(c, c) / np.dot(a, R)
        worst = max(worst, float(np.abs(Y - F).max() / np.abs(Y).max()))
out["C5b_max_rel"] = worst
# parity: M = adjoint of the quaternion SU(2) is even under the puncture's -1 (Ad(-1) = id)
QI = np.array([[1j, 0], [0, -1j]]); m1 = -np.eye(2)
out["Ad_minus1_is_identity_on_M"] = bool(np.allclose(m1 @ QI @ np.linalg.inv(m1), QI))
print(json.dumps(out, indent=1, default=str)); json.dump(out, open("main_recheck.json", "w"), indent=1, default=str)
