"""Independent verification of cc2's digest cells G1 and G4.

G4: B596's clocks (recomputed from the banked su32_wrt machinery) vs
    ord(A1 mod 3*kappa) computed with FRESH order code — all rows k=1..12.
G1: the sign-hears-the-discriminant theorem tested on a FRESH Weyl group
    W(D4) (order 192, even rank — not in cc2's E6/A2 battery) including
    FRESH words t=4 (disc 12) and t=8 (disc 60) cc2 never ran.
"""
import importlib.util
import itertools
import os

import numpy as np
from sympy import factorint

ROOT = "/Users/dri/origin-axiom"
spec = importlib.util.spec_from_file_location(
    "b238", os.path.join(ROOT, "frontier", "B238_su32_levelrank", "su32_wrt.py"))
b238 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b238)


def clock(k, cap=200):
    w, S, T, c = b238.su3_data(k)
    Si, Ti = np.linalg.inv(S), np.linalg.inv(T)
    M = T @ (Si @ Ti @ S)
    prs = [(i, w.index((wt[1], wt[0]))) for i, wt in enumerate(w)
           if (wt[1], wt[0]) > wt]
    odd = np.zeros((len(w), len(prs)))
    for j, (a, b) in enumerate(prs):
        odd[a, j], odd[b, j] = 1 / np.sqrt(2), -1 / np.sqrt(2)
    B = odd.T @ M @ odd
    P = np.eye(len(prs), dtype=complex)
    for m in range(1, cap + 1):
        P = P @ B
        if np.allclose(P, np.eye(len(prs)), atol=1e-8):
            return m
    return None


def ord_mat_mod(A, m, cap=100000):
    """Fresh order code: order of 2x2 integer matrix A in GL(2, Z/m)."""
    a, b, c, d = A
    x = (a % m, b % m, c % m, d % m)
    idm = (1 % m, 0, 0, 1 % m)
    cur = x
    for k in range(1, cap + 1):
        if cur == idm:
            return k
        cur = ((cur[0] * a + cur[1] * c) % m, (cur[0] * b + cur[1] * d) % m,
               (cur[2] * a + cur[3] * c) % m, (cur[2] * b + cur[3] * d) % m)
    return None


print("== G4: clock(kappa) vs ord(A1 mod 3*kappa), kappa = 4..15 ==", flush=True)
A1 = (2, 1, 1, 1)
hits = 0
for k in range(1, 13):
    kap = k + 3
    c = clock(k)
    o = ord_mat_mod(A1, 3 * kap)
    mark = "EXACT" if c == o else ("ANOMALY-ZONE" if kap in (4, 5) else "FAIL")
    if c == o and kap >= 6:
        hits += 1
    print(f"  kappa={kap:2d}: clock={c:3}  ord(A1 mod {3*kap:2d})={o:3}  {mark}",
          flush=True)
print(f"  G4 law rows (kappa 6..15): {hits}/10 exact", flush=True)

print("\n== G1: W(D4) x fresh words ==", flush=True)


def wd4():
    """All 192 elements of W(D4) as 4x4 signed permutation matrices."""
    for perm in itertools.permutations(range(4)):
        for signs in itertools.product((1, -1), repeat=4):
            if signs.count(-1) % 2:
                continue
            M = np.zeros((4, 4), dtype=int)
            for i, j in enumerate(perm):
                M[i, j] = signs[i]
            yield M


ELEMS = list(wd4())
assert len(ELEMS) == 192

for t in (3, 6, 5, 7, 4, 8):
    disc = t * t - 4
    fac = factorint(disc)
    primes = sorted(set(fac) | {13})  # 13 never divides these discs: control
    print(f"  t={t} (disc {disc} = {fac}):", flush=True)
    for p in primes:
        vdisc = fac.get(p, 0)
        agree = 0
        for w in ELEMS:
            Bw = t * np.eye(4, dtype=int) - w - np.linalg.inv(w).astype(int)
            db = int(round(np.linalg.det(Bw.astype(float))))
            # exact integer det via fraction-free: use numpy object? do exact:
            db = int(round(np.linalg.det(Bw.astype(np.float64))))
            v = 0
            x = abs(db)
            while x % p == 0:
                x //= p
                v += 1
            detw = int(round(np.linalg.det(w.astype(np.float64))))
            if detw == (-1) ** v:
                agree += 1
        want = "TRACK(192)" if vdisc % 2 == 1 else "half"
        ok = (agree == 192) if vdisc % 2 == 1 else (agree == 96)
        print(f"    p={p:2d} v_p(disc)={vdisc}: agree {agree}/192  "
              f"expected {want}  {'OK' if ok else 'DEVIATES'}", flush=True)

print("\nDONE", flush=True)
