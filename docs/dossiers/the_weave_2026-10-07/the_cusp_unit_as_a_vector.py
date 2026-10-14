"""W64: the cusp's unit as a vector in M (main's P-113), in both frames. The rule (W64_RULE.md) was committed before
this script.

  K1  the moves on M: the cube group O, L's eigenlines, the isotropic ones, the special isotropic lines and their orbits
  K2  R's modular law: R(tau + 1) and R(-1/tau) against signed permutations
  K3  R's end data per eigenline of L: the leading exponents along tau = iy
  K4  the Higgs's sections at weight -1/2 with end data per eigenline (surface frame)
  K5  the fermions' sections at weight 3/2 with end data per eigenline (surface frame)
  K6  the potential's isotropic/real dichotomy (fibre frame)
  K7  the weave's anisotropy on the cone (fibre frame)
  plus the read-outs: m at the special lines, every placement's dimension and cusp direction, S~ on M

Run: python3 the_cusp_unit_as_a_vector.py  ->  the_cusp_unit_as_a_vector.json beside it.
"""
import itertools
import json
import math
import sys
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sy
from scipy.optimize import minimize

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_common_point as CP  # noqa: E402  (the record's moves: AUT)
import the_index_on_the_weaves_surface as IW  # noqa: E402  (W45: the chi formula)

OUT = HERE / "the_cusp_unit_as_a_vector.json"
mp.mp.dps = 30
I = mp.mpc(0, 1)
QI = np.array([[1j, 0], [0, -1j]])
QJ = np.array([[0, 1], [-1, 0]], dtype=complex)
QK = QI @ QJ
UNITS = [QI, QJ, QK]
J1 = 1j
V_PLUS = np.array([0, 1, -1j])    # e_j - sqrt(-1) e_k
V_MINUS = np.array([0, 1, 1j])    # e_j + sqrt(-1) e_k
E_I = np.array([1, 0, 0], dtype=complex)
TAUS = [mp.mpc(0, 1), mp.mpc(-0.5, mp.sqrt(3) / 2), mp.mpc(0, 4), mp.mpc(0.13, 1.21), mp.mpc(-0.31, 1.07),
        mp.mpc(0.42, 1.55), mp.mpc(0.07, 2.3), mp.mpc(-0.22, 0.99), mp.mpc(0.35, 0.95), mp.mpc(0.0, 1.8)]


# ----------------------------------------------------------------------------------------------------------- K1
def rho_word(w):
    M = np.eye(2, dtype=complex)
    for g in w:
        base = QI if abs(g) == 1 else QJ
        M = M @ (base if g > 0 else np.linalg.inv(base))
    return M


def coords(X):
    """the imaginary-quaternion coordinates of a 2 x 2 matrix: x_u = -tr(U X)/2"""
    return np.array([-np.trace(U @ X) / 2 for U in UNITS])


def move_on_M(name):
    aut = CP.AUT[name]
    ia, ib = rho_word(aut[1]), rho_word(aut[2])
    imgs = [ia, ib, ia @ ib]
    M = np.array([np.real(coords(X)) for X in imgs]).T     # columns: the images of e_i, e_j, e_k
    return np.round(M).astype(int)


def closure(gens):
    G = {tuple(np.eye(3, dtype=int).ravel())}
    frontier = [np.eye(3, dtype=int)]
    while frontier:
        new = []
        for A in frontier:
            for g in gens:
                B = g @ A
                key = tuple(B.ravel())
                if key not in G:
                    G.add(key)
                    new.append(B)
        frontier = new
    return [np.array(k).reshape(3, 3) for k in sorted(G)]


def line_key(v):
    v = np.asarray(v, dtype=complex)
    k = int(np.argmax(np.abs(v) > 1e-9))
    w = v / v[k]
    return tuple(np.round(w.real, 9)) + tuple(np.round(w.imag, 9))


