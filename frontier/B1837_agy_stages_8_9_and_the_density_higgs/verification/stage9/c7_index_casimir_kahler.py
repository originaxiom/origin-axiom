"""S303 check c7 (value-free; first principles; random matrices only, no frame values).
 (1) Theorem 74's index arithmetic: for a line bundle V of degree d on a closed genus-g curve and ANY rank-2 B with
     deg B = 2g - 2, Riemann-Roch gives chi(V x B) = chi(V) + chi(V x K) = 2d; the lane's code sums (-chi(V) - chi(V x K))
     and (chi(V) + chi(V x K)), which is zero by construction for any integers.
 (2) SU(2): T^a = Q_a / (2i) on main's units: [T^a, T^b] = i eps_abc T^c, tr(T^a T^b) = delta/2, C_2(doublet) = 3/4.
 (3) R4 (Theorem 66): for ANY Y_u, Y_d and scalars k_u, k_d > 0, the one-Higgs Kahler-normalised cross-sector ratio
     s(sqrt(k_d) Y_d sqrt(k_d)) / s(sqrt(k_u) Y_u sqrt(k_u)) equals the two-Higgs (s(Y_d)/s(Y_u)) / tan beta with
     tan beta := k_u / k_d: an identity in one free positive number, whatever its name."""
import itertools, pathlib, sys
import numpy as np
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parents[4]) + "/frontier/B1827_the_framing_ledger/verification/recheck")
from identities_and_order5 import B

# (1)
bad = 0
for g in range(0, 6):
    for d in range(-20, 21):
        chiV = d + 1 - g; chiVK = (d + 2 * g - 2) + 1 - g; chiVB = (2 * d + (2 * g - 2)) + 2 * (1 - g)
        bad += (chiVB != chiV + chiVK) or (chiVB != 2 * d)
print("(1) RR: chi(V x B) = chi(V) + chi(V x K) = 2d fails in %d of %d (g, d) cases; the lane's sum is identically 0" % (bad, 6 * 41))
# (2)
T = [Q / 2j for Q in (B.QI, B.QJ, B.QK)]
lie = 0.0
for a, b in itertools.permutations(range(3), 2):
    c = 3 - a - b; e = 1 if (a, b, c) in ((0, 1, 2), (1, 2, 0), (2, 0, 1)) else -1
    lie = max(lie, np.abs(T[a] @ T[b] - T[b] @ T[a] - 1j * e * T[c]).max())
tr = max(abs(np.trace(T[a] @ T[b]) - (0.5 if a == b else 0)) for a in range(3) for b in range(3))
C2 = sum(t @ t for t in T)
print("(2) su(2) relations (up to the orientation of the units) dev %.1e; tr(T^a T^b) - delta/2 dev %.1e; C_2 = %s" % (
    min(lie, max(np.abs(T[a] @ T[b] - T[b] @ T[a] + 1j * (1 if (a, b) in ((0, 1), (1, 2), (2, 0)) else -1) * T[3 - a - b]).max()
                 for a, b in itertools.permutations(range(3), 2))), tr, np.round(np.diag(C2).real, 12)))
# (3)
rng = np.random.default_rng(3031107); worst = 0.0
for _ in range(200):
    Yu = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3)); Yd = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
    ku, kd = np.exp(rng.normal(size=2) * 3)
    s = lambda A: np.sort(np.linalg.svd(A, compute_uv=False))
    one = s(np.sqrt(kd) * Yd * np.sqrt(kd)) / s(np.sqrt(ku) * Yu * np.sqrt(ku))
    two = (s(Yd) / s(Yu)) / (ku / kd)
    worst = max(worst, np.abs(one / two - 1).max())
print("(3) one-Higgs Kahler ratio vs two-Higgs with tan beta := k_u/k_d, 200 random (Y_u, Y_d, k_u, k_d): worst %.1e" % worst)
