"""W100: a blind replication of B1667's end radius L at two generic moduli (rule: W100_RULE.md).

The route is the Fuchsian side, independent of B1667's torus-side route:
- the punctured-torus group from its Fricke traces (x, y; z by the root that the side of Re tau picks);
- its weight-two cusp form by Hejhal's method (the pullback's path chosen in floats and applied in mpmath);
- the periods give tau = omega_A / omega_B, with the lattice omega_B (Z + tau Z);
- L(Y) = 2 pi Y / h - log(h |a_1| / (2 pi |omega_B|)), at Y_max = 1 / min|c| and Y_2 = h / 2.
Newton on (x, y) reaches each target from the hexagonal traces (3, 3), at N = 30, and is then polished at N = 45 and at
N = 60. One run; the output is committed before it is read. DRY=1 swaps the targets for the exploration's non-target
point (the pre-run review), and writes nothing in the dossier.

Run from the repository root: python3 docs/dossiers/the_weave_2026-10-07/the_canonical_cusp_replication.py
"""
import json
import os
import sys
import time
from pathlib import Path

import numpy as np
import mpmath as mp
mp.mp.dps = 30
I = mp.mpc(0, 1)


def mat(a, b, c, d):
    return mp.matrix([[a, b], [c, d]])


def inv(M):
    return mat(M[1, 1], -M[0, 1], -M[1, 0], M[0, 0])


def mob(M, w):
    return (M[0, 0] * w + M[0, 1]) / (M[1, 0] * w + M[1, 1])


def group(x, y, s=1):
    z = (x * y + s * mp.sqrt(x * x * y * y - 4 * (x * x + y * y))) / 2
    lam = (x + mp.sqrt(x * x - 4)) / 2
    A = mat(lam, 0, 0, 1 / lam)
    p = (z - y / lam) / (lam - 1 / lam)
    s = y - p
    B = mat(p, 1, p * s - 1, s)
    K = A * B * inv(A) * inv(B)
    wf = (K[0, 0] - K[1, 1]) / (2 * K[1, 0])
    Mc = mat(0, -1, 1, -wf)
    return Mc * A * inv(Mc), Mc * B * inv(Mc), Mc * K * inv(Mc), z


def setup(x, y, s=1, maxlen=5):
    A, B, K, z = group(x, y, s)
    h = abs(K[0, 1])
    gens = {'a': A, 'A': inv(A), 'b': B, 'B': inv(B)}
    back = {'a': 'A', 'A': 'a', 'b': 'B', 'B': 'b'}
    words = []

    def rec(w, M):
        if w and abs(M[1, 0]) > mp.mpf(10) ** -20:
            words.append((w, M))
        if len(w) == maxlen:
            return
        for g, Gm in gens.items():
            if w and back[g] == w[-1]:
                continue
            rec(w + g, M * Gm)

    rec('', mat(1, 0, 0, 1))
    F = np.array([[float(M[0, 0]), float(M[0, 1]), float(M[1, 0]), float(M[1, 1])] for _, M in words])
    cmin = min(abs(M[1, 0]) for _, M in words)
    return dict(A=A, B=B, K=K, z=z, h=h, words=words, F=F, cmin=cmin)


def pullback(G, w):
    """the path is chosen in floats; the composite map is built and applied in mpmath"""
    h, F, hf = G['h'], G['F'], float(G['h'])
    gam = mat(1, 0, 0, 1)
    wf = complex(w)
    for _ in range(5000):
        k = int(np.floor(wf.real / hf + 0.5))
        if k:
            gam = mat(1, -k * h, 0, 1) * gam
            wf = wf - k * hf
        den = F[:, 2] * wf + F[:, 3]
        ims = wf.imag / np.abs(den) ** 2
        j = int(np.argmax(ims))
        if ims[j] <= wf.imag * (1 + 1e-12):
            break
        gam = G['words'][j][1] * gam
        wf = (F[j, 0] * wf + F[j, 1]) / den[j]
    else:
        raise RuntimeError('pullback did not terminate')
    ws = mob(gam, w)
    k = mp.floor(mp.re(ws) / h + mp.mpf(1) / 2)       # final exact recentring
    if k:
        gam = mat(1, -k * h, 0, 1) * gam
        ws = mob(gam, w)
    return ws, gam


