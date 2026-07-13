"""B569 — the 'Complete Chain' handoff (sixteenth sigma->SM chain), adjudicated.

Link 4 (compactness via E6 level-1 CS): the handoff's modular data pairs the
  SU(3)_1 conformal weight h = 1/3 with E6's central charge c = 6. Inconsistent:
  (ST)^3 != S^2, so 'rho(A1)' is WORD-DEPENDENT — two SL(2,Z) words for the same
  A1 give Z = -1 and Z = +1. The true E6_1 weight is h(27) = 2/3 (proved from
  the E6 root system below). The consistent E6_1 rep gives: rho(A1) unitary,
  order 4, [theta, rho] = 0, theta-even eigenvalues {+i, -i}, theta-odd
  eigenvalue +1, Z = +1. The claimed chirality bit Z = -1 does not exist.
Link 7 (G_SM the unique chiral theory on F4): REFUTED — the 26 of F4 is
  self-dual (its nonzero weights are the 24 short roots, closed under negation),
  so 27|_F4 = 1 + 26 restricted to ANY subgroup of F4 (including
  G_SM = H1 cap H2) is self-conjugate = vector-like. Zero chiral theories on
  the F4 stage; re-derives the chirality wall (B565-T3, index == 0) from pure
  Lie theory. (The '27 -> 16+10+1' is the Spin(10)xU(1) < E6 branching;
  Spin(10) is not a subgroup of F4.)
See frontier/B569_complete_chain/FINDINGS.md.
"""
import numpy as np
import sympy as sp

from fractions import Fraction

W3 = np.exp(2j * np.pi / 3)


def _modular(s_sign, h27, c):
    S = np.array([[W3 ** (s_sign * a * b) for b in range(3)] for a in range(3)]) / np.sqrt(3)
    T = np.diag([np.exp(2j * np.pi * (h - c / 24)) for h in (0, h27, h27)])
    return S, T


def _two_words(S, T):
    return (T @ T @ S @ T,
            T @ S @ np.linalg.inv(T) @ np.linalg.inv(S))


def _roots(C, n):
    allr = {tuple(1 if i == j else 0 for i in range(n)) for j in range(n)}
    frontier = set(allr)
    while frontier:
        new = set()
        for rt in frontier:
            for j in range(n):
                pj = sum(C[i][j] * rt[i] for i in range(n))
                y = list(rt)
                y[j] -= pj
                ty = tuple(y)
                if ty not in allr:
                    allr.add(ty)
                    new.add(ty)
        frontier = new
    return allr


# ---------- the SL(2,Z) words: two spellings of the monodromy ----------
def test_a1_two_words_in_sl2z():
    T = sp.Matrix([[1, 1], [0, 1]])
    S = sp.Matrix([[0, -1], [1, 0]])
    A1 = sp.Matrix([[2, 1], [1, 1]])                      # the fig-8 monodromy, = F^2
    assert T**2 * S * T == A1                             # the handoff's word
    assert T * (S * T**-1 * S**-1) == A1                  # a second word, same element
    assert (S * T)**3 == S**2 == -sp.eye(2)               # the relation any rep must honor
    # order 4 mod 3 — the mechanism behind rho(A1)^4 = I in the Z/3 theory
    A1m3 = A1.applyfunc(lambda x: x % 3)
    assert (A1**2).applyfunc(lambda x: x % 3) == 2 * sp.eye(2)
    assert (A1**4).applyfunc(lambda x: x % 3) == sp.eye(2)


# ---------- h(27) = 2/3 at E6 level 1, from the root system (exact) ----------
def test_h27_is_two_thirds():
    C6 = sp.Matrix([
        [2, 0, -1, 0, 0, 0], [0, 2, 0, -1, 0, 0], [-1, 0, 2, -1, 0, 0],
        [0, -1, -1, 2, -1, 0], [0, 0, 0, -1, 2, -1], [0, 0, 0, 0, -1, 2]])
    roots = _roots(C6.tolist(), 6)
    assert len(roots) == 72
    pos = [sp.Matrix(r) for r in roots if all(c >= 0 for c in r)]
    assert len(pos) == 36
    ip = lambda x, y: (x.T * C6 * y)[0, 0]
    rho = sp.Rational(1, 2) * sum(pos, sp.zeros(6, 1))
    G = C6.inv()
    minuscule = []
    for node in range(6):
        lam = G[:, node]
        dim = sp.prod([sp.Rational(ip(lam + rho, a), ip(rho, a)) for a in pos])
        if dim == 27:
            h = sp.Rational(ip(lam, lam) + 2 * ip(lam, rho), 2 * (1 + 12))
            minuscule.append((node + 1, h))
    assert [h for _, h in minuscule] == [sp.Rational(2, 3)] * 2   # nodes 1 and 6: the 27, 27bar
    assert all(h != sp.Rational(1, 3) for _, h in minuscule)      # the handoff's h is SU(3)_1's


# ---------- Gauss–Milgram: h = 1/3 pairs with c = 2 mod 8, h = 2/3 with c = 6 ----------
def test_gauss_milgram_pairing():
    for h, c in [(sp.Rational(1, 3), 2), (sp.Rational(2, 3), 6)]:
        gs = ((1 + 2 * sp.exp(2 * sp.pi * sp.I * h)) / sp.sqrt(3)
              - sp.exp(2 * sp.pi * sp.I * sp.Rational(c, 8)))
        assert abs(complex(sp.N(gs, 30))) < 1e-25


