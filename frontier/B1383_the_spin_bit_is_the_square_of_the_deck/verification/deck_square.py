#!/usr/bin/env python3
"""B1383 -- THE SPIN BIT IS THE SQUARE OF THE DECK.  B1382 identified m004's two spin structures with the Gieseking
manifold's two Pin types (B1141's lift rho_1 <-> Pin+, rho_2 <-> Pin-) and flagged a physics reading: Pin+ is the type
T^2 = (-1)^F fermions require.  OPEN_LEADS sL-3 asked whether physics therefore fixes the spin bit.  This computes the
sign law that decides it, for every way the deck can sit in a spacetime.

Setting (B1382, imported, exact over Q(w)): G_eps is the double cover of Isom(H^3) in which reflections lift with square
eps; the Gieseking generator t lifts to (lam W, c), W = [[1,-w],[0,1]], and (lam W, c)^2 = (eps A, 0).  On the spinors
of m004 with spin structure sigma (a -> sigma A) the lifted deck therefore squares to
        tau^2 = eps * sigma            -- the one number everything below is made of.

Sections (each asserts; record deck_square_run.txt):
  S1 Clifford algebras Cl(n, eps), n <= 7, as explicit 8x8 matrices with entries in {0, +-1, +-i} (exact in floating
     point): anticommutation, and (e_1...e_n)^2 = (-1)^(n(n-1)/2) eps^n
  S2 the control where Stiefel-Whitney classes decide: S^2 -> RP^2 with k extra reversed directions (the total space of
     kL over RP^2); the lift of (antipode, -1 on R^k) squares in Cl(3+k, eps) exactly as w1, w2 of T RP^2 + kL predict
  S3 the graded product G_eps (x) Cl(k, eps): associative on samples; at the fixed point j it is Cl(1+k, eps)
  S4 THE SIGN LAW: the deck paired with k reversed directions, g = (tau, -1 on R^k), squares on sigma's spinors to
        q(eps, sigma, k) = eps^(k+1) (-1)^(k(k+1)/2) sigma
     so the quotient carries the ambient structure (Spin for k odd, Pin^eps for k even) iff q = +1; and for odd k the
     reflection the k-dimensional factor sees has type eps_k = -sigma, whatever eps
  S5 the mapping torus M_tau of the deck (B1104's one-level-up Gieseking analog): every (eps, sigma) extends; the
     structures are (sigma, sign of the lifted tick), four per type = |H^1(M_tau; Z/2)| (H_1 = Z^2); the double tick
     z = s^2 a^-1 (the fibre of M_tau -> N) lifts to eps*sigma: periodic (Ramond) iff eps*sigma = +1
  S6 the generation-parity lemma: an antilinear map with square -1 on C^n needs n even (det X conj(X) = |det X|^2 >= 0);
     hypercharge cannot supply the -1 (conj(h) h = 1 on U(1)); so a CP of Pin- type is impossible on three generations
     of the lepton singlet: the Standard Model's CP, whenever it is a symmetry (gauged, spontaneously broken), is Pin+
  S7 the realization table, with eps = + (the type fixed by M-theory, by T^2 = (-1)^F theories, and by the SM's CP)
  S8 main's open Dirac doubling (B933/B940 obligation O1): J = sigma_2 K commutes with their operator
     D = -i[t(s1 dx + s2 dy + s3 dt) - s3], with their SU(2) automorphy twist conj(k), and J^2 = -1 -- the whole spectrum
     is Kramers-doubled on either spin structure, with no role for the deck (a different 'Kramers' from S4-S7)
Usage: python3 deck_square.py"""
import importlib.util
import itertools
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
_B1382 = HERE.parents[1] / "B1382_the_spin_bit_is_the_parents_pin_type" / "verification" / "pin_types.py"
_spec = importlib.util.spec_from_file_location("b1382_pin_types", _B1382)
P = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(P)

SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
SZ = np.array([[1, 0], [0, -1]], dtype=complex)
E2 = np.eye(2, dtype=complex)
QUBITS = 3                                   # 8 x 8 matrices host Cl(n, eps) for n <= 7
ONE = np.eye(2 ** QUBITS, dtype=complex)


def kron(*ms):
    out = np.eye(1, dtype=complex)
    for m in ms:
        out = np.kron(out, m)
    return out


def clifford(n, eps):
    """n anticommuting 8x8 matrices with square eps (Jordan-Wigner strings)."""
    gens = []
    for q in range(QUBITS):
        pre, post = [SZ] * q, [E2] * (QUBITS - q - 1)
        gens += [kron(*pre, SX, *post), kron(*pre, SY, *post)]
    gens.append(kron(*[SZ] * QUBITS))
    assert n <= len(gens)
    gens = [g if eps == 1 else 1j * g for g in gens[:n]]
    for i, x in enumerate(gens):
        for j, y in enumerate(gens):
            assert np.array_equal(x @ y + y @ x, 2 * eps * ONE if i == j else 0 * ONE)
    return gens


