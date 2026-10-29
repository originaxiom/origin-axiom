"""THE CRITICAL LINE, POST HOC (labelled): resolving the failed control C5 and reading A2 and A6 further, after the one
run's output (ac6d0c6bc) was committed and read.  Data-free.  The web seat, 2026-10-29.  0 of 19.

P1  C5 (beta = 1 against 3/(pi y)): the run's z-profile (mean, rms, count beyond 3, largest relative deviation), and a
    fresh sample at beta = 1 with 24 blocks (23 degrees of freedom for each standard error) on the same grid.
P2  A2's two flagged members:
    beta = 0: exact two-sided i.i.d. Geometric(1/2) runs (no chain), 10^8 runs in 20 independent blocks: the tail T on a
              fine grid around the flagged bins (1.80-2.00 by 0.01; 3.70-4.00 by 0.02) and over [1, 6]; the bin
              densities; the apex density N on the same bins (does N itself rise there?);
    beta = 0.1: a fresh sample from the run's sampler, 24 blocks of 2000 chains, the same grid as the run.
    For each, the run's rule (a later bin above an earlier one by more than 3 SE) and the adjacent-bin rises, with
    their sizes relative to the density.
P3  A6: the second differences of P on beta in [0.80, 0.97] at h = 0.0025, to show whether anything happens at
    2 log phi beside the growth toward beta = 1 (the h = 0.02 stencil of the run reached 1.002, past the transition).
"""
import importlib.util, json, math, pathlib, sys, time
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("cl", HERE / "critical_line.py")
cl = importlib.util.module_from_spec(spec); spec.loader.exec_module(cl)
RUN = json.loads((HERE / "critical_line.json").read_text())
Y = cl.YGRID


def rises(blocks, Y, ylo=1.0, yhi=6.0):
    nb = blocks.shape[0]
    w = np.diff(Y)
    D = -np.diff(blocks, axis=1) / w[None, :]
    keep = (Y[:-1] >= ylo - 1e-9) & (Y[:-1] < yhi - 1e-9)
    D = D[:, keep]; yb = Y[:-1][keep]
    worst, where = -np.inf, None
    for i in range(D.shape[1] - 1):
        diff = D[:, i + 1:] - D[:, [i]]
        se = diff.std(0, ddof=1) / math.sqrt(nb)
        z = np.where(se > 0, diff.mean(0) / np.where(se > 0, se, 1), 0)
        j = int(np.argmax(z))
        if z[j] > worst: worst, where = float(z[j]), (float(yb[i]), float(yb[i + 1 + j]), float(diff.mean(0)[j] / D.mean(0)[i]))
    adj = D[:, 1:] - D[:, :-1]
    adjz = adj.mean(0) / (adj.std(0, ddof=1) / math.sqrt(nb))
    k = int(np.argmax(adjz))
    return {"max_rise_z": worst, "bins": where[:2], "rise_over_density": where[2],
            "max_adjacent_z": float(adjz[k]), "adjacent_at": float(yb[k + 1]),
            "adjacent_rise_over_density": float(adj.mean(0)[k] / D.mean(0)[k]),
            "n_adjacent_above_3": int((adjz > 3).sum()), "n_bins": int(D.shape[1])}