def isotropic_lines_of(g):
    w, V = np.linalg.eig(g.astype(complex))
    out = []
    for lam in sorted(set(np.round(w, 9)), key=lambda z: (z.real, z.imag)):
        idx = [i for i in range(3) if abs(w[i] - lam) < 1e-7]
        B = np.linalg.qr(V[:, idx])[0] if len(idx) > 1 else V[:, idx]
        if B.shape[1] == 1:
            v = B[:, 0]
            if abs(v @ v) < 1e-9:
                out.append(v)
        elif B.shape[1] == 2:
            u, x = B[:, 0], B[:, 1]
            a, b, c = x @ x, 2 * (u @ x), u @ u     # (u + s x).(u + s x) = c + b s + a s^2
            if abs(a) > 1e-12:
                out += [u + s * x for s in np.roots([a, b, c])]
            else:                                   # x itself is isotropic: one root at s = infinity
                out += [x] + ([u - c / b * x] if abs(b) > 1e-12 else [])
    return out


def K1():
    L, R = move_on_M("L"), move_on_M("R")
    G = closure([L, R])
    signed = [np.diag(s) @ np.eye(3, dtype=int)[list(p)] for p in itertools.permutations(range(3))
              for s in itertools.product((1, -1), repeat=3)]
    rot = {tuple(m.ravel()) for m in signed if round(np.linalg.det(m)) == 1}
    is_O = {tuple(g.ravel()) for g in G} == rot
    quarter_i = bool(np.array_equal(L @ np.array([1, 0, 0]), [1, 0, 0]) and np.array_equal(L @ L, np.diag([1, -1, -1])))
    quarter_j = bool(np.array_equal(R @ np.array([0, 1, 0]), [0, 1, 0]) and np.array_equal(R @ R, np.diag([-1, 1, -1])))
    eig = {"e_i": complex((L @ E_I) @ np.conj(E_I) / (E_I @ np.conj(E_I))),
           "v+": complex((L @ V_PLUS) @ np.conj(V_PLUS) / (V_PLUS @ np.conj(V_PLUS))),
           "v-": complex((L @ V_MINUS) @ np.conj(V_MINUS) / (V_MINUS @ np.conj(V_MINUS)))}
    are_eig = all(np.allclose(L @ v, eig[k] * v) for k, v in (("e_i", E_I), ("v+", V_PLUS), ("v-", V_MINUS)))
    iso = {k: abs(v @ v) for k, v in (("e_i", E_I), ("v+", V_PLUS), ("v-", V_MINUS))}
    conj_swaps = line_key(np.conj(V_PLUS)) == line_key(V_MINUS)
    lines = {}
    for g in G:
        if np.array_equal(g, np.eye(3, dtype=int)):
            continue
        for v in isotropic_lines_of(g):
            lines.setdefault(line_key(v), v)
    orbits, seen = [], set()
    for k, v in lines.items():
        if k in seen:
            continue
        orb = {line_key(g @ v) for g in G}
        seen |= orb
        orbits.append(sorted(orb))
    sizes = sorted(len(o) for o in orbits)
    quarter_lines = set()
    for g in G:
        if round(np.trace(g)) == 1 and not np.array_equal(g, np.eye(3, dtype=int)):
            if np.array_equal(g @ g @ g @ g, np.eye(3, dtype=int)) and not np.array_equal(g @ g, np.eye(3, dtype=int)):
                quarter_lines |= {line_key(v) for v in isotropic_lines_of(g)}
    six = [o for o in orbits if len(o) == 6]
    holds = (is_O and len(G) == 24 and quarter_i and quarter_j and are_eig and iso["e_i"] > 0.5
             and iso["v+"] < 1e-12 and iso["v-"] < 1e-12 and conj_swaps and sizes == [6, 8, 12]
             and bool(six) and set(six[0]) == quarter_lines and line_key(V_PLUS) in quarter_lines)
    return {"L on M": L.tolist(), "R on M": R.tolist(),
            "the group has 24 elements and is O": bool(is_O and len(G) == 24),
            "L a quarter-turn about e_i, R about e_j": [quarter_i, quarter_j],
            "L's eigenvalues on e_i, v+, v-": {k: [v.real, v.imag] for k, v in eig.items()},
            "v.v on e_i, v+, v-": iso, "conjugation exchanges v+ and v-": bool(conj_swaps),
            "the special isotropic lines": len(lines), "their orbits' sizes": sizes,
            "the 6-orbit is the quarter-turns' fixed lines": bool(six and set(six[0]) == quarter_lines),
            "holds": bool(holds)}, G, L, R, orbits, lines


