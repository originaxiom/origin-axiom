"""B610 (slice 1) — the m136/silver weld scan: the second object's
stage-side hearing (the Listening Campaign, Phase 4 / K4.2, K4.4).

THE OBJECT (per the campaign adjudication 5): the R^2 L punctured-torus
bundle = the census manifold m136 (monodromy [[3,2],[1,1]], trace 4,
eigenvalue 2+sqrt(3)) — chat-1's handoff called it "5_2"; corrected.
The stage-side hearing form depends on the object only through its weld
word: B_odd = -U^T W_{RRL} U (fig-8's RL -> m136's RRL). Everything else
is the banked B601 machinery.

REGISTERED BEFORE RUNNING (MB12, discriminating facts computed):
  - operation non-trivial: W_{RRL} != W_{RL} (different words, different
    matrices; the fig-8 rows rerun as controls and must differ);
  - VERIFY chat-1's claim: "silver tr_odd is COMPLEX (rotates through
    omega, omega-bar)" — the m136 odd trace at some levels is non-real.
    CAN fail (the trace could be real everywhere, as golden's is) and
    CAN pass — genuinely unknown;
  - the m136 trace-law scan kappa = 4..16 + 20, 24: which kappa give
    nonzero trace; whether a two-indicator law analog exists (the
    fig-8's [5|k]/phi - [4|k] came from ITS eigenvalue field; m136's
    eigenvalue field is Q(sqrt 3), disc 12 — candidate indicators
    [12|k], [6|k], [4|k], [3|k] — reported, not presumed);
  - spectra: conjugation-closure per level (the B601 law's universality
    test — K4.3 row); unit-modulus census (where does the m136 hearing
    leave the unit circle? the golden-exclusivity law's second-object
    test).
Universality rows only; no interpretation. Structure-scan tier.

Run: python3 m136_weld_scan.py   (~3 min)
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
    assert np.allclose(Cm @ W, W @ Cm, atol=1e-9)
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


phi = (1 + math.sqrt(5)) / 2
print("THE m136 WELD SCAN (word RRL) with fig-8 (RL) controls:", flush=True)
print(f"{'kappa':>6} {'tr(RRL) real':>14} {'tr(RRL) imag':>14} "
      f"{'cc':>4} {'unit':>5} {'tr(RL) (control)':>18}", flush=True)
nonreal = []
for kap in (4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 20, 24):
    k = kap - 3
    B = odd_form(k, "RRL")
    tr = np.trace(B)
    lams = np.linalg.eigvals(B)
    cc = conj_closed(lams)
    unit = all(abs(abs(z) - 1) < 1e-7 for z in lams)
    Bc = odd_form(k, "RL")
    trc = np.trace(Bc)
    differ = not np.allclose(B, Bc, atol=1e-9)
    assert differ, f"operation trivial at kappa={kap}?!"
    if abs(tr.imag) > 1e-8:
        nonreal.append(kap)
    print(f"{kap:>6} {tr.real:>+14.9f} {tr.imag:>+14.9f} "
          f"{str(cc):>4} {str(unit):>5} {trc.real:>+11.9f}"
          f"{trc.imag:>+8.1e}j", flush=True)

print(f"\nnon-real m136 odd traces at kappa = {nonreal}", flush=True)
print("chat-1's 'silver tr_odd is COMPLEX' verdict: "
      f"{'CONFIRMED at the listed kappa' if nonreal else 'REFUTED — real everywhere scanned'}",
      flush=True)
print("\nB610 SLICE-1 DONE", flush=True)
