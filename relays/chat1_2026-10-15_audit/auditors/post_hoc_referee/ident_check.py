"""Referee 2 (read-only, scratch): test the post hoc's void diagnosis. Rebuild F at -1/2 and 3/2, f and the particular
7/2 sections exactly as post_hoc_completions.py does (from a scratch extraction of the SM seat at 87cf7f551), then
  I1: theta_{-1/2} F_l against (e0 + 1/24) F_l(3/2), the structural s, at the value level and coefficient by coefficient;
  I2: alpha_l from the (e_i, 1/8) coefficient alone (where the particular section is zero by construction), then the
      value residual of particular - E4 F_l - alpha_l f;
  I3: beta_l the same way for theta^2 F_l (normalised at its unit);
  ISO: |G(F_i, E4 R, R)| against |G(F_i, E4 F_i, R)| at the five points (values, not coefficients).
"""
import sys, os, time, json
from fractions import Fraction
import numpy as np
import mpmath as mp

DOSS = sys.argv[1]
sys.path.insert(0, DOSS); os.chdir(DOSS)
t0 = time.time()
import the_surface_yukawa as SY  # noqa
SU, RC = SY.SU, SY.RC
mp.mp.dps = 40
I = mp.mpc(0, 1)
K32, K72, KM12 = Fraction(3, 2), Fraction(7, 2), Fraction(-1, 2)
UNIT8 = {l: SY.E8[l] - 8 for l in SY.LINES}
log = lambda *a: print(round(time.time() - t0, 1), *a, flush=True)


def solve72(units, norm_line, excl=("e_i", 0), N=30, M=120):   # verbatim from post_hoc_completions.py
    u = dict(zip(SY.LINES, units))
    n0 = -u[norm_line]
    cols = [(l, n) for l in SY.LINES for n in range(-u[l], N) if not (l == norm_line and n == n0) and (l, n) != excl]
    thetas = [mp.pi / 3 + mp.mpf("0.02") + j * (mp.pi / 3 - mp.mpf("0.04")) / (M - 1) for j in range(M)]
    A = mp.matrix(3 * M, len(cols)); b = mp.matrix(3 * M, 1)
    kk = mp.mpf(K72.numerator) / K72.denominator
    for r, th in enumerate(thetas):
        t = mp.exp(I * th); ts, tk = -1 / t, mp.power(t, kk)
        for c, (l, n) in enumerate(cols):
            e = n + SU.LAM[l]; sc = mp.exp(2 * mp.pi * e * SU.H0); v2 = SU.matvec(SU.RS, SU.B[l])
            for q in range(3):
                A[3 * r + q, c] = (SU.B[l][q] * SU.qp(e, ts) - tk * v2[q] * SU.qp(e, t)) * sc
        e = n0 + SU.LAM[norm_line]; v2 = SU.matvec(SU.RS, SU.B[norm_line])
        for q in range(3):
            b[3 * r + q] = -(SU.B[norm_line][q] * SU.qp(e, ts) - tk * v2[q] * SU.qp(e, t))
    Q, Rm = mp.qr(A, mode="skinny"); x = mp.lu_solve(Rm, Q.H * b)
    res = mp.norm(A * x - b) / mp.norm(b)
    terms = [(norm_line, n0 + SU.LAM[norm_line], mp.mpf(1))] + [
        (l, n + SU.LAM[l], x[c] * mp.exp(2 * mp.pi * (n + SU.LAM[l]) * SU.H0)) for c, (l, n) in enumerate(cols)]
    return terms, float(res)


CAP = SY.CAP8 // 8
sig = lambda m, p: sum(d ** p for d in range(1, m + 1) if m % d == 0)
E4 = {0: mp.mpf(1)}; E4.update({8 * m: mp.mpf(240 * sig(m, 3)) for m in range(1, CAP + 1)})
E2 = {0: mp.mpf(1)}; E2.update({8 * m: mp.mpf(-24 * sig(m, 1)) for m in range(1, CAP + 1)})


def serre(X, k):
    D = {key: (mp.mpf(key[1]) / 8) * a for key, a in X.items()}
    return SY.add((1, D), (-mp.mpf(k.numerator) / (12 * k.denominator), SY.scal_vec(E2, X)))


PTS = np.array([0.1 + 0.9j, 1j, -0.3 + 1.2j, 0.45 + 1.6j, 2j])
ev = SY.np_eval


def vres(X, Y, s):
    xv, yv = ev(X)(PTS), ev(Y)(PTS)
    return float(np.max(np.abs(xv - complex(s) * yv)) / np.max(np.abs(xv)))