# ----------------------------------------------------------------------------------------------------------- K2, K3
def Rvec(t):
    q = mp.exp(I * mp.pi * t)
    t2, t3, t4 = (mp.jtheta(n, 0, q) for n in (2, 3, 4))
    D = mp.pi * t2 * t3 * t4
    return mp.matrix([-t2 ** 2 / D, -t4 ** 2 / D, I * t3 ** 2 / D])


def to_np(v):
    return np.array([complex(v[k]) for k in range(3)])


def fit_perm(pairs):
    """the signed permutation P and scalars c with lhs = c P rhs at every pair"""
    best = None
    for p in itertools.permutations(range(3)):
        for s in itertools.product((1, -1), repeat=3):
            P = np.diag(s) @ np.eye(3)[list(p)]
            worst, cs = 0.0, []
            for lhs, rhs in pairs:
                Pr = [sum(P[i, j] * rhs[j] for j in range(3)) for i in range(3)]
                c = sum(lhs[i] * mp.conj(Pr[i]) for i in range(3)) / sum(abs(x) ** 2 for x in Pr)
                res = max(abs(lhs[i] - c * Pr[i]) for i in range(3)) / max(abs(x) for x in lhs)
                worst = max(worst, float(res))
                cs.append(c)
            if best is None or worst < best[0]:
                best = (worst, P, cs)
    return best


def K2(L):
    pairsT = [(Rvec(t + 1), Rvec(t)) for t in TAUS]
    pairsS = [(Rvec(-1 / t), Rvec(t)) for t in TAUS]
    wT, PT, cT = fit_perm(pairsT)
    wS, PS, cS = fit_perm(pairsS)
    cT_dev = max(float(abs(c - mp.exp(I * mp.pi / 4))) for c in cT)
    sign = [c / mp.power(-I * t, mp.mpf(-0.5)) for c, t in zip(cS, TAUS)]
    sgn = int(round(float(mp.re(sign[0]))))
    cS_dev = max(float(abs(s - sgn)) for s in sign)
    Ps = sgn * PS
    swap = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
    holds = (wT < 1e-25 and wS < 1e-25 and cT_dev < 1e-25 and cS_dev < 1e-25 and np.array_equal(PT, L.T)
             and np.array_equal(Ps, swap) and round(np.linalg.det(-Ps)) == 1)
    return {"tau + 1: residual": wT, "its matrix": PT.astype(int).tolist(),
            "equals L^-1": bool(np.array_equal(PT, L.T)),
            "its scalar against e^{i pi/4}": cT_dev, "-1/tau: residual": wS, "its matrix (sign fixed by the scalar)":
            Ps.astype(int).tolist(), "the scalar against (-i tau)^(-1/2)": cS_dev, "is the i-j swap":
            bool(np.array_equal(Ps, swap)), "-P is a rotation": bool(round(np.linalg.det(-Ps)) == 1),
            "holds": bool(holds)}, PT, Ps


def eigencomponents(Rv):
    Ri, Rj, Rk = Rv
    return Ri, (Rj + I * Rk) / 2, (Rj - I * Rk) / 2       # R = c_i e_i + c+ v+ + c- v-


def K3():
    ys = list(range(4, 11))
    logs = {"e_i": [], "v+": [], "v-": []}
    for y in ys:
        c = eigencomponents(Rvec(mp.mpc(0, y)))
        for k, v in zip(logs, c):
            logs[k].append(float(mp.log(abs(v))))
    lam = {k: float(-np.polyfit(ys, v, 1)[0] / (2 * np.pi)) for k, v in logs.items()}
    want = {"e_i": 0.125, "v+": -0.125, "v-": 0.375}
    ri = np.polyfit(ys, np.array(logs["e_i"]) - np.array(logs["v+"]), 1)[0]
    rm = np.polyfit(ys, np.array(logs["v-"]) - np.array(logs["v+"]), 1)[0]
    Rv = to_np(Rvec(mp.mpc(0, 10)))
    dirn = abs(np.vdot(V_PLUS / np.sqrt(2), Rv)) / np.linalg.norm(Rv)
    holds = (all(abs(lam[k] - want[k]) < 1e-6 for k in want) and abs(ri + np.pi / 2) < 1e-6 and abs(rm + np.pi) < 1e-6
             and abs(dirn - 1) < 1e-12)
    return {"leading exponents (q = e^{2 pi i tau})": lam, "the slope of log|c_i/c+|": float(ri),
            "the slope of log|c-/c+|": float(rm), "|<v+/sqrt 2, R/|R|>| at 10i": float(dirn), "holds": bool(holds)}


