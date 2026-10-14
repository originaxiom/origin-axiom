"""Independent checks of chat1's field notes (auditor's code; does not import chat1's scripts).
Theta functions: direct series in tau (no nome root), z in the 'pi z' convention (period 1).
wp: the q-series of the Weierstrass function for the lattice Z + tau Z (independent of theta functions)."""
import itertools, json
import mpmath as mp
import numpy as np
import sympy as sp

mp.mp.dps = 40
I = mp.mpc(0, 1)
out = {}

def th(n, z, t, K=60):
    e = lambda x: mp.exp(I * mp.pi * x)
    ks = range(-K, K + 1)
    if n == 1: return -I * mp.fsum((-1) ** k * e(t * (k + mp.mpf(1) / 2) ** 2 + (2 * k + 1) * z) for k in ks)
    if n == 2: return mp.fsum(e(t * (k + mp.mpf(1) / 2) ** 2 + (2 * k + 1) * z) for k in ks)
    if n == 3: return mp.fsum(e(t * k * k + 2 * k * z) for k in ks)
    if n == 4: return mp.fsum((-1) ** k * e(t * k * k + 2 * k * z) for k in ks)

def wp(z, t, N=200):
    """Weierstrass p for the lattice Z + tau Z, by its q-series (u = e^{2 pi i z}, q = e^{2 pi i tau})."""
    u = mp.exp(2 * I * mp.pi * z); q = mp.exp(2 * I * mp.pi * t)
    s = mp.mpf(1) / 12 + u / (1 - u) ** 2
    for n in range(1, N):
        qn = q ** n
        s += qn * u / (1 - qn * u) ** 2 + qn / u / (1 - qn / u) ** 2 - 2 * qn / (1 - qn) ** 2
    return (2 * I * mp.pi) ** 2 * s

def R_of(t):
    d = mp.pi * th(2, 0, t) * th(3, 0, t) * th(4, 0, t)
    return [-th(2, 0, t) ** 2 / d, -th(4, 0, t) ** 2 / d, I * th(3, 0, t) ** 2 / d]

# --- 0. wp's Laurent check (no constant term) and theta1'(0) = pi th2 th3 th4
t0 = mp.mpc(0.13, 1.07)
z = mp.mpf("1e-6")
out["wp_laurent_const_term"] = float(abs(wp(z, t0) - 1 / z ** 2))
d1 = mp.diff(lambda w: th(1, w, t0), 0)
out["theta1p_vs_pi_th2th3th4_rel"] = float(abs(d1 - mp.pi * th(2, 0, t0) * th(3, 0, t0) * th(4, 0, t0)) / abs(d1))

