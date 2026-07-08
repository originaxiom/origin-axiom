#!/usr/bin/env python3
"""B473 C1 — the off-critical seam controls (numeric-exact first pass, dps via complex128).

Design sharpened by the arithmetic itself: the critical pair's level 15 = 3·5 (two primes
-> the biquadratic/Klein-four architecture). Controls:
  (1,3): level tr(A1A3) = 27 = 3^3 (PRIME POWER -> only one quadratic subfield: the
         Klein-four architecture CANNOT exist — prediction: structural collapse)
  (2,3): level tr(A2A3) = 63 = 9·7 (two primes -> a Klein-four-like lattice CAN exist —
         prediction: architecture present, different fields — the class-shift test)
For each pair at its level: Weil ops W_m = Wr^m Wl^m, orders, spectral projectors,
Par-inserted pair traces tr(Par P_a Q_b); report the vanishing-pattern profile."""
import numpy as np
np.seterr(all="ignore")

def weil_ops(N, m1, m2):
    z = np.exp(2j*np.pi/N)
    D = np.diag([z**((j*(j-1)//2) % N) for j in range(N)])
    F = np.array([[z**((i*j) % N) for j in range(N)] for i in range(N)])/np.sqrt(N)
    Wr = (F @ D @ F.conj().T).conj().T
    def W(m):
        return np.linalg.matrix_power(Wr, m) @ np.linalg.matrix_power(D, m)
    Par = np.zeros((N, N), complex)
    for j in range(N): Par[(-j) % N, j] = 1
    return W(m1), W(m2), Par

def order_and_projs(W, N, cap=400):
    ev, V = np.linalg.eig(W)
    # find the operator order (smallest k with W^k = phase-free identity)
    P = np.eye(N, dtype=complex); order = None
    for k in range(1, cap+1):
        P = P @ W
        if np.max(np.abs(P - np.eye(N))) < 1e-8: order = k; break
    if order is None: return None, None
    ks = [int(round((np.angle(l)/(2*np.pi))*order)) % order for l in ev]
    projs = {}
    for kk in sorted(set(ks)):
        idx = [i for i in range(N) if ks[i] == kk]
        Q, _ = np.linalg.qr(V[:, idx])
        projs[kk] = Q @ Q.conj().T
    return order, projs

for (m1, m2, N) in ((1, 2, 15), (1, 3, 27), (2, 3, 63)):
    W1, W2, Par = weil_ops(N, m1, m2)
    o1, P1 = order_and_projs(W1, N)
    o2, P2 = order_and_projs(W2, N)
    if P1 is None or P2 is None:
        print(f"pair ({m1},{m2}) @ level {N}: order cap exceeded", flush=True); continue
    vals = []
    zero_cnt = 0
    for a, Pa in P1.items():
        for b, Qb in P2.items():
            t = np.trace(Par @ Pa @ Qb)
            vals.append(abs(t))
            if abs(t) < 1e-9: zero_cnt += 1
    tot = len(vals)
    nz = sorted(v for v in vals if v >= 1e-9)
    print(f"pair ({m1},{m2}) @ level {N}: ord(W{m1}) = {o1}, ord(W{m2}) = {o2}; "
          f"torus cells = {tot}; ZERO cells = {zero_cnt} ({100*zero_cnt/tot:.1f}%); "
          f"nonzero |values|: min {nz[0]:.4f}, max {nz[-1]:.4f}, distinct~{len(set(np.round(nz,6)))}",
          flush=True)
print("C1 DONE", flush=True)
