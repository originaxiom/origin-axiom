#!/usr/bin/env python3
"""W-P1, step 2: the two Gramians (W-P1b-G). Data-free; no frame is read; synthetic couplings only.

    python3 -I wp1b_gramians.py

Condition: relays/cards/CHAT1_W-P1_STEPS_conditions.md, "Step 2, the two Gramians" (committed before this script).
The Weil representations are wp1b_class_test.py's (its text run up to its group). D(a, b) = psi(3ab) X^a Z^b, B1953's.
The frame's transport is class 2's label action with the identity labelling: A(T): (a, b) -> (a, b - a),
A(S): (a, b) -> (-b, a).

  J1  per class, the K in GL(2, F_5) with rho_a(g) D(Kv) rho_a(g)^-1 = D(K A(g) v), no phase, g = T, S, all 24 v;
  J2  t(v, w) = tr(D(v) P D(w)^dagger) against zeta^(+3 omega) and zeta^(-3 omega), omega(v, w) = v1 w2 - v2 w1;
  J3  synthetic even couplings A(w) (seed 11): the Gramians over the 3 and the 2 of O_K = sum A(w) (x) D(Kw), within and
      between the classes; the difference against (sqrt 5 / 4)(S_1 - S_2); Parseval; the control with A(2w) = A(w);
  J4  ten steps of gamma = T S T^-1 S^-1 on synthetic covariant data, both classes: covariance residuals, G_3's ratios.
"""
import itertools
import pathlib

import numpy as np

src = (pathlib.Path(__file__).resolve().parent / "wp1b_class_test.py").read_text()
exec(compile(src[:src.index("Gs = {a: group(a)")], "wp1b_class_test.py", "exec"))

psi = lambda x: z ** (x % 5)
PTS = [(p, q) for p in range(5) for q in range(5) if (p, q) != (0, 0)]


def Dw(v):
    p, q = int(v[0]) % 5, int(v[1]) % 5
    return psi(3 * p * q) * np.linalg.matrix_power(Xs, p) @ np.linalg.matrix_power(Zs, q)


AT = np.array([[1, 0], [-1, 1]]) % 5
AS = np.array([[0, -1], [1, 0]]) % 5
inv2 = lambda M: (np.round(np.linalg.inv(M) * round(np.linalg.det(M))).astype(int) * pow(int(round(np.linalg.det(M))) % 5, -1, 5)) % 5
omega = lambda v, w: (v[0] * w[1] - v[1] * w[0]) % 5
E3, E2 = (np.eye(5) + P) / 2, (np.eye(5) - P) / 2

# J1
Ks = {}
for a in (1, 2):
    S, T = weil(a)
    Ks[a] = []
    for e in itertools.product(range(5), repeat=4):
        K = np.array(e).reshape(2, 2)
        d = int(round(np.linalg.det(K))) % 5
        if d == 0:
            continue
        ok = all(np.allclose(M @ Dw(K @ np.array(v)) @ np.linalg.inv(M), Dw(K @ (Ag @ np.array(v))), atol=1e-9)
                 for M, Ag in ((T, AT), (S, AS)) for v in PTS)
        if ok:
            Ks[a].append((K, d))
    print("J1 a=%d: K with no phase: %d; determinants %s; their square classes %s; the K: %s" % (
        a, len(Ks[a]), sorted({d for K, d in Ks[a]}), sorted({"square" if d in (1, 4) else "non-square" for K, d in Ks[a]}),
        [K.tolist() for K, d in Ks[a]]))

# J2
plus = max(abs(np.trace(Dw(v) @ P @ Dw(w).conj().T) - psi(3 * omega(v, w))) for v in PTS for w in PTS)
minus = max(abs(np.trace(Dw(v) @ P @ Dw(w).conj().T) - psi(-3 * omega(v, w))) for v in PTS for w in PTS)
print("J2: t(v, w) against zeta^(+3 omega): %.1e; against zeta^(-3 omega): %.1e" % (plus, minus))

# J3
rng = np.random.default_rng(11)
A = {}
for v in PTS:
    mv = ((-v[0]) % 5, (-v[1]) % 5)
    if mv in A:
        A[v] = A[mv]
    else:
        A[v] = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))


def O_of(Af, K):
    return sum(np.kron(Af[v], Dw(K @ np.array(v))) for v in PTS)


