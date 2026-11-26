# s15_spectra.py -- spectrum of T = L_* + R_* + L^-1_* + R^-1_* (adjacency of the 4-regular Schreier graph) on the
# largest orbit of each leaf k != 4 mod p. Floating point: numpy.linalg.eigvalsh, float64 (errors ~1e-12).
# Also splits functions into N-invariant ones (constant on sign-change blocks) and their complement:
# T commutes with the averaging over N (s01: L,R normalise N), so both parts are T-invariant.
import sys
import numpy as np
from modn import orbits
r3 = 2*np.sqrt(3)
for p in map(int, sys.argv[1:]):
    x, y, z, Li, Ri, k, nc, lab = orbits(p)
    sizes = np.bincount(lab)
    rows = []
    for kv in range(p):
        if kv == 4 % p: continue
        labs = np.unique(lab[k == kv]); big = max(labs, key=lambda l: sizes[l])
        mem = np.nonzero(lab == big)[0]; n = len(mem)
        if n < 30: continue
        pos = -np.ones(p**3, dtype=np.int64); pos[mem] = np.arange(n)
        T = np.zeros((n, n))
        for M in (Li, Ri):
            q = pos[M[mem]]
            T[q, np.arange(n)] += 1; T[np.arange(n), q] += 1
        # N-averaging projector
        def nimg(s):
            a, b, c = x[mem], y[mem], z[mem]
            if s == 0: a, b = -a, -b
            elif s == 1: a, c = -a, -c
            else: b, c = -b, -c
            return pos[((a % p)*p + (b % p))*p + (c % p)]
        P = np.eye(n)
        for s in range(3):
            Q = np.zeros((n, n)); Q[nimg(s), np.arange(n)] = 1; P += Q
        P /= 4
        ev = np.linalg.eigvalsh(T)
        # restrict to the two parts
        w, V = np.linalg.eigh(P)
        Vin = V[:, w > 0.5]; Vout = V[:, w < 0.5]
        ein = np.linalg.eigvalsh(Vin.T @ T @ Vin); eout = np.linalg.eigvalsh(Vout.T @ T @ Vout)
        lam2 = sorted(ev)[-2]; lmin = ev.min()
        print("p=%d k=%d n=%d  lambda2=%.6f  lambda_min=%.6f  (2sqrt3=%.4f)  N-inv part: dim %d, max nontriv %.6f, min %.6f | complement: dim %d, max %.6f, min %.6f  | #eig=+-2 (|.|<1e-9): +2:%d -2:%d  0:%d" % (
            p, kv, n, lam2, lmin, r3, Vin.shape[1], sorted(ein)[-2], ein.min(), Vout.shape[1], eout.max(), eout.min(),
            np.sum(np.abs(ev-2) < 1e-9), np.sum(np.abs(ev+2) < 1e-9), np.sum(np.abs(ev) < 1e-9)), flush=True)
