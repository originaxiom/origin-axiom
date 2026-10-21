#!/usr/bin/env python3
"""B1684 -- the SM seat's W59 (D1, the one-loop potential on the shared fibre), checked on main by main's own code
(P-099, P-100). Written from W59's rule (its definitions) without reading the seat's script.

    python3 main_w59.py        # writes main_w59.json next to this file; exit 0 if every check holds

M1  the twisted determinant: -zeta'(0) of the twisted Laplacian by an Epstein-Poisson evaluation (incomplete gamma
    functions on both lattices), against |theta_1(w|tau)/eta(tau)|^2 exp(-2 pi (Im w)^2 / y); the three parity sectors'
    product is 4.
M2  the matter determinant's checkable steps: Riemann-Hurwitz (genus 3), the holomorphic differentials x^a dx / w^b on
    w^4 = cubic by valuations, zeta_Sigma(0) = -3/2 = -1 - p, and the S and T invariance of y^(1/2)|eta|^2 and
    (y|eta|^4)^(-1/4).
M3  tau: the critical points of log(y|eta|^4) and of E(tau, 3) over a neighbourhood of the fundamental domain to
    y = 6 (Newton from a grid, classified by the Hessian); E(tau, 3) by Chowla-Selberg against the lattice sum; the
    joint parity sum = -(15/16) E(tau, 3).
M4  the line: the stationary points on the torus of a joint-parity boson of charge 1 at tau_0, tau_1 and omega, with
    values and types; a fermion's minimum.
M5  who sees which line (charges in units of 6Y).
M6  the Higgs alone at omega (charge 3): its global minima on the torus of lines, and the twists each field sees there.
M7  W62's structural point, for the Higgs's term only: on a half-period line its tau-dependence is invariant under the
    stabiliser of that line (index 3), not under SL(2, Z), and its gradient at omega is not zero.
"""
import json, math, os, sys
import numpy as np
from scipy.special import exp1, kv, zeta as hzeta

HERE = os.path.dirname(os.path.abspath(__file__))
OMEGA = complex(-0.5, math.sqrt(3) / 2)
PAR = [(0.5, 0.0), (0.0, 0.5), (0.5, 0.5)]


# ---------- theta functions and eta (series) ----------
def eta(tau, K=80):
    q = np.exp(2j * np.pi * tau)
    return np.exp(2j * np.pi * tau / 24) * np.prod([1 - q ** n for n in range(1, K)])


def theta1(w, tau, K=40):
    n = np.arange(-K, K)
    h = n + 0.5
    return -1j * np.sum(np.where(n % 2 == 0, 1.0, -1.0) * np.exp(1j * np.pi * h * h * tau + 2j * np.pi * h * w))


# ---------- M1: the twisted determinant by an Epstein-Poisson evaluation ----------
def logdet_epstein(phi, tau, N=14):
    """-zeta'(0) for eigenvalues |p|^2, p in c + L*, where c.1 = phi1, c.tau = phi2 (L = Z + tau Z in R^2)."""
    L = np.array([[1.0, 0.0], [tau.real, tau.imag]])          # rows: the basis vectors 1 and tau
    Ls = np.linalg.inv(L).T                                    # rows: the dual basis
    c = np.linalg.solve(L, np.array(phi, float))               # c.e1 = phi1, c.e2 = phi2
    V = abs(np.linalg.det(L))
    k = np.arange(-N, N + 1); A, B = np.meshgrid(k, k, indexing="ij"); A = A.ravel(); B = B.ravel()
    P = c[None, :] + A[:, None] * Ls[0][None, :] + B[:, None] * Ls[1][None, :]
    x = np.pi * np.sum(P * P, axis=1)
    lam0 = np.sum(exp1(x))                                     # sum_p Gamma(0, pi|p|^2)
    nz = (A != 0) | (B != 0)
    Lv = A[nz, None] * L[0][None, :] + B[nz, None] * L[1][None, :]
    u = np.pi * np.sum(Lv * Lv, axis=1)
    ph = np.cos(2 * np.pi * (A[nz] * phi[0] + B[nz] * phi[1]))
    lam0 += V * (-1.0 + np.sum(ph * np.exp(-u) / u))           # covol(L) [ -1 + sum_{l != 0} e^{2 pi i l.c} Gamma(1, pi|l|^2)/(pi|l|^2) ] (Poisson to L)
    return -lam0                                               # log det = -Z'(0) = -Lambda(0); zeta(0) = 0 (no zero mode)


