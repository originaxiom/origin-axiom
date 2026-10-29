"""B1813's LIMITS AT SOURCE (P-442; main's task B), the one script of LIMITS_RULE.md (sealed 792562983).

Data-free.  The web seat, 2026-10-29.  0 of 19.
(a) E r = E[2 log(a + x')], a ~ Geometric(1/2), x' ~ the ?-measure (i.i.d. Geometric(1/2) digits, depth 48).
(b) T0(Y) = (1/E r) sum_a 2^-a E[2 arccosh((a + s)/(2Y))_+], s = x' + y, at Y = 1.5, 2, 3, against B1813's limit.
(c) C_Y(theta) = Y^(1/2) 4^Y T0(Y) at Y = (floor(2 Y0) + theta)/2, Y0 = 8 and 15, theta on 40 points.
(d) the series C(theta) = (2/E r) E_s[2^s g(s - theta)], g(v) = sum_j 2^-(j+v) sqrt((j+v)_+); its mean; its first
    Fourier coefficient against g1 E[2^s e^(2 pi i s)] with g_n = Gamma(3/2)/(log 2 + 2 pi i n)^(3/2) (sign convention
    of the series); the local rate at Y ~ 15.
(e) post hoc (the values were read before the seal): P(beta) log(1/(1-beta))/(1-beta) at beta = 0.95, 0.98, 0.99 from
    THE CRITICAL LINE's committed output.
Run: python3 limits.py --run > limits_out.txt
"""
import json, math, pathlib, sys
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
LN2 = math.log(2.0)
NB, NPER = 20, 200_000                     # 20 blocks x 2e5 = 4e6 draws of (x', y)


def qm(rng, n, depth=48):
    v = np.zeros(n)
    for _ in range(depth):
        v = 1.0 / (rng.geometric(0.5, n) + v)
    return v


def g(v, jmin=-3, jmax=90):
    tot = np.zeros_like(v)
    for j in range(jmin, jmax + 1):
        t = j + v
        tot += np.where(t > 0, 2.0 ** (-t) * np.sqrt(np.maximum(t, 0.0)), 0.0)
    return tot


