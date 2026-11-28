#!/usr/bin/env python3
"""sm2 (fam1-v1-unset-05): an independent recomputation for card Q0014 (the leading mode of the symmetric Farey operator
F_s on [0, 1]). numpy and the standard library. Written from the card's definitions only.

    python3 relays/claims/banking/code/sm2_Q0014_farey.py            # the card's values of s
    python3 relays/claims/banking/code/sm2_Q0014_farey.py --control  # the second eigenfunction at s = 0.5 in its place

(F_s f)(x) = (1 + x)^(-2s) [f(x/(1 + x)) + f(1/(1 + x))]. Discretised by Nystrom collocation at N Gauss-Legendre nodes on
[0, 1] with barycentric interpolation (weights (-1)^j sqrt((1 - t_j^2) omega_j) on [-1, 1]), N = 64, 128, 256; the leading
eigenpair by numpy's eig, checked by power iteration; h_s read at 2001 equally spaced points. lambda_1 also from word sums
Z_n(s) over the words in L = [[1,1],[0,1]] and R = [[1,0],[1,1]] holding both letters, Z_18 / Z_17.
"""
import sys
import numpy as np

CONTROL = "--control" in sys.argv

def nodes(N):
    t, w = np.polynomial.legendre.leggauss(N)
    bw = (-1.0) ** np.arange(N) * np.sqrt((1 - t ** 2) * w)
    return (t + 1) / 2, bw

def interp_matrix(y, t, bw):
    D = y[:, None] - t[None, :]
    hit = np.isclose(D, 0.0, atol=1e-15)
    D[hit] = 1.0
    K = bw[None, :] / D
    K = K / K.sum(axis=1, keepdims=True)
    rows = np.where(hit.any(axis=1))[0]
    for r in rows:
        K[r] = 0.0; K[r, np.argmax(hit[r])] = 1.0
    return K

def operator(s, N):
    t, bw = nodes(N)
    A = (1 + t) ** (-2 * s)
    M = A[:, None] * (interp_matrix(t / (1 + t), t, bw) + interp_matrix(1 / (1 + t), t, bw))
    return M, t, bw

def modes(s, N, which=0):
    M, t, bw = operator(s, N)
    ev, V = np.linalg.eig(M)
    order = np.argsort(-ev.real)
    lam = ev[order[which]].real; v = V[:, order[which]].real
    if v[np.argmax(np.abs(v))] < 0: v = -v
    return lam, v, t, bw, M, ev[order]

def power(M, iters=3000):
    v = np.ones(M.shape[0])
    lam = 0.0
    for _ in range(iters):
        u = M @ v; lam = np.linalg.norm(u) / np.linalg.norm(v); v = u / np.linalg.norm(u)
    return lam

def word_ratio(s, n):
    def Z(n):
        mats = np.array([[[1, 0], [0, 1]]], dtype=np.int64)
        hasL = np.array([False]); hasR = np.array([False])
        Lm = np.array([[1, 1], [0, 1]], dtype=np.int64); Rm = np.array([[1, 0], [1, 1]], dtype=np.int64)
        for _ in range(n):
            mats = np.concatenate([mats @ Lm, mats @ Rm])
            hasL = np.concatenate([np.ones_like(hasL), hasL]); hasR = np.concatenate([hasR, np.ones_like(hasR)])
        keep = hasL & hasR
        tr = (mats[:, 0, 0] + mats[:, 1, 1])[keep].astype(float)
        lw = (tr + np.sqrt(tr * tr - 4)) / 2
        return float(np.sum(lw ** (-2 * s)))
    return Z(n + 1) / Z(n)

grid = np.linspace(0, 1, 2001)
S_LIST = [0.0] + [round(0.1 * k, 1) for k in range(1, 10)] + [0.95]
if CONTROL:
    S_LIST = [0.5]
lams, rows, bad = [], [], []
for s in S_LIST:
    out = {}
    for N in (64, 128, 256):
        lam, v, t, bw, M, ev = modes(s, N, 1 if CONTROL else 0)
        h = interp_matrix(grid, t, bw) @ v
        out[N] = (lam, h, M, ev)
    lam, h, M, ev = out[256]
    agree = abs(out[256][0] - out[128][0])
    pw = power(out[128][2]) if not CONTROL else float("nan")
    h = h / h[np.argmax(np.abs(h))]
    dh = np.diff(h)
    if s == 0.0:
        shape = "constant" if np.max(np.abs(h - h[0])) < 1e-10 else "not constant"
        ok = shape == "constant" and h.min() > 0
    else:
        shape = "strictly decreasing" if np.all(dh < 0) else ("changes sign" if h.min() < 0 < h.max() else "not monotone")
        ok = shape == "strictly decreasing" and h.min() > 0
    if not ok: bad.append(s)
    lams.append(lam)
    print("s = %.2f: lambda_1 = %.10f (N = 256; |N256 - N128| = %.1e; power iteration at 128: %.10f); h %s, min h %.4f, "
          "largest step %.2e" % (s, lam, agree, pw, shape, h.min(), dh.max() if s > 0 else 0.0))
    rows.append((s, lam, shape))
if not CONTROL:
    for s in (0.25, 0.5):
        lam = [l for (ss, l, _) in rows if ss == s]
        lam = lam[0] if lam else modes(s, 256)[0]
        print("word sums: s = %.2f, Z_18/Z_17 = %.6f, collocation %.6f, difference %.1e"
              % (s, word_ratio(s, 17), lam, abs(word_ratio(s, 17) - lam)))
    falls = all(a > b for a, b in zip(lams, lams[1:]))
    print("DECISIVE: lambda_1 at s = 0: %.10f; at s = 0.95: %.4f" % (lams[0], lams[-1]))
    print("DECISIVE: lambda_1 falls strictly over s = 0, 0.1, ..., 0.9, 0.95: %s" % falls)
    print("DECISIVE: h_s constant at s = 0 and positive, strictly decreasing at s = 0.1, ..., 0.9, 0.95: %s (fails at %s)"
          % (not bad, bad))
    ok = falls and not bad and abs(lams[0] - 2) < 1e-10 and round(lams[-1], 4) == 1.0203
else:
    print("DECISIVE: the second eigenfunction at s = 0.5 passes the check: %s" % (not bad))
    ok = False
print("RESULT: the card's claim %s" % ("holds" if ok else "does not come out"))
sys.exit(0 if ok else 1)