# ----------------------------------------------------------------------------------------------------------- K4, K5
def collocate(rS, rT, k, units, N=24, M=120):
    """holomorphic sections of weight k for (rho(S), rho(T)) with end data units per eigenline (e_i, v+, v-) of
    rho(T): f(tau + 1) = rho(T) f(tau), f(-1/tau) = tau^k rho(S) f(tau). Returns the dimension, the gap and the null
    space (in the eigenbasis columns), and the column list"""
    w, P = np.linalg.eig(rT)
    lam = [float(np.angle(z) / (2 * np.pi)) % 1.0 for z in w]
    which = {}
    for j, l in enumerate(lam):
        which[j] = min((("e_i", 0.125), ("v+", 0.875), ("v-", 0.375)), key=lambda p: abs(p[1] - l))[0]
    shift = {"e_i": units[0], "v+": units[1], "v-": units[2]}
    cols = [(j, n) for j in range(3) for n in range(-shift[which[j]], N)]
    h0 = np.sqrt(3) / 2

    def phi(j, n, t):
        e = n + lam[j]
        return np.exp(2j * np.pi * e * t) * np.exp(2 * np.pi * e * h0)

    thetas = np.linspace(np.pi / 3 + 0.02, 2 * np.pi / 3 - 0.02, M)
    rows = []
    for th in thetas:
        t = np.exp(1j * th)
        ts = -1 / t
        tk = np.exp(float(k) * np.log(t))
        block = np.zeros((3, len(cols)), dtype=complex)
        for c, (j, n) in enumerate(cols):
            block[:, c] = P[:, j] * phi(j, n, ts) - tk * (rS @ P[:, j]) * phi(j, n, t)
        rows.append(block)
    A = np.vstack(rows)
    _, s, vh = np.linalg.svd(A)
    s = s / s[0]
    null = int(sum(s < 1e-9))
    gap = [float(s[len(s) - null - 1]) if null < len(s) else None, float(s[-1]) if null else None]
    return null, gap, (vh[len(s) - null:].conj() if null else None), cols, P, lam, which


def reps(PT, Ps):
    rT = np.exp(1j * np.pi / 4) * PT.astype(complex)
    rS = np.exp(1j * np.pi / 4) * Ps.astype(complex)
    return rS, rT


def K4(rS, rT):
    rows = {}
    for u in itertools.product((0, 1), repeat=3):
        d, gap, _, _, _, lam, which = collocate(rS, rT, Fraction(-1, 2), u)
        chi = IW.chi(Fraction(-1, 2), rS, rT)[0] + sum(u)
        ex = {"e_i": 0.125 - u[0], "v+": 0.875 - u[1], "v-": 0.375 - u[2]}
        lead = min(ex, key=ex.get)
        rows[str(u)] = {"dimension (collocation)": d, "gap": gap, "chi + sum(u)": round(chi, 9),
                        "the generic section's cusp eigenline": lead, "isotropic": lead != "e_i"}
    d, gap, null, cols, P, lam, which = collocate(rS, rT, Fraction(-1, 2), (0, 1, 0))
    match = None
    if d == 1:
        vec = null[0]
        h0 = np.sqrt(3) / 2
        y0 = 1.0
        xs = np.arange(64) / 64
        Pinv = np.linalg.inv(P)
        samples = [Pinv @ to_np(Rvec(mp.mpc(x, y0))) for x in xs]
        worst, scale = 0.0, None
        for c, (j, n) in enumerate(cols):
            if n > 4:
                continue
            e = n + lam[j]
            a = np.mean([s[j] * np.exp(-2j * np.pi * e * (x + 1j * y0)) for s, x in zip(samples, xs)])
            b = a * np.exp(-2 * np.pi * e * h0)                 # in the collocation's normalization
            if scale is None and abs(vec[c]) > 1e-6:
                scale = b / vec[c]
            if scale is not None:
                worst = max(worst, abs(b - scale * vec[c]) / abs(scale))
        match = float(worst)
    holds = (rows["(0, 0, 0)"]["dimension (collocation)"] == 0 and rows["(0, 1, 0)"]["dimension (collocation)"] == 1
             and match is not None and match < 1e-8)
    return {"placements": rows, "R against the null vector (u = (0, 1, 0)), largest relative difference": match,
            "holds": bool(holds)}