def main():
    if "--run" not in sys.argv: raise SystemExit(__doc__)
    rng = np.random.default_rng(442)
    A = np.arange(1, 121, dtype=float)                       # a = 1..120
    W = 2.0 ** (-A)
    Er_b, T_b, CY8_b, CY15_b, Cs_b, F1_b, Es_b = [], [], [], [], [], [], []
    TH = np.arange(40) / 40.0
    THf = TH
    VG = np.arange(65536) / 65536.0
    GV = g(VG)                                               # g is 1-periodic; tabulated once, interpolated periodically
    gp = lambda v: np.interp(np.mod(v, 1.0), VG, GV, period=1.0)
    Y0s = {8: [(16 + th) / 2 for th in TH], 15: [(30 + th) / 2 for th in TH]}
    for blk in range(NB):
        xp = qm(rng, NPER); y = qm(rng, NPER); s = xp + y
        a = rng.geometric(0.5, NPER).astype(float)
        Er = (2 * np.log(a + qm(rng, NPER))).mean()          # an independent x' for E r
        Er_b.append(Er)

        def T0(Yv):
            tot = 0.0
            for ai, wi in zip(A, W):
                arg = (ai + s) / (2 * Yv)
                if ai + 2 < 2 * Yv: continue
                tot += wi * np.where(arg > 1, 2 * np.arccosh(np.maximum(arg, 1.0)), 0.0).mean()
            return tot / Er

        def CY(Yv):                                           # Y^(1/2) 4^Y T0(Y), with 2^(2Y - a) to avoid underflow
            tot = 0.0
            for ai in A:
                if ai + 2 < 2 * Yv: continue
                arg = (ai + s) / (2 * Yv)
                tot += 2.0 ** (2 * Yv - ai) * np.where(arg > 1, 2 * np.arccosh(np.maximum(arg, 1.0)), 0.0).mean()
            return math.sqrt(Yv) * tot / Er

        T_b.append([T0(v) for v in (1.5, 2.0, 3.0)])
        CY8_b.append([CY(v) for v in Y0s[8]])
        CY15_b.append([CY(v) for v in Y0s[15]])
        w2 = 2.0 ** s
        Cs_b.append([(2 / Er) * (w2 * gp(s - th)).mean() for th in THf])
        F1_b.append((w2 * np.exp(2j * math.pi * s)).mean())
        Es_b.append(w2.mean())
    Er_b = np.array(Er_b); T_b = np.array(T_b); CY8 = np.array(CY8_b); CY15 = np.array(CY15_b); Cs = np.array(Cs_b)
    m = lambda X: X.mean(0); se = lambda X: X.std(0, ddof=1) / math.sqrt(NB)
    Er = Er_b.mean()
    print("B1813's LIMITS AT SOURCE — one run of the sealed rule (792562983)\n")
    print("(a)  E r = %.6f +- %.6f;  E r / 2 = %.6f (B1813: 0.7924; Kesseboehmer-Stratmann: chi ~ 0.792)  L1: %s" % (
        Er, Er_b.std(ddof=1) / math.sqrt(NB), Er / 2, abs(Er / 2 - 0.7924) < 1e-3))
    ref = (0.3829, 0.1676, 0.03462)
    z = (m(T_b) - np.array(ref)) / se(T_b)
    print("(b)  T0(1.5), T0(2), T0(3) = %s +- %s; B1813 %s; z %s  L2: %s" % (
        np.round(m(T_b), 6), np.round(se(T_b), 6), ref, np.round(z, 2), bool(np.all(abs(z) < 3))))
    for Y0, X in ((8, CY8), (15, CY15)):
        c, e = m(X), se(X)
        d = X - X[:, [0]]                                     # common random numbers: differences from theta = 0
        dse = d.std(0, ddof=1) / math.sqrt(NB)
        imax, imin = int(np.argmax(c)), int(np.argmin(c))
        rng_ = c[imax] - c[imin]
        dd = X[:, imax] - X[:, imin]; dd_se = dd.std(ddof=1) / math.sqrt(NB)
        print("(c)  Y0 = %d: C_Y(theta) mean %.5f, range %.5f (%.3f%% of mean; %.1f SE of the paired difference), "
              "max at theta %.3f, min at theta %.3f; C_Y(0) = %.5f" % (Y0, c.mean(), rng_, 100 * rng_ / c.mean(), rng_ / dd_se,
                                                                     TH[imax], TH[imin], c[0]))
        if Y0 == 15:
            L3 = bool(rng_ / c.mean() > 0.002 and rng_ > 3 * dd_se)
            print("     L3 (range > 0.2% of the mean, beyond 3 SE): %s" % L3)
        print("     C_Y on theta (every 4th): " + ", ".join("%.3f:%.4f" % (t, v) for t, v in zip(TH[::4], c[::4])))
    Cser = m(Cs)
    Cbar = Cser.mean()
    ghat0 = math.gamma(1.5) / LN2 ** 1.5
    Cbar_an = (2 / Er) * ghat0 * np.mean(Es_b)
    fft = np.fft.fft(Cser) / len(Cser)
    F1 = np.mean(F1_b)
    g1 = math.gamma(1.5) / (LN2 + 2j * math.pi) ** 1.5
    pred1 = (2 / Er) * g1 * F1
    print("(d)  the series: C-bar = %.5f (analytic mean (2/E r) g0 E[2^s] = %.5f); min %.5f, max %.5f (range %.3f%%)" % (
        Cbar, Cbar_an, Cser.min(), Cser.max(), 100 * (Cser.max() - Cser.min()) / Cbar))
    print("     first Fourier coefficient |c1| = %.5f; predicted |(2/E r) g1 E[2^s e^(2 pi i s)]| = %.5f; |E[2^s e^(2 pi i s)]| = %.5f"
          % (abs(fft[1]), abs(pred1), abs(F1)))
    print("     C(theta) (every 4th of 40): " + ", ".join("%.3f:%.4f" % (t, v) for t, v in zip(THf[::4], Cser[::4])))
    print("     L4 (C-bar in (3.85, 4.05)): %s" % (3.85 < Cbar < 4.05))
    # the approach of C_Y to C at theta = 0 (finite-Y correction)
    for Y0, X in ((8, CY8), (15, CY15)):
        print("     C_Y(theta)/C(theta) at Y0 = %d (theta = 0, 0.25, 0.5, 0.75): %s" % (
            Y0, [round(m(X)[i] / Cser[i], 5) for i in (0, 10, 20, 30)]))
    # local rate at Y ~ 15, averaged over a full period
    c15 = m(CY15)
    print("     local rate at Y ~ 15 from the form: 2 log 2 + 1/(2Y) = %.5f (2 log 2 = %.5f)" % (2 * LN2 + 1 / 30, 2 * LN2))
    # (e) post hoc
    run = json.loads((HERE.parent / "chat1_2026-10-29_critical_line" / "critical_line.json").read_text())
    P = {e["beta"]: e["P"] for e in run["line"]}
    rat = {b: P[b] * math.log(1 / (1 - b)) / (1 - b) for b in (0.95, 0.98, 0.99)}
    print("(e)  POST HOC (values read before the seal): P(beta) log(1/(1-beta))/(1-beta): %s  L5: %s" % (
        {b: round(v, 4) for b, v in rat.items()}, 0.3 < rat[0.99] < 3))
    print("\n     the hierarchy exponent (B2): 2 log 2 / pi = %.6f; the modulation's period in x: e^(pi/2) = %.4f" % (
        2 * LN2 / math.pi, math.exp(math.pi / 2)))


if __name__ == "__main__":
    main()
