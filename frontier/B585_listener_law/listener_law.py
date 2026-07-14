"""B585 — the listener's law.

N1 (naming): on the stage S^2 = -C, in SL(2,Z) S^2 = -I, so the C-twisted play
is (up to the central sign) the play of the OTHER SL(2,Z) lift -M: verify
tr(C rho(W)) = -tr rho(S^2 W) and the channel identities
  tr_odd = (Z(W) + Z(S^2 W))/2,   tr_even = (Z(W) - Z(S^2 W))/2
on several words. K1 (BLIND): the SU(3)_k ladder k=1..12 — odd-block dim,
tr_odd, tr_even, clock order, Z. Gates: k=2 reproduces B584/B238 exactly.
Law-hunting only AFTER the table prints; any law must pass held-out k=13..16.

Run: python3 listener_law.py (pyenv, ~1 min). Firewall: nothing to CLAIMS.md.
"""
import cmath
import importlib.util
import os
from fractions import Fraction

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location(
    "b238", os.path.join(HERE, "..", "B238_su32_levelrank", "su32_wrt.py"))
b238 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b238)

PHI = (1 + 5 ** 0.5) / 2


def stage(k):
    w, S, T, c = b238.su3_data(k)
    n = len(w)
    C = np.zeros((n, n))
    for i, wt in enumerate(w):
        C[w.index((wt[1], wt[0])), i] = 1.0
    assert b238.modular_gate(S, T), f"modular gate failed at k={k}"
    assert np.allclose(C @ S, S @ C, atol=1e-9) and np.allclose(C @ T, T @ C, atol=1e-9), \
        f"C not central at k={k}"
    assert np.allclose(np.abs(S @ S), C, atol=1e-8), f"|S^2| != C at k={k}"
    return w, S, T, C


def rho_word(S, T, word):
    Si, Ti = np.linalg.inv(S), np.linalg.inv(T)
    R, L = T, Si @ Ti @ S
    M = np.eye(S.shape[0], dtype=complex)
    for ch in word:
        M = M @ (R if ch == 'R' else L)
    return M


def block_order(B, cap=2520):
    P = np.eye(B.shape[0], dtype=complex)
    for k in range(1, cap + 1):
        P = P @ B
        if np.allclose(P, np.eye(B.shape[0]), atol=1e-8):
            return k
    return None


def frac_of_2pi(e, maxden=720):
    f = Fraction(cmath.phase(e) / (2 * np.pi)).limit_denominator(maxden)
    return f if abs(float(f) - cmath.phase(e) / (2 * np.pi)) < 1e-8 else None


# ---------------- N1: the naming theorem (the two lifts) ----------------
print("N1 — the naming theorem: C-twist = the other SL(2,Z) lift (up to the central sign)")
w, S, T, C = stage(2)
n = len(w)
S2 = S @ S
assert np.allclose(S2, -C, atol=1e-9), "S^2 != -C at k=2"
print("  S^2 = -C on the stage (exact);  in SL(2,Z): S^2 = -I  => C-insertion = (-M)-lift insertion")
for word in ("RL", "RRLL", "RRRLLL", "RRL"):
    M = rho_word(S, T, word)
    Z = np.trace(M)
    ZC = np.trace(C @ M)
    Zlift = np.trace(S2 @ M)                       # the (-M)-lift play
    assert abs(ZC + Zlift) < 1e-9, f"tr(C rho) != -tr(S^2 rho) at {word}"
    tr_odd = np.trace(M @ (np.eye(n) - C) / 2)
    tr_even = np.trace(M @ (np.eye(n) + C) / 2)
    assert abs(tr_odd - (Z + Zlift) / 2) < 1e-9
    assert abs(tr_even - (Z - Zlift) / 2) < 1e-9
    print(f"  {word:>7}: Z={Z:+.6f}  Z(-M lift)={Zlift:+.6f}  "
          f"odd=(Z+Zlift)/2={tr_odd:+.6f}  even=(Z-Zlift)/2={tr_even:+.6f}")
print("  => the theta-odd channel = what the TWO LIFTS AGREE ON (their symmetrization);")
print("     the theta-even channel = the lift-dependence. Chirality is lift-agreement. VERIFIED")
print("  (-A1 has trace -3 != 3: the two lifts are genuinely different Sol bundles;")
print("   cf. B279 for the complement-level spin bit — adjacent, distinct object.)")