def main():
    if "--run" not in sys.argv: raise SystemExit(__doc__)
    t0 = time.time(); out = {}
    print("THE CRITICAL LINE, POST HOC (labelled; after the run's output ac6d0c6bc was committed and read)\n")

    # P1a: the run's z-profile at beta = 1
    h = RUN["heights"]["1.0"]; T = np.array(h["T"]); se = np.array(h["se"])
    sel = (Y >= 1) & (Y <= 6 + 1e-9); ex = 3 / (math.pi * Y[sel])
    z = (T[sel] - ex) / se[sel]; rel = T[sel] / ex - 1
    print("P1a the run at beta = 1: mean z %+.2f, rms z %.2f, |z| > 3 at %d of %d points, max |z| %.2f; "
          "largest relative deviation %.2e" % (z.mean(), math.sqrt((z ** 2).mean()), int((abs(z) > 3).sum()), sel.sum(),
                                               abs(z).max(), abs(rel).max()))
    out["P1a"] = {"mean_z": float(z.mean()), "rms_z": float(math.sqrt((z ** 2).mean())), "n_beyond_3": int((abs(z) > 3).sum()),
                  "max_abs_z": float(abs(z).max()), "max_rel_dev": float(abs(rel).max())}

    op = cl.Op(40, 4000)
    rng = np.random.default_rng(29102026)

    def fresh(b, nblocks):
        m = 0.0 if b == 1.0 else op.P(b)[0]
        hn, _ = op.eigfun(b, m)
        blocks = []
        for _ in range(nblocks):
            a, xp, y = cl.sampler(op, b, m, hn, 2000, 1500, 100, rng)
            above, rsum, asum, n = cl.tails(a, xp, y)
            blocks.append(above / rsum)
        return np.array(blocks)

    # P1b: fresh beta = 1, 24 blocks
    B1 = fresh(1.0, 24)
    T1 = B1.mean(0); se1 = B1.std(0, ddof=1) / math.sqrt(24)
    z1 = (T1[sel] - ex) / se1[sel]
    print("P1b fresh beta = 1 (24 blocks): mean z %+.2f, rms z %.2f, |z| > 3 at %d of %d, max |z| %.2f; largest relative "
          "deviation %.2e  [%.0f s]" % (z1.mean(), math.sqrt((z1 ** 2).mean()), int((abs(z1) > 3).sum()), sel.sum(),
                                        abs(z1).max(), abs(T1[sel] / ex - 1).max(), time.time() - t0))
    out["P1b"] = {"mean_z": float(z1.mean()), "rms_z": float(math.sqrt((z1 ** 2).mean())), "n_beyond_3": int((abs(z1) > 3).sum()),
                  "max_abs_z": float(abs(z1).max()), "max_rel_dev": float(abs(T1[sel] / ex - 1).max()),
                  "rises": rises(B1, Y)}
    print("    its monotonicity read-out: %s" % out["P1b"]["rises"])

    # P2a: beta = 0 exact, 1e8 runs in 20 blocks
    FINE = np.unique(np.round(np.concatenate([np.arange(1.0, 1.8, 0.01), np.arange(1.80, 2.0001, 0.005),
                                              np.arange(2.0, 3.7, 0.02), np.arange(3.70, 4.0001, 0.01),
                                              np.arange(4.0, 6.0001, 0.05)]), 6))
    def cf(n, depth=40):
        v = np.zeros(n)
        for _ in range(depth):
            v = 1.0 / (rng.geometric(0.5, n) + v)
        return v
    blocks0, apex = [], []
    edges = FINE
    for blk in range(20):
        num = np.zeros(len(FINE)); den = 0.0; hist = np.zeros(len(edges) - 1)
        for _ in range(10):
            n = 500_000
            a = rng.geometric(0.5, n).astype(float); xp = cf(n); yy = cf(n)
            R = (a + xp + yy) / 2; den += (2 * np.log(a + xp)).sum()
            Rs = np.sort(R[R > 1.0])
            for i, yv in enumerate(FINE):
                s = Rs[np.searchsorted(Rs, yv, side="right"):]
                num[i] += (2 * np.arccosh(s / yv)).sum()
            hist += np.histogram(R, bins=edges)[0]
        blocks0.append(num / den); apex.append(hist / den / np.diff(edges))
    B0 = np.array(blocks0); A0 = np.array(apex)
    r0 = rises(B0, FINE)
    Nd = A0.mean(0); Nse = A0.std(0, ddof=1) / math.sqrt(20)
    adjN = (A0[:, 1:] - A0[:, :-1]); adjNz = adjN.mean(0) / (adjN.std(0, ddof=1) / math.sqrt(20))
    print("\nP2a beta = 0 exact (10^8 runs, 20 blocks): T(1.5) %.5f, T(2) %.5f, T(3) %.6f" % tuple(
        B0.mean(0)[np.argmin(abs(FINE - v))] for v in (1.5, 2.0, 3.0)))
    print("    height-density rises: %s" % r0)
    print("    the apex density N: adjacent rises beyond 3 SE at %d of %d bins; largest at R = %.3f (z %+.1f)  [%.0f s]" % (
        int((adjNz > 3).sum()), len(adjNz), FINE[1:-1][int(np.argmax(adjNz))], adjNz.max(), time.time() - t0))
    win = (FINE[:-1] >= 1.80) & (FINE[:-1] < 2.0)
    print("    N on [1.80, 2.00) (per unit flow time and unit R): " + ", ".join("%.3f:%.4f" % (r, v) for r, v in zip(FINE[:-1][win], Nd[win])))
    D0 = (-np.diff(B0, axis=1) / np.diff(FINE)[None, :]).mean(0)
    print("    height density on [1.80, 2.00): " + ", ".join("%.3f:%.4f" % (r, v) for r, v in zip(FINE[:-1][win], D0[win])))
    out["P2a"] = {"rises": r0, "N_adjacent_above_3": int((adjNz > 3).sum()),
                  "N_window": {"%.3f" % r: float(v) for r, v in zip(FINE[:-1][win], Nd[win])},
                  "density_window": {"%.3f" % r: float(v) for r, v in zip(FINE[:-1][win], D0[win])}}

    # P2b: beta = 0.1 fresh, 24 blocks
    Bb = fresh(0.1, 24)
    rb = rises(Bb, Y)
    print("\nP2b fresh beta = 0.1 (24 blocks): %s  [%.0f s]" % (rb, time.time() - t0))
    out["P2b"] = rb

    # P3: second differences of P near 2 log phi
    hh = 0.0025
    bs = np.arange(0.80, 0.97 + 1e-9, 0.01)
    sd = []
    for b in bs:
        Pm, P0, Pp = (op.P(b + k * hh)[0] for k in (-1, 0, 1))
        sd.append((Pp - 2 * P0 + Pm) / hh ** 2)
    print("\nP3  P'' (h = %.4f) on [0.80, 0.97]: %s" % (hh, ", ".join("%.2f:%.3f" % (b, v) for b, v in zip(bs, sd))))
    print("    2 log phi = %.6f lies between %.2f and %.2f" % (cl.TWO_LOG_PHI, bs[bs < cl.TWO_LOG_PHI][-1], bs[bs > cl.TWO_LOG_PHI][0]))
    out["P3"] = {"%.2f" % b: v for b, v in zip(bs, sd)}
    (HERE / "critical_line_posthoc.json").write_text(json.dumps(out, default=float, indent=1))
    print("\n[%.0f s]" % (time.time() - t0))


if __name__ == "__main__":
    main()
