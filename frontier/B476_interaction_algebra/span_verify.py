#!/usr/bin/env python3
"""B476 — the 'critical interaction algebra' adjudication (seat-1's gl(2)xgl(3)/SM claim).
All four load-bearing numbers refuted; the true structure identified (parity blocks)."""
import sys
import numpy as np

def weil_pair(N):
    z = np.exp(2j*np.pi/N)
    D = np.diag([z**((j*(j-1)//2) % N) for j in range(N)])
    F = np.array([[z**((i*j) % N) for j in range(N)] for i in range(N)])/np.sqrt(N)
    WR = (F @ D @ F.conj().T).conj().T
    return WR @ D, WR @ WR @ D @ D

def order(M, cap=200):
    P = np.eye(len(M), dtype=complex)
    for k in range(1, cap+1):
        P = P @ M
        if np.max(np.abs(P - np.eye(len(M)))) < 1e-9: return k
    return None

def span_dim(mats, tol=1e-9):
    A = np.array([m.flatten() for m in mats])
    s = np.linalg.svd(A, compute_uv=False)
    return int((s > tol*s[0]).sum())

def product_span(N):
    W1, W2 = weil_pair(N)
    o1, o2 = order(W1), order(W2)
    mats = []
    P1 = np.eye(N, dtype=complex)
    for j in range(o1):
        P2 = np.eye(N, dtype=complex)
        for l in range(o2):
            mats.append(P1 @ P2)
            P2 = P2 @ W2
        P1 = P1 @ W1
    return span_dim(mats)

def main():
    d15, d3, d5 = product_span(15), product_span(3), product_span(5)
    print(f"dim span at N=15: {d15} (claim 36: {'REFUTED' if d15 != 36 else 'ok'})")
    print(f"dim mod-3 span:   {d3}  (claim 4 = gl(2): {'REFUTED' if d3 != 4 else 'ok'}; true: C + M2 parity blocks)")
    print(f"dim mod-5 span:   {d5}  (claim 9 = gl(3): {'REFUTED' if d5 != 9 else 'ok'}; true: M2 + M3 parity blocks)")
    print(f"tensor factorization: {d3}x{d5} = {d3*d5} vs {d15} -> {'REFUTED' if d3*d5 != d15 else 'factors'}")
    ok = d15 == 49 and d3 == 5 and d5 == 13
    print("ALL CHECKS PASS" if ok else "CHECK FAILURE")
    sys.exit(0 if ok else 1)

if __name__ == '__main__':
    main()
