"""B1957: the physical lane's package 'registered domain index join' (2026-11-16), its PROOF.md ('the residual
registering action on actual sections'): the finite algebra of the hand derivation, rebuilt on main.  Exact where it
can be (Gaussian rationals through sympy-free integer arithmetic on quaternion units; numpy for random controls).
What is NOT here: any analysis (operators, domains, kernels on the cusp).  The note itself says it removes no
foundational input.
 J1  the residual of an inner element: with R_h = 1_3 (x) rho(h) and a lift B with B R_k B^-1 = R_(h k h^-1), the
     operator C_h = B R_h^-1 commutes with every R_k and C_(hk) = C_h C_k.  For the two lifts of the note on Q8:
     B^axis = O_g (x) g gives C_h = O_(rho(h)) (x) 1_2, of signs (1, -1, -1) at i and (-1, 1, -1) at j on the axes
     (i, j, k); B^perm = Pi_g (x) g gives C_h = 1.
 J2  on the binary octahedral group (48 elements): O_g, the conjugation on the three imaginary axes, is a signed
     permutation of determinant 1; its unsigned permutation Pi_g is a homomorphism; on Q8 Pi = 1; a quarter-turn has
     det Pi = -1.
 J3  the bracket: for an orthogonal A, (A x) x (A y) = det(A) A (x x y) (random A of both signs).
 J4  the coupling Y(S, M)_ab = sum_mn (C_a^T eps S C_b)_mn M_mn with (C_1, C_2, C_3) = (j, i, k): its span over all
     S, M is all of M_3(C) (rank 9), and already with S traceless; identity (10a) for the quaternion basis.
 J5  covariance: Y(g S g^-1, g M g^T) = O_g Y(S, M) O_g^T for g in SL(2, C) (random g).
 J6  the note's two hand values of Y, and its rejecting control: at J_b (rho = j) the signed slots satisfy
     A^T O Y O^T A = Y and the unsigned ones do not.
 J7  the classification: the only (L, R) with L^T Y R = Y for every Y in M_3(C) are L = c, R = 1/c scalars
     (the solution space of the linear system for fixed L has the stated form: checked as the commutant of M_3)."""
import functools, itertools
import numpy as np
print = functools.partial(print, flush=True)
I2 = np.eye(2, dtype=complex); qi = np.array([[1j, 0], [0, -1j]]); qj = np.array([[0, 1], [-1, 0]], dtype=complex); qk = qi @ qj; eps = qj.copy()
Q = [qi, qj, qk]                       # the oriented basis: Q_a Q_b = -delta_ab + eps_abc Q_c
Cs = [qj, qi, qk]                      # the note's order (j, i, k)


def O_of(g, basis=Q):
    """conjugation X -> g X g^-1 on the span of the basis (complex 3 x 3; real orthogonal for g in SU(2))"""
    gi = np.linalg.inv(g); out = np.zeros((3, 3), dtype=complex)
    for b, X in enumerate(basis):
        Y = g @ X @ gi
        for a, Z in enumerate(basis): out[a, b] = -0.5 * np.trace(Y @ Z)       # tr(Q_a Q_b) = -2 delta
    return out


def Yc(S, M):
    return np.array([[np.sum((Cs[a].T @ eps @ S @ Cs[b]) * M) for b in range(3)] for a in range(3)])


def binary_octahedral():
    r = 1 / np.sqrt(2); gens = [qi, qj, (I2 + qi + qj + qk) / 2, (I2 + qi) * r]; G = [I2]
    grew = True
    while grew:
        grew = False
        for g in list(G):
            for h in gens:
                x = g @ h
                if not any(np.allclose(x, y) for y in G): G.append(x); grew = True
    return G