# --- 1. C9/C10/O6: half-period values, f_s^2 = c^2 (wp - e_s), sum R_r^2 e_r with each pairing
UNIT_THETA = {"i": 2, "j": 4, "k": 3}
zero_of = {2: lambda t: mp.mpf(1) / 2, 4: lambda t: t / 2, 3: lambda t: (1 + t) / 2}
rows = []
for t in [mp.mpc(0.13, 1.07), mp.mpc(0, 1), mp.mpc(-0.31, 0.82), mp.mpc(0.2, 1.6), mp.mpc(0.45, 0.7), mp.mpc(-0.5, mp.sqrt(3) / 2)]:
    e = {s: wp(zero_of[s](t), t) for s in (2, 3, 4)}
    th2, th3, th4 = th(2, 0, t), th(3, 0, t), th(4, 0, t)
    # classical: e1 = wp(1/2) = (pi^2/3)(th3^4 + th4^4), e2 = wp(tau/2) = -(pi^2/3)(th2^4 + th3^4), e3 = wp((1+tau)/2) = (pi^2/3)(th2^4 - th4^4)
    cl = {2: mp.pi ** 2 / 3 * (th3 ** 4 + th4 ** 4), 4: -mp.pi ** 2 / 3 * (th2 ** 4 + th3 ** 4), 3: mp.pi ** 2 / 3 * (th2 ** 4 - th4 ** 4)}
    row = {"tau": [float(t.real), float(t.imag)],
           "e_vs_classical_rel": float(max(abs(e[s] - cl[s]) for s in (2, 3, 4)) / max(abs(cl[s]) for s in (2, 3, 4)))}
    zt = mp.mpc(0.231, 0.117)
    worst = 0
    for s in (2, 3, 4):
        c = th(s, 0, t) / d1 if t == t0 else th(s, 0, t) / mp.diff(lambda w: th(1, w, t), 0)
        f = th(s, zt, t) / th(1, zt, t)
        worst = max(worst, abs(f ** 2 - c ** 2 * (wp(zt, t) - e[s])) / abs(f ** 2))
    row["f_s^2_vs_c^2(wp-e_s)_rel"] = float(worst)
    R = dict(zip("ijk", R_of(t)))
    scale = sum(abs(R[u]) ** 2 * abs(e[UNIT_THETA[u]]) for u in "ijk")
    pairs = {}
    for perm in itertools.permutations((2, 4, 3)):
        pairs["".join(map(str, perm))] = float(abs(sum(R[u] ** 2 * e[p] for u, p in zip("ijk", perm))) / scale)
    row["sum_R2_e_by_pairing"] = pairs
    # uniqueness: a_r^2 proportional to (e3-e2, e1-e3, e2-e1) with e1,e2,e3 the units' (i,j,k) partners
    E = [e[2], e[4], e[3]]
    sol = [E[2] - E[1], E[0] - E[2], E[1] - E[0]]
    Rsq = [R[u] ** 2 for u in "ijk"]
    lam = sol[0] / Rsq[0]
    row["a_r^2_solution_vs_R_r^2_rel"] = float(max(abs(sol[k] - lam * Rsq[k]) for k in range(3)) / max(abs(x) for x in sol))
    rows.append(row)
out["C9_C10_O6"] = rows

# --- 2. Fierz: sum_r (psi^T eps u_r psi) u_r = -2 psi psi^T eps
QI = np.array([[1j, 0], [0, -1j]]); QJ = np.array([[0, 1], [-1, 0]], dtype=complex); QK = QI @ QJ; EPS = QJ
rng = np.random.default_rng(86)
fz = 0.0
for _ in range(100):
    psi = rng.normal(size=2) + 1j * rng.normal(size=2)
    lhs = sum((psi @ EPS @ u @ psi) * u for u in (QI, QJ, QK))
    rhs = -2 * np.outer(psi, psi) @ EPS
    fz = max(fz, np.abs(lhs - rhs).max() / np.abs(rhs).max())
out["fierz_max_rel"] = float(fz)

# --- 3. C5b: heavy mass = ||R x a||^2/|a.R| = |R||a|(1 + |Rhat^dag ahat|) in [|R||a|, 2|R||a|]; C8: C = (1+|Rhat^dag a0hat|)^-2
def Rnp(t):
    return np.array([complex(x) for x in R_of(mp.mpc(t.real, t.imag))])
def anull(xi): return np.array([1 - xi * xi, 1j * (1 + xi * xi), -2 * xi])
def Y(a, R): return np.outer(a, R) + np.outer(R, a) - np.dot(a, R) * np.eye(3)
mass_formula, ratio_lo, ratio_hi, c8 = 0.0, 9.0, 0.0, 0.0
for t in [0.13 + 1.07j, 1j, -0.31 + 0.82j, 0.5 + 0.866j]:
    R = Rnp(t)
    for _ in range(40):
        a = anull(complex(rng.normal(), rng.normal())) * complex(rng.normal(), rng.normal())
        s = np.linalg.svd(Y(a, R), compute_uv=False)
        ov = abs(np.vdot(R / np.linalg.norm(R), a / np.linalg.norm(a)))
        pred = np.linalg.norm(R) * np.linalg.norm(a) * (1 + ov)
        mass_formula = max(mass_formula, abs(s[0] - pred) / s[0])
        r = s[0] / (np.linalg.norm(R) * np.linalg.norm(a)); ratio_lo = min(ratio_lo, r); ratio_hi = max(ratio_hi, r)
        # C8 near the cone
        a0 = a / np.linalg.norm(a); d = rng.normal(size=3) + 1j * rng.normal(size=3); d /= np.linalg.norm(d)
        aa = a0 + 1e-5 * d
        s2 = np.linalg.svd(Y(aa, R), compute_uv=False)
        slope = (s2[1] / s2[0]) / (abs(np.dot(aa, aa)) / np.linalg.norm(aa) ** 2)
        c8 = max(c8, abs(slope - (1 + ov) ** -2) / (1 + ov) ** -2)
