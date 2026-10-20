"""Main's independent check of the SM seat's W107 (N3 on the weave): every primitive positive word in L, R of length
2-16 up to rotation (Lyndon words), its lift T(w) on the triplet as the product of the record's letter lifts (B1621's
T_of on the single letters), its operator mean, the mean's line in the parity basis, and the weave's mean of means."""
import contextlib, importlib.util, io, pathlib
import numpy as np
from collections import Counter
FR = pathlib.Path(__file__).resolve().parents[3] / "frontier"
spec = importlib.util.spec_from_file_location("om", FR / "B1617_the_weave_at_tau_omega" / "verification" / "weave_at_omega.py")
om = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(om)
cp = om.cp
T_of = lambda auto: cp.restrict(om.M_of(auto), cp.TB)
TL, TR = T_of({"a": "a", "b": "ab"}), T_of({"a": "ab", "b": "b"})
Ta, Tb = T_of({"a": "a", "b": "abA"}), T_of({"a": "baB", "b": "b"})
_, P = np.linalg.eig(Ta + 0.3719 * Tb); P, _ = np.linalg.qr(P)          # B1621's parity basis

def lyndon(nmax):                                                        # Duval: Lyndon words over {L < R}
    w = [-1]
    while w:
        w[-1] += 1; m = len(w)
        if m >= 2: yield "".join("LR"[c] for c in w)
        while len(w) < nmax: w.append(w[len(w) - m])
        while w and w[-1] == 1: w.pop()

def order(M, cap=200):
    X = M.copy()
    for k in range(1, cap + 1):
        if np.allclose(X, np.eye(3), atol=1e-9): return k
        X = X @ M
    return None

words = list(lyndon(16)); odd = rank1 = 0; agree = 0; axes = Counter(); means = []
for w in words:
    M2 = np.eye(2, dtype=int)
    for ch in w: M2 = M2 @ (np.array([[1, 1], [0, 1]]) if ch == "L" else np.array([[1, 0], [1, 1]]))
    if int(np.trace(M2)) % 2 == 0: continue
    odd += 1
    T = np.eye(3, dtype=complex)
    for ch in w: T = T @ (TL if ch == "L" else TR)
    N = order(T); mean = sum(np.linalg.matrix_power(T, k) for k in range(N)) / N
    r = int(np.linalg.matrix_rank(mean, tol=1e-8))
    nL, nR = w.count("L"), w.count("R")
    agree += (r == 1) == ((nL - nR) % 8 == 0)
    if r == 1:
        rank1 += 1
        v = np.linalg.svd(P.conj().T @ mean @ P)[0][:, 0]; v = v / v[np.argmax(abs(v))]
        axes[tuple(int(np.sign(round(x.real, 6))) for x in v)] += 1
        assert np.allclose(abs(v), 1, atol=1e-6)                         # trimaximal: every entry of equal modulus
    means.append(P.conj().T @ mean @ P)
avg = sum(means) / len(means); off = np.abs(avg - np.diag(np.diag(avg))).max(); dg = np.abs(np.diag(avg))
print(f"threads (primitive positive words, length 2-16, up to rotation): {len(words)}; odd trace: {odd}")
print(f"rank-one tick means: {rank1}; zero: {odd - rank1}; 'rank one iff #L = #R mod 8' holds on {agree} of {odd}")
print(f"rank-one lines (signs in the parity basis, up to overall phase): {dict(axes)}")
print(f"the weave's mean of means: diagonal {np.round(dg, 4)}, largest off-diagonal {off:.4f} ({off / dg.max():.1%} of the diagonal)")