if __name__ == "__main__":
    rng = np.random.default_rng(8)
    # J2
    G = binary_octahedral(); Os = [O_of(g).real for g in G]; signed = all(np.allclose(np.abs(O).sum(axis=0), 1) and np.allclose(np.abs(O).sum(axis=1), 1) and np.allclose(np.abs(O) ** 2, np.abs(O)) and abs(np.linalg.det(O) - 1) < 1e-9 for O in Os)
    Pis = [np.abs(O).round() for O in Os]; idx = lambda x: next(i for i, y in enumerate(G) if np.allclose(x, y))
    hom = all(np.allclose(Pis[idx(G[a] @ G[b])], Pis[a] @ Pis[b]) for a in range(len(G)) for b in range(len(G)))
    q8 = [s * x for s in (1, -1) for x in (I2, qi, qj, qk)]; piq = all(np.allclose(Pis[idx(h)], np.eye(3)) for h in q8); quarter = (I2 + qi) / np.sqrt(2)
    print("J2: the binary octahedral group has %d elements; every O_g is a signed permutation of determinant 1: %s; g -> Pi_g is a homomorphism: %s; Pi = 1 on Q8: %s; det Pi at the quarter-turn (1 + i)/sqrt 2: %.0f; the signs of O at i and at j on (i, j, k): %s, %s" % (
        len(G), signed, hom, piq, np.linalg.det(Pis[idx(quarter)]), np.diag(O_of(qi).real).round().astype(int).tolist(), np.diag(O_of(qj).real).round().astype(int).tolist()))
    # J1
    okc = True; mult = True; cax = {}; cperm = True
    for h in q8:
        Rh = np.kron(np.eye(3), h); Bax = np.kron(O_of(h).real, h); Bpm = np.kron(Pis[idx(h)], h); Cax = Bax @ np.linalg.inv(Rh); Cpm = Bpm @ np.linalg.inv(Rh); cax[idx(h)] = Cax
        okc &= np.allclose(Cax, np.kron(O_of(h).real, np.eye(2))); cperm &= np.allclose(Cpm, np.eye(6))
        for k in q8:
            Rk = np.kron(np.eye(3), k); okc &= np.allclose(Cax @ Rk, Rk @ Cax) and np.allclose(Bax @ Rk @ np.linalg.inv(Bax), np.kron(np.eye(3), h @ k @ np.linalg.inv(h)))
    for h in q8:
        for k in q8: mult &= np.allclose(cax[idx(h @ k)], cax[idx(h)] @ cax[idx(k)])
    print("J1: on Q8: the axis lift intertwines R as the inner automorphism, its residual is O (x) 1 and commutes with every R_k: %s; the residual is multiplicative: %s; the permutation lift's residual is the identity: %s" % (okc, mult, cperm))
    # J3
    worst = 0.0; dets = set()
    for trial in range(200):
        A, _r = np.linalg.qr(rng.normal(size=(3, 3)))
        if trial % 2: A = A @ np.diag([-1.0, 1.0, 1.0])                 # the QR factor of a 3 x 3 matrix always has determinant +1: half the samples are reflected
        x, y = rng.normal(size=3), rng.normal(size=3); d = np.linalg.det(A); dets.add(int(round(d))); worst = max(worst, np.max(np.abs(np.cross(A @ x, A @ y) - d * A @ np.cross(x, y))))
    print("J3: (A x) x (A y) = det(A) A (x x y) on 200 random orthogonal A (determinants %s): largest difference %.1e" % (sorted(dets), worst))
    # J4
    E = [np.array([[1.0 if (r, c) == (p, q) else 0.0 for c in range(2)] for r in range(2)], dtype=complex) for p in range(2) for q in range(2)]
    full = np.array([Yc(S, M).ravel() for S in E for M in E]); tl = np.array([Yc(S, M).ravel() for S in Q for M in E])
    z = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3)); lc = np.zeros((3, 3, 3)); 
    for a, b, c in itertools.permutations(range(3)): lc[a, b, c] = np.linalg.det(np.eye(3)[[a, b, c]])
    w10 = 0.0
    for d in range(3):
        lhs = sum(z[a, b] * Q[a] @ Q[d] @ Q[b] for a in range(3) for b in range(3))
        rhs = np.trace(z) * Q[d] - sum(z[d, b] * Q[b] for b in range(3)) - sum(z[a, d] * Q[a] for a in range(3)) + sum(z[a, b] * lc[a, b, d] for a in range(3) for b in range(3)) * I2
        w10 = max(w10, np.max(np.abs(lhs - rhs)))
    print("J4: the span of Y(S, M) over all S, M has rank %d; with S traceless, rank %d; identity (10a) for a random z: largest difference %.1e" % (np.linalg.matrix_rank(full), np.linalg.matrix_rank(tl), w10))
    # J5
    w9 = 0.0
    for _ in range(100):
        g = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2)); g = g / np.sqrt(np.linalg.det(g)); S = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2)); Mm = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
        Og = O_of(g, Cs); w9 = max(w9, np.max(np.abs(Yc(g @ S @ np.linalg.inv(g), g @ Mm @ g.T) - Og @ Yc(S, Mm) @ Og.T)), np.max(np.abs(Og.T @ Og - np.eye(3))))
    print("J5: Y(g S g^-1, g M g^T) = O_g Y O_g^T and O_g^T O_g = 1 on 100 random g in SL(2, C): largest difference %.1e" % w9)
    # J6
    S0 = np.array([[1, 0], [0, 0]], dtype=complex); M0 = np.array([[0, -1], [0, 0]], dtype=complex); Y0 = Yc(S0, M0); Y1 = Yc(np.diag([1, -1]).astype(complex), M0)
    want0 = np.array([[-1, 0, -1j], [0, 0, 0], [1j, 0, -1]]); want1 = np.array([[-1, 0, -1j], [0, 1, 0], [1j, 0, -1]])
    Oj = O_of(qj, Cs).real.round(); moved0 = Oj @ Y0 @ Oj.T; moved1 = Oj @ Y1 @ Oj.T
    print("J6: Y0 and the traceless-S value are the note's: %s, %s; O at j in the order (j, i, k): %s; the unsigned slots fail (O Y O^T differs from Y by %.0f and %.0f); the signed slots hold: %s" % (
        np.allclose(Y0, want0), np.allclose(Y1, want1), np.diag(Oj).astype(int).tolist(), np.max(np.abs(moved0 - Y0)), np.max(np.abs(moved1 - Y1)), np.allclose(Oj.T @ moved0 @ Oj, Y0) and np.allclose(Oj.T @ moved1 @ Oj, Y1)))
    # J7: L^T Y L^-T = Y for all Y: the commutant of M_3 is the scalars
    basis = [np.array([[1.0 if (r, c) == (p, q) else 0.0 for c in range(3)] for r in range(3)]) for p in range(3) for q in range(3)]
    rows = []
    for Yb in basis: rows.append(np.kron(np.eye(3), Yb) - np.kron(Yb.T, np.eye(3)))        # vec(Y X - X Y) with X unknown
    print("J7: the matrices commuting with all of M_3 form a space of dimension %d (the scalars)" % (9 - np.linalg.matrix_rank(np.vstack(rows))))
