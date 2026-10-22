"""B1708: W120 and W121 (the SM seat's, relays 200-201) checked on main's own code.  No data.
(1) the cone: -dt^2 + t^2 g with g of constant curvature kappa (Ric = 2 kappa g) is Ricci-flat iff kappa = -1 (sympy).
(2) the least volume among the orientable punctured-torus bundles over words in L, R to length 10, both monodromy signs.
(3) SL2(Z)'s abelianization Z/12 from its presentation (Smith form); chi(T) = 1, chi(L) = 11, chi(LR) = 0.
(4) Im(tau)^p |eta|^(2q) is SL2(Z)-invariant only for q = 2p; near a pinched fibre (z ~ e^{2 pi i tau}) Im(tau)|eta|^4
    ~ (-log|z|/2pi) |z|^(1/6).
(5) W121's lifts: rho_T built from its definition (B1634: the multiplier of eta^21 (theta2^2, theta3^2, theta4^2), weight
    23/2), the positive twists T_a = T and T_b = S T S^-1; (T_a T_b)^k scalar exactly at k = 3, 6, 9, 12; -I at k = 6
    (twelve twists), I at k = 12 (twenty-four)."""
import itertools, json, math, pathlib
import numpy as np, sympy as sp, mpmath as mp
HERE = pathlib.Path(__file__).resolve().parent
out = {}
# (1)
t, x, y, z, k = sp.symbols('t x y z kappa', real=True)
X = [t, x, y, z]; r2 = x**2 + y**2 + z**2; c = 4 / (1 + k * r2)**2
g = sp.diag(-1, t**2 * c, t**2 * c, t**2 * c); gi = g.inv()
Gam = [[[sp.simplify(sum(gi[a, d] * (sp.diff(g[d, b], X[cc]) + sp.diff(g[d, cc], X[b]) - sp.diff(g[b, cc], X[d])) for d in range(4)) / 2) for cc in range(4)] for b in range(4)] for a in range(4)]
def ric(b, cc):
    return sp.simplify(sum(sp.diff(Gam[a][b][cc], X[a]) - sp.diff(Gam[a][b][a], X[cc]) + sum(Gam[a][a][d] * Gam[d][b][cc] - Gam[a][cc][d] * Gam[d][b][a] for d in range(4)) for a in range(4)))
Ric = {(b, cc): ric(b, cc) for b in range(4) for cc in range(b, 4)}
out["1_cone"] = {"Ric_tt": str(Ric[(0, 0)]), "Ric_xx": str(sp.factor(Ric[(1, 1)])), "Ric_xy": str(Ric[(1, 2)]),
                 "all_vanish_at_kappa_-1": all(sp.simplify(v.subs(k, -1)) == 0 for v in Ric.values()),
                 "Ric_xx_proportional_to_kappa_plus_1": sp.simplify(Ric[(1, 1)] / (k + 1)).has(k + 1) is False}
# (2)
import snappy
def necklaces(n):
    seen, outw = set(), []
    for w in itertools.product("LR", repeat=n):
        s = "".join(w); rots = {s[i:] + s[:i] for i in range(n)}
        if s in seen or len(set(s)) < 2: seen |= rots; continue
        seen |= rots; outw.append(min(rots))
    return outw
vols = []
for n in range(2, 11):
    for w in necklaces(n):
        for sgn in "+-":
            M = snappy.Manifold("b+" + sgn + w)
            v = float(M.volume())
            if v > 0.5: vols.append((v, sgn + w))
vols.sort()
out["2_volumes"] = {"bundles": len(vols), "least": vols[:4], "the_least_is_pm_LR": all(abs(v - vols[0][0]) > 1e-6 or w[1:] in ("LR", "RL") for v, w in vols),
                    "least_value": vols[0][0]}
# (3)
Mrel = sp.Matrix([[4, 0], [1, 3]])          # S^4 = 1; S^2 (ST)^-3 = 1 -> -s - 3t, i.e. s + 3t = 0 (columns s, t)
from sympy.matrices.normalforms import smith_normal_form
out["3_abelianization"] = {"smith": [int(v) for v in smith_normal_form(Mrel, domain=sp.ZZ).diagonal()],
                           "chi(T)": 1, "chi(S)": (-3) % 12, "chi(L) = chi(S T^-1 S^-1)": (-1) % 12, "chi(R) = chi(T)": 1, "chi(LR)": 0}