def gram(O, E):
    R = (O @ np.kron(np.eye(3), E) @ O.conj().T).reshape(3, 5, 3, 5)
    return np.einsum("ixkx->ik", R)


def ratios(H):
    e = np.sort(np.abs(np.linalg.eigvalsh((H + H.conj().T) / 2)))[::-1]
    return [float(np.sqrt(e[1] / e[0])), float(np.sqrt(e[2] / e[0]))]


def S_j(Af, j):
    return sum(Af[v] @ Af[w].conj().T for v in PTS for w in PTS if omega(v, w) in (j, (-j) % 5))


def run_J3(Af, label):
    G = {a: [(gram(O_of(Af, K), E3), gram(O_of(Af, K), E2)) for K, d in Ks[a]] for a in (1, 2)}
    within = max(max(np.abs(g3 - G[a][0][0]).max() for g3, g2 in G[a]) for a in (1, 2))
    plain = sum(Af[v] @ Af[v].conj().T for v in PTS)
    pars = max(np.abs(g3 + g2 - 5 * plain).max() for a in (1, 2) for g3, g2 in G[a])
    diff = G[1][0][0] - G[2][0][0]
    cf = np.sqrt(5) / 4 * (S_j(Af, 1) - S_j(Af, 2))
    print("J3 %s: within a class, the largest difference between its K's: %.1e; Parseval (G_3 + G_2 = 5 x plain) in "
          "both: %.1e; between the classes, |G_3(class 1) - G_3(class 2)|: %.3e; against (sqrt 5/4)(S_1 - S_2): "
          "%.1e, against minus it: %.1e" % (label, within, pars, np.abs(diff).max(), np.abs(diff - cf).max(),
                                           np.abs(diff + cf).max()))
    print("J3 %s: G_3's ratios: class 1 %s, class 2 %s; G_2's ratios: class 1 %s, class 2 %s; ||S_1 - S_2|| %.3e" % (
        label, ["%.6f" % x for x in ratios(G[1][0][0])], ["%.6f" % x for x in ratios(G[2][0][0])],
        ["%.6f" % x for x in ratios(G[1][0][1])], ["%.6f" % x for x in ratios(G[2][0][1])],
        np.abs(S_j(Af, 1) - S_j(Af, 2)).max()))


run_J3(A, "synthetic")
Ac = {v: sum(A[((c * v[0]) % 5, (c * v[1]) % 5)] for c in (1, 2, 3, 4)) / 4 for v in PTS}
run_J3(Ac, "control, A(2w) = A(w)")

# J4
def rand_unitary(n, r):
    Q, R = np.linalg.qr(r.normal(size=(n, n)) + 1j * r.normal(size=(n, n)))
    return Q * (np.diag(R) / np.abs(np.diag(R)))


r2 = np.random.default_rng(12)
U, V = rand_unitary(3, r2), rand_unitary(3, r2)
Ag = (AT @ AS @ inv2(AT) @ inv2(AS)) % 5
Agi = inv2(Ag)
ret = np.array_equal(np.linalg.matrix_power(Ag, 10) % 5, np.eye(2, dtype=int))
for a in (1, 2):
    S, T = weil(a)
    Rg = T @ S @ np.linalg.inv(T) @ np.linalg.inv(S)
    K = Ks[a][0][0]
    Ak = dict(A)
    O0 = O_of(Ak, K)
    r0 = ratios(gram(O0, E3))
    res, dr = [], []
    for k in range(1, 11):
        Ak = {v: U @ Ak[tuple(int(x) for x in (Agi @ np.array(v)) % 5)] @ V.conj().T for v in PTS}
        Ok = O_of(Ak, K)
        Uk, Vk, Rk = (np.linalg.matrix_power(M, k) for M in (U, V, Rg))
        res.append(np.abs(Ok - np.kron(Uk, Rk) @ O0 @ np.kron(Vk, Rk).conj().T).max())
        dr.append(max(abs(x - y) for x, y in zip(ratios(gram(Ok, E3)), r0)))
    print("J4 a=%d (K = %s): ten steps of gamma: largest covariance residual %.1e; G_3's ratios move by at most %.1e; "
          "A(gamma)^10 = I on the labels: %s; rho(gamma)^10 = I: %s" % (
              a, K.tolist(), max(res), max(dr), ret, np.allclose(np.linalg.matrix_power(Rg, 10), np.eye(5))))