def logdet_theta(w, tau):
    return 2 * math.log(abs(theta1(w, tau) / eta(tau))) - 2 * math.pi * (w.imag ** 2) / tau.imag


def m1():
    rng = np.random.default_rng(59)
    taus = [complex(rng.uniform(-0.5, 0.5), rng.uniform(0.9, 1.8)) for _ in range(8)]
    out = {"samples": [], "maps_tried": {}}
    # which w corresponds to holonomies (phi1 along 1, phi2 along tau): try the four sign choices, keep the one that fits
    maps = {"phi2-phi1*tau": lambda p, t: p[1] - p[0] * t, "phi1-phi2*tau": lambda p, t: p[0] - p[1] * t,
            "phi2+phi1*tau": lambda p, t: p[1] + p[0] * t, "phi1+phi2*tau": lambda p, t: p[0] + p[1] * t}
    phis = [tuple(rng.uniform(0.05, 0.95, 2)) for _ in range(8)]
    for name, f in maps.items():
        out["maps_tried"][name] = max(abs(logdet_epstein(p, t) - logdet_theta(f(p, t), t)) for p, t in zip(phis, taus))
    best = min(out["maps_tried"], key=out["maps_tried"].get)
    for p, t in zip(phis, taus):
        out["samples"].append({"tau": [t.real, t.imag], "phi": list(p), "epstein": logdet_epstein(p, t),
                               "theta": logdet_theta(maps[best](p, t), t)})
    out["map"] = best; out["max_diff"] = out["maps_tried"][best]
    prods = []
    for t in taus[:5]:
        prods.append(math.exp(sum(logdet_epstein(p, t) for p in PAR)))
    out["parity_product"] = prods
    out["holds"] = bool(out["max_diff"] < 1e-9 and all(abs(x - 4) < 1e-9 for x in prods))
    return out


# ---------- M2: the matter determinant's checkable steps ----------
def m2():
    g_rh = (8 * (2 * 1 - 2) + 4 * (2 - 1)) // 2 + 1          # 2g - 2 = deg (2g_E - 2) + sum (e - 1)
    n, d = 4, 3                                               # w^4 = cubic, gcd(4, 3) = 1
    diffs = [(a, b) for b in range(1, n) for a in range(0, 6)
             if b <= n - 1 and d * b >= n * (a + 1) + 1]          # holomorphic at the roots (b <= n-1) and at infinity
    g_super = (n - 1) * (d - 1) // 2
    from fractions import Fraction as F
    cones = 4 * F(1, 12) * (F(1, 2) - 2)
    zeta0 = cones - 1
    p = F(1, 12) * 4 * F(1 * 3, 2)
    inv = []
    for t in (complex(0.1, 1.2), complex(-0.3, 0.9), complex(0.45, 2.1), complex(0.0, 1.0)):
        f = lambda z: math.sqrt(z.imag) * abs(eta(z)) ** 2
        inv.append(max(abs(f(t) - f(-1 / t)), abs(f(t) - f(t + 1))) / f(t))
    return {"genus_riemann_hurwitz": g_rh, "genus_superelliptic": g_super,
            "holomorphic_differentials": [f"x^{a} dx / w^{b}" for a, b in diffs],
            "zeta_Sigma_0": str(zeta0), "p": str(p), "minus_one_minus_p": str(-1 - p),
            "S_T_invariance_rel": inv,
            "holds": bool(g_rh == 3 and g_super == 3 and diffs == [(0, 2), (0, 3), (1, 3)]
                          and zeta0 == F(-3, 2) == -1 - p and max(inv) < 1e-12)}


# ---------- lattice sums for the six-dimensional term ----------
def _lattice(N):
    k = np.arange(-N, N + 1); M, Nn = np.meshgrid(k, k, indexing="ij"); M = M.ravel(); Nn = Nn.ravel()
    keep = (M != 0) | (Nn != 0)
    return M[keep], Nn[keep]


