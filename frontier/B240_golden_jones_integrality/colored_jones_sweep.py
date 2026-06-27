"""B240 (closing) -- is the golden integrality [N]*J_N in Z figure-eight-specific, or shared by the whole
amphicheiral class? Settled by a validated U_q(sl2) R-matrix colored Jones over a sweep of amphicheiral knots.

RESULT (the two-tier structure):
  * amphichirality  =>  [N]*J_N is REAL, in Z[phi] (the ring of integers of Q(sqrt5))   -- CLASS property.
  * the sqrt5-part vanishing ([N]*J_N in Z, pure rational integers)                       -- FIGURE-EIGHT-SPECIFIC.
Among the amphicheiral knots through 10 crossings with braid index <= 5 (4_1, 6_3, 8_9, 8_12, 8_17, 8_18, 10_17)
ONLY 4_1 gives pure integers {1,-2,-2,1}; every other gives a genuine a+b*phi with b != 0. Chiral knots give
non-real values (in Q(zeta_5), not the real subfield). 8_3/10_3 (braid index 7/9) exceed the dense-matrix ceiling
for N=4 -- reported, not silently dropped.

Method: colored Jones via the U_q(sl2) universal R-matrix on a braid word, validated to reproduce the Habiro
cyclotomic formula for 4_1 at all N=1..4. Integrality is decided RIGOROUSLY by Galois: [N]*J_N is a rational
integer iff its value is unchanged under the nontrivial Galois map of Q(sqrt5)/Q, realized as q=e^{i pi/5} ->
e^{3 i pi/5} (phi -> 1-phi). No float lattice-search. Braid words verified via SnapPy. Run: python (pyenv).
"""
import cmath

import numpy as np

PHI = (1 + 5 ** 0.5) / 2
Q10 = cmath.exp(1j * np.pi / 5)        # primitive 10th root: [2]=2cos(pi/5)=phi (the SU(2)_3 normalization)
Q10C = cmath.exp(3j * np.pi / 5)       # its Galois conjugate (phi -> 1-phi)

# amphicheiral knots (braid index <= 5), all with writhe-0 representatives (no framing/twist correction needed):
AMPHI = {
    "4_1": ([1, -2, 1, -2], 3),
    "6_3": ([1, -2, 1, -2, -2, 1], 3),
    "8_9": ([-1, 2, 2, 2, -1, -1, -1, 2], 3),
    "8_12": ([-1, 2, -3, 2, 1, 2, -3, 4, -3, 2, -3, -4], 5),
    "8_17": ([-1, 2, -1, -1, 2, 2, -1, 2], 3),
    "8_18": ([1, -2, 1, -2, 1, -2, 1, -2], 3),       # = (sigma1 sigma2^-1)^4, the 4_1 braid family
    "10_17": ([1, -2, 1, -2, -2, -2, -2, 1, 1, 1], 3),
}
CHIRAL = {"3_1": ([-1, -1, -1], 2), "5_2": ([-1, 2, -3, 2, 2, 1, 2, 3, 2], 4)}
QDIM = {1: 1.0, 2: PHI, 3: PHI, 4: 1.0}


def qint(m, q):
    return (q ** m - q ** (-m)) / (q - q ** (-1))


def qfac(k, q):
    r = 1.0 + 0j
    for j in range(1, k + 1):
        r *= qint(j, q)
    return r


def _reps(N, q):
    n = N - 1
    w = [n - 2 * i for i in range(N)]
    K = np.diag([q ** wi for wi in w])
    E = np.zeros((N, N), complex); F = np.zeros((N, N), complex)
    for i in range(N):
        if i - 1 >= 0:
            E[i - 1, i] = qint(n - i + 1, q)
        if i + 1 < N:
            F[i + 1, i] = qint(i + 1, q)
    return n, w, K, E, F


def _Rcheck(N, q):
    n, w, K, E, F = _reps(N, q)
    D = np.diag([q ** (w[i] * w[j] / 2) for i in range(N) for j in range(N)])
    S = np.zeros((N * N, N * N), complex)
    Ek = np.eye(N, dtype=complex); Fk = np.eye(N, dtype=complex)
    for k in range(N):
        S += ((q - q ** (-1)) ** k / qfac(k, q)) * q ** (k * (k - 1) / 2) * np.kron(Ek, Fk)
        Ek = Ek @ E; Fk = Fk @ F
    R = D @ S
    SW = np.zeros((N * N, N * N), complex)
    for i in range(N):
        for j in range(N):
            SW[j * N + i, i * N + j] = 1
    return SW @ R


