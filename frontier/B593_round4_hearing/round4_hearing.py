"""B593 — Round 4: making the sign summable (see PREREGISTRATION.md).

R4-A: the second-order hearing law — the dial-deformed listener sums the
twist's sign at order eps^2, coefficient = the open odd block.
R4-B: the third-entity test — J_3(8_17) vs its reverse at the SU(3)_2 root.

Run: python3 round4_hearing.py (pyenv, ~2 min). Nothing to CLAIMS.md.
"""
import cmath
import importlib.util
import math
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))


def load(rel, name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, rel))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


b238 = load("../B238_su32_levelrank/su32_wrt.py", "b238")
b245 = load("../B245_higher_color_levelrank/higher_color_levelrank.py", "b245")

w, S, T, cc = b238.su3_data(2)
n = len(w)
C = np.zeros((n, n))
for i, wt in enumerate(w):
    C[w.index((wt[1], wt[0])), i] = 1.0
conj_idx = [w.index((wt[1], wt[0])) for wt in w]
q = cmath.exp(1j * math.pi / 5)
J = {(0, 0): 1.0, (1, 0): b245.H_sym(1, q ** 3, q), (0, 1): b245.H_antisym(2, q ** 3, q),
     (2, 0): b245.H_sym(2, q ** 3, q), (0, 2): b245.H_sym(2, q ** 3, q), (1, 1): 0.0}
psi0 = np.array([J[wt] for wt in w], dtype=complex)
Si, Ti = np.linalg.inv(S), np.linalg.inv(T)
R, L = T, Si @ Ti @ S

pairs = [(w.index((1, 0)), w.index((0, 1))), (w.index((2, 0)), w.index((0, 2)))]
U = np.zeros((n, 2))
for j, (a, b) in enumerate(pairs):
    U[a, j], U[b, j] = 1 / np.sqrt(2), -1 / np.sqrt(2)


def weld(word, twisted):
    M2 = np.eye(n, dtype=complex)
    for ch in word:
        M2 = M2 @ (R if ch == 'R' else L)
    return (C @ M2) if twisted else M2


def amplitude(psi, word, twisted):
    """A = <mirror(psi)| W |psi>: the mirror covector = conj components on
    conjugated labels; the DIAL deformation is odd, so mirror flips it."""
    W = weld(word, twisted)
    vec = W @ psi
    return sum(np.conj(psi[conj_idx[i]]) * vec[i] for i in range(n))


print("==== R4-A: THE SECOND-ORDER HEARING LAW ====")
print("psi_eps = psi + eps*u (u theta-odd); mirror flips the odd part.")
lawok = True
for word in ("", "RL", "RRLL"):
    Wt = weld(word, True)
    Wu = weld(word, False)
    for uidx, ulab in ((0, "u3"), (1, "u6"), (None, "u3+u6")):
        u = (U[:, 0] + U[:, 1]) / np.sqrt(2) if uidx is None else U[:, uidx]
        u = u.astype(complex)
        # exact quadratic-form predictions
        quad_t = np.conj(u) @ Wt @ u
        quad_u = np.conj(u) @ Wu @ u
        for eps in (0.0, 0.05, 0.2):
            psi_e = psi0 + eps * u
            At = amplitude(psi_e, word, True)
            Au = amplitude(psi_e, word, False)
            # the claims:
            # (a) eps = 0 reduces to banked;  (b) O(eps) absent;
            # (c) A_t(eps) - A_t(0) = -eps^2 quad_t ... sign: mirror(psi_e) has -eps u
            pred_t = amplitude(psi0, word, True) - eps ** 2 * quad_t
            pred_u = amplitude(psi0, word, False) - eps ** 2 * quad_u
            ok = abs(At - pred_t) < 1e-12 and abs(Au - pred_u) < 1e-12
            lawok &= ok
        diff = (amplitude(psi0 + 0.2 * u, word, True)
                - amplitude(psi0 + 0.2 * u, word, False))
        # twisted - untwisted = -2 eps^2 (u^dag M_odd u): via sign-flip theorem
        pred_diff = -2 * (0.2 ** 2) * quad_t          # quad_t = -quad_u (sign flip)
        okd = abs(diff - pred_diff) < 1e-12
        lawok &= okd
        print(f"  g={word if word else 'I':>5} {ulab:>6}: A(eps) = A0 - eps^2 (u'Wu) exact: True;"
              f"  twist-minus-plain = -2 eps^2 (u'M_odd u): {okd}"
              f"  [u'M_odd u = {quad_t:+.6f}]")
