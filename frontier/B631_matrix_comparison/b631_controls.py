"""B631 addendum — PIPELINE CONTROLS (adversarial verification that the
sealed run's p = 0.700 is real, not a broken instrument's number).

The sealed comparison ran once and stands untouched; these controls
validate the INSTRUMENT (the statistic + the Haar sampler) per the house
standard ("the zero is real, not a broken pipeline's zero", B575):

C1 POSITIVE CONTROL — framework := the frozen |U_PMNS|² itself.
   Expect D = 0 exactly and p = 1/(N+1) (the minimum attainable).
C2 NEAR-MATCH CONTROL — framework := |U'|² for U' = U_PMNS·exp(iεK),
   small ε. Expect small D and p far below 0.01 (the instrument CAN
   fire MATCH-CANDIDATE on a genuinely close matrix).
C3 SAMPLER CALIBRATION — Haar-U(3) moduli²: each |U_ij|² must follow
   Beta(1,2) (mean 1/3, P(x ≤ t) = 1 − (1−t)²) — the known law.
C4 SEED ROBUSTNESS — the sealed p under two fresh seeds; the verdict
   band must not move.
C5 PATH CONSISTENCY — the observed-path statistic equals the
   batched/vectorized-path statistic on the same matrix.
"""
import itertools
import math

import numpy as np

A2 = np.array([(4 / 7) * math.sin(2 * math.pi * k / 7) ** 2 for k in (1, 2, 3)])
B2 = A2[np.array([[0, 1, 2], [1, 2, 0], [2, 0, 1]])]

s12, s23, s13 = map(math.sqrt, (0.307, 0.546, 0.0220))
c12, c23, c13 = (math.sqrt(1 - v * v) for v in (s12, s23, s13))
e = complex(math.cos(1.19 * math.pi), math.sin(1.19 * math.pi))
U_PMNS = np.array([
    [c12 * c13, s12 * c13, s13 * e.conjugate()],
    [-s12 * c23 - c12 * s23 * s13 * e,
     c12 * c23 - s12 * s23 * s13 * e, s23 * c13],
    [s12 * s23 - c12 * c23 * s13 * e,
     -c12 * s23 - s12 * c23 * s13 * e, c23 * c13]])
PM = np.abs(U_PMNS) ** 2
pm_flat = PM.ravel()

PERMS = list(itertools.permutations(range(3)))
base = np.arange(9).reshape(3, 3)
IDX = np.array([T[np.ix_(p, q)].ravel()
                for T in (base, base.T) for p in PERMS for q in PERMS])


def stat_D(flat9, target=None):
    t = pm_flat if target is None else target
    d = np.sqrt(((flat9[IDX] - t) ** 2).mean(axis=1))
    return float(d.min())


def null_p(D_obs, N, seed):
    rng = np.random.default_rng(seed)
    count, done, CHUNK = 0, 0, 20000
    while done < N:
        n = min(CHUNK, N - done)
        Z = (rng.standard_normal((n, 3, 3))
             + 1j * rng.standard_normal((n, 3, 3))) / math.sqrt(2)
        Q, R = np.linalg.qr(Z)
        ph = np.einsum('nii->ni', R)
        Q = Q * (ph / np.abs(ph))[:, None, :]
        P = (np.abs(Q) ** 2).reshape(n, 9)
        dm = np.sqrt(((P[:, IDX] - pm_flat) ** 2).mean(axis=2)).min(axis=1)
        count += int((dm <= D_obs).sum())
        done += n
    return (count + 1) / (N + 1)


print("== C1 positive control: framework = |U_PMNS|^2 itself ==")
D_self = stat_D(pm_flat)
p_self = null_p(D_self, 100000, 1)
print(f"  D = {D_self:.3e} (expect 0), p = {p_self:.6f} "
      f"(expect {1/100001:.6f})")
assert D_self < 1e-12 and abs(p_self - 1 / 100001) < 1e-9

print("== C2 near-match control: U' = U_PMNS.exp(i eps K), eps = 0.02 ==")
rng = np.random.default_rng(7)
K = rng.standard_normal((3, 3)) + 1j * rng.standard_normal((3, 3))
K = (K + K.conj().T) / 2
w, V = np.linalg.eigh(K)
for eps in (0.02, 0.05):
    Ue = U_PMNS @ (V @ np.diag(np.exp(1j * eps * w)) @ V.conj().T)
    Dn = stat_D((np.abs(Ue) ** 2).ravel())
    pn = null_p(Dn, 100000, 2)
    print(f"  eps = {eps}: D = {Dn:.6f}, p = {pn:.6f}")
    assert pn < 0.01, "instrument fails to fire on a genuinely close matrix"

print("== C3 sampler calibration: |U_ij|^2 ~ Beta(1,2) ==")
rng = np.random.default_rng(3)
Z = (rng.standard_normal((200000, 3, 3))
     + 1j * rng.standard_normal((200000, 3, 3))) / math.sqrt(2)
Q, R = np.linalg.qr(Z)
ph = np.einsum('nii->ni', R)
Q = Q * (ph / np.abs(ph))[:, None, :]
P = np.abs(Q) ** 2
for (i, j) in [(0, 0), (1, 2), (2, 1)]:
    x = P[:, i, j]
    m, cdf_half = x.mean(), (x <= 0.5).mean()
    print(f"  entry ({i},{j}): mean = {m:.4f} (expect 0.3333), "
          f"P(x<=0.5) = {cdf_half:.4f} (expect 0.7500)")
    assert abs(m - 1 / 3) < 0.005 and abs(cdf_half - 0.75) < 0.005
rowsums = P.sum(axis=2)
assert np.allclose(rowsums, 1, atol=1e-10), "sampler not unitary"
print("  row sums = 1 exactly (unitarity)")

print("== C4 seed robustness of the sealed p ==")
D_obs = stat_D(B2.ravel())
for seed in (101, 202):
    p = null_p(D_obs, 200000, seed)
    print(f"  seed {seed}: p = {p:.4f}")
    assert 0.68 < p < 0.72, "verdict band moved under reseeding"

print("== C5 path consistency ==")
flat = B2.ravel()
d_loop = min(math.sqrt(sum((flat[i] - pm_flat[k]) ** 2
                           for k, i in enumerate(row)) / 9) for row in IDX)
assert abs(d_loop - D_obs) < 1e-15
print(f"  loop path D = {d_loop:.8f} == vectorized D = {D_obs:.8f}")

print("\nALL CONTROLS PASS — the sealed p = 0.700 is the instrument's true "
      "reading, not an artifact.")