# ---------------- K1: the clock map (BLIND — table first, law after) ----------------
print("\nK1 — the SU(3)_k ladder (BLIND; kappa = k+3):")
print("  k  kap  dim_odd   Z            tr_even      tr_odd       clock")
rows = {}
for k in range(1, 13):
    w, S, T, C = stage(k)
    n = len(w)
    M = rho_word(S, T, "RL")
    pairs = [(i, w.index((wt[1], wt[0]))) for i, wt in enumerate(w) if (wt[1], wt[0]) > wt]
    odd = np.zeros((n, len(pairs)))
    for j, (i, ib) in enumerate(pairs):
        odd[i, j], odd[ib, j] = 1 / np.sqrt(2), -1 / np.sqrt(2)
    B = odd.T @ M @ odd
    Z = np.trace(M)
    tr_odd = np.trace(M @ (np.eye(n) - C) / 2)
    tr_even = Z - tr_odd
    order = block_order(B) if pairs else 1
    rows[k] = (len(pairs), Z, tr_even, tr_odd, order, B)
    print(f"  {k:2d}  {k+3:3d}  {len(pairs):5d}   {Z:+.6f}  {tr_even:+.6f}  {tr_odd:+.6f}   {order}")

# gates: k=2 must reproduce B584/B238
d2, Z2, e2, o2, ord2, B2 = rows[2]
assert abs(Z2 - (-1 / PHI)) < 1e-9 and abs(e2) < 1e-9 and abs(o2 - (-1 / PHI)) < 1e-9 and ord2 == 10
print("  gate: k=2 reproduces B584 (tr_even=0, tr_odd=-1/phi, clock 10)  PASS")

print("\n(the table above was printed BLIND; law-hunting below is post-hoc and any law")
print(" must pass the held-out levels k=13..16 before being stated as a finding)")

# post-hoc: eigenvalue arguments of the odd blocks as fractions of 2pi
print("\npost-hoc: odd-block eigenvalue args (fractions of 2pi):")
for k in range(1, 13):
    B = rows[k][5]
    if B.shape[0] == 0:
        continue
    fr = [frac_of_2pi(e) for e in np.linalg.eigvals(B)]
    print(f"  k={k:2d}: {[str(f) for f in fr]}")

# ---------------- the HOLD-OUT test (post-hoc laws, registered then tested) ----------------
print("\nHOLD-OUT: candidate laws read off the blind table (registered BEFORE computing k=13..17):")
print("  LAW-O: tr_odd = -1/phi if 5|kappa; +1 if 4|kappa; 0 otherwise  (kappa=20 = the collision)")
print("  LAW-E: tr_even = -1 if kappa==2 mod 4; +1 if kappa==1 mod 6 or (4|kappa, kappa>=8); 0 else")
print("  predictions: kap16 odd=+1; kap17 odd=0; kap18 odd=0,even=-1; kap19 odd=0,even=+1; kap20 = ?")
for k in range(13, 18):
    w, S, T, C = stage(k)
    n = len(w)
    M = rho_word(S, T, "RL")
    Z = np.trace(M)
    tr_odd = np.trace(M @ (np.eye(n) - C) / 2)
    tr_even = Z - tr_odd
    kap = k + 3
    pred_o = (-1 / PHI if kap % 5 == 0 else 0) + (1 if kap % 4 == 0 else 0)
    hit = "HIT " if abs(tr_odd - pred_o) < 1e-7 else "MISS"
    print(f"  k={k:2d} kap={kap:2d}: tr_even={tr_even:+.6f}  tr_odd={tr_odd:+.6f}  "
          f"LAW-O(additive) pred={pred_o:+.6f} {hit}")

# ---------------- M1: the mechanism test (field containment) ----------------
# PREREGISTERED before this sweep: if LAW-O's 5|kappa is really "sqrt(5) in Q(zeta_kappa)"
# (the stage's field contains the WORD'S trace field), then the resonance locus must MOVE
# with the word: silver RRLL (field Q(sqrt2)) fires iff 8|kappa; bronze RRRLLL (Q(sqrt13))
# iff 13|kappa; RRL (Q(sqrt3)) iff 12|kappa. The 4|kappa unit tone's locus is read blind.
print("\nM1 — mechanism test (preregistered): does the resonance locus move with the trace field?")
WORDS = {"RL": "Q(sqrt5): 5|kap", "RRLL": "Q(sqrt2): 8|kap",
         "RRRLLL": "Q(sqrt13): 13|kap", "RRL": "Q(sqrt3): 12|kap"}
print("  kap: " + "  ".join(f"{wd:>7}" for wd in WORDS))
loci = {wd: [] for wd in WORDS}
for k in range(1, 24):
    w, S, T, C = stage(k)
    n = len(w)
    vals = []
    for wd in WORDS:
        M = rho_word(S, T, wd)
        t_odd = np.trace(M @ (np.eye(n) - C) / 2)
        vals.append(t_odd)
        if abs(t_odd) > 1e-7:
            loci[wd].append(k + 3)
    print(f"  {k+3:3d}: " + "  ".join(f"{v.real:+.4f}" if abs(v.imag) < 1e-7 else f"{v:+.3f}"
                                       for v in vals))
print("\n  nonzero loci (kappa):")
for wd, pred in WORDS.items():
    print(f"    {wd:>7} ({pred}):  {loci[wd]}")