def hejhal(G, N, Y0):
    h = G['h']
    M = 2 * N
    rows, rhs, ymin = [], [], mp.inf
    for m in range(M):
        w = -h / 2 + h * (m + mp.mpf(1) / 2) / M + I * Y0
        ws, g = pullback(G, w)
        ymin = min(ymin, mp.im(ws))
        j = (g[1, 0] * w + g[1, 1]) ** (-2)
        q, qs = mp.exp(2 * mp.pi * I * w / h), mp.exp(2 * mp.pi * I * ws / h)
        row, qn, qsn = [], mp.mpf(1), mp.mpf(1)
        for n in range(1, N + 1):
            qn *= q
            qsn *= qs
            row.append(qn - j * qsn)
        rows.append(row[1:])
        rhs.append(-row[0])
    sol, res = mp.qr_solve(mp.matrix(rows), mp.matrix(rhs))
    return [mp.mpf(1)] + [sol[i] for i in range(N - 1)], res, ymin


def hejhal_auto(G, N):
    Y0 = mp.mpf('0.6') / G['cmin']
    for _ in range(12):
        ymin = min(mp.im(pullback(G, -G['h'] / 2 + G['h'] * (m + mp.mpf(1) / 2) / (2 * N) + I * Y0)[0])
                   for m in range(2 * N))
        if Y0 < mp.mpf('0.9') * ymin:
            break
        Y0 = mp.mpf('0.7') * ymin
    a, res, ymin = hejhal(G, N, Y0)
    return a, res, ymin, Y0


def Fint(G, a, w):
    h = G['h']
    q = mp.exp(2 * mp.pi * I * w / h)
    s, qn = 0, mp.mpf(1)
    for n in range(1, len(a) + 1):
        qn *= q
        s += a[n - 1] * h / (2 * mp.pi * I * n) * qn
    return s


def period(G, a, M):
    c, d = M[1, 0], M[1, 1]
    w0 = -d / c + I / abs(c)
    return Fint(G, a, mob(M, w0)) - Fint(G, a, w0)


def evaluate(x, y, N, s=1):
    G = setup(x, y, s)
    a, res, ymin, Y0 = hejhal_auto(G, N)
    oA, oB = period(G, a, G['A']), period(G, a, G['B'])
    tau = oA / oB
    h = G['h']
    base = -mp.log(h * abs(a[0]) / (2 * mp.pi * abs(oB)))
    Ymax, Y2 = 1 / G['cmin'], h / 2
    return dict(tau=tau, Lmax=2 * mp.pi * Ymax / h + base, L2=2 * mp.pi * Y2 / h + base, h=h, cmin=G['cmin'],
                Ymax=Ymax, Y2=Y2, res=res, Y0=Y0, ymin=ymin, a=a, z=G['z'])


def newton(target, x, y, N, s, tol, maxit=25):
    for _ in range(maxit):
        t = evaluate(x, y, N, s)['tau']
        r = t - target
        if abs(r) < tol:
            break
        d = mp.mpf(10) ** -12
        tx = (evaluate(x + d, y, N, s)['tau'] - t) / d
        ty = (evaluate(x, y + d, N, s)['tau'] - t) / d
        J = mp.matrix([[mp.re(tx), mp.re(ty)], [mp.im(tx), mp.im(ty)]])
        dx = mp.lu_solve(J, mp.matrix([-mp.re(r), -mp.im(r)]))
        lamb = mp.mpf(1)
        while True:
            xn, yn = x + lamb * dx[0], y + lamb * dx[1]
            if xn > 2 and yn > 2 and xn * xn * yn * yn > 4 * (xn * xn + yn * yn):
                break
            lamb /= 2
        x, y = xn, yn
    return x, y


def solve(target, N, steps=10, Npath=30):
    """the root s by the side of Re tau; continued from the hexagonal traces (3, 3), then polished at N"""
    s = 1 if mp.re(target) > 0 else -1
    x, y = mp.mpf(3), mp.mpf(3)
    t0 = evaluate(x, y, Npath, s)['tau']
    for k in range(1, steps + 1):
        x, y = newton(t0 + (target - t0) * k / steps, x, y, Npath, s, mp.mpf(10) ** -8)
    x, y = newton(target, x, y, N, s, mp.mpf(10) ** -24)
    return x, y, s




HERE = Path(__file__).resolve().parent
DRY = os.environ.get("DRY") == "1"
TAU1 = mp.mpc("0.137", "1.291") if not DRY else mp.mpc("0.31", "1.07")
TAU2 = mp.mpc("-0.284", "2.173") if not DRY else mp.mpc("-0.31", "1.07")
OMEGA_CLOSED = (mp.mpf("0.69208004049"), mp.mpf("2.78647514288"))     # B1667's eta^4 closed form, quoted


def cnum(z):
    return [float(mp.re(z)), float(mp.im(z))]


