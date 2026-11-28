#!/usr/bin/env python3
"""Banking seat V1 (fam1-v1-unset-04), Q0014: an own recomputation, sharing nothing with the producer's code.
(F_s f)(x) = (1 + x)^(-2s) [f(x/(1 + x)) + f(1/(1 + x))] on [0, 1], discretised by a Nystrom-style matrix on
Gauss-Legendre nodes with barycentric interpolation (not Chebyshev collocation), at M = 100, 200 and 300 nodes; lambda_1
the eigenvalue of largest modulus, h_s its eigenvector read on 2001 points; the mass on [0, 0.05] by Gauss-Legendre
quadrature of the interpolant; a discretisation-free check of lambda_1 by the word sums Z_18 / Z_17.
    python3 relays/claims/banking/q0014_own.py                    the decisive run
    python3 relays/claims/banking/q0014_own.py --plant-second     the failing control: the monotonicity check applied
                                                                  to the second eigenvector at s = 0.5, which must fail
Exit 0 when every value comes out as the card states; 1 otherwise."""
import sys
import numpy as np

ARGS = sys.argv[1:]
if ARGS not in ([], ["--plant-second"]):
    print("usage: no argument, or --plant-second"); sys.exit(2)
PLANT = ARGS == ["--plant-second"]


def nodes(M):
    t, a = np.polynomial.legendre.leggauss(M)
    x = (t + 1) / 2
    bw = (-1.0) ** np.arange(M) * np.sqrt((1 - t * t) * a)
    return x, bw


def interp_matrix(x, bw, y):
    """rows: the barycentric interpolation weights from the nodes x to the points y"""
    d = y[:, None] - x[None, :]
    hit = np.isclose(d, 0, atol=1e-15)
    d = np.where(hit, 1, d)
    W = bw[None, :] / d
    W = W / W.sum(axis=1, keepdims=True)
    rows = np.where(hit.any(axis=1))[0]
    for r in rows:
        W[r] = hit[r].astype(float)
    return W


def operator(s, M):
    x, bw = nodes(M)
    A = (1 + x)[:, None] ** (-2 * s) * (interp_matrix(x, bw, x / (1 + x)) + interp_matrix(x, bw, 1 / (1 + x)))
    return x, bw, A


def leading(s, M, which=0):
    x, bw, A = operator(s, M)
    ev, V = np.linalg.eig(A)
    order = np.argsort(-np.abs(ev))
    lam = ev[order[which]]
    h = V[:, order[which]].real
    if h.sum() < 0:
        h = -h
    grid = np.linspace(0, 1, 2001)
    hg = interp_matrix(x, bw, grid) @ h
    tq, aq = np.polynomial.legendre.leggauss(200)
    lo = interp_matrix(x, bw, 0.025 * (tq + 1)) @ h @ (0.025 * aq)
    tot = interp_matrix(x, bw, 0.5 * (tq + 1)) @ h @ (0.5 * aq)
    nxt = np.abs(ev[order[1:4]])
    return lam, hg, lo / tot, nxt


def word_sum(n, s):
    L = np.array([[1, 1], [0, 1]], dtype=np.int64); R = np.array([[1, 0], [1, 1]], dtype=np.int64)
    P = np.array([L, R]); onlyL = np.array([True, False]); onlyR = np.array([False, True])
    for _ in range(n - 1):
        P = np.concatenate([P @ L, P @ R])
        onlyL = np.concatenate([onlyL, np.zeros_like(onlyL)]); onlyR = np.concatenate([np.zeros_like(onlyR), onlyR])
    keep = ~(onlyL | onlyR)
    tr = (P[:, 0, 0] + P[:, 1, 1])[keep].astype(float)
    lam = (tr + np.sqrt(tr * tr - 4)) / 2
    return keep.sum(), np.sum(lam ** (-2 * s))


ok = True
def show(label, got, good):
    global ok
    print(("DECISIVE: %s %s" % (label, got)).rstrip())
    if not good:
        ok = False

rec_lam = {0.0: 2.000000, 0.1: 1.848487, 0.2: 1.710186, 0.3: 1.584087, 0.4: 1.469311, 0.5: 1.365112, 0.6: 1.270911,
           0.7: 1.186353, 0.8: 1.111484, 0.9: 1.047292, 0.95: 1.020343}
rec_mass = {0.0: 0.0500, 0.1: 0.0546, 0.2: 0.0601, 0.3: 0.0667, 0.4: 0.0749, 0.5: 0.0855, 0.6: 0.0998, 0.7: 0.1204,
            0.8: 0.1539, 0.9: 0.2215, 0.95: 0.2968}
x1 = np.linspace(0.05, 1, 20)
F1 = (1 + x1) ** -2 * ((1 + x1) / x1 + (1 + x1))
show("M0 F_1(1/x) = 1/x on 20 points, worst difference", "%.1e" % np.max(np.abs(F1 - 1 / x1)),
     np.max(np.abs(F1 - 1 / x1)) < 1e-14)
lams, masses = [], []
for s in sorted(rec_lam):
    l3 = [leading(s, M) for M in (100, 200, 300)]
    lam, hg, mass, nxt = l3[2]
    spread = max(abs(l3[i][0] - lam) for i in range(2))
    pos = bool(np.all(hg > 0))
    dec = bool(np.all(np.diff(hg) < 0))
    const = float(np.max(np.abs(hg / hg[0] - 1)))
    lams.append(lam.real); masses.append(mass)
    agree = abs(lam.real - rec_lam[s]) < 1e-6 and abs(lam.imag) < 1e-12 and abs(round(mass, 4) - rec_mass[s]) < 1e-9
    want = (const < 1e-10) if s == 0 else (pos and dec)
    show("s = %.2f: lambda_1 %.6f (M = 100, 200 against 300 within %.0e), mass on [0, 0.05] %.4f; h positive %s, "
         "strictly decreasing %s%s; the next three moduli at M = 300 %s; as recorded %s"
         % (s, lam.real, spread, mass, pos, dec, ", constant to %.0e" % const if s == 0 else "",
            ["%.4f" % v for v in nxt], agree), "", agree and want)
show("M3 lambda_1 strictly decreasing, mass strictly increasing", (bool(np.all(np.diff(lams) < 0)),
                                                                  bool(np.all(np.diff(masses) > 0))),
     bool(np.all(np.diff(lams) < 0)) and bool(np.all(np.diff(masses) > 0)))
for s in (0.25, 0.5):
    n17, z17 = word_sum(17, s); n18, z18 = word_sum(18, s)
    lam = leading(s, 300)[0].real
    rel = abs(z18 / z17 - lam) / lam
    show("M1 s = %.2f: words %d and %d; Z_18 / Z_17 = %.6f against lambda_1 %.6f, relative difference"
         % (s, n17, n18, z18 / z17, lam), "%.2e" % rel, rel < 1e-3)
if PLANT:
    lam2, hg2, _, _ = leading(0.5, 300, which=1)
    dec2 = bool(np.all(np.diff(hg2) < 0)) and bool(np.all(hg2 > 0))
    show("control: the second eigenvector at s = 0.5 (eigenvalue %.4f) positive and strictly decreasing" % lam2.real,
         dec2, dec2)
sys.exit(0 if ok else 1)
