"""B596 — the clock is the cat-map period (see PREREGISTRATION.md).

Q1: recompute the theta-odd clock(kappa) directly and sweep it against the
classical orders ord(A1 mod m) for m in {kappa, 2 kappa, kappa^2, ...} — blind.
Q2: the silver word at two kappa. Run: python3 cat_map_clock.py (~3 min).
"""
import importlib.util
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location(
    "b238", os.path.join(HERE, "..", "B238_su32_levelrank", "su32_wrt.py"))
b238 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b238)


def clock(k, word="RL", cap=2520):
    w, S, T, c = b238.su3_data(k)
    n = len(w)
    Si, Ti = np.linalg.inv(S), np.linalg.inv(T)
    R, L = T, Si @ Ti @ S
    M = np.eye(n, dtype=complex)
    for ch in word:
        M = M @ (R if ch == 'R' else L)
    prs = [(i, w.index((wt[1], wt[0]))) for i, wt in enumerate(w)
           if (wt[1], wt[0]) > wt]
    if not prs:
        return 1
    odd = np.zeros((n, len(prs)))
    for j, (a, b) in enumerate(prs):
        odd[a, j], odd[b, j] = 1 / np.sqrt(2), -1 / np.sqrt(2)
    B = odd.T @ M @ odd
    P = np.eye(len(prs), dtype=complex)
    for m in range(1, cap + 1):
        P = P @ B
        if np.allclose(P, np.eye(len(prs)), atol=1e-8):
            return m
    return None


def mat_word(word):
    R = np.array([[1, 1], [0, 1]], dtype=object)
    L = np.array([[1, 0], [1, 1]], dtype=object)
    M = np.eye(2, dtype=object)
    for ch in word:
        M = M @ (R if ch == 'R' else L)
    return M


def ord_mod(A, m, cap=100000):
    """order of A in GL(2, Z/m); also the +-I-refined (projective) order."""
    I = np.eye(2, dtype=object)
    P = I.copy()
    proj = None
    for k in range(1, cap + 1):
        P = (P @ A) % m
        if proj is None and (np.array_equal(P % m, (-I) % m)):
            proj = k                      # A^k = -I
        if np.array_equal(P % m, I % m):
            return k, proj
    return None, proj


print("Q1 — the BLIND sweep (golden word RL, A1 = [[2,1],[1,1]]):")
print("  kap  clock   ord(k) ord(2k) ord(k^2)  A^j=-I@k")
A1 = mat_word("RL")
rows = {}
for kap in range(4, 16):
    k = kap - 3
    cl = clock(k)
    o1, p1 = ord_mod(A1, kap)
    o2, _ = ord_mod(A1, 2 * kap)
    o3, _ = ord_mod(A1, kap * kap)
    rows[kap] = (cl, o1, o2, o3, p1)
    print(f"  {kap:3d}  {cl:5d}   {o1:5d} {o2:6d} {o3:7d}   {str(p1):>6}")

print("\n  the candidate laws (read off the table, tested on every row):")
for name, f in (("clock = ord(2 kap)", lambda r: r[0] == r[2]),
                ("clock = ord(kap)", lambda r: r[0] == r[1]),
                ("clock = 2 ord(kap)", lambda r: r[0] == 2 * r[1]),
                ("clock | ord(2 kap)", lambda r: r[2] % r[0] == 0),
                ("ord(2 kap) | clock", lambda r: r[0] % r[2] == 0)):
    hits = sum(1 for r in rows.values() if f(r))
    print(f"    {name:>20}: {hits}/12")

print("\nQ2 — the silver word (RRLL) at kap = 6, 8:")
As = mat_word("RRLL")
for kap in (6, 8):
    cl = clock(kap - 3, "RRLL")
    o1, _ = ord_mod(As, kap)
    o2, _ = ord_mod(As, 2 * kap)
    print(f"  kap={kap}: clock = {cl};  ord(kap) = {o1};  ord(2 kap) = {o2}")
print("\nDONE (reads are post-hoc; the winning law, if any, is banked with its misses)")