class Sixd:
    """V(phi; tau) = -sum' coef(m, n) cos 2 pi (m phi1 + n phi2) y^3 / |m + n tau|^6, with derivatives in phi."""
    def __init__(self, tau, N=48, coef=None):
        self.m, self.n = _lattice(N); y = tau.imag
        w = y ** 3 / np.abs(self.m + self.n * tau) ** 6
        self.w = w * (coef(self.m, self.n) if coef else 1.0)

    def val(self, P):                                     # P: (k, 2)
        a = 2 * np.pi * (np.outer(P[:, 0], self.m) + np.outer(P[:, 1], self.n))
        return -(np.cos(a) @ self.w)

    def grad(self, P):
        a = 2 * np.pi * (np.outer(P[:, 0], self.m) + np.outer(P[:, 1], self.n)); s = np.sin(a) * self.w
        return np.stack([2 * np.pi * (s @ self.m), 2 * np.pi * (s @ self.n)], axis=1)

    def hess(self, P):
        a = 2 * np.pi * (np.outer(P[:, 0], self.m) + np.outer(P[:, 1], self.n)); c = np.cos(a) * self.w
        f = 4 * np.pi ** 2
        return np.stack([np.stack([f * (c @ (self.m * self.m)), f * (c @ (self.m * self.n))], 1),
                         np.stack([f * (c @ (self.m * self.n)), f * (c @ (self.n * self.n))], 1)], 1)


def joint_coef(m, n):                                      # sum over the three parities of (-1)^{2(m p1 + n p2)}
    return np.where((m % 2 == 0) & (n % 2 == 0), 3.0, -1.0)


def stationary_points(S, grid=40, sign=1.0):
    g = (np.arange(grid) + 0.5) / grid
    seeds = [(0, 0), (0.5, 0), (0, 0.5), (0.5, 0.5), (1 / 3, 1 / 3), (2 / 3, 2 / 3)]   # stationary by symmetry (V even; omega's rotation)
    P = np.array([(a, b) for a in g for b in g] + [(a + 1e-9, b + 1e-9) for a, b in seeds])
    for _ in range(60):
        G = sign * S.grad(P); H = sign * S.hess(P)
        step = np.linalg.solve(H + 1e-14 * np.eye(2)[None], G[..., None])[..., 0]
        nrm = np.linalg.norm(step, axis=1, keepdims=True); step = step * np.minimum(1.0, 0.05 / np.maximum(nrm, 1e-300))
        P = np.mod(P - step, 1.0)
    G = np.linalg.norm(S.grad(P), axis=1); P = P[G < 1e-7]
    pts = []
    for p in P:
        q = np.round(p, 6) % 1.0
        if not any(min(abs(q[0] - r[0]), 1 - abs(q[0] - r[0])) < 1e-5 and min(abs(q[1] - r[1]), 1 - abs(q[1] - r[1])) < 1e-5 for r in pts):
            pts.append(q)
    res = []
    for q in pts:
        q2 = np.array([q]); ev = np.linalg.eigvalsh(sign * S.hess(q2)[0])
        typ = "min" if ev.min() > 1e-9 else ("max" if ev.max() < -1e-9 else ("saddle" if ev.min() < -1e-9 < 1e-9 < ev.max() else "degenerate"))
        res.append({"phi": [float(round(q[0], 6)) % 1.0, float(round(q[1], 6)) % 1.0], "value": float(sign * S.val(q2)[0]),
                    "type": typ, "hess_eigs": [float(e) for e in ev]})
    return sorted(res, key=lambda r: r["value"])


# ---------- M3: tau ----------
def E3_cs(tau, K=40):
    s = 3; x, y = tau.real, tau.imag
    t1 = 2 * hzeta(2 * s) * y ** s
    t2 = 2 * math.sqrt(math.pi) * y ** (1 - s) * math.gamma(s - 0.5) * hzeta(2 * s - 1) / math.gamma(s)
    t3 = 0.0
    for n in range(1, K):
        sig = sum(dd ** (1 - 2 * s) for dd in range(1, n + 1) if n % dd == 0)
        t3 += n ** (s - 0.5) * sig * kv(s - 0.5, 2 * math.pi * n * y) * math.cos(2 * math.pi * n * x)
    return t1 + t2 + 8 * math.pi ** s * math.sqrt(y) / math.gamma(s) * t3


def E3_direct(tau, N=300):
    m, n = _lattice(N)
    return float(np.sum(tau.imag ** 3 / np.abs(m + n * tau) ** 6))