def prod(ms):
    out = ONE
    for m in ms:
        out = out @ m
    return out


def scalar(M):
    for c in (1, -1):
        if np.array_equal(M, c * ONE):
            return c
    raise AssertionError("not +-1")


def s1_clifford():
    table = {}
    for eps in (1, -1):
        for n in range(8):
            v = prod(clifford(n, eps))
            table[(eps, n)] = scalar(v @ v)
            assert table[(eps, n)] == (-1) ** (n * (n - 1) // 2) * eps ** n
    return table


def s2_rp2_control():
    """w(T RP^2) = (1+a)^3, w(kL) = (1+a)^k: w1 = (1+k) a, w2 = (1 + k(k+1)/2) a^2 (a^3 = 0)."""
    rows = {}
    for k in range(5):
        c2 = (1 + k * (k + 1) // 2) % 2
        c11 = (1 + k) % 2
        orientable = c11 == 0
        got = {}
        for eps in (1, -1):
            v = prod(clifford(3 + k, eps))                  # the lift of (-I_3) x (-I_k): all 3+k reflections
            got[eps] = scalar(v @ v) == 1                   # an involution <=> the structure descends
            if orientable:
                predicted = c2 == 0                                         # Spin(T RP^2 + kL): w2 = 0
            else:
                predicted = (c2 == 0) if eps == 1 else ((c2 + c11) % 2 == 0)   # Pin+: w2 = 0; Pin-: w2 + w1^2 = 0
            assert got[eps] == predicted
        if orientable:
            assert got[1] == got[-1]                        # a spin structure knows no Pin convention
        rows[k] = ("orientable" if orientable else "unorientable", got[1], got[-1])
    assert rows[0] == ("unorientable", False, True)          # RP^2 itself: Pin- only (w2 = w1^2 = a^2)
    return rows


class Graded:
    """G_eps (x) Cl(k, eps): elements (x, u, p) -- x = (M, kbit) in G_eps, u a Clifford matrix of parity p -- with
    (x1, u1, p1)(x2, u2, p2) = (x1 x2, (-1)^(p1 kbit2) u1 u2, p1 + p2): odd elements of the two factors anticommute,
    as in Cl(3+k) = Cl(3) (x)^ Cl(k); (-M, -u) and (M, u) are the same element (the shared central -1)."""

    def __init__(self, eps):
        self.g = P.G(eps)

    def mul(self, X, Y):
        (x1, u1, p1), (x2, u2, p2) = X, Y
        sign = -1 if (p1 and x2[1]) else 1
        return (self.g.mul(x1, x2), sign * (u1 @ u2), (p1 + p2) % 2)


def same(X, Y):
    (x1, u1, p1), (x2, u2, p2) = X, Y
    return P.meq(x1[0], x2[0]) and x1[1] == x2[1] and np.array_equal(u1, u2) and p1 == p2


def sign_against(M, target):
    for s in (1, -1):
        if P.meq(M, P.mscale(s, target)):
            return s
    raise AssertionError("not +-target")


def s3_graded(W):
    for eps in (1, -1):
        gr = Graded(eps)
        e = clifford(3, eps)
        us = [(ONE, 0), (e[0], 1), (e[0] @ e[1], 0), (e[0] @ e[1] @ e[2], 1)]
        xs = [(P.A, 0), (P.B, 1), (W, 1), (P.mat([[2, 1], [1, 1]]), 0)]
        samples = [(x, u, p) for x in xs for (u, p) in us]
        for X, Y, Z in itertools.product(samples[::3], samples[1::3], samples[2::3]):
            assert same(gr.mul(gr.mul(X, Y), Z), gr.mul(X, gr.mul(Y, Z)))
        for k in range(5):                                   # at the fixed point j: c (x) U is e_0 f_1...f_k in Cl(1+k)
            U = prod(clifford(k, eps))
            (Msq, kb), usq, psq = gr.mul(((P.I2, 1), U, k % 2), ((P.I2, 1), U, k % 2))
            assert kb == 0 and psq == 0
            v = prod(clifford(1 + k, eps))
            assert sign_against(Msq, P.I2) * scalar(usq) == scalar(v @ v)
    return True


def s4_sign_law(W):
    """g = (deck, -1 on R^k).  g^2 = ((s1 A, 0), s2) ~ s1 s2 ((A, 0), 1); on sigma's spinors (sigma A, 0) acts trivially,
    so g^2 acts as q = s1 s2 sigma."""
    law, eps_k = {}, {}
    for eps in (1, -1):
        gr = Graded(eps)
        for k in range(5):
            U = prod(clifford(k, eps))
            gt = ((W, 1), U, k % 2)
            (Msq, kb), usq, psq = gr.mul(gt, gt)
            assert kb == 0 and psq == 0
            s = sign_against(Msq, P.A) * scalar(usq)
            for sigma in (1, -1):
                q = s * sigma
                assert q == eps ** (k + 1) * (-1) ** (k * (k + 1) // 2) * sigma
                law[(eps, sigma, k)] = q
                if k % 2:                                    # a k-fold reflection squares to (-1)^(k(k-1)/2) eps_k
                    eps_k[(eps, sigma, k)] = q * (-1) ** (k * (k - 1) // 2)
                    assert eps_k[(eps, sigma, k)] == -sigma
    for sigma in (1, -1):                                    # odd k: the total is orientable, no Pin convention enters
        for k in (1, 3):
            assert law[(1, sigma, k)] == law[(-1, sigma, k)]
    assert all(law[(eps, sigma, 0)] == eps * sigma for eps in (1, -1) for sigma in (1, -1))   # B1382 is k = 0
    return law, eps_k


def s5_mapping_torus(W):
    """pi_1(M_tau) = <a, b, s | R(a, b), s a s^-1 = a, s b s^-1 = beat(b)> (no s^2 = a: that relation is the Gieseking
    quotient); s lifts to ((lam W, c), translation by 1)."""
    from sympy import Matrix, ZZ
    from sympy.matrices.normalforms import smith_normal_form

    def exps(word):
        return [word.count("a") - word.count("A"), word.count("b") - word.count("B")]

    rel = [exps(P.RELATOR) + [0], [0, 0, 0], [x - y for x, y in zip([0, 1], exps(P.BEAT["b"]))] + [0]]
    snf = smith_normal_form(Matrix(rel), domain=ZZ)
    diag = [abs(snf[i, i]) for i in range(3)]
    free_rank = sum(1 for d in diag if d == 0)
    assert free_rank == 2 and all(d in (0, 1) for d in diag)          # H_1(M_tau) = Z^2 (B1104: Z^2)
    out = {}
    for eps in (1, -1):
        g = P.G(eps)

        def mul(X, Y):
            return (g.mul(X[0], Y[0]), X[1] + Y[1])

        def inv(X):
            return (g.inv(X[0]), -X[1])

        for sigma in (1, -1):
            a = ((P.mscale(sigma, P.A), 0), 0)
            b = ((P.mscale(sigma, P.B), 0), 0)
            ok_rel = P.meq(P.ev(P.RELATOR, a[0][0], b[0][0]), P.I2)
            beat_b = P.ev(P.BEAT["b"], a[0][0], b[0][0])
            for lam in (1, -1):
                s = ((P.mscale(lam, W), 1), 1)
                sas, sbs = mul(mul(s, a), inv(s)), mul(mul(s, b), inv(s))
                ok_a = P.meq(sas[0][0], a[0][0]) and sas[0][1] == 0 and sas[1] == 0
                ok_b = P.meq(sbs[0][0], beat_b) and sbs[0][1] == 0 and sbs[1] == 0
                z = mul(mul(s, s), inv(a))
                assert z[0][1] == 0 and z[1] == 2                          # the pure translation by 2: the double tick
                zt = sign_against(z[0][0], P.I2)
                assert zt == eps * sigma
                out[(eps, sigma, lam)] = (ok_rel and ok_a and ok_b, zt)
    assert all(v[0] for v in out.values()) and len(out) == 8            # 4 Pin+ and 4 Pin- structures: all extend
    return diag, out


def s6_generation_parity(trials=200, seed=7):
    rng = np.random.default_rng(seed)
    for n in range(1, 6):
        if n % 2 == 0:                                   # even n: X = diag of [[0,1],[-1,0]] blocks has X conj(X) = -1
            X = np.kron(np.eye(n // 2), np.array([[0, 1], [-1, 0]], dtype=complex))
            assert np.array_equal(X @ X.conj(), -np.eye(n))
        for _ in range(trials):                          # det(X conj X) = |det X|^2 >= 0, while det(-I_n) = (-1)^n
            X = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
            d = np.linalg.det(X @ X.conj())
            assert abs(d.imag) < 1e-9 * max(1.0, abs(d)) and d.real > 0
    thetas = rng.uniform(0, 2 * np.pi, size=trials)      # a hypercharge phase on the singlet: conj(h) h = 1, never -1
    assert np.allclose(np.conj(np.exp(1j * thetas)) * np.exp(1j * thetas), 1.0)
    return {"odd n admits X conj(X) = -1": False, "even n admits it": True, "U(1) supplies -1": False}


def s7_realizations(law, eps_k, torus):
    eps = 1                                              # physics' type (M-theory; T^2 = (-1)^F; the SM's CP -- S6)
    a = [sigma for sigma in (1, -1) if law[(eps, sigma, 0)] == 1]
    b = {zt: [sigma for sigma in (1, -1) if torus[(eps, sigma, 1)][1] == zt] for zt in (1, -1)}
    c = {k: [sigma for sigma in (1, -1) if eps_k[(eps, sigma, k)] == 1] for k in (1, 3)}
    c2 = {k: [sigma for sigma in (1, -1) if law[(eps, sigma, k)] == 1] for k in (2, 4)}
    assert a == [1] and b == {1: [1], -1: [-1]} and c == {1: [-1], 3: [-1]} and c2 == {2: [-1], 4: [1]}
    return {"(a) parent as space / deck gauged (k = 0)": a,
            "(b) B1104's mapping torus, double tick periodic (Ramond)": b[1],
            "(b) B1104's mapping torus, double tick antiperiodic (NS, thermal)": b[-1],
            "(c) deck inside the 4d CP/T/R, reflection type Pin+ (k = 1)": c[1],
            "(c) deck inside the 4d parity, reflection type Pin+ (k = 3)": c[3],
            "(c') deck with a 4d pi-rotation (k = 2), total Pin+": c2[2],
            "(c') deck with the 4d inversion (k = 4), total Pin+": c2[4]}


def s8_dirac_doubling(trials=100, seed=11):
    """B933/B940's operator D = -i[t(s1 dx + s2 dy + s3 dt) - s3] (t > 0 real, derivatives real operators) and twist
    psi(x*) = conj(k) psi(x), k in SU(2).  J = s2 K: J D J^-1 has coefficients s2 conj(C) s2."""
    J = lambda C: SY @ C.conj() @ SY                     # SY^-1 = SY
    coeffs = {"dx": -1j * SX, "dy": -1j * SY, "dt": -1j * SZ, "1": 1j * SZ}     # D at t = 1 (t is a real scalar)
    assert all(np.array_equal(J(C), C) for C in coeffs.values())                 # [J, D] = 0
    assert np.array_equal(SY @ SY.conj(), -E2)                                  # J^2 = -1
    rng = np.random.default_rng(seed)
    for _ in range(trials):                                                     # [J, conj(k)] = 0 for k in SU(2)
        v = rng.normal(size=4)
        v /= np.linalg.norm(v)
        k = np.array([[v[0] + 1j * v[1], v[2] + 1j * v[3]], [-v[2] + 1j * v[3], v[0] - 1j * v[1]]])
        assert np.allclose(J(k.conj()), k.conj(), atol=1e-14)
    return True


if __name__ == "__main__":
    W, d, mu = P.s2_intertwiner()
    assert d == P.ONE and mu == P.ONE
    t1 = s1_clifford()
    print("S1  Cl(n, eps), n <= 7, explicit: (e_1...e_n)^2 = (-1)^(n(n-1)/2) eps^n for all 16 cases, e.g.",
          {n: (t1[(1, n)], t1[(-1, n)]) for n in range(8)})
    for k, row in s2_rp2_control().items():
        print("S2  RP^2 control, k = %d: total space of %dL is %s; lift of (antipode, -1) an involution in Cl(3+k,+) %s,"
              " in Cl(3+k,-) %s -- as w1, w2 predict" % (k, k, row[0], row[1], row[2]))
    print("S3  G_eps (x) Cl(k, eps) associative on 64 triples per eps; at the fixed point j it is Cl(1+k, eps), k = 0..4:",
          s3_graded(W))
    law, eps_k = s4_sign_law(W)
    for k in range(5):
        print("S4  k = %d: q(eps, sigma) = %s  %s" % (
            k, {(e, s): law[(e, s, k)] for e in (1, -1) for s in (1, -1)},
            "| type seen by the k-dim factor eps_k = %s (= -sigma)" % {s: eps_k[(1, s, k)] for s in (1, -1)}
            if k % 2 else "| total unorientable: descends in Pin^eps iff q = +1"))
    diag, torus = s5_mapping_torus(W)
    print("S5  mapping torus M_tau: H_1 invariant factors %s -> Z^2; all 8 (eps, sigma, lam) lifts extend; double tick z~ ="
          % diag, {(e, s): torus[(e, s, 1)][1] for e in (1, -1) for s in (1, -1)}, "(= eps*sigma)")
    print("S6  generation parity:", s6_generation_parity())
    for name, sig in s7_realizations(law, eps_k, torus).items():
        print("S7  %-68s -> %s" % (name, ["rho_1 (B1141's)" if s == 1 else "rho_2 (the other)" for s in sig]))
    print("S8  B940's Dirac operator: J = s2 K commutes with D and with the SU(2) twist, J^2 = -1:", s8_dirac_doubling(),
          "-> every eigenvalue doubled on either spin structure (main's O1), no deck involved")
    print("DONE")