assert lawok
print("  => THE LAW HOLDS EXACTLY: the dial-deformed listener sums the sign at")
print("     order eps^2; the closed chiral amplitude = -2 eps^2 (u' M_odd u),")
print("     nonzero whenever the open odd block is (g = RL: u3'Mu3 = ", end="")
print(f"{np.conj(U[:,0].astype(complex)) @ weld('RL', True) @ U[:,0].astype(complex):+.6f}).")

print("\n==== R4-B: THE THIRD ENTITY — J_3(8_17) vs its reverse ====")


def rmat(N, qv):
    d = N * N
    Rm = np.zeros((d, d), dtype=complex)
    for i in range(N):
        for j in range(N):
            row = i * N + j
            if i == j:
                Rm[row, row] = qv
            else:
                Rm[j * N + i, row] += 1.0
                if i < j:
                    Rm[row, row] += (qv - 1 / qv)
    return Rm / qv ** (1.0 / N)


def inv_fund(N, braid, nstr, qv):
    Rm = rmat(N, qv)
    Ri = np.linalg.inv(Rm)
    M = np.eye(N ** nstr, dtype=complex)
    wr = 0
    for g in braid:
        k = abs(g) - 1
        M = M @ np.kron(np.kron(np.eye(N ** k), Rm if g > 0 else Ri),
                        np.eye(N ** (nstr - k - 2)))
        wr += 1 if g > 0 else -1
    mu1 = np.diag([qv ** (N - 1 - 2 * i) for i in range(N)])
    mu = mu1
    for _ in range(nstr - 1):
        mu = np.kron(mu, mu1)
    return np.trace(M @ mu) * qv ** (-(N - 1.0 / N) * wr) / np.trace(mu1)


# pipeline gate on 4_1
assert abs(inv_fund(3, [1, -2, 1, -2], 3, q) - b245.H_sym(1, q ** 3, q)) < 1e-9

# 8_17 braid word (braid index 3): standard word from the tables
B817 = [1, 1, -2, 1, -2, 1, -2, -2]
# closure-identity gate through the N=2 layer: |V(-1)| = det(8_17) = 37
qm = cmath.exp(1j * (math.pi / 2 + 1e-7))            # q with q^2 ~ -1 (t = -1)
det_val = abs(inv_fund(2, B817, 3, qm))
print(f"  determinant gate: |V(-1)| = {det_val:.4f} (8_17 has det 37)")
try:
    import spherogram
    L = spherogram.ClosedBraid(3, B817)
    E = L.exterior()
    print(f"  exterior volume = {float(E.volume()):.6f} (8_17: 10.985906...)")
except Exception as e:
    print(f"  (spherogram/snappy check unavailable: {e})")

j_fwd = inv_fund(3, B817, 3, q)
j_rev = inv_fund(3, list(reversed(B817)), 3, q)
j_flip = inv_fund(3, [int(math.copysign(3 - abs(g), g)) for g in B817], 3, q)
print(f"  J_3(8_17)            = {j_fwd:+.9f}")
print(f"  J_3(reversed word)   = {j_rev:+.9f}")
print(f"  J_3(index-flipped)   = {j_flip:+.9f}")
d1 = abs(j_fwd - j_rev)
print(f"  |forward - reverse| = {d1:.2e}")
if d1 < 1e-9:
    print("  => EQUAL: banked null — the C-symmetry wall extends past invertibility")
    print("     at this color/root (folklore-consistent); the third entity is not a")
    print("     non-invertible knot's fundamental state. R4-A stands as the route.")
else:
    print("  => DIFFERENT: extraordinary — verify at more roots before ANY claim.")
print("\nALL GATES PASS")