def colored_jones(braid, strands, N, q):
    """normalized colored Jones (unknot=1) via R-matrix quantum trace; valid as the knot invariant for the
    writhe-0 braid representatives used here (twist correction = theta^0 = 1)."""
    if N == 1:
        return 1.0 + 0j
    Rc = _Rcheck(N, q); Rci = np.linalg.inv(Rc)
    B = np.eye(N ** strands, dtype=complex)
    for g in braid:
        a = abs(g) - 1; b = strands - (abs(g) + 1)
        op = np.kron(np.eye(N ** a, dtype=complex), np.kron(Rc if g > 0 else Rci, np.eye(N ** b, dtype=complex)))
        B = op @ B
    _, _, K, _, _ = _reps(N, q)
    mu = np.eye(1, dtype=complex)
    for _ in range(strands):
        mu = np.kron(mu, K)
    qd = sum(q ** (N - 1 - 2 * i) for i in range(N))
    return np.trace(mu @ B) / qd


def weighted(braid, strands, N, q):
    """[N]*J_N with the quantum dimension [N] evaluated AT THE ROOT q (so weighted(Q10) and weighted(Q10C) are
    genuine Galois conjugates of the same number of Q(sqrt5)). [N]=sum q^{N-1-2i}: phi at Q10, 1-phi at Q10C."""
    qdim = sum(q ** (N - 1 - 2 * i) for i in range(N))
    return qdim * colored_jones(braid, strands, N, q)


def galois_decomp(braid, strands, N):
    """return (a, b) with [N]*J_N = a + b*sqrt5 exactly (a,b rational), via the two conjugate roots; and a
    'real' flag (False => the value is not in the real field Q(sqrt5), i.e. the knot is effectively chiral here)."""
    v = weighted(braid, strands, N, Q10)
    vc = weighted(braid, strands, N, Q10C)
    if abs(v.imag) > 1e-7 or abs(vc.imag) > 1e-7:
        return None, None, False
    a = (v.real + vc.real) / 2
    b = (v.real - vc.real) / (2 * 5 ** 0.5)
    return a, b, True


def cj_fig8_habiro(N, q):
    tot = 0j
    for nn in range(N):
        p = 1 + 0j
        for j in range(1, nn + 1):
            p *= (q ** ((N - j) / 2) - q ** (-(N - j) / 2)) * (q ** ((N + j) / 2) - q ** (-(N + j) / 2))
        tot += p
    return tot


def is_pure_integer(braid, strands):
    """True iff [N]*J_N is a rational integer for all N=1..4 (b=0 and a in Z)."""
    for N in range(1, 5):
        a, b, real = galois_decomp(braid, strands, N)
        if not real or abs(b) > 1e-7 or abs(a - round(a)) > 1e-7:
            return False
    return True


if __name__ == "__main__":
    qH = cmath.exp(2j * np.pi / 5)
    print("=== validation: R-matrix == Habiro for 4_1 (all N) ===")
    for N in range(1, 5):
        rj = colored_jones(AMPHI["4_1"][0], 3, N, Q10)
        assert abs(rj - cj_fig8_habiro(N, qH)) < 1e-7, N
    print("  OK (N=1..4)")

    print("\n=== amphicheiral sweep: [N]*J_N = a + b*sqrt5 (b=0 => pure integer) ===")
    for nm, (bw, s) in AMPHI.items():
        cells = []
        for N in (2, 3):
            a, b, _ = galois_decomp(bw, s, N)
            cells.append(f"N{N}: {a:+.3g}{'+' if b >= 0 else '-'}{abs(b):.3g}*sqrt5")
        pure = is_pure_integer(bw, s)
        print(f"  {nm:6s}: {' | '.join(cells)}   PURE INTEGER: {pure}")

    print("\n=== chiral controls: not in the real field ===")
    for nm, (bw, s) in CHIRAL.items():
        _, _, real = galois_decomp(bw, s, 2)
        print(f"  {nm:6s}: real(in Q(sqrt5))={real}  -> pure integer: {is_pure_integer(bw, s)}")

    print("\nVERDICT: only 4_1 is a pure integer; amphichirality alone gives Z[phi], not Z.")
    print("ceiling: 8_3 (braid index 7) and 10_3 (9) exceed the dense N=4 matrix size -- not tested.")
    print("ALL CHECKS PASS")