def K5(rS, rT):
    rows, ok = {}, True
    for u in itertools.product((0, 1), repeat=3):
        d, gap, *_ = collocate(rS, rT, Fraction(3, 2), u)
        chi = IW.chi(Fraction(3, 2), rS, rT)[0] + sum(u)
        rows[str(u)] = {"dimension (collocation)": d, "gap": gap, "chi + sum(u)": round(chi, 9)}
        ok &= d == sum(u) and abs(chi - sum(u)) < 1e-9
    return {"placements": rows, "holds": bool(ok)}


# ----------------------------------------------------------------------------------------------------------- K6, K7
def r6(x):
    return x[:3] + 1j * x[3:]


def K6():
    a = sy.symbols("a1:4", real=True)
    b = sy.symbols("b1:4", real=True)
    z = [a[i] + sy.I * b[i] for i in range(3)]
    zc = [a[i] - sy.I * b[i] for i in range(3)]
    cross = [zc[1] * z[2] - zc[2] * z[1], zc[2] * z[0] - zc[0] * z[2], zc[0] * z[1] - zc[1] * z[0]]
    lhs = sum(sy.expand(c * sy.conjugate(c)) for c in cross)
    n2 = sum(z[i] * zc[i] for i in range(3))
    zz = sum(z[i] ** 2 for i in range(3))
    rhs = n2 ** 2 - zz * sy.conjugate(zz)
    exact = sy.simplify(sy.expand(lhs - rhs).subs({sy.conjugate(s): s for s in a + b})) == 0
    rng = np.random.default_rng(6401)
    out = {"|a* x a|^2 = |a|^4 - |a.a|^2 (sympy)": bool(exact)}
    ok = bool(exact)
    for lam2 in (1.0, -1.0):
        best = None
        for _ in range(200):
            f = lambda x: lam2 * abs(r6(x) @ r6(x)) ** 2 / np.vdot(r6(x), r6(x)).real ** 2  # noqa: E731
            res = minimize(f, rng.normal(size=6), method="BFGS", options={"gtol": 1e-13, "maxiter": 2000})
            if best is None or res.fun < best.fun:
                best = res
        av = r6(best.x) / np.linalg.norm(r6(best.x))
        iso = abs(av @ av)
        ph = np.angle(av @ av) / 2
        realness = float(np.linalg.norm((np.exp(-1j * ph) * av).imag))
        out[f"lambda2 = {lam2:+.0f}"] = {"|a.a| / |a|^2": float(iso), "|Im(e^{-i phi} a)|": realness}
        ok &= iso < 1e-8 if lam2 > 0 else realness < 1e-8
    out["holds"] = bool(ok)
    return out


def A_of(a):
    return float(np.sum(np.abs(a) ** 4) / np.linalg.norm(a) ** 4)


def K7(G, orbits, lines):
    chis = [(np.trace(g) ** 2 + np.trace(g @ g)) / 2 for g in G]
    n_inv = float(np.sum(np.abs(chis) ** 2) / len(G))
    rng = np.random.default_rng(6402)
    inv_ok = True
    for _ in range(20):
        a = rng.normal(size=3) + 1j * rng.normal(size=3)
        for g in G:
            b = g @ a
            inv_ok &= abs(A_of(b) - A_of(a)) < 1e-12
    by_size = {len(o): [A_of(lines[k]) for k in o] for o in orbits}
    cone = []
    for _ in range(10000):
        u, v = rng.normal(size=3), rng.normal(size=3)
        v -= (v @ u) / (u @ u) * u
        v *= np.linalg.norm(u) / np.linalg.norm(v)
        cone.append(A_of(u + 1j * v))
    lands = {}
    for c in (-0.1, 0.1):
        best = None
        for _ in range(200):
            def f(x):
                z = r6(x)
                n = np.vdot(z, z).real
                return abs(z @ z) ** 2 / n ** 2 + c * np.sum(np.abs(z) ** 4) / n ** 2
            res = minimize(f, rng.normal(size=6), method="BFGS", options={"gtol": 1e-12, "maxiter": 2000})
            if best is None or res.fun < best.fun:
                best = res
        z = r6(best.x)
        z = z / np.linalg.norm(z)
        hit = {}
        for o in orbits:
            hit[len(o)] = max(abs(np.vdot(lines[k] / np.linalg.norm(lines[k]), z)) for k in o)
        lands[f"c = {c:+.1f}"] = {"the minimum": float(best.fun), "|a.a|": float(abs(z @ z)),
                                  "largest overlap with each orbit's lines": {str(k): float(v) for k, v in hit.items()}}
    ok = (abs(n_inv - 3) < 1e-9 and inv_ok
          and all(abs(x - 0.5) < 1e-12 for x in by_size[6]) and all(abs(x - 1 / 3) < 1e-12 for x in by_size[8])
          and all(abs(x - 0.375) < 1e-12 for x in by_size[12])
          and min(cone) >= 1 / 3 - 1e-12 and max(cone) <= 0.5 + 1e-12
          and abs(lands["c = -0.1"]["largest overlap with each orbit's lines"]["6"] - 1) < 1e-6
          and abs(lands["c = +0.1"]["largest overlap with each orbit's lines"]["8"] - 1) < 1e-6)
    return {"dimension of O's phase-invariant quartics (character count)": n_inv, "A is O-invariant": bool(inv_ok),
            "A / |a|^4 on each orbit": {str(k): [min(v), max(v)] for k, v in by_size.items()},
            "A / |a|^4 over 10000 cone points": [min(cone), max(cone)], "the minima": lands, "holds": bool(ok)}


