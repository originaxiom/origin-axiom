"""W-trace, step 1 of main's road (S_THE_PUSH_BACK §10.1), for the matter's own invariant defect (chat1; no data).

The quantity is main's f(tau) = |D(tau)| / ||R(tau)||^2, the matter's isotropy defect relative to the triplet's norm.
- It is modular invariant, bounded (about 1.09 at i), vanishes on omega's orbit, and falls toward the cusp.
- D = sum_r c_r R_r^2 (B1654), with the closed form c_r = -2 pi ln|theta_r(0)/eta|^2 - 2 pi ln((pi/2)|eta|^2) (W87).
  Because sum_r R_r^2 = 0 (Jacobi), this is D = -4 pi sum_r ln|theta_r(0)| R_r^2, a closed form in theta constants.
  It is checked here against main's quadrature values (B1654's end_data_defect_output.txt).

The rule that picks no thread: <f>_t, the mean of f over every primitive closed geodesic of trace t (all of one
length, so a plain mean of the threads' arc-length averages), for t = 3 .. TMAX, against the area average over the
modular surface (main: 0.31500491).

main's step 1 can fail by "no trend toward the equidistributed value (Duke), or the cusp taking over at every layer".
Threads come from every positive matrix of trace t, written as its unique word in L, R and kept if primitive and
least among its rotations. Each geodesic is sampled at 80 points per unit length on its axis. f is evaluated at the
point reduced to the fundamental domain, where the theta series converge fast.
Usage: python3 -B w_trace_defect.py [TMAX] > w_trace_defect_run.txt   (writes w_trace_defect.json)
"""
import json, math, os, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
TMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 40
K = 40


def theta_consts(tau):
    tau = np.asarray(tau, dtype=complex)
    q = np.exp(1j * np.pi * tau)[..., None]
    n = np.arange(0, K)
    t2 = 2 * np.sum(q ** ((n + 0.5) ** 2), -1)
    m = np.arange(1, K)
    t3 = 1 + 2 * np.sum(q ** (m ** 2), -1)
    t4 = 1 + 2 * np.sum((-1) ** m * q ** (m ** 2), -1)
    t1p = 2 * np.pi * np.sum((-1) ** n * (2 * n + 1) * q ** ((n + 0.5) ** 2), -1)
    return t2, t3, t4, t1p


def f_of(tau):
    t2, t3, t4, d = theta_consts(tau)
    R2, R4, R3 = -t2 ** 2 / d, -t4 ** 2 / d, 1j * t3 ** 2 / d
    D = -4 * np.pi * (np.log(np.abs(t2)) * R2 ** 2 + np.log(np.abs(t3)) * R3 ** 2 + np.log(np.abs(t4)) * R4 ** 2)
    return np.abs(D) / (np.abs(R2) ** 2 + np.abs(R3) ** 2 + np.abs(R4) ** 2)


def reduce(tau):
    tau = np.array(tau, dtype=complex)
    for _ in range(200):
        tau = tau - np.round(tau.real)
        small = np.abs(tau) < 1 - 1e-13
        if not small.any():
            break
        tau = np.where(small, -1 / tau, tau)
    return tau


def word_of(a, b, c, d):
    """the unique positive word in L = [[1,0],[1,1]], R = [[1,1],[0,1]] with this matrix (left to right)"""
    w = []
    while (a, b, c, d) != (1, 0, 0, 1):
        if a >= b and c >= d and (a, c) != (b, d) and a - b >= 0 and c - d >= 0 and not (b == 0 and d == 0):
            # M = M' R  <=>  M' = M R^-1 = [[a, b - a], [c, d - c]]: needs b >= a, d >= c; M = M' L <=> M' = [[a - b, b], [c - d, d]]
            pass
        if b >= a and d >= c:
            w.append("R"); b, d = b - a, d - c
        elif a >= b and c >= d:
            w.append("L"); a, c = a - b, c - d
        else:
            return None
    return "".join(reversed(w))