def logyeta4(tau):
    return math.log(tau.imag * abs(eta(tau)) ** 4)


def to_F(t):
    for _ in range(60):
        t = complex(t.real - round(t.real), t.imag)
        if abs(t) < 1 - 1e-12:
            t = -1 / t
        else:
            break
    if abs(t.real + 0.5) < 1e-9:
        t = complex(0.5, t.imag)
    return t


def critical_points(f, h=1e-5):
    def grad(t):
        return np.array([(f(t + h) - f(t - h)) / (2 * h), (f(t + 1j * h) - f(t - 1j * h)) / (2 * h)])

    def hess(t):
        fxx = (f(t + h) - 2 * f(t) + f(t - h)) / h ** 2; fyy = (f(t + 1j * h) - 2 * f(t) + f(t - 1j * h)) / h ** 2
        fxy = (f(t + h + 1j * h) - f(t + h - 1j * h) - f(t - h + 1j * h) + f(t - h - 1j * h)) / (4 * h * h)
        return np.array([[fxx, fxy], [fxy, fyy]])
    found = []
    for x0 in np.linspace(-0.55, 0.55, 12):
        for y0 in np.linspace(0.80, 6.0, 14):
            t = complex(x0, y0)
            for _ in range(80):
                g = grad(t); H = hess(t)
                try:
                    d = np.linalg.solve(H, g)
                except np.linalg.LinAlgError:
                    break
                if np.linalg.norm(d) > 0.1:
                    d = d * 0.1 / np.linalg.norm(d)
                t = complex(t.real - d[0], max(t.imag - d[1], 0.3))
                if np.linalg.norm(d) < 1e-12:
                    break
            if np.linalg.norm(grad(t)) < 1e-6 and t.imag <= 6.5:
                tF = to_F(t)
                if not any(abs(tF - u) < 1e-5 for u, _ in found):
                    ev = np.linalg.eigvalsh(hess(tF))
                    typ = "min" if ev.min() > 0 else ("max" if ev.max() < 0 else "saddle")
                    found.append((tF, typ))
    return [{"tau": [round(t.real, 7), round(t.imag, 7)], "type": typ} for t, typ in found]


def m3():
    samples = [complex(0.1, 1.1), complex(-0.3, 1.7), OMEGA, complex(0, 1), complex(0.25, 2.5)]
    cs_vs_direct = max(abs(E3_cs(t) - E3_direct(t)) / E3_direct(t) for t in samples)
    joint = []
    for t in samples:
        S = Sixd(t, N=120, coef=joint_coef); joint.append(float(-S.val(np.zeros((1, 2)))[0] / E3_direct(t, N=120) + 15 / 16))
    crit_eta = critical_points(logyeta4); crit_E = critical_points(E3_cs)
    grows = [E3_cs(complex(0, y)) for y in (4, 6, 8)]
    near = lambda L, z, typ: any(abs(complex(*c["tau"]) - z) < 1e-4 and c["type"] == typ for c in L)
    om = complex(0.5, math.sqrt(3) / 2)
    holds = (cs_vs_direct < 1e-9 and max(abs(j) for j in joint) < 1e-8                 # the even sublattice's truncation at N = 120
             and len(crit_eta) == 2 and near(crit_eta, 1j, "saddle") and near(crit_eta, om, "max")
             and len(crit_E) == 2 and near(crit_E, 1j, "saddle") and near(crit_E, om, "min") and grows[0] < grows[1] < grows[2])
    return {"E3_chowla_selberg_vs_direct_rel": cs_vs_direct, "joint_parity_minus_(-15/16)": joint,
            "critical_points_log_y_eta4": crit_eta, "critical_points_E3": crit_E, "E3_at_y_4_6_8": grows,
            "holds": bool(holds)}


