"""B601 — the pairing law across levels: is the golden conjugate-pairing a
basis accident or a spectral fact, and at which levels does it hold?

CONTEXT. P3-V2 (banked #961) tested the two NAIVE directions
((1,0)-(0,1))/sqrt2, ((2,0)-(0,2))/sqrt2 at kappa = 10 and found their
hearing values non-conjugate — outcome B's recorded defect. But that test
was basis-dependent: the theta-odd space at level k has dimension
(#weights - #self-conjugate)/2 (= 2 at k = 2, 16 at k = 7). The
basis-INDEPENDENT question: the full odd hearing form
    B_odd = -U^T W_RL U   (U = the odd pair-direction basis),
whose value at u is the hearing coefficient u' M_odd u (the identity
u^T (Cm W) u = -u^T W u for odd u, Cm symmetric real, [Cm, W] = 0) —
is its SPECTRUM conjugation-closed (real char poly)? Is its TRACE real?
Is the DIAGONAL value multiset conjugation-closed?

REGISTERED BEFORE RUNNING (MB12 triple-check):
  - operation non-trivial: W_RL is genuinely complex; B_odd changes with k;
  - each per-level verdict can PASS (real char poly — as the banked k=2
    case must) and can FAIL (complex coefficients — nothing forces reality
    for a non-Hermitian complex symmetric form);
  - machinery gate: at k = 2 the diagonal must equal the banked
    {1/(2phi) + i sin(2pi/5)/sqrt5, conjugate} exactly (1e-9).
No outcome-bearing P3 claim: this arc REFINES the recorded V2 defect
(structure-scan tier). Scan k = 2..7 and 12 (kappa = 5..10, 15; golden
multiples kappa in {5, 10, 15} marked).

Run: python3 pairing_law_scan.py   (~2 min)
"""
import importlib.util
import math
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location(
    "b238", os.path.join(HERE, "..", "B238_su32_levelrank", "su32_wrt.py"))
b238 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b238)


def odd_form(level):
    w, S, T, cc = b238.su3_data(level)
    n = len(w)
    Cm = np.zeros((n, n))
    for i, wt in enumerate(w):
        Cm[w.index((wt[1], wt[0])), i] = 1.0
    Si, Ti = np.linalg.inv(S), np.linalg.inv(T)
    WRL = T @ (Si @ Ti @ S)
    assert np.allclose(Cm @ WRL, WRL @ Cm, atol=1e-9), "[C, W] != 0"
    pairs = sorted({(min(a, b), max(a, b)) for (a, b) in w if a != b})
    U = np.zeros((n, len(pairs)))
    for j, (a, b) in enumerate(pairs):
        U[w.index((a, b)), j] = 1 / np.sqrt(2)
        U[w.index((b, a)), j] = -1 / np.sqrt(2)
    # odd check
    for j in range(len(pairs)):
        assert np.allclose(Cm @ U[:, j], -U[:, j]), "basis not theta-odd"
    B = -(U.T @ WRL @ U)
    return pairs, B


def multiset_conj_closed(vals, tol=1e-7):
    left = list(vals)
    for v in vals:
        # find a partner for conj(v)
        best = None
        for i, u in enumerate(left):
            if abs(u - np.conj(v)) < tol:
                best = i
                break
        if best is None:
            return False
        left.pop(best)
    return True


# machinery gate at k = 2
pairs2, B2 = odd_form(2)
phi = (1 + math.sqrt(5)) / 2
h3 = 1 / (2 * phi) + 1j * math.sin(2 * math.pi / 5) / math.sqrt(5)
d2 = np.diag(B2)
g = (abs(d2[0] - h3) < 1e-9 and abs(d2[1] - np.conj(h3)) < 1e-9) or \
    (abs(d2[1] - h3) < 1e-9 and abs(d2[0] - np.conj(h3)) < 1e-9)
print(f"machinery gate k=2: diagonal = banked golden pair: {g}", flush=True)
assert g, "k=2 gate failed"

print("\nTHE PAIRING LAW SCAN (kappa = k + 3; golden multiples marked *):",
      flush=True)
print(f"{'k':>3} {'kappa':>6} {'dim_odd':>8} {'trace real':>11} "
      f"{'diag conj-closed':>17} {'charpoly real':>14} "
      f"{'spec conj-closed':>17}", flush=True)
for k in (2, 3, 4, 5, 6, 7, 12):
    pairs, B = odd_form(k)
    d = len(pairs)
    tr = np.trace(B)
    tr_real = abs(tr.imag) < 1e-8
    diag_cc = multiset_conj_closed(np.diag(B))
    coeffs = np.poly(B)                       # char poly coefficients
    cp_real = max(abs(c.imag) for c in coeffs) < 1e-7
    lams = np.linalg.eigvals(B)
    spec_cc = multiset_conj_closed(lams)
    star = "*" if (k + 3) % 5 == 0 else " "
    print(f"{k:>3} {k+3:>5}{star} {d:>8} {str(tr_real):>11} "
          f"{str(diag_cc):>17} {str(cp_real):>14} {str(spec_cc):>17}",
          flush=True)
    if k in (2, 7):
        print(f"      trace = {tr:+.9f}", flush=True)
        if d <= 20:
            print("      diag  = " + "  ".join(f"{x:+.6f}" for x in np.diag(B)),
                  flush=True)

# ---- SECTION 2: THE TRACE LAW --------------------------------------------
# Noticed in the scan: trace(B_odd) is real at every level and takes golden
# values on a two-indicator law. REGISTERED as the mod-4/mod-5 conjecture
# after seeing kappa <= 15 + 20, then CONFIRMED on the discriminating
# predictions kappa = 16 (-> -1) and kappa = 40 (-> -1/phi^2) before this
# final form was written:
#
#     trace(B_odd)(kappa) = [5|kappa]/phi - [4|kappa]
#
# i.e. tr_odd(RL) = [4|kappa] - [5|kappa]/phi (the hearing minus) — EXACTLY
# B587/B585's LAW-O, derived there in the finite Weil model. The odd
# RL-trace law is STAGE-UNIVERSAL across the two models.
print("\nTHE TRACE LAW: trace(B_odd) = [5|k]/phi - [4|k]  (= -LAW-O, B587):",
      flush=True)
lawok = True
for kap in (5, 6, 7, 8, 9, 10, 11, 12, 15, 16, 18, 20, 24, 25):
    k = kap - 3
    _, B = odd_form(k)
    tr = np.trace(B)
    pred = (1 / phi if kap % 5 == 0 else 0.0) - (1.0 if kap % 4 == 0 else 0.0)
    ok = abs(tr - pred) < 1e-8
    lawok &= ok
    print(f"  kappa={kap:>2}: trace = {tr.real:+.9f}  predicted {pred:+.9f}"
          f"  [{ok}]", flush=True)
assert lawok, "TRACE LAW FAILED"
print("\nDONE (structure scan + the trace law; refines the V2 defect on "
      "record)", flush=True)
