"""THE CRITICAL LINE (P-441; main's task A), the one script of CRITICAL_LINE_RULE.md (sealed be2d87e30).

Data-free: no measured number is read, and no height is set beside any datum.  The web seat, 2026-10-29.  0 of 19.

M1  the induced transfer operator L_(b,m) f(x) = sum_k e^(-m k) (k+x)^(-2b) f(1/(k+x)) on [0,1], barycentric Chebyshev
    collocation (B852's method); the sum direct to K0, the tail from the interpolant's value and slope at 0 against
    Euler-Maclaurin sums of e^(-m t)(t+x)^(-s); P(b) = the m with spectral radius 1.
M2  b* with P(b*) = b*.
M3  the equilibrium sampled by its backward chain (rejection from q(k) ~ e^(-m k) k^(-2b)); per run k the apex
    R = (a + x' + y)/2 and the flow time r = 2 log(a + x'); T_b(y) = sum 2 arccosh(R/y)_+ / sum r.
M4  monotonicity of the bin densities on [1, 6]; M5 the order in b; M6 the mean flow time per letter.
Controls C1-C6 and cells A1-A6 as the rule states them.

Run:  python3 critical_line.py --run > critical_line_out.txt   (writes critical_line.json beside it)
"""
import json, math, pathlib, sys, time
import numpy as np
import mpmath as mp
from scipy.optimize import brentq

HERE = pathlib.Path(__file__).resolve().parent
LOG2, PHI = math.log(2.0), (1 + 5 ** 0.5) / 2
TWO_LOG_PHI = 2 * math.log(PHI)
mp.mp.dps = 25


# ------------------------------------------------------------------------------------------------ M1: the operator
class Op:
    def __init__(self, N=40, K0=4000):
        self.N, self.K0 = N, K0
        j = np.arange(N)
        self.t = np.cos(np.pi * (2 * j + 1) / (2 * N))                 # Chebyshev-Gauss nodes on [-1, 1]
        self.x = (self.t + 1) / 2                                      # on [0, 1]
        self.bw = (-1.0) ** j * np.sin(np.pi * (2 * j + 1) / (2 * N))  # barycentric weights
        k = np.arange(1, K0 + 1, dtype=float)
        self.k = k
        Z = 1.0 / (k[None, :] + self.x[:, None])                       # N x K0 preimages
        self.B = self.rows(Z.ravel()).reshape(N, K0, N)                # interpolation rows at every preimage
        # value and slope at 0 of the interpolant, as rows (Chebyshev coefficients via the DCT of the nodal values)
        n = np.arange(N)
        C = np.cos(np.outer(n, np.arccos(self.t))) * (2.0 / N)         # c_n = (2/N) sum_j f_j T_n(t_j)
        C[0] /= 2
        self.r0 = ((-1.0) ** n) @ C                                    # f(0)  = sum c_n T_n(-1)
        self.r1 = (2.0 * (-1.0) ** (n + 1) * n ** 2) @ C               # f'(0) = 2 sum c_n T_n'(-1)

    def rows(self, z):
        z = np.atleast_1d(z)
        d = z[:, None] - self.x[None, :]
        hit = np.abs(d) < 1e-15
        d[hit] = 1.0
        w = self.bw[None, :] / d
        R = w / w.sum(axis=1, keepdims=True)
        if hit.any():
            ii, jj = np.nonzero(hit)
            R[ii] = 0.0
            R[ii, jj] = 1.0
        return R

    def tail_sums(self, b, m):
        """S_s(x) = sum_{k > K0} e^(-m k) (k + x)^(-s) for s = 2b and 2b + 1, by Euler-Maclaurin"""
        out = []
        a0 = self.K0 + 1
        for s in (2 * b, 2 * b + 1):
            vals = []
            for x in self.x:
                if m * a0 > 60:
                    vals.append(0.0); continue
                u = a0 + x
                if m == 0.0:
                    integral = mp.mpf(u) ** (1 - s) / (s - 1)
                else:
                    integral = mp.e ** (m * x) * mp.mpf(m) ** (s - 1) * mp.gammainc(1 - s, m * u)
                g = math.exp(-m * a0) * u ** (-s)
                gp = g * (-m - s / u)
                vals.append(float(integral) + g / 2 - gp / 12)
            out.append(np.array(vals))
        return out

    def matrix(self, b, m):
        W = np.exp(-m * self.k)[None, :] * (self.k[None, :] + self.x[:, None]) ** (-2 * b)
        M = np.einsum("ik,ikj->ij", W, self.B)
        if m * (self.K0 + 1) <= 60:
            S0, S1 = self.tail_sums(b, m)
            M += S0[:, None] * self.r0[None, :] + S1[:, None] * self.r1[None, :]
        return M

    def radius(self, b, m):
        ev = np.linalg.eigvals(self.matrix(b, m))
        return float(np.max(ev.real))

    def P(self, b):
        """the line: the m >= 0 with spectral radius 1 (0 if the radius at m = 0 is already <= 1)"""
        if b >= 1 - 1e-12:
            r0 = self.radius(b, 0.0)
            if r0 <= 1 + 1e-9: return 0.0, r0
        f = lambda m: self.radius(b, m) - 1.0
        lo, hi = (1e-12 if b > 0.5 else 0.0), max(2.0, 4.0 * abs(b) + 2.0)
        if b <= 0.5: lo = 1e-6
        while f(lo) < 0: lo /= 10
        m = brentq(f, lo, hi, xtol=1e-14, rtol=1e-13, maxiter=200)
        return m, self.radius(b, m)

    def eigfun(self, b, m):
        ev, V = np.linalg.eig(self.matrix(b, m))
        i = int(np.argmax(ev.real))
        v = V[:, i].real
        v = v / v[np.argmax(np.abs(v))]
        return v, float(ev[i].real)