def per_exponent(X, Y, s, top=22):
    """relative deviation |X_k - s Y_k| / |X_k| by exponent; the first exponent where it exceeds 1e-6, and at 22"""
    out = {}
    for k in sorted(set(X) | set(Y), key=lambda z: z[1]):
        if k[1] > 8 * top: continue
        xk, yk = X.get(k, 0), Y.get(k, 0)
        if abs(xk) == 0: continue
        out[k] = float(abs(xk - s * yk) / abs(xk))
    first = min((k[1] / 8 for k, v in out.items() if v > 1e-6), default=None)
    worst_low = max((v for k, v in out.items() if k[1] <= 8 * 10), default=None)
    return first, worst_low, max(out.values())


F32, FM12 = [], []
for name, u in SY.MATTER:
    terms, r, line = SY.best_section(u, K32); F32.append(SY.to_series(terms, SY.E8))
    terms, r, line = SY.best_section(u, KM12); FM12.append(SY.to_series(terms, SY.E8))
    log("built", name, "3/2 and -1/2")
terms, r, line = SY.best_section((0, 1, 0), KM12); Rser = SY.to_series(terms, SY.E8)

res = {"I1": {}, "I2": {}, "I3": {}}
for j, ((name, u), l) in enumerate(zip(SY.MATTER, ("e_i", "v+", "v-"))):
    e0 = mp.mpf(UNIT8[l]) / 8
    s_struct = e0 + mp.mpf(1) / 24
    th1 = serre(FM12[j], KM12)
    unit = th1.get((l, UNIT8[l]))
    res["I1"][name] = {"s structural": float(s_struct), "theta F unit coefficient": complex(unit),
                       "value residual with the structural s": vres(th1, F32[j], s_struct),
                       "per exponent (first > 1e-6, worst <= 10, worst <= 22)": per_exponent(th1, F32[j], s_struct)}
    log("I1", name, res["I1"][name])

fbest = None
for line in SY.LINES:
    terms, r = RC.solve((0, 0, 0), K72, line)
    if fbest is None or r < fbest[1]: fbest = (terms, r, line)
fser = SY.to_series(fbest[0], SY.E8)
log("f built on", fbest[2], "f(e_i,1/8) =", complex(fser.get(("e_i", 1), 0)))
E4F = [SY.scal_vec(E4, F) for F in FM12]
for j, ((name, u), l) in enumerate(zip(SY.MATTER, ("e_i", "v+", "v-"))):
    terms, r = solve72(u, l); P = SY.to_series(terms, SY.E8)
    diff = SY.add((1, P), (-1, E4F[j]))
    a = diff.get(("e_i", 1), 0) / fser[("e_i", 1)]
    res["I2"][name] = {"alpha from (e_i,1/8)": complex(a), "value residual": vres(diff, fser, a),
                       "per exponent": per_exponent(diff, fser, a)}
    th2 = serre(serre(FM12[j], KM12), K32)
    u2 = th2[(l, UNIT8[l])]
    th2 = {k: v / u2 for k, v in th2.items()}
    d3 = SY.add((1, th2), (-1, E4F[j]))
    b_ = d3.get(("e_i", 1), 0) / fser[("e_i", 1)]
    res["I3"][name] = {"beta from (e_i,1/8)": complex(b_), "value residual": vres(d3, fser, b_),
                       "per exponent": per_exponent(d3, fser, b_)}
    log("I2/I3", name, res["I2"][name], res["I3"][name])

iso = SY.G_series(FM12[0], E4F[1], Rser); ref = SY.G_series(FM12[0], E4F[0], Rser)
iv, rv = ev(iso)(PTS), ev(ref)(PTS)
res["ISO values"] = float(np.max(np.abs(iv)) / np.max(np.abs(rv)))
rr = SY.dot_series(Rser, Rser)
res["R.R coefficients: max |.| at exponent <= 10, <= 22, all"] = [
    float(max((abs(v) for k, v in rr.items() if k <= 80), default=0)),
    float(max((abs(v) for k, v in rr.items() if k <= 176), default=0)), float(max(abs(v) for v in rr.values()))]
log("ISO", res["ISO values"], res["R.R coefficients: max |.| at exponent <= 10, <= 22, all"])
json.dump(res, open(sys.argv[2], "w"), indent=1, default=lambda z: [z.real, z.imag] if isinstance(z, complex) else str(z))
log("done")
