"""B1957: two statements of the physical lane about main's own B1953, checked on main (exact algebra on level 5's Weil
space; no frame, no data).
MAIN-01  with E3 = (1 + P)/2 and E2 = (1 - P)/2 the projectors on the 3 and the 2, every one of the 24 operators D(v) has
         trace 1/2 over the 3 and -1/2 over the 2; so for O = sum_w zeta^(-ab) Y(w) (x) D(w) and F = sum_w zeta^(-ab) Y(w),
         tr_3 O = F/2 and tr_2 O = -F/2 (B1953 had F and -F), while tr_W(O 6Y) = -(5/2) F stands.
JOIN     the part of O that commutes with the whole continuous gauge group on W = 3 + 2 (by Schur's lemma: A (x) 1_3 + B (x) 1_2)
         is (F/6) (x) 1_3 + (-F/4) (x) 1_2 = -(F/12) (x) 6Y; and an operator of that form has proportional Gramians over the
         3 and the 2, which a generic O has not."""
import numpy as np
z = np.exp(2j * np.pi / 5); psi = lambda x: z ** (x % 5)
X = np.roll(np.eye(5), 1, axis=0).astype(complex); Z = np.diag([psi(x) for x in range(5)])
D = lambda a, b: psi(3 * a * b) * np.linalg.matrix_power(X, a % 5) @ np.linalg.matrix_power(Z, b % 5)
P = np.array([[1.0 if (x + y) % 5 == 0 else 0.0 for y in range(5)] for x in range(5)]); E3, E2 = (np.eye(5) + P) / 2, (np.eye(5) - P) / 2; Y6 = (np.eye(5) - 5 * P) / 2
PTS = [(i, j) for i in range(5) for j in range(5) if (i, j) != (0, 0)]


def build(Y):
    return sum(np.kron(psi(-a * b) * Y[a, b], D(a, b)) for a, b in PTS), sum(psi(-a * b) * Y[a, b] for a, b in PTS)


def trW(M, E):
    return np.einsum("iajb,ba->ij", M.reshape(3, 5, 3, 5), E)


if __name__ == "__main__":
    t3 = {np.round(np.trace(D(*v) @ E3), 12) for v in PTS}; t2 = {np.round(np.trace(D(*v) @ E2), 12) for v in PTS}; ty = {np.round(np.trace(D(*v) @ Y6), 12) for v in PTS}
    print("MAIN-01: over the 24 operators, the trace over the 3 takes the values %s, over the 2 %s, against 6Y %s; the ranks of the two projectors are %d and %d" % (sorted(complex(x) for x in t3), sorted(complex(x) for x in t2), sorted(complex(x) for x in ty), round(np.trace(E3).real), round(np.trace(E2).real)))
    rng = np.random.default_rng(5); Y = rng.normal(size=(5, 5, 3, 3)) + 1j * rng.normal(size=(5, 5, 3, 3)); O, F = build(Y)
    print("         for a random family of 24 matrices: tr_3 O - F/2: %.1e; tr_2 O + F/2: %.1e; tr_W(O 6Y) + (5/2) F: %.1e" % (np.abs(trW(O, E3) - F / 2).max(), np.abs(trW(O, E2) + F / 2).max(), np.abs(trW(O, Y6) + 2.5 * F).max()))
    proj = np.kron(trW(O, E3) / 3, E3) + np.kron(trW(O, E2) / 2, E2)
    print("JOIN:    the part of O of the form A (x) 1_3 + B (x) 1_2 is -(F/12) (x) 6Y: %.1e; it is the orthogonal projection (the rest is orthogonal to every such operator: %.1e)" % (np.abs(proj + np.kron(F / 12, Y6)).max(), max(abs(np.vdot(np.kron(M, E), O - proj)) for M in (np.eye(3), rng.normal(size=(3, 3))) for E in (E3, E2))))
    R = O.reshape(3, 5, 3, 5); H = lambda E: np.einsum("iajb,bc,kcjd,da->ik", R, E, R.conj(), E)                       # the family Gramian with W traced over one block
    sp = lambda M: (lambda e: e / e[-1])(np.linalg.eigvalsh((M + M.conj().T) / 2)); Rp = proj.reshape(3, 5, 3, 5); Hp = lambda E: np.einsum("iajb,bc,kcjd,da->ik", Rp, E, Rp.conj(), E)
    print("         normalised spectra of the Gramians over the 3 and the 2: for the projected part they agree to %.1e; for O itself they differ by %.2f" % (np.abs(sp(Hp(E3)) - sp(Hp(E2))).max(), np.abs(sp(H(E3)) - sp(H(E2))).max()))