# ---------- M4, M6: the line ----------
def m4():
    out = {}
    for name, t in (("tau_0", complex(0.17, 1.13)), ("tau_1", complex(0.05, 1.40)), ("omega", OMEGA)):
        S = Sixd(t, N=48, coef=joint_coef)
        out[name] = {"boson": stationary_points(S, sign=1.0), "fermion_min": stationary_points(S, sign=-1.0)[0]}
    o = out["omega"]["boson"]
    third = [r for r in o if r["type"] == "min" and any(abs(r["phi"][0] - a) < 1e-4 and abs(r["phi"][1] - a) < 1e-4 for a in (1 / 3, 2 / 3))]
    two = [r for r in o if any(abs(r["phi"][0] - a) < 1e-4 and abs(r["phi"][1] - b) < 1e-4 for a, b in PAR)]
    out["omega_summary"] = {"n_stationary": len(o), "global_min": o[0], "three_torsion_minima": third,
                            "two_torsion_points": two, "max": o[-1]}
    fz = [min(abs(out[k]["fermion_min"]["phi"][i]), 1 - abs(out[k]["fermion_min"]["phi"][i])) for k in ("tau_0", "tau_1", "omega") for i in (0, 1)]
    out["fermion_min_at_zero"] = bool(max(fz) < 1e-4)
    t0 = out["tau_0"]["boson"]
    out["tau_0_summary"] = {"n_stationary": len(t0), "global_min": t0[0]}
    out["tau_1_summary"] = {"n_stationary": len(out["tau_1"]["boson"]), "global_min": out["tau_1"]["boson"][0],
                            "local_minima": [r for r in out["tau_1"]["boson"] if r["type"] == "min"]}
    return out


CHARGES = {"Q": 1, "u^c": -4, "d^c": 2, "L": -3, "e^c": 6, "H": 3}


def twisted(q, w):
    return any(abs((q * x) - round(q * x)) > 1e-12 for x in w)


def m5():
    from fractions import Fraction as F
    three = [(F(a, 3), F(b, 3)) for a in range(3) for b in range(3) if (a, b) != (0, 0)]
    two = [(F(a, 2), F(b, 2)) for a in range(2) for b in range(2) if (a, b) != (0, 0)]
    sees3 = {str(w): sorted(k for k, q in CHARGES.items() if any((q * x).denominator != 1 for x in w)) for w in three}
    sees2 = {str(w): sorted(k for k, q in CHARGES.items() if any((q * x).denominator != 1 for x in w)) for w in two}
    ok3 = all(v == sorted(["Q", "u^c", "d^c"]) for v in sees3.values())
    ok2 = all(v == sorted(["Q", "L", "H"]) for v in sees2.values())
    return {"three_torsion": sees3, "two_torsion": sees2, "holds": bool(ok3 and ok2)}


def m6():
    S = Sixd(OMEGA, N=48, coef=joint_coef)
    g = 3                                                   # V_H(w) = V_joint(3 w): its minima are w with 3w at the global minima
    k = np.arange(0, 9) / 9.0
    W = np.array([(a, b) for a in k for b in k])
    vals = S.val(np.mod(g * W, 1.0))
    vmin = vals.min()
    lines = [tuple(np.round(W[i] * 9).astype(int)) for i in range(len(W)) if abs(vals[i] - vmin) < 1e-9]
    # a fine-grid check that no w off the ninths is lower
    fine = (np.arange(180) + 0.5) / 180; F2 = np.array([(a, b) for a in fine for b in fine])
    lower = float(S.val(np.mod(g * F2, 1.0)).min() - vmin)
    from fractions import Fraction as Fr
    w0 = (Fr(1, 9), Fr(1, 9))
    tw = {k_: str((q * w0[0]) % 1) for k_, q in CHARGES.items()}
    de_differ = all(((CHARGES["d^c"] * Fr(a, 9)) % 1, (CHARGES["d^c"] * Fr(b, 9)) % 1) != ((CHARGES["e^c"] * Fr(a, 9)) % 1, (CHARGES["e^c"] * Fr(b, 9)) % 1) for a, b in lines)
    three_w_fixed = all((((3 * a) % 9) * 1, ((3 * b) % 9)) in [(3, 3), (6, 6)] for a, b in lines)
    return {"n_lines": len(lines), "lines_in_ninths": [list(map(int, l)) for l in lines], "V_min": float(vmin),
            "fine_grid_min_minus_V_min": lower, "twists_at_(1/9,1/9)": tw, "d_e_differ_on_every_line": bool(de_differ),
            "three_w_at_the_order_3_fixed_points": bool(three_w_fixed),
            "holds": bool(len(lines) == 18 and lower > -1e-9 and de_differ and three_w_fixed)}


