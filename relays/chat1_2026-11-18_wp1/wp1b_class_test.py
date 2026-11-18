#!/usr/bin/env python3
"""W-P1, step 2 (W-P1b): the class test, at the level of the representation. Data-free; no frame is read.

    python3 -I wp1b_class_test.py

Condition: relays/cards/CHAT1_W-P1_STEPS_conditions.md, step 2 (committed before this script). Level 5's Weil
representation on functions on F_5 in the class of the form a x^2 / 5 (a = 1, the knot's; a = 2, the act's with the
cover's pairing; B1955 § 2): rho(T) = diag zeta^(a x^2), rho(S) = c F with F[x, y] = zeta^(-2 a x y), c fixed by
rho(S)^2 = (rho(S) rho(T))^3 (as wp1_weil.py). The Heisenberg operators are D(p, q) = X^p Z^q, (X f)(x) = f(x - 1),
(Z f)(x) = zeta^x f(x): the labels of the record's lines of order 5 (B1952: the lines are the Weyl operators).

  C0  the group: SL(2, F_5) reached from S and T, 120 elements, and the representation genuine (two words reaching one
      element give one matrix);
  C1  the class-invariant quantities, in both classes: det rho(g) = 1 for all g; rho(-I) is the parity; the even and
      odd parts' dimensions; the commutant of rho(G) (dimension, and that it is spanned by I and the parity);
      6Y = (I - 5P)/2's eigenvalues; |tr rho(g)|^2 against the number of points of F_5^2 that g fixes, for all g; the
      signature tr R(T^2)/tr R(T)^2 for R = W (x) conj(W);
  C2  the label action: for each g, the permutation pi_a(g) of the 25 labels with rho_a(g) D(v) rho_a(g)^-1 =
      phi_a(g, v) D(pi_a(g) v), and its phases phi_a; whether pi_1 = pi_2 and phi_1 = phi_2 for all g and v; and
      whether pi_a(g) is g itself acting on (p, q) or another matrix;
  C3  the class-dependent quantities: on how many elements tr rho_1(g) and tr rho_2(g) differ; whether
      tr rho_2(g) = tr rho_1(h g h^-1) for h = diag(2, 1) (determinant 2, a non-residue) for all g; the even part's
      traces on the elements of order 5 in each class;
  C4  the controls the condition names: tr rho(gamma^2) must differ between the classes; det and rho(-I) must not;
  C5  the golden iteration over one period, gamma = T S T^-1 S^-1 = [[2, 1], [1, 1]]: tr rho_a(gamma^k) for
      k = 1 to 10, and the dimension of each class's fixed space of rho_a(gamma) and its parity.
"""
import itertools

import numpy as np

z = np.exp(2j * np.pi / 5)
X5 = np.arange(5)
P = np.zeros((5, 5)); P[(-X5) % 5, X5] = 1
EVEN = np.array([[1, 0, 0, 0, 0], [0, 1, 0, 0, 1], [0, 0, 1, 1, 0]], float).T / np.array([1, np.sqrt(2), np.sqrt(2)])
ODD = np.array([[0, 1, 0, 0, -1], [0, 0, 1, -1, 0]], float).T / np.sqrt(2)
Xs = np.zeros((5, 5)); Xs[(X5 + 1) % 5, X5] = 1           # (X f)(x) = f(x - 1)
Zs = np.diag(z ** X5)


def D(p, q):
    return np.linalg.matrix_power(Xs, p % 5) @ np.linalg.matrix_power(Zs, q % 5)


def weil(a):
    T = np.diag(z ** ((a * X5 * X5) % 5))
    F = z ** ((-2 * a * np.outer(X5, X5)) % 5)
    A, B = F @ F, np.linalg.matrix_power(F @ T, 3)
    k = np.argmax(np.abs(B))
    S = (A.flat[k] / B.flat[k]) * F
    assert np.allclose(S @ S, np.linalg.matrix_power(S @ T, 3))
    return S, T


Sg = np.array([[0, -1], [1, 0]]); Tg = np.array([[1, 1], [0, 1]])
key = lambda g: tuple((g % 5).ravel())


def group(a):
    S, T = weil(a)
    G = {key(np.eye(2, dtype=int)): (np.eye(2, dtype=int), np.eye(5, dtype=complex))}
    front, clashes, arrivals = [key(np.eye(2, dtype=int))], 0, 0
    while front:
        nxt = []
        for k in front:
            g, M = G[k]
            for gg, MM in ((Sg, S), (Tg, T)):
                h, N = (gg @ g) % 5, MM @ M
                kk = key(h)
                if kk in G:
                    arrivals += 1
                    clashes += not np.allclose(G[kk][1], N, atol=1e-9)
                else:
                    G[kk] = (h, N); nxt.append(kk)
        front = nxt
    return G, clashes, arrivals


def nfix(g):
    return sum(1 for v in itertools.product(range(5), repeat=2) if tuple((g @ np.array(v)) % 5) == v)


def label_action(M):
    """the permutation of labels and the phases: M D(v) M^-1 = phi D(w)"""
    Mi = np.linalg.inv(M)
    out = {}
    for v in itertools.product(range(5), repeat=2):
        C = M @ D(*v) @ Mi
        for w in itertools.product(range(5), repeat=2):
            Dw = D(*w)
            ph = np.vdot(Dw, C) / 5
            if abs(abs(ph) - 1) < 1e-9 and np.allclose(C, ph * Dw, atol=1e-9):
                out[v] = (w, ph)
                break
        else:
            raise AssertionError("no label for %s" % (v,))
    return out


