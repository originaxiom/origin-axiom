#!/usr/bin/env python3
"""Card W-P1, corrected after its referee read: the golden iteration on level 5's Weil space, in both classes. Data-free.

    python3 -I wp1_weil.py

The Weil representation of SL(2, F_5) on functions on F_5, in the class of the form a x^2 / 5 (a = 1, the knot's
residue class; a = 2, the act's non-residue class, B1955 § 2): rho(T) = diag zeta^(a x^2), rho(S) = c F with
F[x, y] = zeta^(-2 a x y), zeta = exp(2 pi i / 5), and the scalar c fixed so that rho(S)^2 = (rho(S) rho(T))^3, the
relation S^2 = (ST)^3 = -I of SL(2, Z). gamma = [[2, 1], [1, 1]] = T S T^-1 S^-1. Printed for each class:
  W1  the relations: rho(S)^4 = I, rho(S)^2 is the parity x -> -x, and the even and odd parts have dimensions 3 and 2;
  W2  gamma mod 5, gamma^5 mod 5, and whether rho(gamma)^5 equals the parity;
  W3  tr rho(gamma) and tr rho(gamma^2), and rho(gamma)'s eigenphases in tenths of a turn, on the even and odd parts;
  W4  the signature tr R(T^2) / tr R(T)^2 for R = W_a (x) conj(W_b), for the four pairs (a, b).
First run (2026-11-18) stopped at the relation check, before any result: the Fourier kernel had the sign +2axy, for
which no scalar c satisfies the relation; it is -2axy here, and nothing else is changed.
"""
import numpy as np

z = np.exp(2j * np.pi / 5)
X = np.arange(5)
Pm = np.zeros((5, 5)); Pm[(-X) % 5, X] = 1          # the parity f(x) -> f(-x)


def weil(a):
    T = np.diag(z ** ((a * X * X) % 5))
    F = z ** ((-2 * a * np.outer(X, X)) % 5)
    A, B = F @ F, np.linalg.matrix_power(F @ T, 3)   # rho(S) = c F: c^2 A = c^3 B, so c = A/B (a scalar)
    k = np.argmax(np.abs(B))
    c = A.flat[k] / B.flat[k]
    S = c * F
    assert np.allclose(S @ S, np.linalg.matrix_power(S @ T, 3)), "the relation"
    return T, S


even = np.array([[1, 0, 0, 0, 0], [0, 1, 0, 0, 1], [0, 0, 1, 1, 0]], float).T / np.array([1, np.sqrt(2), np.sqrt(2)])
odd = np.array([[0, 1, 0, 0, -1], [0, 0, 1, -1, 0]], float).T / np.sqrt(2)
G = np.array([[2, 1], [1, 1]])
print("W2: gamma mod 5 = %s; gamma^5 mod 5 = %s" % (G.tolist(), (np.linalg.matrix_power(G, 5) % 5).tolist()))
rhos = {}
for a in (1, 2):
    T, S = weil(a)
    rhos[a] = (T, S)
    Si, Ti = np.linalg.inv(S), np.linalg.inv(T)
    g = T @ S @ Ti @ Si
    print("W1 a=%d: S^4 = I %s; S^2 = parity %s; dims even/odd %d/%d" % (
        a, np.allclose(np.linalg.matrix_power(S, 4), np.eye(5)), np.allclose(S @ S, Pm), even.shape[1], odd.shape[1]))
    print("W2 a=%d: rho(gamma)^5 = parity %s" % (a, np.allclose(np.linalg.matrix_power(g, 5), Pm)))
    tr1, tr2 = np.trace(g), np.trace(g @ g)
    ev_e = np.linalg.eigvals(even.T @ g @ even); ev_o = np.linalg.eigvals(odd.T @ g @ odd)
    tenths = lambda v: sorted(int(round((np.angle(x) / (2 * np.pi) % 1) * 10)) % 10 or 10 for x in v)
    print("W3 a=%d: tr rho(gamma) = %.6f%+.6fi; tr rho(gamma^2) = %.6f%+.6fi (sqrt 5 = %.6f); eigenphases in tenths: "
          "even %s, odd %s" % (a, tr1.real, tr1.imag, tr2.real, tr2.imag, np.sqrt(5), tenths(ev_e), tenths(ev_o)))
for a in (1, 2):
    for b in (1, 2):
        Ta, Tb = rhos[a][0], rhos[b][0]
        t1 = np.trace(Ta) * np.conj(np.trace(Tb)); t2 = np.trace(Ta @ Ta) * np.conj(np.trace(Tb @ Tb))
        print("W4 (a, b) = (%d, %d): tr R(T^2) / tr R(T)^2 = %.6f%+.6fi" % (a, b, (t2 / t1 ** 2).real, (t2 / t1 ** 2).imag))