# ---------- M7: W62's structural point, the Higgs's term on a half-period line ----------
def higgs_on_line(tau, w0, N=60):
    """sum over the three parity copies of a charge-3 boson's six-dimensional term at the line w0 (3 w0 = w0 mod 1)."""
    m, n = _lattice(N); y = tau.imag; wt = y ** 3 / np.abs(m + n * tau) ** 6
    tot = 0.0
    for p in PAR:
        ph = ((p[0] + 3 * w0[0]) % 1.0, (p[1] + 3 * w0[1]) % 1.0)
        tot += -np.sum(np.cos(2 * np.pi * (m * ph[0] + n * ph[1])) * wt)
    return float(tot)


def m7():
    out = {}
    h = 1e-5
    for w0 in PAR:
        f = lambda t: higgs_on_line(t, w0)
        g = ((f(OMEGA + h) - f(OMEGA - h)) / (2 * h), (f(OMEGA + 1j * h) - f(OMEGA - 1j * h)) / (2 * h))
        t = complex(0.13, 1.21)
        S = lambda z: -1 / z; T = lambda z: z + 1; T2 = lambda z: z + 2
        # the line's stabiliser: (1/2, 1/2) is fixed by S and T^2 (theta group); (0, 1/2) by T; (1/2, 0) by S T^2 S
        diffs = {"S": abs(f(S(t)) - f(t)), "T": abs(f(T(t)) - f(t)), "T2": abs(f(T2(t)) - f(t))}
        out[str(w0)] = {"grad_at_omega": [float(g[0]), float(g[1])], "|grad|": float(math.hypot(*g)), "invariance": diffs}
    # the joint parity sum (every line copy alike) is SL(2, Z)-invariant: its gradient at omega vanishes
    f0 = lambda t: -E3_direct(t, N=60) * (-15 / 16)
    g0 = math.hypot((f0(OMEGA + h) - f0(OMEGA - h)) / (2 * h), (f0(OMEGA + 1j * h) - f0(OMEGA - 1j * h)) / (2 * h))
    out["joint_parity_grad_at_omega"] = g0
    out["holds"] = bool(all(out[str(w)]["|grad|"] > 1e-3 for w in PAR) and g0 < 1e-6
                        and out[str((0.5, 0.5))]["invariance"]["S"] < 1e-5 and out[str((0.5, 0.5))]["invariance"]["T2"] < 1e-5   # the box's truncation at N = 60
                        and out[str((0.5, 0.5))]["invariance"]["T"] > 1e-3)
    return out


def main():
    res = {"M1": m1(), "M2": m2(), "M3": m3(), "M4": m4(), "M5": m5(), "M6": m6(), "M7": m7()}
    om = res["M4"]["omega_summary"]
    res["M4"]["holds"] = bool(len(om["three_torsion_minima"]) == 2 and om["global_min"] in om["three_torsion_minima"]
                              and res["M4"]["fermion_min_at_zero"])
    res["hold"] = {k: res[k]["holds"] for k in ("M1", "M2", "M3", "M4", "M5", "M6", "M7")}
    with open(os.path.join(HERE, "main_w59.json"), "w", encoding="utf-8") as fh:
        json.dump(res, fh, indent=1, default=float)
    print(json.dumps(res["hold"]))
    print("M1", res["M1"]["map"], res["M1"]["max_diff"], res["M1"]["parity_product"])
    print("M3 eta", res["M3"]["critical_points_log_y_eta4"], "E3", res["M3"]["critical_points_E3"])
    print("M4 omega", om["n_stationary"], om["global_min"]["value"], [(r["phi"], round(r["value"], 4), r["type"]) for r in om["two_torsion_points"]])
    print("M4 tau_0", res["M4"]["tau_0_summary"]["n_stationary"], res["M4"]["tau_0_summary"]["global_min"]["phi"],
          "tau_1", res["M4"]["tau_1_summary"]["n_stationary"], [(r["phi"], round(r["value"], 4)) for r in res["M4"]["tau_1_summary"]["local_minima"]])
    print("M6", res["M6"]["n_lines"], res["M6"]["twists_at_(1/9,1/9)"])
    print("M7", {k: round(v["|grad|"], 4) for k, v in res["M7"].items() if isinstance(v, dict)}, res["M7"]["joint_parity_grad_at_omega"])
    return 0 if all(res["hold"].values()) else 1


if __name__ == "__main__":
    sys.exit(main())