Gs = {a: group(a) for a in (1, 2)}
for a in (1, 2):
    G, cl, arr = Gs[a]
    print("C0 a=%d: elements %d; repeated arrivals %d; clashes %d" % (a, len(G), arr, cl))

for a in (1, 2):
    G = Gs[a][0]
    dets = max(abs(np.linalg.det(M) - 1) for g, M in G.values())
    mI = G[key(-np.eye(2, dtype=int))][1]
    # commutant of the image: solve M X = X M for all generators
    S, T = weil(a)
    K = np.vstack([np.kron(np.eye(5), A) - np.kron(A.T, np.eye(5)) for A in (S, T)])
    dimc = 25 - np.linalg.matrix_rank(K, tol=1e-8)
    Y6 = (np.eye(5) - 5 * P) / 2
    chi2 = max(abs(abs(np.trace(M)) ** 2 - nfix(g)) for g, M in G.values())
    t1, t2 = np.trace(T), np.trace(T @ T)
    sig = (t2 * np.conj(t2)) / (t1 * np.conj(t1)) ** 2
    print("C1 a=%d: max |det - 1| %.1e; rho(-I) = parity %s; even/odd dims %d/%d; commutant dim %d, I and P in it %s; "
          "6Y eigenvalues %s; max ||tr|^2 - fixed points| %.1e; signature for W (x) conj W %.6f" % (
              a, dets, np.allclose(mI, P), EVEN.shape[1], ODD.shape[1], dimc,
              all(np.allclose(A @ P, P @ A) for A in (S, T)), sorted(np.round(np.linalg.eigvals(Y6).real, 6)),
              chi2, sig.real))

acts = {}
for a in (1, 2):
    G = Gs[a][0]
    acts[a] = {k: label_action(M) for k, (g, M) in G.items()}
same_pi = all(acts[1][k][v][0] == acts[2][k][v][0] for k in acts[1] for v in acts[1][k])
same_phi = all(np.isclose(acts[1][k][v][1], acts[2][k][v][1]) for k in acts[1] for v in acts[1][k])
for a in (1, 2):
    G = Gs[a][0]
    is_g = all(acts[a][k][v][0] == tuple((g @ np.array(v)) % 5) for k, (g, M) in G.items() for v in acts[a][k])
    print("C2 a=%d: the labels move as g itself acts on (p, q): %s" % (a, is_g))
print("C2: the same permutation of labels in both classes for every g: %s; the same phases: %s" % (same_pi, same_phi))
diff_ph = sum(1 for k in acts[1] for v in acts[1][k] if not np.isclose(acts[1][k][v][1], acts[2][k][v][1]))
print("C2: (element, label) pairs whose phase differs between the classes: %d of %d" % (diff_ph, 120 * 25))
# which labels' transformation differs
diff_pi = sum(1 for k in acts[1] for v in acts[1][k] if acts[1][k][v][0] != acts[2][k][v][0])
print("C2: (element, label) pairs whose image label differs between the classes: %d of %d" % (diff_pi, 120 * 25))

G1, G2 = Gs[1][0], Gs[2][0]
ndiff = sum(1 for k in G1 if not np.isclose(np.trace(G1[k][1]), np.trace(G2[k][1])))
h = np.array([[2, 0], [0, 1]]); hi = np.array([[3, 0], [0, 1]])
outer = all(np.isclose(np.trace(G2[k][1]), np.trace(G1[key(h @ G1[k][0] @ hi)][1])) for k in G1)
print("C3: elements whose traces differ between the classes: %d of 120; tr rho_2(g) = tr rho_1(h g h^-1) for "
      "h = diag(2, 1), for all g: %s" % (ndiff, outer))
for a in (1, 2):
    G = Gs[a][0]
    vals = sorted({round(np.trace(EVEN.T @ M @ EVEN).real, 6) for g, M in G.values()
                   if np.allclose(np.linalg.matrix_power(g, 5) % 5, np.eye(2)) and not np.allclose(g % 5, np.eye(2))})
    print("C3 a=%d: the even part's traces on the elements of order 5: %s ((1 +- sqrt 5)/2 = %.6f, %.6f)" % (
        a, vals, (1 + 5 ** 0.5) / 2, (1 - 5 ** 0.5) / 2))

gam = np.array([[2, 1], [1, 1]])
r = {}
for a in (1, 2):
    S, T = weil(a)
    g = T @ S @ np.linalg.inv(T) @ np.linalg.inv(S)
    assert np.allclose(g, Gs[a][0][key(gam)][1]), "gamma's word"
    r[a] = g
tr2 = [np.trace(r[a] @ r[a]) for a in (1, 2)]
dets = [np.linalg.det(Gs[a][0][key(-np.eye(2, dtype=int))][1]) for a in (1, 2)]
print("C4: tr rho(gamma^2) = %.6f, %.6f (differ: %s); det rho(-I) = %.6f, %.6f and rho(-I) the parity in both: %s" % (
    tr2[0].real, tr2[1].real, not np.isclose(tr2[0], tr2[1]), dets[0].real, dets[1].real,
    all(np.allclose(Gs[a][0][key(-np.eye(2, dtype=int))][1], P) for a in (1, 2))))
for a in (1, 2):
    trs = [np.trace(np.linalg.matrix_power(r[a], k)) for k in range(1, 11)]
    w, V = np.linalg.eig(r[a])
    fix = V[:, np.isclose(w, 1)]
    par = [np.allclose(P @ fix[:, j], fix[:, j]) for j in range(fix.shape[1])]
    print("C5 a=%d: tr rho(gamma^k), k = 1..10: %s; fixed space of rho(gamma): dimension %d, even %s" % (
        a, ["%.3f%+.3fi" % (x.real, x.imag) for x in trs], fix.shape[1], par))
