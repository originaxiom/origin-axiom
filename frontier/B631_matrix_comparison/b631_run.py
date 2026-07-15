"""B631 — THE MATRIX COMPARISON (the interaction round's one authorized
comparison; runs once, mechanically, under the sealed design B630).

Protocol per COMPARISON_DESIGN.md: (0) verify BOTH seals (B629 values,
B630 design) against the hash ledger; (1) build |B|^2 from the sealed
closed form and |U_PMNS|^2 from the frozen PDG 2024 parameters; (2)
D_obs = min over the 72 alignments of RMS; (3) the 10^6-sample Haar-U(3)
null with the IDENTICAL statistic, seed 20260715; (4) report ALL NINE
deviations at the optimal alignment, two declared tiers (no verdict
weight) with the null's expected counts; (5) robustness rows R-a, R-b;
(6) the verdict by the locked table. One run; no reruns.
"""
import hashlib
import itertools
import math
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
LEDGER = os.path.join(HERE, "..", "B598_l85_campaign", "ARTIFACT_HASHES.txt")
ledger = open(LEDGER).read()
for rel in ("B629_interaction_values/SEALED_INTERACTION_VALUES.md",
            "B630_matrix_comparison_design/COMPARISON_DESIGN.md"):
    h = hashlib.sha256(
        open(os.path.join(HERE, "..", rel), "rb").read()).hexdigest()
    assert h in ledger, f"seal broken: {rel}"
    print(f"seal verified: {rel} sha256={h[:16]}...")

# ---- the framework matrix (B629 closed form) --------------------------------
A2 = np.array([(4 / 7) * math.sin(2 * math.pi * k / 7) ** 2 for k in (1, 2, 3)])
LATIN = np.array([[1, 2, 3], [2, 3, 1], [3, 1, 2]]) - 1
B2 = A2[LATIN]                       # |B_ij|^2, channel order (27, 351', 351)
assert np.allclose(B2.sum(axis=0), 1) and np.allclose(B2.sum(axis=1), 1)

# ---- the frozen measured table (B630 section 1) -----------------------------
s12sq, s23sq, s13sq = 0.307, 0.546, 0.0220     # B615 freeze, byte-for-byte
DELTA = 1.19 * math.pi                          # PDG 2024 central


def pmns_sq(s12sq, s23sq, s13sq, delta):
    s12, s23, s13 = map(math.sqrt, (s12sq, s23sq, s13sq))
    c12, c23, c13 = map(lambda s: math.sqrt(1 - s * s), (s12, s23, s13))
    e = complex(math.cos(delta), math.sin(delta))
    U = np.array([
        [c12 * c13, s12 * c13, s13 * e.conjugate()],
        [-s12 * c23 - c12 * s23 * s13 * e,
         c12 * c23 - s12 * s23 * s13 * e, s23 * c13],
        [s12 * s23 - c12 * c23 * s13 * e,
         -c12 * s23 - s12 * c23 * s13 * e, c23 * c13]])
    P = np.abs(U) ** 2
    assert np.allclose(P.sum(axis=0), 1) and np.allclose(P.sum(axis=1), 1)
    return P

PM = pmns_sq(s12sq, s23sq, s13sq, DELTA)
print("\nfrozen |U_PMNS|^2 (PDG 2024 central, delta=1.19pi):")
for r in PM:
    print("   " + "  ".join(f"{x:.6f}" for x in r))

# ---- the 72 alignments as flat index arrays ---------------------------------
PERMS = list(itertools.permutations(range(3)))
IDX = []
base = np.arange(9).reshape(3, 3)
for T in (base, base.T):
    for p in PERMS:
        for q in PERMS:
            IDX.append(T[np.ix_(p, q)].ravel())
IDX = np.array(IDX)                              # (72, 9)
pm_flat = PM.ravel()


def stat_D(flat9):
    """min over the 72 alignments of RMS(aligned - PMNS); returns (D, argmin)."""
    variants = flat9[IDX]                        # (72, 9)
    d = np.sqrt(((variants - pm_flat) ** 2).mean(axis=1))
    k = int(d.argmin())
    return float(d[k]), k


D_obs, k_obs = stat_D(B2.ravel())
n_align_distinct = len({tuple(np.round(B2.ravel()[i], 12)) for i in IDX})
print(f"\nD_obs = {D_obs:.8f}  (optimal alignment #{k_obs}; "
      f"{n_align_distinct} distinct framework variants of 72 — circulant degeneracy)")