out["C5b_heavy_mass_formula_max_rel"] = float(mass_formula)
out["C5b_heavy_over_|R||a|_range"] = [float(ratio_lo), float(ratio_hi)]
out["C8_closed_form_max_rel_at_eps_1e-5"] = float(c8)

# --- 4. O7: [R(gamma tau)] = [R(tau)] for gamma in Gamma(4), not for gamma in Gamma(2) \ Gamma(4)
def proj_dist(u, v):
    u = np.array(u); v = np.array(v)
    return float(np.linalg.norm(np.cross(u, v)) / (np.linalg.norm(u) * np.linalg.norm(v)))
def mob(g, t): return (g[0][0] * t + g[0][1]) / (g[1][0] * t + g[1][1])
G4 = {"T^4": [[1, 4], [0, 1]], "lower4": [[1, 0], [4, 1]], "[[5,4],[-4,-3]]": [[5, 4], [-4, -3]], "[[-3,4],[-4,5]]": [[-3, 4], [-4, 5]]}
G2not4 = {"T^2": [[1, 2], [0, 1]], "lower2": [[1, 0], [2, 1]], "[[3,2],[4,3]]": [[3, 2], [4, 3]]}
o7 = {}
for t in [mp.mpc(0.11, 1.3), mp.mpc(-0.2, 0.9)]:
    R0 = [complex(x) for x in R_of(t)]
    for name, g in {**G4, **G2not4}.items():
        tg = mob(g, t)
        Rg = [complex(x) for x in R_of(tg)] if mp.im(tg) > 0.05 else None
        o7[f"{name}@{complex(t)}"] = {"Im(g tau)": float(mp.im(tg)), "proj_dist": proj_dist(R0, Rg) if Rg else None,
                                      "in_Gamma4": name in G4}
out["O7_gamma4"] = o7

# --- 5. fixed points of every move (trace maps of a->a, b->ab and a->ab, b->b): exactly (0,0,0) and (2,2,2)
x, y, zz = sp.symbols("x y z")
L = (x, zz, x * zz - y); Rm = (zz, y, y * zz - x)
G = sp.groebner([L[0] - x, L[1] - y, L[2] - zz, Rm[0] - x, Rm[1] - y, Rm[2] - zz], x, y, zz, order="lex")
out["fixed_point_groebner"] = [str(g) for g in G.exprs]
out["fixed_points"] = [str(s) for s in sp.solve(list(G.exprs), [x, y, zz], dict=True)]
# kappa preserved by both maps
kap = lambda X, Yv, Z: X ** 2 + Yv ** 2 + Z ** 2 - X * Yv * Z - 2
out["kappa_preserved_L_R"] = [sp.simplify(kap(*L) - kap(x, y, zz)) == 0, sp.simplify(kap(*Rm) - kap(x, y, zz)) == 0]

# --- 6. P-128's identity: th3(x)^2 th3(y)^2 + th1(x)^2 th1(y)^2 = th2(x)^2 th2(y)^2 + th4(x)^2 th4(y)^2
idw = 0
for t in [mp.mpc(0.13, 1.07), mp.mpc(-0.4, 0.8)]:
    for (xx, yy) in [(mp.mpc(0.1, 0.2), mp.mpc(-0.3, 0.05)), (mp.mpc(0.37, -0.1), mp.mpc(0.2, 0.3))]:
        lhs = th(3, xx, t) ** 2 * th(3, yy, t) ** 2 + th(1, xx, t) ** 2 * th(1, yy, t) ** 2
        rhs = th(2, xx, t) ** 2 * th(2, yy, t) ** 2 + th(4, xx, t) ** 2 * th(4, yy, t) ** 2
        idw = max(idw, abs(lhs - rhs) / abs(lhs))
out["P128_theta_identity_max_rel"] = float(idw)

print(json.dumps(out, indent=1, default=str))
