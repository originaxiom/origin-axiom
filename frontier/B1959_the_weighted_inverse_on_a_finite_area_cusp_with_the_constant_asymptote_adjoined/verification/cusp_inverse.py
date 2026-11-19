"""B1959: the weighted inverse of a Laplace-type operator on a finite-area hyperbolic cusp, with the constant asymptote
adjoined.  The computable steps of the proof in FINDINGS.md, each checked here; K4 and K7 with a control that breaks them
(corrected 2026-11-19 at Review 85: this line said each step had one; K2, K5 and K6 have none).
Main's own code; nothing of any seat's is run.  Light: one-dimensional solves on grids.
 K1  the channel operator: on exp(i m x) with D_x = d/dx + i (w/2) exp(-t), -exp(2t) D_x^2 is (m exp(t) + w/2)^2: a
     perfect square, equal to w^2/4 at m = 0.
 K2  with u = exp(t/2) v the operator -u'' + u' is exp(t/2) (-v'' + v/4), and the norm of u against exp(-t) dt is the
     plain norm of v: the zero-frequency channel is -d^2/dt^2 + 1/4 + ell^2 c, so its spectrum starts at
     c + 1/(4 ell^2).  Numerically: the count of eigenvalues below the threshold does not change with the cut.
 K3  with u = exp(-delta t) W: -u'' + u' + V u = exp(-delta t) [-W'' + (1 + 2 delta) W' + (V - delta - delta^2) W],
     and V = ell^2 c exceeds delta + delta^2 exactly when delta < beta_c.
 K4  zero frequency, c > 0: for |f| <= exp(-delta t), the decaying solution obeys
     sup exp(delta t)|u| <= max(|u(0)|, ell^2/(ell^2 c - delta - delta^2)).  Control: a weight beyond beta_c fails.
 K5  zero frequency, c = 0: u' = ell^2 exp(t) int_t^oo exp(-s) f and u = a - int_t^oo u'; bounds ell^2/(1 + delta)
     and ell^2/(delta (1 + delta)).
 K6  non-zero frequencies: N = (sum_m |u_m|^2)^(1/2) obeys -N'' + N' + K N <= ell^2 F with K = min_m V_m, and so
     N(t) <= N(T1) exp(-beta_1 (t - T1)) + ell^2 F0 exp(-delta t)/(K1 - delta - delta^2).
 K7  a whole surface (a cap closed onto the cusp), the channel of the kernel: for a decaying source orthogonal to the
     constants the solution orthogonal to the constants is a constant a plus a decaying part, a is fixed by the
     source, and it is not zero: the decaying space alone is not enough (the control)."""
import functools, math
import numpy as np
import sympy as sp
print = functools.partial(print, flush=True)
rng = np.random.default_rng(1959)

def solve_tri(lo, di, up, rhs):
    """a tridiagonal system by elimination"""
    n = len(di); c = np.zeros(n, dtype=complex); d = np.zeros(n, dtype=complex); c[0] = up[0] / di[0]; d[0] = rhs[0] / di[0]
    for i in range(1, n):
        den = di[i] - lo[i] * c[i - 1]; c[i] = (up[i] / den) if i < n - 1 else 0; d[i] = (rhs[i] - lo[i] * d[i - 1]) / den
    x = np.zeros(n, dtype=complex); x[-1] = d[-1]
    for i in range(n - 2, -1, -1): x[i] = d[i] - c[i] * x[i + 1]
    return x

def mode_solve(V, src, t, left, right=0.0):
    """-u'' + u' + V u = src on the grid t, u(t_0) = left, u(t_end) = right"""
    h = t[1] - t[0]; n = len(t); lo = np.full(n, -1 / h ** 2 - 1 / (2 * h), dtype=complex); up = np.full(n, -1 / h ** 2 + 1 / (2 * h), dtype=complex); di = 2 / h ** 2 + V.astype(complex)
    rhs = src.astype(complex).copy(); di[0] = di[-1] = 1; up[0] = 0; lo[-1] = 0; rhs[0] = left; rhs[-1] = right
    return solve_tri(lo, di, up, rhs)

def smooth_noise(t, k=6):
    g = sum(rng.normal() * np.sin(rng.uniform(0.3, 3) * t + rng.uniform(0, 6.28)) for _ in range(k)); return g / np.max(np.abs(g))

