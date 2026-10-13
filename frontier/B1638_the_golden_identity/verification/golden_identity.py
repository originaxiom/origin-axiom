#!/usr/bin/env python3
"""B1638 -- THE GOLDEN IDENTITY.  B1636 found the weave's lowest coupling golden (masses 1 : 1/phi : 1/phi^2) on the tick's
axis, exactly where F = sum_p |theta_p/eta|^4 = 8, and conjectured that {F = 8} is the union of the discriminant-5 geodesics.
A mechanism: on the axis of a hyperbolic M = [[a, b], [c, d]] (the circle |tau - (a-d)/2c|^2 = (tr^2 - 4)/4c^2) the
conjugate of tau is a Moebius image, and since theta_p and eta have real q-coefficients, conj(g_p(tau)) = g_p(N_M tau) with
g_p = (theta_p/eta)^2 and N_M = [[d - a, -2b], [2c, d - a]] (det = tr^2 - 4, the discriminant).  So on the axis
F = H_M(tau) := sum_p g_p(tau) g_p(N_M tau), and if H_M is the constant 8 everywhere, F = 8 on the axis.
 I1  H_LR at 40 random tau (Re in [-0.5, 0.5], Im in [0.4, 3]), at 50 digits: the largest |H - 8|.
 I2  the other five matchings of the three theta constants (sum_p g_p(tau) g_{pi(p)}(N tau)): their spread over the points.
 I3  H_M for other closed geodesics: L^2 R, L R^2 (tr 4), L^3 R (tr 5), L^2 R^2 (tr 6), L R L R^2: constant or not (spread).
 I4  positive controls: RL and L R L^-1 ... the discriminant-5 classes (conjugates of LR): H constant 8.
 I5  the axis check: on 10 points of LR's axis, conj(g_p(tau)) - g_p(N tau) and F - 8.
Writes golden_identity.json."""
import json, pathlib, itertools, random
import mpmath as mp
HERE = pathlib.Path(__file__).resolve().parent
mp.mp.dps = 50


def g(t):
    e = lambda x: mp.exp(1j * mp.pi * t * x)
    K = 80
    th2 = mp.fsum(e((n + mp.mpf(1) / 2) ** 2) for n in range(-K, K))
    th3 = mp.fsum(e(n * n) for n in range(-K, K + 1))
    th4 = mp.fsum((-1) ** abs(n) * e(n * n) for n in range(-K, K + 1))
    eta = mp.exp(1j * mp.pi * t / 12) * mp.fprod(1 - mp.exp(2j * mp.pi * t * n) for n in range(1, 600))
    return [th2 ** 2 / eta ** 2, th3 ** 2 / eta ** 2, th4 ** 2 / eta ** 2]


def mob(M, t):
    return (M[0][0] * t + M[0][1]) / (M[1][0] * t + M[1][1])


def N_of(M):
    a, b, c, d = M[0][0], M[0][1], M[1][0], M[1][1]
    return [[d - a, -2 * b], [2 * c, d - a]]


def mul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def H(M, t, perm=(0, 1, 2)):
    N = N_of(M); a, b = g(t), g(mob(N, t))
    return mp.fsum(a[i] * b[perm[i]] for i in range(3))


def spread(vals):
    return float(max(abs(v - vals[0]) for v in vals))


def main():
    rnd = random.Random(1638)
    pts = [mp.mpc(rnd.uniform(-0.5, 0.5), rnd.uniform(0.4, 3.0)) for _ in range(40)]
    L = [[1, 1], [0, 1]]; R = [[1, 0], [1, 1]]; Li = [[1, -1], [0, 1]]
    LR = mul(L, R)
    out = {}
    vals = [H(LR, t) for t in pts]
    out["I1"] = {"points": len(pts), "max_abs_H_minus_8": float(max(abs(v - 8) for v in vals)), "N": N_of(LR)}
    out["I2"] = {str(p): spread([H(LR, t, p) for t in pts[:10]]) for p in itertools.permutations(range(3)) if p != (0, 1, 2)}
    others = {"L^2 R": mul(L, LR), "L R^2": mul(LR, R), "L^3 R": mul(L, mul(L, LR)), "L^2 R^2": mul(mul(L, LR), R), "L R L R^2": mul(LR, mul(LR, R))}
    out["I3"] = {}
    for nm, M in others.items():
        tr = M[0][0] + M[1][1]
        v = [H(M, t) for t in pts[:10]]
        out["I3"][nm] = {"trace": tr, "discriminant": tr * tr - 4, "spread": spread(v), "first": complex(v[0])}
    controls = {"RL": mul(R, L), "L (LR) L^-1": mul(mul(L, LR), Li), "R^-1 (LR) R": mul(mul([[1, 0], [-1, 1]], LR), R)}
    out["I4"] = {nm: {"trace": M[0][0] + M[1][1], "max_abs_H_minus_8": float(max(abs(H(M, t) - 8) for t in pts[:10]))} for nm, M in controls.items()}
    N = N_of(LR); ax = []
    for k in range(10):
        s = mp.mpf(0.2) + k * (mp.pi - mp.mpf(0.4)) / 9
        t = mp.mpf(0.5) + mp.sqrt(5) / 2 * mp.exp(1j * s)
        a, b = g(t), g(mob(N, t))
        ax.append({"conj_mismatch": float(max(abs(mp.conj(x) - y) for x, y in zip(a, b))), "F_minus_8": float(abs(mp.fsum(abs(x) ** 2 for x in a) - 8))})
    out["I5"] = {"max_conj_mismatch": max(r["conj_mismatch"] for r in ax), "max_F_minus_8": max(r["F_minus_8"] for r in ax)}
    json.dump(out, open(HERE / "golden_identity.json", "w"), indent=1, default=str)
    print(json.dumps(out, indent=1, default=str))


if __name__ == "__main__":
    main()