# ------------------------------------------------------------------------------------------------ M3: the sampler
def sampler(op, b, m, h_nodes, n_chains, n_fwd, burn, rng, Kq=1_000_000):
    """two-sided run sequences from the equilibrium at (b, m); returns forward digits, x' and y per kept position"""
    hgrid = np.linspace(0, 1, 20001)
    hv = op.rows(hgrid) @ h_nodes
    assert hv.min() > 0, "h not positive"
    hmax = hv.max() * 1.0001
    k = np.arange(1, Kq + 1, dtype=float)
    q = np.exp(-m * k) * k ** (-2 * b)
    tail = 0.0
    if m == 0.0:                                              # beta = 1: Pareto tail beyond Kq, sum k^-2 ~ 1/Kq
        tail = 1.0 / Kq if b == 1.0 else 0.0
    cdf = np.cumsum(q); total = cdf[-1] + tail; cdf /= total

    def draw(n):
        u = rng.random(n)
        kk = np.searchsorted(cdf, u, side="right") + 1.0
        over = u >= cdf[-1]
        if over.any():                                         # the tail: P(k > t) ~ Kq/t
            kk[over] = np.floor(Kq / rng.random(int(over.sum()))) + 1.0
        return kk

    L = n_fwd + 2 * burn
    D = np.empty((n_chains, L))
    x = rng.random(n_chains)
    for t in range(L):
        kk = np.empty(n_chains); todo = np.arange(n_chains)
        while todo.size:
            prop = draw(todo.size)
            z = 1.0 / (prop + x[todo])
            acc = (1 + x[todo] / prop) ** (-2 * b) * (op.rows(z) @ h_nodes) / hmax
            assert acc.max() <= 1.0 + 1e-9
            ok = rng.random(todo.size) < acc
            kk[todo[ok]] = prop[ok]
            todo = todo[~ok]
        D[:, t] = kk
        x = 1.0 / (kk + x)
    F = D[:, ::-1]                                             # forward time
    Lf = F.shape[1]
    X = np.zeros((n_chains, Lf + 1))                           # X[:, j] = [0; F_j, F_(j+1), ...]
    for j in range(Lf - 1, -1, -1):
        X[:, j] = 1.0 / (F[:, j] + X[:, j + 1])
    Y = np.zeros((n_chains, Lf))                               # Y[:, j] = [0; F_(j-1), F_(j-2), ...]
    for j in range(1, Lf):
        Y[:, j] = 1.0 / (F[:, j - 1] + Y[:, j - 1])
    sl = slice(burn, burn + n_fwd)
    return F[:, sl], X[:, burn + 1:burn + n_fwd + 1], Y[:, sl]