if __name__ == "__main__":
    t, x, w, m, d, c, ell = sp.symbols("t x w m delta c ell", real=True); u = sp.Function("u"); v = sp.Function("v"); W = sp.Function("W"); Vs = sp.Symbol("V")
    Dx = lambda g: sp.diff(g, x) + sp.I * (w / 2) * sp.exp(-t) * g; e = sp.exp(sp.I * m * x)
    k1 = sp.simplify(-sp.exp(2 * t) * Dx(Dx(e)) / e - (m * sp.exp(t) + w / 2) ** 2)
    print("K1: -exp(2t) D_x^2 on exp(i m x), minus (m exp(t) + w/2)^2: %s; at m = 0 it is %s" % (k1, sp.simplify((-sp.exp(2 * t) * Dx(Dx(e)) / e).subs(m, 0))))
    uu = sp.exp(t / 2) * v(t); k2 = sp.simplify((-sp.diff(uu, t, 2) + sp.diff(uu, t)) / sp.exp(t / 2) - (-sp.diff(v(t), t, 2) + v(t) / 4))
    uw = sp.exp(-d * t) * W(t); k3 = sp.simplify((-sp.diff(uw, t, 2) + sp.diff(uw, t) + Vs * uw) * sp.exp(d * t) - (-sp.diff(W(t), t, 2) + (1 + 2 * d) * sp.diff(W(t), t) + (Vs - d - d ** 2) * W(t)))
    b = (sp.sqrt(1 + 4 * ell ** 2 * c) - 1) / 2
    print("K2: the conjugation by exp(t/2): remainder %s.  K3: the conjugation by exp(-delta t): remainder %s; beta^2 + beta - ell^2 c = %s" % (k2, k3, sp.simplify(b ** 2 + b - ell ** 2 * c)))
    L, cc, dl = 1.5, 0.4, 0.3; V0 = L * L * cc; beta = (math.sqrt(1 + 4 * V0) - 1) / 2
    counts = []
    for Tm in (30.0, 60.0):
        tt = np.linspace(0, Tm, int(Tm * 40) + 1); h = tt[1] - tt[0]; n = len(tt)
        H = np.diag(np.full(n, 2 / h ** 2 + 0.25 + V0)) + np.diag(np.full(n - 1, -1 / h ** 2), 1) + np.diag(np.full(n - 1, -1 / h ** 2), -1); H[0, 0] = 1 / h ** 2 + 0.25 + V0 - 0.5 / h   # the condition u' = 0 at the cut, as v' = -v/2
        ev = np.linalg.eigvalsh(H); counts.append((int(np.sum(ev < 0.25 + V0 - 1e-9)), float(ev[0])))
    print("K2, numerically (ell^2 c = %.2f, threshold %.4f): eigenvalues below the threshold with the cut at 30 and at 60: %d and %d; the lowest %.4f and %.4f" % (V0, 0.25 + V0, counts[0][0], counts[1][0], counts[0][1], counts[1][1]))
    tt = np.linspace(0, 40, 16001); worst = 0; bound = max(1.0, L * L / (V0 - dl - dl * dl))
    for _ in range(40):
        f = np.exp(-dl * tt) * smooth_noise(tt); u0 = rng.uniform(-1, 1); uu_ = mode_solve(np.full(len(tt), V0), L * L * f, tt, u0).real
        worst = max(worst, float(np.max(np.exp(dl * tt[tt < 30]) * np.abs(uu_[tt < 30]))))
    d2 = 0.8; f = np.exp(-d2 * tt) * smooth_noise(tt); uu_ = mode_solve(np.full(len(tt), V0), L * L * f, tt, 1.0).real
    print("K4: beta_c = %.4f, delta = %.2f: over 40 sources the largest sup of exp(delta t)|u| is %.3f, the bound %.3f; the control delta = %.2f > beta_c: exp(delta t)|u| at t = 10, 20, 30: %.1f, %.1f, %.1f (grows)"
          % (beta, dl, worst, bound, d2, *[float(np.exp(d2 * T) * abs(uu_[np.searchsorted(tt, T)])) for T in (10, 20, 30)]))
    tt = np.linspace(0, 30, 30001); h = tt[1] - tt[0]; wmax = umax = 0
    for _ in range(20):
        f = np.exp(-dl * tt) * smooth_noise(tt); g = np.exp(-tt) * f; tail = np.concatenate([np.cumsum((g[::-1][:-1] + g[::-1][1:]) / 2 * h)[::-1], [0.0]]); wv = L * L * np.exp(tt) * tail
        tw = np.concatenate([np.cumsum((wv[::-1][:-1] + wv[::-1][1:]) / 2 * h)[::-1], [0.0]]); sel = tt < 20
        wmax = max(wmax, float(np.max(np.exp(dl * tt[sel]) * np.abs(wv[sel])))); umax = max(umax, float(np.max(np.exp(dl * tt[sel]) * np.abs(tw[sel]))))
    print("K5: c = 0: the largest sup of exp(delta t)|u'| is %.4f (bound ell^2/(1 + delta) = %.4f) and of exp(delta t)|u - a| %.4f (bound ell^2/(delta (1 + delta)) = %.4f)" % (wmax, L * L / (1 + dl), umax, L * L / (dl * (1 + dl))))
    wt, mu, nu = 3.0, 0.2, 0.3; ms = [n_ + nu for n_ in (-2, -1, 1, 2)]; T1 = math.log(wt / min(abs(q) for q in ms)); tt = np.linspace(0, 7.0, 28001); h = tt[1] - tt[0]
    Vm = [(q * np.exp(tt) + wt / 2) ** 2 + L * L * mu for q in ms]; K = np.min(np.array(Vm), axis=0); worstR = -1e9; worstB = 0; okK = float(np.min(K[tt >= T1] - (min(abs(q) for q in ms) ** 2) * np.exp(2 * tt[tt >= T1]) / 4))
    for _ in range(12):
        fs = [np.exp(-dl * tt) * smooth_noise(tt) * 0.5 * np.exp(1j * rng.uniform(0, 6.28)) for _ in ms]; us = [mode_solve(Vq, L * L * fq, tt, rng.normal() + 1j * rng.normal()) for Vq, fq in zip(Vm, fs)]
        N = np.sqrt(sum(np.abs(q) ** 2 for q in us)); F = np.sqrt(sum(np.abs(q) ** 2 for q in fs)); i1 = np.searchsorted(tt, T1); sel = slice(i1 + 2, len(tt) - 4000)
        N2 = (N[2:] - 2 * N[1:-1] + N[:-2]) / h ** 2; N1 = (N[2:] - N[:-2]) / (2 * h); R = (-N2 + N1 + K[1:-1] * N[1:-1] - L * L * F[1:-1])[sel]; pos = N[1:-1][sel] > 1e-9
        worstR = max(worstR, float(np.max(R[pos] / (1 + K[1:-1][sel][pos] * N[1:-1][sel][pos])))); K1 = float(K[i1]); b1 = (math.sqrt(1 + 4 * K1) - 1) / 2; F0 = float(np.max(np.exp(dl * tt) * F))
        cmp_ = N[i1] * np.exp(-b1 * (tt - T1)) + L * L * F0 * np.exp(-dl * tt) / (K1 - dl - dl * dl); worstB = max(worstB, float(np.max((N / cmp_)[i1:len(tt) - 4000])))
    print("K6: frequencies %s, weight %.0f: beyond T1 = %.3f the least potential minus m0^2 exp(2t)/4 is at least %.3f; over 12 sources the largest of (-N'' + N' + K N - ell^2 F)/(1 + K N) is %.1e (not positive, up to the grid); the largest N over its comparison function is %.4f (at most 1)"
          % ([round(q, 1) for q in ms], wt, T1, okK, worstR, worstB))
    R0 = 3 * math.pi / 4; Tm = 22.0; n = 49001; tt = np.linspace(-R0, Tm, n); h = tt[1] - tt[0]; mid = (tt[:-1] + tt[1:]) / 2
    phi = np.where(tt < 0, math.sqrt(2) * np.sin(tt + R0), np.exp(-tt)); pm = np.where(mid < 0, math.sqrt(2) * np.sin(mid + R0), np.exp(-mid)); cell = np.full(n, h); cell[0] = cell[-1] = h / 2
    wgt = np.maximum(phi, 0) * cell; wgt[0] = pm[0] * h / 4; area = float(np.sum(wgt)); bump = np.where(tt < 0, np.sin(np.pi * np.clip(-tt / R0, 0, 1)) ** 2, 0.0); cusp = tt >= 0; As = []; ratios = []; plain = []
    def solve(src):
        """the scheme sum of phi_mid (u_i - u_j)^2 / h, solved exactly: the flux phi u' is minus the running integral of the source"""
        uu_ = np.concatenate([[0.0], np.cumsum(-np.cumsum(src * wgt)[:-1] / pm * h)]); return uu_ - np.sum(uu_ * wgt) / area
    for _ in range(16):
        f = np.where(cusp, np.exp(-dl * np.maximum(tt, 0)), 1.0) * smooth_noise(tt); f = f - bump * np.sum(f * wgt) / np.sum(bump * wgt)   # orthogonal to the constants by a bump in the cap, so the decay is kept
        uu_ = solve(f); a = float(uu_[-1]); As.append(a); fsup = float(np.max(np.where(cusp, np.exp(dl * np.maximum(tt, 0)), 1.0) * np.abs(f))); fc = float(np.max(np.exp(dl * tt[cusp]) * np.abs(f[cusp])))
        dec = float(np.max(np.exp(dl * tt[cusp]) * np.abs(uu_[cusp] - a))); ratios.append(((abs(a) + dec) / fsup, dec / fc))
        g = f + 0.2 * cusp; g = g - bump * np.sum(g * wgt) / np.sum(bump * wgt); u2 = solve(g); plain.append(float(abs(u2[np.searchsorted(tt, 20.0)] - u2[np.searchsorted(tt, 10.0)])))   # the control: a source orthogonal to the constants that does not decay
    print("K7: a cap closed onto the cusp (area per unit of x: %.4f, exact sqrt 2 + 2 = %.4f); over 16 sources orthogonal to the constants: the constant a ranges over [%.3f, %.3f] (not zero: the decaying space alone misses these sources); the largest (|a| + sup exp(delta t)|u - a|)/sup exp(delta t)|f| is %.3f; the largest of sup exp(delta t)|u - a| over the cusp's sup exp(delta t)|f| is %.3f (bound 1/(delta (1 + delta)) = %.3f); the control, a source orthogonal to the constants with 0.2 left on the cusp: u changes by %.3f to %.3f between t = 10 and 20 (it grows like 0.2 t: no constant tail)"
          % (area, math.sqrt(2) + 2, min(As), max(As), max(r[0] for r in ratios), max(r[1] for r in ratios), 1 / (dl * (1 + dl)), min(plain), max(plain)))