# ----------------------------------------------------------------------------------------------------------- main
def readouts(L, R, Ps, orbits, lines, k4):
    ro = {}
    spec = {}
    for name, t in (("i", mp.mpc(0, 1)), ("2i", mp.mpc(0, 2)), ("omega", mp.mpc(-0.5, mp.sqrt(3) / 2))):
        Rv = to_np(Rvec(t))
        row = {}
        for o in orbits:
            ms = []
            for key in o:
                a = lines[key] / np.linalg.norm(lines[key])
                Y = np.outer(a, Rv) + np.outer(Rv, a) - (a @ Rv) * np.eye(3)
                U, s, Vh = np.linalg.svd(Y)
                ms.append([float(s[1] / s[0]), float(s[0] / np.linalg.norm(Rv)),
                           float(abs(np.vdot(np.conj(Rv) / np.linalg.norm(Rv), U[:, 0])))])
            row[f"{len(o)}-orbit [m, heavy mass / |R|, |<R-bar/|R|, heavy state>|], min and max"] = [
                [min(x[i] for x in ms) for i in range(3)], [max(x[i] for x in ms) for i in range(3)]]
        spec[name] = row
    ro["m at the special lines"] = spec
    ro["every placement at weight -1/2"] = k4["placements"]
    Ri = np.round(np.linalg.inv(R)).astype(int)
    St = L @ Ri @ L
    ro["S~ = L R^-1 L on M"] = St.tolist()
    ro["S~ against -P, P and their inverses"] = {"-P": bool(np.array_equal(St, -Ps)), "P": bool(np.array_equal(St, Ps)),
                                                "(-P)^-1": bool(np.array_equal(St, np.linalg.inv(-Ps).round()))}
    return ro


def main():
    k1, G, L, R, orbits, lines = K1()
    k2, PT, Ps = K2(L)
    k3 = K3()
    rS, rT = reps(PT, Ps)
    k4 = K4(rS, rT)
    k5 = K5(rS, rT)
    k6 = K6()
    k7 = K7(G, orbits, lines)
    out = {"status": "W64: the cusp's unit as a vector in M, in both frames (the rule W64_RULE.md first; one run)",
           "K1": k1, "K2": k2, "K3": k3, "K4": k4, "K5": k5, "K6": k6, "K7": k7}
    out["cells"] = {k: out[k]["holds"] for k in ("K1", "K2", "K3", "K4", "K5", "K6", "K7")}
    out["every cell holds"] = all(out["cells"].values())
    out["read-outs"] = readouts(L, R, Ps, orbits, lines, k4)
    def enc(x):
        if isinstance(x, complex):
            return [float(np.real(x)), float(np.imag(x))]
        return float(x) if isinstance(x, (np.floating, float)) else str(x)
    OUT.write_text(json.dumps(out, indent=1, default=enc) + "\n", encoding="utf-8")
    print(json.dumps(out["cells"], indent=1), "\nevery cell holds:", out["every cell holds"])


if __name__ == "__main__":
    main()
