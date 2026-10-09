import itertools
import numpy as np
from setup import *

rng = np.random.default_rng(7)

print("== D1: products of inner_a, inner_b ==")
prods = []
for ea in range(2):
    for eb in range(2):
        prods.append(np.linalg.matrix_power(a_in, ea) @ np.linalg.matrix_power(b_in, eb))
print("all diagonal:", all(np.allclose(M, np.diag(np.diag(M))) for M in prods))
V = np.array([np.diag(M).real for M in prods])
print("products (diag entries):", V.tolist())
print("rank of span of all 4 products (incl. identity):", np.linalg.matrix_rank(V))
print("rank of span of the 3 nontrivial products {a,b,ab}:", np.linalg.matrix_rank(V[1:]))
# longer words
words = []
for L in range(1, 7):
    for w_ in itertools.product([a_in, b_in], repeat=L):
        M = np.eye(3, dtype=complex)
        for x in w_:
            M = M @ x
        words.append(np.diag(M).real)
print("rank of span of all words up to length 6:", np.linalg.matrix_rank(np.array(words)))
# is a,b,ab the full character-support: dimension of algebra generated
print("(they are 3 commuting involutions; diagonal algebra dim is 3)")

print("\n== D2: the tick P ==")
ev, evec = np.linalg.eig(P)
print("eigenvalues:", np.round(ev, 6))
print("is {1,w,w^2}:", all(any(abs(e - t) < 1e-9 for e in ev) for t in [1, w, w * w]))
print("|eigvec components|^2:", np.round(np.abs(evec) ** 2, 6).tolist())
# cycles the axes
print("P e0, e1, e2 ->", [int(np.argmax(np.abs(P[:, i]))) for i in range(3)], "(axis i -> i+1)")
# all 8 signed 3-cycles of det 1 (both orientations), z=1
cnt = 0
okall = True
for S, sg, p, s in signed_perms_det1():
    if sg == 1 and p != (0, 1, 2):
        cnt += 1
        evs = np.linalg.eigvals(S)
        _, V_ = np.linalg.eig(S)
        o1 = all(any(abs(e - t) < 1e-8 for e in evs) for t in [1, w, w * w])
        o2 = np.allclose(np.abs(V_) ** 2, 1 / 3, atol=1e-8)
        okall &= (o1 and o2)
print("all", cnt, "signed 3-cycles (det+1): eigenvalues {1,w,w^2} and |comp|^2=1/3:", okall)

print("\n== D3: operator mean (1/3)(I+P+P^2) ==")
Mn = (np.eye(3) + P + P @ P) / 3
print(np.round(Mn, 6).real.tolist())
print("rank:", np.linalg.matrix_rank(Mn), " |entries|:", np.round(np.abs(Mn), 6).flatten().tolist())
print("commutes with inner_a:", np.allclose(Mn @ a_in, a_in @ Mn), " ||[M,a]|| =", np.linalg.norm(Mn @ a_in - a_in @ Mn))
print("commutes with inner_b:", np.allclose(Mn @ b_in, b_in @ Mn))
# also for the other orientation / signed 3-cycles
for S, sg, p, s in signed_perms_det1():
    if sg == 1 and p != (0, 1, 2):
        Pm = S.astype(complex)
        Mn2 = (np.eye(3) + Pm + Pm @ Pm) / 3
        r = np.linalg.matrix_rank(Mn2)
        mods = np.round(np.abs(Mn2), 6)
        # for signed ones the mean may be a different rank-one; note it
        print("  signed 3-cycle p=%s s=%s: rank=%d, entry moduli all 1/3? %s, commutes with a: %s" % (
            p, s, r, np.allclose(mods, 1 / 3, atol=1e-6), np.allclose(Mn2 @ a_in, a_in @ Mn2)))

print("\n== D4: means on diagonal forms ==")


def mean_dirac(D, Pm):
    return sum(np.linalg.matrix_power(Pm, k).conj().T @ D @ np.linalg.matrix_power(Pm, k) for k in range(3)) / 3


def mean_T(D, Pm):
    return sum(np.linalg.matrix_power(Pm, k).T @ D @ np.linalg.matrix_power(Pm, k) for k in range(3)) / 3


worst = 0
for trial in range(2000):
    d = rng.normal(size=3) + 1j * rng.normal(size=3)
    if trial % 4 == 0:
        d = rng.normal(size=3)  # real
    if trial % 7 == 0:
        d = d - d.mean()  # traceless
    D = np.diag(d)
    for nm, f in [('Dirac', mean_dirac), ('TxT', mean_T), ('Sym2', mean_T)]:
        Mm = f(D, P)
        sv = np.linalg.svd(Mm, compute_uv=False)
        worst = max(worst, sv.max() - sv.min())
        # compare with (tr D/3) I
        assert np.allclose(Mm, np.trace(D) / 3 * np.eye(3), atol=1e-10)
print("max singular-value spread over 2000 diagonal D, 3 tensors (P=3-cycle, z=1):", worst)
print("mean = (trD/3) I verified. traceless D gives the ZERO matrix (singular values 0,0,0: equal, degenerate).")
# signed 3-cycles and with z phases
worst2 = 0
for S, sg, p, s in signed_perms_det1():
    if sg != 1:
        continue
    for z in [1, -1, 1j, -1j]:
        g = z * S.astype(complex)
        for trial in range(50):
            d = rng.normal(size=3) + 1j * rng.normal(size=3)
            D = np.diag(d)
            for nm, f in [('Dirac', mean_dirac), ('TxT', mean_T)]:
                sv = np.linalg.svd(f(D, g), compute_uv=False)
                worst2 = max(worst2, sv.max() - sv.min())
print("robustness over even-perm G elements (incl. identity-type) z in {1,-1,i,-i}: max spread =", worst2,
      "(nonzero allowed only where sum of g^k is not a clean cycle; see below)")

# for element of order 3 only: check mean for signed 3-cycles, with z=1
w3 = 0
for S, sg, p, s in signed_perms_det1():
    if sg == 1 and p != (0, 1, 2):
        g = S.astype(complex)
        for trial in range(50):
            d = rng.normal(size=3) + 1j * rng.normal(size=3)
            for f in (mean_dirac, mean_T):
                sv = np.linalg.svd(f(np.diag(d), g), compute_uv=False)
                w3 = max(w3, sv.max() - sv.min())
print("signed 3-cycles z=1 only: max spread =", w3)

print("\n== controls (criterion can fail) ==")
# non-diagonal M: mean is circulant, singular values a+2b, a-b, a-b
M = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
print("generic full M, Dirac mean singular values:", np.round(np.linalg.svd(mean_dirac(M, P), compute_uv=False), 4))
Msym = M + M.T
print("generic symmetric M, Sym2 mean singular values:", np.round(np.linalg.svd(mean_T(Msym, P), compute_uv=False), 4))
# a non-invariance-adapted average: mean over inner group acts on diag trivially (nothing to see)
d = rng.normal(size=3)
print("diag D itself (no averaging), sv:", np.round(np.linalg.svd(np.diag(d), compute_uv=False), 4))