YGRID = np.unique(np.round(np.concatenate([np.arange(1.0, 2.0, 0.01), np.arange(2.0, 4.0, 0.02),
                                           np.arange(4.0, 8.0 + 1e-9, 0.1)]), 6))


def tails(a, xp, y):
    R = ((a + xp + y) / 2).ravel()
    r = (2 * np.log(a + xp)).ravel()
    Rs = np.sort(R[R > 1.0])
    above = np.empty(len(YGRID))
    for i, yy in enumerate(YGRID):
        s = Rs[np.searchsorted(Rs, yy, side="right"):]
        above[i] = (2 * np.arccosh(s / yy)).sum()
    return above, r.sum(), a.sum(), Rs.size


# ------------------------------------------------------------------------------------------------ the run
def main():
    if "--run" not in sys.argv: raise SystemExit(__doc__)
    t0 = time.time(); out = {"rule": "be2d87e30"}
    op = Op(40, 4000); op2 = Op(52, 8000)
    print("THE CRITICAL LINE — one run of the sealed rule (be2d87e30)\n")

    # M1: the line, with convergence in N and K0
    grid = [-8, -4, -2, -1, -0.5] + [round(0.05 * i, 2) for i in range(21)] + [0.98, 0.99]
    line = {}
    for b in grid:
        m, rad = op.P(b); m2, _ = op2.P(b)
        line[b] = m
        out.setdefault("line", []).append({"beta": b, "P": m, "P_N52_K8000": m2, "radius": rad})
    print("M1  the line mu = P(beta)   [N=40, K0=4000 | N=52, K0=8000]")
    for e in out["line"]:
        print("    beta %6.2f  P = %.10f   (%.10f; diff %.1e)" % (e["beta"], e["P"], e["P_N52_K8000"], abs(e["P"] - e["P_N52_K8000"])))

    # controls C1-C4
    c1 = abs(line[0.0] - LOG2)
    r_gauss = op.radius(1.0, 0.0); c2 = abs(r_gauss - 1.0)
    b852 = {0.2: 0.53660, 0.5: 0.31124, 0.8: 0.10570}
    c3 = {b: line[b] - v for b, v in b852.items()}
    d = 1e-4
    dP0 = (op.P(d)[0] - op.P(-d)[0]) / (2 * d)
    c4 = abs(-dP0 - 0.7924)
    C = {"C1": c1 < 1e-9, "C2": c2 < 1e-8, "C3": all(abs(v) < 5e-5 for v in c3.values()), "C4": c4 < 1e-3}
    print("\nC1  P(0) - log 2 = %.2e  -> %s" % (line[0.0] - LOG2, C["C1"]))
    print("C2  radius at (1, 0) - 1 = %.2e  -> %s" % (r_gauss - 1, C["C2"]))
    print("C3  P - B852:  %s  -> %s" % (", ".join("P(%.1f) %+.1e" % (b, v) for b, v in c3.items()), C["C3"]))
    print("C4  -P'(0) = %.6f  (B1813: 0.7924)  -> %s" % (-dP0, C["C4"]))

    # M2: b*
    bstar = brentq(lambda b: op.P(b)[0] - b, 0.05, 0.95, xtol=1e-12)
    out["beta_star"] = bstar
    print("\nM2  beta* = %.10f   (P(beta*) = beta*);  A1 (beta* in (0.35, 0.45)): %s" % (bstar, 0.35 < bstar < 0.45))

    # M6 (analytic side): -P'(beta), the slope at -8, smoothness at 2 log phi
    mfpl = {}
    for b in [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95, 0.99]:
        mfpl[b] = -(op.P(b + d)[0] - op.P(b - d)[0]) / (2 * d)
    out["minus_dP"] = mfpl
    slope8 = -line[-8] / -8.0 * -1.0                           # -P(b)/b at b = -8
    slope8 = line[-8] / 8.0
    A4 = max(mfpl.values()) < TWO_LOG_PHI
    A5 = abs(slope8 / TWO_LOG_PHI - 1) < 0.02
    sd = {}
    for h in (0.02, 0.01, 0.005):
        Ps = [op.P(TWO_LOG_PHI + j * h)[0] for j in (-2, -1, 0, 1, 2)]
        sd[h] = [(Ps[i + 1] - 2 * Ps[i] + Ps[i - 1]) / h ** 2 for i in (1, 2, 3)]
    A6 = all(max(v) - min(v) < 0.05 * max(abs(x) for x in v) + 1e-3 for v in sd.values())
    out.update(slope_at_minus8=slope8, second_diffs_at_2logphi={str(k): v for k, v in sd.items()}, P_at_2logphi=op.P(TWO_LOG_PHI)[0])
    print("\nM6  -P'(beta) (mean flow time per letter): " + ", ".join("%.2f: %.5f" % (b, v) for b, v in mfpl.items()))
    print("    A4 (below 2 log phi = %.6f on [0, 1]): %s" % (TWO_LOG_PHI, A4))
    print("    -P(beta)/beta at beta = -8: %.6f  (%.2f%% from 2 log phi)  A5: %s" % (slope8, 100 * (slope8 / TWO_LOG_PHI - 1), A5))
    print("    P(2 log phi) = %.10f; second differences there: %s  A6 (no kink): %s" % (
        out["P_at_2logphi"], {k: ["%.5f" % x for x in v] for k, v in sd.items()}, A6))

    # M3-M5: the equilibrium's heights
    rng = np.random.default_rng(20261029)
    betas = sorted([0.0, 0.1, 0.2, bstar, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95, 1.0])
    NB, CH, FW, BURN = 8, 2000, 1500, 100
    res = {}
    for b in betas:
        m = 0.0 if b == 1.0 else op.P(b)[0]
        hn, lam = op.eigfun(b, m)
        blocks = []
        for blk in range(NB):
            a, xp, y = sampler(op, b, m, hn, CH, FW, BURN, rng)
            above, rsum, asum, nexc = tails(a, xp, y)
            blocks.append((above / rsum, rsum / asum, nexc))
        Tb = np.array([q[0] for q in blocks])
        res[b] = {"T": Tb.mean(0), "Tse": Tb.std(0, ddof=1) / math.sqrt(NB), "blocks": Tb,
                  "flow_per_letter": float(np.mean([q[1] for q in blocks])), "m": m, "lam": lam}
        print("\nM3  beta %.4f (mu %.6f, eigenvalue %.9f): T(1) %.5f, T(1.5) %.5f, T(2) %.5f, T(3) %.6f, T(6) %.2e; "
              "flow per letter %.5f  [%.0f s]" % (b, m, lam, *[res[b]["T"][np.argmin(abs(YGRID - v))] for v in (1, 1.5, 2, 3, 6)],
                                                   res[b]["flow_per_letter"], time.time() - t0))

    # C5, C6
    T1 = res[1.0]; sel = (YGRID >= 1) & (YGRID <= 6 + 1e-9)
    z5 = (T1["T"][sel] - 3 / (math.pi * YGRID[sel])) / T1["Tse"][sel]
    C["C5"] = bool(np.all(np.abs(z5) < 3))
    T0 = res[0.0]; ref = {1.5: 0.3829, 2.0: 0.1676, 3.0: 0.03462}
    z6 = {y: (T0["T"][np.argmin(abs(YGRID - y))] - v) / T0["Tse"][np.argmin(abs(YGRID - y))] for y, v in ref.items()}
    C["C6"] = all(abs(v) < 3 for v in z6.values())
    print("\nC5  beta = 1 against 3/(pi y) on [1, 6]: max |z| %.2f over %d grid points -> %s" % (np.abs(z5).max(), sel.sum(), C["C5"]))
    print("C6  beta = 0 against B1813's limit: %s -> %s" % (", ".join("T(%.1f) z %+.2f" % (y, v) for y, v in z6.items()), C["C6"]))

    # M4: monotonicity on [1, 6]
    w = np.diff(YGRID)
    A2 = True; mono = {}
    for b in betas:
        dens_blocks = -np.diff(res[b]["blocks"], axis=1) / w[None, :]
        keep = YGRID[:-1] < 6 - 1e-9
        Dm = dens_blocks[:, keep]
        dm = Dm.mean(0)
        worst, where = -np.inf, None
        for i in range(Dm.shape[1] - 1):
            diff = Dm[:, i + 1:] - Dm[:, [i]]
            se = diff.std(0, ddof=1) / math.sqrt(NB)
            zz = np.where(se > 0, diff.mean(0) / np.where(se > 0, se, 1), 0)
            j = int(np.argmax(zz))
            if zz[j] > worst: worst, where = float(zz[j]), (float(YGRID[i]), float(YGRID[i + 1 + j]))
        adj = (Dm[:, 1:] - Dm[:, :-1]); adjz = adj.mean(0) / (adj.std(0, ddof=1) / math.sqrt(NB))
        mono[b] = {"max_rise_z": worst, "at_bins": where, "max_adjacent_rise_z": float(adjz.max()),
                   "density_at_1": float(dm[0]), "argmax_density_y": float(YGRID[:-1][keep][int(np.argmax(dm))])}
        if worst > 3: A2 = False
    print("\nM4  monotonicity on [1, 6] (rule: no later bin's density above an earlier bin's by more than 3 SE):")
    for b in betas:
        e = mono[b]
        print("    beta %.4f: largest standardised rise %+.2f (bins at %.2f -> %.2f); largest adjacent %+.2f; density mode at y = %.2f"
              % (b, e["max_rise_z"], *e["at_bins"], e["max_adjacent_rise_z"], e["argmax_density_y"]))
    print("    A2 (every member monotone on [1, 6]): %s" % A2)

    # M5: the order in beta
    worst5 = np.inf; at5 = None
    for b1, b2 in zip(betas[:-1], betas[1:]):
        diff = res[b2]["blocks"] - res[b1]["blocks"]
        se = diff.std(0, ddof=1) / math.sqrt(NB)
        zz = diff.mean(0) / np.where(se > 0, se, np.inf)
        i = int(np.argmin(zz))
        if zz[i] < worst5: worst5, at5 = float(zz[i]), (b1, b2, float(YGRID[i]))
    A3 = worst5 > -3
    print("\nM5  order in beta on [1, 8]: smallest standardised step %+.2f (beta %.3f -> %.3f at y = %.2f); A3: %s" % (worst5, *at5, A3))

    # M6 (sample side)
    print("\nM6  flow time per letter, sample against -P'(beta):")
    for b in betas:
        dd = -(op.P(b + d)[0] - op.P(b - d)[0]) / (2 * d) if b < 1 else float("nan")
        print("    beta %.4f: sample %.5f, -P' %.5f" % (b, res[b]["flow_per_letter"], dd))

    cells = {"A1": 0.35 < bstar < 0.45, "A2": A2, "A3": A3, "A4": A4, "A5": A5, "A6": A6}
    print("\nCONTROLS: %s" % ", ".join("%s %s" % (k, "holds" if v else "FAILS") for k, v in C.items()))
    print("CELLS:    %s" % ", ".join("%s %s" % (k, "holds" if v else "fails") for k, v in cells.items()))
    out.update(controls=C, cells=cells, monotonicity={str(k): v for k, v in mono.items()},
               order_worst={"z": worst5, "at": at5},
               heights={str(b): {"y": YGRID.tolist(), "T": res[b]["T"].tolist(), "se": res[b]["Tse"].tolist(),
                                 "mu": res[b]["m"], "flow_per_letter": res[b]["flow_per_letter"]} for b in betas})
    (HERE / "critical_line.json").write_text(json.dumps(out, default=float, indent=1))
    print("\n[%.0f s]" % (time.time() - t0))


if __name__ == "__main__":
    main()