# ---- the nine deviations at the optimal alignment (ALL reported) ------------
aligned = B2.ravel()[IDX[k_obs]].reshape(3, 3)
dev = np.abs(aligned - PM)
print("\naligned |B|^2 (framework, at the D-optimal alignment):")
for r in aligned:
    print("   " + "  ".join(f"{x:.6f}" for x in r))
print("per-entry |aligned - measured| (ALL NINE, no selection):")
for r in dev:
    print("   " + "  ".join(f"{x:.6f}" for x in r))
for tier in (0.01, 0.001):
    print(f"  matches at |Delta| <= {tier}: {int((dev <= tier).sum())}/9")

# ---- the Haar null (design section 4) ----------------------------------------
N = 10 ** 6
SEED = 20260715
rng = np.random.default_rng(SEED)
CHUNK = 20000
count_le = 0
tier_counts = {0.01: 0.0, 0.001: 0.0}
d_all = np.empty(N)
done = 0
while done < N:
    n = min(CHUNK, N - done)
    Z = (rng.standard_normal((n, 3, 3)) + 1j * rng.standard_normal((n, 3, 3))) / math.sqrt(2)
    Q, R = np.linalg.qr(Z)
    ph = np.einsum('nii->ni', R)
    Q = Q * (ph / np.abs(ph))[:, None, :]
    P = (np.abs(Q) ** 2).reshape(n, 9)           # doubly stochastic each
    variants = P[:, IDX]                         # (n, 72, 9)
    d = np.sqrt(((variants - pm_flat) ** 2).mean(axis=2))
    kmin = d.argmin(axis=1)
    dmin = d[np.arange(n), kmin]
    d_all[done:done + n] = dmin
    count_le += int((dmin <= D_obs).sum())
    best = variants[np.arange(n), kmin]          # (n, 9) optimal-aligned
    for tier in tier_counts:
        tier_counts[tier] += float((np.abs(best - pm_flat) <= tier).sum())
    done += n
p_D = (count_le + 1) / (N + 1)
print(f"\nHaar null: N={N}, seed={SEED}")
print(f"  null D: median={np.median(d_all):.6f}, 1%={np.quantile(d_all, 0.01):.6f}, "
      f"10%={np.quantile(d_all, 0.10):.6f}, min={d_all.min():.6f}")
print(f"  p_D = P(D_rand <= D_obs) = ({count_le}+1)/({N}+1) = {p_D:.6f}")
for tier, tot in tier_counts.items():
    print(f"  null expected matches (of 9) at |Delta| <= {tier}: {tot / N:.4f}")

# ---- robustness rows (design section 6; NO verdict weight) -------------------
RA = np.array([[0.681, 0.297, 0.0222], [0.109, 0.370, 0.521],
               [0.210, 0.333, 0.457]])
pm_save = pm_flat
pm_flat = RA.ravel()
D_ra, _ = stat_D(B2.ravel())
pm_flat = pm_save
print(f"\nR-a (handoff NuFIT-proxy table): D = {D_ra:.8f}")
for dl, name in [(0.0, "0"), (math.pi / 2, "pi/2"), (math.pi, "pi"),
                 (3 * math.pi / 2, "3pi/2")]:
    pm_flat = pmns_sq(s12sq, s23sq, s13sq, dl).ravel()
    D_dl, _ = stat_D(B2.ravel())
    print(f"R-b delta_CP = {name:>5}: D = {D_dl:.8f}")
pm_flat = pm_save

# ---- the verdict (design section 5, locked) ----------------------------------
if p_D < 0.01:
    verdict, word = "MATCH-CANDIDATE (to seat 4 before ANY claim)", "matches"
elif p_D < 0.1:
    verdict, word = ("AMBIGUOUS (suggestive-only; NO escalation; no further "
                     "SM comparison at this level without a new owner-level "
                     "directive + principled prereg)"), "does not match"
else:
    verdict = ("STRUCTURED-NULL (the stopping rule fires: the "
               "SM-comparison capability at this level is exhausted)")
    word = "does not match"
print(f"\n==== VERDICT (locked table): {verdict} ====")
print(f'\n"The 3x3 odd hearing form at E6 level 2 {word} the PMNS matrix '
      f'at the 1% tier, with null-model p-value {p_D:.4f}."')
print("\nB631 DONE — raw output banked; seat 4 reviews before any narrative.")
