"""B612 — THE PAIRING-CHIRALITY LAW, properly sealed: amphichiral <=>
conjugation-closed hearing spectrum at every level with dim_odd >= 2.

REGISTERED BEFORE RUNNING (MB12, the B611 degenerate edge excluded by
construction — dim_odd(kappa=4) = 1 rows carry no weight):
  P: for every scanned level kappa in {5..16, 20, 24} (all dim_odd >= 2):
     - AMPHICHIRAL objects (cyclic-palindromic blocks, the banked B134
       theorem): RL (1,1); RRLL (2,2); RLRL (1,1,1,1); RRRLLL (3,3)
       — conjugation-closed at EVERY level;
     - CHIRAL objects: RRL (2,1); RRRL (3,1); RRLLL (2,3)
       — closed at NO level.
  Falsifiable both ways: B610/B611 showed closure genuinely fails for
  chiral welds and holds for amphichiral ones level-by-level; a single
  exception on either side kills the law. Seven objects, 14 levels each.
  New objects this run: RLRL, RRRLLL, RRLLL (never computed).

Run: python3 pairing_chirality.py   (~10 min; kappa 24 at 231 weights)
"""
import importlib.util
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location(
    "b238", os.path.join(HERE, "..", "B238_su32_levelrank", "su32_wrt.py"))
b238 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b238)

CACHE = {}


def stage(level):
    if level not in CACHE:
        w, S, T, cc = b238.su3_data(level)
        n = len(w)
        Cm = np.zeros((n, n))
        for i, wt in enumerate(w):
            Cm[w.index((wt[1], wt[0])), i] = 1.0
        R = T
        L = np.linalg.inv(S) @ np.linalg.inv(T) @ S
        prs = sorted({(min(a, b), max(a, b)) for (a, b) in w if a != b})
        U = np.zeros((n, len(prs)))
        for j, (a, b) in enumerate(prs):
            U[w.index((a, b)), j] = 1 / np.sqrt(2)
            U[w.index((b, a)), j] = -1 / np.sqrt(2)
        CACHE[level] = (R, L, U)
    return CACHE[level]


def odd_form(level, word):
    R, L, U = stage(level)
    W = np.eye(R.shape[0], dtype=complex)
    for ch in word:
        W = W @ (R if ch == "R" else L)
    return -(U.T @ W @ U)


def conj_closed(vals, tol=1e-7):
    left = list(vals)
    for v in vals:
        hit = next((i for i, u in enumerate(left)
                    if abs(u - np.conj(v)) < tol), None)
        if hit is None:
            return False
        left.pop(hit)
    return True


KAPPAS = (5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 20, 24)
AMPHI = {"RL": "RL", "RRLL": "RRLL", "RLRL": "RLRL", "RRRLLL": "RRRLLL"}
CHIRAL = {"RRL": "RRL", "RRRL": "RRRL", "RRLLL": "RRLLL"}
ok = True
for label, word in {**AMPHI, **CHIRAL}.items():
    closed = []
    for kap in KAPPAS:
        B = odd_form(kap - 3, word)
        if conj_closed(np.linalg.eigvals(B)):
            closed.append(kap)
    amph = label in AMPHI
    want = list(KAPPAS) if amph else []
    good = closed == want
    ok &= good
    print(f"{label:>8} ({'amphichiral' if amph else 'chiral':>11}): "
          f"closed at {closed if closed else 'NONE'}  "
          f"[{'as the law demands' if good else 'LAW VIOLATED'}]",
          flush=True)

print(f"\nTHE PAIRING-CHIRALITY LAW (dim_odd >= 2): "
      f"{'PASS — 7 objects x 14 levels' if ok else 'FAIL'}", flush=True)
assert ok, "law violated"
print("B612 DONE", flush=True)
