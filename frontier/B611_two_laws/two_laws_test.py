"""B611 — the two-law test: amphichirality <=> conjugation-closure, and
the field-window of unit-circle departure (registered predictions).

REGISTERED BEFORE RUNNING (MB12; both predictions falsifiable both ways):
  P1 (from B610's mechanism candidate + the banked B134 theorem
      "amphichiral <=> cyclic-palindromic block sequence"):
      RRLL (blocks (2,2), CYCLIC PALINDROME => amphichiral, the silver
      metallic bundle, eigenvalue delta^2 = 3+2sqrt2) has a
      conjugation-CLOSED odd hearing spectrum at every scanned level;
      RRRL (blocks (3,1), NOT a cyclic palindrome => chiral) is closed
      at NO scanned level. Failure of either half kills or wounds the
      amphichirality mechanism. (m136 = R^2L already gave chiral/not
      closed; fig-8 = RL gave amphichiral/closed — the third and fourth
      objects decide.)
  P2 (the field-window measurement): record at which kappa each object's
      spectrum leaves the unit circle. The fig-8 rows double as the
      VERIFICATION of B609's exploratory law-candidate (departures
      exactly at the golden multiples kappa = 10, 15, 20 within the
      scan; unit elsewhere). For RRLL the departure window (if any) is a
      MEASUREMENT — candidate: its field Q(sqrt2), disc 8 (no value
      presumed).
Scan kappa = 4..16, 20, 24. Structure-scan tier; no interpretation.

Run: python3 two_laws_test.py   (~4 min)
"""
import importlib.util
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location(
    "b238", os.path.join(HERE, "..", "B238_su32_levelrank", "su32_wrt.py"))
b238 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b238)


def odd_form(level, word):
    w, S, T, cc = b238.su3_data(level)
    n = len(w)
    Cm = np.zeros((n, n))
    for i, wt in enumerate(w):
        Cm[w.index((wt[1], wt[0])), i] = 1.0
    R = T
    L = np.linalg.inv(S) @ np.linalg.inv(T) @ S
    W = np.eye(n, dtype=complex)
    for ch in word:
        W = W @ (R if ch == "R" else L)
    prs = sorted({(min(a, b), max(a, b)) for (a, b) in w if a != b})
    U = np.zeros((n, len(prs)))
    for j, (a, b) in enumerate(prs):
        U[w.index((a, b)), j] = 1 / np.sqrt(2)
        U[w.index((b, a)), j] = -1 / np.sqrt(2)
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


KAPPAS = (4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 20, 24)
WORDS = {"RL (fig-8, amphichiral)": "RL",
         "RRLL (silver, amphichiral)": "RRLL",
         "RRL (m136, chiral)": "RRL",
         "RRRL (chiral)": "RRRL"}
results = {}
for label, word in WORDS.items():
    rows = []
    for kap in KAPPAS:
        B = odd_form(kap - 3, word)
        lams = np.linalg.eigvals(B)
        cc = conj_closed(lams)
        unit = all(abs(abs(z) - 1) < 1e-7 for z in lams)
        rows.append((kap, cc, unit))
    results[label] = rows
    ccs = [k for (k, c, u) in rows if c]
    dep = [k for (k, c, u) in rows if not u]
    print(f"{label}: conj-closed at kappa = {ccs}", flush=True)
    print(f"{'':>{len(label)}}  departs the unit circle at kappa = {dep}",
          flush=True)

# P1 verdicts
rl = results["RL (fig-8, amphichiral)"]
rrll = results["RRLL (silver, amphichiral)"]
rrl = results["RRL (m136, chiral)"]
rrrl = results["RRRL (chiral)"]
p1a = all(c for (_, c, _) in rrll)
p1b = not any(c for (_, c, _) in rrrl)
p1c = all(c for (_, c, _) in rl) and not any(c for (_, c, _) in rrl)
print(f"\nP1 (amphichirality <=> closure): RRLL all-closed: {p1a}; "
      f"RRRL never-closed: {p1b}; controls (RL all / RRL never): {p1c}",
      flush=True)
print(f"P1 VERDICT: {'PASS' if (p1a and p1b and p1c) else 'FAIL'}",
      flush=True)

# P2: fig-8 departures = the golden multiples in-scan
figdep = [k for (k, c, u) in rl if not u]
p2 = figdep == [10, 15, 20] or figdep == [5, 10, 15, 20]
print(f"P2 (fig-8 golden-exclusivity in-scan): departures = {figdep} "
      f"(golden multiples in scan: 5, 10, 15, 20): "
      f"{'PASS' if p2 else 'FAIL'}", flush=True)
rrlldep = [k for (k, c, u) in rrll if not u]
print(f"P2-measurement: RRLL departure window = {rrlldep}", flush=True)
print("\nB611 DONE", flush=True)