def at_target(target):
    t0 = time.time()
    rec = {"target": cnum(target)}
    for N in (45, 60):
        x, y, s = solve(target, N)
        r = evaluate(x, y, N, s)
        rec["N=%d" % N] = {"x": mp.nstr(x, 25), "y": mp.nstr(y, 25), "z": mp.nstr(r["z"], 25), "root": s,
                           "tau error": float(abs(r["tau"] - target)), "L_max": mp.nstr(r["Lmax"], 20),
                           "L_2": mp.nstr(r["L2"], 20), "h": mp.nstr(r["h"], 15), "min|c|": mp.nstr(r["cmin"], 15),
                           "Y_max": mp.nstr(r["Ymax"], 15), "Y_2": mp.nstr(r["Y2"], 15),
                           "a_2": cnum(r["a"][1]), "a_3": cnum(r["a"][2]), "Hejhal residual": float(r["res"]),
                           "Y0": mp.nstr(r["Y0"], 10), "lowest pulled-back height": mp.nstr(r["ymin"], 10)}
    rec["seconds"] = round(time.time() - t0, 1)
    return rec


def main():
    T0 = time.time()
    out = {"rule": "W100_RULE.md", "status": "one run" if not DRY else "DRY (non-target points)", "dps": mp.mp.dps}
    # R0, the gate at omega (traces 3, 3, the larger root)
    g = {}
    for N in (45, 60):
        r = evaluate(mp.mpf(3), mp.mpf(3), N, 1)
        g["N=%d" % N] = {"tau": cnum(r["tau"]), "L_max": mp.nstr(r["Lmax"], 20), "L_2": mp.nstr(r["L2"], 20),
                         "difference from the closed form": [float(abs(r["Lmax"] - OMEGA_CLOSED[0])),
                                                             float(abs(r["L2"] - OMEGA_CLOSED[1]))]}
    out["R0"] = g
    gate = max(max(v["difference from the closed form"]) for v in g.values()) < 1e-9
    out["cells"] = {"R0": gate}
    if not gate:
        out["stopped"] = "the gate failed"
    else:
        res = {"tau1": at_target(TAU1), "tau2": at_target(TAU2),
               "tau1 + 1": at_target(TAU1 + 1), "-1/tau1": at_target(-1 / TAU1)}
        out["targets"] = res
        Lf = lambda k, n, q: mp.mpf(res[k]["N=%d" % n][q])
        r1 = max(abs(Lf(k, 45, q) - Lf(k, 60, q)) for k in ("tau1", "tau2") for q in ("L_max", "L_2"))
        r2 = max(res[k]["N=60"]["tau error"] for k in ("tau1", "tau2"))
        lt = mp.log(abs(TAU1))
        cov = {q: {"L(tau1 + 1) - L(tau1)": float(Lf("tau1 + 1", 60, q) - Lf("tau1", 60, q)),
                   "L(-1/tau1) - L(tau1) - log|tau1|": float(Lf("-1/tau1", 60, q) - Lf("tau1", 60, q) - lt)}
               for q in ("L_max", "L_2")}
        r3 = max(abs(v) for d in cov.values() for v in d.values())
        r4 = all(mp.mpf(res[k]["N=60"]["Y_2"]) >= mp.mpf(res[k]["N=60"]["Y_max"]) for k in ("tau1", "tau2"))
        band = {k: (0.6 <= float(Lf(k, 60, "L_max")) <= 0.7 and 2.2 <= float(Lf(k, 60, "L_2")) <= 2.9)
                for k in ("tau1", "tau2")}
        out["R1, largest change between N = 45 and N = 60"] = float(r1)
        out["R2, largest tau error at N = 60"] = r2
        out["R3, covariance at tau1"] = cov
        out["R5, the band"] = band
        out["cells"].update({"R1": bool(r1 < 1e-9), "R2": bool(r2 < 1e-20), "R3": bool(r3 < 1e-9), "R4": bool(r4),
                             "R5 (tau1)": band["tau1"], "R5 (tau2)": band["tau2"]})
        out["for main: L at the targets (N = 60)"] = {k: {"tau": res[k]["target"], "L_max": res[k]["N=60"]["L_max"],
                                                          "L_2": res[k]["N=60"]["L_2"]} for k in ("tau1", "tau2")}
    out["seconds"] = round(time.time() - T0, 1)
    text = json.dumps(out, indent=1) + "\n"
    if DRY:
        sys.stdout.write(text)
    else:
        (HERE / "the_canonical_cusp_replication.json").write_text(text, encoding="utf-8")
        (HERE / "the_canonical_cusp_replication_run.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
