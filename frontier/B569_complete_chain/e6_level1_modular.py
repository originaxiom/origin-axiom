"""B569 — the E6 level-1 modular image of the figure-eight monodromy, done consistently.

The incoming 'Complete Chain' handoff evaluated rho(A1) = T^2 S T in what it called
"E6 level-1 modular data": S = w^{ab}/sqrt(3), T = diag(-i, e^{i pi/6}, e^{i pi/6})
(i.e. conformal weight h(27) = 1/3 with central charge c = 6). That pairing is
INCONSISTENT: h = 1/3 is the SU(3)_1 weight (c = 2); the true E6_1 weight is
h(27) = 2/3 (proved here from the E6 root system). With the hybrid data
(ST)^3 != S^2, so "rho(A1)" depends on the SL(2,Z) word chosen for A1:
  A1 = T^2 S T           gives  Z = -1
  A1 = T (S T^-1 S^-1)   gives  Z = +1     (same group element!)
The handoff's headline Z = -1 is a word artifact.

The CONSISTENT E6_1 data (S = w^{-ab}/sqrt3, h = 2/3, c = 6) is a genuine
SL(2,Z) rep (word-independent). Then:
  rho(A1): unitary, order 4, commutes with theta = (27 <-> 27bar),
  theta-even block eigenvalues {+i, -i}, theta-odd eigenvalue +1,   Z = +1.
The conjugate theory SU(3)_1 (S = w^{ab}, h = 1/3, c = 2) gives the same Z = +1
(the trace is real). There is no -1: the claimed "chirality bit" does not exist.

Placement: Tr rho(A1) is the level-1 invariant of the CLOSED torus bundle with
monodromy A1 (a Sol manifold — the fiber Dehn-filling of the knot complement),
not of M3 itself; and the 2-dim theta-even block carries no F4 action (the
smallest faithful F4 rep is 26). Unitarity here is the measurement face
(the two-faces theorem, PR #884) — the algebra-face real-form wall (B565-H1)
is untouched.

Run: python3 frontier/B569_complete_chain/e6_level1_modular.py
"""
import numpy as np
import sympy as sp

# ---------------------------------------------------------------- h(27) = 2/3, exactly
C6 = sp.Matrix([
    [ 2,  0, -1,  0,  0,  0],
    [ 0,  2,  0, -1,  0,  0],
    [-1,  0,  2, -1,  0,  0],
    [ 0, -1, -1,  2, -1,  0],
    [ 0,  0,  0, -1,  2, -1],
    [ 0,  0,  0,  0, -1,  2]])          # Bourbaki E6 (node 2 = the branch node)


def roots_from_cartan(C):
    """All roots, in simple-root coordinates, by reflection closure.
    s_j(x) = x - <x, alpha_j^vee> alpha_j with <alpha_i, alpha_j^vee> = C[i,j]."""
    n = C.shape[0]
    allr = set()
    frontier = set()
    for j in range(n):
        e = tuple(1 if i == j else 0 for i in range(n))
        allr.add(e)
        frontier.add(e)
    while frontier:
        new = set()
        for rt in frontier:
            for j in range(n):
                pj = sum(C[i, j] * rt[i] for i in range(n))
                y = list(rt)
                y[j] -= pj
                ty = tuple(y)
                if ty not in allr:
                    allr.add(ty)
                    new.add(ty)
        frontier = new
    return allr


def e6_level1_weight():
    """Weyl dim formula at each fundamental node; return {node: (dim, h at level 1)}."""
    G = C6.inv()                                   # (w_i, w_j) = C^{-1} (simply-laced)
    roots = roots_from_cartan(C6)
    pos = [sp.Matrix(r) for r in roots if all(c >= 0 for c in r)]
    ip = lambda x, y: (x.T * C6 * y)[0, 0]         # Gram = Cartan (norms 2)
    rho = sp.Rational(1, 2) * sum(pos, sp.zeros(6, 1))
    out = {}
    for node in range(6):
        lam = G[:, node]
        dim = sp.prod([sp.Rational(ip(lam + rho, a), ip(rho, a)) for a in pos])
        h = sp.Rational(ip(lam, lam) + 2 * ip(lam, rho), 2 * (1 + 12))  # k=1, h_vee=12
        out[node + 1] = (dim, h)
    return len(roots), out


# ---------------------------------------------------------------- the modular data
W3 = np.exp(2j * np.pi / 3)


def modular_pair(s_sign, h27, c):
    S = np.array([[W3 ** (s_sign * a * b) for b in range(3)] for a in range(3)]) / np.sqrt(3)
    T = np.diag([np.exp(2j * np.pi * (h - c / 24)) for h in (0, h27, h27)])
    return S, T


def is_genuine_rep(S, T, tol=1e-12):
    r1 = np.linalg.norm(np.linalg.matrix_power(S @ T, 3) - S @ S)
    r2 = np.linalg.norm(np.linalg.matrix_power(S, 4) - np.eye(3))
    return r1 < tol and r2 < tol, r1


def rho_two_words(S, T):
    w1 = T @ T @ S @ T                                     # A1 = T^2 S T
    w2 = T @ S @ np.linalg.inv(T) @ np.linalg.inv(S)       # A1 = T (S T^-1 S^-1)
    return w1, w2


if __name__ == '__main__':
    nroots, table = e6_level1_weight()
    print(f"E6: {nroots} roots; level-1 conformal weights by node:")
    for node, (dim, h) in table.items():
        tag = "  <-- the 27" if dim == 27 else ""
        print(f"  node {node}: dim {dim}, h = {h}{tag}")

    print("\n(S-sign, h, c) consistency scan:")
    for name, args in [("seat hybrid (w^ab, 1/3, 6)", (1, 1 / 3, 6)),
                       ("SU(3)_1     (w^ab, 1/3, 2)", (1, 1 / 3, 2)),
                       ("E6_1       (w^-ab, 2/3, 6)", (-1, 2 / 3, 6))]:
        S, T = modular_pair(*args)
        ok, r = is_genuine_rep(S, T)
        w1, w2 = rho_two_words(S, T)
        print(f"  {name}: genuine rep = {ok} (||(ST)^3 - S^2|| = {r:.2e}); "
              f"Z(word1) = {np.trace(w1):.4f}, Z(word2) = {np.trace(w2):.4f}")

    S, T = modular_pair(-1, 2 / 3, 6)
    rho, _ = rho_two_words(S, T)
    C = np.array([[1, 0, 0], [0, 0, 1], [0, 1, 0]])
    vodd = np.array([0, 1, -1]) / np.sqrt(2)
    print("\nconsistent E6_1: rho(A1) eigenvalues", np.round(np.linalg.eigvals(rho), 8))
    print("  theta-odd eigenvalue:", np.round((rho @ vodd)[1] * np.sqrt(2), 8))
    print("  rho^4 = I:", np.linalg.norm(np.linalg.matrix_power(rho, 4) - np.eye(3)) < 1e-12,
          " (matches ord(A1) = 4 in SL(2, Z/3))")
