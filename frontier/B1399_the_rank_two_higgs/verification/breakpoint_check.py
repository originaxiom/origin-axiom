"""B1399 design time: the breakpoint reduction checked on SYNTHETIC shells -- no census member, no harmonic form.

F_theta = cos(theta) g1 + sin(theta) g2 on the torus, g_i = sum_j Re(c_ij e^{2 pi i k_j . x}); chi(theta) = chi({F_theta > 0}) by B1386's
Morse count.  The claims sealed in PREREGISTRATION.md:
  - chi changes only at theta = psi(x) +- pi/2, x a critical point of the angle map psi = arg(g1 + i g2);
  - at psi + pi/2 a saddle of psi raises chi by one and an extremum lowers it; at psi - pi/2 the reverse;
  - the zeros of h = g1 grad g2 - g2 grad g1 have indices summing to zero, the common zeros of (g1, g2) index +1 (completeness);
  - a shell of two directions gives chi = 0 in every direction (separable: {F > 0} is a band).
Every claim is checked against the Morse count on a grid of directions (farther than 2e-3 from a breakpoint)."""
import importlib.util
import math
import sys
import time
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")
import numpy as np

ROOT = Path(__file__).resolve().parents[3]
spec = importlib.util.spec_from_file_location("b1386_the_open_cusp", ROOT / "frontier" / "B1386_the_open_eisenstein_cusp" / "verification" / "the_open_cusp.py")
T = importlib.util.module_from_spec(spec)
spec.loader.exec_module(T)
TWO_PI = 2 * np.pi


def fields(K, c, X):
    """g = sum_j Re(c_j e^{2 pi i k_j x}), its gradient and Hessian at the points X (n x 2)"""
    E = c[None, :] * np.exp(1j * TWO_PI * (X @ K.T))
    g = np.real(E.sum(1))
    dg = np.real((1j * TWO_PI) * (E @ K))
    KK = np.einsum("ja,jb->jab", K, K)
    H = np.real(-(TWO_PI ** 2) * np.einsum("nj,jab->nab", E, KK))
    return g, dg, H


def h_and_Dh(K, a, b, X):
    g1, d1, H1 = fields(K, a, X)
    g2, d2, H2 = fields(K, b, X)
    h = g1[:, None] * d2 - g2[:, None] * d1
    Dh = (np.einsum("ni,nj->nij", d2, d1) - np.einsum("ni,nj->nij", d1, d2)
          + g1[:, None, None] * H2 - g2[:, None, None] * H1)
    return h, Dh, g1, g2


def zeros_of_h(K, a, b, seeds):
    """damped Newton on h = 0 from a seeds x seeds grid, deduplicated modulo the lattice"""
    g = (np.arange(seeds) + 0.5) / seeds
    X = np.array([(s, t) for s in g for t in g])
    for _ in range(80):
        h, Dh, _, _ = h_and_Dh(K, a, b, X)
        ok = np.abs(np.linalg.det(Dh)) > 1e-14
        step = np.zeros_like(X)
        step[ok] = np.linalg.solve(Dh[ok], h[ok][:, :, None])[:, :, 0]
        n = np.linalg.norm(step, axis=1)
        step *= np.minimum(1, 0.05 / np.maximum(n, 1e-300))[:, None]
        X = (X - step) % 1.0
    h = h_and_Dh(K, a, b, X)[0]
    scale = np.max(np.abs(h_and_Dh(K, a, b, np.random.default_rng(0).random((4000, 2)))[0]))
    pts = []
    for x in X[np.linalg.norm(h, axis=1) < 1e-9 * scale]:
        if not any(np.allclose((x - p + 0.5) % 1.0 - 0.5, 0, atol=1e-6) for p in pts):
            pts.append(x)
    return np.array(pts).reshape(-1, 2)


def breakpoints(K, a, b):
    """[(theta, jump)] from the critical points of psi; the index sum; the number of common zeros; the seeds used"""
    for seeds in (64, 128, 256):
        P = zeros_of_h(K, a, b, seeds)
        h, Dh, g1, g2 = h_and_Dh(K, a, b, P)
        rho = np.hypot(g1, g2)
        rmax = np.max(np.hypot(*h_and_Dh(K, a, b, np.random.default_rng(1).random((4000, 2)))[2:]))
        idx = np.sign(np.linalg.det(Dh))
        common = rho < 1e-7 * rmax
        if idx.sum() == 0 and np.all(idx[common] == 1):
            break
    out = []
    for r, d, G1, G2 in zip(rho, idx, g1, g2):
        if r < 1e-7 * rmax:
            continue
        psi = math.atan2(G2, G1)
        saddle = d < 0
        out.append(((psi + math.pi / 2) % (2 * math.pi), +1 if saddle else -1))
        out.append(((psi - math.pi / 2) % (2 * math.pi), -1 if saddle else +1))
    return sorted(out), int(idx.sum()), int(common.sum()), seeds


def chi_theta(K, a, b, th):
    c = math.cos(th) * a + math.sin(th) * b
    terms = []
    for k, z in zip(K, c):
        terms += [(z / 2, (int(k[0]), int(k[1]))), (np.conj(z) / 2, (-int(k[0]), -int(k[1])))]
    chi, complete, gap, _ = T.morse_chi(terms)
    assert complete
    return chi


def main(NG=720):
    rng = np.random.default_rng(1399 + 7)
    cases = [np.array([(1, 0), (0, 1), (1, 1)]), np.array([(1, 0), (0, 1)]),
             np.array([(2, 1), (1, 2), (1, -1), (3, 0), (0, 3), (3, 3)])]
    bad = 0
    for K in cases:
        for rep in range(2):
            a = rng.normal(size=len(K)) + 1j * rng.normal(size=len(K))
            b = rng.normal(size=len(K)) + 1j * rng.normal(size=len(K))
            t0 = time.time()
            grid = np.arange(NG) * 2 * math.pi / NG + 1e-4
            if len(K) <= 2:
                vals = sorted(set(chi_theta(K, a, b, th) for th in grid))
                bad += vals != [0]
                print("shell of %d directions, rep %d: chi over %d directions takes %s (the two-direction rule: [0])" % (len(K), rep, NG, vals), flush=True)
                continue
            bps, isum, ncommon, seeds = breakpoints(K, a, b)
            ts = sorted(set(round(t, 9) for t, _ in bps))
            gmax, gi = max(((ts[(i + 1) % len(ts)] - ts[i]) % (2 * math.pi), i) for i in range(len(ts)))
            th0 = (ts[gi] + gmax / 2) % (2 * math.pi)
            base = chi_theta(K, a, b, th0)

            def predicted(th):
                return base + sum(j for t, j in bps if (t - th0) % (2 * math.pi) < (th - th0) % (2 * math.pi))

            mism = [round(float(th), 4) for th in grid
                    if min(abs(((th - t) + math.pi) % (2 * math.pi) - math.pi) for t, _ in bps) >= 2e-3
                    and chi_theta(K, a, b, th) != predicted(th)]
            bad += len(mism) + (isum != 0)
            print("shell of %d directions, rep %d: %d breakpoints, index sum %d, %d common zeros, %d seeds per side, net jump %d; "
                  "grid of %d: %d mismatches %s (%.0f s)" % (len(K), rep, len(bps), isum, ncommon, seeds, sum(j for _, j in bps), NG,
                                                          len(mism), mism[:5], time.time() - t0), flush=True)
    print("TOTAL FAILURES", bad)
    return bad


if __name__ == "__main__":
    sys.exit(1 if main(int(sys.argv[1]) if len(sys.argv) > 1 else 720) else 0)