# ---------- the handoff's hybrid data: not a rep; Z is word-dependent ----------
def test_seat_data_word_dependent():
    S, T = _modular(1, 1 / 3, 6)                          # SU(3)_1 weights + E6 charge
    assert np.linalg.norm(np.linalg.matrix_power(S @ T, 3) - S @ S) > 1     # (ST)^3 != S^2
    w1, w2 = _two_words(S, T)
    assert abs(np.trace(w1) - (-1)) < 1e-12               # the handoff's Z = -1 ...
    assert abs(np.trace(w2) - (+1)) < 1e-12               # ... flips sign on the other word
    assert np.linalg.norm(w1 - w2) > 1                    # same group element, different matrix


# ---------- the consistent theories: genuine reps, word-independent, Z = +1 ----------
def test_consistent_e6_level1():
    for s_sign, h, c in [(-1, 2 / 3, 6), (1, 1 / 3, 2)]:  # E6_1 and its conjugate SU(3)_1
        S, T = _modular(s_sign, h, c)
        assert np.linalg.norm(np.linalg.matrix_power(S @ T, 3) - S @ S) < 1e-12
        assert np.linalg.norm(np.linalg.matrix_power(S, 4) - np.eye(3)) < 1e-12
        w1, w2 = _two_words(S, T)
        assert np.linalg.norm(w1 - w2) < 1e-12            # word-independent
        assert abs(np.trace(w1) - 1) < 1e-12              # Z = +1 in BOTH theories
    # the E6_1 rep in detail
    S, T = _modular(-1, 2 / 3, 6)
    rho, _ = _two_words(S, T)
    assert np.linalg.norm(rho @ rho.conj().T - np.eye(3)) < 1e-12            # unitary
    assert np.linalg.norm(np.linalg.matrix_power(rho, 4) - np.eye(3)) < 1e-12  # order 4
    C = np.array([[1, 0, 0], [0, 0, 1], [0, 1, 0]])       # theta = 27 <-> 27bar
    assert np.linalg.norm(C @ rho - rho @ C) < 1e-12      # theta COMMUTES ...
    assert np.linalg.norm(C @ rho @ C - np.linalg.inv(rho)) > 1              # ... does not invert
    ev = sorted(np.linalg.eigvals(rho), key=lambda z: (round(z.real, 6), round(z.imag, 6)))
    assert np.allclose(ev, [-1j, 1j, 1])                  # {+i, -i, +1} — no -1 anywhere
    vodd = np.array([0, 1, -1]) / np.sqrt(2)
    assert np.allclose(rho @ vodd, vodd)                  # theta-odd eigenvalue is +1, not -1


# ---------- Link 7 kill: the 26 of F4 is self-dual ----------
def test_f4_26_self_dual():
    # Bourbaki F4: alpha1, alpha2 long (norm 2); alpha3, alpha4 short (norm 1)
    C4 = [[2, -1, 0, 0], [-1, 2, -2, 0], [0, -1, 2, -1], [0, 0, -1, 2]]
    d = [Fraction(1), Fraction(1), Fraction(1, 2), Fraction(1, 2)]   # (a_i, a_i)/2
    B = [[Fraction(C4[i][j]) * d[j] for j in range(4)] for i in range(4)]
    assert all(B[i][j] == B[j][i] for i in range(4) for j in range(4))
    roots = _roots(C4, 4)
    assert len(roots) == 48
    ip = lambda x, y: sum(B[i][j] * x[i] * y[j] for i in range(4) for j in range(4))
    short = {r for r in roots if ip(r, r) == 1}
    assert len(short) == 24
    assert all(tuple(-c for c in r) in short for r in short)          # negation-closed
    # the highest short root is the unique dominant short root; Weyl dim formula gives 26
    pos = [r for r in roots if all(c >= 0 for c in r)]
    cop = lambda x, j: Fraction(2) * sum(B[i][j] * x[i] for i in range(4)) / B[j][j]
    dom = [r for r in short if all(cop(r, j) >= 0 for j in range(4))]
    assert len(dom) == 1
    lam = dom[0]
    rho = [sum(Fraction(r[i]) for r in pos) / 2 for i in range(4)]
    coip = lambda x, a: Fraction(2) * ip(x, a) / ip(a, a)             # <x, a^vee>
    lam_rho = [Fraction(lam[i]) + rho[i] for i in range(4)]
    dim = Fraction(1)
    for a in pos:
        dim *= coip(lam_rho, a) / coip(rho, a)
    assert dim == 26
    # the 24 nonzero weights ARE the short roots (negation-closed); the remaining
    # 2 dims are zero weights (a nonzero F4 weight has W-orbit >= |W|/|W(B3)| = 24 > 2)
    assert 1152 // 48 == 24 > 2
    # => the character of the 26 is real => 26 = 26*; 27|_F4 = 1 + 26 self-conjugate;
    #    its restriction to ANY subgroup of F4 (incl. G_SM) is self-conjugate: no chirality.