# (4)
mp.mp.dps = 30
def eta(tau): q = mp.exp(2j * mp.pi * tau); return mp.exp(2j * mp.pi * tau / 24) * mp.qp(q)
def f(tau, p, q): return mp.im(tau) ** p * abs(eta(tau)) ** (2 * q)
rng = np.random.default_rng(120); inv = {}
for p_, q_ in ((1, 1), (1, 2), (1, 3), (2, 4), (2, 3)):
    dev = 0
    for _ in range(4):
        tau = mp.mpc(rng.uniform(-0.5, 0.5), rng.uniform(0.9, 1.6))
        dev = max(dev, abs(f(-1 / tau, p_, q_) / f(tau, p_, q_) - 1), abs(f(tau + 1, p_, q_) / f(tau, p_, q_) - 1))
    inv["p=%d q=%d" % (p_, q_)] = float(dev)
slopes = []
for zz in (1e-3, 1e-5, 1e-7):
    tau = mp.log(zz) / (2j * mp.pi)                 # z = e^{2 pi i tau}
    slopes.append(float(mp.log(f(tau, 1, 2) / (-mp.log(zz) / (2 * mp.pi))) / mp.log(zz)))
out["4_invariance_and_exponent"] = {"max_rel_dev": inv, "exponent_of_|z|_after_the_log": slopes}
# (5)
def th(n, tau):                                  # direct sums in tau: no nome branch (mpmath's q^(1/4) wraps under tau -> tau + 1)
    N = range(-40, 41)
    if n == 2: return mp.fsum(mp.exp(1j * mp.pi * tau * (m + mp.mpf(1) / 2) ** 2) for m in N)
    if n == 3: return mp.fsum(mp.exp(1j * mp.pi * tau * m * m) for m in N)
    return mp.fsum((-1) ** abs(m) * mp.exp(1j * mp.pi * tau * m * m) for m in N)
def F(tau):
    e = eta(tau) ** 21
    return mp.matrix([e * th(2, tau) ** 2, e * th(3, tau) ** 2, e * th(4, tau) ** 2])
taus = [mp.mpc(0.13, 1.21), mp.mpc(-0.27, 1.05), mp.mpc(0.31, 1.47), mp.mpc(0.05, 1.9)]
def solve_rho(img_fn):
    A = mp.matrix(3, len(taus)); B = mp.matrix(3, len(taus))
    for j, tau in enumerate(taus):
        Fv, Gv = F(tau), img_fn(tau)
        for i in range(3): A[i, j] = Fv[i]; B[i, j] = Gv[i]
    At = A[:, 0:3]; Bt = B[:, 0:3]
    R = Bt * mp.inverse(At)
    res = max(abs(x) for x in (R * A - B))                  # the fourth tau as a check
    return np.array([[complex(R[i, j]) for j in range(3)] for i in range(3)]), float(res)
rT, resT = solve_rho(lambda tau: F(tau + 1))
rS, resS = solve_rho(lambda tau: F(-1 / tau) / mp.sqrt(-1j * tau) ** 23)
Ta, Tb = rT, rS @ rT @ np.linalg.inv(rS)
P = Ta @ Tb; prods = {}
for kk in range(1, 13):
    Mk = np.linalg.matrix_power(P, kk); lam = Mk[0, 0]
    prods[kk] = {"scalar": bool(np.allclose(Mk, lam * np.eye(3), atol=1e-12)), "lambda": [round(lam.real, 10), round(lam.imag, 10)] if np.allclose(Mk, lam * np.eye(3), atol=1e-12) else None}
out["5_lifts"] = {"rho_T(T)_residual": resT, "rho_T(S)_residual": resS, "products": prods,
                  "scalar_exactly_at": [kk for kk, v in prods.items() if v["scalar"]]}
json.dump(out, open(HERE / "w120_w121_on_main.json", "w"), indent=1, default=str)
print(json.dumps(out, indent=1, default=str)[:4000])