def threads_of_trace(t):
    out = set()
    for a in range(1, t):
        d = t - a
        n = a * d - 1
        for b in range(1, n + 1):
            if n % b:
                continue
            c = n // b
            w = word_of(a, b, c, d)
            if w is None or "L" not in w or "R" not in w:
                continue
            L = len(w)
            if any(w == w[:p] * (L // p) for p in range(1, L) if L % p == 0):
                continue                                  # not primitive
            if w == min(w[i:] + w[:i] for i in range(L)):
                out.add(w)
    return sorted(out)


def mat(w):
    A, B, C, D = 1, 0, 0, 1
    for ch in w:
        if ch == "L": A, B, C, D = A + B, B, C + D, D
        else: A, B, C, D = A, A + B, C, C + D
    return A, B, C, D


def thread_average(w, npl=80):
    best = None
    for k in range(len(w)):
        M = mat(w[k:] + w[:k])
        if best is None or abs(M[2]) < abs(best[2]): best = M
    a, b, c, d = best
    t = a + d
    x0 = (a - d) / (2 * c); rho = math.sqrt(t * t - 4) / (2 * abs(c)); ell = 2 * math.acosh(t / 2)
    n = max(64, int(npl * ell))
    s = -ell / 2 + ell * np.arange(n) / n
    tau = x0 + rho * (np.tanh(s) + 1j / np.cosh(s))
    return float(np.mean(f_of(reduce(tau)))), ell


def area_average(nx=200, ny=400, ycap=12.0):
    """<f> over the fundamental domain with the hyperbolic area measure (x in [-1/2, 1/2], y from the arc to ycap; the
    tail above ycap, where f ~ |q| y, is negligible)"""
    gx, wx = np.polynomial.legendre.leggauss(nx); X = 0.5 * gx; WX = 0.5 * wx
    gu, wu = np.polynomial.legendre.leggauss(ny)
    num = 0.0
    for x, wxi in zip(X, WX):
        y0 = math.sqrt(1 - x * x)
        u0, u1 = 1 / ycap, 1 / y0                      # integrate in u = 1/y: dA = dx dy / y^2 = dx du
        U = u0 + (u1 - u0) * (gu + 1) / 2; WU = wu * (u1 - u0) / 2
        fv = f_of(x + 1j / U)
        num += wxi * np.sum(WU * fv)
    return num / (math.pi / 3)                          # the whole domain's area; above ycap f ~ |q| y adds nothing


if __name__ == "__main__":
    pts = {"omega": np.exp(2j * np.pi / 3), "i": 1j, "0.13+1.07i": 0.13 + 1.07j, "0.3+1.6i": 0.3 + 1.6j,
           "2.2i": 2.2j, "3.0i": 3.0j}
    main_vals = {"omega": 4.052021e-14, "i": 1.088735, "0.13+1.07i": 0.9959543, "0.3+1.6i": 0.4138416,
                 "2.2i": 0.1276502, "3.0i": 0.01551}
    print("the closed form against main's quadrature (B1654, end_data_defect_output.txt):")
    for k_, tau in pts.items():
        print(f"  tau = {k_}: closed form {float(f_of(tau)):.7g}; main {main_vals[k_]:.7g}")
    inv = max(abs(float(f_of(tau)) - float(f_of(g(tau)))) for tau in (0.21 + 1.13j, -0.37 + 0.98j, 0.05 + 2.4j)
              for g in (lambda z: z + 1, lambda z: -1 / z, lambda z: (2 * z + 1) / (z + 1)))
    print(f"invariance of f under T, S and [[2,1],[1,1]] at three points: largest difference {inv:.1e}")
    A1, A2 = area_average(), area_average(nx=300, ny=600, ycap=16.0)
    print(f"area average of f over the modular surface: {A1:.8f} (finer: {A2:.8f}); main's: 0.31500491")
    out = {"area average": A2, "layers": {}}
    print("the rule that picks no thread, on f: the layer mean <f>_t over every primitive thread of trace t")
    for t in range(3, TMAX + 1):
        ws = threads_of_trace(t)
        avs = [thread_average(w)[0] for w in ws]
        m = float(np.mean(avs))
        out["layers"][t] = {"threads": len(ws), "mean": m, "min": min(avs), "max": max(avs),
                            "per thread": dict(zip(ws, avs)) if len(ws) <= 12 else None}
        print(f"  t = {t:3d}: {len(ws):4d} threads; <f>_t = {m:.5f} (deviation from the area average {m - A2:+.5f}); "
              f"thread range {min(avs):.3f} .. {max(avs):.3f}", flush=True)
    ts = sorted(out["layers"])
    print("the trend, averaged over windows of ten consecutive traces (weights: the threads):")
    for lo in range(3, TMAX + 1, 10):
        win = [t for t in ts if lo <= t < lo + 10]
        nthr = sum(out["layers"][t]["threads"] for t in win)
        mw = sum(out["layers"][t]["mean"] * out["layers"][t]["threads"] for t in win) / nthr
        print(f"  t = {win[0]}..{win[-1]}: {nthr:5d} threads; mean {mw:.5f} (deviation {mw - A2:+.5f})")
    json.dump(out, open(os.path.join(HERE, "w_trace_defect.json"), "w"), indent=1)
